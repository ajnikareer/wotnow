"""
Basil (Nutrition) and Civic (Civic Sense) expanded skills.
Provides 16 verified, realistic skills for each agent.
"""
from cards_existing import make_card

def get_basil_cards():
    cards = []

    # 1. NUT-021: Skipping breakfast
    cards.append(make_card(
        "NUT-021", "basil", "Breakfast", "Skipping breakfast impact and quick healthy fuel",
        ["junior", "middle", "senior"],
        ["Skipping breakfast leaves blood glucose depleted after a 10-hour nocturnal fast.",
         "Students who eat breakfast demonstrate higher memory retention and classroom focus."],
        ["Eat a balanced morning meal containing complex carbs and protein (poha, idli, eggs, or oatmeal)", "Keep easy backup options ready: a banana, handful of roasted chana, or a boiled egg", "Hydrate with a glass of water before leaving home"],
        ["Never replace breakfast with sugary sodas or packaged cream biscuits", "Never attend morning exams on an empty stomach"],
        "Skipping breakfast helps students stay lean and active.", "myth", "Skipping breakfast crashes morning metabolism and causes intense overeating of junk later.",
        "Why does eating breakfast improve school exam performance?",
        ["It makes you sleepy", "It replenishes brain glucose needed for memory, focus, and quick thinking", "It takes up time", "It has no effect"], 1,
        "Glucose from wholesome breakfast feeds the brain for alert cognitive performance.",
        ["Running late for school at {at}, {name} wants to rush out without eating any breakfast."],
        "What should {name} do for quick morning brain fuel?",
        [("Grab a quick healthy item like a banana, milk, or roasted chana", "Provides instant glucose and protein.", True, "banana|boiled egg|milk|chana|quick food", 45),
         ("Do not skip breakfast entirely before school hours", "Prevents mid-morning fatigue and headaches.", True, "don'?t skip|eat something|morning fuel", 35),
         ("Drink a glass of water before heading out", "Ensures morning hydration.", False, "water|hydrate", 20)],
        ["eat nothing", "grab sugary cola", "skip food until lunch"],
        "National Institute of Nutrition (ICMR-NIN)", "https://www.nin.res.in"
    ))

    # 2. NUT-022: Hidden sugars
    cards.append(make_card(
        "NUT-022", "basil", "Sugar", "Spotting hidden sugars in malt and 'health' drinks",
        ["junior", "middle", "senior"],
        ["Many popular 'brown malt drinks' contain over 50% sugar by weight (sucrose, maltodextrin).",
         "The WHO recommends keeping free sugars below 25 grams (about 5-6 teaspoons) per day."],
        ["Read the nutrition label: ingredients are listed in descending order by weight", "Look for alias names for sugar: sucrose, liquid glucose, maltodextrin, high-fructose syrup", "Enjoy plain milk or flavour with fresh cardamom, cinnamon, or cocoa powder instead"],
        ["Never believe front-of-pack claims like 'Energy Booster' without checking sugar grams", "Never add multiple scoops of sugar to already-sweetened malt powders"],
        "Commercial chocolate malt powders are rich protein supplements for growing kids.", "myth", "Most commercial malt mixes are primarily refined sugars and malt extract with minimal protein.",
        "If 'Sugar' is the first or second ingredient on a food label, what does that mean?",
        ["It has no sugar", "Sugar makes up the largest proportion of that product", "It is very healthy", "It is organic"], 1,
        "Ingredients must be listed in order of weight, from highest to lowest.",
        ["In the supermarket at {at}, {name} looks at a health drink powder claiming 'Immunity & Growth'."],
        "How can {name} verify what is really inside?",
        [("Turn to the back panel and check the Ingredients list", "Reveals real composition and order of ingredients.", True, "ingredients list|back panel|label|check grams", 45),
         ("Check grams of added sugar per 100g serving", "Identifies hidden sucrose and maltodextrin.", True, "sugar grams|added sugar|maltodextrin", 35),
         ("Do not rely solely on bold front-of-pack marketing claims", "Separates marketing from nutritional reality.", False, "don'?t trust claims|front of pack", 20)],
        ["buy based on cartoon actor", "assume healthy without checking", "ignore ingredients"],
        "Food Safety and Standards Authority of India (FSSAI)", "https://fssai.gov.in"
    ))

    # 3. NUT-023: Junk food ads
    cards.append(make_card(
        "NUT-023", "basil", "Media literacy", "Deconstruct junk food and fast food advertisements",
        ["middle", "senior"],
        ["Food marketers use vibrant cartoon mascots, gaming partnerships, and free toys to target youth.",
         "Ultra-processed foods are engineered to hit a 'bliss point' of sugar, salt, and fat that bypasses fullness."],
        ["Ask: 'What ingredients are they hiding behind this flashy celebration ad?'", "Check the actual nutritional table rather than celebrity endorsement slogans", "Understand that processed snacks are occasional treats, not everyday meal substitutes"],
        ["Never assume a snack is healthy just because a famous cricketer endorses it", "Never replace fresh home-cooked meals with packaged snacks"],
        "Sports stars eat the exact packaged chips and soda they advertise on TV.", "myth", "Professional athletes follow strict whole-food nutrition and rarely consume the ultra-processed products they endorse.",
        "Why do junk food commercials feature energetic gaming and pop music?",
        ["To teach cooking", "To associate processed snacks with fun and coolness, bypassing nutrition scrutiny", "To help you study", "To save money"], 1,
        "Marketing targets emotions so consumers overlook high saturated fat and sodium levels.",
        ["A viral TV ad at {at} claims a new crispy chip brand gives you 'Super Energy for Gaming'."],
        "How should {name} critically evaluate this claim?",
        [("Recognize that the ad uses gaming themes to sell ultra-processed carbs", "Deconstructs manipulative advertising techniques.", True, "marketing trick|gaming themes|ad tactic|evaluate", 40),
         ("Check the nutrition label for sodium, trans fat, and refined palm oil", "Reveals real nutritional drawbacks.", True, "check label|sodium|palm oil|trans fat", 40),
         ("Treat chips as an occasional snack, not everyday study fuel", "Balanced relationship with treats.", False, "occasional|treat|not daily fuel", 20)],
        ["believe chips give superpowers", "eat bags daily", "replace dinner with chips"],
        "Consumer Protection (Misleading Advertisements) Rules", "https://consumeraffairs.nic.in"
    ))

    # 4. NUT-024: Sodium & noodles
    cards.append(make_card(
        "NUT-024", "basil", "Sodium", "Sodium and salt in instant noodles and packaged snacks",
        ["junior", "middle", "senior"],
        ["A single packet of instant noodles often contains 70% to 100% of a student's daily sodium limit.",
         "Excess sodium increases blood pressure, strains kidneys, and causes dehydration."],
        ["Check sodium mg on the label; ideal daily intake is under 2,000 mg (about 1 teaspoon of salt)", "Use half the tastemaker seasoning packet and add boiled peas, carrots, or egg for balance", "Enjoy instant noodles occasionally rather than as a daily after-school habit"],
        ["Never drink all the leftover salty noodle broth", "Never add extra table salt to pre-seasoned chips and noodles"],
        "Instant noodles are just wheat flour and can be eaten daily for lunch.", "myth", "Fried noodles are laden with palm oil, and seasoning packets are concentrated sodium bombs.",
        "How much of your total daily sodium allowance can be in one packet of instant noodles?",
        ["Almost zero", "Up to 70-100% of your entire recommended daily limit", "5 percent", "Only 1 mg"], 1,
        "One tastemaker sachet can exceed the recommended sodium intake for an entire day.",
        ["Craving an after-school snack at {at}, {name} prepares a packet of instant noodles."],
        "How can {name} make this snack healthier and lower in sodium?",
        [("Use half the tastemaker spice packet to cut salt in half", "Significantly reduces sodium overload.", True, "half tastemaker|less spice packet|less salt", 45),
         ("Toss in fresh vegetables (carrots, peas, spinach) or a boiled egg", "Adds dietary fiber, vitamins, and protein.", True, "add vegetables|egg|peas|carrots|fiber", 35),
         ("Do not drink the remaining salty soup broth", "Avoids consuming dissolved sodium residue.", False, "don'?t drink broth|leave soup", 20)],
        ["add extra salt", "eat 3 packets daily", "drink all salty broth"],
        "ICMR Dietary Guidelines for Indians", "https://www.nin.res.in"
    ))

    # 5. NUT-025: Seasonal fruits
    cards.append(make_card(
        "NUT-025", "basil", "Produce", "Eating local and seasonal fruits and vegetables",
        ["junior", "middle", "senior"],
        ["Seasonal produce ripens naturally on plants, yielding maximum vitamin C and antioxidant levels.",
         "Out-of-season produce is kept in cold storage for months and often treated with artificial ripening agents."],
        ["Eat seasonal fruits: mangoes/watermelons in summer; guavas/oranges in winter; papayas/bananas year-round", "Choose local Indian fruits like amla, ber, jamun, and pomegranate for affordable rich nutrition", "Wash all fruits thoroughly under running water before peeling or eating"],
        ["Never choose expensive imported apples over fresh local seasonal fruits", "Never skip washing fruits before eating"],
        "Imported fruits with foreign stickers are much healthier than local Indian fruits.", "myth", "Local Indian fruits like amla and guava contain 5 times more Vitamin C than imported apples.",
        "Why is eating an amla (Indian gooseberry) or guava better than an expensive imported kiwi?",
        ["They have more seeds", "Local amla and guava pack far higher Vitamin C at a fraction of the cost and carbon footprint", "They look bigger", "They have stickers"], 1,
        "Amla is one of nature's richest sources of Vitamin C, costing very little.",
        ["Shopping for fruit with family at {at}, {name} sees costly imported berries alongside fresh local guavas."],
        "Why is picking the local seasonal fruit the smarter choice?",
        [("Seasonal local guavas are fresher and richer in Vitamin C and fiber", "Higher nutritional density.", True, "guava|vitamin c|fresher|seasonal|local", 45),
         ("Local produce supports nearby farmers and requires minimal transport emissions", "Eco-friendly and sustainable.", False, "local farmers|environment|lower cost", 25),
         ("Wash thoroughly with water before eating", "Removes surface dust and handling residue.", True, "wash with water|clean fruit", 30)],
        ["buy imported only for stickers", "never wash fruit", "avoid local fruits"],
        "Ministry of Agriculture & Farmers Welfare", "https://agricoop.nic.in"
    ))

    # 6. NUT-026: Plant protein
    cards.append(make_card(
        "NUT-026", "basil", "Protein", "Powerhouse plant protein: Dal, sprouts, paneer and chana",
        ["junior", "middle", "senior"],
        ["Proteins are the building blocks needed for muscle growth, tissue repair, and immune antibodies.",
         "Combining grains and legumes (like rice + dal or roti + rajma) forms a complete amino acid profile."],
        ["Include a protein source in every meal: dal, chana, rajma, paneer, tofu, sprouts, or eggs", "Sprout moong or chana at home to double their vitamin and digestive enzyme content", "Snack on roasted peanuts or chana instead of fried potato chips"],
        ["Never rely solely on plain rice or bread without any lentils or legumes", "Never take unverified gym protein powders without medical advice"],
        "Vegetarian diets cannot provide enough protein for growing school athletes.", "myth", "Combining lentils, dairy, nuts, seeds, and sprouts provides abundant, high-quality complete protein.",
        "What happens when you combine rice with dal or roti with rajma?",
        ["They cancel each other out", "Their amino acids complement each other to form complete, high-quality protein", "It makes you fat", "It has zero protein"], 1,
        "Grain + pulse combinations provide all nine essential amino acids.",
        ["{name}'s school lunchbox at {at} contains only plain butter noodles."],
        "How can {name} upgrade this meal to build strong muscles?",
        [("Add protein like paneer cubes, boiled eggs, tofu, or sprouts", "Provides essential amino acids for growth.", True, "paneer|egg|sprouts|dal|chana|protein", 45),
         ("Understand that protein keeps you satiated and alert through the afternoon", "Prevents 2 PM classroom slumps.", True, "fullness|energy|muscle repair", 35),
         ("Snack on a small cup of roasted peanuts or moong sprouts", "Wholesome natural protein snack.", False, "peanuts|sprouts|roasted chana", 20)],
        ["eat only plain carb noodles", "take bodybuilding supplements", "skip protein entirely"],
        "ICMR National Institute of Nutrition", "https://www.nin.res.in"
    ))

    # 7. NUT-027: Iron & Vitamin C
    cards.append(make_card(
        "NUT-027", "basil", "Iron", "Beating anemia: Iron-rich foods paired with Vitamin C",
        ["junior", "middle", "senior"],
        ["Over 50% of Indian schoolchildren and teenagers have mild iron-deficiency anemia.",
         "Vitamin C dramatically enhances the absorption of non-heme plant iron in the gut."],
        ["Eat iron-rich foods: palak (spinach), methi, beetroot, lentils, and jaggery in moderation", "Squeeze fresh lemon juice over your dal and vegetables to boost iron uptake with Vitamin C", "Cook in traditional cast-iron pans to naturally leach safe dietary iron into curries"],
        ["Never drink hot tea or coffee with meals (tannins block iron absorption)", "Never ignore persistent symptoms of unusual fatigue, pale nails, and dizziness"],
        "Drinking a cup of chai right after eating dal and roti is good for digestion.", "myth", "Chai tannins bind with dietary iron in your stomach, completely blocking its absorption.",
        "What should you squeeze onto your dal to help your body absorb plant iron?",
        ["Warm milk", "Fresh lemon juice (rich in Vitamin C)", "Salty sauce", "Vinegar"], 1,
        "Vitamin C converts plant iron into a chemical form easily absorbed by intestinal walls.",
        ["During lunch at {at}, {name} notices palak dal on the table."],
        "How can {name} maximize iron absorption from this green leafy meal?",
        [("Squeeze fresh lemon juice directly over the spinach dal", "Vitamin C triples plant iron absorption.", True, "lemon juice|vitamin c|citrus", 45),
         ("Avoid drinking tea or caffeinated beverages right after the meal", "Prevents tannins from binding iron.", True, "no tea|no coffee|avoid chai with food", 35),
         ("Include iron-rich foods regularly to prevent fatigue and anemia", "Keeps red blood cell hemoglobin high.", False, "iron rich|prevent anemia|energy", 20)],
        ["drink chai with meal", "throw away greens", "eat without vitamin c"],
        "Anemia Mukt Bharat Guidelines (MoHFW)", "https://anemiamuktibharat.info"
    ))

    # 8. NUT-028: Food allergies
    cards.append(make_card(
        "NUT-028", "basil", "Allergies", "Food allergies in friends and lunchbox etiquette",
        ["junior", "middle", "senior"],
        ["Severe food allergies (nuts, eggs, dairy, shellfish) can trigger life-threatening anaphylaxis in minutes.",
         "Even microscopic crumbs on shared spoons or lunchbox lids can induce an allergic reaction."],
        ["Always ask: 'Does anyone have food allergies?' before sharing homemade snacks", "Never pressure friends to taste unfamiliar dishes if they express hesitation", "Call a teacher and school nurse immediately if a friend experiences hives, lip swelling, or breathing difficulty"],
        ["Never tease or hide allergen ingredients in a friend's lunch as a prank", "Never force a child with allergies to eat shared treats"],
        "If someone is allergic to peanuts, eating a tiny crumb will not hurt them.", "myth", "Microscopic allergen traces can trigger severe airway constriction in sensitive individuals.",
        "A friend at your lunch table says they have a severe peanut allergy. What is the respectful rule?",
        ["Force them to try peanut chikki", "Never share peanut snacks and wash hands after eating", "Tell them it's in their mind", "Hide peanuts in sandwich"], 1,
        "Food allergies are serious medical conditions. Respect dietary boundaries completely.",
        ["At lunchtime at {at}, {name} opens a box of peanut brittle (chikki) beside a classmate who has a peanut allergy."],
        "What is the considerate, safe lunch etiquette for {name}?",
        [("Ask if having peanuts nearby is safe or eat at a considerate distance", "Prevents accidental airborne or surface contamination.", True, "ask friend|keep distance|don'?t share peanut", 45),
         ("Do not share utensils, spoons, or lunchboxes with the allergic friend", "Avoids allergen cross-contact.", True, "don'?t share spoon|no cross contamination", 35),
         ("Know the symptoms of allergic reaction (facial swelling, hives, wheezing)", "Enables instant emergency alert.", False, "allergic signs|swelling|tell teacher", 20)],
        ["prank friend with peanut", "force friend to taste", "laugh at allergy"],
        "Food Allergy India Network", "https://allergyfreeindia.org"
    ))

    # 9. NUT-029: Exam nutrition
    cards.append(make_card(
        "NUT-029", "basil", "Exam fuel", "Exam season brain fuel: Hydration, light meals and energy drinks",
        ["junior", "middle", "senior"],
        ["Dehydration of just 2% significantly reduces mathematical calculation speed and attention span.",
         "High-sugar energy drinks cause a sharp insulin spike followed by an exhausting brain crash."],
        ["Drink plain water, coconut water, or buttermilk regularly while studying", "Eat light, frequent meals (fruits, nuts, curd, dal-chawal) to maintain steady glucose", "Avoid heavy, oily deep-fried parathas or bhaturas right before morning exams"],
        ["Never consume high-caffeine energy cans to pull all-nighters", "Never skip water during long study sessions"],
        "Canned energy drinks sharpen student memory for board exams.", "myth", "Energy drinks cause heart palpitations, severe anxiety jitters, and a steep cognitive energy crash.",
        "What drink provides the steadiest brain focus without causing jittery crashes during exam week?",
        ["Commercial energy drink can", "Plain water, chaas (buttermilk) or coconut water", "Three sugary sodas", "Black coffee with extra sugar"], 1,
        "Hydration with clean water and electrolytes sustains cerebral circulation without spikes.",
        ["Studying for important exams at {at}, {name} feels drowsy and considers buying a canned energy drink."],
        "What is the wiser, scientifically sound brain-fuel choice?",
        [("Drink a glass of water, splash face with cool water, and take a 5-minute stretch break", "Restores oxygen delivery to brain naturally.", True, "drink water|stretch break|hydrate|wash face", 40),
         ("Avoid high-caffeine energy drinks that trigger anxiety and crashes", "Protects heart rhythm and focus.", True, "no energy drinks|avoid caffeine cans|no soda", 35),
         ("Snack on a handful of almonds, walnuts, or an apple for clean energy", "Supplies steady glucose and omega-3s.", False, "nuts|apple|fruit|wholesome snack", 25)],
        ["drink 2 cans energy drink", "skip water all day", "pull all nighter with coffee"],
        "NIN Nutrition Advice for Students", "https://www.nin.res.in"
    ))

    # 10. NUT-030: Mindful eating
    cards.append(make_card(
        "NUT-030", "basil", "Mindful eating", "Mindful eating: Chewing slowly and ditching mealtime screens",
        ["junior", "middle", "senior"],
        ["It takes approximately 20 minutes for stomach satiety hormones (leptin) to signal fullness to the brain.",
         "Eating while watching YouTube or TV distracts the brain, leading to subconscious 30% overeating."],
        ["Put phones and tablets away and switch off the television during meals", "Chew each bite thoroughly to help saliva enzymes kickstart carbohydrate digestion", "Pause halfway through your plate and check: 'Am I still genuinely hungry?'"],
        ["Never swallow meals in 3 minutes while glued to a mobile video", "Never force yourself to finish overflowing portions when already comfortably full"],
        "Watching funny reels while eating helps you digest food faster.", "myth", "Screen distraction blocks brain fullness signals, leading to overeating and acid indigestion.",
        "Why does eating while watching videos cause indigestion and unintended weight gain?",
        ["Screens emit cold light", "Distraction prevents the brain from sensing fullness signals, causing unmeasured overeating", "Food gets cold", "It has no effect"], 1,
        "Mindless eating disconnects the brain from biological hunger and fullness cues.",
        ["Sitting down for dinner at {at}, {name} instinctively props a phone against the water glass to watch reels."],
        "How should {name} transform this into a healthy mindful meal?",
        [("Put the phone away and enjoy dinner with family without screens", "Fosters mindful connection and satiety awareness.", True, "put phone away|no screens|turn off tv", 40),
         ("Eat slowly, savoring textures, flavors, and chewing well", "Aids digestive enzyme production.", True, "eat slowly|chew well|savor food", 35),
         ("Listen to your stomach and stop eating when pleasantly satisfied", "Prevents uncomfortable bloating.", False, "listen to body|stop when full|satiety", 25)],
        ["stare at reels while eating", "swallow whole without chewing", "eat until bursting"],
        "Centre for Mindful Eating Guidelines", "https://thecenterformindfuleating.org"
    ))

    # 11. NUT-031: Festival treats
    cards.append(make_card(
        "NUT-031", "basil", "Festivals", "Healthy balance during festival celebrations and feasts",
        ["junior", "middle", "senior"],
        ["Festivals in India bring rich traditional sweets made of ghee, jaggery, milk, and nuts.",
         "Labeling festive foods as 'evil' creates unhealthy guilt; balance and portion awareness work best."],
        ["Enjoy favorite festival sweets mindfully in small portions rather than bingeing", "Prioritize homemade traditional treats over adulterated commercial sweets", "Keep daily water intake high and eat plenty of fresh salad and fruit alongside festive meals"],
        ["Never skip regular meals to 'save room' for a massive binge of sweets", "Never shame yourself or others for enjoying festival foods"],
        "Eating sweets during Diwali or Eid will immediately ruin your health permanently.", "myth", "Traditional festive treats enjoyed in moderate portions as part of celebrations are perfectly healthy.",
        "What is the best way to enjoy festival sweets without feeling sick or sluggish?",
        ["Eat 20 gulab jamuns in one sitting", "Savor 1-2 pieces mindfully, stay hydrated, and balance with wholesome meals", "Fast all day then binge", "Refuse all family foods angrily"], 1,
        "Moderation, hydration, and positive family celebration preserve festive joy and health.",
        ["It's festival day at {at}, and the dining table is filled with laddus, jalebis, and samosas."],
        "How can {name} enjoy the festivities while taking good care of their body?",
        [("Choose favorite traditional treats and enjoy 1 or 2 pieces mindfully", "Prevents sugar overload while partaking in festivities.", True, "moderate portion|savor sweet|enjoy mindfully", 40),
         ("Drink plenty of water and eat regular fiber-rich vegetables", "Prevents sluggishness and dehydration.", True, "drink water|fiber|vegetables|balance", 35),
         ("Do not skip normal meals or feel guilty about enjoying family traditions", "Promotes healthy, guilt-free food relationships.", False, "no guilt|eat normal meals|celebrate", 25)],
        ["binge on sweets all day", "skip lunch completely", "punish yourself for eating"],
        "FSSAI Safe and Nutritious Food at Home", "https://fssai.gov.in"
    ))

    # 12. NUT-032: Street food safety
    cards.append(make_card(
        "NUT-032", "basil", "Street food", "Street food smarts: Hygiene checks and safe snacking",
        ["junior", "middle", "senior"],
        ["Waterborne bacteria (E. coli, Salmonella, Vibrio) cause acute food poisoning and typhoid.",
         "Uncovered cut fruits (papaya, watermelon) on roadside carts attract flies and vehicle exhaust fumes."],
        ["Choose stalls that serve freshly cooked, piping-hot food straight from the tava or kadhai", "Ensure the vendor uses clean RO/filtered water, clean aprons, and covers food containers", "Avoid pre-cut fruit platters or unpasteurized drinks mixed with crushed raw roadside ice"],
        ["Never drink roadside juices made with murky industrial block ice", "Never eat food from stalls with flies buzzing over open ingredients"],
        "Roadside industrial block ice is made from purified RO water.", "myth", "Block ice is often manufactured from unpotable water meant for chemical cooling, carrying typhoid microbes.",
        "What is the safest type of street food to eat when snacking outdoors?",
        ["Pre-cut watermelon slices sitting out in the sun", "Piping hot freshly steamed idlis or freshly fried samosas straight from hot oil", "Open juice made with roadside block ice", "Raw chutney with flies"], 1,
        "High cooking heat kills bacteria instantly; freshly prepared hot foods are safest.",
        ["Walking through a market at {at}, {name} and friends want to grab a quick street food snack."],
        "What safety indicators should {name} check before ordering?",
        [("Check that the stall is clean, ingredients are covered, and vendor uses filtered water", "Ensures basic hygienic standards.", True, "clean stall|covered food|filtered water|hygiene", 40),
         ("Opt for freshly cooked piping hot dishes rather than pre-cut raw fruits", "Heat destroys dangerous gastrointestinal microbes.", True, "piping hot|freshly cooked|avoid cut fruits", 40),
         ("Avoid drinks made with crushed industrial block ice", "Blocks contain non-potable water bacteria.", False, "avoid block ice|no raw ice", 20)],
        ["eat from fly-infested stall", "eat uncovered street fruit", "drink murky road ice"],
        "FSSAI Clean Street Food Hub Initiative", "https://fssai.gov.in"
    ))

    # 13. NUT-033: Leftovers
    cards.append(make_card(
        "NUT-033", "basil", "Food safety", "Leftover food safety: Cooling, refrigerating and reheating",
        ["middle", "senior"],
        ["The 'Danger Zone' for bacterial proliferation is between 5°C and 60°C.",
         "Perishable cooked foods left at warm room temperature for over 2 hours multiply millions of bacteria."],
        ["Refrigerate leftover rice, dal, and curries within 2 hours of cooking", "Store leftovers in covered clean containers and consume within 24 to 48 hours", "Reheat leftovers thoroughly until steaming hot (above 74°C) before eating"],
        ["Never leave cooked food sitting out on the counter overnight", "Never reheat the same batch of food multiple times"],
        "Smelling cooked food is an infallible way to tell if it has gone bad.", "myth", "Many dangerous pathogenic bacteria (Staphylococcus, Salmonella) produce zero odor or taste changes.",
        "Within how many hours must cooked food be refrigerated to stop bacterial growth?",
        ["24 hours", "Within 2 hours of cooking", "5 days", "Never refrigerate"], 1,
        "After 2 hours at room temperature, bacterial populations double every 20 minutes.",
        ["After dinner at {at}, a large pot of cooked chicken curry or paneer sits on the kitchen stove."],
        "How should {name} handle these leftovers safely?",
        [("Allow it to cool slightly and place in refrigerator within 2 hours", "Stops bacterial multiplication in the Danger Zone.", True, "refrigerate|within 2 hours|cool and fridge", 45),
         ("Store in a covered clean airtight container", "Prevents contamination from fridge odors and moisture.", False, "clean container|airtight|covered", 20),
         ("Reheat thoroughly until steaming hot throughout before eating tomorrow", "Kills any surface bacterial spores.", True, "reheat steaming hot|heat thoroughly|hot", 35)],
        ["leave on stove all night", "eat unheated cold leftovers", "sniff test only"],
        "WHO Five Keys to Safer Food", "https://who.int"
    ))

    # 14. NUT-034: Food waste
    cards.append(make_card(
        "NUT-034", "basil", "Sustainability", "Reducing plate food waste at home and school",
        ["junior", "middle", "senior"],
        ["Food waste rotting in landfills produces methane, a greenhouse gas 28 times more potent than CO2.",
         "Taking smaller initial portions allows you to take seconds without throwing untouched food in the bin."],
        ["Serve smaller first portions on your plate; you can always ask for a second helping", "Pack only the amount of lunch you know you will eat at school", "Transform leftover rotis into healthy poha/rolls and leftover rice into fried rice"],
        ["Never heap mountains of food onto your plate that you cannot finish", "Never throw away whole untouched fruits into the dustbin"],
        "Leaving food on your plate at restaurants shows that you come from a wealthy family.", "myth", "Wasting food disrespects farmers' hard labor and exacerbates global environmental damage.",
        "What is the simplest way to ensure zero food waste from your dinner plate?",
        ["Take double what you need", "Start with modest portions and take seconds only if still hungry", "Feed it all to pets", "Throw it out quietly"], 1,
        "Portion control at serving time prevents untouched food ending up in trash bins.",
        ["At the school canteen or dining hall at {at}, {name} is serving lunch from the buffet counter."],
        "What plate habit ensures {name} leaves zero food waste?",
        [("Serve a modest first portion of rice, sabzi, and dal", "Ensures you only take what you can eat.", True, "small portion|modest portion|take less first", 45),
         ("Take second helpings only if still genuinely hungry", "Adjusts intake to real hunger without waste.", True, "second helping if hungry|take seconds", 35),
         ("Appreciate the farmers, water, and labor that produced the meal", "Builds gratitude and respect for food.", False, "respect food|farmer gratitude|no waste", 20)],
        ["overflow plate with food", "throw half in dustbin", "waste food carelessly"],
        "UNEP Food Waste Index", "https://unep.org"
    ))

    # 15. NUT-035: Calcium & Vit D
    cards.append(make_card(
        "NUT-035", "basil", "Bone health", "Building strong bones: Calcium, sunlight and Vitamin D",
        ["junior", "middle", "senior"],
        ["Human bone density reaches its peak by age 20; adolescence is the critical window for bone building.",
         "Without Vitamin D synthesized via sunlight, the body can absorb less than 15% of dietary calcium."],
        ["Consume calcium sources: curd (dahi), milk, ragi (finger millet), sesame seeds (til), and paneer", "Spend 20-30 minutes outdoors in morning sunlight to allow skin to synthesize Vitamin D naturally", "Engage in weight-bearing play like running, jumping rope, and dancing to strengthen bone matrix"],
        ["Never rely solely on calcium pills without consulting a doctor", "Never spend all daylight hours indoors under artificial white lights"],
        "Only cow's milk contains calcium; non-milk drinkers cannot have strong bones.", "myth", "Ragi (finger millet), sesame seeds, tofu, and dark leafy greens pack enormous calcium reserves.",
        "Why is spending 20-30 minutes in morning outdoor sunlight crucial for your bones?",
        ["To get a tan", "Sunlight triggers your skin to produce Vitamin D, which absorbs calcium into bones", "To warm clothes", "It does nothing"], 1,
        "Vitamin D is synthesized by UVB sunlight and acts as the gatekeeper for bone calcium absorption.",
        ["{name} dislikes drinking plain cow's milk and worries about bone strength at {at}."],
        "How can {name} build rock-solid bones through diet and lifestyle?",
        [("Eat non-dairy calcium rich foods like ragi, curd, sesame, and paneer", "Supplies essential mineral building blocks.", True, "ragi|curd|sesame|paneer|calcium", 45),
         ("Get 20-30 minutes of natural outdoor sunlight daily for Vitamin D", "Activates calcium absorption in gut.", True, "sunlight|outdoor time|vitamin d", 35),
         ("Play weight-bearing sports like running, skipping, or football", "Physical impact stimulates bone mineralization.", False, "sports|running|exercise|bone density", 20)],
        ["stay in dark room always", "drink sugary milkshakes only", "ignore bone health"],
        "Indian Society for Bone and Mineral Research (ISBMR)", "https://isbmr.org"
    ))

    # 16. NUT-036: Diet myths
    cards.append(make_card(
        "NUT-036", "basil", "Diet myths", "Busting magic food fads, detox teas and crash diets",
        ["middle", "senior"],
        ["The human liver and kidneys detoxify the bloodstream continuously; no tea or juice 'detoxes' you.",
         "Severe calorie-restriction crash diets during teenage years stunt growth and damage hormonal health."],
        ["Recognize that no single superfood possesses magical healing powers; balance is everything", "Trust whole home-cooked meals over expensive commercial detox supplements", "Fuel your body with diverse food groups: grains, pulses, dairy/alternatives, vegetables, fruits, and healthy fats"],
        ["Never starve yourself on crash juice cleanses or unverified viral diets", "Never eliminate whole food groups without certified medical advice"],
        "Drinking special green detox tea can melt away fat and flush all body toxins in 3 days.", "myth", "Detox teas are marketing scams that act as harsh laxatives. Your liver cleans your body naturally.",
        "What organs in your body already perform natural, scientifically proven detoxification 24/7?",
        ["The stomach and teeth", "Your liver and kidneys", "Your hair and nails", "The gallbladder only"], 1,
        "The liver breaks down waste and the kidneys filter blood into urine continuously.",
        ["A social media influencer at {at} urges teenagers to skip solid meals and drink an expensive 'Detox Cleanser'."],
        "How should {name} react to this fad diet claim?",
        [("Recognize it as an unscientific marketing gimmick; the liver and kidneys detoxify naturally", "Rejects harmful commercial diet scams.", True, "marketing gimmick|fad diet|liver and kidneys|unscientific", 45),
         ("Eat balanced, wholesome solid meals with plenty of water and fiber", "Provides real sustained nourishment.", True, "balanced meal|whole food|healthy eating", 35),
         ("Avoid dangerous crash diets that harm growing teen metabolism", "Protects physical development.", False, "no crash diets|healthy mindset", 20)],
        ["buy the detox tea", "starve for 5 days", "stop eating solid food"],
        "ICMR National Institute of Nutrition", "https://www.nin.res.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Basil")
    return cards


def get_civic_cards():
    cards = []

    # 1. CIV-021: Spitting
    cards.append(make_card(
        "CIV-021", "civic", "Hygiene", "Public spitting, paan stains and respiratory disease spread",
        ["junior", "middle", "senior"],
        ["Saliva and sputum droplets carry bacteria (like Mycobacterium tuberculosis) that remain airborne for hours.",
         "Public spitting disfigures sidewalks and walls and is a punishable offense under municipal civic bylaws."],
        ["Always spit into a tissue paper and dispose of it in a closed waste bin", "Rinse mouth in dedicated washbasin sinks, not on walls or staircases", "Remind family and peers that spitting spreads tuberculosis and respiratory infections"],
        ["Never spit on footpaths, roads, bus stops, or building stairwells", "Never spit out of moving buses or car windows"],
        "Spitting paan or tobacco on public walls is harmless once it dries.", "myth", "Dried sputum particles get kicked up as infectious dust that passersby inhale into their lungs.",
        "Why is public spitting strictly prohibited on roads, metro stations, and public spaces?",
        ["It looks funny", "It spreads deadly airborne diseases like Tuberculosis and damages public hygiene", "It wastes saliva", "It takes time"], 1,
        "Spitting transmits infectious respiratory bacteria and viruses to everyone nearby.",
        ["Walking through a bus station at {at}, {name} sees someone about to spit paan onto the wall."],
        "How can {name} promote responsible civic cleanliness?",
        [("Politely remind that public spitting spreads diseases and spoils shared spaces", "Promotes community hygiene awareness.", True, "don'?t spit|spreads disease|public cleanliness|polite", 45),
         ("Use designated washroom sinks or spit into a tissue for the dustbin", "Directs to hygienic disposal.", True, "use sink|tissue|dustbin", 35),
         ("Lead by personal example and never spit on shared streets", "Sets positive civic standard.", False, "lead by example|civic sense", 20)],
        ["spit on the wall", "encourage spitting", "ignore completely"],
        "Swachh Bharat Urban Guidelines", "https://swachhbharaturban.gov.in"
    ))

    # 2. CIV-022: Noise pollution
    cards.append(make_card(
        "CIV-022", "civic", "Noise", "Noise pollution: Honking, loudspeakers and silent zones",
        ["junior", "middle", "senior"],
        ["Prolonged exposure to noise above 85 decibels causes permanent sensorineural hearing loss.",
         "Hospitals, courts, and educational institutions are designated Silent Zones (no honking allowed within 100m)."],
        ["Avoid honking vehicle horns unless preventing an imminent collision", "Keep personal headphones and portable speaker volumes moderate in public transport", "Respect night-time silence rules: no loud speakers after 10 PM near residential areas"],
        ["Never honk near hospital ICUs, old-age homes, or school exam centres", "Never blast party speakers into midnight disturbing studying neighbours"],
        "Continuous honking in a traffic jam makes the vehicles in front move faster.", "myth", "Honking does not clear stopped traffic; it causes intense acoustic stress and road rage.",
        "Why is honking completely prohibited within 100 meters of a hospital?",
        ["Hospitals are big", "Sudden loud acoustic spikes trigger cardiac stress and disturb critical patients", "To save horn battery", "Doctors don't like sound"], 1,
        "Noise spikes induce dangerous stress and sleep deprivation in ICU patients.",
        ["A driver behind {name}'s school van at {at} is leaning on their horn right outside a hospital gate."],
        "What civic rule should road users remember?",
        [("Hospitals are 24/7 Silent Zones where honking is strictly illegal", "Protects recovering patients from acoustic shock.", True, "silent zone|hospital|no honking|illegal", 45),
         ("Honking does not magically clear red lights or traffic bottlenecks", "Dispels useless aggressive honking.", True, "honking doesn'?t clear traffic|patience", 35),
         ("Keep noise low and respect quiet hours in residential neighbourhoods", "Basic civic courtesy.", False, "respect quiet|neighbourhood", 20)],
        ["honk louder", "encourage honking at hospital", "blast horn"],
        "Central Pollution Control Board (CPCB) Noise Rules", "https://cpcb.nic.in"
    ))

    # 3. CIV-023: Assisting visually impaired
    cards.append(make_card(
        "CIV-023", "civic", "Accessibility", "Respectful assistance for visually impaired citizens",
        ["junior", "middle", "senior"],
        ["People with visual impairment navigate using white canes, tactile pavings, and auditory landmarks.",
         "Grabbing someone's arm or cane unexpectedly without asking startles and disorients them."],
        ["Always ask first: 'Hello, may I help you cross the road or find the platform?'", "Offer your elbow for them to hold lightly; walk a half-step ahead at a natural pace", "Verbally describe steps, curbs, and hazards clearly (e.g. 'Step down in two steps')"],
        ["Never grab someone's white cane or pull them by the wrist", "Never pet or distract a working guide dog"],
        "You should grab a blind person's hand and pull them across the road without talking.", "myth", "Grabbing people without consent causes fear and loss of balance. Ask first, offer elbow.",
        "How should you offer physical guidance to a visually impaired person crossing a street?",
        ["Pull their cane", "Ask first, then offer your elbow for them to hold as you walk", "Push them from behind", "Shout directions"], 1,
        "Holding your elbow allows them to follow your body movement smoothly and safely.",
        ["Near a busy road crossing at {at}, {name} sees a person with a white cane waiting by the curb."],
        "How should {name} offer assistance respectfully?",
        [("Greet them politely and ask: 'Hello, would you like assistance crossing the street?'", "Always obtains consent first.", True, "ask first|may i help|greet politely", 45),
         ("If they accept, offer your elbow and guide them smoothly", "Proper sighted-guide technique.", True, "offer elbow|guide gently|walk ahead", 35),
         ("Describe curbs and steps clearly: 'Curb step down right now'", "Provides necessary spatial context.", False, "verbal descriptions|curb step|describe road", 20)],
        ["grab cane suddenly", "drag across road without speaking", "push from behind"],
        "Department of Empowerment of Persons with Disabilities", "https://disabilityaffairs.gov.in"
    ))

    # 4. CIV-024: Ambulances
    cards.append(make_card(
        "CIV-024", "civic", "Emergency transit", "Giving immediate right-of-way to emergency ambulances",
        ["junior", "middle", "senior"],
        ["Every second lost in transit reduces survival odds for heart attack and trauma victims.",
         "Failing to give way to emergency vehicles attracts a fine of up to ₹10,000 under the Motor Vehicles Act."],
        ["Move your vehicle or cycle immediately to the left side of the road when a siren sounds", "Clear the center lane or create an emergency green corridor", "Never tail or closely follow an ambulance to zip through cleared traffic"],
        ["Never block or race an ambulance with flashing lights and sirens", "Never freeze in the middle of an intersection"],
        "Following right behind a rushing ambulance is a smart shortcut to bypass city traffic.", "myth", "Tailgating ambulances causes rear-end crashes and obstructs emergency braking.",
        "What should all vehicles immediately do when an ambulance siren is heard approaching from behind?",
        ["Speed up and race it", "Safely pull over to the left to open a clear lane", "Stop dead in the middle lane", "Ignore siren"], 1,
        "Pulling to the left creates a continuous open emergency corridor for critical patients.",
        ["Riding on the road at {at}, an ambulance siren blares loudly behind {name}'s vehicle."],
        "What is the immediate legal and moral civic duty?",
        [("Safely maneuver to the left side of the road to clear the path", "Opens a clear channel for emergency transit.", True, "pull to left|clear path|move aside|give way", 45),
         ("Encourage other drivers to yield right-of-way", "Builds active community compliance.", False, "encourage others|yield right of way", 20),
         ("Never tailgate behind the ambulance to skip signals", "Extremely hazardous and illegal.", True, "don'?t tailgate|no chasing ambulance", 35)],
        ["block the ambulance", "race the ambulance", "tailgate to skip traffic"],
        "Motor Vehicles Act Section 194E", "https://morth.nic.in"
    ))

    # 5. CIV-025: Service workers
    cards.append(make_card(
        "CIV-025", "civic", "Respect", "Treating sanitation workers, security guards and domestic staff with dignity",
        ["junior", "middle", "senior"],
        ["Sanitation workers, housekeeping staff, and security guards keep our cities functional and safe.",
         "Article 14 and 21 of the Indian Constitution uphold equal human dignity for every citizen."],
        ["Greet service staff with a warm 'Namaste', 'Good morning', or 'Thank you'", "Address domestic workers, bus conductors, and guards with polite respectful honorifics (Bhaiya, Didi, Uncle)", "Offer drinking water to delivery agents and cleaners visiting your building"],
        ["Never speak rudely, snap fingers, or look down upon manual laborers", "Never leave broken glass unseparated in trash that can cut waste collectors' hands"],
        "You only need to show respect to rich professionals, not sanitation workers.", "myth", "Dignity of labor is the bedrock of civilized society. Every honest job deserves deep respect.",
        "What is the simplest everyday habit that shows civic respect to your apartment security guard?",
        ["Ignoring them completely", "A polite greeting, acknowledging their work, and saying 'Thank you'", "Ordering them around", "Complaining always"], 1,
        "Simple everyday courtesy validates the dignity and contribution of essential service staff.",
        ["A delivery partner climbs three flights of stairs in hot weather at {at} to hand over a package."],
        "What civic courtesy should {name} extend?",
        [("Receive package with a warm 'Thank you' and offer a glass of clean water", "Demonstrates genuine human warmth and empathy.", True, "thank you|offer water|polite greeting", 45),
         ("Speak with respect and patience without snapping or arrogance", "Affirms dignity of labor.", True, "respectful tone|patience|no arrogance", 35),
         ("Recognize their hard work keeping city logistics moving", "Fosters civic appreciation.", False, "appreciate work|kindness", 20)],
        ["slam door in face", "scold for taking stairs", "speak rudely"],
        "National Commission for Safai Karamcharis", "https://ncsk.nic.in"
    ))

    # 6. CIV-026: Wedding food waste
    cards.append(make_card(
        "CIV-026", "civic", "Functions", "Buffet discipline and zero food waste at weddings and parties",
        ["junior", "middle", "senior"],
        ["Thousands of tons of edible food are dumped into garbage pits after lavish weddings every night.",
         "Unattended heaps of wasted food on dirty paper plates attract stray pests and rot."],
        ["Take small initial portions at wedding buffets; you can revisit counters freely", "Only pick dishes you genuinely intend to eat rather than trying to taste everything on one plate", "Encourage hosts to partner with food rescue NGOs (like Robin Hood Army) to distribute surplus untouched food"],
        ["Never pile mountains of halwa and biryani only to abandon half-eaten plates", "Never throw whole untouched food packets into garden hedges"],
        "Leaving half your wedding buffet plate unconsumed is standard high-class etiquette.", "myth", "Wasting food while millions face hunger is deeply insensitive and un-civic.",
        "You are at a wedding reception buffet with 20 delicious dishes. What is the smart, civic way to eat?",
        ["Heap all 20 dishes onto one plate so it overflows", "Take 2-3 dishes you really enjoy in small portions, and return for seconds if hungry", "Take everything and dump half", "Smash the plate"], 1,
        "Taking modest portions avoids wasting food and lets you enjoy meals fresher.",
        ["At a family wedding function at {at}, {name} is at the dessert buffet counter."],
        "What is the responsible civic approach?",
        [("Take small portions of one or two treats you will actually finish", "Prevents plate food abandonment.", True, "small portion|take what you finish|one treat", 45),
         ("Do not leave half-eaten desserts on chairs or ledges", "Leaves shared spaces clean.", True, "don'?t abandon plate|put in bin", 35),
         ("If surplus untouched food remains, suggest donating to verified food charities", "Feeds vulnerable communities.", False, "donate surplus|food charity|no waste", 20)],
        ["pile plate to overflow", "leave half-eaten food on chairs", "dump full plates"],
        "Robin Hood Army & Feeding India Guidelines", "https://robinhoodarmy.com"
    ))

    # 7. CIV-027: Leaking taps
    cards.append(make_card(
        "CIV-027", "civic", "Water", "Closing leaking public taps and reporting pipeline bursts",
        ["junior", "middle", "senior"],
        ["A single faucet dripping one drop per second wastes over 3,000 litres of treated water every year.",
         "Clean drinking water is an increasingly scarce natural resource in Indian cities."],
        ["Close any running or half-open public tap you see at railway stations, parks, or schools", "Place a bucket underneath while alerting facility maintenance if a tap cannot be shut fully", "Report major street pipeline bursts on municipal citizen grievance helplines"],
        ["Never walk past a gushing municipal drinking tap without taking action", "Never leave school washroom taps running while soaping hands"],
        "A leaking tap in a public park is the government's problem, not a citizen's concern.", "myth", "Public water belongs to all citizens. Closing running taps is a direct civic duty.",
        "What should you do if you notice a drinking water tap running freely at a train station?",
        ["Walk past quickly", "Stop for 5 seconds and turn the tap handle fully closed", "Take a selfie", "Complain on social media without closing it"], 1,
        "Taking 5 seconds to close the tap saves hundreds of litres of clean drinking water.",
        ["At the public park or sports ground at {at}, a drinking water fountain tap is left gushing full blast."],
        "What should {name} do?",
        [("Step up and turn the tap firmly clockwise until the water flow stops completely", "Immediately halts precious water wastage.", True, "turn off tap|close tap|stop water", 45),
         ("If the washer is broken, report the leak to the park supervisor or maintenance staff", "Ensures permanent plumbing fix.", True, "report leak|tell supervisor|maintenance", 35),
         ("Remind peers to turn off taps while brushing or applying soap", "Promotes everyday conservation habits.", False, "remind peers|save water", 20)],
        ["walk past freely", "leave tap running", "break the tap"],
        "Jal Jeevan Mission Guidelines", "https://jaljeevanmission.gov.in"
    ))

    # 8. CIV-028: Pet walking
    cards.append(make_card(
        "CIV-028", "civic", "Pets", "Responsible pet walking: Leashes, scooping and colony courtesy",
        ["junior", "middle", "senior"],
        ["Dog waste contains harmful bacteria (Campylobacter, Salmonella) and parasite eggs that contaminate shoes.",
         "Unleashed pet dogs can startle young children, elderly strollers, or provoke territorial street dogs."],
        ["Always keep your pet dog on a secure, comfortable leash in public society areas and parks", "Carry old newspapers, plastic bags, or a poop-scooper to clean up your pet's waste immediately", "Ensure pets are up-to-date on yearly anti-rabies vaccinations and society registration"],
        ["Never leave your pet's waste on common walking tracks, flowerbeds, or building corridors", "Never allow pets to jump onto unwilling neighbors or strangers"],
        "Leaving dog poop on public pavements is fine because it dissolves in rain naturally.", "myth", "Pavement feces spread diseases to children, soil shoes, and ruin common hygiene.",
        "What must a responsible pet parent always carry when walking their dog in a society park?",
        ["Only a phone", "A sturdy leash and a bag or scooper to pick up pet waste", "Heavy stick", "Biscuits only"], 1,
        "Leashing ensures control and waste bags keep neighborhood walking tracks spotless.",
        ["Walking a family pet in the colony garden at {at}, the dog relieves itself near the jogging track."],
        "What is {name}'s civic obligation as a pet guardian?",
        [("Use a bag or paper to pick up the waste and deposit it in an outdoor garbage bin", "Restores public cleanliness immediately.", True, "scoop waste|pick up poop|bag|dustbin", 45),
         ("Keep the dog on a secure leash at all times in common areas", "Prevents unexpected jumps on elderly neighbors.", True, "keep on leash|leashed dog|control", 35),
         ("Respect neighbors who may feel anxious around unfamiliar dogs", "Cultivates mutual community harmony.", False, "respect neighbors|courteous", 20)],
        ["leave waste on jogging track", "run away without cleaning", "unleash dog near toddlers"],
        "Animal Welfare Board Guidelines on Pet Dogs in Resident Welfare Associations", "https://awbi.gov.in"
    ))

    # 9. CIV-029: Shared spaces
    cards.append(make_card(
        "CIV-029", "civic", "Community", "Respecting shared spaces: Corridors, elevators and parks",
        ["junior", "middle", "senior"],
        ["Corridors and stairwells are primary emergency fire evacuation corridors that must stay 100% clear.",
         "Dumping personal shoes, bicycles, and flowerpots in common corridors creates dangerous trip hazards."],
        ["Keep shared stairwells and lift lobbies free of personal junk, old furniture, and garbage bags", "Hold the elevator door politely for approaching residents carrying groceries or prams", "Dispose of personal snack wrappers in outdoor dustbins, never leaving them on park benches"],
        ["Never leave leaky garbage bags leaking smelly liquid in shared elevator lobbies", "Never scribble graffiti or stick chewing gum inside common lifts"],
        "Corridors outside your apartment door belong exclusively to your flat to store clutter.", "myth", "Common corridors are shared community property and legal fire escape routes.",
        "Why must building stairwells and common corridors always be kept completely clear of clutter?",
        ["For decoration", "They are emergency fire evacuation routes that people must navigate in smoke and darkness", "To sweep faster", "No reason"], 1,
        "Blocked staircases cause lethal crush injuries and trapped residents during night fire alarms.",
        ["In the apartment building at {at}, someone has dumped old broken bicycles and boxes in the stairwell."],
        "What civic issue does {name} recognize?",
        [("Stairwells are emergency fire escape routes that must remain completely unobstructed", "Ensures unhindered life-saving evacuation.", True, "fire escape|unobstructed|emergency exit|clear stairwell", 45),
         ("Common spaces belong to all residents and should be kept tidy and clean", "Prevents blight and community friction.", True, "shared space|tidy|clean lobby", 35),
         ("Notify the Resident Welfare Association (RWA) or building committee to clear the blockage", "Follows proper governance channels.", False, "inform rwa|society committee|clear items", 20)],
        ["dump more junk in stairs", "block the fire exit completely", "ignore fire hazard"],
        "Model Bye-Laws for Resident Welfare Associations", "https://mohua.gov.in"
    ))

    # 10. CIV-030: Upstander
    cards.append(make_card(
        "CIV-030", "civic", "Anti-bullying", "From bystander to upstander: Standing up against teasing",
        ["junior", "middle", "senior"],
        ["Bullying thrives when surrounding peers remain silent, which bullies interpret as approval.",
         "Research shows that when a single peer intervenes kindly, over 50% of bullying stops within 10 seconds."],
        ["Stand next to the targeted student and invite them away: 'Come on, let's go play basketball together'", "Speak clearly to the teaser: 'That's not funny, let's stop this'", "Report persistent bullying to a trusted teacher or school counselor"],
        ["Never join in laughing or filming teasing videos on mobile phones", "Never resort to physical violence or aggressive insults to solve conflict"],
        "Watching someone get teased without saying anything means you are neutral and innocent.", "myth", "Passive silence empowers the bully. An upstander uses gentle words to support the victim.",
        "What is the most effective way a student can act as an 'upstander' when a classmate is mocked?",
        ["Laugh along", "Step in, support the classmate, and invite them away to a safe spot", "Film a video for social media", "Punch the bully"], 1,
        "Distracting the situation and supporting the victim dissolves the bully's audience.",
        ["In the school courtyard at {at}, two older students are mocking a classmate's accent and laughing."],
        "How can {name} act as a courageous civic upstander?",
        [("Walk up to the classmate and warmly invite them to join your group", "Removes the victim from the aggressive interaction.", True, "invite away|support friend|stand with victim|upstander", 45),
         ("Clearly say: 'Hey, that's unkind, let's stop this' without getting aggressive", "Disapproves bullying behavior firmly.", True, "tell to stop|not funny|unkind|speak up", 35),
         ("Inform a teacher if the teasing persists or turns physical", "Secures responsible adult intervention.", False, "tell teacher|counselor|report", 20)],
        ["laugh along with teasers", "record a video on phone", "encourage mockery"],
        "CBSE Anti-Bullying Guidelines for Schools", "https://cbse.gov.in"
    ))

    # 11. CIV-031: Heritage protection
    cards.append(make_card(
        "CIV-031", "civic", "Heritage", "Preserving historical monuments and stopping graffiti vandalism",
        ["junior", "middle", "senior"],
        ["Ancient stone monuments and forts represent irreplaceable centuries-old national architecture.",
         "Scratching names or painting graffiti on protected archaeological sites is a crime under AMASR Act."],
        ["Admire historical monuments with eyes and cameras without touching delicate carvings", "Follow all ASI site rules: carry waste back with you and stay within marked visitor ropes", "Speak up politely if friends pull out keys or markers to scratch graffiti on ancient walls"],
        ["Never carve or scratch initials ('Raju loves Priya') into ancient stone or bricks", "Never discard plastic bottles, wrappers, or chewing gum inside heritage compounds"],
        "Scratching your name onto an ancient fort wall is a harmless romantic tradition.", "myth", "Carving scratches off the protective mineral patina, accelerating chemical weathering and stone crumbling.",
        "What law protects Indian historical monuments from graffiti, defacement, and destruction?",
        ["The Traffic Code", "The Ancient Monuments and Archaeological Sites and Remains (AMASR) Act", "The Forest Bill", "None"], 1,
        "The AMASR Act makes defacing historical monuments punishable by fines and imprisonment.",
        ["On a school excursion to a historical monument at {at}, a classmate takes out a coin to carve initials on a stone pillar."],
        "What should {name} tell them immediately?",
        [("Firmly stop them: 'Please don't carve on ancient stone, it permanently ruins centuries of heritage'", "Prevents irreversible physical vandalism.", True, "don'?t carve|preserve heritage|stop scratching|ruins monument", 45),
         ("Remind them that defacing monuments is an illegal offense under archaeological laws", "Cites legal prohibition and penalties.", True, "illegal|heritage law|asi|punishable", 35),
         ("Keep our shared cultural heritage pristine for future generations", "Instills civic pride.", False, "cultural pride|future generations|protect", 20)],
        ["hand them a marker", "scratch names together", "ignore vandalism"],
        "Archaeological Survey of India (ASI)", "https://asi.nic.in"
    ))

    # 12. CIV-032: Municipal apps
    cards.append(make_card(
        "CIV-032", "civic", "Grievances", "Reporting civic problems on municipal apps (potholes, streetlights)",
        ["middle", "senior"],
        ["Municipal corporations in India have dedicated grievance apps (Swachhata, MyGov, local Smart City portals).",
         "Geo-tagged citizen photo reports automatically route repair work orders to local ward engineers."],
        ["Download and use your city's municipal grievance app (e.g. Swachhata-MoHUA or city corporation app)", "Take a clear, geotagged photo showing the broken streetlight, open pothole, or garbage dump", "Track the complaint ticket number until the municipal authority marks it resolved with an 'after' photo"],
        ["Never submit fake, abusive, or duplicate frivolous complaint tickets", "Never ignore severe public hazards (like open electric junction boxes) without reporting"],
        "Filing municipal complaints online is useless because nobody ever checks civic apps.", "myth", "Swachhata and Smart City portals have mandatory time-bound SLAs monitored by municipal commissioners.",
        "What feature in citizen grievance apps ensures municipal workers find the exact location of a pothole?",
        ["The colour of your phone", "GPS geotagging embedded in the submitted photograph", "Your horoscope", "Social media likes"], 1,
        "Geotagged photos pinpoint exact latitude/longitude coordinates for engineering crews.",
        ["Outside school at {at}, a deep road pothole fills with water, creating an accident hazard for cyclists."],
        "How can {name} and their family take constructive civic action?",
        [("Take a clear geotagged photo using the official municipal grievance app", "Initiates an official traceable civic repair ticket.", True, "municipal app|swachhata app|photo|geotagged|file complaint", 45),
         ("Provide the exact street name and prominent landmark in the description", "Enables ward staff to locate the pothole easily.", True, "landmark|street name|description", 35),
         ("Track the complaint ticket until the road repair is completed", "Ensures civic accountability.", False, "track ticket|resolution|follow up", 20)],
        ["do nothing and complain", "post memes without reporting", "fill with garbage"],
        "Ministry of Housing and Urban Affairs (MoHUA)", "https://mohua.gov.in"
    ))

    # 13. CIV-033: Voting & duties
    cards.append(make_card(
        "CIV-033", "civic", "Democracy", "Why voting and Fundamental Duties matter for every citizen",
        ["junior", "middle", "senior"],
        ["Democracy thrives on active, informed citizen participation, not passive cynicism.",
         "Article 51A of the Indian Constitution lists 11 Fundamental Duties, including protecting public property and the environment."],
        ["Learn how local elections function (ward corporators, MLAs, MPs) and how budgets are spent", "Encourage eligible adult family members to register and vote in every single election", "Fulfill student fundamental duties: protect the environment, respect the national flag, and develop scientific temper"],
        ["Never treat voting day as just a leisure picnic holiday", "Never trade votes for money, gifts, or communal pressure"],
        "A single citizen's vote makes zero difference in a country of 1.4 billion people.", "myth", "Crucial elections have been won or lost by a single vote. Every vote shapes governance and schools.",
        "Where are the Fundamental Duties of Indian citizens listed in the Constitution?",
        ["Article 21", "Article 51A", "Article 370", "The Preamble"], 1,
        "Article 51A outlines citizen duties toward the nation, public property, and nature.",
        ["Election day approaches in the city at {at}, and {name}'s family considers skipping voting to go to the mall."],
        "What democratic perspective should {name} share?",
        [("Voting is a democratic right and duty that determines our roads, schools, and hospitals", "Connects voting to quality of public life.", True, "duty to vote|democracy|vote matters|elect good leaders", 45),
         ("Encourage every eligible adult in the family to exercise their constitutional franchise", "Promotes civic participation.", True, "encourage family|go vote|cast vote", 35),
         ("Remember that student fundamental duties include developing a rational scientific temper", "Cites Article 51A civic values.", False, "scientific temper|fundamental duties|article 51a", 20)],
        ["tell family to skip voting", "sell vote for cash", "mock the election"],
        "Election Commission of India (SVEEP)", "https://ecisveep.nic.in"
    ))

    # 14. CIV-034: Places of worship
    cards.append(make_card(
        "CIV-034", "civic", "Religious spaces", "Decorum, courtesy and quiet respect in places of worship",
        ["junior", "middle", "senior"],
        ["Temples, mosques, churches, gurdwaras, and viharas are sanctified spaces for quiet contemplation.",
         "Respecting diverse traditions (removing shoes, covering heads, turning off phones) fosters interfaith peace."],
        ["Turn mobile phones completely to silent or switch them off before entering any place of worship", "Follow traditional dress and entry customs respectfully (cover head, remove footwear, wash feet)", "Maintain quiet speaking tones and refrain from running or shouting inside prayer halls"],
        ["Never take intrusive flash photography or selfies in front of praying worshippers", "Never mock or disrespect sacred symbols or rituals of other communities"],
        "It is acceptable to answer loud phone calls in a temple or church if it's an important video game update.", "myth", "Prayer spaces are sanctuaries of peace. Loud phone chatter is deeply disruptive and disrespectful.",
        "What is the first thing you should do with your mobile phone before entering a place of worship?",
        ["Turn ringtone to max", "Switch it to silent mode or turn it off completely", "Play loud music", "Record a live stream"], 1,
        "Silencing phones preserves the tranquil spiritual atmosphere for all visitors.",
        ["Visiting an ancient temple, gurdwara, or church at {at}, {name} enters the quiet prayer hall."],
        "What respectful decorum should {name} uphold?",
        [("Silence mobile phone and speak only in gentle whisper tones", "Protects tranquil worship environment.", True, "silence phone|whisper|quiet|turn off sound", 45),
         ("Respect site-specific customs like removing shoes or covering head", "Demonstrates cultural courtesy.", True, "remove shoes|cover head|follow customs", 35),
         ("Do not disturb praying devotees with flash selfies or videos", "Preserves personal privacy and sanctity.", False, "no flash|no selfies|respect devotees", 20)],
        ["shout loudly across hall", "answer phone calls loudly", "mock sacred traditions"],
        "National Foundation for Communal Harmony", "https://nfch.nic.in"
    ))

    # 15. CIV-035: Priority queues
    cards.append(make_card(
        "CIV-035", "civic", "Priority queues", "Prioritizing the elderly, pregnant women and disabled in public queues",
        ["junior", "middle", "senior"],
        ["Standing for extended periods causes painful joint stress for elderly and pregnant citizens.",
         "Designated priority seats and ticket counters ensure equitable access to basic public infrastructure."],
        ["Offer your seat immediately to elderly passengers, pregnant women, or people with infants on buses/metros", "Allow seniors or persons with mobility aids to move ahead in ticket, billing, or clinic queues", "Queue in an orderly single-file line without jumping spots or cutting in front of others"],
        ["Never pretend to be asleep in designated 'Senior Citizen' seats to avoid standing", "Never shove past slow-walking elderly commuters on escalators or stairs"],
        "Pretending to sleep in a metro priority seat is a smart way to keep your seat.", "myth", "Feigning sleep to deprive elderly or pregnant citizens of seats shows a severe lack of empathy.",
        "You are seated on a crowded metro and an elderly person with a cane boards. What should you do?",
        ["Close your eyes and pretend to sleep", "Stand up immediately, smile, and offer them your seat", "Look at your phone", "Complain loudly"], 1,
        "Offering your seat to seniors demonstrates basic civic compassion and respect.",
        ["In a long queue at a medical dispensary or metro counter at {at}, an elderly person with a walking stick joins the back of the line."],
        "How can {name} exhibit exemplary civic kindness?",
        [("Smile and offer to let the senior person move ahead in the queue", "Shows active consideration for physical vulnerability.", True, "let move ahead|offer spot|priority queue|seniors first", 45),
         ("Offer your seat if on a bus or metro train", "Protects fragile commuters from falling during transit.", True, "give seat|offer seat|stand up", 35),
         ("Maintain orderly queue discipline without pushing or cutting lines", "Prevents stampedes and chaos.", False, "queue discipline|no pushing|orderly line", 20)],
        ["pretend to sleep", "cut in front of senior", "push past"],
        "Ministry of Social Justice and Empowerment", "https://socialjustice.gov.in"
    ))

    # 16. CIV-036: Gratitude
    cards.append(make_card(
        "CIV-036", "civic", "Gratitude", "Everyday gratitude to community helpers and municipal crews",
        ["junior", "middle", "senior"],
        ["A community that values its service workers fosters higher social happiness and civic pride.",
         "Expressing genuine verbal appreciation ('Thank you for your service') transforms working morale."],
        ["Thank your school bus driver and conductor when stepping down every afternoon", "Say a heartfelt 'Thank you' to street sweepers and garbage collectors working in your lane", "Keep your own classroom desks and school cafeteria tables neat to lighten helper workloads"],
        ["Never treat cleaners as invisible or treat their service as something to take for granted", "Never litter on grounds right in front of someone sweeping"],
        "Saying 'Thank you' to sanitation workers or bus conductors is unnecessary because they get paid.", "myth", "Compensation pays for work; human gratitude and courtesy validate human dignity.",
        "What is the simplest way to show everyday gratitude to your school bus driver at the end of the day?",
        ["Run out without looking", "Smile and say: 'Thank you Bhaiya/Uncle, have a good evening!'", "Honk the horn", "Leave candy wrappers on the floor"], 1,
        "A warm, respectful verbal thank you acknowledges their responsibility for your safety.",
        ["At school dismissal at {at}, {name} steps off the bus after a safe journey home."],
        "What closing civic gesture should {name} make?",
        [("Look at the driver and conductor, smile, and say: 'Thank you for the safe ride!'", "Recognizes essential daily service with warmth.", True, "thank you|gratitude|safe ride|polite goodbye", 45),
         ("Pick up any personal snack wrappers or trash from your seat", "Keeps the shared vehicle tidy for tomorrow.", True, "pick up trash|clean seat|no litter", 35),
         ("Extend the same everyday kindness to all community workers", "Cultivates lifelong civic empathy.", False, "kindness|community helpers", 20)],
        ["rush off without acknowledging", "throw trash under seat", "scold driver"],
        "Department of School Education and Literacy (Civic Values)", "https://dsel.education.gov.in"
    ))

    print(f"Loaded {len(cards)} expanded cards for Civic")
    return cards
