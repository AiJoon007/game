

### Tonks Intro ###

label tonks_intro_E1:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"
    gen "(...)" ("base", xpos="far_left", ypos="head")

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"
    gen "(Can't I even have one quiet day here?...)" ("base", xpos="far_left", ypos="head")
    gen "Who is it?" ("base", xpos="far_left", ypos="head")
    ton "It's Tonks--"
    ton "*Ugh*..."
    gen "..................." ("base", xpos="far_left", ypos="head")
    ton "I meant, Nymphadora Tonks, Sir."
    gen "(Nympho...{w=0.6} what?)" ("base", xpos="far_left", ypos="head")
    ton "Ministry of Magic, Auror division.{w=0.8} May I come in, Sir?"

    if letter_favors.read:
        gen "(Oh shit, the fuzz!!!)" ("angry", xpos="far_left", ypos="head")
        gen "(I thought they would have forgotten about those damn letters by now...)" ("base", xpos="far_left", ypos="head")
        ton "Sir, I'm here to discuss an important matter with you regarding your students."
        gen "(Governments are all the same with their bloody rules.)" ("base", xpos="far_left", ypos="head")
        ton "Sir?"
        gen "(...)" ("base", xpos="far_left", ypos="head")
    else:
        gen "(Another female?)" ("base", xpos="far_left", ypos="head")
        gen "(She sounds a bit too old to be a student...)" ("base", xpos="far_left", ypos="head")
        gen "(...)" ("base", xpos="far_left", ypos="head")

    menu:
        gen "(Should I let her in?)" ("base", xpos="far_left", ypos="head")
        "\"Please, come on in.\"":
            call bld
            gen "(Better to just let my charm play...)" ("grin", xpos="far_left", ypos="head")
        "\"Not right now.\"":
            call bld
            ton "But, Sir..."
            ton "I've travelled across half the country just to get here."
            gen "........................." ("base", xpos="far_left", ypos="head")
            ton "Via apparition, of course. It only took me a couple of seconds..."
            ton "But still, it's quite a long walk up here from Hogsmeade..."
            ton "I'd just like to get this over with. May I come in, Sir?"
            gen "(I wouldn't mind having a look at her...)" ("base", xpos="far_left", ypos="head")
            gen "(There is something special about women in uniform...)" ("base", xpos="far_left", ypos="head")
            ton "Sir?"
            gen "*Uhm* Yes, you may enter..." ("base", xpos="far_left", ypos="head")

    #Tonks walks in
    call bld("hide")
    pause.2

    play sound "sounds/door.ogg"
    call ton_chibi("stand","door","base")
    call chibi_emote("hearts", "tonks")
    with d3
    pause.5

    call chibi_emote("hide", "tonks")
    with d3
    pause.1

    call bld
    gen "*Hmm*?" ("base", xpos="far_left", ypos="head")

    call ton_walk("desk", "base")
    pause.5

    $ tonks.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")
    show CG tonks as cg zorder 17:
        pos (-1040, -35)
    with fade

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton "Thank you, Professor." ("base", "base", "base", "mid", xpos="right", ypos="base", trans=d3)

    show CG tonks as cg zorder 17:
        pos (-1040, -35)
        ease_quad 5.0 pos (-1040, -600)

    gen "(Oh shit,{w=0.1} she's hot...)"

    show CG tonks as cg zorder 17:
        zoom 1.0
        pos (-1040, -600)
        ease_quad 5.0 pos (0, 0) zoom 0.5

    ton "I apologise for arriving unannounced...{w=0.8} And a couple of days late..." ("open", "base", "base", "R")
    gen "Please, I'm glad you could make it."
    ton "I was occupied with some unfinished ministry business. Took me a lot longer to solve than I had anticipated..." ("normal", "narrow", "base", "mid")

    ton "I had quite the \"pleasant\" encounter with a group of centaurs." ("soft", "wide", "raised", "R")
    gen "Centaurs?!"
    ton @ hair horny "*Mhmm*..." ("base", "base", "base", "mid")
    ton "As usual, they ignored the boundaries of their allocated territory." ("open", "closed", "base", "mid")
    ton "I had to get them to comply with our rules, to the best of my abilities..." ("soft", "base", "base", "mid")
    gen "Is that so?..."

    menu:
        "-Start jerking off!-":
            $ states.gen.masturbating = True
            $ jerked_off_during_tonks_intro = True
            call gen_chibi("jerk_off_behind_desk")
            hide cg
            with fade

            nar "You take out your cock and start jerking off."

            gen "Tell me more!" ("grin", xpos="far_left", ypos="head")

        "-Pay attention-":
            $ states.gen.masturbating = False
            $ jerked_off_during_tonks_intro = False
            hide cg
            with fade
            gen "Tell me about it..." ("base", xpos="far_left", ypos="head")

    if states.gen.masturbating:
        ton "Oh... about the centaurs?" ("annoyed", "base", "raised", "mid")
        gen "Yes, centaurs!" ("base", xpos="far_left", ypos="head")
        gen "Half of a man, and the other half that of a horse?" ("angry", xpos="far_left", ypos="head")
        ton "Yes?" ("normal", "narrow", "raised", "mid")
        gen "With the bottom half being that of a{w=0.2}.{w=0.2}.{w=0.2}.{w=0.6} horse?!" ("base", xpos="far_left", ypos="head")
        ton "Of course, Sir." ("base", "base", "shocked", "mid")
        gen "(Sweet!)" ("grin", xpos="far_left", ypos="head")
        gen "Just wanted to check if I still knew my mythology..." ("base", xpos="far_left", ypos="head")
        gen "(And it wasn't just dudes with horse heads...)" ("angry", xpos="far_left", ypos="head")
        gen "(That would have been weird...)" ("base", xpos="far_left", ypos="head")

        ton "They are fascinating creatures, aren't they, Professor?" ("soft", "base", "base", "R", trans=dissolve)
        gen "What?{w} Oh yes, very fascinating..." ("base", xpos="far_left", ypos="head")

        nar "*Fap-Fap-Fap*!"
        gen "Don't mind me... Please continue..." ("base", xpos="far_left", ypos="head")
        gen "I'd like to hear more about the things you did with those centaurs!" ("grin", xpos="far_left", ypos="head")
        ton "I'm sorry Professor, but that's classified information." ("open", "closed", "shocked", "mid")
        ton "The Ministry would be furious if they knew I had told you!" ("upset", "wide", "raised", "mid")
        ton @ cheeks blush "(Not that I would mention any of it... They'd probably sack me on the spot for that...)" ("mad", "base", "worried", "R")
        ton "(I did the job. That's all that should matter to them...)" ("upset", "base", "base", "down")
        gen "Come on! ..." ("angry", xpos="far_left", ypos="head")
        ton "I'm sorry, Professor, but I really shouldn't!" ("open", "base", "base", "mid")
        ton "Anyway, sharing stories is not why I came here." ("normal", "base", "base", "R")
        gen "(Balls...)" ("base", xpos="far_left", ypos="head")

        # Stop Masturbating
        $ states.gen.masturbating = False
        call gen_chibi("sit_behind_desk")
        with d3
        pause.8

    else:
        ton "Of course, Sir." ("base", "base", "base", "mid")
        ton "I had to make a compelling offer, so they'd peacefully return to their assigned territory, which isn't easy..." ("open", "base", "base", "mid")
        gen "(...)" ("base", xpos="far_left", ypos="head")
        ton @ hair horny "You'd never be able to guess how I did it, it's quite the story." ("horny", "base", "base", "R")
        ton "Unfortunately, I cannot tell you...{w} Strictly confidential Ministry information..." ("soft", "base", "raised", "mid")
        gen "(Why? Did she suck them off?)" ("base", xpos="far_left", ypos="head")
        ton "Okay then, let's get this over with." ("open", "narrow", "base", "R")

    ton "Professor Dumbledore, are you aware of why the Ministry has sent me here?" ("open", "wide", "raised", "mid", trans=dissolve)

    if letter_favors.read:
        gen "More or less..." ("base", xpos="far_left", ypos="head")
        ton "We have received a letter from a Miss named \"Hermione Granger\", about the trading of... \"favours\" between staff and students at this school." ("open", "base", "base", "mid") #not sure if it's better to put miss in quotations or not. My logic is that the fact that she is a "miss" is a given, the name however is something the ministry may not know hence the quotations
        gen "Yes, she very much enjoys doing that..." ("base", xpos="far_left", ypos="head")
        ton "Trading favours?" ("soft", "base", "raised", "mid")
        gen "(I wish...)" ("base", xpos="far_left", ypos="head")
        gen "No. She enjoys writing letters...{w} lots of 'em..." ("base", xpos="far_left", ypos="head")
    else:
        gen "I can't say that I am." ("base", xpos="far_left", ypos="head")
        ton "So you haven't had any complaints from students in regard to \"favour trading\"?" ("open", "base", "raised", "mid")
        gen "(Oh, fuck...)" ("angry", xpos="far_left", ypos="head")
        gen "That depends...{w=0.3} What sort of favours are you referring to?" ("grin", xpos="far_left", ypos="head")
        ton "..." ("base", "base", "angry", "mid")
        ton "Well, we've received a letter from a Miss \"Hermione Granger\"." ("open", "base", "base", "L") #same here as line 159
        gen "Oh, good..." ("base", xpos="far_left", ypos="head")
        gen "..." ("angry", xpos="far_left", ypos="head")

    ton "I take it that you're acquainted with Miss Granger?" ("open", "base", "base", "mid")
    gen "You could say that..." ("base", xpos="far_left", ypos="head")
    ton "Fantastic! Let's get right to it then!" ("grin", "base", "base", "mid") #the second line was superfluous. You already established the point of the meeting earlier, so the reader knows what "let's get right to it" means
    gen "..." ("base", xpos="far_left", ypos="head")
    show screen blktone
    with d5
    gen "(I need to be smart about this...)" ("base", xpos="far_left", ypos="head")
    hide screen blktone
    with d5

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"I had no sexual relations with that woman!\"":
            ton "Sir?" ("upset", "wide", "shocked", "stare")
            ton "I'm sorry Professor, I wasn't accusing you of--" ("soft", "base", "worried", "downR")
            gen "I repeat, I had no sexual relations with that woman." ("base", xpos="far_left", ypos="head")
            ton "Professor! I wasn't implying that--..." ("mad", "base", "raised", "mid")
            ton "In the letter she wrote, Miss Granger never accused you of selling favours to your students..." ("mad", "base", "raised", "L")
            ton "Nonetheless, she was very persistent that certain other teachers weren't behaving as adequately..." ("soft", "base", "base", "mid")

        "\"What did she want?\"":
            ton "Miss Granger wrote about several students, most commonly girls of the Slytherin House, that were inclined to do favours for their male teachers." ("open", "base", "base", "R") #Tonks is a hogwarts graduate. Slytherin doesn't need to be in quotations, she knows what it is.
            gen "So what?" ("base", xpos="far_left", ypos="head")
            ton @ hair horny "According to her letter, those favours tend to be very...{w=0.1} \"sexual\" in nature..." ("soft", "base", "raised", "mid")

    gen "(Shit...)" ("base", xpos="far_left", ypos="head")
    ton "Professor, this is a very serious allegation, don't you agree that the ministry is under an obligation to investigate?" ("open", "wide", "raised", "mid")
    gen "..........................................{w} No?" ("base", xpos="far_left", ypos="head")
    ton "I'm sorry?" ("upset", "base", "raised", "mid")
    gen "Well, I can't say I'm very well versed in these...{w=0.8} very,{w=0.6} very rare occurrences." ("angry", xpos="far_left", ypos="head")
    gen "I was actually just about to begin my own investigation in the matter." ("base", xpos="far_left", ypos="head")
    ton "The Ministry has sent me specifically to determine if there is any truth to Miss Granger's concerns..." ("open", "base", "base", "L")
    ton "I'll be happy to look into this for you." ("soft", "base", "base", "mid")
    gen "Now, now. I wouldn't want you to waste your time with this." ("base", xpos="far_left", ypos="head")
    ton "Don't worry, Professor. {i}Investigation{/i} is in my job description." ("base", "base", "angry", "mid")
    ton "I'll just stay for a little while, just to examine these claims and question the students." ("open", "base", "base", "R")
    gen "That won't be necessary." ("base", xpos="far_left", ypos="head")
    ton "Do have some confidence in me, Professor. This is what I was trained for..." ("horny", "base", "base", "mid")
    gen "................................." ("base", xpos="far_left", ypos="head")
    ton "I've already got a room down in Hogsmeade." ("open", "base", "base", "R")
    ton "I'll be staying there, so no need to worry about accommodation." ("base", "base", "base", "mid")
    gen "Great..." ("base", xpos="far_left", ypos="head")
    ton "I shall start right away!" ("base", "happyCl", "base", "mid")
    ton "Good day, Sir." ("base", "base", "base", "mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    call bld
    gen "This can't be good..." ("base", xpos="far_left", ypos="head")

    $ states.sna.busy = True
    $ states.her.busy = True
    $ states.ton.ev.intro.e1_complete = True

    jump end_tonks_event


label tonks_intro_E2:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"
    ton "Professor, it's Tonks."
    ton "May I come in?"
    gen "(Her again...)" ("base", xpos="far_left", ypos="head")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Come in...\"":
            pass

        "\"Not now, I'm busy!\"":
            call bld
            gen "That will have to wait, I'm afraid..." ("base", xpos="far_left", ypos="head")
            ton "But Sir, I need to update you on the investigation!"
            ton "Please, hear me out, Professor!"
            ton "The students have been reluctant to even speak about the \"favour trading\" in my presence, which raises red flags." #idk I like this phrase more but that's subjective
            ton "You'd think that if those girls were innocent, they'd be telling me about it."
            gen "....................." ("base", xpos="far_left", ypos="head")
            ton "Be that as it may, I will keep pushing them till they open up to me..."
            gen "Good for you..." ("base", xpos="far_left", ypos="head")
            ton "And they will, as soon as I can get my hands on some Veritaserum!"
            ton "But Professor Snape has been very reluctant to provide me with a vial of his..."
            ton "{size=-4}Very suspicious if you ask me... Very suspicious indeed...{/size}"
            ton "Either way, it's only a matter of time until this will all be cleared up!"
            gen "Great! I can't wait to hear about it..." ("base", xpos="far_left", ypos="head")
            ton "Of course, Sir."
            ton "I'll gladly spare some of my time and tell you right now, if you don't mind."
            gen "Wait, what?" ("base", xpos="far_left", ypos="head")
            ton "I'm coming in..."
            gen "(Shit!)" ("angry", xpos="far_left", ypos="head")

    call ton_walk(action="enter", xpos="mid", ypos="base")

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton "Professor." ("soft", "base", "base", "mid", xpos="right", ypos="base", trans=dissolve)
    gen "Hey! If it isn't..." ("base", xpos="far_left", ypos="head")

    menu:
        gen "(What was her name again?...)" ("base", xpos="far_left", ypos="head")
        "\"Tonks!\"":
            pass
        "\"Nymphadora!\"":
            ton "Sir?" ("annoyed", "base", "base", "R")
            gen "What? Isn't that your name, or did I get it wrong again?" ("base", xpos="far_left", ypos="head")
            ton "I'm sorry, Sir.{w=0.3} I thought that, when I was a student here, I made it very clear that I wouldn't want to be called Nymphadora--" ("normal", "closed", "annoyed", "down")
            ton "Please, just call me Tonks, Professor." ("annoyed", "wide", "base", "mid")
            gen "Fine..." ("base", xpos="far_left", ypos="head")
        "\"Nympho-whora!\"":
            ton "What?!" ("clench", "wide", "shocked", "stare")
            ton "I'm sorry, Professor. I clearly must have misheard you..." ("disgust", "narrow", "annoyed", "down")
            ton "What did you just call me?" ("mad", "base", "angry", "mid")
            gen "*Uhm*...{w=0.5} isn't that your name?" ("base", xpos="far_left", ypos="head")
            ton "My name is \"Tonks\", Professor!" ("upset", "base", "angry", "mid")
            ton "You of all people should know this..." ("annoyed", "base", "angry", "R")
            gen ".............." ("base", xpos="far_left", ypos="head")
            gen "(Tonks...)" ("base", xpos="far_left", ypos="head")
            gen "(Still a weird fucking name...)" ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Found any evidence yet?\"":
            ton "Sadly no, Professor." ("open", "base", "base", "mid")
            gen "(Sadly...?)" ("base", xpos="far_left", ypos="head")
        "\"How's the investigation going?\"":
            pass
    ton "I haven't gotten a chance to do my job properly so far." ("upset", "base", "base", "R")
    ton "I've been rather preoccupied listening to Miss Granger's own {i}investigations{/i}..." ("open", "narrow", "base", "R")
    ton "That girl sure is something, isn't she?" ("open", "base", "raised", "mid")
    ton @ hair horny "Not that I mind listening to her." ("soft", "base", "shocked", "R")
    ton "She gave me a very long report that went well into the evening, whilst I enjoyed a glass of firewhisky..." ("open", "base", "base", "mid")
    ton "She has been very thorough in documenting all the happenings she's witnessed..." ("base", "base", "base", "mid")
    gen "I can imagine that..." ("base", xpos="far_left", ypos="head")
    ton "Anyhow... She had no proof of any illicit activities.{w} It's all just hearsay." ("open", "closed", "base", "R")
    ton @ hair horny "As much as I wish it were true..." ("horny", "closed", "base", "R")
    gen "*huh*?" ("base", xpos="far_left", ypos="head")
    ton "So I could conclude this whole business sooner, of course..." ("base", "narrow", "base", "downR")
    ton "And bring this favour trading business to an end, once, and for all." ("open", "base", "base", "mid")
    gen "Best of luck with that..." ("base", xpos="far_left", ypos="head")
    ton "Thank you, Professor." ("base", "wide", "shocked", "mid")
    ton "I really should get going.{w} Lots that needs to be taken care of." ("open", "base", "base", "R")
    gen "Don't overwork yourself..." ("base", xpos="far_left", ypos="head")
    ton "I won't Professor.{w} Have a good night." ("base", "base", "base", "mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    call bld
    gen "Shit..." ("base", xpos="far_left", ypos="head")
    gen "I better talk to Snape about this..." ("base", xpos="far_left", ypos="head")

    $ states.her.busy = True
    $ states.ton.ev.intro.e2_complete = True

    jump end_tonks_event


### Snape Hangout Event 1 ###
# You discuss Tonks and the Ministry with Snape.

label ss_he_tonks_E1:
    sna "........................." ("snape_31", ypos="head")
    sna "That bloody wench has outdone herself, once again!" ("snape_35")
    gen "Granger?" ("base", xpos="far_left", ypos="head")
    sna "Yes! She and her cursed letters!" ("snape_08")
    sna "I'm certain she was the one who informed the Ministry about our little escapades..." ("snape_16")
    sna "And now we have an Auror breathing down our necks... All thanks to that mischievous little whore!" ("snape_15")
    gen "................." ("base", xpos="far_left", ypos="head")
    sna "...................." ("snape_31")
    gen "On the subject of that Auror..." ("base", xpos="far_left", ypos="head")
    sna "Nymphadora?" ("snape_39")
    gen "Yes, the Nympho." ("base", xpos="far_left", ypos="head")
    gen "She came by the other day..." ("base", xpos="far_left", ypos="head")
    sna "What?!" ("snape_36")
    gen "Twice, actually..." ("base", xpos="far_left", ypos="head")
    sna "And you're telling me about this... now?" ("snape_32")
    sna "I'm surprised you didn't blow our cover right there and then..." ("snape_16")
    gen "What can I say... I'm very good with the ladies!" ("grin", xpos="far_left", ypos="head")
    sna "Or you are just too lucky for your own good, more likely..." ("snape_43")
    gen "That too, to a lesser extent..." ("base", xpos="far_left", ypos="head")

    if states.her.ev.intro.masturbated:

        sna "Please tell me you didn't jerk off in front of her as well..." ("snape_03")
        gen "Well..." ("base", xpos="far_left", ypos="head")
        sna "Did you?" ("snape_01")

        if jerked_off_during_tonks_intro:
            gen "No..." ("base", xpos="far_left", ypos="head")
            sna "*glares*" ("snape_04")
            gen "Yes...? But I didn't finish this time..." ("base", xpos="far_left", ypos="head")
            sna "What you mean by \"I didn't fin--" ("snape_08")
        else:
            gen "Not this time." ("base", xpos="far_left", ypos="head")

    sna "Listen, we have to be even more cautious, now that there's an Auror making her rounds..." ("snape_10")
    sna "They are the ministry's private investigators." ("snape_35")
    sna "One slip-up and they will have us locked up in no time!" ("snape_24")
    gen "\"Us?\"..." ("base", xpos="far_left", ypos="head")
    gen "What wrong did I do?" ("base", xpos="far_left", ypos="head")
    sna "You snapped the most talented, clever, and most beloved wizard that's ever lived out of existence!" ("snape_10")
    gen "Oh right...{w=0.3} Who was it again?" ("base", xpos="far_left", ypos="head")
    sna "Albus{w=0.2} Percival{w=0.2} Wulfric{w=0.2} Brian{w=0.2} Dumbledore!" ("snape_34")
    gen "..........................." ("base", xpos="far_left", ypos="head")
    gen "I thought I traded places with just one person..." ("base", xpos="far_left", ypos="head")
    sna "That {b}is{/b} one person!" ("snape_30", trans=hpunch)
    sna "It's our headmaster's full name. And it's your name now!{w} You best make sure to remember it." ("snape_34")
    gen "Yeah...{w=0.5} I'm not even going to try..." ("base", xpos="far_left", ypos="head")
    sna "Let's just hope this whole Ministry situation will solve itself..." ("snape_31")

    sna "Thankfully, out of all the people the ministry could have sent..." ("snape_06")
    sna "They brought that clumsy, good-for-nothing hufflepuff..." ("snape_35")
    sna "As long as we keep our heads down and act as if we've nothing to hide..." ("snape_03")
    sna "There will be nothing to worry about." ("snape_09")
    gen "I have my doubts about that." ("base", xpos="far_left", ypos="head")
    sna "Let her continue her little investigation. And you can be as unhelpfully helpful as usual..." ("snape_04")

    menu:
        gen "................." ("base", xpos="far_left", ypos="head")
        "{size=-2}\"That's a bit uncalled-for, don't you think?\"{/size}":
            sna "Maybe you're right." ("snape_06")
            sna "My apologies." ("snape_09")
            gen "Apologies accepted." ("base", xpos="far_left", ypos="head")

        "-Let it slide-":
            pass

    gen "So..." ("base", xpos="far_left", ypos="head")
    gen "What if she's not going to leave that easily?" ("base", xpos="far_left", ypos="head")
    gen "Can you think of any spell, or potion to help us with that?" ("base", xpos="far_left", ypos="head")
    sna "And what would this potion or spell achieve exactly?" ("snape_05")
    gen "I don't know... Send her to the shadow realm or something?" ("base", xpos="far_left", ypos="head")
    sna "What on earth..." ("snape_03")
    sna "Actually, I'd rather not know..." ("snape_06")
    sna "No, and even if there was one... we're still dealing with a trained Auror here." ("snape_01")
    sna "We should keep everything running as normal." ("snape_35")
    sna "Or as normal as can be, without the real Albus..." ("snape_09")
    gen ".................." ("base", xpos="far_left", ypos="head")
    sna "Even if she finds any concrete proof of something going on, any involvement on our part should be kept quiet at all cost." ("snape_01")
    sna "And as soon as she is out of here, I'll go back to drinking wine, whilst enjoying my students' company..." ("snape_40")
    gen "And Granger? What do you suggest we do with her?" ("base", xpos="far_left", ypos="head")
    sna "*Tzzzgh*-{w=0.6} Like that annoying brat can do any harm to us..." ("snape_25")
    sna "A girl her age would do anything for attention, is what I'd say..." ("snape_09")
    sna "Do you think some student's word would be as good as the headmaster's?" ("snape_02")
    sna "The Headmaster of the most respected educational institution in the country, no less..." ("snape_37")
    gen "I'm the headmaster of the most respected institution in the country!?!" ("angry", xpos="far_left", ypos="head")
    sna "It is also the only magical institution..." ("snape_09")
    gen "...................................." ("base", xpos="far_left", ypos="head")

    nar "You spend the remainder of the day with Snape, drenching your worries in plenty of wine..."

    $ states.sna.ev.hangouts.tonks_e1 = True
    $ ss_event_pause += 1
    $ hg_event_pause += 1

    $ chair_OBJ.hidden = False
    $ fireplace_OBJ.foreground = None

    jump end_snape_hangout_points


label tonks_intro_E3:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"

    gen "............" ("base", xpos="far_left", ypos="head")

    ton "Professor Dumbledore, may I come in?"
    gen "(It's that hot Ministry chick again...)" ("base", xpos="far_left", ypos="head")

    menu:
        "\"Yes, please come on in.\"":
            pass
        "\"Not right now.\"":
            ton "But it's urgent, Sir. I need to talk to you about Miss Granger's favour trading accusations..."
            gen "(Shit. That can't be good.)" ("angry", xpos="far_left", ypos="head")
            gen "Do you mind coming another time, I'm very busy...{w} watering the bird." ("base", xpos="far_left", ypos="head")
            ton "Watering what?"
            ton "Sir, I'm coming in."
        "\"Who is it?\"":
            ton "It's Tonks."
            gen "Who?" ("base", xpos="far_left", ypos="head")
            ton "..."
            ton "Nymphadora Tonks..."
            gen "(That {i}Nympho{/i} again...)" ("base", xpos="far_left", ypos="head")
            ton "Sir, I'm coming in."

    #Tonks enters the office
    call ton_walk(action="enter", xpos="desk", ypos="base")

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton "Professor..." ("soft", "base", "base", "mid", xpos="mid", ypos="base", trans=dissolve)
    gen "How's the investigation going? Nothing to report, I gather?" ("base", xpos="far_left", ypos="head")
    ton "On the contrary..." ("open", "wide", "shocked", "stare")
    ton @ hair angry "It's worse than I could have ever imagined!" ("open", "wide", "angry", "mid")
    gen "(........)" ("angry", xpos="far_left", ypos="head")
    ton "This school truly has changed since I was a student here." ("mad", "base", "base", "mid")
    ton "I never thought I would see Hogwarts in a state such as this..." ("open", "base", "annoyed", "down")
    ton @ hair angry "Corrupted! Right down to the core!" ("mad", "base", "angry", "mid")
    gen "(What's the matter with her hair?!)" ("angry", xpos="far_left", ypos="head")
    ton @ hair angry "You don't have to search for too long to uncover the vile debaucheries that are happening at this school..." ("open", "base", "annoyed", "mid")
    gen "(Snape, you fucking idiot! You blew it!!!)" ("angry", xpos="far_left", ypos="head")
    ton @ hair angry "Teachers taking advantage of their students, promising house points in return for sexual acts..." ("open", "base", "angry", "R") #in a sexual favour, the sex act is the favour
    ton @ hair horny "While they abuse their authority and power to do the most despicable things to them..." ("open", "base", "annoyed", "R")
    ton @ hair angry "But the Dumbledore I know would never allow such disgracefulness at his school..." ("mad", "base", "angry", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    stop music fadeout 1.0
    ton @ hair angry "I had this suspicion... Since the very day I got here..." ("open", "wide", "angry", "mid")
    # Tonks threatens Genie.
    # Maybe have her chibi point her wand at him?
    play music "music/hitman.ogg" fadein 1 if_changed
    ton @ hair angry "Now tell me, who are you?{w} And you better tell the truth!" ("mad", "base", "angry", "mid")
    gen "(Shit, how often is this going to happen to me?)" ("angry", xpos="far_left", ypos="head")

    menu:
        gen "I am..." ("angry", xpos="far_left", ypos="head")
        "\"Albus Dumbledore!\"":
            ton "You are most certainly {b}not{/b} Albus Dumbledore!" ("upset", "base", "angry", "mid")
            gen "No wait, it was {i}Albertus Dumblerdore{/i}! That's it!" ("angry", xpos="far_left", ypos="head")
            gen "(Yes, that was probably it...)" ("base", xpos="far_left", ypos="head")
        "\"You know who!\"":
            ton @ hair scared "What?!" ("open", "wide", "base", "mid")
            gen "You...{w=0.8} know...{w=0.8} who..." ("base", xpos="far_left", ypos="head")
            ton "That can't be true, you're making it up!" ("open", "base", "annoyed", "mid")
            gen "You know who I am. You said it yourself earlier." ("base", xpos="far_left", ypos="head")
            gen "(If only I could remember what she called me...)" ("base", xpos="far_left", ypos="head")
        #"The danger!":
        #    ton "What?" ("base", "wide", "shocked", "stare")
        #    gen "I am the one who knocks..." ("angry", xpos="far_left", ypos="head")

    ton "I've had enough of this!" ("mad", "base", "angry", "mid")
    ton "Reveal your true identity, dark wizard!" ("open", "base", "angry", "mid")
    gen "I'm not a dark wizard, you racist twat!" ("angry", xpos="far_left", ypos="head")
    ton @ hair angry "How dare you call me a racist!" ("mad", "shocked", "angry", "mid")
    gen "Bring it! Do your worst, witch!" ("angry", xpos="far_left", ypos="head")
    call hide_characters
    hide screen bld1
    with d3

    # Glass break animation.
    # Duel won't happen and Tonks just casts a spell.

    play music "music/boss_battle_#2_metal_loop.ogg" fadein 1 fadeout 1 if_changed
    play sound "sounds/glass_break.ogg"
    pause.1

    show screen snape_glass
    pause 2.3

    hide screen snape_glass
    with irisout
    pause.1

    call gen_chibi("hide")
    $ desk_OBJ.idle = "desk_dumbledore"
    $ chair_left_OBJ.hidden = True
    call cast_spell("revelio")
    ton @ hair angry "Revelio!" ("open_wide", "shocked", "annoyed", "mid", ypos="head", flip=False)
    call bld("hide")
    pause.6

    $ desk_OBJ.idle = "ch_gen sit_behind_desk"
    with d9
    pause.6

    ton "" ("disgust", "shocked", "shocked", "stare", xpos="right", ypos="base")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    play music "music/Under-the-Radar by PhobyAk.ogg" if_changed
    ton "No way!" ("soft", "shocked", "base", "mid")
    gen "What just happened?" ("base", xpos="far_left", ypos="head")
    ton "What... are you...?" ("mad", "shocked", "raised", "mid")
    gen "(Can she see through the illusion?)" ("base", xpos="far_left", ypos="head")
    ton "Wait a minute... Are you...{w=0.5} {size=+4}a Genie?{/size}" ("open", "shocked", "raised", "mid")
    gen "(This witch knows her shit!)" ("angry", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")

    gen "Some people would say I'm {b}the{/b} Genie, actually!" ("grin", xpos="far_left", ypos="head")
    gen "The most powerful being in the entire universe... Multiple universes even..." ("base", xpos="far_left", ypos="head")
    gen "Glad my reputation precedes me..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "How curious... I've never had a Genie before." ("horny", "wide", "base", "down") # Tonks looks horny.
    gen "I'm sorry-- what?" ("base", xpos="far_left", ypos="head")
    ton "I meant, I've never had the pleasure of meeting a Genie before. This is brilliant!" ("grin", "shocked", "shocked", "mid")
    gen "(Is she hitting on me?!)" ("base", xpos="far_left", ypos="head")
    gen "I'm flattered... But how were you able to tell?" ("base", xpos="far_left", ypos="head")
    ton "I'm an Auror. It's my job to identify and catch magical beings..." ("soft", "wide", "shocked", "mid")
    ton "But, if you are here, what happened to Professor Dumbledore?{w} Did he use one of your wishes and wish himself away?" ("mad", "wide", "shocked", "R")
    gen "Not exactly..." ("base", xpos="far_left", ypos="head")
    ton "So? What happened to him?" ("upset", "base", "raised", "mid")
    gen "I believe we traded places when one of my magical inventions went wrong..." ("base", xpos="far_left", ypos="head")
    ton "Really?! Is he okay?" ("mad", "wide", "base", "mid")
    gen "I think so.{w} He travelled to my universe, and I'm stuck in this dull place..." ("base", xpos="far_left", ypos="head")
    gen "Believe me, there are a lot more brothels in Agrabah.{w} I bet he's having the time of his life..." ("base", xpos="far_left", ypos="head")
    ton "So, you just {i}*poofed*{/i} in here and decided to turn this school into your own private brothel..." ("open", "narrow", "angry", "mid")
    ton "Because you were bored?!" ("upset", "base", "angry", "mid")
    gen "Hey! I'm an immortal being... boredom is my worst enemy." ("base", xpos="far_left", ypos="head")
    gen "And I didn't do much, just a nudge in the right direction..." ("base", xpos="far_left", ypos="head")
    ton @ hair angry "You need to bring him back, the real Dumbledore, immediately!" ("mad", "base", "angry", "mid")
    gen "I don't know how, ... yet.{w} We're still working on it..." ("base", xpos="far_left", ypos="head")
    ton "We? Who else knows about this?" ("open", "narrow", "annoyed", "mid")

    menu:
        gen "(Crap...)" ("base", xpos="far_left", ypos="head")
        "\"You know who...\"":
            ton @ hair scared "{size=+4}What?!{/size}" ("open", "wide", "worried", "mid")
            gen "(Why do they keep freaking out whenever I say this...)" ("base", xpos="far_left", ypos="head")
            gen "That Snape guy." ("base", xpos="far_left", ypos="head")

        "\"Nobody...\"":
            ton "You mean Professor Snape is in on this?!" ("open", "wide", "shocked", "mid")
            gen "What? But I didn't--" ("base", xpos="far_left", ypos="head")

    ton "But of course!{w} After all, he was mentioned in Miss Granger's letter as one of the main offenders." ("disgust", "wide", "shocked", "stare")
    ton @ hair angry "That sleazy, vile snake...{w} Naturally he'd be all over an opportunity such as this." ("mad", "base", "angry", "R")
    gen "(Snake? Have I been saying his name wrong this entire time?...)" ("base", xpos="far_left", ypos="head")
    gen "(I hate when that happens...)" ("base", xpos="far_left", ypos="head")
    ton "And to think I believed that creep when I questioned him about it." ("mad", "closed", "angry", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    ton "He's a very skilled liar, I'll give him that." ("upset", "narrow", "angry", "down")
    gen "Are you going to lock us up now?" ("base", xpos="far_left", ypos="head")
    ton "I very well should! It would be the moral thing to do." ("open", "base", "angry", "mid")
    gen "(Shit...)" ("base", xpos="far_left", ypos="head")
    ton "You and Professor Snape should be locked in Azkaban for what you've done..." ("mad", "base", "angry", "mid")
    ton "And stay there for the rest of your lives..." ("open", "base", "angry", "mid")
    gen "You can't do that to me, I'm immortal! I'd go insane!" ("angry", xpos="far_left", ypos="head")
    ton "You should have thought about that before deciding to fuck your own students!" ("mad", "base", "angry", "mid")
    gen "But I haven't even gotten to that part yet!" ("angry", xpos="far_left", ypos="head")
    ton "And you never will!" ("open", "wide", "angry", "mid")
    ton "I'm going to put you in the smallest cell Azkaban has to offer..." ("open", "base", "angry", "mid")
    gen "No, please! I hate confined spaces!" ("angry", xpos="far_left", ypos="head")
    # fake game over
    $ renpy.music.stop(fadeout=4)
    stop weather fadeout 4
    play sound "sounds/level_failed.ogg"
    show screen cartoon_zoom
    gen "...{w=6.0}{nw}" ("angry", xpos="far_left", ypos="head")
    call gameover()
    # back from game over

    call weather_sound
    stop music fadeout 1.5

    play sound "sounds/scratch.ogg"
    ton "Unless..." ("upset", "narrow", "annoyed", "downR", trans=hpunch)

    gen "Unless?" ("angry", xpos="far_left", ypos="head")
    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton @ hair horny "You let me join in on the fun!" ("grin", "base", "raised", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "What?" ("angry", xpos="far_left", ypos="head") #screenshake
    ton "The ministry sent me to investigate what they assumed to be a silly rumour a student made up..." ("base", "base", "angry", "R")
    ton "And whilst I could just squash the rumour and go back to a dull, quiet desk job." ("disgust", "base", "raised", "mid") #rule of 3
    ton @ hair horny "I simply couldn't pass up an opportunity like this..." ("horny", "narrow", "base", "mid") #now that she's not being official and talking ministry business, she should slip back into more casual language
    ton @ hair horny "Keeping quiet would be far more... \"exciting\"." ("soft", "base", "base", "stare")
    gen "How so?" ("base", xpos="far_left", ypos="head")
    ton "I know for a fact that the Ministry has been trying to plant an inside man here at Hogwarts." ("normal", "base", "base", "R")
    gen "Then what are you suggesting?" ("base", xpos="far_left", ypos="head")
    ton "Hire me as a teacher." ("base", "base", "base", "mid")
    ton "I could teach the students a thing or two about the \"Defence against the Dark Arts\"..." ("open", "base", "base", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    ton "And if you and Snape want this favour trading to continue, you'll need somebody who can keep things quiet with the ministry." ("base", "closed", "base", "mid")
    gen "Do I even have a choice?" ("base", xpos="far_left", ypos="head")
    ton "The alternative would be me informing the ministry, and locking you both up." ("soft", "base", "base", "mid") #formal language here for the 'official procedure'
    gen "Then welcome aboard!" ("grin", xpos="far_left", ypos="head")
    ton "Don't worry. I'm not here to spoil your little act." ("base", "base", "raised", "mid")
    gen "That's a relief..." ("base", xpos="far_left", ypos="head")
    ton "I'll inform the other teachers about my stay." ("open", "base", "base", "R")
    ton "And the Ministry too of course. I'll be their inside man at Hogwarts, here at the request of Professor Dumbledore himself, no less." ("base", "base", "base", "mid")
    ton @ hair horny "If only they knew..." ("horny", "narrow", "base", "mid")
    ton "In any case, Profess--" ("open", "base", "base", "R")
    ton "I'm sorry, what would you like me to call you?" ("mad", "base", "raised", "mid")

    menu:
        gen "You can call me..." ("base", xpos="far_left", ypos="head")
        "\"Professor is fine.\"":
            $ name_genie_tonks = "Professor"
            ton "Very well." ("base", "base", "base", "mid")
        "\"You can call me Genie.\"":
            $ name_genie_tonks = "Genie"
            ton "Very well, Genie." ("base", "base", "base", "mid")
        "\"Call me Daddy...\"":
            $ name_genie_tonks = "Daddy"
            ton "What? Are you serious?!" ("open", "wide", "shocked", "stare")
            ton @ hair happy "*Ha-Ha-Ha!*...{w=0.3} you're too funny!" ("silly", "happyCl", "raised", "mid")
            gen "(What?-- Now it's yellow!)" ("angry", xpos="far_left", ypos="head")
            ton @ hair happy "Are all Genies this desperate?" ("crooked_smile", "base", "raised", "mid")
            gen "Desperate? Why Desperate? ..." ("base", xpos="far_left", ypos="head")
            ton @ hair happy "Nothing..." ("base", "base", "base", "down")
            ton @ hair horny "Very well... \"Daddy\"! {heart}{heart}{heart}" ("horny", "narrow", "base", "mid")
            gen "*He*-*He*-*He*-He*..." ("grin", xpos="far_left", ypos="head")

    ton "Call me to your office whenever you require my help, [name_genie_tonks]." ("base", "base", "base", "mid") #would it be better to have her call him by the requested name here, since later on we have the bit where Tonks submits to genie and calls him sir
    gen "I most certainly will..." ("base", xpos="far_left", ypos="head")

    #Tonks leaves
    call ton_walk(action="leave")

    call bld
    gen "What an interesting turn of events..." ("base", xpos="far_left", ypos="head")
    gen "Who would've guessed that she's such a pervert?!" ("grin", xpos="far_left", ypos="head")

    $ states.ton.unlocked = True
    $ achievements.unlock("unlockton", True)
    call popup("{size=-4}You can now summon Tonks into your office.{/size}", "Character unlocked!", "interface/icons/head/tonks.webp")

    gen "(Now that the matter is resolved, I guess I can get back to teaching Hermione...)"

    $ states.ton.busy = True

    $ states.ton.ev.intro.e3_complete = True
    $ nt_event_pause += 1

    call music_block
    jump main_room_menu


### Snape Hangout Event 2 ###
# You inform Snape that Tonks is now an ally and has been made a teacher.

label ss_he_tonks_E2:
    sna "........................." ("snape_31", ypos="head")
    sna "So, here is the plan..." ("snape_03")
    sna "You get a shovel and a body-bag ready, and I'll do the \"Avada Kedavra\"!" ("snape_01")
    gen "\"Avra-ka--\"{w} What the fuck are you talking about?" ("base", xpos="far_left", ypos="head")
    sna "Tonks! We need to get rid of her! Immediately!" ("snape_10")
    sna "Otherwise things will never go back to how they were!" ("snape_03")
    gen "Have you lost your mind again?" ("base", xpos="far_left", ypos="head")
    sna "No, but I'm about to!" ("snape_01")
    #sna "I haven't had a mouth on my cock in so long..." ("snape_29")
    #sna "Please, Genie. I need a fix!" ("snape_19") # Weird look
    #gen "..................." ("base", xpos="far_left", ypos="head")
    #sna "..................." ("snape_19") # Weird look
    #gen "Would you stop looking at me like that!!!" ("angry", xpos="far_left", ypos="head")
    #sna "What? Don't be ridiculous..." ("snape_14")
    gen "..................." ("base", xpos="far_left", ypos="head")
    sna "What a fool I was to believe that she'd be gone by now..." ("snape_31")
    sna "But of course not!" ("snape_32")
    sna "{size=+5}Instead they made that mischievous {b}cunt{/b} a teacher!{/size}" ("snape_33", trans=hpunch) # Screaming
    gen "Actually, that was--" ("base", xpos="far_left", ypos="head")
    sna "The whole universe has turned against me!" ("snape_43")
    sna "That bloody Ministry! Curse them!" ("snape_35")
    sna "Of course it was only a matter of time until they got themselves involved..." ("snape_06")
    sna "We had something good, Genie. And now it's over..." ("snape_26")

    gen "Well, lucky for us, it isn't over just yet..." ("base", xpos="far_left", ypos="head")
    sna "What's that supposed to mean? Are you concocting something?!" ("snape_25")
    gen "It's like you've said..." ("base", xpos="far_left", ypos="head")
    gen "The situation solved itself!" ("grin", xpos="far_left", ypos="head")
    gen "She's going to join us." ("base", xpos="far_left", ypos="head")

    sna "Join us? Doing what?" ("snape_05")
    gen "Corrupting those precious students of ours, of course!" ("grin", xpos="far_left", ypos="head")
    sna "And according to you, Tonks wants to help us break that Gryffindor bitch as well?" ("snape_34")
    gen "Yep." ("base", xpos="far_left", ypos="head")
    sna "*Ha-ha-ha*!{w} That's just fucking silly!" ("snape_28")
    gen "................" ("base", xpos="far_left", ypos="head")
    sna "Good one..." ("snape_45")
    sna "No seriously. What's going on?" ("snape_03")
    gen "She asked me if she could join us..." ("base", xpos="far_left", ypos="head")
    sna "*A-ha-ha-ha-ha*..." ("snape_28")
    gen "Who do you think made her a teacher in the first place?" ("base", xpos="far_left", ypos="head")
    sna "Stop it, please!!!" ("snape_42")
    gen "You don't believe me..." ("base", xpos="far_left", ypos="head")
    sna "Not a single word! *A-Ha-ha-ha*..." ("snape_28")
    gen "Fair enough..." ("base", xpos="far_left", ypos="head")
    sna "*Ha-ha-ha*--" ("snape_42")
    sna "*cough* {w=0.4}*cough* {w=0.4}*cough*..." ("snape_17", trans=hpunch)
    gen "..............." ("base", xpos="far_left", ypos="head")
    sna "..................." ("snape_31")

    sna "But none of this makes any sense!" ("snape_03")
    gen "Well, as it turns out..." ("base", xpos="far_left", ypos="head")
    sna "She's a pervert!" ("snape_36") # Revelation
    gen "She's a-- wait, how did you know?" ("base", xpos="far_left", ypos="head")
    sna "How could I've been so ignorant!" ("snape_08")
    gen "Am I missing something here, you're not a mind reader, are you?" ("base", xpos="far_left", ypos="head")
    sna "I'm a very skilled Occlumens, but no..." ("snape_31")
    gen "(Occlu-what?)" ("base", xpos="far_left", ypos="head")
    gen "Could you stop making up words..." ("base", xpos="far_left", ypos="head")
    sna "It's quite obvious in hindsight..." ("snape_35")
    gen "It...{w=0.4} is?" ("base", xpos="far_left", ypos="head")
    sna "Why would the Ministry have sent a full-fledged Auror, to deal with some eccentric insinuations made by some petty student..." ("snape_16")
    gen "Shouldn't they?" ("base", xpos="far_left", ypos="head")
    sna "Just because of some silly rumour about teachers having sexual intercourse with their students?" ("snape_34")
    gen "And that's not a reasonable enough concern to send somebody to look into it?" ("base", xpos="far_left", ypos="head")
    sna "It's the Ministry we're talking about...{w=0.8} They don't give a shit..." ("snape_30")
    sna "They wouldn't even believe it if \"you-know-who\" were to make a return..." ("snape_31")
    gen "Who?" ("base", xpos="far_left", ypos="head")
    sna "That Tonks had to be the only Ministry personnel seeing some truth in Granger's letters..." ("snape_35")
    sna "What if she specifically requested to be sent here to investigate?" ("snape_03")
    gen "She might have..." ("base", xpos="far_left", ypos="head")
    sna "So...{w=0.4} what does she want?" ("snape_04")
    sna "Surely she's taking the position for a reason..." ("snape_01")
    gen "It appears that she'd like to be part of this whole favour trading business, which is also why she asked to be made a teacher..." ("base", xpos="far_left", ypos="head")
    gen "And in return, she'll keep things quiet with the ministry." ("base", xpos="far_left", ypos="head")

    sna "*Hmm*... Not having to worry about the Ministry anymore, you say..." ("snape_38")
    sna "And I'm supposed to believe that she'd be willing to do that for us?" ("snape_25")
    sna "How exactly did you end up in this situation with her?" ("snape_04")
    gen "I don't know... It just... happened." ("base", xpos="far_left", ypos="head")
    gen "She pretty much figured everything out by herself." ("base", xpos="far_left", ypos="head")
    gen "Straight away. She even guessed that I'm a Genie..." ("base", xpos="far_left", ypos="head")
    sna "So she knows everything? How did she--" ("snape_03")
    gen "It appears the \"illusion charm\" wasn't perfect. She momentarily got a glimpse through it..." ("base", xpos="far_left", ypos="head")
    sna "That's impressive... perhaps I didn't give her enough credit..." ("snape_01")

    sna "If what you're telling me about her intentions is true..." ("snape_03")
    sna "Maybe she could be persuaded to help with the Granger situation..." ("snape_05")

    #if states.her.ev.intro.convinced:
    #    gen "Way ahead of you!" ("grin", xpos="far_left", ypos="head")
    #    gen "She's already offered to help with Granger." ("base", xpos="far_left", ypos="head")
    #else:
    gen "Oh, I'm sure there's little to no persuasion needed." ("base", xpos="far_left", ypos="head")
    gen "I have no doubt that she'd be well into the idea of convincing Granger to sell favours herself..." ("base", xpos="far_left", ypos="head")

    sna "What a wicked bitch!" ("snape_13")
    sna "If only we were selling favours back then..." ("snape_46")
    sna "You know what they say about students from Hufflepuff..." ("snape_20")
    sna "They always come last!" ("snape_21")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "I'm calling dibs on her!" ("base", xpos="far_left", ypos="head")
    sna "You do what?" ("snape_14")
    gen "Dibs, she's mine. I said it first..." ("base", xpos="far_left", ypos="head")
    sna "Are you twelve or something?" ("snape_04")
    gen "Over twelve thousand, actually." ("base", xpos="far_left", ypos="head")

    pause.1
    call blktone

    nar "You and professor Snape keep discussing various staff members of Hogwarts."
    nar "The bond between you two grows stronger."

    call sly_plus
    call hide_blktone

    $ states.sna.ev.hangouts.tonks_e2 = True
    $ ss_event_pause += 1

    jump end_snape_hangout_points


### Snape Hangout Event 3 ###
# You tell Snape that you made Tonks the teacher for 'DAtDA'

label ss_he_tonks_E3:
    call bld
    gen "Our new partner in crime, is she getting on well?" ("base", xpos="far_left", ypos="head")
    sna "Tonks? I haven't seen her that much... I prefer not to fraternize with the other teachers..." ("snape_09", ypos="head")
    sna "Shouldn't you know what that witch is up to? You made her a teacher, after all..." ("snape_01")
    gen "I'm sure she's still just settling down..." ("base", xpos="far_left", ypos="head")
    sna "Probably drinking booze down at Hogsmeade, more likely..." ("snape_35")
    sna "What subject is she even supposed to teach? What did you give her?" ("snape_03")
    gen "I have not the slightest clue..." ("base", xpos="far_left", ypos="head")
    sna "................" ("snape_38")
    sna "You know, I've been teaching \"Potions\" at this school for as long as I can remember..." ("snape_06")
    sna "Of course I'm the best they have.{w=0.8} And they don't call me \"Master of Potions\" for nothing!" ("snape_17")
    sna "But if we're honest, even a \"dim-witted Demiguise\" could teach potions to those simpletons..." ("snape_35")

    menu:
        gen "..............." ("base", xpos="far_left", ypos="head")
        "\"Are the students really that bad?\"":
            sna "*sigh* You have no idea, even an ape would show more learning abilities." ("snape_06")
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        "\"... Demiguise?\"":
            gen "What the fuck is that?" ("base", xpos="far_left", ypos="head")
            sna "*Sigh*... I keep forgetting you're not from around here..." ("snape_06")
            sna "It's a magical beast that can make itself invisible and has precognitive sight." ("snape_24")
            gen "... Sounds boring, forget I asked." ("base", xpos="far_left", ypos="head")
            sna "..........." ("snape_05")
            sna "Anyway, back to the topic at hand--" ("snape_04")

    sna "When it comes to \"Defence against the dark arts\"..." ("snape_03")
    sna "That's a subject that requires skill and cunning!" ("snape_02")
    sna "And a very competent and skilled teacher, to guide those hopeless souls through their lessons..." ("snape_40")
    sna "Now, If you were to assign me for that, and give Tonks my old subject to teach..." ("snape_20")
    gen "Yeah, about that...{w=0.4} I think I might have given that role to her..." ("base", xpos="far_left", ypos="head")
    sna "{size=+5}You did what?!{/size}" ("snape_33", trans=hpunch)
    gen "\"Defence against... something-something\"..." ("base", xpos="far_left", ypos="head")
    sna "You should have given me the \"defence against the dark arts\" position!" ("snape_34")
    sna "And she could've had something else... like \"muggle studies\", or something." ("snape_16")
    gen "First come, first served, I suppose..." ("base", xpos="far_left", ypos="head")
    gen "And I am not making her teach any \"smuggle studies\", who do you take me for?" ("base", xpos="far_left", ypos="head")
    sna "Curse you..." ("snape_08")
    gen "There wasn't really any room for me to argue with her..." ("base", xpos="far_left", ypos="head")
    gen "It was either that, or prison." ("base", xpos="far_left", ypos="head")
    sna ".................." ("snape_31")

    sna "I can't say that I trust her just yet..." ("snape_35")
    sna "Not before I get to slip in a couple of drops of \"Veritaserum\" into her drink..." ("snape_03")
    gen "\"Veritaserum\"?" ("base", xpos="far_left", ypos="head")
    sna "Truth potion!{w=0.4} I oftentimes use some on my \"very attractive Slytherins\"..." ("snape_02")
    sna "Only a single drop, and they'll tell me everything I want to know." ("snape_41")
    sna "Very handy should you need information to blackmail someone..." ("snape_46")
    sna "Or learn everything about their secret fetishes..." ("snape_20")
    gen "Neat!" ("grin", xpos="far_left", ypos="head")

    pause.1
    call blktone

    nar "You take some time to muse about the fetishes Tonks might have..."
    nar "For blackmailing... or to have some fun..."

    $ states.sna.ev.hangouts.tonks_e3 = True
    $ ss_event_pause += 1

    call sly_plus
    call hide_blktone

    jump end_snape_hangout_points
