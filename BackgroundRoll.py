from random import randint

"""Personality/IDEALS/BOND/FLAW ROLL OPTIONS"""

player_trait =[]
player_ideal =[]
player_bond =[]
player_flaw = []


#############################################################################################################################################################
acolyte_trait = {
1 : "I idolize a particular hero of my faith, and constantlyrefer to that person\'s deeds and example.",
2 : "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
3 : "I see omens in every event and action. The gods try to speak to us, we just need to listen",
4 : "Nothing can shake my optimistic attitude.",
5 : "I quote (or misquote) sacred texts and proverbs in almost every situation",
6 : "I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.",
7 : "I\'ve enjoyed fine food, drink, and high society among my temple\'s elite. Rough living grates on me.",
8 : "I\'ve spent so long in the temple that I have little practical experience dealing with people in the outside world"
}
acolyte_ideal = {
1 : "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)",
2 : "Charity. I always try to help those in need, no matter what the personal cost. (Good)",
3 : "Change. We must help bring about the changes the gods are constantly working in the world. (Chaotic",
4 : "Power. I hope to one day rise to the top of my faith\'s religious hierarchy. (Lawful)",
5 : "Faith. I trust that my deity will guide my actions, I have faith that if I work hard, things will go well. (Lawful)",
6 : "Aspiration. I seek to prove myself worthy of my god\'s favor by matching my actions against his or her teachings. (Any)"
}
acolyte_bond = {
1 : "I would die to recover an ancient relic of my faith thatwas lost long ago.",
2 : "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
3 : "I owe my life to the priest who took me in when my parents died",
4 : "Everything I do is for the common people",
5 : "I will do anything to protect the temple where I served",
6 : "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy"
}
acolyte_flaw = {
1: "I judge others harshly, and myself even more severely.",
2: "I put too much trust in those who wield power within my temples hierarchy.",
3: "My piety sometimes leads me to blindly trust those that profess faith in my god.",
4: "I am inflexible in my thinking.",
5: "I am suspicious of strangers and expect the worst of them",
6: "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life."
}

charlatan_trait = {
1 : "I fall in and out of love easily, and am always pursuing someone.",
2 : "I have a joke for every occasion, especially occasions where humor is inappropriate.",
3 : "Flattery is my preferred trick for getting what I want.",
4 : " I\'m a born gambler who can\'t resist taking a risk for a potential payoff.",
5 : "I lie about almost everything, even when there\'s no good reason to.",
6 : "Sarcasm and insults are my weapons of choice.",
7 : "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
8 : "I pocket anything I see that might have some value."
}
charlatan_ideal = {
1 : "Independence. I am a free spirit, no one tells me what to do. (Chaotic)",
2 : "Fairness. I never target people who can\'t afford to lose a few coins. (Lawful)",
3 : "Charity. I distribute the money I acquire to the people who really need it. (Good) ",
4 : "Creativity. I never run the same con twice. (Chaotic)",
5 : "Friendship. Material goods come and go. Bonds of friendship last forever. (Good)",
6 : "Aspiration. I\'m determined to make something of myself. (Any)"
}
charlatan_bond = {
1 : "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
2 : "I owe everything to my mentor a horrible person who\'s probably rotting in jail somewhere.",
3 : "Somewhere out there, I have a child who doesn\'t know me. I\'m making the world better for him or her.",
4 : "I come from a noble family, and one day I\'ll reclaim my lands and title from those who stole them from me.",
5 : "A powerful person killed someone I love. Some day soon, I\'ll have my revenge.",
6 : "I swindled and ruined a person who didn\'t deserve it. I seek to atone for my misdeeds but might never be able to forgive myself."
}
charlatan_flaw = {
1: "I can\'t resist a pretty face.",
2: "I\'m always in debt. I spend my illgotten gains on decadent luxuries faster than I bring them in.",
3: "My piety sometimes leads me to blindly trust those that profess faith in my god.",
4: "I\'m convinced that no one could ever fool me the way I fool others.",
5: "I can\'t resist swindling people who are more powerful than me.",
6: "I hate to admit it and will hate myself for it, but I\'ll run."
}

criminal_trait = {
1 : "I always have a plan for what to do when things go wrong.",
2 : "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
3 : "The first thing I do in a new place is note the locations of everthing valuable, or whyere such things could be hidden.",
4 : "I would rather make a new friend than a new enemy.",
5 : "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
6 : "I don\'t pay attention to the risks in a situation. Never tell me the odds.",
7 : "The best way tp get me to do something is to tell me I can\'t do it.",
8 : "I blow up at the slightest insult."
}
criminal_ideal = {
1 : "Honor. I don\'t steal from others in the trade. (Lawful)",
2 : "Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)",
3 : "Charity. I steal from the wealthy so that I can help people in need. (Good)",
4 : "Greed. I will do whatever it takes to become wealthy. (Evil)",
5 : "People. I\'m loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care. (Neutral)",
6 : "Redemption. There\'s a spark of good in everyone. (Good)",
}
criminal_bond = {
1 : "I\'m trying to pay off an old debt I owe to a generous benefactor.",
2 : "My ill gotten gains go to support my family.",
3 : "Something important was taken from me, and I aim to steal it back.",
4 : "I will become the greatest thief that ever lived.",
5 : "I\'m guilty of a terrible crime. I hope I can redeem myself for it.",
6 : "There\'s a spark of good ineveryone.(Good)",
}
criminal_flaw = {
1 : "When I see something valuable, I can\'t think about anything but how to steal it.",
2 : "When faced with a choice between money and my friends, I usually choose the money.",
3 : "If there\'s a plan, I\'ll forget it. If I don\'t forget it, I\'ll ignore it.",
4 : "I have a \'tell\' that reveals when I\'m lying.",
5 : "I turn tail and run when things look bad.",
6 : "An innocent person is in prison for a crime that I committed. I\'m okay with that.",
}

entertainer_trait = {
1 : "I know a story relevant to almost every situation. ",
2 : "Whenever I come to a new place, I collect local rumors and spread gossip.",
3 : "I\'m a hopeless romantic, always searching for that special someone.",
4 : "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
5 : "I love a good insult, even one directed at me.",
6 : "I get bitter if I\'m not the center of attention.",
7 : "I\'ll settle for nothing less than perfection.",
8 : "I change my mood or my mind as quickly as I change key in a song."
}
entertainer_ideal = {
1 : "Beauty. When I perform, I make the world better than it was. (Good)",
2 : "Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are. (Lawful)",
3 : "Creativity. The world is in need of new ideas and bold action. (Chaotic)",
4 : "Greed. I\'m only in it for the money and fame.(Evil)",
5 : "People. I like seeing the smiles on people\'s faces when I perform. That\'s all that matters. (Neutral)",
6 : "Honesty. Art should reflect the soul, it should come from within and reveal who we really are. (Any)",
}
entertainer_bond = {
1 : "My instrument is my most treasured possession, and it reminds me of someone I love.",
2 : "Someone stole my precious instrument, and someday I\'ll get it back.",
3 : "I want to be famous, whatever it takes.",
4 : "I idolize a hero of the old tales and measure my deeds against that person\'s.",
5 : "I will do anything to prove myself superior to my hated rival.",
6 : "I would do anything for the other members of my old troupe.",
}
entertainer_flaw = {
1 : "I\'ll do anything to win fame and renown.",
2 : "I\'m a sucker for a pretty face.",
3 : "A scandal prevents me from ever going home again.",
4 : "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
5 : "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
6 : "Despite my best efforts, I am unreliable to my friends.",
}

guild_artisan_trait = {
1 : "1 I believe that anything worth doing is worth doing right. I can\'t help it I\'m a perfectionist.",
2 : "I\'m a snob who looks down on those who can\'t appreciate fine art.",
3 : "I always want to know how things work and what makes people tick.",
4 : "I\'m full of witty aphorisms and have a proverb for every occasion.",
5 : "I\'m rude to people who lack my commitment to hard work and fair play.",
6 : "I like to talk at length about my profession.",
7 : "I don\'t part with my money easily and will haggle tirelessly to get the best deal possible.",
8 : "I\'m well known for my work, and I want to make sure everyone appreciates it. I\'m always taken aback when people haven\'t heard of me."
}
guild_artisan_ideal = {
1 : "Ideal 1 Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization. (Lawful)",
2 : "Generosity. My talents were given to me so that I could use them to benefit the world. (Good)",
3 : "Freedom. Everyone should be free to pursue his or her own livelihood. (Chaotic)",
4 : "Greed. I\'m only in it for the money. (Evil)",
5 : "People. I\'m committed to the people I care about, not to ideals. (Neutral)",
6 : "Aspiration. I work hard to be the best there is at my craft.",
}
guild_artisan_bond = {
1 : "The workshop where I learned my trade is the most important place in the world to me.",
2 : "I created a great work for someone, and then found them unworthy to receive it. I\'m still looking for someone worthy.",
3 : "I owe my guild a great debt for forging me into the person I am today.",
4 : "I pursue wealth to secure someone\'s love.",
5 : "One day I will return to my guild and prove that I am the greatest artisan of them all.",
6 : "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood.",
}
guild_artisan_flaw = {
1 : "Flaw 1 I\'ll do anything to get my hands on something rare or priceless.",
2 : "I\'m quick to assume that someone is trying to cheat me.",
3 : "No one must ever learn that I once stole money from guild coffers.",
4 : "I\'m never satisfied with what I have I always want more.",
5 : "I would kill to acquire a noble title.",
6 : "I\'m horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I\'m surrounded by rivals.",
}

hermit_trait = {
1 : "I\'ve been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.",
2 : "I am utterly serene, even in the face of disaster.",
3 : "The leader of my community had something wise to say on every topic, and I am eager to share that wisdom.",
4 : "I feel tremendous empathy for all who suffer.",
5 : "I\'m oblivious to etiquette and social expectations.",
6 : "I connect everything that happens to me to a grand, cosmic plan.",
7 : "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.",
8 : "I am working on a grand philosophical theory and love sharing my ideas."
}
hermit_ideal = {
1 : "Greater Good. My gifts are meant to be shared with all, not used for my own benefit. (Good)",
2 : "Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking. (Lawful)",
3 : "Free Thinking. Inquiry and curiosity are the pillars of progress. (Chaotic)",
4 : "Power. Solitude and contemplation are paths toward mystical or magical power. (Evil)",
5 : "Live and Let Live. Meddling in the affairs of others only causes trouble. (Neutral)",
6 : "Self Knowledge. If you know yourself, there\'s nothing left to know. (Any)",
}
hermit_bond = {
1 : "Nothing is more important than the other members of my hermitage, order, or association.",
2 : "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
3 : "I\'m still seeking the enlightenment I pursued in my seclusion, and it still eludes me.",
4 : "I entered seclusion because I loved someone I could not have.",
5 : "Should my discovery come to light, it could bring ruin to the world.",
6 : "My isolation gave me great insight into a great evil that only I can destroy.",
}
hermit_flaw = {
1 : "Now that I\'ve returned to the world, I enjoy its delights a little too much.",
2 : "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.",
3 : "I am dogmatic in my thoughts and philosophy.",
4 : "I let my need to win arguments overshadow friendships and harmony.",
5 : "I\'d risk too much to uncover a lost bit of knowledge.",
6 : "I like keeping secrets and won\'t share them with anyone",
}

noble_trait = {
1 : "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
2 : "The common folk love me for my kindness and generosity.",
3 : "No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses.",
4 : "I take great pains to always look my best and follow the latest fashions.",
5 : "I don\'t like to get my hands dirty, and I won\'t be caught dead in unsuitable accommodations.",
6 : "Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
7 : "My favor, once lost, is lost forever.",
8 : "If you do me an injury, I will crush you, ruin your name, and salt your fields."
}
noble_ideal = {
1 : "Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity. (Good)",
2 : "Responsibility. It is my duty to respect the authority of those above me, just as those below me must respect mine. (Lawful)",
3 : "Independence. I must prove that I can handle myself without the coddling of my family. (Chaotic)",
4 : "Power. If I can attain more power, no one will tell me what to do. (Evil)",
5 : "Family. Blood runs thicker than water. (Any)",
6 : "Noble Obligation. It is my duty to protect and care for the people beneath me. (Good)",
}
noble_bond = {
1 : "I will face any challenge to win the approval of my family.",
2 : "My house\'s alliance with another noble family must be sustained at all costs.",
3 : "Nothing is more important than the other members of my family.",
4 : "I am in love with the heir of a family that my family despises.",
5 : "My loyalty to my sovereign is unwavering.",
6 : "The common folk must see me as a hero of the people.",
}
noble_flaw = {
1 : "I secretly believe that everyone is beneath me.",
2 : "I hide a truly scandalous secret that could ruin my family forever.",
3 : "I too often hear veiled insults and threats in every word addressed to me, and I\'m quick to anger.",
4 : "I have an insatiable desire for carnal pleasures.",
5 : "In fact, the world does revolve around me.",
6 : "By my words and actions, I often bring shame to my family.",
}

outlander_trait = {
1 : "I\'m driven by a wanderlust that led me away from home.",
2 : "I watch over my friends as if they were a litter of newborn pups.",
3 : "I once ran twenty five miles without stopping to warn to my clan of an approaching orc horde. I\'d do it again if I had to.",
4 : "I have a lesson for every situation, drawn from observing nature.",
5 : "I place no stock in wealthy or well mannered folk. Money and manners won\'t save you from a hungry owlbear.",
6 : "I\'m always picking things up, absently fiddling with them, and sometimes accidentally breaking them.",
7 : "I feel far more comfortable around animals than people.",
8 : "I was, in fact, raised by wolves."
}
outlander_ideal = {
1 : "Change. Life is like the seasons, in constant change, and we must change with it. (Chaotic)",
2 : "Greater Good. It is each person\'s responsibility to make the most happiness for the whole tribe. (Good)",
3 : "Honor. If I dishonor myself, I dishonor my whole clan. (Lawful)",
4 : "Might. The strongest are meant to rule. (Evil)",
5 : "Nature. The natural world is more important than all the constructs of civilization. (Neutral)",
6 : "Glory. I must earn glory in battle, for myself and my clan. (Any)",
}
outlander_bond = {
1 : "My family, clan, or tribe is the most important thing in my life, even when they are far from me.",
2 : "An injury to the unspoiled wilderness of my home is an injury to me.",
3 : "I will bring terrible wrath down on the evildoers who destroyed my homeland.",
4 : "I am the last of my tribe, and it is up to me to ensure their names enter legend.",
5 : "I suffer awful visions of a coming disaster and will do anything to prevent it.",
6 : "It is my duty to provide children to sustain my tribe.",
}
outlander_flaw = {
1 : "I am too enamored of ale, wine, and other intoxicants.",
2 : "There\'s no room for caution in a life lived to the fullest.",
3 : "I remember every insult I\'ve received and nurse a silent resentment toward anyone who\'s ever wronged me.",
4 : "I am slow to trust members of other races, tribes, and societies.",
5 : "Violence is my answer to almost any challenge.",
6 : "Don\'t expect me to save those who can\'t save themselves. It is nature\'s way that the strong thrive and the weak perish.",
}

sage_trait = {
1 : "I use polysyllabic words that convey the impression of great erudition.",
2 : "I \'ve read every book in the world  \'s greatest libraries or I like to boast that I have.",
3 : "I\'m used to helping out those who aren\'t as smart as I am, and I patiently explain anything and everything to others.",
4 : "There  \'s nothing I like more than a good mystery.",
5 : "I\'m willing to listen to every side of an argument before I make my own judgment.",
6 : "I . . . speak . . . slowly . . . when talking . . . to idiots, . . . which . . . almost . . . everyone . . . is . . . compared . . . to me.",
7 : "I am horribly, horribly awkward in social situations.",
8 : "8 I\'m convinced that people are always trying to steal my secrets."
}
sage_ideal = {
1 : "Knowledge. The path to power and self  improvement is through knowledge. (Neutral)",
2 : "Beauty. What is beautiful points us beyond itself toward what is true. (Good)",
3 : "Logic. Emotions must not cloud our logical thinking. (Lawful)",
4 : "No Limits. Nothing should fetter the infinite possibility inherent in all existence. (Chaotic)",
5 : "Power. Knowledge is the path to power and domination.",
6 : "Self Improvement. The goal of a life of study is the betterment of oneself. (Any)",
}
sage_bond = {
1 : "It is my duty to protect my students.",
2 : "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
3 : "I work to preserve a library, university, scriptorium, or monastery.",
4 : "My life  \'s work is a series of tomes related to a specific field of lore.",
5 : "I  \'ve been searching my whole life for the answer to a certain question.",
6 : "I sold my soul for knowledge. I hope to do great deeds and win it back.",
}
sage_flaw = {
1 : "I am easily distracted by the promise of information.",
2 : "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
3 : "Unlocking an ancient mystery is worth the price of a civilization.",
4 : "I overlook obvious solutions in favor of complicated ones.",
5 : "I speak without really thinking through my words, invariably insulting others.",
6 : "I can\'t keep a secret to save my life, or anyone else\'s.",
}

sage_trait = {
1 : "I use polysyllabic words that convey the impression of great erudition.",
2 : "I \'ve read every book in the world  \'s greatest libraries or I like to boast that I have.",
3 : "I\'m used to helping out those who aren\'t as smart as I am, and I patiently explain anything and everything to others.",
4 : "There  \'s nothing I like more than a good mystery.",
5 : "I\'m willing to listen to every side of an argument before I make my own judgment.",
6 : "I . . . speak . . . slowly . . . when talking . . . to idiots, . . . which . . . almost . . . everyone . . . is . . . compared . . . to me.",
7 : "I am horribly, horribly awkward in social situations.",
8 : "8 I\'m convinced that people are always trying to steal my secrets."
}
sage_ideal = {
1 : "Knowledge. The path to power and self  improvement is through knowledge. (Neutral)",
2 : "Beauty. What is beautiful points us beyond itself toward what is true. (Good)",
3 : "Logic. Emotions must not cloud our logical thinking. (Lawful)",
4 : "No Limits. Nothing should fetter the infinite possibility inherent in all existence. (Chaotic)",
5 : "Power. Knowledge is the path to power and domination.",
6 : "Self Improvement. The goal of a life of study is the betterment of oneself. (Any)",
}
sage_bond = {
1 : "It is my duty to protect my students.",
2 : "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
3 : "I work to preserve a library, university, scriptorium, or monastery.",
4 : "My life  \'s work is a series of tomes related to a specific field of lore.",
5 : "I  \'ve been searching my whole life for the answer to a certain question.",
6 : "I sold my soul for knowledge. I hope to do great deeds and win it back.",
}
sage_flaw = {
1 : "I am easily distracted by the promise of information.",
2 : "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
3 : "Unlocking an ancient mystery is worth the price of a civilization.",
4 : "I overlook obvious solutions in favor of complicated ones.",
5 : "I speak without really thinking through my words, invariably insulting others.",
6 : "I can\'t keep a secret to save my life, or anyone else\'s.",
}

sailor_trait = {
1 : "My friends know they can rely on me, no matter what.",
2 : "I work hard so that I can play hard when the work is done.",
3 : "I enjoy sailing into new ports and making new friends over a flagon of ale.",
4 : "I stretch the truth for the sake of a good story.",
5 : "To me, a tavern brawl is a nice way to get to know a new city.",
6 : "I never pass up a friendly wager.",
7 : "My language is as foul as an otyugh nest.",
8 : "I like a job well done, especially if I can convince someone else to do it."
}
sailor_ideal = {
1 : "Respect. The thing that keeps a ship together is mutual respect between captain and crew. (Good)",
2 : "Fairness. We all do the work, so we all share in the rewards. (Lawful)",
3 : "Mastery. I\'m a predator, and the other ships on the sea are my prey.",
4 : "People. I\'m committed to my crewmates, not to ideals.",
5 : "Aspiration. Someday I\'ll own my own ship and chart my own destiny. (Any)",
6 : "Freedom. The sea is freedom, the freedom to go anywhere and do anything. (Chaotic)",
}
sailor_bond = {
1 : "I\'m loyal to my captain first, everything else second.",
2 : "The ship is most important crewmates and captains come and go.",
3 : "I\'ll always remember my first ship.",
4 : "In a harbor town, I have a paramour whose eyes nearly stole me from the sea.",
5 : "I was cheated out of my fair share of the profits, and I want to get my due.",
6 : "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine.",
}
sailor_flaw = {
1 : "I follow orders, even if I think they\'re wrong.",
2 : "I\'ll say anything to avoid having to do extra work.",
3 : "Once someone questions my courage, I never back down no matter how dangerous the situation.",
4 : "Once I start drinking, it\'s hard for me to stop.",
5 : "I can\'t help but pocket loose coins and other trinkets I come across.",
6 : "My pride will probably lead to my destruction.",
}

soldier_trait = {
1 : "I\'m always polite and respectful.",
2 : "I\'m haunted by memories o f war. I can\'t get the images of violence out of my mind.",
3 : "I\'ve lost too many friends, and I\'m slow to make new ones.",
4 : "I\'m full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
5 : "I can stare down a hell hound without flinching.",
6 : "I enjoy being strong and like breaking things.",
7 : "I have a crude sense of humor.",
8 : "I face problems head-on. A simple, direct solution is the best path to success."
}
soldier_ideal = {
1 : "Greater Good. Our lot is to lay down our lives in defense of others. (Good)",
2 : "Responsibility. I do what I must and obey just authority. (Lawful)",
3 : "Independence. When people follow orders blindly, they embrace a kind of tyranny. (Chaotic)",
4 : "Might. In life as in war, the stronger force wins. (Evil)",
5 : "Live and Let Live. Ideals aren\'t worth killing over or going to war for. (Neutral)",
6 : "Nation. My city, nation, or people are all that matter. (Any)",
}
soldier_bond = {
1 : "I would still lay down my life for the people I served with.",
2 : "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
3 : "My honor is my life.",
4 : "I\'ll never forget the crushing defeat my company suffered or the enemies who dealt it.",
5 : "Those who fight beside me are those worth dying for.",
6 : "I fight for those who cannot fight for themselves.",
}
soldier_flaw = {
1 : "The monstrous enemy we faced in battle still leaves me quivering with fear.",
2 : "I have little respect for anyone who is not a proven warrior.",
3 : "I made a terrible mistake in battle cost many lives  and I would do anything to keep that mistake secret.",
4 : "My hatred of my enemies is blind and unreasoning.",
5 : "I obey the law, even if the law causes misery.",
6 : "I\'d rather eat my armor than admit when I\'m wrong.",
}

urchin_trait = {
1 : "I hide scraps of food and trinkets away in my pockets.",
2 : "I ask a lot of questions.",
3 : "I like to squeeze into small places where no one else can get to me.",
4 : "I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms.",
5 : "I eat like a pig and have bad manners.",
6 : "I think anyone who\'s nice to me is hiding evil intent.",
7 : "I don\'t like to bathe.",
8 : "I bluntly say what other people are hinting at or hiding."
}
urchin_ideal = {
1 : "Respect. All people, rich or poor, deserve respect. (Good)",
2 : "Community. We have to take care of each other, because no one else is going to do it. (Lawful)",
3 : "Change. The low are lifted up, and the high and mighty are brought down. Change is the nature of things. (Chaotic)",
4 : "Retribution. The rich need to be shown what life and death are like in the gutters. (Evil)",
5 : "People. I help the people who help me that\'s what keeps us alive. (Neutral)",
6 : "Aspiration. I\'m going to prove that I\'m worthy of a better life.",
}
urchin_bond = {
1 : "My town or city is my home, and I\'ll fight to defend it.",
2 : "I sponsor an orphanage to keep others from enduring what I was forced to endure.",
3 : "I owe my survival to another urchin who taught me to live on the streets.",
4 : "I owe a debt I can never repay to the person who took pity on me.",
5 : "I escaped my life of poverty by robbing an important person, and I\'m wanted for it.",
6 : "No one else should have to endure the hardships I\'ve been through.",
}
urchin_flaw = {
1 : "If I\'m outnumbered, I will run away from a fight.",
2 : "Gold seems like a lot of money to me, and I\'ll do just about anything for more of it.",
3 : "I will never fully trust anyone other than myself.",
4 : "I\'d rather kill someone in their sleep then fight fair.",
5 : "It\'s not stealing if I need it more than someone else.",
6 : "People who can\'t take care of themselves get what they deserve.",
}

#############################################################################################################################################################


print '\n' + "Your character has many qualities that define them, but we\'re going to focus on four of them which you can either write your own, choose CAREFULLY from our list, or radomly recieve one from our list." + '\n' + "You will choose a TRAIT, IDEAL, BOND, and a FLAW!"+ '\n'
print "Now that you have chosen %s as your background,  pick a TRAIT from below" % (player_background[0]) + '\n'*3

def choose_acolyte_trait():
    if player_background == ["ACOLYTE"]:
        print "1: " + acolyte_trait[1]
        print "2: " + acolyte_trait[2]
        print "3: " + acolyte_trait[3]
        print "4: " + acolyte_trait[4]
        print "5: " + acolyte_trait[5]
        print "6: " + acolyte_trait[6]
        print "7: " + acolyte_trait[7]
        print "8: " + acolyte_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(acolyte_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(acolyte_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_acolyte_trait()

def choose_acolyte_ideal():
    if player_background == ["ACOLYTE"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + acolyte_ideal[1]
        print "2: " + acolyte_ideal[2]
        print "3: " + acolyte_ideal[3]
        print "4: " + acolyte_ideal[4]
        print "5: " + acolyte_ideal[5]
        print "6: " + acolyte_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(acolyte_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(acolyte_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_acolyte_ideal()

def choose_acolyte_bond():
    if player_background == ["ACOLYTE"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + acolyte_bond[1]
        print "2: " + acolyte_bond[2]
        print "3: " + acolyte_bond[3]
        print "4: " + acolyte_bond[4]
        print "5: " + acolyte_bond[5]
        print "6: " + acolyte_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(acolyte_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(acolyte_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_acolyte_bond()

def choose_acolyte_flaw():
    if player_background == ["ACOLYTE"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + acolyte_flaw[1]
        print "2: " + acolyte_flaw[2]
        print "3: " + acolyte_flaw[3]
        print "4: " + acolyte_flaw[4]
        print "5: " + acolyte_flaw[5]
        print "6: " + acolyte_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(acolyte_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(acolyte_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_acolyte_flaw()

def choose_entertainer_trait():
    if player_background == ["ENTERTAINER"]:
        print "1: " + entertainer_trait[1]
        print "2: " + entertainer_trait[2]
        print "3: " + entertainer_trait[3]
        print "4: " + entertainer_trait[4]
        print "5: " + entertainer_trait[5]
        print "6: " + entertainer_trait[6]
        print "7: " + entertainer_trait[7]
        print "8: " + entertainer_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(entertainer_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(entertainer_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_entertainer_trait()

def choose_entertainer_ideal():
    if player_background == ["ENTERTAINER"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + entertainer_ideal[1]
        print "2: " + entertainer_ideal[2]
        print "3: " + entertainer_ideal[3]
        print "4: " + entertainer_ideal[4]
        print "5: " + entertainer_ideal[5]
        print "6: " + entertainer_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(entertainer_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(entertainer_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_entertainer_ideal()

def choose_entertainer_bond():
    if player_background == ["ENTERTAINER"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + entertainer_bond[1]
        print "2: " + entertainer_bond[2]
        print "3: " + entertainer_bond[3]
        print "4: " + entertainer_bond[4]
        print "5: " + entertainer_bond[5]
        print "6: " + entertainer_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(entertainer_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(entertainer_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_entertainer_bond()

def choose_entertainer_flaw():
    if player_background == ["ENTERTAINER"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + entertainer_flaw[1]
        print "2: " + entertainer_flaw[2]
        print "3: " + entertainer_flaw[3]
        print "4: " + entertainer_flaw[4]
        print "5: " + entertainer_flaw[5]
        print "6: " + entertainer_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(entertainer_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(entertainer_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_entertainer_flaw()

def choose_criminal_trait():
    if player_background == ["CRIMINAL"]:
        print "1: " + criminal_trait[1]
        print "2: " + criminal_trait[2]
        print "3: " + criminal_trait[3]
        print "4: " + criminal_trait[4]
        print "5: " + criminal_trait[5]
        print "6: " + criminal_trait[6]
        print "7: " + criminal_trait[7]
        print "8: " + criminal_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(criminal_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(criminal_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_criminal_trait()

def choose_criminal_ideal():
    if player_background == ["CRIMINAL"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + criminal_ideal[1]
        print "2: " + criminal_ideal[2]
        print "3: " + criminal_ideal[3]
        print "4: " + criminal_ideal[4]
        print "5: " + criminal_ideal[5]
        print "6: " + criminal_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(criminal_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(criminal_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_criminal_ideal()

def choose_criminal_bond():
    if player_background == ["CRIMINAL"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + criminal_bond[1]
        print "2: " + criminal_bond[2]
        print "3: " + criminal_bond[3]
        print "4: " + criminal_bond[4]
        print "5: " + criminal_bond[5]
        print "6: " + criminal_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(criminal_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(criminal_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_criminal_bond()

def choose_criminal_flaw():
    if player_background == ["CRIMINAL"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + criminal_flaw[1]
        print "2: " + criminal_flaw[2]
        print "3: " + criminal_flaw[3]
        print "4: " + criminal_flaw[4]
        print "5: " + criminal_flaw[5]
        print "6: " + criminal_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(criminal_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(criminal_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_criminal_flaw()

def choose_charlatan_trait():
    if player_background == ["CHARLATAN"]:
        print "1: " + charlatan_trait[1]
        print "2: " + charlatan_trait[2]
        print "3: " + charlatan_trait[3]
        print "4: " + charlatan_trait[4]
        print "5: " + charlatan_trait[5]
        print "6: " + charlatan_trait[6]
        print "7: " + charlatan_trait[7]
        print "8: " + charlatan_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(charlatan_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(charlatan_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_charlatan_trait()

def choose_charlatan_ideal():
    if player_background == ["CHARLATAN"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + charlatan_ideal[1]
        print "2: " + charlatan_ideal[2]
        print "3: " + charlatan_ideal[3]
        print "4: " + charlatan_ideal[4]
        print "5: " + charlatan_ideal[5]
        print "6: " + charlatan_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(charlatan_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(charlatan_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_charlatan_ideal()

def choose_charlatan_bond():
    if player_background == ["CHARLATAN"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + charlatan_bond[1]
        print "2: " + charlatan_bond[2]
        print "3: " + charlatan_bond[3]
        print "4: " + charlatan_bond[4]
        print "5: " + charlatan_bond[5]
        print "6: " + charlatan_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(charlatan_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(charlatan_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_charlatan_bond()

def choose_charlatan_flaw():
    if player_background == ["CHARLATAN"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + charlatan_flaw[1]
        print "2: " + charlatan_flaw[2]
        print "3: " + charlatan_flaw[3]
        print "4: " + charlatan_flaw[4]
        print "5: " + charlatan_flaw[5]
        print "6: " + charlatan_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(charlatan_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(charlatan_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_charlatan_flaw()

def choose_guild_artisan_trait():
    if player_background == ["GUILD ARTISAN"]:
        print "1: " + guild_artisan_trait[1]
        print "2: " + guild_artisan_trait[2]
        print "3: " + guild_artisan_trait[3]
        print "4: " + guild_artisan_trait[4]
        print "5: " + guild_artisan_trait[5]
        print "6: " + guild_artisan_trait[6]
        print "7: " + guild_artisan_trait[7]
        print "8: " + guild_artisan_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(guild_artisan_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(guild_artisan_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_guild_artisan_trait()

def choose_guild_artisan_ideal():
    if player_background == ["GUILD ARTISAN"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + guild_artisan_ideal[1]
        print "2: " + guild_artisan_ideal[2]
        print "3: " + guild_artisan_ideal[3]
        print "4: " + guild_artisan_ideal[4]
        print "5: " + guild_artisan_ideal[5]
        print "6: " + guild_artisan_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(guild_artisan_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(guild_artisan_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_guild_artisan_ideal()

def choose_guild_artisan_bond():
    if player_background == ["GUILD ARTISAN"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + guild_artisan_bond[1]
        print "2: " + guild_artisan_bond[2]
        print "3: " + guild_artisan_bond[3]
        print "4: " + guild_artisan_bond[4]
        print "5: " + guild_artisan_bond[5]
        print "6: " + guild_artisan_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(guild_artisan_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(guild_artisan_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_guild_artisan_bond()

def choose_guild_artisan_flaw():
    if player_background == ["GUILD ARTISAN"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + guild_artisan_flaw[1]
        print "2: " + guild_artisan_flaw[2]
        print "3: " + guild_artisan_flaw[3]
        print "4: " + guild_artisan_flaw[4]
        print "5: " + guild_artisan_flaw[5]
        print "6: " + guild_artisan_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(guild_artisan_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(guild_artisan_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_guild_artisan_flaw()

def choose_hermit_trait():
    if player_background == ["HERMIT"]:
        print "1: " + hermit_trait[1]
        print "2: " + hermit_trait[2]
        print "3: " + hermit_trait[3]
        print "4: " + hermit_trait[4]
        print "5: " + hermit_trait[5]
        print "6: " + hermit_trait[6]
        print "7: " + hermit_trait[7]
        print "8: " + hermit_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(hermit_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(hermit_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_hermit_trait()

def choose_hermit_ideal():
    if player_background == ["HERMIT"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + hermit_ideal[1]
        print "2: " + hermit_ideal[2]
        print "3: " + hermit_ideal[3]
        print "4: " + hermit_ideal[4]
        print "5: " + hermit_ideal[5]
        print "6: " + hermit_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(hermit_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(hermit_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_hermit_ideal()

def choose_hermit_bond():
    if player_background == ["HERMIT"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + hermit_bond[1]
        print "2: " + hermit_bond[2]
        print "3: " + hermit_bond[3]
        print "4: " + hermit_bond[4]
        print "5: " + hermit_bond[5]
        print "6: " + hermit_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(hermit_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(hermit_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_hermit_bond()

def choose_hermit_flaw():
    if player_background == ["HERMIT"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + hermit_flaw[1]
        print "2: " + hermit_flaw[2]
        print "3: " + hermit_flaw[3]
        print "4: " + hermit_flaw[4]
        print "5: " + hermit_flaw[5]
        print "6: " + hermit_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(hermit_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(hermit_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_hermit_flaw()

def choose_noble_trait():
    if player_background == ["NOBLE"]:
        print "1: " + noble_trait[1]
        print "2: " + noble_trait[2]
        print "3: " + noble_trait[3]
        print "4: " + noble_trait[4]
        print "5: " + noble_trait[5]
        print "6: " + noble_trait[6]
        print "7: " + noble_trait[7]
        print "8: " + noble_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(noble_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(noble_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_noble_trait()

def choose_noble_ideal():
    if player_background == ["NOBLE"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + noble_ideal[1]
        print "2: " + noble_ideal[2]
        print "3: " + noble_ideal[3]
        print "4: " + noble_ideal[4]
        print "5: " + noble_ideal[5]
        print "6: " + noble_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(noble_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(noble_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_noble_ideal()

def choose_noble_bond():
    if player_background == ["NOBLE"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + noble_bond[1]
        print "2: " + noble_bond[2]
        print "3: " + noble_bond[3]
        print "4: " + noble_bond[4]
        print "5: " + noble_bond[5]
        print "6: " + noble_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(noble_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(noble_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_noble_bond()

def choose_noble_flaw():
    if player_background == ["NOBLE"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + noble_flaw[1]
        print "2: " + noble_flaw[2]
        print "3: " + noble_flaw[3]
        print "4: " + noble_flaw[4]
        print "5: " + noble_flaw[5]
        print "6: " + noble_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(noble_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(noble_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_noble_flaw()

def choose_outlander_trait():
    if player_background == ["OUTLANDER"]:
        print "1: " + outlander_trait[1]
        print "2: " + outlander_trait[2]
        print "3: " + outlander_trait[3]
        print "4: " + outlander_trait[4]
        print "5: " + outlander_trait[5]
        print "6: " + outlander_trait[6]
        print "7: " + outlander_trait[7]
        print "8: " + outlander_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(outlander_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(outlander_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_outlander_trait()

def choose_outlander_ideal():
    if player_background == ["OUTLANDER"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + outlander_ideal[1]
        print "2: " + outlander_ideal[2]
        print "3: " + outlander_ideal[3]
        print "4: " + outlander_ideal[4]
        print "5: " + outlander_ideal[5]
        print "6: " + outlander_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(outlander_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(outlander_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_outlander_ideal()

def choose_outlander_bond():
    if player_background == ["OUTLANDER"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + outlander_bond[1]
        print "2: " + outlander_bond[2]
        print "3: " + outlander_bond[3]
        print "4: " + outlander_bond[4]
        print "5: " + outlander_bond[5]
        print "6: " + outlander_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(outlander_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(outlander_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_outlander_bond()

def choose_outlander_flaw():
    if player_background == ["OUTLANDER"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + outlander_flaw[1]
        print "2: " + outlander_flaw[2]
        print "3: " + outlander_flaw[3]
        print "4: " + outlander_flaw[4]
        print "5: " + outlander_flaw[5]
        print "6: " + outlander_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(outlander_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(outlander_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_outlander_flaw()

def choose_sage_trait():
    if player_background == ["SAGE"]:
        print "1: " + sage_trait[1]
        print "2: " + sage_trait[2]
        print "3: " + sage_trait[3]
        print "4: " + sage_trait[4]
        print "5: " + sage_trait[5]
        print "6: " + sage_trait[6]
        print "7: " + sage_trait[7]
        print "8: " + sage_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(sage_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(sage_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_sage_trait()

def choose_sage_ideal():
    if player_background == ["SAGE"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + sage_ideal[1]
        print "2: " + sage_ideal[2]
        print "3: " + sage_ideal[3]
        print "4: " + sage_ideal[4]
        print "5: " + sage_ideal[5]
        print "6: " + sage_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(sage_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(sage_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_sage_ideal()

def choose_sage_bond():
    if player_background == ["SAGE"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + sage_bond[1]
        print "2: " + sage_bond[2]
        print "3: " + sage_bond[3]
        print "4: " + sage_bond[4]
        print "5: " + sage_bond[5]
        print "6: " + sage_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(sage_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(sage_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_sage_bond()

def choose_sage_flaw():
    if player_background == ["SAGE"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + sage_flaw[1]
        print "2: " + sage_flaw[2]
        print "3: " + sage_flaw[3]
        print "4: " + sage_flaw[4]
        print "5: " + sage_flaw[5]
        print "6: " + sage_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(sage_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(sage_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_sage_flaw()

def choose_sailor_trait():
    if player_background == ["SAILOR"]:
        print "1: " + sailor_trait[1]
        print "2: " + sailor_trait[2]
        print "3: " + sailor_trait[3]
        print "4: " + sailor_trait[4]
        print "5: " + sailor_trait[5]
        print "6: " + sailor_trait[6]
        print "7: " + sailor_trait[7]
        print "8: " + sailor_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(sailor_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(sailor_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_sailor_trait()

def choose_sailor_ideal():
    if player_background == ["SAILOR"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + sailor_ideal[1]
        print "2: " + sailor_ideal[2]
        print "3: " + sailor_ideal[3]
        print "4: " + sailor_ideal[4]
        print "5: " + sailor_ideal[5]
        print "6: " + sailor_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(sailor_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(sailor_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_sailor_ideal()

def choose_sailor_bond():
    if player_background == ["SAILOR"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + sailor_bond[1]
        print "2: " + sailor_bond[2]
        print "3: " + sailor_bond[3]
        print "4: " + sailor_bond[4]
        print "5: " + sailor_bond[5]
        print "6: " + sailor_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(sailor_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(sailor_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_sailor_bond()

def choose_sailor_flaw():
    if player_background == ["SAILOR"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + sailor_flaw[1]
        print "2: " + sailor_flaw[2]
        print "3: " + sailor_flaw[3]
        print "4: " + sailor_flaw[4]
        print "5: " + sailor_flaw[5]
        print "6: " + sailor_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(sailor_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(sailor_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_sailor_flaw()

def choose_soldier_trait():
    if player_background == ["SOLDIER"]:
        print "1: " + soldier_trait[1]
        print "2: " + soldier_trait[2]
        print "3: " + soldier_trait[3]
        print "4: " + soldier_trait[4]
        print "5: " + soldier_trait[5]
        print "6: " + soldier_trait[6]
        print "7: " + soldier_trait[7]
        print "8: " + soldier_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(soldier_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(soldier_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_soldier_trait()

def choose_soldier_ideal():
    if player_background == ["SOLDIER"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + soldier_ideal[1]
        print "2: " + soldier_ideal[2]
        print "3: " + soldier_ideal[3]
        print "4: " + soldier_ideal[4]
        print "5: " + soldier_ideal[5]
        print "6: " + soldier_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(soldier_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(soldier_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_soldier_ideal()

def choose_soldier_bond():
    if player_background == ["SOLDIER"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + soldier_bond[1]
        print "2: " + soldier_bond[2]
        print "3: " + soldier_bond[3]
        print "4: " + soldier_bond[4]
        print "5: " + soldier_bond[5]
        print "6: " + soldier_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(soldier_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(soldier_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_soldier_bond()

def choose_soldier_flaw():
    if player_background == ["SOLDIER"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + soldier_flaw[1]
        print "2: " + soldier_flaw[2]
        print "3: " + soldier_flaw[3]
        print "4: " + soldier_flaw[4]
        print "5: " + soldier_flaw[5]
        print "6: " + soldier_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(soldier_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(soldier_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_soldier_flaw()

def choose_urchin_trait():
    if player_background == ["URCHIN"]:
        print "1: " + urchin_trait[1]
        print "2: " + urchin_trait[2]
        print "3: " + urchin_trait[3]
        print "4: " + urchin_trait[4]
        print "5: " + urchin_trait[5]
        print "6: " + urchin_trait[6]
        print "7: " + urchin_trait[7]
        print "8: " + urchin_trait[8]
        print
        while True:
            trait_input = raw_input("Enter R for RANDOM, the number of your desired trait, or NONE to write your own: ").upper()
            if trait_input == "1" or trait_input == "2" or trait_input == "3" or trait_input == "4" or trait_input == "5" or trait_input == "6" or trait_input == "7" or trait_input == "8":
                player_trait.append(urchin_trait[(int(trait_input))])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                print
                return True
            elif trait_input == "NONE":
                player_trait.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            elif trait_input == "R":
                x = randint(1,8)
                player_trait.append(urchin_trait[x])
                print
                print
                print "Your trait is now: %s" % player_trait[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
choose_urchin_trait()

def choose_urchin_ideal():
    if player_background == ["URCHIN"]:
        print "Now pick a IDEAL from below"
        print
        print
        print
        print "1: " + urchin_ideal[1]
        print "2: " + urchin_ideal[2]
        print "3: " + urchin_ideal[3]
        print "4: " + urchin_ideal[4]
        print "5: " + urchin_ideal[5]
        print "6: " + urchin_ideal[6]
        print
        while True:
            ideal_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if ideal_input == "1" or ideal_input == "2" or ideal_input == "3" or ideal_input == "4" or ideal_input == "5" or ideal_input == "6":
                player_ideal.append(urchin_ideal[(int(ideal_input))])
                print "Your ideal is now: %s" % player_ideal[0]
                print
                print
                return True
            elif ideal_input == "NONE":
                player_ideal.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your ideal is now: %s" % player_ideal[0]
                print
                return True
            elif ideal_input == "R":
                x = randint(1,6)
                player_ideal.append(urchin_ideal[x])
                print
                print
                print "Your trait is now: %s" % player_ideal[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_urchin_ideal()

def choose_urchin_bond():
    if player_background == ["URCHIN"]:
        print
        print
        print "Now pick a BOND from below"
        print
        print
        print
        print "1: " + urchin_bond[1]
        print "2: " + urchin_bond[2]
        print "3: " + urchin_bond[3]
        print "4: " + urchin_bond[4]
        print "5: " + urchin_bond[5]
        print "6: " + urchin_bond[6]
        print
        while True:
            bond_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if bond_input == "1" or bond_input == "2" or bond_input == "3" or bond_input == "4" or bond_input == "5" or bond_input == "6":
                player_bond.append(urchin_bond[(int(bond_input))])
                print "Your bond is now: %s" % player_bond[0]
                print
                print
                return True
            elif bond_input == "NONE":
                player_bond.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            elif bond_input == "R":
                x = randint(1,6)
                player_bond.append(urchin_bond[x])
                print
                print
                print "Your bond is now: %s" % player_bond[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_urchin_bond()

def choose_urchin_flaw():
    if player_background == ["URCHIN"]:
        print
        print
        print "Now pick a FLAW from below"
        print
        print
        print
        print "1: " + urchin_flaw[1]
        print "2: " + urchin_flaw[2]
        print "3: " + urchin_flaw[3]
        print "4: " + urchin_flaw[4]
        print "5: " + urchin_flaw[5]
        print "6: " + urchin_flaw[6]
        print
        while True:
            flaw_input = raw_input("Enter R for RANDOM, the number of your desired ideal, or NONE to write your own: ").upper()
            if flaw_input == "1" or flaw_input == "2" or flaw_input == "3" or flaw_input == "4" or flaw_input == "5" or flaw_input == "6":
                player_flaw.append(urchin_flaw[(int(bond_input))])
                print "Your flaw is now: %s" % player_flaw[0]
                print
                print
                return True
            elif flaw_input == "NONE":
                player_flaw.append(str(raw_input("Enter your own: ")))
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            elif flaw_input == "R":
                x = randint(1,6)
                player_flaw.append(urchin_flaw[x])
                print
                print
                print "Your flaw is now: %s" % player_flaw[0]
                print
                return True
            else:
                print
                print "Invalid input try again!"
                print
    else:
        return None
choose_urchin_flaw()


print
print "This is your BACKGROUND:"
print "I am a a(n) %s!" % player_background[0]
print player_trait[0]
print "I believe in " + player_ideal[0]
print player_bond[0]
print "Unfortunately " + player_flaw[0]
print

dick = raw_input("thanks ")
