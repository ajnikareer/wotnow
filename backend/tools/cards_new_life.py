"""
New Agents in the LIFE Pillar:
- Storm (Disaster Readiness - DIS)
- Guardian (Personal & Body Safety - SAFE) [sensitive, approve-first]
- Nyaya (Rights & Law - LAW)
- Stride (Fitness & Body Care - FIT)
- Care (Hygiene & Self-care - HYG) [sensitive puberty cards]
"""
from cards_existing import make_card

def get_storm_cards():
    cards = []

    # DIS-001: Earthquake indoors
    cards.append(make_card(
        "DIS-001", "storm", "Earthquake", "Earthquake indoors: Drop, Cover, and Hold On",
        ["junior", "middle", "senior"],
        ["Falling debris, collapsing ceiling plaster, and shattering glass cause most earthquake injuries.",
         "Taking shelter under sturdy furniture protects your vital head, neck, and torso."],
        ["DROP onto your hands and knees immediately to prevent being knocked over", "COVER your head and neck under a sturdy table, desk, or bed", "HOLD ON to the furniture leg until the ground stops shaking"],
        ["Never run outside during active shaking (falling building tiles and glass will strike you)", "Never use elevators during or immediately after an earthquake"],
        "Standing in a doorway is the safest spot during an indoor earthquake.", "myth", "Modern door frames are not reinforced and doors swinging violently crush fingers. Drop, cover, and hold under a desk.",
        "What is the internationally proven emergency response when ground shaking starts indoors?",
        ["Run into the corridor", "Drop, Cover, and Hold On under a sturdy desk", "Stand near glass windows", "Take the elevator"], 1,
        "Dropping low under sturdy desks protects vital organs from falling masonry and glass.",
        ["In the classroom or home at {at}, violent earthquake tremors begin rattling the room."],
        "What should {name} do immediately?",
        [("Drop immediately under a sturdy desk or table", "Prevents being thrown down and protects from ceiling debris.", True, "drop|under desk|table|cover", 45),
         ("Hold onto the desk legs and cover head and neck with arms", "Keeps shield in place as furniture shifts.", True, "hold on|cover head|protect neck", 35),
         ("Stay indoors away from windows until shaking ceases completely", "Escaping mid-shake is when most injuries occur.", False, "stay indoors|away from windows|wait for shaking to stop", 20)],
        ["run down stairs during shaking", "use elevator", "stand near glass"],
        "National Disaster Management Authority (NDMA)", "https://ndma.gov.in"
    ))

    # DIS-002: Earthquake outdoors
    cards.append(make_card(
        "DIS-002", "storm", "Earthquake", "Earthquake outdoors: Finding open space",
        ["junior", "middle", "senior"],
        ["Outside buildings, the greatest hazards are falling glass facades, signage, brick cornices, and electric poles.",
         "The 'danger zone' extends directly outwards from exterior building walls."],
        ["Move quickly to an open clearing away from buildings, streetlights, and power cables", "Drop to the ground and cover your head until shaking stops", "If in a vehicle, have the driver pull over safely away from overpasses and bridges"],
        ["Never shelter directly under building balconies, awnings, or billboards", "Never touch fallen overhead electric cables"],
        "Standing right next to the outer wall of a tall building protects you during an earthquake.", "myth", "Exterior walls shed glass, air conditioners, and concrete slabs first. Move into open clearings.",
        "When an earthquake strikes while you are walking outdoors on a street, where should you head?",
        ["Under a large glass billboard", "Into an open ground or wide space away from buildings and power poles", "Into an underground basement", "Under a tree"], 1,
        "Open spaces away from falling overhead architecture are the safest outdoor refuge zones.",
        ["Walking in a market street at {at}, the ground shakes violently and streetlamps sway."],
        "How should {name} seek safety?",
        [("Move away from building walls, hoardings, and electric poles into an open area", "Evades falling architectural debris.", True, "open space|away from buildings|clear area|no poles", 45),
         ("Drop to the ground and protect your head with your bag or hands", "Prevents falling and shields skull.", True, "drop|protect head|cover with bag", 35),
         ("Stay alert to moving vehicles and stay away from elevated flyovers", "Overpasses suffer structural resonance.", False, "away from flyovers|alert", 20)],
        ["stand under glass facade", "touch electric poles", "run into collapsing shops"],
        "NDMA Earthquake Safety Guidelines", "https://ndma.gov.in"
    ))

    # DIS-003: Post-earthquake checks
    cards.append(make_card(
        "DIS-003", "storm", "Aftermath", "Post-earthquake evacuation: Gas, aftershocks and stairs",
        ["junior", "middle", "senior"],
        ["Earthquakes sever underground gas lines and weaken building support pillars.",
         "Aftershocks can occur minutes, hours, or days later, collapsing already-damaged structures."],
        ["Evacuate using stairwells calmly once shaking stops; never use elevators", "Check for gas leaks: if you smell gas, open windows, do not touch switches, and evacuate outside", "Expect aftershocks and be prepared to Drop, Cover, and Hold on again"],
        ["Never light matches, candles, or lighters after an earthquake", "Never re-enter a visibly cracked building until certified safe by structural engineers"],
        "Using the elevator right after an earthquake is safe if power is working.", "myth", "Elevator shafts warp during quakes and aftershocks will trap you inside in total darkness. Take stairs.",
        "Why must you never strike a match or lighter after an earthquake?",
        ["It wastes matches", "Broken underground gas pipes can cause an instant explosion", "It attracts rain", "No reason"], 1,
        "Gas leaks are widespread post-quake; any spark causes devastating fires.",
        ["The ground stops shaking at {at}. {name}'s family needs to evacuate their multi-story building."],
        "What evacuation protocol should {name} ensure?",
        [("Take the stairs calmly in single file; never use the elevator", "Prevents getting trapped in damaged elevator shafts.", True, "stairs|no elevator|stairwell|walk calm", 45),
         ("Do not switch on lights or strike matches in case of broken gas lines", "Prevents gas explosions.", True, "no matches|no lighters|check gas smell", 35),
         ("Assemble at the outdoor neighborhood open ground and prepare for aftershocks", "Safe congregation point.", False, "open ground|assembly point|aftershocks", 20)],
        ["take the lift", "light candle to see in dark", "run back inside damaged flat"],
        "NDMA Post-Disaster Protocol", "https://ndma.gov.in"
    ))

    # DIS-004: Flood evacuation
    cards.append(make_card(
        "DIS-004", "storm", "Floods", "Home flood evacuation: Moving high and cutting power",
        ["junior", "middle", "senior"],
        ["Just 15 cm (6 inches) of fast-moving floodwater can knock a person off their feet.",
         "Rising floodwaters reaching wall sockets electrocute entire flooded ground floors."],
        ["Switch off main electrical circuit breakers and close the cylinder gas regulator before evacuating", "Move to upper floors or higher ground with your emergency go-bag", "Follow official disaster warnings and evacuate early before water cuts off road exits"],
        ["Never walk, swim, or drive through moving floodwaters ('Turn Around, Don't Drown')", "Never touch electrical equipment while standing in water"],
        "If floodwater looks only ankle-deep, it is completely safe to walk across the street.", "myth", "Ankle-deep rushing water possesses enormous kinetic force and hides open manholes and live electrical cables.",
        "What is the vital electrical action before water enters your home?",
        ["Turn on all lights", "Turn off the main electrical circuit breaker (MCB) immediately", "Plug in appliances", "Nothing"], 1,
        "Cutting mains power prevents waterlogged house electrocution.",
        ["Monsoon rains cause river water to rise rapidly near {name}'s home at {at}."],
        "What should {name} and family do before water enters the ground floor?",
        [("Switch off the main electrical power breaker and turn off gas regulator", "Eliminates electrocution and gas fire risks.", True, "switch off mains|cut power|breaker|gas off", 45),
         ("Move essential documents, medications, and family to higher floors or relief shelter", "Preserves life and vital papers.", True, "higher floors|higher ground|evacuate|shelter", 35),
         ("Do not wade through rushing brown floodwater outside", "Prevents drowning and missing drain falls.", False, "don'?t wade|avoid floodwater", 20)],
        ["walk into rushing currents", "leave electrical mains on", "ignore evacuation alerts"],
        "Central Water Commission (CWC)", "https://cwc.gov.in"
    ))

    # DIS-005: Cyclone warning
    cards.append(make_card(
        "DIS-005", "storm", "Cyclones", "Cyclone alert readiness: Securing home and tracking alerts",
        ["junior", "middle", "senior"],
        ["Tropical cyclones produce destructive winds over 150 km/h, storm surges, and torrential downpours.",
         "Unsecured tin roofs, loose metal sheets, and tree branches turn into deadly high-speed projectiles."],
        ["Secure or bring indoors all loose outdoor objects, flowerpots, and tin sheets", "Tape large window panes diagonally with duct tape to prevent flying glass shards", "Tune into official All India Radio / IMD weather bulletins on a battery-powered radio or phone"],
        ["Never step outside during the calm 'eye of the storm' (destructive reverse winds resume abruptly)", "Never believe unverified WhatsApp cyclone forward rumors"],
        "When the wind suddenly goes completely calm during a cyclone, the storm is officially over.", "myth", "This is the 'eye of the cyclone'. The other half of the eyewall with violent opposite winds will strike shortly.",
        "What happens when the calm 'eye' of a tropical cyclone passes directly overhead?",
        ["The storm is 100% finished", "Winds drop temporarily, but ferocious opposite-direction winds will strike within minutes", "Sunshine forever", "It turns into snow"], 1,
        "The eye is surrounded by the destructive eyewall; remain indoors.",
        ["A Red Alert cyclone warning is issued for {name}'s coastal district at {at}."],
        "How should {name} prepare the home?",
        [("Secure loose outdoor objects, metal sheets, and board or tape windows", "Stops objects turning into lethal flying missiles.", True, "secure loose objects|tape windows|shut shutters", 45),
         ("Keep emergency drinking water, battery torches, and a radio ready", "Essential for expected multi-day power outages.", True, "emergency water|torches|battery radio|power outage", 35),
         ("Stay indoors in the strongest central room away from windows until all-clear is given", "Protects from roof and window failures.", False, "stay indoors|central room|away from windows", 20)],
        ["go to the beach to see waves", "step outside during the calm eye", "leave tin sheets loose"],
        "India Meteorological Department (IMD Cyclone Warning)", "https://mausam.imd.gov.in"
    ))

    # DIS-006: Lightning safety
    cards.append(make_card(
        "DIS-006", "storm", "Lightning", "Lightning storm safety: The 30-30 rule and outdoor crouching",
        ["junior", "middle", "senior"],
        ["A lightning bolt carries over 300 million volts of electricity and is hotter than the surface of the sun.",
         "Tall solitary trees and open metal poles act as natural lightning rods; standing under them is lethal."],
        ["Follow the 30-30 Rule: If time between lightning flash and thunder is under 30 seconds, get indoors immediately", "Stay inside a fully enclosed building or metal-roofed car until 30 minutes after the last thunderclap", "If caught in an open field, crouch low on the balls of your feet with heels touching ('lightning crouch')"],
        ["Never shelter under isolated tall trees or tin-roofed sheds in open fields", "Never lie flat on the wet ground (ground currents conduct through your whole body)"],
        "Standing under a tall solitary tree during a thunderstorm keeps you dry and safe.", "myth", "Lightning hits the highest point; current blasts down the trunk and jumps to nearby people (side flash).",
        "What is the safest body posture if caught in an open meadow with zero indoor shelter during lightning?",
        ["Lie flat on your stomach", "Crouch low on balls of feet, tuck head, with heels touching together", "Climb a tree", "Hold metal umbrella high"], 1,
        "Crouching minimizes height and touching heels lets current loop through feet without crossing the heart.",
        ["A sudden thunderstorm with frequent lightning strikes erupts while {name} is in a sports field at {at}."],
        "What should {name} do?",
        [("Immediately seek shelter inside a sturdy building or closed vehicle", "Safest Faraday cage and structural protection.", True, "seek shelter|indoor building|sturdy building|closed car", 45),
         ("Do not shelter under isolated tall trees or touch metal fences", "Eliminates side-flash and ground current paths.", True, "no tall trees|no metal fences|avoid poles", 35),
         ("If trapped in the open, crouch low on balls of feet without lying flat", "Minimizes ground contact area.", False, "lightning crouch|balls of feet|crouch low", 20)],
        ["stand under tallest tree", "hold metal umbrella high", "lie flat in mud puddle"],
        "NDMA Lightning Safety Guidelines", "https://ndma.gov.in"
    ))

    # DIS-007: Heatwave
    cards.append(make_card(
        "DIS-007", "storm", "Heatwave", "Heatwave survival: Hydration, ORS and timing activities",
        ["junior", "middle", "senior"],
        ["Heatstroke occurs when internal body temperature exceeds 40°C, causing brain and organ shutdown.",
         "Drinking plain water alone is insufficient during heavy sweating; electrolytes (salts) must be replenished."],
        ["Drink plenty of water, ORS (Oral Rehydration Salts), lassi, chaas, and lemon water regularly", "Schedule essential outdoor chores before 10 AM or after 5 PM, avoiding peak afternoon sun", "Wear loose, light-colored cotton clothing and cover your head with a damp cloth or wide-brim hat"],
        ["Never leave children or pets locked inside parked cars (temperatures reach fatal 60°C in 15 mins)", "Never do strenuous outdoor sports during afternoon red heat alert hours"],
        "You only need to drink water when you feel extremely thirsty during a heatwave.", "myth", "Thirst is a delayed symptom; by the time you feel parched, your body is already clinically dehydrated.",
        "What should you drink alongside water during severe 44°C summer heatwaves?",
        ["Hot black coffee", "Electrolyte fluids like ORS, buttermilk (chaas), and lemon water with salt", "Sugary sodas only", "Vinegar"], 1,
        "Electrolytes replace sodium and potassium lost through sweat, preventing heat cramps and stroke.",
        ["The thermometer reads 45°C during an official Heatwave Alert at {at}."],
        "How should {name} structure their day?",
        [("Stay indoors in shaded, ventilated spaces during peak hours (12 PM to 4 PM)", "Avoids direct thermal solar radiation.", True, "stay indoors|avoid peak sun|12 to 4 pm|shade", 40),
         ("Hydrate continuously with water, ORS, and homemade cooling drinks (aam panna, chaas)", "Maintains cellular electrolyte balance.", True, "hydrate|ors|chaas|water|electrolytes", 40),
         ("Wear loose, breathable cotton clothes and cover head if stepping out", "Prevents sunburn and solar heat absorption.", False, "cotton clothes|cover head|light colors", 20)],
        ["play football at 2 pm", "lock pet in closed car", "drink ice soda only"],
        "NDMA National Heatwave Action Plan", "https://ndma.gov.in"
    ))

    # DIS-008: Cold wave
    cards.append(make_card(
        "DIS-008", "storm", "Cold wave", "Cold wave survival: Layering and carbon monoxide danger",
        ["junior", "middle", "senior"],
        ["Burning coal angithis, charcoal braziers, or wood in closed bedrooms releases lethal Carbon Monoxide (CO).",
         "Carbon Monoxide is an invisible, odorless, tasteless gas that silently suffocates sleeping families."],
        ["Wear multiple loose, warm layers (thermal inners, woolens, windbreaker) instead of one heavy coat", "Ensure active cross-ventilation (leave windows slightly cracked) if using heating appliances", "Cover head, neck, hands, and feet (warm cap, muffler, woolen socks) where body heat radiates fastest"],
        ["Never sleep in an airtight closed room with a burning coal angithi or unvented gas heater", "Never ignore symptoms of hypothermia: uncontrollable shivering, slurred speech, and extreme drowsiness"],
        "Sleeping with a burning charcoal angithi in an airtight bedroom keeps the family warm and completely safe.", "myth", "Airtight coal burning produces lethal carbon monoxide, causing hundreds of fatal winter asphyxiations yearly.",
        "Why is it deadly to burn a coal angithi or wood brazier inside a tightly sealed bedroom with all windows closed?",
        ["It gets too bright", "Incomplete combustion generates invisible, odorless Carbon Monoxide gas that kills in sleep", "It makes room cold", "It wastes wood"], 1,
        "Carbon monoxide binds to hemoglobin 200 times stronger than oxygen, causing painless suffocation.",
        ["During freezing winter temperatures at {at}, relatives want to bring a glowing charcoal angithi into a closed bedroom."],
        "What life-saving intervention must {name} make?",
        [("Explain that burning charcoal in an enclosed room generates lethal Carbon Monoxide gas", "Warns against invisible asphyxiation hazard.", True, "carbon monoxide|deadly gas|odorless|suffocation|angithi danger", 45),
         ("Insist on keeping windows cracked for fresh air ventilation if any heater is used", "Maintains essential oxygen exchange.", True, "ventilation|keep window open|fresh air", 35),
         ("Use extra woolen blankets and multiple clothing layers for warmth instead of open coal", "Safe thermal management.", False, "extra blankets|layers|woolens", 20)],
        ["seal all windows with burning coal", "sleep beside unventilated angithi", "ignore headache"],
        "NDMA Cold Wave Guidelines", "https://ndma.gov.in"
    ))

    # DIS-009: Landslides
    cards.append(make_card(
        "DIS-009", "storm", "Landslides", "Hillside landslides: Warning signs and safe evacuation",
        ["middle", "senior"],
        ["Prolonged torrential monsoon rains saturate mountain soil, causing catastrophic mud and boulder slides.",
         "Warning signs include tilted trees, cracks opening on slopes, jammed doors, and sudden muddy stream surges."],
        ["Evacuate immediately to designated ridge shelters if you observe widening soil cracks on hillside slopes", "Stay alert during continuous heavy hill rainfall and listen for rumbling sounds like locomotives", "Avoid building or camping near steep slopes, drainage ravines, and mountain stream channels"],
        ["Never stay in valley bottoms directly in the path of a potential mudflow", "Never drive across road sections with falling rocks or fresh mudslides"],
        "Landslides strike instantly with zero prior warning signs on the hillside.", "myth", "Landslides give multiple advance warnings: tilting telephone poles, new ground cracks, and muddy springs.",
        "Which of the following is an early physical warning sign of an impending hillside landslide?",
        ["Singing birds", "Trees and electric poles tilting sideways and new cracks appearing in masonry walls", "Dry soil", "Clear sky"], 1,
        "Soil creep tilts rooted poles and trees days before complete slope failure.",
        ["On a vacation or trip in a hilly region at {at}, continuous heavy rains cause new cracks to appear in the lodge's slope."],
        "What should {name} and guests do?",
        [("Alert adults and evacuate uphill to stable ridge ground away from the slope", "Moves out of downward mud avalanche trajectory.", True, "evacuate|stable ground|ridge|away from slope", 45),
         ("Listen for ominous deep rumbling sounds or sudden muddying of clear streams", "Signals active debris flow initiation.", True, "rumbling sound|muddy stream|warning signs", 35),
         ("Report slope movement to local administration and disaster helplines", "Alerts emergency response.", False, "report to police|local administration|112", 20)],
        ["hide in basement at bottom of hill", "ignore ground cracks", "camp beside steep ravine"],
        "Geological Survey of India (GSI Landslide Division)", "https://gsi.gov.in"
    ))

    # DIS-010: Tsunami
    cards.append(make_card(
        "DIS-010", "storm", "Tsunami", "Coastal tsunami warning signs: Sea withdrawal and high ground",
        ["junior", "middle", "senior"],
        ["Undersea earthquakes displace massive water columns, generating tsunami wave trains over 800 km/h.",
         "Nature's primary visual tsunami warning is a dramatic, sudden retreat of ocean water exposing the seabed."],
        ["If you feel a strong coastal earthquake or see the sea suddenly pull back, run inland and uphill immediately", "Climb to elevated ground at least 30 meters above sea level, or to the 4th floor of a reinforced concrete building", "Stay on high ground for several hours: tsunamis arrive as a series of multiple waves over hours"],
        ["Never run down to the beach to collect stranded fish or look at the exposed seabed", "Never wait for an official siren if natural warning signs (quake, sea retreat) occur"],
        "A tsunami is just one big wave; once the first wave recedes, it is safe to return to the beach.", "myth", "Tsunamis are a series of wave crests; the second or third wave is frequently much larger than the first.",
        "You are on a beach when the ocean water suddenly pulls back hundreds of meters, exposing stranded shells. What do you do?",
        ["Run out onto the wet sand to collect shells", "Turn around immediately and sprint inland to high ground", "Take photos", "Jump into the ocean"], 1,
        "Sudden sea withdrawal is the definitive sign of a massive incoming tsunami wave crest. Run inland.",
        ["While visiting a coastal beach at {at}, {name} notices the ocean water pulling back rapidly into the horizon."],
        "What urgent action must {name} initiate?",
        [("Shout to companions and run inland toward high ground immediately", "Minutes count before wave arrival.", True, "run inland|high ground|sprint away from beach", 45),
         ("Do not pause to collect belongings, take videos, or gather stranded marine life", "Any delay is fatal.", True, "don'?t collect fish|no photos|drop belongings", 35),
         ("Remain on elevated ground for hours until disaster authorities issue official all-clear", "Tsunamis strike in successive waves.", False, "stay on high ground|multiple waves", 20)],
        ["walk toward exposed seabed", "wait for official announcement on beach", "stay on shore"],
        "Indian National Centre for Ocean Information Services (INCOIS)", "https://incois.gov.in"
    ))

    # DIS-011: Go-Bag
    cards.append(make_card(
        "DIS-011", "storm", "Emergency kit", "Assembling a family Emergency Go-Bag (72-hour survival kit)",
        ["junior", "middle", "senior"],
        ["During major disasters, municipal electricity, tap water, and cellular networks can stay down for 72 hours.",
         "A pre-packed, waterproof Go-Bag ensures your family can evacuate in under 60 seconds."],
        ["Pack essential documents (Aadhaar, property papers, insurance) sealed inside waterproof plastic ziplocks", "Include battery torches, spare batteries, a loud emergency whistle, and a portable battery power bank", "Pack water bottles, water purification tablets, dry non-perishable rations (chana, biscuits), and a first aid kit"],
        ["Never overload the Go-Bag so heavily that a student cannot easily carry it while running", "Never forget critical daily prescription medicines required by family elders"],
        "A disaster Emergency Go-Bag is only needed in movies and war zones.", "myth", "Floods, earthquakes, and cyclones strike Indian cities with zero warning; a Go-Bag saves lives every year.",
        "What is the most critical item to keep inside waterproof bags within your emergency kit?",
        ["Heavy textbooks", "Vital personal identification documents, medical papers, and emergency contact list", "Video game console", "Extra shoes"], 1,
        "Waterproof document storage protects legal identity and allows rapid post-disaster insurance and relief.",
        ["{name}'s family at {at} is preparing their 72-hour disaster Emergency Go-Bag."],
        "What core items should {name} ensure are packed inside?",
        [("Store key family documents and emergency cash in sealed waterproof pouches", "Protects vital identity and emergency finances.", True, "waterproof documents|aadhaar|emergency cash", 40),
         ("Pack a battery-powered torch, emergency whistle, and portable phone power bank", "Provides light, signaling, and communication.", True, "torch|whistle|power bank|batteries", 35),
         ("Include dry ready-to-eat food, water purification tablets, and basic first aid", "Ensures 72 hours of self-sustained survival.", False, "first aid|water purification|dry rations", 25)],
        ["pack heavy television set", "leave documents loose in rain", "pack perishable cooked curry"],
        "NDMA Emergency Kit Checklist", "https://ndma.gov.in"
    ))

    # DIS-012: Family plan
    cards.append(make_card(
        "DIS-012", "storm", "Family plan", "Family disaster communication plan: Emergency contacts and meeting spots",
        ["junior", "middle", "senior"],
        ["Local mobile cell towers crash during disasters due to power cuts and massive calling congestion.",
         "Out-of-state long-distance SMS text messages frequently pass through when local voice calls fail."],
        ["Designate an out-of-city relative (Aunt/Uncle in another state) as the central family check-in contact", "Memorize your parents' mobile phone numbers by heart rather than relying on phone memory", "Agree on two fixed family meeting points: one right outside your home, and one outside the neighborhood"],
        ["Never clog emergency networks with continuous long phone calls; send short SMS check-in texts", "Never leave an agreed evacuation meeting point without leaving a written note"],
        "In a major earthquake, you will easily be able to video call your parents on mobile phones.", "myth", "Local cellular towers fail instantly during major disasters. Plan offline meeting spots and out-of-state SMS.",
        "Why should your family designate an out-of-state relative as your emergency disaster check-in contact?",
        ["They have more free time", "Local city lines get jam-packed, while long-distance text routing through other states stays operational", "To share recipes", "It is mandatory by law"], 1,
        "An out-of-area contact acts as a central communication bridge when local networks fail.",
        ["Planning family disaster readiness at {at}, {name} discusses emergency communication."],
        "What key plan should {name} establish?",
        [("Memorize two primary parent phone numbers and designate an out-of-state family contact", "Ensures communication when local lines fail.", True, "memorize phone numbers|out of town contact|central contact", 45),
         ("Agree on two specific physical meeting spots (one local, one outside neighborhood)", "Enables reunification if separated.", True, "meeting spots|reunification point|neighborhood spot", 35),
         ("Use short SMS text messages instead of continuous voice calls during network congestion", "Conserves scarce network bandwidth.", False, "short sms|text over call|conserve battery", 20)],
        ["rely 100% on battery phone memory", "have no meeting spot", "panic and wander aimlessly"],
        "National Disaster Management Authority (Disaster Preparedness)", "https://ndma.gov.in"
    ))

    # DIS-013: Official alerts
    cards.append(make_card(
        "DIS-013", "storm", "Alerts", "Official disaster alerts vs viral WhatsApp panic rumors",
        ["middle", "senior"],
        ["Viral social media forwards spread fabricated dam-burst warnings, false death tolls, and fake dates.",
         "The National Disaster Management Authority (NDMA) and IMD publish verified color-coded alerts (Yellow, Orange, Red)."],
        ["Rely exclusively on verified government sources: NDMA (sachet.ndma.gov.in), IMD, and District Collector handles", "Check the 'Sachet' National Disaster Alert Portal app on your smartphone for localized warnings", "Verify sensational forward claims against official press releases before forwarding to family groups"],
        ["Never forward unverified voice notes claiming 'a massive dam has collapsed' or 'super-cyclone incoming'", "Never share outdated disaster photos from previous years as current news"],
        "Forwarding every alarming disaster audio clip on WhatsApp helps warn your family just in case.", "myth", "Panic rumors cause stampedes, choke emergency helplines, and prevent real relief from reaching victims.",
        "What is the official disaster early warning portal and mobile app developed by NDMA India?",
        ["TikTok", "SACHET (sachet.ndma.gov.in)", "WhatsApp rumors", "Snapchat"], 1,
        "SACHET is the Government of India's integrated early warning platform providing real-time regional alerts.",
        ["A scary audio clip spreads on family WhatsApp at {at} claiming an earthquake will strike the city at 4 PM."],
        "How should {name} debunk this panic rumor?",
        [("Explain that science CANNOT predict exact earthquake times; the forward is a fabricated hoax", "Dispels scientifically impossible rumors.", True, "earthquakes cannot be predicted|fake forward|hoax|debunk", 45),
         ("Cross-check alerts on the official NDMA SACHET portal or IMD official handles", "Directs to verified scientific sources.", True, "sachet portal|ndma|imd|official source", 35),
         ("Ask family members to delete the forward and not share panic in society groups", "Stops the viral chain of panic.", False, "don'?t forward|delete hoax|calm family", 20)],
        ["forward to 10 school groups", "panic and sleep in garden", "believe unverified audio note"],
        "National Disaster Alert Portal (SACHET - NDMA)", "https://sachet.ndma.gov.in"
    ))

    # DIS-014: Wall collapse
    cards.append(make_card(
        "DIS-014", "storm", "Monsoon structural", "Dilapidated walls and old building collapses in monsoon",
        ["junior", "middle", "senior"],
        ["Heavy monsoon rains saturate lime mortar and soil foundations, causing sudden boundary wall collapses.",
         "Over 60% of monsoon structural fatalities occur when pedestrians walk beside waterlogged old walls."],
        ["Walk in the center of lanes, keeping a wide 3-meter safety margin away from old boundary walls", "Avoid taking shelter from rain under decaying concrete awnings, balconies, or leaning brick fences", "Report dangerously tilted or water-seeping walls to your local municipal ward office"],
        ["Never lean your bicycle or stand directly against waterlogged masonry walls during downpours", "Never ignore fresh cracks or bulging in boundary walls"],
        "Standing right under a cracked building balcony keeps you dry from monsoon rain safely.", "myth", "Waterlogged concrete balconies collapse without warning under the weight of accumulated rainwater.",
        "Why is it dangerous to walk right beside ancient boundary walls during heavy monsoon rain?",
        ["Walls are cold", "Saturated rainwater destabilizes old foundations, causing sudden wall collapses onto pedestrians", "Moss stains clothes", "No danger"], 1,
        "Water absorption weakens mortar bonds, causing heavy masonry walls to topple outward.",
        ["Walking home in torrential rain at {at}, {name} sees classmates sheltering under an ancient crumbling boundary wall."],
        "What should {name} urgently advise?",
        [("Move away from the wall and maintain a wide standoff safety distance", "Prevents being crushed by sudden structural failure.", True, "move away from wall|keep distance|standoff distance", 45),
         ("Explain that waterlogged brick foundations can collapse outward with zero warning", "Communicates mechanical monsoon risk.", True, "waterlogged wall|collapse hazard|decaying brick", 35),
         ("Seek shelter inside a sturdy, modern shop or permanent concrete structure", "Identifies safe shelter.", False, "sturdy shelter|permanent building", 20)],
        ["lean against crumbling wall", "climb cracked fence", "sit under cracked balcony"],
        "Building Materials and Technology Promotion Council (BMTPC)", "https://bmtpc.org"
    ))

    # DIS-015: Electric wires in water
    cards.append(make_card(
        "DIS-015", "storm", "Electrocution", "Submerged electric wires and step potential in floodwaters",
        ["junior", "middle", "senior"],
        ["Fallen live overhead power lines electrify surrounding pooled water for dozens of meters.",
         "'Step potential' occurs when voltage differences between your two feet create a lethal shock loop."],
        ["Treat all standing rainwater around electric poles, transformers, or fallen wires as live and lethal", "If you feel a tingling sensation in your feet while walking, stop immediately, keep feet together, and bunny-hop away", "Alert local electricity distribution officials and police immediately to shut off power to the sector"],
        ["Never walk or cycle through pooled water near leaning electric poles or dangling cables", "Never touch metal gates, lampposts, or signboards submerged in water"],
        "Waterlogged puddles around electric transformers are harmless unless you touch the metal pole directly.", "myth", "Current leaks directly into pooled water, creating lethal electrical gradients across the surface.",
        "What should you do if your legs feel a sudden electric tingling sensation in shallow floodwater?",
        ["Take giant long strides", "Keep feet tightly together and bunny-hop or shuffle away without lifting feet apart", "Lie down in water", "Run fast"], 1,
        "Keeping feet together eliminates the voltage difference ('step potential') across your body.",
        ["After a severe storm at {at}, a heavy tree branch has snapped a high-voltage wire into a large water puddle."],
        "How should {name} react?",
        [("Stay at least 15 meters away and do not step into the waterlogged area", "Maintains safe electrical clearance distance.", True, "stay away|15 meters|don'?t step in water|live wire", 45),
         ("Warn other pedestrians and cyclists loudly to stay back", "Prevents bystander electrocution.", True, "warn pedestrians|shout warning|keep back", 35),
         ("Call the electricity emergency complaint number and police 112 immediately", "Ensures grid technicians de-energize the feeder.", False, "call electricity board|call 112|report wire", 20)],
        ["touch the wire with a stick", "walk through the puddle", "pick up live cable"],
        "Central Electricity Authority (Measures Relating to Safety)", "https://cea.nic.in"
    ))

    # DIS-016: Safe water post-disaster
    cards.append(make_card(
        "DIS-016", "storm", "Water safety", "Safe drinking water after floods: Boiling and chlorine tablets",
        ["junior", "middle", "senior"],
        ["Floodwaters submerge municipal pipelines, mixing sewage, animal carcasses, and cholera bacteria into drinking wells.",
         "Consuming unpurified floodwater triggers deadly epidemics of cholera, typhoid, and hepatitis A."],
        ["Boil all drinking water vigorously at a rolling boil for at least 1 to 3 continuous minutes", "Use Halazone / chlorine water purification tablets according to packaging instructions if boiling is impossible", "Store purified drinking water in narrow-mouthed, clean containers with secure lids"],
        ["Never drink clear-looking tap water after a flood without boiling (pathogens are invisible)", "Never wash dishes, fruit, or brush teeth with contaminated floodwater"],
        "If floodwater from a well looks crystal clear, it is completely pure and safe to drink without boiling.", "myth", "Deadly pathogens like cholera and typhoid bacteria are microscopic and thrive in clear-looking water.",
        "How long must drinking water be kept at a vigorous rolling boil to sterilize post-flood water?",
        ["5 seconds", "At least 1 to 3 minutes of continuous rolling boiling", "1 hour", "Just warm it"], 1,
        "1-3 minutes of vigorous rolling boiling kills all vegetative bacteria, viruses, and amoebic cysts.",
        ["Following heavy river floods at {at}, the municipal tap water runs with a strange smell."],
        "What water purification protocol must {name} implement at home?",
        [("Bring all drinking water to a continuous rolling boil for at least 1-3 minutes", "Thermal sterilization destroys waterborne pathogens.", True, "boil water|rolling boil|1 to 3 minutes", 45),
         ("Use chlorine disinfection tablets if gas or electricity for boiling is unavailable", "Chemical disinfection alternative.", True, "chlorine tablets|halazone|water purification", 35),
         ("Keep purified water covered in clean containers; do not drink raw tap water", "Prevents secondary contamination.", False, "covered container|no raw tap water", 20)],
        ["drink directly from flood tap", "filter through cloth only", "drink flood puddle water"],
        "WHO Guidelines for Drinking-water Quality in Emergencies", "https://who.int"
    ))

    # DIS-017: Assisting vulnerable
    cards.append(make_card(
        "DIS-017", "storm", "Inclusive evacuation", "Community solidarity: Assisting elderly and disabled neighbors",
        ["junior", "middle", "senior"],
        ["Elderly citizens, persons with mobility challenges, and toddlers face severe evacuation barriers.",
         "A resilient community checks on vulnerable households within the first 15 minutes of a disaster alert."],
        ["Check on elderly or disabled neighbors during evacuation alerts to ensure they have heard the warning", "Help carry essential medications, walking canes, and emergency bags for senior citizens", "Assist them along safe evacuation routes calmly without rushing or creating panic"],
        ["Never leave elderly neighbors behind in ground-floor flood zones without verification", "Never shout or cause hysteria that triggers cardiac distress in vulnerable seniors"],
        "During disaster evacuation, you should only care about yourself and ignore elderly neighbors.", "myth", "Community mutual aid is what saves lives during disasters before government rescue boats arrive.",
        "What is the most compassionate civic action during a neighborhood evacuation warning?",
        ["Run away silently", "Knock on elderly or disabled neighbors' doors to ensure they know and offer evacuation help", "Lock your gate", "Watch from window"], 1,
        "Checking on vulnerable neighbors ensures nobody is left trapped in flood or fire zones.",
        ["A cyclone or flood evacuation alert sounds in the neighborhood at {at}."],
        "How should {name} demonstrate community leadership?",
        [("Check on elderly or disabled neighbors living nearby to confirm they are evacuating safely", "Ensures vulnerable individuals are accounted for.", True, "check on elderly|assist neighbors|disabled neighbors|evacuation help", 45),
         ("Help them pack vital prescription medicines, walking aids, and identity cards", "Secures critical life-support supplies.", True, "pack medicines|assist canes|help carry", 35),
         ("Guide them calmly to the community relief center or high-ground assembly point", "Safe transit support.", False, "guide to shelter|community center|calm", 20)],
        ["ignore calling neighbors", "spread panic screams", "block neighbors' exit"],
        "NDMA Community Based Disaster Risk Management (CBDRM)", "https://ndma.gov.in"
    ))

    # DIS-018: School drill
    cards.append(make_card(
        "DIS-018", "storm", "Drills", "School disaster evacuation drills: Discipline beats panic",
        ["junior", "middle", "senior"],
        ["Historical disaster analyses show that stairwell stampedes cause 4 times more injuries than building damage.",
         "Regular disaster drills build muscle memory, allowing students to evacuate calmly on instinct."],
        ["Take school disaster drills seriously as realistic life-saving training, not playtime", "Follow teacher directions instantly, walk briskly in single file, and maintain total silence", "Keep hands free: do not hold hands across the staircase or stop to pick up dropped pens"],
        ["Never run, push, scream, or shove on school staircases during an evacuation drill", "Never joke or make false alarm screams that trigger panic stampedes"],
        "School disaster drills are boring wastes of class time that will never be used in real life.", "myth", "Schools that practice regular drills achieve 100% casualty-free evacuations during real earthquakes and fires.",
        "What is the single most critical behavioral rule when evacuating school staircases during a drill?",
        ["Run as fast as you can", "Walk calmly in single file, no pushing, no running, and maintain silence", "Shout loudly", "Slide down banister"], 1,
        "Orderly walking in single file prevents deadly crowd crushes and tripping on stairwells.",
        ["A disaster evacuation siren rings across the school campus at {at}."],
        "How should {name} and classmates conduct themselves?",
        [("Walk briskly in orderly single file without running or pushing", "Eliminates stairwell crush risks.", True, "single file|walk calmly|no running|no pushing", 45),
         ("Maintain silence so teachers' emergency instructions can be heard by all", "Ensures auditory command flow.", True, "maintain silence|listen to teacher|quiet", 35),
         ("Assemble at the designated outdoor school sports ground for roll-call headcount", "Verifies all students are safely accounted for.", False, "assembly ground|sports field|roll call|headcount", 20)],
        ["run screaming on stairs", "push younger kids down", "stop to tie shoelaces on stairs"],
        "National School Safety Policy Guidelines (NDMA)", "https://ndma.gov.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Storm")
    return cards
