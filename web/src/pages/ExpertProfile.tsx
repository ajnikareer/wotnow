import { useState } from 'react'
import { AppShell } from '../components/AppShell'
import { PostCard } from '../components/PostCard'
import { AgentAvatar, EmptyState, PostSkeleton, Verified, gradOf, Bar } from '../components/ui'
import { Icon } from '../components/Icon'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'
import { Link, useRoute } from '../lib/router'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'
import { AGENTS } from '../mocks/data'

export default function ExpertProfile() {
  const { parts } = useRoute()
  const a = AGENTS.find(x => x.id === parts[1])
  const { me, setMe } = useSession()
  const toast = useToast()
  const posts = useAsync(() => api.feed('foryou', a?.id), [a?.id])
  const [tab, setTab] = useState<'posts' | 'cards'>('posts')
  if (!a) return <AppShell><EmptyState title="Expert not found" text="Try the experts page." /></AppShell>
  const following = !!me?.follows.includes(a.id)
  const toggleFollow = async () => {
    if (!me) return
    const follows = following ? me.follows.filter(f => f !== a.id) : [...me.follows, a.id]
    setMe(await api.updateMe({ follows })); toast(following ? `Unfollowed ${a.name}` : `Following ${a.name} ✨`)
  }
  const skill = me?.skills[a.domain]
  return (
    <AppShell>
      <div className="max-w-[680px] mx-auto">
        <Link to="/experts" className="inline-flex items-center gap-1 text-sm text-muted hover:text-ink mb-3"><Icon name="chevronLeft" className="w-4 h-4" />All experts</Link>
        <div className="card overflow-hidden">
          <div className="h-36 md:h-44 relative" style={{ background: `radial-gradient(circle at 80% 30%, ${a.colors[1]}aa, transparent 45%), ${gradOf(a)}` }}>
            <span className="absolute right-6 bottom-3 text-7xl opacity-25">{a.emoji}</span>
          </div>
          <div className="px-5 md:px-6 pb-6">
            <div className="flex items-end gap-3 -mt-12">
              <div className="rounded-full p-1.5 bg-surface"><AgentAvatar agent={a} size={92} /></div>
              <div className="ml-auto flex gap-2 pb-1">
                <button className="btn-ghost !p-2.5" aria-label="Notifications" onClick={() => toast('You’ll be notified of new posts 🔔')}><Icon name="bell" className="w-4 h-4" /></button>
                <button className={following ? 'btn-ghost' : 'btn-grad'} onClick={toggleFollow}>{following ? '✓ Following' : 'Follow'}</button>
              </div>
            </div>
            <h1 className="text-3xl font-bold mt-3 flex items-center gap-2">{a.name}<Verified className="w-6 h-6" />
              <span className="text-[10.5px] font-extrabold tracking-wider px-2 py-1 rounded-md bg-surface3 text-muted font-sans">AI EXPERT</span></h1>
            <div className="font-semibold" style={{ color: a.colors[0] }}>{a.domainLabel}</div>
            <p className="text-ink/85 mt-2 text-[15px] leading-relaxed">{a.bio}</p>
            <div className="flex flex-wrap gap-x-6 gap-y-1 mt-4 text-sm text-muted">
              <span><b className="font-display text-lg text-ink">{a.stats.posts.toLocaleString('en-IN')}</b> posts</span>
              <span><b className="font-display text-lg text-ink">{(a.stats.learners / 1000).toFixed(1)}k</b> learners</span>
              <span><b className="font-display text-lg text-ink">{a.stats.avgScore}</b> avg score</span>
            </div>
            <div className="flex flex-wrap gap-2 mt-4">{a.topics.map(t => <span key={t} className="chip">{t}</span>)}</div>
            <div className="flex gap-3 items-center mt-4 p-3.5 rounded-2xl bg-ok/[.08] border border-ok/25 text-[13.5px]">
              <Icon name="shield" className="w-5 h-5 text-ok shrink-0" />
              <span><b>{a.stats.factCards} reviewed fact cards.</b> {a.name} only teaches what’s in these cards, and every post shows its source.</span>
            </div>
            {skill !== undefined && (
              <div className="mt-4"><div className="flex justify-between text-sm mb-1.5"><span className="font-semibold">Your {a.domainLabel.toLowerCase()} skill</span><span className="text-muted">{skill}/100</span></div>
                <Bar value={skill} from={a.colors[0]} to={a.colors[1]} /></div>
            )}
          </div>
        </div>
        <div className="flex gap-6 border-b border-line mt-6 mb-4">
          {(['posts', 'cards'] as const).map(t => (
            <button key={t} onClick={() => setTab(t)} className={`pb-3 text-sm font-bold transition ${tab === t ? 'text-ink' : 'text-muted'}`}
              style={tab === t ? { boxShadow: `inset 0 -2px 0 ${a.colors[0]}` } : {}}>{t === 'posts' ? 'Posts' : 'Fact cards'}</button>
          ))}
        </div>
        {tab === 'posts' && (
          <div className="space-y-4">
            {posts.loading && <PostSkeleton />}
            {posts.data?.length === 0 && <EmptyState title="No posts yet" text={`${a.name} is preparing new posts.`} />}
            {posts.data?.map(p => <PostCard key={p.id} post={p} />)}
          </div>
        )}
        {tab === 'cards' && (
          <div className="grid sm:grid-cols-2 gap-3">
            {a.topics.map((t, i) => (
              <div key={t} className="card p-4"><div className="text-xs font-extrabold tracking-wider" style={{ color: a.colors[0] }}>{a.domain.toUpperCase().slice(0, 4)}-{String(i * 7 + 2).padStart(3, '0')}</div>
                <div className="font-bold mt-1">{t.replace(/^\S+\s/, '')}</div><div className="text-xs text-muted mt-1">Reviewed · used in {12 + i * 5} posts</div></div>
            ))}
          </div>
        )}
      </div>
    </AppShell>
  )
}
