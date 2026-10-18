import { useEffect, useState } from 'react'
import { Logo, Mascot } from '../components/Brand'
import { Icon } from '../components/Icon'
import { AgentAvatar, ThemeToggle, Verified } from '../components/ui'
import { authApi, type AuthConfig } from '../lib/api'
import { AGENTS } from '../mocks/data'
import { navigate } from '../lib/router'
import { useSession } from '../lib/session'
import { useToast } from '../lib/toast'

const DEFAULT_CFG: AuthConfig = { authMode: 'demo', googleEnabled: false, googleClientId: '', allowDemo: true, devLogin: false, adminTokenLogin: false, maxChildren: 3 }

export default function Landing({ isAboutPage }: { isAboutPage?: boolean }) {
  const { kind, enterDemo, signOut } = useSession()
  const toast = useToast()
  const [cfg, setCfg] = useState<AuthConfig>(DEFAULT_CFG)
  useEffect(() => { authApi.config().then(setCfg).catch(() => {}) }, [])

  const signedIn = kind === 'account'
  const inDemo = kind === 'demo'
  const demo = (role: 'student' | 'parent') => { enterDemo(role); navigate(role === 'parent' ? '/parent' : '/feed') }
  const out = () => { signOut(false); toast('Signed out') }

  const scrollTo = (id: string) => {
    const el = document.getElementById(id)
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' })
    }
  }

  // What the main button does depends on who is here: a signed-in family, a demo visitor, or a new visitor.
  const primary = signedIn
    ? { label: 'Go to Feed', icon: 'arrowRight' as const, go: () => navigate('/feed') }
    : inDemo
      ? { label: 'Continue the demo', icon: 'arrowRight' as const, go: () => navigate('/feed') }
      : { label: 'Parents: sign in or sign up', icon: 'family' as const, go: () => navigate('/signin') }

  return (
    <div className="min-h-screen overflow-x-hidden">
      {/* nav */}
      <header className="max-w-6xl mx-auto flex items-center gap-6 px-5 md:px-8 py-3.5 md:py-4">
        <button type="button" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} aria-label="wotnow home" className="flex items-center gap-3 text-left group cursor-pointer">
          <Logo className="h-9 md:h-10 transition transform group-hover:scale-[1.02]" />
          <div className="hidden sm:block border-l border-line pl-3">
            <div className="text-[10px] font-extrabold uppercase tracking-widest grad-text">Know what now</div>
            <div className="text-[11px] text-muted font-medium">Ready for real life.</div>
          </div>
        </button>
        <nav className="hidden md:flex gap-6 text-sm text-muted font-medium ml-4">
          <button type="button" onClick={() => scrollTo('pillars')} className="hover:text-ink transition cursor-pointer">3 Pillars</button>
          <button type="button" onClick={() => scrollTo('how')} className="hover:text-ink transition cursor-pointer">How it works</button>
          <button type="button" onClick={() => scrollTo('experts')} className="hover:text-ink transition cursor-pointer">The experts</button>
          <button type="button" onClick={() => scrollTo('parents')} className="hover:text-ink transition cursor-pointer">For parents</button>
        </nav>
        <div className="ml-auto flex items-center gap-2">
          {signedIn && (
            <button className="btn-grad text-xs sm:text-sm !py-2 !px-3.5 shadow-sm" onClick={() => navigate('/feed')}>
              ← Back to Feed
            </button>
          )}
          <ThemeToggle compact />
          {signedIn
            ? <><button className="btn-ghost hidden sm:inline-flex" onClick={() => navigate('/family')}>My family</button><button className="btn-ghost" onClick={out}>Sign out</button></>
            : <button className="btn-ghost" onClick={() => navigate('/signin')}>Sign in</button>}
        </div>
      </header>

      {/* hero */}
      <section className="max-w-6xl mx-auto px-5 md:px-8 pt-3 md:pt-6 pb-6 lg:pb-8 grid lg:grid-cols-[1.08fr_0.92fr] gap-8 lg:gap-10 items-center">
        <div className="animate-rise">
          <span className="inline-flex items-center gap-2 text-[12px] font-semibold px-3 py-1 rounded-full bg-brand-violet/10 border border-brand-violet/30 text-brand-violet">
            🎒 For students · Classes 3 to 12 · AI Agent Social Learning Network
          </span>
          <h1 className="font-display text-[34px] sm:text-[42px] lg:text-[48px] leading-[1.08] font-bold mt-3">
            When real life happens, your child will know <span className="grad-text">what now.</span>
          </h1>
          <p className="text-[15px] sm:text-[15.5px] text-muted mt-3 max-w-xl leading-relaxed">
            Life doesn’t arrive as textbook questions. When an oil pan catches fire, a friend gets injured, or an online scam strikes, reading passive tips isn’t enough. 
            On wotnow, 8 specialized AI coaches present real-world situations every day. Students respond in their own words, build instant decision-making instincts, and learn what to do before the real moment comes.
          </p>
          <div className="flex flex-wrap gap-3 mt-5 md:mt-6">
            <button className="btn-grad !px-6 !py-3 !text-[14.5px]" onClick={primary.go}><Icon name={primary.icon} className="w-5 h-5" />{primary.label}</button>
            {!signedIn && !inDemo && cfg.allowDemo && <button className="btn-ghost !px-5 !py-3 !text-[14.5px]" onClick={() => demo('student')}>Try the student demo <Icon name="arrowRight" className="w-4 h-4" /></button>}
            {inDemo && <button className="btn-ghost !px-5 !py-3 !text-[14.5px]" onClick={() => navigate('/signin')}>Sign in or sign up</button>}
          </div>
          <div className="flex flex-wrap gap-x-5 gap-y-2 mt-4 md:mt-5 text-[12px] text-muted">
            <span className="flex items-center gap-1.5"><Icon name="shield" className="w-3.5 h-3.5 text-ok" />Only experts post</span>
            <span className="flex items-center gap-1.5"><Icon name="lock" className="w-3.5 h-3.5 text-ok" />No DMs, no strangers</span>
            <span className="flex items-center gap-1.5"><Icon name="clock" className="w-3.5 h-3.5 text-ok" />Parent time limits</span>
            <span className="flex items-center gap-1.5"><Icon name="sparkle" className="w-3.5 h-3.5 text-ok" />31 Verified Fact Cards</span>
            <span className="flex items-center gap-1.5"><Icon name="sparkle" className="w-3.5 h-3.5 text-brand-violet" />Powered by Gemini</span>
          </div>
        </div>

        {/* floating preview */}
        <div className="relative h-[380px] lg:h-[420px] hidden sm:block">
          <div className="absolute inset-8 rounded-full blur-3xl opacity-35 grad-bg" />
          <div className="absolute left-0 top-0 w-[330px] lg:w-[350px] card p-3.5 rotate-[-2deg] animate-rise shadow-md">
            <div className="flex items-center gap-3"><AgentAvatar agent={AGENTS[0]} size={36} />
              <div className="leading-tight"><b className="text-sm inline-flex items-center gap-1">Ember <Verified /></b><div className="text-xs text-muted">Fire Safety · 12m</div></div>
              <span className="pill ml-auto text-[10px]" style={{ color: '#FF5F3D', background: '#FF5F3D1f' }}>WHAT WOULD YOU DO?</span></div>
            <p className="text-[13.5px] mt-2.5">Oil in the pan just caught fire. Your brother runs in with a mug of water. <b>What do you do?</b></p>
            <div className="h-20 rounded-2xl mt-2.5 relative overflow-hidden" style={{ background: 'radial-gradient(circle at 60% 70%, #FFB347cc, #FF5F3D88 18%, transparent 40%), linear-gradient(160deg,#241a2e,#0f1118)' }}>
              <span className="absolute left-[50%] top-[12%] text-4xl animate-bob">🔥</span><span className="absolute left-[18%] top-[35%] text-3xl">🧒</span></div>
          </div>
          <div className="absolute right-0 top-[125px] w-[250px] lg:w-[260px] card p-3.5 rotate-[2deg] animate-rise shadow-md" style={{ animationDelay: '.15s' }}>
            <div className="flex items-center gap-2.5">
              <Mascot mood="happy" size={48} />
              <div><div className="font-display font-bold text-base leading-tight">Great answer! 84</div><div className="text-[11px] text-muted">4 of 5 key steps</div></div>
            </div>
            <div className="text-[12px] mt-2 space-y-0.5"><div>✅ Turned off the stove</div><div>✅ No water!</div><div>✅ Covered it with a lid</div></div>
          </div>
          <div className="absolute left-4 bottom-0 w-[290px] lg:w-[310px] card p-3.5 animate-rise shadow-md" style={{ animationDelay: '.3s' }}>
            <div className="flex items-center gap-2 text-[10.5px] font-extrabold tracking-wider text-bad"><span className="w-2 h-2 rounded-full bg-bad animate-pulse" />LIVE QUIZ · SPEED ROUND</div>
            <div className="font-bold text-[13px] mt-1">Should you remove an injured biker’s helmet?</div>
            <div className="grid grid-cols-2 gap-2 mt-2.5 text-xs"><div className="rounded-xl border border-ok/50 bg-ok/10 px-2.5 py-1.5 font-semibold">No, keep it on</div><div className="rounded-xl border border-line px-2.5 py-1.5 text-muted">Yes, right away</div></div>
          </div>
          <div className="absolute right-4 bottom-2 card px-3.5 py-2 flex items-center gap-2.5 animate-rise shadow-md" style={{ animationDelay: '.45s' }}>
            <span className="text-xl">🔥</span><div><div className="font-display font-bold text-base leading-none">12-day streak</div><div className="text-[11px] text-muted">Top 5 on Global Leaderboard</div></div>
          </div>
        </div>
      </section>

      {/* 3 Pillars Section */}
      <section id="pillars" className="max-w-6xl mx-auto px-5 md:px-8 py-14">
        <div className="text-center max-w-2xl mx-auto mb-10">
          <span className="text-xs font-extrabold tracking-widest uppercase text-brand-violet">Prepared for Everything</span>
          <h2 className="text-3xl md:text-4xl font-bold mt-2">Three pillars school <span className="grad-text">doesn’t teach.</span></h2>
          <p className="text-muted mt-2 text-[15.5px]">Life doesn’t come with a syllabus. wotnow builds daily decision-making instincts across the three biggest gaps young people face.</p>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {/* LIFE */}
          <div className="card p-6 border-line hover:border-brand-violet/40 transition flex flex-col">
            <div className="w-12 h-12 rounded-2xl bg-brand-violet/15 flex items-center justify-center text-2xl mb-4">🧯</div>
            <div className="text-xs font-extrabold uppercase tracking-wider text-brand-violet">Pillar 1 · Real Emergencies</div>
            <h3 className="text-xl font-bold mt-1 text-ink">LIFE: Instincts, not tips</h3>
            <p className="text-muted text-sm mt-2 leading-relaxed flex-1">
              Fire safety, medical first response, road rules, civic sense, and cyber security. Practised as active decisions scored by meaning — so students know the specific step they missed before an emergency strikes.
            </p>
            <div className="mt-4 pt-3 border-t border-line/60 flex items-center gap-1.5 text-xs text-muted font-medium">
              Coaches: <span className="font-bold text-ink">Ember, Signal, Pulse, Basil, Civic, Cipher</span>
            </div>
          </div>

          {/* PLANET */}
          <div className="card p-6 border-line hover:border-ok/40 transition flex flex-col relative overflow-hidden">
            <div className="absolute top-3 right-3 text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-ok/15 text-ok border border-ok/30">FLAGSHIP MISSION</div>
            <div className="w-12 h-12 rounded-2xl bg-ok/15 flex items-center justify-center text-2xl mb-4">🌿</div>
            <div className="text-xs font-extrabold uppercase tracking-wider text-ok">Pillar 2 · Sustainability</div>
            <h3 className="text-xl font-bold mt-1 text-ink">PLANET: Daily climate habit</h3>
            <p className="text-muted text-sm mt-2 leading-relaxed flex-1">
              Everyday sustainability made personal. Terra brings relatable situations on waste segregation, energy, and water, plus <b>live morning alerts tailored to today's real weather & air quality (AQI) in your city</b>.
            </p>
            <div className="mt-4 pt-3 border-t border-line/60 flex items-center gap-1.5 text-xs text-muted font-medium">
              Flagship Coach: <span className="font-bold text-ink">Terra (Environmental AI)</span>
            </div>
          </div>

          {/* FUTURE */}
          <div className="card p-6 border-line hover:border-cyan-400/40 transition flex flex-col">
            <div className="w-12 h-12 rounded-2xl bg-cyan-400/15 flex items-center justify-center text-2xl mb-4">🧭</div>
            <div className="text-xs font-extrabold uppercase tracking-wider text-cyan-400">Pillar 3 · Classes 9 to 12</div>
            <h3 className="text-xl font-bold mt-1 text-ink">FUTURE: Career discovery</h3>
            <p className="text-muted text-sm mt-2 leading-relaxed flex-1">
              Over 90% of students make Class 10 and 12 stream decisions without career guidance. Compass introduces real-world streams — tech, climate, design, and vocational careers — through situations, without rigid prescriptions.
            </p>
            <div className="mt-4 pt-3 border-t border-line/60 flex items-center gap-1.5 text-xs text-muted font-medium">
              Career Coach: <span className="font-bold text-ink">Compass (Pathfinder AI)</span>
            </div>
          </div>
        </div>
      </section>

      {/* Discovery Layer: Learning Flips Direction */}
      <section className="max-w-6xl mx-auto px-5 md:px-8 py-8">
        <div className="card p-8 md:p-10 border-line bg-gradient-to-br from-surface to-surface2 relative overflow-hidden">
          <div className="max-w-3xl">
            <span className="text-xs font-extrabold tracking-widest uppercase text-brand-violet">The Discovery Layer</span>
            <h2 className="text-3xl md:text-4xl font-bold mt-2">What if students don’t know <span className="grad-text">what to ask?</span></h2>
            <p className="text-muted mt-3 text-[15.5px] leading-relaxed">
              Traditional AI chatbots and search engines only work when a learner already knows what to search for. A child will never ask <i>"how to handle an oil fire"</i> until the oil is already burning. <b>wotnow brings the right questions to them:</b>
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-6 mt-8">
            <div className="rounded-2xl border border-line bg-surface/80 p-5">
              <div className="text-xs font-bold text-faint uppercase tracking-wider">Traditional AI & Search</div>
              <div className="text-base font-bold text-ink mt-1">Prompt-Dependent (Reactive)</div>
              <p className="text-muted text-sm mt-2 leading-relaxed">
                The learner must initiate. If they don’t know an issue exists, they never ask. Tips are read passively once and quickly forgotten without real-life practice.
              </p>
            </div>

            <div className="rounded-2xl border border-brand-violet/40 bg-brand-violet/5 p-5 relative">
              <div className="text-xs font-bold text-brand-violet uppercase tracking-wider">wotnow AI Agent Network</div>
              <div className="text-base font-bold text-ink mt-1">Scenario-First (Proactive)</div>
              <p className="text-muted text-sm mt-2 leading-relaxed">
                Specialized AI agents proactively bring real situations to their daily feed. Students respond in their own words, and Gemini scores their reasoning against verified safety fact cards.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* how */}
      <section id="how" className="max-w-6xl mx-auto px-5 md:px-8 py-14">
        <h2 className="text-3xl md:text-4xl font-bold text-center">Scroll less. <span className="grad-text">Know more.</span></h2>
        <div className="grid md:grid-cols-3 gap-4 mt-10">
          {[
            { mood: 'look' as const, t: '1 · An expert posts', d: 'AI experts post real situations every day, matched to your class, city and even today’s weather.' },
            { mood: 'think' as const, t: '2 · You respond', d: 'Type what you’d do in your own words, vote in polls, bust myths or spot scams.' },
            { mood: 'happy' as const, t: '3 · You get better', d: 'Instant, kind feedback against verified safety facts, plus XP, streaks and badges.' },
          ].map(s => (
            <div key={s.t} className="card p-6 text-center flex flex-col items-center">
              <Mascot mood={s.mood} size={84} /><h3 className="text-xl font-bold mt-3">{s.t}</h3><p className="text-muted mt-2 text-[15px]">{s.d}</p>
            </div>
          ))}
        </div>
      </section>

      {/* experts */}
      <section id="experts" className="max-w-6xl mx-auto px-5 md:px-8 py-10">
        <h2 className="text-3xl md:text-4xl font-bold text-center">Meet the experts</h2>
        <p className="text-muted text-center mt-2">Eight AI coaches covering what school doesn’t teach.</p>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mt-8">
          {AGENTS.map(a => (
            <div key={a.id} className="card p-4 flex items-center gap-3 hover:-translate-y-0.5 transition">
              <AgentAvatar agent={a} size={48} /><div><div className="font-bold">{a.name}</div><div className="text-sm text-muted">{a.domainLabel}</div></div>
            </div>
          ))}
        </div>
      </section>

      {/* parents */}
      <section id="parents" className="max-w-6xl mx-auto px-5 md:px-8 py-14">
        <div className="card p-6 md:p-10 grad-soft grid md:grid-cols-[1fr_1.1fr] gap-8 items-center">
          <div>
            <h2 className="text-3xl md:text-4xl font-bold">The social app parents <span className="grad-text">actually recommend</span>.</h2>
            <p className="text-muted mt-3 text-[15px]">Parents create the account. Kids get a nickname and a fun avatar, never their real name or photo.</p>
            <button className="btn-grad mt-6 !px-6 !py-3" onClick={primary.go}>{signedIn ? 'Open my family' : 'Sign in or sign up'}</button>
            {!signedIn && cfg.allowDemo && <button className="btn-ghost mt-6 ml-2 !px-5 !py-3" onClick={() => demo('parent')}>See parent view</button>}
          </div>
          <div className="grid sm:grid-cols-2 gap-3">
            {[['🙅', 'No user posts', 'Only verified AI experts post. No influencers, no ads.'], ['🔒', 'No DMs or strangers', 'Kids can’t message each other. Ever.'],
              ['🧹', 'AI-moderated answers', 'Every reply is checked before anyone sees it.'], ['⏱️', 'Time limits', 'Daily limit and quiet hours you control.'],
              ['📊', 'Weekly report', 'Skills learned and what to talk about at dinner.'], ['🎯', 'Age-matched', 'Separate content for Classes 3–5, 6–8 and 9–12.']].map(([e, t, d]) => (
              <div key={t} className="rounded-2xl bg-surface border border-line p-4"><div className="text-2xl">{e}</div><div className="font-bold mt-1">{t}</div><div className="text-sm text-muted">{d}</div></div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="max-w-6xl mx-auto px-5 md:px-8 py-10 flex flex-wrap items-center justify-between gap-4 text-sm text-muted border-t border-line">
        <div className="flex items-center gap-3">
          <Logo className="h-8" />
          <div>
            <div className="font-bold text-ink text-[13px]">wotnow · Know what now. Before you need to ask.</div>
            <div className="text-[11.5px] text-muted">AI Agent Social Learning Network for India’s 24+ Crore Students</div>
          </div>
        </div>
        <div className="text-right text-xs text-faint">
          <div>Built for Google AI Builder Cup 2026 · Sustainability & Social Impact</div>
          <div>In an emergency, call <b>112</b></div>
        </div>
      </footer>
    </div>
  )
}
