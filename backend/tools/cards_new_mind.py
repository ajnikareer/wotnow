"""
New Agents in the MIND Pillar:
- Echo (Feelings & Mental Wellbeing - FEEL) [sensitive, approve-first]
- Pixel (Digital Balance & Screen Health - TECH)
- Saathi (Inclusion & Empathy - INC)
"""
from cards_existing import make_card

def get_echo_cards():
    cards = []

    # FEEL-001: Naming your emotions
    cards.append(make_card(
        "FEEL-001", "echo", "Emotional Literacy", "Naming your emotions: The feelings wheel",
        ["junior", "middle", "senior"],
        ["Psychologist Dan Siegel coined 'Name it to tame it': labeling an emotion activates the brain's prefrontal cortex, reducing amygdala reactivity.",
         "Vague labels like 'bad' or 'weird' keep distress fuzzy; identifying 'lonely', 'overwhelmed', or 'envious' leads to targeted solutions."],
        ["Use an emotion wheel or mood chart to identify the precise sub-emotion you are experiencing", "Acknowledge feelings without judgment: 'I am noticing a sensation of envy in my chest'", "Remember that emotions are temporary brain signals, not permanent personal identities"],
        ["Never suppress or bottle up painful feelings hoping they will magically vanish", "Never shame yourself for experiencing normal human feelings like jealousy or fear"],
        "Mentally strong people never feel sad, anxious, jealous, or overwhelmed.", "myth", "Emotional strength is not feeling numb; it is having the self-awareness to recognize painful emotions and process them healthily.",
        "What happens in your brain when you accurately name a strong, distressing emotion?",
        ["Your brain shuts down completely", "The logical prefrontal cortex activates, helping calm down the amygdala alarm center", "Your heart rate doubles instantly", "Emotions get permanently stuck in your head"], 1,
        "Labeling emotions ('naming to tame') dampens autonomic nervous arousal and restores cognitive clarity.",
        ["After receiving lower marks than expected at {at}, {name} feels a tight heaviness in their stomach and snaps angrily at a sibling."],
        "How should {name} process this emotional state constructively?",
        [("Pause and identify the underlying emotion: disappointment and embarrassment rather than pure anger", "Practices accurate emotional labeling.", True, "name disappointment|underlying emotion|name it to tame it", 45),
         ("Acknowledge that feeling sad or disappointed after hard work is completely valid and normal", "Validates emotional experience without judgment.", True, "validate feeling|normal human response|self compassion", 35),
         ("Apologize to the sibling and take three slow, calming breaths", "Takes relational responsibility and resets physiology.", False, "apologize to sibling|calming breaths", 20)],
        ["scream and throw textbooks", "bottle up emotions and pretend everything is perfect", "punish self through starvation"],
        "National Institute of Mental Health and Neurosciences (NIMHANS)", "https://nimhans.ac.in"
    ))

    # FEEL-002: Exam anxiety & panic attacks
    cards.append(make_card(
        "FEEL-002", "echo", "Anxiety Management", "Taming exam anxiety: The 5-4-3-2-1 grounding technique",
        ["middle", "senior"],
        ["Exam anxiety triggers a fight-or-flight adrenal surge that reduces working memory and makes your mind feel blank.",
         "Physical grounding (5-4-3-2-1 sensory check) and 4-7-8 rhythmic breathing physically downshift the nervous system within 90 seconds."],
        ["Practice 5-4-3-2-1: Name 5 things you see, 4 things you can touch, 3 sounds you hear, 2 things you smell, 1 thing you taste", "Inhale through your nose for 4 seconds, hold for 7 seconds, exhale slowly through pursed lips for 8 seconds", "Remind yourself: 'An exam measures my preparation on a few questions today, not my entire worth as a human'"],
        ["Never hyperventilate with shallow chest breathing when panic surges", "Never stay up all night drinking caffeine before a morning examination"],
        "If your mind goes blank in an exam hall, it means you have forgotten everything and are doomed to fail.", "myth", "A blank mind is temporary cortisol-induced working memory vasoconstriction. Calming your breath restores memory access within 2 minutes.",
        "What is the immediate physiological goal of using the 5-4-3-2-1 grounding technique?",
        ["To memorize 5 math formulas simultaneously", "To pull sensory attention back into the present moment and deactivate the fight-or-flight panic cycle", "To fall into deep sleep during the test", "To test your eyesight"], 1,
        "Grounding breaks catastrophic mental loops by reconnecting your attention with immediate physical reality.",
        ["Inside the exam hall at {at}, {name} flips open the question paper, feels their heart hammering at 140 bpm, and feels completely blank."],
        "What should {name} do in the first 2 minutes?",
        [("Put the pen down, close eyes, and take three deliberate 4-7-8 slow breaths into the belly", "Physiologically calms autonomic nervous arousal.", True, "4-7-8 breathing|slow belly breaths|put pen down", 45),
         ("Use the 5-4-3-2-1 grounding technique to reconnect with the physical desk and surroundings", "Deactivates panic cascade through present-moment sensory focus.", True, "5-4-3-2-1 grounding|feel desk|anchor in room", 35),
         ("Scan the paper for the single easiest question you recognize and solve that first to rebuild momentum", "Restores cognitive confidence through small wins.", False, "find easiest question first|rebuild momentum", 20)],
        ["tear up question paper", "run out of the hall screaming", "give up and leave paper blank"],
        "Tele-MANAS (Mental Health Helpline 14416) - MoHFW", "https://telemanas.mohfw.gov.in"
    ))

    # FEEL-003: Saying 'No' without guilt
    cards.append(make_card(
        "FEEL-003", "echo", "Boundaries", "Saying 'No' with kindness: Healthy boundaries protect you",
        ["junior", "middle", "senior"],
        ["Saying 'yes' to everyone else often means saying 'no' to your own mental health, sleep, and core duties.",
         "A boundary is not an attack or rejection of the other person; it is a clear statement of what you can and cannot do."],
        ["Use clear, polite phrases: 'I can't take that on right now, but thank you for thinking of me'", "Deliver your refusal without long, fabricated excuses; simple clarity commands respect", "Notice if you say 'yes' purely out of fear that people will stop liking you"],
        ["Never apologize excessively for protecting your study hours or rest", "Never agree to do a classmate's homework out of fear of being cast out of the group"],
        "Being a kind and caring friend means you must agree to every single request anyone asks of you.", "myth", "Compulsive agreeableness is people-pleasing, not kindness. Healthy relationships require mutual boundaries and honest limits.",
        "Which of the following is the most mature way to decline an unmanageable favor from a friend?",
        ["Make up an elaborate lie about a fake doctor appointment", "State calmly: 'I'd love to help, but I'm booked with exam revision this evening, so I can't join'", "Ignore their calls for three weeks", "Yell at them for being selfish"], 1,
        "Honest, prompt, and calm boundaries preserve self-respect and friendship without deception.",
        ["A popular classmate at {at} demands that {name} write their complete history essay project by tomorrow morning."],
        "How should {name} assert this personal boundary?",
        [("Say clearly and calmly: 'No, I cannot write your project for you, but I can share the library book links'", "Sets a firm ethical boundary with helpful alternative.", True, "refuse to write essay|say no clearly|set firm boundary", 50),
         ("Recognize that true friendship is never conditional on completing someone else's academic work", "Rejects manipulative social coercion.", True, "friendship not conditional on homework|reject pressure", 30),
         ("Seek advice from a teacher or parent if the classmate uses bullying or threats", "Escalates extortion safely to trusted adults.", False, "tell teacher if threatened|seek adult support", 20)],
        ["stay up all night writing peer's essay", "do homework out of fear", "insult classmate on group chat"],
        "NIMHANS Child & Adolescent Mental Health Services", "https://nimhans.ac.in"
    ))

    # FEEL-004: The art of a genuine apology
    cards.append(make_card(
        "FEEL-004", "echo", "Relationship Repair", "The 4-part genuine apology: Repairing damaged trust",
        ["junior", "middle", "senior"],
        ["A fake apology says 'I am sorry IF you felt hurt'; a genuine apology takes full ownership: 'I was wrong, I hurt you, and I will fix it.'",
         "The four parts of an authentic apology: Own the specific action, Acknowledge the impact, Make amends, and Change the behavior."],
        ["Say explicitly: 'I was wrong to share your secret; I broke your trust and made you feel exposed'", "Ask sincerely: 'What can I do to help make this right between us?'", "Give the hurt person space and time to forgive you without demanding immediate smiles"],
        ["Never attach defensive justifications: 'I am sorry, BUT you provoked me first'", "Never expect someone to trust you instantly just because you said the word 'sorry'"],
        "Adding the word 'BUT' in an apology ('I'm sorry, BUT you started it') makes the apology more balanced and fair.", "myth", "Using 'but' instantly cancels out the apology, shifting blame back onto the victim and deepening emotional damage.",
        "What makes an apology genuinely restorative and mature?",
        ["Blaming someone else for your actions", "Taking clear responsibility for specific harm, expressing remorse, and offering concrete restitution", "Buying expensive candy to bribe them", "Posting a vague status on social media"], 1,
        "Authentic apologies focus entirely on acknowledging harm, taking responsibility, and changing future conduct.",
        ["In the school corridor at {at}, {name} repeated a humiliating rumor about a friend to get laughs from a group of classmates."],
        "How should {name} deliver a sincere restorative apology?",
        [("Approach the friend privately and take unconditional ownership of the betrayal without excuses", "Delivers direct personal accountability.", True, "take full ownership|private apology|no excuses", 45),
         ("Acknowledge the specific emotional hurt and humiliation caused by repeating the rumor", "Validates the victim's pain with empathy.", True, "acknowledge emotional hurt|rumor impact|validate pain", 35),
         ("Publicly correct the false rumor in front of the same peer group where it was spoken", "Makes active public restitution to restore dignity.", False, "correct rumor publicly|active restitution", 20)],
        ["say 'it was just a joke bro'", "blame the classmate who originally started the rumor", "pretend it never happened"],
        "CBSE School Counseling Guidelines - Restorative Practices", "https://cbse.gov.in"
    ))

    # FEEL-005: Being left out or excluded
    cards.append(make_card(
        "FEEL-005", "echo", "Social Rejection", "Coping with exclusion: You are not defined by someone's clique",
        ["junior", "middle", "senior"],
        ["Social exclusion activates the same anterior cingulate cortex pain pathways in the brain as physical bodily injury.",
         "Being excluded by a school clique is usually about group insecurity and conformity, not an indictment of your worth as a person."],
        ["Remind yourself: 'Their choice to exclude me reflects their group dynamics, not my value as a human'", "Direct your energy toward cultivating one or two authentic, kind individual friendships rather than chasing popular cliques", "Engage in passion-driven clubs (music, robotics, sports, art) where connection forms around shared interests"],
        ["Never change your core ethical values or mock others just to win acceptance from an exclusive clique", "Never isolate yourself entirely or conclude that nobody in the world will ever like you"],
        "If a popular group of classmates doesn't invite you to sit at their table, it proves you are inherently unlikable.", "myth", "Clique behavior thrives on artificial exclusion to manufacture status. Your worth is completely independent of their group dynamics.",
        "When dealing with painful social exclusion at school, what is the most constructive response?",
        ["Beg them to let you hang out with them", "Seek out genuine shared-interest clubs and invest in individual friendships based on mutual kindness", "Spread hateful gossip about everyone in the clique", "Stop eating lunch entirely"], 1,
        "Focusing on genuine shared interests and quality individual relationships builds lasting social resilience.",
        ["At lunch break at {at}, {name} sees classmates whispering and laughing while hiding their phones, deliberately leaving {name} out of an outing."],
        "How should {name} navigate this painful moment?",
        [("Acknowledge the sting of exclusion without internalizing it as a personal defect", "Practices emotional regulation and self-worth protection.", True, "acknowledge pain|do not internalize defect|protect self worth", 45),
         ("Step away from the clique and sit with someone else or join a library activity", "Chooses healthy social alternatives over begging for inclusion.", True, "step away from clique|find kind peers|join library group", 35),
         ("Talk through the feelings with a trusted sibling, parent, or school counselor", "Processes social distress with supportive adults.", False, "talk to trusted adult|process distress", 20)],
        ["plead with the group to accept you", "throw food at their table", "post passive-aggressive rants online"],
        "National Mental Health Programme - Adolescent Life Skills", "https://mohfw.gov.in"
    ))

    # FEEL-006: Supporting a friend in distress
    cards.append(make_card(
        "FEEL-006", "echo", "Peer Support", "Being there for a friend: Compassionate listening over quick fixes",
        ["middle", "senior"],
        ["When friends are in deep sorrow or distress, they don't need cliches like 'everything happens for a reason'; they need non-judgmental presence.",
         "Distinguish everyday teenage sadness from mental health crises; never promise to keep secrets about self-harm or suicide."],
        ["Sit with them, listen actively, and say: 'I hear how heavy this feels for you; you are not alone'", "Offer practical micro-support: walking together, sharing class notes, or getting a glass of water", "If a friend mentions self-harm, hopelessness, or giving up on life, tell a trusted adult immediately"],
        ["Never dismiss their pain with toxic positivity like 'just smile and cheer up!'", "NEVER promise to keep a secret when a friend's physical life or safety is at risk"],
        "If a distressed friend asks you to promise never to tell anyone about their self-harm plans, you must keep that secret no matter what.", "myth", "Life safety overrides all secrecy promises. True friendship means breaking confidence to save a friend's life by notifying adults.",
        "What is the most supportive thing to say when a friend breaks down crying over family troubles?",
        ["'Stop crying, it's not a big deal'", "'I am here with you, take all the time you need, and I'm listening'", "'My problems are way worse than yours'", "'You should just smile more'"], 1,
        "Validating presence and active listening provide safety and comfort without judgment or unsolicited advice.",
        ["Sitting on the bench at {at}, a close friend confides that they feel hopeless, overwhelmed by family conflict, and want to end their pain."],
        "How should {name} respond with care and responsibility?",
        [("Listen with deep empathy and stay physically present with the friend", "Provides immediate compassionate emotional anchoring.", True, "deep empathy|stay present|do not leave alone", 40),
         ("Clearly explain that you care about their life too much to keep thoughts of harm a secret", "Establishes vital safety boundary.", True, "refuse to keep self harm secret|care too much", 35),
         ("Guide the friend directly to the school counselor or call the Tele-MANAS helpline 14416 together", "Connects crisis situation with professional mental health care.", False, "school counselor|call tele-manas 14416", 25)],
        ["promise to keep suicidal thoughts secret", "mock friend for being dramatic", "leave friend alone in isolated spot"],
        "Tele-MANAS Toll Free 24/7 Mental Health Helpline (14416)", "https://telemanas.mohfw.gov.in"
    ))

    # FEEL-007: Anger management & cooling down
    cards.append(make_card(
        "FEEL-007", "echo", "Emotional Regulation", "Cooling the fire: Managing anger before saying things you regret",
        ["junior", "middle", "senior"],
        ["Anger is a secondary emotion that usually masks underlying hurt, fear, frustration, or perceived injustice.",
         "When angry, your brain releases adrenaline that impairs logical judgment; taking a mandatory cooling break prevents catastrophic blowups."],
        ["Recognize physical anger cues: clenched fists, racing pulse, hot neck, or shallow breathing", "Enforce the 10-second rule: count slowly from 1 to 10 or drink a cold glass of water before replying", "Step away physically: 'I am too angry to talk fairly right now; I will talk when I cool down'"],
        ["Never send text messages, post online comments, or make major decisions while enraged", "Never resort to physical aggression, breaking items, or screaming insults"],
        "Venting anger by punching walls, screaming, and smashing plates helps you get rid of anger safely.", "myth", "Research shows physical aggressive venting rehearses and amplifies anger pathways. Slow breathing and physical stepping away extinguish it.",
        "What physiological action is scientifically proven to de-escalate acute anger rapidly?",
        ["Screaming at the top of your lungs into a pillow", "Slow diaphragmatic exhalations and physical cold water face washing", "Punching a door", "Writing an angry email immediately"], 1,
        "Slow exhalations trigger the vagus nerve and parasympathetic system, reducing heart rate and blood pressure.",
        ["During a heated football dispute on the playground at {at}, an opponent shoves {name} and insults {name}'s family."],
        "How should {name} handle the surge of intense anger?",
        [("Step back, take deep diaphragmatic breaths, and refuse to engage in physical violence", "De-escalates physical conflict through emotional discipline.", True, "step back|deep breaths|refuse physical fight", 45),
         ("Tell the referee or sports teacher clearly about the foul play rather than retaliating", "Uses official grievance systems over street fighting.", True, "report to referee or teacher|do not retaliate", 35),
         ("Allow bodily adrenaline to subside before discussing the dispute with the opponent", "Waits for cognitive prefrontal recovery.", False, "let adrenaline subside|cool down before talking", 20)],
        ["punch the opponent in the face", "start a massive gang brawl", "post violent threats online"],
        "NIMHANS Adolescent Anger Management Guide", "https://nimhans.ac.in"
    ))

    # FEEL-008: Social media envy & comparison
    cards.append(make_card(
        "FEEL-008", "echo", "Digital Wellbeing", "The comparison trap: Highlight reels vs real life",
        ["middle", "senior"],
        ["Comparing your messy behind-the-scenes life to other people's curated, filtered social media highlight reels creates chronic depression and envy.",
         "Social media algorithms intentionally amplify envy and luxury flexes because outrage and desire drive longer screen time."],
        ["Remind yourself: 'Nobody posts their failed exams, family fights, or morning acne on Instagram'", "Mute or unfollow accounts that consistently leave you feeling inadequate, ugly, or poor", "Spend time celebrating your real-world achievements: books read, sports played, and genuine friendships"],
        ["Never measure your beauty or worth by the number of likes, hearts, or views on a photo", "Never buy items you cannot afford just to photograph them for social media clout"],
        "People whose social media profiles show luxury vacations, flawless skin, and constant parties live genuinely perfect lives.", "myth", "Social feeds are carefully curated stage performances. Influencers often experience severe anxiety, loneliness, and financial strain behind the camera.",
        "Why does scrolling through luxury vacation photos on social media frequently make teenagers feel depressed?",
        ["Because phones emit radiation that causes sadness", "Because you are comparing your unfiltered everyday reality to someone else's top 1% staged highlight reel", "Because vacations are bad for health", "Because phones are too heavy"], 1,
        "Comparing your private struggles to another person's public best moments creates an artificial, toxic illusion of personal deficiency.",
        ["Late at night in bed at {at}, {name} scrolls through classmates' beach holiday stories and feels a deep ache of inadequacy and sadness."],
        "What is the healthiest mental shift for {name}?",
        [("Recognize that social media stories are selective highlights and turn off the device", "Breaks the comparison spiral through reality testing.", True, "recognize selective highlights|turn off phone|stop scrolling", 50),
         ("Unfollow or mute accounts that trigger persistent feelings of envy and inadequacy", "Curates a protective digital environment.", True, "mute envy triggering accounts|digital boundary", 30),
         ("Write down three specific blessings or accomplishments in your own everyday life", "Practices grounded gratitude.", False, "three blessings|grounded gratitude", 20)],
        ["stay up all night stewing in jealousy", "beg parents to take out loans for luxury trips", "post fake staged photos to compete"],
        "UNICEF - Digital Parenting and Mental Health", "https://unicef.org"
    ))

    # FEEL-009: Respectful disagreement
    cards.append(make_card(
        "FEEL-009", "echo", "Communication", "Disagreeing with grace: Attack the argument, not the person",
        ["middle", "senior"],
        ["Two smart, kind people can look at the same facts and come to completely different conclusions; disagreement is normal in society.",
         "Attacking a person's intelligence, character, or family (ad hominem) destroys dialogue; focusing on evidence builds shared wisdom."],
        ["Listen to understand the other person's perspective rather than listening merely to formulate your counter-attack", "Use phrases like: 'I see your point about X, but what about the evidence on Y?'", "Separate someone's ideas from their character: you can reject an idea while fully respecting the human holding it"],
        ["Never resort to name-calling, sarcastic mocking, or shouting over someone to win a debate", "Never turn an intellectual or political difference into a lifelong personal grudge"],
        "If you truly believe you are right in a debate, it is fully justified to insult the other person's intelligence.", "myth", "Insults are the weapon of someone who has run out of solid reasoning. Respectful logic and evidence persuade; personal attacks alienate.",
        "What distinguishes a constructive debate from a destructive argument?",
        ["Using louder vocal volume than your opponent", "Focusing on facts and logic while treating the other person with dignity and respect", "Insulting their family background", "Interrupting them every two seconds"], 1,
        "Constructive debate examines evidence objectively without degrading human relationships.",
        ["In the school debate club at {at}, an opponent presents an argument that {name} strongly disagrees with."],
        "How should {name} structure the rebuttal?",
        [("Acknowledge the opponent's core premise respectfully before presenting counter-evidence", "Practices intellectual charity and respectful debate.", True, "acknowledge premise|present counter evidence|respectful rebuttal", 45),
         ("Address the factual data and reasoning directly without mocking the opponent personally", "Avoids ad hominem attacks.", True, "address data and reasoning|no personal insults", 35),
         ("Keep tone calm and modulated to allow the merits of the argument to speak for themselves", "Demonstrates emotional maturity.", False, "calm tone|modulated voice", 20)],
        ["call opponent stupid", "scream until the timer expires", "refuse to shake hands after debate"],
        "National Curriculum Framework - Life Skills & Critical Thinking", "https://ncert.nic.in"
    ))

    # FEEL-010: Identifying trusted adults
    cards.append(make_card(
        "FEEL-010", "echo", "Help Seeking", "Building your safety circle: Identifying trusted adults",
        ["junior", "middle", "senior"],
        ["Every young person encounters problems too heavy to carry alone—bullying, family distress, abuse, or deep depression.",
         "A trusted adult is someone who listens without mocking, protects your physical safety, respects boundaries, and takes constructive action."],
        ["Identify at least 3 trusted adults in different settings: one at home, one at school (teacher/counselor), and one in the community (doctor/relative)", "Practice reaching out: 'I am dealing with something really difficult and I need your guidance'", "Save national safety helpline numbers (Childline 1098, Tele-MANAS 14416) in your contacts"],
        ["Never suffer in silent isolation believing that nobody cares or that you deserve to suffer", "Never trust an adult who demands that you keep dark, abusive, or uncomfortable physical secrets"],
        "Going to a teacher or counselor for help with heavy emotional problems is a sign of personal weakness.", "myth", "Asking for help when overwhelmed is the highest form of courage and wisdom. No human is equipped to solve every crisis alone.",
        "Which of the following qualities indicates an adult is genuinely trustworthy to confide in?",
        ["They ask you to keep secret meetings hidden from your parents", "They listen patiently without mockery, respect your dignity, and prioritize your safety", "They gossip about other students' problems", "They dismiss your feelings as stupid"], 1,
        "Trustworthy adults maintain safety, active listening, healthy boundaries, and mature responsibility.",
        ["Facing overwhelming anxiety and family conflict at home at {at}, {name} feels trapped and doesn't know who to turn to."],
        "How should {name} seek appropriate support?",
        [("Reach out to a trusted school counselor, favorite teacher, or school nurse during recess", "Accesses accessible institutional support channels.", True, "reach out to counselor|trusted teacher|school nurse", 45),
         ("State clearly: 'I am feeling overwhelmed and need help finding a safe way forward'", "Articulates distress clearly.", True, "state overwhelmed clearly|ask for help", 35),
         ("Know that if school adults are unavailable, national helplines like Tele-MANAS (14416) offer free support", "Leverages national crisis helplines.", False, "tele-manas 14416|childline 1098", 20)],
        ["keep suffering in silence", "turn to unverified strangers on internet chat rooms", "run away from home"],
        "Childline India 1098 - Ministry of Women and Child Development", "https://childlineindia.org"
    ))

    # FEEL-011: Moving to a new school or city
    cards.append(make_card(
        "FEEL-011", "echo", "Adaptation", "Starting fresh: Navigating a new school or city transition",
        ["junior", "middle", "senior"],
        ["Relocating to a new school or city triggers culture shock, grief for old friendships, and feelings of social disorientation.",
         "It takes an average of 3 to 6 months for a new environment to feel familiar; early loneliness is completely normal and temporary."],
        ["Give yourself permission to feel awkward; transitioning into new routines takes time", "Take initiative with low-pressure moves: smile, ask for directions, or offer to carry sports equipment", "Join at least one co-curricular club (choir, chess, sports, art) to connect over structured activities"],
        ["Never isolate yourself in corners with headphones on during every recess break", "Never compare the new school unfavorably in front of new classmates ('my old city was 100x better')"],
        "If you don't make three best friends on your very first day at a new school, you will be an outcast forever.", "myth", "Deep friendships take months of repeated proximity and shared experiences to develop. Give yourself time to settle in.",
        "What is the single most effective way to begin making friends when transferring to a new school?",
        ["Bragging about how much cooler your old school was", "Joining a school club or sports team where students collaborate around a shared activity", "Sitting alone with a hoodie over your eyes", "Insulting the teachers"], 1,
        "Co-curricular clubs provide structured shared tasks where casual conversations spark friendships naturally.",
        ["On their first week at a new school in a new city at {at}, {name} sits alone in the cafeteria feeling deeply homesick and awkward."],
        "How should {name} navigate this transition?",
        [("Recognize that early loneliness is a universal transition phase that eases over months", "Normalizes transitional adaptation timeline.", True, "transition takes time|homesick is normal|be patient", 40),
         ("Sign up for a sports team, science club, or drama group to meet peers naturally", "Engages in structured social environments.", True, "join sports or club|meet peers naturally", 40),
         ("Ask a classmate a simple question about school homework or cafeteria menus to break the ice", "Takes small, low-risk relational steps.", False, "ask simple question|break ice|small step", 20)],
        ["refuse to speak to anyone", "complain loudly that the new city is terrible", "skip school repeatedly"],
        "NCERT Guidelines on Guidance & Counseling for School Students", "https://ncert.nic.in"
    ))

    # FEEL-012: Coping with grief & loss
    cards.append(make_card(
        "FEEL-012", "echo", "Grief & Healing", "Grief and loss: Walking through bereavement with patience",
        ["junior", "middle", "senior"],
        ["Losing a beloved grandparent, parent, sibling, or pet triggers waves of sorrow, numbness, anger, and deep yearning.",
         "Grief does not follow a neat straight line; it comes in unpredictable waves that gradually become more manageable over time."],
        ["Allow yourself to cry and express sorrow without feeling embarrassed or weak", "Create a memory box, photo album, or journal preserving fond memories and lessons from your loved one", "Maintain basic physical routines: eat regular meals, drink water, and get fresh air even when sad"],
        ["Never tell yourself 'I should be over this by now'; there is no statutory timeline for grief", "Never bottle up painful emotions or pretend you don't care to look 'tough'"],
        "Properly grieving means crying for exactly one week, after which you should never feel sad about the person again.", "myth", "Grief comes in waves over years. You never 'get over' losing someone deeply loved; you learn to grow around the loss.",
        "What is the healthiest mindset when dealing with the painful loss of a loved one or family pet?",
        ["Force yourself to never mention their name again", "Allow feelings of sadness to surface without shame, while leaning on family support and fond memories", "Blame yourself for their death", "Lock yourself in a dark room for a year"], 1,
        "Patience, gentle self-care, and shared remembrance allow the heart to heal without suppression.",
        ["Following the passing of a beloved grandparent at {at}, {name} feels sudden bursts of tears during class and struggles to concentrate on schoolwork."],
        "How should {name} handle this season of bereavement?",
        [("Allow the tears to flow and explain to a kind teacher that you are currently grieving a family loss", "Communicates bereavement needs to educators.", True, "allow tears|tell teacher about loss|express sorrow", 45),
         ("Share memories and feelings openly with family members rather than isolating in secret", "Leans on shared familial support.", True, "share memories with family|talk openly", 35),
         ("Engage in a quiet reflective remembrance like planting a tree or creating a memory scrapbook", "Channels grief into meaningful tribute.", False, "plant tree|memory scrapbook|meaningful tribute", 20)],
        ["punish yourself for feeling sad", "pretend nothing happened", "turn to substance abuse"],
        "NIMHANS Bereavement and Grief Support Resources", "https://nimhans.ac.in"
    ))

    # FEEL-013: Overcoming fear of failure
    cards.append(make_card(
        "FEEL-013", "echo", "Growth Mindset", "The power of 'YET': Transforming fear of failure into growth",
        ["junior", "middle", "senior"],
        ["Stanford psychologist Carol Dweck demonstrated that a 'Fixed Mindset' views ability as static, while a 'Growth Mindset' views intelligence as a muscle.",
         "Adding the word 'YET' ('I don't understand quadratic equations YET') rewires the brain from defeat into constructive learning mode."],
        ["Replace 'I can't do this' with 'I haven't mastered this yet'", "Treat mistakes as diagnostic data showing exactly where your understanding needs reinforcement", "Focus praise and self-talk on effort, strategy, and perseverance rather than innate 'genius'"],
        ["Never avoid challenging subjects or sports competitions purely out of fear of looking foolish", "Never attach your core human worth to an exam score or competition rank"],
        "If you fail a mathematics test, it proves that your brain simply lacks the innate DNA for math.", "myth", "The brain possesses neuroplasticity; struggling through hard problems literally builds new neural synapses and mathematical ability.",
        "What simple three-letter word transforms a defeatist statement into an empowering growth mindset?",
        ["NOT", "YET", "WHY", "NOW"], 1,
        "'Yet' acknowledges current challenge while emphasizing that mastery develops through practice over time.",
        ["After scoring 35% on a class physics test at {at}, {name} throws down the paper declaring: 'I am terrible at physics, I give up.'"],
        "How can {name} reframe this setback with a growth mindset?",
        [("Reframe the thought: 'I don't understand these mechanics concepts YET, but I can improve with practice'", "Applies the neuroplastic growth mindset filter.", True, "power of yet|not understood yet|effort and practice", 45),
         ("Review the marked paper to identify specific concept gaps and error patterns", "Uses test as diagnostic learning data.", True, "analyze specific errors|concept gaps|diagnostic data", 35),
         ("Seek targeted help from a teacher or peer to practice 5 similar problem types", "Executes concrete corrective action.", False, "seek targeted help|practice 5 problems", 20)],
        ["rip up physics textbook", "conclude you are born stupid", "stop attending science classes"],
        "Mindset Works - Dr. Carol Dweck Research Foundation", "https://mindsetworks.com"
    ))

    # FEEL-014: Daily gratitude practice
    cards.append(make_card(
        "FEEL-014", "echo", "Positive Psychology", "Rewiring the negativity bias: The 3 Good Things exercise",
        ["junior", "middle", "senior"],
        ["The human brain evolved a natural 'negativity bias' that magnifies threats and forgets everyday blessings and safety.",
         "Spending 2 minutes writing down '3 Good Things' every evening physically rewires neural pathways, boosting optimism and sleep quality."],
        ["Write down 3 specific things that went well today before going to bed, no matter how small", "Note why each good thing happened ('I had a warm samosa because Mom thought of me')", "Express spontaneous verbal appreciation to people who help you (parents, conductors, sweepers)"],
        ["Never dismiss small joys (a cool breeze, a funny joke) as trivial or unworthy of gratitude", "Never use gratitude to toxicly invalidate genuine pain; gratitude complements problem solving"],
        "Practicing gratitude means pretending that bad things never happen and ignoring all life problems.", "myth", "Gratitude doesn't ignore hardship; it balances brain chemistry so you don't overlook daily goodness while solving life challenges.",
        "What is the proven neurological benefit of writing down 3 good things each evening?",
        ["It makes you forget everything you learned", "It counteracts evolutionary negativity bias and strengthens positive neural pathways", "It makes you sleep 18 hours straight", "It cures all viral infections"], 1,
        "Systematic gratitude practice trains the brain to notice resources, kindness, and beauty rather than only threats.",
        ["At the end of a tiring, stressful school day at {at}, {name} feels drained, grumpy, and convinced that the whole day was a disaster."],
        "How can {name} reset their mental state before sleeping?",
        [("Spend 3 minutes noting three concrete things that were positive during the day", "Exercises positive cognitive reframing.", True, "three good things|concrete positive moments|evening reset", 45),
         ("Reflect on the simple daily privileges often taken for granted: clean drinking water, a comfortable bed, family presence", "Cultivates perspective and emotional grounding.", True, "reflect on blessings|clean water|warm bed|perspective", 35),
         ("Notice how this gentle practice reduces nighttime anxiety and tension", "Recognizes positive emotional shifts.", False, "reduces tension|calm before sleep", 20)],
        ["scroll angry comments on social media before bed", "complain bitterly to siblings", "stew in resentment"],
        "Greater Good Science Center - UC Berkeley Gratitude Studies", "https://greatergood.berkeley.edu"
    ))

    # FEEL-015: Body image neutrality
    cards.append(make_card(
        "FEEL-015", "echo", "Self-Perception", "Body neutrality: Valuing what your body DOES over how it LOOKS",
        ["middle", "senior"],
        ["Commercial advertising, cinema, and social media airbrushing create impossible beauty standards that trigger body dysmorphia.",
         "Body neutrality moves beyond forced praise: instead of obsessing over whether your body is 'pretty', appreciate what your body enables you to DO."],
        ["Thank your legs for running, your lungs for breathing, and your hands for drawing or playing music", "Remember that fashion models and celebrities use heavy makeup, professional lighting, and AI filters", "Wear comfortable clothing that fits your current body comfortably rather than squeezing into painful sizes"],
        ["Never skip meals or adopt extreme starvation diets to look like an internet influencer", "Never make unsolicited comments on someone else's weight, skin shade, height, or facial features"],
        "Having visible acne, stretch marks, body hair, or skin pores is a medical defect that means you are dirty.", "myth", "Pores, textures, and body hair are universal biological traits. Airbrushed social media pictures erase normal human biology with digital software.",
        "What is the core philosophy of 'Body Neutrality'?",
        ["Constantly staring in the mirror reciting that you are the most gorgeous person alive", "Appreciating your body as an incredible instrument for living, learning, and feeling rather than an ornament for display", "Ignoring your body's need for food and water", "Wearing plastic bags to hide yourself"], 1,
        "Body neutrality frees young people from appearance obsession by focusing on functional health and capability.",
        ["Looking in the mirror at {at}, {name} feels miserable about emerging facial acne and wants to skip a school presentation."],
        "How should {name} reframe this self-conscious moment?",
        [("Recognize that adolescent acne is a natural hormonal phase experienced by nearly all teenagers", "Normalizes common developmental biology.", True, "acne is natural hormonal phase|universal among teens|normalize", 45),
         ("Shift focus to the valuable ideas in the presentation rather than facial aesthetics", "Prioritizes intellectual competence over appearance.", True, "focus on presentation ideas|competence over ornament", 35),
         ("Remember that classmates are thinking about their own insecurities rather than scrutinizing your skin", "Dispel the spotlight effect.", False, "dispel spotlight effect|others not scrutinizing", 20)],
        ["apply harsh bleaching chemicals to face", "skip school presentation out of shame", "refuse to leave the bedroom"],
        "Indian Association of Dermatologists, Venereologists and Leprologists (IADVL)", "https://iadvl.org"
    ))

    # FEEL-016: Handling class WhatsApp group drama
    cards.append(make_card(
        "FEEL-016", "echo", "Digital Dynamics", "Exiting group chat drama: Preserving peace over flame wars",
        ["junior", "middle", "senior"],
        ["Class WhatsApp and Discord groups frequently devolve into late-night gossip, meme mocking, exclusion, and aggressive flame wars.",
         "Getting drawn into typing frantic counter-attacks late at night drains emotional energy and creates permanent screenshot evidence."],
        ["Mute high-drama group chats for 8 hours or 1 year so notifications do not disrupt your peace", "Step back and ask: 'Will this argument matter in 1 month? Is typing a reply making anyone kinder?'", "Exit toxic group chats cleanly or speak to the group admin privately about basic civility rules"],
        ["Never forward cruel memes or screenshots targeting a classmate to other chat groups", "Never post personal secrets or intimate feelings into large peer group chats"],
        "If someone insults you in a class group chat, you must immediately insult them back with ten memes to protect your honor.", "myth", "Escalating flame wars gives trolls exactly the spectacle they desire. Muting, documenting violations, or walking away displays true strength.",
        "What is the most mature response when a class WhatsApp group erupts into malicious bullying against a classmate?",
        ["Add funny laughing emojis to stay on the bullies' good side", "Refuse to participate in the mockery, support the targeted classmate privately, and report the abuse to a teacher", "Forward the screenshots to 20 other groups", "Insult everyone's parents"], 1,
        "Refusing complicity, offering private empathy to the victim, and alerting adults stops bullying cycles without feeding drama.",
        ["At 10:30 PM at {at}, a class chat group erupts into a toxic argument where classmates exchange abusive voice notes and insults."],
        "How should {name} protect their peace of mind?",
        [("Resist the urge to jump into the late-night flame war and mute the group chat notifications", "Exercises healthy digital self-containment.", True, "do not join flame war|mute group notifications|protect peace", 45),
         ("Reach out privately to anyone being targeted with a kind message of solidarity", "Offers safe, empathetic 1-on-1 allyship.", True, "private solidarity message|check on victim", 35),
         ("Put the phone in another room to protect sleep and report severe cyberbullying to school tomorrow", "Safeguards rest and utilizes institutional safety channels.", False, "put phone away|sleep peacefully|report severe abuse", 20)],
        ["type abusive voice notes in rage", "forward drama to viral meme pages", "stay awake until 3 AM arguing"],
        "CERT-In Cyber Swachhta Kendra - Guidelines for Youth", "https://cyberswachhtakendra.gov.in"
    ))

    # FEEL-017: Talking to parents about mental health
    cards.append(make_card(
        "FEEL-017", "echo", "Family Communication", "Talking to parents: Bridging the mental health conversation gap",
        ["middle", "senior"],
        ["Many traditional parents dismiss emotional distress as 'just laziness' or 'too much mobile phone' because they grew up without mental health language.",
         "Approaching parents with vulnerability, specific symptoms, and patience bridges generational divides far better than angry shouting."],
        ["Choose a calm, quiet moment when parents are not stressed from work or chores to initiate the conversation", "Use 'I-statements': 'Mom/Dad, I have been feeling constantly exhausted and anxious for three weeks, and I need guidance'", "Frame mental health like physical health: 'Just like we see a doctor for high fever, I think speaking to a counselor would help me'"],
        ["Never begin a sensitive emotional conversation during the middle of a screaming argument", "Never dismiss parents as unloving simply because they initially struggle to understand clinical depression"],
        "If parents say 'just do yoga and study harder', it proves they completely hate you and you can never talk to them.", "myth", "Parents often respond with yoga/study out of genuine care filtered through limited past knowledge. Patient education bridges the gap.",
        "How should you phrase a request to see a counselor when speaking to traditional parents?",
        ["'You ruined my life and I hate this house!'", "'I have been struggling with persistent anxiety that is affecting my studies and sleep; could we consult a counselor together?'", "'Give me 50,000 rupees for therapy right now'", "'I am never taking another exam'"], 1,
        "Connecting emotional support to physical health, academic performance, and mutual partnership reassures parents and unlocks support.",
        ["At home at {at}, {name} has been feeling persistent dread and sadness for a month and wants to ask parents to consult a counselor."],
        "How should {name} structure this conversation?",
        [("Pick a quiet evening moment and express vulnerability using calm 'I feel' statements", "Chooses optimal timing and non-defensive framing.", True, "calm evening moment|I feel statements|vulnerability", 45),
         ("Explain specific physical impacts: difficulty sleeping, racing heart, and trouble concentrating on studies", "Anchors distress in tangible, relatable symptoms.", True, "concrete symptoms|trouble sleeping|concentration issues", 35),
         ("Suggest speaking together with a school counselor or family doctor as an accessible first step", "Provides low-barrier, reassuring professional entry point.", False, "school counselor first step|consult family doctor", 20)],
        ["scream during dinner that parents are toxic", "bottle it up until a complete breakdown", "run away"],
        "Tele-MANAS Guidelines for Adolescent-Parent Communication", "https://telemanas.mohfw.gov.in"
    ))

    # FEEL-018: Sleep, circadian rhythm, and mood
    cards.append(make_card(
        "FEEL-018", "echo", "Biological Foundations", "Sleep and emotional stability: Your brain's nightly wash cycle",
        ["junior", "middle", "senior"],
        ["During deep REM and slow-wave sleep, the brain's glymphatic system cleans out toxic metabolic waste and emotionally recalibrates the amygdala.",
         "Chronic sleep deprivation of under 7 hours produces emotional volatility, irritability, and depressive symptoms identical to clinical mood disorders."],
        ["Aim for 8 to 9 hours of uninterrupted sleep every night as a non-negotiable mental health foundation", "Keep bedroom dark and cool, and stop looking at blue-light screens at least 45 minutes before sleep", "Maintain consistent sleep and wake times even on weekends to synchronize your circadian rhythm"],
        ["Never sacrifice sleep as a badge of honor to prove how hard you study", "Never consume caffeinated energy drinks or coffee in the late afternoon or evening"],
        "Sleeping only 4 hours a night is a sign of high ambition and supreme mental discipline.", "myth", "Chronic sleep deprivation damages IQ, destroys working memory, impairs emotional control, and triggers long-term mental health breakdowns.",
        "What happens to your emotional regulation centers when you are severely sleep-deprived?",
        ["They become 10 times stronger and calmer", "The emotional amygdala becomes hyper-reactive while the prefrontal logical control center disconnects", "You become immune to sadness", "Nothing changes"], 1,
        "Sleep deprivation uncouples prefrontal regulatory control, making you prone to sudden crying, rage, and anxiety.",
        ["Preparing for unit tests at {at}, {name} sleeps only 4 hours for four consecutive nights and finds themselves bursting into tears over small mistakes."],
        "What is the most urgent intervention {name} needs?",
        [("Recognize that the emotional breakdown is a direct biological symptom of severe sleep debt", "Identifies physiological root cause of mood instability.", True, "recognize sleep debt symptom|biological root cause", 45),
         ("Prioritize getting 8 to 9 hours of solid recovery sleep tonight before doing any more revision", "Restores essential neurological regulation.", True, "prioritize 8 to 9 hours sleep|stop late studying", 35),
         ("Power down mobile screens and create a dark, quiet sleep environment", "Optimizes melatonin production and restorative sleep.", False, "turn off screens|dark quiet room", 20)],
        ["drink three cans of energy drink to stay up later", "assume you have gone permanently crazy", "skip school completely"],
        "National Sleep Foundation - Adolescent Sleep Health Guidelines", "https://sleepfoundation.org"
    ))

    return cards


def get_pixel_cards():
    cards = []

    # TECH-001: Screen time balance & digital boundaries
    cards.append(make_card(
        "TECH-001", "pixel", "Digital Habits", "Digital balance: Setting phone boundaries that stick",
        ["junior", "middle", "senior"],
        ["Smartphones are pocket slot machines engineered with infinite feeds and variable notifications to keep your attention captive.",
         "Setting intentional physical and temporal boundaries reclaims 3 to 4 hours of your day for real-world passions, fitness, and sleep."],
        ["Establish a 'phone curfew' by charging your phone outside your bedroom 60 minutes before bedtime", "Turn your phone screen to Grayscale (black & white) mode to eliminate visual dopamine rewards from icons", "Use app limits with passcode locks managed by yourself or a parent to enforce realistic cut-offs"],
        ["Never keep your smartphone right beside your pillow while sleeping", "Never check your notifications within the first 15 minutes of waking up in the morning"],
        "Using your phone for 7 hours a day on social media has zero impact on your academic or mental performance.", "myth", "Heavy screen time is clinically linked to attention fragmentation, decreased reading comprehension, and heightened anxiety.",
        "What simple screen display adjustment removes the addictive visual appeal of app icons and notifications?",
        ["Setting brightness to maximum", "Switching screen display to Grayscale (black and white)", "Using neon yellow wallpaper", "Inverting colors randomly"], 1,
        "Grayscale strips away the vibrant red and orange notification badges engineered by app designers to hook attention.",
        ["At home at {at}, {name} realizes they spent 5 hours scrolling through short-form video feeds instead of practicing guitar and doing homework."],
        "How should {name} establish healthy digital boundaries?",
        [("Switch phone screen to grayscale mode and place it in another room during study and sleep hours", "Reduces visual dopamine hooks and physical accessibility.", True, "switch to grayscale|keep phone in another room|phone curfew", 45),
         ("Set daily 30-minute hard app limits on video platforms using built-in digital wellbeing tools", "Automates behavioral boundaries through software timers.", True, "set 30 min app limit|digital wellbeing tools", 35),
         ("Substitute scrolling with hands-on physical activities: guitar practice, outdoor cycling, or board games", "Replaces passive consumption with active engagement.", False, "substitute real activities|guitar practice|outdoor cycling", 20)],
        ["delete all apps then reinstall them 2 hours later", "blame parents for having a phone", "give up all technology"],
        "Ministry of Electronics and IT - Digital Wellbeing Advisory", "https://meity.gov.in"
    ))

    # TECH-002: Notification diet
    cards.append(make_card(
        "TECH-002", "pixel", "Attention Management", "The notification diet: Silence the synthetic noise",
        ["junior", "middle", "senior"],
        ["Every notification chime triggers a cortisol and dopamine spike that interrupts your brain's flow state and takes 23 minutes to fully recover.",
         "Most notifications are not urgent messages from friends; they are corporate algorithms begging you to reopen their apps."],
        ["Turn off all notifications for shopping, gaming, video streaming, and news apps immediately", "Keep sound/vibration alerts enabled ONLY for direct phone calls and 1-on-1 human messages", "Schedule batch notification summaries twice a day rather than receiving real-time interruptions"],
        ["Never leave push notifications turned on for casual mobile games or shopping discounts", "Never allow flashing LED notification lights to disturb your study desk"],
        "You must keep all app notifications turned on so you don't miss breaking world news or flash sales.", "myth", "Push notifications are advertising channels, not emergency alarms. Turning off 90% of notifications restores hours of deep daily focus.",
        "How long does it take the human brain to regain deep focus after being interrupted by a single phone chime?",
        ["3 seconds", "Roughly 20 to 23 minutes", "2 hours", "Zero seconds"], 1,
        "Cognitive science shows task switching and attentional residue require over 20 minutes to return to deep concentration.",
        ["While working on a science project at {at}, {name}'s phone buzzes every 3 minutes with game energy alerts, sale coupons, and group chat memes."],
        "How should {name} execute a notification diet?",
        [("Open system settings and permanently disable notifications for all games, shopping, and social feeds", "Eliminates non-essential algorithmic distractions.", True, "disable non-essential notifications|turn off game alerts|shopping alerts off", 50),
         ("Enable 'Do Not Disturb' or Focus Mode during dedicated study blocks", "Shields working memory during deep study sessions.", True, "enable do not disturb|focus mode|study block", 30),
         ("Keep alerts active only for urgent direct calls from family members", "Preserves genuine emergency channels.", False, "family calls only|emergency channel", 20)],
        ["check phone at every single buzz", "throw phone at the wall", "leave all notifications on full volume"],
        "Cyber Swachhta Kendra - Mobile Hygiene Guidelines", "https://cyberswachhtakendra.gov.in"
    ))

    # TECH-003: Gaming limits & stopping loops
    cards.append(make_card(
        "TECH-003", "pixel", "Gaming Health", "Mastering gaming limits: Sunk cost and stopping cues",
        ["junior", "middle", "senior"],
        ["Modern competitive and online games deliberately eliminate 'stopping cues' (like chapters or quarters) to keep players locked in 'just one more match'.",
         "The 'sunk cost fallacy' tricks you into grinding hours for virtual armor or rank points that have zero utility outside the game server."],
        ["Set a clear end time BEFORE booting up a game (e.g., 'I will play exactly two matches or 45 minutes')", "Use an external physical alarm clock placed across the room rather than an easily dismissed phone banner", "Treat gaming as a delicious dessert earned after finishing homework and exercise, not the main course of your day"],
        ["Never play online games past midnight on school nights", "Never spend real family money or allowance on randomized digital weapon crates"],
        "Professional esports players play 16 hours a day without sleeping, so doing the same is good training.", "myth", "Top esports athletes follow strict physical workouts, sleep hygiene, nutrition, and mental health protocols to maintain reaction speed.",
        "What is a 'stopping cue' in digital media and games?",
        ["A button that turns off the internet", "A natural transition point (like the end of a chapter or match) that reminds you to pause and re-evaluate your time", "An in-game weapon", "A cheat code"], 1,
        "Stopping cues signal natural closure; games remove them intentionally to foster endless automatic play.",
        ["It is 10:30 PM on a school night at {at}. {name} lost three ranked battle royale matches in a row and wants to keep playing until winning."],
        "How should {name} overcome this gaming spiral?",
        [("Recognize the 'tilt' and sunk-cost trap: playing tired leads to worse gameplay and ruined tomorrow sleep", "Recognizes emotional tilt and cognitive fatigue.", True, "recognize tilt|sunk cost trap|stop playing when tired", 45),
         ("Firmly log off the console, power down the display, and head to bed", "Enforces discipline over impulse.", True, "log off console|power down|go to bed", 35),
         ("Remind yourself that virtual rank points do not matter compared to tomorrow's school performance", "Puts gaming status in perspective.", False, "rank points do not matter|school performance priority", 20)],
        ["play until 3 AM chasing one win", "smash controller in rage", "skip school tomorrow to sleep"],
        "WHO - Gaming Disorder Clinical Guidance", "https://who.int"
    ))

    # TECH-004: Doom-scrolling & news overload
    cards.append(make_card(
        "TECH-004", "pixel", "Information Diet", "Escaping doom-scrolling: Breaking the catastrophe news loop",
        ["middle", "senior"],
        ["Doom-scrolling is the compulsive habit of continuously scrolling through distressing, sensationalist disaster news and outrage online.",
         "Social media algorithms heavily favor terrifying headlines because human survival instincts prioritize threat detection above all else."],
        ["Notice the bodily sensation of doom-scrolling: tight chest, clenched jaw, shallow breathing, and rising dread", "Set a hard 10-minute daily timer for checking current events and get news from curated, reliable print/weekly summaries", "Practice 'scroll-stopping': physically stand up, stretch your arms, and look out the window at green trees"],
        ["Never consume sensationalist crime or disaster headlines right before closing your eyes to sleep", "Never share unverified terrifying breaking news videos on WhatsApp without fact-checking"],
        "Doom-scrolling through catastrophic news for three hours a day makes you a responsible, well-informed citizen.", "myth", "Compulsive doom-scrolling causes learned helplessness, severe anxiety, and emotional paralysis without helping a single victim.",
        "Why do social media algorithms consistently serve catastrophic, negative news to your feed?",
        ["Because only bad things happen in the universe", "Because threatening news hooks human survival attention and keeps eyes on screen longer for ad revenue", "Because algorithms want you to be safe", "Because government mandates it"], 1,
        "Fear and outrage generate the highest engagement metrics, which algorithms exploit for commercial profit.",
        ["Lying in bed at {at}, {name} spends 90 minutes scrolling through horrifying stories of wars, plane crashes, and epidemics, feeling sick with anxiety."],
        "What immediate action should {name} take?",
        [("Recognize the doom-scrolling loop, physically place the phone on the desk, and stand up", "Breaks the physical trance state.", True, "break doom scrolling trance|put phone on desk|stand up", 45),
         ("Drink a glass of water and replace digital dread with calming physical reality (reading a book or deep breathing)", "Re-grounds the nervous system in immediate safety.", True, "drink water|calming reality|deep breathing", 35),
         ("Delete sensationalist algorithm-driven news aggregators from the phone", "Removes the source of toxic information overload.", False, "delete news aggregators|curate information diet", 20)],
        ["keep scrolling until dawn", "forward scary posts to all classmates", "believe the world is ending tomorrow"],
        "NIMHANS Guidelines on Media Consumption & Mental Well-being", "https://nimhans.ac.in"
    ))

    # TECH-005: Phone-free meal tables
    cards.append(make_card(
        "TECH-005", "pixel", "Interpersonal Presence", "Phone-free meals: Reclaiming human connection at the dinner table",
        ["junior", "middle", "senior"],
        ["'Phubbing' (phone snubbing) is the act of ignoring the living people sitting right across from you to stare at a glowing glass screen.",
         "Family meal tables without digital screens are the single strongest predictor of adolescent emotional resilience and vocabulary development."],
        ["Keep the dining table a sacred 100% phone-free zone for the entire family", "Place all phones in a basket or on a side table on silent mode during dinner", "Ask engaging table conversation questions: 'What was the funniest thing that happened today?'"],
        ["Never scroll social feeds, text friends, or watch YouTube videos while eating meals with others", "Never leave your phone face-up on the dining table where flashing screens interrupt conversations"],
        "Having your phone sitting face-up on the dinner table has zero effect on conversation quality if it is on silent.", "myth", "Studies prove the mere visible presence of a phone on a table reduces conversation depth, empathy, and interpersonal trust.",
        "What is the term used by psychologists for ignoring the people right in front of you in favor of your smartphone?",
        ["Multi-texting", "Phubbing (Phone Snubbing)", "Screen diving", "Digital surfing"], 1,
        "Phubbing damages personal relationships and signals to loved ones that a screen is more important than their presence.",
        ["During dinner with family at {at}, {name}'s phone chimes with non-urgent Instagram comments, and {name} reaches to unlock it."],
        "How should {name} handle this social situation?",
        [("Leave the phone untouched and place it face-down away from the dinner table", "Prioritizes immediate family presence over digital pings.", True, "leave phone untouched|place face down away|prioritize family", 45),
         ("Engage actively in conversation with family members about their day", "Cultivates genuine interpersonal connection.", True, "engage in family conversation|listen actively", 35),
         ("Suggest a family rule where everyone deposits devices in a basket during meal times", "Builds collective healthy digital norms.", False, "family device basket|screen free meals", 20)],
        ["eat while texting with both hands", "ignore family questions to watch reels", "wear headphones at dinner"],
        "Indian Academy of Pediatrics (IAP) - Screen Time Guidelines", "https://iapindia.org"
    ))

    # TECH-006: Deep work & study focus
    cards.append(make_card(
        "TECH-006", "pixel", "Deep Work", "Deep study focus: The Pomodoro technique and phone separation",
        ["junior", "middle", "senior"],
        ["Human multitasking is a neurological myth; the brain cannot focus on two complex tasks simultaneously, it merely switches back and forth frantically.",
         "Studying with a phone buzzing nearby reduces effective IQ and doubles the hours required to memorize textbook material."],
        ["Use the Pomodoro Technique: 25 minutes of 100% distraction-free study followed by a strict 5-minute break", "Physically place your phone in another room or inside a closed drawer while studying", "Use website blockers on your computer to lock distracting entertainment portals during homework hours"],
        ["Never attempt to study for difficult exams with a video stream playing in the corner of your screen", "Never respond to text messages during active 25-minute study sprints"],
        "Gen Z brains have evolved to multitask effortlessly between calculus homework, music, and group texting at the same time.", "myth", "Human brain architecture has not changed. Multitasking creates superficial learning, frequent errors, and cognitive exhaustion.",
        "What is the core structure of the classic 'Pomodoro Technique' for academic study?",
        ["Studying for 10 hours straight without food", "25 minutes of single-task focused study followed by a 5-minute restorative break", "Checking social media every 2 minutes", "Studying only while eating tomatoes"], 1,
        "The 25/5 rhythm matches optimal human attention spans and prevents mental fatigue during revision.",
        ["At the study desk at {at}, {name} needs to prepare three chapters of biology but keeps picking up the phone every 4 minutes to check messages."],
        "How should {name} structure their study environment?",
        [("Physically walk the phone into another room or drawer and turn on Do Not Disturb", "Removes visual and physical cognitive temptation.", True, "phone in another room|drawer|do not disturb", 45),
         ("Set a kitchen or desk timer for 25 minutes of single-task biology reading", "Implements Pomodoro focus sprint.", True, "25 minute timer|pomodoro sprint|single task study", 35),
         ("Reward yourself with a 5-minute stretch or walk after completing the focus block", "Provides clean, restorative break without digital relapse.", False, "5 min stretch break|restorative pause", 20)],
        ["keep phone open next to textbook", "reply to every text instantly", "study with music videos playing"],
        "CBSE Guidance on Study Skills and Concentration", "https://cbse.gov.in"
    ))

    # TECH-007: In-game spending discipline
    cards.append(make_card(
        "TECH-007", "pixel", "Gaming Economics", "Resisting microtransactions: Virtual cosmetics vs real wealth",
        ["junior", "middle", "senior"],
        ["Free-to-play mobile games employ behavioral dark patterns, fake countdowns, and peer pressure to sell virtual gun skins and dance emotes.",
         "Spending real rupee money on pixels inside a game yields zero tangible value; when the game server shuts down, all skins vanish permanently."],
        ["Set a firm rule: Never spend real currency on cosmetic skins that do not alter core gameplay", "If you want to make an in-game purchase, wait a mandatory 72-hour cooling-off period before deciding", "Never memorize or store parental credit cards or UPI details inside app stores"],
        ["NEVER secretly use a parent's credit card or banking OTP to purchase game passes", "NEVER fall for scams promising 'free diamonds' or 'free V-bucks' in exchange for account passwords"],
        "Buying rare limited-edition weapon skins in online games is a smart financial investment that will make you wealthy later.", "myth", "Game terms of service forbid real-money account trading, and game economies crash regularly. Virtual cosmetics are pure consumable expenses.",
        "What happens to all your purchased in-game weapon skins and character outfits when the game developer closes the game servers?",
        ["They get transferred to your bank account", "They disappear completely and permanently with zero compensation", "The government reimburses you", "They turn into real physical clothes"], 1,
        "You do not own virtual items; you merely hold a temporary, revocable license that expires when servers shut down.",
        ["A new limited-time mythical character skin appears in {name}'s favorite battle game at {at} for Rs 1,499, expiring in 12 hours."],
        "How should {name} evaluate this virtual purchase?",
        [("Recognize the artificial scarcity countdown as a dark marketing pattern designed to trigger impulse buys", "Identifies deceptive urgency marketing.", True, "artificial scarcity|marketing trick|resist fake countdown", 45),
         ("Remember that Rs 1,499 represents real family money that could fund books, shoes, or long-term savings", "Compares virtual utility to real-world purchasing power.", True, "real money utility|1499 for books or savings", 35),
         ("Refuse to spend real money on cosmetic pixels that offer zero gameplay improvement", "Enforces sound spending boundaries.", False, "refuse cosmetic spending|zero real value", 20)],
        ["steal parent phone to authorize transaction", "borrow money from peers to buy skin", "fall for scam diamond websites"],
        "Ministry of Consumer Affairs - Advisory on E-Gaming Microtransactions", "https://consumeraffairs.nic.in"
    ))

    # TECH-008: App age ratings and content appropriateness
    cards.append(make_card(
        "TECH-008", "pixel", "Content Safety", "App age ratings: Protecting developing brains from adult content",
        ["junior", "middle", "senior"],
        ["Age ratings on games and apps (PEGI 18, ESRB M, 13+) exist because developing adolescent brains process extreme violence, horror, and sexual themes differently than adults.",
         "Premature exposure to hyper-graphic violence and adult themes desensitizes emotional empathy and triggers chronic sleep disturbances."],
        ["Check app and game age ratings (12+, 16+, 18+) before downloading new titles", "Respect age restrictions: they are designed by neuroscientists and psychologists to safeguard adolescent mental development", "Talk openly with parents if you accidentally stumble across graphic, violent, or disturbing web content"],
        ["Never fake your date of birth to bypass 18+ restrictions on adult gambling or dating apps", "Never peer-pressure younger siblings or juniors into watching graphic horror movies or adult games"],
        "Age ratings on video games are just pointless suggestions made by boring adults with no real scientific basis.", "myth", "Age ratings reflect clinical research on cognitive readiness, emotional trauma processing, and addiction vulnerability in youth.",
        "What does an '18+' or 'Mature' rating on a video game indicate?",
        ["The game is suitable for kindergarten children", "The game contains graphic violence, mature sexual content, or intense themes unsuitable for developing adolescents", "The game costs 18 rupees", "The game takes 18 hours to complete"], 1,
        "Mature ratings warn that content requires adult emotional maturity to process without psychological distress.",
        ["At a friend's house at {at}, peers want to boot up an ultra-violent 18+ horror survival game known for extreme gore and torture scenes."],
        "How should {name} respond?",
        [("Politely decline to play graphic 18+ horror, suggesting an engaging multiplayer alternative suitable for the group", "Sets comfortable personal boundary against distressing content.", True, "decline 18+ horror|suggest multiplayer alternative|boundary", 45),
         ("Recognize that setting boundaries around what enters your mind protects your mental health and sleep", "Values mental wellbeing over peer conformity.", True, "protect mental health|care for mind|no peer pressure", 35),
         ("Leave the room comfortably if others insist on playing disturbing content", "Removes self from uncomfortable environment calmly.", False, "leave room comfortably|remove self", 20)],
        ["force yourself to watch and suffer nightmares for weeks", "mock friends who feel scared", "lie about age online"],
        "Ministry of Information and Broadcasting - Digital Content Classification", "https://mib.gov.in"
    ))

    # TECH-009: Nighttime posting and delayed reactions
    cards.append(make_card(
        "TECH-009", "pixel", "Online Conduct", "The midnight rule: Never post or message when tired or angry",
        ["middle", "senior"],
        ["Late at night, your prefrontal cortex is depleted, your inhibitions drop, and emotional impulses dominate your judgment.",
         "Frantic midnight texts, impulsive romantic confessions, and angry comments posted after 11 PM account for 80% of digital regrets."],
        ["Enforce the 'Midnight Rule': Never send a sensitive, emotional, or confrontational text after 10 PM", "Save passionate, angry messages as drafts and sleep on them; review them with fresh eyes tomorrow morning", "Put your phone away across the room when settling in for bed"],
        ["Never hit 'Send' on a heated argument while lying in bed in the dark", "Never post personal vulnerability rants on public social media stories late at night"],
        "If someone insults you online at midnight, you must reply within 60 seconds or you look weak.", "myth", "Late-night replies look reckless and reactive. Replying with cool, calculated composure the next morning shows mastery and power.",
        "What is the golden rule regarding angry or emotionally intense text drafts typed late at night?",
        ["Send them immediately with five exclamation marks", "Save the message as a draft, sleep on it, and review it in daylight before deciding to send", "Post it on your public Instagram story", "Send it to their parents"], 1,
        "Sleeping on emotional drafts allows prefrontal executive function to restore, preventing embarrassing relationship catastrophes.",
        ["At 11:45 PM in bed at {at}, {name} receives a rude, sarcastic message from a peer and types out a furious, 4-paragraph scathing counter-attack."],
        "What should {name} do before hitting Send?",
        [("Pause and apply the midnight rule: do NOT send the message right now", "Enforces impulse control during neurological fatigue.", True, "apply midnight rule|do not send now|pause", 45),
         ("Save the text in a notes app or draft, put the phone down, and go to sleep", "Allows restorative sleep to clear emotional adrenaline.", True, "save as draft|sleep on it|put phone down", 35),
         ("Reread the draft in the morning to decide whether a calm 1-sentence reply is even necessary", "Exercises daylight perspective.", False, "reread in morning|calm reply if needed", 20)],
        ["hit send immediately in rage", "forward screenshot to public groups", "call peer repeatedly to scream"],
        "Cyber Swachhta Kendra - Netiquette for Young Citizens", "https://cyberswachhtakendra.gov.in"
    ))

    # TECH-010: Group chat notification overload
    cards.append(make_card(
        "TECH-010", "pixel", "Digital Peace", "Muting the chaos: Surviving 50-person group chats",
        ["junior", "middle", "senior"],
        ["Large school, sports, and social group chats generate hundreds of meaningless memes, stickers, and side chatter every hour.",
         "Feeling obligated to read every single group chat bubble creates continuous background anxiety and drains battery and study time."],
        ["Mute large group chats permanently or for 1 year, checking them on YOUR schedule once or twice a day", "Turn off auto-download for photos and videos in WhatsApp to save phone storage and cellular data", "Use group chats for functional logistics (homework questions, event times), not endless 24/7 banter"],
        ["Never feel guilty for missing 200 unread memes in a school chat group", "Never post large chain letters, spam forwarding messages, or unverified rumors into group chats"],
        "You have a social obligation to read every single message and respond with an emoji in every group chat you belong to.", "myth", "Group chats are broadcast channels, not private conversations. Constantly checking group chats fractures your attention span.",
        "What WhatsApp setting protects your phone storage from being clogged with thousands of forwarded memes and videos?",
        ["Turning brightness down", "Disabling 'Media Auto-Download' in chat settings", "Deleting your account", "Using airplane mode forever"], 1,
        "Disabling media auto-download stops thousands of useless media files from automatically filling your phone storage.",
        ["{name}'s phone at {at} receives 450 notifications in one afternoon from an energetic school dance group chat discussing song ideas."],
        "How should {name} manage this digital overload?",
        [("Mute the group chat for 1 year so alerts do not buzz continuously", "Protects focus and peace of mind effortlessly.", True, "mute group chat 1 year|silence alerts|stop buzzing", 50),
         ("Schedule a dedicated 10-minute window in the evening to review key announcements", "Batches information consumption efficiently.", True, "review on own schedule|batch check evening", 30),
         ("Disable automatic media downloads to preserve device storage and mobile data", "Prevents storage clutter.", False, "disable media auto download|save storage", 20)],
        ["leave and rejoin the group 10 times in anger", "scream at classmates to stop texting", "throw phone in water"],
        "CERT-In Guidelines on Safe Messaging Practices", "https://cert-in.org.in"
    ))

    # TECH-011: Walking and commuting with screens
    cards.append(make_card(
        "TECH-011", "pixel", "Physical Safety", "Zombie walking: Why staring at screens while walking is deadly",
        ["junior", "middle", "senior"],
        ["'Distracted walking' while texting or watching videos narrows your peripheral vision by 90%, blinding you to open manholes, stairs, and traffic.",
         "Pedestrians using phones have a 4x higher risk of collision with motor vehicles, electric scooters, and train platforms."],
        ["Keep your phone safely in your pocket or backpack whenever your feet are moving outdoors", "If you must answer an urgent message, step completely aside against a building wall and stop moving", "Never wear noise-cancelling headphones over both ears while crossing busy roads or railway tracks"],
        ["NEVER cross a road, pedestrian zebra crossing, or railway track while looking at a phone screen", "NEVER walk down school staircases with your eyes glued to a mobile video"],
        "Walking while texting is completely safe because peripheral vision automatically alerts you to all oncoming traffic.", "myth", "Cognitive tunneling blinds distracted pedestrians. People staring at screens regularly walk straight into open drains, poles, and moving cars.",
        "What happens to your field of situational awareness when you walk while looking down at a smartphone?",
        ["It expands by 200%", "It narrows by up to 90%, leaving you oblivious to approaching vehicles and road hazards", "It makes your reflexes twice as fast", "Nothing changes"], 1,
        "Looking down creates severe cognitive tunneling, rendering you completely blind to environmental hazards.",
        ["While walking home from school along a busy road at {at}, {name}'s phone buzzes with a video link from a friend."],
        "What should {name} do?",
        [("Keep the phone in your pocket and keep eyes and ears focused on traffic until reaching home safely", "Prioritizes immediate physical survival over digital content.", True, "keep phone in pocket|eyes on traffic|safety first", 50),
         ("If truly urgent, step safely off the roadway onto a wide sidewalk corner before glancing at the screen", "Stops movement before checking device.", True, "step aside safely|stop moving before checking", 30),
         ("Remove headphones or keep volume low so approaching vehicle horns are clearly audible", "Maintains vital auditory situational awareness.", False, "remove headphones|hear vehicle horns", 20)],
        ["watch video while crossing busy intersection", "text while walking down stairs", "ignore approaching bus"],
        "Ministry of Road Transport and Highways (MoRTH) - Pedestrian Safety Advisory", "https://morth.nic.in"
    ))

    # TECH-012: Healthy video watching habits
    cards.append(make_card(
        "TECH-012", "pixel", "Content Consumption", "Intentional viewing: Taming the infinite video algorithm",
        ["junior", "middle", "senior"],
        ["Video platforms use autoplay, recommended feeds, and variable short-form clips to keep viewers in a semi-hypnotic consumption trance.",
         "Shifting from passive algorithmic feeding to intentional, active searching restores control over what enters your mind."],
        ["Turn OFF 'Autoplay' in YouTube and streaming app settings so videos do not play automatically", "Search specifically for what you want to learn, watch it, and then close the browser tab", "Ask yourself every 20 minutes: 'Did I choose to watch this, or did an algorithm pick it for me?'"],
        ["Never click on hyper-sensationalist clickbait thumbnails designed to outrage or shock you", "Never leave video streams running in the background all night while falling asleep"],
        "Video recommendation algorithms care deeply about your education, character, and mental health.", "myth", "Algorithms have one single commercial objective: maximize time-on-screen to sell more advertisements, regardless of content quality.",
        "What setting on YouTube prevents the app from immediately starting a new video when your current video finishes?",
        ["Turning on captions", "Disabling 'Autoplay'", "Increasing playback speed to 2x", "Lowering screen brightness"], 1,
        "Disabling autoplay restores an essential stopping cue, allowing you to choose whether to continue or close the app.",
        ["{name} opens a video app at {at} to watch a 5-minute physics tutorial, but finds themselves clicking through gaming drama clips 45 minutes later."],
        "How should {name} take back control?",
        [("Turn off Autoplay and close the video platform immediately upon finishing the physics tutorial", "Restores intentionality and enforces stopping cues.", True, "turn off autoplay|close tab after tutorial|intentionality", 45),
         ("Clean your watch history and click 'Not Interested' on clickbait recommendation rabbit holes", "Retrains algorithmic feed recommendations.", True, "clean watch history|click not interested|retrain algorithm", 35),
         ("Bookmark direct educational playlists rather than browsing the chaotic homepage feed", "Eliminates algorithmic homepage traps.", False, "bookmark direct playlists|avoid homepage feed", 20)],
        ["keep watching clickbait for another 3 hours", "blame physics for being boring", "leave videos playing all night"],
        "Digital India - Safe Internet Surfing Practices", "https://digitalindia.gov.in"
    ))

    # TECH-013: The 24-hour weekend digital detox
    cards.append(make_card(
        "TECH-013", "pixel", "Digital Fasting", "The weekend digital detox: Rediscovering the physical world",
        ["middle", "senior"],
        ["Taking a 24-hour break from screens on a Saturday or Sunday resets your dopamine baseline, lowers cortisol, and sparks creative clarity.",
         "Unplugged time frees up hours for deep conversations, outdoor sports, cooking, reading physical books, and tactile creativity."],
        ["Choose a specific 24-hour window (e.g., Saturday 6 PM to Sunday 6 PM) for your digital detox", "Inform family and close friends in advance: 'I am taking a screen-free day, call my home landline or parent if urgent'", "Plan tactile physical activities in advance: hiking, sketching, board games, cycling, or baking"],
        ["Never treat a screen-free day as punishment; view it as a luxurious retreat for your brain", "Never keep your phone in your pocket during a detox day; lock it in a desk drawer"],
        "Taking one day off from your smartphone will cause your social relationships to completely collapse.", "myth", "Real friends respect digital detoxes. Disconnecting for 24 hours rejuvenates your mental energy and deepens real-world presence.",
        "What is the primary neurological benefit of an occasional 24-hour digital detox?",
        ["Your phone charges 500% faster", "It resets overstimulated dopamine receptors and restores attention stamina and presence", "It cures myopia completely", "It makes you forget how to type"], 1,
        "Stepping away from hyper-stimulating screens resets dopamine baselines, making everyday real-world activities feel enjoyable again.",
        ["On Sunday morning at {at}, {name} realizes they feel constantly anxious, irritable, and chained to their glowing phone screen."],
        "How should {name} plan and execute a restorative digital detox?",
        [("Turn off the smartphone, store it in a drawer, and declare a 24-hour screen-free retreat", "Initiates clean physical boundary from digital stimulation.", True, "turn off phone|store in drawer|24 hour screen free", 50),
         ("Fill the day with immersive offline activities: playing football, reading a paper novel, and cooking with family", "Replaces digital dopamine with healthy tactile stimulation.", True, "offline activities|football|paper novel|cooking with family", 30),
         ("Notice the return of mental stillness, creative thoughts, and deep restful sleep", "Reaps the cognitive rewards of unplugged time.", False, "mental stillness|creative clarity|deep sleep", 20)],
        ["stare at the locked drawer complaining of boredom", "cheat by using a tablet instead", "quit after 5 minutes"],
        "National Institute of Mental Health and Neurosciences - Digital Detox Advisory", "https://nimhans.ac.in"
    ))

    # TECH-014: Follower count & like addiction
    cards.append(make_card(
        "TECH-014", "pixel", "Self-Worth", "Vanity metrics: Why follower counts do not equal human worth",
        ["middle", "senior"],
        ["Social media 'likes', 'views', and follower counts are vanity metrics engineered by ad tech companies to trigger slot-machine dopamine loops.",
         "Tying your self-esteem to fluctuating social metrics makes you emotionally vulnerable to internet algorithms and anonymous trolls."],
        ["Remember: A post with 5 likes is not inferior to a post with 50,000 likes; algorithms measure virality, not truth or beauty", "Turn off public like counts in Instagram settings to liberate yourself from metric anxiety", "Focus on the quality of your real-world character: Are you loyal, trustworthy, hardworking, and kind?"],
        ["Never delete a creative drawing or essay you love just because it didn't get enough online likes", "Never engage in dangerous stunts, pranks, or humiliating acts to chase viral views"],
        "The number of followers you have on Instagram or YouTube is an accurate measure of how smart, beautiful, and successful you are.", "myth", "Follower counts measure sensationalism, algorithmic favor, or paid promotion—never wisdom, integrity, or true happiness.",
        "What setting on major social platforms helps disconnect your self-worth from engagement approval?",
        ["Buying fake bot followers", "Hiding like and view counts on posts", "Posting 50 selfies a day", "Using extreme face filters"], 1,
        "Hiding like counts removes the public scorecard, allowing you to share and consume content without constant comparison anxiety.",
        ["{name} spends four hours painting a watercolor landscape at {at}, posts it online, and feels heartbroken when it receives only 6 likes."],
        "How should {name} reframe this creative experience?",
        [("Remember that the intrinsic joy and artistic growth of painting is what truly matters, not an algorithm's score", "Restores internal locus of creative evaluation.", True, "intrinsic joy of painting|artistic growth|ignore vanity score", 45),
         ("Recognize that social algorithms prioritize controversial outrage over delicate art", "Understands technical mechanics of platform distribution.", True, "algorithms favor outrage over art|not reflection of talent", 35),
         ("Display the physical painting proudly in your room or gift it to a friend who appreciates it", "Anchors art in meaningful real-world connection.", False, "display painting in room|gift to friend", 20)],
        ["tear up painting in tears", "spend money buying fake bot likes", "quit art forever"],
        "UNICEF - The Psychology of Social Media Metrics on Youth", "https://unicef.org"
    ))

    # TECH-015: Warning signs of digital addiction
    cards.append(make_card(
        "TECH-015", "pixel", "Addiction Awareness", "Spotting screen addiction: Recognizing the red flags",
        ["junior", "middle", "senior"],
        ["Digital addiction is characterized by loss of control over screen use, withdrawal irritability when offline, and neglect of essential life duties.",
         "Catching digital overuse early through self-assessment prevents severe academic failure, physical posture degradation, and social isolation."],
        ["Watch for red flags: lying about screen time, feeling restless/angry when disconnected, neglecting meals and hygiene", "Take an honest weekly self-inventory: Are your grades slipping? Are you sleeping less than 7 hours? Are real friendships fading?", "Ask for help from parents, school counselors, or clinics (like SHUT clinic at NIMHANS) if you cannot stop alone"],
        ["Never steal money, lie to family, or skip school to feed an online gaming habit", "Never dismiss friends or parents when they express loving concern about your device obsession"],
        "Because everyone carries a smartphone, it is scientifically impossible to become addicted to screens.", "myth", "Behavioral addictions hijack the exact same dopamine reward circuits as chemical dependencies. Clinical screen addiction is recognized globally by WHO.",
        "Which of the following is a recognized clinical warning sign of behavioral screen addiction?",
        ["Charging your phone when the battery reaches 10%", "Experiencing intense anger, agitation, or panic whenever the phone is temporarily removed", "Using a phone calculator for math homework", "Calling your grandmother on weekends"], 1,
        "Severe emotional distress or aggression when separated from devices indicates psychological dependency.",
        ["At home at {at}, {name}'s parents ask to put away the phone for dinner, and {name} screams in fury, feeling uncontrollable panic and rage."],
        "How should {name} reflect upon this intense reaction?",
        [("Recognize the intense anger as a serious warning sign of digital dependency and neurological dysregulation", "Identifies behavioral addiction red flag objectively.", True, "recognize rage as addiction warning|loss of control|dependency", 50),
         ("Acknowledge that parents are trying to help establish healthy life balance, not attack you", "Replaces defensive hostility with understanding.", True, "acknowledge parents care|healthy balance", 30),
         ("Agree together on structured daily screen windows and seek school counseling support if rage persists", "Collaborates on constructive intervention.", False, "agree on structured limits|counseling if needed", 20)],
        ["smash dinner plates in rage", "lock bedroom door and refuse to eat", "run away from home with phone"],
        "NIMHANS SHUT Clinic (Service for Healthy Use of Technology)", "https://nimhans.ac.in"
    ))

    # TECH-016: Device physical hygiene
    cards.append(make_card(
        "TECH-016", "pixel", "Hardware Care", "Device hygiene: Cleaning screens safely and protecting hardware",
        ["junior", "middle", "senior"],
        ["Smartphone screens harbor more bacteria than a toilet seat; regular gentle cleaning prevents acne, skin infections, and device decay.",
         "Taking physical care of your digital tools (cables, keyboards, screens) extends their lifespan and teaches financial stewardship."],
        ["Clean glass screens using a dry microfiber cloth; lightly dampen with 70% isopropyl alcohol for disinfection", "Never spray liquids, soapy water, or harsh household window cleaners directly onto device ports or screens", "Gently coil charging cables in wide loops; never bend or yank cords sharply from the plug head"],
        ["Never eat crumbly snacks directly over laptop keyboards or drop sticky juice onto game controllers", "Never use metal safety pins or needles to dig dirt out of phone charging ports"],
        "Washing your smartphone screen with running tap water and dish soap is the best way to sanitize it.", "myth", "Water and soap penetrate microphone meshes and speaker grilles, destroying internal motherboards. Use dry microfiber and alcohol wipes only.",
        "What is the safest material to use when wiping dust, oil, and fingerprints off a glass smartphone or tablet screen?",
        ["Rough paper towels or sandpaper", "A clean microfiber cloth (like the ones used for spectacles)", "A wet soapy bathroom sponge", "Steel wool"], 1,
        "Microfiber lifts skin oils and dust without scratching delicate anti-fingerprint oleophobic glass coatings.",
        ["At the study desk at {at}, {name}'s phone screen is coated in greasy fingerprints and study desk dust, and the charging cable is frayed near the connector."],
        "How should {name} properly maintain this hardware?",
        [("Wipe the screen gently with a clean dry microfiber cloth, avoiding harsh liquid sprays into ports", "Applies safe screen cleaning technique.", True, "microfiber cloth|gentle wipe|avoid liquid in ports", 45),
         ("Stop yanking cables by the thin wire; grasp the hard plastic plug head to disconnect safely", "Protects electrical cable integrity.", True, "grasp plug head|never yank cord|reinforce cable", 35),
         ("Keep food, beverages, and open water bottles away from electronic keyboards and tablets", "Prevents catastrophic liquid spills.", False, "keep drinks away|food away from devices", 20)],
        ["run phone under bathroom tap", "clean screen with glass bleach and steel wool", "yank cable from 3 meters away"],
        "Consumer Electronics Safety & Maintenance Guidelines", "https://bis.gov.in"
    ))

    # TECH-017: Leveraging technology for real creation
    cards.append(make_card(
        "TECH-017", "pixel", "Creative Agency", "Consumer to creator: Using tech to build, compose, and solve",
        ["middle", "senior"],
        ["The greatest tragedy of the smartphone era is reducing a miraculous supercomputer into a passive entertainment pacifier.",
         "Transforming from a passive digital consumer into an active digital creator (coding, 3D modeling, music production, writing) builds true agency."],
        ["Shift your screen ratio: For every 1 hour of passive video consumption, spend 1 hour actively building or creating", "Learn foundational digital creation tools: Python programming, Canva/Figma visual design, Audacity audio editing", "Use the internet to publish educational tutorials, open-source code, digital art, or community journalism"],
        ["Never allow technology to keep you entirely in the role of a passive, paying customer", "Never assume that creating software or digital media is reserved only for geniuses"],
        "Smartphones and computers are designed exclusively for playing games, scrolling memes, and streaming movies.", "myth", "Computers are bicycles for the mind. They are the most powerful creative, scientific, and enterprise instruments ever invented.",
        "What characterizes an active 'digital creator' mindset compared to a passive 'digital consumer'?",
        ["Watching 10 hours of video game walkthroughs per day", "Using digital software to write code, design artwork, compose music, or solve community problems", "Buying every new phone model on launch day", "Commenting angry emojis on celebrity pages"], 1,
        "Creators leverage technology as an expressive tool to solve problems, build assets, and share original value.",
        ["During school holidays at {at}, {name} realizes they have spent 6 hours every day watching other people play sandbox games."],
        "How can {name} transition from consumer to creator?",
        [("Decide to use the computer to design their own game levels, write stories, or learn basic Python coding", "Channels time into active digital production.", True, "learn python coding|design game levels|create original content", 50),
         ("Follow free structured courses on creative platforms like Atal Tinkering Labs or Khan Academy", "Leverages free, world-class educational tools.", True, "free creative courses|atal tinkering labs|structured learning", 30),
         ("Share an original creation with classmates for constructive feedback rather than just consuming others' work", "Builds confidence and community through creation.", False, "share original work|seek feedback", 20)],
        ["watch 8 hours of gaming streams instead", "believe you can never learn to code", "give up on technology completely"],
        "Atal Innovation Mission - Atal Tinkering Labs", "https://aim.gov.in"
    ))

    # TECH-018: Ergonomics & 20-20-20 eye rule
    cards.append(make_card(
        "TECH-018", "pixel", "Physical Wellbeing", "Screen ergonomics: Defeating 'Text Neck' and the 20-20-20 eye rule",
        ["junior", "middle", "senior"],
        ["Bending your neck forward at a 60-degree angle to look down at a phone places 27 kilograms of crushing gravitational pressure on your cervical spine.",
         "Staring at nearby digital screens reduces blink rates by 50%, causing dry eye syndrome, ocular strain, and progressive myopia."],
        ["Apply the 20-20-20 Rule: Every 20 minutes, look at an object at least 20 feet (6 meters) away for 20 seconds", "Hold your phone up closer to eye level rather than dropping your chin to your chest ('bring phone to eyes, not eyes to phone')", "Keep computer screens an arm's length away with the top of the monitor aligned with your eye line"],
        ["Never hunch over a laptop in bed with your spine bent like a folded taco", "Never read smartphones in a pitch-black bedroom without ambient room lighting"],
        "Slouching over your phone with your neck bent down for 6 hours a day causes no permanent physical spinal damage.", "myth", "'Text Neck' causes premature spinal disc degeneration, chronic headaches, pinched nerves, and permanent postural hunching.",
        "What does the famous ophthalmological '20-20-20 Rule' prescribe for screen users?",
        ["Spend 20 hours on screens, 20 minutes outside, 20 rupees on drops", "Every 20 minutes, look at an object 20 feet away for at least 20 seconds", "Blink 20 times every 20 hours", "Wear 20 pairs of spectacles"], 1,
        "Looking 20 feet away relaxes the eye's ciliary muscles, immediately preventing eye strain and fatigue.",
        ["After 3 hours of online study at {at}, {name} has a throbbing headache, dry burning eyes, and a stiff, painful neck."],
        "How should {name} adjust ergonomics immediately?",
        [("Apply the 20-20-20 rule: stand up, look out the window at distant trees, and blink deliberately", "Relaxes ciliary eye muscles and restores tear film.", True, "20-20-20 rule|look at distant trees|blink deliberately", 45),
         ("Elevate the screen on books so the top edge is at eye level and sit with back supported", "Eliminates forward cervical spinal strain.", True, "elevate screen to eye level|straight back|proper posture", 35),
         ("Ensure room has comfortable, balanced ambient lighting rather than a glare in pitch darkness", "Reduces harsh ocular contrast fatigue.", False, "ambient lighting|eliminate glare", 20)],
        ["rub eyes aggressively with dirty hands", "continue hunching closer to the screen", "take painkillers and ignore posture"],
        "All India Ophthalmological Society (AIOS) - Computer Vision Syndrome Advisory", "https://aios.org"
    ))

    return cards


def get_saathi_cards():
    cards = []

    # INC-001: Interacting with classmates with physical disabilities
    cards.append(make_card(
        "INC-001", "saathi", "Accessibility", "Respectful interaction: Classmates with physical disabilities",
        ["junior", "middle", "senior"],
        ["A wheelchair, crutch, or white cane is an extension of a person's personal body space; touching or pushing it without permission is a violation.",
         "Treat classmates with disabilities as complete equals: speak directly to them at eye level, not to their caregiver or companion."],
        ["Always ask 'Would you like some assistance?' and wait for their answer before grabbing or pushing a wheelchair", "Sit down on a chair when having a long conversation so you are at comfortable eye level with a wheelchair user", "Keep hallways, ramps, and classroom doorways completely clear of backpacks and desks"],
        ["NEVER lean on, grab, or push someone's wheelchair without their explicit consent", "NEVER talk down to someone with a physical disability as if they are a helpless toddler"],
        "If you see a classmate in a wheelchair, you should immediately grab the handles and push them without asking to be helpful.", "myth", "A wheelchair is personal bodily space. Grabbing it without asking is alarming and disrespectful. Always ask permission first.",
        "What is the polite and respectful protocol before assisting a classmate who uses mobility aids?",
        ["Grab their crutches and carry them", "Ask politely if they would like assistance, and respect their answer if they say 'No thanks, I've got this'", "Ignore them completely", "Push their wheelchair as fast as possible"], 1,
        "Dignity means respecting autonomy: always ask first, listen to their specific preference, and honor their independence.",
        ["At the school entrance ramp at {at}, {name} sees a classmate in a wheelchair preparing to navigate an incline."],
        "How should {name} offer support respectfully?",
        [("Walk up, make friendly eye contact, and ask: 'Hi, would you like a hand with the ramp today?'", "Offers assistance politely while respecting bodily autonomy.", True, "ask permission first|friendly eye contact|respect autonomy", 50),
         ("Wait for their response and follow their specific directions on how to hold or push the chair", "Follows user's explicit preference.", True, "wait for response|follow directions", 30),
         ("Ensure the ramp pathway is clear of discarded water bottles or student bags", "Proactively clears physical accessibility obstacles.", False, "clear pathway|remove obstacles", 20)],
        ["grab wheelchair handles from behind without speaking", "pat classmate on head like a child", "stare awkwardly and walk away"],
        "Department of Empowerment of Persons with Disabilities (DEPwD)", "https://disabilityaffairs.gov.in"
    ))

    # INC-002: Sign language basics & deaf communication
    cards.append(make_card(
        "INC-002", "saathi", "Deaf Culture", "Communicating with Deaf peers: Eye contact, light, and sign basics",
        ["junior", "middle", "senior"],
        ["Deaf and hard-of-hearing people communicate through rich visual languages; Indian Sign Language (ISL) is a complete, expressive linguistic system.",
         "When speaking with someone who lip-reads or signs, facial expressions, clear lighting, and facing them directly are essential."],
        ["Tap gently on their shoulder or wave your hand in their field of vision to get their attention politely", "Face the person directly in good lighting so your mouth and facial expressions are clearly visible", "Learn basic Indian Sign Language (ISL) signs for 'Hello', 'Thank you', 'Friend', and 'Help'"],
        ["Never cover your mouth with your hand or turn your back while speaking to someone who lip-reads", "Never shout loudly into the ear of a deaf person; shouting distorts lip shapes and does not help"],
        "Shouting at the top of your lungs into a deaf person's ear helps them understand what you are saying.", "myth", "Shouting distorts facial and lip movements and can cause painful acoustic feedback in hearing aids. Speak at normal volume facing them.",
        "What is the polite way to get the attention of a deaf or hard-of-hearing classmate in a noisy room?",
        ["Throwing a pencil at their head", "A gentle tap on the shoulder or a friendly wave within their visual field", "Screaming their name repeatedly", "Turning off the room lights violently"], 1,
        "Gentle visual or tactile cues respect dignity and establish natural communication without aggression.",
        ["During group project discussion in the classroom at {at}, a hard-of-hearing classmate is looking down while another student speaks quickly from across the table."],
        "How should {name} facilitate inclusive communication?",
        [("Gently wave a hand in their view to signal the discussion is starting and face them directly", "Ensures visual engagement and mutual presence.", True, "gentle wave|face them directly|good lighting", 45),
         ("Speak at a natural, steady pace with clear lip movement without exaggerated shouting", "Supports natural lip-reading without distortion.", True, "steady pace|clear lip movement|do not shout", 35),
         ("Write down key project decisions and bullet points in a shared notebook so nothing is missed", "Provides accessible visual notes.", False, "write down key points|shared notebook", 20)],
        ["exclude deaf peer from project", "shout directly into their ear", "talk behind their back"],
        "Indian Sign Language Research and Training Centre (ISLRTC)", "https://islrtc.nic.in"
    ))

    # INC-003: Respecting accents & dialects
    cards.append(make_card(
        "INC-003", "saathi", "Linguistic Diversity", "Accents and mother tongues: Linguistic diversity is India's strength",
        ["junior", "middle", "senior"],
        ["An accent simply means a person has the brilliance and courage to speak more than one language.",
         "India is home to over 19,500 spoken mother tongues and dialects; mocking someone's regional pronunciation is ignorant and deeply hurtful."],
        ["Appreciate that someone with an accent speaks their mother tongue PLUS another language", "Focus on the content and meaning of what a peer is saying, never mock their phonetics or rhythm", "If you do not understand a word, ask politely: 'Could you please repeat that last sentence?'"],
        ["Never imitate, mock, or exaggerate someone's regional accent for cheap laughs in class", "Never judge someone's intelligence or capability by their fluency in English"],
        "People who speak English with a heavy regional mother-tongue accent are less intelligent and uneducated.", "myth", "Accent has zero correlation with intelligence. Many world-renowned scientists and thinkers speak English as their third or fourth language.",
        "What does having an accent when speaking English or Hindi genuinely signify?",
        ["That the person has poor memory", "That the person is multilingual and mastered another rich mother tongue first", "That they need medical treatment", "That they cannot learn"], 1,
        "Accents are the melodic footprint of a person's multilingual heritage and cognitive breadth.",
        ["A new student from a different state speaks English with a regional inflection at {at}, and two classmates giggle and mock the pronunciation."],
        "How should {name} respond?",
        [("Step in and say: 'His point was really interesting, let's listen to what he is actually saying'", "Redirects attention to substantive ideas and halts mockery.", True, "listen to his point|halt mockery|stand up for peer", 50),
         ("Engage the new student in conversation warmly, asking about their background and experiences", "Builds welcoming interpersonal bridge.", True, "engage warmly|ask about background|inclusive friendship", 30),
         ("Remind peers privately that India's diverse mother tongues are a shared cultural treasure", "Educates peers on linguistic respect.", False, "remind peers of linguistic diversity|cultural respect", 20)],
        ["join in mocking the accent", "laugh along to avoid being targeted", "tell new student to stop talking"],
        "National Education Policy (NEP) - Multilingualism and Cultural Harmony", "https://education.gov.in"
    ))

    # INC-004: Welcoming new students
    cards.append(make_card(
        "INC-004", "saathi", "Hospitality", "The buddy system: Making sure no newcomer sits alone",
        ["junior", "middle", "senior"],
        ["Entering a new school where everyone already has established friend groups is one of the most intimidating experiences in childhood.",
         "A single welcoming gesture—inviting a new peer to sit at your lunch table—can permanently change their school trajectory."],
        ["Take initiative: Walk over, introduce yourself, and say 'Hi, welcome to our class, I'm {name}'", "Invite them to sit with you during lunch and guide them to science labs and water coolers", "Introduce the new student to your other friends so their social circle broadens naturally"],
        ["Never stare at new students without saying hello or leave them wandering lost in corridors", "Never treat new classmates as rivals or invaders in your established social circles"],
        "New students prefer being left completely alone in the corner for their first two months to adjust quietly.", "myth", "Newcomers feel deep anxiety and isolation. A warm, friendly welcome immediately dispels fear and builds belonging.",
        "What is the simplest and most powerful way to make a new classmate feel welcome on day one?",
        ["Stare at their shoes silently", "Invite them to sit at your lunch table and show them where the library and labs are", "Ask them why they left their old school", "Ignore them completely"], 1,
        "Sharing lunch and guiding them through physical school logistics creates immediate safety and comfort.",
        ["On Monday morning at {at}, a new student stands alone against the corridor wall clutching their books, looking anxious as crowds rush past."],
        "How should {name} act as an inclusive peer?",
        [("Walk up warmly, introduce yourself, and offer to show them to the homeroom classroom", "Takes proactive welcoming initiative.", True, "walk up warmly|introduce self|show homeroom", 45),
         ("Invite them to sit together during recess and introduce them to two other friendly classmates", "Integrates newcomer into peer community.", True, "invite to recess lunch|introduce to friends", 35),
         ("Answer their questions about teachers, timetables, and locker locations with patience", "Provides helpful practical orientation.", False, "answer timetable questions|practical orientation", 20)],
        ["walk past without looking", "whisper with friends about their appearance", "prank the new student"],
        "CBSE Adolescent Peer Educator Program", "https://cbse.gov.in"
    ))

    # INC-005: Dismantling gender stereotypes
    cards.append(make_card(
        "INC-005", "saathi", "Gender Equality", "Beyond stereotypes: Human potential has no gender",
        ["junior", "middle", "senior"],
        ["Gender stereotypes restrict human potential: boys are pressured to suppress tears, while girls are discouraged from sports, coding, or leadership.",
         "True equality recognizes that strength, sensitivity, scientific curiosity, empathy, and courage belong equally to all human beings."],
        ["Encourage girls in robotics, mathematics, cricket, and public debate leadership", "Support boys in expressing emotions, cooking, artistic dance, and caregiving without mocking them", "Divide classroom duties (cleaning, carrying chairs, technology setup) equally without gender segregation"],
        ["Never say 'You throw like a girl' or 'Boys don't cry'—both phrases enforce harmful myths", "Never assume certain school subjects or careers belong exclusively to one gender"],
        "Boys are biologically wired to be good at math and coding, while girls are biologically wired only for languages and art.", "myth", "Cognitive research shows zero innate difference in mathematical or scientific capability between boys and girls. Differences stem from social conditioning.",
        "Why is telling a crying boy that 'Boys don't cry' psychologically harmful?",
        ["Because boys have more tears than girls", "Because it teaches boys to bottle up normal human emotions, leading to emotional numbness and aggression", "Because it makes them laugh", "Because boys have no tear ducts"], 1,
        "Suppressing emotions harms mental health. Emotional expression is a human trait, not a gender weakness.",
        ["In the science lab at {at}, a male student laughs when a female classmate volunteers to be team captain for the robotics rover build."],
        "How should {name} promote gender inclusion?",
        [("Affirm the female classmate's leadership role and support her captaincy based on competence", "Champions merit-based leadership over bias.", True, "support her captaincy|merit over bias|stand against stereotype", 50),
         ("Point out that engineering and leadership belong to whoever has the passion and skill, regardless of gender", "Challenges restrictive gender assumptions.", True, "engineering for everyone|passion and skill", 30),
         ("Collaborate enthusiastically as a team player under her project direction", "Models equitable, respectful teamwork.", False, "collaborate under her direction|respectful teamwork", 20)],
        ["tell female student to do paperwork instead", "agree that girls cant build robots", "boycott the project"],
        "Ministry of Women and Child Development - Beti Bachao Beti Padhao", "https://wcd.nic.in"
    ))

    # INC-006: Standing up against body shaming
    cards.append(make_card(
        "INC-006", "saathi", "Upstander", "Crushing body shaming: Defending peers against appearance bullying",
        ["junior", "middle", "senior"],
        ["Body shaming targets weight, height, skin complexion, hair texture, or facial features, causing severe lifelong depression and eating disorders.",
         "Cruel comments disguised as 'just a joke' are bullying; staying silent makes bystanders complicit in the harm."],
        ["Call out body shaming in the moment: 'That's not funny, let's not make comments about people's bodies'", "Check in privately with the targeted person: 'Hey, what they said was awful, I don't agree with it at all'", "Compliment peers on their character, wit, kindness, and effort rather than their physical measurements"],
        ["Never join in laughter when someone is mocked for their weight, skin color, or height", "Never give unsolicited advice on dieting, skin lightening, or gym routines to peers"],
        "Making fun of a classmate's weight or dark skin is harmless banter as long as everyone laughs.", "myth", "Body shaming inflicts deep emotional trauma and triggers self-loathing and eating disorders. Cruelty is never banter.",
        "What is the most effective way for a bystander to stop appearance-based teasing in a group conversation?",
        ["Laugh along so you don't get teased next", "Look at the person teasing and say calmly: 'We don't do body comments here, let's talk about something else'", "Film the teasing and post it on social media", "Start teasing the teaser's physical body"], 1,
        "Clear, calm social boundaries set by peers extinguish bullying far faster than passive silence.",
        ["In the school courtyard at {at}, a group of students loudly teases a classmate about their weight and height, calling them cruel nicknames."],
        "How should {name} act as an upstander?",
        [("Speak up clearly to the group: 'Leave them alone, commenting on people's bodies is completely uncool'", "Interrupts bullying behavior directly with moral courage.", True, "speak up clearly|leave them alone|body shaming uncool", 50),
         ("Stand beside the targeted classmate and guide them away from the teasing circle", "Provides physical solidarity and safe exit.", True, "stand beside classmate|guide away from circle", 30),
         ("Spend the rest of lunch hanging out with them and reporting the bullying to a teacher if it repeats", "Follows up with genuine friendship and institutional safety.", False, "hang out as friends|report persistent bullying", 20)],
        ["join the laughter to fit in", "film the bullying on your phone", "tell the victim they should diet"],
        "National Commission for Protection of Child Rights (NCPCR) - Anti-Bullying Guidelines", "https://ncpcr.gov.in"
    ))

    # INC-007: Respecting elders and domestic workers
    cards.append(make_card(
        "INC-007", "saathi", "Human Dignity", "Every job has dignity: Respecting sanitation and domestic workers",
        ["junior", "middle", "senior"],
        ["A society is judged by how it treats the people who keep it clean, fed, and running: domestic helpers, sweepers, drivers, and security guards.",
         "Dignity of labor is a foundational democratic value; ordering workers around with disrespect reflects poorly on your character, not theirs."],
        ["Always address service workers, security guards, and domestic staff with polite honorifics (Bhaiya, Didi, Uncle, Aunty)", "Say 'Thank you' and 'Please' when staff hand you clean water, sweep your classroom, or open gates", "Clean up your own spills, return your own cafeteria trays, and never leave humiliating messes for staff"],
        ["Never talk down to domestic helpers or speak to them in commanding, rude tones", "Never litter on school grounds with the arrogant thought: 'The sweeper is paid to clean this'"],
        "Because domestic workers and sweepers are paid wages, you do not need to show them basic politeness or say thank you.", "myth", "Wages pay for labor, not for subservience. Dignity, kindness, and courtesy are fundamental human rights due to every worker.",
        "What does leaving your trash scattered on a classroom floor because 'sweepers will clean it' demonstrate?",
        ["High personal wealth", "A total lack of civic responsibility and disrespect for human labor", "Superior education", "Good efficiency"], 1,
        "Respecting dignity of labor means minimizing other people's toil through personal accountability.",
        ["In the school cafeteria at {at}, {name} sees a student deliberately spill curry on the floor, laugh, and shout at the cleaning staff: 'Come clean this quickly!'"],
        "How should {name} respond with civic dignity?",
        [("Pick up napkins and help wipe up the spill, apologizing to the cleaning staff member for the classmate's rudeness", "Demonstrates humility and dignity of labor through action.", True, "help wipe up spill|apologize to staff|dignity of labor", 50),
         ("Address the rude student firmly: 'Staff members are not your personal servants, treat people with respect'", "Asserts civic and human boundaries against arrogance.", True, "staff not servants|treat with respect|confront arrogance", 30),
         ("Thank the cleaning staff member warmly for keeping the cafeteria clean and healthy for all students", "Affirms human dignity and gratitude.", False, "thank cleaning staff warmly|affirm dignity", 20)],
        ["laugh along with the rude student", "kick curry further across floor", "order staff to hurry up"],
        "Ministry of Labour and Employment - Dignity of Labour Principles", "https://labour.gov.in"
    ))

    # INC-008: Overcoming language barriers in school
    cards.append(make_card(
        "INC-008", "saathi", "Empathy", "Bridging language gaps: Patience with peers learning a new tongue",
        ["junior", "middle", "senior"],
        ["Students moving across states often struggle to express complex thoughts in Hindi or English while their intellect remains razor-sharp.",
         "Mocking broken grammar or laughing at hesitations silences intelligent peers and creates deep academic trauma."],
        ["Give peers full, patient time to finish their sentences without interrupting or finishing their words", "Use simple vocabulary, gestures, or visual diagrams when explaining concepts across language differences", "Encourage and praise their courage in communicating in a second or third language"],
        ["Never laugh at grammatical mistakes or unusual word choices made by non-native speakers", "Never roll your eyes or sigh loudly while someone is searching for a word in class"],
        "If a student struggles to speak English fluently in science class, it means they are incapable of understanding science.", "myth", "Language is merely a tool for communication, not a measure of intelligence. Deep scientific concepts exist independently of English fluency.",
        "How should you act when a classmate from another state hesitates while searching for words in English or Hindi?",
        ["Finish their sentence aggressively for them", "Listen patiently with encouraging body language and give them time to express their thought", "Tell them to sit down", "Laugh at their grammar"], 1,
        "Patience and warm non-verbal encouragement create psychological safety for language learners.",
        ["During an environmental science seminar at {at}, a student who recently relocated from a rural district struggles to find English words to explain solar irrigation."],
        "How should {name} support the presenter?",
        [("Listen with attentive, encouraging eye contact, allowing them the time needed to articulate their ideas", "Creates a supportive, patient audience environment.", True, "listen attentively|encouraging eye contact|patient listening", 45),
         ("Supportively suggest a technical word if they look to the room for help, without taking over the presentation", "Offers gentle, collaborative assistance.", True, "suggest word gently|collaborative support|do not take over", 35),
         ("Applaud enthusiastically for the quality of the solar irrigation concept once the presentation concludes", "Celebrates substantive scientific ideas over linguistic polish.", False, "applaud concept quality|celebrate ideas", 20)],
        ["giggle at grammatical stumbles", "tell teacher to disqualify the speaker", "mimic their pronunciation"],
        "NCERT - Inclusive Education in Indian Classrooms", "https://ncert.nic.in"
    ))

    # INC-009: Wheelchair & accessibility awareness
    cards.append(make_card(
        "INC-009", "saathi", "Universal Design", "Accessibility for all: Keeping ramps, corridors, and doors open",
        ["junior", "middle", "senior"],
        ["Universal design and accessibility are human rights: ramps, wide doors, elevators, and tactile paving allow all citizens full participation.",
         "Parking bicycles in front of ramps, cluttering corridors, or misusing accessible restrooms creates insurmountable barriers for disabled peers."],
        ["Never park bicycles, scooters, or sports gear across wheelchair ramps or curb cuts", "Hold heavy doors open when you see someone using crutches, a wheelchair, or carrying heavy boxes", "Keep accessible restroom stalls available for individuals who genuinely require their grab rails and turning radius"],
        ["Never use accessible wheelchair ramps as skate ramps or obstacle courses", "Never crowd elevator doors when a student with mobility aids is trying to enter"],
        "Accessible ramps are just decorative architectural features that school skate clubs can use for stunts.", "myth", "Ramps and tactile paving are vital lifelines that ensure citizens with disabilities can access education, transit, and healthcare.",
        "Why is it critical to keep yellow tactile paving stones on sidewalks and railway stations completely clear of obstacles?",
        ["Because they look nice when clean", "Because visually impaired citizens rely on tactile bumps to navigate safely with white canes", "Because they are made of gold", "Because trains park on them"], 1,
        "Tactile paving guides visually impaired pedestrians away from hazards; blocking them causes painful collisions.",
        ["Outside the school auditorium at {at}, students leave ten bicycles leaning directly against the wheelchair access ramp."],
        "How should {name} demonstrate civic accessibility awareness?",
        [("Help move the bicycles safely away from the ramp into the designated cycle parking zone", "Removes physical barrier to ensure universal access.", True, "move bicycles away|clear access ramp|designated parking", 50),
         ("Remind classmates politely that blocking ramps prevents peers in wheelchairs from entering the auditorium", "Educates peers on disability rights and physical access.", True, "educate classmates|blocking ramps prevents access", 30),
         ("Suggest to school administration that clear 'Keep Ramp Clear' signage be painted on the ground", "Proposes long-term infrastructural solution.", False, "suggest keep ramp clear signs|infrastructural fix", 20)],
        ["leave bikes blocking ramp", "add your own bike to the pile", "mock disabled peers for complaining"],
        "Accessible India Campaign (Sugamya Bharat Abhiyan)", "https://accessibleindia.gov.in"
    ))

    # INC-010: Understanding invisible disabilities & neurodiversity
    cards.append(make_card(
        "INC-010", "saathi", "Neurodiversity", "Invisible disabilities: ADHD, Autism, and Dyslexia explained",
        ["middle", "senior"],
        ["Many disabilities are invisible: ADHD, autism, dyslexia, epilepsy, chronic pain, and diabetes do not involve wheelchairs or white canes.",
         "Neurodiversity recognizes that human brains are wired differently; what looks like 'laziness' or 'acting weird' is often a neurological difference."],
        ["Never assume someone is faking difficulty just because 'they look completely normal'", "Be patient if a neurodivergent peer needs instructions written down or avoids noisy, chaotic environments", "Celebrate diverse cognitive strengths: dyslexic thinkers often excel in spatial reasoning, while autistic peers excel in deep focus"],
        ["Never mock a classmate who flaps their hands, rocks, or wears noise-canceling headphones to self-soothe", "Never use diagnostic terms like 'Autistic' or 'ADHD' as casual playground insults"],
        "If someone can walk and talk normally, it is impossible for them to have a genuine disability.", "myth", "Over 80% of disabilities are invisible, including learning differences, autoimmune conditions, and sensory processing disorders.",
        "What does the term 'Neurodiversity' mean?",
        ["A disease that needs to be cured with pills", "The understanding that brain differences (like autism and ADHD) are natural variations of the human genome, not personal defects", "A computer programming language", "A school for doctors"], 1,
        "Neurodiversity views brain differences through the lens of human diversity and strength rather than deficit.",
        ["In class at {at}, an autistic student rocks gently in their chair and wears ear-defenders during loud group activities, prompting whispers from peers."],
        "How should {name} foster an inclusive environment?",
        [("Treat the classmate with warm, respectful normality and normalize sensory regulation tools", "Normalizes neurodivergent accommodations.", True, "treat with respect|normalize ear defenders|sensory regulation", 45),
         ("Gently explain to curious peers that loud noise can cause sensory overload and ear defenders help them focus", "Spreads accurate neurodiversity awareness.", True, "explain sensory overload|educate peers|dispel whispers", 35),
         ("Include the classmate in project discussions by communicating clearly without chaotic shouting", "Adapts group work for inclusive participation.", False, "clear communication|inclusive group work", 20)],
        ["mock the classmate's rocking", "pull off their ear defenders", "demand they act normal"],
        "National Trust for the Welfare of Persons with Autism, Cerebral Palsy, Mental Retardation and Multiple Disabilities", "https://thenationaltrust.gov.in"
    ))

    # INC-011: The lasting harm of derogatory nicknames
    cards.append(make_card(
        "INC-011", "saathi", "Verbal Respect", "Names and dignity: The deep sting of derogatory nicknames",
        ["junior", "middle", "senior"],
        ["Calling someone by a cruel nickname based on their weight, skin shade, caste, region, or disability is verbal violence that erodes self-esteem.",
         "Even if the person smiles or laughs along awkwardly, inside they often feel humiliated, diminished, and deeply unsafe."],
        ["Always address peers by their real, preferred name or an affectionate nickname they genuinely love", "If someone says 'Please don't call me that', stop immediately and permanently—no debate, no excuses", "Notice nervous laughter: victims often smile to avoid escalating conflict, not because they find the nickname funny"],
        ["Never use nicknames that reference someone's body size, glasses, dental braces, or skin tone", "Never justify cruelty with 'It's just an affectionate nickname bro'"],
        "If a classmate smiles when you call them a cruel nickname about their weight, it proves they genuinely enjoy it.", "myth", "Smiling is a common appeasement response to survive social humiliation. Forcing cruel labels damages human dignity.",
        "What should you do if you realize a nickname you frequently use makes a classmate feel uncomfortable or sad?",
        ["Tell them they are too sensitive and keep using it", "Apologize sincerely, stop using the nickname immediately, and address them by their chosen name", "Use it even louder in front of teachers", "Make up a worse nickname"], 1,
        "True maturity means respecting other people's dignity and dropping hurtful labels instantly.",
        ["In the playground at {at}, several boys repeatedly call a classmate 'Chashmish' and 'Mota', while the classmate looks down with a forced, uncomfortable smile."],
        "How should {name} intervene constructively?",
        [("Ask the classmate privately what they actually prefer to be called and start using their real name consistently", "Validates their true personal identity and dignity.", True, "ask preferred name|use real name consistently|restore dignity", 45),
         ("Tell the group firmly: 'Hey guys, call him by his actual name, let's drop the nicknames'", "Sets a clear, respectful peer standard.", True, "call him by real name|drop nicknames|firm boundary", 35),
         ("Never join in repeating the derogatory label", "Refuses to amplify verbal bullying.", False, "refuse to repeat nickname|lead by example", 20)],
        ["call him worse names", "tell him to get thicker skin", "laugh along with the bullies"],
        "CBSE Guidelines on Prevention of Bullying in Schools", "https://cbse.gov.in"
    ))

    # INC-012: Dignified sharing & lunchbox etiquette
    cards.append(make_card(
        "INC-012", "saathi", "Cultural Harmony", "Lunchbox diplomacy: Respecting diverse dietary traditions and foods",
        ["junior", "middle", "senior"],
        ["Food is an intimate expression of culture, family heritage, regional agriculture, and religious traditions.",
         "Making disgusted faces or saying 'Eww, what stinks?' at someone's traditional home-cooked lunch causes deep cultural shame and alienation."],
        ["Approach unfamiliar lunch dishes with curiosity rather than disgust: 'That smells aromatic, what dish is that?'", "Respect diverse dietary boundaries (vegetarian, Jain, halal, egg-free, allergies) without mocking or tampering with food", "Practice hygienic sharing: offer food politely without touching someone else's lunchbox with unwashed fingers"],
        ["Never say 'Eww gross!' to someone eating their family's traditional home-cooked meal", "Never trick a vegetarian or religious peer into eating meat, eggs, or ingredients they abstain from"],
        "Tricking a strict vegetarian friend into eating chicken nuggets by lying about the ingredients is a hilarious, harmless prank.", "myth", "Deceiving someone about what they eat violates their bodily autonomy, religious beliefs, and can trigger severe allergic reactions.",
        "What is the most respectful attitude toward a classmate's unfamiliar regional lunchbox dish?",
        ["Screaming that it smells disgusting and running away", "Asking with genuine polite curiosity about what ingredients and spices were used in the dish", "Throwing it in the trash", "Forcing them to eat your food instead"], 1,
        "Culinary curiosity celebrates cultural diversity and turns meal breaks into opportunities for shared friendship.",
        ["At the lunch table at {at}, a student opens a tiffin box with fermented regional bamboo shoots and fish, and classmates make gagging noises."],
        "How should {name} model inclusive lunchbox diplomacy?",
        [("Shut down the mockery and ask the classmate with curiosity: 'What is this regional specialty called?'", "Models cultural openness and halts humiliation.", True, "shut down mockery|ask with curiosity|cultural openness", 50),
         ("Explain to peers that every culture has unique fermented, pickled, or spiced foods that taste delicious", "Broadens cultural understanding through reason.", True, "explain diverse food traditions|educate peers", 30),
         ("Ensure the lunch table remains a warm, welcoming space where all food traditions are honored", "Preserves collective harmony and belonging.", False, "warm welcoming lunch table|honor all traditions", 20)],
        ["yell that the food is stinky", "demand they move to another table", "spit on the tiffin box"],
        "Ek Bharat Shreshtha Bharat - Cultural Understanding Initiatives", "https://ekbharat.gov.in"
    ))

    # INC-013: Respecting diverse regional festivals
    cards.append(make_card(
        "INC-013", "saathi", "Interfaith Harmony", "Celebrating India's mosaic: Embracing diverse festivals with joy",
        ["junior", "middle", "senior"],
        ["India's cultural genius lies in its pluralism: Diwali, Eid, Christmas, Gurpurab, Onam, Pongal, Bihu, and Chhath Puja reflect shared humanity.",
         "Participating in or wishing peers joy during their festivals strengthens community fabric and builds broad-minded global citizens."],
        ["Wish your classmates joy on their cultural and religious festivals (e.g., 'Eid Mubarak', 'Happy Gurpurab', 'Merry Christmas')", "Learn the meaning and history behind regional festivals: harvest gratitude, victory of truth over darkness, or universal charity", "Share festive sweets (mithai, sewaiyan, plum cake, payasam) with warmth and mutual affection"],
        ["Never insult or belittle another community's sacred rituals, prayer customs, or traditional attire", "Never divide school friendship circles along religious, caste, or regional fault lines"],
        "You are only allowed to learn about or celebrate the specific festivals practiced by your own immediate family.", "myth", "India's greatest strength is composite culture. Sharing the joy of our neighbors' festivals enriches our own understanding of humanity.",
        "What shared universal theme unites diverse Indian harvest and light festivals across all regions?",
        ["Competition over who buys the most plastic", "Gratitude to nature, the triumph of light and justice, and sharing prosperity with community", "Staying angry at neighbors", "Refusing to share sweets"], 1,
        "Across every state and faith, Indian festivals celebrate ecological gratitude, light over darkness, and shared community generosity.",
        ["In the school courtyard at {at}, students from diverse backgrounds are talking about upcoming festive holidays (Diwali, Eid, and Christmas)."],
        "How can {name} celebrate this cultural mosaic?",
        [("Ask friends about their favorite family customs, recipes, and childhood memories during their holidays", "Deepens mutual respect through genuine personal storytelling.", True, "ask about family customs|recipes|shared storytelling", 45),
         ("Wish classmates warm greetings on their festive days and share traditional festive treats happily", "Fosters inclusive community celebration.", True, "warm greetings|share festive treats|celebrate together", 35),
         ("Appreciate how India's multi-faith heritage makes our classrooms vibrant, colorful, and resilient", "Values pluralism and national harmony.", False, "appreciate multi-faith heritage|national harmony", 20)],
        ["mock religious traditions you dont practice", "refuse to eat sweets from other communities", "argue over which festival is superior"],
        "Ministry of Culture - Composite Culture of India", "https://indiaculture.gov.in"
    ))

    # INC-014: Practicing active empathetic listening
    cards.append(make_card(
        "INC-014", "saathi", "Active Listening", "The gift of presence: Listening with your whole heart",
        ["junior", "middle", "senior"],
        ["Most people do not listen to understand; they listen only to reply, interrupt, or offer unsolicited advice.",
         "Active empathetic listening means giving your complete attention, withholding judgment, and letting the other person feel truly heard."],
        ["Put away your smartphone, lean slightly forward, and maintain warm eye contact when someone is confiding in you", "Summarize what you hear: 'It sounds like you felt really betrayed when that happened, is that right?'", "Avoid jumping in with immediate advice unless they explicitly ask: 'What do you think I should do?'"],
        ["Never interrupt someone in the middle of their sentence to talk about your own life experiences", "Never dismiss someone's feelings with 'Oh that's nothing, listen to what happened to me!'"],
        "Being a great listener means immediately interrupting with a 10-step plan to solve all their problems.", "myth", "People in emotional distress need connection and understanding first, not a lecture. Listening without fixing is the deepest gift.",
        "Which conversational response shows authentic empathetic listening?",
        ["'That's completely your fault'", "'That sounds really overwhelming; I'm so glad you shared that with me, I'm here for you'", "'Whatever, can I tell you my story now?'", "'You should just stop being sad'"], 1,
        "Validating feelings and offering presence without judgment creates emotional safety and deep trust.",
        ["Sitting under a tree at {at}, a classmate starts opening up about feeling overwhelmed by family financial stress."],
        "How should {name} practice active listening?",
        [("Put away your phone completely, make gentle eye contact, and listen without interrupting", "Provides undivided, respectful attention.", True, "put phone away|gentle eye contact|do not interrupt", 45),
         ("Reflect back their feelings with empathy: 'That must feel really heavy to carry, I'm right here with you'", "Validates emotional experience without judgment.", True, "validate feelings|that sounds heavy|right here with you", 35),
         ("Resist the urge to turn the conversation back onto your own life or offer unasked-for financial advice", "Keeps the spotlight on the person in need.", False, "do not make it about yourself|hold space", 20)],
        ["scroll Instagram while they talk", "interrupt to talk about your pocket money", "tell them to just be positive"],
        "NCERT - Life Skills Education and Communication", "https://ncert.nic.in"
    ))

    # INC-015: Practicing forgiveness & resolving peer conflicts
    cards.append(make_card(
        "INC-015", "saathi", "Conflict Resolution", "Releasing grudges: The liberating strength of forgiveness",
        ["junior", "middle", "senior"],
        ["Holding onto a bitter grudge is like drinking poison and expecting the other person to suffer.",
         "Forgiveness does not mean accepting ongoing abuse or pretending bad behavior is okay; it means releasing toxic hatred so you can heal."],
        ["Distinguish forgiveness from weakness: letting go of rage requires immense inner strength and emotional maturity", "Focus on resolving conflicts using 'I-messages': 'I felt hurt when you broke your promise, can we talk about it?'", "Set healthy boundaries: you can forgive someone while deciding not to be their close partner until trust is rebuilt"],
        ["Never nurse silent revenge fantasies that keep you locked in bitterness and stress", "Never use social exile or group ostracization as a weapon against a classmate who made a mistake"],
        "Forgiving a classmate who hurt you means you must let them treat you like a doormat forever.", "myth", "Forgiveness frees your heart from toxic bitterness; boundaries determine how close that person is allowed to get in the future.",
        "What is the healthiest reason to forgive someone who apologized for hurting you?",
        ["Because you want them to owe you money", "To liberate your own mind from toxic bitterness, reduce stress, and restore personal peace", "Because teachers forced you to shake hands", "So you can plot revenge later"], 1,
        "Forgiveness is an act of self-care that frees your emotional energy from the grip of past hurt.",
        ["Following a bitter disagreement over a science fair presentation at {at}, a teammate apologizes sincerely for snapping in anger."],
        "How should {name} navigate this conflict resolution?",
        [("Accept the apology gracefully, acknowledging that everyone makes mistakes under pressure", "Practices restorative forgiveness and empathy.", True, "accept apology gracefully|acknowledge stress|forgive mistake", 45),
         ("Share calmly how the outburst felt so mutual understanding is established before moving forward", "Communicates honest emotional impact constructively.", True, "communicate impact calmly|clear the air", 35),
         ("Rebuild the collaborative relationship with clear, fair ground rules for future team meetings", "Establishes healthy future working boundaries.", False, "clear ground rules|rebuild partnership", 20)],
        ["hold a grudge for the rest of the year", "tell everyone in school never to talk to that peer", "demand revenge"],
        "Gandhi Smriti and Darshan Samiti - Non-Violent Communication", "https://gandhismriti.gov.in"
    ))

    # INC-016: Mixed-ability team projects
    cards.append(make_card(
        "INC-016", "saathi", "Collaboration", "Inclusive teamwork: Thriving together in mixed-ability groups",
        ["middle", "senior"],
        ["Classrooms bring together diverse strengths: some peers excel in writing, others in visual sketching, math, or oral presentation.",
         "Inclusive teams do not dump all the work on the highest-scoring student; they structure tasks so every member contributes with pride."],
        ["Map team roles to individual talents: visual charts, speech delivery, factual research, and physical building", "Support peers who struggle with specific academic tasks by breaking steps into manageable chunks", "Celebrate the collective victory of the entire team rather than claiming individual dominance"],
        ["Never sideline or exclude a team member who has learning differences or lower exam marks", "Never do all the project work in secret and hand in the project without involving your teammates"],
        "The fastest and best way to complete a group project is for the top student to do 100% of the work while everyone else watches.", "myth", "Group projects teach real-world collaborative leadership, delegation, and mutual empowerment—not solo heroism.",
        "What is the primary responsibility of a student team captain in a mixed-ability group project?",
        ["To scream at everyone until they obey", "To identify each teammate's unique strength and empower everyone to make a meaningful contribution", "To do the entire project alone overnight", "To take all the stage credit"], 1,
        "True leadership unlocks the potential of every team member, ensuring everyone learns and contributes.",
        ["For an inter-house social studies exhibition at {at}, {name}'s team includes a peer with dyslexia and a peer who speaks limited English."],
        "How should {name} structure the project for inclusive success?",
        [("Structure roles around non-textual strengths: 3D model building, interview recordings, and visual map illustrations", "Leverages diverse strengths creatively.", True, "structure around non-textual strengths|3d model|visual illustrations", 50),
         ("Collaborate on speech practice patiently, creating supportive cue cards with bullet points", "Provides accessible communication scaffolding.", True, "speech practice|accessible cue cards|patient support", 30),
         ("Ensure every team member presents a meaningful section of the display during teacher evaluation", "Guarantees shared dignity and stage presence.", False, "shared presentation|meaningful section for all", 20)],
        ["kick both teammates off the squad", "hide their names from the report", "complain to teacher that team is weak"],
        "NCERT Guidelines on Inclusive Pedagogical Practices", "https://ncert.nic.in"
    ))

    # INC-017: Community volunteering & service
    cards.append(make_card(
        "INC-017", "saathi", "Civic Service", "Seva and volunteering: Humility in community action",
        ["junior", "middle", "senior"],
        ["Volunteering at animal shelters, elder care homes, or community soup kitchens connects us to the larger human family.",
         "True service (Seva) is performed with humility and respect, never as a self-aggrandizing photo-op for social media likes."],
        ["Approach community service with a posture of learning and listening rather than acting like a wealthy savior", "Focus on the real needs of the community: cleaning, serving food, reading books to elders, or sorting relief materials", "Keep mobile phones in your pocket; never take exploitative selfies with vulnerable children or elders"],
        ["Never treat volunteering purely as an empty resume-polishing exercise without genuine compassion", "Never look down on the communities you are serving with pity or condescension"],
        "Taking photos of yourself handing bananas to impoverished children and posting them on Instagram is the definition of true charity.", "myth", "Exploitative 'poverty tourism' robs vulnerable people of their human dignity. Authentic service is done with quiet humility and respect.",
        "What is the traditional Indian concept of 'Seva' (selfless service)?",
        ["Hiring people to clean your room", "Serving the community selflessly with humility, without expecting personal fame, wealth, or social media applause", "Running for political office", "Giving away expired canned food"], 1,
        "Authentic Seva dissolves human ego and builds deep solidarity with all living beings.",
        ["During a weekend volunteer drive at {at}, {name}'s group helps serve meals at a community night shelter. A peer pulls out a phone to film shelter residents eating."],
        "How should {name} guide the ethical standard of the team?",
        [("Politely ask the teammate to put the phone away, explaining that people in shelters deserve dignity and privacy", "Protects human dignity and opposes exploitative media.", True, "put phone away|protect privacy|human dignity", 50),
         ("Remind the team that true community service focuses on compassionate action rather than social media clout", "Reframes volunteering around authentic values.", True, "focus on service not clout|humble service", 30),
         ("Serve food with warm smiles, eye contact, and genuine humility", "Embodies authentic Seva.", False, "serve with warmth and humility|respectful presence", 20)],
        ["pose for selfies with residents while holding food", "post photos online with pitying captions", "refuse to serve food"],
        "National Service Scheme (NSS) - Ministry of Youth Affairs and Sports", "https://nss.gov.in"
    ))

    # INC-018: Being an upstander against identity-based bullying
    cards.append(make_card(
        "INC-018", "saathi", "Upstander", "The power of the upstander: Standing united against prejudice",
        ["junior", "middle", "senior"],
        ["Prejudice and discrimination thrive when good people stand by silently and do nothing.",
         "An 'Upstander' is someone who recognizes injustice, speaks up safely, supports the victim, and refuses to let hatred become normal."],
        ["Use the 4 Ds of intervention: Direct (speak up), Distract (interrupt with a question), Delegate (get help), Delay (support victim after)", "Stand physically beside the targeted peer so they know they are not alone against the crowd", "Report hate speech, casteist slurs, and religious discrimination to school leaders and parents immediately"],
        ["Never be a silent bystander whose silence gives permission to bigots and bullies", "Never put your own physical life in extreme danger; use distraction or get adult intervention when violence threatens"],
        "If you see a classmate being targeted with hate slurs, staying silent is the best way to remain neutral and fair.", "myth", "Silence always helps the oppressor, never the victim. Staying neutral in situations of injustice means siding with the bully.",
        "Which of the following describes an effective 'Distraction' tactic to interrupt bullying without physical confrontation?",
        ["Joining in the insults", "Walking up to the targeted peer and asking: 'Hey, our science teacher is looking for you in Lab 2, can you come now?'", "Throwing rocks at the bullies", "Laughing loudly"], 1,
        "Distraction interrupts the harassment dynamic cleanly, giving the victim a safe exit without escalating violence.",
        ["In the school bus at {at}, older students corner a younger student from a minority community, hurling discriminatory slurs and threats."],
        "How should {name} act as an upstander?",
        [("Use the Delegate strategy: alert the bus conductor and driver immediately that bullying is happening", "Delegates intervention to authority figures for immediate safety.", True, "alert bus driver and conductor|delegate intervention|immediate safety", 45),
         ("Walk over, sit beside the younger student, and say: 'Hey, sit with me up front, you are safe here'", "Provides immediate physical solidarity and protective presence.", True, "sit beside student|you are safe here|protective solidarity", 35),
         ("Report the specific discriminatory incident to school administration the following morning", "Holds perpetrators accountable through official channels.", False, "report to school administration|hold accountable", 20)],
        ["join in chanting hate slurs", "look down at phone pretending not to notice", "encourage the bullies"],
        "NCPCR - Framework on Eliminating Discrimination in Educational Institutions", "https://ncpcr.gov.in"
    ))

    return cards
