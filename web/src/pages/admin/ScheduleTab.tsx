import { useEffect, useState } from 'react'
import { Badge, Section, Toggle, when } from './kit'

function Num({ label, value, onChange, min, max, hint }: { label: string; value: number; onChange: (n: number) => void; min: number; max: number; hint?: string }) {
  return (
    <div><label className="label">{label}</label>
      <input className="input" type="number" min={min} max={max} value={value} onChange={e => onChange(Math.max(min, Math.min(max, Number(e.target.value) || min)))} />
      {hint && <div className="text-xs text-muted mt-1">{hint}</div>}</div>
  )
}
function Time({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  return <div><label className="label">{label}</label><input className="input" type="time" value={value} onChange={e => onChange(e.target.value)} /></div>
}

export function ScheduleView({ data, runs, busy, onSave, onReset, onRunNow }: {
  data: any; runs: any[]; busy: boolean; onSave: (patch: any) => void; onReset: () => void; onRunNow: (agents: string[]) => void
}) {
  const [d, setD] = useState<any>(data.config)
  useEffect(() => setD(data.config), [data])
  const set = (k: string, v: any) => setD({ ...d, [k]: v })
  const dirty = JSON.stringify(d) !== JSON.stringify(data.config)
  const planned = d.posts_per_expert_per_day * Object.values(d.experts).filter(Boolean).length

  return (
    <>
      <Section title="Posting schedule" hint={`Posts are spread across the active window (${data.timezone}, now ${data.now}). Experts are staggered so they don't all post at once.`}
        right={<div className="flex gap-2"><button className="btn-ghost" disabled={busy} onClick={onReset}>Reset to defaults</button><button className="btn-grad" disabled={busy || !dirty} onClick={() => onSave(d)}>Save changes</button></div>}>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <Num label="Posts per expert per day" value={d.posts_per_expert_per_day} min={0} max={6} onChange={v => set('posts_per_expert_per_day', v)} hint={`≈ ${planned} new posts a day`} />
          <Time label="Active from" value={d.active_start} onChange={v => set('active_start', v)} />
          <Time label="Active until" value={d.active_end} onChange={v => set('active_end', v)} />
          <Num label="Max posts per pass" value={d.max_per_tick} min={1} max={5} onChange={v => set('max_per_tick', v)} hint="Avoids bursts after a restart" />
        </div>
        <div className="grid sm:grid-cols-2 gap-x-8 gap-y-4 mt-5">
          <Toggle on={d.approve_first} onChange={v => set('approve_first', v)} label="Approve first: new posts wait in the review queue" />
          <Toggle on={d.reviewed_only} onChange={v => set('reviewed_only', v)} label="Reviewed-only: experts use only reviewed fact cards" />
          <Toggle on={d.alerts_enabled} onChange={v => set('alerts_enabled', v)} label="Daily city alerts by Terra" />
          <Toggle on={d.quizzes_enabled} onChange={v => set('quizzes_enabled', v)} label="Live quizzes" />
        </div>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-5">
          <Time label="City alerts at" value={d.alerts_time} onChange={v => set('alerts_time', v)} />
          <div><label className="label">Quiz times (comma separated)</label>
            <input className="input" defaultValue={d.quiz_times.join(', ')} key={d.quiz_times.join(',')} onBlur={e => set('quiz_times', e.target.value.split(',').map((x: string) => x.trim()).filter(Boolean))} /></div>
          <Num label="Review queue limit" value={d.max_pending} min={1} max={200} onChange={v => set('max_pending', v)} hint="Generation pauses when full" />
          <Num label="Retry after failure (min)" value={d.failure_backoff_min} min={1} max={720} onChange={v => set('failure_backoff_min', v)} />
        </div>
        <div className="mt-5"><div className="label">Experts</div>
          <div className="flex flex-wrap gap-2">{data.experts.map((e: any) => (
            <button key={e.id} onClick={() => set('experts', { ...d.experts, [e.id]: !d.experts[e.id] })}
              className={`chip !py-1.5 transition ${d.experts[e.id] ? '!border-brand-violet/50 !bg-brand-violet/10 !text-ink' : 'opacity-50'}`}>{e.emoji} {e.name}</button>
          ))}</div></div>
        <div className="mt-4"><div className="label">Post types</div>
          <div className="flex flex-wrap gap-2">{data.formats.map((f: string) => (
            <button key={f} onClick={() => set('formats', { ...d.formats, [f]: !d.formats[f] })}
              className={`chip !py-1.5 transition ${d.formats[f] ? '!border-brand-violet/50 !bg-brand-violet/10 !text-ink' : 'opacity-50'}`}>{f.replace('_', ' ')}</button>
          ))}</div></div>
      </Section>

      <Section title="Today" hint="When each expert's next post is due, and what's been posted."
        right={<button className="btn-ghost" disabled={busy} onClick={() => onRunNow([])}>⚡ Generate now (all)</button>}>
        <table className="w-full text-sm">
          <thead><tr className="text-left text-muted text-xs"><th className="py-1.5">Expert</th><th>Due at</th><th>Due</th><th>Posted</th><th>Status</th><th /></tr></thead>
          <tbody>{data.schedule.map((r: any) => (
            <tr key={r.agent} className="border-t border-line">
              <td className="py-2 font-semibold">{r.name}</td><td>{r.enabled ? r.slots.join(', ') || '–' : 'off'}</td><td>{r.due}</td><td>{r.done}</td>
              <td>{!r.enabled ? <Badge>off</Badge> : r.behind > 0 ? <Badge tone="warn">{r.behind} behind</Badge> : <Badge tone="ok">on track</Badge>}</td>
              <td className="text-right"><button className="btn-ghost !py-1 !px-3" disabled={busy} onClick={() => onRunNow([r.agent])}>Generate</button></td></tr>
          ))}</tbody>
        </table>
      </Section>

      <Section title="Recent pipeline runs" hint="Every pass that created something or hit a problem.">
        {runs.length === 0 ? <p className="text-sm text-muted">No runs yet.</p> : (
          <div className="space-y-2">{runs.map((r: any) => (
            <div key={r.id} className="rounded-2xl border border-line p-3 text-sm">
              <div className="flex flex-wrap items-center gap-2"><b>{when(r.ts)}</b><Badge>{r.source}</Badge><span className="text-muted">{r.ms} ms</span></div>
              {r.actions.map((a: any, i: number) => (
                <div key={i} className="mt-1">{a.type === 'post' ? <>📝 <b>{a.agent}</b> · {a.kind} · <Badge tone={a.status === 'live' ? 'ok' : 'warn'}>{a.status}</Badge> <Badge tone={a.source === 'gemini' ? 'info' : 'mute'}>{a.source}</Badge> {a.title}</>
                  : a.type === 'alert' ? <>🌦️ Alert for {a.city}</> : <>⚡ Quiz: {a.title}</>}</div>
              ))}
              {r.errors.map((e: any, i: number) => <div key={i} className="mt-1 text-bad">⚠️ {e.agent ? `${e.agent}: ` : ''}{e.error}</div>)}
            </div>
          ))}</div>
        )}
      </Section>
    </>
  )
}
