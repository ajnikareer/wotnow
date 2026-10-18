/** Shared types = the API contract with the backend (see docs/project doc §15). */

export type Domain = 'fire' | 'road' | 'firstaid' | 'nutrition' | 'civic' | 'environment' | 'digital' | 'careers'
export type Band = 'junior' | 'middle' | 'senior' // Classes 3–5 · 6–8 · 9–12
export type PostType = 'scenario' | 'poll' | 'myth_fact' | 'scam_legit' | 'local_alert'
export type Mood = 'think' | 'look' | 'happy' | 'wow'

export interface Agent {
  id: string
  name: string
  domain: Domain
  domainLabel: string
  emoji: string
  colors: [string, string]
  bio: string
  topics: string[]
  stats: { posts: number; learners: number; avgScore: number; factCards: number }
}

export interface Option { id: string; text: string }

export interface Post {
  id: string
  agentId: string
  type: PostType
  createdAt: string
  bands: Band[]
  title: string
  body: string
  question?: string
  scene?: { emojis: string[]; bubble?: string }
  statement?: string                 // myth_fact
  message?: { from: string; text: string } // scam_legit
  options?: Option[]                 // poll
  chips?: string[]                   // local_alert
  steps?: { emoji: string; text: string }[]
  city?: string
  sourceCards: { id: string; title: string }[]
  stats: { responses: number; avgScore?: number }
  my?: { answered?: boolean; score?: number; choice?: string; checkedIn?: boolean }
}

export interface ChecklistItem { id: string; point: string; hit: boolean; note: string }
export interface Evaluation {
  score: number
  label: string
  checklist: ChecklistItem[]
  dangerous: boolean
  dangerousReason?: string
  feedback: string
  sourceCards: { id: string; title: string }[]
  xpAwarded: number
  me: Pick<Me, 'xp' | 'level' | 'streak'>
}

export interface VoteResult {
  choice: string
  correct: string
  isCorrect: boolean
  distribution: Record<string, number>
  explanation: string
  xpAwarded: number
}

export interface Response {
  id: string
  nickname: string
  avatar: string
  text: string
  score: number
  expertPick?: boolean
  expertReply?: string
}

export interface Me {
  id: string
  nickname: string
  avatar: string
  grade: number
  band: Band
  city: string
  country?: string
  school?: string
  className?: string
  xp: number
  level: number
  levelName: string
  nextLevelXp: number
  streak: number
  answers: number
  avgScore: number
  skills: Partial<Record<Domain, number>>
  badges: { id: string; emoji: string; name: string; earned: boolean }[]
  follows: string[]
}

export interface LeaderRow { rank: number; nickname: string; avatar: string; xp: number; me?: boolean; sub?: string; city?: string; country?: string }
export interface Leaderboard { scope: 'global' | 'country' | 'city'; rows: LeaderRow[]; me: LeaderRow; teams?: LeaderRow[]; myCity?: string; myCountry?: string; totalLearners?: number }

export interface QuizQuestion { id: string; text: string; options: Option[]; correct: string; explanation: string }
export interface LiveQuiz { id: string; agentId: string; title: string; startsIn: number; players: number; activePlayers?: string[]; questions: QuizQuestion[] }

export interface ParentSummary {
  child: Pick<Me, 'nickname' | 'avatar' | 'grade' | 'streak' | 'xp' | 'levelName' | 'skills'>
  minutesToday: number
  dailyLimit: number
  week: { day: string; minutes: number; answers: number }[]
  recent: { postTitle: string; agentId: string; score: number; when: string; missed?: string }[]
  conversationStarters: string[]
  safety: { flaggedReplies: number; blockedContent: number; dms: 'disabled' }
  settings: { dailyLimit: number; quietHours: string; weeklyEmail: boolean; topics: Record<Domain, boolean> }
}
