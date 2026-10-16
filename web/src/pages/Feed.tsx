import { useState } from 'react'
import { AppShell } from '../components/AppShell'
import { PostCard } from '../components/PostCard'
import { AgentAvatar, EmptyState, PostSkeleton } from '../components/ui'
import { Icon } from '../components/Icon'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'
import { Link } from '../lib/router'
import { useSession } from '../lib/session'
import { AGENTS } from '../mocks/data'

type Tab = 'foryou' | 'following' | 'near'

export default function Feed() {
  const [tab, setTab] = useState<Tab>('foryou')
  const { me } = useSession()
  const { data, loading, error, reload } = useAsync(() => api.feed(tab), [tab])
  const seen = new Set(['civic', 'cipher', 'compass'])
  return (
    <AppShell>
      <div className="max-w-[640px] mx-auto">
        <div className="flex items-center gap-1 mb-4">
          {([['foryou', 'For you'], ['near', 'Near me'], ['following', 'Following']] as [Tab, string][]).map(([t, l]) => (
            <button key={t} onClick={() => setTab(t)} className={`px-4 py-2 rounded-full text-sm font-bold transition ${tab === t ? 'bg-ink text-bg' : 'text-muted hover:text-ink'}`}>{l}</button>
          ))}
          <span className="ml-auto chip"><Icon name="pin" className="w-3.5 h-3.5" />{me?.city ?? 'Pune'}</span>
        </div>

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
              <div className="text-[13px] text-muted mt-0.5">Fastest correct answers win · 1,204 waiting</div>
            </div>
            <span className="btn-grad">Join</span>
          </div>
        </Link>

        <div className="space-y-4">
          {loading && !data && [0, 1, 2].map(i => <PostSkeleton key={i} />)}
          {error && <EmptyState title="Couldn’t load the feed" text={error} action={<button className="btn-ghost" onClick={reload}>Try again</button>} />}
          {data?.length === 0 && <EmptyState title="Nothing here yet" text="Follow a few more experts to fill this tab." action={<Link to="/experts" className="btn-grad">Find experts</Link>} />}
          {data?.map(p => <PostCard key={p.id} post={p} />)}
          {data && data.length > 0 && <p className="text-center text-sm text-muted py-6">🎉 You’re all caught up. New posts arrive every few hours.</p>}
        </div>
      </div>
    </AppShell>
  )
}
