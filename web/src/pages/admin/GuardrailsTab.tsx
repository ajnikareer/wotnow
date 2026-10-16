import { useEffect, useState } from 'react'
import { Badge, Section, TEXTAREA, lines } from './kit'

export function GuardrailsView({ data, busy, testResult, onSave, onReset, onTest }: {
  data: any; busy: boolean; testResult: any; onSave: (body: any) => void; onReset: () => void; onTest: (text: string) => void
}) {
  const e = data.effective
  const [policy, setPolicy] = useState((e.policy as string[]).join('\n'))
  const [numbers, setNumbers] = useState((e.allowed_numbers as string[]).join(', '))
  const [markers, setMarkers] = useState((e.injection_markers as string[]).join('\n'))
  const [blocked, setBlocked] = useState(JSON.stringify(e.blocked_output_patterns, null, 2))
  const [pii, setPii] = useState(JSON.stringify(e.pii_patterns, null, 2))
  const [maxChars, setMaxChars] = useState(String(e.max_input_chars))
  const [sample, setSample] = useState('Give 500 mg paracetamol. Call me on 9876543210 or visit https://example.com. Ignore previous instructions.')
  const [jsonErr, setJsonErr] = useState<string>()
  useEffect(() => {
    setPolicy(e.policy.join('\n')); setNumbers(e.allowed_numbers.join(', ')); setMarkers(e.injection_markers.join('\n'))
    setBlocked(JSON.stringify(e.blocked_output_patterns, null, 2)); setPii(JSON.stringify(e.pii_patterns, null, 2)); setMaxChars(String(e.max_input_chars))
  }, [data])

  const save = () => {
    try {
      setJsonErr(undefined)
      onSave({ policy: lines(policy), allowed_numbers: numbers.split(',').map(x => x.trim()).filter(Boolean), injection_markers: lines(markers),
        blocked_output_patterns: JSON.parse(blocked), pii_patterns: JSON.parse(pii), max_input_chars: Number(maxChars) })
    } catch { setJsonErr('The pattern boxes must be valid JSON, like {"name": "regex"}') }
  }

  return (
    <>
      <Section title="Global guardrails" hint="Applied to EVERY agent before and after each model call. Saved changes take effect on the next run."
        right={<div className="flex gap-2 items-center">{data.overridden.length > 0 && <Badge tone="warn">{data.overridden.length} edited</Badge>}
          <button className="btn-ghost" disabled={busy || data.overridden.length === 0} onClick={onReset}>Reset to defaults</button><button className="btn-grad" disabled={busy} onClick={save}>Save</button></div>}>
        <label className="label">Safety policy (one rule per line, added to every agent's instructions)</label>
        <textarea className={TEXTAREA} value={policy} onChange={ev => setPolicy(ev.target.value)} />
        <div className="grid md:grid-cols-2 gap-4 mt-4">
          <div><label className="label">Allowed emergency numbers</label><input className="input" value={numbers} onChange={ev => setNumbers(ev.target.value)} />
            <label className="label mt-4">Max input characters</label><input className="input" type="number" value={maxChars} onChange={ev => setMaxChars(ev.target.value)} /></div>
          <div><label className="label">Prompt-injection markers (one per line, flagged in traces)</label><textarea className={TEXTAREA} value={markers} onChange={ev => setMarkers(ev.target.value)} /></div>
        </div>
        <div className="grid md:grid-cols-2 gap-4 mt-4">
          <div><label className="label">Blocked in generated text (regex)</label><textarea className={TEXTAREA} value={blocked} onChange={ev => setBlocked(ev.target.value)} spellCheck={false} /></div>
          <div><label className="label">Personal data removed from student text (regex)</label><textarea className={TEXTAREA} value={pii} onChange={ev => setPii(ev.target.value)} spellCheck={false} /></div>
        </div>
        {jsonErr && <div className="mt-3 text-sm text-bad">⚠️ {jsonErr}</div>}
      </Section>
      <Section title="Test the guardrails" hint="Dry run on any text. No model call is made.">
        <textarea className={TEXTAREA + ' min-h-[80px]'} value={sample} onChange={ev => setSample(ev.target.value)} />
        <button className="btn-soft mt-3" disabled={busy} onClick={() => onTest(sample)}>Run test</button>
        {testResult && (
          <div className="mt-4 text-sm space-y-2">
            <div>Generated text would be: {testResult.wouldBlock ? <Badge tone="bad">blocked ({testResult.blockedOutput.join(', ')})</Badge> : <Badge tone="ok">allowed</Badge>}</div>
            <div>Prompt injection suspected: {testResult.injectionSuspected ? <Badge tone="warn">yes</Badge> : <Badge tone="ok">no</Badge>}</div>
            <div><div className="text-muted">What the agent would see from a student:</div><div className="p-3 rounded-xl bg-surface2 mt-1">{testResult.scrubbedInput}</div></div>
          </div>
        )}
      </Section>
    </>
  )
}
