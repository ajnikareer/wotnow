import { useEffect, useState } from 'react'
import { Icon } from './Icon'
import { useToast } from '../lib/toast'

export interface ShareModalData {
  title: string
  score: number
  correct: number
  total: number
  rank: number
  players: number
  xpAwarded: number
  nickname?: string
}

export function ShareModal({
  data,
  onClose,
}: {
  data: ShareModalData | null
  onClose: () => void
}) {
  const toast = useToast()
  const [copied, setCopied] = useState(false)

  useEffect(() => {
    if (!data) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose()
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [data, onClose])

  if (!data) return null

  const shareUrl = typeof window !== 'undefined' ? `${window.location.origin}/#/live` : 'https://wotnow.in/#/live'
  const shareText = `🏆 I scored ${data.score} pts (${data.correct}/${data.total} correct, Rank #${data.rank} of ${data.players}) on WotNow Live Quiz: "${data.title}"!\n\nCan you beat my score? Play live on WotNow:\n${shareUrl}`

  const handleCopy = async () => {
    try {
      if (navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(shareText)
      } else {
        const textarea = document.createElement('textarea')
        textarea.value = shareText
        document.body.appendChild(textarea)
        textarea.select()
        document.execCommand('copy')
        document.body.removeChild(textarea)
      }
      setCopied(true)
      toast('Scorecard copied to clipboard! 📋')
      setTimeout(() => setCopied(false), 2500)
    } catch {
      toast('Failed to copy, please share manually')
    }
  }

  const handleWhatsApp = () => {
    const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(shareText)}`
    window.open(waUrl, '_blank', 'noopener,noreferrer')
  }

  const handleTwitter = () => {
    const twUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(shareText)}`
    window.open(twUrl, '_blank', 'noopener,noreferrer')
  }

  const handleSystemShare = async () => {
    if (typeof navigator !== 'undefined' && navigator.share) {
      try {
        await navigator.share({
          title: `WotNow Live Quiz: ${data.title}`,
          text: shareText,
          url: shareUrl,
        })
      } catch (err: unknown) {
        if ((err as Error)?.name !== 'AbortError') {
          handleCopy()
        }
      }
    } else {
      handleCopy()
    }
  }

  const hasNativeShare = typeof navigator !== 'undefined' && typeof navigator.share === 'function'

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-rise"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
    >
      <div
        className="card max-w-md w-full p-6 text-left shadow-2xl border border-line bg-surface relative overflow-hidden"
        onClick={e => e.stopPropagation()}
      >
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 w-8 h-8 rounded-full bg-surface2 hover:bg-surface3 flex items-center justify-center text-muted hover:text-ink transition"
          aria-label="Close"
        >
          <Icon name="x" className="w-4 h-4" />
        </button>

        {/* Modal Header */}
        <div className="flex items-center gap-2 mb-4">
          <div className="w-10 h-10 rounded-xl bg-brand-violet/15 border border-brand-violet/30 flex items-center justify-center text-brand-violet">
            <Icon name="trophy" className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-lg font-bold text-ink leading-tight">Share Quiz Result</h3>
            <p className="text-xs text-muted">Challenge your friends and family</p>
          </div>
        </div>

        {/* Preview Scorecard */}
        <div className="rounded-2xl border border-line bg-surface2/70 p-4 mb-5 relative overflow-hidden">
          <div className="flex items-center justify-between text-xs text-muted mb-2 font-medium">
            <span className="flex items-center gap-1.5 font-bold text-brand-violet">
              <span className="w-2 h-2 rounded-full bg-brand-violet animate-pulse" />
              WotNow Live Quiz
            </span>
            {data.nickname && <span className="chip text-[11px] py-0.5">{data.nickname}</span>}
          </div>

          <div className="font-bold text-base text-ink mb-1">{data.title}</div>

          <div className="flex items-baseline gap-2 mb-3">
            <div className="font-display text-4xl font-extrabold text-ink">#{data.rank}</div>
            <div className="text-xs text-muted font-medium">of {data.players} {data.players === 1 ? 'learner' : 'learners'}</div>
          </div>

          <div className="grid grid-cols-3 gap-2 text-center">
            <div className="rounded-xl bg-surface border border-line/50 p-2">
              <div className="font-display font-bold text-base text-ink">{data.score}</div>
              <div className="text-[10px] text-muted uppercase tracking-wider font-semibold">Points</div>
            </div>
            <div className="rounded-xl bg-surface border border-line/50 p-2">
              <div className="font-display font-bold text-base text-ink">{data.correct}/{data.total}</div>
              <div className="text-[10px] text-muted uppercase tracking-wider font-semibold">Correct</div>
            </div>
            <div className="rounded-xl bg-surface border border-line/50 p-2">
              <div className="font-display font-bold text-base grad-text">+{data.xpAwarded}</div>
              <div className="text-[10px] text-muted uppercase tracking-wider font-semibold">XP</div>
            </div>
          </div>
        </div>

        {/* Share Action Buttons */}
        <div className="space-y-2.5">
          {/* WhatsApp */}
          <button
            onClick={handleWhatsApp}
            className="w-full flex items-center justify-center gap-3 py-3 px-4 rounded-2xl bg-[#25D366] hover:bg-[#20ba59] text-white font-bold text-sm shadow-sm transition active:scale-[0.98]"
          >
            <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current" aria-hidden="true">
              <path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24h-.18zm4.52 11.66c-.25-.13-1.47-.72-1.7-.81-.23-.08-.39-.13-.56.13-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.13-1.06-.39-2.02-1.25-.75-.67-1.26-1.5-1.4-1.75-.15-.25-.02-.39.11-.51.11-.11.25-.29.38-.44.12-.14.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.24.9 2.44 1.03 2.61.13.17 1.77 2.7 4.29 3.79.6.26 1.07.41 1.44.53.6.19 1.15.16 1.58.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.06-.1-.23-.17-.48-.29z" />
            </svg>
            Share on WhatsApp
          </button>

          {/* X / Twitter */}
          <button
            onClick={handleTwitter}
            className="w-full flex items-center justify-center gap-3 py-3 px-4 rounded-2xl bg-[#0F1419] dark:bg-[#1E232B] hover:opacity-90 text-white font-bold text-sm shadow-sm transition active:scale-[0.98] border border-line"
          >
            <svg viewBox="0 0 24 24" className="w-4 h-4 fill-current" aria-hidden="true">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 23.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
            </svg>
            Post to X / Twitter
          </button>

          {/* System Share (mobile / supported browsers) */}
          {hasNativeShare && (
            <button
              onClick={handleSystemShare}
              className="w-full flex items-center justify-center gap-2 py-3 px-4 rounded-2xl bg-surface2 hover:bg-surface3 text-ink font-semibold text-sm border border-line transition active:scale-[0.98]"
            >
              <Icon name="share" className="w-4 h-4 text-brand-violet" />
              More Share Options (System Dialog)
            </button>
          )}

          {/* Copy Link / Scorecard */}
          <button
            onClick={handleCopy}
            className={`w-full flex items-center justify-center gap-2 py-3 px-4 rounded-2xl font-semibold text-sm border transition active:scale-[0.98] ${
              copied
                ? 'bg-ok/15 text-ok border-ok/40'
                : 'bg-surface hover:bg-surface2 text-ink border-line'
            }`}
          >
            <Icon name={copied ? 'check' : 'share'} className="w-4 h-4" />
            {copied ? 'Copied to Clipboard! ✓' : 'Copy Scorecard Text & Link'}
          </button>
        </div>
      </div>
    </div>
  )
}
