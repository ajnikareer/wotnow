import { useState, type ReactNode } from 'react'
import { useToast } from '../../lib/toast'

export type Tone = 'ok' | 'warn' | 'bad' | 'info' | 'mute'
const TONES: Record<Tone, string> = {
  ok: 'bg-ok/15 text-ok', warn: 'bg-warn/15 text-warn', bad: 'bg-bad/15 text-bad', info: 'bg-brand-violet/15 text-brand-violet', mute: 'bg-surface3 text-muted',
}

export function Badge({ tone = 'mute', children }: { tone?: Tone; children: ReactNode }) {
  return <span className={`inline-block text-[11px] font-bold px-2 py-0.5 rounded-md ${TONES[tone]}`}>{children}</span>
}

export function Section({ title, hint, right, children }: { title: string; hint?: string; right?: ReactNode; children: ReactNode }) {
  return (
    <section className="card p-5 mb-5">
      <div className="flex items-start gap-3 mb-3">
        <div className="flex-1 min-w-0"><h2 className="text-lg font-bold">{title}</h2>{hint && <p className="text-sm text-muted mt-0.5">{hint}</p>}</div>
        {right}
      </div>
      {children}
    </section>
  )
}

export function Stat({ label, value, sub, tone }: { label: string; value: ReactNode; sub?: ReactNode; tone?: Tone }) {
  return (
    <div className="rounded-2xl bg-surface2 border border-line p-3.5">
      <div className="text-[12px] text-muted">{label}</div>
      <div className="font-display text-2xl font-bold mt-0.5 flex items-center gap-2">{value}{tone && <Badge tone={tone}>{tone === 'ok' ? 'OK' : tone === 'warn' ? 'CHECK' : tone === 'bad' ? 'DOWN' : '·'}</Badge>}</div>
      {sub && <div className="text-xs text-muted mt-0.5">{sub}</div>}
    </div>
  )
}

export function Toggle({ on, onChange, label, disabled }: { on: boolean; onChange: (v: boolean) => void; label?: string; disabled?: boolean }) {
  return (
    <button type="button" role="switch" aria-checked={on} disabled={disabled} onClick={() => onChange(!on)}
      className={`inline-flex items-center gap-2 text-sm font-medium disabled:opacity-40 ${on ? 'text-ink' : 'text-muted'}`}>
      <span className={`w-10 h-6 rounded-full p-0.5 transition ${on ? 'grad-bg' : 'bg-surface3'}`}><span className={`block w-5 h-5 rounded-full bg-white shadow transition ${on ? 'translate-x-4' : ''}`} /></span>
      {label}
    </button>
  )
}

export function Loading({ text = 'Loading…' }: { text?: string }) {
  return <div className="p-10 text-center text-muted"><div className="skeleton h-6 w-40 mx-auto mb-3" />{text}</div>
}

export function ErrorBox({ message, onRetry }: { message: string; onRetry?: () => void }) {
  return (
    <div className="p-4 rounded-2xl bg-bad/10 border border-bad/25 text-sm flex items-center gap-3">
      <span className="flex-1">⚠️ {message}</span>{onRetry && <button className="btn-ghost !py-1.5" onClick={onRetry}>Retry</button>}
    </div>
  )
}

/** Runs an async admin action with a busy flag and toast feedback. */
export function useAction() {
  const toast = useToast()
  const [busy, setBusy] = useState(false)
  const run = async <T,>(fn: () => Promise<T>, okMsg?: string): Promise<T | undefined> => {
    setBusy(true)
    try { const r = await fn(); if (okMsg) toast(okMsg); return r }
    catch (e: any) { toast('⚠️ ' + (e?.message || 'Something went wrong')); return undefined }
    finally { setBusy(false) }
  }
  return { busy, run }
}

export const lines = (s: string): string[] => s.split('\n').map(x => x.trim()).filter(Boolean)
export const when = (v?: string | number | null): string => {
  if (v === undefined || v === null || v === '') return '–'
  const d = typeof v === 'number' ? new Date(v * 1000) : new Date(v)
  return isNaN(d.getTime()) ? String(v) : d.toLocaleString('en-IN', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' })
}
export const pct = (n: number) => `${Math.round(n * 100)}%`
export const TEXTAREA = 'input font-mono text-[13px] leading-relaxed min-h-[110px] resize-y'
