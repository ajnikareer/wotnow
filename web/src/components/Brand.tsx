import { useId } from 'react'
import type { Mood } from '../lib/types'

const GRAD = (id: string) => (
  <linearGradient id={id} x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stopColor="#8B5CF6" /><stop offset=".55" stopColor="#22D3EE" /><stop offset="1" stopColor="#34D399" />
  </linearGradient>
)
const GRAD_BG = (id: string) => (
  <linearGradient id={id} x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stopColor="#8B5CF6" stopOpacity="0.12" />
    <stop offset=".55" stopColor="#22D3EE" stopOpacity="0.08" />
    <stop offset="1" stopColor="#34D399" stopOpacity="0.06" />
  </linearGradient>
)
const S = { fill: 'none', stroke: 'currentColor', strokeWidth: 20, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const }

function LogoEye({ cx }: { cx: number }) {
  return (
    <g>
      <circle cx={cx} cy={75} r={28} fill="#fff" stroke="currentColor" strokeWidth={7} />
      <circle cx={cx + 7} cy={67} r={11.5} fill="#141824" />
      <circle cx={cx + 12} cy={63} r={3.5} fill="#22D3EE" />
      <circle cx={cx + 5} cy={70} r={2} fill="#fff" />
    </g>
  )
}

/** Primary logo: clean wotnow lettering with cute eyes as the o's. */
export function Logo({ className = 'h-9' }: { className?: string }) {
  const id = useId().replace(/:/g, '')
  return (
    <svg viewBox="-10 20 440 90" className={`${className} filter drop-shadow-[0_2px_8px_rgba(139,92,246,0.18)]`} role="img" aria-label="wotnow">
      <defs>
        {GRAD('lg' + id)}
      </defs>
      <path d="M0 50 L15 100 L29 64 L43 100 L58 50" {...S} />
      <LogoEye cx={109} />
      <path d="M174 30 V86 Q174 100 189 100 M160 52 H190" {...S} />
      <path d="M216 100 V50 M216 74 Q216 50 238 50 Q260 50 260 74 V100" {...S} />
      <LogoEye cx={311} />
      <path d="M362 50 L377 100 L391 64 L405 100 L420 50" {...S} />
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
