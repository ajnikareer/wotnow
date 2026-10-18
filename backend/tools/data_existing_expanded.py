"""
Data module for expanding the 8 existing agents:
Ember, Signal, Pulse, Basil, Civic, Terra, Cipher, Compass.
Adds 12 new cards to each existing agent (bringing each to 15-16 cards).
"""

def get_expanded_existing_cards():
    cards = {}

    # 1. EMBER (Fire Safety) - FIRE
    cards["ember"] = [
        {
            "id": "FIRE-021", "subtopic": "Gas leak", "title": "LPG gas cylinder leak smell",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "LPG has ethyl mercaptan added to give it a strong rotten-egg smell so leaks are noticed instantly.",
                "Any electrical switch (on or off) produces a tiny spark that can ignite accumulated LPG gas."
            ],
            "do": [
                "Open all doors and windows to let gas disperse",
                "Turn off the cylinder regulator valve if safely accessible",
                "Evacuate everyone from the house immediately and call 1906 / 112 from outside"
            ],
            "dont": [
                "Never turn any light or fan switch on or off",
                "Never light matches, candles or lighters anywhere near the house"
            ],
            "myths": [{"statement": "Switching on an exhaust fan helps clear LPG gas quickly.", "answer": "myth", "truth": "Flipping the exhaust switch creates an electrical spark that can ignite the gas. Open windows manually."}],
            "quiz": [{"q": "You smell strong LPG gas in the kitchen. What is the safest first action?", "options": ["Turn on the exhaust fan", "Open windows and do not touch any electrical switches", "Light a match to find the leak", "Spray water on the cylinder"], "correct": 1, "explanation": "Electrical switches cause sparks. Open windows naturally and never touch any switches."}],
            "scenario": {
                "situations": ["It's {time}. {name} enters the kitchen at home and notices a strong, pungent gas smell near the stove."],
                "question": "What should {name} do right now?",
                "emojis": ["🍳", "👃", "🚪"], "bubble": "Should I turn on the exhaust fan?!",
                "rubric": [
                    {"point": "Do not touch any switches, lighters, or flames", "note": "Sparks cause instant gas ignition.", "weight": 35, "critical": True, "keys": "(no|not|never|don'?t)[^.]{0,25}(switch|light|flame|exhaust|spark)"},
                    {"point": "Open all doors and windows for natural ventilation", "note": "Allows heavy LPG gas to flow outside.", "weight": 35, "critical": True, "keys": "open[^.]{0,20}(window|door)"},
                    {"point": "Turn off cylinder regulator and evacuate outside", "note": "Cuts off the fuel source and keeps family safe.", "weight": 30, "critical": False, "keys": "(turn|shut|close)[^.]{0,15}(regulator|valve)|(leave|evacuat|outside|call)"}
                ],
                "dangerous": ["(turn|switch)[^.]{0,10}on", "exhaust fan", "match", "lighter"]
            },
            "sources": [{"name": "Indian Oil Safety Manual", "url": "https://iocl.com"}]
        },
        {
            "id": "FIRE-022", "subtopic": "Personal fire", "title": "Clothes catching fire: Stop, Drop, and Roll",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "Running when clothes are on fire fans the flames and feeds them more oxygen.",
                "Rolling on the ground smothers flames by depriving them of air."
            ],
            "do": [
                "Stop moving immediately — do not run",
                "Drop to the ground and cover your face with your hands",
                "Roll back and forth until the flames are completely out"
            ],
            "dont": ["Never run when clothes are burning", "Don't peel off clothes stuck to burned skin"],
            "myths": [{"statement": "If your clothes catch fire, running to a bathroom is the best response.", "answer": "myth", "truth": "Running provides wind and oxygen that makes the fire burn faster. Stop, drop, and roll on the spot."}],
            "quiz": [{"q": "If a person's clothes catch fire, what should they do immediately?", "options": ["Run as fast as possible to water", "Stop, drop to the ground, and roll", "Wave their arms to blow it out", "Wrap up in synthetic blankets"], "correct": 1, "explanation": "Stop, Drop, and Roll cuts off the oxygen supply and puts out the flames."}],
            "scenario": {
                "situations": ["During a festival celebration at {at}, a stray spark lands on {name}'s sleeve and the fabric catches fire."],
                "question": "What must {name} do immediately?",
                "emojis": ["🔥", "🏃", "🛡️"], "bubble": "Should I run for water?!",
                "rubric": [
                    {"point": "Stop immediately without running", "note": "Running supplies oxygen and spreads flames.", "weight": 30, "critical": True, "keys": "stop|don'?t run|never run"},
                    {"point": "Drop to the ground and protect face", "note": "Keeps fire away from the face and lungs.", "weight": 35, "critical": True, "keys": "drop|ground|cover face"},
                    {"point": "Roll repeatedly until flames are extinguished", "note": "Smothers the fire against the ground.", "weight": 35, "critical": True, "keys": "roll|smother"}
                ],
                "dangerous": ["run[^.]{0,10}(fast|away|water)", "fan the flame"]
            },
            "sources": [{"name": "National Fire Protection Association", "url": "https://nfpa.org"}]
        },
        {
            "id": "FIRE-023", "subtopic": "Extinguishers", "title": "Using a fire extinguisher: The PASS method",
            "bands": ["middle", "senior"],
            "facts": [
                "Fire extinguishers are designed only for small, contained incipient-stage fires.",
                "PASS stands for: Pull the pin, Aim low at the base, Squeeze the lever, Sweep side to side."
            ],
            "do": [
                "Verify you have an unblocked exit route behind you before using",
                "Pull the safety pin and aim at the base of the fire",
                "Squeeze handle and sweep from side to side 6-8 feet away"
            ],
            "dont": ["Never aim high at the flames — aim at the base fuel", "Don't fight a fire that is taller than you or spreading"],
            "myths": [{"statement": "You should aim a fire extinguisher at the top tips of the flames.", "answer": "myth", "truth": "Aiming at the top does nothing. You must aim at the base of the fire where the fuel is."}],
            "quiz": [{"q": "What does the 'A' in the PASS fire extinguisher technique stand for?", "options": ["Aim at the base of the fire", "Ask for help", "Attack immediately", "Always spray high"], "correct": 0, "explanation": "A stands for Aim at the base of the fire, where the fuel source is burning."}],
            "scenario": {
                "situations": ["In the school science lab at {at}, a small wastepaper bin catches fire. An adult brings a dry powder fire extinguisher."],
                "question": "How should the extinguisher be operated using PASS?",
                "emojis": ["🧯", "🔥", "🏫"], "bubble": "How do we aim it?",
                "rubric": [
                    {"point": "Pull the safety pin to break the tamper seal", "note": "Releases the operating lever lock.", "weight": 30, "critical": False, "keys": "pull|pin|seal"},
                    {"point": "Aim low at the base of the flames", "note": "Directs extinguishing agent at the burning fuel.", "weight": 35, "critical": True, "keys": "aim[^.]{0,15}base|low"},
                    {"point": "Squeeze handle and sweep side to side", "note": "Covers the entire fire surface.", "weight": 35, "critical": True, "keys": "squeeze|sweep|side to side"}
                ],
                "dangerous": ["aim (high|top|flames)", "block the exit"]
            },
            "sources": [{"name": "Delhi Fire Service Guidelines", "url": "https://delhifireservice.gov.in"}]
        },
        {
            "id": "FIRE-024", "subtopic": "Evacuation", "title": "Testing closed doors during a fire",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "Opening a hot door can cause a backdraft or let deadly smoke and heat rush into the room.",
                "Use the back of your hand to feel the door and doorknob; the back of the hand is more sensitive and won't blister palm grip."
            ],
            "do": [
                "Feel the door, knob, and frame with the back of your hand before opening",
                "If it feels warm or hot, keep it closed and use your secondary escape route",
                "Seal cracks around closed doors with cloth or towels to block smoke"
            ],
            "dont": ["Never touch a door with an open palm", "Never fling open a warm door"],
            "myths": [{"statement": "If a closed door is hot, opening it slightly to peek is safe.", "answer": "myth", "truth": "Opening a hot door feeds oxygen to the fire and allows toxic smoke to engulf you immediately."}],
            "quiz": [{"q": "How should you test a closed door before opening it during a fire alarm?", "options": ["Turn the knob quickly and look", "Feel the door and knob with the back of your hand", "Kick the door open", "Smell the keyhole"], "correct": 1, "explanation": "Touch the door and knob with the back of your hand. If hot, do not open it."}],
            "scenario": {
                "situations": ["The building fire alarm sounds at {at}. {name} reaches the bedroom door to exit into the corridor."],
                "question": "What must {name} do before opening the door?",
                "emojis": ["🚪", "✋", "🏃"], "bubble": "Should I just run outside?",
                "rubric": [
                    {"point": "Touch the door and handle with the back of the hand", "note": "Tests for heat safely without blistering palms.", "weight": 40, "critical": True, "keys": "back of (the )?hand|feel|touch door"},
                    {"point": "Do not open if warm or hot", "note": "Indicates active fire on the other side.", "weight": 30, "critical": True, "keys": "(if hot|if warm)[^.]{0,25}(don'?t open|keep closed|seal)"},
                    {"point": "Use alternate exit or seal gaps and signal for help", "note": "Prevents smoke inhalation.", "weight": 30, "critical": False, "keys": "alternate|window|signal|seal|cloth|towel"}
                ],
                "dangerous": ["open (the )?door right away", "kick door"]
            },
            "sources": [{"name": "NDMA Fire Safety Advisory", "url": "https://ndma.gov.in"}]
        }
    ]

    # 2. SIGNAL (Road Safety) - ROAD
    cards["signal"] = [
        {
            "id": "ROAD-022", "subtopic": "Two-wheeler", "title": "Pillion passenger safety rules",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "Pillion riders face the same risk of head injury as drivers in a collision.",
                "Sitting with both legs on one side (side-saddle) severely compromises balance during sudden braking."
            ],
            "do": [
                "Wear an approved ISI-marked helmet with chin strap securely fastened",
                "Sit astride facing forward with one leg on each footrest",
                "Hold firmly onto the rider's waist or motorcycle grab rail"
            ],
            "dont": ["Never sit sideways without a footrest", "Never ride without strapping your helmet"],
            "myths": [{"statement": "Only the person driving a scooter needs to wear a helmet.", "answer": "myth", "truth": "Pillion passengers have an equal risk of head injury and are legally required to wear a helmet."}],
            "quiz": [{"q": "What is the safest way to sit as a pillion passenger on a two-wheeler?", "options": ["Sitting sideways for comfort", "Astride facing forward with both feet on footrests and a strapped helmet", "Standing on the back footrests", "Sitting without holding on"], "correct": 1, "explanation": "Astride posture ensures balance and an ISI helmet protects against traumatic head injury."}],
            "scenario": {
                "situations": ["{relation} offers {name} a ride on a scooter to school at {at}."],
                "question": "What must {name} check before getting on the scooter?",
                "emojis": ["🛵", "⛑️", "🎒"], "bubble": "Can I just hop on?",
                "rubric": [
                    {"point": "Wear an ISI-certified helmet and fasten the chin strap", "note": "Unstrapped helmets fly off on impact.", "weight": 40, "critical": True, "keys": "helmet|strap|isi"},
                    {"point": "Sit astride with feet on footrests facing forward", "note": "Maintains balance on sudden turns or stops.", "weight": 30, "critical": True, "keys": "astride|both sides|footrest|facing forward"},
                    {"point": "Hold the grab rail or driver securely", "note": "Prevents falling off during acceleration.", "weight": 30, "critical": False, "keys": "hold|grab rail|waist"}
                ],
                "dangerous": ["no helmet", "sit sideways", "stand on"]
            },
            "sources": [{"name": "Ministry of Road Transport and Highways (MoRTH)", "url": "https://morth.nic.in"}]
        },
        {
            "id": "ROAD-023", "subtopic": "Railway tracks", "title": "Railway tracks and level crossing safety",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "Trains travel at high speeds and can take up to 1 kilometer to come to a full stop.",
                "Walking on tracks or crossing closed level crossings is illegal and the leading cause of rail fatalities."
            ],
            "do": [
                "Always use designated Foot Over Bridges (FOBs) or subways to cross tracks",
                "Wait patiently behind closed railway crossing gates until the train passes and gates fully reopen",
                "Remove headphones and stay alert near railway stations and platforms"
            ],
            "dont": ["Never duck under closed railway crossing gates", "Never walk or take selfies on railway tracks"],
            "myths": [{"statement": "You will easily hear an approaching train from far away.", "answer": "myth", "truth": "Modern electric trains are surprisingly quiet from the front until they are dangerously close."}],
            "quiz": [{"q": "A railway crossing gate is down with red lights flashing. What should you do?", "options": ["Duck under the gate if no train is in sight", "Wait behind the barrier until the gate is fully opened", "Walk across the tracks quickly", "Follow others crossing"], "correct": 1, "explanation": "Never bypass closed gates. Trains approach faster than perceived and gates open only when safe."}],
            "scenario": {
                "situations": ["On the way home from school, {name} reaches the local railway crossing. The barrier is closed and some cyclists are ducking underneath."],
                "question": "What is the only safe choice for {name}?",
                "emojis": ["🚆", "🚧", "🚶"], "bubble": "Should I follow them under the gate?",
                "rubric": [
                    {"point": "Wait patiently behind the closed crossing gate", "note": "Ducking under closed barriers is illegal and fatal.", "weight": 45, "critical": True, "keys": "wait|stay behind|don'?t cross|do not duck"},
                    {"point": "Do not walk on or cross active railway tracks", "note": "Trains cannot stop quickly for pedestrians.", "weight": 35, "critical": True, "keys": "no tracks|fob|foot overbridge|bridge"},
                    {"point": "Keep headphones off and stay attentive", "note": "Ensures horns and warning bells are heard.", "weight": 20, "critical": False, "keys": "headphones off|alert|listen"}
                ],
                "dangerous": ["duck under", "cross (the )?tracks", "run across"]
            },
            "sources": [{"name": "Indian Railways Safety Directorate", "url": "https://indianrailways.gov.in"}]
        },
        {
            "id": "ROAD-024", "subtopic": "Monsoon roads", "title": "Waterlogged roads and open drains in monsoon",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "Muddy rainwater conceals open manholes, missing drain covers, and dangerous potholes.",
                "Fallen electrical wires in pooled water can electrocute people several meters away."
            ],
            "do": [
                "Avoid walking through standing or flooded water whenever possible",
                "Use an umbrella or stick to test ground depth before stepping if walking is unavoidable",
                "Stay clear of electric poles, transformers, and submerged cables"
            ],
            "dont": ["Never wade through deep rainwater on foot", "Never touch electric poles or fallen wires in wet weather"],
            "myths": [{"statement": "If others are wading through knee-deep water, it is safe to follow.", "answer": "myth", "truth": "Floodwater can wash away manhole lids at any moment. Hidden currents and electrocution hazards remain invisible."}],
            "quiz": [{"q": "While walking home in heavy rain, the road ahead is flooded with murky water. What should you do?", "options": ["Wade straight through the middle", "Find an alternate higher route or wait safely in a sheltered shop", "Jump into the water to test depth", "Touch an electric pole for balance"], "correct": 1, "explanation": "Murky water hides missing manhole covers and electrical current leaks. Find a higher, dry route."}],
            "scenario": {
                "situations": ["After sudden monsoon rain at {at}, the street outside school is flooded with murky knee-deep water."],
                "question": "How should {name} navigate this safely?",
                "emojis": ["🌧️", "🌊", "🚶"], "bubble": "Can I just wade through?",
                "rubric": [
                    {"point": "Avoid wading through deep or murky floodwater", "note": "Hides open drains, potholes, and broken glass.", "weight": 40, "critical": True, "keys": "avoid|don'?t wade|alternate|higher ground|wait"},
                    {"point": "Stay far away from electric poles, cables, and transformers", "note": "Prevents fatal electrocution through water.", "weight": 40, "critical": True, "keys": "electric pole|wire|cable|transformer|shock"},
                    {"point": "Inform parents or wait with teachers until safe", "note": "Adult guidance ensures safe transport home.", "weight": 20, "critical": False, "keys": "call parent|tell adult|wait with teacher"}
                ],
                "dangerous": ["wade through", "touch (electric )?pole", "swim"]
            },
            "sources": [{"name": "National Disaster Management Authority (NDMA)", "url": "https://ndma.gov.in"}]
        }
    ]

    # 3. PULSE (First Aid) - AID
    cards["pulse"] = [
        {
            "id": "AID-022", "subtopic": "Bleeding", "title": "Cuts and severe bleeding first aid",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "Firm direct pressure with a clean cloth stops over 90% of bleeding by allowing platelets to clot.",
                "Removing a soaked cloth tears away developing clots; instead, add another cloth on top."
            ],
            "do": [
                "Press firmly directly on the wound using a clean cloth or bandage",
                "Maintain steady pressure without peeking for at least 5-10 minutes",
                "Elevate the injured limb above heart level if possible and get adult help"
            ],
            "dont": ["Never use mud, turmeric, or leaves on open cuts", "Never pull out an embedded object like glass"],
            "myths": [{"statement": "Applying turmeric or coffee powder directly into a deep cut stops bleeding safely.", "answer": "myth", "truth": "Home powders cause severe contamination and infections. Use clean direct pressure."}],
            "quiz": [{"q": "A classmate gets a deep cut that is bleeding heavily. What is the immediate first aid?", "options": ["Apply direct firm pressure with a clean cloth", "Pour turmeric powder into the cut", "Tie a rope tightly around the neck", "Wash with hot water"], "correct": 0, "explanation": "Continuous direct pressure with clean cloth compresses blood vessels and enables natural clotting."}],
            "scenario": {
                "situations": ["While working on a craft project at {at}, a cutter slips and {name}'s friend cuts their hand deeply with heavy bleeding."],
                "question": "What first aid should {name} provide right now?",
                "emojis": ["🩹", "🩸", "🧒"], "bubble": "Should I put haldi on it?",
                "rubric": [
                    {"point": "Apply firm direct pressure with a clean cloth or gauze", "note": "Direct pressure is the primary method to control bleeding.", "weight": 40, "critical": True, "keys": "direct pressure|press|clean cloth|bandage|gauze"},
                    {"point": "Do not remove soaked cloth; add more on top", "note": "Preserves newly formed blood clots.", "weight": 25, "critical": False, "keys": "don'?t remove|keep pressing|add on top"},
                    {"point": "Call a teacher or adult and seek medical attention", "note": "Deep wounds may require stitches or tetanus shots.", "weight": 35, "critical": True, "keys": "call adult|teacher|doctor|nurse|108|112"}
                ],
                "dangerous": ["turmeric|haldi|coffee", "tie tightly around neck", "wash hot"]
            },
            "sources": [{"name": "Indian Red Cross Society First Aid Manual", "url": "https://indianredcross.org"}]
        },
        {
            "id": "AID-023", "subtopic": "Animal bite", "title": "Dog bite and scratch protocol",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "Rabies virus is transmitted through animal saliva and is almost 100% fatal once symptoms appear.",
                "Immediate thorough washing with running water and soap dramatically reduces virus transmission."
            ],
            "do": [
                "Wash the wound immediately under running tap water with soap for at least 15 minutes",
                "Apply an antiseptic like povidone iodine after washing",
                "Go to a hospital or doctor the same day for anti-rabies vaccination (PEP)"
            ],
            "dont": ["Never apply chili powder, lime, or bandages tightly over the bite", "Never delay medical care"],
            "myths": [{"statement": "A scratch from a puppy doesn't require a doctor visit.", "answer": "myth", "truth": "Any break in skin from dogs or cats carries rabies risk. Always wash thoroughly and visit a doctor the same day."}],
            "quiz": [{"q": "What is the crucial first aid step immediately after a street dog bites or scratches you?", "options": ["Wash under running water with soap for 15 minutes", "Tie a bandage tightly and sleep", "Apply mustard oil", "Wait 10 days to see if sick"], "correct": 0, "explanation": "Washing with soap and water for 15 minutes removes saliva and physically inactivates the rabies virus."}],
            "scenario": {
                "situations": ["While playing in the park at {at}, a friendly stray dog gets startled and bites {name}'s calf, breaking the skin."],
                "question": "What must {name} do right away?",
                "emojis": ["🐕", "💧", "🩺"], "bubble": "Should we bandage it immediately?",
                "rubric": [
                    {"point": "Wash with soap and running water for at least 15 minutes", "note": "Soap breaks down the lipid envelope of the rabies virus.", "weight": 45, "critical": True, "keys": "wash[^.]{0,25}(soap|water)|running water|15 min"},
                    {"point": "Do not tie tightly or apply chili/herbs", "note": "Irritants worsen tissue damage.", "weight": 20, "critical": False, "keys": "no bandage|no chili|no haldi"},
                    {"point": "Visit doctor the same day for rabies vaccination", "note": "Post-exposure prophylaxis saves lives.", "weight": 35, "critical": True, "keys": "doctor|hospital|rabies|vaccin|same day|injection"}
                ],
                "dangerous": ["chili|haldi|lime", "bandage tightly", "ignore|wait"]
            },
            "sources": [{"name": "National Centre for Disease Control (NCDC)", "url": "https://ncdc.gov.in"}]
        },
        {
            "id": "AID-024", "subtopic": "Unconsciousness", "title": "Fainting and recovery position",
            "bands": ["junior", "middle", "senior"],
            "facts": [
                "Fainting (syncope) happens when blood flow to the brain drops temporarily.",
                "Laying a person flat and elevating their feet restores blood circulation to the brain quickly."
            ],
            "do": [
                "Lay the person flat on their back and elevate feet 12 inches (30 cm)",
                "Loosen tight collars, ties, and belts for easy breathing",
                "Turn onto recovery side position if they vomit or don't regain consciousness within 1 minute"
            ],
            "dont": ["Never make a fainting person sit up quickly", "Never splash water in their face or force liquids into their mouth"],
            "myths": [{"statement": "Giving water to an unconscious person will wake them up.", "answer": "myth", "truth": "Liquids given to an unconscious person can enter their windpipe and choke them."}],
            "quiz": [{"q": "A student faints during morning school assembly. What is the correct first action?", "options": ["Force them to drink water immediately", "Lay them flat on their back and raise their feet", "Slap their cheeks", "Hold them upright"], "correct": 1, "explanation": "Laying them flat and raising feet redirects blood back to the brain."}],
            "scenario": {
                "situations": ["During school sports day at {at}, a classmate collapses and faints onto the grass."],
                "question": "What is the proper first response for {name}?",
                "emojis": ["😵", "🦶", "🩺"], "bubble": "Should I pour water in their mouth?",
                "rubric": [
                    {"point": "Lay flat on back and elevate legs/feet", "note": "Promotes venous blood return to the brain.", "weight": 40, "critical": True, "keys": "lay flat|raise (legs|feet)|elevate"},
                    {"point": "Loosen tight clothing and ensure fresh air", "note": "Clears airway and prevents overheating.", "weight": 25, "critical": False, "keys": "loosen|collar|fresh air|crowd back"},
                    {"point": "Do not give food or drink while unconscious; get medical help", "note": "Prevents choking and aspiration.", "weight": 35, "critical": True, "keys": "(no|don'?t)[^.]{0,15}(water|drink)|call nurse|doctor|108|112"}
                ],
                "dangerous": ["force (water|liquid)", "slap", "stand up"]
            },
            "sources": [{"name": "World Health Organization (WHO) Basic First Aid", "url": "https://who.int"}]
        }
    ]

    return cards
