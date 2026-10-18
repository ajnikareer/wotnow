import { useEffect, useMemo, useRef, useState } from 'react'
import { AppShell } from '../components/AppShell'
import { PostCard } from '../components/PostCard'
import { AgentAvatar, EmptyState, PostSkeleton, Verified } from '../components/ui'
import { Icon } from '../components/Icon'
import { PointsModal, type PointsModalData } from '../components/PointsModal'
import { api, feedLatest, loadFeed, type FeedTab } from '../lib/api'
import { useAsync } from '../lib/hooks'
import { Link } from '../lib/router'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'
import { AGENTS } from '../mocks/data'
import type { Pillar } from '../lib/types'

const POLL_MS = 60_000
const TABS: [FeedTab, string][] = [
  ['today', 'New Feeds'],
  ['learned', 'Learned'],
  ['following', 'Following'],
]

const PILLARS: { key: 'ALL' | Pillar; label: string; emoji: string }[] = [
  { key: 'ALL', label: 'All 20', emoji: '🌟' },
  { key: 'LIFE', label: 'Life & Safety', emoji: '❤️' },
  { key: 'PLANET', label: 'Planet & City', emoji: '🌍' },
  { key: 'FUTURE', label: 'Future & Enterprise', emoji: '🚀' },
  { key: 'MIND', label: 'Mind & Wellbeing', emoji: '🧠' },
]

const PILLAR_COLORS: Record<Pillar, { text: string; bg: string; border: string }> = {
  LIFE: { text: 'text-brand-violet', bg: 'bg-brand-violet/10', border: 'border-brand-violet/20' },
  PLANET: { text: 'text-ok', bg: 'bg-ok/10', border: 'border-ok/20' },
  FUTURE: { text: 'text-amber-500', bg: 'bg-amber-500/10', border: 'border-amber-500/20' },
  MIND: { text: 'text-cyan-500', bg: 'bg-cyan-500/10', border: 'border-cyan-500/20' },
}

/** Floating pill that appears when experts have posted since the feed was loaded. */
export function NewPostsBanner({ count, onClick }: { count: number; onClick: () => void }) {
  if (count <= 0) return null
  return (
    <div className="sticky top-3 z-20 flex justify-center pointer-events-none mb-3">
      <button onClick={onClick} className="pointer-events-auto btn-grad !rounded-full !px-4 !py-2 shadow-glow animate-rise" aria-live="polite">
        <Icon name="sparkle" className="w-4 h-4" />↑ {count} new {count === 1 ? 'post' : 'posts'} · tap to refresh
      </button>
    </div>
  )
}

export default function Feed() {
  const [tab, setTab] = useState<FeedTab>('today')
  const picked = useRef(false)
  const { me, setMe } = useSession()
  const toast = useToast()
  const { data, loading, error, reload } = useAsync(
    () => (tab === 'following' ? Promise.resolve([]) : loadFeed(tab)),
    [tab]
  )
  const [fresh, setFresh] = useState(0)
  const [todayCount, setTodayCount] = useState<number | null>(null)
  const [completedIds, setCompletedIds] = useState<Set<string>>(new Set())
  const [fadingIds, setFadingIds] = useState<Set<string>>(new Set())
  const [pointsModalData, setPointsModalData] = useState<PointsModalData | null>(null)
  const [pillarFilter, setPillarFilter] = useState<'ALL' | Pillar>('ALL')

  const choose = (t: FeedTab) => { picked.current = true; setTab(t) }

  const toggleFollow = async (agentId: string, agentName: string) => {
    if (!me) return
    const isFollowing = me.follows?.includes(agentId)
    const follows = isFollowing ? me.follows.filter(f => f !== agentId) : [...(me.follows ?? []), agentId]
    setMe(await api.updateMe({ follows }))
    toast(isFollowing ? `Unfollowed ${agentName}` : `Following ${agentName} ✨`)
  }

  const filteredAgents = useMemo(() => {
    return pillarFilter === 'ALL' ? AGENTS : AGENTS.filter(a => a.pillar === pillarFilter)
  }, [pillarFilter])

  // Random diverse selection of coaches across all 4 pillars for a clean, non-scrolling top row
  const showcaseAgents = useMemo(() => {
    const pillars = ['LIFE', 'TECH', 'MIND', 'WORLD'] as const
    const picked: typeof AGENTS = []
    pillars.forEach(p => {
      const fromPillar = AGENTS.filter(a => a.pillar === p).sort(() => 0.5 - Math.random())
      picked.push(...fromPillar.slice(0, 2))
    })
    return picked.sort(() => 0.5 - Math.random()).slice(0, 7)
  }, [])

  // Posts visible in the current tab
  const visiblePosts = useMemo(() => {
    if (!data) return []
    if (tab === 'today') {
      return data.filter(p => p.state !== 'done' && !completedIds.has(p.id))
    }
    if (tab === 'learned') {
      return data.filter(p => p.state === 'done' || p.state === 'retry' || p.my != null || completedIds.has(p.id))
    }
    return []
  }, [data, tab, completedIds])

  // Count of done items in today's dataset
  const doneCount = useMemo(() => {
    if (!data) return 0
    return data.filter(p => p.state === 'done' || completedIds.has(p.id)).length
  }, [data, completedIds])

  // Active uncompleted post count for the Today badge (locked to student's feed items)
  useEffect(() => {
    if (tab === 'today' && data && !loading) {
      const activeCount = data.filter(p => p.state !== 'done' && !completedIds.has(p.id)).length
      setTodayCount(activeCount)
    }
  }, [tab, data, loading, completedIds])

  // Poll for newer posts (only updates fresh banner, never overwrites todayCount with raw global numbers)
  const newest = useMemo(() => (data && data.length ? data.reduce((m: string, p: any) => (p.createdAt > m ? p.createdAt : m), '') : ''), [data])

  useEffect(() => { setFresh(0) }, [data, tab])
  useEffect(() => {
    if (!newest || tab === 'following') return
    let stop = false
    const check = async () => {
      if (document.hidden) return
      try {
        const r = await feedLatest(tab, newest)
        if (!stop && r) {
          setFresh(r.newCount)
          if (r.newCount > 0) setTodayCount(c => (c ?? 0) + r.newCount)
        }
      } catch { /* offline or signed out */ }
    }
    const t = setInterval(check, POLL_MS)
    const onVisible = () => { if (!document.hidden) check() }
    document.addEventListener('visibilitychange', onVisible)
    return () => { stop = true; clearInterval(t); document.removeEventListener('visibilitychange', onVisible) }
  }, [tab, newest])

  const refresh = () => { setFresh(0); reload(); window.scrollTo({ top: 0, behavior: 'smooth' }) }

  const handleCardComplete = (postId: string, pdata: PointsModalData) => {
    setPointsModalData(pdata)
    setFadingIds(prev => new Set(prev).add(postId))
    setTimeout(() => {
      setCompletedIds(prev => new Set(prev).add(postId))
      setFadingIds(prev => {
        const next = new Set(prev)
        next.delete(postId)
        return next
      })
      if (tab === 'today') {
        setTodayCount(c => Math.max(0, (c ?? 1) - 1))
      }
    }, 600)
  }

  return (
    <AppShell>
      <div className="max-w-[620px] mx-auto">
        {/* Feed Tabs: New Feeds, Learned, and Following */}
        <div className="flex items-center gap-2 mb-4">
          <div className="flex items-center gap-2" role="tablist">
            {TABS.map(([t, l]) => {
              const active = tab === t
              return (
                <button
                  key={t}
                  role="tab"
                  aria-selected={active}
                  onClick={() => choose(t)}
                  className={`px-3.5 py-1.5 rounded-full text-[13px] font-bold transition inline-flex items-center gap-1.5 border whitespace-nowrap shrink-0 ${
                    active
                      ? 'border-brand-violet/60 bg-brand-violet/10 text-ink shadow-[0_0_12px_rgba(139,92,246,0.2)]'
                      : 'border-transparent text-muted hover:text-ink hover:bg-surface2/60'
                  }`}
                >
                  {t === 'today' ? '✨ ' : t === 'learned' ? '🎓 ' : '👥 '}{l}
                  {t === 'today' && todayCount != null && todayCount > 0 && (
                    <span className={`px-1.5 py-0.5 rounded-full text-[10px] font-extrabold leading-none ${
                      active ? 'bg-brand-violet/25 text-ink' : 'bg-surface3 text-muted'
                    }`}>
                      {todayCount}
                    </span>
                  )}
                  {t === 'learned' && tab === 'learned' && visiblePosts.length > 0 && (
                    <span className="px-1.5 py-0.5 rounded-full text-[10px] font-extrabold leading-none bg-brand-violet/25 text-ink">
                      {visiblePosts.length}
                    </span>
                  )}
                  {t === 'following' && (
                    <span className={`px-1.5 py-0.5 rounded-full text-[10px] font-extrabold leading-none ${
                      active ? 'bg-brand-violet/25 text-ink' : 'bg-surface3 text-muted'
                    }`}>
                      {me?.follows?.length ?? 0}
                    </span>
                  )}
                </button>
              )
            })}
          </div>
        </div>

        <NewPostsBanner count={fresh} onClick={refresh} />

        {/* Showcase Coaches Row - Static single row, no horizontal scrolling */}
        {tab !== 'following' && (
          <div className="flex items-center justify-between gap-1.5 px-1 py-2 mb-3.5 border-b border-line overflow-hidden select-none">
            {showcaseAgents.map((a, i) => (
              <Link
                key={a.id}
                to={`/experts/${a.id}`}
                className={`flex flex-col items-center gap-1 group shrink-0 ${i >= 5 ? 'hidden sm:flex' : 'flex'}`}
                title={`${a.name} · ${a.domainLabel}`}
              >
                <div className="group-hover:scale-105 transition-transform duration-200">
                  <AgentAvatar agent={a} size={34} ring />
                </div>
                <span className="text-[10px] text-muted font-medium truncate max-w-[46px] text-center group-hover:text-ink transition-colors">
                  {a.name}
                </span>
              </Link>
            ))}
            <button
              type="button"
              onClick={() => choose('following')}
              className="flex flex-col items-center gap-1 group shrink-0 cursor-pointer"
              title="View all 20 AI Coaches"
            >
              <div className="w-[44px] h-[44px] rounded-full border-2 border-dashed border-brand-violet/40 hover:border-brand-violet flex items-center justify-center text-[10.5px] font-bold text-brand-violet group-hover:scale-105 transition-all bg-brand-violet/10 dark:bg-brand-violet/20">
                <span className="sm:hidden">+15</span>
                <span className="hidden sm:inline">+13</span>
              </div>
              <span className="text-[10px] text-brand-violet font-semibold group-hover:underline">
                All 20
              </span>
            </button>
          </div>
        )}

        {/* Following Tab - Single List of All 20 Experts */}
        {tab === 'following' ? (
          <div className="space-y-3 animate-rise">
            <div className="card p-4 border-line">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                  <h2 className="text-base font-bold flex items-center gap-2 text-ink">
                    <span>👥</span> All 20 Specialized AI Coaches
                  </h2>
                  <p className="text-xs text-muted mt-0.5">
                    Toggle follow to customize whose lessons appear in your feed.
                  </p>
                </div>
                <div className="flex items-center gap-1.5 text-xs font-bold px-2.5 py-1 rounded-full bg-brand-violet/15 text-brand-violet w-fit shrink-0">
                  <span>✓</span> {me?.follows?.length ?? 0} of 20 Followed
                </div>
              </div>

              {/* Pillar Filter Tabs */}
              <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar pt-3 mt-3 border-t border-line">
                {PILLARS.map(p => {
                  const count = p.key === 'ALL' ? AGENTS.length : AGENTS.filter(a => a.pillar === p.key).length
                  const active = pillarFilter === p.key
                  return (
                    <button
                      key={p.key}
                      type="button"
                      onClick={() => setPillarFilter(p.key)}
                      className={`px-3 py-1 rounded-full text-xs font-semibold shrink-0 transition flex items-center gap-1.5 ${
                        active
                          ? 'bg-brand-violet text-white shadow-sm'
                          : 'bg-surface2 text-muted hover:text-ink'
                      }`}
                    >
                      <span>{p.emoji}</span>
                      <span>{p.label}</span>
                      <span className={`text-[10px] px-1.5 py-0.2 rounded-full font-bold ${active ? 'bg-white/25 text-white' : 'bg-surface3 text-muted'}`}>
                        {count}
                      </span>
                    </button>
                  )
                })}
              </div>
            </div>

            {/* List of Experts */}
            <div className="space-y-2.5">
              {filteredAgents.map(a => {
                const isFollowing = !!me?.follows?.includes(a.id)
                const pillarStyle = PILLAR_COLORS[a.pillar] || PILLAR_COLORS.LIFE
                return (
                  <div
                    key={a.id}
                    className="card p-3.5 border-line hover:border-brand-violet/40 transition flex items-center gap-3.5"
                  >
                    <Link to={`/experts/${a.id}`} className="shrink-0 group">
                      <div className="group-hover:scale-105 transition">
                        <AgentAvatar agent={a} size={44} ring />
                      </div>
                    </Link>
                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-2">
                        <Link to={`/experts/${a.id}`} className="font-bold text-sm text-ink truncate hover:underline flex items-center gap-1">
                          {a.name} <Verified />
                        </Link>
                        <span className={`text-[9.5px] font-extrabold uppercase tracking-wider px-2 py-0.5 rounded-full border ${pillarStyle.bg} ${pillarStyle.text} ${pillarStyle.border}`}>
                          {a.pillar}
                        </span>
                      </div>
                      <div className="text-xs font-semibold text-ink/80 mt-0.5 truncate">{a.domainLabel}</div>
                      <p className="text-[11.5px] text-muted line-clamp-1 mt-0.5 leading-snug">
                        {a.persona}
                      </p>
                    </div>
                    <div className="flex flex-col items-end gap-1.5 shrink-0">
                      <button
                        type="button"
                        onClick={() => toggleFollow(a.id, a.name)}
                        className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1 ${
                          isFollowing
                            ? 'bg-surface2 text-muted hover:bg-bad/10 hover:text-bad border border-line'
                            : 'btn-grad !py-1.5 !px-3 !text-xs shadow-sm'
                        }`}
                      >
                        {isFollowing ? (
                          <><span>✓</span> Following</>
                        ) : (
                          <><span>+</span> Follow</>
                        )}
                      </button>
                      <Link
                        to={`/experts/${a.id}`}
                        className="text-[10.5px] text-muted hover:text-ink font-semibold"
                      >
                        View profile →
                      </Link>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>
        ) : (
          /* Post Feed for New Feeds and Learned */
          <div className="space-y-3.5">
            {loading && !data && [0, 1, 2].map(i => <PostSkeleton key={i} />)}
            {error && (
              <EmptyState
                title="Couldn’t load the feed"
                text={error}
                action={<button className="btn-ghost" onClick={reload}>Try again</button>}
              />
            )}

            {data && visiblePosts.length === 0 && (
              tab === 'today' ? (
                <EmptyState
                  title={doneCount > 0 ? "You're all caught up! 🎉" : "No new feeds right now"}
                  text={
                    doneCount > 0
                      ? "Great job! You completed all current safety activities. All your completed answers and learnings are saved in the Learned tab."
                      : "The experts post through the day. Check back soon, or view your learning portfolio in the Learned tab."
                  }
                  action={<button className="btn-grad" onClick={() => choose('learned')}>View Learned</button>}
                />
              ) : (
                <EmptyState
                  title="No learned topics yet 📚"
                  text="Complete safety scenarios and participate in quick challenges in New Feeds to build your learning portfolio."
                  action={<button className="btn-grad" onClick={() => choose('today')}>Explore New Feeds</button>}
                />
              )
            )}

            {visiblePosts.map(p => {
              const isFading = fadingIds.has(p.id)
              return (
                <div
                  key={p.id}
                  className={`transition-all duration-500 transform ${
                    isFading ? 'opacity-0 scale-95 pointer-events-none' : 'opacity-100 scale-100'
                  }`}
                >
                  <PostCard post={p} onComplete={handleCardComplete} />
                </div>
              )
            })}

            {data && visiblePosts.length > 0 && (
              <p className="text-center text-xs text-muted py-5">
                {tab === 'today'
                  ? '🎉 You’re all caught up for now. New posts arrive through the day.'
                  : '🎓 End of your learned activities.'}
              </p>
            )}
          </div>
        )}
      </div>

      <PointsModal
        data={pointsModalData}
        onClose={() => setPointsModalData(null)}
      />
    </AppShell>
  )
}
