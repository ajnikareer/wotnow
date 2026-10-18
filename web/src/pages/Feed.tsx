import { useEffect, useMemo, useRef, useState } from 'react'
import { AppShell } from '../components/AppShell'
import { PostCard } from '../components/PostCard'
import { StateLegend } from '../components/StateLegend'
import { AgentAvatar, EmptyState, PostSkeleton } from '../components/ui'
import { Icon } from '../components/Icon'
import { PointsModal, type PointsModalData } from '../components/PointsModal'
import { feedLatest, loadFeed, type FeedTab } from '../lib/api'
import { shouldLeaveToday } from '../lib/feedTabs'
import { useAsync } from '../lib/hooks'
import { Link } from '../lib/router'
import { useSession } from '../lib/session'
import { AGENTS } from '../mocks/data'

const POLL_MS = 60_000
const TABS: [FeedTab, string][] = [['today', 'Today'], ['foryou', 'For you'], ['near', 'Near me'], ['following', 'Following']]

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
  // "Today" comes first and is the landing tab, unless nothing but the city alert has been posted today
  const [tab, setTab] = useState<FeedTab>('today')
  const picked = useRef(false)                                        // true once the student chooses a tab themselves
  const { me } = useSession()
  const { data, loading, error, reload } = useAsync(() => loadFeed(tab), [tab])
  const [fresh, setFresh] = useState(0)
  const [todayCount, setTodayCount] = useState<number | null>(null)
  const [completedIds, setCompletedIds] = useState<Set<string>>(new Set())
  const [fadingIds, setFadingIds] = useState<Set<string>>(new Set())
  const [pointsModalData, setPointsModalData] = useState<PointsModalData | null>(null)
  const [showDone, setShowDone] = useState(false)
  const seen = new Set(['civic', 'cipher', 'compass'])

  const choose = (t: FeedTab) => { picked.current = true; setTab(t) }

  // Count done items in this tab
  const doneCount = useMemo(() => {
    if (!data) return 0
    return data.filter(p => p.state === 'done' || completedIds.has(p.id)).length
  }, [data, completedIds])

  // Filter out done posts unless user toggles "Show completed"
  const visiblePosts = useMemo(() => {
    if (!data) return []
    if (showDone) return data
    return data.filter(p => p.state !== 'done' && !completedIds.has(p.id))
  }, [data, completedIds, showDone])

  // Nothing new today (only the city alert, or nothing at all): start on "For you" instead of an empty page.
  useEffect(() => { if (shouldLeaveToday(tab, picked.current, loading, data)) setTab('foryou') }, [tab, data, loading])

  // The number on the Today tab: counts only active (not done) posts
  useEffect(() => {
    if (tab === 'today' && data && !loading) {
      const activeCount = data.filter(p => p.state !== 'done' && !completedIds.has(p.id)).length
      setTodayCount(activeCount)
    }
  }, [tab, data, loading, completedIds])

  useEffect(() => { feedLatest('today', '').then(r => { if (r) setTodayCount(r.todayCount) }).catch(() => { /* not signed in yet */ }) }, [])

  // The newest post time currently on screen; the poll asks the server how many are newer.
  const newest = useMemo(() => (data && data.length ? data.reduce((m: string, p: any) => (p.createdAt > m ? p.createdAt : m), '') : ''), [data])

  useEffect(() => { setFresh(0) }, [data, tab])
  useEffect(() => {
    if (!newest) return
    let stop = false
    const check = async () => {
      if (document.hidden) return
      try {
        const r = await feedLatest(tab, newest)
        if (!stop && r) { setFresh(r.newCount); setTodayCount(r.todayCount) }
      } catch { /* offline or signed out: try again next time */ }
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
      <div className="max-w-[640px] mx-auto">
        <div className="flex items-center gap-2 mb-4">
          <div className="flex items-center gap-1 overflow-x-auto no-scrollbar" role="tablist">
            {TABS.map(([t, l]) => (
              <button key={t} role="tab" aria-selected={tab === t} onClick={() => choose(t)}
                className={`shrink-0 px-4 py-2 rounded-full text-sm font-bold transition inline-flex items-center gap-1.5 ${tab === t ? 'bg-ink text-bg' : 'text-muted hover:text-ink'}`}>
                {l}
                {t === 'today' && todayCount != null && todayCount > 0 && (
                  <span className={`px-1.5 py-0.5 rounded-full text-[10.5px] font-extrabold leading-none ${tab === t ? 'bg-bg text-ink' : 'grad-bg text-[#06080C]'}`}>{todayCount}</span>
                )}
              </button>
            ))}
          </div>
          <span className="ml-auto chip shrink-0"><Icon name="pin" className="w-3.5 h-3.5" />{me?.city ?? 'Pune'}</span>
        </div>

        <NewPostsBanner count={fresh} onClick={refresh} />

        {/* stories = expert shortcuts */}
        <div className="flex gap-4 overflow-x-auto no-scrollbar pb-4 mb-4 border-b border-line">
          {AGENTS.map(a => (
            <Link key={a.id} to={`/experts/${a.id}`} className="flex flex-col items-center gap-1.5 shrink-0 group">
              <div className="group-hover:scale-105 transition"><AgentAvatar agent={a} size={56} ring seen={seen.has(a.id)} /></div>
              <span className="text-[11.5px] text-muted font-medium">{a.name}</span>
            </Link>
          ))}
        </div>

        {/* live banner */}
        <Link to="/live" className="block mb-4 rounded-3xl p-4 md:p-5 border border-brand-violet/30 overflow-hidden relative"
          style={{ background: 'linear-gradient(120deg, rgba(139,92,246,.22), rgba(34,211,238,.12) 60%, rgba(52,211,153,.08))' }}>
          <div className="flex items-center gap-4">
            <AgentAvatar agent={AGENTS[1]} size={52} />
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-1.5 text-[11px] font-extrabold tracking-wider text-bad"><span className="w-2 h-2 rounded-full bg-bad animate-pulse" />LIVE QUIZ</div>
              <div className="font-bold text-[16px] leading-tight mt-0.5">Road Safety Blitz · 5 questions</div>
              <div className="text-[13px] text-muted mt-0.5">5 quick questions · Fastest answers earn bonus XP</div>
            </div>
            <span className="btn-grad">Join</span>
          </div>
        </Link>

        <StateLegend
          doneCount={doneCount}
          showDone={showDone}
          onToggleShowDone={() => setShowDone(!showDone)}
        />

        <div className="space-y-4">
          {loading && !data && [0, 1, 2].map(i => <PostSkeleton key={i} />)}
          {error && <EmptyState title="Couldn’t load the feed" text={error} action={<button className="btn-ghost" onClick={reload}>Try again</button>} />}
          {data && visiblePosts.length === 0 && (tab === 'today'
            ? <EmptyState
                title={doneCount > 0 ? "You're all caught up for today! 🎉" : "Nothing new today yet"}
                text={doneCount > 0
                  ? `Awesome work! You completed today's safety activities. Check out 'For you' to explore more or come back tomorrow.`
                  : "The experts post through the day. Check back soon, or have a look at everything in For you."}
                action={<button className="btn-grad" onClick={() => choose('foryou')}>Go to For you</button>}
              />
            : <EmptyState title="Nothing here yet" text="Follow a few more experts to fill this tab." action={<Link to="/experts" className="btn-grad">Find experts</Link>} />)}
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
          {data && visiblePosts.length > 0 && <p className="text-center text-sm text-muted py-6">🎉 You’re all caught up. New posts arrive through the day.</p>}
        </div>
      </div>

      <PointsModal
        data={pointsModalData}
        onClose={() => setPointsModalData(null)}
      />
    </AppShell>
  )
}
