import type { Evaluation, Leaderboard, LiveQuiz, Me, ParentSummary, Post, Response, VoteResult, Agent } from '../lib/types'
import { AGENTS, POSTS, ME, LEADERBOARDS, LIVE_QUIZ, PARENT, RESPONSES, SCENARIO_KEYS, VOTE_KEYS } from './data'

/* In-browser fake backend. Same signatures as the live API, persisted to localStorage. */

const wait = (ms: number) => new Promise(r => setTimeout(r, ms))
const store = {
  get<T>(k: string, d: T): T { try { const v = localStorage.getItem('wn_mock_' + k); return v ? JSON.parse(v) : d } catch { return d } },
  set(k: string, v: unknown) { try { localStorage.setItem('wn_mock_' + k, JSON.stringify(v)) } catch { /* ignore */ } },
}
const clone = <T,>(x: T): T => JSON.parse(JSON.stringify(x))

function me(): Me { return store.get('me', clone(ME)) }
function saveMe(m: Me) { store.set('me', m) }
function myPosts(): Record<string, Post['my']> { return store.get('my', {}) }
function addXp(n: number): Me {
  const m = me(); m.xp += n
  while (m.xp >= m.nextLevelXp) { m.level += 1; m.nextLevelXp += 800; m.levelName = LEVELS[Math.min(m.level - 1, LEVELS.length - 1)] }
  saveMe(m); return m
}
const LEVELS = ['Beginner', 'Aware', 'Alert', 'Capable', 'Skilled', 'Steady', 'Prepared', 'Guardian', 'Responder', 'Life-Ready']

function withMy(p: Post): Post { return { ...p, my: myPosts()[p.id] } }

const NEGATION = /(no|not|never|don'?t|do not|stop|avoid|instead of|without)\b[^.]{0,30}$/i

export const mockApi = {
  async me(): Promise<Me> { await wait(150); return me() },
  async updateMe(patch: Partial<Me>): Promise<Me> { const m = { ...me(), ...patch }; saveMe(m); return m },
  async agents(): Promise<Agent[]> { await wait(120); return AGENTS },
  async agent(id: string): Promise<Agent | undefined> { await wait(120); return AGENTS.find(a => a.id === id) },

  async feed(tab: 'foryou' | 'following' | 'near' = 'foryou', agentId?: string): Promise<Post[]> {
    await wait(350)
    const m = me()
    let list = POSTS.filter(p => p.bands.includes(m.band) || m.band === 'senior')
    if (agentId) list = POSTS.filter(p => p.agentId === agentId)
    else if (tab === 'following') list = list.filter(p => m.follows.includes(p.agentId))
    else if (tab === 'near') list = list.filter(p => p.type === 'local_alert' || p.agentId === 'terra' || p.agentId === 'civic')
    return list.map(withMy)
  },
  async post(id: string): Promise<{ post: Post; responses: Response[] }> {
    await wait(200)
    const p = POSTS.find(x => x.id === id); if (!p) throw new Error('Post not found')
    return { post: withMy(p), responses: RESPONSES[id] ?? [] }
  },

  async answer(postId: string, text: string): Promise<Evaluation> {
    await wait(1800 + Math.random() * 900) // feels like Gemini thinking
    const key = SCENARIO_KEYS[postId]
    const post = POSTS.find(p => p.id === postId)!
    if (!key) throw new Error('No rubric for this post in mock mode')
    const checklist = key.rubric.map(r => ({ id: r.id, point: r.point, note: r.note, hit: r.keys.test(text) }))
    let score = key.rubric.reduce((s, r, i) => s + (checklist[i].hit ? r.weight : 0), 0)
    let dangerous = false
    for (const rx of key.dangerous) {
      const m = rx.exec(text)
      if (m && !NEGATION.test(text.slice(Math.max(0, m.index - 40), m.index))) { dangerous = true; break }
    }
    if (dangerous) score = Math.min(score, 40)
    if (text.trim().length < 12) score = Math.min(score, 20)
    const missed = checklist.filter(c => !c.hit)
    const label = dangerous ? 'Careful! That could be dangerous.' : score >= 90 ? 'Brilliant answer!' : score >= 70 ? (missed.length === 1 ? 'Good. One key step missing.' : 'Good answer!') : score >= 40 ? 'Nice try. A few steps missing.' : 'Let’s learn this one together.'
    const feedback = dangerous
      ? `Part of your answer could make things worse. ${missed[0]?.note ?? ''} ${key.tips}`.trim()
      : missed.length === 0 ? `${key.good} You covered every key step. 🎉` : `${score >= 70 ? key.good + ' ' : ''}Next time, remember: ${missed[0].point.toLowerCase()}. ${key.tips}`
    const xp = Math.round(score / 2)
    const m = addXp(xp)
    const my = myPosts(); my[postId] = { answered: true, score }; store.set('my', my)
    return { score, label, checklist, dangerous, feedback, sourceCards: post.sourceCards, xpAwarded: xp, me: { xp: m.xp, level: m.level, streak: m.streak } }
  },

  async vote(postId: string, choice: string): Promise<VoteResult> {
    await wait(350)
    const k = VOTE_KEYS[postId]
    const isCorrect = choice === k.correct
    const post = POSTS.find(p => p.id === postId)!
    const xp = isCorrect ? (post.type === 'poll' ? 10 : 5) : 2
    addXp(xp)
    const my = myPosts(); my[postId] = { choice }; store.set('my', my)
    return { choice, correct: k.correct, isCorrect, distribution: k.dist, explanation: k.explanation, xpAwarded: xp }
  },
  async voteResult(postId: string): Promise<VoteResult | null> {
    const c = myPosts()[postId]?.choice; if (!c) return null
    const k = VOTE_KEYS[postId]
    return { choice: c, correct: k.correct, isCorrect: c === k.correct, distribution: k.dist, explanation: k.explanation, xpAwarded: 0 }
  },
  async checkin(postId: string): Promise<{ xpAwarded: number }> {
    await wait(250); addXp(5)
    const my = myPosts(); my[postId] = { checkedIn: true }; store.set('my', my)
    return { xpAwarded: 5 }
  },

  async leaderboard(scope: 'class' | 'school' | 'city'): Promise<Leaderboard> { await wait(250); return LEADERBOARDS[scope] },
  async liveQuiz(): Promise<LiveQuiz> { await wait(200); return LIVE_QUIZ },
  async submitQuiz(score: number): Promise<{ rank: number; players: number; xpAwarded: number }> {
    await wait(600); const xp = score; addXp(xp)
    return { rank: Math.max(1, Math.round(120 - score * 1.1)), players: LIVE_QUIZ.players, xpAwarded: xp }
  },
  async parent(): Promise<ParentSummary> { await wait(300); return store.get('parent', clone(PARENT)) },
  async updateParentSettings(s: ParentSummary['settings']): Promise<ParentSummary> {
    const p = store.get('parent', clone(PARENT)); p.settings = s; p.dailyLimit = s.dailyLimit; store.set('parent', p); return p
  },
  reset() { ['me', 'my', 'parent'].forEach(k => localStorage.removeItem('wn_mock_' + k)) },
}
