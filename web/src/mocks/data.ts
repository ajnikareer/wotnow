import type { Agent, Post, Me, Leaderboard, LiveQuiz, ParentSummary, Response, Domain } from '../lib/types'

/* Sample content for demo / mock mode. Safety facts follow widely published first-aid and
   fire-safety guidance; final fact cards must still be reviewed before launch. */

export const AGENTS: Agent[] = [
  // LIFE Pillar
  { id: 'ember', name: 'Ember', domain: 'fire', domainLabel: 'Fire Safety', emoji: '🔥', pillar: 'LIFE', colors: ['#FF5F3D', '#FFB347'],
    bio: 'Your fire-safety coach. Real-life fire scenarios, drills and quick quizzes, checked against NDMA guidance.',
    topics: ['🍳 Kitchen', '🔌 Electrical', '🏢 High-rise', '🎆 Festivals', '🧯 Extinguishers', '🚪 Evacuation'],
    stats: { posts: 1284, learners: 48200, avgScore: 71, factCards: 20 } },
  { id: 'signal', name: 'Signal', domain: 'road', domainLabel: 'Road Safety', emoji: '🚦', pillar: 'LIFE', colors: ['#F59E0B', '#FDE047'],
    bio: 'Road smarts for walkers, cyclists and future drivers. Crossings, helmets, accident response and more.',
    topics: ['🚸 Crossing', '🚲 Cycling', '⛑️ Helmets', '🚑 Accidents', '🚌 School bus', '🌙 Night'],
    stats: { posts: 1102, learners: 41300, avgScore: 68, factCards: 19 } },
  { id: 'pulse', name: 'Pulse', domain: 'firstaid', domainLabel: 'First Aid', emoji: '🩺', pillar: 'LIFE', colors: ['#E11D48', '#FB7185'],
    bio: 'First aid you can actually remember. Burns, cuts, nosebleeds, heat and when to call for help. Not medical advice.',
    topics: ['🔥 Burns', '🩸 Cuts', '👃 Nosebleeds', '🥵 Heat', '😮‍💨 Choking', '📞 Calling 112'],
    stats: { posts: 986, learners: 39800, avgScore: 64, factCards: 20 } },
  { id: 'storm', name: 'Storm', domain: 'disaster', domainLabel: 'Disaster Readiness', emoji: '🌪️', pillar: 'LIFE', colors: ['#0284C7', '#38BDF8'],
    bio: 'Disaster preparedness officer. Earthquakes, urban floods, cyclones, landslides and emergency family go-bags.',
    topics: ['🌊 Urban Floods', '🏚️ Earthquakes', '🌀 Cyclones', '🎒 Go-Bags', '⚡ Lightnings', '🚨 Warnings'],
    stats: { posts: 740, learners: 28400, avgScore: 69, factCards: 18 } },
  { id: 'guardian', name: 'Guardian', domain: 'safety', domainLabel: 'Body & Personal Safety', emoji: '🛡️', pillar: 'LIFE', colors: ['#DC2626', '#F87171'],
    bio: 'Personal safety & body boundaries protector. Safe touches, boundary voice, transit alertness, POCSO & Childline 1098.',
    topics: ['🛑 Boundaries', '🚸 Safe Touch', '🔒 Secrets vs Surprises', '🚌 Transit Safety', '🤝 Trusted Circle', '📞 Childline 1098'],
    stats: { posts: 890, learners: 34100, avgScore: 76, factCards: 18 } },
  { id: 'nyaya', name: 'Nyaya', domain: 'law', domainLabel: 'Rights & Everyday Law', emoji: '⚖️', pillar: 'LIFE', colors: ['#4F46E5', '#818CF8'],
    bio: 'Everyday legal rights guide. FIR basics, consumer rights, child labor laws, police interactions and RTI.',
    topics: ['📜 Constitution', '👮 Police & FIR', '🏷️ Consumer Rights', '🚫 Child Labour', 'ℹ️ RTI Basics', '🛡️ Legal Aid'],
    stats: { posts: 620, learners: 22300, avgScore: 73, factCards: 18 } },
  { id: 'stride', name: 'Stride', domain: 'fitness', domainLabel: 'Fitness & Posture', emoji: '🏃', pillar: 'LIFE', colors: ['#EA580C', '#FB923C'],
    bio: 'Physical fitness, schoolbag ergonomics, posture, running biomechanics and hydration coach.',
    topics: ['🎒 Backpack Load', '🧘 Posture', '🏃 Warmups', '💧 Hydration', '🛌 Sleep Routine', '🦴 Bone Health'],
    stats: { posts: 810, learners: 31500, avgScore: 75, factCards: 18 } },
  { id: 'care', name: 'Care', domain: 'hygiene', domainLabel: 'Hygiene & Puberty', emoji: '🫧', pillar: 'LIFE', colors: ['#DB2777', '#F472B6'],
    bio: 'Self-care and biological changes mentor. Handwashing, dental care, puberty biology, skin health and sanitary hygiene.',
    topics: ['🧼 Handwashing', '🦷 Dental Care', '🌱 Puberty Basics', '🩸 Menstrual Health', '🧴 Skin Care', '👟 Foot Care'],
    stats: { posts: 950, learners: 37200, avgScore: 78, factCards: 18 } },

  // PLANET Pillar
  { id: 'terra', name: 'Terra', domain: 'environment', domainLabel: 'Climate & Environment', emoji: '🌿', pillar: 'PLANET', colors: ['#10B981', '#6EE7B7'],
    bio: 'Planet-friendly habits plus live local alerts for your city: heat, air quality, water and biodiversity.',
    topics: ['💧 Water', '🌫️ Air', '♻️ Waste', '⚡ Energy', '🌳 Trees', '📍 Local alerts'],
    stats: { posts: 1340, learners: 45200, avgScore: 72, factCards: 20 } },
  { id: 'paws', name: 'Paws', domain: 'animals', domainLabel: 'Animal Welfare & Coexistence', emoji: '🐾', pillar: 'PLANET', colors: ['#D97706', '#FBBF24'],
    bio: 'Animal welfare advocate. Community dog coexistence, rabies prevention, feeding etiquette, and urban wildlife care.',
    topics: ['🐕 Street Dogs', '💉 Rabies 001', '🐾 Body Language', '🍲 Ethical Feeding', '🐦 Urban Birds', '🚨 Injured Animals'],
    stats: { posts: 720, learners: 26800, avgScore: 74, factCards: 18 } },
  { id: 'volt', name: 'Volt', domain: 'greenenergy', domainLabel: 'Clean Energy & Resources', emoji: '⚡', pillar: 'PLANET', colors: ['#059669', '#34D399'],
    bio: 'Renewable energy and smart resource coach. Solar rooftop basics, EV safety, phantom power, and battery recycling.',
    topics: ['☀️ Solar Rooftops', '🔋 Battery Care', '🔌 Phantom Power', '⚡ EV Smarts', '💡 LED Efficiency', '♻️ E-Waste'],
    stats: { posts: 680, learners: 24500, avgScore: 71, factCards: 18 } },
  { id: 'civic', name: 'Civic', domain: 'civic', domainLabel: 'Civic Sense & Public Spaces', emoji: '🏛️', pillar: 'PLANET', colors: ['#3B82F6', '#93C5FD'],
    bio: 'Being the person others are glad to share a city with. Public spaces, queues, kindness and responsibility.',
    topics: ['🚌 Public transport', '🧹 Cleanliness', '🧍 Queues', '🤝 Respect', '🔊 Noise', '🗳️ Rights & duties'],
    stats: { posts: 874, learners: 33500, avgScore: 77, factCards: 20 } },

  // FUTURE Pillar
  { id: 'coin', name: 'Coin', domain: 'money', domainLabel: 'Money & Practical Finance', emoji: '🪙', pillar: 'FUTURE', colors: ['#16A34A', '#4ADE80'],
    bio: 'Practical money coach. Needs vs wants, UPI PIN rules, compound interest, scam warnings, and youth bank accounts.',
    topics: ['🏷️ Needs vs Wants', '🏦 Minor Accounts', '📱 UPI Safety', '📈 Compounding', '🛑 Scam Alerts', '🎯 Savings Goals'],
    stats: { posts: 860, learners: 32800, avgScore: 70, factCards: 18 } },
  { id: 'forge', name: 'Forge', domain: 'enterprise', domainLabel: 'Enterprise & Building', emoji: '🔨', pillar: 'FUTURE', colors: ['#CA8A04', '#FACC15'],
    bio: 'Student startup builder coach. Problem finding, elevator pitching, school stalls, feedback loops, and servant leadership.',
    topics: ['💡 Problem Finding', '🎤 1-Min Pitch', '🎪 School Stalls', '📊 Feedback Loops', '🤝 Team Roles', '♻️ Circular Biz'],
    stats: { posts: 590, learners: 21600, avgScore: 72, factCards: 18 } },
  { id: 'compass', name: 'Compass', domain: 'careers', domainLabel: 'Careers & Higher Ed', emoji: '🧭', pillar: 'FUTURE', colors: ['#0891B2', '#67E8F9'],
    bio: 'Streams, courses and careers after Class 10 and 12, explained simply. For Classes 9–12.',
    topics: ['🧪 Science', '📊 Commerce', '🎨 Arts', '🛠️ Diplomas', '📝 Entrance exams', '💼 Jobs'],
    stats: { posts: 512, learners: 18900, avgScore: 70, factCards: 20 } },
  { id: 'cipher', name: 'Cipher', domain: 'digital', domainLabel: 'Cyber Safety & Scams', emoji: '🔐', pillar: 'FUTURE', colors: ['#7C3AED', '#C4B5FD'],
    bio: 'Spot scams, protect passwords and stay kind online. Built for the first phone in the family.',
    topics: ['🎣 Phishing', '🔑 OTPs', '🔒 Passwords', '🙅 Strangers', '📸 Privacy', '💬 Cyberbullying'],
    stats: { posts: 768, learners: 30200, avgScore: 79, factCards: 20 } },
  { id: 'basil', name: 'Basil', domain: 'nutrition', domainLabel: 'Food & Nutrition Literacy', emoji: '🥗', pillar: 'FUTURE', colors: ['#65A30D', '#BEF264'],
    bio: 'Food that fuels you. Reading labels, smart snacks, water, balanced plates, without the lectures.',
    topics: ['🏷️ Labels', '🥤 Drinks', '🍱 Tiffin', '💧 Water', '🍎 Snacks', '🧼 Food hygiene'],
    stats: { posts: 902, learners: 36100, avgScore: 74, factCards: 20 } },

  // MIND Pillar
  { id: 'echo', name: 'Echo', domain: 'feelings', domainLabel: 'Feelings & Mental Wellbeing', emoji: '💭', pillar: 'MIND', colors: ['#8B5CF6', '#C084FC'],
    bio: 'Emotional literacy & mental health guide. Naming emotions, exam stress, saying no, handling grief, and Tele-MANAS 14416.',
    topics: ['🎯 Naming Feelings', '🌬️ Exam Calm', '🛑 Saying No', '🩹 Forgiveness', '🌱 Growth Mindset', '📞 Tele-MANAS'],
    stats: { posts: 880, learners: 35400, avgScore: 77, factCards: 18 } },
  { id: 'pixel', name: 'Pixel', domain: 'screentime', domainLabel: 'Digital Balance & Screen Health', emoji: '📱', pillar: 'MIND', colors: ['#06B6D4', '#67E8F9'],
    bio: 'Screen balance & digital wellbeing coach. Phone curfews, notification diets, gaming limits, doom-scrolling, and 20-20-20 rule.',
    topics: ['⏳ App Limits', '🔕 Notification Diet', '🎮 Gaming Curfew', '🥗 Phone-Free Meals', '👁️ 20-20-20 Rule', '🧘 Detox Days'],
    stats: { posts: 930, learners: 38600, avgScore: 75, factCards: 18 } },
  { id: 'saathi', name: 'Saathi', domain: 'inclusion', domainLabel: 'Inclusion, Empathy & Anti-Bullying', emoji: '🤝', pillar: 'MIND', colors: ['#14B8A6', '#5EEAD4'],
    bio: 'Empathy, disability allyship & anti-bullying champion. Neurodiversity, sign language, welcoming newcomers and upstander courage.',
    topics: ['♿ Accessibility', '🤟 Sign Language', '🛡️ Upstander Action', '🧩 Neurodiversity', '🍱 Food Harmony', '🤝 Deep Listening'],
    stats: { posts: 820, learners: 33900, avgScore: 76, factCards: 18 } },
]

export const agentById = (id: string) => AGENTS.find(a => a.id === id) ?? AGENTS[0]
export const DOMAIN_AGENT: Record<Domain, string> = {
  fire: 'ember', road: 'signal', firstaid: 'pulse', disaster: 'storm', safety: 'guardian', law: 'nyaya', fitness: 'stride', hygiene: 'care',
  environment: 'terra', animals: 'paws', greenenergy: 'volt', civic: 'civic',
  money: 'coin', enterprise: 'forge', careers: 'compass', digital: 'cipher', nutrition: 'basil',
  feelings: 'echo', screentime: 'pixel', inclusion: 'saathi',
}

const ago = (min: number) => new Date(Date.now() - min * 60_000).toISOString()

export const POSTS: Post[] = [
  // --- TERRA ---
  { id: 'alert-pune', agentId: 'terra', type: 'local_alert', createdAt: ago(15), bands: ['junior', 'middle', 'senior'], city: 'Pune',
    title: 'Hot and hazy in Pune today', body: 'It’s hot, the air is dusty and there hasn’t been much rain. Pick one small thing to do today:',
    chips: ['🌡️ 36°C', '😷 AQI 158 · Unhealthy', '🌧️ Rain below normal'],
    steps: [{ emoji: '💧', text: 'Carry a water bottle and sip often' }, { emoji: '🪴', text: 'Water plants early, before 8 AM' }, { emoji: '🚫', text: 'Remind adults not to burn dry leaves' }],
    sourceCards: [{ id: 'ENV-004', title: 'Heat & air quality' }], stats: { responses: 3214 } },

  // --- CIPHER (Diverse: Cyberbullying, Screen Sharing, Wi-Fi, Phishing, Passwords, SMS) ---
  { id: 'cyberbullying', agentId: 'cipher', type: 'scenario', createdAt: ago(25), bands: ['middle', 'senior'],
    title: 'Class group chat drama',
    body: 'In your school section WhatsApp group, someone posts an embarrassing morphed photo of Rohan. Classmates start sending laughing stickers and insulting comments. Rohan stops replying and looks devastated. Your friend whispers: “Forward it to the other group!”',
    question: 'How should you respond right now?', scene: { emojis: ['📱', '😢', '💬'], bubble: 'Forward it, everyone is laughing!' },
    sourceCards: [{ id: 'DIG-029', title: 'Handling cyberbullying' }], stats: { responses: 4120, avgScore: 84 } },

  { id: 'screenshare-scam', agentId: 'cipher', type: 'scam_legit', createdAt: ago(45), bands: ['middle', 'senior'],
    title: 'Urgent gaming account unlock', body: 'A Discord DM pops up from “GamerSupport_Official”:',
    message: { from: 'GamerSupport_Official', text: '⚠️ Your account will be banned in 15 mins for suspicious activity! To verify ownership, download AnyDesk or QuickSupport on your mobile and send us your 9-digit remote connection code.' },
    sourceCards: [{ id: 'DIG-028', title: 'Screen-sharing app fraud' }], stats: { responses: 5820 } },

  { id: 'wifi-sniff', agentId: 'cipher', type: 'poll', createdAt: ago(60), bands: ['junior', 'middle', 'senior'],
    title: 'Free Wi-Fi at the railway station', body: 'You’re waiting for a train and see an open network named “Free_Public_Station_WiFi” with no password required.',
    question: 'What is safe to do on this open public Wi-Fi?',
    options: [
      { id: 'a', text: 'Log into your parent’s net-banking app to pay a bill' },
      { id: 'b', text: 'Browse public news websites with HTTPS' },
      { id: 'c', text: 'Enter credit card details for online shopping' },
      { id: 'd', text: 'Accept a pop-up prompt to install a “security certificate”' }
    ],
    sourceCards: [{ id: 'DIG-026', title: 'Public Wi-Fi risks' }], stats: { responses: 8940 } },

  { id: 'game-skin-phish', agentId: 'cipher', type: 'myth_fact', createdAt: ago(90), bands: ['junior', 'middle', 'senior'],
    title: 'Free Mythic Skins', body: 'A popular YouTube comment claims:',
    statement: '“Entering your gaming password on a third-party rewards website is safe as long as the URL has a green padlock icon.”',
    sourceCards: [{ id: 'DIG-031', title: 'Gaming scams & credential phishing' }], stats: { responses: 11200 } },

  { id: 'passphrase-power', agentId: 'cipher', type: 'poll', createdAt: ago(110), bands: ['middle', 'senior'],
    title: 'The strongest password', body: 'You need a password that is almost impossible for hacker algorithms to crack, but easy for you to remember.',
    question: 'Which of these is the most secure password format?',
    options: [
      { id: 'a', text: 'P@ssw0rd123!' },
      { id: 'b', text: 'Rahul_2012' },
      { id: 'c', text: 'mango-tractor-purple-guitar (4 random words)' },
      { id: 'd', text: 'Your phone number backwards' }
    ],
    sourceCards: [{ id: 'DIG-010', title: 'Strong passwords' }], stats: { responses: 9450 } },

  { id: 'scam-power', agentId: 'cipher', type: 'scam_legit', createdAt: ago(130), bands: ['middle', 'senior'],
    title: 'A message to Dad', body: 'Your dad got this SMS last night. Is it real?',
    message: { from: '+91 98•••• 4417', text: 'Dear customer, your electricity will be disconnected tonight at 9:30 PM as your last bill was not updated. Please call electricity officer immediately on 98•••• 4417.' },
    sourceCards: [{ id: 'DIG-007', title: 'Bill and KYC scams' }], stats: { responses: 7410 } },

  // --- COIN (Practical Finance) ---
  { id: 'needs-wants', agentId: 'coin', type: 'scenario', createdAt: ago(140), bands: ['junior', 'middle', 'senior'],
    title: 'The limited-edition hoodie',
    body: 'Kabir saved ₹1,500 from his birthday. His school exam reference books cost ₹600. His classmates are all ordering a trendy anime hoodie that costs exactly ₹1,500. His friend says: “Borrow books later, buy the hoodie before it sells out!”',
    question: 'How should Kabir prioritize his money?', scene: { emojis: ['👕', '📚', '🪙'], bubble: 'Buy the hoodie now!' },
    sourceCards: [{ id: 'MON-001', title: 'Needs vs Wants' }], stats: { responses: 3120, avgScore: 78 } },

  { id: 'upi-pin-scam', agentId: 'coin', type: 'scam_legit', createdAt: ago(160), bands: ['middle', 'senior'],
    title: 'Selling an old bicycle on OLX', body: 'You list your old cycle for ₹2,000. A buyer messages immediately:',
    message: { from: '+91 99•••• 8122', text: 'I am sending ₹2,000 advance via Google Pay QR code. Please scan this QR code and enter your 6-digit UPI PIN to claim the money in your bank account.' },
    sourceCards: [{ id: 'MON-005', title: 'UPI safety & collect requests' }], stats: { responses: 8320 } },

  // --- ECHO (Mental Health & Feelings) ---
  { id: 'exam-panic', agentId: 'echo', type: 'scenario', createdAt: ago(175), bands: ['middle', 'senior'],
    title: 'Blank mind before science exam',
    body: 'It’s 8:45 AM, 15 minutes before the science board exam. Priya’s heart is pounding, her palms are drenched in sweat, and she feels like she has forgotten every single chapter. Her classmate shouts: “Quick, revise all 5 chapters right now!”',
    question: 'What should Priya do to calm her brain?', scene: { emojis: ['😰', '📝', '🧠'], bubble: 'I forgot everything!!' },
    sourceCards: [{ id: 'FEEL-002', title: 'Taming exam anxiety' }], stats: { responses: 4210, avgScore: 72 } },

  { id: 'tele-manas', agentId: 'echo', type: 'poll', createdAt: ago(190), bands: ['junior', 'middle', 'senior'],
    title: 'Free national mental health support', body: 'Dealing with heavy stress, loneliness, or anxiety can feel overwhelming.',
    question: 'Which toll-free number connects students in India to free, 24/7 confidential mental health counselors in 20+ languages?',
    options: [
      { id: 'a', text: '100' },
      { id: 'b', text: '14416 (Tele-MANAS)' },
      { id: 'c', text: '139' },
      { id: 'd', text: '1930' }
    ],
    sourceCards: [{ id: 'FEEL-006', title: 'Tele-MANAS support' }], stats: { responses: 6720 } },

  // --- PIXEL (Screen Balance & Digital Wellbeing) ---
  { id: 'eye-rule-20', agentId: 'pixel', type: 'myth_fact', createdAt: ago(210), bands: ['junior', 'middle', 'senior'],
    title: 'Screen eye strain', body: 'Many students believe this about screen time:',
    statement: '“Looking at a screen continuously for 4 hours will not cause eye fatigue if your screen brightness is lowered to 50%.”',
    sourceCards: [{ id: 'TECH-001', title: 'Digital balance & eye health' }], stats: { responses: 8190 } },

  { id: 'phone-curfew', agentId: 'pixel', type: 'poll', createdAt: ago(230), bands: ['middle', 'senior'],
    title: 'Deep sleep and screens', body: 'Blue light from phone screens tells your brain that it is still midday.',
    question: 'How long before bedtime should you stop looking at phone screens to protect restorative sleep?',
    options: [
      { id: 'a', text: '5 minutes' },
      { id: 'b', text: 'At least 30 to 60 minutes' },
      { id: 'c', text: 'Keep scrolling until you fall asleep' },
      { id: 'd', text: 'Screens have no effect on sleep' }
    ],
    sourceCards: [{ id: 'TECH-002', title: 'Notification diet & sleep hygiene' }], stats: { responses: 7450 } },

  // --- SAATHI (Inclusion, Empathy & Anti-Bullying) ---
  { id: 'upstander-lunch', agentId: 'saathi', type: 'scenario', createdAt: ago(250), bands: ['junior', 'middle', 'senior'],
    title: 'The new student at the lunch table',
    body: 'Dev, a new student who recently moved from another state and speaks with an accent, sits alone in the cafeteria. Two seniors at the adjacent table start mimicking his accent loudly and pointing. Your classmates look away in silence.',
    question: 'What can you do to be an active upstander?', scene: { emojis: ['🍱', '🗣️', '🤝'], bubble: 'Look at how he talks!' },
    sourceCards: [{ id: 'INC-001', title: 'Respectful interaction & anti-bullying' }], stats: { responses: 3840, avgScore: 82 } },

  // --- GUARDIAN (Body Boundaries & Personal Safety) ---
  { id: 'secret-surprise', agentId: 'guardian', type: 'myth_fact', createdAt: ago(270), bands: ['junior', 'middle', 'senior'],
    title: 'Secrets vs Surprises', body: 'Important rule for personal safety:',
    statement: '“If an adult tells you to keep a secret that makes you feel uneasy, scared, or uncomfortable, you must keep it so you don’t get them into trouble.”',
    sourceCards: [{ id: 'SAFE-002', title: 'Secrets vs surprises' }], stats: { responses: 10420 } },

  { id: 'swimsuit-rule', agentId: 'guardian', type: 'poll', createdAt: ago(290), bands: ['junior', 'middle'],
    title: 'Body boundaries', body: 'Personal safety is every child’s right.',
    question: 'What is the universal “Swimsuit Rule” for personal body safety?',
    options: [
      { id: 'a', text: 'Swimsuits are only worn at public pools' },
      { id: 'b', text: 'Parts of your body covered by a swimsuit are strictly private; nobody has the right to touch or photograph them' },
      { id: 'c', text: 'Only strangers can violate personal boundaries' },
      { id: 'd', text: 'Safety rules only apply when you are an adult' }
    ],
    sourceCards: [{ id: 'SAFE-001', title: 'The Swimsuit Rule' }], stats: { responses: 8910 } },

  // --- NYAYA (Everyday Law & Rights) ---
  { id: 'mrp-chips', agentId: 'nyaya', type: 'scenario', createdAt: ago(310), bands: ['middle', 'senior'],
    title: 'Cold drink above MRP',
    body: 'On a sweltering afternoon, Arjun buys a ₹20 chilled mango drink at a bus station stall. The vendor charges him ₹25, stating: “₹5 extra cooling charge for the refrigerator!” Arjun points to the printed MRP on the bottle.',
    question: 'What are Arjun’s legal consumer rights?', scene: { emojis: ['🧃', '💵', '🏪'], bubble: 'Cooling charge is ₹5 extra!' },
    sourceCards: [{ id: 'LAW-003', title: 'Consumer Protection Act & MRP' }], stats: { responses: 3670, avgScore: 76 } },

  { id: 'zero-fir', agentId: 'nyaya', type: 'myth_fact', createdAt: ago(330), bands: ['middle', 'senior'],
    title: 'Filing an FIR', body: 'Know your legal rights:',
    statement: '“A police station can refuse to register your complaint if the crime happened in another town or outside their jurisdiction.”',
    sourceCards: [{ id: 'LAW-002', title: 'Zero FIR rights' }], stats: { responses: 9810 } },

  // --- PAWS (Animal Welfare & Coexistence) ---
  { id: 'dog-body-lang', agentId: 'paws', type: 'scenario', createdAt: ago(350), bands: ['junior', 'middle', 'senior'],
    title: 'Approached by an excited street dog',
    body: 'Tanvi is walking home when a community dog trots towards her, barking with perked ears and stiff tail. Her younger cousin panics, screams, and starts running away as fast as possible.',
    question: 'What should Tanvi do right now?', scene: { emojis: ['🐕', '🏃‍♀️', '🌳'], bubble: 'Run as fast as you can!' },
    sourceCards: [{ id: 'ANI-001', title: 'Understanding dog body language' }], stats: { responses: 4190, avgScore: 81 } },

  { id: 'rabies-wash', agentId: 'paws', type: 'poll', createdAt: ago(370), bands: ['junior', 'middle', 'senior'],
    title: 'Immediate animal bite first aid', body: 'If a stray animal scratches or breaks your skin:',
    question: 'What is the single most critical first step before visiting a clinic or doctor?',
    options: [
      { id: 'a', text: 'Apply turmeric and tie a tight bandage' },
      { id: 'b', text: 'Wash the wound thoroughly with soap under running tap water for at least 15 minutes' },
      { id: 'c', text: 'Wait 48 hours to check if the animal falls sick' },
      { id: 'd', text: 'Put ice cubes directly on the bite' }
    ],
    sourceCards: [{ id: 'ANI-002', title: 'Dog bite first aid & rabies prevention' }], stats: { responses: 11400 } },

  // --- VOLT (Clean Energy & Resources) ---
  { id: 'phantom-charger', agentId: 'volt', type: 'myth_fact', createdAt: ago(390), bands: ['junior', 'middle', 'senior'],
    title: 'Phone chargers left in wall sockets', body: 'Energy habits at home:',
    statement: '“A phone charger plugged into the wall with the switch turned ON consumes zero electricity when no phone is connected.”',
    sourceCards: [{ id: 'GRN-001', title: 'Phantom vampire power' }], stats: { responses: 7920 } },

  { id: 'lithium-trash', agentId: 'volt', type: 'poll', createdAt: ago(410), bands: ['middle', 'senior'],
    title: 'Old swollen phone battery', body: 'You find an old puffy smartphone battery in a drawer.',
    question: 'Why should you NEVER throw lithium-ion batteries into normal household garbage?',
    options: [
      { id: 'a', text: 'They cause the garbage bin to smell bad' },
      { id: 'b', text: 'When compressed in garbage trucks, damaged lithium batteries ignite violent chemical fires' },
      { id: 'c', text: 'Batteries degrade into plastic pellets' },
      { id: 'd', text: 'It is completely safe if wrapped in newspaper' }
    ],
    sourceCards: [{ id: 'GRN-004', title: 'Battery care & e-waste' }], stats: { responses: 8650 } },

  // --- STORM (Disaster Readiness) ---
  { id: 'earthquake-desk', agentId: 'storm', type: 'scenario', createdAt: ago(430), bands: ['junior', 'middle', 'senior'],
    title: 'Tremors inside the classroom',
    body: 'During class, the ground begins rumbling violently. Overhead fans shake and glass windows rattle. Several students scream and bolt toward the door and stairwell.',
    question: 'What must you do immediately?', scene: { emojis: ['🏫', '🏚️', '🪑'], bubble: 'Run to the stairs!!' },
    sourceCards: [{ id: 'DIS-001', title: 'Earthquake indoors: Drop, Cover, Hold on' }], stats: { responses: 5120, avgScore: 79 } },

  { id: 'flood-walk', agentId: 'storm', type: 'myth_fact', createdAt: ago(450), bands: ['junior', 'middle', 'senior'],
    title: 'Urban flash floods', body: 'During heavy monsoon waterlogging:',
    statement: '“It is completely safe to walk or cycle across moving floodwater if it only looks ankle-deep.”',
    sourceCards: [{ id: 'DIS-002', title: 'Flood safety & Turn Around Don’t Drown' }], stats: { responses: 10300 } },

  // --- STRIDE (Fitness & Ergonomics) ---
  { id: 'backpack-weight', agentId: 'stride', type: 'poll', createdAt: ago(470), bands: ['junior', 'middle'],
    title: 'The 10% schoolbag rule', body: 'Heavy backpacks can permanently deform developing spine discs.',
    question: 'According to pediatric guidelines, what is the maximum recommended weight for a student’s backpack?',
    options: [
      { id: 'a', text: 'Up to 35% of the student’s body weight' },
      { id: 'b', text: 'No more than 10% of the student’s body weight' },
      { id: 'c', text: 'Exactly 15 kg for all classes' },
      { id: 'd', text: 'Any weight is fine if it has double straps' }
    ],
    sourceCards: [{ id: 'FIT-003', title: 'School backpack safety' }], stats: { responses: 9870 } },

  // --- CARE (Hygiene & Puberty) ---
  { id: 'wash-20s', agentId: 'care', type: 'poll', createdAt: ago(490), bands: ['junior', 'middle', 'senior'],
    title: 'Why 20 seconds of soap?', body: 'Hand hygiene prevents infections.',
    question: 'Why do doctors emphasize rubbing hands with soap for at least 20 full seconds rather than a quick 5-second splash?',
    options: [
      { id: 'a', text: 'Soap needs 20 seconds to change color' },
      { id: 'b', text: 'Soap molecules need 20 seconds of friction to pry open and dismantle the fatty lipid shell of viruses and bacteria' },
      { id: 'c', text: 'It is only required in surgical hospitals' },
      { id: 'd', text: 'To make extra foam for scent' }
    ],
    sourceCards: [{ id: 'HYG-001', title: 'The 20-second handwashing technique' }], stats: { responses: 11150 } },

  // --- FORGE (Student Enterprise) ---
  { id: 'pitch-60s', agentId: 'forge', type: 'poll', createdAt: ago(510), bands: ['middle', 'senior'],
    title: 'The 60-Second Elevator Pitch', body: 'You have 60 seconds to present your student eco-project to the school principal.',
    question: 'What should you talk about in your very first sentence?',
    options: [
      { id: 'a', text: 'How much money the product will cost' },
      { id: 'b', text: 'The specific painful problem you are solving and who suffers from it' },
      { id: 'c', text: 'A long list of features and colors' },
      { id: 'd', text: 'Your personal hobby history' }
    ],
    sourceCards: [{ id: 'ENT-001', title: 'Spotting real problems' }], stats: { responses: 4620 } },

  // --- COMPASS (Careers) ---
  { id: 'streams', agentId: 'compass', type: 'myth_fact', createdAt: ago(530), bands: ['senior'],
    title: 'Choosing a stream after Class 10', body: 'A common belief in high school:',
    statement: '“Science is the only stream for high-scoring students; Arts and Humanities have no high-paying modern career paths.”',
    sourceCards: [{ id: 'CAR-001', title: 'Choosing a stream after Class 10' }], stats: { responses: 7900 } },

  // --- EMBER, SIGNAL, PULSE, BASIL, CIVIC (Foundational Life Scenarios) ---
  { id: 'oil-fire', agentId: 'ember', type: 'scenario', createdAt: ago(550), bands: ['middle', 'senior'],
    title: 'Oil fire in the pan',
    body: 'It’s 8 PM. Maya is frying snacks when the oil in the pan suddenly catches fire. Flames are reaching up toward the chimney hood. Her younger brother runs in with a mug of water.',
    question: 'What should Maya do, right now?', scene: { emojis: ['🔥', '🍳', '🧒'], bubble: 'Should I throw water?!' },
    sourceCards: [{ id: 'FIRE-012', title: 'Kitchen oil fires' }, { id: 'FIRE-003', title: 'When to get out' }], stats: { responses: 2418, avgScore: 61 } },

  { id: 'road-first', agentId: 'signal', type: 'poll', createdAt: ago(570), bands: ['senior'],
    title: 'First at a bike accident', body: 'You’re first to reach a bike accident on a busy road. The rider is awake but can’t stand up.',
    question: 'What do you do first?',
    options: [{ id: 'a', text: 'Lift them into a car and rush to hospital' }, { id: 'b', text: 'Make the spot safe from traffic, then call 112' },
      { id: 'c', text: 'Take off their helmet so they can breathe' }, { id: 'd', text: 'Give them water and help them sit up' }],
    sourceCards: [{ id: 'ROAD-021', title: 'Helping at a road accident' }], stats: { responses: 18902 } },

  { id: 'toothpaste', agentId: 'pulse', type: 'myth_fact', createdAt: ago(590), bands: ['junior', 'middle', 'senior'],
    title: 'Burns', body: 'Lots of people believe this. Do you?', statement: '“Putting toothpaste on a burn helps it heal faster.”',
    sourceCards: [{ id: 'AID-002', title: 'Minor burns' }], stats: { responses: 9320 } },

  { id: 'nosebleed', agentId: 'pulse', type: 'scenario', createdAt: ago(610), bands: ['junior', 'middle', 'senior'],
    title: 'Nosebleed in class', body: 'During maths class, your friend Sam’s nose suddenly starts bleeding. Sam looks scared, and someone shouts “Tilt your head back!”',
    question: 'How do you help Sam?', scene: { emojis: ['🩸', '🧑‍🎓', '🏫'], bubble: 'Tilt your head back!' },
    sourceCards: [{ id: 'AID-011', title: 'Nosebleeds' }], stats: { responses: 5120, avgScore: 58 } },

  { id: 'drink', agentId: 'basil', type: 'poll', createdAt: ago(630), bands: ['junior', 'middle', 'senior'],
    title: 'After the match', body: 'You just played football for an hour on a hot afternoon.', question: 'What’s the best drink?',
    options: [{ id: 'a', text: 'A cold fizzy drink' }, { id: 'b', text: 'Plain water (lots of it)' }, { id: 'c', text: 'An energy drink' }, { id: 'd', text: 'Packaged fruit juice' }],
    sourceCards: [{ id: 'NUT-005', title: 'Staying hydrated' }], stats: { responses: 11240 } },

  { id: 'bus-wrapper', agentId: 'civic', type: 'scenario', createdAt: ago(650), bands: ['junior', 'middle'],
    title: 'No dustbin on the bus', body: 'Riya finishes a packet of chips on the city bus. There’s no dustbin anywhere, and her friend says “Just drop it under the seat, everyone does.”',
    question: 'What should Riya do?', scene: { emojis: ['🚌', '🍟', '👧'], bubble: 'Everyone does it…' },
    sourceCards: [{ id: 'CIV-003', title: 'Litter & public spaces' }], stats: { responses: 3890, avgScore: 79 } },

  { id: 'lift-fire', agentId: 'ember', type: 'myth_fact', createdAt: ago(670), bands: ['junior', 'middle', 'senior'],
    title: 'Fire in a building', body: 'Quick one!', statement: '“If there’s a fire in your building, take the lift. It’s the fastest way out.”',
    sourceCards: [{ id: 'FIRE-020', title: 'Escaping a building fire' }], stats: { responses: 12110 } },
]

/* ---------- mock-only answer keys (the real backend keeps these server-side) ---------- */
type Rubric = { id: string; point: string; weight: number; note: string; keys: RegExp }[]
export const SCENARIO_KEYS: Record<string, { rubric: Rubric; dangerous: RegExp[]; good: string; tips: string }> = {
  'cyberbullying': {
    rubric: [
      { id: 'r1', point: 'Do NOT forward or share the photo', weight: 35, note: 'Forwarding makes you part of the bullying chain.', keys: /(not|never|don'?t|stop)[^.]{0,20}(forward|share|send)|don'?t forward/i },
      { id: 'r2', point: 'Take screenshots as proof and support Rohan', weight: 30, note: 'Evidence is needed to report, and checking in on Rohan shows true allyship.', keys: /screenshot|proof|evidence|support|comfort|check on/i },
      { id: 'r3', point: 'Report to a trusted adult, teacher or school counselor', weight: 35, note: 'School authorities or parents can intervene safely.', keys: /teacher|parent|adult|counselor|report|principal|1930/i },
    ],
    dangerous: [/(forward|share|laugh|mock)[^.]{0,15}(photo|pic)/i, /insult|swear|abuse/i],
    good: 'You stood up against cyber harassment.', tips: 'Never forward cruel photos. Screenshot the evidence, block the sender, and tell an adult.',
  },
  'needs-wants': {
    rubric: [
      { id: 'r1', point: 'Prioritize Needs (exam books) before Wants (hoodie)', weight: 45, note: 'School study books are essential; fashion clothing is a want.', keys: /need|book|essential|study|exam|priorit/i },
      { id: 'r2', point: 'Save remainder or plan for the hoodie later', weight: 30, note: 'Buy the ₹600 books first, save the ₹900 towards the hoodie.', keys: /save|later|budget|remain|balance/i },
      { id: 'r3', point: 'Resist peer pressure', weight: 25, note: 'Spending all savings just because friends did is a financial trap.', keys: /peer pressure|friend|resist|own choice/i },
    ],
    dangerous: [/borrow books|buy hoodie (only|first|now)/i],
    good: 'Smart budgeting! Needs always come before wants.', tips: 'Buy your ₹600 essential exam books first. You still keep ₹900 in savings!',
  },
  'exam-panic': {
    rubric: [
      { id: 'r1', point: 'Stop cramming and close the books', weight: 30, note: 'Last 15 minutes of frantic reading only floods the brain with cortisol.', keys: /close|stop (reading|cramming)|put away/i },
      { id: 'r2', point: 'Use deep 4-7-8 breathing or grounding', weight: 40, note: 'Slow exhales activate the parasympathetic nervous system to calm racing heart.', keys: /breath|inhale|exhale|grounding|calm|water|relax/i },
      { id: 'r3', point: 'Remember that blankness is temporary adrenaline', weight: 30, note: 'Once Priya sits and reads question 1, recognition memory kicks in.', keys: /temporary|memory|start|question 1|reassur|normal/i },
    ],
    dangerous: [/read all|revise everything|panic/i],
    good: 'You know how to reset your nervous system.', tips: 'Take 4 slow deep breaths. Memory blanks are just adrenaline; the facts return as soon as you read the first question.',
  },
  'upstander-lunch': {
    rubric: [
      { id: 'r1', point: 'Do not join in the laughter or stay silent', weight: 30, note: 'Bystander silence encourages bullies.', keys: /not (laugh|silent)|don'?t laugh/i },
      { id: 'r2', point: 'Invite Dev over or sit with him', weight: 40, note: 'Direct inclusion neutralizes isolation immediately.', keys: /sit with|invite|talk to|join|welcome|dev/i },
      { id: 'r3', point: 'Politely speak up or notify a teacher', weight: 30, note: 'Saying “that’s uncool” or informing a teacher stops the harassment.', keys: /tell|stop|uncool|teacher|staff/i },
    ],
    dangerous: [/laugh|join/i],
    good: 'That is true leadership and empathy.', tips: 'A simple “Hey Dev, want to sit with us?” completely changes someone’s school experience.',
  },
  'mrp-chips': {
    rubric: [
      { id: 'r1', point: 'Explain that charging above MRP is illegal', weight: 40, note: 'MRP stands for Maximum Retail Price; cooling charges cannot exceed MRP.', keys: /mrp|illegal|law|maximum retail price|not allowed/i },
      { id: 'r2', point: 'Refuse to pay extra or ask for a cash receipt', weight: 35, note: 'Vendors rarely write illegal surcharges on official bills.', keys: /bill|receipt|refuse|20 only/i },
      { id: 'r3', point: 'Report to National Consumer Helpline 1915', weight: 25, note: 'Consumers can report violations via 1915 or consumer helpline portal.', keys: /consumer|helpline|1915|complaint|report/i },
    ],
    dangerous: [], good: 'Knowing your rights protects everyone.', tips: 'MRP includes all taxes and costs. No seller can legally charge above MRP for cooling or handling.',
  },
  'dog-body-lang': {
    rubric: [
      { id: 'r1', point: 'Stop and do NOT run', weight: 45, note: 'Running activates the dog’s predatory chase reflex.', keys: /(not|don'?t|never|stop)[^.]{0,15}run|stand still/i },
      { id: 'r2', point: 'Be a Tree: fold arms and look away', weight: 35, note: 'Fold arms across chest, stay still, avoid direct eye contact.', keys: /tree|fold arms|arms|look away|no eye contact|quiet/i },
      { id: 'r3', point: 'Wait calmly until the dog loses interest', weight: 20, note: 'Dogs sniff and walk away when there is no reaction.', keys: /wait|walk away|calm|leave/i },
    ],
    dangerous: [/run|scream|shout|throw stone|hit/i],
    good: 'You saved both yourself and your cousin!', tips: '“Be a Tree”: Stand still, fold arms, and look at your feet. When you become boring, the dog walks away.',
  },
  'earthquake-desk': {
    rubric: [
      { id: 'r1', point: 'Drop, Cover, and Hold On under desks', weight: 45, note: 'Ducking under a desk protects against falling concrete and light fixtures.', keys: /drop|cover|hold|under (the )?(desk|table|bench)/i },
      { id: 'r2', point: 'Do NOT run for the stairs or elevators during shaking', weight: 35, note: 'Most injuries occur from falling debris while trying to flee.', keys: /(not|don'?t|never)[^.]{0,20}(run|stairs|lift|elevator)|stay inside/i },
      { id: 'r3', point: 'Protect head and neck with arms', weight: 20, note: 'Clasp hands behind neck if no desk is available.', keys: /head|neck|arms|protect/i },
    ],
    dangerous: [/run (outside|stairs|lift)|use elevator|balcony/i],
    good: 'Spot-on disaster survival instinct.', tips: 'Drop, Cover, and Hold On. Running during tremors leads to stampedes and falling debris injuries.',
  },
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
  'screenshare-scam': { correct: 'scam', dist: { scam: 92, legit: 8 },
    explanation: 'Scam! Legitimate tech support never asks you to install AnyDesk or QuickSupport. These apps let hackers view your entire screen, read OTPs, and steal passwords in real time.' },
  'wifi-sniff': { correct: 'b', dist: { a: 11, b: 76, c: 7, d: 6 },
    explanation: 'Unsecured public Wi-Fi broadcasts data openly. Anyone on the same hotspot can snoop on unencrypted traffic. Never do banking or shopping on public Wi-Fi without a VPN!' },
  'game-skin-phish': { correct: 'myth', dist: { myth: 84, fact: 16 },
    explanation: 'Myth! A green padlock only means encryption, not honesty. Fake phishing websites use free SSL certificates to look legit and steal your account login.' },
  'passphrase-power': { correct: 'c', dist: { a: 22, b: 12, c: 62, d: 4 },
    explanation: 'A passphrase made of 4 random words (e.g. mango-tractor-purple-guitar) has huge entropy, making it virtually impossible for computers to brute-force crack, while being super easy to remember.' },
  'scam-power': { correct: 'scam', dist: { scam: 89, legit: 11 },
    explanation: 'Scam. Electricity boards do not send threats from personal mobile numbers asking you to call. Check your bill status only on the official state electricity board app.' },
  'upi-pin-scam': { correct: 'scam', dist: { scam: 94, legit: 6 },
    explanation: 'Scam! You NEVER need to enter your UPI PIN to receive money. Entering your PIN always sends money OUT of your bank account. Scammers send fake QR collect requests.' },
  'tele-manas': { correct: 'b', dist: { a: 14, b: 72, c: 6, d: 8 },
    explanation: '14416 is Tele-MANAS, the Government of India’s free 24/7 tele-mental health helpline available in 20+ languages for counseling and crisis support.' },
  'eye-rule-20': { correct: 'myth', dist: { myth: 78, fact: 22 },
    explanation: 'Myth! Prolonged close-up screen focus locks your eye muscles. Follow the 20-20-20 rule: every 20 minutes, look at an object 20 feet away for 20 seconds.' },
  'phone-curfew': { correct: 'b', dist: { a: 12, b: 77, c: 7, d: 4 },
    explanation: 'Blue light from phones halts melatonin production. Giving screens a 30 to 60 minute break before sleep allows the brain to enter natural deep rest.' },
  'secret-surprise': { correct: 'myth', dist: { myth: 91, fact: 9 },
    explanation: 'Myth! Good surprises make people happy and have an end date. Unsafe secrets make you feel scared or guilty. You NEVER have to keep an unsafe secret. Tell your Trusted 5 adults!' },
  'swimsuit-rule': { correct: 'b', dist: { a: 8, b: 88, c: 2, d: 2 },
    explanation: 'The Swimsuit Rule is the gold standard for child safety: parts of your body covered by a swimsuit are strictly private. Nobody has the right to touch or photograph them.' },
  'zero-fir': { correct: 'myth', dist: { myth: 83, fact: 17 },
    explanation: 'Myth! Under Indian law, a “Zero FIR” can be registered at ANY police station in the country, even if the crime occurred outside their territorial jurisdiction.' },
  'rabies-wash': { correct: 'b', dist: { a: 9, b: 84, c: 5, d: 2 },
    explanation: 'Washing animal scratches or bites under running water with soap for 15 full minutes physically flushes away the virus and saves lives before you reach the hospital.' },
  'phantom-charger': { correct: 'myth', dist: { myth: 74, fact: 26 },
    explanation: 'Myth! Plugged-in chargers with the switch on consume 0.2–0.5W of phantom power 24/7. Always flip the wall switch off when your phone is unplugged.' },
  'lithium-trash': { correct: 'b', dist: { a: 7, b: 86, c: 4, d: 3 },
    explanation: 'Punctured or crushed lithium batteries ignite explosive chemical fires inside garbage compaction trucks. Always deposit old batteries at e-waste bins.' },
  'flood-walk': { correct: 'myth', dist: { myth: 87, fact: 13 },
    explanation: 'Myth! Just 6 inches of fast-moving flood water can sweep away an adult. Murky floodwater also hides open manholes, electric shock hazards, and submerged debris.' },
  'backpack-weight': { correct: 'b', dist: { a: 11, b: 82, c: 5, d: 2 },
    explanation: 'Schoolbags must never exceed 10% of a student’s body weight. Heavier bags lead to chronic neck strain, spinal disc compression, and posture problems.' },
  'wash-20s': { correct: 'b', dist: { a: 5, b: 89, c: 3, d: 3 },
    explanation: 'Soap molecules need 20 seconds of friction to break open the fatty lipid membranes of viruses. Thorough lathering destroys germs that quick rinsing leaves behind.' },
  'pitch-60s': { correct: 'b', dist: { a: 14, b: 79, c: 4, d: 3 },
    explanation: 'Great pitches always begin with the PROBLEM. If the audience doesn’t understand the problem and who is hurting, they will never care about your product.' },
  'streams': { correct: 'myth', dist: { myth: 86, fact: 14 },
    explanation: 'Myth! Commerce, Humanities, Design, Law, and Technology all lead to flourishing modern careers. Stream choice should match your curiosity and strengths, not outdated stereotypes.' },
  'road-first': { correct: 'b', dist: { a: 27, b: 61, c: 4, d: 8 },
    explanation: 'Moving an injured person can worsen spine trauma. Make the spot safe, call 112, and keep them still. India’s Good Samaritan Law protects people who stop to help.' },
  'drink': { correct: 'b', dist: { a: 22, b: 64, c: 9, d: 5 },
    explanation: 'Plain water is the best way to rehydrate after normal play. Fizzy drinks, energy drinks and packaged juices add lots of sugar, and energy drinks aren’t meant for kids.' },
  'toothpaste': { correct: 'myth', dist: { myth: 71, fact: 29 },
    explanation: 'Myth! Toothpaste traps heat and can cause skin infections. Cool the burn under cool running tap water for 20 minutes, then cover loosely with a clean cloth.' },
  'lift-fire': { correct: 'myth', dist: { myth: 88, fact: 12 },
    explanation: 'Myth! Lifts can lose power or open directly onto a burning floor. Always take the stairs, stay low under smoke, and evacuate to the open assembly point.' },
}

export const RESPONSES: Record<string, Response[]> = {
  'cyberbullying': [
    { id: 'c1', nickname: 'BraveKoala', avatar: '🐨', score: 95, expertPick: true,
      text: 'Do not forward it! Take a screenshot for proof, message Rohan privately to let him know he is not alone, and report the message to the class teacher or counselor.',
      expertReply: 'Outstanding maturity. Supporting the targeted student while collecting proof is the gold standard of an upstander. 🛡️' },
  ],
  'needs-wants': [
    { id: 'n1', nickname: 'SunnyOtter', avatar: '🦦', score: 98, expertPick: true,
      text: 'Buy the ₹600 school books first because they are a clear Need for exams. Save the remaining ₹900 towards the hoodie for next month.',
      expertReply: 'Perfect application of Needs vs Wants. You secured your exams AND kept money in your pocket! 🪙' },
  ],
  'exam-panic': [
    { id: 'e1', nickname: 'ZippyDolphin', avatar: '🐬', score: 92, expertPick: true,
      text: 'Close the books immediately. Sit down, sip water, and do slow 4-7-8 breathing. Remind yourself that blankness is just adrenaline, and memory returns when reading question 1.',
      expertReply: 'Scientifically accurate. Taking deep exhales resets the nervous system so your prefrontal cortex can think clearly again. 🧠' },
  ],
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
    topics: {
      fire: true, road: true, firstaid: true, disaster: true, safety: true, law: true, fitness: true, hygiene: true,
      environment: true, animals: true, greenenergy: true, civic: true,
      money: true, enterprise: true, careers: false, digital: true, nutrition: true,
      feelings: true, screentime: true, inclusion: true,
    } },
}
