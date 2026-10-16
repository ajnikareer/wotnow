import { useEffect, useState } from 'react'
import { Badge, Section, TEXTAREA, Toggle, lines } from './kit'

function CardRow({ c, busy, onSave, onReset }: { c: any; busy: boolean; onSave: (id: string, body: any) => void; onReset: (id: string) => void }) {
  const [open, setOpen] = useState(false)
  const [title, setTitle] = useState<string>(c.title)
  const [facts, setFacts] = useState<string>(c.facts.join('\n'))
  const [dos, setDos] = useState<string>(c.do.join('\n'))
  const [donts, setDonts] = useState<string>(c.dont.join('\n'))
  useEffect(() => { setTitle(c.title); setFacts(c.facts.join('\n')); setDos(c.do.join('\n')); setDonts(c.dont.join('\n')) }, [c])
  const dirty = title !== c.title || facts !== c.facts.join('\n') || dos !== c.do.join('\n') || donts !== c.dont.join('\n')
  return (
    <div className="rounded-2xl border border-line">
      <div className="flex flex-wrap items-center gap-2 p-3">
        <button className="font-semibold text-left flex-1 min-w-[200px]" onClick={() => setOpen(!open)}>{open ? '▾' : '▸'} {c.id} · {c.title}</button>
        {c.edited && <Badge tone="warn">edited</Badge>}
        {c.hasScenario && <Badge>scenario</Badge>}{c.quizItems > 0 && <Badge>{c.quizItems} quiz</Badge>}{c.myths > 0 && <Badge>{c.myths} myths</Badge>}{c.scams > 0 && <Badge>{c.scams} scams</Badge>}
        <Toggle on={c.reviewed} disabled={busy} onChange={v => onSave(c.id, { reviewed: v })} label={c.reviewed ? `Reviewed${c.reviewedBy ? ` by ${c.reviewedBy}` : ''}` : 'Not reviewed'} />
        <Toggle on={!c.disabled} disabled={busy} onChange={v => onSave(c.id, { disabled: !v })} label={c.disabled ? 'Disabled' : 'In use'} />
      </div>
      {open && (
        <div className="border-t border-line p-4 space-y-3">
          <div><label className="label">Title</label><input className="input" value={title} onChange={e => setTitle(e.target.value)} /></div>
          <div><label className="label">Facts (one per line)</label><textarea className={TEXTAREA} value={facts} onChange={e => setFacts(e.target.value)} /></div>
          <div className="grid md:grid-cols-2 gap-3">
            <div><label className="label">Do (one per line)</label><textarea className={TEXTAREA} value={dos} onChange={e => setDos(e.target.value)} /></div>
            <div><label className="label">Don't (one per line)</label><textarea className={TEXTAREA} value={donts} onChange={e => setDonts(e.target.value)} /></div>
          </div>
          <p className="text-xs text-muted">Edits change what the AI is taught when it writes new posts, and the offline template text. The ready-made quiz questions, myths and scenario rubrics shipped with the card are not editable here.</p>
          <div className="flex gap-2">
            <button className="btn-grad" disabled={busy || !dirty} onClick={() => onSave(c.id, { title, facts: lines(facts), do: lines(dos), dont: lines(donts) })}>Save card</button>
            <button className="btn-ghost" disabled={busy || !c.edited} onClick={() => onReset(c.id)}>Reset to shipped version</button>
          </div>
        </div>
      )}
    </div>
  )
}

export function CardsView({ cards, reviewedOnly, experts, agent, setAgent, busy, onSave, onReset, onReviewedOnly }: {
  cards: any[]; reviewedOnly: boolean; experts: any[]; agent: string; setAgent: (a: string) => void; busy: boolean
  onSave: (id: string, body: any) => void; onReset: (id: string) => void; onReviewedOnly: (v: boolean) => void
}) {
  const reviewed = cards.filter(c => c.reviewed).length
  return (
    <Section title="Fact cards" hint="The only knowledge the experts may teach from. Mark a card reviewed once a qualified person has checked it."
      right={<select className="input !py-2 !w-auto" value={agent} onChange={e => setAgent(e.target.value)}><option value="">All experts</option>{experts.map(e => <option key={e.id} value={e.id}>{e.name}</option>)}</select>}>
      <div className="flex flex-wrap items-center gap-4 mb-4 p-3 rounded-2xl bg-surface2">
        <Toggle on={reviewedOnly} disabled={busy} onChange={onReviewedOnly} label="Reviewed-only mode: experts use only reviewed cards" />
        <span className="text-sm text-muted">{reviewed} of {cards.length} cards shown are reviewed</span>
        {reviewedOnly && reviewed === 0 && <Badge tone="bad">no reviewed cards: nothing can be generated</Badge>}
      </div>
      <div className="space-y-2">{cards.map(c => <CardRow key={c.id} c={c} busy={busy} onSave={onSave} onReset={onReset} />)}</div>
    </Section>
  )
}
