"""
New Agents in the LIFE Pillar (Part 3):
- Stride (Fitness & Body Care - FIT)
- Care (Hygiene & Self-care - HYG) [sensitive puberty basics]
"""
from cards_existing import make_card

def get_stride_cards():
    cards = []

    # 1. FIT-001: 60 mins play
    cards.append(make_card(
        "FIT-001", "stride", "Physical play", "60 minutes of active play daily: Heart health and joy",
        ["junior", "middle", "senior"],
        ["The WHO recommends at least 60 minutes of moderate-to-vigorous daily physical activity for youth.",
         "Active outdoor play releases endorphins and brain-derived neurotrophic factor (BDNF) which enhances learning."],
        ["Accumulate at least 60 minutes of movement daily: running, football, cycling, swimming, or dancing", "Mix high-energy games with casual playground activities throughout the day", "Invite friends outdoors instead of spending all weekend glued to mobile gaming screens"],
        ["Never replace active outdoor playtime with continuous sedentary sofa sitting", "Never worry about body shape or calories: movement is about energy, joy, and vitality"],
        "Playing active outdoor games is only for kids who want to become professional Olympic athletes.", "myth", "Daily physical play is essential for every young person's heart, bone density, and emotional happiness.",
        "How much daily physical activity does the World Health Organization recommend for students aged 5 to 17?",
        ["Zero minutes", "At least 60 minutes of moderate-to-vigorous physical play daily", "5 hours of heavy gym lifting", "10 seconds"], 1,
        "60 minutes of daily play builds strong bones, cardiovascular endurance, and cheerful moods.",
        ["On a Saturday afternoon at {at}, {name} and friends have been playing mobile games for 4 hours."],
        "How can {name} energize the afternoon?",
        [("Propose going outside for an hour of football, cycling, tag, or badminton", "Achieves essential daily 60 minutes of movement.", True, "go outside|play football|cycling|60 minutes play", 45),
         ("Recognize that active play releases endorphins that boost happiness and focus", "Understands mental and physical vitality benefits.", True, "endorphins|vitality|heart health|mood", 35),
         ("Encourage playful movement for fun, friendship, and joy without any body talk", "Promotes body-neutral joyful fitness.", False, "movement for fun|no body shaming|joyful", 20)],
        ["stay on sofa for 8 hours", "obsess over calories", "refuse to move"],
        "World Health Organization Physical Activity Guidelines for Children", "https://who.int"
    ))

    # 2. FIT-002: Study posture
    cards.append(make_card(
        "FIT-002", "stride", "Ergonomics", "Study ergonomics: Sitting posture and spine alignment",
        ["junior", "middle", "senior"],
        ["Slouching forward ('tech neck') tilts the head, exerting up to 27 kg of gravitational strain on the cervical spine.",
         "Poor study posture causes chronic upper back pain, tension headaches, and shallow chest breathing."],
        ["Sit with feet flat on the floor, knees at a 90-degree angle, and lower back supported by the chair", "Raise study books or screens to eye level using book stands or a stack of boxes", "Keep shoulders relaxed and roll them backwards every 30 minutes"],
        ["Never study lying flat on your stomach on a soft bed for hours (compresses neck nerves)", "Never hunch shoulders forward with your nose 10 cm from the textbook"],
        "Lying on your stomach on the bed while doing homework is completely healthy for your spine.", "myth", "Prone bed reading hyperextends cervical vertebrae, causing chronic neck muscle spasms.",
        "What angle should your knees and elbows ideally maintain while studying at an ergonomic desk?",
        ["180 degrees straight", "Approximately 90 degrees with feet flat on the floor", "Crossed under body", "Hanging loose"], 1,
        "A 90-degree alignment keeps the spine naturally supported and prevents muscular strain.",
        ["Studying for long hours at a desk at {at}, {name} notices their neck aching and shoulders hunched forward."],
        "How should {name} optimize their study posture?",
        [("Adjust chair and desk so feet rest flat on the floor with knees and hips at 90 degrees", "Restores biomechanically neutral spine alignment.", True, "feet flat|90 degrees|spine neutral|lumbar support", 45),
         ("Elevate the textbook or laptop screen closer to eye level", "Eliminates forward cervical neck tilt.", True, "eye level|elevate screen|book stand", 35),
         ("Take a 2-minute posture break to roll shoulders backwards and stretch", "Relieves accumulated muscular tension.", False, "roll shoulders|stretch break", 20)],
        ["slouch nose to desk", "study on bed on stomach", "ignore neck pain"],
        "Indian Association of Physiotherapists Ergonomic Guidelines", "https://physiotherapyindia.org"
    ))

    # 3. FIT-003: Backpack safety
    cards.append(make_card(
        "FIT-003", "stride", "Backpack safety", "School backpack safety: The 10% weight rule and dual straps",
        ["junior", "middle", "senior"],
        ["Carrying a school bag heavier than 10% of your body weight causes compensatory spine curvature.",
         "Sliding a heavy bag over one shoulder causes asymmetrical shoulder hiking and scoliosis."],
        ["Ensure your packed school bag weighs under 10% of your body weight (e.g. max 4 kg for a 40 kg student)", "Always wear BOTH padded shoulder straps snugly so the bag rests flat against your mid-back", "Pack heaviest books closest to your spine and unpack unnecessary books every evening"],
        ["Never sling a heavy school backpack over a single shoulder", "Never let the backpack sag below your lower waist or buttocks"],
        "Slinging a heavy school bag over one single shoulder looks cool and causes zero harm.", "myth", "Single-shoulder carrying shifts your entire skeletal center of gravity, causing chronic shoulder asymmetry.",
        "According to the Ministry of Education School Bag Policy, a student's bag should not exceed what percentage of body weight?",
        ["50%", "Not more than 10% of the student's body weight", "25%", "80%"], 1,
        "The 10% limit protects developing spinal columns from compressive disc damage.",
        ["Packing the school bag for tomorrow at {at}, {name}'s backpack feels like a heavy sack of bricks."],
        "How should {name} practice backpack ergonomics?",
        [("Unpack books not on tomorrow's timetable to keep bag weight below 10% of body weight", "Adheres to statutory School Bag Policy limits.", True, "under 10 percent|unpack extra books|follow timetable", 45),
         ("Place the heaviest textbooks closest to your back and use both padded shoulder straps", "Optimizes load distribution near center of gravity.", True, "wear both straps|heaviest books close to spine", 35),
         ("Adjust straps so the bottom of the backpack rests above the waistline", "Prevents lumbar backward pulling.", False, "above waistline|snug straps", 20)],
        ["carry over one shoulder only", "pack whole library daily", "let bag sag below knees"],
        "Ministry of Education Policy on School Bag", "https://dsel.education.gov.in"
    ))

    # 4. FIT-004: Sleep hygiene
    cards.append(make_card(
        "FIT-004", "stride", "Sleep", "Quality sleep for growing minds: 8-10 hours and regular schedules",
        ["junior", "middle", "senior"],
        ["Growth hormone (somatotropin) is secreted primarily during deep Stage 3 slow-wave sleep.",
         "Sleep deprivation impairs memory consolidation, immune resistance, and emotional regulation."],
        ["Aim for 8 to 10 hours of consistent, restful sleep every single night", "Maintain a regular sleep schedule: go to bed and wake up at the same time even on weekends", "Keep the bedroom dark, quiet, and cool to support natural sleep cycle transitions"],
        ["Never pull all-nighter study sessions before examinations (severely damages recall)", "Never consume heavy meals or caffeine right before sleeping"],
        "Sleeping 4 hours a night during exam week gives you more time to study and score higher.", "myth", "Sleep-deprived brains experience severe cognitive blackout, memory lapses, and panic during exams.",
        "How many hours of nightly sleep do school-age children and teenagers require for optimal brain growth?",
        ["3 hours", "8 to 10 hours of quality sleep", "14 hours", "2 hours"], 1,
        "8-10 hours enables deep REM dreaming (memory consolidation) and physical cellular repair.",
        ["It is 11 PM before an exam at {at}, and {name} is tempted to stay awake all night cramming."],
        "What scientific advice should {name} follow?",
        [("Go to sleep now to ensure at least 7-8 hours of sleep before the morning exam", "Enables hippocampal memory consolidation.", True, "sleep now|7-8 hours sleep|memory consolidation", 45),
         ("Understand that sleep deprivation causes severe brain fog and calculation errors during tests", "Debunks all-nighter cramming myths.", True, "prevent brain fog|no all-nighter|recall needs sleep", 35),
         ("Maintain consistent bedtimes to keep circadian rhythms synchronized", "Promotes deep restorative sleep.", False, "circadian rhythm|consistent bedtime", 20)],
        ["stay awake all night with coffee", "sleep 2 hours only", "cram in panic all night"],
        "Indian Society for Sleep Research (ISSR)", "https://issr.in"
    ))

    # 5. FIT-005: Screen wind-down
    cards.append(make_card(
        "FIT-005", "stride", "Sleep science", "Screen-free wind-down: Blue light and natural melatonin",
        ["junior", "middle", "senior"],
        ["Blue wavelength light from smartphones tricks the brain's pineal gland into thinking it is daytime.",
         "Using screens in bed suppresses natural melatonin secretion, delaying sleep onset by over 60 minutes."],
        ["Turn off all screens (mobiles, tablets, laptops, TV) at least 60 minutes before bedtime", "Replace late-night scrolling with calming activities: reading physical books, listening to soft music, or journaling", "Charge your mobile phone outside the bedroom or away from arm's reach of your pillow"],
        ["Never scroll through social media or play video games in the dark in bed", "Never sleep with a buzzing phone right next to your head"],
        "Using a phone in complete darkness before sleeping helps your eyes get tired and fall asleep faster.", "myth", "Intense blue light in dark bedrooms severely disrupts circadian melatonin release and strains retinas.",
        "What natural sleep hormone is suppressed when your eyes stare at bright smartphone screens before bed?",
        ["Adrenaline", "Melatonin (the sleep signal hormone)", "Insulin", "Digestive bile"], 1,
        "Melatonin prepares the body for slumber; blue screen photons completely suppress its release.",
        ["At 10 PM at {at}, {name} is lying in bed scrolling through short video reels on a smartphone in the dark."],
        "How should {name} reset their nighttime routine for deep sleep?",
        [("Put the smartphone away and switch off screens 60 minutes before sleeping", "Allows natural melatonin production to kick in.", True, "put phone away|screens off 60 mins|melatonin", 45),
         ("Engage in a calm offline wind-down: read a physical book or listen to calming music", "Lowers nervous system arousal.", True, "read physical book|offline wind down|calm", 35),
         ("Charge the phone across the room to prevent subconscious midnight scrolling", "Removes sleep disruption temptation.", False, "charge across room|no phone in bed", 20)],
        ["stare at bright reels in dark", "sleep with phone under ear", "play games till 2 am"],
        "Sleep Medicine Guidelines (AIIMS New Delhi)", "https://aiims.edu"
    ))

    # 6. FIT-006: 20-20-20 eye rule
    cards.append(make_card(
        "FIT-006", "stride", "Vision care", "Digital eye strain: The 20-20-20 rule and blinking",
        ["junior", "middle", "senior"],
        ["Staring at digital screens drops normal blinking rate by 60%, causing dry, burning eyes.",
         "The 20-20-20 rule relaxes the eye's ciliary accommodation muscles, preventing myopia progression."],
        ["Follow the 20-20-20 Rule: Every 20 minutes, look at an object 20 feet (6 meters) away for 20 seconds", "Remember to blink consciously while reading screens to spread protective tear film across eyes", "Spend at least 90 minutes outdoors in natural daylight daily (proven to slow childhood nearsightedness)"],
        ["Never read in dim lighting or with severe glare reflecting off your monitor", "Never rub itchy dry eyes with unwashed fingers"],
        "Staring continuously at a screen for 4 hours without blinking builds stronger eye muscles.", "myth", "Continuous near-focus locks ciliary muscles in spasm, triggering severe headaches and vision strain.",
        "What does the famous '20-20-20' vision rule advise during computer or phone usage?",
        ["Play 20 games in 20 minutes", "Every 20 minutes, look at an object 20 feet away for at least 20 seconds", "Blink 200 times", "Turn screen brightness to 20%"], 1,
        "Looking 20 feet away allows intraocular focusing muscles to relax to an infinite focal resting state.",
        ["Attending online classes or doing digital homework for 2 hours at {at}, {name}'s eyes feel dry and stinging."],
        "How should {name} practice the 20-20-20 rule?",
        [("Pause every 20 minutes and gaze out of the window at a distant tree (20 feet away) for 20 seconds", "Relaxes overworked ciliary eye muscles.", True, "20-20-20 rule|look 20 feet away|20 seconds|relax eyes", 45),
         ("Blink eyes completely several times to lubricate the cornea with natural tears", "Restores moisture barrier.", True, "blink consciously|lubricate eyes|moisture", 35),
         ("Ensure study room has balanced ambient lighting without harsh screen glare", "Reduces contrast strain.", False, "balanced lighting|no glare", 20)],
        ["rub eyes vigorously with dirty hands", "stare unblinking for 3 hours", "turn room lights off completely"],
        "All India Ophthalmological Society (AIOS Vision Care)", "https://aios.org"
    ))

    # 7. FIT-007: Safe stretching
    cards.append(make_card(
        "FIT-007", "stride", "Flexibility", "Safe warm-ups and stretching: Dynamic before, static after",
        ["junior", "middle", "senior"],
        ["Dynamic warm-ups (high knees, arm circles) increase core muscle temperature and synovial joint lubrication.",
         "Static stretches (holding still for 30s) are best performed after workouts during the cool-down."],
        ["Perform 5-10 minutes of dynamic warm-ups (jogging, lunges, leg swings) before playing competitive sports", "Perform gentle static stretches (hamstring stretch, quad stretch, calf stretch) after workouts", "Breathe smoothly through your nose during all stretches—never hold your breath"],
        ["Never perform aggressive, bouncy stretches on cold, un-warmed muscles (causes muscle tears)", "Never stretch to the point of sharp, stabbing joint pain"],
        "Stretching cold muscles by bouncing violently up and down is the best way to prevent sports injuries.", "myth", "Bouncing (ballistic stretching) on cold muscles triggers the stretch reflex, tearing muscle fibers.",
        "When should dynamic warm-ups (moving joints through full range) be performed?",
        ["While sleeping", "Before starting sports and workouts, to prepare muscles and joints", "Only after you shower", "Never"], 1,
        "Dynamic warm-ups prepare cardiovascular and neuromuscular pathways for exertion.",
        ["About to play a fast-paced game of football or athletics at {at}, {name} wants to sprint immediately."],
        "What safe warm-up protocol should {name} follow?",
        [("Spend 5 to 10 minutes doing dynamic warm-ups (light jogging, high knees, arm swings)", "Elevates muscle temperature and joint fluid.", True, "dynamic warm up|light jog|arm circles|prepare muscles", 45),
         ("Do not bounce aggressively into cold static stretches", "Prevents acute muscle strain.", True, "no bouncing|no aggressive stretch", 35),
         ("Perform slow, relaxing static stretches during the post-game cool-down", "Restores resting muscle length safely.", False, "cool down|static stretch after game", 20)],
        ["sprint at 100% on cold muscles", "bounce violently on toes", "skip warm up completely"],
        "Sports Authority of India (Athlete Warm-up Manual)", "https://sportsauthorityofindia.nic.in"
    ))

    # 8. FIT-008: Sports hydration
    cards.append(make_card(
        "FIT-008", "stride", "Hydration", "Sports hydration: Sipping water and beating dehydration cramps",
        ["junior", "middle", "senior"],
        ["Losing just 2% of body weight in sweat reduces athletic stamina, agility, and concentration by over 20%.",
         "Severe dehydration during sports causes painful muscle spasms and heat exhaustion."],
        ["Drink a glass of water 30 minutes before starting sports or physical training", "Take small sips of water every 15-20 minutes during play rather than gulping massive volumes all at once", "Rehydrate with water, fresh nimbu pani, or coconut water after finishing active play"],
        ["Never wait until you are severely dizzy or parched before drinking fluids", "Never substitute clean water with sugary commercial sodas during sports"],
        "Gulping down 1 litre of ice water while sprinting heavily prevents all sports tiredness.", "myth", "Gulping huge quantities causes stomach sloshing and nausea. Small, frequent sips are optimal.",
        "How often should student athletes take small sips of water during outdoor sports in warm weather?",
        ["Once every 5 hours", "Every 15 to 20 minutes during active play intervals", "Never drink during sports", "Only before bed"], 1,
        "Frequent small sips replace sweat losses continuously without overloading the stomach.",
        ["Playing an intense cricket or basketball match at {at} in hot 34°C weather, {name} begins sweating heavily."],
        "How should {name} manage hydration?",
        [("Take small, frequent sips of water during game timeouts every 15-20 minutes", "Maintains blood volume and prevents heat cramps.", True, "frequent sips|water breaks|every 15-20 mins|hydrate", 45),
         ("Avoid gulping down huge amounts of ice cold water all at once", "Prevents stomach cramps and discomfort.", True, "no gulping huge water|small sips", 35),
         ("Replenish electrolytes after the game with natural nimbu pani or coconut water", "Restores lost sodium and potassium.", False, "nimbu pani|coconut water|electrolytes", 20)],
        ["refuse water for 3 hours", "drink sugary cola during match", "wait until fainting"],
        "National Institute of Sports Medicine Guidelines", "https://sportsauthorityofindia.nic.in"
    ))

    # 9. FIT-009: Sports injuries
    cards.append(make_card(
        "FIT-009", "stride", "Injury prevention", "Listening to your body: Never playing through sharp pain",
        ["middle", "senior"],
        ["Normal exercise creates mild muscular fatigue; sharp, localized, or stabbing pain signals acute tissue damage.",
         "'Playing through the pain' transforms minor muscle strains into severe, surgery-requiring ligament tears."],
        ["Stop playing immediately if you feel a sharp twist, pop, snap, or localized joint stabbing pain", "Inform your PE coach, sports teacher, or parents honestly rather than hiding injuries", "Follow the RICE protocol (Rest, Ice, Compression, Elevation) and see a sports doctor for evaluation"],
        ["Never ignore persistent joint swelling or inability to bear weight on a limb", "Never let teammates pressure you to 'be tough and keep running' on an injured joint"],
        "True champions always ignore broken bones and sharp torn ligaments to finish the match.", "myth", "Playing on damaged ligaments causes permanent chronic joint instability and ruins athletic careers.",
        "What is the difference between healthy workout tiredness and an acute sports injury?",
        ["There is no difference", "Tiredness is general muscle fatigue; an injury is sharp, localized, stabbing pain or swelling", "Tiredness hurts joints", "Pain is always good"], 1,
        "Sharp pain is the body's mandatory emergency signal to halt movement immediately.",
        ["During a football match at {at}, {name}'s knee twists with a sharp pop and intense throbbing pain."],
        "What is the only responsible action for {name}?",
        [("Stop playing immediately and step off the field; do not bear weight on the knee", "Prevents catastrophic secondary ligament tear.", True, "stop playing|step off field|no weight on knee", 45),
         ("Inform the coach and apply a wrapped cold ice pack to reduce swelling", "Initiates prompt acute first response.", True, "inform coach|ice pack|rest", 35),
         ("Seek medical evaluation before returning to running or competitive sports", "Ensures proper diagnosis.", False, "medical evaluation|doctor check", 20)],
        ["run through the sharp pain", "let friends twist the knee to fix it", "hide injury from coach"],
        "Indian Orthopaedic Association Sports Committee", "https://ioaindia.org"
    ))

    # 10. FIT-010: Headphone volume
    cards.append(make_card(
        "FIT-010", "stride", "Hearing health", "Protecting hearing: The 60/60 rule for headphones and earbuds",
        ["junior", "middle", "senior"],
        ["Listening through in-ear earbuds at maximum volume exposes eardrums to over 100 decibels.",
         "Auditory hair cells in the cochlea cannot regenerate once destroyed by excessive acoustic pressure."],
        ["Follow the 60/60 Rule: Listen at a maximum of 60% volume for no more than 60 minutes at a time", "Choose over-ear headphones instead of in-ear earbuds that blast acoustic waves directly against eardrums", "If someone sitting an arm-length away can hear music leaking from your headphones, it is dangerously loud"],
        ["Never crank headphone volume to maximum to drown out loud bus or city street noise", "Never sleep with in-ear headphones playing music into your ears all night"],
        "If you lose some hearing from loud music, eardrum cells naturally regrow like fingernails.", "myth", "Cochlear hair cells are non-renewable; noise-induced sensorineural hearing loss is irreversible.",
        "What does the scientifically proven '60/60' hearing protection rule state?",
        ["Listen for 60 seconds", "Keep volume below 60% and limit continuous listening to 60 minutes", "Listen 60 times a day", "Buy 60 earphones"], 1,
        "The 60/60 rule maintains acoustic decibel pressure within biologically safe limits.",
        ["Listening to music or podcasts with earbuds at {at}, {name} keeps turning the volume slider to 100%."],
        "How should {name} protect their lifelong hearing?",
        [("Set the volume slider to 60% or lower and take regular listening breaks", "Prevents acoustic trauma to cochlear hair cells.", True, "60% volume|lower volume|listening breaks|60/60 rule", 45),
         ("Recognize that noise-induced hearing loss and tinnitus (ear ringing) are permanent", "Understands non-renewable nature of hearing.", True, "permanent hearing loss|tinnitus|protect eardrums", 35),
         ("Use noise-canceling headphones in noisy environments instead of blasting volume", "Allows comfortable listening at safe low volumes.", False, "over ear headphones|safe volume", 20)],
        ["blast volume at 100% all day", "sleep with earphones playing loud", "ignore ear ringing"],
        "World Health Organization Make Listening Safe Campaign", "https://who.int"
    ))

    # 11. FIT-011: Movement breaks
    cards.append(make_card(
        "FIT-011", "stride", "Sedentary breaks", "Breaking prolonged sitting: 2-minute movement snacks",
        ["junior", "middle", "senior"],
        ["Sitting still for over 60 minutes slows vascular blood circulation, lowering brain alertness.",
         "Taking a 2-minute 'movement snack' (standing, stretching, pacing) boosts focus and metabolic rate."],
        ["Stand up and stretch every 45 to 60 minutes while studying or reading", "Perform quick movement snacks: 10 jumping jacks, 5 bodyweight squats, or a brisk walk around the room", "Walk while memorizing vocabulary or pacing during phone conversations"],
        ["Never stay frozen in a chair for 4 continuous hours without standing up", "Never spend your entire school recess sitting at your desk looking at screens"],
        "Sitting completely motionless for 5 hours without moving proves superior academic dedication.", "myth", "Prolonged sitting stagnates cerebral blood flow, actually reducing memory retention and problem-solving speed.",
        "What is a 'movement snack' during study sessions?",
        ["Eating chips while sitting", "A quick 1 to 2 minute physical burst of standing, stretching, or light pacing every hour", "Running a marathon", "Sleeping"], 1,
        "Short active micro-breaks reactivate muscle pumps, circulating oxygen back to the brain.",
        ["Studying for term exams at {at}, {name} has been sitting at the desk continuously for 3 hours."],
        "How should {name} refresh their mind and body?",
        [("Stand up immediately, stretch arms overhead, and do a 2-minute movement break", "Reactivates blood circulation and breaks muscular stiffness.", True, "stand up|stretch|movement break|2 minutes", 45),
         ("Pace around the room or do 10 gentle squats to pump fresh oxygen to the brain", "Improves cognitive alertness and focus.", True, "pace room|squats|boost focus|oxygen to brain", 35),
         ("Drink a glass of water before sitting back down to resume studying", "Combines movement with hydration.", False, "drink water|resume study refreshed", 20)],
        ["sit motionless for 6 hours", "eat sugary cookies to stay awake", "slouch deeper into chair"],
        "American College of Sports Medicine (Sedentary Behavior Guidelines)", "https://acsm.org"
    ))

    # 12. FIT-012: Swimming safety
    cards.append(make_card(
        "FIT-012", "stride", "Aquatics", "Swimming pool safety: Supervision and no shallow diving",
        ["junior", "middle", "senior"],
        ["Diving headfirst into shallow water causes severe cervical spine fractures and permanent paralysis.",
         "Drowning in pools happens silently and swiftly in under 30 seconds without splashing or shouting."],
        ["Only swim in pools or beaches with certified adult lifeguards on active duty", "Always check pool water depth markings; NEVER dive headfirst into water less than 2.5 meters (8 feet) deep", "Follow pool deck rules: walk calmly without running on slippery wet tile decks"],
        ["Never push friends into swimming pools or hold someone's head underwater as a prank", "Never swim alone without adult supervision, no matter how confident a swimmer you are"],
        "Diving headfirst into the shallow 4-foot end of the pool is safe if you arch your back.", "myth", "Shallow diving is the leading cause of catastrophic sports spinal cord injuries and quadriplegia.",
        "What is the golden safety rule regarding diving headfirst into swimming pools?",
        ["Dive anywhere", "NEVER dive into shallow water; only dive in designated deep pools with certified lifeguard oversight", "Close your eyes", "Dive in darkness"], 1,
        "Shallow water diving causes the head to strike the concrete floor with catastrophic impact.",
        ["At a swimming pool party at {at}, a classmate wants to dive headfirst into the 4-foot shallow pool."],
        "What life-saving warning should {name} deliver?",
        [("Stop them immediately: 'Never dive headfirst into shallow water, it causes severe neck and spinal fractures'", "Prevents catastrophic spinal cord injury.", True, "never dive shallow|spinal fracture|no diving 4 feet", 45),
         ("Check depth markings: enter shallow water feet-first by stepping down ladders", "Ensures safe pool entry protocol.", True, "feet first|check depth markings|use ladder", 35),
         ("Remind everyone that pool pranks like pushing people in can lead to silent drowning", "Promotes pool safety discipline.", False, "no pushing pranks|swimming supervision", 20)],
        ["encourage diving in 3 feet", "push friend into pool unexpectedly", "swim alone in dark"],
        "Rashtriya Life Saving Society (RLSS India Water Safety)", "https://lifesavingindia.org"
    ))

    # 13. FIT-013: Exercising in bad air
    cards.append(make_card(
        "FIT-013", "stride", "Environmental fitness", "Exercising in polluted air: Adapting workouts when AQI is high",
        ["junior", "middle", "senior"],
        ["During heavy aerobic exercise, minute ventilation increases 10-fold, pulling pollutants deep into lung alveoli.",
         "Running outdoors on 'Severe' AQI days does more cardiovascular damage than benefits."],
        ["Check your city's daily Air Quality Index (AQI) before planning outdoor sports workouts", "If AQI exceeds 200 ('Poor' or worse), shift workouts indoors (skipping rope, yoga, bodyweight training)", "Exercise in well-ventilated indoor spaces or air-purified rooms during winter smog episodes"],
        ["Never run outdoor endurance marathons or play intense outdoor matches in heavy winter smog", "Never believe that 'tough athletes' can adapt their lungs to breathe toxic chemical smoke safely"],
        "Exercising heavily outdoors in thick toxic winter smog makes your lungs tougher and immune.", "myth", "Deep inhalation of PM2.5 in heavy smog triggers acute asthma attacks and permanent pulmonary inflammation.",
        "When the outdoor Air Quality Index (AQI) is in the 'Severe' category (300+), what should students do for fitness?",
        ["Run 10 km on highway", "Shift workouts indoors (yoga, bodyweight exercises, indoor stretches)", "Stop moving for 3 months", "Sleep all day"], 1,
        "Indoor light training maintains physical fitness while protecting delicate lung alveoli from toxic particulates.",
        ["Planning outdoor football practice at {at}, the morning air is thick with winter smog and AQI is 340."],
        "How should {name} and the team adapt?",
        [("Shift physical training indoors: do indoor stretching, bodyweight circuits, or yoga", "Avoids heavy inhalation of toxic PM2.5 smog.", True, "indoor training|yoga|bodyweight circuit|avoid smog", 45),
         ("Cancel strenuous outdoor sprinting and marathon runs during severe air pollution alerts", "Protects cardiovascular and pulmonary health.", True, "cancel outdoor sprinting|severe aqi alert", 35),
         ("Understand that fitness is about long-term health, which includes protecting lung tissue", "Embraces holistic health wisdom.", False, "protect lungs|long term health", 20)],
        ["run sprints in dense smog", "ignore burning throat", "claim air pollution is fake"],
        "Indian Journal of Medical Research (Air Pollution & Exercise)", "https://ijmr.org.in"
    ))

    # 14. FIT-014: Sportsmanship
    cards.append(make_card(
        "FIT-014", "stride", "Character", "Team sportsmanship: Celebrating effort and handling defeat gracefully",
        ["junior", "middle", "senior"],
        ["Sports build character, resilience, teamwork, and emotional regulation under pressure.",
         "Blaming teammates, arguing with referees, or throwing equipment degrades sportsmanship and team morale."],
        ["Shake hands warmly with opponents and referees after every match, win or lose", "Encourage teammates who make mistakes: 'Good try, let's win the next ball together!'", "Celebrate effort, improvement, and teamwork rather than solely obsessing over the final score"],
        ["Never throw tantrums, abuse referees, or blame individual teammates for a lost match", "Never gloat or mock defeated opponents with arrogant celebration dances"],
        "A true winner is someone who screams at their teammates whenever they make a mistake.", "myth", "True leadership is lifting up teammates who make mistakes and respecting opponents with humility.",
        "What is the mark of authentic, mature sportsmanship after losing a hard-fought championship match?",
        ["Kicking the goalpost in anger", "Shaking hands with opponents with a smile, congratulating them, and reviewing areas to improve", "Crying and insulting the referee", "Refusing to leave the pitch"], 1,
        "Gracious defeat demonstrates inner resilience, dignity, and true sporting character.",
        ["After a tense inter-school match at {at}, {name}'s team loses by one point in the final minute."],
        "How should {name} lead the team's conduct?",
        [("Lead the team to shake hands warmly with the opponents and congratulate their victory", "Exhibits dignified, gracious sportsmanship.", True, "shake hands|congratulate opponents|gracious in defeat", 45),
         ("Encourage teammates who made mistakes: 'We fought hard together, we will learn and grow'", "Maintains supportive team cohesion.", True, "encourage teammates|no blaming|learn and grow", 35),
         ("Thank the match referees and volunteers for officiating the game", "Shows respect for match officials.", False, "thank referees|respect officials", 20)],
        ["blame the goalkeeper angrily", "refuse to shake hands", "throw equipment on pitch"],
        "Ministry of Youth Affairs and Sports (Code of Sports Ethics)", "https://yas.nic.in"
    ))

    # 15. FIT-015: Belly breathing
    cards.append(make_card(
        "FIT-015", "stride", "Mind-body", "Diaphragmatic belly breathing for calm focus and stress release",
        ["junior", "middle", "senior"],
        ["Shallow chest breathing triggers the sympathetic 'fight-or-flight' stress and anxiety response.",
         "Deep diaphragmatic (belly) breathing stimulates the vagus nerve, lowering heart rate and cortisol in 60 seconds."],
        ["Practice 'Box Breathing' or 4-4-4 belly breathing: Inhale for 4 seconds, hold for 4, exhale slowly for 4", "Place one hand on your chest and one on your belly; make the belly hand rise while the chest stays still", "Use diaphragmatic breathing right before walking into an exam hall, stepping up to bat, or public speaking"],
        ["Never hyperventilate with rapid, shallow gasps when feeling nervous", "Never underestimate the immediate physical calming power of your breath"],
        "Taking deep belly breaths is just a superstitious myth that has zero medical effect on stress.", "myth", "Diaphragmatic breathing physically activates the parasympathetic nervous system, slowing heart rate and lowering blood pressure.",
        "How should your stomach move during proper calming diaphragmatic (belly) breathing?",
        ["It should suck in completely on inhale", "Your belly should gently expand outward like a balloon on inhale, and sink in on exhale", "It should not move at all", "Only shoulders should rise"], 1,
        "Expanding the belly allows the diaphragm to descend, filling the lower lung lobes with oxygen.",
        ["Feeling intense heart-pounding nervousness before a big school stage speech at {at}."],
        "How can {name} use breathwork to regain composure?",
        [("Practice slow diaphragmatic belly breathing: inhale through nose 4s, expand belly, exhale slowly 4s", "Activates parasympathetic nervous system calming.", True, "belly breathing|diaphragmatic breathing|inhale 4s|exhale slowly", 45),
         ("Feel the heart rate steady and shoulder muscles relax with each long exhalation", "Restores physiological homeostasis.", True, "heart rate steadies|relax shoulders|calm focus", 35),
         ("Remind yourself that nervousness is just energy that can be channeled into focused performance", "Positive cognitive reframing.", False, "channel energy|focus|composure", 20)],
        ["breathe in rapid panic gasps", "hold breath until dizzy", "scream in fear"],
        "All India Institute of Medical Sciences (Integrative Medicine Guidelines)", "https://aiims.edu"
    ))

    # 16. FIT-016: Active commuting
    cards.append(make_card(
        "FIT-016", "stride", "Active transit", "Active commuting: Walking and cycling to school safely",
        ["junior", "middle", "senior"],
        ["Students who walk or cycle to school demonstrate higher cardiovascular fitness and classroom attention.",
         "Active commuting builds independent road sense, reduces family fuel costs, and cuts school gate traffic jams."],
        ["Walk or cycle to school using pedestrian footpaths, designated cycle lanes, or quiet residential lanes", "Form a 'Walking School Bus' or cycle group with neighborhood classmates for mutual fun and safety", "Wear a strapped helmet when cycling and attach front/rear reflectors for early morning visibility"],
        ["Never weave in and out of heavy highway traffic on a bicycle", "Never ride a cycle with broken brakes or loose handlebars"],
        "Cycling to school is only for kids whose families cannot afford a motorcycle.", "myth", "Cycling is the premier modern global eco-friendly health habit embraced by students and leaders worldwide.",
        "What essential safety gear should you always wear when cycling to school?",
        ["Sunglasses only", "A properly fitted, securely strapped bicycle helmet and bright clothing", "Heavy boots", "Large cape"], 1,
        "A strapped bicycle helmet protects the skull and brain from traumatic impact during falls.",
        ["Living 1.5 km away from school at {at}, {name} considers cycling instead of taking a motorized auto."],
        "How can {name} make active cycling commuting safe and joyful?",
        [("Wear an ISI-approved bicycle helmet securely strapped on every single ride", "Vital protective cranial armor.", True, "wear helmet|strap helmet|cycle safety", 45),
         ("Check cycle brakes, tire pressure, and ensure front and rear reflectors are clean", "Ensures mechanical roadworthiness.", True, "check brakes|tire pressure|reflectors", 35),
         ("Ride defensively, obey traffic signals, and signal turns clearly with hand gestures", "Practices predictable road citizenship.", False, "ride defensively|hand signals|obey signals", 20)],
        ["cycle without brakes", "ride against traffic at night with no lights", "perform stunts on main road"],
        "National Urban Transport Policy Guidelines", "https://mohua.gov.in"
    ))

    # 17. FIT-017: Home fitness
    cards.append(make_card(
        "FIT-017", "stride", "Bodyweight", "Zero-equipment home fitness: Squats, push-ups and jumping jacks",
        ["junior", "middle", "senior"],
        ["Bodyweight calisthenics build functional muscular strength, tendon resilience, and joint mobility.",
         "You do NOT need expensive gym memberships, dumbbells, or machines to build a strong, capable body."],
        ["Incorporate simple bodyweight exercises: bodyweight squats, wall/knee push-ups, jumping jacks, and planks", "Focus on clean, controlled form rather than rushing through sloppy repetitions", "Create fun home fitness challenges with family: how many gentle squats or jumping jacks during commercial breaks"],
        ["Never lift heavy unmonitored weights at home without certified coach supervision", "Never sacrifice exercise posture just to show off high repetition numbers"],
        "You cannot build real physical fitness unless you buy expensive gym memberships and heavy weights.", "myth", "Calisthenics using your own bodyweight builds exceptional functional athletic strength naturally.",
        "What is the most important element when performing bodyweight exercises like squats or push-ups?",
        ["Rushing as fast as possible", "Maintaining correct, controlled form and steady breathing", "Holding your breath", "Wearing fancy shoes"], 1,
        "Proper biomechanical form protects joints and maximizes muscular benefit.",
        ["Stuck at home on a rainy day at {at}, {name} wants to do a quick 15-minute bodyweight fitness session."],
        "What balanced routine should {name} follow?",
        [("Perform a circuit of bodyweight squats, jumping jacks, knee push-ups, and a 20-second plank", "Engages all major compound muscle groups.", True, "bodyweight squats|push ups|jumping jacks|plank|calisthenics", 45),
         ("Focus on smooth, controlled form and breathe steadily without holding breath", "Protects joints and ensures muscle oxygenation.", True, "controlled form|steady breathing|proper posture", 35),
         ("Celebrate movement and strength with family for positive energy", "Promotes joyful fitness lifestyle.", False, "positive energy|joyful movement", 20)],
        ["do dangerous acrobatics on furniture", "hold breath until fainting", "give up because no gym"],
        "Fit India Movement Guidelines (Sports Authority of India)", "https://fitindia.gov.in"
    ))

    # 18. FIT-018: Rest days
    cards.append(make_card(
        "FIT-018", "stride", "Recovery", "The power of rest days: Muscle recovery and injury prevention",
        ["junior", "middle", "senior"],
        ["Muscles do NOT grow during training; exercise creates microscopic tears that rebuild stronger during rest.",
         "Overtraining without adequate recovery causes chronic fatigue, immune breakdown, and stress fractures."],
        ["Schedule at least 1 or 2 dedicated rest or light active-recovery days (gentle walks) every week", "Understand that rest, nutritious meals, and quality sleep are 50% of any athletic training equation", "Listen to persistent exhaustion signals: if feeling chronically burned out, take a restorative recovery day"],
        ["Never train at 100% maximum intensity 7 days a week with zero rest", "Never feel guilty about taking a scheduled rest day; rest is when your body grows stronger"],
        "Taking a rest day is a sign of laziness and will instantly make you lose all your fitness.", "myth", "Rest days allow glycogen replenishment and muscular tissue rebuilding; they are vital for elite performance.",
        "What happens to your muscles during rest days and deep nighttime sleep?",
        ["They disappear", "Microscopic muscle tears repair and rebuild thicker and stronger than before", "They turn to fat", "Nothing"], 1,
        "Protein synthesis and cellular tissue repair occur exclusively during periods of rest.",
        ["Training hard for athletics at {at}, {name} feels exhausted and guilty about taking a Sunday rest day."],
        "What restorative wisdom should {name} embrace?",
        [("Understand that rest days are when your body repairs muscles and rebuilds stamina", "Affirms biological necessity of recovery.", True, "rest days rebuild muscles|recovery|repairs tissue", 45),
         ("Take an active recovery day: enjoy a gentle walk, stretch, read, and sleep well", "Promotes restorative, guilt-free balance.", True, "gentle walk|sleep well|active recovery", 35),
         ("Return to training tomorrow feeling energized, refreshed, and injury-free", "Prevents chronic athletic burnout.", False, "refreshed|prevent burnout", 20)],
        ["punish body with 7-day exhaustion", "feel guilty about resting", "train through extreme fatigue"],
        "Sports Authority of India (Athlete Recovery Protocols)", "https://sportsauthorityofindia.nic.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Stride")
    return cards


def get_care_cards():
    cards = []

    # 1. HYG-001: 20-second handwashing
    cards.append(make_card(
        "HYG-001", "care", "Hand hygiene", "The 20-second handwashing technique with soap and water",
        ["junior", "middle", "senior"],
        ["Washing hands with soap for 20 seconds breaks down viral lipid envelopes and rinses off pathogenic bacteria.",
         "Soap requires friction across all surfaces (palms, back of hands, between fingers, thumbs, and fingernails)."],
        ["Wet hands with clean water, apply soap, and lather vigorously for at least 20 full seconds (hum 'Happy Birthday' twice)", "Scrub all zones: palm to palm, backs of hands, interlaced fingers, thumbs, and fingertips into palms", "Rinse thoroughly under running water and dry with a clean personal towel"],
        ["Never just splash water for 2 seconds without soap and call it 'clean'", "Never wipe clean hands on dirty pants or unwashed shirts"],
        "Splashing hands with plain tap water for 3 seconds removes all germs effectively.", "myth", "Plain water cannot break down greasy dirt or viral membranes. Soap friction for 20 seconds is essential.",
        "How long should you rub your hands with soap to ensure complete bacterial and viral removal?",
        ["2 seconds", "At least 20 continuous seconds", "10 minutes", "Half a second"], 1,
        "20 seconds of soap friction physically destroys viral membranes and lifts microbial dirt.",
        ["Before eating lunch at {at}, {name} rushes to the washroom sink to clean hands."],
        "How should {name} execute proper hand hygiene?",
        [("Apply soap and scrub vigorously for 20 seconds across palms, backs, fingers, and nails", "Covers all anatomical hand surfaces thoroughly.", True, "20 seconds|soap and water|between fingers|nails|scrub", 45),
         ("Rinse thoroughly under running water to flush away loosened dirt and microbes", "Flushes dislodged germs down the drain.", True, "rinse clean water|running water", 35),
         ("Dry hands with a clean dry towel rather than wiping on school uniform", "Prevents instant re-contamination.", False, "clean towel|dry properly", 20)],
        ["quick 2-second splash with no soap", "wipe dirty hands on pants", "eat with unwashed hands"],
        "WHO Guidelines on Hand Hygiene in Health Care and Schools", "https://who.int"
    ))

    # 2. HYG-002: Dental health
    cards.append(make_card(
        "HYG-002", "care", "Dental care", "Dental health: Brushing twice daily and tongue cleaning",
        ["junior", "middle", "senior"],
        ["Mouth bacteria feed on residual food sugars, producing lactic acid that dissolves protective tooth enamel (cavities).",
         "Brushing before bed removes overnight plaque acids when saliva flow drops during sleep."],
        ["Brush teeth twice daily: once in the morning and once at night before going to bed for 2 full minutes", "Use gentle circular strokes along the gumline with a soft-bristled toothbrush; clean tongue with a tongue cleaner", "Rinse your mouth with clean water after eating sweet, sticky, or starchy foods"],
        ["Never scrub teeth horizontally like a saw with hard bristles (erodes protective enamel and gums)", "Never go to sleep with sweet chocolate or candy coating your teeth"],
        "Brushing your teeth violently hard with a stiff brush cleans them twice as well.", "myth", "Hard brushing erodes protective tooth enamel and causes painful receding gum tissue. Use gentle circular motions.",
        "Why is brushing your teeth at night before bed even more critical than morning brushing?",
        ["Toothpaste smells nice", "Saliva production drops during sleep, allowing trapped sugar acids to destroy enamel undisturbed all night", "To look clean", "No reason"], 1,
        "Night brushing removes food substrates before nocturnal dry mouth allows bacterial acid attacks.",
        ["Getting ready for bed at {at}, {name} considers skipping nighttime tooth brushing because of tiredness."],
        "What dental habit should {name} uphold?",
        [("Spend 2 minutes gently brushing teeth with circular strokes before sleeping", "Removes sugar plaque before nighttime bacterial acid attacks.", True, "brush teeth at night|2 minutes|soft brush|circular strokes", 45),
         ("Clean the tongue gently to remove bacterial coating and freshen breath", "Reduces oral microbial load and bad breath.", True, "clean tongue|tongue scraper|rinse mouth", 35),
         ("Rinse with water and smile with clean, protected teeth", "Ensures lifelong cavity-free dentition.", False, "rinse with water|dental health", 20)],
        ["sleep with candy in mouth", "skip brushing for days", "scrub teeth violently with wire brush"],
        "Indian Dental Association (Oral Hygiene Guidelines)", "https://ida.org.in"
    ))

    # 3. HYG-003: Bathing & clean clothes
    cards.append(make_card(
        "HYG-003", "care", "Bathing", "Daily bathing, fresh undergarments and hygiene in humid weather",
        ["junior", "middle", "senior"],
        ["Warm, humid climates encourage fungal skin infections (ringworm, athlete's foot) in sweaty skin folds.",
         "Sweat itself is odorless; body odor is caused by skin bacteria fermenting apocrine sweat secretions."],
        ["Bathe daily with water and soap, paying special attention to armpits, groin, neck, and feet", "Change into clean, fresh undergarments and breathable cotton clothes every single day", "Dry skin folds thoroughly with a clean towel before putting on fresh clothes"],
        ["Never re-wear damp, sweaty unwashed undergarments or socks from yesterday", "Never leave damp towels rolled up in a dark corner (breeds mold and mildew)"],
        "Spray perfume or deodorant heavily over unwashed sweaty clothes replaces the need for a daily bath.", "myth", "Perfume mixed with stale sweat creates an intensely unpleasant odor and fails to remove skin bacteria.",
        "What type of clothing fabric is healthiest for hot, humid Indian weather?",
        ["Heavy nylon plastic", "Breathable, natural 100% cotton clothing", "Polyester leather", "Rubber suit"], 1,
        "Cotton absorbs sweat and allows cross-ventilation, preventing fungal skin infections.",
        ["After an active, sweaty sports session at {at}, {name} prepares to change clothes."],
        "What personal hygiene routine keeps skin healthy and fresh?",
        [("Take a refreshing bath with soap and water to wash away sweat and bacteria", "Cleanses skin pores and prevents fungal infections.", True, "daily bath|soap and water|wash sweat", 45),
         ("Dry skin thoroughly and change into fresh, clean cotton undergarments", "Keeps skin dry and prevents chafing.", True, "dry thoroughly|fresh undergarments|clean cotton clothes", 35),
         ("Hang up used damp clothes and towel in sunlight or airy place to dry", "Prevents bacterial and fungal growth on textiles.", False, "dry towel|air clothes|sunlight", 20)],
        ["spray deodorant over dirty sweat", "wear sweaty clothes 3 days in a row", "stay in wet gym gear"],
        "Indian Association of Dermatologists (IADVL Public Education)", "https://iadvl.org"
    ))

    # 4. HYG-004: Nail hygiene
    cards.append(make_card(
        "HYG-004", "care", "Nail care", "Nail hygiene: Trimming straight, clean fingernails and no biting",
        ["junior", "middle", "senior"],
        ["The dark crevice beneath long fingernails harbors thousands of fecal bacteria, pinworm eggs, and viruses.",
         "Biting nails transfers infectious pathogens directly into the mouth and causes painful nail bed infections (paronychia)."],
        ["Trim fingernails and toenails regularly using a clean nail clipper, cutting straight across", "Scrub gently under fingernails with soap and water while washing hands", "Keep nails neatly trimmed and smooth with an emery board or file"],
        ["Never bite or chew fingernails or peel off ragged cuticle skin with teeth", "Never share unsterilized nail clippers with people who have fungal nail infections"],
        "Biting your fingernails is a harmless nervous habit that doesn't affect your health.", "myth", "Nail biting ingests pinworm eggs, causes oral dental misalignment, and leads to severe bacterial finger infections.",
        "Why is keeping fingernails short and clean vital before eating food with your hands in India?",
        ["To look shiny", "Long nails harbor dangerous bacteria and worm eggs that contaminate food eaten with hands", "To type faster", "No reason"], 1,
        "Eating with short, clean nails prevents accidental ingestion of trapped bacterial dirt.",
        ["Examining their hands at {at}, {name} notices long fingernails with dark dirt trapped underneath."],
        "How should {name} practice proper nail hygiene?",
        [("Trim fingernails neatly using a clean nail clipper, cutting smoothly straight across", "Removes the primary trap for microbial contamination.", True, "trim nails|clean nail clipper|cut straight across", 45),
         ("Scrub gently under nails with soap and a soft brush while washing hands", "Flushes away trapped particulate dirt.", True, "wash under nails|soap|scrub clean", 35),
         ("Avoid biting nails or tearing cuticles with teeth", "Stops fecal-oral microbial transmission.", False, "stop nail biting|don'?t bite nails", 20)],
        ["bite nails with teeth", "leave black dirt under nails", "scrape nails with sharp needles"],
        "National Health Portal India (Personal Hygiene)", "https://nhp.gov.in"
    ))

    # 5. HYG-005: Cough etiquette
    cards.append(make_card(
        "HYG-005", "care", "Respiratory hygiene", "Respiratory etiquette: The elbow crook cough and tissue disposal",
        ["junior", "middle", "senior"],
        ["A single sneeze launches over 40,000 microscopic droplets at speeds up to 160 km/h.",
         "Coughing into bare palms transfers infectious viruses onto door handles, shared pencils, and bus rails."],
        ["Cough or sneeze into the crook of your elbow ('the Dracula cough') if no tissue is available", "Use a clean paper tissue to cover your nose and mouth when sneezing, and discard in a closed dustbin", "Wash hands immediately with soap and water or use sanitizer after blowing your nose"],
        ["Never cough or sneeze openly into classroom air without covering", "Never cough directly into bare palms that touch doorknobs and friends' hands"],
        "Coughing into your bare hands is the polite, standard way to cover your mouth.", "myth", "Hands touch desks, food, and doorknobs, rapidly spreading flu and colds to everyone. Cough into your elbow crook.",
        "Why is sneezing into your elbow crook vastly superior to sneezing into your bare hand?",
        ["It looks funny", "Your inner elbow rarely touches shared objects like doorknobs, stopping the spread of germs", "It catches sound", "It has no germs"], 1,
        "The elbow crook contains droplets without contaminating hands that touch shared surfaces.",
        ["In a crowded classroom at {at}, {name} feels a sudden, powerful sneeze coming on."],
        "What is the hygienic respiratory response?",
        [("Raise your inner elbow crook to cover your mouth and nose tightly as you sneeze", "Blocks respiratory droplets from contaminating hands or air.", True, "elbow crook|sneeze in elbow|cover with elbow", 45),
         ("Or use a clean paper tissue and discard it immediately into a waste bin", "Safe hygienic particulate containment.", True, "tissue|dustbin|cover nose and mouth", 35),
         ("Wash hands with soap afterwards if hands touched any nasal fluids", "Breaks transmission chains.", False, "wash hands|sanitizer", 20)],
        ["sneeze openly across the classroom", "sneeze into bare palms then touch doorknob", "wipe nose on sleeve"],
        "Ministry of Health and Family Welfare (Respiratory Hygiene)", "https://mohfw.gov.in"
    ))

    # 6. HYG-006: Head lice
    cards.append(make_card(
        "HYG-006", "care", "Hair care", "Head lice facts: Gentle treatment, no sharing combs and zero shame",
        ["junior", "middle", "senior"],
        ["Head lice are tiny wingless insects that crawl; they CANNOT jump, fly, or transmit any diseases.",
         "Lice infestation has zero connection to personal cleanliness; anyone can catch lice through direct head-to-head contact."],
        ["Tell parents calmly if your scalp feels intensely itchy, especially behind ears or at the nape of the neck", "Use a fine-toothed anti-lice comb and gentle medicated anti-lice shampoo recommended by a doctor", "Wash bedsheets, pillowcases, and hats in warm water to prevent re-infestation"],
        ["Never tease or shame a classmate who has head lice (it has nothing to do with cleanliness)", "Never share personal hair combs, brushes, caps, or helmets with others"],
        "Having head lice means a child is dirty and never washes their hair.", "myth", "Lice actually prefer clean, healthy hair. Head lice is a common, easily treatable childhood occurrence with zero shame.",
        "How do head lice actually travel from one child's hair to another?",
        ["They fly through the air", "They crawl through direct head-to-head contact or sharing personal caps and combs", "They jump 10 feet", "They swim in pools"], 1,
        "Lice have claws for crawling along hair shafts; they cannot jump or fly.",
        ["A classmate at {at} is embarrassed because their scalp is itchy and has head lice."],
        "How should {name} respond with kindness and scientific clarity?",
        [("Reassure the classmate that head lice is very common, easily treated, and NOT caused by being dirty", "Eliminates stigma and peer teasing.", True, "not dirty|very common|easily treated|no shame", 45),
         ("Advise consulting parents for a gentle medicated shampoo and fine-toothed nit comb", "Recommends safe, medically approved treatment.", True, "medicated shampoo|fine comb|tell parents", 35),
         ("Avoid head-to-head contact and do not share personal combs, caps, or hairbands", "Prevents physical transmission safely.", False, "don'?t share combs|avoid head contact", 20)],
        ["mock and bully the student", "shave student's head forcibly", "spray insect poison on head"],
        "Indian Academy of Pediatrics (Pediculosis Guidelines)", "https://iapindia.org"
    ))

    # 7. HYG-007: Washroom manners
    cards.append(make_card(
        "HYG-007", "care", "Sanitation", "School washroom etiquette: Flushing, cleanliness and washing hands",
        ["junior", "middle", "senior"],
        ["Unhygienic public washrooms spread urinary tract infections (UTIs) and gastrointestinal bugs.",
         "Leaving a washroom clean for the next user is a fundamental civic and hygienic responsibility."],
        ["Always flush the toilet completely after every use, holding the flush handle until clean water cycles", "Dispose of sanitary pads, tissues, and trash in designated dustbins, NEVER into the toilet bowl (causes choking)", "Wash hands thoroughly with soap and water after every single washroom visit"],
        ["Never stand or squat on Western ceramic toilet seats with dirty shoes (causes catastrophic toilet bowl shattering)", "Never leave toilet seats wet or un-flushed"],
        "Flushing the toilet is unnecessary if you only used it for a short time.", "myth", "Leaving unflushed waste breeds foul ammonia odors and attracts flies that transmit gastrointestinal bacteria.",
        "Where should used paper towels and sanitary pads always be disposed of in a school washroom?",
        ["Inside the toilet bowl flush", "In the dedicated covered sanitary waste dustbin", "On the floor", "Out the window"], 1,
        "Flushing pads or thick paper chokes sewer plumbing. Always use the dustbin.",
        ["Using the school or public washroom at {at}, {name} finishes and prepares to leave."],
        "What complete hygiene and civic routine should {name} execute?",
        [("Flush the toilet completely and ensure the bowl is spotless for the next person", "Fundamental sanitation etiquette.", True, "flush completely|clean toilet bowl|leave clean", 45),
         ("Dispose of all tissues or waste into the closed dustbin, not the flush", "Prevents plumbing blockage.", True, "dustbin|dispose waste in bin|no choking", 35),
         ("Wash hands thoroughly with soap and water before returning to class", "Cleanses hands of enteric pathogens.", False, "wash hands with soap|clean hands", 20)],
        ["leave unflushed toilet", "stand on western seat with muddy shoes", "flush sanitary pads down drain"],
        "Swachh Bharat Swachh Vidyalaya Guidelines", "https://dsel.education.gov.in"
    ))

    # 8. HYG-008: Sun protection
    cards.append(make_card(
        "HYG-008", "care", "Skin health", "Sun protection in tropical heat: Shade, cotton and hydration",
        ["junior", "middle", "senior"],
        ["Ultraviolet (UV) radiation is strongest between 11 AM and 3 PM, causing painful sunburns and cellular damage.",
         "Wearing wide-brim hats, sunglasses, and breathable clothing shields delicate facial skin naturally."],
        ["Seek shade under trees or covered verandahs during intense peak midday sun hours", "Wear a cap or carry an umbrella when walking outside in bright tropical sunlight", "Apply broad-spectrum sunscreen (SPF 30+) on exposed face, neck, and arms before prolonged outdoor sports"],
        ["Never stare directly at the sun (causes irreversible solar retinal burns and blindness)", "Never stay outdoors without drinking water during high UV index days"],
        "You only need sun protection on hot sunny days; cloudy days have zero harmful UV radiation.", "myth", "Up to 80% of solar UV rays penetrate cloud cover. Sun protection matters whenever the UV index is moderate to high.",
        "What is the most effective natural way to protect your face and neck from scorching afternoon sun?",
        ["Running fast", "Wearing a wide-brim hat or cap and staying in shaded areas", "Putting ice in pockets", "None"], 1,
        "Hats, umbrellas, and natural shade block direct UV photons from damaging skin tissue.",
        ["Spending sports day outdoors under bright scorching sunlight at {at}, {name}'s skin begins feeling hot and red."],
        "How should {name} protect their skin and health?",
        [("Seek shade under canopies or trees whenever not actively competing on the field", "Reduces direct solar radiation exposure.", True, "seek shade|under trees|canopy|avoid direct sun", 45),
         ("Wear a cap or hat and apply sunscreen to exposed neck and face", "Shields skin from UV sunburn.", True, "wear cap|sunscreen|hat|protect skin", 35),
         ("Drink water regularly to keep skin and body hydrated from within", "Counteracts thermal dehydration.", False, "drink water|hydrate", 20)],
        ["stare directly at sun", "stay in sun without water for 6 hours", "ignore severe sunburn"],
        "Indian Association of Dermatologists Sun Safety Guidelines", "https://iadvl.org"
    ))

    # 9. HYG-009: Ear care
    cards.append(make_card(
        "HYG-009", "care", "Ear safety", "Ear hygiene: Nothing smaller than your elbow in your ear",
        ["junior", "middle", "senior"],
        ["Earwax (cerumen) is a healthy, protective substance that traps dust, bacteria, and insects naturally.",
         "Ears are self-cleaning organs; inserting cotton buds or hairpin objects pushes wax deep against the eardrum."],
        ["Remember the golden ENT medical rule: 'Never put anything smaller than your elbow inside your ear'", "Clean only the external outer ear (pinna) with a soft towel after bathing", "Consult an ENT doctor if your ear feels blocked, painful, or has yellowish discharge"],
        ["Never insert cotton ear buds, safety pins, matchsticks, or car keys into your ear canal", "Never pour unverified warm oil or herbal concoctions into ears without medical advice"],
        "Cotton ear buds are designed to be shoved deep inside your ear canal to dig out wax.", "myth", "Cotton buds pack wax into hard impactions against the eardrum and risk perforating delicate ear membranes.",
        "What does earwax actually do inside your ear canal?",
        ["It is dirty garbage", "It is a protective natural barrier with antimicrobial properties that traps dust and insects", "It blocks sound", "It makes you sick"], 1,
        "Earwax lubricates the ear canal and possesses natural antibacterial enzymes.",
        ["After taking a bath at {at}, {name}'s friend takes a safety pin or cotton bud to dig inside their ear."],
        "What urgent ENT safety advice should {name} deliver?",
        [("Stop them immediately: 'Never insert cotton buds, pins, or keys into your ear canal'", "Prevents eardrum perforation and hearing trauma.", True, "never put buds in ear|no pins in ear|eardrum danger", 45),
         ("Explain that earwax is natural protection and the ear canal cleans itself outward automatically", "Explains self-cleaning physiological biology.", True, "ear cleans itself|earwax is protective|wax pushes outward", 35),
         ("Advise wiping only the outer ear with a clean towel and seeing a doctor if blocked", "Promotes safe external hygiene.", False, "wipe outer ear|see doctor if blocked", 20)],
        ["dig ear with hairpin", "pour hot mustard oil in ear", "push cotton bud deep inside"],
        "Association of Otolaryngologists of India (AOI Ear Care)", "https://aoi.org.in"
    ))

    # 10. HYG-010: Personal items
    cards.append(make_card(
        "HYG-010", "care", "Infection control", "Personal hygiene boundaries: Never sharing towels, bottles and razors",
        ["junior", "middle", "senior"],
        ["Damp towels and washcloths harbor fungi, staphylococcus bacteria, and scabies mites.",
         "Directly sharing drinking bottles mouth-to-mouth transmits glandular fever, throat infections, and cold sores."],
        ["Use your own personal towel, toothbrush, hairbrush, and drinking water bottle", "If sharing water with a friend, pour water into their mouth from above without touching bottle lips ('fountain drinking')", "Wash your bath towel and pillowcase weekly in warm soapy water and dry thoroughly in sunlight"],
        ["Never share toothbrushes (transmits bloodborne bacteria through micro-gum bleeds)", "Never use an unfamiliar person's shaving razor, nail clipper, or unwashed towel"],
        "Sharing your personal toothbrush with your best friend is a great sign of close friendship.", "myth", "Sharing toothbrushes transfers oral pathogens and bloodborne viruses directly into gum micro-abrasions.",
        "Why must you never share personal items like toothbrushes, razors, or wet towels?",
        ["It wastes soap", "They transfer infectious skin bacteria, bloodborne viruses, and fungal spores between bodies", "It is illegal", "No reason"], 1,
        "Personal hygiene items contact body fluids and broken skin, transferring pathogens directly.",
        ["At school or sports practice at {at}, a classmate asks to share {name}'s personal towel and drink from their bottle."],
        "How can {name} share water safely while maintaining hygiene boundaries?",
        [("Pour water from above into their mouth without letting their lips touch the bottle rim", "Prevents saliva and oral pathogen cross-contamination.", True, "pour from above|no lip contact|hygienic water sharing", 45),
         ("Politely explain that personal bath towels and toothbrushes should never be shared", "Maintains healthy personal hygiene boundaries.", True, "don'?t share towels|personal items|prevent infection", 35),
         ("Wash and sanitize your personal water bottle and towel regularly at home", "Maintains personal item cleanliness.", False, "wash bottle|clean towel", 20)],
        ["share toothbrush", "wipe face with friend's sweaty towel", "share lip balm mouth to mouth"],
        "National Health Mission (Infection Prevention Guidelines)", "https://nhm.gov.in"
    ))

    # 11. HYG-011: Mosquito defense
    cards.append(make_card(
        "HYG-011", "care", "Vector control", "Mosquito defense: Dengue, malaria and eliminating stagnant water",
        ["junior", "middle", "senior"],
        ["Aedes mosquitoes (which transmit Dengue and Chikungunya) bite primarily during early morning and late afternoon.",
         "Aedes mosquitoes breed in clean, stagnant water inside household flowerpots, air coolers, and discarded plastic cups."],
        ["Inspect and empty all stagnant water from air coolers, flowerpot saucers, and terrace tins once every week ('Dry Day')", "Wear light-colored, full-sleeve shirts and full pants when playing outdoors in the evening", "Use mosquito nets while sleeping and apply safe natural mosquito repellent lotion"],
        ["Never allow stagnant water to pool in open drums, old tires, or rooftop overhead tanks", "Never ignore high sudden fever accompanied by severe pain behind the eyes (dengue danger)"],
        "Dengue mosquitoes breed in dirty sewer gutters and only bite in the middle of midnight darkness.", "myth", "Aedes dengue mosquitoes breed in CLEAN, fresh stagnant water (coolers, flower vases) and bite during daytime hours.",
        "Where do dengue-carrying Aedes mosquitoes commonly breed in urban homes?",
        ["In hot ovens", "In clean, undisturbed stagnant water in air coolers, flowerpot saucers, and discarded coconut shells", "In dry dustbins", "In books"], 1,
        "Aedes lays eggs on the waterline of clean stagnant containers; weekly emptying stops the life cycle.",
        ["Observing home surroundings at {at}, {name} notices stagnant water sitting in flowerpot plates and an old cooler."],
        "What mosquito control action should {name} take?",
        [("Empty and scrub clean all flowerpot saucers, bird baths, and cooler trays immediately", "Destroys mosquito larvae breeding sites completely.", True, "empty stagnant water|clean cooler|dry day|flowerpot saucers", 45),
         ("Wear full-sleeve clothing and apply mosquito repellent during morning and evening hours", "Prevents daytime mosquito bites.", True, "full sleeves|repellent|prevent bites", 35),
         ("Ensure overhead water tanks are securely covered with tight-fitting lids", "Blocks mosquito entry to water reserves.", False, "cover water tanks|tight lids", 20)],
        ["leave stagnant water for months", "wear shorts in dengue outbreak", "ignore mosquito breeding"],
        "National Center for Vector Borne Diseases Control (NCVBDC)", "https://ncvbdc.mohfw.gov.in"
    ))

    # 12. HYG-012: Sick day care
    cards.append(make_card(
        "HYG-012", "care", "Illness care", "Sick day care: Resting, staying home and returning safely",
        ["junior", "middle", "senior"],
        ["Attending school with an active contagious viral fever spreads infection to dozens of classmates.",
         "Rest, hydration, and fever monitoring allow your body's immune system to clear infections efficiently."],
        ["Stay home from school if you have a fever (above 37.8°C / 100°F), vomiting, or contagious rash", "Rest in bed, drink plenty of fluids (water, soups, ORS, fresh fruit juices), and eat light meals", "Return to school only after being fever-free for at least 24 hours without taking fever-reducing medicines"],
        ["Never force yourself to attend school exams with high burning fever", "Never self-medicate with leftover prescription antibiotics for common viral colds"],
        "Going to school with high fever proves you are a heroic, dedicated student.", "myth", "Attending school while sick spreads contagion to peers, delays your own recovery, and risks medical collapse.",
        "When is it safe to return to school after recovering from a contagious fever?",
        ["While still shivering with fever", "At least 24 hours after your fever has completely resolved without fever-reducing pills", "In 10 minutes", "Never return"], 1,
        "The 24-hour fever-free milestone ensures viral shedding has dropped to safe non-contagious levels.",
        ["Waking up with high fever, sore throat, and shivering body at {at}, {name} has a school test."],
        "What is the responsible health decision?",
        [("Stay home, inform the school, and focus on rest, hydration, and medical recovery", "Protects personal health and stops schoolwide viral spread.", True, "stay home|rest in bed|inform school|hydrate", 45),
         ("Drink plenty of warm liquids, soups, and consult a doctor with parents", "Supports immune system recovery.", True, "warm liquids|soup|consult doctor", 35),
         ("Return to school only after being completely fever-free for at least 24 hours", "Safe, non-contagious return protocol.", False, "fever free 24 hours|safe return", 20)],
        ["go to school with high fever", "take random unprescribed antibiotics", "cough on classmates"],
        "Indian Academy of Pediatrics School Health Guidelines", "https://iapindia.org"
    ))

    # 13. HYG-013: Puberty basics (Class 6+, sensitive)
    cards.append(make_card(
        "HYG-013", "care", "Growing up", "Growing up: Normal physical and emotional changes of puberty",
        ["middle", "senior"],
        ["Puberty is the natural biological transition from childhood to young adulthood triggered by hormones.",
         "Everyone's puberty timeline is completely unique; starting earlier or later than peers is 100% normal."],
        ["Understand that bodily changes (growth spurts, voice deepening, body hair, sweat increase) are natural and healthy", "Maintain daily bathing, wear clean cotton clothes, and talk openly with trusted parents, doctors, or counselors", "Treat your own developing body and your classmates' changes with dignity, kindness, and zero teasing"],
        ["Never feel ashamed, scared, or embarrassed about natural biological development", "Never mock or tease classmates whose voices crack or who experience rapid growth spurts"],
        "If your voice cracks or you grow taller later than your friends, there is something medically wrong with you.", "myth", "Every human body has an individual biological clock. Puberty variation across ages 10 to 16 is entirely normal.",
        "What biological chemical messengers trigger growth spurts and body changes during puberty?",
        ["Sugar", "Natural hormones (like testosterone and estrogen) released by the endocrine system", "Vitamins only", "Bile"], 1,
        "Hormones orchestrate natural adolescent growth spurts, bone density increase, and maturity.",
        ["Experiencing sudden growth spurts, voice changes, or oily skin at {at}, {name} feels confused and self-conscious."],
        "What reassuring scientific understanding should {name} remember?",
        [("Recognize that puberty changes are natural, healthy biological milestones of growing up", "Normalizes adolescent developmental biology.", True, "natural changes|puberty is normal|healthy milestones|growing up", 45),
         ("Talk openly with trusted parents, school nurse, or counselor about any questions", "Secures supportive adult guidance.", True, "talk to parents|school nurse|counselor|ask questions", 35),
         ("Maintain daily hygiene with gentle bathing and treat developing bodies with respect", "Promotes self-care and dignity.", False, "daily hygiene|respect body", 20)],
        ["feel ashamed of body changes", "mock friends' changing voices", "hide in fear"],
        "Adolescent Health Division (Ministry of Health and Family Welfare - RKSK)", "https://nhm.gov.in"
    ))

    # 14. HYG-014: Menstrual hygiene (Class 6+, sensitive)
    cards.append(make_card(
        "HYG-014", "care", "Menstrual health", "Menstrual hygiene fundamentals: Normal biology and clean care",
        ["middle", "senior"],
        ["Menstruation is a completely natural, healthy biological process showing that the reproductive system is functional.",
         "Good menstrual hygiene prevents reproductive tract infections and enables girls to study and play with confidence."],
        ["Change sanitary pads every 4 to 6 hours (or clean menstrual cups/reusable cloth pads hygienically)", "Wrap used sanitary pads neatly in newspaper and dispose of them in a covered dustbin (NEVER flush in toilets)", "Maintain daily bathing with clean water and wear clean, dry, breathable cotton underwear"],
        ["Never flush sanitary pads down the toilet (causes catastrophic plumbing blockages)", "Never treat menstruation as 'impure', dirty, or a topic of shame or stigma"],
        "A girl on her period is impure and must sit isolated in a dark corner without touching food.", "myth", "Menstruation is a pure, clean, natural biological cycle. Ancient taboos and isolation myths have zero scientific validity.",
        "How often should a sanitary pad be changed to maintain optimal hygiene and prevent bacterial growth?",
        ["Once every 3 days", "Every 4 to 6 hours (or sooner if heavily soaked)", "Once a week", "Never change"], 1,
        "Changing pads every 4-6 hours prevents bacterial multiplication and skin rash.",
        ["A student in Class 7 at {at} experiences her period at school for the first time and feels panicked."],
        "How should {name} and friends respond with compassionate, dignified care?",
        [("Reassure her that periods are completely natural, normal, and nothing to feel scared or ashamed of", "Provides immediate emotional comfort and destigmatization.", True, "completely natural|normal biology|no shame|reassure friend", 45),
         ("Help her visit the school nurse or female teacher to obtain a clean sanitary pad", "Facilitates access to menstrual hygiene products.", True, "school nurse|clean pad|sanitary product", 35),
         ("Wrap used pads in paper and dispose of them in the covered washroom dustbin", "Ensures hygienic disposal practices.", False, "wrap in paper|dispose in dustbin", 20)],
        ["mock or tease the girl", "tell her she is impure", "flush pad in toilet"],
        "Menstrual Hygiene Scheme Guidelines (MoHFW)", "https://nhm.gov.in"
    ))

    # 15. HYG-015: Body odour
    cards.append(make_card(
        "HYG-015", "care", "Body care", "Understanding body odour: Sweat glands, daily washing and clean fabrics",
        ["middle", "senior"],
        ["During puberty, apocrine sweat glands develop in armpits and groin, producing protein-rich sweat.",
         "Bacteria naturally living on skin break down this sweat, which creates body odour (BO)."],
        ["Wash armpits and body thoroughly with soap and warm water during your daily bath", "Wear freshly washed, clean cotton clothes every day—never re-wear sweaty yesterday shirts", "Use an antiperspirant or gentle deodorant on clean, dry skin after bathing if desired"],
        ["Never mask body odour with heavy sprays of perfume instead of taking a bath", "Never shame or bully classmates about body odour; offer gentle, private advice if asked"],
        "Sweat itself smells naturally disgusting the instant it comes out of your pores.", "myth", "Fresh sweat is 100% odorless. Odour only develops hours later when surface skin bacteria ferment the sweat.",
        "What actually causes body odour in armpits during puberty?",
        ["Eating spicy chips", "Skin bacteria breaking down sweat secreted by apocrine glands", "Dirty water", "Wearing shoes"], 1,
        "Bacterial breakdown of organic sweat components produces characteristic body odor.",
        ["After gym class at {at}, {name} notices body odour and feels conscious about teammates."],
        "What is the effective, scientific personal care solution?",
        [("Take a daily bath using soap and water, washing armpits and skin folds thoroughly", "Cleanses away the bacteria that cause body odour.", True, "daily bath|soap and water|wash armpits|body hygiene", 45),
         ("Wear clean, freshly laundered cotton clothes every day", "Prevents wearing stale bacterial sweat residue.", True, "clean cotton clothes|fresh clothes|laundered shirt", 35),
         ("Use a mild deodorant on clean dry skin rather than spraying heavily over dirty sweat", "Proper post-bath application.", False, "deodorant on clean skin|gentle care", 20)],
        ["spray whole bottle perfume over sweat", "stop bathing for a week", "mock classmates"],
        "Indian Association of Dermatologists (Adolescent Skin Care)", "https://iadvl.org"
    ))

    # 16. HYG-016: Water bottles & tiffins
    cards.append(make_card(
        "HYG-016", "care", "Food containers", "Sanitizing school water bottles, straws and tiffin box gaskets",
        ["junior", "middle", "senior"],
        ["Moist rubber gaskets inside tiffin boxes and silicone bottle straws harbor invisible black mold and biofilm.",
         "Drinking from moldy water bottles causes persistent throat irritation, stomach cramps, and diarrhea."],
        ["Wash your school water bottle daily with hot water, liquid soap, and a bottle brush", "Remove rubber sealing rings and silicone straws from tiffin lids weekly to scrub away hidden black mold", "Allow water bottles and tiffins to air-dry completely upside down on a dish rack before closing lids"],
        ["Never leave water sitting in school bottles for 5 days over the weekend", "Never leave leftover food rotting inside closed tiffin boxes in your school bag"],
        "Rinsing your water bottle with plain cold water once a month is enough to keep it clean.", "myth", "Saliva backwash and moisture create thick slimy bacterial biofilms inside bottles that only soap scrubbing removes.",
        "Where does dangerous black mold secretly grow inside school tiffin boxes and sipper bottles?",
        ["On the outside sticker", "Inside the silicone rubber lid gaskets and straw crevices", "In the bag pocket", "On the spoon handle"], 1,
        "Silicone sealing gaskets trap moisture and food grease, forming toxic mold colonies if unwashed.",
        ["Opening a school water bottle at {at}, {name} notices a black slimy ring around the rubber lid gasket."],
        "How should {name} sanitize this container properly?",
        [("Remove the rubber gasket and scrub it thoroughly with hot water, soap, and an old brush", "Removes hazardous fungal mold colonies completely.", True, "remove gasket|scrub with soap|hot water|bottle brush", 45),
         ("Wash the bottle inside out with bottle brush and let it air-dry completely", "Ensures complete drying so mold cannot regrow.", True, "wash thoroughly|air dry completely|upside down", 35),
         ("Commit to washing school drinking bottles with soap daily after returning home", "Establishes daily hygiene discipline.", False, "wash daily|clean bottles", 20)],
        ["drink from moldy bottle", "scrape mold with dirty fingernail", "ignore black slime"],
        "FSSAI Clean Food and Water Storage Norms", "https://fssai.gov.in"
    ))

    # 17. HYG-017: Footwear hygiene
    cards.append(make_card(
        "HYG-017", "care", "Foot health", "Foot hygiene: Washing feet, changing socks and airing sports shoes",
        ["junior", "middle", "senior"],
        ["Feet have over 250,000 sweat glands; closed canvas school shoes create dark, warm, humid incubators.",
         "Athlete's foot is a common fungal infection causing intense itching and peeling between toes."],
        ["Wash feet thoroughly with soap and water every day, especially scrubbing between all toes", "Dry your feet completely with a towel before putting on socks and shoes (fungi love moisture)", "Wear clean, fresh cotton socks every day and air out your sports shoes in sunlight or breezy balconies"],
        ["Never wear the same sweaty, damp socks two days in a row", "Never wear damp sports shoes that have not dried out from yesterday's rain"],
        "Smelly shoes are caused by bad luck and have nothing to do with washing feet or socks.", "myth", "Smelly feet (bromodosis) are caused by bacteria fermenting trapped foot sweat in unwashed socks.",
        "What simple daily habit eliminates smelly feet and prevents athlete's foot fungus?",
        ["Wearing plastic bags", "Washing feet with soap, drying thoroughly between toes, and wearing fresh clean cotton socks daily", "Never taking shoes off", "Perfuming shoes"], 1,
        "Clean socks and dry inter-toe skin eliminate the humid breeding ground for foot bacteria and fungi.",
        ["Taking off sports shoes after school at {at}, {name}'s shoes smell intensely and toes feel damp and itchy."],
        "What foot hygiene routine restores comfort?",
        [("Wash feet immediately with soap and water, scrubbing and drying thoroughly between toes", "Eliminates odor-causing bacteria and fungi.", True, "wash feet with soap|dry between toes|clean feet", 45),
         ("Put damp socks in the laundry and wear a fresh, clean pair of cotton socks tomorrow", "Stops bacterial re-inoculation.", True, "fresh socks daily|clean cotton socks|wash socks", 35),
         ("Loosen shoelaces and leave sports shoes outside in an airy, sunny spot to dry out completely", "Solar UV and air circulation eliminate damp shoe odors.", False, "air out shoes|sunny spot|breezy balcony", 20)],
        ["wear same sweaty socks all week", "keep wet shoes inside closed cupboard", "ignore itchy toes"],
        "Indian Journal of Dermatology (Tinea Pedis Prevention)", "https://e-ijd.org"
    ))

    # 18. HYG-018: Skin care basics
    cards.append(make_card(
        "HYG-018", "care", "Skin wellness", "Teen skin care fundamentals: Gentle washing, water and no fairness fads",
        ["middle", "senior"],
        ["Adolescent hormones stimulate sebaceous glands, producing excess sebum that clogs pores into pimples (acne).",
         "Squeezing or popping pimples pushes bacteria deeper into the dermis, causing permanent pitted scars."],
        ["Wash your face twice daily with plain water or a mild, gentle soap-free cleanser", "Drink plenty of water and eat fruits and vegetables to keep skin healthy from within", "Consult a certified dermatologist if acne is painful or persistent—treatments exist!"],
        ["Never squeeze, pop, or scratch acne pimples with fingernails (leaves permanent scars)", "Never use harsh chemical fairness bleaching creams (many contain toxic steroids and mercury)"],
        "Skin fairness bleaching creams are safe everyday cosmetics that make you successful in life.", "myth", "Fairness creams often contain dangerous steroids that permanently thin skin and damage health. Embrace your natural skin tone with pride.",
        "Why must you NEVER squeeze or pop a pimple on your face?",
        ["It makes you tall", "Popping pushes infection deeper into skin tissues, leading to inflammation and permanent scarring", "It brings rain", "No reason"], 1,
        "Popping breaks the follicular wall, spreading infection and leaving permanent pitted hyperpigmentation.",
        ["Noticing a new red pimple on their forehead before school at {at}, {name} wants to squeeze and pop it."],
        "What scientific skin-care wisdom should {name} follow?",
        [("Do NOT squeeze, pick, or pop the pimple", "Prevents deep bacterial infection and permanent scarring.", True, "don'?t pop pimple|do not squeeze|leave alone", 45),
         ("Wash face gently twice daily with a mild cleanser and keep hands off your face", "Cleans excess sebum without irritating skin barrier.", True, "gentle wash|mild cleanser|hands off face", 35),
         ("Take pride in your natural skin tone and reject harmful chemical fairness creams", "Champions healthy self-acceptance and safety.", False, "reject fairness creams|natural skin tone|dermatologist", 20)],
        ["pop pimple with dirty nails", "apply chemical bleach to skin", "scrub face with sandpaper"],
        "IADVL Taskforce Against Steroid Abuse (Skin Safety)", "https://iadvl.org"
    ))

    print(f"Loaded {len(cards)} expanded cards for Care")
    return cards
