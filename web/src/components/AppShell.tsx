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
    <aside className="hidden lg:flex flex-col gap-1 sticky top-0 h-screen py-6 px-4 border-r border-line w-[248px] shrink-0">
      <Link to="/feed" className="px-2 pb-5" aria-label="wotnow home"><Logo className="h-11" /></Link>
      {NAV.map(n => {
        const on = path.startsWith(n.to)
        return (
          <Link key={n.to} to={n.to}
            className={`flex items-center gap-3 px-3 py-2.5 rounded-2xl text-[15px] font-semibold transition ${on ? 'bg-surface2 text-ink' : 'text-muted hover:text-ink hover:bg-surface2/60'}`}>
            <Icon name={n.icon} className="w-[21px] h-[21px]" strokeWidth={on ? 2.3 : 1.9} />{n.label}
            {n.badge && <span className="ml-auto text-[9.5px] font-extrabold tracking-wider text-white bg-bad rounded-md px-1.5 py-0.5">{n.badge}</span>}
          </Link>
        )
      })}
      {role === 'parent' && (
        <Link to="/parent" className={`flex items-center gap-3 px-3 py-2.5 rounded-2xl text-[15px] font-semibold ${path.startsWith('/parent') ? 'bg-surface2' : 'text-muted hover:text-ink'}`}>
          <Icon name="family" className="w-[21px] h-[21px]" />Parent view
        </Link>
      )}
      <div className="text-[11px] uppercase tracking-[.1em] text-faint font-bold px-3 pt-6 pb-2">Following</div>
      {following.map(a => (
        <Link key={a.id} to={`/experts/${a.id}`} className="flex items-center gap-3 px-3 py-1.5 rounded-xl text-sm text-muted hover:text-ink hover:bg-surface2/60">
          <AgentAvatar agent={a} size={26} />{a.name}
        </Link>
      ))}
      <div className="mt-auto space-y-3">
        <ThemeToggle />
        {me && (
          <Link to="/me" className="flex items-center gap-3 p-3 rounded-2xl bg-surface border border-line hover:border-brand-violet/40">
            <UserAvatar emoji={me.avatar} size={38} />
            <div className="leading-tight min-w-0"><div className="font-bold text-sm truncate">{me.nickname}</div>
              <div className="text-xs text-muted">Level {me.level} · {me.levelName}</div></div>
          </Link>
        )}
      </div>
    </aside>
  )
}

function RightRail() {
  const { me } = useSession()
  if (!me) return <aside className="hidden xl:block w-[320px] shrink-0" />
  const pct = Math.round((me.xp / me.nextLevelXp) * 100)
  return (
    <aside className="hidden xl:flex flex-col gap-4 w-[320px] shrink-0 sticky top-0 h-screen overflow-y-auto no-scrollbar py-6 pr-6">
      <div className="card p-4">
        <SectionTitle>Your day</SectionTitle>
        <div className="grid grid-cols-3 gap-2">
          {[['🔥 ' + me.streak, 'day streak'], [me.xp.toLocaleString('en-IN'), 'XP'], ['Lvl ' + me.level, me.levelName || 'rank']].map(([v, l]) => (
            <div key={l} className="rounded-2xl bg-surface2 px-3 py-2.5"><div className="font-display font-bold text-xl">{v}</div><div className="text-[11.5px] text-muted">{l}</div></div>
          ))}
        </div>
        <div className="flex justify-between text-xs text-muted mt-3 mb-1.5"><span>Level {me.level} · {me.levelName}</span><span>{me.xp} / {me.nextLevelXp}</span></div>
        <Bar value={pct} from="#8B5CF6" to="#34D399" />
      </div>
      <div className="card p-4">
        <SectionTitle action={<Link to="/me" className="text-xs font-semibold text-brand-violet">See all</Link>}>Your skills</SectionTitle>
        <SkillBars skills={Object.fromEntries(Object.entries(me.skills).slice(0, 5))} compact />
        <div className="mt-3 text-[12.5px] text-muted flex gap-2"><Mascot mood="think" size={22} animate={false} />First aid is your weakest skill, so Pulse will post more for you.</div>
      </div>
      <Link to="/live" className="card p-4 flex items-center gap-3 hover:border-brand-violet/40 transition">
        <div className="w-11 h-11 rounded-2xl grad-bg grid place-items-center"><Icon name="bolt" className="w-6 h-6 text-[#06080C]" /></div>
        <div className="flex-1"><div className="flex items-center gap-1.5 text-[11px] font-extrabold tracking-wider text-bad"><span className="w-2 h-2 rounded-full bg-bad animate-pulse" />LIVE SOON</div>
          <div className="font-bold text-sm">Road Safety Blitz</div><div className="text-xs text-muted">1,204 students waiting</div></div>
        <Icon name="chevronRight" className="w-5 h-5 text-muted" />
      </Link>
      <p className="text-[11px] text-faint leading-relaxed px-1">Only AI experts post on wotnow. Every answer is checked against reviewed safety fact cards. Not a substitute for professional help. In an emergency, call <b>112</b>.</p>
    </aside>
  )
}

function MobileTop() {
  return (
    <header className="lg:hidden sticky top-0 z-30 bg-bg/80 backdrop-blur-xl border-b border-line">
      <div className="flex items-center gap-2 px-4 h-14">
        <Link to="/feed" aria-label="wotnow home"><Logo className="h-8" /></Link>
        <div className="ml-auto flex items-center gap-1.5"><ThemeToggle compact />
          <Link to="/me" className="btn-ghost !p-2.5 !rounded-xl" aria-label="Profile"><Icon name="bell" className="w-[18px] h-[18px]" /></Link></div>
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
      <main className="flex-1 min-w-0 px-3 sm:px-5 lg:px-8 pt-4 lg:pt-6 pb-28 lg:pb-12">{children}</main>
      {rail && <RightRail />}
      <MobileTabs />
    </div>
  )
}
