"""
Signal (Road Safety) and Pulse (First Aid) expanded skills.
Provides 16 verified, realistic skills for each agent.
"""
from cards_existing import make_card

def get_signal_cards():
    cards = []

    # 1. ROAD-021: Pillion passenger
    cards.append(make_card(
        "ROAD-021", "signal", "Two-wheeler", "Pillion passenger safety on two-wheelers",
        ["junior", "middle", "senior"],
        ["Pillion riders face identical risk of head trauma as drivers during a collision.",
         "Sitting side-saddle (both legs on one side) severely unbalances the vehicle during sudden stops."],
        ["Wear an ISI-approved helmet with chin strap fastened snugly", "Sit astride facing forward with both feet on footrests", "Hold firmly onto the rider's waist or side grab rail"],
        ["Never sit side-saddle without footrests", "Never ride without strapping helmet buckle"],
        "Only the person steering the scooter needs to wear a helmet.", "myth", "Pillion passengers suffer equal head injury risks and are legally mandated to wear helmets.",
        "What is the safest way to sit as a pillion passenger on a two-wheeler?",
        ["Sitting sideways", "Astride facing forward with feet on footrests and strapped helmet", "Standing on back footpegs", "Holding mobile phone"], 1,
        "Astride posture maintains balance and strapped ISI helmets protect from head injuries.",
        ["{relation} offers {name} a ride on a motorcycle at {at}."],
        "What must {name} do before getting onto the two-wheeler?",
        [("Wear an ISI-marked helmet with chin strap securely locked", "Unstrapped helmets fly off on impact.", True, "helmet|strap|isi|chin strap", 40),
         ("Sit astride facing forward with feet on footrests", "Maintains center of gravity.", True, "astride|facing forward|footrest|both feet", 35),
         ("Hold the waist or rear grab rail securely", "Prevents falling off during acceleration.", False, "hold|grab rail|waist", 25)],
        ["no helmet", "sit sideways", "stand on pegs"],
        "Ministry of Road Transport and Highways (MoRTH)", "https://morth.nic.in"
    ))

    # 2. ROAD-022: Underage driving
    cards.append(make_card(
        "ROAD-022", "signal", "Underage driving", "Saying NO to underage driving",
        ["middle", "senior"],
        ["Driving without a valid licence is illegal under Section 199A of the Motor Vehicles Act.",
         "Parents and vehicle owners face heavy fines and imprisonment if a minor is caught driving."],
        ["Refuse politely and firmly if friends offer keys or pressure you to drive", "Use public buses, cycles, or walk instead of unauthorized vehicles", "Remind peers of legal penalties and accident risks"],
        ["Never drive a two-wheeler or car before age 18 (16 for gearless 50cc with licence)", "Never accept rides from unlicensed minor peers"],
        "Driving inside a private colony without a licence is completely legal.", "myth", "Motor Vehicle Act rules apply to all roads and public-access colonies.",
        "A 14-year-old friend asks you to drive their father's scooter around the block. What should you do?",
        ["Drive slowly only", "Firmly say NO and decline the keys", "Drive without helmet", "Record a video while riding"], 1,
        "Underage driving is illegal, dangerous, and causes severe accidents.",
        ["At {at}, a classmate shows car keys and invites {name} to go for a joyride."],
        "What is the only responsible action for {name}?",
        [("Say NO firmly and refuse to ride or drive", "Prevents illegal and hazardous joyriding.", True, "say no|refuse|decline|don'?t drive", 45),
         ("Remind friend of legal penalties under MV Act", "Awareness of 3-year jail for vehicle owner.", False, "illegal|law|licence|mv act", 25),
         ("Choose safe walking or authorized transport", "Safe travel alternative.", True, "walk|bus|cycle|safe", 30)],
        ["take the keys", "agree to drive", "hop in for fun"],
        "Motor Vehicles Amendment Act", "https://morth.nic.in"
    ))

    # 3. ROAD-023: Rear seat belts
    cards.append(make_card(
        "ROAD-023", "signal", "Seat belts", "Wearing seat belts in rear passenger seats",
        ["junior", "middle", "senior"],
        ["Unbelted rear passengers become human missiles during a collision, crushing front occupants.",
         "Wearing a seat belt reduces fatal collision injury rates by over 45%."],
        ["Fasten your three-point seat belt immediately upon entering any car", "Adjust the lap belt snugly over hips and diagonal belt across chest", "Remind fellow backseat passengers to buckle up before the car moves"],
        ["Never tuck the shoulder strap behind your back or armpit", "Never share one seat belt between two people"],
        "Rear seat passengers do not need seat belts because front seats protect them.", "myth", "Unbuckled rear passengers slam violently into front seats, killing front occupants.",
        "Why is buckling up in the back seat just as critical as the front?",
        ["To avoid dust", "It stops you being launched forward into the front seats or windshield", "It looks cool", "To sleep better"], 1,
        "In a crash, rear passengers fly forward at highway speed without belts.",
        ["{name} gets into the rear seat of a taxi at {at} with {relation}."],
        "What should {name} do before the taxi pulls into traffic?",
        [("Buckle the rear three-point seat belt securely", "Restrains body during sudden deceleration.", True, "buckle|seat belt|strap", 45),
         ("Position belt across collarbone and flat over hips", "Distributes crash forces across strong bones.", False, "chest|hips|lap|adjust", 25),
         ("Ask other family members to buckle up too", "Ensures whole car is secured.", True, "ask others|family|everyone buckle", 30)],
        ["don'?t buckle", "tuck behind back", "ignore belt"],
        "World Health Organization Road Safety", "https://who.int"
    ))

    # 4. ROAD-024: Railway crossings
    cards.append(make_card(
        "ROAD-024", "signal", "Railways", "Railway tracks and level crossing discipline",
        ["junior", "middle", "senior"],
        ["High-speed trains require up to 1 kilometer of braking distance to stop completely.",
         "Crossing closed railway barriers or walking along tracks is punishable under the Railway Act."],
        ["Wait patiently behind lowered crossing boom barriers until gates fully open", "Cross tracks exclusively using Foot Over Bridges (FOBs) or subways", "Remove headphones and look both directions at stations"],
        ["Never duck under or bypass closed level crossing gates", "Never take photos, reels or walk along train tracks"],
        "You can easily see and hear an oncoming electric train from a mile away.", "myth", "Modern electric locomotives produce minimal frontal noise until dangerously close.",
        "A railway crossing gate is down and red signals are flashing. What is the rule?",
        ["Duck under if no train is visible", "Wait behind the barrier until it lifts completely", "Walk cycle across", "Follow motorbikes"], 1,
        "Never bypass closed gates. Trains approach faster than they appear.",
        ["On the way home from school at {at}, the railway crossing barrier lowers and warning bells ring."],
        "What must {name} do?",
        [("Wait calmly behind the closed gate barrier", "Prevents being trapped on tracks.", True, "wait|stay behind|don'?t cross|closed gate", 45),
         ("Do not duck under or follow impatient cyclists", "Crossing closed gates is illegal and lethal.", True, "don'?t duck|never bypass|wait for train", 35),
         ("Stay alert with headphones removed", "Ensures approach horns are heard.", False, "headphones off|alert|listen", 20)],
        ["duck under", "cross tracks", "squeeze past"],
        "Indian Railways Safety Directorate", "https://indianrailways.gov.in"
    ))

    # 5. ROAD-025: Metro platform
    cards.append(make_card(
        "ROAD-025", "signal", "Metro", "Metro and railway platform edge safety",
        ["junior", "middle", "senior"],
        ["High-speed trains create an aerodynamic suction zone near the platform edge.",
         "The yellow tactile strip marks the safety boundary away from moving trains."],
        ["Stand well behind the yellow safety line until the train comes to a complete halt", "Allow arriving passengers to exit completely before boarding", "Keep luggage, bags and feet behind the safety edge"],
        ["Never lean over the platform edge to look down the tracks", "Never run on platforms or push in boarding lines"],
        "Standing right at the edge helps you get a seat faster without any danger.", "myth", "Crowd surges or dizziness can cause instant falls onto high-voltage tracks.",
        "What does the yellow tactile line on a metro or railway platform indicate?",
        ["Decoration", "The safety boundary: stay behind it until train stops", "Luggage zone", "Ticket check area"], 1,
        "Standing behind the yellow line protects against suction and train collision.",
        ["Waiting at the busy metro station at {at}, {name} sees people crowding the platform edge."],
        "How should {name} position themselves safely?",
        [("Stand firmly behind the yellow tactile safety line", "Maintains safe standoff distance from tracks.", True, "behind yellow line|safety line|step back", 40),
         ("Allow alighting passengers to get off before boarding", "Prevents doorway congestion and crush.", True, "let off first|exit first|passengers alight", 35),
         ("Do not push, shove or run on the platform", "Maintains crowd order.", False, "no push|no run|calm", 25)],
        ["lean over edge", "stand past yellow line", "push into train"],
        "Delhi Metro Rail Corporation Safety Guide", "https://delhimetrorail.com"
    ))

    # 6. ROAD-026: Moving vehicles
    cards.append(make_card(
        "ROAD-026", "signal", "Boarding", "Never boarding or alighting from moving buses or trains",
        ["junior", "middle", "senior"],
        ["Human foot speed cannot match vehicle momentum, throwing people under wheels.",
         "Boarding or jumping from moving buses causes severe head trauma and wheel crushes."],
        ["Wait for the bus or auto to come to a full, stationary halt at the curb", "Hold handrails firmly while stepping on or off", "Queue in an orderly line at designated bus stops"],
        ["Never sprint to jump onto a moving bus footboard", "Never lean out of doors or travel on the footboard"],
        "Jumping off a moving bus is safe if you run in the same direction.", "myth", "Foot friction instantly flips the body backward under the rear dual wheels.",
        "What must you always verify before stepping onto or off a bus?",
        ["That friends are watching", "That the vehicle has come to a complete, stationary stop", "That your bag is zipped", "That driver is smiling"], 1,
        "Never board or alight while tires are rotating.",
        ["The school bus at {at} begins rolling forward while {name}'s friend tries to hop onto the footboard."],
        "What should {name} tell their friend right now?",
        [("Wait and do not jump onto a moving vehicle", "Prevents falling under rear wheels.", True, "wait|don'?t jump|stop|moving vehicle", 45),
         ("Signal the driver or conductor to stop fully", "Ensures safe boarding.", True, "tell driver|conductor|stop bus", 35),
         ("Never travel standing on the footboard", "Footboard travel is fatal.", False, "no footboard|step inside|seats", 20)],
        ["jump on", "pull onto moving bus", "run and grab door"],
        "State Transport Authority Road Safety Rules", "https://morth.nic.in"
    ))

    # 7. ROAD-027: Monsoon hazards
    cards.append(make_card(
        "ROAD-027", "signal", "Monsoon", "Navigating waterlogged roads and hidden manholes",
        ["junior", "middle", "senior"],
        ["Rainwater conceals displaced manhole lids, deep potholes, and broken glass.",
         "Fallen electric wires in pooled water conduct lethal currents across wide areas."],
        ["Avoid wading through deep or murky floodwater whenever possible", "Stay on elevated pavements and test puddles with an umbrella stick", "Keep clear of electric poles, junction boxes, and transformers"],
        ["Never step into swirling drain water", "Never touch electric poles or lampposts in the rain"],
        "If others walk through waterlogged roads, it is safe to follow their steps.", "myth", "Manhole covers get displaced in seconds by underground hydraulic pressure.",
        "While walking home in heavy monsoon rains, the road ahead is flooded with brown water. What is the safest action?",
        ["Walk straight through", "Find a higher alternate route or seek shelter until water drains", "Jump in puddles", "Touch electric pole for support"], 1,
        "Brown water hides open manholes and live electrical leaks.",
        ["Sudden monsoon showers at {at} flood the road outside with knee-deep muddy water."],
        "How should {name} proceed safely?",
        [("Avoid walking through murky floodwater; find higher dry ground", "Hides missing manhole lids and open ditches.", True, "avoid floodwater|higher ground|alternate route|wait", 40),
         ("Stay far away from electric poles and submerged transformers", "Prevents fatal electrocution through water.", True, "electric pole|wire|transformer|shock", 40),
         ("Contact parents or wait with teachers in a sheltered shop", "Coordinates safe transportation.", False, "call parent|wait with teacher|shelter", 20)],
        ["wade through", "touch pole", "run through water"],
        "NDMA Urban Flood Guidelines", "https://ndma.gov.in"
    ))

    # 8. ROAD-028: Night walking
    cards.append(make_card(
        "ROAD-028", "signal", "Night safety", "Walking safely at night: Visibility and direction",
        ["junior", "middle", "senior"],
        ["Drivers cannot spot pedestrians in dark clothing until they are under 18 meters away.",
         "Walking facing oncoming traffic lets you see approaching headlights and react."],
        ["Wear light-coloured or reflective clothing after sunset", "Walk on footpaths, or walk facing oncoming traffic if no footpath exists", "Carry a flashlight or use mobile torch pointed at your feet"],
        ["Never walk in dark clothes with your back to vehicular traffic", "Never cross unlit highway stretches without streetlights"],
        "Pedestrians can always be seen by car headlights from 100 meters away.", "myth", "Low beams illuminate dark clothing only at very short, hazardous braking distances.",
        "If there is no sidewalk on a rural or quiet road at night, which side should you walk on?",
        ["The right side (facing oncoming traffic)", "The left side with your back to cars", "The exact middle", "Zigzag"], 0,
        "Facing oncoming traffic lets you see vehicle headlights and step off if needed.",
        ["It's 8 PM at {at}. {name} needs to walk home along a road with broken streetlights."],
        "How can {name} ensure maximum visibility and safety?",
        [("Wear light or reflective clothing and use a torch", "Allows drivers to spot you from 100m away.", True, "light clothing|reflective|torch|flashlight", 40),
         ("Walk facing oncoming traffic on the road shoulder", "Maintains visual eye contact with approaching drivers.", True, "facing traffic|facing cars|shoulder|footpath", 35),
         ("Stay alert and avoid staring down at a mobile phone screen", "Maintains 360-degree situational awareness.", False, "no phone|alert|look ahead", 25)],
        ["wear all black", "walk with back to traffic", "stare at phone"],
        "SaveLIFE Foundation Pedestrian Safety Guide", "https://savelifefoundation.org"
    ))

    # 9. ROAD-029: Rash driving
    cards.append(make_card(
        "ROAD-029", "signal", "Rash driving", "Speaking up against rash driving and speeding",
        ["middle", "senior"],
        ["Over-speeding is responsible for over 70% of fatal road crashes in India.",
         "Passengers have the legal right to demand the driver stop if they feel unsafe."],
        ["Speak up clearly and politely: 'Please slow down, I feel unsafe'", "If the driver refuses, demand to be let off at a safe public spot", "Call parents or 112 if in an auto or cab where driver refuses to stop"],
        ["Never stay quiet out of politeness or embarrassment", "Never distract the driver by grabbing steering controls"],
        "Telling a driver to slow down makes them angry and drives worse.", "myth", "A clear, calm passenger objection often snaps an overconfident driver out of aggressive driving.",
        "You are in an auto-rickshaw that is overtaking rashly at dangerous speeds. What should you do?",
        ["Stay quiet", "Firmly request the driver to slow down or pull over", "Jump out while moving", "Cheer the driver"], 1,
        "Voice your concern firmly and demand safe speed or exit at a safe spot.",
        ["While traveling in a cab at {at}, the driver begins weaving through traffic at high speed."],
        "What should {name} do?",
        [("Politely and firmly ask driver: 'Please slow down, I do not want to speed'", "Directly communicates passenger objection.", True, "slow down|drive carefully|speed limit", 40),
         ("If driver ignores, ask to pull over at the nearest well-lit public stop", "Enables safe exit from dangerous vehicle.", True, "pull over|stop here|let me out", 35),
         ("Share live trip status with family or call 112 if threatened", "Emergency backup protocol.", False, "call parent|share trip|112", 25)],
        ["grab the steering wheel", "jump out moving", "stay silent"],
        "MoRTH Road Safety Cell", "https://morth.nic.in"
    ))

    # 10. ROAD-030: Hit and run
    cards.append(make_card(
        "ROAD-030", "signal", "Hit and run", "Witnessing a hit-and-run: Vital details and emergency report",
        ["middle", "senior"],
        ["The first 60 seconds are critical for memorizing registration numbers and vehicle details.",
         "Prompt medical dispatch during the Golden Hour saves 50% of crash victims."],
        ["Memorize registration number, vehicle color, model and direction of escape", "Call 112 / 108 immediately and state exact accident location", "Signal other bystanders to help create a safety perimeter around the victim"],
        ["Never chase a fleeing vehicle on foot or cycle", "Never move an unconscious injured victim roughly"],
        "Witnesses should pursue hit-and-run drivers on their bicycles to catch them.", "myth", "Chasing fleeing vehicles leads to secondary crashes. Memorize details and call police.",
        "You witness a car hit a cyclist and speed away. What is the most critical information to note?",
        ["The color of cyclist's bag", "The car's license plate number, color, and make", "The shop signboards", "The weather"], 1,
        "Vehicle registration number enables police to apprehend the fleeing driver.",
        ["At {at}, a speeding car hits a pedestrian and flees without stopping."],
        "What key actions should {name} take immediately?",
        [("Note registration number, vehicle make, color, and direction", "Crucial forensic evidence for police.", True, "number plate|registration|color|make|car details", 40),
         ("Call 112 for police and 108 for ambulance immediately", "Dispatches medical trauma teams.", True, "call (112|108)|ambulance|police", 35),
         ("Stay at a safe distance and help comfort the injured person", "Protects victim from further traffic.", False, "comfort|safe perimeter|bystanders", 25)],
        ["chase the car", "drag victim across road", "ignore and leave"],
        "Supreme Court Committee on Road Safety", "https://morth.nic.in"
    ))

    # 11. ROAD-031: Truck blind spots
    cards.append(make_card(
        "ROAD-031", "signal", "Heavy vehicles", "Staying out of truck and bus blind spots (No-Zones)",
        ["junior", "middle", "senior"],
        ["Heavy trucks have massive blind spots directly in front, directly behind, and along both flanks.",
         "If you cannot see the truck driver's face in their side mirror, they cannot see you."],
        ["Maintain at least 10 meters distance when following behind large buses or trucks", "Never overtake a truck on the left (curb) side when it might turn", "Pass trucks briskly on the right without lingering in their side blind spots"],
        ["Never squeeze your cycle between a turning truck and the curb", "Never tailgate directly behind container trucks"],
        "Truck drivers have elevated seats so they can see everything right around their bumper.", "myth", "High bonnets create a 6-meter blind zone directly in front where small pedestrians are invisible.",
        "What is the golden rule of heavy vehicle mirrors?",
        ["Mirrors are for looks", "If you cannot see the driver in their mirror, they cannot see you", "Trucks see everything", "Overtake on left"], 1,
        "If the mirror doesn't reflect the driver's eyes, you are in their blind spot.",
        ["Riding a bicycle at {at}, {name} approaches a large cement truck that is signaling a left turn."],
        "What is the only safe move for {name}?",
        [("Stay well behind the truck and do not squeeze on the left side", "Left turns create deadly rear-wheel pinch zones.", True, "stay behind|don'?t squeeze|wait|no left", 45),
         ("Keep visual contact with driver's right mirror", "Ensures driver is aware of presence.", True, "mirror|blind spot|visible", 35),
         ("Give the truck plenty of turning room", "Heavy trucks swing wide.", False, "space|turning room|distance", 20)],
        ["squeeze on left", "undertake truck", "overtake turning truck"],
        "Indian Road Safety Campaign", "https://road-safety.co.in"
    ))

    # 12. ROAD-032: Headphones
    cards.append(make_card(
        "ROAD-032", "signal", "Distraction", "Headphones, phones and audio awareness near traffic",
        ["junior", "middle", "senior"],
        ["Audio cues (horns, engine revs, tire screeches) provide 50% of pedestrian hazard warnings.",
         "Active noise cancellation completely blocks ambient sounds of approaching electric vehicles."],
        ["Keep one ear completely uncovered or turn off noise-cancellation near roadways", "Pause music and pocket phones before stepping off curbs to cross", "Look left-right-left even when music is off"],
        ["Never walk across busy intersections while texting or browsing", "Never wear over-ear headphones at maximum volume on roads"],
        "Looking with your eyes is enough; hearing plays no role in pedestrian safety.", "myth", "Auditory cues detect vehicles turning from behind and speeding in blind corners.",
        "Why is wearing noise-cancelling headphones while walking near roads dangerous?",
        ["It drains battery", "It blocks horns and approaching engine noises, preventing evasion", "It attracts rain", "It hurts ears"], 1,
        "Blocked hearing prevents you from reacting to horns and approaching sirens.",
        ["Walking toward school along a busy road at {at}, {name}'s friend has big headphones playing loud music."],
        "What should {name} advise their friend?",
        [("Take off headphones or keep one ear free near traffic", "Restores critical auditory awareness.", True, "take off headphones|one ear free|volume down", 45),
         ("Stay fully alert to vehicle horns, reversing beeps and sirens", "Enables split-second reaction.", True, "listen|horns|alert|hear traffic", 35),
         ("Keep phone inside bag rather than texting while walking", "Eliminates visual distraction.", False, "phone in pocket|no texting", 20)],
        ["turn volume to max", "text while crossing", "ignore horns"],
        "NIMHANS Road Safety & Pedestrian Study", "https://nimhans.ac.in"
    ))

    # 13. ROAD-033: Dogs chasing cycles
    cards.append(make_card(
        "ROAD-033", "signal", "Cycling", "Handling stray dogs barking or chasing your cycle",
        ["junior", "middle", "senior"],
        ["Dogs have an innate predatory chase instinct triggered by fast spinning pedals and panic.",
         "Panic pedaling causes cyclists to swerve into oncoming cars and crash."],
        ["Stop pedaling, slow down smoothly, and dismount calmly", "Place the bicycle between yourself and the dog as a physical barrier", "Speak firmly in a low, calm voice: 'No! Go home!' without shouting"],
        ["Never pedal faster in blind panic into traffic", "Never kick out with your feet, which risks severe bites and falls"],
        "Pedaling as hard as possible is the best way to outrun a street dog.", "myth", "Chasing speeds up dogs and causes cyclists to crash into curbs or vehicles.",
        "A stray street dog begins barking and chasing your bicycle. What should you do?",
        ["Pedal wildly into the main road", "Slow down steadily, dismount, and keep cycle between you and dog", "Kick the dog", "Throw your bag"], 1,
        "Dismounting cancels the chase reflex and the bicycle frame acts as a shield.",
        ["Cycling down a colony lane at {at}, two street dogs run out barking loudly at {name}'s tires."],
        "How should {name} handle this safely?",
        [("Slow down steadily without swerving into traffic", "Cancels dog's speed chase instinct.", True, "slow down|stop pedaling|don'?t panic", 40),
         ("Dismount and keep the bicycle frame between self and dogs", "Forms a sturdy physical defensive shield.", True, "dismount|get off|cycle between|shield", 40),
         ("Walk calmly away without running or making eye contact", "Prevents escalation.", False, "walk away|calm|no running", 20)],
        ["pedal faster into traffic", "kick at dogs", "scream and throw bike"],
        "Animal Welfare Board of India", "https://awbi.gov.in"
    ))

    # 14. ROAD-034: Road signs
    cards.append(make_card(
        "ROAD-034", "signal", "Signage", "Essential road signs every student must recognize",
        ["junior", "middle", "senior"],
        ["Circular signs with red borders give orders (prohibitions); triangular signs give warnings.",
         "School Zone signs indicate 25 km/h limits and high pedestrian crossing density."],
        ["Recognize octagonal red STOP signs (must come to complete halt)", "Recognize triangular Pedestrian Crossing and School Ahead warning signs", "Follow blue circular signs which indicate compulsory positive instructions"],
        ["Never ignore 'No Entry' or 'One Way' street markings", "Never cross against red pedestrian walking figures"],
        "School zone signs are only meant for bus drivers, not cyclists or pedestrians.", "myth", "Traffic signs govern all road users, helping cyclists predict driver behaviors.",
        "What shape is an international regulatory STOP sign on Indian roads?",
        ["Round circle", "Octagon (8-sided red polygon)", "Inverted triangle", "Square"], 1,
        "The octagonal shape is unique so drivers can recognize it even when covered in snow or mud.",
        ["At the intersection outside school at {at}, {name} sees an octagonal red sign and a pedestrian crossing symbol."],
        "What do these signs instruct road users to do?",
        [("STOP requires vehicles to come to a full stationary halt", "Mandatory stop before proceeding.", True, "stop sign|complete stop|halt", 40),
         ("Pedestrian crossing warns of designated walking rights-of-way", "Priority zone for walkers.", True, "pedestrian crossing|zebra crossing|school zone", 40),
         ("Check all directions before stepping onto zebra lines", "Defensive crossing habits.", False, "look both ways|check traffic", 20)],
        ["ignore stop sign", "run through red", "speed up"],
        "Indian Roads Congress (IRC) Traffic Sign Code", "https://irc.nic.in"
    ))

    # 15. ROAD-035: Accident witness
    cards.append(make_card(
        "ROAD-035", "signal", "First response", "Calling emergency services: Being an effective crash witness",
        ["middle", "senior"],
        ["Clear landmark descriptions allow ambulance dispatchers to reach victims 10 minutes faster.",
         "Panicking and hanging up delays medical intervention during trauma care."],
        ["State the exact location first (road name, nearest shop/landmark, intersection)", "State the number of injured persons and whether anyone is trapped or unconscious", "Stay on the call until the emergency operator instructs you to hang up"],
        ["Never give vague directions like 'near a big tree'", "Never hang up before the dispatcher confirms location"],
        "When calling 112/108, describing the injuries is more important than giving the location.", "myth", "If the call drops before location is known, help cannot be dispatched.",
        "What is the first thing you must clearly tell the 112/108 emergency operator?",
        ["Your school marks", "The exact location with a prominent landmark", "The car model", "Your opinion of the driver"], 1,
        "Location first allows operators to dispatch the nearest emergency unit while you talk.",
        ["{name} comes across a two-wheeler collision at {at} and dials 112."],
        "How should {name} structure the emergency report?",
        [("Provide exact road name and prominent nearby landmark first", "Allows GPS dispatch immediately.", True, "location|landmark|road name|where", 45),
         ("Report number of injured persons and conscious state", "Determines number of ambulances needed.", True, "how many hurt|unconscious|injuries", 35),
         ("Stay on the line and follow dispatcher instructions", "Ensures vital questions are answered.", False, "stay on line|don'?t hang up|operator", 20)],
        ["hang up immediately", "give vague location", "scream without location"],
        "National Emergency Response Support System (112 India)", "https://112.gov.in"
    ))

    # 16. ROAD-036: Good Samaritan law
    cards.append(make_card(
        "ROAD-036", "signal", "Good Samaritan", "Good Samaritan protections under Indian law",
        ["middle", "senior"],
        ["The Supreme Court of India established Good Samaritan rules to protect crash helpers from harassment.",
         "Hospitals cannot force Good Samaritans to pay admission fees or reveal personal identities."],
        ["Help accident victims without fear of legal or police harassment", "Good Samaritans can leave immediately after taking a victim to hospital", "You are not required to become a court witness unless you voluntarily choose to"],
        ["Never withhold help because of fear of police questioning", "Never take photos of victims instead of rendering aid"],
        "If you help a road accident victim into an ambulance, police will force you to pay for hospital care.", "myth", "Under Indian Good Samaritan law, helpers cannot be forced to pay or face detention.",
        "What legal protection does the Indian Good Samaritan law grant citizens who help accident victims?",
        ["They get free movie tickets", "Complete immunity from police harassment, detention, and hospital fee liability", "They must become police officers", "None"], 1,
        "Good Samaritans are legally protected to encourage life-saving bystander intervention.",
        ["A road crash occurs at {at}. Bystanders are hesitant to help, fearing police harassment."],
        "What should {name} explain to encourage safe bystander assistance?",
        [("Indian Good Samaritan law protects helpers from police interrogation", "Supreme Court guidelines guarantee immunity.", True, "good samaritan|no police harassment|protected|law", 45),
         ("Helpers cannot be forced to pay hospital admission charges", "Hospitals are legally required to accept trauma victims.", True, "no hospital fees|free|accept victim", 35),
         ("Calling 108 and comforting the injured saves lives during the Golden Hour", "Focuses on prompt medical care.", False, "golden hour|save lives|call 108", 20)],
        ["bystanders go to jail", "leave victim bleeding", "take selfies"],
        "Ministry of Road Transport Good Samaritan Guidelines", "https://morth.nic.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Signal")
    return cards


def get_pulse_cards():
    cards = []

    # 1. AID-021: Cuts & bleeding
    cards.append(make_card(
        "AID-021", "pulse", "Bleeding", "Direct pressure first aid for severe cuts and bleeding",
        ["junior", "middle", "senior"],
        ["Continuous firm pressure directly on an open cut stops over 90% of bleeding by enabling clotting.",
         "Peeling off a blood-soaked bandage rips away developing platelet clots; always layer new cloth on top."],
        ["Press firmly on the wound using a clean cloth, sterile gauze, or clean handkerchief", "Maintain continuous pressure for at least 10 minutes without lifting to check", "Elevate the injured limb above heart level if no bone fracture is suspected"],
        ["Never put turmeric powder, mud, coffee or ash on open wounds", "Never remove an embedded object like glass or metal"],
        "Applying turmeric or coffee powder to deep wounds heals them safely.", "myth", "Home powders cause horrific wound infections and tissue necrosis. Use clean direct pressure.",
        "A friend cuts their arm deeply on broken glass and blood is flowing. What is the immediate first aid?",
        ["Pour haldi into it", "Apply firm continuous direct pressure with a clean cloth", "Wash with hot water", "Wave arm in air"], 1,
        "Firm direct pressure compresses severed capillaries and allows natural clotting.",
        ["In the craft room at {at}, a cutter slips and {name}'s friend cuts their hand deeply."],
        "What should {name} do right now?",
        [("Apply firm direct pressure with a clean cloth or gauze", "Compresses blood vessels to stop bleeding.", True, "direct pressure|press|clean cloth|gauze", 40),
         ("If cloth soaks through, add another cloth on top without removing the first", "Preserves newly formed blood clots.", True, "don'?t remove|layer on top|add more cloth", 30),
         ("Call teacher/school nurse and seek medical help for stitches/tetanus", "Professional wound closure.", False, "call nurse|teacher|doctor|112", 30)],
        ["haldi|turmeric|coffee", "remove soaked cloth", "wash with hot water"],
        "Indian Red Cross Society First Aid Manual", "https://indianredcross.org"
    ))

    # 2. AID-022: Animal bite
    cards.append(make_card(
        "AID-022", "pulse", "Animal bite", "Dog bite and scratch: Urgent rabies protocol",
        ["junior", "middle", "senior"],
        ["Rabies is transmitted via infected animal saliva and is nearly 100% fatal once symptoms appear.",
         "Washing thoroughly with soap and running water physically washes away virus particles."],
        ["Wash wound immediately under running tap water with soap for at least 15 continuous minutes", "Apply an antiseptic solution like povidone iodine after thorough washing", "Visit a medical clinic the same day for anti-rabies vaccination (PEP) and tetanus toxoid"],
        ["Never apply chili powder, lime, oil, or turmeric to animal bites", "Never tie a tight bandage over open animal bite wounds"],
        "A minor scratch from a friendly stray puppy does not need a doctor's visit.", "myth", "Any scratch that breaks skin can transmit rabies. Immediate washing and vaccination are mandatory.",
        "What is the first and most critical step immediately after a dog bite or scratch?",
        ["Wait 10 days", "Wash under running water with soap for 15 minutes", "Tie a cloth tightly", "Apply mustard oil"], 1,
        "Soap dissolves the rabies viral lipid envelope and running water flushes it away.",
        ["While playing at {at}, a stray dog bites {name}'s calf, breaking the skin."],
        "What must {name} do immediately?",
        [("Wash the wound under running tap water with soap for 15 minutes", "Flushes out saliva and inactivates rabies virus.", True, "wash[^.]{0,20}(soap|water)|15 min|running water", 45),
         ("Apply antiseptic and do not bandage tightly", "Prevents secondary infection without trapping virus.", False, "antiseptic|betadine|povidone|no tight bandage", 20),
         ("Go to a hospital or clinic on the same day for rabies vaccine", "Post-exposure prophylaxis saves lives.", True, "hospital|doctor|rabies vaccine|injection|same day", 35)],
        ["chili powder", "haldi|turmeric", "bandage tightly", "ignore bite"],
        "National Centre for Disease Control (NCDC)", "https://ncdc.gov.in"
    ))

    # 3. AID-023: Fainting
    cards.append(make_card(
        "AID-023", "pulse", "Fainting", "Fainting first aid and the recovery position",
        ["junior", "middle", "senior"],
        ["Fainting (syncope) occurs when temporary blood flow to the brain drops.",
         "Laying the person flat and elevating their feet returns pooled blood to the heart and brain."],
        ["Lay the person flat on their back and elevate legs 30 cm (12 inches)", "Loosen tight collars, ties, and belts to aid respiration", "Turn onto side (recovery position) if vomiting or not waking within 1 minute"],
        ["Never force an unconscious person to drink water or eat sugar", "Never make a fainting person stand up quickly"],
        "Splashing cold water into a fainted person's face will wake them up safely.", "myth", "Splashing water can cause aspiration into the windpipe and choke an unconscious person.",
        "A student collapses and faints during morning school assembly. What is the correct response?",
        ["Pour water into mouth", "Lay flat on back and elevate feet 30 cm", "Slap cheeks", "Make them run"], 1,
        "Laying flat and raising legs restores blood circulation to the brain.",
        ["During school assembly at {at}, a classmate suddenly sways and collapses unconscious onto the floor."],
        "What is the proper first aid response for {name}?",
        [("Lay them flat on their back and elevate their feet/legs", "Promotes venous blood return to brain.", True, "lay flat|raise legs|elevate feet", 40),
         ("Loosen tight collar, tie, and ask crowd to step back for fresh air", "Ensures open airway and cool environment.", True, "loosen collar|fresh air|crowd back", 30),
         ("Do not force liquids into mouth; call school nurse/doctor", "Prevents choking and aspiration.", False, "no water in mouth|call nurse|doctor", 30)],
        ["pour water into mouth", "slap face", "force to stand up"],
        "World Health Organization Basic First Aid", "https://who.int"
    ))

    # 4. AID-024: Sprains
    cards.append(make_card(
        "AID-024", "pulse", "Sprains", "Treating sprains and strains with the RICE method",
        ["junior", "middle", "senior"],
        ["A sprain is a stretched or torn ligament supporting a joint (commonly ankle or wrist).",
         "Applying direct ice without a cloth barrier can cause frostbite skin burns."],
        ["Rest the injured joint immediately—stop playing sports", "Ice the area using a cloth-wrapped cold pack for 15-20 minutes", "Compress lightly with an elastic crepe bandage and Elevate above heart level"],
        ["Never apply hot balms, heat packs or massage during the first 48 hours", "Never wrap an elastic bandage so tightly that toes turn blue or numb"],
        "Massaging a freshly sprained ankle with warm mustard oil speeds recovery.", "myth", "Heat and massage increase internal bleeding and joint swelling. Use cold RICE protocol.",
        "What does the 'I' in the RICE sprain treatment stand for?",
        ["Ignore", "Ice (wrapped in cloth for 15-20 mins)", "Instant run", "Iodine spray"], 1,
        "Ice constricts injured blood vessels, reducing swelling and pain.",
        ["During a basketball match at {at}, {name}'s friend twists their ankle and falls in pain."],
        "How should {name} assist using RICE?",
        [("Stop play and rest the injured ankle completely", "Prevents further ligament tearing.", True, "rest|stop playing|sit down", 30),
         ("Apply a cold ice pack wrapped in a towel for 15 minutes", "Reduces swelling and inflammation.", True, "ice|cold pack|wrap in towel", 40),
         ("Elevate the ankle on a chair/pillow and seek adult evaluation", "Facilitates fluid drainage away from joint.", False, "elevate|raise ankle|doctor|nurse", 30)],
        ["massage vigorously", "hot balm", "continue playing"],
        "Indian Orthopaedic Association", "https://ioaindia.org"
    ))

    # 5. AID-025: Fractures
    cards.append(make_card(
        "AID-025", "pulse", "Fractures", "Suspected bone fracture: Splinting and immobilization",
        ["middle", "senior"],
        ["Moving broken bone fragments can sever adjacent nerves, arteries, and muscle tissue.",
         "Supporting the joint above and below the injury stabilizes the fracture."],
        ["Keep the injured limb completely still in the position found", "Support the limb with rolled magazines, cardboard, or a folded towel as a temporary splint", "Call 108 / 112 or get adult transport to an emergency hospital"],
        ["Never attempt to straighten a bent or deformed limb", "Never give food or water in case emergency surgery is needed"],
        "If a broken bone looks bent, you should pull it straight right away.", "myth", "Attempting to realign bones without anesthesia causes severe agony and tears blood vessels.",
        "What is the most critical first aid rule for a suspected broken arm?",
        ["Pull it straight", "Immobilize and support it without moving the bone", "Give a heavy meal", "Massage with oil"], 1,
        "Immobilization prevents bone ends from cutting internal nerves and arteries.",
        ["A student falls from the jungle gym at {at} and holds a visibly deformed, painful forearm."],
        "What first aid should {name} provide?",
        [("Do not move or attempt to straighten the injured arm", "Avoids nerve and vascular damage.", True, "don'?t move|do not straighten|keep still", 45),
         ("Support the limb gently with a sling or soft padding", "Stabilizes limb comfortably.", True, "support|sling|padding|cushion", 30),
         ("Call the school nurse/108 and keep the student calm", "Arranges professional orthopaedic transport.", False, "call 108|nurse|hospital|adult", 25)],
        ["pull straight", "massage bone", "force to move fingers"],
        "St John Ambulance First Aid Guidelines", "https://stjohn.org"
    ))

    # 6. AID-026: Snake bite
    cards.append(make_card(
        "AID-026", "pulse", "Snake bite", "Snake bite do's and don'ts: Safe emergency response",
        ["junior", "middle", "senior"],
        ["India's 'Big Four' venomous snakes are the Russell's viper, saw-scaled viper, cobra, and krait.",
         "Cutting, sucking venom, or tying tight tourniquets causes gangrene and limb amputations."],
        ["Keep the victim calm, still, and reassure them (panic accelerates venom circulation)", "Immobilize the bitten limb with a loose splint below heart level", "Transport immediately to a government hospital equipped with Anti-Snake Venom (ASV)"],
        ["Never cut the bite with blades or suck out venom with mouth", "Never tie tight rope tourniquets that stop pulse"],
        "Sucking venom out with your mouth like in movies saves snake bite victims.", "myth", "Mouth suction removes zero venom, poisons the rescuer, and introduces deadly mouth bacteria.",
        "What is the only proven medical cure for a venomous snake bite?",
        ["Herbal leaf paste", "Anti-Snake Venom (ASV) administered at a hospital", "Cutting the skin", "Drinking milk"], 1,
        "Anti-Snake Venom neutralizes circulating venom toxins effectively.",
        ["While walking in garden bushes at {at}, {name}'s friend is bitten on the ankle by a snake."],
        "What must {name} do?",
        [("Keep friend completely calm and still without walking", "Muscle contraction pumps venom through lymphatics.", True, "keep calm|still|don'?t walk|sit down", 40),
         ("Do not cut, suck venom, or tie tight tourniquets", "Prevents tissue necrosis and gangrene.", True, "no cutting|no sucking|no tourniquet", 35),
         ("Rush directly to the nearest hospital with Anti-Snake Venom", "ASV is the sole antidote.", False, "hospital|asv|anti snake venom|doctor", 25)],
        ["cut with blade", "suck venom", "tie tight rope tourniquet"],
        "National Health Mission (NHM) Snakebite Protocol", "https://nhm.gov.in"
    ))

    # 7. AID-027: Insect stings
    cards.append(make_card(
        "AID-027", "pulse", "Insect sting", "Bee, wasp and hornet stings: Safe stinger removal",
        ["junior", "middle", "senior"],
        ["A honeybee stinger has an attached venom sac that continues pumping venom for 60 seconds.",
         "Squeezing a stinger with tweezers or fingers squeezes remaining venom into the skin."],
        ["Scrape the stinger out sideways using a fingernail or plastic card edge immediately", "Wash the area with soap and water, then apply a cold ice pack for 10 minutes", "Watch for allergic reactions (facial swelling, throat tightness, breathing trouble) -> 108"],
        ["Never squeeze the venom sac with tweezers", "Never scratch the sting site"],
        "Pulling a bee stinger out with pinchers is the best way to remove it.", "myth", "Pinching squeezes the venom sac like a dropper. Scrape it off sideways.",
        "How should you remove a bee stinger embedded in your arm?",
        ["Pinch firmly with fingers", "Scrape it out sideways with a fingernail or plastic card", "Burn it with match", "Suck it out"], 1,
        "Scraping removes the stinger without injecting venom from the attached gland.",
        ["A bee stings {name}'s classmate on the hand in the garden at {at}."],
        "What is the correct first aid technique?",
        [("Scrape the stinger off sideways using a ruler, card or fingernail", "Prevents injecting remaining venom sac contents.", True, "scrape|plastic card|fingernail|sideways", 40),
         ("Apply a cold ice pack wrapped in a cloth to soothe swelling", "Reduces localized pain and inflammation.", True, "ice pack|cold cloth|wash soap", 35),
         ("Check for signs of severe allergic reaction (anaphylaxis)", "Life-threatening emergencies need 108.", False, "allergic reaction|swelling|breathing|108", 25)],
        ["squeeze venom sac", "burn stinger", "rub with mud"],
        "Indian Academy of Pediatrics (IAP)", "https://iapindia.org"
    ))

    # 8. AID-028: Asthma attack
    cards.append(make_card(
        "AID-028", "pulse", "Asthma", "Supporting a classmate having an asthma attack",
        ["junior", "middle", "senior"],
        ["Asthma causes airway narrowing, wheezing, chest tightness, and shortness of breath.",
         "Laying an asthma patient flat makes breathing significantly harder."],
        ["Help the student sit upright comfortably and stay calm and reassuring", "Help them locate their prescribed rescue inhaler (blue cap) and spacer", "Call the school nurse or 108 if symptoms worsen or inhaler is unavailable"],
        ["Never force an asthmatic person to lie down flat", "Never crowd around them or give random medicines"],
        "During an asthma attack, making the person lie down flat helps them breathe.", "myth", "Lying down compresses lung capacity. Sitting upright allows diaphragm expansion.",
        "What position helps a student breathe easiest during an asthma attack?",
        ["Lying flat on stomach", "Sitting upright leaning slightly forward", "Hanging upside down", "Running"], 1,
        "Sitting upright with shoulders relaxed gives lungs the maximum expansion volume.",
        ["After running in sports class at {at}, a classmate begins wheezing heavily and gasping for air."],
        "How should {name} assist them?",
        [("Help them sit upright comfortably and stay calm", "Opens airways and prevents panic hyperventilation.", True, "sit upright|lean forward|stay calm", 40),
         ("Help them locate their prescribed inhaler with adult supervision", "Delivers bronchodilator medicine.", True, "inhaler|puffer|spacer|adult", 35),
         ("Call the school nurse or teacher immediately", "Ensures medical supervision.", False, "call nurse|teacher|108", 25)],
        ["lay flat on back", "crowd around", "give cold water"],
        "Chest Council of India", "https://chestcouncil.org"
    ))

    # 9. AID-029: Electric shock
    cards.append(make_card(
        "AID-029", "pulse", "Electric shock", "Electric shock rescue: Safety of the rescuer first",
        ["junior", "middle", "senior"],
        ["The human body is an excellent electrical conductor; touching a victim passes current to you.",
         "Electric current causes muscle spasm (tetany), preventing victims from releasing live wires."],
        ["Turn off the main electrical circuit breaker / switch immediately", "If mains cannot be reached, use a dry non-conductive object (wooden broom handle) to separate wire from victim", "Check breathing once separated; call 108 / 112 immediately"],
        ["Never touch an electrocuted person with bare hands while they are connected", "Never use metal, wet wood, or damp cloth to push wires away"],
        "If someone is caught by electric current, pulling their shirt with bare hands is safe.", "myth", "Electric current instantly travels through clothing moisture into the rescuer.",
        "What must you do first before touching someone who is touching a live electrical wire?",
        ["Touch their arm", "Turn off the main power switch or circuit breaker", "Pour water on them", "Put a blanket over them"], 1,
        "Always de-energize the circuit first so the rescuer does not get electrocuted.",
        ["In the laundry area at {at}, {name} sees someone shaking and frozen touching a frayed appliance cord."],
        "What is {name}'s immediate action?",
        [("Do NOT touch the victim with bare hands", "Prevents rescuer electrocution.", True, "do not touch|don'?t touch bare|hands off", 40),
         ("Switch off the main power switch or unplug the appliance", "Cuts circuit instantly.", True, "switch off|turn off mains|unplug|breaker", 40),
         ("Use dry wooden broom handle if switch is inaccessible, then call 108", "Insulating tool for emergency separation.", False, "dry wood|broom|plastic|call 108", 20)],
        ["touch victim directly", "pour water", "pull with bare hands"],
        "Central Electricity Authority Safety Norms", "https://cea.nic.in"
    ))

    # 10. AID-030: Eye injuries
    cards.append(make_card(
        "AID-030", "pulse", "Eye injury", "Eye first aid: Chemical splashes and foreign particles",
        ["junior", "middle", "senior"],
        ["Rubbing an eye with a speck of dust scratches the sensitive transparent cornea.",
         "Chemical splashes (detergents, lab acids, lime) require immediate 15-minute continuous flushing."],
        ["Flush the eye gently with clean running tap water or saline for 15 minutes for chemicals", "Blink repeatedly in a bowl of clean water to dislodge loose eyelashes or dust", "Cover loosely with a clean paper cup or eye pad and see an ophthalmologist"],
        ["Never rub the eye with fingers, knuckles, or dirty handkerchiefs", "Never attempt to remove an object embedded into the eyeball with needles or tweezers"],
        "Rubbing your eye vigorously removes dust particles quickly.", "myth", "Rubbing grinds abrasive particles into the corneal lens, causing permanent scarring.",
        "What is the first aid for household cleaning liquid splashed into a student's eye?",
        ["Close eye tightly", "Rinse immediately with clean lukewarm running water for 15 minutes", "Apply eye drops blindly", "Rub with towel"], 1,
        "Continuous irrigation flushes chemicals out before chemical burns occur.",
        ["In the chemistry lab at {at}, liquid cleaning detergent splashes into {name}'s classmate's eye."],
        "What must {name} and classmate do immediately?",
        [("Rinse eye continuously under running tap water for at least 15 minutes", "Flushes chemical irritant before corneal burning.", True, "flush|rinse|running water|15 min|eye wash", 45),
         ("Do not rub the eye with hands or cloth", "Prevents corneal abrasion.", True, "don'?t rub|do not scratch", 30),
         ("Inform teacher and consult an eye doctor immediately", "Professional ophthalmic check.", False, "tell teacher|eye doctor|hospital", 25)],
        ["rub eye", "close and wait", "apply random eye drops"],
        "All India Ophthalmological Society (AIOS)", "https://aios.org"
    ))

    # 11. AID-031: Head bump
    cards.append(make_card(
        "AID-031", "pulse", "Head injury", "Head bump, concussion signs, and danger symptoms",
        ["junior", "middle", "senior"],
        ["A concussion is a traumatic brain injury that affects mental cognitive function.",
         "Repeated vomiting, confusion, or unequal pupils indicate increasing intracranial pressure."],
        ["Rest quietly and apply a cold compress wrapped in cloth to the bump for 15 minutes", "Monitor closely for red-flag symptoms: repeated vomiting, drowsiness, uneven pupils, confusion", "Take to an emergency doctor immediately if red flags appear or if knocked unconscious"],
        ["Never let an athlete return to play sports on the same day after a head blow", "Never ignore a child who cannot remember what happened before the fall"],
        "A child who bumps their head can return to playing cricket immediately if they don't bleed.", "myth", "Concussions occur without external bleeding. Rest and monitoring are vital.",
        "Which of the following is a dangerous symptom following a head bump?",
        ["A small superficial skin bump", "Repeated vomiting and extreme drowsiness", "Normal hunger", "Crying for 1 minute then laughing"], 1,
        "Repeated vomiting and drowsiness signal internal brain swelling or bleeding.",
        ["During PE class at {at}, a classmate collides heads with another player and falls to the ground dizzy."],
        "How should {name} and the coach manage this head injury?",
        [("Stop playing immediately and rest quietly", "Prevents secondary impact syndrome.", True, "stop playing|rest|sit down|no sports", 35),
         ("Apply a cold compress to the site of impact", "Reduces scalp swelling.", False, "cold compress|ice pack|cloth", 25),
         ("Watch for danger signs: vomiting, severe headache, confusion -> hospital", "Indicates serious concussion.", True, "vomiting|confusion|drowsy|doctor|hospital", 40)],
        ["return to game immediately", "ignore dizziness", "shake head"],
        "Indian Journal of Neurotrauma Guidelines", "https://ijnt.org"
    ))

    # 12. AID-032: Seizures
    cards.append(make_card(
        "AID-032", "pulse", "Seizures", "Seizure first aid: Protecting without restraining",
        ["middle", "senior"],
        ["Seizures are temporary electrical disturbances in the brain causing involuntary muscle convulsions.",
         "Putting objects into a seizing person's mouth breaks teeth and blocks their airway."],
        ["Clear hard, sharp, or hot objects away from around the seizing person", "Cushion their head with a folded jacket or soft pillow", "Turn onto side (recovery position) once jerking stops to keep airway clear"],
        ["Never put spoons, keys, fingers or cloth into their mouth (they cannot swallow their tongue)", "Never hold down or forcefully restrain seizing arms and legs"],
        "Putting an iron key in a person's hand stops an epileptic seizure.", "myth", "Metal keys have zero medical effect on neurological seizures. Keep safe and clear space.",
        "What is the single most important 'DON'T' during an active epileptic seizure?",
        ["Cushioning head", "Never force spoons, fingers or keys into their mouth", "Timing the seizure", "Loosening collars"], 1,
        "Forcing objects into the mouth breaks teeth and suffocates the person.",
        ["A student in the classroom at {at} collapses and begins experiencing jerking convulsions."],
        "What first aid should {name} provide?",
        [("Clear nearby desks, chairs, and sharp items away", "Prevents head and bodily impact injuries.", True, "clear space|move desks|sharp objects", 35),
         ("Cushion head with folded clothes and do NOT put anything in mouth", "Protects skull; avoids airway obstruction.", True, "cushion head|nothing in mouth|no spoon|no key", 40),
         ("Time the seizure duration and turn to side after jerking stops", "Monitors status and prevents saliva aspiration.", False, "time duration|turn on side|recovery position|call 108", 25)],
        ["put spoon in mouth", "put keys in hand", "restrain arms forcefully"],
        "Indian Epilepsy Association", "https://epilepsyindia.org"
    ))

    # 13. AID-033: Water rescue
    cards.append(make_card(
        "AID-033", "pulse", "Water rescue", "Water rescue safety: Reach or throw, don't jump in",
        ["junior", "middle", "senior"],
        ["A drowning person panics instinctively and will climb on top of a rescuer, drowning both.",
         "Over 70% of drowning victims drown within 10 meters of a safe bank or pool edge."],
        ["Shout loudly for adult help immediately", "Extend a long stick, tree branch, bamboo pole, or towel while lying flat on the bank (REACH)", "Throw a floating lifebuoy, plastic can, football, or rope (THROW)"],
        ["Never jump into deep water to rescue someone unless trained in life-saving", "Never stand upright on slippery banks while pulling someone"],
        "Jumping into the water is the fastest and best way to save a drowning friend.", "myth", "Untrained rescuers are pulled under and drowned by panicked drowning victims.",
        "What is the golden sequence for non-swimmer water rescue?",
        ["Jump, swim, pull", "Shout for help, Reach with pole, or Throw floating object", "Dive deep", "Wait and watch"], 1,
        "Reach or Throw keeps the rescuer safely dry on the bank while saving the victim.",
        ["While near a river bank or pool at {at}, {name} sees someone struggling and splashing in deep water."],
        "What should {name} do?",
        [("Shout loudly for adult help and emergency assistance", "Alerts nearby capable swimmers.", True, "shout for help|call adults|call 112", 35),
         ("Reach with a long stick or branch while lying flat on stomach", "Lying flat prevents rescuer being pulled into water.", True, "reach|stick|branch|pole|lie flat", 40),
         ("Throw a floating object (can, tire tube, ring, football)", "Provides buoyancy until help arrives.", False, "throw|floating object|buoy|rope", 25)],
        ["jump in water", "swim without training", "stand on slippery edge"],
        "Rashtriya Life Saving Society (RLSS India)", "https://lifesavingindia.org"
    ))

    # 14. AID-034: Poisoning
    cards.append(make_card(
        "AID-034", "pulse", "Poisoning", "Accidental chemical or pesticide ingestion first aid",
        ["junior", "middle", "senior"],
        ["Swallowed corrosives (toilet cleaner, acid, bleach) burn the throat coming down.",
         "Inducing vomiting burns the esophagus a second time and can enter lungs (chemical pneumonitis)."],
        ["Call 108 / 112 or national poison control helpline immediately", "Identify the substance and keep the bottle/package for doctors", "Rinse mouth with water if corrosive was held in mouth without swallowing"],
        ["Never make the victim vomit (unless specifically told by a poison doctor)", "Never force them to drink raw eggs, salt water, or milk blindly"],
        "Making a person drink concentrated salt water to induce vomiting is standard poison first aid.", "myth", "Salt water causes fatal salt poisoning and vomiting burns the esophagus.",
        "If a child accidentally swallows toilet cleaner, why should you NOT induce vomiting?",
        ["It wastes cleaner", "The corrosive chemical burns the throat a second time on the way up", "It tastes bad", "It stops hiccups"], 1,
        "Corrosives burn tissue twice if vomited, causing catastrophic airway damage.",
        ["A young child at {at} accidentally sips from an unmarked bottle containing liquid floor disinfectant."],
        "What must {name} do?",
        [("Do NOT induce vomiting or force liquids", "Prevents chemical burns and lung aspiration.", True, "do not induce vomiting|don'?t make vomit|no salt water", 40),
         ("Keep the chemical bottle and packaging to show emergency doctors", "Enables doctors to identify exact toxins.", True, "keep bottle|identify chemical|packaging", 35),
         ("Call 108 / 112 and rush to hospital emergency immediately", "Emergency gastric decontamination.", False, "call 108|112|hospital|emergency", 25)],
        ["make vomit", "feed raw eggs", "give salt water"],
        "National Poisons Information Centre (AIIMS New Delhi)", "https://aiims.edu"
    ))

    # 15. AID-035: Calling 108/112
    cards.append(make_card(
        "AID-035", "pulse", "Calling 108/112", "Mastering medical emergency calls (108 / 112)",
        ["junior", "middle", "senior"],
        ["Emergency dispatchers initiate ambulance sirens while still on the call gathering facts.",
         "Answering dispatcher questions does NOT delay the ambulance arrival time."],
        ["State exact location first with specific nearby landmark (school gate, petrol pump, temple)", "Describe what happened, how many are injured, and if anyone is unconscious", "Follow dispatcher instructions and do not hang up until they tell you to"],
        ["Never hang up in frustration while answering operator questions", "Never make prank calls to 108 / 112 (punishable by law)"],
        "Staying on the phone answering 108 questions delays the ambulance from leaving.", "myth", "The nearest ambulance is dispatched immediately; the call gathers preparation data.",
        "Why is stating a prominent landmark essential when calling 108 for an ambulance in India?",
        ["To chat", "GPS can be imprecise; landmarks guide drivers directly through crowded streets", "To test the operator", "It is optional"], 1,
        "Landmarks prevent ambulances from getting lost in winding Indian colony streets.",
        ["An elderly neighbour collapses at {at} and {name} dials 108."],
        "How should {name} deliver the emergency report?",
        [("Give exact colony address, gate number, and nearest landmark first", "Allows driver navigation immediately.", True, "address|location|landmark|gate number", 45),
         ("State patient's consciousness, breathing status, and age", "Prepares oxygen/defibrillator equipment.", True, "conscious|breathing|condition|age", 35),
         ("Stay on the line and unlock the building gate for ambulance crew", "Speeds paramedic entry.", False, "stay on line|open gate|wait for crew", 20)],
        ["hang up abruptly", "give vague city name only", "prank call"],
        "EMRI Green Health Services (108 Ambulance)", "https://emri.in"
    ))

    # 16. AID-036: First aid kit
    cards.append(make_card(
        "AID-036", "pulse", "First aid kit", "Assembling a student home first-aid kit",
        ["junior", "middle", "senior"],
        ["A well-organized first aid kit contains supplies for bleeding, burns, and sprains.",
         "First aid kits should NEVER contain unprescribed prescription medicines or antibiotics."],
        ["Stock sterile gauze pads, adhesive bandages (band-aids), and medical adhesive tape", "Include antiseptic liquid/ointment, blunt-ended safety scissors, and crepe roller bandages", "Keep kit in an accessible, dry, cool place known to all family members"],
        ["Never store loose, expired or unlabeled medicine tablets in a first aid kit", "Never lock the kit so tightly that it cannot be opened in a rush"],
        "A good first aid kit should be packed with leftover antibiotic capsules.", "myth", "First aid kits are for immediate trauma care. Unprescribed antibiotics are dangerous.",
        "Which of the following belongs in a standard home first-aid kit?",
        ["Expired pills", "Sterile gauze, adhesive bandages, antiseptic, and scissors", "Candy", "Needles"], 1,
        "Clean wound dressing supplies and antiseptic are standard first aid essentials.",
        ["{name}'s family at {at} is assembling their home first-aid kit."],
        "What essential supplies should {name} ensure are packed in the box?",
        [("Pack sterile gauze pads, band-aids, and roller bandages", "For managing bleeding and bandaging cuts.", True, "gauze|band-aid|bandage|dressing", 40),
         ("Include antiseptic lotion, adhesive tape, and clean scissors", "For sanitizing and cutting tape.", True, "antiseptic|tape|scissors", 35),
         ("Store in an easily accessible, dry location known to the family", "Ensures immediate access during emergencies.", False, "accessible|dry place|known location", 25)],
        ["pack random loose pills", "lock with secret code", "store in wet bathroom"],
        "Indian Red Cross Society", "https://indianredcross.org"
    ))

    print(f"Loaded {len(cards)} expanded cards for Pulse")
    return cards
