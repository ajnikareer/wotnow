import { useEffect, useState } from 'react'
import type { Post, VoteResult } from '../lib/types'
import { api } from '../lib/api'
import { labelOf, stateOf, type CardState } from '../lib/cardState'
import { timeAgo } from '../lib/hooks'
import { Link, navigate } from '../lib/router'
import { useToast } from '../lib/toast'
import { useSession } from '../lib/session'
import { AgentAvatar, Verified, agentOf } from './ui'
import { Icon } from './Icon'
import type { PointsModalData } from './PointsModal'
import '../styles/neon.css'

const TYPE_LABEL: Record<Post['type'], string> = {
  scenario: 'WHAT WOULD YOU DO?', poll: 'POLL', myth_fact: 'MYTH OR FACT', scam_legit: 'SCAM OR LEGIT?', local_alert: 'LOCAL ALERT',
}

export function getBinaryConfig(post: Post) {
  if (post.options && post.options.length === 2) {
    return {
      typeLabel: 'QUICK CHECK',
      intro: post.body || 'Quick check:',
      options: post.options.map(o => ({ id: o.id, label: o.text })),
    }
  }

  const text = (post.statement || post.question || post.body || '').trim()
  const isQuestion = text.endsWith('?') || /^(should|is|can|do|does|would|could|are|will|have|has)\b/i.test(text.replace(/^[“"']/, ''))
  const isMyth = /myth|belief|folklore|old wives|rumour|rumor/i.test(text) || /lots of people believe/i.test(post.body || '')

  if (isQuestion) {
    return {
      typeLabel: 'YES OR NO?',
      intro: post.body === 'Lots of people believe this. Do you?' ? 'Quick question:' : (post.body || 'Quick question:'),
      options: [
        { id: 'myth', label: '❌ No' },
        { id: 'fact', label: '✅ Yes' },
      ],
    }
  }

  if (isMyth) {
    return {
      typeLabel: 'MYTH OR FACT?',
      intro: post.body || 'Lots of people believe this. Do you?',
      options: [
        { id: 'myth', label: '❌ Myth' },
        { id: 'fact', label: '✅ Fact' },
      ],
    }
  }

  // Statements default naturally to True or False
  return {
    typeLabel: 'TRUE OR FALSE?',
    intro: post.body === 'Lots of people believe this. Do you?' ? 'True or false?' : (post.body || 'True or false?'),
    options: [
      { id: 'myth', label: '❌ False' },
      { id: 'fact', label: '✅ True' },
    ],
  }
}

export function PostHeader({ post }: { post: Post }) {
  const a = agentOf(post.agentId)
  const typeLabel = post.type === 'myth_fact' ? getBinaryConfig(post).typeLabel : TYPE_LABEL[post.type]
  return (
    <div className="flex items-center gap-2.5">
      <Link to={`/experts/${a.id}`}><AgentAvatar agent={a} size={38} /></Link>
      <div className="leading-tight min-w-0">
        <Link to={`/experts/${a.id}`} className="font-bold text-[14px] inline-flex items-center gap-1.5 hover:underline">
          {a.name}<Verified /><span className="text-[9px] font-extrabold tracking-wider px-1.5 py-0.5 rounded-md bg-surface3 text-muted">AI</span>
        </Link>
        <div className="text-[11.5px] text-muted flex items-center gap-1">
          {a.domainLabel} · {timeAgo(post.createdAt)}
          {post.city && <><span>·</span><Icon name="pin" className="w-3 h-3" />{post.city}</>}
        </div>
      </div>
      <span className="pill ml-auto shrink-0 text-[10px] sm:text-xs" style={{ color: a.colors[0], background: `${a.colors[0]}1f` }}>{typeLabel}</span>
    </div>
  )
}

export function Scene({ post, tall = false }: { post: Post; tall?: boolean }) {
  const a = agentOf(post.agentId)
  const [e1, e2, e3] = post.scene?.emojis ?? [a.emoji]
  return (
    <div className={`relative mt-2.5 rounded-xl overflow-hidden ${tall ? 'h-48 md:h-56' : 'h-36 md:h-44'}`}
      style={{ background: `radial-gradient(circle at 60% 75%, ${a.colors[1]}cc 0, ${a.colors[0]}99 16%, transparent 38%), radial-gradient(circle at 18% 18%, rgba(139,92,246,.28), transparent 42%), linear-gradient(160deg, #241a2e, #0f1118)` }}>
      {post.scene?.bubble && (
        <div className="absolute left-[7%] top-[14%] bg-white text-[#111] text-xs font-bold px-2.5 py-1.5 rounded-xl rounded-bl-md shadow-xl animate-rise">{post.scene.bubble}</div>
      )}
      <span className="absolute left-[52%] top-[20%] text-[52px] md:text-[64px] animate-bob" style={{ filter: `drop-shadow(0 0 24px ${a.colors[0]})` }}>{e1}</span>
      {e2 && <span className="absolute left-[50%] top-[58%] text-[36px] md:text-[44px]">{e2}</span>}
      {e3 && <span className="absolute left-[16%] top-[50%] text-[34px] md:text-[42px]">{e3}</span>}
      <span className="absolute right-2.5 bottom-2 text-[10px] text-white/75 bg-black/35 backdrop-blur px-2 py-0.5 rounded-full">✨ AI scene</span>
    </div>
  )
}

function Meta({ post, extra }: { post: Post; extra?: string }) {
  const toast = useToast()
  return (
    <div className="flex items-center gap-3.5 mt-2.5 text-[12px] text-muted">
      {post.stats.responses > 0 && (
        <span className="inline-flex items-center gap-1.5"><Icon name="users" className="w-3.5 h-3.5" />{post.stats.responses.toLocaleString('en-IN')}</span>
      )}
      {extra && <span>{extra}</span>}
      <button className="ml-auto p-1.5 rounded-lg hover:bg-surface2 hover:text-ink" aria-label="Save" onClick={() => toast('Saved to your collection 🔖')}><Icon name="bookmark" className="w-3.5 h-3.5" /></button>
      <button className="p-1.5 rounded-lg hover:bg-surface2 hover:text-ink" aria-label="Share" onClick={() => toast('Share card ready to send 📤')}><Icon name="share" className="w-3.5 h-3.5" /></button>
    </div>
  )
}

/* ---------- Scenario (opens detail to answer) ---------- */
function ScenarioBody({ post }: { post: Post }) {
  const answered = post.my?.answered
  return (
    <>
      <p className="mt-2.5 text-[14px] leading-relaxed text-ink/90">{post.body} <strong className="text-ink">{post.question}</strong></p>
      <Link to={`/post/${post.id}`}><Scene post={post} /></Link>
      <Link to={`/post/${post.id}`} className="mt-2.5 flex items-center gap-2.5 rounded-xl bg-surface2 border border-line pl-3.5 pr-1.5 py-1.5 hover:border-brand-violet/50 transition">
        <span className="text-muted text-xs sm:text-[13px] flex-1">{answered ? `You scored ${post.my?.score}. See feedback and top answers` : 'Type what you would do…'}</span>
        <span className={answered ? 'btn-soft !py-1.5 !px-3 !text-xs' : 'btn-grad !py-1.5 !px-3 !text-xs'}>{answered ? 'View' : 'Answer · up to +50 XP'}</span>
      </Link>
      <Meta post={post} extra={post.stats.avgScore ? `Avg score ${post.stats.avgScore}` : undefined} />
    </>
  )
}

/* ---------- Vote-style posts: poll / myth-fact / scam-legit ---------- */
function useVote(post: Post, onResult?: (s: CardState) => void, onComplete?: (data: PointsModalData) => void) {
  const [res, setRes] = useState<VoteResult | null>(null)
  const [busy, setBusy] = useState(false)
  const toast = useToast()
  const { refreshMe, me } = useSession()
  useEffect(() => { if (post.my?.choice) api.voteResult(post.id).then(setRes) }, [post.id, post.my?.choice])
  const vote = async (c: string) => {
    if (res || busy) return
    setBusy(true)
    try {
      const r = await api.vote(post.id, c)
      setRes(r)
      const correct = r.isCorrect
      onResult?.(correct ? 'done' : 'retry')                    // the border changes colour straight away
      refreshMe()
      if (correct) {
        onComplete?.({
          xp: r.xpAwarded || 10,
          title: 'Correct answer!',
          subtitle: r.explanation || 'Great safety instincts.',
          streak: me?.streak,
          totalXp: (me?.xp ?? 0) + (r.xpAwarded || 10),
        })
      } else {
        toast(`Good try! +${r.xpAwarded} XP for answering`)
      }
    } finally { setBusy(false) }
  }
  return { res, vote, busy }
}

function Explanation({ res }: { res: VoteResult }) {
  return (
    <div className={`mt-2.5 p-3 rounded-xl text-[13px] leading-relaxed animate-rise border ${res.isCorrect ? 'bg-ok/10 border-ok/25' : 'bg-warn/10 border-warn/25'}`}>
      <b>{res.isCorrect ? '✅ You got it.' : '💡 Here’s the thing.'}</b> {res.explanation}
    </div>
  )
}

function PollBody({ post, onResult, onComplete }: { post: Post; onResult: (s: CardState) => void; onComplete?: (data: PointsModalData) => void }) {
  const { res, vote, busy } = useVote(post, onResult, onComplete)
  return (
    <>
      <p className="mt-2.5 text-[14px] leading-relaxed text-ink/90">{post.body} <strong className="text-ink">{post.question}</strong></p>
      <div className="mt-2.5 space-y-1.5">
        {post.options!.map(o => {
          const pct = res?.distribution[o.id] ?? 0
          const correct = res && o.id === res.correct
          const mine = res && o.id === res.choice
          return (
            <button key={o.id} disabled={!!res || busy} onClick={() => vote(o.id)}
              className={`relative w-full text-left rounded-xl border px-3.5 py-2.5 text-[13.5px] overflow-hidden transition
                ${res ? (correct ? 'border-ok/60' : mine ? 'border-bad/50' : 'border-line') : 'border-line hover:border-brand-violet/60 hover:bg-surface2'}`}>
              {res && <span className={`absolute inset-y-0 left-0 transition-[width] duration-700 ${correct ? 'bg-ok/15' : 'bg-surface3/60'}`} style={{ width: `${pct}%` }} />}
              <span className="relative flex items-center gap-2.5">
                <span className="flex-1">{o.text}</span>
                {mine && <span className="text-[9.5px] font-extrabold tracking-wider px-1.5 py-0.5 rounded-md bg-surface3">YOU</span>}
                {res && <span className={`font-bold tabular-nums text-xs ${correct ? 'text-ok' : 'text-muted'}`}>{pct}%</span>}
              </span>
            </button>
          )
        })}
      </div>
      {res && <Explanation res={res} />}
      <Meta post={post} extra={res ? undefined : 'Tap to vote'} />
    </>
  )
}

function BinaryBody({ post, kind, onResult, onComplete }: { post: Post; kind: 'myth_fact' | 'scam_legit'; onResult: (s: CardState) => void; onComplete?: (data: PointsModalData) => void }) {
  const { res, vote, busy } = useVote(post, onResult, onComplete)
  const cfg = kind === 'myth_fact'
    ? getBinaryConfig(post)
    : {
        typeLabel: 'SCAM OR LEGIT?',
        intro: post.body,
        options: [{ id: 'scam', label: '🚩 Scam' }, { id: 'legit', label: '✅ Legit' }],
      }
  const opts = cfg.options
  return (
    <>
      <p className="mt-2.5 text-[14px] text-ink/90">{cfg.intro}</p>
      {kind === 'myth_fact' ? (
        <div className="mt-2.5 rounded-xl p-3.5 sm:p-4 font-display text-[16.5px] sm:text-[18px] font-semibold leading-snug grad-soft border border-line">{post.statement}</div>
      ) : (
        <div className="mt-2.5 rounded-xl p-3 bg-surface2 border border-line">
          <div className="text-[11px] text-muted mb-1.5">From: {post.message!.from}</div>
          <div className="rounded-xl rounded-bl-md bg-surface3 px-3.5 py-2.5 text-[13.5px] max-w-[92%]">{post.message!.text}</div>
        </div>
      )}
      <div className="grid grid-cols-2 gap-2 mt-2.5">
        {opts.map((o, i) => {
          const correct = res && o.id === res.correct
          const mine = res && o.id === res.choice
          return (
            <button key={o.id} disabled={!!res || busy} onClick={() => vote(o.id)}
              className={`rounded-xl py-2.5 font-bold text-sm border transition active:scale-[.98]
                ${res ? (correct ? 'bg-ok/15 border-ok/50 text-ok' : 'opacity-50 border-line') :
                  i === 0 ? 'border-bad/30 bg-bad/[.06] text-bad hover:bg-bad/10' : 'border-ok/30 bg-ok/[.06] text-ok hover:bg-ok/10'}
                ${mine && !correct ? 'animate-shake' : ''}`}>
              {o.label}{res && <span className="ml-2 font-bold opacity-80">{res.distribution[o.id]}%</span>}
            </button>
          )
        })}
      </div>
      {res && <Explanation res={res} />}
      <Meta post={post} />
    </>
  )
}

/* ---------- Local alert ---------- */
function AlertBody({ post, onResult, onComplete }: { post: Post; onResult: (s: CardState) => void; onComplete?: (data: PointsModalData) => void }) {
  const [done, setDone] = useState(!!post.my?.checkedIn)
  const { refreshMe, me } = useSession()
  return (
    <>
      <p className="mt-2.5 text-[14px] leading-relaxed"><strong>{post.title}.</strong> <span className="text-ink/90">{post.body}</span></p>
      <div className="flex flex-wrap gap-1.5 mt-2.5">{post.chips?.map(c => <span key={c} className="chip text-xs">{c}</span>)}</div>
      <div className="grid sm:grid-cols-3 gap-2 mt-2.5">
        {post.steps?.map(s => (
          <div key={s.text} className="rounded-xl bg-surface/60 border border-line p-2.5 text-[12.5px] leading-snug">
            <div className="text-lg mb-1">{s.emoji}</div>{s.text}
          </div>
        ))}
      </div>
      <div className="flex items-center gap-2.5 mt-2.5">
        <button disabled={done} className={done ? 'btn-soft !py-1.5 !px-3 !text-xs' : 'btn-ink !py-1.5 !px-3 !text-xs'}
          onClick={async () => {
            const r = await api.checkin(post.id)
            setDone(true)
            onResult('done')
            refreshMe()
            onComplete?.({
              xp: r.xpAwarded || 5,
              title: 'Daily check-in completed!',
              subtitle: 'You took action on today’s safety alert.',
              streak: me?.streak,
              totalXp: (me?.xp ?? 0) + (r.xpAwarded || 5),
            })
          }}>
          <Icon name="check" className="w-3.5 h-3.5" />{done ? 'You did one today' : 'I’ll do one today'}
        </button>
        <span className="text-xs text-muted">
          {post.stats.responses > 0 ? `${post.stats.responses} ${post.stats.responses === 1 ? 'learner' : 'learners'} completed` : 'Take action today'}
        </span>
      </div>
    </>
  )
}

export function PostCard({ post, onComplete, className = '' }: { post: Post; onComplete?: (postId: string, p: PointsModalData) => void; className?: string }) {
  const isAlert = post.type === 'local_alert'
  // A result produced on this card (a vote, a check-in) is shown at once; the server's state takes over on the next load.
  const [local, setLocal] = useState<CardState | null>(null)
  useEffect(() => { setLocal(null) }, [post.id, (post as any).state])
  const state = stateOf(post, local)
  const label = labelOf(post, state)

  const handleComplete = (data: PointsModalData) => {
    onComplete?.(post.id, data)
  }

  return (
    <article className={`card wn-card wn-${state} relative p-3.5 sm:p-4 animate-rise ${isAlert ? 'grad-soft' : ''} ${className}`} data-state={state}
      onDoubleClick={() => post.type === 'scenario' && navigate(`/post/${post.id}`)}>
      {label && <span key={state} className="wn-tag" aria-label={`Status: ${label}`}>{label}</span>}
      <PostHeader post={post} />
      {post.type === 'scenario' && <ScenarioBody post={post} />}
      {post.type === 'poll' && <PollBody post={post} onResult={setLocal} onComplete={handleComplete} />}
      {post.type === 'myth_fact' && <BinaryBody post={post} kind="myth_fact" onResult={setLocal} onComplete={handleComplete} />}
      {post.type === 'scam_legit' && <BinaryBody post={post} kind="scam_legit" onResult={setLocal} onComplete={handleComplete} />}
      {isAlert && <AlertBody post={post} onResult={setLocal} onComplete={handleComplete} />}
    </article>
  )
}
