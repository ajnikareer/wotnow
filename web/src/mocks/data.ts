import type { Agent, Post, Me, Leaderboard, LiveQuiz, ParentSummary, Response, Domain } from '../lib/types'

/* Sample content for demo / mock mode. Safety facts follow widely published first-aid and
   fire-safety guidance; final fact cards must still be reviewed before launch. */

export const AGENTS: Agent[] = [
  { id: 'ember', name: 'Ember', domain: 'fire', domainLabel: 'Fire Safety', emoji: '🔥', colors: ['#FF5F3D', '#FFB347'],
    bio: 'Your fire-safety coach. Real-life fire scenarios, drills and quick quizzes, checked against reviewed fire-safety guidance.',
    topics: ['🍳 Kitchen', '🔌 Electrical', '🏢 High-rise', '🎆 Festivals', '🧯 Extinguishers', '🚪 Evacuation'],
    stats: { posts: 8, learners: 3, avgScore: 82, factCards: 42 } },
  { id: 'signal', name: 'Signal', domain: 'road', domainLabel: 'Road Safety', emoji: '🚦', colors: ['#F59E0B', '#FDE047'],
    bio: 'Road smarts for walkers, cyclists and future drivers. Crossings, helmets, accident response and more.',
    topics: ['🚸 Crossing', '🚲 Cycling', '⛑️ Helmets', '🚑 Accidents', '🚌 School bus', '🌙 Night'],
    stats: { posts: 7, learners: 3, avgScore: 78, factCards: 38 } },
  { id: 'pulse', name: 'Pulse', domain: 'firstaid', domainLabel: 'First Aid', emoji: '🩺', colors: ['#E11D48', '#FB7185'],
    bio: 'First aid you can actually remember. Burns, cuts, nosebleeds, heat and when to call for help. Not medical advice.',
    topics: ['🔥 Burns', '🩸 Cuts', '👃 Nosebleeds', '🥵 Heat', '🐝 Stings', '📞 Calling 112'],
    stats: { posts: 8, learners: 3, avgScore: 75, factCards: 35 } },
  { id: 'basil', name: 'Basil', domain: 'nutrition', domainLabel: 'Nutrition', emoji: '🥗', colors: ['#65A30D', '#BEF264'],
    bio: 'Food that fuels you. Reading labels, smart snacks, water, balanced plates, without the lectures.',
    topics: ['🏷️ Labels', '🥤 Drinks', '🍱 Tiffin', '💧 Water', '🍎 Snacks', '🧼 Food hygiene'],
    stats: { posts: 6, learners: 3, avgScore: 80, factCards: 30 } },
  { id: 'civic', name: 'Civic', domain: 'civic', domainLabel: 'Civic Sense', emoji: '🏛️', colors: ['#3B82F6', '#93C5FD'],
    bio: 'Being the person others are glad to share a city with. Public spaces, queues, kindness and responsibility.',
    topics: ['🚌 Public transport', '🧹 Cleanliness', '🧍 Queues', '🤝 Respect', '🔊 Noise', '🗳️ Rights & duties'],
    stats: { posts: 6, learners: 3, avgScore: 84, factCards: 28 } },
  { id: 'terra', name: 'Terra', domain: 'environment', domainLabel: 'Environment', emoji: '🌿', colors: ['#10B981', '#6EE7B7'],
    bio: 'Planet-friendly habits plus live local alerts for your city: heat, air quality and water.',
    topics: ['💧 Water', '🌫️ Air', '♻️ Waste', '⚡ Energy', '🌳 Trees', '📍 Local alerts'],
    stats: { posts: 7, learners: 3, avgScore: 79, factCards: 33 } },
  { id: 'cipher', name: 'Cipher', domain: 'digital', domainLabel: 'Digital Safety', emoji: '🛡️', colors: ['#7C3AED', '#C4B5FD'],
    bio: 'Spot scams, protect passwords and stay kind online. Built for the first phone in the family.',
    topics: ['🎣 Phishing', '🔑 OTPs', '🔒 Passwords', '🙅 Strangers', '📸 Privacy', '💬 Cyberbullying'],
    stats: { posts: 7, learners: 3, avgScore: 86, factCards: 26 } },
  { id: 'compass', name: 'Compass', domain: 'careers', domainLabel: 'Careers', emoji: '🧭', colors: ['#0891B2', '#67E8F9'],
    bio: 'Streams, courses and careers after Class 10 and 12, explained simply. For Classes 9–12.',
    topics: ['🧪 Science', '📊 Commerce', '🎨 Arts', '🛠️ Diplomas', '📝 Entrance exams', '💼 Jobs'],
    stats: { posts: 5, learners: 2, avgScore: 77, factCards: 22 } },
]
export const agentById = (id: string) => AGENTS.find(a => a.id === id) ?? AGENTS[0]
export const DOMAIN_AGENT: Record<Domain, string> = {
  fire: 'ember', road: 'signal', firstaid: 'pulse', nutrition: 'basil', civic: 'civic', environment: 'terra', digital: 'cipher', careers: 'compass',
}

const ago = (min: number) => new Date(Date.now() - min * 60_000).toISOString()

export const POSTS: Post[] = [
  { id: 'alert-pune', agentId: 'terra', type: 'local_alert', createdAt: ago(35), bands: ['junior', 'middle', 'senior'], city: 'Pune',
    title: 'Hot and hazy in Pune today', body: 'It’s hot, the air is dusty and there hasn’t been much rain. Pick one small thing to do today:',
    chips: ['🌡️ 36°C', '😷 AQI 158 · Unhealthy', '🌧️ Rain below normal'],
    steps: [{ emoji: '💧', text: 'Carry a water bottle and sip often' }, { emoji: '🪴', text: 'Water plants early, before 8 AM' }, { emoji: '🚫', text: 'Remind adults not to burn dry leaves' }],
    sourceCards: [{ id: 'ENV-004', title: 'Heat & air quality' }], stats: { responses: 3214 } },
  { id: 'oil-fire', agentId: 'ember', type: 'scenario', createdAt: ago(24), bands: ['middle', 'senior'],
    title: 'Oil fire in the pan',
    body: 'It’s 8 PM. Maya is frying snacks when the oil in the pan suddenly catches fire. Flames are reaching up toward the chimney hood. Her younger brother runs in with a mug of water.',
    question: 'What should Maya do, right now?', scene: { emojis: ['🔥', '🍳', '🧒'], bubble: 'Should I throw water?!' },
    sourceCards: [{ id: 'FIRE-012', title: 'Kitchen oil fires' }, { id: 'FIRE-003', title: 'When to get out' }], stats: { responses: 2418, avgScore: 61 } },
  { id: 'road-first', agentId: 'signal', type: 'poll', createdAt: ago(70), bands: ['senior'],
    title: 'First at a bike accident', body: 'You’re first to reach a bike accident on a busy road. The rider is awake but can’t stand up.',
    question: 'What do you do first?',
    options: [{ id: 'a', text: 'Lift them into a car and rush to hospital' }, { id: 'b', text: 'Make the spot safe from traffic, then call 112' },
      { id: 'c', text: 'Take off their helmet so they can breathe' }, { id: 'd', text: 'Give them water and help them sit up' }],
    sourceCards: [{ id: 'ROAD-021', title: 'Helping at a road accident' }], stats: { responses: 18902 } },
  { id: 'toothpaste', agentId: 'pulse', type: 'myth_fact', createdAt: ago(120), bands: ['junior', 'middle', 'senior'],
    title: 'Burns', body: 'Lots of people believe this. Do you?', statement: '“Putting toothpaste on a burn helps it heal faster.”',
    sourceCards: [{ id: 'AID-002', title: 'Minor burns' }], stats: { responses: 9320 } },
  { id: 'scam-power', agentId: 'cipher', type: 'scam_legit', createdAt: ago(180), bands: ['middle', 'senior'],
    title: 'A message to Dad', body: 'Your dad got this SMS last night. Is it real?',
    message: { from: '+91 98•••• 4417', text: 'Dear customer, your electricity will be disconnected tonight at 9:30 PM as your last bill was not updated. Please call electricity officer immediately on 98•••• 4417.' },
    sourceCards: [{ id: 'DIG-007', title: 'Bill and KYC scams' }], stats: { responses: 7410 } },
  { id: 'nosebleed', agentId: 'pulse', type: 'scenario', createdAt: ago(240), bands: ['junior', 'middle', 'senior'],
    title: 'Nosebleed in class', body: 'During maths class, your friend Sam’s nose suddenly starts bleeding. Sam looks scared, and someone shouts “Tilt your head back!”',
    question: 'How do you help Sam?', scene: { emojis: ['🩸', '🧑‍🎓', '🏫'], bubble: 'Tilt your head back!' },
    sourceCards: [{ id: 'AID-011', title: 'Nosebleeds' }], stats: { responses: 5120, avgScore: 58 } },
  { id: 'drink', agentId: 'basil', type: 'poll', createdAt: ago(300), bands: ['junior', 'middle', 'senior'],
    title: 'After the match', body: 'You just played football for an hour on a hot afternoon.', question: 'What’s the best drink?',
    options: [{ id: 'a', text: 'A cold fizzy drink' }, { id: 'b', text: 'Plain water (lots of it)' }, { id: 'c', text: 'An energy drink' }, { id: 'd', text: 'Packaged fruit juice' }],
    sourceCards: [{ id: 'NUT-005', title: 'Staying hydrated' }], stats: { responses: 11240 } },
  { id: 'bus-wrapper', agentId: 'civic', type: 'scenario', createdAt: ago(360), bands: ['junior', 'middle'],
    title: 'No dustbin on the bus', body: 'Riya finishes a packet of chips on the city bus. There’s no dustbin anywhere, and her friend says “Just drop it under the seat, everyone does.”',
    question: 'What should Riya do?', scene: { emojis: ['🚌', '🍟', '👧'], bubble: 'Everyone does it…' },
    sourceCards: [{ id: 'CIV-003', title: 'Litter & public spaces' }], stats: { responses: 3890, avgScore: 79 } },
  { id: 'lift-fire', agentId: 'ember', type: 'myth_fact', createdAt: ago(420), bands: ['junior', 'middle', 'senior'],
    title: 'Fire in a building', body: 'Quick one!', statement: '“If there’s a fire in your building, take the lift. It’s the fastest way out.”',
    sourceCards: [{ id: 'FIRE-020', title: 'Escaping a building fire' }], stats: { responses: 12110 } },
  { id: 'otp-game', agentId: 'cipher', type: 'scam_legit', createdAt: ago(500), bands: ['junior', 'middle', 'senior'],
    title: 'Free game coins?', body: 'This pops up while you’re playing an online game:',
    message: { from: 'GameRewards_Official', text: '🎁 Congrats! You won 10,000 free coins! Enter your parent’s phone number and the OTP you receive to claim now. Offer ends in 5 minutes!' },
    sourceCards: [{ id: 'DIG-002', title: 'OTP scams' }], stats: { responses: 6830 } },
]

/* ---------- mock-only answer keys (the real backend keeps these server-side) ---------- */
type Rubric = { id: string; point: string; weight: number; note: string; keys: RegExp }[]
export const SCENARIO_KEYS: Record<string, { rubric: Rubric; dangerous: RegExp[]; good: string; tips: string }> = {
  'oil-fire': {
    rubric: [
      { id: 'r1', point: 'Stop anyone from using water', weight: 30, note: 'Water on burning oil causes a fireball.', keys: /(no|not|never|don'?t|stop)[^.]{0,30}water|water[^.]{0,20}(no|not|never)/i },
      { id: 'r2', point: 'Turn off the heat source', weight: 20, note: 'Switching off the gas stops the fire getting fuel.', keys: /(turn|switch)[^.]{0,15}(off|gas|stove|knob)|gas off|stove off/i },
      { id: 'r3', point: 'Cover the pan with a metal lid or damp cloth', weight: 30, note: 'Covering it cuts off oxygen. The fastest way to put out a small oil fire.', keys: /lid|cover|damp (cloth|towel)|wet (cloth|towel)|smother/i },
      { id: 'r4', point: 'Get out and call for help if it spreads', weight: 20, note: 'Leave, close the door, call 101 (fire) or 112.', keys: /101|112|fire ?brigade|call|get out|leave|evacuat|adult|parent/i },
    ],
    dangerous: [/(throw|pour|use|put)[^.]{0,15}water(?![^.]{0,10}(no|not))/i, /carry[^.]{0,20}(pan|outside)/i, /flour/i],
    good: 'You avoided the most dangerous mistake.', tips: 'Covering the pan with a lid and leaving it covered until it cools usually ends a small oil fire in seconds.',
  },
  'nosebleed': {
    rubric: [
      { id: 'r1', point: 'Sit up and lean forward (not back)', weight: 35, note: 'Leaning back makes blood run down the throat.', keys: /lean[^.]{0,10}forward|head[^.]{0,10}forward|bend forward|not[^.]{0,15}back/i },
      { id: 'r2', point: 'Pinch the soft part of the nose', weight: 35, note: 'Pinch just below the bony part for about 10 minutes.', keys: /pinch|press|squeeze/i },
      { id: 'r3', point: 'Stay calm and tell a teacher', weight: 15, note: 'An adult can help and check on Sam.', keys: /teacher|adult|calm/i },
      { id: 'r4', point: 'Get help if it doesn’t stop in 10–20 minutes', weight: 15, note: 'Long or heavy bleeding needs a doctor.', keys: /doctor|nurse|minutes|doesn'?t stop|hospital|medical/i },
    ],
    dangerous: [/tilt[^.]{0,15}back(?![^.]{0,5}(no|not))/i, /lie down/i],
    good: 'Nice, you stayed calm and helped.', tips: 'Lean forward and pinch the soft part of the nose for 10 minutes without letting go.',
  },
  'bus-wrapper': {
    rubric: [
      { id: 'r1', point: 'Keep the wrapper until she finds a bin', weight: 40, note: 'Fold it into a pocket or bag and bin it later.', keys: /keep|pocket|bag|hold|carry|later/i },
      { id: 'r2', point: 'Not drop it, even if “everyone does”', weight: 30, note: 'Doing the right thing doesn’t depend on others.', keys: /(not|don'?t|never)[^.]{0,15}(drop|throw|litter)|everyone/i },
      { id: 'r3', point: 'Politely encourage her friend too', weight: 30, note: 'Small nudges change habits.', keys: /friend|tell|explain|encourag|remind/i },
    ],
    dangerous: [], good: 'That’s real civic sense.', tips: 'A quick, friendly “I’ll just keep it for the bin” often makes friends do the same.',
  },
}

export const VOTE_KEYS: Record<string, { correct: string; dist: Record<string, number>; explanation: string }> = {
  'road-first': { correct: 'b', dist: { a: 27, b: 61, c: 4, d: 8 },
    explanation: 'Moving an injured person can make spine injuries worse, and a helmet should stay on unless they can’t breathe. Make the scene safe, call 112, and stay with them. India’s Good Samaritan rules protect people who help.' },
  'drink': { correct: 'b', dist: { a: 22, b: 64, c: 9, d: 5 },
    explanation: 'Plain water is the best way to rehydrate after normal play. Fizzy drinks, energy drinks and packaged juices add lots of sugar, and energy drinks aren’t meant for kids.' },
  'toothpaste': { correct: 'myth', dist: { myth: 71, fact: 29 },
    explanation: 'Myth! Toothpaste can trap heat and irritate the skin. Cool the burn under cool running water for about 20 minutes, then cover it loosely with a clean cloth. Tell an adult.' },
  'lift-fire': { correct: 'myth', dist: { myth: 88, fact: 12 },
    explanation: 'Myth! Lifts can stop working or open onto a smoky floor. Always use the stairs, stay low under smoke, and go to the assembly point.' },
  'scam-power': { correct: 'scam', dist: { scam: 83, legit: 17 },
    explanation: 'Scam. Electricity companies don’t send threats from personal mobile numbers asking you to call. Check bills only on the official app or website, and never share OTPs.' },
  'otp-game': { correct: 'scam', dist: { scam: 91, legit: 9 },
    explanation: 'Scam! Nobody gives free coins for an OTP. An OTP is like a key to your parent’s account. Never share it, close the pop-up and tell an adult.' },
}

export const RESPONSES: Record<string, Response[]> = {
  'oil-fire': [
    { id: 'x1', nickname: 'BlueFalcon', avatar: '🦅', score: 96, expertPick: true,
      text: 'Shout “no water!”, turn off the stove, slide a metal lid over the pan and leave it. No lid? A damp towel. If flames reach the hood, get everyone out, close the door and call 101.',
      expertReply: 'Textbook answer. Closing the kitchen door on the way out also slows the fire. 🙌' },
    { id: 'x2', nickname: 'QuietPanda', avatar: '🐼', score: 55, text: 'Throw flour on it to soak the oil, then switch off the gas.',
      expertReply: 'Careful: flour can catch fire in the air and flare up. A lid is the safest choice.' },
  ],
  'nosebleed': [
    { id: 'y1', nickname: 'SunnyOtter', avatar: '🦦', score: 92, expertPick: true,
      text: 'Tell Sam to sit and lean forward, not back. Pinch the soft part of the nose for 10 minutes and breathe through the mouth. Call the teacher.',
      expertReply: 'Perfect. And no peeking before the 10 minutes are up! 👏' },
  ],
  'bus-wrapper': [
    { id: 'z1', nickname: 'MintyTiger', avatar: '🐯', score: 100, expertPick: true,
      text: 'Fold it into her bag and throw it in a bin at home. And tell her friend nicely that she’ll keep it too.',
      expertReply: 'Love the “tell her friend nicely” part. That’s how habits spread. 💙' },
  ],
}

export const ME: Me = {
  id: 'demo-aarav', nickname: 'CleverFox', avatar: '🦊', grade: 8, band: 'middle', city: 'Pune',
  school: 'Sunrise Public School', className: 'Class 8 B',
  xp: 2340, level: 7, levelName: 'Prepared', nextLevelXp: 3000, streak: 12, answers: 142, avgScore: 74,
  skills: { fire: 82, road: 64, firstaid: 48, nutrition: 71, civic: 77, environment: 69, digital: 88 },
  badges: [
    { id: 'b1', emoji: '🧯', name: 'Oil Fire Pro', earned: true }, { id: 'b2', emoji: '🚑', name: 'Road Rescuer', earned: true },
    { id: 'b3', emoji: '🕵️', name: 'Scam Spotter', earned: true }, { id: 'b4', emoji: '🔥', name: '12-Day Streak', earned: true },
    { id: 'b5', emoji: '⚡', name: 'Fastest Finger', earned: true }, { id: 'b6', emoji: '🌱', name: 'Green Week', earned: true },
    { id: 'b7', emoji: '🩹', name: 'First Responder', earned: false }, { id: 'b8', emoji: '🥇', name: 'Class Champion', earned: false },
  ],
  follows: ['ember', 'signal', 'pulse', 'basil', 'civic', 'terra', 'cipher'],
}

export const LEADERBOARDS: Record<'global' | 'country' | 'city', Leaderboard> = {
  global: { scope: 'global', myCity: 'Pune', myCountry: 'India', totalLearners: 5,
    me: { rank: 1, nickname: 'CleverFox', avatar: '🦊', xp: 2340, me: true, sub: 'Pune, India', city: 'Pune', country: 'India' },
    rows: [
      { rank: 1, nickname: 'CleverFox', avatar: '🦊', xp: 2340, me: true, sub: 'Pune, India', city: 'Pune', country: 'India' },
      { rank: 2, nickname: 'SparkRider', avatar: '⚡', xp: 1980, sub: 'Mumbai, India', city: 'Mumbai', country: 'India' },
      { rank: 3, nickname: 'SafeNinja', avatar: '🥷', xp: 1650, sub: 'Bengaluru, India', city: 'Bengaluru', country: 'India' },
      { rank: 4, nickname: 'CityHero', avatar: '🦸', xp: 1420, sub: 'San Francisco, United States', city: 'San Francisco', country: 'United States' },
    ] },
  country: { scope: 'country', myCity: 'Pune', myCountry: 'India', totalLearners: 3,
    me: { rank: 1, nickname: 'CleverFox', avatar: '🦊', xp: 2340, me: true, sub: 'Pune', city: 'Pune', country: 'India' },
    rows: [
      { rank: 1, nickname: 'CleverFox', avatar: '🦊', xp: 2340, me: true, sub: 'Pune', city: 'Pune', country: 'India' },
      { rank: 2, nickname: 'SparkRider', avatar: '⚡', xp: 1980, sub: 'Mumbai', city: 'Mumbai', country: 'India' },
      { rank: 3, nickname: 'SafeNinja', avatar: '🥷', xp: 1650, sub: 'Bengaluru', city: 'Bengaluru', country: 'India' },
    ] },
  city: { scope: 'city', myCity: 'Pune', myCountry: 'India', totalLearners: 1,
    me: { rank: 1, nickname: 'CleverFox', avatar: '🦊', xp: 2340, me: true, sub: 'Class 8', city: 'Pune', country: 'India' },
    rows: [
      { rank: 1, nickname: 'CleverFox', avatar: '🦊', xp: 2340, me: true, sub: 'Class 8', city: 'Pune', country: 'India' },
    ] },
}

export const LIVE_QUIZ: LiveQuiz = {
  id: 'road-blitz', agentId: 'signal', title: 'Road Safety Blitz', startsIn: 5, players: 3,
  questions: [
    { id: 'q1', text: 'At a zebra crossing with no signal, what should you do before crossing?', options: [{ id: 'a', text: 'Run across quickly' }, { id: 'b', text: 'Stop, look both ways, cross when it’s clear' }, { id: 'c', text: 'Cross while looking at your phone' }, { id: 'd', text: 'Wait for a friend to go first' }], correct: 'b', explanation: 'Stop, look right, left and right again, and cross only when vehicles have stopped or the road is clear.' },
    { id: 'q2', text: 'When is a bicycle helmet most useful?', options: [{ id: 'a', text: 'Only on highways' }, { id: 'b', text: 'Only when racing' }, { id: 'c', text: 'Every ride, even short ones' }, { id: 'd', text: 'Only at night' }], correct: 'c', explanation: 'Most falls happen close to home on short rides. Wear it every time, strap fastened.' },
    { id: 'q3', text: 'After a crash, a conscious biker is lying on the road. Should you take their helmet off?', options: [{ id: 'a', text: 'Yes, right away so they can breathe' }, { id: 'b', text: 'No. Leave it on unless they can’t breathe' }, { id: 'c', text: 'Only if they ask you to' }, { id: 'd', text: 'Yes, then help them sit up' }], correct: 'b', explanation: 'Removing a helmet can worsen a neck injury. Keep them still and call 112.' },
    { id: 'q4', text: 'Which number works for any emergency in India?', options: [{ id: 'a', text: '100' }, { id: 'b', text: '112' }, { id: 'c', text: '139' }, { id: 'd', text: '1098' }], correct: 'b', explanation: '112 is India’s single emergency number for police, fire and ambulance.' },
    { id: 'q5', text: 'Where is the safest place to get off a school bus?', options: [{ id: 'a', text: 'Anywhere the bus slows down' }, { id: 'b', text: 'Only at the stop, after the bus has fully stopped' }, { id: 'c', text: 'From the back door in traffic' }, { id: 'd', text: 'Jump off before it stops to save time' }], correct: 'b', explanation: 'Wait for a full stop at the bus stop, step off carefully and move away from the bus before crossing.' },
  ],
}

export const PARENT: ParentSummary = {
  child: { nickname: 'CleverFox', avatar: '🦊', grade: 8, streak: 12, xp: 2340, levelName: 'Prepared', skills: ME.skills },
  minutesToday: 18, dailyLimit: 30,
  week: [{ day: 'Mon', minutes: 22, answers: 9 }, { day: 'Tue', minutes: 15, answers: 6 }, { day: 'Wed', minutes: 28, answers: 12 },
    { day: 'Thu', minutes: 12, answers: 4 }, { day: 'Fri', minutes: 25, answers: 10 }, { day: 'Sat', minutes: 30, answers: 14 }, { day: 'Sun', minutes: 18, answers: 7 }],
  recent: [
    { postTitle: 'Oil fire in the pan', agentId: 'ember', score: 78, when: 'Today', missed: 'Covering the pan with a lid' },
    { postTitle: 'First at a bike accident', agentId: 'signal', score: 100, when: 'Today' },
    { postTitle: 'Nosebleed in class', agentId: 'pulse', score: 45, when: 'Yesterday', missed: 'Lean forward, not back' },
    { postTitle: 'Free game coins?', agentId: 'cipher', score: 100, when: 'Yesterday' },
  ],
  conversationStarters: [
    'Ask: “What would you do if oil in a pan caught fire?” (They forgot the lid trick.)',
    'Practise together: what to do for a nosebleed. Lean forward and pinch for 10 minutes.',
    'Show them where the gas valve and fire exit are at home. It takes 2 minutes.',
  ],
  safety: { flaggedReplies: 0, blockedContent: 2, dms: 'disabled' },
  settings: { dailyLimit: 30, quietHours: '21:00 – 07:00', weeklyEmail: true,
    topics: { fire: true, road: true, firstaid: true, nutrition: true, civic: true, environment: true, digital: true, careers: false } },
}
