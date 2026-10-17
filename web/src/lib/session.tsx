import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react'
import { api, ApiError, authApi } from './api'
import { navigate } from './router'
import { decodeToken, isExpired, needsRefresh } from './token'
import type { Me } from './types'

/**
 * Who is using the app.
 *   kind 'account'  a signed-in parent (Google, or the server's test sign-in) acting as one of their children
 *   kind 'demo'     "Try the student demo": the one shared demo student, no sign-in
 *   kind null       nobody yet (landing / sign-in pages)
 *
 * localStorage:  wn_token (session)  ·  wn_child (the active child)  ·  wn_role ('student' | 'parent': which view is open)
 * The session survives reloads and restarts; the server ends it (14 days, or "sign out of all devices").
 */
export type Role = 'student' | 'parent' | null
export type Kind = 'account' | 'demo' | null

type Ctx = {
  kind: Kind; role: Role; me?: Me
  /** The signed-in parent's email (read from the session token), for display. */
  email?: string
  /** Store a new session (after Google or test sign-in). */
  loginWithToken: (token: string) => void
  /** Open a child's profile (student view or parent view). */
  enterChild: (childId: string, role?: 'student' | 'parent') => Promise<void>
  /** Open the shared demo student. Never signs anybody in. */
  enterDemo: (role?: 'student' | 'parent') => void
  signIn: (r: 'student' | 'parent') => void
  /** Forget the session on this device and go to the sign-in page. Pass a path to go elsewhere, or false to stay put.
   *  (Older callers that navigate right after signOut() still work: this destination wins.) */
  signOut: (to?: string | false) => void
  refreshMe: () => Promise<void>
  setMe: (m: Me) => void
}

const noop = () => {}
const SessionCtx = createContext<Ctx>({
  kind: null, role: null, loginWithToken: noop, enterChild: async () => {}, enterDemo: noop, signIn: noop, signOut: noop, refreshMe: async () => {}, setMe: noop,
})

const has = () => typeof localStorage !== 'undefined'
const KEYS = ['wn_token', 'wn_child', 'wn_role', 'wn_uid']

/** The stored session, unless it has already expired (then it is dropped). */
function readToken(): string | null {
  if (!has()) return null
  const t = localStorage.getItem('wn_token')
  if (t && isExpired(decodeToken(t))) { for (const k of KEYS) localStorage.removeItem(k); return null }
  return t
}

export function SessionProvider({ children }: { children: ReactNode }) {
  const [token, setToken] = useState<string | null>(readToken)
  const [role, setRole] = useState<Role>(() => {
    if (!has()) return null
    localStorage.removeItem('wn_uid')                       // guest profiles from older versions are gone
    const r = localStorage.getItem('wn_role') as Role
    return r === 'student' || r === 'parent' ? r : readToken() ? 'student' : null
  })
  const [me, setMe] = useState<Me>()
  const kind: Kind = token ? 'account' : role ? 'demo' : null

  const refreshMe = useCallback(async () => {
    try { setMe(await api.me()) }
    catch (e) { if (e instanceof ApiError && e.status === 409) navigate('/family') /* signed in, but no child profile yet */ }
  }, [])
  useEffect(() => { if (role) refreshMe() }, [role, token, refreshMe])

  // Keep a signed-in family signed in: renew a token that is a few days old.
  useEffect(() => {
    if (!token || !needsRefresh(decodeToken(token))) return
    let alive = true
    authApi.refresh().then(r => { if (alive && r?.token) { localStorage.setItem('wn_token', r.token); setToken(r.token) } }).catch(() => { /* a 401 already sent them to sign in */ })
    return () => { alive = false }
  }, [token])

  const loginWithToken = (t: string) => {
    localStorage.setItem('wn_token', t)
    localStorage.removeItem('wn_uid'); localStorage.removeItem('wn_child'); localStorage.removeItem('wn_role')
    setToken(t); setRole('student'); setMe(undefined)
  }
  const signIn = (r: 'student' | 'parent') => { localStorage.setItem('wn_role', r); setRole(r) }
  const enterChild = async (childId: string, r: 'student' | 'parent' = 'student') => {
    localStorage.setItem('wn_child', childId)
    signIn(r)
    setMe(undefined)
    await refreshMe()
  }
  const enterDemo = (r: 'student' | 'parent' = 'student') => {
    localStorage.removeItem('wn_token'); localStorage.removeItem('wn_child')
    setToken(null); setMe(undefined); signIn(r)
  }
  const signOut = (to?: string | false) => {
    const dest = to === undefined ? '/signin' : to
    try { (window as any).google?.accounts?.id?.disableAutoSelect?.() } catch { /* Google script not loaded */ }   // don't sign back in silently
    for (const k of KEYS) localStorage.removeItem(k)
    setToken(null); setRole(null); setMe(undefined)
    if (dest) setTimeout(() => navigate(dest), 0)             // after the caller's own navigate(), if it has one: this destination wins
  }

  const email = decodeToken(token)?.email || undefined
  return <SessionCtx.Provider value={{ kind, role, me, email, loginWithToken, enterChild, enterDemo, signIn, signOut, refreshMe, setMe }}>{children}</SessionCtx.Provider>
}
export const useSession = () => useContext(SessionCtx)
