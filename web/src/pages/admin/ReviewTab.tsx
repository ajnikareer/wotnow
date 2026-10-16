import { Badge, Section, when, type Tone } from './kit'

const STATUS_TONE: Record<string, Tone> = { live: 'ok', pending: 'warn', unpublished: 'mute', rejected: 'bad' }

export function ReviewView({ posts, total, experts, filters, setFilters, open, detail, busy, onOpen, onStatus }: {
  posts: any[]; total: number; experts: any[]; filters: { status: string; agent: string }; setFilters: (f: { status: string; agent: string }) => void
  open: string | null; detail: any; busy: boolean; onOpen: (id: string | null) => void; onStatus: (id: string, status: string) => void
}) {
  return (
    <Section title="Review queue" hint="Approve posts that wait for review, or unpublish anything that shouldn't be live. Changes take effect immediately."
      right={<div className="flex gap-2">
        <select className="input !py-2 !w-auto" value={filters.status} onChange={e => setFilters({ ...filters, status: e.target.value })}>
          {['', 'pending', 'live', 'unpublished', 'rejected'].map(s => <option key={s} value={s}>{s || 'All statuses'}</option>)}</select>
        <select className="input !py-2 !w-auto" value={filters.agent} onChange={e => setFilters({ ...filters, agent: e.target.value })}>
          <option value="">All experts</option>{experts.map(e => <option key={e.id} value={e.id}>{e.name}</option>)}</select></div>}>
      <div className="text-xs text-muted mb-2">{total} post{total === 1 ? '' : 's'}</div>
      {posts.length === 0 && <p className="text-sm text-muted py-6 text-center">Nothing here.</p>}
      <div className="space-y-2">
        {posts.map(p => (
          <div key={p.id} className="rounded-2xl border border-line">
            <div className="flex flex-wrap items-center gap-2 p-3 cursor-pointer" onClick={() => onOpen(open === p.id ? null : p.id)}>
              <Badge tone={STATUS_TONE[p.status] ?? 'mute'}>{p.status}</Badge>
              <Badge tone="info">{p.type.replace('_', ' ')}</Badge>
              <span className="font-semibold">{p.title}</span>
              <span className="text-muted text-sm">· {p.agentId} · {p.origin ?? 'seed'}/{p.source ?? '?'} · {when(p.createdAt)}</span>
              <span className="ml-auto text-muted">{open === p.id ? '▲' : '▼'}</span>
            </div>
            {open === p.id && (
              <div className="border-t border-line p-4 text-sm space-y-3">
                {!detail ? <div className="skeleton h-20" /> : (
                  <>
                    <div><b>{detail.title}</b><p className="mt-1">{detail.body}</p>{detail.question && <p className="font-semibold mt-1">{detail.question}</p>}{detail.statement && <p className="font-display text-lg mt-1">{detail.statement}</p>}
                      {detail.message && <p className="mt-1 p-2 rounded-xl bg-surface2">From {detail.message.from}: {detail.message.text}</p>}</div>
                    {detail.options && <ul className="space-y-1">{detail.options.map((o: any) => <li key={o.id}>{o.id === detail.answerKey ? '✅' : '▫️'} {o.text}</li>)}</ul>}
                    {detail.answerKey && !detail.options && <div>Answer: <Badge tone="ok">{detail.answerKey}</Badge></div>}
                    {detail.explanation && <div className="text-muted">💡 {detail.explanation}</div>}
                    {detail.rubric && (<div><div className="font-semibold mb-1">Hidden rubric</div>
                      <ul className="space-y-1">{detail.rubric.map((r: any) => <li key={r.id}>{r.critical ? '⚠️' : '•'} {r.point} <span className="text-muted">({r.weight} pts · {r.card})</span></li>)}</ul>
                      {detail.dangerousActions?.length > 0 && <div className="mt-1 text-bad">Dangerous: {detail.dangerousActions.join('; ')}</div>}</div>)}
                    <div className="text-xs text-muted">Cards: {(detail.sourceCards || []).map((c: any) => c.id).join(', ') || '–'}{detail.quality && ` · duplicate similarity ${detail.quality.similarity} (${detail.quality.dedupe})`}</div>
                    <div className="flex flex-wrap gap-2 pt-1">
                      {detail.status !== 'live' && <button className="btn-grad" disabled={busy} onClick={() => onStatus(p.id, 'live')}>✓ {detail.status === 'pending' ? 'Approve & publish' : 'Publish'}</button>}
                      {detail.status === 'live' && <button className="btn-soft" disabled={busy} onClick={() => onStatus(p.id, 'unpublished')}>Unpublish</button>}
                      {detail.status !== 'rejected' && <button className="btn-ghost text-bad" disabled={busy} onClick={() => onStatus(p.id, 'rejected')}>✗ Reject</button>}
                    </div>
                  </>
                )}
              </div>
            )}
          </div>
        ))}
      </div>
    </Section>
  )
}
