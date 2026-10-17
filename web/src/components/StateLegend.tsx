import '../styles/neon.css'

/** One line that explains the card borders. */
export function StateLegend() {
  const item = (cls: string, text: string) => (
    <span className="inline-flex items-center gap-1.5"><span className={`wn-dot ${cls}`} aria-hidden />{text}</span>
  )
  return (
    <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-[12px] text-muted mb-3 px-1" aria-label="What the card borders mean">
      {item('wn-new', 'New since your last visit')}
      {item('wn-done', 'Done')}
      {item('wn-retry', 'Try again')}
    </div>
  )
}
