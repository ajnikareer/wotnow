import { useState } from 'react'
import { AppShell } from '../components/AppShell'
import { Mascot } from '../components/Brand'
import { Skeleton, UserAvatar } from '../components/ui'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'
import { Link } from '../lib/router'
import type { LeaderRow } from '../lib/types'

type Scope = 'global' | 'country' | 'city'

function countryFlag(country?: string): string {
  if (!country) return '🇮🇳'
  const c = country.toLowerCase().trim()
  if (c.includes('india') || c === 'in') return '🇮🇳'
  if (c.includes('united states') || c === 'usa' || c === 'us') return '🇺🇸'
  if (c.includes('united kingdom') || c === 'uk' || c.includes('britain') || c.includes('england')) return '🇬🇧'
  if (c.includes('canada')) return '🇨🇦'
  if (c.includes('australia')) return '🇦🇺'
  if (c.includes('singapore')) return '🇸🇬'
  if (c.includes('emirates') || c === 'uae') return '🇦🇪'
  if (c.includes('germany')) return '🇩🇪'
  if (c.includes('france')) return '🇫🇷'
  if (c.includes('japan')) return '🇯🇵'
  return '🌍'
}

function Podium({ rows }: { rows: LeaderRow[] }) {
  if (!rows || rows.length === 0) return null
  const count = Math.min(rows.length, 3)
  const first = rows[0]
  const second = count >= 2 ? rows[1] : undefined
  const third = count >= 3 ? rows[2] : undefined

  const col = (r: LeaderRow | undefined, h: string, place: number) => r && (
    <div key={r.nickname} className="flex flex-col items-center gap-2 flex-1 min-w-0">
      {place === 1 && <span className="text-2xl animate-bob">👑</span>}
      <UserAvatar emoji={r.avatar} size={place === 1 ? 60 : 48} highlight={place === 1 || r.me} />
      <div className="text-sm font-bold truncate max-w-full text-center">
        {r.me ? `${r.nickname} (you)` : r.nickname}
      </div>
      {r.sub && <div className="text-[11px] text-muted truncate max-w-full text-center">{r.sub}</div>}
      <div className={`w-full rounded-t-2xl rounded-b-md border grid place-items-center ${h} ${place === 1 ? 'border-brand-violet/40' : 'border-line bg-surface2'}`}
        style={place === 1 ? { background: 'linear-gradient(180deg, rgba(139,92,246,.25), rgb(var(--surface2)))' } : {}}>
        <div className="text-center px-1">
          <div className="font-display text-2xl md:text-3xl font-bold">{place}</div>
          <div className="text-xs text-muted tabular-nums">{r.xp.toLocaleString('en-IN')} XP</div>
        </div>
      </div>
    </div>
  )

  if (count === 1) {
    return (
      <div className="flex justify-center mt-6">
        <div className="w-44">{col(first, 'h-36', 1)}</div>
      </div>
    )
  }

  return (
    <div className="flex items-end justify-center gap-3 mt-6">
      {second && col(second, 'h-28', 2)}
      {col(first, 'h-36', 1)}
      {third && col(third, 'h-24', 3)}
    </div>
  )
}

function Row({ r }: { r: LeaderRow }) {
  return (
    <div className={`flex items-center gap-3 px-4 py-3 rounded-xl transition ${r.me ? 'bg-brand-violet/10 border border-brand-violet/30' : 'hover:bg-surface2/50'}`}>
      <span className="w-7 text-sm font-bold text-muted tabular-nums">#{r.rank}</span>
      <UserAvatar emoji={r.avatar} size={36} highlight={r.me} />
      <div className="min-w-0 flex-1">
        <div className="font-semibold text-sm truncate">{r.me ? `${r.nickname} (you)` : r.nickname}</div>
        {r.sub && <div className="text-xs text-muted truncate">{r.sub}</div>}
      </div>
      <span className="ml-auto text-sm font-semibold text-muted tabular-nums">{r.xp.toLocaleString('en-IN')} XP</span>
    </div>
  )
}

export default function Leaderboard() {
  const [scope, setScope] = useState<Scope>('global')
  const { data, loading } = useAsync(() => api.leaderboard(scope), [scope])

  const tabs: [Scope, string, string][] = [
    ['global', 'Global', '🌍'],
    ['country', data?.myCountry || 'Country', countryFlag(data?.myCountry)],
    ['city', data?.myCity || 'City', '📍'],
  ]

  const podiumCount = data?.rows ? Math.min(data.rows.length, 3) : 0
  const remainingRows = data?.rows ? data.rows.slice(podiumCount) : []
  const userInPodium = data?.rows ? data.rows.slice(0, podiumCount).some(r => r.me) : false
  const userInRemaining = remainingRows.some(r => r.me)

  return (
    <AppShell>
      <div className="max-w-[640px] mx-auto">
        <div className="flex items-center gap-3">
          <div>
            <h1 className="text-3xl font-bold">Leaderboard</h1>
            <p className="text-xs text-muted mt-0.5">Real learners climbing through daily safety smarts</p>
          </div>
          {data?.totalLearners !== undefined && (
            <span className="chip ml-auto text-xs">{data.totalLearners} {data.totalLearners === 1 ? 'learner' : 'learners'}</span>
          )}
        </div>

        {/* Global / Country / City tabs */}
        <div className="inline-flex p-1 rounded-2xl bg-surface2 border border-line mt-4 w-full sm:w-auto">
          {tabs.map(([s, label, icon]) => (
            <button
              key={s}
              onClick={() => setScope(s)}
              className={`flex-1 sm:flex-initial px-4 py-2 rounded-xl text-sm font-bold transition flex items-center justify-center gap-1.5 ${
                scope === s ? 'bg-surface shadow-soft text-ink' : 'text-muted hover:text-ink'
              }`}
            >
              <span>{icon}</span>
              <span>{label}</span>
            </button>
          ))}
        </div>

        {loading && !data && (
          <div className="mt-6 space-y-3">
            <Skeleton className="h-40 w-full" />
            <Skeleton className="h-12 w-full" />
          </div>
        )}

        {data && (
          <>
            {data.rows.length === 0 ? (
              <div className="card p-8 mt-6 text-center">
                <div className="text-4xl mb-2">🌟</div>
                <div className="font-bold text-lg">
                  Be the first on the {scope === 'city' ? data.myCity : (scope === 'country' ? data.myCountry : 'Global')} board!
                </div>
                <p className="text-sm text-muted mt-1 max-w-sm mx-auto">
                  Answer scenarios and quizzes from our 8 safety experts to earn points and claim rank #1.
                </p>
                <div className="mt-4">
                  <Link to="/feed" className="btn-grad inline-flex items-center gap-2">
                    Go to Feed →
                  </Link>
                </div>
              </div>
            ) : (
              <>
                <Podium rows={data.rows} />

                {remainingRows.length > 0 && (
                  <div className="card p-2 mt-4 space-y-1">
                    {remainingRows.map(r => (
                      <Row key={`${r.rank}-${r.nickname}`} r={r} />
                    ))}
                  </div>
                )}

                {/* Show user's row if they are not in the podium and not in remaining rows */}
                {!userInPodium && !userInRemaining && data.me && (
                  <div className="card p-2 mt-3">
                    <div className="text-center text-muted text-xs py-0.5">⋯</div>
                    <Row r={data.me} />
                  </div>
                )}
              </>
            )}

            <div className="flex items-center gap-3 mt-6 p-4 rounded-2xl grad-soft border border-line text-sm">
              <Mascot mood="happy" size={44} />
              <span className="text-xs text-muted">
                Leaderboards show <b>nicknames only</b>. Real learners only — answer daily to climb and keep your streak alive!
              </span>
            </div>
          </>
        )}
      </div>
    </AppShell>
  )
}
