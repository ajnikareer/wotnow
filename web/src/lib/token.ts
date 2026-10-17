/** Reads the (public) payload of our session token. Only used to know WHEN to refresh or drop it; the server is the judge of validity. */
export interface TokenInfo { sub: string; email: string; iat: number; exp: number }

export const REFRESH_AFTER_S = 3 * 86400        // sessions last 14 days; a token older than 3 days is renewed when the app opens

export function decodeToken(token: string | null | undefined): TokenInfo | null {
  if (!token) return null
  const parts = token.split('.')
  if (parts.length !== 3) return null
  try {
    const b64 = parts[1].replace(/-/g, '+').replace(/_/g, '/')
    const p = JSON.parse(atob(b64 + '='.repeat((4 - (b64.length % 4)) % 4)))
    if (typeof p.exp !== 'number' || typeof p.iat !== 'number') return null
    return { sub: String(p.sub ?? ''), email: String(p.email ?? ''), iat: p.iat, exp: p.exp }
  } catch { return null }
}

/** Unreadable tokens count as expired. */
export const isExpired = (info: TokenInfo | null, nowS = Math.floor(Date.now() / 1000)): boolean => !info || info.exp <= nowS

export const needsRefresh = (info: TokenInfo | null, nowS = Math.floor(Date.now() / 1000)): boolean =>
  !!info && info.exp > nowS && nowS - info.iat > REFRESH_AFTER_S
