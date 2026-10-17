import type { Post } from './types'
import type { FeedTab } from './api'

/**
 * "Today" is the landing tab. If nothing but the city alert has been posted today (or nothing at all), the student would land
 * on an almost empty page, so the feed moves on to "For you", but only until the student has picked a tab themselves.
 */
export function shouldLeaveToday(tab: FeedTab, picked: boolean, loading: boolean, data: Post[] | undefined): boolean {
  if (tab !== 'today' || picked || loading || !data) return false
  return !data.some(p => p.type !== 'local_alert')
}
