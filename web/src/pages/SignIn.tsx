import { useEffect, useRef, useState } from 'react'
import { Logo, Mascot } from '../components/Brand'
import { ThemeToggle } from '../components/ui'
import { authApi, type AuthConfig } from '../lib/api'
import { navigate } from '../lib/router'
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

export default function SignIn() {
  const { signIn } = useSession()
  const [cfg, setCfg] = useState<AuthConfig>()
  const [err, setErr] = useState<string>()
  const [busy, setBusy] = useState(false)
  const box = useRef<HTMLDivElement>(null)

  useEffect(() => { authApi.config().then(setCfg).catch(e => setErr(e.message)) }, [])

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
          try {
            const r = await authApi.google(resp.credential)
            localStorage.setItem('wn_token', r.token)
            localStorage.removeItem('wn_child')
            navigate('/family')
          } catch (e: any) { setErr(e.message); setBusy(false) }
        },
      })
      google.accounts.id.renderButton(box.current, { theme: 'outline', size: 'large', shape: 'pill', text: 'continue_with', width: 280 })
    }).catch(e => setErr(e.message))
    return () => { dead = true }
  }, [cfg])

  const demo = () => { signIn('student'); navigate('/feed') }

  return (
    <div className="min-h-screen flex flex-col">
      <header className="flex items-center px-5 py-4 max-w-3xl w-full mx-auto"><a href="#/"><Logo className="h-9" /></a><div className="ml-auto"><ThemeToggle compact /></div></header>
      <div className="flex-1 grid place-items-center px-5 pb-16">
        <div className="card p-8 md:p-10 max-w-md w-full text-center animate-rise">
          <Mascot mood="look" size={84} className="mx-auto" />
          <h1 className="text-2xl md:text-3xl font-bold mt-3">Parents, welcome 👋</h1>
          <p className="text-muted mt-2 text-[15px] leading-relaxed">Sign in with Google to create your child’s profile, set time limits and see their weekly progress. Your child never needs an account of their own.</p>
          <div className="mt-6 min-h-[48px] grid place-items-center">
            {!cfg && !err && <div className="skeleton h-11 w-64" />}
            {cfg?.googleEnabled && <div ref={box} className={busy ? 'opacity-50 pointer-events-none' : ''} />}
            {cfg && !cfg.googleEnabled && (
              <div className="p-4 rounded-2xl bg-surface2 border border-line text-sm text-muted">Google sign-in isn’t switched on for this server yet. You can still try the app as a demo student.</div>
            )}
          </div>
          {busy && <div className="text-sm text-muted mt-3">Signing you in…</div>}
          {err && <div className="mt-4 p-3 rounded-2xl bg-bad/10 border border-bad/25 text-sm text-left">⚠️ {err}</div>}
          {(!cfg || cfg.allowDemo) && (
            <button className="btn-ghost w-full mt-6" onClick={demo}>Try the student demo instead</button>
          )}
          <p className="text-[11.5px] text-faint mt-5 leading-relaxed">We only receive your name and email from Google. Children are identified by a nickname, class and city. You can delete everything anytime.</p>
        </div>
      </div>
    </div>
  )
}
