import { useId } from 'react'
import type { Mood } from '../lib/types'

const GRAD = (id: string) => (
  <linearGradient id={id} gradientUnits="userSpaceOnUse" x1="0" y1="50" x2="420" y2="75">
    <stop offset="0%" stopColor="#EA4335" />
    <stop offset="45%" stopColor="#F97316" />
    <stop offset="100%" stopColor="#FBBF24" />
  </linearGradient>
)
const GRAD_BG = (id: string) => (
  <linearGradient id={id} x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stopColor="#EA4335" stopOpacity="0.18" />
    <stop offset=".55" stopColor="#F97316" stopOpacity="0.12" />
    <stop offset="1" stopColor="#FBBF24" stopOpacity="0.08" />
  </linearGradient>
)
const BRAND_COLOR = '#F97316'
const S = { fill: 'none', stroke: BRAND_COLOR, strokeWidth: 18, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const }

function LogoEye({ cx }: { cx: number }) {
  return (
    <g>
      <circle cx={cx} cy={75} r={28} fill="#fff" stroke="#EA580C" strokeWidth={6.5} />
      <circle cx={cx + 7} cy={67} r={11.5} fill="#1C1917" />
      <circle cx={cx + 12} cy={63} r={3.5} fill="#F97316" />
      <circle cx={cx + 5} cy={70} r={2} fill="#fff" />
    </g>
  )
}

/** Primary logo: clean sunset coral/amber wotnow lettering matching the mascot emoji. */
export function Logo({ className = 'h-5.5' }: { className?: string }) {
  const id = useId().replace(/:/g, '')
  return (
    <svg viewBox="-10 20 440 90" className={`${className} filter drop-shadow-[0_2px_10px_rgba(249,115,22,0.38)]`} role="img" aria-label="wotnow">
      <defs>
        <linearGradient id={`sunset-${id}`} x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#EA4335" />
          <stop offset="45%" stopColor="#F97316" />
          <stop offset="100%" stopColor="#FBBF24" />
        </linearGradient>
      </defs>
      <path d="M0 50 L15 100 L29 64 L43 100 L58 50" fill="none" stroke={`url(#sunset-${id})`} strokeWidth={18} strokeLinecap="round" strokeLinejoin="round" />
      <LogoEye cx={109} />
      <path d="M174 30 V86 Q174 100 189 100 M160 52 H190" fill="none" stroke={`url(#sunset-${id})`} strokeWidth={18} strokeLinecap="round" strokeLinejoin="round" />
      <path d="M216 100 V50 M216 74 Q216 50 238 50 Q260 50 260 74 V100" fill="none" stroke={`url(#sunset-${id})`} strokeWidth={18} strokeLinecap="round" strokeLinejoin="round" />
      <LogoEye cx={311} />
      <path d="M362 50 L377 100 L391 64 L405 100 L420 50" fill="none" stroke={`url(#sunset-${id})`} strokeWidth={18} strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}

/** The bubble mascot. Moods: think · look · happy · wow. */
export function Mascot({ mood = 'look', size = 64, animate = true, className = '' }:
  { mood?: Mood; size?: number; animate?: boolean; className?: string }) {
  const id = useId().replace(/:/g, '')
  const eye = (cx: number) => {
    if (mood === 'happy') return <path key={cx} d={`M${cx - 18} ${90} Q${cx} ${62} ${cx + 18} ${90}`} fill="none" stroke="#fff" strokeWidth={12} strokeLinecap="round" />
    const pupil = mood === 'think' ? { dx: 8, dy: -9, r: 10.5 } : mood === 'wow' ? { dx: 0, dy: 0, r: 6 } : { dx: 0, dy: 4, r: 11 }
    return (
      <g key={cx} className={animate ? 'animate-blink' : ''} style={{ transformOrigin: `${cx}px 84px`, transformBox: 'view-box' as any }}>
        <circle cx={cx} cy={84} r={27} fill="#fff" />
        <g className={animate && mood === 'think' ? 'animate-wander' : ''}>
          <circle cx={cx + pupil.dx} cy={84 + pupil.dy} r={pupil.r} fill="#141824" />
          {mood !== 'wow' && <circle cx={cx + pupil.dx + 4} cy={84 + pupil.dy - 4} r={3} fill="#fff" />}
        </g>
      </g>
    )
  }
  const motion = !animate ? '' : mood === 'wow' ? 'animate-shake' : mood === 'happy' ? 'animate-pop' : 'animate-bob'
  return (
    <svg viewBox="0 0 200 200" width={size} height={size} className={`${motion} ${className}`} role="img" aria-label={`wotnow mascot, ${mood}`}>
      <defs>{GRAD('mg' + id)}</defs>
      <path d="M58 20 H142 Q192 20 192 70 V98 Q192 148 142 148 H102.8 L69.2 169 L73.4 148 H58 Q8 148 8 98 V70 Q8 20 58 20 Z" fill={`url(#mg${id})`} />
      {eye(72)}{eye(128)}
    </svg>
  )
}
