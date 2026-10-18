"""
New Agents in the FUTURE Pillar:
- Coin (Money & Practical Finance - MON)
- Forge (Enterprise & Building Things - ENT)
"""
from cards_existing import make_card

def get_coin_cards():
    cards = []

    # MON-001: Needs vs Wants
    cards.append(make_card(
        "MON-001", "coin", "Budgeting", "Needs vs Wants: The golden financial filter",
        ["junior", "middle", "senior"],
        ["A 'need' is essential for survival, health, and basic education; a 'want' is a desire that can be delayed or skipped.",
         "Distinguishing between needs and wants is the single most important habit for avoiding lifelong debt."],
        ["Pause 24 hours before buying non-essential items to curb impulse spending", "Ask yourself: 'What happens if I do not buy this today?'", "Cover food, books, and essential bus fare before spending on snacks or merchandise"],
        ["Never label temporary peer cravings as urgent life needs", "Never spend emergency savings on entertainment or trendy clothing"],
        "If you desire something intensely, that automatically turns it into a financial need.", "myth", "Emotional intensity does not change necessity. Needs sustain life and daily function; wants are upgrades.",
        "Which of the following is genuinely classified as a 'need' for a school student?",
        ["A limited-edition gaming skin", "Prescription spectacles or standard school uniform", "Brand-new trendy sneakers when current shoes fit well", "Eating out at a fast-food cafe every afternoon"], 1,
        "Medical items, nutrition, and essential school requirements are basic needs; luxury brand upgrades are wants.",
        ["While shopping with friends at {at}, {name} sees a stylish imported jacket on discount that everyone praises, but {name} only has pocket money saved for upcoming textbook purchases."],
        "How should {name} decide whether to purchase it?",
        [("Prioritize necessary school textbooks as a core need over the jacket", "Ensures essential obligations are fulfilled without financial distress.", True, "prioritize needs|textbooks first|essential over luxury", 45),
         ("Implement a 24-hour cooling-off period to evaluate true value", "Stops instant peer-pressure impulse buying.", True, "pause 24 hours|cooling off|evaluate impulse", 35),
         ("Recognize the jacket as a temporary want that can be saved for later", "Demonstrates clear financial self-control.", False, "want not need|save for it later|delay gratification", 20)],
        ["borrow money to buy immediately", "spend book money on jacket", "give into peer pressure"],
        "Reserve Bank of India - Financial Education", "https://rbi.org.in/financialeducation"
    ))

    # MON-002: The 50/30/20 Rule for Youth
    cards.append(make_card(
        "MON-002", "coin", "Savings", "Budgeting your money: The 50/30/20 bucket method",
        ["middle", "senior"],
        ["The 50/30/20 rule splits income: 50% for necessities, 30% for personal wants/fun, and 20% for future savings.",
         "Budgeting does not mean depriving yourself of fun; it ensures you enjoy today while securing tomorrow."],
        ["Divide any received allowance or gift money into three distinct jars or envelopes", "Always deposit the 20% savings first ('pay yourself first')", "Track total expenses in a pocket notebook or mobile ledger at least once a week"],
        ["Never spend 100% of money received on the day you receive it", "Never dip into the savings bucket for impulsive weekend outings"],
        "Budgeting means you are never allowed to spend money on entertainment or fun.", "myth", "A healthy budget explicitly reserves 30% for guilt-free fun so you don't burn out or binge spend.",
        "According to the 50/30/20 budgeting rule, what proportion of allowance should be directed to future savings?",
        ["0%", "5%", "At least 20%", "90%"], 2,
        "Allocating 20% toward long-term savings builds an emergency cushion and teaches compound wealth.",
        ["{name} receives 500 rupees as monthly pocket money at {at}. Friends urge {name} to spend it all immediately on milkshakes and video games."],
        "How should {name} allocate this money systematically?",
        [("Set aside at least 100 rupees (20%) immediately into a savings jar", "Secures the savings component before any spending occurs.", True, "save 20%|100 rupees|pay yourself first", 45),
         ("Allocate 50% for actual requirements like stationery and bus fare", "Covers recurring necessary expenses responsibly.", True, "stationery|bus fare|50% needs", 35),
         ("Allow a planned portion for social fun without exceeding the budget", "Enjoys treats responsibly within limits.", False, "budgeted fun|enjoy within limits|30% wants", 20)],
        ["spend all 500 on day one", "borrow when money runs out", "skip savings entirely"],
        "National Centre for Financial Education (NCFE)", "https://ncfe.org.in"
    ))

    # MON-003: Unit Pricing & Supermarket Comparison
    cards.append(make_card(
        "MON-003", "coin", "Smart Shopping", "Unit pricing: Spotting deceptive supermarket packaging",
        ["junior", "middle", "senior"],
        ["Bigger boxes or family packs are not always cheaper; manufacturers sometimes price larger volumes higher per gram.",
         "Unit pricing measures cost per standard metric (e.g., price per 100g or per liter), exposing true costs."],
        ["Calculate the price per 100g or per piece before assuming the 'jumbo pack' is a discount", "Look at the lowest and highest shelves in grocery aisles where cheaper unpromoted brands sit", "Check expiry and manufacturing dates before buying bulk perishables"],
        ["Never trust flashy 'Buy 2 Get 1 Free' stickers without comparing single-pack unit costs", "Never purchase excess perishable groceries just because of a bulk offer"],
        "Larger package sizes are always guaranteed to be cheaper per gram than small packs.", "myth", "Retailers frequently exploit this assumption; unit price calculations regularly reveal smaller packs are cheaper.",
        "How do you determine which brand of cereal or detergent offers the genuinely lowest price?",
        ["Check which box has the brightest cartoon character", "Calculate the price per 100 grams or millilitres", "Pick whichever box says 'Special Value Pack'", "Buy whichever is placed at eye level"], 1,
        "Comparing price per standard unit (gram/ml) reveals exact mathematical value regardless of box size.",
        ["At the grocery store at {at}, {name} sees Brand A selling 200g of biscuits for Rs 40 (Rs 20/100g) and a 'Giant Saver Pack' of 350g for Rs 84 (Rs 24/100g)."],
        "Which option should {name} choose and why?",
        [("Calculate price per 100g and discover the smaller pack is cheaper per unit", "Performs objective unit price comparison.", True, "calculate unit price|per 100g|smaller pack cheaper", 50),
         ("Reject the deceptive 'Giant Saver' claim", "Identifies deceptive retail marketing tactics.", True, "reject giant saver label|marketing trick", 30),
         ("Check the expiry date on the shelf items before completing payment", "Validates product shelf life.", False, "check expiry date|fresh stock", 20)],
        ["blindly buy giant pack assuming cheaper", "ignore unit pricing", "assume marketing labels never mislead"],
        "Department of Consumer Affairs, Government of India", "https://consumeraffairs.nic.in"
    ))

    # MON-004: MRP and Checking Receipts
    cards.append(make_card(
        "MON-004", "coin", "Consumer Rights", "MRP laws and bill verification: Never overpay",
        ["junior", "middle", "senior"],
        ["Maximum Retail Price (MRP) is the legal ceiling in India; charging even one rupee above MRP is a punishable offense under Legal Metrology laws.",
         "Billing errors, duplicate scans, and unapplied promotional discounts occur regularly at checkout counters."],
        ["Always check the printed MRP on packaged bottles and snacks before handing over money", "Review itemized printed bills line-by-line before leaving the store premises", "Report vendors who charge extra for 'chilling' cold drinks to the National Consumer Helpline (1915)"],
        ["Never accept hand-written overcharges above the printed MRP", "Never leave a store without collecting a printed tax invoice or cash receipt"],
        "Shopkeepers have legal permission to charge extra 5 rupees above MRP for keeping drinks in their refrigerator.", "myth", "Under the Legal Metrology Act, MRP is all-inclusive of cooling, storage, and taxes. Overcharging is illegal.",
        "What should you do if a vendor demands 5 rupees extra above the printed MRP for a cold bottle of juice?",
        ["Quietly pay whatever they demand", "Point out the printed MRP and refuse to pay extra cooling charges", "Threaten physical violence", "Throw the bottle on the counter"], 1,
        "By Indian law, MRP includes all taxes and retailer margins; cooling is an overhead cost the shopkeeper cannot charge extra for.",
        ["At a tourist bus stand kiosk at {at}, {name} is handed a bottle of water with MRP Rs 20, but the shopkeeper insists on Rs 25 citing 'refrigeration fees'."],
        "How should {name} handle this consumer situation?",
        [("Politely point out the printed MRP of Rs 20 and state cooling fees are legally included", "Asserts legal consumer rights calmly.", True, "printed mrp 20|cooling fee illegal|legal metrology", 45),
         ("Decline to purchase and find an authorized vendor if the seller insists on overcharging", "Refuses to reward illicit retail extortion.", True, "refuse to pay extra|find honest vendor", 35),
         ("Know that consumer complaints can be registered on National Consumer Helpline 1915", "Utilizes official redressal mechanisms.", False, "helpline 1915|consumer forum", 20)],
        ["pay the illegal markup without checking", "engage in shouting match", "take goods without paying"],
        "National Consumer Helpline (NCH)", "https://consumerhelpline.gov.in"
    ))

    # MON-005: UPI & Digital Payment Safety
    cards.append(make_card(
        "MON-005", "coin", "Digital Finance", "UPI PIN safety: Enter PIN only to SEND money",
        ["middle", "senior"],
        ["Your UPI PIN (4 or 6 digits) is an authorization key to transfer money OUT of your bank account.",
         "Receiving money via UPI, Google Pay, PhonePe, or Paytm NEVER requires entering your PIN, scanning a QR code, or clicking an approval link."],
        ["Remember the golden rule: UPI PIN is ONLY entered when debited/paying, NEVER to receive funds", "Immediately decline any caller or buyer who asks you to 'enter PIN to collect cash prize'", "Check the beneficiary account name on the confirmation screen before hitting submit"],
        ["NEVER enter your UPI PIN on forms sent via SMS, WhatsApp, or OLX chats", "NEVER share your banking OTP or UPI PIN with bank managers or tech support"],
        "You must enter your UPI PIN to authenticate receiving cashback or money transfers from a buyer.", "myth", "Receiving money is completely automatic and requires zero PIN entries. If prompted for a PIN, money is leaving your account.",
        "A buyer on an online marketplace offers to pay you Rs 500 and sends a QR code saying 'Scan and enter PIN to receive payment'. What is happening?",
        ["It is a safe standard transaction", "It is an advance payment feature", "It is a scam designed to drain Rs 500 from your account", "It verifies your identity"], 2,
        "Scanning a QR code and entering a PIN always debits funds from your account, never credits it.",
        ["{name} is selling an old bicycle on an online portal. A buyer at {at} claims to have sent Rs 2,000 and messages: 'Accept request and enter your UPI PIN to claim money.'"],
        "What should {name} do?",
        [("Refuse to enter the UPI PIN, recognizing that receiving money never requires a PIN", "Demonstrates core digital banking awareness.", True, "never enter pin to receive|refuse request|scam attempt", 50),
         ("Check account balance directly in the official banking app without clicking chat links", "Verifies funds through secure independent channels.", True, "check banking app directly|do not click links", 30),
         ("Block and report the fraudulent buyer profile immediately", "Prevents further exploitation of community members.", False, "block and report scammer|cybercrime report", 20)],
        ["enter pin to test if money arrives", "share banking otp", "scan unverified qr code"],
        "Reserve Bank of India - Sachet Portal", "https://sachet.rbi.org.in"
    ))

    # MON-006: Minor Bank Accounts & Debit Cards
    cards.append(make_card(
        "MON-006", "coin", "Banking", "Minor savings accounts: Opening your first bank account",
        ["middle", "senior"],
        ["Indian banks allow minors above age 10 to operate independent savings bank accounts (like SBI Pehla Kadam) with debit cards and checkbooks.",
         "Holding a real bank account transitions youth from cash dependency to structured digital financial literacy."],
        ["Keep your physical debit card, CVV number, and ATM PIN strictly confidential", "Memorize your 4-digit ATM PIN and never write it down on the card surface or slip", "Check monthly bank passbook statements to verify account balance and interest earned"],
        ["Never let friends or strangers punch your ATM PIN on keypad screens", "Never throw away ATM transaction slips without tearing them into tiny shreds"],
        "Minors in India are legally forbidden from holding bank accounts or using ATM debit cards.", "myth", "Minors aged 10+ can operate savings accounts independently under RBI guidelines to cultivate financial discipline.",
        "Where is the safest place to record your newly issued ATM debit card PIN?",
        ["Written on the back of the debit card with permanent marker", "Stored in your head through memorization only", "Posted on your study desk whiteboard", "Shared in a family WhatsApp group"], 1,
        "ATM PINs must only be memorized. Writing it down invites unauthorized physical withdrawals if the card is misplaced.",
        ["{name} receives their first teenage debit card from their bank branch at {at}. A classmate asks to borrow the card to check how it works."],
        "How should {name} safeguard the new banking card?",
        [("Firmly refuse to hand over the debit card or disclose the secret PIN", "Establishes strict personal boundary around banking credentials.", True, "refuse to lend card|keep pin secret|memorize pin", 50),
         ("Memorize the PIN and scratch or cover the 3-digit CVV on the back", "Prevents unauthorized merchant card transactions.", True, "scratch cvv|keep secure|safe storage", 30),
         ("Review monthly passbook statements with parents to track deposits", "Practices ongoing account reconciliation.", False, "review passbook|track statements", 20)],
        ["lend debit card to friends", "write pin on debit card", "post card photo on social media"],
        "Reserve Bank of India Guidelines for Minor Accounts", "https://rbi.org.in"
    ))

    # MON-007: The Magic of Compound Interest
    cards.append(make_card(
        "MON-007", "coin", "Investing", "Compound interest: Earning interest on your interest",
        ["middle", "senior"],
        ["Albert Einstein famously called compound interest the 'eighth wonder of the world': you earn returns on your initial principal AND on accumulated returns.",
         "Time in the market is vastly more powerful than timing the market; starting at age 14 creates exponential growth compared to starting at age 30."],
        ["Start investing small amounts (even Rs 100/month via Recurring Deposit or PPF) as early as possible", "Let your investments grow undisturbed over years rather than withdrawing small profits prematurely", "Understand the Rule of 72: divide 72 by annual interest rate to find years needed to double money"],
        ["Never delay saving until your late twenties assuming small amounts don't matter", "Never confuse high-risk gambling with long-term compound investing"],
        "To build substantial wealth through compounding, you must start with hundreds of thousands of rupees.", "myth", "Compound growth relies on TIME and consistency, not large starting sums. Rs 500 invested monthly over decades creates massive wealth.",
        "If an investment pays an 8% annual return, roughly how many years will it take to double your money according to the Rule of 72?",
        ["2 years", "9 years (72 divided by 8)", "20 years", "72 years"], 1,
        "The Rule of 72 states 72 / 8 = 9 years to double your initial capital automatically.",
        ["{name} at {at} receives Rs 2,000 birthday gift. Option A is spending it on trendy branded sneakers; Option B is depositing it in a long-term compound savings bond."],
        "How should {name} evaluate this financial crossroads?",
        [("Recognize that early compounding allows small deposits to multiply exponentially over time", "Understands exponential compounding trajectory.", True, "early compounding|exponential growth|rule of 72", 45),
         ("Calculate how leaving money untouched over years builds financial freedom", "Appreciates patient delayed gratification.", True, "leave untouched|builds future cushion|patience", 35),
         ("Choose to invest the majority while keeping a modest sum for a small celebratory treat", "Strikes healthy balance between present reward and future security.", False, "split balance|invest majority|small treat", 20)],
        ["blow all money on temporary shoes", "dismiss small savings as useless", "borrow more to buy luxury goods"],
        "Securities and Exchange Board of India (SEBI) - Investor Education", "https://investor.sebi.gov.in"
    ))

    # MON-008: Borrowing & Lending Among Friends
    cards.append(make_card(
        "MON-008", "coin", "Debt & Borrowing", "Borrowing and lending: Preserving friendship and solvency",
        ["middle", "senior"],
        ["Informal loans between friends and peers cause severe social anxiety, broken friendships, and awkward school dynamics.",
         "Borrowing money for non-essential lifestyle wants creates toxic habits before adult life even begins."],
        ["Never borrow money to buy luxury items, treats, or impressionable outfits", "If you must borrow for an emergency (like fare), set an exact repayment deadline and pay early", "Only lend amounts you can afford to lose without destroying the friendship"],
        ["Never shy away from asking for your own money back when a promised deadline passes", "Never guarantee or take loans on behalf of another student"],
        "Borrowing small amounts from peers every week to fund snacks is completely harmless.", "myth", "Casual borrowing creates dependency, damages social trust, and blinds youth to their true spending habits.",
        "What is the healthiest rule regarding lending money to classmates?",
        ["Lend your entire monthly allowance without asking when they will return it", "Only lend small amounts you can comfortably afford not to get back, with clear repayment terms", "Charge 50% weekly interest", "Lend secretly without telling your parents"], 1,
        "Clear agreements and conservative limits protect both personal finances and personal relationships.",
        ["A close classmate at {at} asks {name} to lend Rs 300 to buy a video game, promising to repay 'sometime next month', but has an unpaid past debt."],
        "How should {name} navigate this friendship situation?",
        [("Politely decline the loan, explaining that personal money is budgeted for other commitments", "Sets clear boundaries without aggression.", True, "politely decline|budgeted elsewhere|firm boundary", 45),
         ("Remind the friend calmly about the previous unsettled amount", "Holds friends accountable to past commitments.", True, "previous unsettled balance|clear accountability", 35),
         ("Suggest free alternative games or ways they can earn the money directly", "Offers constructive support without funding debt.", False, "suggest free alternatives|constructive support", 20)],
        ["lend money out of social guilt", "fight violently over old loans", "steal family cash to lend"],
        "National Institute of Securities Markets (NISM)", "https://nism.ac.in"
    ))

    # MON-009: Spotting "Double Your Money" Scams
    cards.append(make_card(
        "MON-009", "coin", "Scam Awareness", "Pyramid schemes & fake returns: If it's too good to be true, it's fake",
        ["middle", "senior"],
        ["No legitimate financial instrument guarantees 20%, 50%, or 100% returns in days or weeks; bank savings yield ~3-7% annually.",
         "Multi-level marketing (MLM) and Telegram crypto bots recruit students by displaying fake rented supercars and fake screenshots."],
        ["Remember: High guaranteed returns with zero risk ALWAYS indicate an illegal Ponzi scam", "Verify financial firms on official SEBI or RBI directories before trusting claims", "Warn peers when a club or senior asks for 'entry fee' to recruit downlines"],
        ["NEVER invest money into Telegram trading signals or Instagram 'fund doubling' groups", "NEVER recruit friends into schemes that pay commissions purely for enrolling new members"],
        "If a senior shows real bank account balance screenshots proving they doubled money in 3 days, the app must be genuine.", "myth", "Balance screenshots are easily fabricated with inspect element or dummy apps to bait gullible recruits.",
        "What is the universal hallmark of a fraudulent pyramid or Ponzi scheme?",
        ["Regulated by SEBI and audited annually", "Promises guaranteed astronomical returns with no risk and rewards recruiting friends", "Provides printed tax invoices for all transactions", "Requires years of patient disciplined compounding"], 1,
        "Guaranteed rapid profits paired with pressure to recruit friends is the textbook definition of an illegal pyramid scheme.",
        ["A senior student invites {name} to a cafe at {at}, presenting an app: 'Deposit Rs 1,000 today, get Rs 2,000 next Monday, plus Rs 500 for every junior you sign up!'"],
        "How should {name} respond?",
        [("Identify this immediately as an illegal Ponzi / pyramid scheme and refuse to participate", "Recognizes predatory recruitment structure.", True, "ponzi scheme|pyramid scam|refuse to join", 50),
         ("Refuse to recruit classmates or risk personal savings", "Protects peer community from financial harm.", True, "refuse to recruit peers|protect savings", 30),
         ("Report the recruiting activity to school authorities or the RBI Sachet portal", "Takes civic action to stop exploitation.", False, "report to school|rbi sachet portal", 20)],
        ["invest savings to test app", "convince best friends to join for bonus", "borrow money to invest"],
        "RBI Sachet Portal against Illegal Deposit Schemes", "https://sachet.rbi.org.in"
    ))

    # MON-010: Online Shopping Traps & Dark Patterns
    cards.append(make_card(
        "MON-010", "coin", "Digital Literacy", "Dark patterns: Deceptive tricks in shopping apps",
        ["junior", "middle", "senior"],
        ["Dark patterns are user-interface tricks designed to manipulate you into spending money, such as fake countdown timers and stealth subscriptions.",
         "The Ministry of Consumer Affairs has legally prohibited 13 deceptive dark patterns in Indian e-commerce."],
        ["Look out for pre-ticked checkboxes adding travel insurance, charity donations, or subscriptions", "Ignore flashing 'Only 2 items left at this price!' banners designed to induce synthetic panic", "Always check the final checkout total before clicking the final 'Pay' button"],
        ["Never make purchases in an emotional state of artificial scarcity", "Never save credit/debit card credentials on casual gaming or shopping websites"],
        "Websites display 'Only 1 left in stock!' purely as a helpful public service to alert shoppers.", "myth", "E-commerce apps regularly code artificial countdown clocks and stock counters to trigger impulse purchases via urgency.",
        "Which of the following is an example of an illegal e-commerce 'dark pattern'?",
        ["Displaying accurate dimensions of a backpack in centimeters", "Pre-ticking a paid magazine subscription box during checkout without your consent", "Showing clear return policies", "Offering customer service phone numbers"], 1,
        "Sneaking paid items into your cart via pre-ticked checkboxes is a banned dark pattern known as 'sneak into basket'.",
        ["While ordering a book online at {at}, {name} notices the checkout bill increased by Rs 99 due to an auto-checked 'VIP Delivery Pass'."],
        "What action should {name} take?",
        [("Spot the pre-checked dark pattern box and uncheck it to remove the unwanted fee", "Demonstrates vigilance against interface tricks.", True, "uncheck hidden box|remove dark pattern|verify bill total", 50),
         ("Carefully review every line item before approving digital payment", "Practices thorough checkout audit.", True, "review line items|check final total", 30),
         ("Complain to the platform or Consumer Helpline if hidden fees cannot be deselected", "Uses consumer protection remedies.", False, "report hidden charges|consumer helpline", 20)],
        ["click pay without checking total", "assume added charge is mandatory government tax", "save card details on untrusted site"],
        "Central Consumer Protection Authority (CCPA) - Dark Patterns Guidelines", "https://consumeraffairs.nic.in"
    ))

    # MON-011: Fair Earning & Value Creation
    cards.append(make_card(
        "MON-011", "coin", "Earning", "Earning your first rupee: Providing genuine value",
        ["middle", "senior"],
        ["Money is earned by solving problems and delivering genuine value to people, not through luck or wishing.",
         "Young people can build legitimate income through skills like tutoring juniors, coding basic websites, pet sitting, or crafting."],
        ["Identify a real skill you possess (e.g., maths tutoring, digital art, gardening) that others need", "Agree on scope of work, timeline, and fair compensation upfront before starting a task", "Deliver high-quality work punctually to build personal reputation and word-of-mouth trust"],
        ["Never take on freelance work that violates child labor protections or interferes with school attendance", "Never misrepresent your qualifications or plagiarize client work"],
        "Making money online as a teenager only happens through viral dance videos or gaming streams.", "myth", "Most sustainable freelance income comes from practical micro-skills like design, tutoring, transcription, and neighborhood assistance.",
        "What is the fundamental basis of legitimate economic earnings?",
        ["Convincing people through deception", "Solving a real problem and providing genuine value to others", "Hoping for lottery windfalls", "Borrowing without intent to repay"], 1,
        "All enduring commerce is an exchange of value: helping someone save time, learn a skill, or solve a practical problem.",
        ["During school summer holidays at {at}, {name} wants to earn money legitimately to purchase a computer course."],
        "What is the most constructive approach for {name}?",
        [("Offer structured academic tutoring to neighborhood primary students in weak subjects", "Builds service based on genuine competence.", True, "offer tutoring|teach juniors|solve academic problem", 45),
         ("Define clear hourly rates and obtain parental approval before commencing", "Maintains transparency and safety.", True, "set clear rate|parental approval|schedule", 35),
         ("Deliver every tutoring session punctually with prepared notes and patience", "Builds sterling reputation and reliability.", False, "punctual delivery|high quality work", 20)],
        ["join get-rich-quick telegram channels", "neglect studies for odd jobs", "charge money for homework copying"],
        "Ministry of Skill Development and Entrepreneurship", "https://msde.gov.in"
    ))

    # MON-012: Festival & Gift Money Wisdom
    cards.append(make_card(
        "MON-012", "coin", "Saving Strategy", "Handling festival and shagun cash: Avoid the windfall trap",
        ["junior", "middle", "senior"],
        ["Windfall cash (Diwali shagun, Eid eidi, birthday envelopes) triggers a mental accounting bias where we treat it as 'free money' to squander.",
         "Treating gift cash with the same discipline as earned income accelerates savings goals by years."],
        ["Deposit at least 50% of any festival gift cash directly into long-term savings or an RD", "Use a modest 25% for a meaningful personal celebration or sharing with family", "Keep a personal ledger noting who gifted what so you cultivate genuine gratitude"],
        ["Never rush to the market within an hour of receiving gift money to spend it on impulse toys", "Never brag about gift amounts to peers or compare shagun envelopes"],
        "Money received as a birthday or festival gift does not count as real money and should be spent instantly.", "myth", "Gift cash has identical purchasing power to hard-earned salary; squandering it wastes prime compounding opportunities.",
        "What is the smartest financial habit when receiving festival cash from grandparents?",
        ["Spend 100% immediately on firecrackers and candy", "Allocate a significant portion to your savings fund while reserving a small portion for a treat", "Hide it in a textbook and forget about it for 10 years", "Hand it to strangers"], 1,
        "Splitting windfall cash balances present celebration with meaningful asset accumulation.",
        ["After family celebrations at {at}, {name} receives Rs 3,000 in cash envelopes from relatives."],
        "How should {name} allocate this windfall?",
        [("Allocate at least Rs 1,500 - Rs 2,000 into a bank deposit or designated savings goal", "Captures windfall for meaningful future utility.", True, "save 50% or more|deposit in bank|long term goal", 45),
         ("Reserve a planned portion for a thoughtful personal book, game, or family treat", "Enjoys celebration mindfully without guilt.", True, "budgeted treat|meaningful celebration", 35),
         ("Thank each relative warmly with handwritten gratitude notes", "Cultivates interpersonal respect and humility.", False, "thank relatives|cultivate gratitude", 20)],
        ["squander all 3000 in one afternoon", "boast about cash to friends", "gamble on arcade machines"],
        "National Centre for Financial Education", "https://ncfe.org.in"
    ))

    # MON-013: Inflation Explained
    cards.append(make_card(
        "MON-013", "coin", "Macroeconomics", "Inflation: Why 100 rupees buys less over time",
        ["middle", "senior"],
        ["Inflation is the general increase in prices over time, which reduces the purchasing power of your money.",
         "If inflation is 6% per year, an item that costs Rs 100 today will cost Rs 106 next year; cash hidden in a drawer loses value every day."],
        ["Understand that money sitting in physical cash loses purchasing power every year", "Look for savings instruments (like PPF or mutual funds via parents) that beat inflation rates", "Calculate real returns: Nominal interest rate minus inflation rate equals real wealth growth"],
        ["Never assume money kept in a piggy bank remains 'safe' from purchasing power erosion", "Never ignore inflation when planning multi-year savings goals like college education"],
        "Keeping paper currency notes hidden under your mattress is the safest way to preserve your family's wealth.", "myth", "While physical notes won't disappear, inflation steadily eats away what those notes can buy. In 15 years, their real purchasing value drops by half.",
        "If a chocolate bar costs Rs 50 today and annual inflation is 6%, what will happen to the price in future years?",
        ["It will become free", "The price will gradually increase over time", "The price will decrease to Rs 10", "Inflation has no effect on goods"], 1,
        "Inflation causes the general price level of goods and services to increase over time.",
        ["At home at {at}, {name} considers keeping Rs 5,000 cash in a secret metal box for five years versus depositing it into an interest-bearing bank account."],
        "How should {name} reason through this decision?",
        [("Recognize that inflation will erode the purchasing power of idle paper cash over five years", "Understands real purchasing power loss.", True, "inflation erodes cash|purchasing power drops|idle cash loses value", 50),
         ("Choose an interest-bearing bank deposit to earn returns that offset price rises", "Selects productive financial vehicles.", True, "bank deposit earns interest|beat inflation", 30),
         ("Learn to calculate real return by comparing interest rates against inflation", "Applies quantitative financial logic.", False, "real return|nominal rate minus inflation", 20)],
        ["hide money under mattress forever", "ignore inflation completely", "assume bank interest is a scam"],
        "Reserve Bank of India - Inflation Metrics", "https://rbi.org.in"
    ))

    # MON-014: Understanding Insurance Basics
    cards.append(make_card(
        "MON-014", "coin", "Risk Protection", "Insurance basics: Protecting against financial catastrophe",
        ["middle", "senior"],
        ["Insurance is a collective safety net where many people pay small regular premiums to protect against rare but devastating financial disasters.",
         "Without health and life insurance, a single hospital emergency can wipe out an entire family's life savings and force them into predatory debt."],
        ["Understand that insurance is protection against catastrophic risk, not an investment to make you rich", "Know the difference: Health insurance pays hospital bills; Term life insurance protects family if an earning parent passes away", "Check that vehicle third-party insurance is always active before driving"],
        ["Never view insurance premiums as 'wasted money' just because no disaster happened this year", "Never hide medical pre-existing conditions when filling insurance declaration forms"],
        "Buying health insurance is a complete waste of money if you stay healthy and don't visit a hospital.", "myth", "Insurance is peace of mind against catastrophic bankruptcy. You pay a small fee so a unexpected critical illness does not ruin your family.",
        "What is the primary fundamental purpose of health and life insurance?",
        ["To make you a stock market millionaire overnight", "To protect individuals and families from catastrophic financial ruin during unforeseen emergencies", "To avoid paying all municipal taxes", "To borrow money without interest"], 1,
        "Insurance pools risk to ensure unexpected medical shocks or accidents do not plunge households into poverty.",
        ["During a family discussion at {at}, a relative suggests canceling family health insurance to save Rs 15,000 annual premium."],
        "How can {name} explain the importance of insurance retention?",
        [("Explain that an unexpected surgery or hospital stay can cost lakhs and wipe out savings", "Articulates catastrophic risk mitigation.", True, "hospital emergency costs lakhs|wipes out savings|protect family", 50),
         ("Clarify that insurance is a risk shield rather than a profit-making scheme", "Differentiates protection from investment.", True, "risk shield not profit|peace of mind", 30),
         ("Recommend comparing policy features rather than eliminating essential coverage", "Suggests constructive optimization.", False, "compare policies|maintain basic coverage", 20)],
        ["cancel insurance to buy gadgets", "assume young people never get sick", "hide medical facts"],
        "Insurance Regulatory and Development Authority of India (IRDAI)", "https://irdai.gov.in"
    ))

    # MON-015: Understanding a Pay Slip & Deductions
    cards.append(make_card(
        "MON-015", "coin", "Work & Salary", "Decoding a pay slip: Gross salary vs In-hand pay",
        ["senior"],
        ["Gross salary is the total compensation promised; Net salary (in-hand) is what actually enters your bank account after mandatory deductions.",
         "Deductions include Employee Provident Fund (EPF for retirement), Professional Tax, and Income Tax (TDS)."],
        ["Understand that a job offering 'Rs 50,000 CTC' will not deliver Rs 50,000 cash into your account each month", "Learn what EPF (Provident Fund) is: a mandatory retirement nest-egg where your employer matches your contribution", "Check that your Permanent Account Number (PAN) is correctly linked to tax deductions"],
        ["Never sign an employment contract without examining the itemized CTC breakdown", "Never ignore tax planning until the final month of the financial year"],
        "If a job offer letter states a salary of Rs 60,000 per month, exactly Rs 60,000 will be transferred to your bank account.", "myth", "Gross salary undergoes statutory deductions like PF, income tax, and health insurance; net in-hand is always lower.",
        "What is the crucial difference between 'Gross Salary' and 'Net Salary' on an employee pay slip?",
        ["There is no difference", "Gross is total compensation before deductions; Net is the actual amount credited to your bank account", "Gross is paid in cash, Net in coupons", "Net is always double the gross amount"], 1,
        "Net salary equals Gross salary minus statutory taxes, provident fund contributions, and insurance deductions.",
        ["A young family member at {at} receives their first job offer letter boasting 'Rs 40,000 monthly CTC' but the bank transfer is Rs 33,500."],
        "How can {name} help them understand their pay slip breakdown?",
        [("Review the pay slip to identify deductions like EPF retirement savings and income tax", "Analyzes itemized pay stub deductions.", True, "review deductions|provident fund epf|income tax tds", 45),
         ("Explain that EPF deduction is not lost money, but a forced savings asset matched by the employer", "Clarifies long-term retirement value.", True, "epf is personal retirement asset|matched by employer", 35),
         ("Help verify that the Employer PAN and UAN numbers are accurately recorded", "Ensures compliance and record accuracy.", False, "check uan number|verify pan", 20)],
        ["accuse company of wage theft without reading slip", "ignore retirement contributions", "refuse to pay statutory taxes"],
        "Employees' Provident Fund Organisation (EPFO)", "https://epfindia.gov.in"
    ))

    # MON-016: Resisting Peer Pressure Spending
    cards.append(make_card(
        "MON-016", "coin", "Social Dynamics", "Peer pressure spending: Confidence without designer labels",
        ["middle", "senior"],
        ["Many teenagers go broke trying to impress classmates with expensive sneakers, branded cafes, and designer stationery.",
         "True personal security and self-worth come from competence, character, and kindness—not clothing logos."],
        ["Practice saying comfortably: 'That's out of my budget right now, but let's hang out in the park'", "Recognize that genuine friends respect your financial honesty; only shallow peers judge your clothing brands", "Calculate how many hours of work or study an expensive luxury item costs before buying"],
        ["Never steal, borrow recklessly, or lie to your parents to keep up with wealthy peers' spending", "Never look down on classmates who carry simple cloth bags or homemade lunchboxes"],
        "Wearing expensive designer brands is the only proven way to earn genuine respect and popularity in school.", "myth", "Brand obsession signals insecurity. Real leadership, warmth, athletic or artistic skill, and wit command far greater respect.",
        "What is the most emotionally mature response when friends suggest an expensive cafe you cannot afford?",
        ["Lie that you already ate, then secretly borrow money", "Confidently state: 'That place is outside my budget, how about we grab street chai or hang in the library?'", "Insult your friends for being rich", "Steal money from your parents' wallet"], 1,
        "Owning your budget with calm confidence earns peer respect and prevents toxic debt traps.",
        ["At school at {at}, {name}'s friend group plans a weekend outing to an upscale restaurant with Rs 1,000 per head cover charge, which exceeds {name}'s allowance."],
        "What is the best course of action for {name}?",
        [("State calmly and without shame that the restaurant exceeds your current budget", "Practices authentic boundary assertion.", True, "outside my budget|honest boundary|no shame", 45),
         ("Propose an affordable alternative or offer to join them afterwards for a walk in the park", "Preserves social connection constructively.", True, "propose alternative|join for walk|affordable spot", 35),
         ("Refuse to pressure parents into funding non-essential luxury outings", "Protects family financial wellbeing.", False, "do not pressure parents|protect family budget", 20)],
        ["borrow cash to fake wealth", "lie and make up fake illnesses", "steal from family"],
        "National Mental Health Programme - Life Skills Education", "https://mohfw.gov.in"
    ))

    # MON-017: In-App Gaming Purchases & Loot Boxes
    cards.append(make_card(
        "MON-017", "coin", "Digital Spending", "In-app gaming traps: Microtransactions and loot boxes",
        ["junior", "middle", "senior"],
        ["Free-to-play mobile games are engineered by behavioral psychologists to trigger dopamine loops and loot-box gambling addictions.",
         "Microtransactions of 'just Rs 49' accumulate into thousands of rupees drained from linked parental cards within days."],
        ["Never link your parent's UPI or credit card directly to Google Play or Apple App Store without biometric confirmation", "Understand that virtual weapon skins and character outfits have zero real-world resale value", "Set a hard monthly cap of Rs 0 on randomized loot boxes, treating them as gambling mechanisms"],
        ["NEVER secretly use a parent's phone to authorize gaming purchases", "NEVER fall for third-party websites promising 'free diamonds' or 'unlimited game coins' in exchange for account logins"],
        "Loot boxes in mobile games are completely harmless games of skill.", "myth", "Loot boxes employ variable-ratio reinforcement schedules identical to slot machines, creating addictive spending spirals.",
        "Why do mobile games convert real currency into virtual gems, diamonds, or coins before you purchase items?",
        ["To comply with international space law", "To psychologically detach you from the feeling of spending real rupee money", "Because banks cannot process rupees", "To give away free bonuses"], 1,
        "Virtual tokens obscure real-world monetary value, making gamers spend far more impulsively.",
        ["While playing a mobile battle-royale game at {at}, {name} is tempted to spend Rs 799 on a limited-time legendary weapon skin using a parent's pre-linked payment profile."],
        "What should {name} do?",
        [("Stop and recognize that virtual game skins deliver zero real-world value and will be obsolete in months", "Critically evaluates virtual asset utility.", True, "virtual skin has zero value|game trap|resist urge", 45),
         ("Always ask explicit parental permission before making any digital purchase", "Practices transparency with guardians.", True, "parental consent|ask permission first", 35),
         ("Advise removing saved payment methods to avoid accidental one-click debits", "Eliminates frictionless spending risks.", False, "remove saved card|disable one click pay", 20)],
        ["secretly click purchase hoping parents wont notice", "steal otp from parent phone", "visit shady gem generator sites"],
        "Ministry of Electronics and Information Technology (MeitY) - Online Gaming Rules", "https://meity.gov.in"
    ))

    # MON-018: Setting a Specific Savings Target
    cards.append(make_card(
        "MON-018", "coin", "Goal Setting", "SMART financial goals: Turning dreams into savings plans",
        ["junior", "middle", "senior"],
        ["Vague goals like 'I want to save money' fail; SMART financial goals (Specific, Measurable, Achievable, Relevant, Time-bound) succeed.",
         "Breaking a Rs 2,400 bicycle repair target into Rs 200 saved per month over 12 months makes huge goals easily achievable."],
        ["Write down the exact item, total cost, target date, and required weekly savings amount", "Create a visual progress tracker (thermometer chart or checklist) on your study desk", "Celebrate reaching 25%, 50%, and 75% milestones without spending the accumulated corpus"],
        ["Never leave your savings goals abstract without a written number and deadline", "Never abandon a goal just because an unexpected expense slowed your progress by two weeks"],
        "Writing down your savings goals makes no measurable difference to whether you achieve them.", "myth", "Studies in behavioral economics show written, visual goal tracking increases savings completion rates by over 40%",
        "Which of the following represents a properly structured 'SMART' financial goal?",
        ["'I want to be rich someday'", "'I will save Rs 300 every month for 6 months to buy a Rs 1,800 science telescope by December'", "'I will stop spending money forever'", "'I hope someone gifts me a computer'"], 1,
        "It includes a specific item, exact target amount, defined monthly saving rate, and a clear deadline.",
        ["{name} dreams of buying a Rs 1,200 scientific calculator for class 11 at {at} in four months."],
        "How should {name} organize this savings plan?",
        [("Calculate the required rate: Rs 1,200 divided by 4 months equals Rs 300 per month (Rs 75/week)", "Applies quantitative milestone planning.", True, "divide 1200 by 4 months|300 per month|75 per week", 50),
         ("Set up a dedicated physical envelope or digital sub-wallet labeled 'Calculator Fund'", "Creates dedicated purpose-driven bucket.", True, "dedicated envelope|calculator fund|visual tracker", 30),
         ("Track progress weekly in a notebook to ensure discipline until the goal is achieved", "Maintains ongoing accountability.", False, "track weekly progress|maintain discipline", 20)],
        ["wait until exam day and borrow money", "give up because 1200 feels too big", "spend savings halfway on snacks"],
        "National Centre for Financial Education - SMART Goals Workbook", "https://ncfe.org.in"
    ))

    return cards


def get_forge_cards():
    cards = []

    # ENT-001: Spotting Everyday Problems
    cards.append(make_card(
        "ENT-001", "forge", "Problem Discovery", "Spotting real problems: Where every great venture begins",
        ["junior", "middle", "senior"],
        ["Entrepreneurs do not start with products; they start with genuine human frustrations, inefficiencies, and unmet needs.",
         "The best student inventions solve everyday frictions they experience firsthand in school, transit, or neighborhood life."],
        ["Keep a 'Bug List' notebook where you write down 3 things that annoyed or slowed people down each day", "Listen carefully to customer complaints: 'I hate waiting in this queue' is a direct business opportunity", "Observe how people create makeshift hacks to solve problems—that hack is your product prototype"],
        ["Never start building a gadget or software without verifying that real people actually suffer from that problem", "Never fall in love with your solution before falling in love with the problem"],
        "Great business ideas come exclusively from sudden lightning bolts of genius inspiration.", "myth", "Vast majority of successful ventures originate from disciplined observation of everyday frictions and inefficiencies.",
        "What is the most effective starting point for creating a successful student enterprise?",
        ["Designing a flashy logo before anything else", "Identifying an unsolved recurring frustration that people already complain about", "Copying an American tech company blindly", "Borrowing huge bank loans"], 1,
        "Businesses exist to solve real problems. Without an authentic pain point, products have no willing buyers.",
        ["In the school library at {at}, {name} notices students constantly struggle to find available reference books because index cards are misplaced and torn."],
        "How should {name} approach this as an aspiring student builder?",
        [("Interview 5 classmates and the librarian to pinpoint exact friction points in locating books", "Conducts foundational customer problem discovery.", True, "interview students and librarian|pinpoint friction|listen to users", 45),
         ("Document the recurring pain point in a problem log before jumping into complex coding", "Validates the real need thoroughly.", True, "document pain point|validate need before building", 35),
         ("Observe what temporary hacks students currently use to find books", "Studies existing informal workarounds.", False, "observe current hacks|workarounds", 20)],
        ["build an expensive app without talking to anyone", "ignore the issue as not my job", "print random posters"],
        "Atal Innovation Mission (AIM) - NITI Aayog", "https://aim.gov.in"
    ))

    # ENT-002: Brainstorming Without Judgment
    cards.append(make_card(
        "ENT-002", "forge", "Ideation", "Brainstorming without judgment: Divergent thinking",
        ["junior", "middle", "senior"],
        ["Effective ideation has two distinct phases: Divergent thinking (generating wild quantity) and Convergent thinking (filtering feasibility).",
         "Critiquing ideas early kills psychological safety and stops bold breakthroughs from ever surfacing."],
        ["Set a timer for 10 minutes and aim for at least 30 diverse ideas without evaluating any of them", "Encourage wild, unconventional ideas—it is easier to tame a wild idea than invigorate a boring one", "Build upon teammates' concepts using the phrase 'Yes, and...' rather than 'No, but...'"],
        ["Never ridicule a teammate's wild suggestion during the initial ideation phase", "Never allow one dominant voice to monopolize the brainstorming whiteboard"],
        "In a brainstorming session, you should immediately reject impossible or absurd ideas as soon as they are mentioned.", "myth", "Judging too early kills creative momentum. Absurd ideas often spark practical, revolutionary hybrid solutions.",
        "Which conversational phrase encourages creative team ideation best?",
        ["'That will never work'", "'That sounds too expensive'", "'Yes, and we could also add...'", "'Our competitors already do that'"], 2,
        "'Yes, and...' accepts the premise and builds upon it, fostering psychological safety and compounding creativity.",
        ["During an innovation club session at {at}, a quiet team member suggests using origami paper folding to package eco-friendly seed balls, but another student laughs."],
        "How should {name} facilitate the team dynamic?",
        [("Remind the team that early brainstorming strictly suspends criticism to foster novel concepts", "Protects divergent psychological safety.", True, "suspend criticism|protect brainstorming|encourage wild ideas", 45),
         ("Build on the idea with 'Yes, and we can test recycled newspaper instead of fresh paper'", "Uses constructive ideation phrasing.", True, "yes and|build on concept|recycled paper", 35),
         ("Ensure everyone gets uninterrupted turns to pitch their ideas onto the board", "Maintains inclusive team participation.", False, "uninterrupted turns|inclusive whiteboard", 20)],
        ["join in mocking the unconventional idea", "shut down the session in anger", "let only the loudest student speak"],
        "Design Thinking for Educators - IDEO", "https://designthinkingforeducators.com"
    ))

    # ENT-003: Building a Team & Assigning Roles
    cards.append(make_card(
        "ENT-003", "forge", "Teamwork", "The builder trifecta: Hacker, Hustler, and Designer",
        ["middle", "senior"],
        ["Enduring projects need diverse skill sets: the Builder (technical/craft), the Hustler (business/sales), and the Designer (user experience/storyteller).",
         "Teams composed of clones with identical skills frequently fight over identical tasks and neglect essential sales and aesthetics."],
        ["Map each team member's natural strengths rather than assigning roles by friend popularity", "Define clear owners for key pillars: Product Quality, Customer Outreach, and Visual Identity", "Establish a weekly standup meeting where everyone answers: What did I do? What is next? Am I blocked?"],
        ["Never form a team where everyone wants to code or craft but no one wants to talk to customers", "Never leave responsibilities ambiguous so tasks fall through the cracks"],
        "The best venture teams are formed by three best friends who all share the exact same strengths and hobbies.", "myth", "Homogeneous teams leave massive blind spots in marketing, finance, or design. Complementary diversity drives success.",
        "In classic venture building, what is the primary responsibility of the 'Hustler' role?",
        ["Writing backend server code", "Talking to customers, securing sales, partnerships, and managing money", "Drawing vector logo art", "Cleaning the office floor"], 1,
        "The hustler drives customer acquisition, communication, resource management, and commercial sustainability.",
        ["At the science fair team registration at {at}, four friends all want to design the robotic arm, but no one wants to prepare the presentation deck or speak to judges."],
        "How should {name} guide the team allocation?",
        [("Identify individual complementary strengths across building, communication, and visual design", "Allocates roles based on functional diversity.", True, "complementary roles|builder hustler designer|balanced team", 45),
         ("Assign a dedicated communicator/hustler responsible for judge presentations and user testing", "Ensures vital outreach is not neglected.", True, "dedicated communicator|judge presentation|clear ownership", 35),
         ("Establish clear shared accountability and celebrate all roles equally", "Prevents status hierarchy among teammates.", False, "equal respect|shared accountability", 20)],
        ["let all four fight over the same robotic motor", "force one person to do everything alone", "quit the competition"],
        "Startup India - DPIIT", "https://startupindia.gov.in"
    ))

    # ENT-004: The 60-Second Elevator Pitch
    cards.append(make_card(
        "ENT-004", "forge", "Communication", "The 60-second elevator pitch: Hook, problem, solution, ask",
        ["junior", "middle", "senior"],
        ["An elevator pitch summarizes your venture in under a minute: Hook, Problem, Solution, Traction/Secret Sauce, and the Ask.",
         "If you cannot explain your project clearly in 60 seconds to a 10-year-old, you do not understand it well enough."],
        ["Structure your pitch: 'We help [Target User] solve [Urgent Problem] through [Unique Solution]'", "Hook the listener in the first 10 seconds with a striking fact or relatable scenario", "End with a concrete 'Ask' (e.g., 'We are looking for 10 beta testers' or 'Rs 500 seed material')"],
        ["Never recite complex technical jargon or buzzwords that confuse listeners", "Never exceed your time limit during school pitch competitions"],
        "An elevator pitch should cram in every single technical line of code and feature specification.", "myth", "Pitches are designed to spark curiosity and secure a follow-up conversation, not deliver an exhaustive user manual.",
        "What are the four essential building blocks of a concise 60-second pitch?",
        ["Logo, office address, favorite color, price tag", "Hook, Problem, Solution, and Clear Ask", "Technical dictionary, apologies, long backstory, resume", "Jokes, complaints, excuses, phone number"], 1,
        "Hook catches attention, Problem establishes urgency, Solution shows value, and the Ask specifies next steps.",
        ["At the school innovation challenge at {at}, {name} has 60 seconds to present their solar-powered backpack charger to a panel of busy teachers."],
        "How should {name} structure the presentation?",
        [("Open with a sharp hook on students losing phone battery during emergency commutes", "Captures immediate panel interest.", True, "sharp hook|emergency commute problem|grab attention", 40),
         ("Explain the solar charging backpack solution clearly without technical jargon", "Articulates value proposition simply.", True, "clear solution|solar backpack|no jargon", 35),
         ("Conclude with a clear ask for student testers to trial the prototype next week", "Provides actionable next step.", True, "clear ask|recruit testers|actionable finish", 25)],
        ["ramble about solar physics for 55 seconds without stating what the product is", "exceed time limit", "read monotonously from paper"],
        "Atal Innovation Mission - Pitch Deck Guidelines", "https://aim.gov.in"
    ))

    # ENT-005: Setting Up a School Event Stall
    cards.append(make_card(
        "ENT-005", "forge", "Sales & Retail", "Running a school carnival stall: Unit economics and cash floats",
        ["junior", "middle", "senior"],
        ["A successful retail stall requires knowing your Cost of Goods Sold (COGS), setting a profitable price, and keeping an exact cash float for change.",
         "Revenue is not profit; if you make Rs 2,000 in sales but spent Rs 1,800 on ingredients, your actual profit is only Rs 200."],
        ["Calculate unit cost: total ingredient/material expense divided by number of servings produced", "Price items to cover costs plus a 30-50% profit margin while remaining affordable for students", "Prepare a cash box with plenty of Rs 10, Rs 20, and Rs 50 notes and coins for customer change"],
        ["Never consume stall food or give freebies to friends without accounting for them in the ledger", "Never leave the stall cash box unattended at any time"],
        "If your stall collects Rs 3,000 cash in the cash box at the end of the day, your team has earned Rs 3,000 profit.", "myth", "Gross sales revenue must subtract material costs, stall entry fees, and packaging before net profit is known.",
        "If you spend Rs 300 to make 30 bookmarks and sell all 30 at Rs 20 each, what is your net profit?",
        ["Rs 600", "Rs 300 (Rs 600 revenue minus Rs 300 cost)", "Rs 20", "Rs 1,000"], 1,
        "Net Profit = Total Revenue (30 x 20 = Rs 600) minus Total Cost (Rs 300) = Rs 300.",
        ["{name}'s student club at {at} prepares homemade lemonade for the annual sports day carnival."],
        "How should {name} manage the stall's financial operations?",
        [("Tally all expenses for lemons, sugar, cups, and ice to calculate exact unit cost per cup", "Establishes accurate cost of goods sold.", True, "tally expenses|calculate unit cost|track cogs", 45),
         ("Maintain an organized cash box with small change and record every sale in a ledger", "Ensures cash flow integrity and customer service.", True, "cash box with change|record sales|ledger", 35),
         ("Calculate net profit only after fully reimbursing initial material costs", "Applies strict financial discipline.", False, "net profit after costs|reimburse seed money", 20)],
        ["eat stock without paying", "leave cash box open on table", "assume all revenue is pure profit"],
        "National Institute for Micro, Small and Medium Enterprises (NI-MSME)", "https://nimsme.org"
    ))

    # ENT-006: Learning from Early Rejection & Failure
    cards.append(make_card(
        "ENT-006", "forge", "Resilience", "Embracing failure: 'No' is just data, not defeat",
        ["junior", "middle", "senior"],
        ["Every renowned entrepreneur faced dozens of rejections before finding product-market fit; rejection is simply market feedback.",
         "Treating failure as learning (iteration) separates enduring creators from those who give up at the first hurdle."],
        ["When someone says 'No thanks', ask politely: 'Could you share what you would change about this?'", "Keep an 'Iteration Log' tracking what worked, what flopped, and what adjustment to test next", "Separate your personal self-worth from your product prototype; your idea was rejected, not you"],
        ["Never take constructive customer feedback as a personal insult or attack", "Never repeat the exact same flawed pitch without modifying your approach"],
        "If the first five customers you approach reject your product, you should immediately quit entrepreneurship.", "myth", "Early rejection is standard. World-class founders test hundreds of iterations based on early critique before finding traction.",
        "What is the most constructive response when a customer declines to buy your homemade product?",
        ["Argue with them angrily", "Politely ask what feature or pricing would make it genuinely useful to them", "Cry in the hallway", "Lower the price to zero"], 1,
        "Customer objections provide the exact roadmap needed to refine product features and value.",
        ["At the craft fair at {at}, {name}'s hand-painted clay pots receive zero purchases in the first three hours while visitors walk past."],
        "How should {name} respond constructively?",
        [("Step out and politely ask browsing visitors what designs or products they were hoping to find", "Gathers rapid customer discovery feedback.", True, "ask visitors feedback|listen to objections|market discovery", 45),
         ("Notice that visitors are asking for functional drainage holes or smaller desk sizes", "Identifies concrete product improvement opportunities.", True, "identify missing features|drainage holes|adjust size", 35),
         ("Pivot the display and signage to highlight practical desk utility rather than giving up", "Executes an immediate iterative pivot.", False, "pivot display|test adjustments|resilience", 20)],
        ["pack up and leave in despair", "insult customers for having poor taste", "slash prices below material costs"],
        "National Skill Development Corporation (NSDC)", "https://nsdcindia.org"
    ))

    # ENT-007: Gathering Honest Customer Feedback
    cards.append(make_card(
        "ENT-007", "forge", "User Research", "The Mom Test: Gathering genuinely honest customer feedback",
        ["middle", "senior"],
        ["Asking 'Do you like my idea?' prompts friends and family to lie politely to avoid hurting your feelings.",
         "The famous 'Mom Test' rule: Ask about their past behaviors, real habits, and actual money spent, never theoretical opinions."],
        ["Ask: 'How do you currently handle this problem?' rather than 'Would you buy my app?'", "Look for evidence of action: If they haven't spent time or money trying to fix it, the problem isn't urgent", "Listen 80% of the time and speak only 20% during user research interviews"],
        ["Never ask leading questions like 'Don't you think my handmade badge is awesome?'", "Never count polite compliments from best friends as proof of market demand"],
        "Asking your parents and best friends 'Would you buy this?' gives completely reliable market validation.", "myth", "Loved ones lie to encourage you. Only observed actions, past spending, and neutral feedback reveal true demand.",
        "Which interview question provides the most honest validation about a new study-planner tool?",
        ["'Don't you think my study planner is pretty?'", "'How did you organize your exam revision last week, and what frustrated you about it?'", "'Will you promise to buy this when it launches?'", "'Do you love apps?'"], 1,
        "Asking about specific past behavior uncovers actual user friction without fishing for polite compliments.",
        ["{name} develops a prototype cardboard desk organizer at {at}. Friends say 'It's super cool!' but no one asks to keep one."],
        "How should {name} validate true user demand?",
        [("Apply the Mom Test: observe whether students actually put pens into it and ask what they currently use", "Probes authentic behavioral adoption.", True, "apply mom test|observe real usage|probe past habits", 50),
         ("Avoid relying on polite verbal compliments as proof of commercial viability", "Recognizes politeness bias in research.", True, "discount polite compliments|seek behavioral proof", 30),
         ("Ask students what specific desk clutter problem frustrates them most during homework", "Uncovers real functional pain points.", False, "uncover real clutter problems|open questions", 20)],
        ["assume instant success based on friend compliments", "force friends to buy out of obligation", "stop asking questions"],
        "NITI Aayog - Women Entrepreneurship Platform (WEP)", "https://wep.gov.in"
    ))

    # ENT-008: Setting Milestones & Project Timelines
    cards.append(make_card(
        "ENT-008", "forge", "Execution", "Milestones & Gantt charts: Turning chaotic projects into reality",
        ["junior", "middle", "senior"],
        ["Ambitious ventures collapse when teams wait until the final 48 hours to assemble prototypes and posters.",
         "Backward planning (working back from launch day) breaks daunting projects into bite-sized weekly milestones."],
        ["Pinpoint launch day and work backwards: prototype ready by Day 10, testing by Day 15, launch by Day 20", "Assign a single accountable owner and deadline for every sub-task on a shared visual checklist", "Hold a 5-minute daily check-in to identify blockers before they cause multi-day delays"],
        ["Never leave deadlines as 'sometime next week' without an exact day and time", "Never let silent bottlenecks fester without asking team members for help"],
        "Leaving all project tasks open-ended without deadlines sparks spontaneous creative genius.", "myth", "Unstructured timelines breed chronic procrastination and emergency all-nighters that destroy build quality.",
        "What is the core principle of 'backward planning' for a school project exhibition?",
        ["Starting on the first day and improvising as you go", "Setting the final exhibition date as the target and scheduling reverse deadlines for each milestone", "Doing all the work the night before", "Waiting for teachers to assign dates"], 1,
        "Reverse scheduling ensures every necessary phase—sourcing, fabrication, testing, and rehearsal—has dedicated time.",
        ["With a science-venture exhibition only 3 weeks away at {at}, {name}'s team has many ambitious ideas but zero physical prototypes built."],
        "How should {name} structure the project timeline?",
        [("Create a backward schedule: Week 1 prototype build, Week 2 user testing, Week 3 presentation rehearsal", "Implements structured reverse milestone planning.", True, "backward schedule|week 1 prototype|week 2 testing|week 3 rehearsal", 45),
         ("Assign specific component ownership (hardware, poster, script) with hard Friday check-ins", "Establishes clear task accountability.", True, "assign component ownership|hard deadlines", 35),
         ("Identify critical dependencies early so delay in sourcing does not stall the entire team", "Mitigates project pipeline bottlenecks.", False, "identify dependencies|prevent blockers", 20)],
        ["wait until day 20 to start assembling parts", "blame teammates without setting deadlines", "abandon the project"],
        "Project Management Institute (PMI) Educational Foundation", "https://pmief.org"
    ))

    # ENT-009: Rejecting Get-Rich-Quick Mindsets
    cards.append(make_card(
        "ENT-009", "forge", "Mindset", "Sweat equity vs shortcuts: Real enterprise takes patience",
        ["middle", "senior"],
        ["Social media glamorizes teenage dropouts making millions overnight through dropshipping or crypto; real enterprise is built on patient iteration.",
         "Sustainable businesses require deep craftsmanship, customer empathy, ethical supplier relationships, and operational discipline."],
        ["Focus on mastering a craft or solving a tangible community need rather than pursuing overnight viral wealth", "Celebrate small milestones: your first paying non-family customer is worth more than 10,000 viral views", "Be suspicious of any course, influencer, or book promising guaranteed passive income with zero effort"],
        ["Never sacrifice product quality, safety, or ethical honesty to make a quick buck", "Never jump between five unrelated business ideas every two weeks without executing one thoroughly"],
        "Successful entrepreneurs achieve wealth effortlessly within a few weeks using automated internet shortcuts.", "myth", "Enduring businesses require years of hard work, continuous iteration, and solving complex real-world challenges.",
        "Which mindset is essential for enduring entrepreneurial success?",
        ["Hunting for overnight get-rich-quick hacks", "Patient craftsmanship, resilience through setbacks, and genuine customer focus", "Copying someone else's viral video", "Avoiding hard work at all costs"], 1,
        "Real value creation requires continuous learning, resilience, and ethical problem solving over long horizons.",
        ["A peer at {at} urges {name} to abandon their eco-friendly pen recycling initiative to join a dubious 'automated social media crypto trading bot'."],
        "How should {name} evaluate this proposition?",
        [("Reject the get-rich-quick shortcut, recognizing that sustainable ventures solve real human needs", "Rebuffs speculative traps in favor of genuine value.", True, "reject shortcut|sustainable venture|solve real needs", 45),
         ("Continue iterating the recycling initiative through measured customer feedback", "Maintains focus on grounded craftsmanship.", True, "iterate recycling initiative|stay grounded|patience", 35),
         ("Evaluate business ideas based on tangible utility rather than flashy influencer hype", "Applies critical business judgment.", False, "evaluate utility over hype|critical thinking", 20)],
        ["gamble project funds on trading bots", "quit school to pursue viral fame", "believe automated riches hype"],
        "National Innovation Foundation (NIF) India", "https://nif.org.in"
    ))

    # ENT-010: Leading Without Being Bossy
    cards.append(make_card(
        "ENT-010", "forge", "Leadership", "Servant leadership: Lead by clearing obstacles, not giving orders",
        ["junior", "middle", "senior"],
        ["Being the project leader does not make you a royal monarch; effective leadership means serving your team and clearing their roadblocks.",
         "Dictatorial leaders alienate talented peers, while empathetic servant leaders inspire voluntary excellence and shared pride."],
        ["Ask teammates daily: 'What is blocking you, and how can I help you finish it?'", "Publicly credit teammates for successes while personally absorbing blame for collective mistakes", "Do the unglamorous grunt work (cleaning up tools, organizing files) alongside your team"],
        ["Never micromanage competent teammates or bark orders like an autocrat", "Never steal credit for a teammate's creative design during showcase presentations"],
        "A strong team leader should make every single minor decision alone and command teammates without discussion.", "myth", "Command-and-control alienates team members. Great leaders empower peers, delegate trust, and facilitate consensus.",
        "What is the hallmark behavior of a true 'servant leader' on a student project?",
        ["Ordering everyone around with a megaphone", "Asking how to clear roadblocks for teammates and sharing credit generously", "Taking all the praise on stage", "Leaving early while others clean up"], 1,
        "Servant leaders view their job as supporting and empowering their team to do their best work.",
        ["As team captain of the robotics squad at {at}, {name} sees two teammates arguing intensely over motor bracket designs."],
        "How should {name} exercise constructive leadership?",
        [("Facilitate a calm discussion focusing on objective design criteria rather than personal egos", "Guides collaborative problem solving.", True, "focus on objective criteria|calm discussion|remove ego", 45),
         ("Help test both bracket options experimentally to let data decide the better solution", "Uses empirical evidence over personal opinion.", True, "test both options experimentally|data driven choice", 35),
         ("Acknowledge both teammates' creative efforts and keep the team atmosphere supportive", "Maintains high team morale and unity.", False, "acknowledge efforts|keep team supportive", 20)],
        ["scream at both members to obey captain orders", "kick both members off the team", "flip a coin without testing"],
        "Center for Creative Leadership - Youth Leadership Development", "https://ccl.org"
    ))

    # ENT-011: Honest Product Marketing & Posters
    cards.append(make_card(
        "ENT-011", "forge", "Marketing & Ethics", "Honest marketing: Communicating value without exaggeration",
        ["junior", "middle", "senior"],
        ["Great marketing connects a real solution with the people who need it; deceptive advertising destroys trust permanently.",
         "Clean visual hierarchy (Headline, Benefit, Proof, Call to Action) outperforms cluttered, exaggerated promotional posters."],
        ["Follow the rule of three: Highlight 1 big headline, 3 key benefits, and 1 clear next action", "Use high-contrast colors and legible fonts that can be read from 5 meters away", "State exactly what your product can and cannot do with absolute honesty"],
        ["Never make false medical, environmental, or performance claims on your promotional flyers", "Never use stolen copyrighted logos or watermarked images without attribution"],
        "Marketing means exaggerating your product's capabilities as much as possible so customers buy it.", "myth", "Exaggeration creates disappointed customers who demand refunds and destroy your reputation. Honest marketing builds loyalty.",
        "Which element makes a promotional event poster most effective at school?",
        ["Ten different fancy cursive fonts with glitter text", "A bold readable headline, clear user benefit, event time/venue, and simple contact info", "Twenty paragraphs of fine print", "Stock photos of celebrities without permission"], 1,
        "Clear visual hierarchy and legible essential facts inform viewers quickly and drive action.",
        ["{name}'s club is designing a poster for their student bike-repair workshop at {at}. A teammate wants to write: 'Guaranteed 100% Brand-New Bike Performance in 5 Minutes!'"],
        "How should {name} refine the marketing message?",
        [("Replace misleading hyperbole with honest value: 'Fast brake tune-ups, tire checks, and chain lubrication by students'", "Restores factual credibility and trust.", True, "honest value proposition|replace hyperbole|clear service list", 50),
         ("Ensure the poster features clear dates, room location, and pricing or free-service details", "Provides essential functional logistics.", True, "clear dates|location|pricing details", 30),
         ("Use clean visual layout with plenty of white space so key information stands out", "Applies solid graphic design principles.", False, "clean layout|white space|legible fonts", 20)],
        ["promise impossible bicycle repairs", "leave off location and time", "copy commercial brand logos"],
        "Advertising Standards Council of India (ASCI)", "https://ascionline.in"
    ))

    # ENT-012: Starting a Waste-to-Wealth Project
    cards.append(make_card(
        "ENT-012", "forge", "Sustainability", "Upcycling ventures: Turning discarded waste into community wealth",
        ["junior", "middle", "senior"],
        ["Waste-to-wealth enterprises apply circular economy principles, transforming discarded trash (paper, fabric scraps, plastic) into valuable products.",
         "Circular ventures generate revenue while reducing municipal landfill pollution, creating dual economic and ecological impact."],
        ["Identify clean waste streams available in large quantities (e.g., used exam notebooks, textile scraps from tailors)", "Design an upcycled product that people want for its quality, not just out of sympathy for the environment", "Calculate production costs thoroughly to ensure the recycled item is economically viable"],
        ["Never produce flimsy novelty items that break immediately and end up back in the landfill in 24 hours", "Never collect hazardous or medical waste for school recycling projects"],
        "Eco-friendly upcycled products will sell automatically even if the build quality is poor and pricing is double market rate.", "myth", "Eco-friendly benefits cannot compensate for terrible utility. Sustainable products must deliver equal or superior quality and fair pricing.",
        "What is the core principle of a 'circular economy' venture?",
        ["Throwing away goods after a single use", "Designing systems where materials are reclaimed, upcycled, and kept in productive use continuously", "Burning plastic waste in open fields", "Mining more raw metals from nature"], 1,
        "Circular models minimize waste by cycling existing materials through reuse, remanufacture, and upcycling.",
        ["At school at {at}, {name} sees kilograms of one-sided blank paper thrown into recycling bins after final term exams."],
        "How can {name} launch an entrepreneurial waste-to-wealth project?",
        [("Collect and bind clean one-sided sheets into sturdy pocket sketchbooks and scratch pads", "Transforms wasted resource into functional product.", True, "bind one-sided paper|pocket sketchbooks|upcycling", 45),
         ("Test sales among art students and library visitors at an affordable, attractive price point", "Validates product-market fit practically.", True, "test sales|affordable price|validate demand", 35),
         ("Reinvest a portion of proceeds into school green club tree-planting initiatives", "Creates circular community benefit.", False, "reinvest in green club|circular impact", 20)],
        ["burn scrap paper behind school", "make unusable shoddy notebooks and force teachers to buy", "discard clean paper"],
        "Ministry of Environment, Forest and Climate Change - Mission LiFE", "https://missionlife-moefcc.nic.in"
    ))

    # ENT-013: What is a Social Enterprise?
    cards.append(make_card(
        "ENT-013", "forge", "Social Innovation", "Social enterprise: Doing good by doing sustainable business",
        ["middle", "senior"],
        ["A social enterprise uses commercial market strategies to solve social, cultural, or environmental problems self-sustainably.",
         "Unlike traditional charities reliant on perpetual donations, a social enterprise earns revenue from sales to fund its community mission."],
        ["Identify a clear double bottom line: Financial sustainability AND measurable social or environmental impact", "Ensure the business model generates sufficient gross margin to survive without continuous grant dependency", "Engage the beneficiary community as partners and co-creators rather than passive charity recipients"],
        ["Never treat social enterprise as an excuse for sloppy accounting or poor product standards", "Never prioritize short-term profit at the cost of the core social mission"],
        "Social enterprises are identical to standard charities and cannot charge money for their products or services.", "myth", "Social enterprises sell products or services commercially to generate independent revenue that perpetually powers their social mission.",
        "What defines the 'double bottom line' of an authentic social enterprise?",
        ["Earning twice as much personal money as traditional jobs", "Measuring both commercial financial sustainability AND positive social/environmental impact", "Filing two sets of tax returns", "Operating in two different countries simultaneously"], 1,
        "A double bottom line holds the enterprise accountable to financial health and measurable positive community impact.",
        ["{name}'s team at {at} wants to help local potters whose traditional earthenware lamps (diyas) face declining sales against cheap plastic LED imports."],
        "How can {name} structure this as a social enterprise rather than a one-time charity donation?",
        [("Partner with potters to design contemporary home decor and create a digital direct-to-consumer store", "Builds durable market linkage and value addition.", True, "partner with artisans|contemporary designs|digital store", 45),
         ("Price the pottery fairly, guaranteeing the artisans receive 70%+ of net margins directly", "Ensures ethical and dignified revenue sharing.", True, "fair pricing|equitable margin share|artisan dignity", 35),
         ("Reinvest platform profits into potter apprenticeships and clay sourcing infrastructure", "Creates sustainable community capacity building.", False, "reinvest in infrastructure|sustainable growth", 20)],
        ["give one-time donation and walk away", "sell pottery at huge loss and go bankrupt", "exploit artisans for personal profit"],
        "National Social Entrepreneurship Mission - Skill India", "https://skillindia.gov.in"
    ))

    # ENT-014: Finding and Approaching Mentors
    cards.append(make_card(
        "ENT-014", "forge", "Networking", "Approaching mentors: Specific questions and respecting time",
        ["middle", "senior"],
        ["Experienced professionals love helping proactive, respectful young builders who demonstrate initiative and do their homework.",
         "Vague requests like 'Can you be my mentor?' get ignored; concise, specific questions about a concrete challenge get enthusiastic replies."],
        ["Research the mentor's past work before reaching out so you can reference specific relevant projects", "Ask 1 or 2 focused questions that can be answered in under 5 minutes or a brief 15-minute call", "Always send a follow-up thank-you note sharing what action you took based on their advice"],
        ["NEVER send a generic 'Hi sir, please mentor me' message without context or proof of work", "NEVER expect busy mentors to do your homework, write your business plan, or review 40-page decks"],
        "Busy industry professionals never respond to student emails or messages.", "myth", "Most leaders gladly help passionate students who write concise, polite, well-researched emails showing genuine commitment.",
        "What is the most effective way to request guidance from an experienced entrepreneur?",
        ["Send a 20-page business proposal with no introduction", "Send a polite 4-sentence email introducing your project, asking one specific question, and offering flexible 15-minute time slots", "Call their personal phone repeatedly during dinner hours", "Ask them to fund your entire project upfront"], 1,
        "Concise, specific emails that respect the recipient's schedule have the highest response rates.",
        ["{name} is building an open-source air quality sensor at {at} and needs advice on calibrating low-cost PM2.5 lasers from an environmental researcher."],
        "How should {name} craft the outreach email?",
        [("State who you are, what sensor prototype you have already built, and link the test data", "Shows concrete proof of work and initiative.", True, "who you are|proof of built prototype|link test data", 45),
         ("Ask one precise technical question regarding laser sensor baseline calibration in dusty weather", "Respects their time with a focused inquiry.", True, "precise technical question|calibration|focused ask", 35),
         ("Keep the message under 150 words and express gratitude for their published research papers", "Demonstrates professionalism and courtesy.", False, "concise under 150 words|cite published research", 20)],
        ["send vague one-line email asking for money", "demand immediate video calls", "copy-paste generic spam template"],
        "Atal Innovation Mission - Mentor India Network", "https://aim.gov.in/mentor-india.php"
    ))

    # ENT-015: Win-Win Negotiation Basics
    cards.append(make_card(
        "ENT-015", "forge", "Negotiation", "Win-win negotiation: Getting what you need while helping others",
        ["middle", "senior"],
        ["Negotiation is not a combat sport where one party crushes the other; enduring business relationships require both sides to win.",
         "Focus on interests, not rigid positions: understanding what the other party truly values unlocks creative compromises."],
        ["Understand the other party's constraints (e.g., a vendor may lack cash but have surplus warehouse space)", "Identify non-monetary trade-offs: publicity, volunteer labor, flexible delivery dates, or barter exchanges", "Know your BATNA (Best Alternative to a Negotiated Agreement) before starting any discussion"],
        ["Never use aggressive ultimatums or threats during business or school negotiations", "Never agree to a deal that leaves you harboring deep resentment or severe financial loss"],
        "In a good negotiation, you must trick or force the other party into losing as much as possible.", "myth", "Win-lose deals cause the loser to sabotage delivery, breach contracts, or refuse future collaboration. Win-win builds enduring partnerships.",
        "What does the term 'BATNA' mean in negotiation strategy?",
        ["Buying All The New Assets", "Best Alternative To a Negotiated Agreement (your backup plan if talks fail)", "Borrowing All Total Net Amounts", "Billing Always Takes New Accounts"], 1,
        "Your BATNA is your walk-away alternative; knowing it gives you confidence to negotiate calmly without desperation.",
        ["At the neighborhood community center at {at}, {name}'s student club wants to host a weekend science workshop, but the manager quotes Rs 2,000 hall rent, which the club cannot afford."],
        "How should {name} negotiate a win-win arrangement?",
        [("Ask the manager what operational challenges the community center currently faces", "Discovers underlying interests and needs.", True, "understand center challenges|listen to manager|find needs", 45),
         ("Offer a creative barter: club members will clean and repaint the center's courtyard benches in exchange for room usage", "Proposes non-cash mutually beneficial trade.", True, "barter volunteer service|clean courtyard|room trade", 35),
         ("Reserve 5 free workshop seats specifically for children of community center staff", "Adds direct personal value for the facility.", False, "free seats for staff children|shared value", 20)],
        ["threaten to complain to the mayor", "abandon the workshop without discussion", "break into the hall secretly"],
        "Harvard Program on Negotiation - Principles of Negotiation", "https://pon.harvard.edu"
    ))

    # ENT-016: Time Management for Student Founders
    cards.append(make_card(
        "ENT-016", "forge", "Productivity", "Balancing grades and building: The Eisenhower Matrix",
        ["middle", "senior"],
        ["Student builders who neglect board exam studies fail school; student builders who never execute remain dreamers.",
         "The Eisenhower Matrix categorizes tasks into four quadrants: Urgent & Important, Important but Not Urgent, Urgent but Not Important, and Neither."],
        ["Schedule 90-minute deep work blocks for school revision before opening project software", "Spend time daily in Quadrant 2 (Important, Not Urgent: strategic building, health, revision) before crises hit", "Say 'no' to time-wasting social obligations and mindless scrolling that drain builder energy"],
        ["Never sacrifice 7+ hours of essential nightly sleep to crunch on startup prototypes", "Never use your venture as a psychological excuse to evade fundamental homework commitments"],
        "Real founders sleep only 3 hours a night and completely fail their high school classes to succeed.", "myth", "Sleep deprivation destroys cognitive performance and decision making. High achievers master focused time blocking.",
        "According to the Eisenhower Matrix, which quadrant should ambitious student builders prioritize to prevent perpetual crises?",
        ["Quadrant 4 (Mindless video games and gossip)", "Quadrant 2 (Important but Not Urgent: planning, proactive study, prototype testing)", "Quadrant 3 (Every random notification that rings)", "Quadrant 1 (Only emergency fire-fighting)"], 1,
        "Investing focused time into Quadrant 2 prevents tasks from exploding into stressful last-minute emergencies.",
        ["With midterm exams in two weeks at {at}, {name} is tempted to spend all evening tweaking 3D models for an entrepreneurship contest."],
        "How should {name} manage time effectively?",
        [("Time-block dedicated study slots for core exam subjects first as the primary priority", "Protects academic baseline without compromise.", True, "time block study first|prioritize exams|academic baseline", 45),
         ("Dedicate a strict 45-minute evening block to project progress rather than unstructured all-nighters", "Maintains measured builder momentum.", True, "strict 45 min block|measured momentum|no all nighter", 35),
         ("Protect 8 hours of sleep to ensure peak retention and cognitive stamina", "Safeguards neurological recovery and health.", False, "protect sleep|cognitive stamina", 20)],
        ["skip school study entirely for startup", "pull all-nighters and fall sick during exams", "abandon project permanently"],
        "Central Board of Secondary Education (CBSE) - Life Skills & Time Management", "https://cbse.gov.in"
    ))

    # ENT-017: Learning from Local Street Entrepreneurs
    cards.append(make_card(
        "ENT-017", "forge", "Practical Wisdom", "Street-smart economics: Lessons from chaiwallas and kirana stores",
        ["junior", "middle", "senior"],
        ["Local street vendors, chaiwallas, and kirana shopkeepers are master entrepreneurs in cash flow, inventory turnover, and customer loyalty.",
         "Silicon Valley buzzwords often obscure fundamental retail truths that local bazaar merchants execute flawlessly every single day."],
        ["Observe how chai vendors manage zero-waste just-in-time inventory with perishable milk and tea leaves", "Study how neighborhood kirana owners remember customer family names and personalize credit to build unbreakable loyalty", "Notice prime foot-traffic location dynamics: why a vendor sets up right beside a bustling railway exit"],
        ["Never dismiss humble informal merchants as uneducated; their practical business mastery is formidable", "Never overlook unit economics and daily cash reconciliation in favor of abstract software theories"],
        "You can only learn valid business strategy from billionaires and professors at elite business schools.", "myth", "Informal street merchants possess deep mastery of micro-location, rapid inventory turns, customer psychology, and cash resilience.",
        "What critical business lesson does a busy morning chaiwalla demonstrate perfectly?",
        ["Carrying massive 3-year stockpiles of milk", "High-speed execution, minimal inventory holding cost, and unbeatable customer relationship warmth", "Spending millions on billboard advertising", "Ignoring customer preference"], 1,
        "Street vendors excel at high-velocity turnover, zero dead stock, tight working capital, and personal rapport.",
        ["On the walk home from school at {at}, {name} observes a vegetable vendor reorganizing fresh spinach under damp jute sacks while placing ripe tomatoes up front."],
        "What entrepreneurial insight can {name} extract from this observation?",
        [("Recognize active inventory preservation (damp sacks protect perishables) and merchandising (eye-level display)", "Extracts practical supply chain and retail principles.", True, "inventory preservation|merchandising|practical retail", 50),
         ("Appreciate how daily customer relationship trust enables small businesses to thrive without advertising budgets", "Values customer loyalty and retention dynamics.", True, "customer trust|unwritten loyalty|retention", 30),
         ("Document practical operational lessons in a personal business observation notebook", "Translates everyday observation into actionable insights.", False, "document practical lessons|field observation", 20)],
        ["mock street vendors as unsophisticated", "assume only app startups have valid business models", "ignore real-world commerce"],
        "Ministry of Housing and Urban Affairs - PM SVANidhi Scheme", "https://pmsvanidhi.mohua.gov.in"
    ))

    # ENT-018: Respecting Intellectual Property & Fair Use
    cards.append(make_card(
        "ENT-018", "forge", "Ethics & IP", "Intellectual property & plagiarism: Building on original work",
        ["middle", "senior"],
        ["Copying someone else's logo, design, or written code and calling it your own is intellectual theft and copyright infringement.",
         "Ethical builders leverage open-source licenses, attribute original creators properly, and focus on adding genuine novel value."],
        ["Check open-source license terms (MIT, Apache, Creative Commons) before using third-party code or media", "Always provide clear attribution to original creators when remixing public domain resources", "Protect your own original designs by documenting creation dates and applying for school innovation patents where appropriate"],
        ["NEVER copy a competitor's logo, trademark name, or marketing slogans for your project", "NEVER submit someone else's project work into a science competition as your own"],
        "If an image or code snippet is visible on Google, it is free for anyone to use commercially without permission or credit.", "myth", "Publicly visible does not mean copyright-free. Most web content is protected by automatic copyright requiring explicit licensing.",
        "What is the required practice when using an open-source icon pack or software library in your student project?",
        ["Claim that you designed all the icons from scratch in Photoshop", "Check the license terms (e.g., Creative Commons / MIT) and include required creator attribution", "Remove the copyright notices from the code files", "Sell the icon library to classmates"], 1,
        "Open-source licenses require honoring attribution terms and keeping licensing notices intact.",
        ["While building a mobile website for their club at {at}, a teammate downloads a famous company's copyrighted swoosh logo to use as the app icon."],
        "How should {name} address this intellectual property breach?",
        [("Explain that copying trademarked logos is illegal and damages the club's credibility", "Explains trademark infringement risks clearly.", True, "trademark violation illegal|copyright risk|protect credibility", 45),
         ("Guide the team to create an original icon or use a verified Creative Commons open-source icon with proper credit", "Implements ethical creative alternatives.", True, "create original icon|creative commons|proper credit", 35),
         ("Include a dedicated credits section acknowledging open-source tools and fonts used in the project", "Demonstrates professional attribution standards.", False, "credits section|acknowledge open source", 20)],
        ["use stolen logo hoping nobody notices", "lie to competition judges about origin", "plagiarize competitor code"],
        "Cell for IPR Promotion and Management (CIPAM) - DPIIT", "https://cipam.gov.in"
    ))

    return cards
