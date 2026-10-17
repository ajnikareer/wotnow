import { API_MODE } from './env'
import { mockApi } from '../mocks/mockApi'
import type { Agent, Evaluation, Leaderboard, LiveQuiz, Me, ParentSummary, Post, Response, VoteResult } from './types'

/** One API surface for the whole app. VITE_API_MODE=mock (default) or live (FastAPI at /api, same domain). */

/** The shared demo student ("Try the student demo"). Real families use a session token instead. */
export const DEMO_ID = 'demo-student'

export class ApiError extends Error {
  status: number
  constructor(status: number, message: string) { super(message); this.status = status }
}

/** Forget the sign-in and send the person to the sign-in page (the session expired or was ended elsewhere). */
function sessionLost() {
  for (const k of ['wn_token', 'wn_child', 'wn_role', 'wn_uid']) localStorage.removeItem(k)
  if (!location.hash.startsWith('#/signin')) location.hash = '#/signin?expired=1'
}

/** Low-level JSON call. Uses the signed-in session (Bearer + the active child) when there is one, otherwise the shared demo student. */
export async function http<T>(path: string, init?: RequestInit): Promise<T> {
  const token = localStorage.getItem('wn_token')
  const child = localStorage.getItem('wn_child')
  const headers: Record<string, string> = { 'Content-Type': 'application/json' }
  if (token) { headers['Authorization'] = `Bearer ${token}`; if (child) headers['X-Child'] = child }
  else headers['X-Demo-User'] = DEMO_ID
  const res = await fetch('/api' + path, { ...init, headers: { ...headers, ...((init?.headers as Record<string, string>) || {}) } })
  if (!res.ok) {
    let msg = res.statusText
    try { const j = await res.json(); msg = typeof j.detail === 'string' ? j.detail : JSON.stringify(j.detail) || msg } catch { /* not json */ }
    if (res.status === 401 && token) sessionLost()
    throw new ApiError(res.status, msg)
  }
  return res.json()
}

export interface AuthConfig {
  authMode: string; googleEnabled: boolean; googleClientId: string; allowDemo: boolean; devLogin: boolean; adminTokenLogin: boolean; maxChildren: number
}
export interface Account {
  id: string; email: string; name: string; picture: string; provider: 'google' | 'dev'; isAdmin: boolean; createdAt: string; children: Me[]; maxChildren: number
}
export interface NewChild { nickname: string; avatar: string; grade: number; city: string }
export type FeedTab = 'today' | 'foryou' | 'near' | 'following'
export interface FeedLatest { latest: string | null; newCount: number; todayCount: number }
export interface SignedIn { token: string; account: Account }

const NO_AUTH: AuthConfig = { authMode: 'demo', googleEnabled: false, googleClientId: '', allowDemo: true, devLogin: false, adminTokenLogin: false, maxChildren: 3 }
const notLive = () => Promise.reject(new Error('Sign-in is only available when the app runs against the server.'))
const live = <T,>(fn: () => Promise<T>): Promise<T> => (API_MODE === 'live' ? fn() : notLive())
const body = (o: unknown) => JSON.stringify(o)

/** Sign-in (Google, or the server's test sign-in), the parent's account and the child profiles. Live mode only. */
export const authApi = {
  config: (): Promise<AuthConfig> => (API_MODE === 'live' ? http<AuthConfig>('/auth/config') : Promise.resolve(NO_AUTH)),
  google: (credential: string) => live(() => http<SignedIn>('/auth/google', { method: 'POST', body: body({ credential }) })),
  devLogin: (email: string, name: string) => live(() => http<SignedIn>('/auth/dev-login', { method: 'POST', body: body({ email, name }) })),
  refresh: () => live(() => http<{ token: string }>('/auth/refresh', { method: 'POST' })),
  logoutAll: () => live(() => http<{ ok: boolean }>('/auth/logout-all', { method: 'POST' })),
  account: () => live(() => http<Account>('/account')),
  addChild: (c: NewChild) => live(() => http<{ child: Me; account: Account }>('/account/children', { method: 'POST', body: body(c) })),
  editChild: (id: string, c: Partial<NewChild>) => live(() => http<Account>(`/account/children/${id}`, { method: 'PUT', body: body(c) })),
  removeChild: (id: string) => live(() => http<Account>(`/account/children/${id}`, { method: 'DELETE' })),
  deleteAccount: () => live(() => http<{ deleted: boolean }>('/account', { method: 'DELETE' })),
}

/** "Anything new since <time>?" and today's post count, for the feed. Cheap on the server (no AI, shared cache). Resolves null in mock mode. */
export const feedLatest = (tab: FeedTab, since: string): Promise<FeedLatest | null> =>
  API_MODE === 'live' ? http<FeedLatest>(`/feed/latest?tab=${tab}&since=${encodeURIComponent(since)}`) : Promise.resolve(null)

const liveApi = {
  me: () => http<Me>('/me'),
  updateMe: (patch: Partial<Me>) => http<Me>('/me', { method: 'POST', body: body(patch) }),
  agents: () => http<Agent[]>('/agents'),
  agent: (id: string) => http<Agent>(`/agents/${id}`),
  feed: (tab: FeedTab = 'foryou', agentId?: string) =>
    http<Post[]>(`/feed?tab=${tab}${agentId ? `&agent=${agentId}` : ''}`),
  post: (id: string) => http<{ post: Post; responses: Response[] }>(`/posts/${id}`),
  answer: (id: string, text: string) => http<Evaluation>(`/posts/${id}/answer`, { method: 'POST', body: body({ text }) }),
  vote: (id: string, choice: string) => http<VoteResult>(`/posts/${id}/vote`, { method: 'POST', body: body({ choice }) }),
  voteResult: (id: string) => http<VoteResult | null>(`/posts/${id}/vote`),
  checkin: (id: string) => http<{ xpAwarded: number }>(`/posts/${id}/checkin`, { method: 'POST' }),
  leaderboard: (scope: 'class' | 'school' | 'city') => http<Leaderboard>(`/leaderboard?scope=${scope}`),
  liveQuiz: () => http<LiveQuiz>('/live/next'),
  submitQuiz: (score: number) => http<{ rank: number; players: number; xpAwarded: number }>('/live/submit', { method: 'POST', body: body({ score }) }),
  parent: () => http<ParentSummary>('/parent/summary'),
  updateParentSettings: (s: ParentSummary['settings']) => http<ParentSummary>('/parent/settings', { method: 'POST', body: body(s) }),
  reset: () => {},
}

export const api = API_MODE === 'live' ? liveApi : mockApi

/** The feed for a tab (or for one expert). One place that hides the live/mock typing difference. */
export const loadFeed = (tab: FeedTab, agentId?: string): Promise<Post[]> =>
  (api.feed as unknown as (t: FeedTab, a?: string) => Promise<Post[]>)(tab, agentId)
