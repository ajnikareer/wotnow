import { Badge, Section, Stat, when } from './kit'

export function OverviewView({ data, busy, onPause, onRunNow, onRefresh }: { data: any; busy: boolean; onPause: (paused: boolean) => void; onRunNow: () => void; onRefresh: () => void }) {
  const p = data.pipeline
  const by = data.posts.byStatus as Record<string, number>
  const skills = Object.entries(data.agentRuns24h.bySkill as Record<string, any>)
  return (
    <>
      {data.reviewedOnly && <div className="mb-4 p-3 rounded-2xl bg-warn/10 border border-warn/25 text-sm">🔒 <b>Reviewed-only mode is on:</b> experts only use fact cards marked reviewed ({data.cards.reviewed} of {data.cards.total}).</div>}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-5">
        <Stat label="Gemini" value={data.ai.geminiReady ? 'Ready' : 'Off'} tone={data.ai.geminiReady ? 'ok' : 'warn'} sub={`${data.ai.runtime} · ${data.ai.model}`} />
        <Stat label="Content pipeline" value={p.paused ? 'Paused' : p.enabled ? 'Running' : 'Disabled'} tone={p.paused ? 'warn' : p.enabled ? 'ok' : 'bad'} sub={`last tick ${when(p.lastTickAt)}`} />
        <Stat label="Posts today (pipeline)" value={data.posts.madeByPipelineToday} sub={`${data.posts.total} posts in total`} />
        <Stat label="Waiting for review" value={by.pending ?? 0} tone={(by.pending ?? 0) > 0 ? 'warn' : undefined} sub={`${by.live ?? 0} live · ${by.rejected ?? 0} rejected`} />
        <Stat label="Students" value={data.people.students} sub={`${data.people.accounts} parent accounts`} />
        <Stat label="Agent runs (24h)" value={data.agentRuns24h.total} sub="judge, writer, reviewer…" />
        <Stat label="Fact cards reviewed" value={`${data.cards.reviewed}/${data.cards.total}`} tone={data.cards.reviewed === 0 ? 'warn' : undefined} sub="by a human" />
        <Stat label="Database" value={data.db} sub={`auth: ${data.authMode} · up ${Math.round(data.uptimeS / 60)} min`} />
      </div>
      <Section title="Pipeline control" hint="Pause stops all automatic posting. Generate now creates one post from every enabled expert right away."
        right={<button className="btn-ghost" onClick={onRefresh}>Refresh</button>}>
        <div className="flex flex-wrap gap-2">
          <button className={p.paused ? 'btn-grad' : 'btn-soft'} disabled={busy} onClick={() => onPause(!p.paused)}>{p.paused ? '▶ Resume posting' : '⏸ Pause posting'}</button>
          <button className="btn-ghost" disabled={busy} onClick={onRunNow}>⚡ Generate now (all enabled experts)</button>
        </div>
        {p.lastRun && <div className="text-sm text-muted mt-3">Last run {when(p.lastRun.ts)} · {p.lastRun.actions.length} actions · {p.lastRun.errors.length} errors · {p.lastRun.source}</div>}
      </Section>
      <Section title="Agent skills, last 24 hours" hint="How each AI skill is doing: successful runs, blocked by a guardrail or the safety reviewer, and speed.">
        {skills.length === 0 ? <p className="text-sm text-muted">No agent runs yet.</p> : (
          <table className="w-full text-sm">
            <thead><tr className="text-left text-muted text-xs"><th className="py-1.5">Skill</th><th>Runs</th><th>OK</th><th>Blocked</th><th>Errors</th><th>Avg time</th></tr></thead>
            <tbody>{skills.map(([k, s]) => (
              <tr key={k} className="border-t border-line"><td className="py-2 font-semibold">{k}</td><td>{s.runs}</td><td><Badge tone="ok">{s.ok}</Badge></td>
                <td>{s.blocked ? <Badge tone="warn">{s.blocked}</Badge> : '0'}</td><td>{s.errors ? <Badge tone="bad">{s.errors}</Badge> : '0'}</td><td>{(s.avgMs / 1000).toFixed(1)} s</td></tr>
            ))}</tbody>
          </table>
        )}
      </Section>
    </>
  )
}
