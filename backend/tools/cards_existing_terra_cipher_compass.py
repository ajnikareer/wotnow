"""
Terra (Environment), Cipher (Digital Safety), and Compass (Careers) expanded skills.
Provides 16-17 verified, realistic skills for each agent.
"""
from cards_existing import make_card

def get_terra_cards():
    cards = []

    # 1. ENV-021: Single-use plastic
    cards.append(make_card(
        "ENV-021", "terra", "Plastic", "Phasing out single-use plastic: Bags, bottles and cutlery",
        ["junior", "middle", "senior"],
        ["Single-use plastic takes over 450 years to fragment into toxic microscopic plastic particles.",
         "India produces over 3.4 million tonnes of plastic waste annually, choking drainage and marine life."],
        ["Keep a foldable cloth bag inside your school backpack for unexpected purchases", "Carry a reusable steel or copper water bottle instead of buying single-use plastic bottles", "Refuse plastic straws, spoons, and disposable plastic carry bags politely: 'I brought my own'"],
        ["Never burn plastic waste in the open (releases carcinogenic dioxins and furans)", "Never throw plastic packets into gutters or open plots"],
        "Thin plastic carry bags dissolve quickly in sunlight and soil.", "myth", "Plastics never biodegrade; they merely fragment into toxic microplastics that enter our drinking water and food.",
        "What is the simplest daily habit to stop plastic waste at the market?",
        ["Ask for three plastic bags", "Carry your own washable cloth tote bag and steel bottle", "Throw plastic in bushes", "Burn plastic"], 1,
        "Carrying a reusable bag eliminates hundreds of single-use plastic bags per person every year.",
        ["At the neighborhood grocery shop at {at}, the vendor offers {name} three thin black plastic carry bags."],
        "What eco-friendly action should {name} take?",
        [("Politely refuse the plastic bags: 'No thank you, I have a cloth bag'", "Cuts single-use plastic at source.", True, "refuse plastic|use cloth bag|brought my own", 45),
         ("Use a reusable cloth tote or backpack to pack items", "Durable, washable, zero-waste carrier.", True, "cloth tote|backpack|reusable bag", 35),
         ("Explain gently to peers why single-use plastics choke city drains", "Spreads environmental awareness.", False, "educate peers|choke drains|microplastics", 20)],
        ["take 5 plastic bags", "dump plastic on road", "burn plastic in garden"],
        "Plastic Waste Management Rules (MoEFCC)", "https://moef.gov.in"
    ))

    # 2. ENV-022: E-waste
    cards.append(make_card(
        "ENV-022", "terra", "E-waste", "Safe disposal of electronic waste (e-waste) and old batteries",
        ["middle", "senior"],
        ["Discarded electronics contain toxic heavy metals: lead, mercury, cadmium, and arsenic.",
         "Tossing batteries into common garbage contaminates local municipal soil and groundwater aquifers."],
        ["Deposit old mobile phones, chargers, and wires at authorized e-waste collection bins", "Look for certified take-back programs at electronics retail stores and schools", "Store swollen or leaking batteries in a fire-safe container before dropping at recycling centers"],
        ["Never throw discarded gadgets, wires, or batteries into normal household dustbins", "Never dismantle or break open old cathode ray tubes or lithium-ion batteries"],
        "Old mobile phones thrown into landfills safely rust away like iron nails.", "myth", "Batteries and circuit boards leach lethal heavy metals like cadmium and lead into drinking wells.",
        "Where should you deposit broken earphones, old tablets, and dead batteries?",
        ["In the wet compost bin", "At an authorized e-waste collection center or brand take-back bin", "In the street gutter", "Burn them in backyard"], 1,
        "Certified e-waste recyclers dismantle electronics in vacuum-sealed facilities to recover gold and copper safely.",
        ["Cleaning out a study desk drawer at {at}, {name} finds three dead mobile batteries and tangled broken chargers."],
        "What is the ecologically responsible way to discard them?",
        [("Collect them in a box and take them to an authorized e-waste drop-off bin", "Prevents hazardous heavy metal soil contamination.", True, "e-waste bin|authorized recycler|collection center", 45),
         ("Do not throw electronics into daily municipal garbage dustbins", "Protects waste pickers from toxic exposure.", True, "don'?t throw in trash|no daily dustbin", 35),
         ("Check if local electronics stores or schools have e-waste drives", "Convenient authorized disposal.", False, "take back drive|school e-waste", 20)],
        ["throw in wet waste", "burn with dry leaves", "bury in garden soil"],
        "E-Waste (Management) Rules (CPCB)", "https://cpcb.nic.in"
    ))

    # 3. ENV-023: Composting
    cards.append(make_card(
        "ENV-023", "terra", "Composting", "Kitchen wet waste composting: Turning peels into black gold",
        ["junior", "middle", "senior"],
        ["Over 50% of urban household waste is organic wet waste (fruit peels, vegetable stalks, tea leaves).",
         "When organic matter rots under plastic in landfills without oxygen, it generates methane, a potent greenhouse gas."],
        ["Segregate wet green waste (fruit peels, vegetable scraps, coffee grounds, eggshells)", "Mix greens with dry brown waste (dry leaves, shredded cardboard, sawdust) in a ventilated pot", "Turn the compost pile once a week to let aerobic bacteria create rich, odor-free garden soil"],
        ["Never add plastic wrappers, foil, dairy, cooked oils, or meat bones to basic home compost", "Never let the compost pile become waterlogged and smelly"],
        "Composting at home always produces terrible foul smells and attracts thousands of flies.", "myth", "A balanced compost pile with proper brown leaves and aeration smells like fresh forest soil.",
        "What two types of waste must be balanced in a home compost bin to keep it healthy?",
        ["Plastic and glass", "Nitrogen-rich 'Greens' (kitchen peels) and Carbon-rich 'Browns' (dry leaves, cardboard)", "Batteries and paper", "Metal and sand"], 1,
        "A 1:2 ratio of wet green peels to dry brown leaves creates ideal aerobic decomposition.",
        ["At home at {at}, {name} notices daily vegetable cuttings and banana peels being thrown into the trash bin."],
        "How can {name} start simple kitchen waste composting?",
        [("Collect fruit and vegetable peels in a separate 'Wet Waste' bin", "Separates organic compostables at source.", True, "separate wet waste|peels|organic", 40),
         ("Layer the wet peels with dry garden leaves or crushed paper in a terracotta pot", "Maintains optimal carbon-nitrogen balance.", True, "layer dry leaves|browns|aeration|terracotta", 40),
         ("Harvest rich dark organic compost in 60-90 days for house plants", "Produces free nutrient-rich natural fertilizer.", False, "harvest compost|soil|plants", 20)],
        ["throw plastic wrappers in compost", "dump peels in street gutter", "burn peels"],
        "Swachh Bharat Mission Solid Waste Management Rules", "https://swachhbharaturban.gov.in"
    ))

    # 4. ENV-024: Native trees
    cards.append(make_card(
        "ENV-024", "terra", "Trees", "Planting and caring for native shade trees (Neem, Peepal, Jamun)",
        ["junior", "middle", "senior"],
        ["Native Indian trees (Neem, Peepal, Banyan, Jamun) support hundreds of local birds and pollinators.",
         "Exotic trees (like Eucalyptus and Conocarpus) deplete groundwater and provide zero food for native biodiversity."],
        ["Plant indigenous native species adapted to local rainfall: Neem, Amla, Jamun, Peepal, Amaltas", "Water newly planted saplings deeply twice a week during their first two summers", "Protect young saplings with bamboo tree guards against grazing goats and cattle"],
        ["Never plant invasive water-guzzling exotic species near groundwater wells", "Never plant trees and abandon them without water in peak summer"],
        "Planting any tree anywhere helps the environment equally, even exotic ornamental species.", "myth", "Exotic monocultures destroy local bird nesting ecosystems. Always plant native indigenous species.",
        "Why are native Indian trees like Neem and Jamun far superior to exotic ornamental trees?",
        ["They have funny names", "They conserve groundwater, provide fruits for local birds, and thrive in Indian heat", "They grow in 2 hours", "They need no sun"], 1,
        "Native trees have evolved with Indian soil, supporting bees, birds, and natural groundwater retention.",
        ["During a school plantation drive at {at}, {name} is selecting saplings for the campus grounds."],
        "What wise ecological choices should {name} make?",
        [("Choose native Indian tree saplings like Neem, Jamun, Peepal, or Amaltas", "Thrives naturally and feeds local urban wildlife.", True, "native trees|neem|jamun|peepal|amaltas", 45),
         ("Commit to regular watering and weeding for the sapling's first two years", "Ensures high sapling survival rates.", True, "water sapling|regular care|tree guard", 35),
         ("Mulch around the base with dry leaves to retain soil moisture", "Prevents evaporation under hot sun.", False, "mulch|retain moisture", 20)],
        ["plant invasive eucalyptus", "abandon sapling without water", "snap branches"],
        "National Afforestation and Eco-Development Board", "https://moef.gov.in"
    ))

    # 5. ENV-025: Stubble burning
    cards.append(make_card(
        "ENV-025", "terra", "Air quality", "Stubble and dry leaf burning: Toxic air and soil degradation",
        ["middle", "senior"],
        ["Burning crop residue or dry leaves releases dense clouds of carbon monoxide, PM2.5, and black carbon.",
         "Ground fires incinerate beneficial earthworms, mycorrhizal fungi, and organic soil carbon."],
        ["Compost dry leaves and autumn garden clippings instead of lighting them on fire", "Advocate for happy-seeders, bio-decomposers, and mulching instead of open crop stubble burning", "Report open garbage or leaf burning fires to municipal pollution ward helplines"],
        ["Never light fires to clear backyard dry leaves or park trimmings", "Never burn municipal trash or plastic in roadside piles"],
        "Burning dry leaves in winter is a harmless way to clear colony gardens and get warm.", "myth", "Leaf burning releases hazardous carcinogenic smoke directly into children's and elders' breathing zones.",
        "What happens to the soil when garden leaves or crop stubble are burned on the ground?",
        ["Soil becomes richer", "Intense heat kills beneficial earthworms, microbes, and destroys soil moisture", "It turns to gold", "Nothing"], 1,
        "Fire sterilizes topsoil, destroying organic nitrogen and beneficial microbial life.",
        ["In the neighborhood park at {at}, a gardener is sweeping dry leaves into a pile and preparing to light a match."],
        "How should {name} intervene respectfully?",
        [("Politely request the gardener not to burn the leaves: 'Burning releases toxic smoke into our lungs'", "Directly addresses airborne health hazard.", True, "don'?t burn|smoke hurts lungs|polite request", 45),
         ("Suggest composting the leaves in a park pit to create free natural plant manure", "Provides a constructive ecological alternative.", True, "compost leaves|leaf mulch|make manure", 35),
         ("Remind that open burning in cities is prohibited by the National Green Tribunal (NGT)", "Points to legal pollution regulations.", False, "ngt ban|illegal burning|clean air", 20)],
        ["help light the fire", "throw plastic into the fire", "ignore toxic smoke"],
        "Commission for Air Quality Management (CAQM)", "https://caqm.nic.in"
    ))

    # 6. ENV-026: Urban flood drains
    cards.append(make_card(
        "ENV-026", "terra", "Water drains", "Preventing urban waterlogging: Stormwater drains vs garbage",
        ["junior", "middle", "senior"],
        ["Stormwater drains are designed solely to channel monsoon rainwater away into natural water bodies.",
         "Plastic bags, gutkha packets, and construction debris clog drain grates, creating flash urban floods."],
        ["Keep street stormwater drain grates clean and free of discarded snack packets", "Dispose of household garbage exclusively via door-to-door municipal collection vans", "Report choked colony drains to the municipal corporation before monsoon season begins"],
        ["Never sweep street dust, leaves, or plastic wrappers into storm drain openings", "Never dump construction debris (malba) into roadside storm gutters"],
        "Stormwater drains are underground trash shoots that automatically wash garbage away.", "myth", "Solid waste accumulates at culvert bends, completely choking stormwater flow and flooding roads.",
        "Why do Indian cities experience sudden knee-deep road flooding after only 30 minutes of rain?",
        ["Rain is too heavy", "Stormwater drains are choked with single-use plastics, silt, and dumped garbage", "Roads are made of sponge", "Tides are high"], 1,
        "Blocked drain gratings prevent heavy runoff from entering drainage networks.",
        ["Walking past a colony storm drain grating at {at}, {name} sees it choked with discarded plastic wrappers."],
        "What proactive civic actions prevent monsoon waterlogging?",
        [("Clear surface plastic wrappers away from the drain grate with a stick or gloves", "Restores immediate rainwater drainage entry.", True, "clear grate|remove plastic|unblock drain", 45),
         ("Throw discarded wrappers into the nearest dry waste bin", "Permanent waste containment.", False, "dustbin|dry waste", 20),
         ("Educate neighbours never to use storm drains as trash cans", "Prevents systemic colony flooding.", True, "don'?t dump in drains|rainwater only", 35)],
        ["sweep more trash into drain", "dump concrete in drain", "ignore blocked grate"],
        "National Disaster Management Authority (Urban Flooding)", "https://ndma.gov.in"
    ))

    # 7. ENV-027: Rainwater harvesting
    cards.append(make_card(
        "ENV-027", "terra", "Water table", "Rooftop rainwater harvesting: Recharging groundwater",
        ["junior", "middle", "senior"],
        ["Concrete roads and paved yards prevent rainwater from percolating into underground aquifers.",
         "A 100 sq meter rooftop in a city with 800mm annual rain can harvest over 60,000 litres of clean water."],
        ["Filter rooftop rainwater through sand and gravel layers to recharge colony borewells", "Store harvested rainwater in clean underground tanks for gardening and toilet flushing", "Keep rooftop catchments clean and inspect first-flush pipe diverters before monsoon"],
        ["Never let pristine rooftop monsoon rain run off into dirty sewage gutters", "Never connect sewage lines into groundwater recharge pits"],
        "Rainwater harvesting is only useful for huge rural farms, not city apartment buildings.", "myth", "Urban rooftop rainwater harvesting directly recharges dry borewells and prevents city floods.",
        "What happens when rainwater from building rooftops is routed into groundwater recharge pits?",
        ["It gets lost", "It recharges depleted subterranean water tables and revives drying wells", "It turns salty", "It causes earthquakes"], 1,
        "Percolation pits channel clean rainwater deep into permeable soil layers, raising the water table.",
        ["{name}'s school or residential building at {at} experiences dry borewells every summer."],
        "How can rooftop rainwater harvesting solve this water crisis?",
        [("Channel clean rooftop rainwater into a filtration chamber and percolation recharge pit", "Directly restores underground aquifer reserves.", True, "rooftop rainwater|recharge pit|groundwater|filter", 45),
         ("Use first-flush diverters to wash away initial roof dust and debris", "Ensures only clean rainwater enters recharge wells.", True, "first flush|filter sand|clean water", 35),
         ("Save thousands of litres of water for secondary non-potable uses", "Reduces tanker dependence.", False, "save water|reduce tanker reliance", 20)],
        ["let all rain wash into sewage", "pave entire garden with concrete", "pump dirty sewage in well"],
        "Central Ground Water Board (CGWB)", "https://cgwb.gov.in"
    ))

    # 8. ENV-028: Saving paper
    cards.append(make_card(
        "ENV-028", "terra", "Forests", "Saving paper: Using both sides, digital notes and recycling",
        ["junior", "middle", "senior"],
        ["Producing 1 tonne of virgin paper consumes approximately 17 mature trees and 26,000 litres of water.",
         "Using both sides of every notebook page cuts individual classroom paper footprint by 50%."],
        ["Use every single page of your school notebooks from top margin to bottom margin", "Bind leftover blank pages from old school notebooks into rough work practice pads", "Donate used textbooks to junior students or school book banks for multi-year reuse"],
        ["Never tear out blank notebook pages to make paper planes or doodles", "Never throw whole paper notebooks into the wet garbage bin"],
        "Tearing out pages from school notebooks doesn't hurt trees because paper comes from shops.", "myth", "Every sheet of virgin paper represents felled pulp trees, heavy water consumption, and bleaching chemicals.",
        "What is the best way to reuse notebooks with 20-30 blank leftover pages at the end of the school year?",
        ["Throw them in trash", "Carefully bind the blank sheets together to create a rough practice notebook", "Burn them", "Scribble on all of them"], 1,
        "Binding unused blank pages creates free rough pads and saves trees from being cut.",
        ["At the end of the school term at {at}, {name} has three half-filled notebooks with 40 clean blank pages each."],
        "What is the eco-friendly way to use these pages?",
        [("Tear out or bind the unused pages together to make a rough work pad for homework", "Maximizes paper utility to the last sheet.", True, "reuse blank pages|make rough pad|bind pages", 45),
         ("Pass on clean textbooks to junior classmates through a book bank", "Extends textbook lifespan across multiple students.", True, "donate textbooks|junior students|book bank", 35),
         ("Send completely filled pages to certified paper recycling vendors", "Recycled pulp saves trees and water.", False, "recycle paper|kabadiwala", 20)],
        ["dump notebooks in garbage bin", "burn paper in yard", "waste clean sheets"],
        "National Green Corps (MoEFCC)", "https://moef.gov.in"
    ))

    # 9. ENV-029: Repair culture
    cards.append(make_card(
        "ENV-029", "terra", "Circular economy", "Repair and reuse culture: Fixing before throwing away",
        ["junior", "middle", "senior"],
        ["Modern 'throwaway culture' drives excessive resource mining, industrial manufacturing, and waste heaps.",
         "Repairing shoes, stitching bags, and replacing appliance parts supports local repair artisans and saves money."],
        ["Take torn school backpacks or broken umbrella ribs to local cobblers and tailors for repair", "Upgrade or repair computer RAM/storage before buying a completely new device", "Organize a toy, game, or book swap meet with friends instead of buying new items"],
        ["Never throw away repairable gadgets or bags just to buy the latest trendy model", "Never treat items as disposable after minor tears or scuffs"],
        "Buying a brand-new backpack every school year is necessary even if your old bag only has a stuck zipper.", "myth", "A local tailor can replace a zipper slider for ₹20 in 5 minutes, saving thousands of rupees and manufacturing waste.",
        "What is the most sustainable option when a zipper gets stuck on your favourite school bag?",
        ["Throw bag in trash", "Take it to a local tailor or cobbler to replace the zipper runner", "Buy 3 new bags", "Tear the bag"], 1,
        "Repairing items honors craftspeople, saves family money, and prevents landfill waste.",
        ["The zipper on {name}'s sturdy school backpack splits open at {at}."],
        "How does {name} practice circular economy thinking?",
        [("Visit a local neighborhood tailor or bag repair artisan to fix the zipper slider", "Extends product lifespan by years for minimal cost.", True, "repair zipper|tailor|cobbler|fix bag", 45),
         ("Understand that repairing items conserves raw materials and fossil energy", "Cultivates sustainability mindset.", True, "save resources|repair culture|not throwaway", 35),
         ("Wash and maintain the backpack to keep it fresh for another school term", "Responsible care of personal belongings.", False, "wash and maintain|reuse bag", 20)],
        ["throw bag in trash immediately", "demand an expensive new bag", "cut the bag"],
        "Mission LiFE (Lifestyle for Environment)", "https://missionlife-moefcc.nic.in"
    ))

    # 10. ENV-030: Engine idling
    cards.append(make_card(
        "ENV-030", "terra", "Air quality", "Switching off vehicle engines at red traffic lights",
        ["junior", "middle", "senior"],
        ["Idling a car engine for over 10 seconds consumes more fuel than restarting the engine.",
         "Vehicle exhaust at idling intersections creates concentrated toxic plumes of benzene and PM2.5 at children's eye level."],
        ["Ask family drivers to switch off the engine at traffic signals with countdown timers over 15 seconds", "Turn off vehicles while waiting outside school pick-up gates or railway crossings", "Walking or cycling for short neighborhood errands under 1 km saves fuel and emissions"],
        ["Never leave car air-conditioners running while idling parked for 20 minutes outside shops", "Never rev engines aggressively while waiting at red lights"],
        "Stopping and restarting your car engine at red lights damages the starter motor and wastes more petrol.", "myth", "Modern vehicle starters are designed for thousands of cycles; idling for 10 seconds wastes far more fuel.",
        "At what traffic signal countdown time is it scientifically proven to save fuel by switching off the engine?",
        ["Only if red light is 1 hour", "If the red light timer is longer than 15-20 seconds", "Never switch off", "Only at night"], 1,
        "Switching off at signals over 15 seconds cuts tailpipe emissions and saves litres of fuel monthly.",
        ["Waiting in a car or auto at a 90-second red light signal at {at}, the engine is idling noisily."],
        "What polite green tip can {name} share with the driver?",
        [("Politely suggest: 'Uncle/Papa, the light is 90 seconds, switching off the engine saves fuel and air'", "Saves fuel and cuts street-level emissions.", True, "switch off engine|red light|save fuel|clean air", 45),
         ("Explain that restarting modern vehicles uses less fuel than 10 seconds of idling", "Debunks outdated mechanical myths.", True, "less fuel than idling|restart safe", 35),
         ("Notice how turning off the engine reduces noise and vibration inside the vehicle", "Improves cabin comfort.", False, "reduce noise|less pollution", 20)],
        ["encourage revving engine", "leave engine running for 30 minutes", "honk continuously"],
        "Petroleum Conservation Research Association (PCRA)", "https://pcra.org"
    ))

    # 11. ENV-031: Birds in summer
    cards.append(make_card(
        "ENV-031", "terra", "Urban wildlife", "Summer water bowls for urban birds and street animals",
        ["junior", "middle", "senior"],
        ["Urbanization, asphalt, and concrete drain covers eliminate natural puddles and drinking ponds for city birds.",
         "During scorching Indian summers (40°C+), hundreds of sparrows, pigeons, and squirrels die of dehydration."],
        ["Place wide, shallow terracotta clay bowls filled with fresh water on balconies, terraces, and gardens", "Keep water bowls in the shade to prevent water from becoming burning hot under midday sun", "Wash and refill the bowl daily with clean water to prevent mosquito larvae from breeding"],
        ["Never leave dirty, stagnant green slime water in bowls (breeds dengue mosquitoes)", "Never use deep slick plastic buckets where small birds can fall in and drown"],
        "Leaving a water bowl outside once a month is enough for birds in May.", "myth", "Shallow water evaporates in hours during peak summer. Daily cleaning and refilling are vital.",
        "What material is best for an outdoor bird water bowl?",
        ["Deep metal bucket", "A wide, shallow unglazed terracotta clay dish (keeps water naturally cool)", "Glass bottle", "Black plastic bag"], 1,
        "Porous terracotta allows gentle evaporation, keeping water refreshingly cool for birds.",
        ["During intense May summer heat at {at}, {name} sees panting sparrows and squirrels on the balcony railing."],
        "How can {name} provide immediate life-saving relief?",
        [("Set out a wide, shallow clay saucer filled with fresh water in a shady spot", "Quenches dehydration safely without drowning hazard.", True, "water bowl|terracotta dish|shade|shallow water", 45),
         ("Wash and replace the water daily to keep it hygienic and mosquito-free", "Prevents dengue and bacterial buildup.", True, "clean daily|refill fresh water|no mosquitoes", 35),
         ("Scatter a few grains of millets, rice, or seeds nearby", "Provides safe summer nourishment.", False, "grains|seeds|bird food", 20)],
        ["put boiling hot water", "use deep bucket where birds drown", "ignore thirsty birds"],
        "Bombay Natural History Society (BNHS)", "https://bnhs.org"
    ))

    # 12. ENV-032: Noise & wildlife
    cards.append(make_card(
        "ENV-032", "terra", "Wildlife", "Noise pollution impact on urban birds, pets and nocturnal wildlife",
        ["junior", "middle", "senior"],
        ["Birds use acoustic song frequencies for territory defense, mating calls, and predator danger alarms.",
         "Urban traffic rumble and festive firecrackers force songbirds to shout, disorienting their navigation."],
        ["Keep festival celebrations green with lights and flowers instead of deafening explosive crackers", "Keep household pets indoors in a quiet, sheltered room with closed curtains during loud celebrations", "Support city silence zones around bird sanctuaries, zoological parks, and forested urban ridges"],
        ["Never burst loud firecrackers near trees, nesting colonies, or animal shelters", "Never play blaring DJ music in eco-sensitive zones or national parks"],
        "Street birds and stray animals do not mind loud chemical firecrackers at all.", "myth", "Dogs hear acoustic frequencies 4 times higher than humans; explosions cause severe panic, tremors, and cardiac arrest.",
        "Why do birds abandon city gardens exposed to continuous loud construction and traffic noise?",
        ["They get bored", "Noise masks their mating calls, alarm songs, and acoustic predator alerts", "They dislike music", "They sleep all day"], 1,
        "Acoustic masking prevents avian communication, forcing bird populations to flee noisy cities.",
        ["During festival night at {at}, neighbours are preparing to burst high-decibel aerial firecrackers near park trees."],
        "What compassionate wildlife awareness can {name} champion?",
        [("Celebrate with beautiful earthen diyas, lanterns, and sweets instead of loud crackers", "Eco-friendly, pollution-free celebration.", True, "diyas|lanterns|no loud crackers|green celebration", 45),
         ("Explain that loud acoustic blasts cause terror and disorientation in nesting birds and pets", "Builds empathy for non-human urban residents.", True, "protect pets|scared birds|noise distress", 35),
         ("Provide a quiet, safe corner inside for frightened domestic pets during celebrations", "Ensures domestic animal safety.", False, "shelter pets|quiet room", 20)],
        ["tie crackers to animal tails", "burst loudest bombs near trees", "laugh at frightened pets"],
        "World Wide Fund for Nature (WWF India)", "https://wwfindia.org"
    ))

    # 13. ENV-033: Air Quality Index
    cards.append(make_card(
        "ENV-033", "terra", "AQI", "Understanding the Air Quality Index (AQI) and protecting lungs",
        ["junior", "middle", "senior"],
        ["The AQI measures 8 major pollutants, with fine PM2.5 (particles 30 times thinner than hair) being the most lethal.",
         "When AQI exceeds 300 ('Severe'), breathing outdoor air for a day equals smoking 15-20 cigarettes."],
        ["Check your city's daily AQI on government apps (Sameer app by CPCB) before outdoor morning sports", "Wear an authentic, well-fitted N95 or FFP2 particulate mask when AQI enters 'Very Poor' (300+) levels", "Shift strenuous aerobic sports indoors during severe smog inversion episodes"],
        ["Never rely on thin cloth handkerchiefs or surgical masks (they filter 0% of micro PM2.5 particles)", "Never do heavy outdoor sprint workouts in dense winter smog"],
        "Wrapping a cotton handkerchief around your mouth blocks all dangerous air pollution.", "myth", "Cotton cloth weaves have pore gaps thousands of times larger than PM2.5 particles. Only certified N95 masks filter them.",
        "What official government mobile app provides real-time AQI readings for Indian cities?",
        ["Instagram", "SAMEER App by the Central Pollution Control Board (CPCB)", "Candy Crush", "Amazon"], 1,
        "The SAMEER app provides hour-by-hour air quality monitoring from CPCB observation towers across India.",
        ["On a cold winter morning at {at}, the city AQI reads 380 ('Severe / Hazardous') on the weather app."],
        "How should {name} adjust daily activities to safeguard lung health?",
        [("Wear a certified, snug-fitting N95 mask if stepping outdoors", "Filters sub-micron fine particulate matter (PM2.5).", True, "n95 mask|well fitted mask|filter pm2.5", 45),
         ("Reschedule heavy outdoor running or football to indoor light stretches", "Prevents deep inhalation of toxic smog.", True, "indoor exercise|avoid heavy outdoor sports|severe aqi", 35),
         ("Check the CPCB SAMEER app daily to monitor air quality trends", "Evidence-based health choices.", False, "check aqi|sameer app|cpcb", 20)],
        ["run 10 km in heavy smog", "wear thin cloth kerchief", "ignore 380 aqi"],
        "CPCB National Air Quality Index Portal", "https://app.cpcbccr.com"
    ))

    # 14. ENV-034: Climate change
    cards.append(make_card(
        "ENV-034", "terra", "Climate", "Climate change explained simply: Greenhouse gases and solutions",
        ["middle", "senior"],
        ["Burning coal, oil, and gas releases excess CO2, which forms an atmospheric blanket trapping solar heat.",
         "Global warming intensifies extreme weather events in India: erratic monsoons, heatwaves, and glacier retreats."],
        ["Understand that individual conservation + renewable energy transitions are essential solutions", "Conserve electricity at home (switch off lights/fans) to cut thermal coal power demand", "Opt for walking, cycling, and public electric buses to lower transport carbon emissions"],
        ["Never fall into climate doomism: positive youth action drives systemic green policies", "Never waste resources thinking 'my tiny action doesn't matter'"],
        "Climate change is a fictional theory that only affects polar bears in the Arctic.", "myth", "Climate change directly triggers 48°C Indian city heatwaves, crop failures, and flash floods.",
        "What primary human activity drives accelerated global climate change?",
        ["Planting flowers", "Burning fossil fuels (coal, petroleum, natural gas) releasing greenhouse gases", "Drinking water", "Painting houses"], 1,
        "Fossil fuel combustion releases billions of tonnes of greenhouse gases into the atmosphere.",
        ["Discussing global climate change in science class at {at}, {name} wonders how young people can make an impact."],
        "What constructive understanding should {name} embrace?",
        [("Recognize that burning fossil fuels traps heat in the atmosphere, warming the planet", "Understands scientific root mechanism.", True, "greenhouse effect|fossil fuels|carbon emissions", 40),
         ("Adopt active daily climate habits: saving electricity, cycling, and minimizing waste", "Translates knowledge into personal lifestyle.", True, "save electricity|walk cycle|reduce waste|lifestyle", 40),
         ("Advocate for clean solar energy and tree conservation in school and community", "Champions collective civic solutions.", False, "solar energy|advocate|plant trees", 20)],
        ["claim climate change is fake", "waste electricity recklessly", "give up in despair"],
        "Intergovernmental Panel on Climate Change (IPCC) Youth Guide", "https://ipcc.ch"
    ))

    # 15. ENV-035: Green festivals
    cards.append(make_card(
        "ENV-035", "terra", "Green festivals", "Celebrating festivals green: Clay idols, herbal colors and zero plastic",
        ["junior", "middle", "senior"],
        ["Plaster of Paris (PoP) idols painted with chemical paints contain lead and mercury, poisoning rivers.",
         "Natural clay (shadu mati) idols dissolve completely in water within 48 hours without polluting ecosystems."],
        ["Choose eco-friendly unbaked clay or seed-embedded idols that dissolve safely at home in a bucket", "Use natural plant colors for Holi: turmeric, beetroot, arrowroot, and marigold petals", "Decorate homes using traditional reusable brass diyas, marigold flowers, and cloth bunting instead of plastic strings"],
        ["Never immerse chemical Plaster of Paris idols into natural lakes or rivers", "Never use toxic metallic chemical colors (silver, copper) during Holi"],
        "Plaster of Paris (PoP) dissolves harmlessly in rivers just like natural river clay.", "myth", "PoP takes months to dissolve, forming a toxic insoluble sludge that suffocates aquatic fish.",
        "Why are natural clay (Shadu Mati) idols vastly superior to Plaster of Paris (PoP) statues?",
        ["They are heavier", "Natural clay dissolves completely in water without releasing toxic lead or chemical sludge", "They are made of plastic", "They shine like neon"], 1,
        "Pure clay returns to nature organically without poisoning municipal water supply sources.",
        ["Preparing for festival celebrations at {at}, {name}'s family goes to select an idol."],
        "What sustainable choice should {name} encourage?",
        [("Choose a pure unbaked clay (shadu mati) idol painted with non-toxic natural colors", "Safeguards water bodies from chemical poisoning.", True, "clay idol|shadu mati|eco friendly|natural color", 45),
         ("Perform immersion at home in a bucket or dedicated municipal artificial tank", "Prevents choking natural lakes and rivers.", True, "home immersion|artificial tank|bucket immersion", 35),
         ("Decorate with fresh flowers and reusable earthen lamps instead of single-use plastic", "Leaves zero plastic footprint.", False, "fresh flowers|earthen diyas|no plastic", 20)],
        ["buy huge painted pop statue", "dump chemical idol in drinking river", "use toxic chemical paints"],
        "CPCB Guidelines on Eco-Friendly Idol Immersion", "https://cpcb.nic.in"
    ))

    # 16. ENV-036: Biodiversity walk
    cards.append(make_card(
        "ENV-036", "terra", "Biodiversity", "Neighborhood nature: Observing local birds, trees and pollinators",
        ["junior", "middle", "senior"],
        ["Even dense Indian concrete cities support hundreds of resilient species: sunbirds, dragonflies, and bees.",
         "Spending regular time observing nature reduces student anxiety and builds deep environmental empathy."],
        ["Take a 20-minute silent 'Biodiversity Walk' once a week in your local park or colony lane", "Keep a pocket nature journal to sketch leaves, record bird calls, and note flowering dates", "Leave undisturbed green patches of wildflowers in gardens for pollinator honeybees and butterflies"],
        ["Never throw stones at birds or destroy spider webs outdoors", "Never spray toxic chemical insecticides on flowering garden plants"],
        "Cities have zero biodiversity; you must visit deep national forest reserves to see living nature.", "myth", "Indian city trees host tailorbirds, bulObjective, barbets, honeybees, and diverse pollinator ecosystems.",
        "What is the ecological term for observing and recording living species in your immediate neighborhood?",
        ["Astronomy", "Citizen Science & Urban Biodiversity Observation", "Speed walking", "Architecture"], 1,
        "Citizen science empowers everyday students to document local species and preserve urban nature.",
        ["On a Sunday morning at {at}, {name} decides to explore the neighborhood park with a notebook."],
        "How can {name} conduct a rewarding urban biodiversity walk?",
        [("Quietly observe and note common birds (sunbirds, mynas, pigeons) and flowering trees", "Develops keen ecological observation skills.", True, "observe birds|trees|nature journal|biodiversity", 45),
         ("Avoid disturbing nests, breaking branches, or trampling pollinator flowerbeds", "Practices ethical, respectful nature exploration.", True, "respect wildlife|no harm|gentle exploration", 35),
         ("Share discoveries with classmates to build collective enthusiasm for urban conservation", "Fosters grassroots environmental care.", False, "share with friends|nature walk", 20)],
        ["throw rocks at bird nests", "pluck all flowers", "trample insect habitats"],
        "India Biodiversity Portal", "https://indiabiodiversity.org"
    ))

    print(f"Loaded {len(cards)} expanded cards for Terra")
    return cards


def get_cipher_cards():
    cards = []

    # 1. DIG-021: UPI collect request
    cards.append(make_card(
        "DIG-021", "cipher", "UPI safety", "UPI collect-request fraud: PIN is ONLY for paying",
        ["middle", "senior"],
        ["Entering your UPI MPIN ALWAYS deducts money from your bank account; it NEVER receives money.",
         "Cyber fraudsters send 'Collect Requests' disguised as 'Refunds' or 'Cashback Prize Won'."],
        ["Remember the golden rule: You NEVER need to enter your UPI PIN to receive money into your account", "Decline and report any suspicious UPI collect requests received on Google Pay, PhonePe, or Paytm", "Verify the sender's VPA / UPI ID before sending any genuine payment"],
        ["Never enter your 4 or 6-digit UPI PIN when someone promises to send you money", "Never approve an unexpected notification pop-up asking for your PIN"],
        "Entering your UPI PIN is required to verify your identity and receive lottery prize cashback.", "myth", "You NEVER enter your UPI PIN to receive money. PIN entry authorizes a debit from your balance.",
        "A buyer on OLX says: 'I have sent you ₹1,000; enter your UPI PIN to accept it.' What is the truth?",
        ["You must enter PIN to accept", "It is a scam: entering your UPI PIN will instantly transfer ₹1,000 from YOUR bank account to the scammer", "It gives bonus", "It is safe"], 1,
        "UPI PIN is an authorization signature for debiting funds. Receiving money is completely automatic.",
        ["Selling an old bicycle on an online marketplace at {at}, the buyer sends a UPI link saying: 'Enter your UPI PIN to receive advance payment.'"],
        "What should {name} do immediately?",
        [("Do NOT enter UPI PIN under any circumstances", "Prevents unauthorized financial theft.", True, "don'?t enter pin|no upi pin|never enter pin", 45),
         ("Recognize that receiving UPI payments NEVER requires entering a PIN", "Understands core UPI architecture.", True, "receiving never needs pin|scam attempt|fraud", 35),
         ("Block the scammer on the app and report their UPI ID as fraud", "Shields other users from fraud.", False, "block scammer|report upi id", 20)],
        ["enter 6-digit pin", "share bank otp", "click approve collect request"],
        "National Payments Corporation of India (NPCI) UPI Safety Guidelines", "https://npci.org.in"
    ))

    # 2. DIG-022: Fake customer care
    cards.append(make_card(
        "DIG-022", "cipher", "Search safety", "Spotting fake customer care helpline numbers on search engines",
        ["middle", "senior"],
        ["Cybercriminals edit Google Maps listings and buy search ads with fake helpline numbers for courier/banks.",
         "When victims call the fake number, fraudsters ask them to install remote screen-sharing apps."],
        ["Find customer care helplines exclusively inside the official verified mobile app or website", "Look for verified domain names ending in official bank URLs, not random blogspot or mobile numbers", "Hang up immediately if an 'agent' asks you to download AnyDesk, TeamViewer, or send ₹5"],
        ["Never google 'courier customer care number' and dial the first random mobile number listed", "Never share account numbers or debit card CVVs with phone callers"],
        "The top phone number displayed on Google search results is always the official certified customer care.", "myth", "Fraudsters easily manipulate Google business listings and buy search ads with personal fraud numbers.",
        "Where is the only authentic place to find the customer support number for an app like Swiggy, Amazon, or a bank?",
        ["A random blog on Google", "Inside the official mobile app under the 'Help & Support' section", "In YouTube comments", "On an anonymous flyer"], 1,
        "Official in-app help desks connect directly to verified support without search engine manipulation.",
        ["A package is delayed at {at}, and {name}'s family wants to search Google for the courier company's toll-free number."],
        "What cyber precaution must {name} explain?",
        [("Do not dial random mobile numbers found in Google search snippets", "Fraudsters post fake phone numbers to scam callers.", True, "don'?t call google search numbers|fake numbers|scam", 40),
         ("Look for customer support inside the courier's official app or tracked order page", "Guarantees authentic communication channel.", True, "in-app support|official app|verified website", 40),
         ("Never install screen-sharing apps if instructed by a phone caller", "Blocks remote device takeover.", False, "no remote apps|never install anydesk", 20)],
        ["call first 10-digit mobile number found", "give card number to caller", "install remote app"],
        "Indian Cyber Crime Coordination Centre (I4C)", "https://cybercrime.gov.in"
    ))

    # 3. DIG-023: QR code scams
    cards.append(make_card(
        "DIG-023", "cipher", "QR safety", "QR code scams: 'Scan QR to receive cash rewards'",
        ["junior", "middle", "senior"],
        ["Scanning a merchant QR code in a payment app is an action to SEND money from your bank.",
         "Scammers send QR codes claiming: 'Scan this barcode to get ₹2,000 refund/scholarship credit.'"],
        ["Remember: Scanning a QR code is for paying someone, never for receiving money into your wallet", "Only scan QR codes at physical merchant checkouts where YOU are the one making a purchase", "Reject any message with QR codes promising surprise lottery cashback or prize redemptions"],
        ["Never scan an unexpected QR code sent on WhatsApp by an unknown buyer or stranger", "Never approve transaction amounts after scanning a stranger's QR code"],
        "Scanning a QR code sent to your WhatsApp is a safe way to claim a free ₹500 shopping voucher.", "myth", "Scanning the code loads a payment debit request that drains money from your linked account.",
        "What happens when you scan a QR code in a payment app like PhonePe or Google Pay?",
        ["It scans your face", "It prepares a transaction to SEND money from your bank account to the merchant", "It deposits cash automatically", "It cleans phone"], 1,
        "QR codes encode the receiver's bank coordinates; scanning them always initiates an outgoing debit.",
        ["A message on WhatsApp at {at} contains a colorful image with a QR code: 'Scan to receive your ₹1,500 government student reward.'"],
        "What should {name} do?",
        [("Do NOT scan the QR code", "Prevents initiating an outgoing payment debit.", True, "don'?t scan|do not scan qr|scam", 45),
         ("Recognize that QR codes are used to PAY money, never to receive rewards", "Basic digital payment literacy.", True, "qr is for paying|cannot receive via qr|fraud", 35),
         ("Delete the message and warn family members about QR reward scams", "Prevents family members falling victim.", False, "delete message|warn family", 20)],
        ["scan code immediately", "enter bank pin after scan", "forward QR to all classmates"],
        "Reserve Bank of India (RBI Kehta Hai)", "https://rbikehtahai.rbi.org.in"
    ))

    # 4. DIG-024: Task scams
    cards.append(make_card(
        "DIG-024", "cipher", "Employment scams", "Work-from-home and 'Like YouTube videos for ₹5,000' task scams",
        ["middle", "senior"],
        ["Scammers recruit students on Telegram/WhatsApp with offers of ₹50-₹100 for liking YouTube videos.",
         "After paying small genuine initial sums, they trap victims into investing thousands in 'prepaid crypto tasks.'"],
        ["Recognize that legitimate companies never hire students on Telegram to like random social media posts", "Understand the bait-and-switch trap: scammers pay ₹200 initially to build trust before stealing ₹50,000", "Block and report unsolicited job recruitment messages on WhatsApp, Instagram, and Telegram"],
        ["Never pay 'registration fees', 'security deposits', or 'crypto recharge' to unlock earned money", "Never share personal bank account details with anonymous Telegram group admins"],
        "Earning ₹5,000 a day just by liking 10 YouTube videos from your bed is a legitimate part-time job.", "myth", "This is an international Ponzi task scam orchestrated by cyber syndicates to lure students.",
        "You are added to a Telegram group promising ₹3,000 daily for reviewing hotels and watching videos. What is this?",
        ["A great career opportunity", "A well-known cyber task scam designed to steal your savings", "A school project", "Government scheme"], 1,
        "Task scams trick victims into sending prepaid deposits that can never be withdrawn.",
        ["A stranger on WhatsApp at {at} offers {name}: 'Work from home: Like 5 videos, earn ₹200 instantly, join Telegram.'"],
        "What is the only smart response for {name}?",
        [("Recognize it immediately as a fraudulent task scam and do not engage", "Rejects criminal recruitment pipeline.", True, "task scam|fraud|don'?t engage|fake job", 45),
         ("Block the phone number and report the chat on WhatsApp", "Halts further contact attempts.", True, "block number|report spam|report whatsapp", 35),
         ("Never send any money or bank details to anonymous online employers", "Protects financial security.", False, "never send money|no deposit", 20)],
        ["join telegram channel", "send ₹1,000 deposit to unlock tasks", "share bank passbook"],
        "Ministry of Home Affairs Cyber Crime Advisory", "https://cybercrime.gov.in"
    ))

    # 5. DIG-025: App permissions
    cards.append(make_card(
        "DIG-025", "cipher", "Privacy", "Auditing app permissions: Camera, microphone and contact access",
        ["junior", "middle", "senior"],
        ["Malicious apps request unnecessary permissions (contacts, SMS, location) to harvest and sell personal data.",
         "A simple calculator or flashlight app has zero legitimate reason to access your camera or contact book."],
        ["Check app permissions during installation: only grant access essential to core app functionality", "Set location and microphone permissions to 'Only while using the app', never 'Allow all the time'", "Regularly audit installed apps in Phone Settings -> Privacy -> Permission Manager"],
        ["Never grant SMS reading permission to unverified utility or gaming apps (steals OTPs)", "Never download apps from unverified third-party APK websites outside official app stores"],
        "Giving all permissions requested by an app is harmless because app stores guarantee 100% safety.", "myth", "Apps frequently harvest contact books and background location to sell to predatory advertisers and scammers.",
        "Why is it suspicious if a basic Offline Calculator app requests permission to read your Contacts and SMS?",
        ["Calculators need friends", "It has no functional need for contacts; it is likely spyware harvesting data and reading bank OTPs", "It makes calculations faster", "It is normal"], 1,
        "Permissions must strictly match functionality. SMS permissions allow malware to read two-factor OTPs.",
        ["Installing a free puzzle game on a smartphone at {at}, the app requests access to Contacts, SMS, and Microphone."],
        "How should {name} manage these permission requests?",
        [("Deny access to SMS, Contacts, and Microphone", "Restricts unnecessary data harvesting.", True, "deny permissions|reject contacts|no sms access", 45),
         ("Uninstall the app if it refuses to run without invasive unrelated permissions", "Refuses predatory spyware apps.", True, "uninstall app|suspicious|delete app", 35),
         ("Review app permissions regularly in system Settings -> Permission Manager", "Maintains ongoing device privacy.", False, "permission manager|check settings|audit privacy", 20)],
        ["allow all permissions always", "give sms access to game", "download random apks"],
        "CERT-In Mobile Security Advisory", "https://cert-in.org.in"
    ))

    # 6. DIG-026: Public Wi-Fi
    cards.append(make_card(
        "DIG-026", "cipher", "Wi-Fi safety", "Public Wi-Fi risks: Packet sniffing and rogue hotspots",
        ["middle", "senior"],
        ["Open public Wi-Fi networks (cafes, railway stations, airports) lack encryption between device and router.",
         "Hackers on the same unencrypted network can intercept unencrypted data packets ('Man-in-the-Middle')."],
        ["Avoid conducting bank transactions, UPI transfers, or entering sensitive passwords on open public Wi-Fi", "Turn off 'Auto-connect to open Wi-Fi networks' in your phone's Wi-Fi settings", "Use cellular mobile data (4G/5G) or a verified Virtual Private Network (VPN) for sensitive tasks"],
        ["Never trust unverified pop-ups on public Wi-Fi asking you to install a 'Security Certificate' or profile", "Never leave Bluetooth and Wi-Fi toggled on when not actively in use"],
        "Free Wi-Fi named 'Railway_Free_Wi-Fi_Official' at a station is guaranteed to be safe and encrypted.", "myth", "Anyone can set up a rogue hotspot with a legitimate-sounding name to intercept victim passwords.",
        "What should you NEVER do while connected to free public Wi-Fi at a shopping mall?",
        ["Check weather", "Log into your bank account, enter credit card details, or change master passwords", "Read a Wikipedia article", "Listen to music"], 1,
        "Financial and password logins should strictly be conducted over secure encrypted cellular networks.",
        ["Waiting at a railway station at {at}, {name} connects to free open station Wi-Fi and needs to check school fee payment."],
        "What is the cyber-safe protocol for {name}?",
        [("Disconnect from public Wi-Fi and use personal mobile cellular data for payments", "Cellular networks are securely encrypted.", True, "use mobile data|disconnect public wifi|cellular data", 45),
         ("Do not enter banking passwords or debit card credentials over open unencrypted Wi-Fi", "Shields credentials from network sniffers.", True, "no banking on public wifi|no passwords", 35),
         ("Turn off 'Auto-connect to open networks' in device settings", "Prevents silent background connections.", False, "turn off auto connect|disable wifi", 20)],
        ["do netbanking on open wifi", "install unknown certificate", "leave wifi open always"],
        "CERT-In Guidelines for Safe Public Wi-Fi Usage", "https://cert-in.org.in"
    ))

    # 7. DIG-027: Phishing URLs
    cards.append(make_card(
        "DIG-027", "cipher", "Phishing", "Spotting deceptive lookalike phishing URLs and websites",
        ["junior", "middle", "senior"],
        ["Phishing sites use typosquatting: subtle misspellings like 'micros0ft.com' or 'sbi-update-kyc.net'.",
         "The padlock icon (HTTPS) only means the connection is encrypted; it does NOT guarantee the site is honest."],
        ["Inspect the domain name carefully: the real address is the text immediately before the final slash (domain.com/)", "Type official addresses directly into the browser address bar rather than clicking SMS links", "Watch out for urgency triggers: 'Account suspended in 2 hours, click to verify now!'"],
        ["Never click login links sent via SMS, WhatsApp, or unsolicited emails", "Never enter passwords on web pages with weird subdomains (like login.google.com.attacker.xyz)"],
        "If a website displays a padlock icon in the browser URL bar, it cannot be a scam website.", "myth", "Scammers get free SSL certificates easily. The padlock means encrypted, not authentic.",
        "Which of the following URLs is a dangerous fake phishing website trying to imitate State Bank of India?",
        ["https://onlinesbi.sbi/", "https://sbi-kyc-verification-update.free-web.xyz/login", "https://sbi.co.in", "https://bank.sbi"], 1,
        "The deceptive URL uses long hyphenated keywords on a suspicious free web domain.",
        ["An urgent SMS arrives on {name}'s phone at {at}: 'Your account is blocked! Update KYC immediately at http://bank-kyc.net/verify'."],
        "What tells {name} this is a phishing scam?",
        [("The URL is not an official bank domain, and banks never send KYC links via SMS", "Identifies fake domain and deceptive protocol.", True, "fake url|not official domain|phishing|banks don'?t text kyc", 45),
         ("The message uses artificial urgency to induce panic and hasty action", "Recognizes social engineering tactic.", True, "artificial urgency|panic|pressure", 35),
         ("Delete the message and report the sending number to cybercrime reporting channels", "Safe disposal and threat intelligence.", False, "delete sms|report number|1930", 20)],
        ["click link and enter password", "share debit card pin", "forward link to family"],
        "National Cyber Security Awareness Guidelines", "https://csk.gov.in"
    ))

    # 8. DIG-028: Screen sharing apps
    cards.append(make_card(
        "DIG-028", "cipher", "Remote access", "Screen-sharing app fraud: AnyDesk, TeamViewer and RustDesk",
        ["middle", "senior"],
        ["Screen-sharing apps allow a remote user across the globe to see your screen and control your device.",
         "Scammers posing as customer care or telecom officers ask victims to read out a 9-digit remote access code."],
        ["Never download AnyDesk, TeamViewer, QuickSupport, or RustDesk on instructions from a phone caller", "Remember: Legitimate banks and customer service agents NEVER ask to view your personal phone screen", "If you accidentally installed one, disconnect internet immediately, uninstall the app, and restart device"],
        ["Never read out your screen-sharing 9-digit access code or grant remote permissions to a stranger", "Never log into banking apps while a screen-sharing session is active"],
        "Customer support executives from electricity boards need remote screen access to fix your meter bill.", "myth", "Electricity and telecom boards NEVER use AnyDesk. Remote access is 100% utilized to steal banking OTPs.",
        "A caller claiming to be from your telecom provider says you must install 'AnyDesk' to update your 5G SIM. What is this?",
        ["A routine upgrade", "A dangerous cyber scam: installing it allows the caller to see your screen and steal your passwords", "A fun game", "Speed booster"], 1,
        "AnyDesk reveals incoming OTPs and bank screens directly to the criminal.",
        ["A caller claiming to be from customer care at {at} tells {name}: 'Download TeamViewer QuickSupport and give me the 9-digit code.'"],
        "What must {name} do?",
        [("Refuse immediately and hang up the call", "Blocks remote takeover before connection.", True, "hang up|refuse|disconnect call", 45),
         ("Never install screen-sharing software or share the 9-digit connection code", "Prevents full remote control of smartphone.", True, "never install anydesk|don'?t share code|teamviewer", 35),
         ("Warn family members that genuine companies never request remote screen access", "Educates household against fraud.", False, "warn family|genuine companies never ask", 20)],
        ["install teamviewer", "give 9-digit code to caller", "open banking app while sharing"],
        "RBI Cyber Security Framework", "https://rbi.org.in"
    ))

    # 9. DIG-029: Cyberbullying
    cards.append(make_card(
        "DIG-029", "cipher", "Cyberbullying", "Handling cyberbullying: Screenshot, block, report and tell",
        ["junior", "middle", "senior"],
        ["Cyberbullying involves harassment, vicious rumours, abusive DMs, or exclusion in online group chats.",
         "Retaliating with angry insults fuels the bully and can lead to disciplinary action against you."],
        ["Do not respond or retaliate with angry messages (bullies seek your emotional reaction)", "Take clear screenshots showing the abusive messages, account handle, and timestamp as evidence", "Block the harasser on the platform, report their account, and tell a trusted adult immediately"],
        ["Never delete the evidence before capturing screenshots", "Never suffer in silence or blame yourself for someone else's abusive behavior"],
        "The best way to deal with an online bully is to insult them back twice as hard in the class group chat.", "myth", "Retaliation escalates the abuse cycle, leaves a toxic digital footprint, and solves nothing.",
        "What is the proven 4-step sequence to handle cyberbullying messages effectively?",
        ["Cry and delete phone", "Do not reply, Screenshot evidence, Block user, Tell a trusted adult", "Forward to all friends", "Insult their family"], 1,
        "Documentation, boundary enforcement, and adult support disempower cyberbullies.",
        ["In a school WhatsApp or gaming group at {at}, someone begins posting targeted insults and mocking {name}."],
        "How should {name} respond constructively?",
        [("Do not reply with anger; capture clear screenshots showing messages and sender numbers", "Preserves objective evidence without escalation.", True, "don'?t reply|take screenshots|capture evidence", 45),
         ("Block the user on the app and report the bullying to platform moderators", "Cuts communication channel immediately.", True, "block user|report account|report to platform", 35),
         ("Share the screenshots with parents or a trusted teacher for school intervention", "Secures institutional support.", False, "tell parent|tell teacher|adult help", 20)],
        ["reply with abusive curses", "delete evidence and suffer silently", "fight in public chat"],
        "Cyber Peace Foundation Youth Safety Guide", "https://cyberpeace.org"
    ))

    # 10. DIG-030: Image threats
    cards.append(make_card(
        "DIG-030", "cipher", "Extortion", "Morphed photos and online extortion: You are not at fault",
        ["middle", "senior"],
        ["Scammers use AI deepfake tools to morph public social media photos and threaten extortion.",
         "Paying money to extortionists NEVER stops the harassment; it only invites higher extortion demands."],
        ["Remember: You are the victim of a crime; this is NEVER your fault and you have nothing to feel ashamed of", "Do not pay any money and do not reply to the blackmailer's threats", "Confide in a parent, teacher, or trusted adult immediately and call the National Cyber Crime Helpline at 1930"],
        ["Never pay blackmailers a single rupee (they will demand more immediately)", "Never panic or self-harm; law enforcement has specialized units to deal with image blackmail"],
        "If an online blackmailer threatens to share a morphed photo, paying them ₹2,000 will make them delete it.", "myth", "Blackmailers never delete files after payment; paying proves you can be coerced and leads to relentless extortion.",
        "What is the official national helpline number for reporting cyber financial fraud and online harassment in India?",
        ["100", "1930", "101", "108"], 1,
        "Dialing 1930 connects directly to the National Cyber Crime Reporting Portal.",
        ["A stranger on Instagram at {at} threatens {name} with an AI-morphed image demanding money."],
        "What is the vital, life-saving course of action for {name}?",
        [("Do NOT pay any money, do not delete the chat, and stop replying", "Halts extortion cycle immediately.", True, "do not pay|stop replying|don'?t send money", 45),
         ("Confide immediately in parents or a trusted school counselor: 'You are the victim, not at fault'", "Removes isolation and fear.", True, "tell parents|trusted adult|not your fault|counselor", 35),
         ("Report immediately on the National Cyber Crime Portal (1930 / cybercrime.gov.in)", "Triggers law enforcement action.", False, "call 1930|cybercrime portal|police", 20)],
        ["pay the money secretly", "panic in isolation", "blame yourself"],
        "National Cyber Crime Reporting Portal (MHA)", "https://cybercrime.gov.in"
    ))

    # 11. DIG-031: Gaming scams
    cards.append(make_card(
        "DIG-031", "cipher", "Gaming safety", "Gaming scams: Free skins, robux, and account credential phishing",
        ["junior", "middle", "senior"],
        ["Third-party websites promising 'Free V-Bucks/Free Robux/Free BGMI UC' are 100% credential-harvesting phishing scams.",
         "Downloading cheat engines or game mods often injects hidden keylogger Trojans into your device."],
        ["Obtain in-game items exclusively through official game stores with parent supervision", "Never enter your gaming email and password on external websites promising free rewards", "Enable two-factor authentication (2FA) on your Steam, Epic, Discord, and Roblox accounts"],
        ["Never share your gaming account login password with online 'friends' who promise to rank up your profile", "Never download unofficial APK cheats or unauthorized modded game clients"],
        "Websites with names like 'free-robux-generator-2026.net' are official partner reward portals.", "myth", "Game developers never partner with free reward generators. These sites exist exclusively to hijack player accounts.",
        "A stranger on Discord offers to give you a rare gaming skin if you give them your login password for 10 minutes. What should you do?",
        ["Share password happily", "Refuse and never share your password: it is a scam to steal your account permanently", "Share email only", "Send credit card"], 1,
        "Never share passwords. Real game developers will never ask for your account password.",
        ["While playing an online multiplayer game at {at}, an opponent posts a link in chat: 'Click here for 5,000 free gems and elite skins!'"],
        "What should {name} do?",
        [("Do NOT click the external link or enter any login credentials", "Protects gaming account from being hijacked.", True, "don'?t click|ignore link|fake skins|scam", 45),
         ("Recognize that third-party 'free gem generators' are phishing traps", "Understands malicious gaming vectors.", True, "phishing trap|fake generator|harvest passwords", 35),
         ("Report the player's account in-game for spamming malicious phishing links", "Protects other community players.", False, "report player|in-game report", 20)],
        ["click link and enter password", "download cheat mod", "share discord token"],
        "CERT-In Online Gaming Advisory", "https://cert-in.org.in"
    ))

    # 12. DIG-032: 2FA setup
    cards.append(make_card(
        "DIG-032", "cipher", "Authentication", "Two-Factor Authentication (2FA): The unbreakable digital lock",
        ["junior", "middle", "senior"],
        ["Two-Factor Authentication (2FA) requires two pieces of evidence: something you know (password) + something you have (phone/app).",
         "Even if a hacker discovers or guesses your password, 2FA blocks over 99% of automated account takeovers."],
        ["Enable 2-Step Verification on your Google, Instagram, WhatsApp, and gaming accounts", "Use an authenticator app (Google Authenticator, Microsoft Authenticator) instead of SMS OTP where available", "Safely write down offline backup recovery codes and store them in a secure home drawer"],
        ["Never share your 2FA prompt or 6-digit authentication codes with anyone who asks", "Never click 'Yes, it's me' on a phone prompt unless you are actively logging in yourself"],
        "A strong 12-character password is so secure that you never need to turn on 2FA.", "myth", "Passwords leak in corporate database breaches. 2FA stops hackers even when your password is leaked.",
        "What does Two-Factor Authentication (2FA) do when someone tries to log into your account from another city?",
        ["It shuts down internet", "It sends a verification prompt to YOUR phone that the hacker cannot access, blocking them", "It changes your photo", "Nothing"], 1,
        "2FA adds a physical hardware barrier that remote cybercriminals cannot bypass.",
        ["Setting up a new email account for school at {at}, {name} sees an option: 'Turn on 2-Step Verification.'"],
        "Why should {name} enable this immediately?",
        [("Turn on 2-Step Verification right away to secure the account", "Adds decisive second layer of defense.", True, "turn on 2fa|2-step verification|enable 2fa", 45),
         ("Understand that 2FA stops hackers even if they leak or steal your password", "Understands dual authentication benefits.", True, "blocks unauthorized access|second layer|stops hackers", 35),
         ("Save backup recovery codes in a safe, offline physical place", "Ensures recovery if phone is lost.", False, "backup codes|recovery codes", 20)],
        ["skip 2fa", "share 2fa code with friends", "click yes on random phone prompts"],
        "National Cyber Security Centre Guidelines", "https://ncsc.gov.uk"
    ))

    # 13. DIG-033: Lost phone protocol
    cards.append(make_card(
        "DIG-033", "cipher", "Device loss", "Lost or stolen smartphone emergency checklist",
        ["middle", "senior"],
        ["Smartphones contain banking access, private family photos, email accounts, and stored passwords.",
         "Swift emergency action within the first hour prevents fraudsters from siphoning linked bank accounts."],
        ["Use Google 'Find My Device' (Android) or Apple 'Find My' (iOS) to remotely lock and locate the phone", "Contact your telecom carrier immediately to block the SIM card (stops scammers from receiving OTPs)", "Log into your Google/Apple accounts on a computer and choose 'Sign out of all sessions'"],
        ["Never delay blocking your SIM card after a phone theft", "Never keep written passwords or bank PINs saved in your phone's plain text notes app"],
        "If your phone is stolen, you only need to look for it next week because screen locks protect everything.", "myth", "Criminals swap stolen SIM cards into other phones in minutes to drain bank accounts via UPI.",
        "What is the most urgent step to take within 30 minutes of your smartphone being stolen?",
        ["Buy new headphones", "Call your telecom provider to block the SIM card and track/lock via Find My Device", "Post on social media", "Wait 3 days"], 1,
        "Blocking the SIM stops incoming bank OTPs, preventing unauthorized financial withdrawals.",
        ["While traveling back from school at {at}, {name} realizes their smartphone is missing from their bag."],
        "What emergency sequence should {name} execute immediately with parents?",
        [("Use Google 'Find My Device' / Apple 'Find My' on a family phone to remotely lock the screen", "Secures device access and initiates location tracking.", True, "find my device|remotely lock|track phone", 45),
         ("Call the telecom customer care to block the SIM card immediately", "Prevents incoming OTP interception.", True, "block sim card|telecom carrier|stop otps", 35),
         ("Change primary passwords and inform bank to freeze mobile UPI access", "Shields linked finances.", False, "change passwords|alert bank|freeze upi", 20)],
        ["wait a week before doing anything", "assume phone is gone and do nothing", "call own phone repeatedly without locking"],
        "Department of Telecommunications CEIR Portal", "https://ceir.sancharsaathi.gov.in"
    ))

    # 14. DIG-034: Digital footprint
    cards.append(make_card(
        "DIG-034", "cipher", "Reputation", "Your permanent digital footprint: Think before posting",
        ["junior", "middle", "senior"],
        ["Content shared online can be screenshotted, downloaded, and archived forever in seconds.",
         "College admission officers and future employers routinely audit applicants' public social media history."],
        ["Apply the 'Billboard Test': Would you be comfortable seeing this post on a giant billboard outside your school?", "Keep personal profiles private and only accept follower requests from people you know in real life", "Think for 60 seconds before posting in anger, frustration, or seeking temporary viral attention"],
        ["Never post personal home addresses, school uniforms with logos, or flight boarding passes", "Never post cruel memes, harassment, or humiliating photos of classmates"],
        "Deleting a photo from Instagram 5 minutes after posting deletes it permanently from the internet.", "myth", "Automated web scrapers, caches, and viewer screenshots archive content permanently in milliseconds.",
        "What is the 'Billboard Test' for evaluating social media posts before hitting publish?",
        ["Testing billboard lighting", "Asking yourself: 'Would I be proud if my parents, teachers, and future employer saw this on a giant billboard?'", "Advertising products", "None"], 1,
        "The billboard test instantly checks whether content aligns with your long-term reputation and values.",
        ["At {at}, {name} is tempted to post an angry, embarrassing rant about a strict teacher on social media."],
        "What wise digital citizenship perspective should {name} remember?",
        [("Remember that online posts leave a permanent digital footprint that can resurface years later", "Recognizes long-term reputational permanence.", True, "permanent digital footprint|cannot be fully deleted|billboard test", 45),
         ("Pause and cool down; do not post impulsive rants or confidential personal grievances online", "Exercises emotional self-regulation.", True, "pause and cool down|don'?t post in anger", 35),
         ("Talk through school frustrations privately with parents or trusted friends in person", "Constructive offline resolution.", False, "talk offline|resolve in person", 20)],
        ["post abusive rant publicly", "tag teacher in cruel memes", "post home address"],
        "Internet and Mobile Association of India (IAMAI)", "https://iamai.in"
    ))

    # 15. DIG-035: Loan app traps
    cards.append(make_card(
        "DIG-035", "cipher", "Financial safety", "Predatory instant loan apps: Blackmail and privacy extortion",
        ["middle", "senior"],
        ["Illegal loan apps attract young users with promises of 'Instant ₹5,000 cash with no credit check'.",
         "Upon installation, they steal the victim's entire contact book and photo gallery to blackmail families."],
        ["Only borrow through RBI-registered Scheduled Commercial Banks or Non-Banking Financial Companies (NBFCs)", "Check the RBI 'whitelist' of approved digital lending apps before ever installing a finance app", "Report harassing loan recovery blackmail to local police cyber cells and the 1930 national helpline"],
        ["Never install unverified Chinese instant loan APKs advertised on social media feeds", "Never grant photo gallery and contact permissions to instant cash apps"],
        "Instant loan apps offering quick ₹2,000 cash without documents are generous charitable services.", "myth", "Unregulated loan apps are vicious extortion traps that harvest contacts and threaten victims with extortionate rates.",
        "Why do illegal instant loan apps demand full access to your phone's Contacts and Photo Gallery?",
        ["To make friends", "To steal your contacts and photos to harass and blackmail your family and friends for money", "To check battery", "To back up photos"], 1,
        "Stolen contact lists are used by recovery syndicates to shame and harass victims' relatives.",
        ["A pop-up ad at {at} urges a senior student: 'Get ₹3,000 instant pocket money now, zero documents, instant download.'"],
        "What critical safety warning should {name} deliver?",
        [("Do NOT download or install unregulated instant loan apps", "Evades predatory extortion traps.", True, "don'?t download|predatory loan app|fraud trap", 45),
         ("Understand that these apps harvest contacts and gallery photos to blackmail borrowers", "Exposes criminal extortion mechanism.", True, "steals contacts|blackmail|harassment|illegal", 35),
         ("Verify that legitimate lending apps must be registered with the Reserve Bank of India", "Follows formal regulatory protections.", False, "rbi approved|legitimate banks only", 20)],
        ["download illegal loan apk", "give access to contacts", "borrow money from strangers online"],
        "RBI Sachet Portal for Unauthorized Entities", "https://sachet.rbi.org.in"
    ))

    # 16. DIG-036: National Cyber Portal
    cards.append(make_card(
        "DIG-036", "cipher", "Reporting", "Reporting cybercrime: The National Cyber Crime Portal (1930 & cybercrime.gov.in)",
        ["junior", "middle", "senior"],
        ["Reporting financial cyber fraud within the 'Golden Hour' (first 2 hours) allows banks to freeze stolen funds in transit.",
         "The Citizen Financial Cyber Fraud Reporting and Management System (CFCFRMS) has saved over ₹1,000 crore."],
        ["Call the National Cyber Crime Helpline number 1930 immediately if money is stolen through online fraud", "File a formal digital complaint on cybercrime.gov.in with transaction IDs, bank statements, and chat logs", "Report cyber threats, stalking, and identity theft promptly without shame or fear"],
        ["Never wait days before reporting online financial theft (stolen funds get laundered quickly)", "Never delete chat logs or SMS transaction alerts before saving screenshots for the police"],
        "Calling 1930 only works for multinational corporations, not individual school students.", "myth", "The 1930 helpline serves all Indian citizens, coordinating with local police to freeze fraudulent transactions.",
        "What national government helpline number should you call immediately if victimized by an online financial scam?",
        ["100", "1930", "108", "112"], 1,
        "1930 is the dedicated Indian National Cyber Crime Helpline for immediate financial fraud intervention.",
        ["A family member at {at} realizes they accidentally clicked a phishing link and ₹5,000 was debited from their account."],
        "What immediate steps should {name} guide them through?",
        [("Dial 1930 immediately to report the fraud to the National Cyber Crime Helpline", "Alerts inter-bank system to freeze funds before withdrawal.", True, "call 1930|dial 1930|cyber crime helpline", 45),
         ("File an online complaint on cybercrime.gov.in with transaction details and screenshots", "Generates formal police FIR investigation ticket.", True, "cybercrime.gov.in|file complaint|screenshots|transaction id", 35),
         ("Call the bank's official emergency toll-free number to freeze the compromised account/card", "Halts further unauthorized debits.", False, "call bank|freeze card|stop debits", 20)],
        ["wait 3 weeks", "delete all bank messages", "do nothing in shame"],
        "Indian Cyber Crime Coordination Centre (MHA)", "https://cybercrime.gov.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Cipher")
    return cards


def get_compass_cards():
    cards = []

    # 1. CAR-021: Software Engineer
    cards.append(make_card(
        "CAR-021", "compass", "Engineering", "Day in the life: Software Engineer and technologist",
        ["senior"],
        ["Software engineering is about creative problem-solving and logic, not just writing syntax.",
         "Engineers spend significant time collaborating in team standups, reading architecture docs, and reviewing code."],
        ["Focus on building strong fundamentals in mathematics, logic, and computational thinking", "Work on personal mini-projects (building a website, automating a study task, creating a game)", "Explore free platforms like Python tutorials, CS50, and open-source GitHub repositories"],
        ["Never believe that you must be a mathematical genius to learn coding", "Never copy-paste code without understanding the underlying logic"],
        "Software engineers work alone in dark rooms staring at green matrix code without speaking to anyone.", "myth", "Modern software engineering is highly collaborative, requiring teamwork, user empathy, and clear communication.",
        "What foundational skill is most important for a career in software technology?",
        ["Typing 100 words per minute", "Logical problem solving, curiosity, and structured thinking", "Memorizing whole textbooks", "Buying expensive monitors"], 1,
        "Problem decomposition and algorithmic logic form the core of computer science.",
        ["A Class 10 student at {at} wants to explore whether software engineering is the right fit."],
        "How can {name} evaluate and explore this career pathway?",
        [("Start building small hands-on projects with Python, HTML, or Scratch", "Validates practical interest through active building.", True, "build projects|learn python|scratch|hands-on", 45),
         ("Recognize that collaboration, communication, and debugging resilience matter as much as coding", "Provides realistic daily work picture.", True, "problem solving|teamwork|logic|communication", 35),
         ("Explore streams with Mathematics after Class 10 (Science or Commerce with Math)", "Ensures academic eligibility for tech degrees.", False, "mathematics stream|pcm|eligibility", 20)],
        ["memorize coding books without touching a computer", "assume coding is impossible", "pay lakhs for fake courses"],
        "All India Council for Technical Education (AICTE)", "https://aicte-india.org"
    ))

    # 2. CAR-022: Healthcare
    cards.append(make_card(
        "CAR-022", "compass", "Healthcare", "Day in the life: Doctor, nurse and healthcare professionals",
        ["senior"],
        ["Healthcare careers require deep biological science knowledge paired with profound human empathy.",
         "Pathways extend beyond MBBS to Nursing, Physiotherapy, Pharmacy, Radiology, and Medical Research."],
        ["Study Physics, Chemistry, and Biology (PCB) in Classes 11 and 12", "Develop emotional resilience, patient active listening, and calmness under pressure", "Explore allied healthcare fields: clinical psychology, biomechanics, biomedical tech, and public health"],
        ["Never choose medicine solely because of parental or social prestige pressure", "Never underestimate the dedication, long hours, and rigorous years of residency required"],
        "The only respectable and successful career in healthcare is becoming an MBBS surgeon.", "myth", "Modern healthcare relies equally on nurse specialists, biomedical engineers, radiographers, and pharmacologists.",
        "What academic stream subject combination is required in Class 11-12 for medical entrance exams like NEET?",
        ["Arts with History", "Physics, Chemistry, and Biology (PCB)", "Commerce with Accounts", "Vocational Carpentry"], 1,
        "NEET eligibility mandates studying Physics, Chemistry, and Biology/Biotechnology in senior secondary.",
        ["A student at {at} is passionate about helping sick people but is unsure about the MBBS journey."],
        "How should {name} help them explore healthcare broadly?",
        [("Explain that healthcare includes vital fields like Nursing, Physiotherapy, Pharmacy, and Biotechnology", "Broadens perspective beyond single entrance exams.", True, "nursing|physiotherapy|pharmacy|biotech|allied health", 45),
         ("Discuss the daily reality: empathy, shift work, continuous learning, and patient care", "Gives balanced, realistic picture of medical life.", True, "empathy|patient care|long hours|dedication", 35),
         ("Prepare strong fundamentals in PCB while exploring volunteer hospital internships", "Combines study with experiential exposure.", False, "pcb stream|hospital exposure", 20)],
        ["force into MBBS blindly", "rank careers by social status", "claim non-doctors are useless"],
        "National Medical Commission (NMC)", "https://nmc.org.in"
    ))

    # 3. CAR-023: Design & UX
    cards.append(make_card(
        "CAR-023", "compass", "Design", "Day in the life: Product and UI/UX Designer",
        ["senior"],
        ["Design is how something works and solves human problems, not just pretty decoration.",
         "UI/UX designers conduct user interviews, sketch wireframes, and design intuitive digital experiences."],
        ["Cultivate visual curiosity, user empathy, and problem observation in everyday life", "Build a diverse design portfolio showcasing how you solved a real problem (sketches, prototypes)", "Prepare for design entrance exams: UCEED (IITs), NID DAT, and NIFT"],
        ["Never think you cannot be a designer because you can't paint realistic oil portraits", "Never design interfaces without interviewing real users about their difficulties"],
        "Design is purely an art career for people who failed at science and commerce.", "myth", "Product and UX design combine cognitive psychology, technology, data analytics, and ergonomics.",
        "Which premier Indian institutions offer Bachelor of Design (B.Des) programs via UCEED?",
        ["Medical colleges", "Indian Institutes of Technology (IIT Bombay, IIT Delhi, IIT Guwahati)", "Police academies", "Law schools"], 1,
        "UCEED is the national entrance examination for B.Des programs across leading IITs and design institutes.",
        ["A Class 11 student at {at} loves both technology and drawing and wonders about career paths."],
        "How can {name} introduce them to User Experience (UX) design?",
        [("Explain that UX designers build intuitive interfaces that make apps easy for everyone to use", "Connects technology with visual empathy.", True, "ux design|user experience|interfaces|apps", 45),
         ("Encourage them to build a portfolio of wireframes, problem solutions, and sketches", "Portfolio-based evaluation is key to design admissions.", True, "portfolio|sketches|prototypes|problem solving", 35),
         ("Explore entrance exams like UCEED and NID DAT open to students from any stream", "Stream flexibility in design careers.", False, "uceed|nid|open to any stream", 20)],
        ["say drawing has no jobs", "force them to abandon creative interests", "claim only artists design"],
        "National Institute of Design (NID)", "https://nid.edu"
    ))

    # 4. CAR-024: Chartered Accountant
    cards.append(make_card(
        "CAR-024", "compass", "Finance", "Day in the life: Chartered Accountant and Financial Analyst",
        ["senior"],
        ["Chartered Accountants (CAs) manage taxation, financial audits, corporate strategy, and forensic accounting.",
         "The Institute of Chartered Accountants of India (ICAI) oversees the rigorous three-stage CA qualification."],
        ["Build rock-solid foundations in accountancy, business economics, and commercial law", "Develop sharp analytical attention to detail, numerical integrity, and ethical responsibility", "Register for the ICAI CA Foundation examination after appearing for Class 12 board exams"],
        ["Never assume CA is only about calculating routine math sums on a calculator", "Never compromise on financial ethics and corporate audit transparency"],
        "You must have studied Commerce in Class 11-12 to register for the CA Foundation exam.", "myth", "Students from ANY stream (Science, Commerce, or Arts) can appear for the ICAI CA Foundation exam.",
        "Which statutory professional body regulates the Chartered Accountancy profession in India?",
        ["UGC", "The Institute of Chartered Accountants of India (ICAI)", "SEBI only", "NITI Aayog"], 1,
        "ICAI is established under an Act of Parliament to regulate the CA profession.",
        ["A student at {at} enjoys numbers, business case studies, and corporate analysis."],
        "How should {name} structure their career exploration for Chartered Accountancy?",
        [("Explain the three-stage pathway: CA Foundation, CA Intermediate, and Articleship/Final", "Maps clear professional milestone roadmap.", True, "ca foundation|intermediate|articleship|final|icai", 45),
         ("Highlight the diverse career roles: forensic auditor, tax advisor, CFO, or financial analyst", "Reveals versatile corporate pathways.", True, "financial analyst|auditor|cfo|advisory", 35),
         ("Emphasize that discipline, analytical rigor, and ethics are paramount", "Sets realistic expectations for dedication.", False, "ethics|discipline|hard work", 20)],
        ["claim CA is impossible", "discourage commerce students", "say accounting is obsolete"],
        "Institute of Chartered Accountants of India (ICAI)", "https://icai.org"
    ))

    # 5. CAR-025: Legal Advocate
    cards.append(make_card(
        "CAR-025", "compass", "Law", "Day in the life: Lawyer, legal advocate and corporate counsel",
        ["senior"],
        ["Law is the framework that safeguards fundamental rights, contracts, justice, and social democracy.",
         "Modern legal practice spans litigation, corporate mergers, intellectual property, and environmental law."],
        ["Cultivate extensive reading habits, critical reasoning, and objective argument construction", "Prepare for national law entrance exams like the Common Law Admission Test (CLAT) for National Law Universities (NLUs)", "Participate in school debating, Model United Nations (MUN), and moot court simulations"],
        ["Never assume courtroom litigation is identical to dramatic Bollywood movie scenes", "Never rely on emotion over documented constitutional case law and evidence"],
        "To become a corporate lawyer, you must study science in school.", "myth", "Law entrance exams (CLAT) test English, Current Affairs, Legal Reasoning, and Logical Reasoning, open to all streams.",
        "What entrance exam provides admission to the premier National Law Universities (NLUs) in India?",
        ["JEE Main", "Common Law Admission Test (CLAT)", "NEET", "CAT"], 1,
        "CLAT is the centralized entrance examination for 5-year integrated BA LLB / BBA LLB programs at 24 NLUs.",
        ["A student passionate about justice, constitutional rights, and public speaking at {at} asks about law."],
        "How can {name} guide their legal career roadmap?",
        [("Introduce the 5-year integrated law degree (BA LLB/BBA LLB) via entrance exams like CLAT", "Clear academic entry point after Class 12.", True, "clat|nlu|ba llb|integrated law|5 year degree", 45),
         ("Discuss varied career paths: court litigation, corporate law, public policy, and judicial services", "Broadens perspective across diverse legal sectors.", True, "corporate law|litigation|judiciary|policy", 35),
         ("Encourage deep reading of newspapers, editorial analysis, and critical logical argumentation", "Builds foundational skills early.", False, "critical reading|arguments|logic|current affairs", 20)],
        ["say lawyers only argue in court", "discourage girls from law", "claim law needs no reading"],
        "Bar Council of India (BCI)", "https://barcouncilofindia.org"
    ))

    # 6. CAR-026: Data Analyst & AI
    cards.append(make_card(
        "CAR-026", "compass", "Data & AI", "Day in the life: Data Analyst and Artificial Intelligence practitioner",
        ["senior"],
        ["Data analysts find actionable trends in massive datasets; AI engineers build predictive machine learning models.",
         "Core disciplines combine statistics, linear algebra, Python programming, and domain business knowledge."],
        ["Build a strong foundation in high school statistics, probability, and linear algebra", "Learn Python libraries: Pandas for data manipulation, Matplotlib for charts, and Scikit-learn for models", "Explore public open data repositories (like Kaggle or Government Data Portal data.gov.in)"],
        ["Never treat AI as a magic black box without understanding the underlying math and data bias", "Never use uncleaned, unverified data to draw definitive statistical conclusions"],
        "You need a supercomputer to start learning data analytics and artificial intelligence.", "myth", "Free cloud platforms like Google Colab let students train machine learning models on basic laptops.",
        "What branch of mathematics forms the absolute core foundation of data science and machine learning?",
        ["Ancient geometry", "Statistics, probability, and linear algebra", "Trigonometry only", "Calculus only"], 1,
        "Machine learning models are fundamentally statistical optimization algorithms.",
        ["A Class 11 student at {at} wants to pursue Artificial Intelligence and Data Science."],
        "What practical, grounded advice should {name} share?",
        [("Strengthen school mathematics, especially statistics, probability, and functions", "Mathematical foundations enable deep AI comprehension.", True, "statistics|probability|maths foundation|linear algebra", 45),
         ("Start learning Python programming and explore datasets on Google Colab or Kaggle", "Hands-on data exploration experience.", True, "python|kaggle|google colab|machine learning", 35),
         ("Understand that ethical AI requires eliminating data bias and respecting user privacy", "Instills responsible technology principles.", False, "ai ethics|privacy|bias", 20)],
        ["believe AI needs no math", "buy expensive crypto courses", "assume AI replaces thinking"],
        "National Association of Software and Service Companies (NASSCOM FutureSkills)", "https://futureskillsprime.in"
    ))

    # 7. CAR-027: Educator
    cards.append(make_card(
        "CAR-027", "compass", "Education", "Day in the life: Teacher, professor and education mentor",
        ["senior"],
        ["Educators shape the intellectual foundations of the next generation of scientists, leaders, and artists.",
         "Modern teaching combines subject expertise, learning psychology, curriculum design, and ed-tech tools."],
        ["Pursue bachelor's degrees in your passion subject, followed by B.Ed (for schools) or Master's/PhD (for universities)", "Qualify eligibility exams: CTET/STET (for school teachers) or UGC NET (for college professorships)", "Develop patience, inspiring public communication, and student-centered mentoring empathy"],
        ["Never view teaching as a fallback option when other jobs fail; it is a foundational calling", "Never stop learning new pedagogy methods and modern digital classroom tools"],
        "School teachers only work 4 hours a day and have zero work outside the classroom.", "myth", "Dedicated teachers spend countless hours preparing lessons, evaluating feedback, and mentoring students.",
        "What national eligibility test is required to teach in central government schools (like Kendriya Vidyalayas)?",
        ["CAT", "Central Teacher Eligibility Test (CTET)", "GATE", "NEET"], 1,
        "CTET conducted by CBSE certifies teachers for Classes 1 to 8 across central schools.",
        ["A student at {at} loves explaining difficult science concepts to peers and wants to become a teacher."],
        "How can {name} validate and plan this rewarding career path?",
        [("Guide them through the pathway: Bachelor's degree in science, followed by B.Ed and CTET", "Clear educational certification steps.", True, "b.ed|ctet|ugc net|teaching pathway", 45),
         ("Encourage them to practice mentoring younger students and designing simple study notes", "Builds pedagogical craft early.", True, "practice teaching|mentoring|lesson design", 35),
         ("Highlight diverse modern roles: school educator, university professor, curriculum writer, ed-tech designer", "Shows broad educational landscape.", False, "curriculum design|professorship|edtech", 20)],
        ["mock teaching as a career", "claim teaching needs no skills", "discourage passion for education"],
        "National Council for Teacher Education (NCTE)", "https://ncte.gov.in"
    ))

    # 8. CAR-028: Armed Forces & Civil Services
    cards.append(make_card(
        "CAR-028", "compass", "Public service", "Serving the nation: Armed Forces (NDA/CDS) and Civil Services (UPSC)",
        ["senior"],
        ["The Armed Forces (Army, Navy, Air Force) offer leadership, discipline, adventure, and patriotic duty.",
         "The Union Public Service Commission (UPSC) selects civil servants (IAS, IPS, IFS) for national governance."],
        ["Apply for the National Defence Academy (NDA) entrance exam conducted by UPSC after Class 12 (now open to women)", "Maintain high physical fitness (running, pull-ups, stamina) alongside mental general awareness for the SSB interview", "For Civil Services (IAS/IPS), complete any graduation degree and build vast general studies knowledge"],
        ["Never believe that civil services or defence exams require joining expensive coaching mafias", "Never neglect physical fitness and sports if aiming for the armed forces"],
        "Women cannot join the combat wings of the Indian Armed Forces or appear for the NDA exam.", "myth", "Following landmark Supreme Court rulings, women cadets now train at NDA and serve as combat officers across Army, Navy, and Air Force.",
        "When can students appear for the National Defence Academy (NDA) entrance examination?",
        ["Only after Master's degree", "While appearing in Class 12 or immediately after passing Class 12", "At age 30", "In Class 8"], 1,
        "The NDA exam is conducted twice yearly by UPSC for 16.5 to 19.5 year old Class 12 students.",
        ["A student at {at} dreams of wearing the uniform and serving the nation in the Armed Forces."],
        "What roadmap should {name} outline?",
        [("Prepare for the NDA entrance examination (Mathematics and General Ability) during Class 12", "Timely entrance exam milestone.", True, "nda entrance exam|upsc nda|class 12|maths and gat", 45),
         ("Maintain rigorous physical conditioning and prepare for the 5-day SSB interview process", "Crucial holistic selection matrix.", True, "physical fitness|ssb interview|officer qualities", 35),
         ("Note that both young women and men are eligible for officer commissions via NDA", "Highlights gender-inclusive defence pathways.", False, "open to women and men|equal opportunity", 20)],
        ["ignore physical fitness completely", "pay bribes to fake recruiting agents", "assume defence is only for boys"],
        "Union Public Service Commission (UPSC NDA Portal)", "https://upsc.gov.in"
    ))

    # 9. CAR-029: Agritech
    cards.append(make_card(
        "CAR-029", "compass", "Agritech", "Modern Agriculture: Agritech, soil science and smart farming",
        ["senior"],
        ["Modern agriculture merges satellite data, drone spraying, genetic crop breeding, and supply-chain logistics.",
         "ICAR oversees agricultural universities offering B.Sc. (Hons) Agriculture and Food Technology."],
        ["Explore agricultural entrance exams: ICAR AIEEA for national agricultural university admissions", "Study subjects like plant genetics, hydroponics, precision drip irrigation, and post-harvest preservation", "Look into entrepreneurship opportunities: organic export, agritech startups, and cold-storage supply chains"],
        ["Never view farming through outdated lenses; modern agriculture is a high-tech multibillion-dollar industry", "Never assume agricultural science has no global corporate career avenues"],
        "A degree in Agriculture only prepares students to do manual ploughing in fields.", "myth", "Agricultural graduates work as agronomists, drone specialists, commodity analysts, and food processing scientists.",
        "Which premier national body coordinates agricultural education and research across Indian universities?",
        ["Medical Council", "Indian Council of Agricultural Research (ICAR)", "CBSE", "SEBI"], 1,
        "ICAR is the apex national body coordinating agricultural research and higher education.",
        ["A student from a farming family at {at} wants to modernize their family's agriculture."],
        "How can {name} guide their higher education pathway?",
        [("Explore B.Sc. (Hons) Agriculture or Agricultural Engineering through ICAR AIEEA entrance exams", "Formal professional agriscience degree.", True, "b.sc agriculture|icar|agritech|agricultural engineering", 45),
         ("Highlight exciting modern domains: precision drone farming, soil chemistry, hydroponics, and seed biotech", "Opens tech-driven agriculture horizon.", True, "drone farming|hydroponics|soil science|biotech", 35),
         ("Discuss agritech entrepreneurship: direct farm-to-consumer supply chains and export markets", "Fosters rural wealth creation.", False, "agritech startups|supply chain|entrepreneurship", 20)],
        ["mock farming backgrounds", "tell them to abandon agriculture entirely", "claim agriculture has no future"],
        "Indian Council of Agricultural Research (ICAR)", "https://icar.org.in"
    ))

    # 10. CAR-030: Sports careers
    cards.append(make_card(
        "CAR-030", "compass", "Sports", "Careers in Sports: Athletes, coaching, physiotherapy and sports management",
        ["junior", "middle", "senior"],
        ["The sports industry has exploded beyond professional athletes to sports science, analytics, and leagues.",
         "Sports science professionals support athletes with biomechanics, nutrition, and injury rehabilitation."],
        ["Pursue specialized degrees: B.Sc. Sports Science, Sports Physiotherapy, or Sports Management", "Look into coaching diplomas from the National Institute of Sports (NIS Patiala / SAI)", "Gain experience with sports journalism, event management, and sports video analytics"],
        ["Never assume that if you don't become a national cricket player, you cannot work in sports", "Never neglect academic qualifications while training in competitive athletics"],
        "If you don't play for Team India, there are zero jobs available in the sports sector.", "myth", "IPL teams, academies, and brands employ thousands of sports physios, performance analysts, and league managers.",
        "Which premier institute under the Sports Authority of India (SAI) trains certified sports coaches?",
        ["IIT Delhi", "Netaji Subhas National Institute of Sports (NIS Patiala)", "AIIMS", "IIM Ahmedabad"], 1,
        "NIS Patiala is Asia's largest sports institute, producing India's top certified Olympic and national coaches.",
        ["A student at {at} loves sports deeply but knows making the national team is statistically challenging."],
        "What diverse sports industry careers can {name} introduce?",
        [("Explore high-demand allied fields: Sports Physiotherapy, Sports Nutrition, and Strength & Conditioning", "Leverages athletic passion with medical science.", True, "sports physiotherapy|sports science|nutrition|coaching", 45),
         ("Look into modern business avenues: Sports Management, Tournament Operations, and Sports Analytics", "Massive growth in league operations.", True, "sports management|analytics|league operations", 35),
         ("Check degree programs under the Sports Authority of India and sports universities", "Legitimate academic degrees.", False, "sports authority of india|sai|nis patiala", 20)],
        ["say sports is a waste of life", "claim only cricket exists", "tell them to give up sports"],
        "Sports Authority of India (SAI)", "https://sportsauthorityofindia.nic.in"
    ))

    # 11. CAR-031: Media & Journalism
    cards.append(make_card(
        "CAR-031", "compass", "Media", "Day in the life: Journalist, content creator and documentary filmmaker",
        ["senior"],
        ["Journalism is the 'Fourth Pillar' of democracy, holding power accountable and informing citizens.",
         "Modern media blends investigative writing, podcasting, data journalism, and video editing."],
        ["Cultivate voracious reading habits, ethical fact-checking, and strong written storytelling", "Pursue degrees in Journalism, Mass Communication, or Film Studies (IIMC, Jamia, FTII)", "Start writing articles for school magazines, local newsletters, or producing audio-video mini-documentaries"],
        ["Never report unverified WhatsApp forwards or sensational rumors as news", "Never compromise on journalistic truth and neutral verification for cheap viral clicks"],
        "Journalism is just screaming loudly on sensational television debate panels.", "myth", "True journalism is deep investigative research, ground reporting, and presenting verified facts calmly.",
        "What premier national institute under the Ministry of I&B trains elite journalists in India?",
        ["NIFT", "Indian Institute of Mass Communication (IIMC)", "National Law School", "IIT Bombay"], 1,
        "IIMC is India's premier government institution for post-graduate mass communication and journalism.",
        ["A student at {at} loves writing, questioning community issues, and making documentary videos."],
        "How should {name} structure their media and journalism exploration?",
        [("Build strong writing and critical fact-checking habits across school publications and blogs", "Creates demonstrable writing portfolio.", True, "fact checking|writing portfolio|school magazine|blog", 45),
         ("Explore degree programs in Mass Communication, Media Studies, and Film Making (e.g. IIMC)", "Formal journalistic education credentials.", True, "mass communication|iimc|journalism degree", 35),
         ("Emphasize ethical responsibility: fighting fake news, verifying sources, and speaking truth", "Instills core Fourth Estate ethics.", False, "ethics|fight fake news|verify sources", 20)],
        ["teach them to make fake news", "say journalism is dead", "encourage clickbait gossip"],
        "Indian Institute of Mass Communication (IIMC)", "https://iimc.gov.in"
    ))

    # 12. CAR-032: Scholarships
    cards.append(make_card(
        "CAR-032", "compass", "Scholarships", "National scholarship portals: Legitimate schemes vs fake fee scams",
        ["junior", "middle", "senior"],
        ["Government and institutional scholarships fund school and university fees for deserving students.",
         "Legitimate scholarship schemes NEVER charge application fees or ask for processing deposits."],
        ["Apply for government scholarships exclusively through the official National Scholarship Portal (scholarships.gov.in)", "Explore central and state merit-cum-means schemes, PM-YASASVI, and NMMS for school students", "Keep verified documents ready: Aadhaar, income certificate, school bonafide, and student bank passbook"],
        ["Never pay money to private agents claiming to 'guarantee' a scholarship approval", "Never share OTPs or banking PINs with unverified scholarship websites"],
        "If a scholarship portal asks for a ₹500 'verification processing fee', it is a standard government requirement.", "myth", "Official Indian government scholarships are 100% free. Any site asking for payment is a cyber scam.",
        "What is the single official central government web portal for all Indian student scholarships?",
        ["scholarship-free-money.xyz", "National Scholarship Portal (scholarships.gov.in)", "cash-grant.net", "lottery.com"], 1,
        "The National Scholarship Portal (NSP) is the unified government window for central and state schemes.",
        ["A student's family at {at} wants financial assistance for higher schooling but worries about fake scams."],
        "How can {name} guide them safely?",
        [("Direct them strictly to the official National Scholarship Portal (scholarships.gov.in)", "Authentic government portal with direct bank benefit transfer.", True, "scholarships.gov.in|national scholarship portal|official scheme", 45),
         ("Warn them that legitimate government scholarships NEVER charge any application fee", "Shields family from scam agents.", True, "never pay fees|free application|no scam agents", 35),
         ("Help them assemble authentic documents: income certificate, marksheet, and Aadhaar-linked account", "Prepares application readiness.", False, "documents ready|aadhaar linked|bonafide", 20)],
        ["pay ₹1,000 to internet cafe agent", "apply on random telegram link", "share bank netbanking password"],
        "National Scholarship Portal (Ministry of Electronics and IT)", "https://scholarships.gov.in"
    ))

    # 13. CAR-033: Vocational skilling
    cards.append(make_card(
        "CAR-033", "compass", "Vocational", "Vocational skilling: ITI, polytechnic diplomas and practical trades",
        ["middle", "senior"],
        ["Skill-based technical trades (electrician, CNC machinist, solar technician) offer high employability.",
         "Polytechnic diplomas allow direct lateral entry into the 2nd year of B.Tech engineering degrees."],
        ["Explore Industrial Training Institutes (ITIs) and Polytechnic Diplomas after Class 10", "Gain hands-on practical skills aligned with the National Skills Qualification Framework (NSQF)", "Look into emerging vocational trades: drone pilot licensing, EV mechanic, and renewable tech installation"],
        ["Never look down upon vocational technical education compared to traditional general degrees", "Never enroll in uncertified private training institutes without DGT / NCVT affiliation"],
        "Students who attend ITI or Polytechnic institutes cannot go to college or get high-paying jobs.", "myth", "Skilled technicians earn excellent salaries, launch manufacturing businesses, or take lateral entry into engineering degrees.",
        "What official government certification ensures an ITI trade course is nationally recognized?",
        ["A printed card", "National Council for Vocational Training (NCVT / DGT) certification", "A local shop stamp", "None"], 1,
        "NCVT certification ensures trade qualifications are recognized by government and multinational industries.",
        ["A Class 10 student at {at} prefers hands-on mechanical building over memorizing abstract textbooks."],
        "How can {name} present vocational education proudly?",
        [("Explain that Polytechnic Diplomas and ITIs provide rapid, high-demand practical technical skills", "Validates practical hands-on learning.", True, "polytechnic diploma|iti|technical skills|hands-on", 45),
         ("Highlight the lateral entry pathway: diploma graduates can enter 2nd year B.Tech directly", "Demonstrates upward academic mobility.", True, "lateral entry b.tech|degree pathways|mobility", 35),
         ("Emphasize high-growth future trades like Electric Vehicle (EV) maintenance and solar installation", "Connects to emerging industry demand.", False, "ev technician|solar energy|nsqf", 20)],
        ["mock vocational education", "say only doctors succeed", "force into unwanted rote learning"],
        "Directorate General of Training (DGT - Ministry of Skill Development)", "https://dgt.gov.in"
    ))

    # 14. CAR-034: High school projects
    cards.append(make_card(
        "CAR-034", "compass", "Extracurriculars", "Building a real profile: Projects, volunteering and student initiatives",
        ["middle", "senior"],
        ["Colleges, scholarship committees, and employers look for initiative, grit, and real-world impact.",
         "Building a working prototype or leading a community literacy drive outshines empty test scores."],
        ["Initiate or join school clubs: coding club, eco-club, robotics, debate society, or literary circle", "Volunteer for verified community causes: teaching younger kids, animal shelter care, or park cleanups", "Document your projects in a simple portfolio or blog showing what you learned and solved"],
        ["Never participate in activities just to collect fake participation certificates", "Never plagiarize someone else's project work and claim it as your own"],
        "Only students with 99% board marks get selected for top university scholarships and internships.", "myth", "Top universities practice holistic review, prioritizing student leadership, curiosity, and tangible projects.",
        "What makes a student project stand out on a college scholarship application?",
        ["Using gold glitter", "Solving a genuine community problem with documented effort, reflection, and impact", "Buying a readymade project online", "Copying Wikipedia"], 1,
        "Authentic problem-solving demonstrates maturity, leadership, and intellectual curiosity.",
        ["A Class 11 student at {at} wants to build an impressive profile for future college applications."],
        "What impactful roadmap should {name} recommend?",
        [("Pick a genuine real-world problem and build a mini-project (e.g. school compost bin, app, or reading drive)", "Shows initiative and tangible execution.", True, "real world project|initiative|community impact|portfolio", 45),
         ("Lead school club activities or volunteer with local verified community groups", "Demonstrates teamwork and leadership.", True, "volunteer|school clubs|leadership|teamwork", 35),
         ("Reflect on learning and document the journey honestly in a student portfolio", "Communicates personal growth authentically.", False, "document journey|portfolio|reflection", 20)],
        ["buy fake certificates online", "plagiarize projects", "focus solely on memorization"],
        "National Youth Policy (Ministry of Youth Affairs and Sports)", "https://yas.nic.in"
    ))

    # 15. CAR-035: Fake colleges
    cards.append(make_card(
        "CAR-035", "compass", "Accreditation", "Spotting fake colleges, unaccredited degrees and fraudulent agents",
        ["senior"],
        ["Enrolling in an unrecognized institution results in worthless degrees ineligible for jobs or government exams.",
         "The University Grants Commission (UGC) and AICTE publish yearly public lists of fake and unaccredited universities."],
        ["Check university accreditation status on the official UGC website (ugc.ac.in) before applying", "Verify technical and engineering college approvals on the AICTE portal (aicte-india.org)", "Beware of glossy brochures promising '100% Guaranteed Foreign Placement' with zero entrance requirements"],
        ["Never pay non-refundable admissions fees to unregistered educational consultancies or agents", "Never take admission in an institute listed on the UGC Fake University Warning List"],
        "If a college has a fancy multi-story glass building and celebrity ads, its degrees are automatically recognized.", "myth", "Physical architecture does not equal legal accreditation. Always verify statutory UGC/AICTE approval.",
        "Which statutory government body maintains the official public list of recognized universities and fake colleges in India?",
        ["Department of Transport", "University Grants Commission (UGC)", "Postal Service", "Tourism Board"], 1,
        "UGC is the statutory authority maintaining the official list of recognized central, state, and private universities.",
        ["A glossy brochure at {at} promises: 'Instant B.Tech Degree in 1 year, no exams needed, apply now!'"],
        "What critical red flags does {name} point out?",
        [("B.Tech degrees cannot be completed in 1 year; this is a fraudulent fake degree scam", "Recognizes impossible academic claims.", True, "fraudulent fake college|impossible claims|scam degree", 45),
         ("Check the institution's legal approval status on the official UGC and AICTE websites", "Verifies formal statutory accreditation.", True, "check ugc list|aicte approval|verify college", 35),
         ("Warn peers never to pay money to unaccredited institutions that sell worthless certificates", "Shields peers from financial and career loss.", False, "warn peers|worthless certificate|no jobs", 20)],
        ["pay the fee for instant degree", "believe fake promises blindly", "ignore ugc warnings"],
        "University Grants Commission (UGC List of Fake Universities)", "https://ugc.ac.in"
    ))

    # 16. CAR-036: Changing streams
    cards.append(make_card(
        "CAR-036", "compass", "Flexibility", "Stream pressure and changing pathways: It is okay to pivot",
        ["senior"],
        ["Many students realize their selected Class 11 stream (Science/Commerce/Arts) does not align with their passions.",
         "The National Education Policy (NEP 2020) encourages multidisciplinary flexibility across subjects."],
        ["Recognize that discovering what you DO NOT like is valuable progress toward finding your true calling", "Consult a certified school career counselor to assess transferable skills and bridge courses", "Remember that undergraduate admissions (law, design, management, humanities) are open to all streams"],
        ["Never consider yourself a failure because a chosen stream feels unfulfilling", "Never suffer in severe silent misery without speaking to parents and counselors"],
        "If you choose Science in Class 11, you must become an engineer or your life is over.", "myth", "Thousands of science students pivot successfully to design, law, management, writing, civil services, and entrepreneurship.",
        "What does the National Education Policy (NEP) promote regarding secondary education streams?",
        ["Strict separation forever", "Multidisciplinary flexibility, eliminating rigid boundaries between arts and sciences", "Closing colleges", "Single subject only"], 1,
        "NEP promotes cross-disciplinary learning, allowing students to study physics with music or economics with history.",
        ["A Class 12 student at {at} feels completely exhausted by engineering coaching and dreams of business and design."],
        "What reassuring guidance should {name} provide?",
        [("Assure them that changing career directions is normal, common, and completely okay", "Relieves psychological burnout and guilt.", True, "it'?s okay to change|normal to pivot|no failure", 45),
         ("Explain that entrance exams for design (UCEED), law (CLAT), and management are open to all streams", "Shows viable alternative pathways.", True, "open to all streams|clat|design|business|cuet", 35),
         ("Encourage an honest, constructive dialogue with family about their true strengths and goals", "Facilitates supportive family resolution.", False, "talk to parents|career counselor|strengths", 20)],
        ["tell them they are a failure", "force them to suffer in silence", "give up on higher education"],
        "National Education Policy (NEP 2020)", "https://dsel.education.gov.in"
    ))

    # 17. CAR-037: Career talks with parents
    cards.append(make_card(
        "CAR-037", "compass", "Family dialogue", "Constructive career conversations with parents",
        ["senior"],
        ["Parents worry primarily about their children's future financial security, career stability, and happiness.",
         "Presenting well-researched career pathways, college options, and job outlooks dispels parental anxiety."],
        ["Prepare for the conversation: research top accredited colleges, admission criteria, and alumni career outcomes", "Acknowledge their concern: 'I know you want me to be secure, here is how this field offers real careers'", "Schedule a calm, dedicated discussion time without angry shouting or defensive arguments"],
        ["Never scream: 'You are ruining my life!' during a heated argument", "Never demand approval for an unconventional career without having done basic research on it"],
        "Parents who suggest traditional engineering or medicine only want to control and punish their children.", "myth", "Parents recommend traditional paths because they represent proven financial stability in their experience.",
        "What is the most persuasive way to present an unconventional career goal (like animation or sports) to parents?",
        ["Slamming the door", "Presenting a clear, researched plan showing accredited colleges, realistic costs, and career opportunities", "Refusing to eat dinner", "Ignoring them"], 1,
        "Preparation and researched facts demonstrate maturity, turning parental anxiety into proud support.",
        ["A student at {at} wants to pursue Psychology or Culinary Arts, but parents insist on engineering coaching."],
        "How should {name} structure a mature family conversation?",
        [("Prepare a structured presentation showing top universities, curriculum, and diverse job roles", "Substitutes vague dreams with concrete research.", True, "research plan|top colleges|career outlook|presentation", 45),
         ("Acknowledge parental love and financial security concerns with respect and empathy", "Validates emotional motivation of parents.", True, "respect concerns|calm conversation|empathy", 35),
         ("Invite a school career counselor or neutral industry professional to join the discussion", "Provides trusted external expert perspective.", False, "counselor|neutral expert|family discussion", 20)],
        ["scream and throw tantrums", "secretly drop out of school", "mock parents' knowledge"],
        "CBSE Career Guidance Guidelines", "https://cbse.gov.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Compass")
    return cards
