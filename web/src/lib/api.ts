import { API_MODE } from './env'
import { mockApi } from '../mocks/mockApi'
import type { Agent, Evaluation, Leaderboard, LiveQuiz, Me, ParentSummary, Post, Response, VoteResult } from './types'

/** One API surface for the whole app. VITE_API_MODE=mock (default) or live (FastAPI at /api, same domain). */

/** Demo identity: the shared "demo-student" (seeded), or a personal guest id created by the demo signup flow. */
export function demoUserId(): string {
  return localStorage.getItem('wn_uid') || 'demo-student'
}
export function newGuestId(): string {
  const id = 'guest-' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4)
  localStorage.setItem('wn_uid', id)
  return id
}

export class ApiError extends Error {
  status: number
  constructor(status: number, message: string) { super(message); this.status = status }
}

/** Low-level JSON call. Uses the Google session (Bearer + active child) when signed in, otherwise the demo identity. */
export async function http<T>(path: string, init?: RequestInit): Promise<T> {
  const token = localStorage.getItem('wn_token')
  const child = localStorage.getItem('wn_child')
  const headers: Record<string, string> = { 'Content-Type': 'application/json' }
  if (token) { headers['Authorization'] = `Bearer ${token}`; if (child) headers['X-Child'] = child }
  else headers['X-Demo-User'] = demoUserId()
  const res = await fetch('/api' + path, { ...init, headers: { ...headers, ...((init?.headers as Record<string, string>) || {}) } })
  if (!res.ok) {
    let msg = res.statusText
    try { const j = await res.json(); msg = typeof j.detail === 'string' ? j.detail : JSON.stringify(j.detail) || msg } catch { /* not json */ }
    if (res.status === 401 && token) {                       // session expired → sign in again
      localStorage.removeItem('wn_token'); localStorage.removeItem('wn_child')
      if (!location.hash.startsWith('#/signin')) location.hash = '#/signin'
    }
    throw new ApiError(res.status, msg)
  }
  return res.json()
}

export interface AuthConfig { authMode: string; googleEnabled: boolean; googleClientId: string; allowDemo: boolean; adminTokenLogin: boolean; maxChildren: number }
export interface Account { id: string; email: string; name: string; picture: string; isAdmin: boolean; children: Me[]; maxChildren: number }
export interface NewChild { nickname: string; avatar: string; grade: number; city: string }

const NO_AUTH: AuthConfig = { authMode: 'demo', googleEnabled: false, googleClientId: '', allowDemo: true, adminTokenLogin: false, maxChildren: 3 }
const notLive = () => Promise.reject(new Error('Sign-in is only available when the app runs against the server.'))

/** Google sign-in, the parent's account and child profiles (live mode only). */
export const authApi = {
  config: (): Promise<AuthConfig> => (API_MODE === 'live' ? http<AuthConfig>('/auth/config') : Promise.resolve(NO_AUTH)),
  google: (credential: string): Promise<{ token: string; account: Account }> =>
    API_MODE === 'live' ? http('/auth/google', { method: 'POST', body: JSON.stringify({ credential }) }) : notLive(),
  account: (): Promise<Account> => (API_MODE === 'live' ? http<Account>('/account') : notLive()),
  addChild: (c: NewChild): Promise<{ child: Me; account: Account }> =>
    API_MODE === 'live' ? http('/account/children', { method: 'POST', body: JSON.stringify(c) }) : notLive(),
  removeChild: (id: string): Promise<Account> => (API_MODE === 'live' ? http<Account>(`/account/children/${id}`, { method: 'DELETE' }) : notLive()),
  deleteAccount: (): Promise<{ deleted: boolean }> => (API_MODE === 'live' ? http('/account', { method: 'DELETE' }) : notLive()),
}

const liveApi = {
  me: () => http<Me>('/me'),
  updateMe: (patch: Partial<Me>) => http<Me>('/me', { method: 'POST', body: JSON.stringify(patch) }),
  agents: () => http<Agent[]>('/agents'),
  agent: (id: string) => http<Agent>(`/agents/${id}`),
  feed: (tab: 'foryou' | 'following' | 'near' = 'foryou', agentId?: string) =>
    http<Post[]>(`/feed?tab=${tab}${agentId ? `&agent=${agentId}` : ''}`),
  post: (id: string) => http<{ post: Post; responses: Response[] }>(`/posts/${id}`),
  answer: (id: string, text: string) => http<Evaluation>(`/posts/${id}/answer`, { method: 'POST', body: JSON.stringify({ text }) }),
  vote: (id: string, choice: string) => http<VoteResult>(`/posts/${id}/vote`, { method: 'POST', body: JSON.stringify({ choice }) }),
  voteResult: (id: string) => http<VoteResult | null>(`/posts/${id}/vote`),
  checkin: (id: string) => http<{ xpAwarded: number }>(`/posts/${id}/checkin`, { method: 'POST' }),
  leaderboard: (scope: 'class' | 'school' | 'city') => http<Leaderboard>(`/leaderboard?scope=${scope}`),
  liveQuiz: () => http<LiveQuiz>('/live/next'),
  submitQuiz: (score: number) => http<{ rank: number; players: number; xpAwarded: number }>('/live/submit', { method: 'POST', body: JSON.stringify({ score }) }),
  parent: () => http<ParentSummary>('/parent/summary'),
  updateParentSettings: (s: ParentSummary['settings']) => http<ParentSummary>('/parent/settings', { method: 'POST', body: JSON.stringify(s) }),
  reset: () => {},
}

export const api = API_MODE === 'live' ? liveApi : mockApi
