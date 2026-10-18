import { AppShell } from '../components/AppShell'
import { Mascot } from '../components/Brand'
import { Icon } from '../components/Icon'
import { Bar, SkillBars, ThemeSegment, UserAvatar } from '../components/ui'
import { api } from '../lib/api'
import { navigate } from '../lib/router'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'

export default function Profile() {
  const { me, signOut, refreshMe } = useSession()
  const toast = useToast()
  if (!me) return <AppShell><div className="max-w-[680px] mx-auto"><div className="skeleton h-48" /></div></AppShell>
  const pct = Math.round((me.xp / me.nextLevelXp) * 100)
  return (
    <AppShell>
      <div className="max-w-[680px] mx-auto space-y-5">
        <div className="card p-5 md:p-6">
          <div className="flex items-center gap-4">
            <div className="rounded-full p-[3px] grad-bg"><div className="rounded-full bg-surface p-1"><UserAvatar emoji={me.avatar} size={72} /></div></div>
            <div className="min-w-0"><h1 className="text-2xl md:text-3xl font-bold truncate">{me.nickname}</h1>
              <div className="text-sm text-muted">Class {me.grade} · {me.city}{me.country ? `, ${me.country}` : ''}</div></div>
            <div className="ml-auto text-right hidden sm:block"><div className="font-display text-3xl font-bold grad-text">Level {me.level}</div><div className="text-sm text-muted">{me.levelName}</div></div>
          </div>
          <div className="flex justify-between text-sm text-muted mt-5 mb-1.5"><span>{me.xp.toLocaleString('en-IN')} XP</span><span>{me.nextLevelXp - me.xp} XP to Level {me.level + 1}</span></div>
          <Bar value={pct} className="h-2.5" from="#8B5CF6" to="#34D399" />
          <div className="grid grid-cols-3 gap-2 mt-5">
            {[['🔥 ' + me.streak, 'day streak'], [String(me.answers), 'answers'], [String(me.avgScore), 'avg score']].map(([v, l]) => (
              <div key={l} className="rounded-2xl bg-surface2 p-3 text-center"><div className="font-display text-2xl font-bold">{v}</div><div className="text-xs text-muted">{l}</div></div>
            ))}
          </div>
        </div>

        <div className="card p-5 md:p-6"><h2 className="text-lg font-bold mb-4">Skill profile</h2><SkillBars skills={me.skills} />
          <div className="mt-4 flex gap-3 items-center p-3 rounded-2xl bg-surface2 text-sm"><Mascot mood="think" size={36} />Tip: answer 3 first-aid posts this week to level up your weakest skill.</div></div>

        <div className="card p-5 md:p-6"><h2 className="text-lg font-bold mb-4">Badges</h2>
          <div className="grid grid-cols-4 gap-2.5">
            {me.badges.map(b => (
              <div key={b.id} className={`rounded-2xl border border-line p-3 text-center ${b.earned ? 'bg-surface2' : 'opacity-40 grayscale'}`}>
                <div className="text-3xl">{b.emoji}</div><div className="text-[11.5px] font-semibold mt-1 leading-tight">{b.name}</div></div>
            ))}
          </div></div>

        <div className="card p-5 md:p-6 space-y-5">
          <h2 className="text-lg font-bold">Settings</h2>
          <div className="flex flex-wrap items-center gap-3"><div className="flex-1 min-w-[160px]"><div className="font-semibold">Appearance</div><div className="text-sm text-muted">Light, dark or match your device</div></div><ThemeSegment /></div>
          <div className="flex items-center gap-3 p-4 rounded-2xl bg-surface2 text-sm"><Icon name="lock" className="w-5 h-5 text-muted" />Time limits, topics and privacy are managed by your parent.</div>
          <div className="flex flex-wrap gap-2">
            <button className="btn-ghost" onClick={() => navigate('/about')}><Icon name="info" className="w-4 h-4" />About WotNow</button>
            <button className="btn-ghost" onClick={() => { api.reset(); refreshMe(); toast('Demo data reset ✨') }}>Reset demo data</button>
            <button className="btn-ghost text-bad" onClick={() => { signOut(); navigate('/') }}><Icon name="logout" className="w-4 h-4" />Sign out</button>
          </div>
        </div>
      </div>
    </AppShell>
  )
}
