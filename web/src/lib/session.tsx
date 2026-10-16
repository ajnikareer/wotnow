import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react'
import { api } from './api'
import type { Me } from './types'

/** Who is using the app: nobody (landing), a student, or a parent. Demo auth for the hackathon. */
type Role = 'student' | 'parent' | null
type Ctx = { role: Role; me?: Me; signIn: (r: Exclude<Role, null>) => void; signOut: () => void; refreshMe: () => Promise<void>; setMe: (m: Me) => void }
const SessionCtx = createContext<Ctx>({ role: null, signIn: () => {}, signOut: () => {}, refreshMe: async () => {}, setMe: () => {} })

export function SessionProvider({ children }: { children: ReactNode }) {
  const [role, setRole] = useState<Role>(() => (typeof window === 'undefined' ? 'student' : (localStorage.getItem('wn_role') as Role) || null))
  const [me, setMe] = useState<Me>()
  const refreshMe = useCallback(async () => { try { setMe(await api.me()) } catch { /* shown by pages */ } }, [])
  useEffect(() => { if (role) refreshMe() }, [role, refreshMe])
  const signIn = (r: Exclude<Role, null>) => { localStorage.setItem('wn_role', r); setRole(r) }
  const signOut = () => {
    localStorage.removeItem('wn_role'); localStorage.removeItem('wn_uid'); localStorage.removeItem('wn_token')
    setRole(null); setMe(undefined)
  }
  return <SessionCtx.Provider value={{ role, me, signIn, signOut, refreshMe, setMe }}>{children}</SessionCtx.Provider>
}
export const useSession = () => useContext(SessionCtx)
