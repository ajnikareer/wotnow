import { useCallback, useEffect, useState } from 'react'

/** Minimal data hook: { data, loading, error, reload }. */
export function useAsync<T>(fn: () => Promise<T>, deps: unknown[] = []) {
  const [state, set] = useState<{ data?: T; loading: boolean; error?: string }>({ loading: true })
  const run = useCallback(() => {
    let alive = true
    set(s => ({ ...s, loading: true, error: undefined }))
    fn().then(d => alive && set({ data: d, loading: false }))
        .catch(e => alive && set({ loading: false, error: String(e?.message || e) }))
    return () => { alive = false }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps)
  useEffect(run, [run])
  return { ...state, reload: run }
}

export function timeAgo(iso: string) {
  const s = (Date.now() - new Date(iso).getTime()) / 1000
  if (s < 60) return 'now'
  if (s < 3600) return `${Math.floor(s / 60)}m`
  if (s < 86400) return `${Math.floor(s / 3600)}h`
  return `${Math.floor(s / 86400)}d`
}
