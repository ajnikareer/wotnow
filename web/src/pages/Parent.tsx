import { useEffect, useState } from 'react'
import { Logo, Mascot } from '../components/Brand'
import { Icon } from '../components/Icon'
import { AgentAvatar, SkillBars, ThemeToggle, UserAvatar, agentByDomain, agentOf } from '../components/ui'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'
import { Link, navigate } from '../lib/router'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'
import type { Domain, ParentSummary } from '../lib/types'

function Ring({ value, max }: { value: number; max: number }) {
  const pct = Math.min(100, Math.round((value / max) * 100))
  return (
    <div className="w-28 h-28 rounded-full grid place-items-center shrink-0" style={{ background: `conic-gradient(#22D3EE 0 ${pct}%, rgb(var(--surface3)) ${pct}% 100%)` }}>
      <div className="w-[92px] h-[92px] rounded-full bg-surface grid place-items-center text-center">
        <div><div className="font-display text-3xl font-bold leading-none">{value}</div><div className="text-[11px] text-muted mt-1">of {max} min</div></div></div>
    </div>
  )
}

export default function Parent() {
  const { signOut } = useSession()
  const toast = useToast()
  const { data } = useAsync(() => api.parent(), [])
  const [s, setS] = useState<ParentSummary['settings'] | undefined>(data?.settings)
  useEffect(() => { if (data) setS(data.settings) }, [data])
  const save = async (next: ParentSummary['settings']) => { setS(next); await api.updateParentSettings(next); toast('Saved ✓') }

  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-30 bg-bg/80 backdrop-blur-xl border-b border-line">
        <div className="max-w-6xl mx-auto flex items-center gap-3 px-4 md:px-6 h-16">
          <Logo className="h-6.5" /><span className="chip !bg-brand-violet/10 !border-brand-violet/30 !text-brand-violet font-bold">Parent</span>
          <div className="ml-auto flex items-center gap-2">
            <Link to="/feed" className="btn-ghost hidden sm:inline-flex">See child’s feed</Link><ThemeToggle compact />
            <button className="btn-ghost !p-2.5" aria-label="Sign out" onClick={() => { signOut(); navigate('/') }}><Icon name="logout" className="w-4 h-4" /></button>
          </div>
        </div>
      </header>
      {!data || !s ? <div className="max-w-6xl mx-auto p-6"><div className="skeleton h-64" /></div> : (
        <main className="max-w-6xl mx-auto px-4 md:px-6 py-6 grid lg:grid-cols-[1fr_360px] gap-5">
          <div className="space-y-5">
            <div className="card p-5 md:p-6 grad-soft">
              <div className="flex flex-wrap items-center gap-4">
                <UserAvatar emoji={data.child.avatar} size={64} />
                <div><div className="text-sm text-muted">Your child</div><h1 className="text-2xl md:text-3xl font-bold">{data.child.nickname}</h1>
                  <div className="text-sm text-muted">Class {data.child.grade} · Level “{data.child.levelName}” · 🔥 {data.child.streak}-day streak</div></div>
                <div className="ml-auto flex items-center gap-4"><Ring value={data.minutesToday} max={s.dailyLimit} />
                  <div className="text-sm"><div className="font-bold">Today</div><div className="text-muted">{s.dailyLimit - data.minutesToday} min left</div></div></div>
              </div>
            </div>

            <div className="card p-5 md:p-6">
              <h2 className="text-lg font-bold">This week</h2>
              <div className="flex items-end gap-3 h-40 mt-4">
                {data.week.map(d => (
                  <div key={d.day} className="flex-1 flex flex-col items-center gap-2 h-full justify-end">
                    <div className="text-[11px] text-muted tabular-nums">{d.answers}</div>
                    <div className="w-full max-w-[38px] rounded-xl grad-bg transition-all" style={{ height: `${(d.minutes / 30) * 100}%`, opacity: .35 + d.minutes / 50 }} />
                    <div className="text-xs font-semibold text-muted">{d.day}</div>
                  </div>
                ))}
              </div>
              <div className="text-xs text-muted mt-2">Bar = minutes · number = answers given</div>
            </div>

            <div className="card p-5 md:p-6"><h2 className="text-lg font-bold mb-4">Skills progress</h2><SkillBars skills={data.child.skills} /></div>

            <div className="card p-5 md:p-6">
              <h2 className="text-lg font-bold mb-2">Recent answers</h2>
              <div className="divide-y divide-line">
                {data.recent.map(r => (
                  <div key={r.postTitle} className="flex items-center gap-3 py-3">
                    <AgentAvatar agent={agentOf(r.agentId)} size={36} />
                    <div className="min-w-0 flex-1"><div className="font-semibold text-sm">{r.postTitle}</div>
                      <div className="text-xs text-muted">{r.when}{r.missed && <> · Missed: <b className="text-warn">{r.missed}</b></>}</div></div>
                    <span className={`font-display font-bold text-lg ${r.score >= 75 ? 'text-ok' : r.score >= 50 ? 'text-warn' : 'text-bad'}`}>{r.score}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="space-y-5">
            <div className="card p-5">
              <div className="flex items-center gap-3"><Mascot mood="look" size={44} /><h2 className="text-lg font-bold">Talk about it at dinner</h2></div>
              <p className="text-xs text-muted mt-1">Suggested by AI from this week’s answers.</p>
              <ul className="mt-3 space-y-2.5">{data.conversationStarters.map(c => <li key={c} className="text-sm p-3 rounded-2xl bg-surface2 leading-relaxed">💬 {c}</li>)}</ul>
            </div>

            <div className="card p-5">
              <h2 className="text-lg font-bold">Safety</h2>
              <div className="grid grid-cols-3 gap-2 mt-3 text-center">
                <div className="rounded-2xl bg-ok/10 p-3"><div className="font-display text-2xl font-bold text-ok">{data.safety.flaggedReplies}</div><div className="text-[11px] text-muted">flagged replies</div></div>
                <div className="rounded-2xl bg-surface2 p-3"><div className="font-display text-2xl font-bold">{data.safety.blockedContent}</div><div className="text-[11px] text-muted">blocked by AI</div></div>
                <div className="rounded-2xl bg-surface2 p-3"><div className="font-display text-lg font-bold mt-1">Off</div><div className="text-[11px] text-muted">messaging</div></div>
              </div>
            </div>

            <div className="card p-5 space-y-5">
              <h2 className="text-lg font-bold">Controls</h2>
              <div><div className="flex justify-between text-sm font-semibold"><span>Daily time limit</span><span className="grad-text font-bold">{s.dailyLimit} min</span></div>
                <input type="range" min={10} max={90} step={5} value={s.dailyLimit} onChange={e => setS({ ...s, dailyLimit: +e.target.value })} onMouseUp={() => save(s)} onTouchEnd={() => save(s)}
                  className="w-full mt-2 accent-violet-500" /></div>
              <div className="flex items-center justify-between text-sm"><span className="font-semibold">Quiet hours</span><span className="chip">{s.quietHours}</span></div>
              <label className="flex items-center justify-between text-sm cursor-pointer"><span className="font-semibold">Weekly email report</span>
                <input type="checkbox" className="w-5 h-5 accent-violet-500" checked={s.weeklyEmail} onChange={e => save({ ...s, weeklyEmail: e.target.checked })} /></label>
              <div>
                <div className="text-sm font-semibold mb-3">Topic Permissions (20 Domains)</div>
                <div className="space-y-3">
                  {[
                    { title: '❤️ Life & Safety', domains: ['fire', 'road', 'firstaid', 'disaster', 'safety', 'law', 'fitness', 'hygiene'] as Domain[] },
                    { title: '🌍 Planet & City', domains: ['environment', 'animals', 'greenenergy', 'civic'] as Domain[] },
                    { title: '🚀 Future & Enterprise', domains: ['money', 'enterprise', 'careers', 'digital', 'nutrition'] as Domain[] },
                    { title: '🧠 Mind & Wellbeing', domains: ['feelings', 'screentime', 'inclusion'] as Domain[] },
                  ].map(group => (
                    <div key={group.title} className="p-2.5 rounded-xl bg-surface2/60 border border-line/40">
                      <div className="text-[11px] font-bold text-muted uppercase tracking-wider mb-2">{group.title}</div>
                      <div className="flex flex-wrap gap-1.5">
                        {group.domains.map(d => {
                          const a = agentByDomain(d)
                          const on = s.topics[d] ?? true
                          return (
                            <button
                              key={d}
                              type="button"
                              onClick={() => save({ ...s, topics: { ...s.topics, [d]: !on } })}
                              className={`chip !text-xs !py-1 !px-2.5 transition ${
                                on ? '!border-brand-violet/50 !bg-brand-violet/10 !text-ink font-medium' : 'opacity-40 line-through'
                              }`}
                            >
                              {a.emoji} {a.domainLabel}
                            </button>
                          )
                        })}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
              <button className="btn-ghost w-full text-bad" onClick={() => toast('In the full app this deletes all of your child’s data.')}>Delete child’s data</button>
            </div>
          </div>
        </main>
      )}
    </div>
  )
}
