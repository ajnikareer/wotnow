import { useState } from 'react'
import { AppShell } from '../components/AppShell'
import { Mascot } from '../components/Brand'
import { Skeleton, UserAvatar } from '../components/ui'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'
import type { LeaderRow } from '../lib/types'

type Scope = 'class' | 'school' | 'city'

function Podium({ rows }: { rows: LeaderRow[] }) {
  const [first, second, third] = rows
  const col = (r: LeaderRow | undefined, h: string, place: number) => r && (
    <div className="flex flex-col items-center gap-2 flex-1 min-w-0">
      {place === 1 && <span className="text-2xl animate-bob">👑</span>}
      <UserAvatar emoji={r.avatar} size={place === 1 ? 60 : 50} highlight={place === 1} />
      <div className="text-sm font-bold truncate max-w-full">{r.nickname}</div>
      <div className={`w-full rounded-t-2xl rounded-b-md border grid place-items-center ${h} ${place === 1 ? 'border-brand-violet/40' : 'border-line bg-surface2'}`}
        style={place === 1 ? { background: 'linear-gradient(180deg, rgba(139,92,246,.25), rgb(var(--surface2)))' } : {}}>
        <div className="text-center"><div className="font-display text-3xl font-bold">{place}</div><div className="text-xs text-muted tabular-nums">{r.xp.toLocaleString('en-IN')} XP</div></div>
      </div>
    </div>
  )
  return <div className="flex items-end gap-3 mt-6">{col(second, 'h-28', 2)}{col(first, 'h-36', 1)}{col(third, 'h-24', 3)}</div>
}

function Row({ r }: { r: LeaderRow }) {
  return (
    <div className={`flex items-center gap-3 px-4 py-3 ${r.me ? 'rounded-2xl bg-brand-violet/10 border border-brand-violet/30' : ''}`}>
      <span className="w-7 text-sm font-bold text-muted tabular-nums">{r.rank}</span>
      <UserAvatar emoji={r.avatar} size={36} highlight={r.me} />
      <div className="min-w-0"><div className="font-semibold text-sm truncate">{r.me ? `${r.nickname} (you)` : r.nickname}</div>{r.sub && <div className="text-xs text-muted">{r.sub}</div>}</div>
      <span className="ml-auto text-sm font-semibold text-muted tabular-nums">{r.xp.toLocaleString('en-IN')}</span>
    </div>
  )
}

export default function Leaderboard() {
  const [scope, setScope] = useState<Scope>('class')
  const { data, loading } = useAsync(() => api.leaderboard(scope), [scope])
  return (
    <AppShell>
      <div className="max-w-[640px] mx-auto">
        <div className="flex items-center gap-3"><h1 className="text-3xl font-bold">Leaderboard</h1><span className="chip ml-auto">This week</span></div>
        <div className="inline-flex p-1 rounded-2xl bg-surface2 border border-line mt-4">
          {([['class', 'My class'], ['school', 'My school'], ['city', 'Schools in city']] as [Scope, string][]).map(([s, l]) => (
            <button key={s} onClick={() => setScope(s)} className={`px-4 py-2 rounded-xl text-sm font-bold transition ${scope === s ? 'bg-surface shadow-soft' : 'text-muted'}`}>{l}</button>
          ))}
        </div>
        {loading && !data && <div className="mt-6 space-y-3"><Skeleton className="h-40 w-full" /><Skeleton className="h-12 w-full" /></div>}
        {data && (
          <>
            <Podium rows={data.rows} />
            <div className="card p-2 mt-1">{data.rows.slice(3).map(r => <Row key={r.rank} r={r} />)}
              {!data.rows.some(r => r.me) && <><div className="text-center text-muted text-xs py-1">⋯</div><Row r={data.me} /></>}</div>
            {data.teams && (
              <div className="card p-5 mt-5">
                <h3 className="font-bold text-lg">🏆 Class vs class</h3>
                <p className="text-sm text-muted">Every answer you give adds to your class team.</p>
                <div className="mt-2">{data.teams.map(t => <Row key={t.rank} r={t} />)}</div>
              </div>
            )}
            <div className="flex items-center gap-3 mt-5 p-4 rounded-2xl grad-soft border border-line text-sm">
              <Mascot mood="happy" size={44} /><span>Leaderboards show <b>nicknames only</b>. Answer daily to climb, and keep your streak alive!</span>
            </div>
          </>
        )}
      </div>
    </AppShell>
  )
}
