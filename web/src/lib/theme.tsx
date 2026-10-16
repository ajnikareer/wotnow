import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react'

export type ThemePref = 'light' | 'dark' | 'system'
type Ctx = { pref: ThemePref; resolved: 'light' | 'dark'; setPref: (p: ThemePref) => void; toggle: () => void }
const ThemeCtx = createContext<Ctx>({ pref: 'system', resolved: 'dark', setPref: () => {}, toggle: () => {} })

const sysDark = () => typeof window !== 'undefined' && window.matchMedia?.('(prefers-color-scheme: dark)').matches

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [pref, setPrefState] = useState<ThemePref>(() => {
    if (typeof window === 'undefined') return 'system'
    return (localStorage.getItem('wn_theme') as ThemePref) || 'system'
  })
  const [resolved, setResolved] = useState<'light' | 'dark'>(() => (pref === 'dark' || (pref === 'system' && sysDark()) ? 'dark' : 'light'))

  useEffect(() => {
    const apply = () => {
      const dark = pref === 'dark' || (pref === 'system' && sysDark())
      document.documentElement.classList.toggle('dark', dark)
      document.querySelector('meta[name="theme-color"]')?.setAttribute('content', dark ? '#0B0D14' : '#F6F7FB')
      setResolved(dark ? 'dark' : 'light')
    }
    apply()
    const mq = window.matchMedia('(prefers-color-scheme: dark)')
    mq.addEventListener?.('change', apply)
    return () => mq.removeEventListener?.('change', apply)
  }, [pref])

  const setPref = useCallback((p: ThemePref) => { localStorage.setItem('wn_theme', p); setPrefState(p) }, [])
  const toggle = useCallback(() => setPref(resolved === 'dark' ? 'light' : 'dark'), [resolved, setPref])
  return <ThemeCtx.Provider value={{ pref, resolved, setPref, toggle }}>{children}</ThemeCtx.Provider>
}

export const useTheme = () => useContext(ThemeCtx)
