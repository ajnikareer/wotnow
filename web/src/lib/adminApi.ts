/** Admin API client. Uses the Google session when signed in as an admin, otherwise the admin token typed into the login box. */
export class AdminAuthError extends Error {}

const TOKEN_KEY = 'wn_admin_token'
export const adminToken = () => sessionStorage.getItem(TOKEN_KEY) || ''
export const setAdminToken = (t: string) => (t ? sessionStorage.setItem(TOKEN_KEY, t) : sessionStorage.removeItem(TOKEN_KEY))

async function call<T = any>(method: string, path: string, body?: unknown): Promise<T> {
  const headers: Record<string, string> = { 'Content-Type': 'application/json' }
  const session = localStorage.getItem('wn_token')
  if (session) headers['Authorization'] = `Bearer ${session}`
  if (adminToken()) headers['X-Admin-Token'] = adminToken()
  const res = await fetch('/api/admin' + path, { method, headers, body: body === undefined ? undefined : JSON.stringify(body) })
  if (res.status === 403 || res.status === 401) throw new AdminAuthError('Admin access required')
  if (!res.ok) {
    let msg = res.statusText
    try { const j = await res.json(); msg = typeof j.detail === 'string' ? j.detail : JSON.stringify(j.detail) } catch { /* not json */ }
    throw new Error(msg)
  }
  return res.json()
}

export const admin = {
  get: <T = any>(p: string) => call<T>('GET', p),
  put: <T = any>(p: string, b: unknown) => call<T>('PUT', p, b),
  post: <T = any>(p: string, b: unknown = {}) => call<T>('POST', p, b),
  del: <T = any>(p: string) => call<T>('DELETE', p),
}
