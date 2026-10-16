import { useEffect, useState } from 'react'
import { Badge, Section, TEXTAREA, Toggle } from './kit'

function SkillRow({ s, busy, onSave, onReset }: { s: any; busy: boolean; onSave: (skill: string, body: any) => void; onReset: (skill: string) => void }) {
  const [t, setT] = useState<string>(String(s.temperature ?? ''))
  useEffect(() => setT(String(s.temperature ?? '')), [s.temperature])
  return (
    <tr className="border-t border-line align-top">
      <td className="py-2.5 pr-3"><div className="font-semibold">{s.skill}</div><div className="text-xs text-muted max-w-xs">{s.description}</div>
        <div className="text-xs mt-1 flex gap-1 flex-wrap"><Badge>{s.agent}</Badge>{s.perExpert && <Badge tone="info">per expert</Badge>}{s.reviewedBy && <Badge tone="ok">reviewed by safety agent</Badge>}</div></td>
      <td className="pr-3"><input className="input !py-1.5 !w-20" type="number" step="0.1" min={0} max={2} value={t} onChange={e => setT(e.target.value)} onBlur={() => t !== String(s.temperature) && onSave(s.skill, { temperature: t })} /></td>
      <td className="pr-3">{s.hasReviewOption ? <Toggle on={!!s.reviewedBy} disabled={busy} onChange={v => onSave(s.skill, { review: v })} /> : <span className="text-muted">–</span>}</td>
      <td className="pr-3"><Toggle on={s.guardrails.piiScrub} disabled={busy} onChange={v => onSave(s.skill, { pii_scrub: v })} /></td>
      <td className="pr-3"><Toggle on={s.guardrails.outputScan} disabled={busy} onChange={v => onSave(s.skill, { guard_output: v })} /></td>
      <td className="text-right">{s.overridden.length > 0 ? <button className="btn-ghost !py-1 !px-3" disabled={busy} onClick={() => onReset(s.skill)}>Reset ({s.overridden.length})</button> : <span className="text-xs text-muted">default</span>}</td>
    </tr>
  )
}

export function AgentsView({ data, busy, onSaveSkill, onResetSkill, onSaveInstruction, onResetInstruction }: {
  data: any; busy: boolean; onSaveSkill: (skill: string, body: any) => void; onResetSkill: (skill: string) => void
  onSaveInstruction: (file: string, text: string) => void; onResetInstruction: (file: string) => void
}) {
  const [file, setFile] = useState<string>(data.instructions[0]?.file ?? '')
  const ins = data.instructions.find((i: any) => i.file === file) ?? data.instructions[0]
  const [text, setText] = useState<string>(ins?.text ?? '')
  useEffect(() => setText(ins?.text ?? ''), [ins?.file, ins?.text])
  return (
    <>
      <Section title="Experts" hint="Each expert is the same model with its own persona and fact cards. Personas are edited in content/agents.json; their knowledge in the Fact cards tab.">
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3">{data.experts.map((e: any) => (
          <div key={e.id} className="rounded-2xl border border-line p-3"><div className="font-bold">{e.emoji} {e.name} <span className="text-muted font-normal">· {e.domain}</span></div>
            <div className="text-xs text-muted mt-1">{e.persona}</div><div className="mt-2"><Badge tone="info">{e.cards} cards in use</Badge></div></div>
        ))}</div>
      </Section>
      <Section title="Skills" hint={`Runtime: ${data.runtime} · provider: ${data.provider}. Changes apply to the next agent run (no redeploy).`}>
        <div className="overflow-x-auto"><table className="w-full text-sm">
          <thead><tr className="text-left text-muted text-xs"><th className="py-1.5">Skill</th><th>Temperature</th><th>Safety review</th><th>PII scrub</th><th>Output scan</th><th /></tr></thead>
          <tbody>{data.skills.map((s: any) => <SkillRow key={s.skill} s={s} busy={busy} onSave={onSaveSkill} onReset={onResetSkill} />)}</tbody>
        </table></div>
        <p className="text-xs text-muted mt-3">Temperature: low = consistent (judging), high = creative (writing). Safety review adds the second agent that checks each draft against the fact cards.</p>
      </Section>
      <Section title="Agent instructions" hint="The text each agent follows. Placeholders in curly braces are filled in per run.">
        <div className="flex flex-wrap items-center gap-2 mb-3">
          <select className="input !py-2 !w-auto" value={file} onChange={e => setFile(e.target.value)}>{data.instructions.map((i: any) => <option key={i.file} value={i.file}>{i.file}{i.overridden ? ' ●' : ''}</option>)}</select>
          {ins?.overridden && <Badge tone="warn">edited</Badge>}
          <span className="text-xs text-muted">used by: {ins?.usedBy.join(', ')}</span>
        </div>
        <textarea className={TEXTAREA + ' min-h-[240px]'} value={text} onChange={e => setText(e.target.value)} spellCheck={false} />
        <div className="text-xs text-muted mt-1">Allowed placeholders: {data.placeholders.map((p: string) => `{${p}}`).join('  ')}. Don't use other curly braces.</div>
        <div className="flex gap-2 mt-3">
          <button className="btn-grad" disabled={busy || text === ins?.text} onClick={() => onSaveInstruction(file, text)}>Save instruction</button>
          <button className="btn-ghost" disabled={busy || !ins?.overridden} onClick={() => onResetInstruction(file)}>Reset to default</button>
        </div>
      </Section>
    </>
  )
}
