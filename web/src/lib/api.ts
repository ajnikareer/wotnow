import { API_MODE } from './env'
import { mockApi } from '../mocks/mockApi'
import type { Agent, Evaluation, Leaderboard, LiveQuiz, Me, ParentSummary, Post, Response, VoteResult } from './types'

/** One API surface for the whole app. VITE_API_MODE=mock (default) or live (FastAPI at /api, same domain). */

/** Demo identity: the shared "demo-student" (seeded), or a personal guest id created by the signup flow. */
export function demoUserId(): string {
  return localStorage.getItem('wn_uid') || 'demo-student'
}
export function newGuestId(): string {
  const id = 'guest-' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4)
  localStorage.setItem('wn_uid', id)
  return id
}

async function http<T>(path: string, init?: RequestInit): Promise<T> {
  const token = localStorage.getItem('wn_token')
  const res = await fetch('/api' + path, {
    ...init,
    headers: { 'Content-Type': 'application/json', ...(token ? { Authorization: `Bearer ${token}` } : { 'X-Demo-User': demoUserId() }), ...(init?.headers || {}) },
  })
  if (!res.ok) {
    let msg = res.statusText
    try { const j = await res.json(); msg = j.detail || msg } catch { /* not json */ }
    throw new Error(msg)
  }
  return res.json()
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
