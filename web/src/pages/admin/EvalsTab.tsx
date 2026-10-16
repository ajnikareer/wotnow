import { useEffect, useState } from 'react'
import { Badge, Section, TEXTAREA, pct, when } from './kit'

export function EvalsView({ data, run, busy, onRun, onSaveCases, onResetCases, onOpenRun }: {
  data: any; run: any | null; busy: boolean; onRun: () => void; onSaveCases: (json: any) => void; onResetCases: () => void; onOpenRun: (id: string) => void
}) {
  const [editor, setEditor] = useState<string>(JSON.stringify({ scenarios: data.scenarios, cases: data.cases }, null, 1))
  const [err, setErr] = useState<string>()
  const [showAll, setShowAll] = useState(false)
  useEffect(() => setEditor(JSON.stringify({ scenarios: data.scenarios, cases: data.cases }, null, 1)), [data])
  const m = run?.metrics
  const running = run?.status === 'running'
  const rows: any[] = run?.results ?? []
  const shown = showAll ? rows : rows.filter(r => !r.ok)
  return (
    <>
      <Section title="Judge evaluation" hint="Runs the golden answers through the real judge path. Use it before and after changing the judge's instructions or temperature."
        right={<button className="btn-grad" disabled={busy || running} onClick={onRun}>{running ? `Running… ${run.done}/${run.total}` : '▶ Run evaluation'}</button>}>
        <div className="text-sm text-muted mb-3">AI mode: <Badge tone={data.aiMode === 'mock' ? 'warn' : 'ok'}>{data.aiMode}</Badge> {data.aiMode === 'mock' && ' (Gemini is off, so this measures the rule-based fallback judge)'} · {data.cases.length} cases{data.customised ? ' (customised)' : ''}</div>
        {m && (
          <>
            <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
              <div className="rounded-2xl bg-surface2 p-3"><div className="text-xs text-muted">Exact matches</div><div className="font-display text-2xl font-bold">{m.exact}/{m.total}</div></div>
              <div className="rounded-2xl bg-surface2 p-3"><div className="text-xs text-muted">Rubric precision</div><div className="font-display text-2xl font-bold">{pct(m.precision)}</div></div>
              <div className="rounded-2xl bg-surface2 p-3"><div className="text-xs text-muted">Rubric recall</div><div className="font-display text-2xl font-bold">{pct(m.recall)}</div></div>
              <div className="rounded-2xl bg-surface2 p-3"><div className="text-xs text-muted">Danger accuracy</div><div className="font-display text-2xl font-bold">{pct(m.dangerAccuracy)}</div></div>
              <div className="rounded-2xl bg-surface2 p-3"><div className="text-xs text-muted">Avg time</div><div className="font-display text-2xl font-bold">{(m.avgMs / 1000).toFixed(1)} s</div></div>
            </div>
            <div className="flex items-center gap-3 mt-4 text-sm"><b>{showAll ? 'All cases' : 'Cases that differ from the expected answer'}</b>
              <button className="btn-ghost !py-1 !px-3" onClick={() => setShowAll(!showAll)}>{showAll ? 'Show only differences' : 'Show all'}</button></div>
            <div className="mt-2 space-y-2">{shown.length === 0 && <div className="text-sm text-ok">✅ Every case matched.</div>}
              {shown.map(r => (
                <div key={r.i} className={`rounded-2xl border p-3 text-sm ${r.ok ? 'border-line' : 'border-bad/30 bg-bad/[.05]'}`}>
                  <div className="flex flex-wrap gap-2 items-center"><b>#{r.i}</b><Badge>{r.scenario}</Badge><Badge tone={r.ok ? 'ok' : 'bad'}>{r.ok ? 'match' : 'differs'}</Badge><span className="text-muted">{r.judgedBy} · {r.ms} ms</span></div>
                  <div className="mt-1">“{r.answer}”</div>
                  <div className="text-muted mt-1">expected {r.expected.join(', ') || 'none'}{r.expectedDanger ? ' + danger' : ''} · got {r.got.join(', ') || 'none'}{r.gotDanger ? ' + danger' : ''}{r.error ? ` · ${r.error}` : ''}</div>
                </div>
              ))}</div>
          </>
        )}
        {!m && !running && <p className="text-sm text-muted">No run selected. Press “Run evaluation”, or open a past run below.</p>}
      </Section>
      <Section title="Past runs">
        {data.runs.length === 0 ? <p className="text-sm text-muted">No evaluations yet.</p> : (
          <table className="w-full text-sm"><thead><tr className="text-left text-muted text-xs"><th className="py-1.5">When</th><th>By</th><th>Exact</th><th>Precision</th><th>Recall</th><th>Danger</th><th /></tr></thead>
            <tbody>{data.runs.map((r: any) => (
              <tr key={r.id} className="border-t border-line"><td className="py-2">{when(r.at)}</td><td>{r.actor}</td>
                <td>{r.metrics ? `${r.metrics.exact}/${r.metrics.total}` : r.status}</td><td>{r.metrics ? pct(r.metrics.precision) : '–'}</td><td>{r.metrics ? pct(r.metrics.recall) : '–'}</td><td>{r.metrics ? pct(r.metrics.dangerAccuracy) : '–'}</td>
                <td className="text-right"><button className="btn-ghost !py-1 !px-3" onClick={() => onOpenRun(r.id)}>Open</button></td></tr>
            ))}</tbody></table>
        )}
      </Section>
      <Section title="Test cases" hint="Scenarios and golden answers (JSON). expected_hits are the rubric ids a good judge should mark as covered; dangerous says whether the answer recommends something unsafe.">
        <textarea className={TEXTAREA + ' min-h-[260px]'} value={editor} onChange={e => setEditor(e.target.value)} spellCheck={false} />
        {err && <div className="text-sm text-bad mt-2">⚠️ {err}</div>}
        <div className="flex gap-2 mt-3">
          <button className="btn-grad" disabled={busy} onClick={() => { try { setErr(undefined); onSaveCases(JSON.parse(editor)) } catch { setErr('That is not valid JSON.') } }}>Save cases</button>
          <button className="btn-ghost" disabled={busy || !data.customised} onClick={onResetCases}>Reset to shipped cases</button>
        </div>
      </Section>
    </>
  )
}
