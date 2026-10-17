import { useEffect, useRef, useState } from 'react'
import { Logo, Mascot } from '../components/Brand'
import { ThemeToggle } from '../components/ui'
import { authApi, type Account, type AuthConfig } from '../lib/api'
import { navigate, useRoute } from '../lib/router'
import { useSession } from '../lib/session'

/** Loads Google Identity Services once. Fails with a clear message when accounts.google.com isn't reachable. */
export function loadGsi(): Promise<any> {
  const w = window as any
  if (w.google?.accounts?.id) return Promise.resolve(w.google)
  return new Promise((resolve, reject) => {
    const s = document.createElement('script')
    s.src = 'https://accounts.google.com/gsi/client'
    s.async = true
    s.defer = true
    s.onload = () => resolve((window as any).google)
    s.onerror = () => reject(new Error('Could not load Google sign-in. Is accounts.google.com reachable from this network?'))
    document.head.appendChild(s)
  })
}

export interface SignInViewProps {
  cfg?: AuthConfig; err?: string; busy: boolean; expired: boolean
  email: string; name: string; setEmail: (v: string) => void; setName: (v: string) => void
  onDev: () => void; onDemo: () => void; boxRef?: { current: HTMLDivElement | null }
}

/** The sign-in page itself (no logic): Google button, the test sign-in (only when the server offers it) and the demo. */
export function SignInView({ cfg, err, busy, expired, email, name, setEmail, setName, onDev, onDemo, boxRef }: SignInViewProps) {
  const canDev = /^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(email.trim())
  const nothing = !!cfg && !cfg.googleEnabled && !cfg.devLogin
  return (
    <div className="min-h-screen flex flex-col">
      <header className="flex items-center px-5 py-4 max-w-3xl w-full mx-auto"><a href="#/"><Logo className="h-9" /></a><div className="ml-auto"><ThemeToggle compact /></div></header>
      <div className="flex-1 grid place-items-center px-5 pb-16">
        <div className="card p-8 md:p-10 max-w-md w-full text-center animate-rise">
          <Mascot mood="look" size={84} className="mx-auto" />
          <h1 className="text-2xl md:text-3xl font-bold mt-3">Sign in or sign up</h1>
          <p className="text-muted mt-2 text-[15px] leading-relaxed">For parents and guardians. Sign in to create your child’s profile, set time limits and see their progress. Your child never needs an account of their own.</p>

          {expired && <div className="mt-5 p-3 rounded-2xl bg-warn/10 border border-warn/25 text-sm text-left" role="status">⏱️ Your session ended. Please sign in again.</div>}

          <div className="mt-6 min-h-[48px] grid place-items-center">
            {!cfg && !err && <div className="skeleton h-11 w-64" />}
            {cfg?.googleEnabled && <div ref={boxRef} data-testid="google-button" className={busy ? 'opacity-50 pointer-events-none' : ''} />}
          </div>

          {cfg?.devLogin && (
            <div className="mt-5 rounded-2xl border border-warn/30 bg-warn/[.06] p-4 text-left" data-testid="dev-login">
              <div className="text-[11px] font-extrabold tracking-wider text-warn">TEST SIGN-IN · NOT FOR PRODUCTION</div>
              <p className="text-[13px] text-muted mt-1">This server can’t use Google sign-in, so you can sign in as any email without a password. It’s switched off on the live site.</p>
              <label className="label mt-3">Email</label>
              <input className="input" type="email" autoComplete="email" placeholder="parent@example.com" value={email} onChange={e => setEmail(e.target.value)}
                onKeyDown={e => { if (e.key === 'Enter' && canDev && !busy) onDev() }} />
              <label className="label mt-3">Name (optional)</label>
              <input className="input" autoComplete="name" placeholder="e.g. Priya" value={name} maxLength={60} onChange={e => setName(e.target.value)} />
              <button className="btn-grad w-full mt-4" disabled={!canDev || busy} onClick={onDev}>{busy ? 'Signing in…' : 'Continue with this email'}</button>
            </div>
          )}

          {nothing && (
            <div className="mt-2 p-4 rounded-2xl bg-surface2 border border-line text-sm text-muted text-left" data-testid="no-signin">Signing in isn’t switched on for this server yet. You can still try the app with the shared demo student below.</div>
          )}
          {busy && !cfg?.devLogin && <div className="text-sm text-muted mt-3">Signing you in…</div>}
          {err && <div className="mt-4 p-3 rounded-2xl bg-bad/10 border border-bad/25 text-sm text-left" role="alert">⚠️ {err}</div>}

          {(!cfg || cfg.allowDemo) && (
            <>
              <div className="flex items-center gap-3 my-5 text-xs text-faint"><span className="flex-1 h-px bg-line" />or<span className="flex-1 h-px bg-line" /></div>
              <button className="btn-ghost w-full" onClick={onDemo}>Try the student demo</button>
              <p className="text-[11.5px] text-faint mt-2">No sign-in. You’ll use a shared demo student.</p>
            </>
          )}
          <p className="text-[11.5px] text-faint mt-5 leading-relaxed">By continuing you confirm you’re a parent or legal guardian. We only receive your name and email. Children are identified by a nickname, class and city, and you can delete everything anytime.</p>
        </div>
      </div>
    </div>
  )
}

/** Sign in or sign up (the same step: the first Google sign-in creates the family account). */
export default function SignIn() {
  const { kind, loginWithToken, enterChild, enterDemo } = useSession()
  const { query } = useRoute()
  const [cfg, setCfg] = useState<AuthConfig>()
  const [err, setErr] = useState<string>()
  const [busy, setBusy] = useState(false)
  const [email, setEmail] = useState('')
  const [name, setName] = useState('')
  const box = useRef<HTMLDivElement>(null)
  const finishing = useRef(false)                      // true while a sign-in is being completed, so the redirect below doesn't race it

  useEffect(() => { authApi.config().then(setCfg).catch(e => setErr(e.message)) }, [])
  useEffect(() => { if (kind === 'account' && !finishing.current) navigate('/family') }, [kind])   // already signed in

  /** One child → straight to their feed. None or several → "Who's learning?". */
  const complete = async (token: string, account: Account) => {
    finishing.current = true
    loginWithToken(token)
    if (account.children.length === 1) { await enterChild(account.children[0].id, 'student'); navigate('/feed') }
    else navigate('/family')
  }

  useEffect(() => {
    if (!cfg?.googleEnabled) return
    let dead = false
    loadGsi().then(google => {
      if (dead || !box.current) return
      google.accounts.id.initialize({
        client_id: cfg.googleClientId,
        auto_select: false,
        callback: async (resp: any) => {
          setBusy(true); setErr(undefined)
          try { const r = await authApi.google(resp.credential); await complete(r.token, r.account) }
          catch (e: any) { finishing.current = false; setErr(e.message); setBusy(false) }
        },
      })
      google.accounts.id.renderButton(box.current, { theme: 'outline', size: 'large', shape: 'pill', text: 'continue_with', width: 300 })
    }).catch(e => setErr(e.message))
    return () => { dead = true }
  }, [cfg])  // eslint-disable-line react-hooks/exhaustive-deps

  const devSignIn = async () => {
    setBusy(true); setErr(undefined)
    try { const r = await authApi.devLogin(email.trim(), name.trim()); await complete(r.token, r.account) }
    catch (e: any) { finishing.current = false; setErr(e.message); setBusy(false) }
  }
  const demo = () => { enterDemo('student'); navigate('/feed') }

  return <SignInView cfg={cfg} err={err} busy={busy} expired={query.get('expired') === '1'} email={email} name={name} setEmail={setEmail} setName={setName}
    onDev={devSignIn} onDemo={demo} boxRef={box} />
}
