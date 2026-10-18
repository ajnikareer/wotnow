import { useCallback, useEffect, useRef, useState } from 'react'
import { Logo } from '../../components/Brand'
import { ThemeToggle } from '../../components/ui'
import { admin, AdminAuthError, adminToken, setAdminToken } from '../../lib/adminApi'
import { Link } from '../../lib/router'
import { AGENTS } from '../../mocks/data'
import { AgentsView } from './AgentsTab'
import { CardsView } from './CardsTab'
import { EvalsView } from './EvalsTab'
import { GuardrailsView } from './GuardrailsTab'
import { ErrorBox, Loading, useAction } from './kit'
import { OverviewView } from './OverviewTab'
import { PeopleView } from './PeopleTab'
import { ReviewView } from './ReviewTab'
import { ScheduleView } from './ScheduleTab'
import { TracesView } from './TracesTab'

const TABS: [string, string][] = [['overview', 'Overview'], ['schedule', 'Schedule'], ['review', 'Review'], ['agents', 'Agents'], ['guardrails', 'Guardrails'],
  ['cards', 'Fact cards'], ['evals', 'Evaluations'], ['traces', 'Traces'], ['people', 'People & audit']]
const SKILLS = ['write_scenario', 'write_poll', 'write_myth_fact', 'write_scam_legit', 'review_post', 'judge', 'moderate', 'expert_reply', 'local_alert', 'live_quiz', 'parent_coach']

/** Loads once; `data` can be replaced by the response of a save (most admin writes return the new state). */
function useLoaded<T>(path: string, deps: unknown[] = []) {
  const [data, setData] = useState<T | null>(null)
  const [error, setError] = useState<string>()
  const load = useCallback(() => { setError(undefined); admin.get<T>(path).then(setData).catch(e => setError(e.message)) }, [path])
  useEffect(() => { load() }, [load, ...deps])  // eslint-disable-line react-hooks/exhaustive-deps
  return { data, setData, error, load }
}

/* ------------------------------------------------------------------ tabs (containers) */
function Overview() {
  const { data, error, load } = useLoaded<any>('/overview')
  const { busy, run } = useAction()
  if (error) return <ErrorBox message={error} onRetry={load} />
  if (!data) return <Loading />
  return <OverviewView data={data} busy={busy} onRefresh={load}
    onPause={p => run(async () => { await admin.post('/pipeline/pause', { paused: p }); load() }, p ? 'Posting paused' : 'Posting resumed')}
    onRunNow={() => run(async () => { await admin.post('/pipeline/run-now', {}); }, 'Started. New posts appear in a few minutes; see the Schedule tab.')} />
}

function Schedule() {
  const p = useLoaded<any>('/pipeline')
  const r = useLoaded<any>('/pipeline/runs?limit=15')
  const { busy, run } = useAction()
  useEffect(() => { const t = setInterval(() => { p.load(); r.load() }, 10000); return () => clearInterval(t) }, [])  // eslint-disable-line react-hooks/exhaustive-deps
  if (p.error) return <ErrorBox message={p.error} onRetry={p.load} />
  if (!p.data) return <Loading />
  return <ScheduleView data={p.data} runs={r.data?.runs ?? []} busy={busy}
    onSave={patch => run(async () => p.setData(await admin.put('/pipeline', patch)), 'Schedule saved')}
    onReset={() => run(async () => p.setData(await admin.post('/pipeline/reset')), 'Back to defaults')}
    onRunNow={agents => run(async () => { await admin.post('/pipeline/run-now', agents.length ? { agents } : {}); setTimeout(() => { p.load(); r.load() }, 4000) }, 'Started. Results appear under “Recent pipeline runs”.')} />
}

function Review() {
  const [filters, setFilters] = useState({ status: 'pending', agent: '' })
  const [open, setOpen] = useState<string | null>(null)
  const [detail, setDetail] = useState<any>(null)
  const q = `/posts?limit=60${filters.status ? `&status=${filters.status}` : ''}${filters.agent ? `&agent=${filters.agent}` : ''}`
  const list = useLoaded<any>(q)
  const { busy, run } = useAction()
  const openPost = (id: string | null) => {
    setOpen(id); setDetail(null)
    if (id) admin.get(`/posts/${id}`).then(setDetail).catch(() => setDetail(null))
  }
  if (list.error) return <ErrorBox message={list.error} onRetry={list.load} />
  return <ReviewView posts={list.data?.posts ?? []} total={list.data?.total ?? 0} experts={AGENTS} filters={filters} setFilters={setFilters} open={open} detail={detail} busy={busy} onOpen={openPost}
    onStatus={(id, status) => run(async () => { const d = await admin.post(`/posts/${id}/status`, { status }); setDetail((x: any) => (x ? { ...x, status: d.status } : x)); list.load() }, `Post is now ${status}`)} />
}

function Agents() {
  const { data, setData, error, load } = useLoaded<any>('/agents')
  const { busy, run } = useAction()
  if (error) return <ErrorBox message={error} onRetry={load} />
  if (!data) return <Loading />
  return <AgentsView data={data} busy={busy}
    onSaveSkill={(s, b) => run(async () => setData(await admin.put(`/agents/skills/${s}`, b)), 'Saved')}
    onResetSkill={s => run(async () => setData(await admin.del(`/agents/skills/${s}`)), 'Reset to default')}
    onSaveInstruction={(f, text) => run(async () => setData(await admin.put(`/agents/instructions/${f}`, { text })), 'Instruction saved. Live on the next run.')}
    onResetInstruction={f => run(async () => setData(await admin.del(`/agents/instructions/${f}`)), 'Reset to default')} />
}

function Guardrails() {
  const { data, setData, error, load } = useLoaded<any>('/guardrails')
  const [test, setTest] = useState<any>(null)
  const { busy, run } = useAction()
  if (error) return <ErrorBox message={error} onRetry={load} />
  if (!data) return <Loading />
  return <GuardrailsView data={data} busy={busy} testResult={test}
    onSave={b => run(async () => setData(await admin.put('/guardrails', b)), 'Guardrails saved. Live on the next run.')}
    onReset={() => run(async () => setData(await admin.del('/guardrails')), 'Reset to defaults')}
    onTest={text => run(async () => setTest(await admin.post('/guardrails/test', { text })))} />
}

function Cards() {
  const [agent, setAgent] = useState('')
  const { data, setData, error, load } = useLoaded<any>(`/cards${agent ? `?agent=${agent}` : ''}`)
  const { busy, run } = useAction()
  if (error) return <ErrorBox message={error} onRetry={load} />
  if (!data) return <Loading />
  const replace = (row: any) => setData({ ...data, cards: data.cards.map((c: any) => (c.id === row.id ? row : c)) })
  return <CardsView cards={data.cards} reviewedOnly={data.reviewedOnly} experts={AGENTS} agent={agent} setAgent={setAgent} busy={busy}
    onSave={(id, b) => run(async () => replace(await admin.put(`/cards/${id}`, b)), 'Card saved')}
    onReset={id => run(async () => replace(await admin.del(`/cards/${id}`)), 'Card reset')}
    onReviewedOnly={v => run(async () => { await admin.put('/pipeline', { reviewed_only: v }); load() }, v ? 'Reviewed-only mode on' : 'Reviewed-only mode off')} />
}

function Evals() {
  const { data, setData, error, load } = useLoaded<any>('/evals')
  const [runDoc, setRunDoc] = useState<any>(null)
  const alive = useRef(true)
  const { busy, run } = useAction()
  useEffect(() => { alive.current = true; return () => { alive.current = false } }, [])
  const poll = async (id: string) => {
    for (let i = 0; i < 240 && alive.current; i++) {
      const d = await admin.get(`/evals/runs/${id}`)
      if (!alive.current) return
      setRunDoc(d)
      if (d.status !== 'running') { load(); return }
      await new Promise(r => setTimeout(r, 1500))
    }
  }
  if (error) return <ErrorBox message={error} onRetry={load} />
  if (!data) return <Loading />
  return <EvalsView data={data} run={runDoc} busy={busy}
    onRun={() => run(async () => { const r = await admin.post('/evals/run'); setRunDoc({ status: 'running', done: 0, total: data.cases.length }); poll(r.runId) })}
    onOpenRun={id => run(async () => setRunDoc(await admin.get(`/evals/runs/${id}`)))}
    onSaveCases={json => run(async () => setData(await admin.put('/evals/cases', json)), 'Test cases saved')}
    onResetCases={() => run(async () => setData(await admin.del('/evals/cases')), 'Back to the shipped test cases')} />
}

function Traces() {
  const [filters, setFilters] = useState({ skill: '', ok: '' })
  const q = `/traces?limit=100${filters.skill ? `&skill=${filters.skill}` : ''}${filters.ok ? `&ok=${filters.ok}` : ''}`
  const { data, error, load } = useLoaded<any>(q)
  if (error) return <ErrorBox message={error} onRetry={load} />
  return <TracesView traces={data?.traces ?? []} skills={SKILLS} filters={filters} setFilters={setFilters} onRefresh={load} />
}

function People() {
  const p = useLoaded<any>('/people')
  const a = useLoaded<any>('/audit?limit=60')
  if (p.error) return <ErrorBox message={p.error} onRetry={p.load} />
  if (!p.data) return <Loading />
  return <PeopleView people={p.data} audit={a.data?.audit ?? []} />
}

/* ------------------------------------------------------------------ gate + shell */
function Gate({ onToken, message }: { onToken: (t: string) => void; message?: string }) {
  const [t, setT] = useState('')
  return (
    <div className="min-h-[70vh] grid place-items-center px-5">
      <div className="card p-8 max-w-md w-full">
        <h1 className="text-2xl font-bold">Admin sign-in</h1>
        <p className="text-sm text-muted mt-1">Sign in with a Google account on the admin list, or paste the admin token.</p>
        <Link to="/signin" className="btn-ghost w-full mt-5">Sign in with Google</Link>
        <div className="text-center text-xs text-muted my-3">or</div>
        <input className="input" type="password" placeholder="Admin token" value={t} onChange={e => setT(e.target.value)} onKeyDown={e => e.key === 'Enter' && t && onToken(t)} />
        <button className="btn-grad w-full mt-3" disabled={!t} onClick={() => onToken(t)}>Open admin</button>
        {message && <div className="mt-4 p-3 rounded-2xl bg-bad/10 border border-bad/25 text-sm">⚠️ {message}</div>}
      </div>
    </div>
  )
}

export default function AdminPage() {
  const [state, setState] = useState<'checking' | 'ok' | 'denied' | 'error'>('checking')
  const [msg, setMsg] = useState<string>()
  const [tab, setTab] = useState('overview')

  const check = useCallback(() => {
    setState('checking')
    admin.get('/overview').then(() => setState('ok')).catch(e => { if (e instanceof AdminAuthError) { setState('denied'); setMsg(adminToken() ? 'That token or account was not accepted.' : undefined) } else { setState('error'); setMsg(e.message) } })
  }, [])
  useEffect(() => { check() }, [check])
  const out = () => { setAdminToken(''); setState('denied'); setMsg(undefined) }

  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-30 bg-bg/80 backdrop-blur-xl border-b border-line">
        <div className="max-w-6xl mx-auto flex items-center gap-3 px-4 md:px-6 h-16">
          <Logo className="h-6.5" /><span className="chip !bg-brand-violet/10 !border-brand-violet/30 !text-brand-violet font-bold">Admin</span>
          <div className="ml-auto flex items-center gap-2"><Link to="/" className="btn-ghost hidden sm:inline-flex">Back to app</Link><ThemeToggle compact />
            {state === 'ok' && <button className="btn-ghost" onClick={out}>Sign out</button>}</div>
        </div>
        {state === 'ok' && (
          <nav className="max-w-6xl mx-auto px-4 md:px-6 flex gap-1 overflow-x-auto no-scrollbar">
            {TABS.map(([k, l]) => (
              <button key={k} onClick={() => setTab(k)} className={`px-3 py-2.5 text-sm font-bold whitespace-nowrap border-b-2 transition ${tab === k ? 'border-brand-violet text-ink' : 'border-transparent text-muted hover:text-ink'}`}>{l}</button>
            ))}
          </nav>
        )}
      </header>
      <main className="max-w-6xl mx-auto px-4 md:px-6 py-6 pb-24">
        {state === 'checking' && <Loading text="Checking access…" />}
        {state === 'error' && <ErrorBox message={msg || 'Could not reach the server'} onRetry={check} />}
        {state === 'denied' && <Gate message={msg} onToken={t => { setAdminToken(t); check() }} />}
        {state === 'ok' && (
          <>
            {tab === 'overview' && <Overview />}{tab === 'schedule' && <Schedule />}{tab === 'review' && <Review />}{tab === 'agents' && <Agents />}
            {tab === 'guardrails' && <Guardrails />}{tab === 'cards' && <Cards />}{tab === 'evals' && <Evals />}{tab === 'traces' && <Traces />}{tab === 'people' && <People />}
          </>
        )}
      </main>
    </div>
  )
}
