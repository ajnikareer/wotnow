import { useEffect, useRef, useState } from 'react'
import { AppShell } from '../components/AppShell'
import { Mascot } from '../components/Brand'
import { Icon } from '../components/Icon'
import { AgentAvatar, agentOf } from '../components/ui'
import { api } from '../lib/api'
import { useAsync } from '../lib/hooks'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'

const QTIME = 10

export default function LiveQuiz() {
  const { data: quiz } = useAsync(() => api.liveQuiz(), [])
  const { refreshMe } = useSession()
  const toast = useToast()
  const [phase, setPhase] = useState<'lobby' | 'q' | 'reveal' | 'end'>('lobby')
  const [count, setCount] = useState(5)
  const [qi, setQi] = useState(0)
  const [left, setLeft] = useState(QTIME)
  const [pick, setPick] = useState<string | null>(null)
  const [points, setPoints] = useState(0)
  const [correct, setCorrect] = useState(0)
  const [result, setResult] = useState<{ rank: number; players: number; xpAwarded: number }>()
  const answeredAt = useRef<number>(QTIME)

  useEffect(() => {
    if (phase !== 'lobby' || !quiz) return
    if (count <= 0) { setPhase('q'); setLeft(QTIME); return }
    const t = setTimeout(() => setCount(c => c - 1), 1000); return () => clearTimeout(t)
  }, [phase, count, quiz])

  useEffect(() => {
    if (phase !== 'q') return
    if (left <= 0) { setPhase('reveal'); return }
    const t = setTimeout(() => setLeft(l => l - 1), 1000); return () => clearTimeout(t)
  }, [phase, left])

  useEffect(() => {
    if (phase !== 'reveal' || !quiz) return
    const q = quiz.questions[qi]
    if (pick === q.correct) { setCorrect(c => c + 1); setPoints(p => p + 10 + Math.max(0, answeredAt.current)) }
    const t = setTimeout(async () => {
      if (qi + 1 < quiz.questions.length) { setQi(qi + 1); setPick(null); setLeft(QTIME); answeredAt.current = QTIME; setPhase('q') }
      else { setPhase('end') }
    }, 3200)
    return () => clearTimeout(t)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [phase])

  useEffect(() => {
    if (phase === 'end' && !result) api.submitQuiz(points).then(r => { setResult(r); refreshMe() })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [phase])

  if (!quiz) return <AppShell rail={false}><div className="max-w-xl mx-auto skeleton h-96" /></AppShell>
  const a = agentOf(quiz.agentId)
  const q = quiz.questions[qi]
  const choose = (id: string) => { if (phase !== 'q' || pick) return; setPick(id); answeredAt.current = left; setTimeout(() => setPhase('reveal'), 400) }
  const restart = () => { setPhase('lobby'); setCount(3); setQi(0); setPick(null); setPoints(0); setCorrect(0); setResult(undefined) }

  return (
    <AppShell rail={false}>
      <div className="max-w-xl mx-auto">
        <div className="card overflow-hidden" style={{ background: `radial-gradient(500px 300px at 50% 0%, ${a.colors[0]}33, transparent 70%), rgb(var(--surface))` }}>
          <div className="flex items-center gap-3 px-5 pt-5">
            <AgentAvatar agent={a} size={40} />
            <div className="leading-tight"><div className="flex items-center gap-1.5 text-[11px] font-extrabold tracking-wider text-bad"><span className="w-2 h-2 rounded-full bg-bad animate-pulse" />LIVE</div>
              <div className="font-bold">{quiz.title}</div></div>
            {quiz.players > 0 ? (
              <span className="ml-auto chip"><Icon name="users" className="w-3.5 h-3.5" />{quiz.players} {quiz.players === 1 ? 'player' : 'players'}</span>
            ) : (
              <span className="ml-auto chip text-brand-violet font-bold text-xs">⚡ Speed Blitz · 5 Qs</span>
            )}
          </div>

          {phase === 'lobby' && (
            <div className="p-8 text-center">
              <Mascot mood="look" size={110} className="mx-auto" />
              <div className="text-muted mt-4">Starting in</div>
              <div className="font-display text-7xl font-bold grad-text animate-pop" key={count}>{count}</div>
              <p className="text-sm text-muted mt-3">5 questions · 10 seconds each · faster correct answers score more</p>
            </div>
          )}

          {(phase === 'q' || phase === 'reveal') && (
            <div className="p-5 md:p-6">
              <div className="flex gap-1.5">{quiz.questions.map((_, i) => <span key={i} className={`h-1.5 flex-1 rounded-full ${i < qi || (i === qi && phase === 'reveal') ? 'grad-bg' : i === qi ? 'bg-ink/40' : 'bg-surface3'}`} />)}</div>
              <div className="text-center text-xs text-muted mt-3">Question {qi + 1} of {quiz.questions.length} · {points} pts</div>
              <div className="w-24 h-24 rounded-full mx-auto mt-4 grid place-items-center" style={{ background: `conic-gradient(#FDE047 0 ${(left / QTIME) * 100}%, rgb(var(--surface3)) ${(left / QTIME) * 100}% 100%)` }}>
                <div className="w-[78px] h-[78px] rounded-full bg-surface grid place-items-center font-display text-3xl font-bold">{phase === 'reveal' ? (pick === q.correct ? '✓' : '✗') : left}</div>
              </div>
              <h2 className="text-center text-xl md:text-2xl font-bold mt-5 leading-snug">{q.text}</h2>
              <div className="grid gap-2.5 mt-5">
                {q.options.map((o, i) => {
                  const isC = phase === 'reveal' && o.id === q.correct
                  const isWrong = phase === 'reveal' && o.id === pick && o.id !== q.correct
                  return (
                    <button key={o.id} onClick={() => choose(o.id)} disabled={phase !== 'q' || !!pick}
                      className={`flex items-center gap-3 p-3.5 rounded-2xl border text-left text-[15px] font-medium transition active:scale-[.99]
                        ${isC ? 'border-ok bg-ok/15' : isWrong ? 'border-bad bg-bad/10 animate-shake' : pick === o.id ? 'border-warn bg-warn/10' : 'border-line bg-surface2 hover:border-brand-violet/50'}`}>
                      <span className={`w-8 h-8 rounded-xl grid place-items-center text-sm font-extrabold shrink-0 ${isC ? 'bg-ok text-white' : pick === o.id ? 'bg-warn text-[#111]' : 'bg-surface3'}`}>{'ABCD'[i]}</span>{o.text}
                    </button>
                  )
                })}
              </div>
              {phase === 'reveal' && <div className="mt-4 p-3.5 rounded-2xl bg-surface2 text-sm animate-rise">💡 {q.explanation}</div>}
            </div>
          )}

          {phase === 'end' && (
            <div className="p-8 text-center">
              <Mascot mood={correct >= 3 ? 'happy' : 'look'} size={110} className="mx-auto" />
              <div className="text-muted mt-3">{quiz.title} · complete</div>
              {result ? (
                <div className="font-display text-6xl font-bold mt-1">
                  #{result.rank}
                  {result.players > 1 && <span className="text-xl text-muted"> of {result.players}</span>}
                </div>
              ) : (
                <div className="skeleton h-14 w-40 mx-auto mt-2" />
              )}
              <div className="grid grid-cols-3 gap-2 mt-6">
                <div className="rounded-2xl bg-surface2 p-3"><div className="font-display text-2xl font-bold">{correct}/{quiz.questions.length}</div><div className="text-xs text-muted">correct</div></div>
                <div className="rounded-2xl bg-surface2 p-3"><div className="font-display text-2xl font-bold">{points}</div><div className="text-xs text-muted">points</div></div>
                <div className="rounded-2xl bg-surface2 p-3"><div className="font-display text-2xl font-bold grad-text">+{result?.xpAwarded ?? points}</div><div className="text-xs text-muted">XP</div></div>
              </div>
              <div className="flex gap-2 justify-center mt-6">
                <button className="btn-grad" onClick={() => toast('Share card ready 📤')}><Icon name="share" className="w-4 h-4" />Share result</button>
                <button className="btn-ghost" onClick={restart}>Play again</button>
              </div>
            </div>
          )}
        </div>
      </div>
    </AppShell>
  )
}
