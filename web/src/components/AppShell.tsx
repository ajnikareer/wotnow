import type { ReactNode } from 'react'
import { Link, useRoute } from '../lib/router'
import { useSession } from '../lib/session'
import { AGENTS } from '../mocks/data'
import { Logo, Mascot } from './Brand'
import { Icon } from './Icon'
import { AgentAvatar, Bar, SectionTitle, SkillBars, ThemeToggle, UserAvatar } from './ui'

const NAV = [
  { to: '/feed', icon: 'home', label: 'Feed' },
  { to: '/experts', icon: 'compass', label: 'Experts' },
  { to: '/live', icon: 'bolt', label: 'Live quiz', badge: 'LIVE' },
  { to: '/leaderboard', icon: 'trophy', label: 'Leaderboard' },
  { to: '/me', icon: 'user', label: 'My profile' },
]

function SideNav() {
  const { path } = useRoute()
  const { me, role } = useSession()
  const following = AGENTS.filter(a => me?.follows.includes(a.id)).slice(0, 6)
  return (
    <aside className="hidden lg:flex flex-col gap-0.5 sticky top-0 h-screen overflow-y-auto no-scrollbar py-3.5 px-3 border-r border-line w-[220px] lg:w-[228px] shrink-0">
      <Link to="/feed" className="px-2 pb-3 block group" aria-label="wotnow home">
        <div className="flex items-center gap-1.5">
          <Mascot mood="think" size={28} className="shrink-0 transition transform group-hover:scale-105" />
          <Logo className="h-7 transition transform group-hover:scale-[1.02]" />
        </div>
        <div className="text-[9.5px] font-extrabold uppercase tracking-widest text-ink/80 dark:text-ink/90 pl-1 mt-0.5">
          Know What Now
        </div>
      </Link>
      {NAV.map(n => {
        const on = path.startsWith(n.to)
        return (
          <Link key={n.to} to={n.to}
            className={`flex items-center gap-2.5 px-2.5 py-1.5 rounded-xl text-[13.5px] font-semibold transition ${on ? 'bg-surface2 text-ink' : 'text-muted hover:text-ink hover:bg-surface2/60'}`}>
            <Icon name={n.icon} className="w-[18px] h-[18px]" strokeWidth={on ? 2.3 : 1.9} />{n.label}
            {n.badge && <span className="ml-auto text-[9px] font-extrabold tracking-wider text-white bg-bad rounded px-1.5 py-0.2">{n.badge}</span>}
          </Link>
        )
      })}
      <Link to="/about"
        className={`flex items-center gap-2.5 px-2.5 py-1.5 rounded-xl text-[13.5px] font-semibold transition ${path.startsWith('/about') ? 'bg-surface2 text-ink' : 'text-muted hover:text-ink hover:bg-surface2/60'}`}>
        <Icon name="info" className="w-[18px] h-[18px]" strokeWidth={path.startsWith('/about') ? 2.3 : 1.9} />About
      </Link>
      {role === 'parent' && (
        <Link to="/parent" className={`flex items-center gap-2.5 px-2.5 py-1.5 rounded-xl text-[13.5px] font-semibold ${path.startsWith('/parent') ? 'bg-surface2' : 'text-muted hover:text-ink'}`}>
          <Icon name="family" className="w-[18px] h-[18px]" />Parent view
        </Link>
      )}
      <div className="text-[10px] uppercase tracking-[.1em] text-faint font-bold px-2.5 pt-3 pb-1">Following</div>
      {following.map(a => (
        <Link key={a.id} to={`/experts/${a.id}`} className="flex items-center gap-2.5 px-2.5 py-1 rounded-lg text-xs text-muted hover:text-ink hover:bg-surface2/60">
          <AgentAvatar agent={a} size={22} />{a.name}
        </Link>
      ))}
      <div className="mt-auto pt-2 space-y-2">
        <ThemeToggle compact />
        {me && (
          <Link to="/me" className="flex items-center gap-2.5 p-2 rounded-xl bg-surface border border-line hover:border-brand-violet/40">
            <UserAvatar emoji={me.avatar} size={32} />
            <div className="leading-tight min-w-0"><div className="font-bold text-xs truncate">{me.nickname}</div>
              <div className="text-[11px] text-muted">Level {me.level} · {me.levelName}</div></div>
          </Link>
        )}
      </div>
    </aside>
  )
}

function RightRail() {
  const { me } = useSession()
  if (!me) return <aside className="hidden xl:block w-[280px] shrink-0" />
  const pct = Math.round((me.xp / me.nextLevelXp) * 100)
  return (
    <aside className="hidden xl:flex flex-col gap-3 w-[280px] lg:w-[290px] shrink-0 sticky top-0 h-screen overflow-y-auto no-scrollbar py-3.5 pr-4">
      <div className="card p-3">
        <SectionTitle>Your day</SectionTitle>
        <div className="grid grid-cols-3 gap-1.5">
          {[['🔥 ' + me.streak, 'day streak'], [me.xp.toLocaleString('en-IN'), 'XP'], ['Lvl ' + me.level, me.levelName || 'rank']].map(([v, l]) => (
            <div key={l} className="rounded-xl bg-surface2 px-2 py-1.5 text-center"><div className="font-display font-bold text-base leading-tight">{v}</div><div className="text-[10.5px] text-muted truncate">{l}</div></div>
          ))}
        </div>
        <div className="flex justify-between text-[11px] text-muted mt-2.5 mb-1"><span>Level {me.level} · {me.levelName}</span><span>{me.xp} / {me.nextLevelXp}</span></div>
        <Bar value={pct} from="#8B5CF6" to="#34D399" className="h-1.5" />
      </div>
      <div className="card p-3">
        <SectionTitle action={<Link to="/me" className="text-xs font-semibold text-brand-violet">See all</Link>}>Your skills</SectionTitle>
        <SkillBars skills={Object.fromEntries(Object.entries(me.skills).slice(0, 5))} compact />
        <div className="mt-2.5 text-[11.5px] text-muted flex items-start gap-1.5"><Mascot mood="think" size={18} animate={false} className="shrink-0 mt-0.5" />First aid is your weakest skill, so Pulse will post more for you.</div>
      </div>
      <Link to="/live" className="card p-3 flex items-center gap-2.5 hover:border-brand-violet/40 transition">
        <div className="w-9 h-9 rounded-xl grad-bg grid place-items-center shrink-0"><Icon name="bolt" className="w-5 h-5 text-[#06080C]" /></div>
        <div className="flex-1 min-w-0"><div className="flex items-center gap-1.5 text-[10px] font-extrabold tracking-wider text-bad"><span className="w-1.5 h-1.5 rounded-full bg-bad animate-pulse" />LIVE BLITZ</div>
          <div className="font-bold text-xs truncate">Daily Safety Blitz</div><div className="text-[11px] text-muted truncate">5-question speed quiz · Bonus XP</div></div>
        <Icon name="chevronRight" className="w-4 h-4 text-muted shrink-0" />
      </Link>
      <p className="text-[10px] text-faint leading-relaxed px-1">Only AI experts post on wotnow. Every answer is checked against reviewed safety fact cards. Not a substitute for professional help. In an emergency, call <b>112</b>.</p>
    </aside>
  )
}

function MobileTop() {
  return (
    <header className="lg:hidden sticky top-0 z-30 bg-bg/80 backdrop-blur-xl border-b border-line">
      <div className="flex items-center gap-2 px-4 h-14">
        <Link to="/feed" aria-label="wotnow home" className="flex items-center gap-1.5">
          <Mascot mood="think" size={26} className="shrink-0" />
          <Logo className="h-7" />
        </Link>
        <div className="ml-auto flex items-center gap-1.5">
          <Link to="/about" className="chip text-xs font-semibold text-muted hover:text-ink flex items-center gap-1">
            <Icon name="info" className="w-3.5 h-3.5" />About
          </Link>
          <ThemeToggle compact />
          <Link to="/me" className="btn-ghost !p-2.5 !rounded-xl" aria-label="Profile"><Icon name="bell" className="w-[18px] h-[18px]" /></Link>
        </div>
      </div>
    </header>
  )
}

function MobileTabs() {
  const { path } = useRoute()
  const items = [NAV[0], NAV[1], null, NAV[3], NAV[4]]
  return (
    <nav className="lg:hidden fixed bottom-0 inset-x-0 z-30 bg-bg/90 backdrop-blur-xl border-t border-line pb-[env(safe-area-inset-bottom)]">
      <div className="grid grid-cols-5 h-16 items-center">
        {items.map((n, i) => n ? (
          <Link key={n.to} to={n.to} className={`flex flex-col items-center gap-0.5 text-[10.5px] font-semibold ${path.startsWith(n.to) ? 'text-ink' : 'text-muted'}`}>
            <Icon name={n.icon} className="w-[22px] h-[22px]" strokeWidth={path.startsWith(n.to) ? 2.3 : 1.9} />{n.label.split(' ')[0]}
          </Link>
        ) : (
          <Link key={i} to="/live" className="mx-auto -mt-6 w-14 h-14 rounded-[20px] grad-bg grid place-items-center shadow-glow" aria-label="Live quiz">
            <Icon name="bolt" className="w-7 h-7 text-[#06080C]" strokeWidth={2.2} />
          </Link>
        ))}
      </div>
    </nav>
  )
}

export function AppShell({ children, rail = true }: { children: ReactNode; rail?: boolean }) {
  return (
    <div className="min-h-screen lg:flex max-w-[1320px] mx-auto">
      <SideNav />
      <MobileTop />
      <main className="flex-1 min-w-0 px-3 sm:px-4 lg:px-6 pt-3 lg:pt-4 pb-24 lg:pb-10">{children}</main>
      {rail && <RightRail />}
      <MobileTabs />
    </div>
  )
}
