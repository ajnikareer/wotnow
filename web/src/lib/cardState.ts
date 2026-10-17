import type { Post } from './types'

/**
 * Neon card states. The server decides the state from what the student has done (so it is the same on every device and
 * survives restarts); the card only draws it. `deriveState` is a fallback for mock mode and for older servers.
 *
 *   new    yellow  posted since your last visit and not answered yet
 *   done   green   answered (score 50+), voted correctly, or did the alert's check-in
 *   retry  red     scenario score under 50, or a wrong vote
 *   none   plain
 */
export type CardState = 'new' | 'done' | 'retry' | 'none'
export type StatefulPost = Post & { state?: CardState }

export const PASS_SCORE = 50                       // same threshold as the server (services/feed.py)
const VOTE_TYPES = ['poll', 'myth_fact', 'scam_legit']

/** What the student has done, when the server didn't send a state. */
function deriveState(post: Post): CardState {
  const my: any = post.my
  if (!my) return 'none'
  if (post.type === 'scenario' && my.answered) return (my.score ?? 0) >= PASS_SCORE ? 'done' : 'retry'
  if (VOTE_TYPES.includes(post.type) && my.choice != null) return my.correct === false ? 'retry' : 'done'
  if (post.type === 'local_alert' && my.checkedIn) return 'done'
  return 'none'
}

/** `override` is a result the student just produced on this card (a vote, a check-in) before the feed was reloaded. */
export function stateOf(post: Post, override?: CardState | null): CardState {
  if (override) return override
  return (post as StatefulPost).state ?? deriveState(post)
}

/** The little tag on the card's border. The colour alone never carries the meaning. */
export function labelOf(post: Post, state: CardState): string | null {
  switch (state) {
    case 'new': return 'NEW'
    case 'done':
      if (post.type === 'scenario') return `DONE ${post.my?.score ?? ''}`.trim()
      if (VOTE_TYPES.includes(post.type)) return 'CORRECT'
      return 'DONE'
    case 'retry': return post.type === 'scenario' ? 'TRY AGAIN' : 'MISSED'
    default: return null
  }
}
