import { useEffect, useState } from 'react'
import { Logo, Mascot } from '../components/Brand'
import { Icon } from '../components/Icon'
import { ThemeToggle, UserAvatar } from '../components/ui'
import { authApi, type Account, type NewChild } from '../lib/api'
import { Link, navigate } from '../lib/router'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'
import type { Me } from '../lib/types'

import { AGENTS } from '../mocks/data'

const AVATARS = ['🦊', '🐼', '🐯', '🦉', '🐬', '🐨', '🦁', '🐙', '🦄', '🐸', '🐧', '🦖']
const EMPTY: NewChild = { nickname: '', avatar: '🦊', grade: 8, city: 'Pune', country: 'India' }

/** Create or edit one child profile. */
export function ChildForm({ initial, title, submitLabel, busy, onSubmit, onCancel }: {
  initial: NewChild; title: string; submitLabel: string; busy: boolean; onSubmit: (c: NewChild) => void; onCancel?: () => void
}) {
  const [f, setF] = useState<NewChild>(initial)
  const [step, setStep] = useState<1 | 2>(1)
  const [selectedExperts, setSelectedExperts] = useState<string[]>(() => {
    return initial.follows && initial.follows.length > 0 ? initial.follows : AGENTS.map(a => a.id)
  })

  const [nickStatus, setNickStatus] = useState<{ checking: boolean; available?: boolean; message?: string }>({ checking: false })

  useEffect(() => {
    const raw = f.nickname.replace(/[^A-Za-z0-9]/g, '')
    if (raw.length < 3) {
      setNickStatus({ checking: false })
      return
    }
    if (initial.nickname && initial.nickname.toLowerCase() === raw.toLowerCase()) {
      setNickStatus({ checking: false, available: true, message: 'Current nickname' })
      return
    }
    let cancelled = false
    setNickStatus({ checking: true })
    const timer = setTimeout(async () => {
      try {
        const res = await authApi.checkNickname(raw)
        if (!cancelled) {
          setNickStatus({ checking: false, available: res.available, message: res.message })
        }
      } catch {
        if (!cancelled) setNickStatus({ checking: false })
      }
    }, 350)
    return () => { cancelled = true; clearTimeout(timer) }
  }, [f.nickname, initial.nickname])

  const ok = f.nickname.replace(/[^A-Za-z0-9]/g, '').length >= 3 && nickStatus.available !== false

  const toggleExpert = (id: string) => {
    setSelectedExperts(prev => prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id])
  }

  const selectAll = () => setSelectedExperts(AGENTS.map(a => a.id))
  const selectNone = () => setSelectedExperts([])

  return (
    <div className="card p-6 mt-5 animate-rise" data-testid="child-form">
      {step === 1 ? (
        <>
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-bold">{title}</h2>
            <span className="text-xs font-bold text-brand-violet bg-brand-violet/10 px-2.5 py-1 rounded-full">Step 1 of 2</span>
          </div>
          <p className="text-sm text-muted mt-1">No real names or photos. Kids are known only by a fun nickname.</p>
          <div className="mt-4"><label className="label">Avatar</label>
            <div className="grid grid-cols-6 gap-2">{AVATARS.map(a => (
              <button key={a} type="button" onClick={() => setF({ ...f, avatar: a })} aria-pressed={f.avatar === a}
                className={`aspect-square rounded-2xl text-2xl grid place-items-center border transition ${f.avatar === a ? 'border-brand-violet bg-brand-violet/10 scale-105' : 'border-line bg-surface2 hover:bg-surface3'}`}>{a}</button>
            ))}</div></div>
          <div className="mt-4">
            <div className="flex items-center justify-between mb-1">
              <label className="label !mb-0">Nickname (3–16 letters or numbers)</label>
              {nickStatus.checking ? (
                <span className="text-xs text-muted">Checking availability…</span>
              ) : nickStatus.available === true ? (
                <span className="text-xs text-ok font-semibold">✓ {nickStatus.message || 'Available'}</span>
              ) : nickStatus.available === false ? (
                <span className="text-xs text-bad font-semibold">✗ {nickStatus.message || 'Already taken'}</span>
              ) : null}
            </div>
            <input
              className={`input ${nickStatus.available === false ? '!border-bad focus:!border-bad focus:!ring-bad/15' : nickStatus.available === true ? '!border-ok/60' : ''}`}
              value={f.nickname}
              maxLength={16}
              placeholder="e.g. CleverFox"
              onChange={e => setF({ ...f, nickname: e.target.value.replace(/[^A-Za-z0-9]/g, '') })}
            />
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mt-4">
            <div><label className="label">Class</label>
              <select className="input" value={f.grade} onChange={e => setF({ ...f, grade: +e.target.value })}>
                {Array.from({ length: 10 }, (_, i) => i + 3).map(g => <option key={g} value={g}>Class {g}</option>)}</select></div>
            <div><label className="label">City</label><input className="input" value={f.city} maxLength={40} placeholder="e.g. Pune" onChange={e => setF({ ...f, city: e.target.value })} /></div>
            <div><label className="label">Country</label><input list="country-suggestions" className="input" value={f.country || 'India'} maxLength={40} placeholder="e.g. India" onChange={e => setF({ ...f, country: e.target.value })} />
              <datalist id="country-suggestions">
                <option value="India" />
                <option value="United States" />
                <option value="United Kingdom" />
                <option value="Canada" />
                <option value="Australia" />
                <option value="Singapore" />
                <option value="United Arab Emirates" />
                <option value="Germany" />
              </datalist>
            </div>
          </div>
          <div className="flex gap-2 mt-5">
            <button className="btn-grad" disabled={!ok} onClick={() => setStep(2)}>
              Next: Choose experts →
            </button>
            {onCancel && <button className="btn-ghost" onClick={onCancel}>Cancel</button>}
          </div>
        </>
      ) : (
        <>
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2.5">
              <span className="text-3xl">{f.avatar}</span>
              <div>
                <h2 className="text-xl font-bold">Choose safety experts</h2>
                <div className="text-xs text-muted">for {f.nickname} · Class {f.grade} · {f.city}{f.country ? `, ${f.country}` : ''}</div>
              </div>
            </div>
            <span className="text-xs font-bold text-brand-violet bg-brand-violet/10 px-2.5 py-1 rounded-full">Step 2 of 2</span>
          </div>

          <p className="text-sm text-muted mt-2">
            Select the safety topics you want in your feed. All experts are selected by default — uncheck any you’d like to skip.
          </p>

          <div className="flex items-center justify-between mt-4 mb-2">
            <span className="text-xs font-bold text-muted">
              {selectedExperts.length} of {AGENTS.length} experts selected
            </span>
            <div className="flex gap-2 text-xs">
              <button type="button" onClick={selectAll} className="text-brand-violet hover:underline font-semibold">Select all</button>
              <span className="text-faint">·</span>
              <button type="button" onClick={selectNone} className="text-muted hover:text-ink font-semibold">Deselect all</button>
            </div>
          </div>

          <div className="grid sm:grid-cols-2 gap-2.5 max-h-[380px] overflow-y-auto pr-1">
            {AGENTS.map(a => {
              const checked = selectedExperts.includes(a.id)
              return (
                <div
                  key={a.id}
                  onClick={() => toggleExpert(a.id)}
                  className={`p-3 rounded-2xl border cursor-pointer transition select-none flex items-start gap-3 ${
                    checked
                      ? 'border-brand-violet/50 bg-brand-violet/[.06]'
                      : 'border-line bg-surface2 opacity-60 hover:opacity-100'
                  }`}
                >
                  <div
                    className="w-10 h-10 rounded-xl grid place-items-center text-xl shrink-0"
                    style={{ background: `linear-gradient(135deg, ${a.colors[0]}, ${a.colors[1]})` }}
                  >
                    {a.emoji}
                  </div>
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-sm text-ink">{a.name}</span>
                      <span className={`w-5 h-5 rounded-full grid place-items-center text-xs font-bold ${
                        checked ? 'bg-ok text-white' : 'border border-muted text-transparent'
                      }`}>
                        ✓
                      </span>
                    </div>
                    <div className="text-[11.5px] font-semibold text-brand-violet">{a.domainLabel}</div>
                    <div className="text-[12px] text-muted line-clamp-1 mt-0.5">{a.bio}</div>
                  </div>
                </div>
              )
            })}
          </div>

          <div className="flex gap-2 mt-5">
            <button className="btn-ghost" onClick={() => setStep(1)} disabled={busy}>
              ← Back
            </button>
            <button
              className="btn-grad flex-1"
              disabled={busy}
              onClick={() => onSubmit({ ...f, follows: selectedExperts })}
            >
              {busy ? 'Saving…' : submitLabel}
            </button>
          </div>
        </>
      )}
    </div>
  )
}

export interface FamilyViewProps {
  acc?: Account; err?: string; adding: boolean; editing?: Me; busy: boolean
  onOpen: (c: Me, role: 'student' | 'parent') => void; onAdd: (f: NewChild) => void; onSave: (f: NewChild) => void; onRemove: (c: Me) => void
  onStartAdd: () => void; onCancelAdd: () => void; onStartEdit: (c: Me) => void; onCancelEdit: () => void
  onSignOut: () => void; onSignOutEverywhere: () => void; onDeleteAccount: () => void
}

/** "Who's learning?": children, add / edit / remove, and the account (sign out, sign out everywhere, delete). No logic of its own. */
export function FamilyView(p: FamilyViewProps) {
  const { acc, err, adding, editing, busy } = p
  const full = acc ? acc.children.length >= acc.maxChildren : false
  const first = (acc?.name || '').split(' ')[0]
  return (
    <div className="min-h-screen">
      <header className="max-w-3xl mx-auto flex items-center gap-3 px-5 py-4">
        <a href="#/"><Logo className="h-6.5" /></a>
        <div className="ml-auto flex items-center gap-2">
          {acc?.isAdmin && <Link to="/admin" className="btn-ghost">Admin</Link>}
          <ThemeToggle compact />
          <button className="btn-ghost" onClick={p.onSignOut}><Icon name="logout" className="w-4 h-4" />Sign out</button>
        </div>
      </header>
      <main className="max-w-3xl mx-auto px-5 pb-16">
        <div className="flex items-center gap-4">
          {acc?.picture ? <img src={acc.picture} alt="" className="w-14 h-14 rounded-full" referrerPolicy="no-referrer" /> : <Mascot mood="happy" size={56} />}
          <div className="min-w-0"><h1 className="text-2xl md:text-3xl font-bold">{acc ? `Hi ${first || 'there'}!` : 'Loading…'}</h1>
            <p className="text-muted text-sm truncate">{acc ? <>{acc.email}{acc.provider === 'dev' && <span className="ml-2 chip !py-0.5 !text-[10px] text-warn">TEST ACCOUNT</span>}</> : ' '}{acc && ' · Who’s learning today?'}</p></div>
        </div>

        {err && <div className="mt-5 p-3 rounded-2xl bg-bad/10 border border-bad/25 text-sm" role="alert">⚠️ {err}</div>}

        <div className="grid sm:grid-cols-2 gap-4 mt-6">
          {!acc && !err && [0, 1].map(i => <div key={i} className="card p-5 skeleton h-[150px]" />)}
          {acc?.children.map(c => (
            <div key={c.id} className="card p-5" data-testid="child-card">
              <div className="flex items-center gap-3">
                <UserAvatar emoji={c.avatar} size={56} />
                <div className="min-w-0"><div className="font-display text-xl font-bold truncate">{c.nickname}</div>
                  <div className="text-sm text-muted">Class {c.grade} · {c.city}{c.country ? `, ${c.country}` : ''}</div>
                  <div className="text-xs text-muted">Level {c.level} · 🔥 {c.streak}-day streak · {c.xp.toLocaleString('en-IN')} XP</div></div>
              </div>
              <div className="flex gap-2 mt-4">
                <button className="btn-grad flex-1" onClick={() => p.onOpen(c, 'student')}>Start learning</button>
                <button className="btn-ghost" onClick={() => p.onOpen(c, 'parent')} title="Parent view" aria-label={`Parent view for ${c.nickname}`}>📊</button>
                <button className="btn-ghost" onClick={() => p.onStartEdit(c)} title="Edit" aria-label={`Edit ${c.nickname}`}>✏️</button>
                <button className="btn-ghost text-bad" onClick={() => p.onRemove(c)} title="Delete" aria-label={`Delete ${c.nickname}`}>🗑️</button>
              </div>
            </div>
          ))}
          {acc && !full && !adding && !editing && (
            <button className="card p-5 grid place-items-center text-muted hover:text-ink border-dashed min-h-[150px]" onClick={p.onStartAdd}>
              <div className="text-center"><div className="text-3xl">＋</div><div className="font-semibold mt-1">Add a child</div></div>
            </button>
          )}
        </div>

        {acc && adding && <ChildForm initial={EMPTY} title="New child profile" submitLabel="Create profile" busy={busy} onSubmit={p.onAdd}
          onCancel={acc.children.length > 0 ? p.onCancelAdd : undefined} />}
        {editing && <ChildForm key={editing.id} initial={{ nickname: editing.nickname, avatar: editing.avatar, grade: editing.grade, city: editing.city, country: editing.country || 'India', follows: editing.follows }}
          title={`Edit ${editing.nickname}`} submitLabel="Save changes" busy={busy} onSubmit={p.onSave} onCancel={p.onCancelEdit} />}
        {acc && full && <p className="text-xs text-muted mt-4">You’ve reached the limit of {acc.maxChildren} child profiles.</p>}

        {acc && (
          <section className="mt-10 pt-6 border-t border-line" aria-label="Account">
            <h2 className="text-sm font-bold text-muted uppercase tracking-wider">Account</h2>
            <div className="flex flex-wrap gap-2 mt-3">
              <button className="btn-ghost" disabled={busy} onClick={p.onSignOutEverywhere}>Sign out of all devices</button>
              <button className="btn-ghost text-bad" disabled={busy} onClick={p.onDeleteAccount}>Delete my account</button>
            </div>
            <p className="text-xs text-faint mt-3">Signing out only ends the session on this device. “All devices” ends every session. Deleting removes your account and all children’s progress.</p>
          </section>
        )}
      </main>
    </div>
  )
}

/** The parent's home after signing in. */
export default function Family() {
  const { kind, enterChild, signOut } = useSession()
  const toast = useToast()
  const [acc, setAcc] = useState<Account>()
  const [err, setErr] = useState<string>()
  const [adding, setAdding] = useState(false)
  const [editing, setEditing] = useState<Me>()
  const [busy, setBusy] = useState(false)

  useEffect(() => { if (kind !== 'account') navigate('/signin') }, [kind])
  useEffect(() => {
    if (kind !== 'account') return
    authApi.account().then(a => { setAcc(a); if (a.children.length === 0) setAdding(true) }).catch(e => setErr(e.message))
  }, [kind])

  const run = async (fn: () => Promise<void>) => { setBusy(true); setErr(undefined); try { await fn() } catch (e: any) { setErr(e.message) } finally { setBusy(false) } }

  return <FamilyView acc={acc} err={err} adding={adding} editing={editing} busy={busy}
    onOpen={async (c, role) => { await enterChild(c.id, role); navigate(role === 'parent' ? '/parent' : '/feed') }}
    onAdd={f => run(async () => {
      const r = await authApi.addChild(f)
      setAcc(r.account)
      setAdding(false)
      toast(`Added ${r.child.nickname} 🎉`)
      await enterChild(r.child.id, 'student')
      navigate('/feed')
    })}
    onSave={f => run(async () => { if (!editing) return; setAcc(await authApi.editChild(editing.id, f)); setEditing(undefined); toast('Saved ✓') })}
    onRemove={c => run(async () => {
      if (!confirm(`Delete ${c.nickname} and all their progress? This can't be undone.`)) return
      setAcc(await authApi.removeChild(c.id))
      if (localStorage.getItem('wn_child') === c.id) localStorage.removeItem('wn_child')
    })}
    onStartAdd={() => { setAdding(true); setEditing(undefined) }} onCancelAdd={() => { setAdding(false); setErr(undefined) }}
    onStartEdit={c => { setEditing(c); setAdding(false) }} onCancelEdit={() => setEditing(undefined)}
    onSignOut={() => { signOut('/signin'); toast('Signed out') }}
    onSignOutEverywhere={() => run(async () => {
      if (!confirm('Sign out of every device where you are signed in?')) return
      await authApi.logoutAll()
      signOut('/signin'); toast('Signed out everywhere')
    })}
    onDeleteAccount={() => run(async () => {
      if (!confirm('Delete your account and ALL your children’s profiles? This can’t be undone.')) return
      if ((prompt('Type DELETE to confirm') || '').trim() !== 'DELETE') return
      await authApi.deleteAccount()
      signOut('/'); toast('Your account was deleted')
    })} />
}
