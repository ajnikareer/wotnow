import { navigate } from '../lib/router'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'

/**
 * A slim strip above the app pages that always says WHO is using the app and gives a way out:
 *   family  → "👤 mum@example.com · learning as CleverFox · Switch child · Parent view · Sign out"
 *   demo    → "🧪 Shared demo student · Sign in or sign up · Exit demo"
 */
export function AccountBar() {
  const { kind, me, email, signOut } = useSession()
  const toast = useToast()
  if (!kind) return null
  const link = 'font-semibold text-ink underline-offset-2 hover:underline'
  return (
    <div className="bg-surface2 border-b border-line text-[12px] text-muted px-4 py-1.5 flex flex-wrap items-center gap-x-3 gap-y-1" role="status" data-testid="account-bar">
      {kind === 'account' ? (
        <>
          <span className="truncate max-w-[60vw]">👤 {email || 'Signed in'}{me ? <> · learning as <b className="text-ink">{me.nickname}</b></> : null}</span>
          <span className="ml-auto flex items-center gap-3">
            <button className={link} onClick={() => navigate('/about')}>About</button>
            <button className={link} onClick={() => navigate('/family')}>Switch child</button>
            <button className={link} onClick={() => navigate('/parent')}>Parent view</button>
            <button className={link} onClick={() => { signOut(); toast('Signed out') }}>Sign out</button>
          </span>
        </>
      ) : (
        <>
          <span>🧪 Shared demo student. Progress is shared with other visitors and isn’t saved for you.</span>
          <span className="ml-auto flex items-center gap-3">
            <button className={link} onClick={() => navigate('/about')}>About</button>
            <button className={link} onClick={() => navigate('/signin')}>Sign in or sign up</button>
            <button className={link} onClick={() => signOut()}>Exit demo</button>
          </span>
        </>
      )}
    </div>
  )
}
