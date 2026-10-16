import { useState } from 'react'
import { Logo, Mascot } from '../components/Brand'
import { Icon } from '../components/Icon'
import { AgentAvatar, ThemeToggle } from '../components/ui'
import { AGENTS } from '../mocks/data'
import { api, newGuestId } from '../lib/api'
import { navigate } from '../lib/router'
import { useSession } from '../lib/session'
import type { Band } from '../lib/types'

const AVATARS = ['🦊', '🐼', '🐯', '🦉', '🐬', '🐨', '🦁', '🐙', '🦄', '🐸', '🐧', '🦖']
const ADJ = ['Clever', 'Brave', 'Sunny', 'Zippy', 'Mighty', 'Calm', 'Swift', 'Witty']
const NOUN = ['Fox', 'Panda', 'Tiger', 'Owl', 'Dolphin', 'Koala', 'Lion', 'Comet']
const band = (g: number): Band => (g <= 5 ? 'junior' : g <= 8 ? 'middle' : 'senior')

/** Parent-led signup: parent consent → child profile → experts. Creates a personal guest identity. */
export default function Start() {
  const { signIn, setMe } = useSession()
  const [step, setStep] = useState(0)
  const [parent, setParent] = useState({ name: '', email: '', consent: false })
  const [child, setChild] = useState({ nickname: 'CleverFox', avatar: '🦊', grade: 8, city: 'Pune' })
  const [follows, setFollows] = useState<string[]>(AGENTS.filter(a => a.id !== 'compass').map(a => a.id))
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState<string>()

  const shuffleName = () => setChild(c => ({ ...c, nickname: ADJ[Math.floor(Math.random() * ADJ.length)] + NOUN[Math.floor(Math.random() * NOUN.length)] }))
  const canNext = step === 0 ? parent.name.trim() && /.+@.+\..+/.test(parent.email) && parent.consent : step === 1 ? child.nickname.trim().length >= 3 : follows.length > 0

  const finish = async () => {
    setBusy(true); setError(undefined)
    try {
      newGuestId()
      const m = await api.updateMe({ nickname: child.nickname, avatar: child.avatar, grade: child.grade, band: band(child.grade), city: child.city,
        follows: follows.filter(f => f !== 'compass' || child.grade >= 9) })
      setMe(m); signIn('student'); navigate('/feed')
    } catch (e: any) {
      setError(e?.message || 'Something went wrong'); setBusy(false)
    }
  }
  const steps = ['Parent', 'Your child', 'Experts']

  return (
    <div className="min-h-screen flex flex-col">
      <header className="flex items-center px-5 py-4 max-w-3xl w-full mx-auto"><a href="#/"><Logo className="h-9" /></a><div className="ml-auto"><ThemeToggle compact /></div></header>
      <div className="flex-1 w-full max-w-xl mx-auto px-5 pb-10">
        <div className="flex gap-2 mt-2 mb-6">
          {steps.map((s, i) => (
            <div key={s} className="flex-1"><div className={`h-1.5 rounded-full ${i <= step ? 'grad-bg' : 'bg-surface3'}`} />
              <div className={`text-xs mt-1.5 font-semibold ${i <= step ? 'text-ink' : 'text-faint'}`}>{s}</div></div>
          ))}
        </div>

        <div className="card p-6 md:p-8 animate-rise" key={step}>
          {step === 0 && (
            <>
              <div className="flex items-center gap-3"><Mascot mood="look" size={56} /><div><h1 className="text-2xl md:text-3xl font-bold">Hi! Let’s set up wotnow</h1><p className="text-muted text-sm">A parent or guardian creates the account.</p></div></div>
              <div className="mt-6 space-y-4">
                <div><label className="label">Your name</label><input className="input" placeholder="e.g. Priya Sharma" value={parent.name} onChange={e => setParent({ ...parent, name: e.target.value })} /></div>
                <div><label className="label">Your email</label><input className="input" type="email" placeholder="you@example.com" value={parent.email} onChange={e => setParent({ ...parent, email: e.target.value })} /></div>
                <label className="flex gap-3 items-start p-4 rounded-2xl bg-surface2 border border-line cursor-pointer">
                  <input type="checkbox" className="mt-1 w-5 h-5 accent-violet-500" checked={parent.consent} onChange={e => setParent({ ...parent, consent: e.target.checked })} />
                  <span className="text-sm leading-relaxed">I’m the parent or legal guardian, and I consent to my child using wotnow. Only a nickname, class and city are stored, and I can delete everything anytime.</span>
                </label>
              </div>
            </>
          )}
          {step === 1 && (
            <>
              <h1 className="text-2xl md:text-3xl font-bold">Create your child’s profile</h1>
              <p className="text-muted text-sm mt-1">No real names or photos. Kids are known only by a fun nickname.</p>
              <div className="flex items-center gap-4 mt-6 p-4 rounded-2xl grad-soft border border-line">
                <div className="w-16 h-16 rounded-full bg-surface grid place-items-center text-4xl">{child.avatar}</div>
                <div><div className="font-display text-2xl font-bold">{child.nickname || '…'}</div><div className="text-sm text-muted">Class {child.grade} · {child.city}</div></div>
              </div>
              <div className="mt-5"><label className="label">Avatar</label>
                <div className="grid grid-cols-6 gap-2">{AVATARS.map(a => (
                  <button key={a} onClick={() => setChild({ ...child, avatar: a })} className={`aspect-square rounded-2xl text-2xl grid place-items-center border transition ${child.avatar === a ? 'border-brand-violet bg-brand-violet/10 scale-105' : 'border-line bg-surface2 hover:bg-surface3'}`}>{a}</button>
                ))}</div></div>
              <div className="mt-5"><label className="label">Nickname</label>
                <div className="flex gap-2"><input className="input" value={child.nickname} maxLength={16} onChange={e => setChild({ ...child, nickname: e.target.value.replace(/[^A-Za-z0-9]/g, '') })} />
                  <button className="btn-ghost shrink-0" onClick={shuffleName}>🎲 Shuffle</button></div></div>
              <div className="grid grid-cols-2 gap-3 mt-5">
                <div><label className="label">Class</label>
                  <select className="input" value={child.grade} onChange={e => setChild({ ...child, grade: +e.target.value })}>
                    {Array.from({ length: 10 }, (_, i) => i + 3).map(g => <option key={g} value={g}>Class {g}</option>)}</select></div>
                <div><label className="label">City</label><input className="input" value={child.city} onChange={e => setChild({ ...child, city: e.target.value })} /></div>
              </div>
            </>
          )}
          {step === 2 && (
            <>
              <h1 className="text-2xl md:text-3xl font-bold">Pick the experts to follow</h1>
              <p className="text-muted text-sm mt-1">You can change these anytime. {child.grade < 9 && 'Careers unlocks in Class 9.'}</p>
              <div className="grid sm:grid-cols-2 gap-2.5 mt-6">
                {AGENTS.map(a => {
                  const locked = a.id === 'compass' && child.grade < 9
                  const on = follows.includes(a.id)
                  return (
                    <button key={a.id} disabled={locked} onClick={() => setFollows(f => on ? f.filter(x => x !== a.id) : [...f, a.id])}
                      className={`flex items-center gap-3 p-3 rounded-2xl border text-left transition ${on ? 'border-brand-violet bg-brand-violet/[.07]' : 'border-line bg-surface2 hover:bg-surface3'} ${locked ? 'opacity-40' : ''}`}>
                      <AgentAvatar agent={a} size={40} /><div className="flex-1"><div className="font-bold text-sm">{a.name}</div><div className="text-xs text-muted">{a.domainLabel}</div></div>
                      <span className={`w-6 h-6 rounded-full grid place-items-center ${on ? 'grad-bg' : 'border border-line'}`}>{on && <Icon name="check" className="w-4 h-4 text-[#06080C]" strokeWidth={3} />}</span>
                    </button>
                  )
                })}
              </div>
            </>
          )}
          {error && <div className="mt-6 p-3 rounded-2xl bg-bad/10 border border-bad/25 text-sm">⚠️ {error}</div>}
          <div className="flex items-center gap-3 mt-8">
            {step > 0 && <button className="btn-ghost" onClick={() => setStep(step - 1)}><Icon name="chevronLeft" className="w-4 h-4" />Back</button>}
            <button className="btn-grad ml-auto !px-6" disabled={!canNext || busy} onClick={() => (step < 2 ? setStep(step + 1) : finish())}>
              {step < 2 ? 'Continue' : busy ? 'Setting up…' : 'Start learning 🚀'}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
