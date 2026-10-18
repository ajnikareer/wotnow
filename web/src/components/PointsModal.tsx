import { useEffect } from 'react'
import { Icon } from './Icon'

export interface PointsModalData {
  xp: number
  title?: string
  subtitle?: string
  streak?: number
  totalXp?: number
}

export function PointsModal({
  data,
  onClose,
}: {
  data: PointsModalData | null
  onClose: () => void
}) {
  useEffect(() => {
    if (!data) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose()
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [data, onClose])

  if (!data) return null

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/40 backdrop-blur-sm animate-rise"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
    >
      <div
        className="card max-w-sm w-full p-6 text-center shadow-2xl border border-line bg-surface relative"
        onClick={e => e.stopPropagation()}
      >
        {/* Sober icon badge */}
        <div className="w-14 h-14 mx-auto rounded-2xl bg-brand-violet/15 border border-brand-violet/30 flex items-center justify-center text-brand-violet mb-3">
          <Icon name="sparkle" className="w-7 h-7" />
        </div>

        {/* Points display */}
        <div className="font-display text-4xl font-extrabold grad-text tracking-tight">
          +{data.xp} XP
        </div>

        <h3 className="text-lg font-bold text-ink mt-2">
          {data.title || 'Well done!'}
        </h3>

        {data.subtitle && (
          <p className="text-sm text-muted mt-1.5 leading-relaxed">
            {data.subtitle}
          </p>
        )}

        {/* Stats summary: streak and total */}
        {(data.streak !== undefined || data.totalXp !== undefined) && (
          <div className="mt-4 pt-3 border-t border-line flex items-center justify-center gap-4 text-xs font-semibold text-muted">
            {data.streak !== undefined && (
              <span className="inline-flex items-center gap-1">
                🔥 {data.streak}-day streak
              </span>
            )}
            {data.totalXp !== undefined && (
              <span className="inline-flex items-center gap-1">
                ⭐ {data.totalXp.toLocaleString('en-IN')} total XP
              </span>
            )}
          </div>
        )}

        <button
          className="btn-ink w-full mt-5 !rounded-xl"
          onClick={onClose}
          autoFocus
        >
          Continue
        </button>
      </div>
    </div>
  )
}
