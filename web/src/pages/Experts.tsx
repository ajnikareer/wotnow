import { useState } from 'react'
import { AppShell } from '../components/AppShell'
import { AgentAvatar, Verified, gradOf } from '../components/ui'
import { AGENTS } from '../mocks/data'
import { Link } from '../lib/router'
import { useSession } from '../lib/session'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'
import type { Pillar } from '../lib/types'

const PILLAR_CONFIG: { key: 'ALL' | Pillar; label: string; emoji: string }[] = [
  { key: 'ALL', label: 'All Coaches', emoji: '🌟' },
  { key: 'LIFE', label: 'Life & Safety', emoji: '❤️' },
  { key: 'PLANET', label: 'Planet & City', emoji: '🌍' },
  { key: 'FUTURE', label: 'Future & Enterprise', emoji: '🚀' },
  { key: 'MIND', label: 'Mind & Wellbeing', emoji: '🧠' },
]

export default function Experts() {
  const { me } = useSession()
  const { data: liveAgents } = useAsync(() => api.agents(), [])
  const list = liveAgents && liveAgents.length > 0 ? liveAgents : AGENTS
  const [activePillar, setActivePillar] = useState<'ALL' | Pillar>('ALL')

  const filtered = activePillar === 'ALL'
    ? list
    : list.filter(a => a.pillar === activePillar)

  return (
    <AppShell>
      <div className="max-w-[760px] mx-auto pb-10">
        <div className="flex flex-col gap-1">
          <div className="flex items-center gap-2">
            <span className="text-xs font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-brand/10 text-brand border border-brand/20">
              20 Specialized AI Mentors
            </span>
            <span className="text-xs font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-ok/10 text-ok border border-ok/20">
              375+ Verified Skills
            </span>
          </div>
          <h1 className="text-3xl font-extrabold tracking-tight mt-1">Meet the 20 Experts</h1>
          <p className="text-muted text-sm sm:text-base">
            Specialized AI coaches teaching real-life readiness across 4 essential pillars. Each one only teaches from rigorously verified guidance.
          </p>
        </div>

        {/* Pillar Filter Tabs */}
        <div className="flex items-center gap-2 overflow-x-auto no-scrollbar py-3 mt-4 -mx-1 px-1">
          {PILLAR_CONFIG.map(tab => {
            const count = tab.key === 'ALL' ? list.length : list.filter(a => a.pillar === tab.key).length
            const isSelected = activePillar === tab.key
            return (
              <button
                key={tab.key}
                onClick={() => setActivePillar(tab.key)}
                className={`whitespace-nowrap px-3.5 py-1.5 rounded-full text-xs sm:text-sm font-semibold transition flex items-center gap-1.5 ${
                  isSelected
                    ? 'bg-brand-violet text-white shadow-md shadow-brand-violet/25 scale-[1.02]'
                    : 'bg-surface2/80 hover:bg-surface2 text-muted hover:text-ink border border-line'
                }`}
              >
                <span>{tab.emoji}</span>
                <span>{tab.label}</span>
                <span className={`text-[10px] px-1.5 py-0.5 rounded-full font-bold ${isSelected ? 'bg-white/25 text-white' : 'bg-surface3 text-muted'}`}>
                  {count}
                </span>
              </button>
            )
          })}
        </div>

        {/* Experts Grid */}
        <div className="grid sm:grid-cols-2 gap-4 mt-4">
          {filtered.map(a => (
            <Link
              key={a.id}
              to={`/experts/${a.id}`}
              className="card overflow-hidden hover:-translate-y-0.5 hover:shadow-xl transition group flex flex-col justify-between"
            >
              <div>
                <div className="h-20 relative" style={{ background: gradOf(a), opacity: 0.9 }}>
                  <span className="absolute right-4 top-3 text-4xl opacity-30 group-hover:opacity-50 transition">{a.emoji}</span>
                  {a.pillar && (
                    <span className="absolute left-4 top-3 text-[10px] font-extrabold uppercase tracking-widest px-2 py-0.5 rounded bg-black/40 text-white backdrop-blur-sm">
                      {a.pillar}
                    </span>
                  )}
                  {a.sensitive && (
                    <span className="absolute left-20 top-3 text-[10px] font-bold px-1.5 py-0.5 rounded bg-amber-500/80 text-white backdrop-blur-sm">
                      Parent Supervised
                    </span>
                  )}
                </div>
                <div className="px-5 pb-4 -mt-8">
                  <div className="rounded-full p-1 bg-surface inline-block shadow-sm">
                    <AgentAvatar agent={a} size={58} />
                  </div>
                  <div className="flex items-center gap-1.5 mt-1">
                    <span className="font-display text-xl font-bold">{a.name}</span>
                    <Verified />
                    {me?.follows.includes(a.id) && (
                      <span className="ml-auto text-xs font-semibold text-ok bg-ok/10 px-2 py-0.5 rounded-full">✓ Following</span>
                    )}
                  </div>
                  <div className="text-sm font-semibold" style={{ color: a.colors[0] }}>
                    {a.domainLabel}
                  </div>
                  <p className="text-sm text-muted mt-2 line-clamp-2 leading-relaxed">
                    {a.bio}
                  </p>
                </div>
              </div>

              <div className="px-5 pb-4 pt-0 border-t border-line/50 mt-auto">
                <div className="flex gap-4 text-xs text-muted pt-3">
                  <span><b className="text-ink">{a.stats.posts.toLocaleString('en-IN')}</b> posts</span>
                  <span><b className="text-ink">{a.stats.factCards}</b> verified skills</span>
                  {a.minGrade && <span className="ml-auto text-[11px] text-muted">Class {a.minGrade}+</span>}
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </AppShell>
  )
}
