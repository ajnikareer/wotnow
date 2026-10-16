import { createContext, useContext, useEffect, useState, type ReactNode, type AnchorHTMLAttributes } from 'react'

/** Tiny hash router: #/feed, #/post/p1 … Works on any static host with zero config. */
type Route = { path: string; parts: string[]; query: URLSearchParams }

function parse(): Route {
  const raw = typeof window === 'undefined' ? '' : window.location.hash.replace(/^#/, '')
  const [p, q = ''] = (raw || '/').split('?')
  const path = p.startsWith('/') ? p : '/' + p
  return { path, parts: path.split('/').filter(Boolean), query: new URLSearchParams(q) }
}

const Ctx = createContext<Route>(parse())

export function RouterProvider({ children, initial }: { children: ReactNode; initial?: string }) {
  const [route, setRoute] = useState<Route>(() => {
    if (initial && typeof window === 'undefined') {
      const [p, q = ''] = initial.split('?')
      return { path: p, parts: p.split('/').filter(Boolean), query: new URLSearchParams(q) }
    }
    return parse()
  })
  useEffect(() => {
    const on = () => { setRoute(parse()); window.scrollTo({ top: 0 }) }
    window.addEventListener('hashchange', on)
    return () => window.removeEventListener('hashchange', on)
  }, [])
  return <Ctx.Provider value={route}>{children}</Ctx.Provider>
}

export const useRoute = () => useContext(Ctx)

export function navigate(to: string) {
  if (typeof window !== 'undefined') window.location.hash = to
}

export function Link({ to, children, ...rest }: { to: string; children: ReactNode } & Omit<AnchorHTMLAttributes<HTMLAnchorElement>, 'href'>) {
  return <a href={'#' + to} {...rest}>{children}</a>
}
