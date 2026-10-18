import { useEffect } from 'react'
import { RouterProvider, useRoute, navigate } from './lib/router'
import { ThemeProvider } from './lib/theme'
import { SessionProvider, useSession } from './lib/session'
import { ToastProvider, useToast } from './lib/toast'
import { ApiError } from './lib/api'
import { AccountBar } from './components/AccountBar'
import Landing from './pages/Landing'
import Start from './pages/Start'
import SignIn from './pages/SignIn'
import Family from './pages/Family'
import Feed from './pages/Feed'
import PostDetail from './pages/PostDetail'
import Experts from './pages/Experts'
import ExpertProfile from './pages/ExpertProfile'
import Leaderboard from './pages/Leaderboard'
import Profile from './pages/Profile'
import Parent from './pages/Parent'
import LiveQuiz from './pages/LiveQuiz'
import AdminPage from './pages/admin/AdminPage'

// Pages anyone can open. Everything else needs a signed-in family or the demo; without either, the visitor is sent to sign in.
// ('start' is the old sign-up form: it forwards to the sign-in page.)
const PUBLIC = new Set(['', 'start', 'signin', 'family', 'admin', 'about'])
// The app pages show the account strip (who is signed in, switch child, sign out).
const APP_PAGES = new Set(['feed', 'post', 'experts', 'leaderboard', 'me', 'parent', 'live', 'about'])

/** A safety net: an API error that a page didn't handle (for example "The shared demo student can't be changed") becomes a message
 *  instead of silence. Expired sessions (401) are already handled by the API client. */
function ErrorNotices() {
  const toast = useToast()
  useEffect(() => {
    const on = (e: PromiseRejectionEvent) => {
      const r: unknown = e.reason
      if (r instanceof ApiError && r.status !== 401) { toast('⚠️ ' + r.message); e.preventDefault() }
    }
    window.addEventListener('unhandledrejection', on)
    return () => window.removeEventListener('unhandledrejection', on)
  }, [toast])
  return null
}

function Routes() {
  const { parts } = useRoute()
  const { kind } = useSession()
  const page = parts[0] ?? ''
  const isPublic = PUBLIC.has(page)
  useEffect(() => { if (!kind && !isPublic) navigate('/signin') }, [kind, isPublic])
  if (!kind && !isPublic) return null
  const content = pageFor(page, parts)
  return <>{APP_PAGES.has(page) && <AccountBar />}{content}</>
}

function pageFor(page: string, parts: string[]) {
  switch (page) {
    case '': return <Landing />
    case 'about': return <Landing isAboutPage={true} />
    case 'start': return <Start />
    case 'signin': return <SignIn />
    case 'family': return <Family />
    case 'admin': return <AdminPage />
    case 'feed': return <Feed />
    case 'post': return <PostDetail />
    case 'experts': return parts[1] ? <ExpertProfile /> : <Experts />
    case 'leaderboard': return <Leaderboard />
    case 'me': return <Profile />
    case 'parent': return <Parent />
    case 'live': return <LiveQuiz />
    default: return <Feed />
  }
}

export default function App({ initialPath }: { initialPath?: string }) {
  return (
    <ThemeProvider>
      <RouterProvider initial={initialPath}>
        <SessionProvider>
          <ToastProvider>
            <ErrorNotices />
            <Routes />
          </ToastProvider>
        </SessionProvider>
      </RouterProvider>
    </ThemeProvider>
  )
}
