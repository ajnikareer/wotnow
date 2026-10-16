import type { ReactNode } from 'react'
import { AGENTS } from '../mocks/data'
import type { Agent, Domain } from '../lib/types'
import { useTheme, type ThemePref } from '../lib/theme'
import { Icon } from './Icon'
import { Link } from '../lib/router'

export const agentOf = (id: string): Agent => AGENTS.find(a => a.id === id) ?? AGENTS[0]
export const agentByDomain = (d: Domain): Agent => AGENTS.find(a => a.domain === d) ?? AGENTS[0]
export const gradOf = (a: Agent) => `linear-gradient(135deg, ${a.colors[0]}, ${a.colors[1]})`

export function AgentAvatar({ agent, size = 42, ring = false, seen = false }: { agent: Agent; size?: number; ring?: boolean; seen?: boolean }) {
  const inner = (
    <div className="rounded-full grid place-items-center shrink-0 select-none"
      style={{ width: size, height: size, background: gradOf(agent), fontSize: size * 0.48 }}>
      <span aria-hidden>{agent.emoji}</span>
    </div>
  )
  if (!ring) return inner
  return (
    <div className="rounded-full p-[2.5px]" style={{ background: seen ? 'rgb(var(--surface3))' : `conic-gradient(from 200deg, ${agent.colors[0]}, ${agent.colors[1]}, ${agent.colors[0]})` }}>
      <div className="rounded-full p-[2.5px] bg-bg">{inner}</div>
    </div>
  )
}

export function Verified({ className = 'w-4 h-4' }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" className={className} aria-label="Verified AI expert">
      <path fill="#38BDF8" d="M12 1.5 14.6 3.4l3.2-.2 1 3 2.7 1.8-1 3.1 1 3.1-2.7 1.8-1 3-3.2-.2L12 22.5l-2.6-1.9-3.2.2-1-3-2.7-1.8 1-3.1-1-3.1 2.7-1.8 1-3 3.2.2z" />
      <path d="m8 12 3 3 5-6" fill="none" stroke="#fff" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}

export function UserAvatar({ emoji, size = 36, highlight = false }: { emoji: string; size?: number; highlight?: boolean }) {
  return (
    <div className={`rounded-full grid place-items-center shrink-0 ${highlight ? 'grad-bg' : 'bg-surface3'}`}
      style={{ width: size, height: size, fontSize: size * 0.5 }}><span aria-hidden>{emoji}</span></div>
  )
}

export function ScoreRing({ score, size = 88, label = '/ 100', color }: { score: number; size?: number; label?: string; color?: string }) {
  const c = color ?? (score >= 75 ? '#10B981' : score >= 50 ? '#F59E0B' : '#EF4444')
  return (
    <div className="rounded-full grid place-items-center shrink-0 animate-pop"
      style={{ width: size, height: size, background: `conic-gradient(${c} 0 ${score}%, rgb(var(--surface3)) ${score}% 100%)` }}>
      <div className="rounded-full bg-surface grid place-items-center text-center" style={{ width: size - 16, height: size - 16 }}>
        <div><div className="font-display font-bold leading-none" style={{ fontSize: size * 0.3 }}>{score}</div>
          <div className="text-[10px] text-muted mt-0.5">{label}</div></div>
      </div>
    </div>
  )
}

export function Bar({ value, from = '#8B5CF6', to = '#22D3EE', className = 'h-2' }: { value: number; from?: string; to?: string; className?: string }) {
  return (
    <div className={`w-full rounded-full bg-surface3 overflow-hidden ${className}`}>
      <div className="h-full rounded-full transition-[width] duration-700" style={{ width: `${Math.max(0, Math.min(100, value))}%`, background: `linear-gradient(90deg, ${from}, ${to})` }} />
    </div>
  )
}

export function SkillBars({ skills, compact = false }: { skills: Partial<Record<Domain, number>>; compact?: boolean }) {
  return (
    <div className={compact ? 'space-y-2.5' : 'space-y-3'}>
      {(Object.entries(skills) as [Domain, number][]).map(([d, v]) => {
        const a = agentByDomain(d)
        return (
          <div key={d} className="grid grid-cols-[110px_1fr_30px] items-center gap-3 text-[13px]">
            <span className="truncate">{a.emoji} {a.domainLabel}</span>
            <Bar value={v} from={a.colors[0]} to={a.colors[1]} />
            <span className="text-right text-muted font-semibold tabular-nums">{v}</span>
          </div>
        )
      })}
    </div>
  )
}

export function SectionTitle({ children, action }: { children: ReactNode; action?: ReactNode }) {
  return (
    <div className="flex items-center justify-between mb-3">
      <h4 className="text-[13px] font-semibold text-muted font-sans tracking-normal">{children}</h4>{action}
    </div>
  )
}

export function ThemeToggle({ compact = false }: { compact?: boolean }) {
  const { resolved, toggle } = useTheme()
  return (
    <button onClick={toggle} className={compact ? 'btn-ghost !p-2.5 !rounded-xl' : 'btn-ghost'} aria-label="Toggle light or dark mode" title="Light / dark">
      <Icon name={resolved === 'dark' ? 'sun' : 'moon'} className="w-[18px] h-[18px]" />
      {!compact && <span>{resolved === 'dark' ? 'Light mode' : 'Dark mode'}</span>}
    </button>
  )
}

export function ThemeSegment() {
  const { pref, setPref } = useTheme()
  const opts: { v: ThemePref; icon: string; label: string }[] = [{ v: 'light', icon: 'sun', label: 'Light' }, { v: 'dark', icon: 'moon', label: 'Dark' }, { v: 'system', icon: 'monitor', label: 'Auto' }]
  return (
    <div className="inline-flex p-1 rounded-2xl bg-surface2 border border-line">
      {opts.map(o => (
        <button key={o.v} onClick={() => setPref(o.v)}
          className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-sm font-semibold transition ${pref === o.v ? 'bg-surface shadow-soft text-ink' : 'text-muted hover:text-ink'}`}>
          <Icon name={o.icon} className="w-4 h-4" />{o.label}
        </button>
      ))}
    </div>
  )
}

export function Skeleton({ className }: { className: string }) { return <div className={`skeleton ${className}`} /> }

export function PostSkeleton() {
  return (
    <div className="card p-5 space-y-3">
      <div className="flex gap-3 items-center"><Skeleton className="w-11 h-11 !rounded-full" /><div className="space-y-2 flex-1"><Skeleton className="h-3 w-32" /><Skeleton className="h-3 w-20" /></div></div>
      <Skeleton className="h-4 w-full" /><Skeleton className="h-4 w-4/5" /><Skeleton className="h-36 w-full !rounded-2xl" />
    </div>
  )
}

export function EmptyState({ title, text, action }: { title: string; text: string; action?: ReactNode }) {
  return (
    <div className="card p-10 text-center flex flex-col items-center gap-3">
      <div className="text-5xl">🫧</div><h3 className="text-xl font-bold">{title}</h3><p className="text-muted max-w-sm">{text}</p>{action}
    </div>
  )
}

export function AgentChipLink({ agent }: { agent: Agent }) {
  return (
    <Link to={`/experts/${agent.id}`} className="flex items-center gap-3 px-3 py-2 rounded-xl hover:bg-surface2 text-sm text-muted hover:text-ink transition">
      <AgentAvatar agent={agent} size={28} />{agent.name}
    </Link>
  )
}

export function Toast({ text }: { text: string | null }) {
  if (!text) return null
  return (
    <div className="fixed z-50 left-1/2 -translate-x-1/2 bottom-24 md:bottom-8 animate-rise">
      <div className="px-4 py-3 rounded-2xl bg-ink text-bg font-semibold text-sm shadow-2xl flex items-center gap-2">{text}</div>
    </div>
  )
}
