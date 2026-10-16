import { useEffect } from 'react'
import { RouterProvider, useRoute, navigate } from './lib/router'
import { ThemeProvider } from './lib/theme'
import { SessionProvider, useSession } from './lib/session'
import { ToastProvider } from './lib/toast'
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

// Pages that don't need a student/parent role (sign-in flows have their own checks; admin has its own login).
const PUBLIC = new Set(['', 'start', 'signin', 'family', 'admin'])

function Routes() {
  const { parts } = useRoute()
  const { role } = useSession()
  const page = parts[0] ?? ''
  const isPublic = PUBLIC.has(page)
  useEffect(() => { if (!role && !isPublic) navigate('/') }, [role, isPublic])
  if (!role && !isPublic) return null

  switch (page) {
    case '': return <Landing />
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
            <Routes />
          </ToastProvider>
        </SessionProvider>
      </RouterProvider>
    </ThemeProvider>
  )
}
