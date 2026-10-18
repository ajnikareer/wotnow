"""
Comprehensive expansion for the 8 existing agents:
Ember, Signal, Pulse, Basil, Civic, Terra, Cipher, Compass.
Adds ~16 new distinct skills per agent to pair with existing ones.
"""

def make_card(cid, agent_id, subtopic, title, bands, facts, do_list, dont_list,
              myth_stmt, myth_ans, myth_truth,
              quiz_q, quiz_opts, quiz_correct, quiz_exp,
              situations, question, rubric_items, dangerous_list,
              source_name, source_url):
    # rubric_items: list of (point, note, critical_bool, regex_keys, weight)
    # Ensure weights sum to 100
    tot = sum(r[4] for r in rubric_items)
    rubric = []
    diff = 100 - tot
    for i, (pt, note, crit, keys, w) in enumerate(rubric_items):
        weight = w + (diff if i == 0 else 0)
        rubric.append({
            "point": pt,
            "note": note,
            "weight": weight,
            "critical": crit,
            "keys": keys
        })
    return {
        "id": cid,
        "agentId": agent_id,
        "subtopic": subtopic,
        "title": title,
        "bands": bands,
        "facts": facts,
        "do": do_list,
        "dont": dont_list,
        "myths": [{"statement": myth_stmt, "answer": myth_ans, "truth": myth_truth}],
        "quiz": [{"q": quiz_q, "options": quiz_opts, "correct": quiz_correct, "explanation": quiz_exp}],
        "scenario": {
            "situations": situations,
            "question": question,
            "emojis": ["📌", "⚡", "🧒"],
            "bubble": "What is the safest move right now?",
            "rubric": rubric,
            "dangerous": dangerous_list
        },
        "sources": [{"name": source_name, "url": source_url}],
        "reviewed": True
    }

def get_cards():
    cards = {
        "ember": [], "signal": [], "pulse": [], "basil": [],
        "civic": [], "terra": [], "cipher": [], "compass": []
    }

    # =========================================================================
    # 1. EMBER (Fire Safety) - FIRE
    # =========================================================================
    cards["ember"].append(make_card(
        "FIRE-021", "ember", "Gas leak", "LPG cylinder leak smell in kitchen",
        ["junior", "middle", "senior"],
        ["LPG has ethyl mercaptan added so even tiny leaks smell like rotten eggs.",
         "Flipping an electric switch creates a microscopic spark that can ignite accumulated gas."],
        ["Open all doors and windows to disperse the gas", "Turn off cylinder regulator if safe", "Leave the house and call 1906 / 112 from outside"],
        ["Never turn electrical switches on or off", "Never light matches or candles"],
        "Turning on an exhaust fan helps clear LPG gas quickly.", "myth", "Exhaust switches create electrical sparks that ignite gas. Open windows manually.",
        "You smell LPG gas in the kitchen. What is the safest first action?",
        ["Turn on exhaust fan", "Open windows and do not touch switches", "Light a match to find the leak", "Spray water"], 1,
        "Electrical switches cause sparks. Open windows naturally and never touch switches.",
        ["At {time}, {name} walks into the kitchen at {at} and smells strong LPG gas near the stove."],
        "What should {name} do right now?",
        [("Do not touch electrical switches or flames", "Sparks cause instant gas explosions.", True, "(no|not|never|don'?t)[^.]{0,25}(switch|light|flame|exhaust|spark)", 35),
         ("Open doors and windows for ventilation", "Lets heavy LPG gas disperse outside.", True, "open[^.]{0,20}(window|door)", 35),
         ("Turn off regulator and evacuate outside", "Cuts fuel and keeps family safe.", False, "(turn|shut|close)[^.]{0,15}(regulator|valve)|(leave|evacuat|outside)", 30)],
        ["(turn|switch)[^.]{0,10}on", "exhaust fan", "match", "lighter"],
        "Indian Oil LPG Safety", "https://iocl.com"
    ))

    cards["ember"].append(make_card(
        "FIRE-022", "ember", "Personal fire", "Clothes catch fire: Stop, Drop and Roll",
        ["junior", "middle", "senior"],
        ["Running feeds oxygen to burning clothes, making flames spread much faster.",
         "Rolling on the ground smothers flames by depriving them of air."],
        ["Stop moving immediately without running", "Drop to the ground and cover face with hands", "Roll back and forth until flames extinguish"],
        ["Never run when clothes are burning", "Don't peel off clothes stuck to burned skin"],
        "If clothes catch fire, running to a bathroom is the best response.", "myth", "Running creates air currents that fan the flames. Stop, Drop and Roll immediately.",
        "What is the first thing to do if your clothes catch fire?",
        ["Run for help", "Stop, drop to the ground, and roll", "Fan the flames with a towel", "Take off your shoes"], 1,
        "Stop, Drop, and Roll cuts off oxygen and extinguishes flames quickly.",
        ["During a festival at {at}, a spark touches {name}'s sleeve and the fabric catches fire."],
        "What must {name} do immediately?",
        [("Stop moving immediately without running", "Running fans flames with oxygen.", True, "stop|don'?t run|never run", 35),
         ("Drop to ground and protect face", "Keeps flames away from airway.", True, "drop|ground|cover face", 35),
         ("Roll back and forth to smother fire", "Smothers the fire against earth.", True, "roll|smother", 30)],
        ["run[^.]{0,15}(away|fast|water)", "fan"],
        "NFPA Fire Safety Guide", "https://nfpa.org"
    ))

    cards["ember"].append(make_card(
        "FIRE-023", "ember", "Extinguishers", "Operating a fire extinguisher: PASS method",
        ["middle", "senior"],
        ["Fire extinguishers are only meant for small incipient fires smaller than a dustbin.",
         "PASS stands for Pull pin, Aim low, Squeeze handle, Sweep side-to-side."],
        ["Ensure you have a clear escape exit behind you", "Pull the pin, aim at the base of the fire", "Squeeze handle and sweep side to side"],
        ["Never aim at the top flames", "Never corner yourself without an exit"],
        "You should aim the fire extinguisher directly at the top of the flames.", "myth", "Aiming at flames wastes the agent. Aim low at the fuel base.",
        "What does the 'A' in the PASS technique stand for?",
        ["Aim at base of fire", "Ask for help", "Attack immediately", "Always spray high"], 0,
        "A stands for Aim low at the base of the fire where fuel is burning.",
        ["In the school lab at {at}, a waste basket catches fire. An adult brings an extinguisher."],
        "How should the extinguisher be operated?",
        [("Pull the safety pin", "Unlocks the squeeze trigger.", False, "pull|pin|seal", 30),
         ("Aim low at the base of the fire", "Targets the fuel source.", True, "aim[^.]{0,15}base|low", 35),
         ("Squeeze handle and sweep side to side", "Covers the entire fire surface.", True, "squeeze|sweep", 35)],
        ["aim (high|top|flames)", "block exit"],
        "Delhi Fire Service Guidelines", "https://delhifireservice.gov.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-024", "ember", "Evacuation", "Testing closed doors during a fire",
        ["junior", "middle", "senior"],
        ["Opening a hot door can cause a backdraft or let toxic smoke rush in.",
         "Use the back of your hand to feel the door and knob so you don't burn your palm."],
        ["Feel door and handle with the back of your hand", "If warm, keep closed and seek another exit", "Seal door cracks with cloth if trapped"],
        ["Never open a warm or hot door", "Never touch door with open palm"],
        "Peeking open a hot door slightly is safe to check the fire.", "myth", "Opening even a crack allows superheated smoke and gas to flash over into the room.",
        "How should you test a closed room door during a fire alarm?",
        ["Turn knob quickly", "Feel door and knob with back of hand", "Kick door", "Smell keyhole"], 1,
        "Touch with back of hand. If warm, keep closed to block flames.",
        ["A fire alarm sounds at {at}. {name} reaches the bedroom door to exit into the hallway."],
        "What must {name} do before opening the door?",
        [("Touch door and knob with back of hand", "Detects heat safely without burning palm.", True, "back of (the )?hand|feel|touch", 40),
         ("Keep door shut if warm or hot", "Blocks fire and lethal gases.", True, "(if hot|if warm)[^.]{0,25}(don'?t open|keep closed|seal)", 35),
         ("Use alternate window escape or signal for rescue", "Prevents smoke inhalation.", False, "alternate|window|signal|call", 25)],
        ["open[^.]{0,15}immediately", "kick door"],
        "NDMA Fire Safety Advisory", "https://ndma.gov.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-025", "ember", "Smoke", "Smoke inhalation and crawling low",
        ["junior", "middle", "senior"],
        ["Smoke and toxic gases rise; cleaner, cooler air remains 30 to 60 cm above the floor.",
         "Most fire casualties result from toxic smoke inhalation rather than direct burns."],
        ["Drop to hands and knees immediately", "Crawl low under smoke toward the nearest exit", "Cover nose and mouth with a damp cloth if possible"],
        ["Never walk upright through thick smoke", "Don't stop to collect belongings"],
        "Holding your breath while walking tall lets you escape smoke safely.", "myth", "One breath of toxic smoke can cause unconsciousness. Stay low where air is clean.",
        "Where is the cleanest air located in a smoke-filled room?",
        ["Near the ceiling", "Near the floor (crawling low)", "In the exact middle", "Near windows only"], 1,
        "Heat and smoke rise, leaving a layer of breathable air near the floor.",
        ["Thick dark smoke begins filling the hallway at {at} during an emergency."],
        "How should {name} move through the smoke to escape?",
        [("Drop down and crawl low on hands and knees", "Avoids breathing rising toxic fumes.", True, "crawl low|hands and knees|stay low|floor", 40),
         ("Cover nose and mouth with a cloth", "Filters particulate matter.", False, "cover[^.]{0,15}(nose|mouth|cloth)", 25),
         ("Head continuously toward the nearest exit", "Escapes before oxygen drops.", True, "exit|door|escape|outside", 35)],
        ["stand tall", "walk upright", "run upright"],
        "Indian Red Cross Fire First Aid", "https://indianredcross.org"
    ))

    cards["ember"].append(make_card(
        "FIRE-026", "ember", "Trapped", "Surviving trapped in a room during fire",
        ["junior", "middle", "senior"],
        ["Sealing gaps prevents smoke from suffocating occupants trapped inside.",
         "Hanging a bright cloth from a window signals firefighters to your location."],
        ["Close door tightly and seal bottom cracks with wet cloth", "Open window slightly for fresh air if no smoke outside", "Call 112 / 101 and wave bright cloth from window"],
        ["Never jump from high floors", "Never break windows if smoke is outside"],
        "Breaking bedroom windows is always the best move if trapped by fire.", "myth", "If outside has smoke or flames, breaking glass draws fire inside. Signal without breaking.",
        "If trapped in a room by hallway fire, what should you seal door cracks with?",
        ["Plastic sheets", "Wet towels or clothes", "Cardboard boxes", "Dry newspaper"], 1,
        "Wet towels or cloth block smoke from penetrating under the door.",
        ["Flames in the corridor block {name}'s exit from the room at {at}."],
        "What should {name} do to stay safe until rescued?",
        [("Close door and seal cracks with wet cloth", "Blocks smoke from entering room.", True, "close door|seal|wet cloth|towel", 40),
         ("Call 112 / 101 and report exact room location", "Directs rescue teams immediately.", True, "call (112|101|emergency)|phone", 30),
         ("Signal from the window with a cloth or flashlight", "Alerts rescuers without jumping.", False, "signal|window|wave|cloth", 30)],
        ["jump from (high|balcony|window)", "open door into fire"],
        "NDMA High-Rise Guidelines", "https://ndma.gov.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-027", "ember", "School drill", "School fire drills and assembly points",
        ["junior", "middle", "senior"],
        ["Panic and stampedes cause more injuries during evacuations than flames.",
         "School assembly grounds ensure teachers can conduct headcount roll calls."],
        ["Follow teacher instructions and walk briskly without pushing", "Leave heavy backpacks and bags behind", "Assemble quietly at the designated muster ground for roll call"],
        ["Never run, push or scream during evacuation", "Never return inside for bags, phones or homework"],
        "During a fire alarm, grabbing your school bag is fine if it takes 5 seconds.", "myth", "Every second counts in fire evacuation. Leave bags; save lives.",
        "What is the most important rule when leaving the classroom during a fire drill?",
        ["Run as fast as you can", "Walk calmly in line without pushing", "Carry all books", "Hide in bathroom"], 1,
        "Orderly walking prevents fatal stairwell crushes and stampedes.",
        ["The fire alarm rings loudly across the school building at {at}."],
        "How should {name} and classmates exit the classroom?",
        [("Leave all bags and personal items behind", "Speeds up evacuation.", True, "leave bag|no bag|belongings", 30),
         ("Walk calmly in single file without running or shoving", "Prevents stampede on stairs.", True, "walk|don'?t run|calm|no push", 35),
         ("Assemble at the designated outdoor sports ground for headcount", "Ensures nobody is missing.", True, "assembly point|ground|roll call|headcount", 35)],
        ["run fast", "push", "go back for (bag|phone)"],
        "Ministry of Education School Safety Manual", "https://dsel.education.gov.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-028", "ember", "Child safety", "Matches and lighters away from young kids",
        ["junior", "middle", "senior"],
        ["Young children perceive lighters and matchsticks as toys rather than hazards.",
         "Most residential fires sparked by children occur in bedrooms and closets."],
        ["Store matches, lighters, and pooja materials in high locked cupboards", "Teach younger siblings that fire tools are adults-only tools", "Hand any stray matchbox found on floor to an adult immediately"],
        ["Never leave lighters on low coffee tables or beds", "Never let children play with diyas or sparklers"],
        "Giving an empty lighter to a toddler as a toy is harmless.", "myth", "Empty lighters still spark and teach dangerous mimicking habits.",
        "Where should matchboxes and lighters always be stored at home?",
        ["On living room coffee table", "In a high, locked cabinet out of reach of children", "In the toy basket", "Under the bed"], 1,
        "Storing out of children's reach prevents accidental house fires.",
        ["At home at {at}, {name} sees their 4-year-old cousin playing with a lighter on the sofa."],
        "What should {name} do right away?",
        [("Gently take the lighter away from the child", "Removes immediate ignition hazard.", True, "take away|remove lighter", 40),
         ("Hand it to a parent or adult immediately", "Ensures adult supervision.", True, "give adult|tell parent|hand to adult", 35),
         ("Store it in a high secure cabinet", "Prevents access by children.", False, "high place|cupboard|cabinet|out of reach", 25)],
        ["let child play", "strike lighter"],
        "Home Safety Council of India", "https://homesafety.gov.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-029", "ember", "Home hazards", "Mosquito coils, candles, and agarbatti",
        ["junior", "middle", "senior"],
        ["A glowing mosquito coil tip reaches over 500°C and can ignite paper or curtains easily.",
         "Leaving candles or coils burning while asleep causes nocturnal house fires."],
        ["Keep coils on sturdy metal stands inside deep metal plates", "Keep candles at least 1 meter away from curtains, beds, and books", "Extinguish all burning coils and candles before going to sleep"],
        ["Never place coils directly on cardboard, plastic or carpets", "Never leave lit candles unattended in empty rooms"],
        "Mosquito coils burn at low temperatures and cannot ignite fabric.", "myth", "Coil embers burn at 500°C and easily set mattresses and bedsheets on fire.",
        "What should always be placed under a mosquito coil stand?",
        ["Cardboard", "A wide metal or ceramic plate", "Newspaper", "Plastic lid"], 1,
        "Metal or ceramic plates catch falling hot ash safely without burning.",
        ["At bedtime at {at}, {name} notices an agarbatti burning right beside blowing window curtains."],
        "What action should {name} take?",
        [("Move the incense far away from curtains and fabric", "Eliminates contact with flammable cloth.", True, "move away|distance|away from curtain", 40),
         ("Place on heatproof ceramic or metal holder", "Safely contains hot falling ash.", False, "metal plate|stand|ceramic", 25),
         ("Extinguish if nobody is in the room or before sleeping", "Prevents unattended fires.", True, "extinguish|put out|before sleep", 35)],
        ["leave near curtain", "ignore"],
        "Bureau of Indian Standards (BIS)", "https://bis.gov.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-030", "ember", "Electrical", "Socket overloading and extension board safety",
        ["junior", "middle", "senior"],
        ["Plugging multiple heating appliances into one strip exceeds wire amp ratings.",
         "Overloaded circuits heat up inside walls, causing hidden attic and wall fires."],
        ["Plug high-power devices (heaters, irons, geysers) directly into dedicated wall sockets", "Check extension cords for frayed insulation or melting smells", "Unplug chargers and boards when not in active use"],
        ["Never plug multiple extension boards into each other (daisy chaining)", "Never run power cords under rugs or doorways"],
        "You can plug an iron, microwave, and kettle into one strip if it has enough holes.", "myth", "Current draw will exceed the cord's rating, melting plastic and causing fires.",
        "Why is it dangerous to plug a room heater into a cheap power strip?",
        ["It wastes electricity", "Heaters draw heavy current that can melt the strip and ignite fire", "It damages the room", "It makes heater too hot"], 1,
        "High-wattage appliances draw heavy currents that overheat thin extension wires.",
        ["In the study room at {at}, {name} sees an iron, room heater, and laptop plugged into a single cheap multi-plug adapter that feels hot."],
        "What should {name} do?",
        [("Switch off and unplug high-draw appliances immediately", "Stops current overload before melting occurs.", True, "switch off|unplug|turn off", 40),
         ("Do not touch burning or melted plastic with bare hands", "Prevents electrical burns.", False, "careful|don'?t touch bare", 20),
         ("Inform parents and connect heater directly to 15A wall socket", "Uses properly rated wiring.", True, "wall socket|15a|tell parent|adult", 40)],
        ["plug more devices", "ignore hot plug"],
        "Central Electricity Authority (Safety Regulations)", "https://cea.nic.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-031", "ember", "Gadgets", "Overheating phone and power bank charging",
        ["junior", "middle", "senior"],
        ["Lithium-ion batteries can enter thermal runaway if punctured, crushed or overheated.",
         "Charging phones under pillows traps heat, preventing natural dissipation."],
        ["Charge phones on hard, flat, ventilated surfaces like tables", "Stop using and safely dispose of any swollen or bulging battery", "Unplug chargers once the device reaches full charge"],
        ["Never charge phones under pillows or on mattresses overnight", "Never use cheap uncertified replacement chargers"],
        "Charging your phone under a soft pillow is completely safe.", "myth", "Pillows trap charging heat, leading to battery swelling and explosion.",
        "What should you do if your power bank feels unusually hot and swollen?",
        ["Put it in freezer", "Stop using and charging it immediately; move to fire-safe area", "Press the bulge down", "Shake it"], 1,
        "Swollen batteries can burst into flame. Discontinue use immediately.",
        ["At night at {at}, {name} finds their phone charging tucked under their sleeping pillow, feeling burning hot."],
        "What is the safest move for {name}?",
        [("Unplug the charger from the wall socket", "Cuts power supply to battery.", True, "unplug|disconnect|switch off", 35),
         ("Move phone off bed onto a hard, non-flammable desk", "Allows phone to dissipate heat safely.", True, "move off bed|table|desk|hard surface", 35),
         ("Never sleep with phone under pillow or bedding", "Prevents thermal runaway.", False, "never under pillow|ventilated", 30)],
        ["leave under pillow", "put in water"],
        "CERT-In Device Safety Advisory", "https://cert-in.org.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-032", "ember", "Vehicles", "Vehicle fire evacuation in cars and buses",
        ["junior", "middle", "senior"],
        ["Vehicle fires spread rapidly due to fuel, oil, upholstery, and electrical wires.",
         "Smoke and toxic fumes fill a closed vehicle cabin in under 60 seconds."],
        ["Alert driver and passengers calmly to pull over safely", "Evacuate everyone immediately and move at least 30 meters away", "Call 112 / 101 from a safe distance outside"],
        ["Never return inside a burning car for bags or valuables", "Never stand downwind of vehicle smoke"],
        "If a car catches fire, you should open the bonnet wide to blow it out.", "myth", "Opening the bonnet lets in massive oxygen, creating an immediate fireball.",
        "If smoke begins billowing from a school bus bonnet, what should students do?",
        ["Stay seated and wait", "Evacuate calmly through doors and move 30 meters away", "Open the engine bonnet", "Collect heavy school bags"], 1,
        "Evacuate quickly and maintain safe standoff distance in case of fuel tank rupture.",
        ["While traveling in a vehicle at {at}, {name} notices acrid electrical smoke pouring from under the dashboard."],
        "What should {name} and passengers do?",
        [("Instruct driver to stop vehicle and turn off ignition", "Cuts fuel pump and electrical flow.", True, "stop vehicle|pull over|turn off engine", 35),
         ("Evacuate all passengers immediately without gathering luggage", "Saves lives before toxic fumes accumulate.", True, "evacuate|get out|leave bags|exit", 35),
         ("Move at least 30 meters upwind and call 112", "Keeps safe distance from fuel explosion.", False, "safe distance|30 meters|call 112", 30)],
        ["go back for luggage", "open bonnet into flames"],
        "Ministry of Road Transport and Highways", "https://morth.nic.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-033", "ember", "Outdoors", "Bonfire and garden leaf burning safety",
        ["junior", "middle", "senior"],
        ["Burning dry leaves releases toxic fine particulate matter and risks runaway fires.",
         "Unattended bonfires can be reignited hours later by sudden wind gusts."],
        ["Clear a 3-meter safety ring of bare dirt around any fire pit", "Keep a bucket of water or sand right next to the campfire", "Drown the coals completely with water and stir until cold before leaving"],
        ["Never burn plastic, rubber or treated wood", "Never walk away from an active campfire"],
        "If a campfire stops showing flames, it is safe to leave without water.", "myth", "Deep embers retain heat for over 24 hours. Drown with water until cool to touch.",
        "How do you ensure a campfire is completely extinguished before leaving?",
        ["Cover it with dry leaves", "Pour water, stir ashes, and feel that coals are cold", "Blow on it", "Walk away"], 1,
        "Drown, stir, and check temperature to ensure no hidden hot embers remain.",
        ["After an outdoor camping activity at {at}, the campfire is smoking but flames are gone."],
        "How should {name} and team properly extinguish the pit?",
        [("Drench all embers thoroughly with water", "Cools down deep glowing coals.", True, "water|drench|pour", 35),
         ("Stir the ashes with a stick and add more water", "Exposes hidden coals to water.", True, "stir|mix ashes", 35),
         ("Confirm ashes are completely cold to the touch", "Ensures zero rekindling risk.", False, "cold|cool|touch", 30)],
        ["leave smoking embers", "cover with dry grass"],
        "Ministry of Environment, Forest and Climate Change", "https://moef.gov.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-034", "ember", "Wildfire", "Grass and forest fire on hiking trails",
        ["middle", "senior"],
        ["Wildfires move uphill much faster than downhill because rising heat pre-warms slope vegetation.",
         "Shifting wind directions can rapidly trap hikers in steep valleys."],
        ["Move downhill and downwind toward natural fire breaks like rivers or wide roads", "Stay in cleared areas with sparse vegetation", "Call forest helpline or 112 with exact trail landmarks"],
        ["Never try to outrun a fire heading uphill", "Never hide inside narrow ravines or caves"],
        "When escaping a forest fire on a mountain, running uphill is safer.", "myth", "Flames race uphill twice as fast as downhill. Always escape downhill and sideways.",
        "Why is it dangerous to run uphill when escaping a forest fire?",
        ["You get tired", "Heat and flames travel uphill significantly faster", "Wild animals are there", "Phone signal drops"], 1,
        "Rising convective heat pre-heats uphill brush, causing fires to explode upward.",
        ["While on a hillside trek at {at}, {name} spots a fast-moving brush fire advancing up the slope."],
        "Which direction should {name} evacuate?",
        [("Move downhill and sideways toward cleared terrain", "Fire races uphill; downhill provides escape time.", True, "downhill|sideways|away from slope", 40),
         ("Avoid narrow ravines and dense dry thickets", "Ravines act as natural chimneys for fire.", True, "avoid ravine|open area|bare ground", 30),
         ("Alert trek leader and call emergency services 112", "Coordinates forest rescue.", False, "call 112|alert leader|forest staff", 30)],
        ["run uphill", "climb higher"],
        "Forest Survey of India Wildfire Guidelines", "https://fsi.nic.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-035", "ember", "Family plan", "Creating a home fire escape plan",
        ["junior", "middle", "senior"],
        ["Families have as little as two minutes to escape safely once a smoke alarm sounds.",
         "Having a designated meeting spot outside ensures everyone is accounted for quickly."],
        ["Map two exit paths (door and window) from every bedroom", "Designate a fixed meeting spot outside (e.g. big tree or park gate)", "Practise the escape drill with family twice a year"],
        ["Never use lifts or elevators during any building fire", "Never search for pets or toys during evacuation"],
        "During a house fire, everyone should gather in the living room first.", "myth", "Gathering indoors risks getting trapped. Everyone must escape outside to the meeting spot.",
        "What is the most crucial part of a family fire escape plan?",
        ["Buying expensive ladders", "Having two ways out of every room and a fixed outdoor meeting point", "Writing long essays", "Keeping windows locked"], 1,
        "Two exits and an outside meeting spot prevent people being trapped inside.",
        ["{name}'s family at {at} is creating their yearly home fire safety plan."],
        "What key elements must {name} include in the family plan?",
        [("Identify two exit routes from every room", "Ensures backup if main door is blocked.", True, "two exits|two ways|door and window", 35),
         ("Pick a fixed outdoor meeting spot outside the building", "Enables instant headcount.", True, "outdoor meeting point|outside spot|tree|gate", 35),
         ("Never take elevators; always take stairways", "Prevents getting trapped in elevator shafts.", False, "no elevator|stairs|staircase", 30)],
        ["use elevator", "meet inside house"],
        "NDMA Home Safety Campaign", "https://ndma.gov.in"
    ))

    cards["ember"].append(make_card(
        "FIRE-036", "ember", "Aftermath", "Safety rules for re-entering a fire-affected building",
        ["middle", "senior"],
        ["Burned structures suffer hidden beam weaknesses, gas pockets, and toxic ash.",
         "Smoldering embers inside wall cavities can reignite hours after flames are doused."],
        ["Wait until the fire department officially declares the structure safe", "Wear sturdy closed shoes and a particulate mask when re-entering", "Have an electrician inspect house wiring before restoring power"],
        ["Never enter a burned building without fire officer permission", "Never use damaged switches or gas valves"],
        "Once flames are out, families can move back into the house immediately.", "myth", "Structural weakness, carbon monoxide, and damaged wiring present deadly post-fire hazards.",
        "Who must grant permission before anyone re-enters a house after a fire?",
        ["The building watchman", "The Fire Department or municipal safety engineer", "The neighbours", "Anyone who is brave"], 1,
        "Only fire officials can verify structural stability and absence of toxic gases.",
        ["A fire at {at} was extinguished by firefighters an hour ago. {name}'s friend wants to run inside to grab their laptop."],
        "What should {name} advise?",
        [("Do not enter until fire officers declare it safe", "Prevents collapse and smoke asphyxiation.", True, "don'?t enter|wait for fire department|officials", 40),
         ("Beware of structural collapse and live fallen wires", "Hidden dangers remain active.", True, "structural collapse|weak floor|live wire", 35),
         ("Do not flip electrical mains back on without inspection", "Avoids electrical flashovers.", False, "no electricity|certified electrician|inspect", 25)],
        ["run inside right away", "climb in window"],
        "Delhi Fire Service Public Notice", "https://delhifireservice.gov.in"
    ))

    print(f"Loaded {len(cards['ember'])} expanded cards for Ember")
    return cards

def get_ember_expanded_cards():
    return get_cards()["ember"]

if __name__ == "__main__":
    c = get_cards()
    print("Cards test loaded successfully.")
