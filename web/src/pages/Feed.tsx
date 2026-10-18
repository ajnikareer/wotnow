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
  { key: 'LIFE', label: 'Life', emoji: '❤️' },
  { key: 'PLANET', label: 'Planet', emoji: '🌍' },
  { key: 'FUTURE', label: 'Future', emoji: '🚀' },
  { key: 'MIND', label: 'Mind', emoji: '🧠' },
]

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
  const { data, loading, error, reload } = useAsync(() => loadFeed(tab), [tab])
  const [fresh, setFresh] = useState(0)
  const [todayCount, setTodayCount] = useState<number | null>(null)
  const [completedIds, setCompletedIds] = useState<Set<string>>(new Set())
  const [fadingIds, setFadingIds] = useState<Set<string>>(new Set())
  const [pointsModalData, setPointsModalData] = useState<PointsModalData | null>(null)
  const [pillarFilter, setPillarFilter] = useState<'ALL' | Pillar>('ALL')
  const seen = new Set(['civic', 'cipher', 'compass'])

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

  // Posts visible in the current tab
  const visiblePosts = useMemo(() => {
    if (!data) return []
    if (tab === 'today') {
      return data.filter(p => p.state !== 'done' && !completedIds.has(p.id))
    }
    if (tab === 'learned') {
      return data.filter(p => p.state === 'done' || p.state === 'retry' || p.my != null || completedIds.has(p.id))
    }
    // following tab
    return data.filter(p => !completedIds.has(p.id))
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
    if (!newest) return
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
      <div className="max-w-[580px] mx-auto">
        {/* Feed Tabs: New Feeds, Learned, and Following */}
        <div className="flex items-center gap-2 mb-3">
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

        {/* Stories / Expert Shortcuts */}
        <div className="flex gap-2.5 overflow-x-auto no-scrollbar pb-2 mb-3 border-b border-line">
          {AGENTS.map(a => (
            <Link key={a.id} to={`/experts/${a.id}`} className="flex flex-col items-center gap-1 shrink-0 group">
              <div className="group-hover:scale-105 transition">
                <AgentAvatar agent={a} size={36} ring seen={seen.has(a.id)} />
              </div>
              <span className="text-[10px] text-muted font-medium">{a.name}</span>
            </Link>
          ))}
          <button
            type="button"
            onClick={() => choose('following')}
            className="flex flex-col items-center gap-1 shrink-0 group cursor-pointer"
            title="View all 20 AI Coaches"
          >
            <div className="w-[36px] h-[36px] rounded-full border border-dashed border-brand-violet/60 flex items-center justify-center text-[11px] font-extrabold text-brand-violet group-hover:scale-105 transition bg-brand-violet/10">
              +20
            </div>
            <span className="text-[10px] text-brand-violet font-semibold">All 20</span>
          </button>
        </div>

        {/* Following Tab - All 20 Coaches Directory */}
        {tab === 'following' && (
          <div className="card p-3.5 mb-3.5 border-line animate-rise">
            <div className="flex items-center justify-between gap-2 mb-2">
              <div>
                <h2 className="text-sm font-bold flex items-center gap-1.5 text-ink">
                  <span>👥</span> All 20 Specialized Coaches
                </h2>
                <p className="text-[11px] text-muted">
                  Follow your favorite coaches across the 4 pillars to personalize your feed.
                </p>
              </div>
              <span className="text-[10.5px] font-bold px-2 py-0.5 rounded-full bg-brand-violet/15 text-brand-violet shrink-0">
                {me?.follows?.length ?? 0} followed
              </span>
            </div>

            {/* Pillar Filter Tabs */}
            <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
              {PILLARS.map(p => {
                const count = p.key === 'ALL' ? AGENTS.length : AGENTS.filter(a => a.pillar === p.key).length
                const active = pillarFilter === p.key
                return (
                  <button
                    key={p.key}
                    type="button"
                    onClick={() => setPillarFilter(p.key)}
                    className={`px-2.5 py-1 rounded-full text-[11px] font-semibold shrink-0 transition flex items-center gap-1 ${
                      active
                        ? 'bg-brand-violet text-white shadow-sm'
                        : 'bg-surface2 text-muted hover:text-ink'
                    }`}
                  >
                    <span>{p.emoji}</span>
                    <span>{p.label}</span>
                    <span className="text-[9.5px] opacity-75">({count})</span>
                  </button>
                )
              })}
            </div>

            {/* Coaches Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-2.5 max-h-[340px] overflow-y-auto pr-1">
              {filteredAgents.map(a => {
                const isFollowing = !!me?.follows?.includes(a.id)
                return (
                  <div key={a.id} className="p-2 rounded-xl bg-surface2/60 border border-line flex items-center gap-2 hover:border-brand-violet/40 transition">
                    <Link to={`/experts/${a.id}`} className="shrink-0">
                      <AgentAvatar agent={a} size={32} ring />
                    </Link>
                    <div className="min-w-0 flex-1">
                      <Link to={`/experts/${a.id}`} className="font-bold text-xs truncate flex items-center gap-1 hover:underline">
                        {a.name} <Verified />
                      </Link>
                      <div className="text-[10.5px] text-muted truncate">{a.domainLabel}</div>
                    </div>
                    <button
                      type="button"
                      onClick={() => toggleFollow(a.id, a.name)}
                      className={`shrink-0 px-2 py-1 rounded-lg text-[10px] font-bold transition ${
                        isFollowing
                          ? 'bg-surface3 text-muted hover:bg-bad/15 hover:text-bad'
                          : 'btn-grad !py-0.5 !px-2 !text-[10px]'
                      }`}
                    >
                      {isFollowing ? 'Following' : '+ Follow'}
                    </button>
                  </div>
                )
              })}
            </div>
          </div>
        )}

        {/* Post Feed */}
        <div className="space-y-3.5">
          {tab === 'following' && (
            <div className="flex items-center justify-between mb-1 px-1">
              <span className="text-[11px] font-bold uppercase tracking-wider text-muted">
                Feed from coaches you follow ({visiblePosts.length})
              </span>
            </div>
          )}

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
                    ? `Great job! You completed all current safety activities. All your completed answers and learnings are saved in the Learned tab.`
                    : "The experts post through the day. Check back soon, or view your learning portfolio in the Learned tab."
                }
                action={<button className="btn-grad" onClick={() => choose('learned')}>View Learned</button>}
              />
            ) : tab === 'learned' ? (
              <EmptyState
                title="No learned topics yet 📚"
                text="Complete safety scenarios and participate in quick challenges in New Feeds to build your learning portfolio."
                action={<button className="btn-grad" onClick={() => choose('today')}>Explore New Feeds</button>}
              />
            ) : (
              <EmptyState
                title="No posts from followed coaches yet 👥"
                text={me?.follows?.length ? "The coaches you follow haven't posted new items yet today. Explore New Feeds or follow more coaches above." : "Follow any coach in the list above to see their real-life situations and challenges in this tab."}
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
                : tab === 'learned'
                  ? '🎓 End of your learned activities.'
                  : '👥 End of followed coaches feed.'}
            </p>
          )}
        </div>
      </div>

      <PointsModal
        data={pointsModalData}
        onClose={() => setPointsModalData(null)}
      />
    </AppShell>
  )
}
