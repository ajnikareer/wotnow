import { useEffect, useState } from 'react'
import { Logo, Mascot } from '../components/Brand'
import { Icon } from '../components/Icon'
import { ThemeToggle, UserAvatar } from '../components/ui'
import { authApi, type Account, type NewChild } from '../lib/api'
import { Link, navigate } from '../lib/router'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'
import type { Me } from '../lib/types'

const AVATARS = ['🦊', '🐼', '🐯', '🦉', '🐬', '🐨', '🦁', '🐙', '🦄', '🐸', '🐧', '🦖']
const EMPTY: NewChild = { nickname: '', avatar: '🦊', grade: 8, city: 'Pune' }

/** The parent's home after Google sign-in: choose which child is learning, add or remove children. */
export default function Family() {
  const { signIn, signOut, refreshMe } = useSession()
  const toast = useToast()
  const [acc, setAcc] = useState<Account>()
  const [err, setErr] = useState<string>()
  const [adding, setAdding] = useState(false)
  const [form, setForm] = useState<NewChild>(EMPTY)
  const [busy, setBusy] = useState(false)

  useEffect(() => {
    if (!localStorage.getItem('wn_token')) { navigate('/signin'); return }
    authApi.account().then(a => { setAcc(a); if (a.children.length === 0) setAdding(true) }).catch(e => setErr(e.message))
  }, [])

  const open = async (c: Me, role: 'student' | 'parent') => {
    localStorage.setItem('wn_child', c.id)
    signIn(role)
    await refreshMe()
    navigate(role === 'parent' ? '/parent' : '/feed')
  }

  const add = async () => {
    setBusy(true); setErr(undefined)
    try {
      const r = await authApi.addChild(form)
      setAcc(r.account); setAdding(false); setForm(EMPTY)
      toast(`Added ${r.child.nickname} 🎉`)
    } catch (e: any) { setErr(e.message) } finally { setBusy(false) }
  }

  const remove = async (c: Me) => {
    if (!confirm(`Delete ${c.nickname} and all their progress? This can't be undone.`)) return
    try {
      const a = await authApi.removeChild(c.id)
      setAcc(a)
      if (localStorage.getItem('wn_child') === c.id) localStorage.removeItem('wn_child')
    } catch (e: any) { setErr(e.message) }
  }

  const out = () => { signOut(); navigate('/') }
  const full = acc ? acc.children.length >= acc.maxChildren : false
  const ok = form.nickname.replace(/[^A-Za-z0-9]/g, '').length >= 3

  return (
    <div className="min-h-screen">
      <header className="max-w-3xl mx-auto flex items-center gap-3 px-5 py-4">
        <a href="#/"><Logo className="h-9" /></a>
        <div className="ml-auto flex items-center gap-2">
          {acc?.isAdmin && <Link to="/admin" className="btn-ghost">Admin</Link>}
          <ThemeToggle compact />
          <button className="btn-ghost" onClick={out}><Icon name="logout" className="w-4 h-4" />Sign out</button>
        </div>
      </header>
      <main className="max-w-3xl mx-auto px-5 pb-16">
        <div className="flex items-center gap-4">
          {acc?.picture ? <img src={acc.picture} alt="" className="w-14 h-14 rounded-full" referrerPolicy="no-referrer" /> : <Mascot mood="happy" size={56} />}
          <div><h1 className="text-2xl md:text-3xl font-bold">{acc ? `Hi ${acc.name?.split(' ')[0] || 'there'}!` : 'Loading…'}</h1>
            <p className="text-muted text-sm">{acc?.email} · Who’s learning today?</p></div>
        </div>

        {err && <div className="mt-5 p-3 rounded-2xl bg-bad/10 border border-bad/25 text-sm">⚠️ {err}</div>}

        <div className="grid sm:grid-cols-2 gap-4 mt-6">
          {acc?.children.map(c => (
            <div key={c.id} className="card p-5">
              <div className="flex items-center gap-3">
                <UserAvatar emoji={c.avatar} size={56} />
                <div className="min-w-0"><div className="font-display text-xl font-bold truncate">{c.nickname}</div>
                  <div className="text-sm text-muted">Class {c.grade} · {c.city}</div>
                  <div className="text-xs text-muted">Level {c.level} · 🔥 {c.streak}-day streak · {c.xp.toLocaleString('en-IN')} XP</div></div>
              </div>
              <div className="flex gap-2 mt-4">
                <button className="btn-grad flex-1" onClick={() => open(c, 'student')}>Start learning</button>
                <button className="btn-ghost" onClick={() => open(c, 'parent')} title="Parent view">📊</button>
                <button className="btn-ghost text-bad" onClick={() => remove(c)} aria-label={`Delete ${c.nickname}`}>🗑️</button>
              </div>
            </div>
          ))}
          {acc && !full && !adding && (
            <button className="card p-5 grid place-items-center text-muted hover:text-ink border-dashed min-h-[150px]" onClick={() => setAdding(true)}>
              <div className="text-center"><div className="text-3xl">＋</div><div className="font-semibold mt-1">Add a child</div></div>
            </button>
          )}
        </div>

        {acc && adding && (
          <div className="card p-6 mt-5 animate-rise">
            <h2 className="text-xl font-bold">New child profile</h2>
            <p className="text-sm text-muted mt-1">No real names or photos. Kids are known only by a fun nickname.</p>
            <div className="mt-4"><label className="label">Avatar</label>
              <div className="grid grid-cols-6 gap-2">{AVATARS.map(a => (
                <button key={a} onClick={() => setForm({ ...form, avatar: a })} className={`aspect-square rounded-2xl text-2xl grid place-items-center border transition ${form.avatar === a ? 'border-brand-violet bg-brand-violet/10 scale-105' : 'border-line bg-surface2 hover:bg-surface3'}`}>{a}</button>
              ))}</div></div>
            <div className="mt-4"><label className="label">Nickname (3–16 letters or numbers)</label>
              <input className="input" value={form.nickname} maxLength={16} placeholder="e.g. CleverFox" onChange={e => setForm({ ...form, nickname: e.target.value.replace(/[^A-Za-z0-9]/g, '') })} /></div>
            <div className="grid grid-cols-2 gap-3 mt-4">
              <div><label className="label">Class</label>
                <select className="input" value={form.grade} onChange={e => setForm({ ...form, grade: +e.target.value })}>
                  {Array.from({ length: 10 }, (_, i) => i + 3).map(g => <option key={g} value={g}>Class {g}</option>)}</select></div>
              <div><label className="label">City</label><input className="input" value={form.city} maxLength={40} onChange={e => setForm({ ...form, city: e.target.value })} /></div>
            </div>
            <div className="flex gap-2 mt-5">
              <button className="btn-grad" disabled={!ok || busy} onClick={add}>{busy ? 'Saving…' : 'Create profile'}</button>
              {acc.children.length > 0 && <button className="btn-ghost" onClick={() => { setAdding(false); setErr(undefined) }}>Cancel</button>}
            </div>
          </div>
        )}
        {acc && full && <p className="text-xs text-muted mt-4">You’ve reached the limit of {acc.maxChildren} child profiles.</p>}
      </main>
    </div>
  )
}
