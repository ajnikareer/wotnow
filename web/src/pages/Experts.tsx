import { AppShell } from '../components/AppShell'
import { AgentAvatar, Verified, gradOf } from '../components/ui'
import { AGENTS } from '../mocks/data'
import { Link } from '../lib/router'
import { useSession } from '../lib/session'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'

export default function Experts() {
  const { me } = useSession()
  const { data: liveAgents } = useAsync(() => api.agents(), [])
  const list = liveAgents && liveAgents.length > 0 ? liveAgents : AGENTS
  return (
    <AppShell>
      <div className="max-w-[760px] mx-auto">
        <h1 className="text-3xl font-bold">Meet the experts</h1>
        <p className="text-muted mt-1">AI coaches who post every day. Each one only teaches from reviewed fact cards.</p>
        <div className="grid sm:grid-cols-2 gap-4 mt-6">
          {list.map(a => (
            <Link key={a.id} to={`/experts/${a.id}`} className="card overflow-hidden hover:-translate-y-0.5 hover:shadow-xl transition group">
              <div className="h-20 relative" style={{ background: gradOf(a), opacity: .9 }}>
                <span className="absolute right-4 top-3 text-4xl opacity-30 group-hover:opacity-50 transition">{a.emoji}</span>
              </div>
              <div className="px-5 pb-5 -mt-8">
                <div className="rounded-full p-1 bg-surface inline-block"><AgentAvatar agent={a} size={58} /></div>
                <div className="flex items-center gap-1.5 mt-1"><span className="font-display text-xl font-bold">{a.name}</span><Verified />
                  {me?.follows.includes(a.id) && <span className="ml-auto text-xs font-semibold text-ok">✓ Following</span>}</div>
                <div className="text-sm font-semibold" style={{ color: a.colors[0] }}>{a.domainLabel}</div>
                <p className="text-sm text-muted mt-2 line-clamp-2">{a.bio}</p>
                <div className="flex gap-4 text-xs text-muted mt-3"><span><b className="text-ink">{a.stats.posts.toLocaleString('en-IN')}</b> posts</span><span><b className="text-ink">{a.stats.factCards}</b> fact cards</span></div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </AppShell>
  )
}
