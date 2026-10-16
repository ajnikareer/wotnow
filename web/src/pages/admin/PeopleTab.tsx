import { Section, Stat, when } from './kit'

export function PeopleView({ people, audit }: { people: any; audit: any[] }) {
  return (
    <>
      <Section title="People" hint="Students are known only by nickname. Parent accounts show the Google email.">
        <div className="grid grid-cols-2 md:grid-cols-5 gap-3 mb-4">
          <Stat label="Students" value={people.students} /><Stat label="Parent accounts" value={people.accounts} />
          <Stat label="Classes 3–5" value={people.byBand.junior} /><Stat label="Classes 6–8" value={people.byBand.middle} /><Stat label="Classes 9–12" value={people.byBand.senior} />
        </div>
        <div className="grid md:grid-cols-2 gap-5">
          <div><div className="font-semibold mb-2">Top by XP</div>{people.top.map((u: any, i: number) => (
            <div key={i} className="flex justify-between text-sm py-1.5 border-t border-line"><span>{i + 1}. {u.nickname} <span className="text-muted">· class {u.grade} · {u.city}</span></span><b>{u.xp}</b></div>))}</div>
          <div><div className="font-semibold mb-2">Parent accounts</div>{people.accountsList.length === 0 && <p className="text-sm text-muted">No Google accounts yet.</p>}
            {people.accountsList.map((a: any, i: number) => (
              <div key={i} className="flex justify-between text-sm py-1.5 border-t border-line"><span>{a.email} <span className="text-muted">· {a.children} child{a.children === 1 ? '' : 'ren'}</span></span><span className="text-muted">{when(a.lastLogin)}</span></div>))}</div>
        </div>
      </Section>
      <Section title="Audit log" hint="Who changed what in the admin console.">
        {audit.length === 0 ? <p className="text-sm text-muted">Nothing yet.</p> : audit.map(a => (
          <div key={a.id} className="text-sm py-1.5 border-t border-line"><span className="text-muted">{when(a.ts)}</span> · <b>{a.actor}</b> · {a.action} <span className="text-muted">{a.target}</span></div>))}
      </Section>
    </>
  )
}
