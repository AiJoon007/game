

### Snape Chitchat ###

label snape_chitchat:

    if states.sna.chatted:
        return

    $ states.sna.chatted = True

    # Prior to hermione introductions
    if not states.her.unlocked:
        random:
            block:
                sna "I am starting to get worried about Albus..." ("snape_06")
                sna "I simply hope he's alright." ("snape_09")
            block:
                sna "Do you know how much longer will that spell of yours last?" ("snape_05")
                sna "I have important matters to discuss with Albus very soon..." ("snape_09")
        return

    if states.her.level >= 0 and states.her.level <= 2:
        random:
            sna "I am feeling rather doubtful about our whole plan again..." ("snape_06")

            block:
                sna "Do you really think you can do this?" ("snape_24")
                sna "Do you think you can break the girl?" ("snape_25")

            block:
                if game.weather in ("rain", "blizzard"):
                    sna "Isn't the weather lovely today?" ("snape_02")
                    sna "I wish it would stay like this forever." ("snape_06")
                else:
                    sna "Don't you just hate this wretched sunny weather?" ("snape_01")
                    sna "I wish it would rain every day." ("snape_06")

            block:
                sna "Are you sure that you are not Albus Dumbledore?" ("snape_05")
                sna "I'm still having a hard time believing this whole thing sometimes..."

            block:
                sna "I killed a pupil once." ("snape_01")
                sna "Yes... I strangled the maggot with my bare hands." ("snape_02")
                sna "........ *Low growl*." ("snape_03")
                sna "Did that sound believable?" ("snape_05")
                sna "The moment those animals stop fearing me, I'm done for." ("snape_06")
                sna "Cultivating fear in the hearts of your students is the most important task for every teacher." ("snape_26")

            block:
                sna "Those Weasley maggots..." ("snape_04")
                sna "One of these days I'll just snap, I swear." ("snape_07")

            block:
                sna "Don't you think that owl post is a bit ridiculous?" ("snape_05")
                sna "I'd much rather use ravens."

            block:
                sna "I'm having the worst day of my life..." ("snape_06")
                sna "So I'm really Not in the mood for chit-chats..."

            block:
                sna "Being a wizard is a twenty-four hours a day..." ("snape_04")
                sna "Seven days a week..." ("snape_03")
                sna "Three hundred and sixty-five days a year occupation." ("snape_04")
                sna "Not even a single holiday..."

            block:
                sna "Quidditch..." ("snape_04")
                sna "What a waste of time and resources!" ("snape_10")
                sna "" ("snape_04")


    if states.her.level >= 3 and states.her.level <= 5:
        random:
            block:
                sna "I have yet to notice any changes in Miss Granger's behaviour..." ("snape_24")
                sna "Are you sure that you know what you're doing?" ("snape_05")
                sna "" ("snape_09")

            block:
                sna "It sure feels good to be able to grant house points or take them away whenever I feel like it." ("snape_24")
                sna "My authority among the students is growing every day..." ("snape_24")
                sna "And when I say \"authority\" I mean \"fear\"." ("snape_02")

            block:
                sna "Did you know that the full moon is known to boost male potency?" ("snape_24")
                sna "It also makes it easier to focus on a task at hand, making you more proactive." ("snape_24")
                sna "But who gives a damn about that, am I right?" ("snape_28")
                sna "" ("snape_29")

            block:
                sna "My precious Slytherins make all of this torment worthwhile..." ("snape_06")
                sna "Their skirts are getting shorter every week, I swear." ("snape_19")

            block:
                sna "There was a time when I was young and full of hope..." ("snape_06")
                sna "*Ha-hah*... I'm pulling your leg, mate." ("snape_28")
                sna "I was never full of hope..." ("snape_29")

            block:
                sna "Someone broke into my personal storage..." ("snape_16")
                sna "They only took some Gillyweed... Lucky they didn't take any of my amorentia." ("snape_29")
                sna "Not that I need or use such things." ("snape_09")

            block:
                sna "A \"Men's rights movement\"...?" ("snape_05")
                sna "What's next? A house elves' rights movement?" ("snape_04")
                sna "How could a top student be that dumb?" ("snape_06")

            block:
                sna "I don't play favourites with my students." ("snape_05")
                sna "I merely tolerate some of them and hate the rest." ("snape_04")

            block:
                sna "There are four student houses at Hogwarts..." ("snape_24")
                sna "Slytherin, Ravenclaw, Gryffindor, and..."
                sna "... and Huff-something..." ("snape_05")
                sna "No one really cares." ("snape_29")
                sna "" ("snape_09")

            block:
                sna "Brooms are for kids and witches." ("snape_24")
                sna "You'll never see a self-respecting wizard prancing around on a broomstick." ("snape_05")
                sna "" ("snape_09")


    if states.her.level >= 6 and states.her.level <= 8:
        random:
            block:
                sna "Any progress on breaking our little ms. know-it-all?" ("snape_24")
                sna "" ("snape_09")

            block:
                sna "The other day this one girl sold me her panties for five house points." ("snape_24")
                sna "And man, was she excited about that..." ("snape_14")
                sna "I think she would've given them away for free just to please me." ("snape_19")
                sna "" ("snape_09")

            block:
                sna "I'm having a rather pleasant day so far..." ("snape_23")
                sna "Bet you didn't expect to hear me saying that?" ("snape_02")

            block:
                sna "Quidditch seems to steadily gain more and more popularity over the years..." ("snape_24")
                sna "How disappointing..." ("snape_04")

            block:
                sna "My life was incredibly dull before your arrival..." ("snape_24")
                sna "Nowadays it's..." ("snape_05")
                sna "... less dull." ("snape_02")

            block:
                sna "Regrets? I don't know the meaning of the word!" ("snape_05")
                sna "I live a very fulfilling life." ("snape_06")
                sna "*Ha-ha-ha*! I'm sorry, I just can't say such nonsense with a straight face." ("snape_28")
                sna "" ("snape_26")

            block:
                sna "There is no room for mistakes during class." ("snape_24")
                sna "One slip-up and the bloody bastards will tear you to shreds." ("snape_04")

            block:
                sna "You are the only person I have to answer to..." ("snape_04")
                sna "So I can almost literally do whatever the bloody hell I want these days..." ("snape_05")
                sna "..............." ("snape_09")
                sna "So that's what freedom feels like, *huh*?" ("snape_06")

            block:
                sna "Autumn... The most depressing time of the year..." ("snape_06")
                sna "I Love it!" ("snape_02")
                sna "" ("snape_23")

            block:
                sna "I have a magical portrait of a stripper hanging in my room." ("snape_24")
                sna "One of my most precious possessions." ("snape_22")
                sna "" ("snape_09")


    if states.her.level >= 9 and states.her.level <= 11:
        random:
            block:
                sna "Miss Granger has gotten aggressive lately, almost to the point of open hostility..." ("snape_24")
                sna "I hope you know what you're doing..." ("snape_05")
                sna "" ("snape_09")

            block:
                sna "I shouldn't feel bad about having sex with my students, right?" ("snape_26")
                sna "I mean, you should see the way some of those girls wear their uniforms..." ("snape_05")
                sna "They're practically asking for it." ("snape_13")
                sna "" ("snape_12")

            block:
                sna "It's been raining a lot lately..." ("snape_23")
                sna "I wonder if I enjoy rainy weather so much simply because it makes most people miserable..." ("snape_02")
                sna "" ("snape_23")

            block:
                sna "According to a recent study, nine out of ten girls secretly fantasise about being abused by their teacher." ("snape_24")
                sna "I bet that tenth girl was Hermione Granger." ("snape_03")
                sna "" ("snape_01")

            block:
                sna "These days I have to actually make an effort to maintain my usual bad mood." ("snape_24")
                sna "" ("snape_23")

            block:
                sna "Do you have a few condoms to spare?" ("snape_24")
                sna "I have a whole pack, but..." ("snape_25")
                sna "... they've expired years ago..." ("snape_06")
                sna "The changes you've brought into my life, mate." ("snape_02")
                sna "" ("snape_23")

            block:
                sna "You think we could turn Hogwarts into a \"girls only\" school?" ("snape_24")
                sna "Hogwarts Girls Academy!" ("snape_23")
                sna "Now that would make this institution bloody perfect... If it wasn't for Lockhart." ("snape_13")

            block:
                sna "Why did the teacher cross the road?" ("snape_24")
                sna "To get away from his students!" ("snape_25")
                sna "*Ha-ha-ha*! Gets me every time!" ("snape_28")
                sna "" ("snape_25")

            block:
                sna "Want to hear a funny story?" ("snape_24")
                sna "Well, I don't know any..." ("snape_06")

            block:
                sna "Do you know what a \"royal goblet\" is?" ("snape_05")
                sna "You do, don't you?" ("snape_13")
                sna "" ("snape_23")


    if states.her.level >= 12 and states.her.level <= 14:
        random:
            block:
                sna "Fifteen points for a blowjob is a fair price, right?" ("snape_24")
                sna "" ("snape_23")

            block:
                sna "Have you ever been in love, mate?" ("snape_24")
                sna "Have you ever been in love with a schoolgirl?" ("snape_02")
                sna "What about half a dozen of them at once?" ("snape_22")
                sna "" ("snape_20")

            block:
                sna "Something rather brilliant happened last night between me and this Slytherin minx." ("snape_20")
                sna "Long story short, all of my muscles ache, and I still feel rather dehydrated..." ("snape_22")
                sna "" ("snape_13")

            block:
                sna "It's getting colder lately..." ("snape_24")
                sna "Winter is coming..." ("snape_23")

            block:
                sna "Have you ever seen muggle women dressed as witches?" ("snape_24")
                sna "So adorable." ("snape_19")

            block:
                sna "Do you know what an \"Internet\" is?" ("snape_24")
                sna "Apparently it allows you to go \"on the line\" and see magical photographs of naked muggle women." ("snape_02") # SNAPE SAYS "ON THE LINE" ON PURPOSE. I KNOW THAT WAS REALLY OBVIOUS MAESTRO
                sna "Kind of makes me wish we had one here in Hogwarts." ("snape_26")
                sna "" ("snape_09")

            block:
                sna "I have two major passions in life..." ("snape_24")
                sna "Dark arts..."
                sna "......" ("snape_12")
                sna "... and sluts." ("snape_13")

            block:
                sna "You think I ought to cut down on my drinking?" ("snape_24")
                sna "But my life is so stressful..." ("snape_06")
                sna "*Hmm*..." ("snape_09")
                sna "I'll try and cut down on the liquor..." ("snape_06")
                sna "In favour of sweaty monkey-sex with my students!" ("snape_21")
                sna "" ("snape_19")

            block:
                sna "Miss Granger has been suspiciously quiet lately..." ("snape_24")
                sna "I bet she is scheming something..." ("snape_03")
                sna "" ("snape_01")

            block:
                sna "It's quite easy to write a book and kill off half of the main characters for the sake of dramatic impact..." ("snape_24")
                sna "To put your characters against impossible odds and let them make it out alive in a believable manner..."
                sna "Now {size=+7}that{/size} requires skill." ("snape_02")
                sna "" ("snape_23")


    if states.her.level >= 15 and states.her.level <= 17:
        random:
            block:
                sna "What if the girl is not our pet, but we are hers?" ("snape_11")
                sna "" ("snape_26")

            block:
                sna "Have you heard of the \"Slug club\"?" ("snape_24")
                sna "What if I start a club of my own?" ("snape_24")
                sna "I would call it the \"Snape Club\"!" ("snape_23")
                sna "I would invite girls over, offer them some tea and muffins..." ("snape_23")
                sna "Feel them up a little..." ("snape_13")
                sna "Bloody brilliant!" ("snape_22")
                sna "" ("snape_02")

            block:
                sna "Tell me Genie... Have you ever had your asshole licked clean by a witch?" ("snape_02")
                sna "A life-changing experience, neither less nor more..." ("snape_21")
                sna "" ("snape_02")

            block:
                sna "So, how is the training going?" ("snape_24")
                sna "All according to plan I hope?" ("snape_24")
                sna "" ("snape_05")

            block:
                sna "I can see the thestrals, you know..." ("snape_06")
                sna "" ("snape_09")

            block:
                sna "You know what I like about Quidditch?" ("snape_24")
                sna "Nothing! Not a single bloody thing!" ("snape_15")
                sna "" ("snape_16")

            block:
                sna "Hogwarts benefited greatly from your arrival." ("snape_24")
                sna "And when I say \"Hogwarts\", I mean \"me\"." ("snape_02")
                sna "" ("snape_23")

            block:
                sna "Real wizards wear black." ("snape_24")
                sna "Am I right?" ("snape_02")
                sna "" ("snape_23")

            block:
                sna "Some of those Slytherin girls simply adore me these days..." ("snape_24")
                sna "Personally, I'd much rather be feared..." ("snape_05")
                sna "But I am willing to settle for mindless adoration..." ("snape_23")

            block:
                sna "You are being way too generous with those Gryffindor points, mate." ("snape_24")
                sna "Lately I can barely keep up with you..." ("snape_25")
                sna "" ("snape_29")


    if states.her.level >= 18 and states.her.level <= 20:
        random:
            block:
                sna "Miss Granger really is changing... I can see it clearly now..." ("snape_24")
                sna "Her grades went down, and even her attendance is far from perfect now..." ("snape_24")
                sna "But despite that she continues to excel at being a pain in my arse!" ("snape_10")
                sna "" ("snape_01")

            block:
                sna "My least favourite colour?" ("snape_05")
                sna "Let me give you two: red and gold." ("snape_07")
                sna "" ("snape_04")

            block:
                sna "I hear the vampire theme is quite popular among the girls lately." ("snape_24")
                sna "I would make a great vampire, don't you think?" ("snape_05")
                sna "Maybe I should buy a couple of those fake fangs..." ("snape_05")
                sna "Just to drive the horny, little sluts completely crazy." ("snape_21")
                sna "" ("snape_02")

            block:
                sna "I... hate my life." ("snape_24")
                sna "No, wait, let me try this again..." ("snape_16")
                sna "I... hate my life." ("snape_17")
                sna "Dammit! I'm trying to say \"love\" but it just won't come out..." ("snape_25")
                sna "I don't think I've ever used the words \"love\" and \"life\" in one sentence before." ("snape_29")
                sna "Let me try this again..." ("snape_06")
                sna "I ha...{w} lo... {w}love my life!" ("snape_10")
                sna "There you go, I love my life..." ("snape_23")

            block:
                sna "Sunlight, chocolate, Quidditch, cats, and orange juice..." ("snape_01")
                sna "That's a list of things I don't care for..." ("snape_01")
                sna "Here is a short list of things I do care for a great deal..." ("snape_02")
                sna "The dark arts, wine, and pussy." ("snape_23")

            block:
                sna "Have you ever seen two wizards in a fistfight?" ("snape_02")
                sna "Bloody hilarious!" ("snape_28")
                sna "" ("snape_23")

            block:
                sna "You know that feeling when you come into a girl's mouth, and she swallows and says: \"Thank you, professor\"?" ("snape_14")
                sna "Isn't that the best?" ("snape_13")
                sna "" ("snape_23")

            block:
                sna "Do you think the Hogwarts ghosts sometimes spy on girls when they are taking a shower?" ("snape_24")
                sna "If I were a ghost I know I would." ("snape_13")
                sna "" ("snape_23")

            block:
                sna "This one girl confessed to me that she has frequent fantasises about being abused by that squib, mister Filch." ("snape_19")
                sna "I think I could arrange that... Should I?" ("snape_14")
                sna "" ("snape_02")

            block:
                sna "I used to hate my job so much..." ("snape_24")
                sna "Hate is clean, simple, and certain..." ("snape_06")
                sna "Now, don't get me wrong - I still hate it." ("snape_09")
                sna "But I also sort of love it now..." ("snape_05")
                sna "How could I not? With all that has been happening lately?"
                sna "To both cherish and hate something to an equal degree..." ("snape_06")
                sna "It's like being in love again..." ("snape_19")
                sna "" ("snape_06")


    if states.her.level >= 21:
        random:
            block:
                sna "Do you know what a \"bukkake\" is?" ("snape_24")
                sna "What about \"deep throating\"?"
                sna "And then there is also \"hate-sex\"."
                sna "Students these days, mate..." ("snape_05")
                sna "They have a special name for everything."
                sna "Although \"hate-sex\" has always been around..." ("snape_06")
                sna "Back in my days we just called it \"sex\"." ("snape_02")

            block:
                sna "I heard a mysterious ticking noise today..." ("snape_04")
                sna "It was kind of catchy..." ("snape_28")

            block:
                sna "I organised a small party the other day..." ("snape_24")
                sna "One girl and three boys..."
                sna "They fucked her and I watched..." ("snape_13")
                sna "........................." ("snape_29")
                sna "You think I've been exercising my dark side a bit too often lately?" ("snape_05")
                sna "" ("snape_06")

            block:
                sna "I'm all out of condoms, mate." ("snape_24")
                sna "You think you could hook me up?" ("snape_02")
                sna "" ("snape_01")

            block:
                sna "I am secretly making this special herbal brew that should make her tits lactate..." ("snape_24")
                sna "Pretty brilliant, *huh*?" ("snape_13")
                sna "" ("snape_23")

            block:
                sna "So, this witch has my cock in her mouth, right?" ("snape_24")
                sna "Her hot girlfriend is cleaning my asshole with her tongue..." ("snape_02")
                sna "Meanwhile, this third girl is on her knees with her mouth open, waiting for me to spit in it..."
                sna "And every time I spit, she says: \"Thank you, professor Snape\"."
                sna "That was a bloody surreal evening..." ("snape_22")
                sna "" ("snape_02")

            block:
                sna "This one girl has been begging me to urinate in her mouth for days, now..." ("snape_06")
                sna "Persistent little minx..."
                sna "Should I give in?" ("snape_05")
                sna "" ("snape_23")

            block:
                sna "I mercilessly dominate both male and female students..." ("snape_04")
                sna "But in very different ways." ("snape_22")
                sna "" ("snape_23")

            block:
                sna "I love my life!" ("snape_23")
                sna "Still hate my job though..." ("snape_16")
                sna "I wish I could skip all the teaching, but keep all the fucking." ("snape_14")
                sna "" ("snape_23")

            block:
                sna "I almost feel bad for having all the fun." ("snape_24")
                sna "Do you want me to send you up some fresh Slytherin slut?" ("snape_14")
                sna "" ("snape_23")

    return
