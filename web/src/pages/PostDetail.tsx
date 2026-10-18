import { useState } from 'react'
import { AppShell } from '../components/AppShell'
import { Mascot } from '../components/Brand'
import { Icon } from '../components/Icon'
import { PostCard, PostHeader, Scene } from '../components/PostCard'
import { EmptyState, PostSkeleton, ScoreRing, UserAvatar, AgentAvatar, agentOf } from '../components/ui'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'
import { Link, useRoute } from '../lib/router'
import { useSession } from '../lib/session'
import { PointsModal, type PointsModalData } from '../components/PointsModal'
import type { Evaluation, Post } from '../lib/types'

const MAX = 600

function EvaluationCard({ ev, post }: { ev: Evaluation; post: Post }) {
  const a = agentOf(post.agentId)
  const mood = ev.dangerous ? 'wow' : ev.score >= 70 ? 'happy' : 'look'
  return (
    <div className="card p-5 mt-4 animate-rise border-2" style={{ borderColor: ev.dangerous ? '#EF444466' : `${a.colors[0]}55` }}>
      <div className="flex items-center gap-4">
        <ScoreRing score={ev.score} />
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 text-sm text-muted"><AgentAvatar agent={a} size={22} />{a.name} reviewed your answer</div>
          <div className="font-display text-xl md:text-2xl font-bold mt-1 leading-tight">{ev.label}</div>
        </div>
        <Mascot mood={mood} size={64} className="hidden sm:block" />
      </div>
      <div className="mt-4 divide-y divide-line">
        {ev.checklist.map(c => (
          <div key={c.id} className="flex gap-3 py-3">
            <span className={`w-6 h-6 rounded-full grid place-items-center shrink-0 text-xs font-extrabold ${c.hit ? 'bg-ok/15 text-ok' : 'bg-bad/15 text-bad'}`}>
              <Icon name={c.hit ? 'check' : 'x'} className="w-3.5 h-3.5" strokeWidth={3} />
            </span>
            <div><div className={`text-[14.5px] ${c.hit ? '' : 'font-bold'}`}>{c.point}</div><div className="text-[13px] text-muted">{c.note}</div></div>
          </div>
        ))}
      </div>
      <div className={`mt-2 p-4 rounded-2xl text-[14.5px] leading-relaxed ${ev.dangerous ? 'bg-bad/10 border border-bad/25' : 'bg-surface2'}`}>{ev.feedback}</div>
      <div className="flex flex-wrap items-center gap-3 mt-4 text-xs text-muted">
        <Icon name="shield" className="w-4 h-4" />Checked against {ev.sourceCards.map(s => <b key={s.id} className="text-ink">{s.id} · {s.title}</b>)}
        <span className="ml-auto font-display font-bold text-sm text-[#06080C] grad-bg px-3 py-1.5 rounded-full">+{ev.xpAwarded} XP</span>
      </div>
    </div>
  )
}

function Thinking({ post }: { post: Post }) {
  const a = agentOf(post.agentId)
  return (
    <div className="card p-6 mt-4 flex items-center gap-4 animate-rise">
      <Mascot mood="think" size={72} />
      <div><div className="font-display text-lg font-bold">{a.name} is reviewing your answer…</div>
        <div className="text-sm text-muted">Checking it against verified {a.domainLabel.toLowerCase()} fact cards</div>
        <div className="flex gap-1.5 mt-2">{[0, 1, 2].map(i => <span key={i} className="w-2 h-2 rounded-full grad-bg animate-bounce" style={{ animationDelay: `${i * .15}s` }} />)}</div></div>
    </div>
  )
}

export default function PostDetail() {
  const { parts } = useRoute()
  const id = parts[1]
  const { refreshMe, me } = useSession()
  const { data, loading, error } = useAsync(() => api.post(id), [id])
  const [text, setText] = useState('')
  const [phase, setPhase] = useState<'write' | 'thinking' | 'done'>('write')
  const [ev, setEv] = useState<Evaluation>()
  const [err, setErr] = useState<string>()
  const [pointsModalData, setPointsModalData] = useState<PointsModalData | null>(null)

  const submit = async () => {
    if (text.trim().length < 5) return
    setPhase('thinking'); setErr(undefined)
    try {
      const r = await api.answer(id, text.trim())
      setEv(r)
      setPhase('done')
      refreshMe()
      if ((r.score ?? 0) >= 50) {
        setPointsModalData({
          xp: r.xpAwarded || 35,
          title: 'Scenario solved!',
          subtitle: `Score: ${r.score}/100 · ${r.rubricSummary || 'Great real-world decision making.'}`,
          streak: me?.streak,
          totalXp: (me?.xp ?? 0) + (r.xpAwarded || 35),
        })
      }
    }
    catch (e: any) { setErr(e.message); setPhase('write') }
  }

  return (
    <AppShell>
      <div className="max-w-[680px] mx-auto">
        <Link to="/feed" className="inline-flex items-center gap-1 text-sm text-muted hover:text-ink mb-3"><Icon name="chevronLeft" className="w-4 h-4" />Back to feed</Link>
        {loading && <PostSkeleton />}
        {error && <EmptyState title="Post not found" text={error} />}
        {data && data.post.type !== 'scenario' && <PostCard post={data.post} />}
        {data && data.post.type === 'scenario' && (() => {
          const post = data.post
          const already = post.my?.answered && phase === 'write' && !ev
          return (
            <>
              <article className="card p-4 md:p-6">
                <PostHeader post={post} />
                <h1 className="text-2xl md:text-[28px] font-bold mt-4 leading-tight">{post.title}</h1>
                <p className="mt-2 text-[16px] leading-relaxed text-ink/90">{post.body}</p>
                <p className="mt-2 text-[17px] font-bold">{post.question}</p>
                <Scene post={post} tall />
              </article>

              {phase === 'write' && (
                <div className="card p-4 md:p-5 mt-4">
                  {already && <div className="mb-3 text-sm p-3 rounded-xl bg-surface2">You already answered this (score {post.my?.score}). You can try again for practice.</div>}
                  <label htmlFor="ans" className="font-bold flex items-center gap-2"><Mascot mood="look" size={28} animate={false} />Your answer</label>
                  <textarea id="ans" className="input mt-3 min-h-[130px] resize-y leading-relaxed" maxLength={MAX} value={text} onChange={e => setText(e.target.value)}
                    placeholder="Write the steps you would take, in your own words…" />
                  <div className="flex items-center gap-3 mt-3">
                    <span className="text-xs text-muted tabular-nums">{text.length}/{MAX}</span>
                    {err && <span className="text-xs text-bad">{err}</span>}
                    <button className="btn-grad ml-auto !px-5" disabled={text.trim().length < 5} onClick={submit}><Icon name="send" className="w-4 h-4" />Submit answer</button>
                  </div>
                  <p className="text-xs text-muted mt-3">Your answer is private. It may appear anonymously in “Top answers” only after AI moderation.</p>
                </div>
              )}
              {phase === 'thinking' && <Thinking post={post} />}
              {phase === 'done' && ev && (
                <>
                  <div className="card p-4 mt-4 flex gap-3"><UserAvatar emoji={me?.avatar ?? '🙂'} size={34} /><p className="text-[14.5px] text-ink/90">{text}</p></div>
                  <EvaluationCard ev={ev} post={post} />
                  <button className="btn-ghost mt-3" onClick={() => { setPhase('write'); setEv(undefined) }}>Try again</button>
                </>
              )}

              {(phase === 'done' || post.my?.answered) && data.responses.length > 0 && (
                <div className="mt-8">
                  <h3 className="text-lg font-bold mb-3">Top answers from students</h3>
                  <div className="space-y-3">
                    {data.responses.map(r => (
                      <div key={r.id} className="card p-4">
                        <div className="flex items-center gap-2.5"><UserAvatar emoji={r.avatar} size={34} /><b className="text-sm">{r.nickname}</b>
                          {r.expertPick && <span className="text-[10px] font-extrabold tracking-wider px-2 py-0.5 rounded-md bg-warn/15 text-warn">⭐ EXPERT PICK</span>}
                          <span className={`ml-auto font-bold text-sm ${r.score >= 75 ? 'text-ok' : 'text-warn'}`}>{r.score}</span></div>
                        <p className="text-[14.5px] mt-2 text-ink/90">{r.text}</p>
                        {r.expertReply && (
                          <div className="mt-3 flex gap-2.5 p-3 rounded-2xl bg-surface2"><AgentAvatar agent={agentOf(post.agentId)} size={26} />
                            <p className="text-[13.5px]"><b>{agentOf(post.agentId).name}</b> · {r.expertReply}</p></div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}
              {phase === 'write' && !post.my?.answered && <p className="text-center text-sm text-muted mt-6">🔒 Top answers unlock after you answer.</p>}
            </>
          )
        })()}
      </div>
      <PointsModal data={pointsModalData} onClose={() => setPointsModalData(null)} />
    </AppShell>
  )
}
