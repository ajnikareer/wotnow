"""
New Agents in the PLANET Pillar:
- Paws (Animals & Wildlife - ANI)
- Volt (Clean Energy & Green Tech - GRN)
"""
from cards_existing import make_card

def get_paws_cards():
    cards = []

    # 1. ANI-001: Dog body language
    cards.append(make_card(
        "ANI-001", "paws", "Canine communication", "Understanding stray dog body language: Wagging vs stiff posture",
        ["junior", "middle", "senior"],
        ["A wagging tail does NOT always mean a friendly dog; a stiff, fast-wagging tail can signal high tension or aggression.",
         "Yawning, lip licking, averting eyes, and turning the head are 'calming signals' dogs use when feeling nervous."],
        ["Look for relaxed body language: loose wagging hips, open mouth, and soft eyes before approaching", "If a dog stiffens, stares fixedly, growls, or curls lips, freeze in place like a tree and avoid direct eye contact", "Walk slowly backwards or sideways away without turning your back or running"],
        ["Never stare directly into an unfamiliar dog's eyes (dogs perceive staring as an aggressive challenge)", "Never disturb a sleeping, eating, or nursing dog or corner a frightened stray"],
        "If a dog's tail is moving back and forth, you can run up and hug it safely without any risk.", "myth", "A high, rigid vibrating tail signals heightened alertness or defensive aggression, not affection.",
        "What should you do if an unfamiliar street dog stiffens its body, raises hackles, and growls at you?",
        ["Scream loudly and sprint", "Freeze calmly like a tree, look slightly down, and back away slowly without running", "Kick the dog", "Smile and show teeth"], 1,
        "Freezing like a tree and avoiding eye contact de-escalates the dog's perceived threat.",
        ["Walking through a colony lane at {at}, {name} sees an unfamiliar stray dog growling stiffly with ears pinned back."],
        "How should {name} navigate this safely?",
        [("Freeze calmly in place and avoid staring directly into the dog's eyes", "Neutralizes perceived challenge and allows dog to calm down.", True, "freeze like a tree|no direct eye contact|calm posture", 45),
         ("Back away slowly and sideways without running or screaming", "Avoids triggering predatory chase instinct.", True, "back away slowly|sideways|no running|no screaming", 35),
         ("Keep arms folded across chest and do not make sudden rapid gestures", "Protects vital torso without threatening movement.", False, "arms folded|no sudden moves", 20)],
        ["sprint away screaming", "stare into dog's eyes aggressively", "throw stones"],
        "Animal Welfare Board of India (Street Dog Behavior Guide)", "https://awbi.gov.in"
    ))

    # 2. ANI-002: Dog bite protocol
    cards.append(make_card(
        "ANI-002", "paws", "Bite safety", "Immediate dog bite first aid: Soap, running water and rabies vaccine",
        ["junior", "middle", "senior"],
        ["Rabies virus is transmitted via saliva through broken skin, scratches, or mucous membranes.",
         "Washing the bite wound immediately with soap and water for 15 minutes eliminates over 90% of the viral load."],
        ["Wash the scratch or bite immediately under running tap water with soap for at least 15 continuous minutes", "Apply an antiseptic solution like povidone iodine after washing thoroughly", "Visit a medical clinic or government hospital on the same day for anti-rabies vaccination (PEP) and tetanus toxoid"],
        ["Never apply chili powder, lime, haldi, or cow dung to animal bites (causes severe sepsis)", "Never bandage the bite wound tightly (traps virus and anaerobic bacteria in tissue)"],
        "If the dog that scratched you looks healthy, you can skip seeing a doctor for 10 days.", "myth", "Rabies can be transmitted before animals show visible symptoms. Post-exposure prophylaxis MUST start immediately.",
        "What is the single most critical first aid action immediately following an animal bite or scratch?",
        ["Tie a tight tourniquet", "Wash the wound under running tap water with soap for at least 15 minutes", "Put red chili on it", "Wait 2 weeks"], 1,
        "Soap dissolves the rabies viral envelope and running water physically flushes virus particles out.",
        ["While playing in the park at {at}, a startled street dog nips {name}'s ankle, breaking the skin."],
        "What immediate life-saving protocol must {name} follow?",
        [("Wash the wound under a running water tap with soap for at least 15 full minutes", "Physically eliminates rabies virus from the wound bed.", True, "wash with soap|15 minutes|running water|clean wound", 45),
         ("Do not cover with tight bandages or apply irritants like chili powder or turmeric", "Prevents tissue damage and infection.", True, "no tight bandage|no chili|no haldi", 35),
         ("Go to a medical clinic on the exact same day to start the anti-rabies vaccination course", "Post-exposure prophylaxis is 100% effective when started early.", False, "doctor same day|rabies vaccine|clinic", 20)],
        ["apply chili powder", "ignore minor scratch", "delay doctor for 2 weeks"],
        "National Rabies Control Programme (NCDC India)", "https://ncdc.gov.in"
    ))

    # 3. ANI-003: Responsible feeding
    cards.append(make_card(
        "ANI-003", "paws", "Community animals", "Responsible stray animal feeding: Fixed spots, hygiene and harmony",
        ["junior", "middle", "senior"],
        ["Community dogs naturally defend territory; feeding them near crowded gates or parking bays creates conflict.",
         "The Animal Welfare Board of India (AWBI) mandates feeding in designated, quiet spots away from walkways."],
        ["Feed community dogs at a fixed, designated spot away from building gates, children's play areas, and traffic", "Feed at consistent, quiet times (early morning or late evening) so dogs do not linger in pedestrian corridors", "Clean up food plates and paper bowls immediately after feeding to maintain colony cleanliness"],
        ["Never feed dogs on narrow stairwells, right outside lift doors, or near play swings", "Never leave rotting food waste lying on common society pavements"],
        "Throwing leftover spicy bones at dogs from your 4th-floor balcony is great animal care.", "myth", "Balcony tossing creates colony hygiene disputes, hits pedestrians, and spicy cooked bones splinter dog intestines.",
        "Where should community dogs be fed in residential apartment societies?",
        ["Directly inside the elevator", "In an agreed, designated quiet corner away from children's play areas and building gates", "On public stairs", "On busy roads"], 1,
        "Designated feeding corners prevent territorial congregation near crowded pedestrian gates.",
        ["Family at {at} wants to feed community street dogs in their neighborhood."],
        "How should {name} structure this compassion responsibly?",
        [("Choose a designated quiet corner away from busy entrance gates, parking spots, and play parks", "Minimizes human-animal conflict in common walking corridors.", True, "designated spot|away from gates|quiet corner|no play areas", 45),
         ("Feed fresh, dog-friendly food (rice with eggs/curd/kibble) at consistent morning or evening hours", "Healthy feeding without toxic cooked spices.", True, "dog friendly food|consistent time|rice and curd", 35),
         ("Clean up all food wrappers and paper bowls immediately after dogs finish eating", "Maintains neighborhood hygiene and harmony.", False, "clean up bowls|no litter|hygiene", 20)],
        ["feed in center of busy road", "leave rotting meat on stairs", "feed spicy curry bones"],
        "AWBI Revised Guidelines for Feeding Community Animals", "https://awbi.gov.in"
    ))

    # 4. ANI-004: Pet dog care
    cards.append(make_card(
        "ANI-004", "paws", "Pet care", "Pet dog care fundamentals: Annual rabies shots, hydration and love",
        ["junior", "middle", "senior"],
        ["Pet dogs require annual core booster vaccinations (Anti-Rabies and DHPPIL) to stay protected.",
         "Dogs cannot sweat through their skin (only pant through tongues); they suffer heatstroke rapidly in summer."],
        ["Ensure your pet receives an annual anti-rabies vaccination certified in their official veterinary book", "Keep fresh, clean drinking water accessible 24/7 in a clean bowl in a cool shady area", "Walk your dog during cool morning and late evening hours; avoid hot asphalt that burns paw pads"],
        ["Never leave a dog locked inside a parked car, even with windows cracked (deadly in 15 mins)", "Never walk dogs on scorching asphalt roads in afternoon sun (blisters sensitive paw pads)"],
        "Dogs only need one rabies vaccination when they are puppies and never need another shot for life.", "myth", "Rabies immunity wanes over time; annual booster shots are legally required to maintain protective immunity.",
        "How do dogs primarily regulate their body temperature and cool down in hot weather?",
        ["Sweating through their back", "Panting through their open mouth and tongue, and small sweat glands on paw pads", "Shedding teeth", "Drinking soda"], 1,
        "Panting evaporates moisture from the respiratory tract; excessive heat overwhelms this mechanism.",
        ["Caring for a pet dog during peak summer at {at}, the afternoon sun makes the road pavement burning hot."],
        "What protective pet care routine should {name} maintain?",
        [("Walk the dog during early mornings and late evenings; test pavement with the back of your hand", "Prevents painful third-degree paw pad burns.", True, "walk early morning|late evening|test pavement|cool hours", 45),
         ("Provide clean, cool drinking water at all times in a shaded corner of the home", "Prevents rapid canine dehydration and heatstroke.", True, "clean water 24/7|shade|hydration", 35),
         ("Ensure yearly anti-rabies and multi-disease booster shots are up to date with the veterinarian", "Maintains essential lifelong immunity.", False, "annual rabies vaccine|vet checkup", 20)],
        ["walk on burning 2 pm asphalt", "leave dog locked in car", "skip annual rabies vaccine"],
        "Veterinary Council of India Guidelines", "https://vci.dadf.gov.in"
    ))

    # 5. ANI-005: Urban monkeys
    cards.append(make_card(
        "ANI-005", "paws", "Wildlife", "Urban monkeys (Macaques): Food rules, eye contact and calmness",
        ["junior", "middle", "senior"],
        ["Rhesus macaques associate crinkling plastic carry bags with food and will snatch them aggressively.",
         "Direct eye contact and smiling (baring your teeth) are interpreted by monkeys as an aggressive threat display."],
        ["Conceal all food, fruits, and snacks inside closed backpacks when walking near monkey troops", "If confronted by an assertive monkey, avoid direct eye contact, stay calm, and walk away slowly without running", "Keep doors and window mesh grills latched in areas with urban monkey populations"],
        ["Never tease, point sticks, throw stones, or chase monkeys (provokes defensive troop attacks)", "Never smile or bare your teeth at an aggressive monkey (monkeys perceive teeth baring as a battle challenge)"],
        "Smiling warmly at an angry monkey will make it feel friendly toward you.", "myth", "In primate body language, showing teeth (grimacing) is a sign of aggression and battle challenge.",
        "What should you NEVER do when carrying food near monkeys at a tourist fort or temple?",
        ["Keep food in backpack", "Carry open plastic bags or eat bananas out in the open in front of them", "Walk calmly", "Stay quiet"], 1,
        "Visible food and crinkling plastic bags instantly trigger monkeys to snatch items aggressively.",
        ["Visiting an ancient temple or fort at {at}, {name} sees a troop of urban monkeys sitting along the railing."],
        "How should {name} pass by without conflict?",
        [("Keep all food, drinks, and snacks securely zipped inside backpacks out of sight", "Eliminates visual and auditory food triggers.", True, "food in backpack|hide food|no plastic bags", 45),
         ("Do not make direct eye contact or bare your teeth at the monkeys", "Avoids triggering territorial primate aggression.", True, "no eye contact|don'?t show teeth|calm posture", 35),
         ("Walk at a steady, calm pace without running or swinging arms aggressively", "Signals non-threatening neutral transit.", False, "walk calmly|no running|no teasing", 20)],
        ["tease monkeys with sticks", "smile showing teeth", "wave food in monkey's face"],
        "Wildlife Institute of India (Human-Macaque Conflict Guidelines)", "https://wii.gov.in"
    ))

    # 6. ANI-006: Snakes in garden
    cards.append(make_card(
        "ANI-006", "paws", "Reptiles", "Snakes at home or garden: Calmness, distance and rescuer helplines",
        ["junior", "middle", "senior"],
        ["Snakes have zero interest in attacking humans; they only bite in self-defense when stepped on or cornered.",
         "Snakes are vital ecological allies that keep crop-destroying rodent populations under control."],
        ["Freeze and take slow steps backwards to maintain a safe 3-meter distance from the snake", "Keep family members, curious children, and domestic pets well away from the area", "Call a certified wildlife rescuer, local NGO, or Forest Department helpline to relocate the snake safely"],
        ["Never try to hit, kill, poke with sticks, or catch the snake yourself", "Never block the snake's exit route if it is trying to escape outside"],
        "If you see a snake in your garden, you must immediately beat it to death with bamboo sticks.", "myth", "Over 80% of snake bites happen when people attempt to corner and kill snakes. Give them space and call a rescuer.",
        "What is the single best response when you spot a snake in your home courtyard or garden?",
        ["Try to grab its tail", "Keep calm, step back at least 3 meters, keep pets away, and call a professional snake rescuer", "Pour kerosene on it", "Throw rocks"], 1,
        "Giving space prevents defensive strikes while a trained rescuer safely bags and relocates the snake.",
        ["In the backyard garden at {at}, {name} spots a 4-foot snake resting near the flowerpots."],
        "What is the safe, ecological response for {name}?",
        [("Keep calm and back away slowly to maintain a safe distance of at least 3-5 meters", "Removes strike hazard; snakes only strike when cornered.", True, "back away slowly|safe distance|3 meters|stay calm", 45),
         ("Alert adults and keep family dogs and curious children far away from the garden", "Secures human and pet safety.", True, "keep pets away|alert adults|clear area", 35),
         ("Call a certified local snake rescuer or Forest Department helpline for humane relocation", "Preserves wildlife without harm.", False, "call snake rescuer|forest helpline|relocate", 20)],
        ["attack snake with stick", "throw petrol on snake", "try to pick up snake"],
        "Forest Department Wildlife Rescue Guidelines", "https://moef.gov.in"
    ))

    # 7. ANI-007: Cattle on roads
    cards.append(make_card(
        "ANI-007", "paws", "Road animals", "Cattle and buffaloes on Indian roads: Wide berth and patience",
        ["junior", "middle", "senior"],
        ["Cattle have lateral monocular vision with a blind spot directly behind their tail.",
         "Loud, sudden horn blasts panic cows, causing erratic bolting across active traffic lanes."],
        ["Slow down your vehicle or cycle smoothly when approaching cattle sitting or walking on the road", "Give cattle a wide passing berth of at least 2 meters, especially avoiding walking right behind their rear hooves", "Do not honk aggressively; cows cannot move quickly on slippery asphalt roads"],
        ["Never slap, strike, or throw objects at cows crossing the road", "Never try to squeeze your bicycle between a moving cow and the road curb"],
        "Blaring your horn continuously an inch away from a sitting cow makes it stand up and move away faster.", "myth", "Loud horns disorient cattle, causing them to panic, kick backward, or bolt directly into oncoming cars.",
        "Where is a cow's natural blind spot located?",
        ["Directly in front of its nose", "Directly behind its tail (never approach quietly from directly behind)", "Above its head", "It has no blind spot"], 1,
        "Standing directly behind cattle risks unexpected defensive backward kicks.",
        ["Cycling home from school at {at}, two large cows are resting near the road divider ahead."],
        "How should {name} navigate past safely?",
        [("Slow down bicycle speed and observe the cows' movements calmly", "Prevents collision if an animal turns suddenly.", True, "slow down|observe calmly|safe speed", 40),
         ("Steer wide around the cattle giving at least 2 meters of clear breathing space", "Maintains safe standoff distance outside kick range.", True, "steer wide|wide berth|2 meters distance", 40),
         ("Do not ring bicycle bells aggressively right into the animals' ears", "Prevents startling animals into traffic lanes.", False, "no aggressive bell|patience", 20)],
        ["kick cow while cycling past", "honk bell an inch from ear", "squeeze dangerously between cow and divider"],
        "Ministry of Road Transport and Highways (Rural Road Safety)", "https://morth.nic.in"
    ))

    # 8. ANI-008: Injured bird
    cards.append(make_card(
        "ANI-008", "paws", "Avian care", "Rescuing an injured or heat-exhausted bird: Safe protocol",
        ["junior", "middle", "senior"],
        ["Injured birds suffer extreme stress; handling them improperly can break fragile hollow wing bones.",
         "A dark, quiet, well-ventilated cardboard box mimics natural shelter, lowering the bird's heart rate."],
        ["Gently cover the injured bird with a light cloth or towel and place it into a ventilated cardboard box", "Keep the box in a warm, quiet, dark room away from household cats, dogs, and loud noises", "Contact a local avian veterinarian, animal shelter, or wildlife rescue NGO immediately for medical care"],
        ["Never force water or milk down an unconscious or injured bird's beak (enters windpipe and drowns them)", "Never try to splint broken wings or pluck damaged feathers with home tweezers"],
        "If an injured bird is lying weak on the ground, you should pry open its beak and pour water down its throat.", "myth", "Forcing water into a bird's beak fills its tracheal airway, causing immediate asphyxiation and drowning.",
        "What is the safest immediate emergency shelter for an injured bird while waiting for a wildlife vet?",
        ["A wire cage with loud music", "A dark, warm cardboard box with air holes lined with a soft cloth", "Under a running tap", "In the freezer"], 1,
        "Darkness and quiet reduce physiological stress and shock in injured birds.",
        ["In the school courtyard at {at}, a pigeon or myna has struck a glass window and lies stunned on the ground."],
        "How should {name} render compassionate, correct first aid?",
        [("Gently pick up the bird using a clean cloth and place in a ventilated cardboard box", "Safe handling that prevents wing damage and reduces shock.", True, "ventilated cardboard box|cloth|gentle handling", 45),
         ("Keep the box in a dark, quiet place away from predatory cats and children", "Allows nervous system recovery from concussion.", True, "dark quiet place|away from cats|low stress", 35),
         ("Do NOT force liquids down its beak; call a local wildlife rescue NGO for treatment", "Prevents fatal aspiration drowning.", False, "no forced water|call wildlife rescue", 20)],
        ["pour water into beak", "throw bird into air to make it fly", "let cats play with it"],
        "Wildlife Trust of India (WTI Emergency Relief Network)", "https://wti.org.in"
    ))

    # 9. ANI-009: Zoo etiquette
    cards.append(make_card(
        "ANI-009", "paws", "Zoo ethics", "Zoo and wildlife park etiquette: Respecting captive animals",
        ["junior", "middle", "senior"],
        ["Animals in zoological parks suffer intense chronic stress when visitors scream, throw stones, or tap glass.",
         "Feeding human junk food (chips, biscuits) to captive animals causes fatal gastrointestinal blockages."],
        ["Observe zoo animals quietly from designated visitor pathways without shouting or making loud mock calls", "Keep all snack packets and plastic wrappers safely zipped inside bags (animals can swallow dropped wrappers)", "Respect safety barriers and moats: never climb over safety railings or lean over enclosures"],
        ["Never throw stones, plastic bottles, or coins into animal enclosures to make them move", "Never feed personal chips, popcorn, or bread to zoo animals"],
        "Throwing a small pebble at a sleeping lion in the zoo is fine because it wakes the animal for your photo.", "myth", "Throwing objects is illegal under the Wildlife Protection Act and causes severe stress and physical injury.",
        "Why is feeding snacks like chips or bread to animals in zoos strictly illegal?",
        ["Animals prefer cooking", "Human processed snacks cause severe digestive toxicity and plastic wrappers can choke animals", "It wastes money", "No reason"], 1,
        "Zoo animals require specialized species-appropriate diets; human junk food is toxic.",
        ["On a school excursion to the zoological park at {at}, some students want to throw chips to monkeys."],
        "What responsible wildlife ethics should {name} uphold?",
        [("Intervene firmly: 'Please don't feed the animals; processed human snacks make them critically sick'", "Stops harmful feeding and enforces zoo rules.", True, "don'?t feed animals|human food makes sick|zoo rules", 45),
         ("Keep all plastic snack packets zipped inside bags and dispose of trash in park dustbins", "Prevents plastic ingestion by wildlife.", True, "zip trash|use dustbins|no plastic in cages", 35),
         ("Observe animals quietly with respect without banging on glass or climbing safety barriers", "Maintains visitor safety and animal peace.", False, "quiet observation|respect barriers", 20)],
        ["throw stones at sleeping tiger", "feed plastic chips packet to bear", "climb over safety fence"],
        "Central Zoo Authority (CZA Visitor Guidelines)", "https://cza.nic.in"
    ))

    # 10. ANI-010: Bee nests
    cards.append(make_card(
        "ANI-010", "paws", "Pollinators", "Bee and wasp nests near home: Calm co-existence and safe removal",
        ["junior", "middle", "senior"],
        ["Honeybees are vital keystone pollinators responsible for pollinating over 70% of human food crops.",
         "Bees sting exclusively in defense of their colony when their hive is physically disturbed or threatened."],
        ["Keep a calm 5-meter distance from outdoor beehives and avoid throwing stones or poking with sticks", "Keep window wire mesh screens closed if a honeybee comb is located near your balcony", "If a hive must be removed, hire professional eco-friendly bee relocators who save the bees without burning them"],
        ["Never throw stones, spray chemical insecticides, or set fire to beehives (triggers mass defensive swarming)", "Never swat wildly at a single bee buzzing near you; stay still and let it fly away"],
        "If you see a honeybee nest on your apartment ledge, burning it with a fiery torch is the best solution.", "myth", "Setting fire to hives is cruel, destroys essential pollinators, and triggers hundreds of aggressive retaliatory stings.",
        "What should you do if a curious honeybee buzzes close to your head in a garden?",
        ["Scream and flail arms wildly", "Stay calm, keep still, and do not swat; the bee will realize you are not a flower and fly away", "Smack it with your phone", "Run fast"], 1,
        "Flailing arms alarms bees; staying calm and still signals you are not a threat.",
        ["A honeybee colony begins building a comb near a balcony window at {at}."],
        "How should {name} and family manage this safely and humanely?",
        [("Keep the window glass or mosquito mesh closed and do NOT disturb or throw objects at the hive", "Avoids provoking defensive swarming behavior.", True, "keep mesh closed|don'?t throw stones|do not disturb", 45),
         ("Understand that honeybees are precious pollinators essential for nature's food security", "Builds ecological reverence for pollinators.", True, "vital pollinators|nature balance|honeybees", 35),
         ("If removal is necessary, contact ethical beekeepers or professional wildlife relocators", "Ensures humane non-lethal colony relocation.", False, "ethical beekeeper|humane relocation|no burning", 20)],
        ["burn hive with fire torch", "spray lethal chemical pesticide", "poke hive with broomstick"],
        "National Bee Board (Department of Agriculture)", "https://nbb.gov.in"
    ))

    # 11. ANI-011: Rabies awareness
    cards.append(make_card(
        "ANI-011", "paws", "Zoonotic disease", "Rabies awareness: Transmission facts and zero delay in vaccination",
        ["junior", "middle", "senior"],
        ["Rabies travels along peripheral nerves to the central nervous system; once symptoms appear, fatality is nearly 100%.",
         "Timely post-exposure prophylaxis (washing + Anti-Rabies Vaccine series) is 100% effective in preventing the disease."],
        ["Understand that rabies can be transmitted by dogs, cats, monkeys, bats, and other warm-blooded mammals", "Know that even a minor scratch that breaks the skin or saliva on an open wound requires vaccine evaluation", "Complete the full 4-dose or 5-dose vaccine course on the exact scheduled days (Day 0, 3, 7, 14, 28)"],
        ["Never miss or delay scheduled vaccine booster dates recommended by the doctor", "Never wait to see if the biting animal survives before starting your own vaccination"],
        "Rabies can be cured easily with herbal pills even after symptoms of hydrophobia appear.", "myth", "Once clinical rabies symptoms appear, the disease is universally fatal. Immediate post-exposure vaccination is the ONLY prevention.",
        "What animal bite or scratch exposures require medical evaluation for anti-rabies vaccination?",
        ["Only tiger bites", "Any break in skin or scratch caused by dogs, cats, monkeys, or other mammals", "Mosquito bites", "Ant bites"], 1,
        "Any mammalian saliva contact with broken skin carries potential rabies risk and requires clinical assessment.",
        ["A friend at {at} was scratched by a stray cat 3 days ago but hasn't visited a clinic because 'it's just a cat.'"],
        "What urgent scientific counsel should {name} deliver?",
        [("Insist on visiting a medical doctor immediately for anti-rabies vaccination", "Timely post-exposure prophylaxis saves lives.", True, "visit doctor immediately|anti rabies vaccine|cat scratch counts", 45),
         ("Explain that rabies can be transmitted by cats and dogs alike through minor scratches", "Debunks dog-only rabies myths.", True, "transmitted by cats|mammals|rabies risk", 35),
         ("Emphasize that completing the full prescribed vaccine schedule guarantees complete protection", "Promotes complete vaccine adherence.", False, "complete vaccine schedule|100% effective", 20)],
        ["tell friend cat scratches are harmless", "apply herbal paste and ignore", "wait until fever starts"],
        "National Center for Disease Control (Rabies Prevention Protocols)", "https://ncdc.gov.in"
    ))

    # 12. ANI-012: Animal cruelty
    cards.append(make_card(
        "ANI-012", "paws", "Animal rights", "Stopping animal cruelty: The Prevention of Cruelty to Animals Act",
        ["junior", "middle", "senior"],
        ["The Prevention of Cruelty to Animals (PCA) Act 1960 makes beating, torturing, or abandoning animals illegal.",
         "Animal cruelty is recognized by psychologists as an early indicator of deep behavioral pathology and violence."],
        ["Treat all sentient animals with compassion, dignity, and kindness", "Speak up firmly if you see peers teasing, hitting, or tying firecrackers to street animals", "Report serious animal cruelty incidents to the local police (112), SPCA, or Animal Welfare Board"],
        ["Never throw stones at sleeping street dogs, cats, or birds for fun", "Never tie tin cans, plastic bags, or crackers to animals' tails"],
        "Street dogs have zero legal protections in India and anyone can beat or poison them freely.", "myth", "Maiming or killing street animals is a punishable criminal offense under Section 428/429 IPC and the PCA Act.",
        "What national legislation in India prohibits and punishes cruelty to animals?",
        ["Traffic Code", "The Prevention of Cruelty to Animals (PCA) Act 1960", "Building Code", "None"], 1,
        "The PCA Act 1960 protects all animals from unnecessary pain, suffering, and torture.",
        ["In a colony lane at {at}, {name} sees some older kids throwing stones at a mother dog and her puppies."],
        "How can {name} act as a courageous animal advocate?",
        [("Speak up firmly: 'Stop! Hurting defenseless animals is cruel and illegal under the law'", "Directly halts cruel behavior with authority.", True, "stop cruelty|illegal under law|protect animals", 45),
         ("Alert a trusted adult, society elder, or security guard to intervene", "Enlists adult authority to protect the puppies.", True, "alert adult|tell security|elder help", 35),
         ("Report repeated animal cruelty to local animal welfare NGOs or police 112", "Legal enforcement mechanism.", False, "report to police|112|animal welfare ngo", 20)],
        ["join in throwing stones", "film the cruelty for laughs", "ignore suffering animals"],
        "Animal Welfare Board of India (PCA Act Provisions)", "https://awbi.gov.in"
    ))

    # 13. ANI-013: Forest border wildlife
    cards.append(make_card(
        "ANI-013", "paws", "Coexistence", "Living near forest fringes: Leopards, elephants and safety rules",
        ["middle", "senior"],
        ["Human settlement expansion into forest fringes creates overlapping corridors with wild leopards and elephants.",
         "Wild animals avoid human interaction; conflict happens when humans surprise them in darkness or block migration paths."],
        ["Keep outdoor village and home perimeter areas brightly lit at night with solar lamps", "Never walk alone after dusk near forest edges; walk in groups making gentle vocal sounds (talking, singing)", "Inform the local Forest Department immediately if a wild animal is sighted near village settlements"],
        ["Never chase wild elephants or try to take close-up selfies with wild leopards", "Never corner or throw stones at a wild animal that has entered human habitation"],
        "Running towards a wild leopard with sticks and flashing phone cameras will scare it away safely.", "myth", "Surrounding and mobbing wild predators induces intense defensive panic, triggering fatal retaliatory attacks.",
        "What is the single most important safety rule when walking near forest border areas after dark?",
        ["Sneak in complete silence", "Travel in groups, carry a torch, and make audible vocal sounds (talking, singing)", "Wear bright green clothes", "Run fast alone"], 1,
        "Sound alerts wild animals from far away, allowing them to retreat into forest cover peacefully.",
        ["Visiting a village near a national park buffer zone at {at}, reports indicate a wild leopard is in the vicinity."],
        "What safety protocol should {name} follow?",
        [("Stay indoors after dusk and keep children and domestic animals inside securely", "Eliminates nocturnal encounter vulnerability.", True, "stay indoors after dusk|secure pets|keep children inside", 45),
         ("Keep outdoor compound lights on and avoid walking alone in dark sugarcane fields", "Illuminates surroundings and deters wildlife.", True, "keep lights on|no walking alone in dark", 35),
         ("Contact the local Forest Department range office for professional tracking and safe rescue", "Ensures scientific wildlife management.", False, "alert forest department|range office", 20)],
        ["go hunting the leopard with sticks", "take flash selfies with wild elephant", "leave toddlers outside in dark"],
        "Ministry of Environment, Forest and Climate Change (Project Tiger / Elephant)", "https://moef.gov.in"
    ))

    # 14. ANI-014: Kite manja & birds
    cards.append(make_card(
        "ANI-014", "paws", "Bird protection", "Kite strings (Manja): The invisible killer of urban birds",
        ["junior", "middle", "senior"],
        ["Glass-coated Chinese manja and nylon strings do not biodegrade, acting as razor-sharp airborne wire traps.",
         "Thousands of pigeons, kites, owls, and fruit bats suffer amputated wings and throat slits from tangled manja."],
        ["Fly kites exclusively with traditional, plain cotton thread (saddi) with zero glass or metal powder coating", "Fly kites in wide, open sports grounds far away from trees where birds roost and nest", "Pick up and safely dispose of tangled stray kite strings found dangling in bushes or trees"],
        ["Never use synthetic nylon or Chinese manja (strictly banned by the National Green Tribunal)", "Never fly kites near dawn and dusk when birds are actively flying to and from their nests"],
        "Synthetic glass-coated Chinese manja is totally legal and safe to use if you wear gloves.", "myth", "Synthetic manja is strictly banned across India; it slashes bird wings, kills two-wheeler riders, and conducts high-voltage electricity.",
        "What type of thread is safe, legal, and bird-friendly for flying kites during festivals?",
        ["Nylon fishing line", "Traditional plain cotton thread (saddi) without glass coating", "Glass-coated wire", "Copper string"], 1,
        "Plain cotton thread snaps under tension without slicing bird flesh or human throats.",
        ["During kite-flying festival celebrations at {at}, {name}'s friends want to buy sharp, banned nylon manja."],
        "How can {name} champion bird-safe skies?",
        [("Insist on flying kites only with traditional plain cotton thread (saddi)", "Eliminates razor-sharp slicing hazards for birds.", True, "plain cotton thread|saddi|no glass coating|bird safe", 45),
         ("Explain that synthetic Chinese manja is illegal and kills thousands of flying birds and motorists", "Highlights statutory ban and severe lethality.", True, "chinese manja is banned|kills birds|slashes wings", 35),
         ("Avoid flying kites near trees, rooftop power lines, or bird roosting colonies", "Reduces physical entanglement risks.", False, "away from trees|open ground", 20)],
        ["buy sharpest glass manja", "fly kites into bird flocks", "leave tangled manja in trees"],
        "National Green Tribunal (Ban on Synthetic Manja)", "https://greentribunal.gov.in"
    ))

    # 15. ANI-015: Pets & fireworks
    cards.append(make_card(
        "ANI-015", "paws", "Pet comfort", "Protecting pets and street animals during festival fireworks",
        ["junior", "middle", "senior"],
        ["Dogs and cats hear acoustic frequencies up to 45,000 Hz (humans hear max 20,000 Hz) with 4x acoustic sensitivity.",
         "High-decibel fireworks explosions cause severe acoustic trauma, heart tremors, and panic running into traffic."],
        ["Create a safe, cozy indoor sanctuary room: close windows, draw heavy curtains, and play soothing music/TV", "Keep pet dogs on a leash during festival evening walks; ensure they wear collars with ID tags and phone numbers", "Provide open stairwell or building compound shelter for terrified neighborhood street animals"],
        ["Never burst loud firecrackers near sleeping street animals or animal shelters", "Never lock a frightened pet outdoors on a balcony where they can leap over in panic"],
        "Dogs who shake and cower during Diwali crackers are just acting dramatic for attention.", "myth", "High-decibel explosions cause genuine physical agony, eardrum pain, and terrifying cardiac stress in animals.",
        "Why is it essential that pet dogs wear a collar with a phone ID tag during festival cracker season?",
        ["For fashion", "Panic from explosions causes hundreds of terrified pets to bolt from gates and get lost", "To look smart", "It is optional"], 1,
        "ID tags ensure lost, panicked pets can be quickly reunited with their families.",
        ["As evening festival fireworks begin at {at}, the family dog is trembling, panting, and hiding under the bed."],
        "How should {name} comfort and protect the pet?",
        [("Close all windows, draw curtains, and turn on soft background television or music to mask the noise", "Dampens external explosion acoustic spikes.", True, "close windows|draw curtains|soft music|mask noise", 45),
         ("Sit near the pet, speak in gentle reassuring tones, and provide a safe indoor den under blankets", "Provides emotional security without reinforcing panic.", True, "gentle reassuring tone|safe den|comfort pet", 35),
         ("Ensure all external doors and balcony railings are securely locked so pet cannot bolt in fear", "Prevents frantic escape and traffic accidents.", False, "secure doors|cannot bolt", 20)],
        ["drag trembling pet outside into fireworks", "tie crackers near dog", "lock dog on open balcony"],
        "Humane Society International (Animal Welfare Guidelines)", "https://hsi.org"
    ))

    # 16. ANI-016: Adopting Indies
    cards.append(make_card(
        "ANI-016", "paws", "Adoption", "Adopting Indie dogs: Natural resilience, loyalty and breaking breed bias",
        ["junior", "middle", "senior"],
        ["Indian Pariah and Indie community dogs have evolved naturally over thousands of years to thrive in the Indian climate.",
         "Foreign brachycephalic breeds (Pugs, Huskies, Bulldogs) suffer severe respiratory distress in hot Indian weather."],
        ["Adopt an Indian community dog from an animal shelter or rescue group instead of buying from commercial puppy mills", "Indie dogs possess exceptional genetic immunity, rarely suffer hereditary diseases, and live long, healthy lives", "Spay/neuter and vaccinate adopted Indie pets to support humane community dog population management"],
        ["Never buy Siberian Huskies or Saint Bernards in tropical Indian cities (it is cruelty to keep arctic dogs in 45°C heat)", "Never abandon pet dogs on the streets when they grow old or fall sick"],
        "Foreign pedigree breed dogs are naturally smarter and more loyal than Indian stray dogs.", "myth", "Indie dogs are among the most intelligent, resilient, loyal, and low-maintenance canine companions in the world.",
        "Why are native Indian street dogs ('Indies') ideally suited for Indian family homes?",
        ["They cost thousands of dollars", "They are naturally adapted to the Indian climate, have strong immune systems, and are fiercely loyal", "They never bark", "They eat plastic"], 1,
        "Centuries of natural selection give Indie dogs robust health, minimal genetic disorders, and natural heat tolerance.",
        ["A family at {at} is planning to get a pet dog and considers buying an expensive imported breed."],
        "What compassionate, logical case should {name} make?",
        [("Advocate for adopting a native Indie street dog or shelter rescue: 'Adopt, Don't Shop!'", "Saves a homeless animal and rejects commercial puppy mills.", True, "adopt don'?t shop|indie dog|shelter rescue|adopt local", 45),
         ("Explain that Indie dogs are naturally adapted to our climate and have robust genetic health", "Highlights superior climate resilience.", True, "adapted to climate|strong immunity|healthy", 35),
         ("Warn that keeping arctic breeds like Huskies in hot Indian weather causes severe thermal suffering", "Prevents cruelty to foreign breeds.", False, "no arctic breeds in heat|prevent cruelty", 20)],
        ["buy from illegal backyard breeder", "demand a husky in 48°C heat", "abandon old pet on road"],
        "Animal Welfare Board of India (Adopt Indies Campaign)", "https://awbi.gov.in"
    ))

    # 17. ANI-017: Heatwaves & wildlife
    cards.append(make_card(
        "ANI-017", "paws", "Summer relief", "Animals in extreme heatwaves: Water bowls, shade and heatstroke signs",
        ["junior", "middle", "senior"],
        ["Urban heat island effects push city surface temperatures over 50°C, causing widespread wildlife heat collapse.",
         "Dehydrated birds and street animals suffer kidney failure when clean drinking water is inaccessible."],
        ["Place wide terracotta water bowls outside your home, shops, and under shady colony trees daily", "Allow street dogs and cats to rest quietly in shaded building corridors, porticos, and basements during peak heat", "Notice heatstroke symptoms in animals: excessive panting, drooling, glassy eyes, and inability to stand up"],
        ["Never chase panting, heat-stressed animals out into scorching afternoon sun", "Never pour ice-cold freezing water directly over a heatstroked animal (triggers thermal shock)"],
        "Street animals never feel the summer heat because they have thick fur coats to protect them.", "myth", "Fur traps heat; street animals suffer intense dehydration, heat cramps, and heatstroke in peak summer.",
        "What is the simplest community service to save urban birds and street animals during scorching June heatwaves?",
        ["Spray perfume", "Place wide, clean water bowls in shady spots outside homes and refill daily", "Keep animals in sun", "None"], 1,
        "Shaded water bowls provide critical hydration that prevents fatal heatstroke in urban wildlife.",
        ["During a blistering 44°C heatwave day at {at}, {name} sees a panting street dog lying exhausted under a small tree."],
        "What compassionate care should {name} provide?",
        [("Provide a shallow bowl of clean, cool drinking water placed nearby in the shade", "Quenches dehydration without startling the animal.", True, "bowl of clean water|water in shade|hydration relief", 45),
         ("Allow the animal to rest peacefully in the shade without chasing it into hot sun", "Permits vital thermoregulation recovery.", True, "allow to rest|keep in shade|don'?t chase", 35),
         ("Apply a cool (not freezing) damp cloth to paw pads and belly if heat exhaustion is severe", "Aids safe external evaporative cooling.", False, "damp cloth on paws|cool down", 20)],
        ["pour boiling water on dog", "chase into burning sun", "throw stones at exhausted animal"],
        "PETA India Summer Animal Care Advisory", "https://petaindia.com"
    ))

    # 18. ANI-018: Plastic & cattle
    cards.append(make_card(
        "ANI-018", "paws", "Waste & animals", "Plastic menace for cattle: Rumen impaction and wet waste rules",
        ["junior", "middle", "senior"],
        ["Cows eat vegetable peelings discarded inside plastic carry bags because they smell the food inside.",
         "Plastic bags cannot be digested; they accumulate in the cow's rumen stomach into a 50 kg concrete-like mass."],
        ["Never discard kitchen vegetable scraps or leftover food sealed inside plastic carry bags", "Feed leftover vegetable peels to cattle in clean metal or bucket containers directly", "Segregate household waste into distinct wet and dry streams so plastic never mixes with organic food"],
        ["Never throw plastic-wrapped food into open garbage dumps accessible to grazing cattle", "Never throw sharp toothpicks, safety pins, or plastic cling film mixed with food waste"],
        "Cows have strong stomachs that can easily digest plastic bags and rubber wrappers safely.", "myth", "Plastic is completely indigestible. Hundreds of kilograms of plastic accumulate inside cows' stomachs, starving them to death.",
        "Why do urban cattle in India swallow dangerous plastic bags?",
        ["They like the taste of plastic", "People throw food scraps and vegetable peels tied inside plastic bags; cows swallow the whole bag to eat the food", "Plastic has vitamins", "No reason"], 1,
        "Cows smell the food inside thin polythene bags and swallow the entire plastic bag whole.",
        ["At home at {at}, someone is about to tie vegetable peelings inside a plastic bag and throw it into the dumpster."],
        "What ecological intervention should {name} make?",
        [("Stop them: 'Never throw food waste tied inside plastic bags; stray cows swallow the bags and die'", "Prevents fatal plastic rumen impaction in grazing cattle.", True, "no food in plastic bags|cows swallow plastic|rumen impaction|segregate", 45),
         ("Feed vegetable peelings directly to cattle in a clean trough, or add to your home compost bin", "Provides safe nourishment or organic soil building.", True, "feed directly without plastic|home compost|composting", 35),
         ("Ensure dry recyclable plastic is kept completely separate from wet organic kitchen waste", "Practices foundational source segregation.", False, "separate wet and dry waste|source segregation", 20)],
        ["tie food inside thick plastic knots", "throw batteries in cow feed", "dump plastic on grazing ground"],
        "Ministry of Fisheries, Animal Husbandry and Dairying", "https://dahd.nic.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Paws")
    return cards


def get_volt_cards():
    cards = []

    # 1. GRN-001: Solar PV
    cards.append(make_card(
        "GRN-001", "volt", "Solar energy", "How rooftop solar photovoltaic (PV) panels generate clean power",
        ["middle", "senior"],
        ["Solar photovoltaic (PV) cells contain semiconductor silicon that knocks electrons free when struck by sunlight.",
         "Rooftop solar generates zero carbon emissions during operation, replacing polluting thermal coal power."],
        ["Understand that rooftop solar panels convert sunlight directly into direct current (DC) electricity", "An inverter converts DC into alternating current (AC) to power household fans, lights, and computers", "Net-metering allows excess solar power generated during sunny afternoons to be exported back to the city grid"],
        ["Never walk or jump on solar glass panels (cracks micro-silicon cells and destroys efficiency)", "Never let thick layers of dust or bird droppings accumulate on panels (wash with clean water)"],
        "Solar panels only work on boiling hot summer days and stop producing electricity in winter.", "myth", "Solar panels operate on SUNLIGHT (photons), not heat. In fact, solar cells operate more efficiently in cool, sunny winter air.",
        "What device in a rooftop solar setup converts Direct Current (DC) from panels into Alternating Current (AC) for home appliances?",
        ["A toaster", "A solar inverter", "A battery charger only", "A transformer fuse"], 1,
        "The solar inverter converts DC generated by silicon cells into 230V AC used by household appliances.",
        ["{name}'s school or home at {at} is installing a 5-kilowatt rooftop solar system."],
        "What clean energy principles should {name} explain?",
        [("Rooftop silicon panels convert sunlight photons directly into clean electricity with zero emissions", "Explains photovoltaic physics and decarbonization.", True, "solar pv|photovoltaic|clean electricity|zero emissions", 45),
         ("The solar inverter transforms DC into AC, and net-metering exports surplus power to the grid", "Understands grid-tied system architecture.", True, "inverter|dc to ac|net metering|grid export", 35),
         ("Keep panels clean from dust and bird droppings with periodic water washing", "Maintains optimal energy generation yield.", False, "clean panels|wash dust|maintain efficiency", 20)],
        ["jump on solar glass", "claim solar pollutes like coal", "cover panels with blankets"],
        "Ministry of New and Renewable Energy (PM Surya Ghar Scheme)", "https://mnre.gov.in"
    ))

    # 2. GRN-002: Electric vehicles
    cards.append(make_card(
        "GRN-002", "volt", "Electric vehicles", "Electric vehicles (EVs): Tailpipe emissions and regenerative braking",
        ["middle", "senior"],
        ["Electric vehicles produce zero tailpipe emissions, eliminating street-level lung-damaging NO2 and PM2.5.",
         "Regenerative braking reverses electric motors during deceleration, capturing kinetic energy back into the battery."],
        ["Understand that electric scooters and cars use high-efficiency electric motors powered by lithium-ion battery packs", "Charge EVs using designated charging equipment and avoid using ungrounded makeshift extension cords", "Advocate for electric public transit (electric city buses and metro rail) to slash citywide air pollution"],
        ["Never leave EV battery chargers exposed to heavy rain without weatherproof protection", "Never use damaged, cracked, or punctured lithium battery packs"],
        "Electric vehicles cause identical street pollution as petrol cars because batteries burn fuel.", "myth", "EVs have zero tailpipe emissions; they produce zero toxic exhaust on city streets where children walk and breathe.",
        "What smart technology in electric vehicles recovers energy when the driver applies brakes?",
        ["Turbo boost", "Regenerative braking (converts kinetic stopping energy into stored battery charge)", "Air filter", "Nitrous boost"], 1,
        "Regenerative braking turns the motor into a generator, recharging batteries during slowing down.",
        ["A family at {at} is deciding between buying a petrol scooter or an electric scooter."],
        "What green tech benefits should {name} highlight?",
        [("Electric scooters have zero tailpipe emissions, keeping city street air clean for pedestrians", "Eliminates toxic urban exhaust emissions.", True, "zero tailpipe emissions|clean air|no petrol smoke", 45),
         ("EVs have significantly lower running and maintenance costs per kilometer compared to petrol", "Highlights compelling long-term economic advantages.", True, "lower running cost|cheaper per km|low maintenance", 35),
         ("Charge safely using certified wall chargers with proper electrical earthing", "Ensures electrical charging safety.", False, "safe charging|grounded socket", 20)],
        ["claim petrol smoke is healthy", "charge ev with damaged ungrounded wire", "puncture ev battery"],
        "NITI Aayog (Shoonya - Zero Pollution Mobility Campaign)", "https://shoonya.info"
    ))

    # 3. GRN-003: BEE Star labels
    cards.append(make_card(
        "GRN-003", "volt", "Energy efficiency", "BEE Star Energy Rating labels: Saving units and money",
        ["junior", "middle", "senior"],
        ["The Bureau of Energy Efficiency (BEE) rates household appliances from 1 Star (least efficient) to 5 Stars (most efficient).",
         "A 5-Star inverter air conditioner consumes up to 30% less electricity than a 1-Star model over its lifetime."],
        ["Look for the official red-and-white BEE Star Label when buying appliances (refrigerators, ACs, fans, geysers)", "Compare the 'Units / Year' (kWh) figure on the label to calculate actual annual electricity savings", "Encourage family to choose 5-Star rated appliances: higher star rating means lower electricity bills and lower coal burned"],
        ["Never peel off or ignore BEE energy efficiency labels on home appliances", "Never buy uncertified electrical appliances without genuine BEE rating logos"],
        "A 1-Star rated air conditioner cools the room much faster and stronger than a 5-Star rated model.", "myth", "Star ratings measure energy efficiency, not cooling power. A 5-Star AC cools identically while using significantly less electricity.",
        "What does a 5-Star rating on a Bureau of Energy Efficiency (BEE) label indicate?",
        ["The appliance is very noisy", "Maximum energy efficiency: consumes the lowest electricity to deliver the same performance", "It is made of gold", "It needs five batteries"], 1,
        "Higher star ratings denote superior technological efficiency and lower electricity consumption.",
        ["Shopping for a new family refrigerator or ceiling fan at {at}, the salesperson points to different models."],
        "How should {name} help the family choose wisely?",
        [("Check the BEE Star Rating label and select a high-efficiency 5-Star rated model", "Minimizes daily electricity consumption and utility costs.", True, "bee star label|5 star rating|energy efficiency|lower electricity", 45),
         ("Explain that higher initial cost is recovered within 1-2 years through significantly lower power bills", "Demonstrates lifecycle cost-benefit thinking.", True, "lower power bills|lifecycle savings|recovers cost", 35),
         ("Verify the official BEE logo and annual electricity consumption figure on the label", "Validates statutory certification.", False, "check bee logo|units per year", 20)],
        ["buy 1-star uncertified appliance", "ignore star labels completely", "claim efficiency doesn'?t matter"],
        "Bureau of Energy Efficiency (BEE India)", "https://beeindia.gov.in"
    ))

    # 4. GRN-004: LED lighting
    cards.append(make_card(
        "GRN-004", "volt", "Lighting tech", "Lighting efficiency: Why LEDs beat incandescent and CFL bulbs",
        ["junior", "middle", "senior"],
        ["Old incandescent bulbs waste 90% of electricity as useless heat, converting only 10% into light.",
         "Light Emitting Diodes (LEDs) consume 80% less power than incandescent bulbs and last over 25,000 hours."],
        ["Replace remaining incandescent yellow bulbs and fluorescent tubes with high-efficiency LED lights", "Switch off lights and fans every time you leave an empty room ('The Last Person Out Rule')", "Clean dust off LED light covers periodically to maximize brightness without increasing wattage"],
        ["Never leave room lights burning in broad daylight with curtains open", "Never dispose of old mercury-containing CFL tubes in household wet trash"],
        "Old yellow incandescent bulbs are much healthier for study rooms than modern energy-efficient LEDs.", "myth", "Incandescent bulbs waste 90% of power as heat and burn out quickly. Warm LEDs provide superior study lighting with 80% less power.",
        "What percentage of electricity did old-fashioned filament light bulbs waste as useless heat?",
        ["Only 1%", "Approximately 90% wasted as heat, producing only 10% light", "Zero percent", "50%"], 1,
        "Filament bulbs operate by thermal incandescence, wasting nearly all energy as radiated heat.",
        ["Replacing old lighting fixtures at home or school at {at}, {name} evaluates different bulb types."],
        "What green technology facts should {name} present?",
        [("Install energy-efficient LED bulbs that consume 80% less electricity than old filament bulbs", "Drastically cuts household lighting energy consumption.", True, "led bulbs|80 percent less energy|energy efficient lighting", 45),
         ("Highlight that LEDs last up to 25,000 hours, drastically reducing manufacturing waste", "Superior operational longevity.", True, "longer lifespan|25000 hours|less waste", 35),
         ("Establish a household habit: always switch off lights when exiting an empty room", "Builds daily conservation discipline.", False, "switch off lights|habit|save power", 20)],
        ["buy hot inefficient filament bulbs", "leave lights on all night in empty rooms", "smash cfl bulbs"],
        "UJALA Scheme (Energy Efficiency Services Limited - EESL)", "https://eeslindia.org"
    ))

    # 5. GRN-005: Wind & hydro
    cards.append(make_card(
        "GRN-005", "volt", "Renewables", "Harnessing wind and water: Kinetic energy converted to electricity",
        ["middle", "senior"],
        ["Wind turbines harness the kinetic energy of air currents to spin an electromagnetic generator.",
         "Hydroelectric plants use the gravitational potential energy of falling water to drive high-speed turbines."],
        ["Understand that wind and hydro are natural renewable resources that replenish without fuel combustion", "India is among the world's top 5 producers of wind energy, with major wind farms in Tamil Nadu and Gujarat", "Support clean grid integration: combining wind, hydro, and solar creates balanced 24/7 renewable power"],
        ["Never assume renewable energy can only come from rooftop solar panels", "Never ignore environmental safeguards needed when planning large hydro dams"],
        "Wind turbines consume massive amounts of diesel fuel to spin their blades on windy days.", "myth", "Wind turbines are spun 100% by natural aerodynamic wind lift, consuming zero fossil fuel.",
        "How do wind turbines generate electricity without burning any coal or gas?",
        ["They have secret engines", "Wind blows across aerodynamic blades, spinning a shaft connected to an electric generator", "They burn oil", "They store thunder"], 1,
        "Aerodynamic lift turns kinetic wind power into mechanical rotation, driving an electromagnetic generator.",
        ["Learning about India's renewable energy goals in science class at {at}, {name} explores green grid technologies."],
        "What comprehensive renewable understanding should {name} share?",
        [("Explain that wind turbines convert kinetic air movement directly into electricity without emissions", "Understands wind energy physics and clean generation.", True, "wind turbines|kinetic energy|clean power|no emissions", 45),
         ("Highlight that combining solar (daytime) with wind (evening/coastal) and hydro balances the grid", "Recognizes complementary renewable energy mix.", True, "energy mix|solar and wind|hydroelectric|balanced grid", 35),
         ("Note India's global leadership with over 180 GW of installed renewable energy capacity", "Fosters national pride in clean tech transitions.", False, "renewable capacity|india green transition", 20)],
        ["claim wind turbines need coal", "say renewables cannot power cities", "ignore clean energy"],
        "National Institute of Wind Energy (NIWE)", "https://niwe.res.in"
    ))

    # 6. GRN-006: Battery safety
    cards.append(make_card(
        "GRN-006", "volt", "Battery tech", "Lithium-ion battery care: Charging safety, swelling and recycling",
        ["junior", "middle", "senior"],
        ["Lithium-ion batteries store immense chemical energy; puncturing or crushing them causes violent thermal runaway.",
         "Charging devices on soft beds or under pillows traps heat, severely degrading battery lifespan and risking fires."],
        ["Charge phones and gadgets on hard, non-flammable surfaces (desks, tiles) with good air ventilation", "Stop using and safely isolate any battery that appears bloated, swollen, or smells strange", "Send dead batteries exclusively to certified e-waste recyclers to recover valuable lithium, nickel, and cobalt"],
        ["Never puncture, bend, hammer, or throw batteries into fire or water", "Never use cheap, uncertified counterfeit chargers with missing safety voltage regulators"],
        "Puncturing a swollen lithium battery with a pin is a great way to let the trapped air out safely.", "myth", "Puncturing an internal lithium cell creates a violent short-circuit that erupts into an instant, explosive chemical fireball.",
        "What should you do immediately if a phone or laptop battery starts swelling or bulging outward?",
        ["Poke it with a needle", "Disconnect charger immediately, stop using it, place in fire-safe area, and take to a certified technician", "Hit it with a hammer", "Put it in boiling water"], 1,
        "Swollen batteries indicate dangerous electrolyte breakdown and must be safely retired without puncturing.",
        ["While charging a portable gadget at {at}, {name} notices the plastic casing is warping and the battery is visibly swollen."],
        "What is the only safe procedure for {name}?",
        [("Unplug the charger immediately and do NOT continue using or charging the device", "Cuts off electrical energy supply before thermal runaway.", True, "unplug immediately|stop using|swollen battery|disconnect", 45),
         ("Place the swollen device on a non-flammable tile surface away from curtains and beds", "Isolates thermal risk.", True, "non-flammable surface|away from beds|isolate", 35),
         ("Do not puncture or squeeze the battery; take it to an authorized electronics repair center", "Prevents explosive short-circuit fire.", False, "do not puncture|authorized repair center", 20)],
        ["pierce swollen battery with pin", "charge overnight under pillow", "throw battery in dustbin"],
        "Bureau of Indian Standards (Battery Safety IS 16046)", "https://bis.gov.in"
    ))

    # 7. GRN-007: Fuel conservation
    cards.append(make_card(
        "GRN-007", "volt", "Conservation", "Fuel conservation: Carpooling, public transit and walking short trips",
        ["junior", "middle", "senior"],
        ["Private personal vehicles are responsible for over 40% of urban transportation greenhouse gas emissions.",
         "One fully loaded electric city bus replaces up to 40 personal private cars on congested roads."],
        ["Walk or ride a bicycle for short errands under 1-2 kilometers rather than asking for car rides", "Coordinate carpooling with neighborhood classmates to travel together in a single shared vehicle", "Choose metro trains and public buses whenever traveling across the city"],
        ["Never use a 1.5-tonne petrol car just to travel 500 meters to buy a single packet of milk", "Never idle vehicle engines while parked waiting for friends"],
        "Taking your own private car alone for every tiny 300-meter errand is a sign of high social status.", "myth", "Single-occupant car driving drives severe urban gridlock, local air toxicity, and global climate change.",
        "How many private cars can a single full city bus or metro train remove from congested roads?",
        ["Zero", "Up to 30 to 40 cars removed from the road", "Only half a car", "1 car"], 1,
        "Public mass transit dramatically multiplies transport fuel efficiency per passenger-kilometer.",
        ["Planning to visit a neighborhood market 800 meters away at {at}, family members consider taking the car."],
        "How can {name} promote green transit?",
        [("Suggest walking or riding bicycles together instead of taking the car for an 800-meter trip", "Cuts unnecessary fuel consumption and vehicle emissions.", True, "walk or cycle|short trip|leave car|save fuel", 45),
         ("Explain that short cold-engine car trips consume the highest fuel and cause high pollution", "Highlights mechanical fuel penalty of short drives.", True, "short trips waste fuel|cold engine pollution", 35),
         ("Enjoy the fresh air, active movement, and zero parking hassles of walking", "Promotes active sustainable living.", False, "active walking|zero parking hassle", 20)],
        ["drive large car 500 meters", "idle engine outside shop for 20 mins", "refuse to walk"],
        "Petroleum Conservation Research Association (PCRA Transport Tips)", "https://pcra.org"
    ))

    # 8. GRN-008: Green buildings
    cards.append(make_card(
        "GRN-008", "volt", "Architecture", "Green buildings: Natural daylighting, cross-ventilation and insulation",
        ["middle", "senior"],
        ["Traditional Indian vernacular architecture used courtyard 'jali' screens and high ceilings for natural cooling.",
         "Green buildings (GRIHA / LEED certified) reduce electricity and water consumption by 30% to 50%."],
        ["Open opposite windows during cool morning and evening hours to create natural cross-ventilation breezes", "Use natural daylight during study hours by placing study desks near windows, keeping lights off", "Install light-colored reflective roof coatings ('cool roofs') to bounce away scorching summer heat"],
        ["Never run air conditioners with windows wide open (forces compressors to run continuously at maximum power)", "Never rely entirely on artificial lighting during bright daytime hours"],
        "A modern building must be completely sealed with black glass windows and have ACs running 24/7.", "myth", "Sealed glass towers trap immense heat like greenhouses in Indian climates. Natural cross-ventilation is far cooler.",
        "What is the official national green building rating system developed in India by TERI and MNRE?",
        ["Star Wars", "GRIHA (Green Rating for Integrated Habitat Assessment)", "Cricket Board", "None"], 1,
        "GRIHA is India's indigenous national green building rating tool assessing sustainability from design to demolition.",
        ["Sitting in a dark room with lights on and curtains closed on a bright sunny afternoon at {at}."],
        "How can {name} practice green building principles at home?",
        [("Draw back the curtains and open windows to harness natural daylight and fresh air", "Eliminates daytime lighting electricity consumption.", True, "natural daylight|open curtains|turn off lights|fresh air", 45),
         ("Open opposite doors or windows to create natural cross-ventilation cooling breezes", "Replaces power-hungry air conditioning with natural ventilation.", True, "cross ventilation|natural breeze|cool room", 35),
         ("Learn how traditional Indian architecture (courtyards, jalis) cools homes naturally without AC", "Connects modern sustainability to indigenous wisdom.", False, "traditional architecture|jali|indigenous cooling", 20)],
        ["run AC with windows open", "turn on all electric lights in broad daylight", "block all ventilation"],
        "GRIHA (Green Rating for Integrated Habitat Assessment)", "https://grihaindia.org"
    ))

    # 9. GRN-009: Smart meters & phantom load
    cards.append(make_card(
        "GRN-009", "volt", "Efficiency", "Phantom power loads: Standby power waste and smart meters",
        ["middle", "senior"],
        ["Appliances left in 'Standby Mode' (TVs, microwaves, chargers, gaming consoles) consume 'vampire power'.",
         "Standby phantom loads account for up to 10% of an average household's total monthly electricity bill."],
        ["Switch off appliances at the primary wall switch instead of leaving them on remote standby", "Unplug laptop and mobile phone chargers when they are not actively charging a connected device", "Check your home's digital electricity meter to understand your family's kilowatt-hour (kWh) consumption"],
        ["Never leave gaming consoles or desktop computers running in sleep mode 24 hours a day", "Never leave phone chargers plugged in and switched on with no phone attached"],
        "When an appliance is turned off using its remote control, it consumes zero electricity from the wall.", "myth", "Remote standby keeps internal transformers and sensors energized, silently consuming vampire power 24/7.",
        "What is 'phantom power' or 'vampire load' in household electronics?",
        ["Spooky ghosts", "Electricity consumed by appliances when switched off by remote but still plugged in and on at the wall", "Solar power", "Static electricity"], 1,
        "Vampire loads continuously drain electricity to power standby indicator LEDs and digital clocks.",
        ["Leaving the living room at {at}, the television, gaming console, and phone chargers are all plugged in on standby."],
        "How can {name} eliminate phantom energy waste?",
        [("Switch off the main power switches on the wall sockets for the TV and gaming console", "Cuts off standby vampire power completely.", True, "switch off at wall|kill phantom load|cut standby power", 45),
         ("Unplug idle chargers that continue drawing small electrical currents when not in use", "Stops continuous transformer drain.", True, "unplug idle chargers|no vampire load", 35),
         ("Track monthly electricity meter bills to celebrate reduced kilowatt-hour (kWh) waste", "Measures tangible household energy conservation.", False, "track meter bill|save kwh", 20)],
        ["leave gaming console on standby 365 days", "leave 5 chargers plugged in always", "ignore energy waste"],
        "Bureau of Energy Efficiency (BEE Energy Conservation Guide)", "https://beeindia.gov.in"
    ))

    # 10. GRN-010: Biogas
    cards.append(make_card(
        "GRN-010", "volt", "Bioenergy", "Biogas technology: Converting organic waste and dung into clean fuel",
        ["junior", "middle", "senior"],
        ["Anaerobic digestion by methanogenic bacteria transforms animal dung and organic scraps into clean methane gas.",
         "Biogas replaces smoky firewood and coal in rural kitchens, preventing deadly indoor respiratory illness."],
        ["Understand that biogas digestors convert organic waste into clean cooking gas (methane) and rich organic fertilizer", "Support community biogas plants that process village cattle dung and school kitchen food scraps", "Use the nutrient-rich digested slurry as a chemical-free organic fertilizer for crops and gardens"],
        ["Never let untreated cattle dung or sewage pollute village drinking ponds and groundwater", "Never inhale concentrated biogas directly from digestor valves (displaces oxygen)"],
        "Biogas smells like raw sewage and produces dirty, black soot when burned on a kitchen stove.", "myth", "Biogas is predominantly methane, burning with a clean, smokeless blue flame identical to LPG.",
        "What natural biological process inside a sealed biogas plant converts organic waste into methane gas?",
        ["Photosynthesis", "Anaerobic digestion (fermentation by bacteria in the absence of oxygen)", "Combustion", "Evaporation"], 1,
        "Methanogenic bacteria break down complex organic polymers in oxygen-free tanks to produce methane.",
        ["Visiting a rural farm or school eco-project at {at}, {name} sees a Gobar Gas / Biogas digestor dome."],
        "What circular economy benefits should {name} explain?",
        [("The digestor turns cattle dung and organic waste into clean, smokeless methane cooking gas", "Explains renewable biofuel generation.", True, "biogas|methane gas|clean cooking fuel|gobar gas", 45),
         ("The leftover digested slurry serves as a superior, chemical-free organic fertilizer for soil", "Produces closed-loop bio-fertilizer.", True, "organic fertilizer|slurry|soil nutrients", 35),
         ("Biogas eliminates indoor smoke from burning firewood, protecting women's and children's lungs", "Promotes rural respiratory health.", False, "no smoke|protect lungs|clean energy", 20)],
        ["claim biogas is dirty soot", "dump raw dung in drinking well", "burn wood in unventilated room"],
        "Ministry of New and Renewable Energy (National Bioenergy Programme)", "https://mnre.gov.in"
    ))

    # 11. GRN-011: Recycling tech
    cards.append(make_card(
        "GRN-011", "volt", "Recycling technology", "How plastic recycling works: Shredding, melting and circular textiles",
        ["middle", "senior"],
        ["Mechanical recycling washes, shreds, and melts clean PET plastic bottles into reusable resin pellets.",
         "Recycled PET (rPET) pellets are extruded into fine polyester yarn used for sports jerseys, backpacks, and ropes."],
        ["Rinse and crush empty plastic bottles before disposing of them in dry recyclable waste bins", "Support circular products manufactured from verified post-consumer recycled plastic (rPET)", "Understand that dirty, contaminated plastic cannot be recycled and ends up incinerated or in landfills"],
        ["Never throw half-full milk packets or sticky food containers into dry paper recycling bins", "Never mix greasy food waste with clean plastic packaging"],
        "All types of plastic can be melted and remelted infinite times without ever degrading in quality.", "myth", "Plastic polymers degrade with each thermal recycling cycle (downcycling). Reducing plastic use is always primary.",
        "What high-performance product can clean recycled PET plastic drink bottles be turned into?",
        ["Organic food", "Recycled polyester textile yarn for sports jerseys and jackets", "Glass windows", "Water"], 1,
        "Clean PET bottles are shredded into flakes, melted, and spun into polyester textile fibers.",
        ["Finishing a bottle of water or juice at {at}, {name} prepares to discard the plastic container."],
        "How should {name} prep the bottle for high-grade mechanical recycling?",
        [("Empty any remaining liquid, rinse lightly, remove cap, and crush the bottle flat", "Prevents contamination and saves transport volume.", True, "rinse bottle|crush flat|dry waste bin|clean plastic", 45),
         ("Deposit it in the blue 'Dry Recyclable Waste' bin for formal kabadiwala collection", "Routes container into circular industrial recycling.", True, "dry waste bin|recyclable|kabadiwala", 35),
         ("Remember that reducing and refusing single-use plastic is always superior to recycling", "Upholds the waste hierarchy (Reduce > Reuse > Recycle).", False, "reduce first|waste hierarchy", 20)],
        ["throw half-full sticky bottle in paper bin", "burn bottle in garden", "litter on road"],
        "Central Pollution Control Board (Plastic Waste Management Division)", "https://cpcb.nic.in"
    ))

    # 12. GRN-012: RO reject water
    cards.append(make_card(
        "GRN-012", "volt", "Water efficiency", "RO water purifiers: Harvesting and reusing reject water",
        ["junior", "middle", "senior"],
        ["Household Reverse Osmosis (RO) purifiers reject 3 to 4 litres of water for every 1 litre of purified drinking water.",
         "Draining RO reject water straight into sewage pipes wastes over 60 litres of clean municipal water per home daily."],
        ["Route the RO reject wastewater pipe into a clean storage bucket or drum in your kitchen", "Use RO reject water for floor mopping, washing dirty utensils, cleaning balconies, or car washing", "Water sturdy garden plants with reject water (if Total Dissolved Solids / TDS is not excessively salty)"],
        ["Never let the RO reject pipe drain directly down the kitchen sink drainpipe into sewer lines", "Never drink RO reject water (it contains concentrated minerals and dissolved salts)"],
        "Reject water from household RO purifiers is toxic poisonous chemical waste that cannot be used for anything.", "myth", "RO reject water is simply concentrated mineral tap water; it is perfectly suited for mopping, washing, and cleaning.",
        "For every 1 litre of pure drinking water produced, approximately how much wastewater does a home RO purifier discard?",
        ["Zero litres", "About 3 to 4 litres of reject water discarded down the drain", "Only 1 drop", "50 litres"], 1,
        "RO membrane technology discards 75% of incoming water to wash concentrated salts away from membranes.",
        ["In the kitchen at {at}, {name} notices the thin white pipe of the RO purifier gushing water straight into the sink drain."],
        "What water-saving intervention should {name} make?",
        [("Place a clean bucket under the RO reject pipe to capture the discarded water", "Harvests dozens of litres of usable water daily.", True, "capture ro reject water|bucket under pipe|harvest wastewater", 45),
         ("Use the harvested reject water for washing utensils, mopping floors, or flushing toilets", "Replaces fresh municipal water for non-potable cleaning chores.", True, "floor mopping|flushing|washing utensils|cleaning", 35),
         ("Explain to family that throwing RO reject water down the drain wastes 60 litres daily", "Builds family conservation awareness.", False, "family conservation|stop waste", 20)],
        ["let pipe run down sink drain 24/7", "drink the salty reject water", "break the purifier"],
        "Central Ground Water Board (Water Conservation Guidelines)", "https://cgwb.gov.in"
    ))

    # 13. GRN-013: Green careers
    cards.append(make_card(
        "GRN-013", "volt", "Green careers", "Green tech careers: Solar engineers, EV designers and sustainability experts",
        ["middle", "senior"],
        ["The global transition to net-zero carbon is creating millions of high-growth 'green collar' careers.",
         "Green industries span renewable energy engineering, energy auditing, circular design, and environmental law."],
        ["Explore technical engineering degrees: Renewable Energy Engineering, Electrical & Battery Tech, or Environmental Science", "Develop skills in environmental impact assessment (EIA), ESG compliance, and energy simulation software", "Look into corporate sustainability: companies hire sustainability managers to decarbonize supply chains"],
        ["Never assume that caring for the planet means you can only volunteer for zero pay", "Never view green jobs as a niche charity sector; it is the dominant economic growth sector of this century"],
        "Careers in renewable energy and environment only offer low-paying volunteer jobs with no future.", "myth", "Solar technology, electric mobility, and grid analytics are multi-trillion-dollar industries hiring top engineers and leaders.",
        "Which of the following is a high-growth 'green collar' career contributing to clean technology?",
        ["Coal miner", "Battery Management System (BMS) Engineer / Renewable Grid Specialist", "Diesel mechanic", "Plastic bag printer"], 1,
        "EV battery design and renewable grid integration are among the fastest-growing engineering specialties globally.",
        ["A student in Class 11 at {at} loves physics and technology and wants a career that helps fight climate change."],
        "How can {name} introduce them to green tech pathways?",
        [("Highlight cutting-edge fields: Electric Vehicle Battery Engineering, Solar PV Architecture, and Smart Grids", "Connects technology interest with climate solutions.", True, "ev battery engineering|solar pv|smart grids|renewable energy", 45),
         ("Discuss emerging roles: ESG Sustainability Consultant, Environmental Law, and Carbon Accounting", "Expands perspective beyond traditional engineering.", True, "sustainability consultant|carbon accounting|esg", 35),
         ("Focus on strong fundamentals in mathematics, physics, and computer simulation modeling", "Prepares rigorous academic bedrock.", False, "maths and physics|simulation modeling|green collar", 20)],
        ["tell them green jobs don'?t exist", "push them into declining fossil fuel careers", "mock climate science"],
        "Skill Council for Green Jobs (SCGJ India)", "https://sscgj.in"
    ))

    # 14. GRN-014: Carbon footprint
    cards.append(make_card(
        "GRN-014", "volt", "Carbon footprint", "Understanding your carbon footprint: Food, travel and energy choices",
        ["junior", "middle", "senior"],
        ["A 'carbon footprint' is the total greenhouse gases (measured in kg of CO2 equivalent) generated by your daily actions.",
         "Major contributors to personal carbon footprints are electricity use, personal transport, food choices, and material goods."],
        ["Calculate your lifestyle carbon footprint using free online student carbon calculators", "Reduce travel footprint: walk, cycle, carpool, and prefer train travel over domestic flights where feasible", "Reduce food footprint: eat local seasonal produce and prevent plate food waste from rotting in landfills"],
        ["Never believe that individual conservation actions are useless; collective youth habits shift entire markets", "Never waste electricity and food thinking nature will replenish resources automatically"],
        "Your personal carbon footprint is fixed at birth and cannot be altered by your daily lifestyle choices.", "myth", "Switching to cycling, eating local produce, and turning off appliances can cut your personal footprint by over 40%",
        "Which of the following personal habits creates the largest reduction in an individual's carbon footprint?",
        ["Buying more plastic gadgets", "Walking/cycling for short trips, cutting food waste, and using energy-efficient appliances", "Leaving fans running", "Taking 3 flights a week"], 1,
        "Active mobility, food waste elimination, and electrical efficiency directly slash greenhouse emissions.",
        ["In environmental science class at {at}, {name} is learning about personal carbon footprints."],
        "How can {name} turn this knowledge into a practical daily action plan?",
        [("Audit personal daily habits: electricity use, short errand transport, and plate food waste", "Builds measurable personal awareness of emissions.", True, "audit daily habits|transport choices|food waste|electricity use", 45),
         ("Adopt active sustainable shifts: use cycles for local trips, switch off idle appliances, eat local food", "Translates awareness into direct carbon reductions.", True, "cycle local trips|switch off appliances|eat local food", 35),
         ("Encourage family and school to track energy conservation together for collective impact", "Amplifies individual impact to community scale.", False, "family conservation|school climate action", 20)],
        ["waste electricity freely", "dump half-eaten meals daily", "claim personal choices don'?t matter"],
        "Mission LiFE (Lifestyle for Environment - NITI Aayog)", "https://missionlife-moefcc.nic.in"
    ))

    # 15. GRN-015: Right to repair
    cards.append(make_card(
        "GRN-015", "volt", "Right to repair", "Right to Repair: Combating planned obsolescence in electronics",
        ["middle", "senior"],
        ["'Planned obsolescence' is when manufacturers intentionally design gadgets to be unrepairable, forcing new purchases.",
         "The Right to Repair framework empowers consumers to access spare parts, repair manuals, and third-party repair services."],
        ["Support the Right to Repair movement: buy electronics from brands that provide modular parts and repair guides", "Learn basic maintenance skills: replacing laptop batteries, cleaning fan dust, or changing phone screens", "Choose repair over premature replacement whenever an appliance or gadget malfunctions"],
        ["Never buy glued-together gadgets designed to be thrown away when a single sub-component fails", "Never discard electronics with simple fixable loose wires or worn-out batteries"],
        "Manufacturers make phones impossible to repair at local shops purely for your safety.", "myth", "Companies restrict repair manuals and glue batteries to force consumers into buying costly new upgrades every 2 years.",
        "What is the objective of the Government of India's 'Right to Repair' portal (righttorepairindia.gov.in)?",
        ["To sell new gadgets", "To ensure consumers and local repairers can access genuine spare parts, diagnostic tools, and manuals", "To ban electronics", "None"], 1,
        "The Right to Repair portal holds manufacturers accountable for providing repair documentation and spare parts.",
        ["A family laptop at {at} has a degraded battery that only lasts 15 minutes, and a salesman urges buying a new ₹60,000 laptop."],
        "How can {name} apply Right to Repair principles?",
        [("Check if the battery can be replaced by a local certified technician for a fraction of the cost", "Restores device functionality without expensive replacement.", True, "replace battery|repair laptop|fraction of cost|right to repair", 45),
         ("Explain that throwing away an entire working laptop for a worn battery generates toxic e-waste", "Highlights ecological impact of planned obsolescence.", True, "prevents e-waste|planned obsolescence|repair over replace", 35),
         ("Check the Department of Consumer Affairs Right to Repair portal for authorized repair options", "Utilizes official consumer protection frameworks.", False, "right to repair portal|consumer rights", 20)],
        ["throw working laptop in dustbin", "buy new laptop for simple dead battery", "burn old laptop"],
        "Department of Consumer Affairs (Right to Repair India Portal)", "https://righttorepairindia.gov.in"
    ))

    # 16. GRN-016: Solar thermal
    cards.append(make_card(
        "GRN-016", "volt", "Solar thermal", "Solar thermal energy: Solar water heaters and solar cookers",
        ["junior", "middle", "senior"],
        ["Solar thermal systems convert sunlight directly into heat energy without generating electricity first.",
         "A rooftop solar water heater replaces electric geysers, saving over 1,500 units of electricity per household annually."],
        ["Understand that solar water heaters use black evacuated glass tubes to absorb solar infrared heat directly into water", "Solar box cookers use mirrors and glass tops to slow-cook rice, dal, and vegetables with zero gas or firewood", "Support rooftop solar water heating in residential buildings and school hostels to cut peak winter electricity demands"],
        ["Never break or shatter evacuated solar glass tubes (maintain vacuum insulation)", "Never touch piping near solar collectors without testing (water reaches scalding 80°C temperatures)"],
        "Solar water heaters need electric heaters running underneath them to warm water on sunny winter days.", "myth", "Evacuated vacuum tubes absorb solar infrared radiation so efficiently that water boils naturally even in cold winter air.",
        "How much electricity can a 100-litre domestic rooftop solar water heater save in a year?",
        ["Zero units", "Approximately 1,500 kWh of electricity saved annually", "1 unit", "50,000 units"], 1,
        "Replacing electric resistance immersion geysers with solar thermal saves massive amounts of coal-fired grid power.",
        ["Looking at an evacuated tube solar water heater on a building terrace at {at}, {name} explains how it works."],
        "What thermal energy facts should {name} share?",
        [("Solar thermal collectors absorb infrared sunlight directly into water tubes with zero electricity used", "Explains direct thermal absorption efficiency.", True, "solar thermal|absorbs heat directly|no electricity used|evacuated tubes", 45),
         ("Rooftop solar water heaters save over 1,500 units of electricity per family each year", "Demonstrates massive energy and cost savings.", True, "saves 1500 units electricity|cuts power bills|replaces geyser", 35),
         ("Solar box cookers can bake and slow-cook meals using trapped greenhouse solar heat", "Introduces solar thermal cooking applications.", False, "solar cooker|slow cook|clean energy", 20)],
        ["break glass tubes", "claim solar heat doesn'?t work in winter", "use coal heater instead"],
        "Ministry of New and Renewable Energy (Solar Thermal Guidelines)", "https://mnre.gov.in"
    ))

    # 17. GRN-017: Digital carbon footprint
    cards.append(make_card(
        "GRN-017", "volt", "Digital energy", "The digital energy footprint: Data centers, video streaming and cloud storage",
        ["middle", "senior"],
        ["The internet and massive hyperscale data centers consume over 2% of the entire world's electricity.",
         "Streaming 4K video, storing thousands of unwanted cloud photos, and spam emails consume continuous server power."],
        ["Delete unwanted duplicate photos, massive unused cloud backup files, and unsubscribe from spam emails", "Lower video streaming resolution to 720p or 1080p when watching on small mobile phone screens (4K is invisible on tiny screens)", "Use local offline downloads over Wi-Fi instead of repeatedly streaming the same music tracks on cellular data"],
        ["Never leave video streams running in the background when nobody is watching the screen", "Never hoard thousands of junk unread promotional emails on cloud servers"],
        "Storing 50,000 unneeded blurry photos in the cloud consumes zero electricity because the cloud is in the sky.", "myth", "The 'cloud' is thousands of massive warehouse data centers packed with servers cooled by enormous air conditioners 24/7.",
        "Where does data stored in the 'cloud' actually live in the physical world?",
        ["In fluffy rain clouds", "Inside massive physical data center warehouses packed with servers running on electricity 24/7", "In space", "On telephone poles"], 1,
        "Cloud data requires continuous physical server power and massive chilling cooling systems.",
        ["Organizing their digital smartphone at {at}, {name} notices 15,000 duplicate blurry photos and 3,000 unread spam emails."],
        "How can {name} practice digital environmental hygiene?",
        [("Delete duplicate blurry photos and empty the trash folder to free up cloud server storage", "Reduces physical server storage and cooling power requirements.", True, "clean cloud storage|delete duplicate photos|digital cleanup", 45),
         ("Unsubscribe from junk marketing email lists and delete old promotional messages", "Stops ongoing data center processing loops.", True, "unsubscribe spam|delete junk emails|clean inbox", 35),
         ("Stream video at 1080p rather than 4K on small phone screens where quality difference is invisible", "Cuts data transfer bandwidth and transmission energy.", False, "stream 1080p|save bandwidth|conserve digital energy", 20)],
        ["leave 4k video playing while sleeping", "hoard 100,000 junk photos", "claim internet needs no power"],
        "International Energy Agency (Data Centres and Energy Use)", "https://iea.org"
    ))

    # 18. GRN-018: Renewable energy myths
    cards.append(make_card(
        "GRN-018", "volt", "Debunking myths", "Busting renewable energy myths: Storage, reliability and recycling",
        ["middle", "senior"],
        ["Modern grid-scale battery storage and pumped-hydro provide continuous power when the sun sets or wind calms.",
         "Solar panels pay back the energy used to manufacture them within 1 to 2 years, producing clean power for 25+ years."],
        ["Understand that renewable energy is now the cheapest source of new electricity generation in history", "Recognize that batteries, solar panels, and wind turbine components are recyclable in certified facilities", "Support decentralized microgrids that bring clean, reliable solar electricity to remote rural communities"],
        ["Never believe that the grid will crash if solar power exceeds 20% (modern smart inverters stabilize grids)", "Never believe that renewable energy technology causes more pollution than coal power"],
        "Renewable energy is so expensive that only rich Western countries can afford solar and wind power.", "myth", "Solar electricity costs have plunged by over 85% in the last decade; solar is now the cheapest electricity in India.",
        "How quickly does a modern solar photovoltaic panel generate back all the energy used to manufacture it?",
        ["It never does", "Within 1 to 2 years of operation, after which it produces clean net-positive power for 25+ years", "In 100 years", "In 50 years"], 1,
        "Solar panels have an Energy Payback Time (EPBT) of just 1-2 years, generating clean energy for decades thereafter.",
        ["In a classroom debate at {at}, an opponent claims solar energy is too unreliable and expensive to replace coal."],
        "How should {name} debunk this myth with scientific data?",
        [("Present data showing that solar energy is now the lowest-cost source of new electricity in India", "Cites official energy economics benchmarks.", True, "solar is cheapest electricity|costs plunged 85%|economic reality", 45),
         ("Explain that combining solar with wind, pumped hydro, and grid battery storage ensures 24/7 reliability", "Solves intermittency with modern grid architecture.", True, "grid battery storage|pumped hydro|wind mix|24/7 reliability", 35),
         ("Point out that over 90% of materials in solar panels (glass, aluminum, silicon) can be recycled", "Addresses circular recycling capabilities.", False, "recyclable materials|circular economy", 20)],
        ["agree that coal must burn forever", "claim solar doesn'?t work", "ignore clean energy economics"],
        "International Renewable Energy Agency (IRENA Renewable Power Generation Costs)", "https://irena.org"
    ))

    print(f"Loaded {len(cards)} expanded cards for Volt")
    return cards
