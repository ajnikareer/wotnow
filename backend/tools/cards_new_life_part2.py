"""
New Agents in the LIFE Pillar (Part 2):
- Guardian (Personal & Body Safety - SAFE) [sensitive, approve-first]
- Nyaya (Rights & Law - LAW)
"""
from cards_existing import make_card

def get_guardian_cards():
    cards = []

    # 1. SAFE-001: Safe & unsafe touch
    cards.append(make_card(
        "SAFE-001", "guardian", "Body safety", "My body belongs to me: Safe touch and the Swimsuit Rule",
        ["junior", "middle", "senior"],
        ["Your body belongs exclusively to you; nobody has the right to touch you in a way that makes you feel uneasy.",
         "The areas covered by a traditional swimsuit (chest, between legs, and bottom) are private parts."],
        ["Remember: Private parts are private; nobody should touch them except doctors or parents keeping you clean/healthy", "Say a loud, firm 'NO!' if anyone tries to touch your private parts or asks you to touch theirs", "Get away immediately and tell a trusted adult on your safety list right away"],
        ["Never keep unsafe touch a secret, even if the person tells you it's a game", "Never feel guilty or blame yourself; you did nothing wrong"],
        "If someone you know well touches you uncomfortably, you must stay quiet because they are an adult.", "myth", "Rules of safe touch apply to everyone: strangers, relatives, neighbors, and teachers alike. Speak up.",
        "What are private parts on your body according to the universal Swimsuit Rule?",
        ["Hands and elbows", "Parts covered by a swimsuit: chest, between legs, and bottom", "Ears and nose", "Knees only"], 1,
        "Swimsuit areas are strictly private. Nobody should touch them inappropriately.",
        ["At {at}, an adult makes {name} feel uneasy and uncomfortable by trying to touch under clothing."],
        "What must {name} do?",
        [("Say 'NO!' loudly and firmly and move away immediately", "Asserts clear bodily boundaries without hesitation.", True, "say no|firm no|move away|run away", 45),
         ("Go straight to a trusted adult on your safety list and tell them everything", "Breaks silence and secures immediate protection.", True, "tell trusted adult|tell parent|tell teacher|report", 40),
         ("Remember that this is NEVER your fault and you have nothing to feel ashamed of", "Affirms self-worth and removes victim-blaming.", False, "not your fault|no shame|body belongs to you", 15)],
        ["keep it a secret", "blame yourself", "stay silent in fear"],
        "POCSO Act Awareness Guidelines (NCPCR)", "https://ncpcr.gov.in"
    ))

    # 2. SAFE-002: Secrets vs surprises
    cards.append(make_card(
        "SAFE-002", "guardian", "Secrets", "Secrets vs surprises: Good surprises vs unsafe secrets",
        ["junior", "middle", "senior"],
        ["A good surprise (like a birthday gift or party) is temporary, happy, and will soon be shared openly with everyone.",
         "An unsafe secret makes you feel worried, guilty, or scared in your tummy, and someone tells you never to tell parents."],
        ["Tell a trusted adult immediately if someone says: 'Keep this a secret from your parents'", "Know the difference: Surprises bring happy smiles; unsafe secrets feel heavy and scary", "Remember: No safe adult will ever ask a child to keep secrets from their mother or father"],
        ["Never promise to keep a secret that makes you feel uneasy or uncomfortable", "Never keep a secret about someone touching you or showing inappropriate pictures"],
        "Keeping a secret that makes you feel scared is fine if an adult tells you you will get a reward.", "myth", "Adults who ask children to keep secrets from parents are crossing safety boundaries. Always tell parents.",
        "How can you tell the difference between a good surprise and an unsafe secret?",
        ["Surprises are written on paper", "Surprises are temporary, happy, and shared soon; unsafe secrets make you feel scared and tell you to hide from parents", "Secrets are always fun", "There is no difference"], 1,
        "Safe surprises end in open happy celebrations; unsafe secrets cause fear and isolation.",
        ["At {at}, an older acquaintance gives {name} an expensive gift and says: 'This is our special secret, don't tell your parents.'"],
        "How should {name} respond?",
        [("Recognize that safe adults do not ask children to keep secrets from parents", "Identifies deceptive grooming tactics.", True, "no secrets from parents|unsafe secret|grooming", 45),
         ("Tell parents or a trusted adult about the gift and the secret request immediately", "Brings transparency and adult oversight.", True, "tell parents|tell trusted adult|show gift", 40),
         ("Understand that you will not get into trouble for reporting an unsafe secret", "Relieves anxiety about speaking up.", False, "won'?t get in trouble|be honest", 15)],
        ["hide gift under bed secretly", "promise to never tell parents", "keep the secret"],
        "Childline India Foundation (Secrets & Surprises)", "https://ncpcr.gov.in"
    ))

    # 3. SAFE-003: 5 Trusted adults
    cards.append(make_card(
        "SAFE-003", "guardian", "Support network", "My 5 Trusted Adults: Building your safety circle",
        ["junior", "middle", "senior"],
        ["A 'Trusted Adult' is someone who listens carefully, believes you, respects boundaries, and takes action to protect you.",
         "Having a pre-identified list of 5 trusted adults ensures you always know whom to turn to in distress."],
        ["Identify 5 adults you feel safe with (e.g. Mother, Father, School Counselor, Grandmother, Aunt, Favorite Teacher)", "Make sure at least one of your 5 trusted adults is outside your immediate home (like a teacher or doctor)", "If the first adult on your list does not listen or seems busy, go to the second adult immediately"],
        ["Never keep worries locked inside just because one adult didn't understand the first time", "Never choose a trusted adult who makes you feel uncomfortable or tells you to hide things"],
        "If you tell one adult about a problem and they don't help, you must give up and suffer silently.", "myth", "Adults can be distracted. Keep telling the next trusted adult on your list until someone takes action.",
        "What is the most important quality of a 'Trusted Adult' on your safety list?",
        ["They give you lots of candy", "They listen without judging, believe you, make you feel safe, and help solve problems", "They have a fancy car", "They let you skip school"], 1,
        "Trusted adults provide emotional security, objective guidance, and active protection.",
        ["{name} is creating their personal 'Safety Hand' (5 Trusted Adults list) at {at}."],
        "How should {name} select their trusted adults?",
        [("Choose 5 adults who listen patiently, believe you, and respect your feelings", "Builds a reliable, empathetic safety network.", True, "listen patiently|believe you|respect feelings|trusted adult", 45),
         ("Include at least one person from school or community (like a favorite teacher or counselor)", "Ensures external support channels.", True, "include teacher|school counselor|external adult", 35),
         ("Remember to keep telling the next adult on your list until someone listens and helps", "Persistence ensures safety resolution.", False, "keep telling|next adult|don'?t give up", 20)],
        ["choose strangers online", "pick someone who tells you to keep secrets", "have zero trusted adults"],
        "Kailash Satyarthi Children's Foundation", "https://satyarthi.org.in"
    ))

    # 4. SAFE-004: Stranger at school gate
    cards.append(make_card(
        "SAFE-004", "guardian", "Strangers", "The stranger at the school gate: Lifts, candies and pets",
        ["junior", "middle", "senior"],
        ["Tricking children with puppies, candy, or claiming 'Your mother sent me to pick you up' is a classic lure.",
         "Parents will ALWAYS inform school authorities or provide the pre-agreed family Safe Word if someone else picks you up."],
        ["Step back at least 5 big steps (two arm-lengths) away from unfamiliar cars or strangers calling to you", "Say firmly: 'No thank you, I will wait with my teacher inside the school gate'", "Walk straight back into the school building and inform the security guard, principal, or teacher"],
        ["Never accept lifts, snacks, chocolates, or money from unfamiliar adults", "Never get into a car or auto with someone unless your parents personally verified it with you"],
        "If a stranger at the school gate knows your nickname, that means your parents sent them to take you home.", "myth", "Strangers can easily overhear your friends calling your name or read your school bag tag. Never go with them.",
        "An unfamiliar person in a car outside school says: 'Your mother is unwell, hop in quickly so I can take you to her.' What do you do?",
        ["Get into the car immediately", "Do NOT get in; run back inside the school gate and tell the teacher or security guard immediately", "Ask for candy", "Walk with them"], 1,
        "Never enter an unfamiliar car. Always verify through school teachers and direct phone contact with parents.",
        ["Waiting outside school at {at}, an unfamiliar adult approaches {name}: 'Your dad asked me to pick you up today, come with me.'"],
        "What is the only safe protocol for {name}?",
        [("Do NOT go with the stranger and step back away from their vehicle", "Avoids abduction and physical grab range.", True, "do not go|step back|refuse lift|stay away", 45),
         ("Ask for the pre-agreed secret family 'Safe Word' or go back inside school to verify", "Verifies parental authorization.", True, "safe word|verify with teacher|call parents", 35),
         ("Stay inside the school gate with teachers or security guards until parents arrive", "Secures safe adult custody.", False, "stay inside school|security guard|wait with teacher", 20)],
        ["get into stranger's car", "walk away with stranger", "believe them without checking"],
        "Delhi Commission for Protection of Child Rights (DCPCR)", "https://dcpcr.delhi.gov.in"
    ))

    # 5. SAFE-005: Feeling followed
    cards.append(make_card(
        "SAFE-005", "guardian", "Street awareness", "Feeling followed on the street: Crossing, shops and shouting",
        ["junior", "middle", "senior"],
        ["Walking with confident posture, head held high, and scanning surroundings discourages opportunistic stalkers.",
         "Heading into a brightly lit public shop or family-filled store instantly eliminates solitary vulnerability."],
        ["Cross the road deliberately to see if the person crosses too, confirming your suspicion", "Do not go home to an empty house; walk immediately into a busy, well-lit public store, bank, or restaurant", "Approach the shopkeeper or security guard clearly: 'I think I am being followed, please help me call my parents'"],
        ["Never walk into empty alleys, dark shortcuts, or deserted park pathways when feeling followed", "Never hesitate to shout loudly: 'STOP! Leave me alone!' if someone approaches too closely"],
        "If someone is following you, walking into a dark quiet shortcut helps you sneak away faster.", "myth", "Dark deserted alleys trap you without bystanders. Always head toward busy, well-lit crowds and shops.",
        "What should you do immediately if you realize a stranger on foot or on a scooter is following you?",
        ["Walk into a dark empty alley", "Head straight into a busy open shop, pharmacy, or bank with staff and call parents", "Look down at phone", "Stop and wait"], 1,
        "Entering a public business provides immediate adult witnesses, CCTV coverage, and telephone access.",
        ["Walking back from tuition at {at}, {name} notices an unfamiliar person matching their pace for three blocks."],
        "What proactive safety moves should {name} make?",
        [("Cross to the other side of the road to confirm if they are tracking your path", "Tests and confirms suspicious intent.", True, "cross road|check if following|confirm", 35),
         ("Walk directly into the nearest busy shop, medical store, or family restaurant", "Places yourself in a safe, populated, well-lit environment.", True, "busy shop|store|restaurant|crowd", 45),
         ("Ask the shopkeeper to help you call your parents or dial police 112", "Activates immediate community and police protection.", False, "call parents|call 112|ask shopkeeper", 20)],
        ["run into dark deserted lane", "go to empty house alone", "confront stranger alone"],
        "National Commission for Women (NCW Safety Guidelines)", "https://ncw.nic.in"
    ))

    # 6. SAFE-006: Home alone
    cards.append(make_card(
        "SAFE-006", "guardian", "Home security", "Home alone safety: Locked doors and phone rules",
        ["junior", "middle", "senior"],
        ["Doors must remain deadbolted from the inside when staying home alone.",
         "Telling callers or strangers at the door 'I am home alone' advertises vulnerability."],
        ["Keep the main entrance door and security latch firmly locked at all times", "Look through the door peephole or window before responding to any doorbell", "If a delivery or repairperson arrives, tell them through the closed door: 'My parents are busy, please leave the package outside'"],
        ["Never open the door to delivery partners, salespeople, or unfamiliar technicians when home alone", "Never tell telephone callers or post on social media: 'Home alone today!'"],
        "If a delivery person brings a parcel for your parents while you are home alone, opening the door wide is polite.", "myth", "Never open the door to anyone when home alone. Ask them to leave the parcel outside or return later.",
        "What should you say through a locked door if a delivery person knocks while you are home alone?",
        ["I am home alone, come in", "My parents are busy right now; please leave the parcel at the door or come back later", "Open door wide", "Cry loudly"], 1,
        "Saying 'parents are busy' signals adult presence in the house without opening the lock.",
        ["Staying home alone for an hour at {at}, the doorbell rings and an unfamiliar courier asks {name} to open the door."],
        "How should {name} manage this safely?",
        [("Keep the door firmly locked and do NOT open it", "Maintains impenetrable physical barrier.", True, "keep door locked|do not open|stay locked", 45),
         ("Speak through the closed door: 'My parents are busy, please leave the parcel outside'", "Gives impression of adult presence indoors.", True, "parents are busy|leave outside|come back later", 40),
         ("Call or text parents to inform them about the delivery knock", "Keeps parents informed in real time.", False, "text parents|call family", 15)],
        ["open door wide", "invite courier inside for water", "say nobody is home but me"],
        "Bureau of Police Research and Development (BPRD Home Safety)", "https://bprd.nic.in"
    ))

    # 7. SAFE-007: Safe word
    cards.append(make_card(
        "SAFE-007", "guardian", "Family security", "Family secret Safe Word: The verification code",
        ["junior", "middle", "senior"],
        ["A family 'Safe Word' is a secret code known exclusively to you and your parents.",
         "If an emergency occurs and parents must send someone else to collect you, that person MUST know the Safe Word."],
        ["Choose a fun, memorable family secret word (e.g. 'BlueMango' or 'FlyingPanda') that you never share with friends", "If an adult approaches saying 'Your parents sent me', demand: 'What is our family Safe Word?'", "If the person cannot state the exact Safe Word, refuse to move and run to school teachers or security"],
        ["Never tell your family Safe Word to classmates, neighbours, or on social media", "Never accept any explanation ('Your parents forgot to tell me the word') as an excuse"],
        "A family safe word should be an easy word like your pet's name that everyone in school knows.", "myth", "The safe word must be a private, unique family secret that no outsider could ever guess.",
        "What must an adult sent by your parents say before you agree to go with them in an emergency?",
        ["They show chocolate", "They must state your secret family 'Safe Word' accurately", "They tell a funny joke", "They promise a toy"], 1,
        "The Safe Word proves direct, verified parental authorization.",
        ["At {at}, an acquaintance approaches {name} saying: 'Your mother asked me to pick you up, hurry.'"],
        "What verification question must {name} ask?",
        [("Ask: 'What is our family secret Safe Word?'", "Tests for authentic parental authorization.", True, "safe word|what is the safe word|secret code", 45),
         ("If they do not know the exact word, refuse to go and step away immediately", "Decisive boundary enforcement.", True, "refuse to go|step away|do not leave", 40),
         ("Notify school authorities or call parents directly to verify", "Confirms emergency status.", False, "call parents|verify with school", 15)],
        ["go with them without checking", "tell them the safe word yourself", "hop in car"],
        "National Center for Missing and Exploited Children Safety Rules", "https://missingkids.org"
    ))

    # 8. SAFE-008: Lost in crowd
    cards.append(make_card(
        "SAFE-008", "guardian", "Crowds", "Lost in a crowded market or festival: Safe helpers",
        ["junior", "middle", "senior"],
        ["Crowded fairs, railway stations, and melas can separate children from parents in seconds.",
         "Wandering around searching in panic increases distance; finding designated uniform helpers is safest."],
        ["Stop walking immediately—stay near where you last saw family ('Freeze and stay in a safe spot')", "Look for Safe Helpers: police officers, railway ticket examiners, security guards, or a mother with children", "Recite your parents' mobile phone numbers clearly to the official helper and ask them to announce over public loudspeakers"],
        ["Never leave the building or festival ground with a stranger who offers to 'drive you home'", "Never hide in dark corners or panic and wander into busy road traffic"],
        "If you get lost in a massive crowd, running around searching every stall is the best way to find parents.", "myth", "Running makes you miss each other. Stay in one open, safe spot and approach a uniformed helper.",
        "Who is the safest person to approach for help if you get lost in a shopping mall or crowded festival?",
        ["A stranger sitting in a car outside", "A uniformed security guard, information desk executive, or a police officer", "Someone hiding in an alley", "Nobody"], 1,
        "Uniformed personnel and customer help desks have public address loudspeaker systems to page parents.",
        ["In a bustling festival fair at {at}, {name} turns around and realizes parents are nowhere in sight."],
        "What should {name} do?",
        [("Stop wandering and look for a uniformed police officer, security guard, or information counter", "Connects to official public assistance.", True, "uniformed police|security guard|information desk|safe helper", 45),
         ("Provide parents' memorized mobile phone numbers clearly to the official helper", "Enables direct phone contact with family.", True, "phone number|call parents|contact details", 40),
         ("Do not leave the festival venue with any stranger offering a private lift", "Prevents abduction outside secured zone.", False, "do not leave with stranger|stay in venue", 15)],
        ["leave festival ground alone", "accept lift from stranger", "hide in dark alley and cry"],
        "National Commission for Protection of Child Rights (NCPCR)", "https://ncpcr.gov.in"
    ))

    # 9. SAFE-009: Online grooming
    cards.append(make_card(
        "SAFE-009", "guardian", "Online safety", "Spotting online grooming: Flattery, gifts and secrecy",
        ["middle", "senior"],
        ["Online predators spend weeks building trust through excessive flattery, gaming gifts, and shared 'secrets'.",
         "Grooming follows a pattern: isolating the young person from parents, requesting photos, and shifting to private apps."],
        ["Be on high alert if an online acquaintance showers you with gaming gifts (Robux, skins) or says: 'Only I understand you'", "Recognize the red flag when an online friend insists: 'Don't tell your parents we chat' or asks to move to Snapchat/Discord DMs", "Take screenshots, block the user, and show the conversation to a trusted adult immediately"],
        ["Never send private photos, video call strangers without clothing, or reveal personal school locations", "Never agree to meet an online-only acquaintance in person in the physical world"],
        "An online friend from an overseas gaming group who sends you gifts and asks for personal photos is just being friendly.", "myth", "Requesting personal photos or asking children to hide chats from parents is textbook predatory grooming.",
        "What is a major red-flag sign of online grooming in gaming and social media chats?",
        ["Sharing game strategies", "Asking you to keep your chats a secret from parents and asking for private photos", "Congratulating on a win", "Playing a match"], 1,
        "Demands for secrecy and requests for personal photos indicate malicious predatory behavior.",
        ["An older gamer in an online community at {at} sends {name} gifts and texts: 'You are so special, don't tell your parents we chat, send me a private photo.'"],
        "What is the urgent safety response for {name}?",
        [("Recognize this immediately as predatory online grooming and do NOT send any photos", "Identifies dangerous grooming pattern.", True, "grooming|red flag|do not send photos|predatory", 45),
         ("Block the user immediately and preserve screenshots of the messages", "Captures forensic evidence while cutting contact.", True, "block user|screenshot messages|cut contact", 40),
         ("Show the conversation to parents or report on Childline 1098 / cybercrime portal", "Activates protective adult intervention.", False, "tell parents|call 1098|cybercrime report", 15)],
        ["send private photos secretly", "keep chat secret from parents", "agree to meet in person alone"],
        "CERT-In Child Online Safety Advisory", "https://cert-in.org.in"
    ))

    # 10. SAFE-010: Uncomfortable comments
    cards.append(make_card(
        "SAFE-010", "guardian", "Boundaries", "Handling uncomfortable comments: Saying NO and telling",
        ["junior", "middle", "senior"],
        ["You have the constitutional and moral right to bodily integrity, personal dignity, and emotional respect.",
         "Uncomfortable comments about your body or personal space from anyone (peers or adults) are unacceptable."],
        ["Use a firm, loud voice with eye contact: 'Stop! I do not like that comment, do not say that to me'", "Walk away with your head held high to a populated, safe area", "Report the incident to a parent, teacher, or trusted adult: remember that telling is NOT 'snitching'"],
        ["Never laugh along or smile nervously when someone makes an inappropriate comment about your body", "Never keep uncomfortable encounters bottled up inside"],
        "If an adult makes an uncomfortable remark about your body, you must smile and stay quiet to be polite.", "myth", "Politeness never requires tolerating boundary violations. You have the right to assert boundaries firmly.",
        "What is the difference between 'snitching' and 'reporting' an uncomfortable safety incident?",
        ["They are the same", "Snitching is trying to get someone in petty trouble; reporting is protecting yourself or others from harm", "Reporting is bad", "None"], 1,
        "Reporting safety violations is an act of courage that protects the entire community.",
        ["At {at}, an older person makes an inappropriate, creepy comment about {name}'s appearance that feels deeply wrong."],
        "How should {name} react?",
        [("Say firmly: 'Stop, do not speak to me like that' and walk away immediately", "Sets clear assertive personal boundary.", True, "say stop|firm boundary|walk away|don'?t speak like that", 45),
         ("Tell a trusted adult, parent, or school counselor what happened right away", "Secures supportive adult intervention.", True, "tell trusted adult|tell parent|counselor|report", 40),
         ("Understand that you have the right to feel safe and respected at all times", "Validates emotional boundary rights.", False, "right to respect|feel safe|not your fault", 15)],
        ["smile and pretend it's fine", "stay silent and cry in room", "blame your clothing"],
        "National Commission for Protection of Child Rights", "https://ncpcr.gov.in"
    ))

    # 11. SAFE-011: School bullying
    cards.append(make_card(
        "SAFE-011", "guardian", "Anti-bullying", "Dealing with school bullying: Adults have a duty to act",
        ["junior", "middle", "senior"],
        ["Bullying is repetitive, aggressive behavior involving an imbalance of power (physical, verbal, or social).",
         "Under CBSE and state school education rules, schools are legally mandated to have Anti-Bullying Committees."],
        ["Tell the bully firmly once: 'Stop, leave me alone' in a calm, confident voice, then walk away", "Report every bullying incident to your class teacher, principal, school counselor, or parents with specific dates", "Stay in groups of friendly classmates during recess, corridors, and bus rides (bullies target isolated students)"],
        ["Never believe the cruel insults bullies say about you (bullying reflects the bully's insecurity, not your worth)", "Never resort to dangerous physical violence that can get you hurt or suspended"],
        "Being bullied in school is just a normal character-building ritual that every student must endure quietly.", "myth", "Bullying causes severe psychological trauma and is strictly illegal under school safety regulations.",
        "Under CBSE guidelines, what committee must every school maintain to protect students from harassment?",
        ["Sports team", "Anti-Bullying and Child Protection Committee", "Canteen committee", "Debate club"], 1,
        "Schools are legally required to maintain anti-bullying committees to resolve harassment complaints.",
        ["A group of students at {at} repeatedly pushes, insults, and steals {name}'s lunchbox during recess."],
        "What is the constructive, empowered response for {name}?",
        [("Report the repeated bullying formally to the class teacher, school counselor, or principal", "Activates school disciplinary protection mechanisms.", True, "tell teacher|counselor|report bullying|principal", 45),
         ("Confide in parents so they can write an official note to the school administration", "Secures family backing and formal institutional records.", True, "tell parents|official note|family support", 35),
         ("Remember that you are worthy, valued, and bullying is NEVER your fault", "Protects mental resilience and self-esteem.", False, "not your fault|valued|worthy", 20)],
        ["suffer silently every day", "skip school permanently", "bring weapons to school"],
        "CBSE School Safety and Anti-Bullying Directives", "https://cbse.gov.in"
    ))

    # 12. SAFE-012: Isolated spaces
    cards.append(make_card(
        "SAFE-012", "guardian", "Environment safety", "Avoiding unsafe isolated spots: Stairwells, basements and abandoned areas",
        ["junior", "middle", "senior"],
        ["Over 80% of peer bullying and predatory harassment occurs in unmonitored, isolated 'blind spots'.",
         "Empty basements, deserted terraces, and isolated washrooms lack adult oversight and CCTV coverage."],
        ["Always use buddy pairs: take a trusted classmate along when visiting distant school washrooms or supply rooms", "Stick to well-lit, populated corridors and active campus areas during recess and after-school hours", "If you must walk through a quiet stairwell, walk purposefully with head up and stay observant"],
        ["Never hang out in dark, deserted school basements, abandoned sports sheds, or rooftop terraces", "Never agree to follow an acquaintance into an empty, isolated room to 'see a secret'"],
        "Hanging out in dark abandoned campus buildings alone is completely safe if you are brave.", "myth", "Isolated unmonitored zones lack emergency exits, witnesses, and immediate adult assistance.",
        "What is the 'Buddy System' rule for visiting distant school areas like sports sheds or quiet washrooms?",
        ["Go alone in dark", "Always take a trusted friend along so you are never isolated in unmonitored spaces", "Hide in closets", "Never wash hands"], 1,
        "The buddy system ensures mutual safety, immediate assistance, and deterrence against harassment.",
        ["During free period at {at}, an older student invites {name} to an empty, deserted basement storeroom."],
        "How should {name} respond?",
        [("Politely refuse to enter isolated unmonitored areas and stay in public corridors", "Eliminates situational vulnerability.", True, "refuse|stay in public|avoid isolated basement|stay in light", 45),
         ("Recognize that isolated unmonitored spaces represent common safety risk zones", "Understands environmental crime prevention.", True, "isolated spaces|safety risk|stay near people", 35),
         ("Use the buddy system and stick to active, populated areas of the campus", "Practices peer safety habits.", False, "buddy system|populated areas", 20)],
        ["follow into dark basement alone", "hide in deserted shed", "ignore intuitive warning feelings"],
        "National Institute of Public Cooperation and Child Development (NIPCCD)", "https://nipccd.nic.in"
    ))

    # 13. SAFE-013: Saying NO to familiar adults
    cards.append(make_card(
        "SAFE-013", "guardian", "Autonomy", "Saying NO to familiar adults: Bodily autonomy and consent",
        ["junior", "middle", "senior"],
        ["Most child boundary violations are committed by people known to the child (relatives, tutors, neighbors).",
         "Children are never obligated to endure uncomfortable physical affection (forced hugs, tickling, sitting on laps)."],
        ["Understand that respect does not require surrendering your bodily comfort: a warm 'Namaste' or handshake is completely polite", "Say firmly: 'I prefer not to hug right now, namaste!' if forced into uncomfortable physical contact", "Tell your parents if a relative, neighbor, or tutor touches you in a way that feels awkward or wrong"],
        ["Never force yourself to sit on an adult's lap if it makes you feel uneasy", "Never believe an adult who says: 'If you loved your uncle/tutor, you would let me touch you'"],
        "Children must always allow relatives and family friends to kiss and hug them even if they feel uncomfortable.", "myth", "Bodily autonomy begins in childhood. You have the total right to choose respectful non-physical greetings.",
        "What is a polite, culturally respectful alternative to an uncomfortable hug from a visiting relative?",
        ["Running away screaming", "A warm smile, folded hands 'Namaste', or a polite handshake", "Insulting them loudly", "Pinching them"], 1,
        "Namaste is an ancient, respectful Indian greeting that maintains healthy physical boundaries.",
        ["At a family gathering at {at}, an adult relative insists {name} sit on their lap, which makes {name} feel uneasy."],
        "How can {name} uphold their bodily boundaries respectfully?",
        [("Step back politely and say: 'I prefer to sit on this chair, namaste Uncle'", "Asserts bodily comfort with poise and respect.", True, "sit on chair|prefer not to|namaste|step back", 45),
         ("Remember that you have the complete right to decide who touches your body", "Reinforces core bodily autonomy.", True, "bodily autonomy|right to choose|my body", 35),
         ("Tell your parents privately if any relative's behavior continues to feel uncomfortable", "Brings parental protection.", False, "tell parents privately|report discomfort", 20)],
        ["endure uncomfortable touch in silence", "blame yourself for feeling uneasy", "let boundaries be violated"],
        "Ministry of Women and Child Development Guidelines", "https://wcd.nic.in"
    ))

    # 14. SAFE-014: Memorizing emergency info
    cards.append(make_card(
        "SAFE-014", "guardian", "Emergency data", "Memorizing vital safety info: Phone numbers and home address",
        ["junior", "middle", "senior"],
        ["Smartphones run out of battery, get lost, or break during real-world crises.",
         "A child who has memorized two parental phone numbers can be safely reunited within 15 minutes."],
        ["Memorize your mother's and father's 10-digit mobile phone numbers by heart through daily rhythm practice", "Know your full home address clearly: Flat/House number, building name, road, colony, and city", "Know your school's full name and your blood group if possible"],
        ["Never rely 100% on phone contacts list without knowing numbers in your head", "Never write your phone number and home address in large visible letters on the outside of your backpack"],
        "Memorizing phone numbers is obsolete in the 21st century because smartphones store everything.", "myth", "If your phone battery dies or is lost, you are helpless unless parent numbers are memorized in your mind.",
        "What two pieces of personal information should every student know by heart from memory?",
        ["Their high score in video games", "At least two parental 10-digit phone numbers and their full home address", "The names of 50 actors", "WiFi passwords"], 1,
        "Parent phone numbers and home address are foundational life-saving safety coordinates.",
        ["During a school trip at {at}, {name}'s mobile phone battery dies completely and {name} gets separated."],
        "How does {name}'s mental preparation save the day?",
        [("Recite mother's or father's 10-digit mobile number from memory to the police or station master", "Enables instant direct telephone reconnection.", True, "recite phone number|memorized number|call mother|call father", 45),
         ("State full home address, colony, and school name clearly", "Provides complete geographical identification.", True, "full address|colony name|school name", 35),
         ("Approach a uniformed officer or customer help desk calmly", "Secures official safe transit.", False, "uniformed officer|help desk|stay calm", 20)],
        ["panic because phone battery is dead", "give up and wander into streets", "follow strangers"],
        "National Commission for Protection of Child Rights Guidelines", "https://ncpcr.gov.in"
    ))

    # 15. SAFE-015: 1098 & 112 Helplines
    cards.append(make_card(
        "SAFE-015", "guardian", "Helplines", "Emergency helplines: Child Helpline 1098 and Police 112",
        ["junior", "middle", "senior"],
        ["1098 is India's 24/7, free, emergency phone outreach service for children in need of care and protection.",
         "Calls to 1098 and 112 can be made from ANY landline or mobile phone even with zero balance and no SIM."],
        ["Dial 1098 if you or another child is facing abuse, child labor, child marriage, or extreme distress", "Dial 112 for immediate all-in-one emergency response (Police, Fire, and Ambulance)", "Speak clearly and state your city, location, and what emergency help you need"],
        ["Never make prank or prank joke calls to 1098 or 112 (it blocks lines for children in real danger)", "Never fear that calling 1098 will get you into trouble; it is a safe child-friendly service"],
        "You need a mobile recharge and positive balance to call emergency helplines like 112 or 1098.", "myth", "Emergency calls to 112 and 1098 are legally mandated to connect free of cost from all telecom networks.",
        "What is the official nationwide emergency helpline number dedicated exclusively to children in India?",
        ["100", "1098 (Childline)", "101", "108"], 1,
        "1098 operates 24/7 across India under the Ministry of Women and Child Development.",
        ["A student at {at} learns that a classmate is being subjected to severe physical harm and needs help."],
        "What confidential emergency action can be taken?",
        [("Call Child Helpline 1098 or Police 112 to report the situation safely", "Triggers professional child protection rescue.", True, "call 1098|childline|dial 112|report distress", 45),
         ("Provide the location, school, or residential details clearly to the counselor", "Enables Child Welfare Committee (CWC) outreach.", True, "provide location|details|counselor|clear report", 35),
         ("Understand that calls to 1098 are confidential, free, and protected by law", "Removes fear of retribution.", False, "confidential|free call|protected", 20)],
        ["make prank calls to 1098", "ignore child in danger", "post on social media without reporting"],
        "Ministry of Women and Child Development (Childline 1098)", "https://wcd.nic.in"
    ))

    # 16. SAFE-016: Helping a friend
    cards.append(make_card(
        "SAFE-016", "guardian", "Peer support", "Supporting a friend who confides in you about an unsafe situation",
        ["junior", "middle", "senior"],
        ["Children experiencing abuse or boundary violations often confide in a best friend before any adult.",
         "A supportive peer listens without judgment, validates their pain, and helps connect them to safe adults."],
        ["Listen calmly, believe them completely, and say: 'Thank you for telling me, I believe you, it is not your fault'", "Gently explain: 'I care about your safety too much to keep this secret. Let's talk to our school counselor together'", "Go with them to hold their hand while speaking to a trusted teacher or parent"],
        ["Never promise to keep a secret that involves someone hurting your friend or them hurting themselves", "Never judge, mock, or share your friend's sensitive secret with other classmates as gossip"],
        "If a friend tells you someone is hurting them at home, keeping their secret forever is true friendship loyalty.", "myth", "True friendship protects lives. Harm and abuse must never be kept secret. Tell a trusted adult.",
        "What is the most supportive thing to say when a friend confides that someone touched them inappropriately?",
        ["Why didn't you stop them?", "I believe you, it is NOT your fault, and I am here to help you get safe adult support", "You must have done something wrong", "Tell everyone in school"], 1,
        "Believing the victim and affirming zero blame relieves guilt and enables healing.",
        ["During lunch break at {at}, a close classmate breaks down in tears and confides about an unsafe touch incident."],
        "How should {name} support their friend?",
        [("Listen with deep empathy, believe them completely, and reassure: 'It is not your fault'", "Provides essential emotional safety.", True, "i believe you|not your fault|listen with empathy", 45),
         ("Encourage and accompany them to speak with the school counselor or trusted teacher", "Bridges the child to professional protection.", True, "school counselor|trusted teacher|tell together|support", 40),
         ("Do not gossip or spread their confidential story across class group chats", "Maintains sacred personal confidentiality.", False, "no gossip|confidential|respect privacy", 15)],
        ["blame the friend", "spread rumor on whatsapp", "promise to keep abuse a secret forever"],
        "NCPCR Guidelines on Peer Support in Child Protection", "https://ncpcr.gov.in"
    ))

    # 17. SAFE-017: Cab & Auto travel
    cards.append(make_card(
        "SAFE-017", "guardian", "Transit safety", "Safe travel in cabs and autos: Live location and safety checks",
        ["middle", "senior"],
        ["Traveling independently in app-based cabs or auto-rickshaws requires simple routine verification habits.",
         "Live location sharing allows parents to track your vehicle's GPS route in real time on a digital map."],
        ["Verify the vehicle license plate, driver name, and car model against your app booking screen before getting in", "Share your trip live location with your parents on WhatsApp or through the cab app's safety feature", "Check that the rear interior door child-lock is not engaged, so you can open the door from the inside anytime"],
        ["Never board a cab or auto if the driver has an unauthorized stranger sitting in the front passenger seat", "Never get into a cab whose license plate does not match the app details"],
        "It is rude to check the license plate number of a taxi before getting inside.", "myth", "Verifying license plates against your booking screen is a basic, universal personal safety rule.",
        "What safety feature on your smartphone should you activate when traveling alone in an auto or cab?",
        ["Play loud games", "Share your 'Live Location' with your parents on WhatsApp or through the transit app", "Turn on airplane mode", "Turn off GPS"], 1,
        "Live location sharing gives parents real-time GPS tracking of your vehicle's speed and route.",
        ["{name} needs to take an auto-rickshaw or app cab home from tuition at {at}."],
        "What safety routine should {name} follow?",
        [("Verify the vehicle license plate number against the booking screen before boarding", "Guarantees you enter the authorized vehicle.", True, "check number plate|verify driver|license plate", 40),
         ("Share live trip location on WhatsApp with parents immediately upon starting the ride", "Enables real-time parental journey tracking.", True, "share live location|parents track|whatsapp location", 40),
         ("Sit directly behind the driver (not in front) and ensure you can open the door from inside", "Maintains strategic exit capability.", False, "sit behind driver|check door opens", 20)],
        ["board vehicle with wrong number plate", "turn off phone GPS", "accept ride with stranger in passenger seat"],
        "MoRTH Guidelines for Passenger Safety in Commercial Transport", "https://morth.nic.in"
    ))

    # 18. SAFE-018: Trusting gut feeling
    cards.append(make_card(
        "SAFE-018", "guardian", "Intuition", "Trusting your gut feeling: That uneasy knot in your stomach",
        ["junior", "middle", "senior"],
        ["Your brain processes millions of subconscious sensory cues (body language, tone, micro-expressions) instantly.",
         "An unexplained feeling of dread, goosebumps, or an uneasy knot in your stomach is your internal alarm bell."],
        ["Trust your instincts: If a person, place, or situation feels 'weird' or 'wrong', treat it as a valid danger signal", "You do not need to justify or explain why you feel unsafe before removing yourself from a situation", "Make an excuse ('My mom is calling me right now') and leave the room or area immediately"],
        ["Never ignore an intuitive warning feeling just to appear 'polite' or 'cool'", "Never stay in a situation that makes your tummy turn just because everyone else is staying"],
        "A gut feeling of uneasiness is just silly childish imagination that should be ignored.", "myth", "Intuition is your brain's evolved survival radar detecting subtle danger cues. Always honor your instincts.",
        "What should you do if an unfamiliar situation or person gives you an intense uneasy feeling in your stomach?",
        ["Force yourself to stay and laugh", "Trust your gut instinct, create an excuse, and leave for a safe place immediately", "Ignore the feeling", "Close your eyes"], 1,
        "Honoring your intuition keeps you steps ahead of danger before a threat escalates.",
        ["Visiting an acquaintance's home or gathering at {at}, {name} gets an intense uneasy 'gut feeling' that something is off."],
        "How should {name} honor their internal alarm?",
        [("Trust the uneasy instinct and prioritize personal safety without worrying about being polite", "Validates subconscious biological radar.", True, "trust gut feeling|instincts|prioritize safety", 45),
         ("Make a calm, quick exit excuse ('I must head home now, my parent is waiting') and leave", "Facilitates safe, non-confrontational departure.", True, "make excuse and leave|exit immediately|walk away", 35),
         ("Rejoin trusted friends or parents in a well-lit, populated environment", "Restores physical safety.", False, "rejoin parents|safe environment", 20)],
        ["ignore gut feeling to look cool", "stay in uncomfortable room", "tell yourself you are silly"],
        "Child Protection Guidelines on Situational Awareness", "https://ncpcr.gov.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Guardian")
    return cards


def get_nyaya_cards():
    cards = []

    # 1. LAW-001: RTE Act
    cards.append(make_card(
        "LAW-001", "nyaya", "Education rights", "Right to Education (RTE Act): Free, compulsory schooling (Ages 6-14)",
        ["junior", "middle", "senior"],
        ["Article 21A of the Indian Constitution makes free and compulsory education a Fundamental Right.",
         "Under the RTE Act 2009, schools cannot deny admission, charge capitation fees, or expel kids aged 6-14."],
        ["Know that every child in India aged 6 to 14 has the legal constitutional right to attend school", "Under Section 12(1)(c), private unassisted schools must reserve 25% of entry-level seats for disadvantaged children", "Physical punishment, mental harassment, and screening interviews of children are strictly illegal"],
        ["Never believe that children from poor families have no legal right to go to school", "Never tolerate corporal punishment (beating, canning) in classrooms"],
        "Private schools can legally beat students with sticks for not doing homework.", "myth", "Corporal punishment is strictly illegal under Section 17 of the RTE Act and punishable by law.",
        "Under Article 21A of the Indian Constitution, education is a fundamental right for which age group?",
        ["Only college students", "Children between the ages of 6 and 14 years", "Only age 18+", "Adults only"], 1,
        "The 86th Constitutional Amendment guarantees free, compulsory education for children aged 6 to 14.",
        ["In a neighborhood at {at}, a 10-year-old child is forced to work in a garage instead of going to school."],
        "What legal constitutional right protects this child?",
        [("The Right to Education (RTE) Act guarantees free, compulsory schooling for ages 6 to 14", "Constitutional fundamental entitlement under Article 21A.", True, "right to education|rte act|article 21a|free schooling", 45),
         ("Corporal punishment and denying school admission are illegal offenses under Indian law", "Affirms legal ban on child deprivation.", True, "illegal to deny schooling|no child labor|punishable", 35),
         ("Report child educational deprivation to local education officers or Childline 1098", "Activates legal remediation channels.", False, "call 1098|report to education department", 20)],
        ["say schooling is only for rich kids", "support child working in garage", "ignore fundamental rights"],
        "Right to Education Act 2009 (Ministry of Education)", "https://dsel.education.gov.in"
    ))

    # 2. LAW-002: Child labour
    cards.append(make_card(
        "LAW-002", "nyaya", "Child protection", "Child Labour Prohibition Act: Why it is illegal and how to report",
        ["junior", "middle", "senior"],
        ["The Child Labour (Prohibition and Regulation) Amendment Act bans employment of children under 14 in all occupations.",
         "Employing adolescents (aged 14-18) in hazardous occupations (mines, chemical factories, fireworks) is a serious crime."],
        ["Recognize that employing children under 14 in roadside dhabas, tea stalls, or homes is illegal", "Understand that child labour deprives young people of their childhood, health, and constitutional education", "Report child labour confidentially by calling Childline 1098 or using the PENCiL portal (pencil.gov.in)"],
        ["Never employ child domestic helpers at home or patronize businesses that exploit young kids", "Never ignore young children working in brick kilns, fireworks factories, or hotels"],
        "Hiring a 12-year-old child to wash dishes at a roadside tea stall is completely legal in India.", "myth", "Employing any child under 14 years in commercial work is a criminal offense punishable with jail time.",
        "What official government web portal enables citizens to report child labour violations across India?",
        ["Amazon", "PENCiL Portal (Platform for Effective Enforcement for No Child Labour)", "Twitter", "Cricket board"], 1,
        "The PENCiL portal integrates central and district task forces to rescue and rehabilitate child labourers.",
        ["At an eatery at {at}, {name} sees an 11-year-old child working long hours cleaning tables instead of attending school."],
        "What is the responsible legal civic response?",
        [("Recognize that employing children under 14 is a criminal offense under the Child Labour Act", "Understands statutory labor prohibition.", True, "child labour act|illegal under 14|criminal offense", 45),
         ("Report the violation confidentially to Child Helpline 1098 or on pencil.gov.in", "Initiates child rescue and rehabilitation.", True, "call 1098|pencil portal|report confidentially", 35),
         ("Advocate that every child belongs in a school classroom, not behind a commercial dishwashing sink", "Affirms dignity and educational equity.", False, "belongs in school|rehabilitation", 20)],
        ["hire child to wash car", "ignore child exploitation", "scold the working child"],
        "Ministry of Labour and Employment (PENCiL Portal)", "https://pencil.gov.in"
    ))

    # 3. LAW-003: Consumer rights
    cards.append(make_card(
        "LAW-003", "nyaya", "Consumer rights", "Consumer Protection Act: Maximum Retail Price (MRP) and bills",
        ["middle", "senior"],
        ["Under the Consumer Protection Act 2019, charging even 1 rupee above the printed MRP is strictly illegal.",
         "Consumers have the legal right to receive a proper bill/cash memo for every commercial transaction."],
        ["Always check the printed Maximum Retail Price (MRP) inclusive of all taxes before paying", "Demand a tax invoice or cash memo; without a bill, you cannot claim warranty or file consumer court complaints", "File consumer complaints against overcharging or defective goods on the National Consumer Helpline (1915)"],
        ["Never pay 'refrigerator cooling charges' or extra fees above the printed MRP on cold drinks", "Never buy goods with scratched off, pasted over, or tampered MRP labels"],
        "Shopkeepers have the legal right to charge ₹5 extra for chilled soft drinks because of electricity costs.", "myth", "The Supreme Court and Consumer Protection Act rule that MRP includes all taxes and refrigeration costs.",
        "What is the toll-free National Consumer Helpline (NCH) number to report overcharging above MRP?",
        ["100", "1915", "101", "108"], 1,
        "Dialing 1915 connects directly to the Department of Consumer Affairs National Consumer Helpline.",
        ["Buying a cold water bottle at {at}, the shopkeeper demands ₹25, while the printed MRP reads ₹20."],
        "How should {name} exercise consumer rights?",
        [("Point out the printed MRP: 'The law states you cannot charge above the printed Maximum Retail Price'", "Asserts statutory consumer rights firmly.", True, "cannot charge above mrp|printed price|consumer law", 45),
         ("Insist on paying only the legal printed MRP of ₹20 and demand a receipt/bill", "Enforces legal transaction price.", True, "pay printed mrp|demand bill|cash memo", 35),
         ("Report persistent overcharging merchants to the National Consumer Helpline at 1915", "Utilizes official consumer redressal.", False, "call 1915|national consumer helpline", 20)],
        ["pay ₹10 extra happily", "accept tampered price label", "threaten shopkeeper with violence"],
        "Department of Consumer Affairs (National Consumer Helpline)", "https://consumerhelpline.gov.in"
    ))

    # 4. LAW-004: FIR basics
    cards.append(make_card(
        "LAW-004", "nyaya", "Criminal law", "What is an FIR: First Information Report and Zero FIR",
        ["senior"],
        ["A First Information Report (FIR) is the written document prepared by police upon receiving information of a cognizable crime.",
         "Under Indian law, a 'Zero FIR' can be filed at ANY police station regardless of where the crime occurred."],
        ["Know that police are legally mandated under Section 154 CrPC to register an FIR for cognizable offenses", "A complainant has the legal right to receive a free physical copy of the registered FIR immediately", "Read the recorded statement carefully before signing to ensure your words are accurately documented"],
        ["Never pay money or bribes to register an FIR (FIR registration is completely free by law)", "Never sign a blank sheet of paper at a police station"],
        "A police station can turn you away and refuse to file an FIR because the crime happened in another town.", "myth", "Under the 'Zero FIR' ruling, ANY police station must register the complaint and transfer it to the relevant station.",
        "What is a 'Zero FIR' under Indian criminal jurisprudence?",
        ["A fake FIR", "An FIR that can be registered at ANY police station irrespective of territorial jurisdiction", "An online game", "A zero-rupee fine"], 1,
        "Zero FIR ensures swift investigation without jurisdictional delays in emergencies.",
        ["A theft or assault occurs at {at}, and {name}'s family goes to the police station to report it."],
        "What core legal knowledge empowers {name}?",
        [("Understand that police must register an FIR for cognizable crimes and provide a free copy", "Enforces Section 154 CrPC entitlements.", True, "register fir|free copy of fir|cognizable offense", 45),
         ("Know that if outside home jurisdiction, a 'Zero FIR' must be accepted anywhere", "Leverages Zero FIR mandate.", True, "zero fir|any police station|jurisdiction", 35),
         ("Verify that the recorded statement matches your exact verbal account before signing", "Ensures documentary integrity.", False, "read before signing|accurate account", 20)],
        ["pay bribe for fir", "sign blank paper", "accept refusal without asking for zero fir"],
        "Bureau of Police Research and Development (Citizen Legal Guide)", "https://bprd.nic.in"
    ))

    # 5. LAW-005: POCSO Act
    cards.append(make_card(
        "LAW-005", "nyaya", "Child protection", "The POCSO Act: Robust legal shield against child abuse",
        ["middle", "senior"],
        ["The Protection of Children from Sexual Offences (POCSO) Act 2012 protects all persons below 18 from abuse.",
         "The POCSO law is gender-neutral, protecting both boys and girls with child-friendly court procedures."],
        ["Know that POCSO treats anyone below 18 years as a child entitled to maximum legal protection", "Reporting is mandatory: any adult, doctor, or teacher who knows of abuse must report it or face imprisonment", "Special POCSO courts ensure the child does not see the accused during court testimony"],
        ["Never believe that the law only protects girls; boys are equally protected under POCSO", "Never reveal the identity, name, or school of a child victim in media or public chats (punishable offense)"],
        "The POCSO Act only applies to protect female children, not male children.", "myth", "The POCSO Act is 100% gender-neutral; boys, girls, and transgender children receive identical legal protections.",
        "What is the maximum age limit defining a 'child' under the POCSO Act 2012?",
        ["14 years", "Any person below 18 years of age", "21 years", "12 years"], 1,
        "POCSO universally defines a child as any individual who has not completed 18 years of age.",
        ["Discussing legal safety in civics class at {at}, students ask about how Indian law protects minors."],
        "What key legal facts should {name} share?",
        [("The POCSO Act is a powerful, gender-neutral law protecting all children below 18 years", "Explains statutory scope and universality.", True, "pocso act|gender neutral|below 18|legal shield", 45),
         ("Mandatory reporting requires adults and institutions to report abuse to police or Childline", "Ensures institutional accountability.", True, "mandatory reporting|adult duty|special courts", 35),
         ("The identity and name of a child victim can NEVER be published publicly by law", "Protects victim confidentiality under Section 23.", False, "identity protected|confidentiality", 20)],
        ["claim boys have no rights", "publish victim names online", "ignore abuse laws"],
        "Ministry of Law and Justice (POCSO Act 2012)", "https://legislative.gov.in"
    ))

    # 6. LAW-006: RTI Act
    cards.append(make_card(
        "LAW-006", "nyaya", "Transparency", "Right to Information (RTI Act): Holding public offices accountable",
        ["senior"],
        ["The Right to Information (RTI) Act 2005 empowers any Indian citizen to question government decisions.",
         "Public Information Officers (PIOs) are legally mandated to reply with certified records within 30 days."],
        ["File an RTI request online at rtionline.gov.in with a nominal ₹10 fee to inspect public project records", "Use RTI to inspect road repair budgets, school mid-day meal funds, or municipal park contracts", "Appeal to the Central/State Information Commission if an office fails to reply within 30 days"],
        ["Never use RTI for private disputes; it applies strictly to public government authorities", "Never feel intimidated: RTI is a celebrated democratic transparency tool for all citizens"],
        "Only certified journalists and lawyers have the legal right to file RTI applications.", "myth", "Every single citizen of India has the constitutional right to file an RTI to inspect government records.",
        "Within how many days is a Public Information Officer (PIO) legally required to respond to an RTI request?",
        ["1 year", "Within 30 days of receiving the application", "5 days", "Never"], 1,
        "The RTI Act mandates a strict 30-day timeline (48 hours if concerning life and liberty).",
        ["A road outside school at {at} was supposedly repaired last month but broke apart in 3 days."],
        "How can {name} and their family use the RTI Act constructively?",
        [("File an RTI query on rtionline.gov.in to obtain the sanctioned budget, contractor name, and work audit", "Extracts public administrative records.", True, "file rti|inspect records|road budget|contractor details", 45),
         ("Know that public authorities are legally bound to respond within 30 days", "Enforces statutory time-bound compliance.", True, "30 days response|public information officer|transparency", 35),
         ("Use certified government documents to hold local ward engineers accountable", "Promotes active citizen democratic oversight.", False, "civic accountability|governance", 20)],
        ["bribe officials for info", "smash road in anger", "assume citizens have no rights"],
        "Department of Personnel and Training (RTI Online Portal)", "https://rtionline.gov.in"
    ))

    # 7. LAW-007: Aadhaar privacy
    cards.append(make_card(
        "LAW-007", "nyaya", "Identity privacy", "Protecting your Aadhaar and personal data: Masked Aadhaar",
        ["junior", "middle", "senior"],
        ["Your 12-digit Aadhaar number is a unique national identity linked to banking and mobile telecom accounts.",
         "Sharing unmasked Aadhaar photocopies carelessly exposes you to identity impersonation and SIM swap fraud."],
        ["Download and use 'Masked Aadhaar' (which displays only the last 4 digits: XXXX-XXXX-1234) from myaadhaar.uidai.gov.in", "Cross out the photocopy with two parallel lines and write the specific purpose (e.g. 'For SIM activation only')", "Lock your Aadhaar biometrics using the official mAadhaar mobile app when not actively visiting verification centers"],
        ["Never share your 6-digit Aadhaar OTP with anyone claiming to be a verification executive", "Never leave photocopies of your Aadhaar card lying around internet cafes"],
        "Hotels and cinema halls have the absolute legal right to demand your original unmasked Aadhaar card copy.", "myth", "UIDAI explicitly clarifies that Masked Aadhaar is legally valid everywhere, and private entities cannot compel unmasked copies.",
        "What is a 'Masked Aadhaar' downloaded from the official UIDAI portal?",
        ["A fake Aadhaar", "An official copy where the first 8 digits are hidden as XXXX-XXXX, displaying only the last 4 digits", "An Aadhaar with a mask picture", "A broken card"], 1,
        "Masked Aadhaar protects privacy by concealing the first 8 digits while remaining 100% legally valid.",
        ["Checking into a hotel or registering at a coaching institute at {at}, the clerk demands a photocopy of Aadhaar."],
        "What privacy safeguard should {name} apply?",
        [("Provide a 'Masked Aadhaar' photocopy where the first 8 digits are concealed", "Prevents unauthorized identity harvesting.", True, "masked aadhaar|hide first 8 digits|last 4 digits", 45),
         ("Cross the photocopy and clearly write: 'Submitted strictly for [Purpose] only'", "Prevents document misuse for other contracts.", True, "cross photocopy|write purpose|watermark", 35),
         ("Never share the Aadhaar OTP with anyone under any circumstances", "Secures identity verification channel.", False, "never share aadhaar otp|lock biometrics", 20)],
        ["give unmasked copy to stranger", "share aadhaar otp on call", "leave card at cyber cafe"],
        "Unique Identification Authority of India (UIDAI)", "https://uidai.gov.in"
    ))

    # 8. LAW-008: Juvenile driving
    cards.append(make_card(
        "LAW-008", "nyaya", "Traffic law", "Juvenile driving laws: Heavy penalties under Section 199A MV Act",
        ["middle", "senior"],
        ["Under Section 199A of the amended Motor Vehicles Act, vehicle owners face 3 years imprisonment if a minor drives.",
         "The vehicle's registration is cancelled for 1 year, and the minor cannot get a driving license until age 25."],
        ["Understand that underage driving carries a ₹25,000 fine on parents and possible juvenile home detention", "Wait until age 18 to obtain a permanent driving license (age 16 for gearless 50cc with parental consent)", "Use cycles, walking, or public transport until reaching legal licensing age"],
        ["Never borrow your parents' car or scooter without having a valid driving license", "Never give into peer pressure urging you to show off driving skills outside school"],
        "If a 15-year-old drives a motorcycle and causes an accident, police cannot touch them because they are a minor.", "myth", "Under MV Act Section 199A, parents face 3 years jail, ₹25,000 fine, and the minor faces juvenile justice trial.",
        "What is the legal penalty on parents/vehicle owners under Section 199A if a minor is caught driving?",
        ["A ₹50 fine", "Up to ₹25,000 fine, 3 years imprisonment, and cancellation of vehicle registration for 1 year", "A warning letter", "No penalty"], 1,
        "Stringent MV Act amendments hold vehicle owners criminally liable for allowing underage driving.",
        ["Friends at {at} tease a 15-year-old for not taking their father's car out on the highway."],
        "How should {name} explain the severe legal reality?",
        [("Explain that Section 199A MV Act imposes a ₹25,000 fine and up to 3 years jail on parents", "Cites exact statutory criminal liability.", True, "mv act section 199a|jail for parents|25000 fine|illegal", 45),
         ("State that the minor will be barred from getting a driving license until age 25", "Highlights long-term personal consequences.", True, "barred until 25|no license until 25", 35),
         ("Take pride in obeying the law and choose safe cycling or walking", "Champions responsible juvenile citizenship.", False, "obey traffic law|cycle|walk", 20)],
        ["encourage joyriding", "claim minors face no law", "steal car keys"],
        "Ministry of Road Transport and Highways (Motor Vehicles Act)", "https://morth.nic.in"
    ))

    # 9. LAW-009: Student voice
    cards.append(make_card(
        "LAW-009", "nyaya", "Participation", "Right to be heard at school: Student councils and grievance boxes",
        ["junior", "middle", "senior"],
        ["Article 12 of the UN Convention on the Rights of the Child guarantees youth the right to express views freely.",
         "School grievance boxes and elected student councils provide structured channels to voice campus concerns."],
        ["Use your school's student council or anonymous suggestion/grievance box to raise constructive concerns", "Advocate for campus improvements: clean drinking water, clean toilets, library books, and sports gear", "Present feedback respectfully with facts, practical solutions, and collective student support"],
        ["Never use grievance boxes to post anonymous personal insults or defamatory rumors about teachers", "Never remain silent about unhygienic washrooms or broken safety equipment"],
        "Students are children and have zero right to express opinions about school facilities.", "myth", "Modern educational jurisprudence recognizes students as primary stakeholders with the legal right to be heard.",
        "What international human rights treaty guarantees children the right to express their views on matters affecting them?",
        ["Trade Agreement", "UN Convention on the Rights of the Child (UNCRC Article 12)", "Postal Code", "None"], 1,
        "UNCRC Article 12 establishes that children's views must be given due weight in all matters affecting them.",
        ["Students at {at} notice that the school science lab lacks basic safety goggles and washroom taps are broken."],
        "How should {name} channel this student voice legally and constructively?",
        [("Draft a respectful, factual petition through the elected Student Council or Grievance Box", "Utilizes established institutional democratic channels.", True, "student council|grievance box|respectful petition|factual", 45),
         ("Highlight the safety implications: students need working washroom hygiene and eye protection", "Frames request around student safety and rights.", True, "safety implications|hygiene rights|lab safety", 35),
         ("Engage with the school principal collaboratively to improve campus infrastructure", "Fosters positive civic negotiation.", False, "collaborate with principal|constructive solution", 20)],
        ["vandalize school property", "post abusive memes online", "stay silent forever"],
        "UN Convention on the Rights of the Child (Article 12)", "https://unicef.org"
    ))

    # 10. LAW-010: Disability rights
    cards.append(make_card(
        "LAW-010", "nyaya", "Inclusion law", "Rights of Persons with Disabilities (RPWD Act 2016): Equal access",
        ["junior", "middle", "senior"],
        ["The RPWD Act 2016 recognizes 21 disabilities and mandates barrier-free accessibility in all public buildings.",
         "Discrimination against persons with disabilities is punishable with imprisonment under Indian law."],
        ["Advocate for ramps, braille signage, and accessible washrooms in schools, metro stations, and public parks", "Understand that inclusive education is a legal right: no school can deny admission based on disability", "Treat disabled peers with equality, dignity, and natural inclusion without pity or condescension"],
        ["Never park bicycles or store clutter blocking wheelchair ramps or tactile pavings", "Never mock, imitate, or use derogatory slurs against people with disabilities"],
        "Wheelchair ramps in schools are optional luxury decorations that schools can skip.", "myth", "Barrier-free accessibility ramps and accessible washrooms are mandatory legal requirements under the RPWD Act.",
        "How many disabilities are officially recognized under the Rights of Persons with Disabilities (RPWD) Act 2016?",
        ["Only 2", "21 benchmark disabilities", "100", "5"], 1,
        "The 2016 Act expanded recognized disabilities from 7 to 21, including autism, intellectual disability, and locomotor disability.",
        ["A student using a wheelchair seeks admission at a school at {at}, but the administration claims they have no ramp."],
        "What legal mandate protects the student?",
        [("The RPWD Act 2016 legally mandates all schools to provide barrier-free accessible infrastructure", "Enforces statutory accessibility mandate.", True, "rpwd act 2016|accessible infrastructure|mandatory ramps|equal rights", 45),
         ("Denying school admission on the grounds of disability violates constitutional equality and the law", "Illegal educational discrimination.", True, "cannot deny admission|inclusive education|equality", 35),
         ("The school must construct ramps and accessible facilities to accommodate all learners", "Obligates reasonable accommodation.", False, "construct ramps|reasonable accommodation", 20)],
        ["support turning the student away", "block the ramp with bicycles", "mock wheelchair users"],
        "Department of Empowerment of Persons with Disabilities (MSJE)", "https://disabilityaffairs.gov.in"
    ))

    # 11. LAW-011: Equality Article 15
    cards.append(make_card(
        "LAW-011", "nyaya", "Constitutional equality", "Article 15: No discrimination on grounds of religion, race, caste or sex",
        ["junior", "middle", "senior"],
        ["Article 15 of the Indian Constitution strictly prohibits discrimination in access to public shops, wells, and parks.",
         "Equality is a fundamental pillar: every Indian citizen stands equal before the law."],
        ["Treat every classmate with equal respect regardless of their family background, language, religion, or caste", "Ensure public spaces like colony playgrounds, water coolers, and sports fields are open to everyone", "Celebrate India's rich cultural diversity as a source of national strength and unity"],
        ["Never exclude a classmate from games or study groups based on their caste, community, or mother tongue", "Never practice or tolerate untouchability or social segregation (punishable under Article 17)"],
        "Colony sports grounds can legally ban children of domestic workers from playing on the grass.", "myth", "Article 15 explicitly forbids discrimination in public places, parks, and wells against any citizen.",
        "Which article of the Indian Constitution prohibits discrimination against any citizen on grounds of religion, race, caste, sex, or place of birth?",
        ["Article 1", "Article 15", "Article 370", "Article 50"], 1,
        "Article 15 is the cornerstone of non-discrimination and fundamental democratic equality in India.",
        ["In a residential colony playground at {at}, someone tries to stop a maintenance worker's child from playing football."],
        "How does {name} uphold constitutional values?",
        [("Point out that public parks and playgrounds belong equally to all children under Article 15", "Champions constitutional non-discrimination.", True, "article 15|equal access|public playground belongs to all", 45),
         ("Invite the child into the football match warmly and pass them the ball", "Practices everyday constitutional equality.", True, "invite to play|pass the ball|inclusive play", 35),
         ("Stand firmly against caste, class, or community prejudice in your neighborhood", "Rejects illegal social segregation.", False, "no discrimination|equality|reject prejudice", 20)],
        ["tell the child to leave", "support playground discrimination", "mock the child's clothes"],
        "Constitution of India (Fundamental Rights - Article 15)", "https://legislative.gov.in"
    ))

    # 12. LAW-012: Cyber law
    cards.append(make_card(
        "LAW-012", "nyaya", "Cyber law", "Information Technology Act: What is illegal on the internet",
        ["middle", "senior"],
        ["The Information Technology (IT) Act 2000 governs digital crimes, data privacy, and online fraud.",
         "Creating fake social media profiles (Section 66D) or hacking accounts (Section 66) carries up to 3 years imprisonment."],
        ["Know that online actions leave IP address digital trails that law enforcement cyber cells trace easily", "Understand that creating fake impersonation profiles or sending offensive abusive messages is a crime", "Respect intellectual property: do not distribute pirated software, cracked games, or copyrighted media"],
        ["Never create fake social media accounts pretending to be your classmates or teachers", "Never hack into a friend's email, Instagram, or gaming account 'as a joke'"],
        "Creating a fake Instagram account of your school principal to post funny jokes is harmless and legal.", "myth", "Identity impersonation and transmitting offensive messages are punishable crimes under Sections 66C and 66D of the IT Act.",
        "What law in India penalizes identity theft, hacking, and online financial cheating?",
        ["Motor Vehicle Code", "The Information Technology (IT) Act 2000", "Forest Act", "Railway Act"], 1,
        "The IT Act 2000 provides the comprehensive legal framework for investigating and penalizing cyber offenses.",
        ["A student at {at} creates a fake social media handle using a classmate's photo to post rude pranks."],
        "What legal warning should {name} deliver?",
        [("Explain that online impersonation and identity theft are punishable crimes under Section 66D IT Act", "Cites statutory cybercrime liability.", True, "section 66d|it act|identity theft|cybercrime|punishable", 45),
         ("Remind them that cyber police trace IP addresses and digital footprints back to personal devices", "Dispels illusion of internet anonymity.", True, "ip address traced|cyber police|digital footprints", 35),
         ("Insist they delete the fake profile immediately and apologize to the classmate", "Facilitates immediate restorative remediation.", False, "delete fake profile|apologize|stop harassment", 20)],
        ["encourage fake profile pranks", "help hack classmate's account", "claim online has no laws"],
        "Ministry of Electronics and Information Technology (IT Act)", "https://meity.gov.in"
    ))

    # 13. LAW-013: Lost documents
    cards.append(make_card(
        "LAW-013", "nyaya", "Lost documents", "Lost official documents (Aadhaar, marksheet, passport): Online police report",
        ["middle", "senior"],
        ["Lost government IDs can be misused by criminals for unauthorized SIM cards or bank loans.",
         "Filing a 'Lost Document Report' online with state police creates a legal shield proving you did not commit subsequent fraud."],
        ["File a 'Lost Article / Document Report' online immediately on your State Police citizen portal", "Download and print the official digitally signed Lost Report receipt (LDR) with its unique reference number", "Apply for duplicate marksheets through official board portals (e.g. CBSE Pariksha Sangam) using the police report"],
        ["Never ignore a lost Aadhaar, PAN card, or board marksheet hoping it will magically turn up", "Never pay unofficial touts to obtain duplicate government documents"],
        "If you lose your original Class 10 marksheet, you can never get another copy in your lifetime.", "myth", "Central and state boards provide official duplicate marksheets online through verified police lost report receipts.",
        "Why must you file a police 'Lost Article Report' immediately after losing an identity card or marksheet?",
        ["To pay fines", "It provides legal proof that you lost the document, protecting you if a criminal misuses it", "To get a reward", "None"], 1,
        "A police lost report creates an official timestamped legal barrier protecting against identity theft.",
        ["While traveling at {at}, {name} loses an official school marksheet and Aadhaar card."],
        "What is the correct, structured legal procedure?",
        [("File an online 'Lost Property / Document Report' on the State Police citizen portal", "Establishes immediate legal record of loss.", True, "online lost report|state police portal|lost document report", 45),
         ("Download the official digital police receipt as legal proof of loss", "Documentary evidence for duplicate reissue.", True, "download receipt|police receipt|proof of loss", 35),
         ("Apply for duplicate documents through the official board portal (CBSE/State Board) and UIDAI", "Lawful replacement process.", False, "apply duplicate|cbse portal|uidai reissue", 20)],
        ["do nothing and panic", "pay touts for fake marksheet", "ignore lost aadhaar"],
        "National Crime Records Bureau (Citizen Services)", "https://ncrb.gov.in"
    ))

    # 14. LAW-014: Child marriage
    cards.append(make_card(
        "LAW-014", "nyaya", "Child protection", "Child marriage is illegal: The Prohibition of Child Marriage Act",
        ["junior", "middle", "senior"],
        ["Under the Prohibition of Child Marriage Act (PCMA), marriage below age 18 for girls and 21 for boys is illegal.",
         "Anyone who performs, conducts, directs, or abets a child marriage faces rigorous imprisonment and non-bailable arrest."],
        ["Know that child marriage destroys education, health, and childhood, and is strictly prohibited by law", "Know that Child Marriage Prohibition Officers (CMPO), police, and Childline 1098 intervene to stop illegal weddings", "Report any impending child marriage secretly and confidentially to Childline 1098 or local police 112"],
        ["Never attend or support a wedding where the bride or groom is a minor child", "Never believe that 'family traditions' overrule the statutory criminal law of India"],
        "If parents arrange a wedding for a 15-year-old girl with community approval, the law cannot stop it.", "myth", "Child marriage is a cognizable, non-bailable offense. Police and Child Welfare Committees halt weddings instantly.",
        "What is the statutory legal age of marriage in India under current law?",
        ["12 for girls, 14 for boys", "Minimum 18 years for females and 21 years for males", "Any age with parent consent", "10 years"], 1,
        "Statutory law mandates minimum 18 for women and 21 for men to protect physical and emotional maturity.",
        ["A 15-year-old student at {at} is being secretly pulled out of school by family for an arranged child marriage."],
        "What urgent legal protection can be mobilized?",
        [("Report immediately to Child Helpline 1098, the school principal, or local police 112", "Mobilizes emergency Child Welfare Committee (CWC) legal stay orders.", True, "call 1098|childline|call 112|report child marriage", 45),
         ("Explain that the Prohibition of Child Marriage Act makes child marriage a non-bailable criminal offense", "Understands statutory criminal prohibition.", True, "pcma act|non-bailable|illegal offense|jail for organizers", 35),
         ("Ensure the reporting is handled confidentially to protect the young student's safety", "Shields child from retaliatory pressure.", False, "confidential reporting|protect student", 20)],
        ["attend the child wedding", "encourage early marriage", "claim tradition beats law"],
        "Ministry of Women and Child Development (PCMA)", "https://wcd.nic.in"
    ))

    # 15. LAW-015: Free legal aid
    cards.append(make_card(
        "LAW-015", "nyaya", "Legal aid", "National Legal Services Authority (NALSA): Free legal aid for all children",
        ["middle", "senior"],
        ["Article 39A of the Indian Constitution directs the state to provide free legal aid to ensure equal justice.",
         "Under Section 12 of the Legal Services Authorities Act, ALL children, women, and disadvantaged citizens get 100% free lawyers."],
        ["Know that children, women, SC/ST citizens, and economically weaker individuals are legally entitled to free lawyers", "Access free legal assistance through District Legal Services Authorities (DLSA) in every district court", "Call the National Legal Services Authority toll-free helpline at 15100 for guidance"],
        ["Never assume justice is only for the wealthy who can afford expensive private advocates", "Never pay fees to a designated Legal Aid panel advocate (their services are fully funded by the state)"],
        "Hiring a lawyer in India always requires paying lakhs of rupees, meaning poor families can never go to court.", "myth", "Under NALSA, the government appoints experienced panel lawyers completely free of cost for eligible citizens.",
        "What national helpline number provides free legal guidance under NALSA in India?",
        ["100", "15100", "101", "108"], 1,
        "Dialing 15100 connects directly to the National Legal Services Authority free legal consultation desk.",
        ["A vulnerable family at {at} faces illegal eviction but has zero money to afford private court lawyers."],
        "How can {name} connect them to justice?",
        [("Inform them about free legal aid provided by the District Legal Services Authority (DLSA) under NALSA", "Directs to statutory free legal aid mechanisms.", True, "nalsa|dlsa|free legal aid|district court legal services", 45),
         ("Call the national legal aid helpline at 15100 for immediate advice", "Accesses free government legal counseling.", True, "call 15100|national legal helpline|free lawyer", 35),
         ("Explain that children and vulnerable citizens are guaranteed free court representation under Article 39A", "Constitutional right to equal justice.", False, "article 39a|equal justice|free representation", 20)],
        ["tell them justice is impossible", "pay loan sharks for lawyer fees", "give up without legal aid"],
        "National Legal Services Authority (NALSA)", "https://nalsa.gov.in"
    ))

    # 16. LAW-016: Child Welfare Committees
    cards.append(make_card(
        "LAW-016", "nyaya", "Child justice", "Child Welfare Committees (CWC) and juvenile justice protections",
        ["middle", "senior"],
        ["Every district in India has a statutory Child Welfare Committee (CWC) acting as a judicial bench for children.",
         "The Juvenile Justice (Care and Protection of Children) Act ensures children are rehabilitated, not criminalized."],
        ["Understand that CWCs have the authority of a judicial magistrate to order shelter, medical care, and rehabilitation", "Special Juvenile Police Units (SJPU) in every police station operate in plain clothes to keep interactions child-friendly", "Any child found lost, abandoned, or subjected to abuse is produced before the CWC for legal protection"],
        ["Never treat juvenile justice as punitive; the law focuses on care, protection, and social reintegration", "Never publish photos or names of children involved in juvenile proceedings"],
        "Police can put children into regular adult prison cells alongside adult convicts.", "myth", "The Juvenile Justice Act strictly prohibits placing children in adult jails; they receive counseling in observation homes.",
        "What statutory district body holds judicial powers to protect children in need of care and rehabilitation?",
        ["Panchayat only", "Child Welfare Committee (CWC)", "Municipal tax office", "Traffic court"], 1,
        "CWCs function as the bench of magistrates under the JJ Act for children requiring care and protection.",
        ["Discussing child safety mechanisms at {at}, students ask who makes legal decisions for rescued street children."],
        "What institutional framework should {name} explain?",
        [("Explain that the statutory Child Welfare Committee (CWC) acts as a judicial authority for child protection", "Explains core JJ Act governance framework.", True, "child welfare committee|cwc|judicial authority|rehabilitation", 45),
         ("State that Special Juvenile Police Units (SJPU) handle children gently in plain clothes", "Highlights child-friendly police standards.", True, "sjpu|plain clothes police|child friendly", 35),
         ("Emphasize that the law aims to rehabilitate and educate vulnerable children, not punish them", "Understands restorative child justice.", False, "rehabilitation|education|care and protection", 20)],
        ["advocate throwing kids in adult jails", "ignore child welfare committees", "condemn street children"],
        "Juvenile Justice (Care and Protection of Children) Act", "https://wcd.nic.in"
    ))

    # 17. LAW-017: Passenger rights
    cards.append(make_card(
        "LAW-017", "nyaya", "Transport rights", "Passenger rights: Rail cancellations, delays and passenger charter",
        ["middle", "senior"],
        ["Indian Railways and the Directorate General of Civil Aviation (DGCA) maintain formal passenger charters.",
         "Passengers have statutory rights to ticket refunds, meals during extended delays, and emergency grievance redressal."],
        ["Use the 'RailMadad' app or helpline 139 for real-time medical aid, security assistance, or cleanliness complaints on trains", "Claim full TDR refunds if a train is delayed by more than 3 hours and you choose not to travel", "Know that airlines must provide free meals/refreshments for delays over 2 to 4 hours under DGCA passenger charter"],
        ["Never travel without a valid ticket or valid government identity proof", "Never pay extra unauthorized cash to railway pantry staff above the printed menu price list"],
        "If a train pantry vendor charges ₹50 extra for a meal, passengers have zero rights to complain.", "myth", "RailMadad (139) takes swift disciplinary action against pantry vendors overcharging above approved IRCTC rates.",
        "What is the official unified helpline number and mobile app for Indian Railway passenger grievances?",
        ["100", "139 (RailMadad)", "101", "108"], 1,
        "Dialing 139 or using the RailMadad app connects directly to the railway grievance cell for immediate action.",
        ["Traveling on a long-distance train at {at}, the coach air conditioning fails and pantry staff overcharge for water."],
        "How should {name} exercise statutory passenger rights?",
        [("File an instant complaint on the RailMadad app or call 139 with the PNR number", "Triggers immediate on-board railway officer intervention.", True, "railmadad|call 139|pnr number|file complaint", 45),
         ("Check the official IRCTC menu price list and refuse to pay unauthorized extra charges", "Asserts approved tariff rights.", True, "irctc approved rates|refuse extra charges|official price list", 35),
         ("Know that passengers have clear rights to cleanliness, safety, and grievance resolution", "Understands passenger service charter.", False, "passenger rights|service charter", 20)],
        ["pay double price silently", "smash train windows", "ignore railmadad portal"],
        "Indian Railways Passenger Charter (RailMadad)", "https://railmadad.indianrailways.gov.in"
    ))

    # 18. LAW-018: Fundamental duties
    cards.append(make_card(
        "LAW-018", "nyaya", "Citizenship", "Fundamental Duties (Article 51A): The citizen's moral compass",
        ["junior", "middle", "senior"],
        ["Rights and duties are two sides of the same coin; democracy cannot survive if citizens demand rights while abandoning duties.",
         "Article 51A of the Indian Constitution lists 11 Fundamental Duties expected of every responsible citizen."],
        ["Abide by the Constitution, respect the National Flag and National Anthem (Article 51A(a))", "Protect and improve the natural environment, including forests, lakes, rivers, and wildlife (Article 51A(g))", "Develop scientific temper, humanism, and the spirit of inquiry and reform (Article 51A(h))"],
        ["Never destroy or vandalize public property (Article 51A(i) mandates abjuring violence and protecting public assets)", "Never treat civic responsibility as someone else's job"],
        "The Constitution of India only gives citizens free rights and asks for zero duties in return.", "myth", "Part IVA (Article 51A) establishes 11 Fundamental Duties essential for national harmony and progress.",
        "Which Fundamental Duty under Article 51A(h) encourages students to question superstitions and explore science?",
        ["Duty to pay tax", "Duty to develop scientific temper, humanism, and the spirit of inquiry and reform", "Duty to build roads", "Duty to swim"], 1,
        "Developing a 'scientific temper' is a unique, celebrated constitutional duty in the Indian Constitution.",
        ["In school assembly at {at}, {name} discusses what makes a great, responsible Indian citizen."],
        "What constitutional wisdom should {name} embody?",
        [("Balance democratic rights with active fulfillment of Fundamental Duties under Article 51A", "Connects rights with civic responsibility.", True, "fundamental duties|article 51a|civic responsibility|balance rights", 45),
         ("Fulfill duties by protecting public property, conserving wildlife, and respecting the National Flag", "Concrete everyday duty execution.", True, "protect public property|conserve environment|respect flag", 35),
         ("Cultivate a scientific temper, questioning blind superstitions and seeking evidence-based truth", "Champions Article 51A(h) scientific inquiry.", False, "scientific temper|spirit of inquiry|evidence", 20)],
        ["vandalize public buses", "claim duties don'?t matter", "promote blind superstition"],
        "Constitution of India (Part IVA - Fundamental Duties)", "https://legislative.gov.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Nyaya")
    return cards
