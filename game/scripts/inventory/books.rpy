
default galadriel1_ITEM = Item("galadriel1_book", "book", "Tome 1: The Tale of Galadriel", 100, "This book tells the story of an elven princess who defies the traditions of her people and chooses to forge her own destiny.\nEffect: Improves imagination.", label="galadriel1_book", limit=1, caption="Read")
default galadriel2_ITEM = Item("galadriel2_book", "book", "Tome 2: The Tale of Galadriel", 200, "This is a continuation on the story of the elven princess who defies the tradition, with a twist.\nEffect: Improves imagination.", label="galadriel2_book", limit=1, caption="Read")
default gameofchairs1_ITEM = Item("game_of_chairs1_book", "book", "Tome 1: Game of Chairs", 50, "An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape.", label="game_of_chairs1_book", limit=1, caption="Read")
default gameofchairs2_ITEM = Item("game_of_chairs2_book", "book", "Tome 2: Game of Chairs", 100, "An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape.", label="game_of_chairs2_book", limit=1, caption="Read")
default gameofchairs3_ITEM = Item("game_of_chairs3_book", "book", "Tome 3: Game of Chairs", 150, "An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape.", label="game_of_chairs3_book", limit=1, caption="Read")
default my_dear_waifu_ITEM = Item("my_dear_waifu_book", "book", "My Dear Waifu", 250, "Relive the glory of your high school days and find your ultimate \"waifu\".{size=-3}\n\nEnding 01 {unicode}✘{/unicode}\nEnding 02 {unicode}✘{/unicode}\nEnding 03 {unicode}✘{/unicode}\nEnding 04 {unicode}✘{/unicode}\nEnding 05 {unicode}✘{/unicode}{/size}", label="waifu_book", limit=1, caption="Read")

label book_start:
    call weather_sound
    stop music fadeout 1
    play sound "sounds/bookopen.ogg"

    if states.fireplace_started:
        call gen_chibi("read_near_fire")
        with d3
    else:
        call gen_chibi("read")
        with d3
    return

label book_end:
    play sound "sounds/bookclose.ogg"

    if states.fireplace_started:
        call gen_chibi("read_near_fire_done")
    else:
        call gen_chibi("read_done")
    return

label galadriel1_book:
    call book_start

    nar "Galadriel - a gentle and gracious elven princess is introduced into the story."
    nar "Galadriel's father - King Methis, and his childhood friend Mofothelis are introduced into the story."
    nar "King Methis makes an announcement. His daughter, princess Galadriel is to be wed to chancellor Mofothelis."
    nar "Galadriel refuses to marry a man who is thrice her age and whom, up until now, she considered only as her uncle."
    nar "King Methis dismisses her daughter's {i}foolish{/i} complaints. Galadriel decides to run away."
    nar "Galadriel manages to leave the royal residence at night unnoticed..."
    nar "King Methis is furious about his daughter's escape. He decides to personally lead the search party."
    nar "Galadriel rides her mare named {i}white dove{/i} through the forest. The Princess enjoys her freedom..."
    nar "After a while she meets a rather handsome human nobleman on a horse..."
    nar "Galadriel rides alongside the nobleman. They exchange meaningless pleasantries, occasionally interrupted with laughter."
    nar "Suddenly the nobleman attacks the princess and knocks her out!"
    nar "When Galadriel comes to, to her horror, she realises that the nobleman is having his way with her."
    nar "Galadriel is screaming for help but the man only laughs at her."
    nar "Galadriel tries to fight the nobleman off. Only now she notices that about half a dozen men are surrounding them. The men are sneering viciously."
    nar "After the nobleman is done with Galadriel, every one of his men in turn has a go at the elven princess. Galadriel cries and begs them to stop."
    nar "Galadriel finds herself in a cage at some sort of market. Her hands are tied, Her noble garments are ripped to shreds and her hair is full of twigs and dry semen."
    nar "A fat, rich looking man buys Galadriel and brings her to his house. The princess does not cry anymore. She is happy to be out of the cage."
    nar "Galadriel is allowed to take a bath after which a servant brings her clean clothes and some food."
    nar "Galadriel is starting to feel hopeful but it does not last. Soon she realises what kind of establishment this is: a whorehouse."
    nar "The elven princess is forced to work as a whore. She detests her new life but has very little choice."
    nar "Galadriel gains popularity quickly. Humans, Dark Elves and even the occasionally dwarfs - she spreads her legs for everyone."
    nar "The fame of the young and beautiful elven whore spreads. Galadriel accepts her new life in the brothel."
    nar "Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant."
    nar "The end."

    call book_end

    gen "What the fuck did I just read?" ("base", xpos="far_left", ypos="head")

    if game.daytime:
        jump night_start
    else:
        jump day_start

label galadriel2_book:
    call book_start

    nar "Galadriel has been pregnant for several months now. To the princess' own surprise her popularity grows seemingly in direct correlation to the size of her belly."
    nar "Although Galadriel maintains the appearance of an obedient whore, in truth she contemplates her escape from the brothel."
    nar "The Elven Royal-Whore knows nothing of the life outside the walls of the brothel. But it does not affect her determination to escape."
    nar "It takes a lot of preparation and careful planning but Galadriel manages to successfully escape from the brothel."
    nar "Galadriel soon gets lost in the vast city and is forced to spend the night on the street."
    nar "Food is hard to come by on the streets. Galadriel fights a pack of stray dogs over some scraps and one of them bites her hand badly."
    nar "The now pregnant Galadriel offers her {i}company{/i} to a couple of filthy-looking homeless men in exchange for food. She spends the night with them."
    nar "Galadriel realises that her life back in the brothel wasn't so bad compared to the live she's been leading for the past several days. She decides to return."
    nar "Galadriel's owner - the fat, wealthy man does not punish Galadriel for escaping. He is happy to have one of his most popular girls back."
    nar "Galadriel is, yet again, warm, fed, and full of cum. She is glad to be back and as popular as ever."
    nar "Galadriel keeps servicing the clients throughout the rest of her pregnancy. The baby is due any day now..."
    nar "A wealthy man wearing a mask booked Galadriel for an entire day. Galadriel is wondering about the man's true identity rather lazily while pleasuring him."
    nar "The mystery man spends the entire day by having his way with Galadriel. Her engorged breasts drip milk heavily as the man fucks her."
    nar "The masked man splatters Galadriel's face with cum for the second time today. He then chooses to reveal his identity and takes his mask off."
    nar "Galadriel recognises the man as her father - King Methis. Only now he realises that the pregnant whore he fucked for hours is his long lost daughter."
    nar "The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face..."
    nar "Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed."
    nar "It takes the elven princess several minutes to realise that she never was pregnant. The entire adventure was nothing but a dream."
    nar "Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis."
    nar "Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite."
    nar "The end."

    call book_end

    gen "..." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        jump night_start
    else:
        jump day_start

label game_of_chairs1_book:
    call book_start

    nar "A new race of half-frozen undead monsters is introduced into the story."
    nar "A family of noble northmen is introduced into the story."
    nar "A group of people known as Watchmen are introduced into the story."
    nar "Half-frozen undead attack the Watchmen killing everyone but one man who flees the massacre."
    nar "The survivor is captured and executed for desertion."
    nar "A bitch gives birth to six pups, later they are given to the children of the Nobles in the north."
    nar "The royal family of the south and the king are introduced into the story."
    nar "The right hand of the south king suddenly dies."
    nar "South King travels North with intention of marrying his son to a Northmen noble."
    nar "Children of the Northmen Nobles send their mother a letter pertaining the sudden demise of the King's right hand."
    nar "The mother believes Southmen plot against the South King."
    nar "South King and his family arrive at the capital of the Northmen."
    nar "South Queen is having sex with her own brother. A little boy is traumatised for life after catching them in the act."
    nar "The little boy is traumatised further after attempted child murder takes place. The kid barely survives and is now in a coma."
    nar "A new family from across the sea is introduced into the story."
    nar "The exiled prince from across the sea plans to forcefully trade his sister in exchange for the army from the local barbarians."
    nar "The child-murdering, sister-fucker brags about killing the previous South King, earning himself a king-slayer title."
    nar "The sister of the exiled prince from across the sea is given three ostrich-like eggs as a wedding gift."
    nar "Noble Northman is appointed the new right hand of the South King."
    nar "Child-murdering, king-slaying, sister-fucker sends an assassin to finish the job, but the mother and his dog kill off the attacker."
    nar "The mother is not amused and suspects the Southmen are at fault."
    nar "Noble Northman sends off his bastard son to serve as a Watchman up North for the rest of his days."
    nar "He's also forced to take a vow of chastity."

    gen "Damn. Serving someone for eternity is one thing, but not being able to fuck is just cruel." ("base", xpos="far_left", ypos="head")

    nar "The bastard gives his tomboy sister a sword the size of a needle."
    nar "A dwarf is introduced into the story."
    nar "South Queen's oldest son, The Bratty Prince, kills a Northmen Commoner and threatens to kill Noble Northmen tomboy."
    nar "Tomboy's overgrown dog bites the Bratty Prince."
    nar "South Queen demands the dog to be killed, but Tomboy releases it to the wild."
    nar "South Queen demands tomboy's sister dog is killed instead."
    nar "The very traumatised boy wakes up from comma and learns that he will be crippled for life, deepening his trauma."
    nar "In the meantime the exiled princess from across the sea friendzones a disgraced knight. Then she gets raped by her newly wed barbarous husband."
    nar "South king laments about his debt issues."
    nar "Mother of the traumatised child plans on telling her husband about the ordeal but is stopped when she meets her old friend with a peculiar nickname, Littletoe."

    gen "*He-he-he*" ("grin", xpos="far_left", ypos="head")

    nar "The virgin bastard struggles to find his place among Watchmen."
    nar "The exiled princess is now pregnant and experiences a Stockholm syndrome."
    nar "The princess threatens her brother."
    nar "The dwarf brother of the king-slayer gives a horse saddle to the crippled boy his brother tried to kill."
    nar "The new right hand of the South King investigates the demise of his predecessor, finding that his king has a bastard child."
    nar "A tournament takes place."
    nar "The Bastard Virgin befriends a certain chubby Watchman."
    nar "Across the sea, the exiled prince has a fight with his sister."
    nar "One of the Noble Northwomen daydreams about becoming a queen while her tomboy sister dreams of becoming a boy."
    nar "Crippled boy's mother plans to arrest the dwarf because she believes he's responsible for the traumatic experiences of her child."
    nar "A man with no balls is introduced into the story. He turns out to be a spy of the South King."
    nar "South king learns that the exiled princess is pregnant and plans killing her, but his advisor talks him out of it."
    nar "Right hand of the South King hands in his resignation, angering the king."
    nar "Queen's brother, the sister-fucker, learns that their dwarf brother is being kept captive by the mother of the child they tried murdering."
    nar "Sister-fucker wounds the king's advisor who just resigned."
    nar "The king rips the letter of resignation, forcing his advisor to remain."
    nar "Some execution takes place."
    nar "King's advisor discovers that two sons of the king are not his."
    nar "The traumatised boy learns how to ride a horse, but is attacked by North-Northmen."
    nar "Noble Northmen rally the lands of the king who's fallen to the rebels, rescue him and enslave a random North-Northwoman."
    nar "The dwarf bargains his life for freedom through a fair trial."
    nar "The dwarf and the mother appoint their fighters, the dwarf's fighter wins."

    gen "*Gah* Nobles.. Always asking someone else to do their bidding." ("base", xpos="far_left", ypos="head")

    nar "The exiled prince grows inpatient waiting for his barbarous troops and threatens to kill his sister's barbarous unborn child."
    nar "His sister's newly wed husband kills him by pouring molten gold on his head."

    gen "*heh* That's just golden." ("base", xpos="far_left", ypos="head")

    nar "King's advisor confronts the Queen about her incestuous love."
    nar "The king gets wounded by a boar and dies."
    nar "Dead King's advisor sends a letter to Dead King's brother, informing him about his brother's unfaithful wife."
    nar "Dead King's advisor confronts the Queen and the Bratty Prince and gets taken prisoner as a result."

    gen "It's as if he's looking to get beheaded." ("base", xpos="far_left", ypos="head")

    nar "Dead King's assassin is caught by the friendzoned knight while he was trying to poison the pregnant exiled princess from across the sea."
    nar "The barbarous soon-to-be daddy is not amused and vows to conquer them all."
    nar "The tomboy and her sister flee north but one of them gets captured."
    nar "Noble Northmen prepare the armies in attempt to free their sister."
    nar "The traumatised, crippled boy is left behind to rule the North."
    nar "Mother of the traumatised boy visits her sister and her milk-drinker of a son."
    nar "The dwarf while heading back South is captured by the local tribesmen."
    nar "Watchmen discover how half-frozen undead are born."
    nar "Barbarous soon-to-be daddy does barbarous things but gets wounded in the process."
    nar "Bratty prince appoints his grandpa as new King's Advisor."
    nar "Daughter of the Dead King's Imprisoned Advisor begs the Bratty Prince for the life of her father."
    nar "An entire nation of Seamen is introduced into the story."
    nar "Mother of the crippled boy asks Seamen for help, in exchange offers her two daughters."
    nar "The virgin bastard receives praise for his service and is given a steel sword."
    nar "Barbarian husband is on the brink of death, his wife tries some slave magic to save him."
    nar "The wife goes into labour and is being assisted by her friendzoned knight."
    nar "A lot of Northmen die in a fight with the Southmen, and the king-slayer gets captured by Northmen."
    nar "Northmen plan to trade the sister-fucker for their people, but South Queen turns them down."
    nar "Dead King's Imprisoned Advisor swears loyalty to the Bratty Prince, hoping to not lose his head."

    gen "Finally the man has seen reason." ("base", xpos="far_left", ypos="head")

    nar "He gets beheaded anyway and his children are forced to watch."

    gen "Well, fuck." ("base", xpos="far_left", ypos="head")

    nar "Northmen rebel against other kingdoms and proclaim independence. Headless man's son is appointed as King of the North."
    nar "Usurpers fight over the South Throne."
    nar "King's Advisor appoints his son, the dwarf as the new advisor."
    nar "The virgin bastard attempts escaping from the Watchmen but his virgin brothers convince him to stay."
    nar "The tomboy escapes the South Kingdom disguised as a boy."

    gen "Surprise, surprise..." ("base", xpos="far_left", ypos="head")

    nar "The Bratty Prince plans on marrying the daughter of the man he just executed."
    nar "Exiled princess gives birth, but her child is born deformed and dead. The slave magic backfired, leaving her husband in a vegetative state."
    nar "She decides to end her husband's life."
    nar "A funeral pyre is prepared, the princess hides her three ostrich-sized eggs inside."
    nar "The witch is captured by barbarians and placed on the funeral pyre alive and set afire."
    nar "Despite the pleas of the friendzoned knight, the mourning wife walks into the flames herself."
    nar "When the embers die the following morning, the princess is found in the ashes, unharmed, flanked by three newly-hatched baby dragons."
    nar "Friendzoned knight and other barbarians pay tribute to their new Queen of Dragons."
    nar "\"This is the way.\" They say unanimously."

    nar "The end."

    call book_end

    gen "The author of this book has some serious issues." ("base", xpos="far_left", ypos="head")
    gen "I wonder if it's even worth picking up the continuation..." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        jump night_start
    else:
        jump day_start

label game_of_chairs2_book:
    call book_start

    nar "A very hot sorceress is introduced into the story."
    nar "The brother of the South King murdered by a boar, The Usurper King, is planning to take the South Throne for himself, with the help of his sexy sorceress."
    nar "The Bratty Prince wants all bastard sons of his father dead, unbeknown of his own bastardly blood."
    nar "The King of the North offers peace to the Southmen in exchange for legal independence and his sisters' safety."
    nar "The King of the North sends his mum and his friend to seek alliance with another royal usurper."
    nar "Some Watchmen take shelter in a house whose owner is having sexual relationship with his many daughters."
    nar "Virgin Watchmen are unamused."
    nar "Newly titled Queen of Dragons struggles keeping her people fed and alive."
    nar "North King's friend reaches the kingdom of Seamen."
    nar "North King's friend is finally reunited with his father and sister."
    nar "The father shames his son by saying he's not worthy of being called a Seaman any more."
    nar "South Queen rejects the peace treaty proposed by the North King and new King's Advisor, the dwarf, exiles the head of the guards to become a Watchman."
    nar "The tomboy disguised as a boy admits her true identity to a boy she likes."
    nar "Chubby Watchman is approached by one of the daughters that sleeps with her father, explaining she's afraid for her unborn child."
    nar "Chubby Watchman asks The Bastard for help, but in his virginal jealousness he refuses."
    nar "Queen of Dragons receives a severed head as a gift from an unknown party."
    nar "A servant of The Usurper King recruits a pirate fleet to aid them."
    nar "The Usurper King tries his luck in siring an heir with the hot sorceress, after his wife fails to produce a son."
    nar "The Bastard uncovers the morbid mystery of the lack of male lineage in his host's house."
    nar "Shortly after, The Bastard gets knocked out cold by the host."
    nar "North King's mum arrives at yet another usurper's camp to negotiate alliance. The usurper turns out to be recently wed."
    nar "A bad-ass female warrior is introduced into the story."
    nar "The Married Usurper refuses to consummate his marriage because he turns out to be gay."
    nar "The Gay but Married Usurper is shown banging his wife's brother in graphic details."

    gen "Poor wife." ("base", xpos="far_left", ypos="head")

    nar "Father of the North King's friend plans an attack on the Northmen with his daughter."
    nar "North King's friend decides to end the friendship by joining his father and sister's vendetta against Northmen."
    nar "The dwarf appoints his favourite whore as Headless Man's daughter handmaiden."
    nar "The Watchmen are forced to leave their shelter because the host is 'in the mood' and needs space."
    nar "When heading south to reach the North Kingdom, Watchmen are attacked by Southmen."
    nar "Someone dies. Tomboy disguised as a boy and the bastard friend she likes are taken prisoner."
    nar "North King's mum attempts to reunite all usurpers but they bicker about the throne."
    nar "Littletoe visits North King's mum and offers her daughters' lives for the sister-fucker."
    nar "Out of nowhere, the hot sorceress gives birth to a demon baby."

    gen "What the fuck?" ("base", xpos="far_left", ypos="head")

    nar "The Bratty Prince publicly abuses his betrothed and shames her dead father."
    nar "The dwarf, King's Advisor, sends two prostitutes to his chamber, in order to calm his temper."
    nar "The Bratty king makes the prostitutes brutally beat each other or be killed, but the dwarf intervenes."

    gen "How dare he! That little shit!" ("angry", xpos="far_left", ypos="head") # Genie obviously means the prince.

    nar "The dwarf discovers that his sister is having an incestuous relationship with their cousin."
    nar "The dwarf blackmails the cousin into spying on his lover."
    nar "The tomboy disguised as a boy and her friend, the bastard child of the dead king, are taken to a local torture chamber."
    nar "The grandpa of the Bratty soon-to-be King visits the torture chambers and recognizes the tomboy disguised as a boy, as just tomboy and makes her his servant."
    nar "After forty days of wandering the desert, the Queen of Dragons and her sickly barbarians find shelter at a desert city."
    nar "The Tomboy Servant frees three men from the torture chambers."
    nar "One of the rescued men promises to kill three men she fingers, the first choice is the torturer."
    nar "The hot sorceresses' demon baby kills the Usurper King's Gay Usurper brother."
    nar "Dead Gay Usurper's army decides to join the killer of their leader. Except his wife and mother-in-law."

    gen "Damn. I was not expecting that." ("base", xpos="far_left", ypos="head")

    nar "The bad-ass female warrior swears fealty to North King's mum."
    nar "North King's treacherous friend, against his sister's orders plans to capture the Northmen's Capital during the absence of the North King."
    nar "The dwarf learns that barrels filled with oil float on water and make a great water minefield."
    nar "A group of Watchmen arrives at an ancient fortress called 'Fisting of the First Men' with the intention of raiding it."
    nar "Some council member proposes marriage to the Queen of Dragons, in exchange for his wealth."
    nar "The friendzoned knight is unamused and advises her to gain the trust of the people another way."
    nar "Against South Queen's wishes, her dwarf brother sends his niece to France for safety."
    nar "North King's treacherous friend captures the Northmen's capital and executes one of his old friends."
    nar "The long ago captured North-Northwoman helps the crippled boy, his challenged servant, and his friend escape."
    nar "The Virgin Bastard captures himself a North-Northwoman but she escapes."
    nar "The Bratty soon-to-be King incites a riot in which he almost dies, and his betrothed almost gets raped."

    gen "What did he want to achieve? Stupid." ("base", xpos="far_left", ypos="head")

    nar "Bratty soon-to-be King's grandpa allows Littletoe to seek alliance abroad, in France."
    nar "An officer who suspected the Tomboy Servant's true identity now lays dead. That was her second wish."
    nar "North King receives news about his treacherous friend's doing and sends men to retake the capital."
    nar "Queen of Dragons starts building herself an Ark for the money borrowed from the wealthy noble who proposed to her."
    nar "In the meantime someone steals her dragons, making her a Queen of Stolen Dragons."
    nar "Treacherous friend is looking for brothers of the friend he betrayed and plans on killing them."
    nar "The grandpa of the Bratty soon-to-be king is looking for the killer of the officer that was recently found."
    nar "The Virgin Bastard recaptures the North-Northwoman but she escapes his clutches again, leading him to a trap."
    nar "South Queen warns her son's betrothed that she should love no one else but her own children."
    nar "Sister-fucker escapes from North King's prison but has left a trail."
    nar "Some highly regarded warlock admits to Queen of the Stolen Dragons that he stole the dragons and offers them back."
    nar "The city council gets slaughtered and the noble who proposed marriage to the Queen of Dragons is made King."
    nar "The treacherous friend burns two children of the local commoners and presents them as the brothers of the friend he betrayed."
    nar "North King learns that his own mum secretly freed the sister-fucker, escorted by the bad-ass female warrior, in order to exchange him for his sisters."
    nar "North King gives his mum house arrest."
    nar "North King seeks a medic to heal his boner. He succeeds."
    nar "Sister of the treacherous friend arrives at Northmen's Seized Capital and criticises him for it."
    nar "Grandpa of the Bratty soon-to-be King leaves the capital with his army."
    nar "The Tomboy Servant, her friend, the man that kills for her, and Hot Pie escape."

    gen "Hot pie? What?" ("base", xpos="far_left", ypos="head")

    nar "South Queen blackmails her dwarf brother by abducting one of the local whores."
    nar "The Bratty soon-to-be king ridicules the man with no balls, who happens to be his spy and plans on attacking the Usurper King."
    nar "The North-Northmen capture the Virgin Bastard and lead him to the North-North King."
    nar "The watchmen whom raided the ancient fortress find a stash full of weapons made of glass."
    nar "The friendzoned Knight accompanies the Queen of Stolen Dragons in order to retrieve the stolen dragons."
    nar "The Usurper's king fleet attacks Southmen's Capital."
    nar "The betrothed of the bratty soon-to-be king convinces him to lead the defence forces, hoping he gets killed."
    nar "The Bratty soon-to-be King chickens out."

    gen "Well. I can't blame her for trying." ("base", xpos="far_left", ypos="head")

    nar "The dwarf takes over the forces and leads the defense."
    nar "The oil barrel minefield turns out to be very effective."
    nar "One of the defence leaders calls the Bratty soon-to-be King a coward and resigns."
    nar "The Usurper's forces rally the castle, the Bratty, cowardly soon-to-be King holds on his mum's skirt in fear."
    nar "South Queen takes her other, younger son, and plans to kill him to save him from being captured."

    gen "What was it again? 'Love her children more than anything' she said *huh*?" ("base", xpos="far_left", ypos="head")

    nar "The whore handmaiden of cowardly soon-to-be king's betrothed and the betrothed herself hide in the castle."
    nar "A rather ugly Southman soldier offers to take the girl home, but she refuses."
    nar "The dwarf lies wounded. Cowardly soon-to-be king's grandpa comes to the rescue, forcing the usurper king to retreat."
    nar "The Cowardly soon-to-be King decides that he's bored of his betrothed, breaking their engagement as he plans to marry one of the French girls."
    nar "The dwarf is worried for his whores when his father is appointed as King's Advisor again."
    nar "The Usurper King is being comforted by the hot sorceress."
    nar "The bad-ass female warrior protects the sister-fucker from his demise."
    nar "North King's mum fails to talk her son out of marrying one of the local girls."
    nar "The Queen of Stolen Dragons gets high and sees her dead husband and her dead child."
    nar "One of the dragons had a gastric reflux and burnt the warlock. The warlock and the noble were planning on betraying her anyway. The noble is locked up."
    nar "Treacherous friend of the North King demands his men to bring the fight to the North King, so they knock him out cold."
    nar "Northmen's Capitol is burnt to the ground."
    nar "After the Tomboy, her friend, the man who kills for her, and Hot Pie escape..."

    gen "This Hot Pie again...?" ("base", xpos="far_left", ypos="head")

    nar "...The tomboy is given a worthless coin by the killer, that will allow her to be led to him."
    nar "Before the man departs, his face magically changes to the face of another man."
    nar "The Virgin Bastard is forced to kill one of his friends to prove himself to the North-Northmen."
    nar "An army of half-frozen undead surrounds the ancient fortress named 'Fisting of the First Men'."
    nar "The chubby watchman pisses himself as he sees them pass."
    nar "The end."

    call book_end

    gen "There's so much going on I don't even know how to describe it all." ("base", xpos="far_left", ypos="head")
    gen "I doubt that's the last book in the series though." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        jump night_start
    else:
        jump day_start

label game_of_chairs3_book:
    call book_start

    nar "A massacre takes place."
    nar "Chubby Watchman and the rest of his friends that survived the attack of the half-frozen undead decide to retreat."
    nar "After his imprisonment, The Virgin bastard decides to switch sides and joins North-Northmen."
    nar "Littletoe offers the dwarf's betrothed to return her to her lands but she again refuses."
    nar "The Usurper King's servant tries to kill the hot sorceress and gets imprisoned."
    nar "Queen of Dragons plans to expand her army."
    nar "South Queen's brother and his bad-ass female warrior companion travel south but get captured by Seamen."
    nar "A funeral takes place."
    nar "The Tomboy disguised as a boy, her friend and Hot Pie rest at a local inn."
    nar "Burnt-faced man discovers the identity of the tomboy disguised as a boy."
    nar "Dwarf's betrothed gossips about the Bratty soon-to-be King with his soon-to-be mother-in-law."
    nar "Treacherous friend gets tortured by unknown captors."
    nar "The cripple, his challenged servant and North-Northwoman encounter other children nobles."
    nar "One of the noble children tells the cripple that he can enter the minds of animals."
    nar "Littletoe is sent with the intention that he marry milk-drinker's mum."
    nar "Hot Pie is employed by the Inn. The tomboy disguised as a boy and her friend split up with Hot Pie."

    gen "I still have no damn clue who that Hot Pie is, but I'm happy for them. I guess." ("base", xpos="far_left", ypos="head")

    nar "The Virgin Bastard plans on attacking the Watchmen with North-Northmen."
    nar "The North-Northwoman stolen by the chubby watchman is carrying a child of her own father and soon enough gives birth."
    nar "The Treacherous Friend is being freed by an unknown man."
    nar "Hot sorceress travels south, looking for more royal blood."

    gen "She must be thirsty." ("base", xpos="far_left", ypos="head")

    nar "Queen of Dragons wants to trade one of her dragons for 8,000 eunuchs and an interpreter."
    nar "Sister-fucker bets his right hand that his travel companion won't get raped by their captors."
    nar "She's safe, but sister-fucker loses a hand anyway, earning himself a new title."
    nar "The Treacherous Friend's rescuer betrays him, puts him in a cell and starts torturing him again."
    nar "One-handed Sister-fucker child-murdering king-slayer and his bad-ass female warrior companion try escaping but fail."
    nar "A man with no balls tells the dwarf a story how he lost his jewels."
    nar "Watchmen are at war with Watchmen."
    nar "A chubby watchman decides to adopt the North-Northwoman's incest child and flee south with them."
    nar "The tomboy disguised as a boy and her friend are taken to a cave by the brotherhood."
    nar "Dwarf's betrothed is given a proposition to marry another man but it turns out the man is gay, and French."
    nar "Queen of Dragons after acquiring her eunuch army, tricks the slavers she traded with and kills them."
    nar "One of the eunuchs is appointed as leader of the eunuch army."
    nar "The Dwarf is concerned about his family's financial debts."
    nar "The dwarf discovers that his betrothed is planning to marry a gay man, so he sets his sister -- The Queen -- to marry the gay man instead."
    nar "Dwarf's betrothed tells Littletoe that she wants to remain in South Kingdom and asks for a green card."
    nar "The father of the dwarf discovers that his son's betrothed was planning to marry the gay French man."
    nar "The Usurper King tells his wife he's been unfaithful to her. She tells him that she's happy for him."
    nar "The Usurper King's daughter teaches his attempted-murderer of a servant how to read."
    nar "In the caves of the brotherhood, two people have a duel to death, one of them dies."
    nar "The man that died during the duel is resurrected."

    gen "Bloody cheater." ("base", xpos="far_left", ypos="head")

    nar "When sister-fucker and his bad-ass companion reach the city of Seamen, he brags about how he killed the previous-previous South King with one hand."
    nar "North King gets bored and executes some of his men."
    nar "The Virgin Bastard is seduced by the woman he was chasing all this time."
    nar "The Bastard is no longer a virgin."
    nar "The grandpa of the Bratty soon-to-be King coerces future mother-in-law to marry The Queen, his daughter, to mother-in-law's son."
    nar "The dwarf informs his betrothed and her whore of a handmaiden that they're now engaged. She acts surprised."
    nar "South Queen tells her dwarf brother, that her son was hoping to see him dead during the last siege."
    nar "Littletoe tells the man with no balls about the dead informant that the Bratty soon-to-be King has killed."
    nar "The hot sorceress stops by the brotherhood and decides to buy herself a young boy, who happens to be tomboy's friend."
    nar "North King tries to reconcile with the Seamen."
    nar "Treacherous Tortured Friend is still being tortured."
    nar "A cripple starts looking for a multi-eyed bird."
    nar "The no-longer-a-virgin bastard is still with the North-Northwoman, their loud relationship angers the locals."
    nar "Treacherous Tortured Friend gets gelded, losing his family jewels in the process."

    gen "That's fucked up man..." ("base", xpos="far_left", ypos="head")

    nar "The tomboy escapes the brotherhood but is captured in the process."
    nar "Hot sorceress tells tomboy's friend that he is a son of the king who was killed by a boar."
    nar "The handmaiden whore threatens the dwarf that their relationship will end if he marries his betrothed."
    nar "The bratty soon-to-be king and his Grandpa joke about rumoured Queen of Dragons."
    nar "Queen of Dragons sieges another city."
    nar "One-handed sister-fucker waves goodbye after attending an unimportant wedding ceremony."
    nar "Bad-ass female warrior is fighting in a pit, one-handed sister-fucker decides to lend her a hand."
    nar "The dwarf and his betrothed get married."
    nar "Father of the dwarf demands he sire an heir, and soon, but the dwarf's new wife has a permanent migraine."
    nar "The captured tomboy is prepared to be sold to her brother for ransom."
    nar "The attempted-murderer of a servant is let free."
    nar "Hot sorceress seduces her boy-toy and puts leeches on him to suck out his royal blood."

    gen "First birthing demons now sucking some poor boy, and not in the fun way. That bitch is out of her mind." ("base", xpos="far_left", ypos="head")

    nar "The Usurper King throws the leeches into the fire and curses other usurpers."
    nar "Queen of Dragons seduces the enemy's lieutenant, making him switch sides."
    nar "Chubby Watchman, his step-son and his lover get attacked by half-frozen undead."
    nar "Chubby Watchman trips over and stabs the half-frozen undead with a glass dagger and kills it. They flee back north."
    nar "Meanwhile the crippled boy has learnt magic and decides to practice it on his challenged servant."
    nar "The bastard refuses to kill an innocent man, but his girlfriend has no such moral dilemmas."
    nar "The bastard is being labelled a coward and is forced to flee, with the help of his step-brother's overgrown dog."
    nar "His girlfriend becomes his ex-girlfriend."
    nar "Queen of Dragons infiltrates the city, asking the slaves she's found to join her, which they do."
    nar "North King once again tries to reconcile with the Seamen."
    nar "Seamen in return kill his mother, his friends and finally they kill him too."
    nar "Dead North King's sister appears at the time of the massacre but is rescued to safety by a man with burnt face."
    nar "Seamen are rewarded by the South Queen for killing the North King."
    nar "The now Gelded, Tortured, Treacherous friend learns that his own men traded him for a free passage."

    gen "Balls. It's almost as if the book author had a personal vendetta against that poor guy..." ("base", xpos="far_left", ypos="head")

    nar "Sister of the Gelded, Tortured, Treacherous friend plans on freeing her brother."
    nar "The tomboy and her burnt-faced rescuer go rampage."
    nar "The one-handed sister-fucker is finally reunited with his Queen. They shake hands."
    nar "Chubby Watchman and his family meet the now magically fluent crippled boy and his companions."
    nar "The family decides to give them their glass weapon."
    nar "Chubby Watchman warns other kingdoms about half-frozen undead."
    nar "The Bastard's ex-girlfriend finds him and shoots him three times with an arrow at point-blank range."

    gen "Shouldn't have put your dick in crazy." ("base", xpos="far_left", ypos="head")

    nar "The Bastard says it's just a flesh wound and walks it off."

    gen "Right..." ("base", xpos="far_left", ypos="head")

    nar "The attempted-murderer of a servant tries freeing the hot sorceresses boy-toy to prevent him from being sucked to death."
    nar "Queen of Dragons wins the battle and basks in her glory."
    nar "The end."

    call book_end

    gen "I don't know what's with the frequent mentions of balls removal, tortures, and death but colour me morbidly curious." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        jump night_start
    else:
        jump day_start

label quidditch_guide_book:
    call book_start

    nar "Quidditch - One of the most popular sports in the wizarding world is a team based sport played on broomsticks..."
    nar "Two opposing teams with seven people making up each team go up against each other..."
    nar "The game is played using four balls... One quaffle, two bludgers and one snitch.\nThe beginning of the match is signalled by the quaffle being thrown into the air by the referee..."
    nar "Quidditch, unlike many other sports is played on an oval shaped pitch with a scoring area on each end..."
    nar "Much like other sports, you're not allowed to go outside the boundary lines with the quaffle or you'd have to hand it over to the opposing team..."
    nar "When the game is set in motion each player takes their assigned positions.\nThere's three chasers, two beaters, one keeper and one seeker..."
    nar "The chasers purpose is to score the Quaffle. Beaters on the other hand is to hit them with the bludgers as to knock the ball out of their grasp... The keeper blocks the goal and the seeker needs to catch the snitch."
    nar "As most injuries are easily remedied through magical means there's nothing to stop a player from knocking into one another as to get a hold of the Quaffle. Distraction tactics are also common even during official matches..."
    nar "The way scoring is done is when the chaser has a hold of the quaffle they need to get to the opponent's side of the pitch and score it by getting it through a hoop..."
    nar "The winning team is decided once the snitch is caught which is worth 150 points to the team of which seeker caught it. Therefore a match could technically go on forever... The longest Quidditch match went on for about 3 months..."

    call book_end

    if quidditchguide_ITEM.used:
        gen "I already knew all of that nonsense..." ("base", xpos="far_left", ypos="head")
    else:
        gen "Bludgers and quaffles?" ("base", xpos="far_left", ypos="head")
        gen "This is even more stupid than I imagined." ("base", xpos="far_left", ypos="head")

    $ quidditchguide_ITEM.used = True
    if game.daytime:
        jump night_start
    else:
        jump day_start
