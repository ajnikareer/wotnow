import { Badge, Section, when } from './kit'

export function TracesView({ traces, skills, filters, setFilters, onRefresh }: {
  traces: any[]; skills: string[]; filters: { skill: string; ok: string }; setFilters: (f: { skill: string; ok: string }) => void; onRefresh: () => void
}) {
  return (
    <Section title="Agent traces" hint="Every ADK agent run: which skill, how long, what the guardrails and the safety reviewer decided."
      right={<div className="flex gap-2">
        <select className="input !py-2 !w-auto" value={filters.skill} onChange={e => setFilters({ ...filters, skill: e.target.value })}><option value="">All skills</option>{skills.map(s => <option key={s} value={s}>{s}</option>)}</select>
        <select className="input !py-2 !w-auto" value={filters.ok} onChange={e => setFilters({ ...filters, ok: e.target.value })}><option value="">Any result</option><option value="true">OK</option><option value="false">Blocked / failed</option></select>
        <button className="btn-ghost" onClick={onRefresh}>Refresh</button></div>}>
      {traces.length === 0 ? <p className="text-sm text-muted py-4">No traces yet.</p> : (
        <div className="overflow-x-auto"><table className="w-full text-sm">
          <thead><tr className="text-left text-muted text-xs"><th className="py-1.5">When</th><th>Skill</th><th>Agent</th><th>Time</th><th>Result</th></tr></thead>
          <tbody>{traces.map(t => (
            <tr key={t.id} className="border-t border-line align-top">
              <td className="py-2 whitespace-nowrap">{when(t.ts)}</td><td className="font-semibold">{t.skill}</td><td className="text-muted">{t.agent}</td><td className="whitespace-nowrap">{((t.ms ?? 0) / 1000).toFixed(1)} s</td>
              <td>{t.ok ? <Badge tone="ok">ok</Badge> : <Badge tone="bad">{t.error ? 'error' : 'blocked'}</Badge>}
                {t.review && <> <Badge tone={t.review.approved ? 'ok' : 'warn'}>reviewer: {t.review.approved ? 'approved' : 'rejected'}</Badge></>}
                {t.pii_scrubbed && <> <Badge tone="info">PII removed</Badge></>}{t.injection_suspected && <> <Badge tone="warn">injection?</Badge></>}
                {(t.blocked || t.error) && <div className="text-xs text-muted mt-1 max-w-xl">{t.blocked || t.error}</div>}</td></tr>
          ))}</tbody></table></div>
      )}
    </Section>
  )
}
