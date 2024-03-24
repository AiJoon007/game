

### Cho Strip ###

label cc_pf_strip:

    if not _events_completed_any:
        gen "{size=-4}(Should I ask her to let me inspect her?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump cho_favor_menu

    return

    # End Event Jump
label end_cho_strip_event:

    if states.cho.tier == 2 and states.cho.level < 9: # Points til 9
        $ states.cho.level += 1

    if states.cho.tier == 3 and states.cho.level < 15: # Points til 15
        $ states.cho.level += 1

    $ cho.wear("all") # Reset clothes
    jump end_cho_event

### Tier 2 (pre Slytherin) ###

label cc_pf_strip_T2_intro_E1:

    call cc_pf_strip

    gen "It's time for your next favour, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    cho "Of course, [name_genie_cho]." ("base", "base", "base", "mid")
    cho "What would you like me to do?" ("soft", "base", "base", "mid")
    gen "First, come a bit closer..." ("base", xpos="far_left", ypos="head")
    cho "Very well, Sir." ("base", "base", "base", "mid")

    call cho_walk("desk", "base")

    cho "" (xpos="mid", ypos="base", trans=fade)
    call ctc

    gen "How often do you typically exercise, Miss Chang?" ("base", xpos="far_left", ypos="head")
    cho "As often as I can, [name_genie_cho]!" ("soft", "base", "base", "mid")
    gen "Which is... how often, exactly? Twice a week?" ("base", xpos="far_left", ypos="head")
    cho "Three times a day, Sir!" ("base", "narrow", "base", "mid")
    with hpunch
    gen "What?!" ("angry", xpos="far_left", ypos="head")
    gen "(I don't even jerk off that often!)" ("angry", xpos="far_left", ypos="head")
    gen "I find that a bit hard to believe... You're not embellishing the truth, are you?" ("base", xpos="far_left", ypos="head")
    cho "I'm not, Sir! It's necessary for someone in my position!" ("open", "closed", "angry", "mid")
    cho "I wake up every morning before dawn, then run around the Quidditch pitch until the sun rises!" ("open", "narrow", "angry", "mid")
    cho "My body's at the absolute peak of human condition!" ("open", "narrow", "angry", "R")
    gen "It is quite impressive..." ("angry", xpos="far_left", ypos="head")
    cho "Glad to hear it, [name_genie_cho]." ("base", "happyCl", "base", "mid")
    gen "I assume you get complimented often?" ("base", xpos="far_left", ypos="head")
    cho "Sometimes..." ("soft", "base", "base", "R")
    gen "And I suspect you have many admirers?" ("grin", xpos="far_left", ypos="head")
    cho "Oh, *umm*... maybe?" ("annoyed", "base", "base", "mid")
    cho "But that's {b}not{/b} why I take such great care of my body, Sir!" ("open", "narrow", "angry", "mid")
    gen "Of course not..." ("base", xpos="far_left", ypos="head")
    cho "Quidditch is a hard game for anyone, as I'm sure you know..." ("open", "closed", "base", "mid")
    cho "But that goes double for girls!{w=0.6} I have to train twice as hard as the boys if I want to stand a chance!" ("open", "narrow", "angry", "mid")
    gen "That's very commendable of you..." ("base", xpos="far_left", ypos="head")
    cho "Thank you, Sir." ("base", "base", "base", "mid")

    label .introspection:

    if _in_replay:
        show screen blkfade
        with d5


        $ cho.equip(cho_outfit_default)
        $ cho.set_pose("default")
        $ cho.animation = None
        $ game.gold = 1984
        $ game.day = 123
        call room("main_room")

        call cho_chibi("stand", "desk", "base", flip=False)
        call gen_chibi("sit_behind_desk")

        cho "" (xpos="mid", ypos="base", flip=False)
        hide screen blkfade
        with d5

    # Ask her to strip.
    gen "So, Why don't you show me what you are made of?{w=1.0} Let me have a proper look at you!" ("grin", xpos="far_left", ypos="head")
    cho "Sir?" ("soft", "wink", "raised", "mid")
    gen "I need you to remove your clothes." ("base", xpos="far_left", ypos="head")

    if _in_replay:
        show screen blkfade
        with d5
        return

    stop music fadeout 1
    cho @ cheeks blush "!!!" ("soft", "wide", "base", "mid")
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    gen "Go on, girl. Start with the top..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "No!" ("scream", "happyCl", "angry", "mid", trans=hpunch)
    cho "Why are you even asking me to do such a thing?!" ("angry", "narrow", "angry", "mid")
    gen "Have you already forgotten that I'm here to train you?" ("base", xpos="far_left", ypos="head")
    cho "And I'm very thankful for that sir, but..." ("open", "closed", "base", "mid")
    gen "Am I not your trusted mentor?" ("base", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "mid")
    gen "Your strong advisor..." ("base", xpos="far_left", ypos="head")
    gen "Your guardian angel!" ("grin", xpos="far_left", ypos="head")
    cho "I don't think taking off my clothes will be necessary for our training, [name_genie_cho]." ("annoyed", "narrow", "angry", "R")
    gen "I'm very disappointed, I've got to say..." ("base", xpos="far_left", ypos="head")
    gen "You aren't this shy about undressing in front of your team, are you?" ("base", xpos="far_left", ypos="head")
    cho "That's entirely different!" ("soft", "narrow", "angry", "mid")
    gen "How so?" ("base", xpos="far_left", ypos="head")
    cho "I'm just not comfortable doing this in front of you, Sir!" ("soft", "closed", "worried", "mid")
    cho @ cheeks blush "You're really old..." ("soft", "narrow", "worried", "downR")
    gen "Pardon me?" ("base", xpos="far_left", ypos="head")
    cho "I meant... You're our headmaster! It just feels wrong to me!" ("soft", "narrow", "worried", "mid")
    gen "Are you one of those shy girls, Miss Chang?" ("base", xpos="far_left", ypos="head")
    cho "No, Sir. I wouldn't say I'm shy, but..." ("soft", "narrow", "worried", "downR")
    gen "Well then prove to me that you aren't, girl!" ("base", xpos="far_left", ypos="head")
    gen "Let me see it!" ("grin", xpos="far_left", ypos="head")

    # Cho stays reluctant.
    cho "Is there no other way to prove it?" ("annoyed", "narrow", "worried", "mid")
    gen "Well, yes.{w=0.3} Several.{w} But we'll get to those later..." ("base", xpos="far_left", ypos="head")
    cho "Later, Sir?" ("soft", "base", "raised", "mid")
    gen "Girl, I wouldn't be asking you this if it wasn't absolutely necessary for your training!" ("angry", xpos="far_left", ypos="head")
    cho "Of course, [name_genie_cho]." ("annoyed", "base", "base", "down")
    gen "All that's required of you is to co-operate..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "(...)" ("annoyed", "base", "worried", "mid")
    gen "Now take off your top..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "(...)" ("annoyed", "narrow", "angry", "mid")
    cho "Only my top?" ("soft", "narrow", "worried", "mid")
    gen "Would you like to take off {b}more?{/b}" ("grin", xpos="far_left", ypos="head")
    cho "I didn't mean it like that!" ("angry", "narrow", "angry", "mid")
    gen "[name_cho_genie], it's only the two of us in here. No need to worry." ("base", xpos="far_left", ypos="head")
    cho "I'm not worried about others, [name_genie_cho]!" ("annoyed", "narrow", "angry", "mid")
    cho "For as long as nobody else will find out...{w} You have to promise me that, Sir!" ("soft", "narrow", "angry", "R")
    gen "Promised! Now take it off!" ("grin", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "mid")
    gen "*Ahem*{w=0.5} Slowly..." ("base", xpos="far_left", ypos="head")
    pause .5
    cho @ cheeks blush "" ("quiver", "happyCl", "worried", "mid")
    pause .8

    # Remove top.
    play sound "sounds/cloth_sound3.ogg"
    $ cho.strip("robe", "top")
    with d3
    pause .5

    $ states.cho.status.show_bra = True

    cho @ cheeks blush "" ("quiver", "narrow", "worried", "mid")
    call ctc

    menu:
        "\"Your posture is remarkable!\"":
            cho "Oh... Glad you noticed!" ("smile", "base", "base", "down") # Happy
            cho "I'm relieved you actually show interest in my body status, Sir!" ("base", "base", "base", "mid")
            gen "(Oh, You have no idea, girl!)" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I thought you just wanted to gush at my body like all the other teachers..." ("soft", "narrow", "worried", "mid")
            gen "Who?{w} Which other teachers are you talking about?{w} Snape?!" ("base", xpos="far_left", ypos="head")
            cho "No, not Snape..." ("annoyed", "narrow", "angry", "R")
            cho @ cheeks blush "(...)" ("annoyed", "base", "worried", "downR")
            cho @ cheeks blush "Promise me you won't tell her!" ("quiver", "narrow", "worried", "mid")
            gen "Her?!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Madam Hooch, Sir." ("soft", "narrow", "worried", "mid")
            gen "Ah, that fit lady..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Yes, she's been eyeing me a lot lately..." ("annoyed", "base", "worried", "downR")
            cho @ cheeks blush "Even more so after our recent game against Hufflepuff..." ("mad", "narrow", "worried", "R")
            gen "I can't blame her... Your body is very pleasant to look at!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "Thank you, Sir." ("base", "base", "base", "mid")

        "\"You have marvellous abs!\"":
            gen "Magnificent." ("angry", xpos="far_left", ypos="head")
            gen "Simply...{w} magnificent..." ("angry", xpos="far_left", ypos="head")
            cho @ cheeks blush "*Ehm*..." ("annoyed", "narrow", "worried", "R") # Embarrassed
            gen "As if Michelangelo himself carved them onto your flesh..." ("angry", xpos="far_left", ypos="head")
            gen "I must say I'm very impressed!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Thank you, Sir." ("soft", "narrow", "worried", "downR")

        "\"*Eh*, I've seen better, but that'll do.\"":
            $ states.cho.mood += 3
            cho "What?!" ("mad", "base", "angry", "mid") # Upset
            gen "(Crap!)" ("angry", xpos="far_left", ypos="head")
            gen "What I meant to say is, you're in great shape, but I still see room for improvements." ("base", xpos="far_left", ypos="head")
            gen "I'm impressed nonetheless!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Thank you, I guess..." ("annoyed", "narrow", "angry", "downR")

    gen "None of the other girls I get to see here have such fine...{w=1.0} contours." ("base", xpos="far_left", ypos="head")
    cho "Other girls?" ("soft", "wide", "base", "mid")
    cho "[name_genie_cho], you aren't training anybody else in Quidditch besides me, are you?" ("soft", "narrow", "angry", "mid")
    gen "What? Of course not..." ("base", xpos="far_left", ypos="head")
    cho "Then which other girls are you talking about?" ("annoyed", "narrow", "angry", "mid")
    gen "(Shit! I better just tell her the truth.)" ("angry", xpos="far_left", ypos="head")
    gen "Just...{w=1.0} Granger..." ("base", xpos="far_left", ypos="head")
    cho "*Phewww*{w=1.0} You scared me there for a second, Sir..." ("smile", "narrow", "worried", "mid")
    gen "You... don't mind?" ("base", xpos="far_left", ypos="head")
    cho "Please. Why should I care what Granger does for you in here?" ("soft", "narrow", "angry", "R")
    cho "All she seems to care about is winning the house cup." ("open", "narrow", "angry", "R")
    cho "As long as you don't help any Gryffindor or Slytherin sluts win the Quidditch cup, everything will be fine." ("base", "narrow", "base", "mid")
    gen "No worries, [name_cho_genie]. I don't have plans to train other {i}sluts{/i} in quidditch." ("grin", xpos="far_left", ypos="head")

    cho "That's a relief..." ("open", "closed", "base", "mid")
    cho "Besides, she clearly doesn't hold a candle against me!" ("open", "narrow", "base", "R")
    cho "All she does is sit on her arse all day, studying in the library..." ("soft", "narrow", "angry", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    cho "You can't expect somebody who's as lazy as her to look as great as I do!" ("soft", "closed", "base", "mid")

    menu:
        "\"Yeah, she's gross.\"":
            $ states.cho.mood = 0
            gen "Miss Granger's body is nothing compared to yours." ("base", xpos="far_left", ypos="head")
            cho "I wholeheartedly agree, Sir!" ("base", "narrow", "angry", "mid")
            gen "Her tits sag too much, and her fat hips are disgusting..." ("base", xpos="far_left", ypos="head")
            hide cho_main
            gen "(Something deep inside me just died saying this...)" ("angry", xpos="far_left", ypos="head")
            cho "She really is a..." ("open", "closed", "raised", "mid")
            cho "... stupid..." ("angry", "closed", "angry", "mid")
            cho "... fat..." ("clench", "narrow", "angry", "mid")
            cho @ cheeks blush "... cow, isn't she?" ("quiver", "narrow", "angry", "mid")
            gen "Speaking of Hermione..." ("base", xpos="far_left", ypos="head")
            gen "Why don't you show me \"your\"{w} very much \"superior\"{w} hips?" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "Are you asking me to take off my bottoms?" ("soft", "wink", "raised", "mid")
            gen "Yes, my dear." ("base", xpos="far_left", ypos="head")

        "\"Nope, you lose\"":
            $ states.cho.mood += 6

            cho "What?!" ("scream", "wide", "angry", "mid", trans=hpunch)
            cho "" ("angry", "narrow", "angry", "mid")
            gen "I'm afraid, Miss Granger is simply...{w} how shall I put it...{w} sexier!" ("base", xpos="far_left", ypos="head")
            cho "But she doesn't even do workouts!" ("clench", "narrow", "angry", "mid")
            gen "Let's just forget about her, shall we?" ("base", xpos="far_left", ypos="head")
            gen "And continue where we left off..." ("base", xpos="far_left", ypos="head")
            cho "And where would that be?" ("annoyed", "narrow", "angry", "mid")
            gen "Your Quidditch training, Miss Chang." ("base", xpos="far_left", ypos="head")
            cho "I'm not sure I want to -- after what you've just said..." ("annoyed", "narrow", "angry", "R")
            gen "Why? What did I say?" ("base", xpos="far_left", ypos="head")
            cho "That Granger's body is better?! We both know that isn't true." ("mad", "narrow", "angry", "mid")
            gen "Do you expect me to apologise?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Yes!{w} Admit that I'm sexier!" ("annoyed", "closed", "angry", "mid") # Snobby
            gen "You are indeed, {b}very sexy{/b}, Miss Chang!" ("grin", xpos="far_left", ypos="head")
            cho "Thank you, Sir." ("base", "narrow", "base", "mid")
            gen "Now take your bottoms off, would you..." ("base", xpos="far_left", ypos="head")
            cho "(...)" ("annoyed", "narrow", "angry", "mid")


    cho @ cheeks blush "Please don't tell anybody about what I'm doing in here, Sir." ("quiver", "narrow", "worried", "mid")
    cho @ cheeks blush "It could really tarnish my reputation." ("soft", "narrow", "worried", "R")
    gen "I'd never think of it..." ("base", xpos="far_left", ypos="head")
    cho "I will take off my bottoms now!" ("scream", "happyCl", "angry", "mid") # Scream
    cho @ cheeks blush "" ("horny", "narrow", "worried", "R")
    gen "(!!!)" ("grin", xpos="far_left", ypos="head")
    pause .4

    # Remove bottoms.
    play sound "sounds/cloth_sound3.ogg"
    hide cho_main
    $ cho.strip("bottom")
    pause 1.2
    play sound "sounds/cloth_sound4.ogg"
    show screen cho_cloth_pile
    pause .4
    cho "" (trans=d3)
    pause .5

    $ states.cho.status.show_panties = True

    cho @ cheeks blush "" ("horny", "narrow", "base", "mid")
    call ctc

    gen "YES!" ("angry", xpos="far_left", ypos="head")
    gen "Look at those thighs!" ("angry", xpos="far_left", ypos="head")
    gen "Those tree trunks!" ("angry", xpos="far_left", ypos="head")
    gen "Even the great \"Chun-Li\" would be jealous of those!" ("grin", xpos="far_left", ypos="head")
    cho "I'm sorry Sir, who's that?" ("soft", "wink", "raised", "mid")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")

        "\"Never seen City Hunter?\"":
            cho "\"City Hunter?\"{w=0.3} Can't say that I have." ("soft", "base", "raised", "mid")
            gen "What about \"Police Story\"?" ("base", xpos="far_left", ypos="head")
            cho "No?" ("soft", "wink", "raised", "mid")
            gen "\"Drunken Master\"?" ("base", xpos="far_left", ypos="head")
            cho "(...)" ("annoyed", "base", "base", "R")
            gen "Please tell me you've at the very least seen \"Rush Hour\"?" ("angry", xpos="far_left", ypos="head")
            cho "No, Sir." ("annoyed", "closed", "base", "mid")
            gen "I'm in shock, over how little you care about your culture..." ("base", xpos="far_left", ypos="head")
            cho "(...)" ("annoyed", "narrow", "angry", "mid")
            gen "Not every man can pull off a cosplay like that!" ("angry", xpos="far_left", ypos="head")
            cho "I'm not following, Sir." ("annoyed", "narrow", "angry", "R")

        "\"She's my main...\"":
            gen "I simply love playing with her..." ("grin", xpos="far_left", ypos="head")
            gen "Seeing that leg rise up when I press the right buttons..." ("base", xpos="far_left", ypos="head")
            cho "What?!" ("open", "narrow", "raised", "mid") # confused

    gen "Speaking of which!{w} I don't believe we are done here just yet." ("grin", xpos="far_left", ypos="head")
    cho "We aren't? But I did exactly what you wanted!" ("open", "base", "worried", "mid")
    gen "You've still got some clothes on..." ("grin", xpos="far_left", ypos="head")
    cho "Sir, is this why you are helping me?" ("open", "closed", "angry", "mid")
    cho "Might this be all just part of a sick scheme to get to see me naked?" ("annoyed", "narrow", "angry", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    menu:
        "\"It absolutely is!\"":
            $ states.cho.mood += 20
            $ cho_mad_about_stripping = True # Flag that enables different dialogue that is a bit more "lewd" in the next favour repeat.
            cho "" ("angry", "wide", "base", "mid") # Shock
            gen "Now take off that bra of yours and show me those titties!" ("grin", xpos="far_left", ypos="head")
            cho "[name_genie_cho], how can you talk to me like that!" ("scream", "closed", "angry", "mid", trans=hpunch)
            cho "I'm your student!" ("clench", "narrow", "angry", "mid")
            gen "And a very pretty one at that!" ("grin", xpos="far_left", ypos="head")
            cho "You disgust me, sir..." ("soft", "narrow", "angry", "mid")

        "\"Of course not...\"":
            $ states.cho.mood += 6
            $ cho_mad_about_stripping = False
            cho "Aye right..." ("soft", "narrow", "raised", "mid") # Expression of disbelieve...
            cho "And I'm supposed to believe that." ("open", "narrow", "base", "R")
            cho "You're practically foaming out of your mouth just looking at me, Sir..." ("soft", "narrow", "angry", "mid")
            gen "I'm not...{w} that's just..." ("angry", xpos="far_left", ypos="head")
            #if butterbeer_ITEM.owned > 0:
            gen "Butterbeer..." ("angry", xpos="far_left", ypos="head")
            cho "This is as far as I will go, Sir!" ("annoyed", "narrow", "angry", "mid")

    cho "If you want a bimbo to strip for you, I suggest you call Hermione instead..." ("annoyed", "narrow", "angry", "mid")
    pause .5

    play sound "sounds/cloth_sound.ogg"
    hide cho_main
    $ cho.wear("all")
    hide screen cho_cloth_pile
    cho "" ("angry", "narrow", "angry", "mid")
    pause .8

    cho "We are done here!" ("angry", "narrow", "angry", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    gen "(She'll do it next time, I'm sure...)" ("base", xpos="far_left", ypos="head")

    jump end_cho_strip_event


label cc_pf_strip_T2_intro_E2:

    call cc_pf_strip

    cho "" ("upset", "base", "base", "R")
    gen "[name_cho_genie], to continue your training where we left off..." ("base", xpos="far_left", ypos="head")
    gen "I'd like you to, once again, undress!" ("grin", xpos="far_left", ypos="head")
    cho "Of course, Sir." ("annoyed", "base", "angry", "downR")

    call cho_walk("desk", "base")

    cho "Down to my undergarments, [name_genie_cho]?" ("soft", "closed", "base", "mid", xpos="mid", ypos="base", trans=fade)
    cho "Or would you like me to take off all of it?" ("soft", "narrow", "base", "mid")
    gen "*Ehm*... All of it?" ("base", xpos="far_left", ypos="head")
    cho "Very well, Sir." ("soft", "closed", "base", "mid")
    gen "(Please don't let this be a trick question.)" ("angry", xpos="far_left", ypos="head")
    cho "" ("upset", "narrow", "base", "mid")
    pause .4

    if cho.is_worn("robe"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("robe")
    # Remove top.
    if cho.is_worn("top"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("robe", "top")
        with d3
        pause .5

        cho "" ("upset", "narrow", "angry", "mid")
        call ctc

    cho "I'm a very good trainee, [name_genie_cho]!" ("soft", "narrow", "angry", "mid")
    gen "Yes you are!" ("grin", xpos="far_left", ypos="head")
    cho "If my trainer requires me to take off my clothing and strip for him..." ("soft", "closed", "base", "mid")
    cho "Then I have no other choice but to indulge..." ("soft", "narrow", "base", "R")
    cho "I see nothing wrong with that..." ("annoyed", "narrow", "angry", "mid")
    pause .4

    # Remove bottoms.
    if cho.is_worn("bottom"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("bottom")
        with d3
        pause .5

        cho "" ("annoyed", "narrow", "base", "mid")
        call ctc

    cho "Would you perhaps like me to climb on top of your desk?" ("soft", "narrow", "raised", "mid")
    cho "And dance for you like some common harlot?" ("soft", "narrow", "base", "R")

    # You saw Hermione strip before.
    if states.her.status.stripping:
        gen "If it's not too much trouble..." ("base", xpos="far_left", ypos="head")
        cho "Of course not, [name_genie_cho]." ("soft", "closed", "base", "mid")
        gen "(I'm having a bit of a déjà vu!)" ("angry", xpos="far_left", ypos="head") # In-game font doesn't support special characters. déjà vu!
    else:
        gen "Yes please!" ("grin", xpos="far_left", ypos="head")
        cho "Whatever you say, Sir!" ("soft", "closed", "base", "mid")
    cho "Like I said, I'd go to any lengths just to please my trainer..." ("soft", "narrow", "base", "mid")

    # Climbs desk.
    call hide_characters
    show screen blkfade
    with d5
    play sound "sounds/08_hop_on_desk.ogg"
    pause 1

    nar "To your surprise, the athletic, petite girl rather playfully climbs on top of your desk."
    pause .5
    gen "Nice!" ("grin", xpos="far_left", ypos="head")
    pause .2

    call cho_chibi("stand", "on_desk", "on_desk", flip=False)
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    cho "After all, I promised I'd do anything to win that Quidditch cup..." ("soft", "narrow", "angry", "mid")
    cho "If stripping for you is what it takes, then..." ("soft", "base", "angry", "down")
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.ogg" fadein 1 if_changed
    cho "Then..." ("angry", "base", "worried", "down")
    cho @ cheeks blush "I-I'll do it..." ("soft", "narrow", "worried", "down")
    gen "(Shit... Is she crying?)" ("base", xpos="far_left", ypos="head")
    gen "(Can she even cry?)" ("base", xpos="far_left", ypos="head")
    gen "Are you alright, girl?" ("base", xpos="far_left", ypos="head")
    cho "No.{w} I'm already regretting climbing up here!!!" ("mad", "closed", "worried", "mid")
    cho @ cheeks blush "(What were you thinking, Cho?!)" ("angry", "narrow", "worried", "down")
    gen "You can come back down if it's too much for yo--" ("base", xpos="far_left", ypos="head")
    cho "Shut up!" ("scream", "closed", "angry", "mid", trans=hpunch) # Scream
    cho "Can't you see what I'm trying to do here?" ("angry", "narrow", "angry", "mid")
    gen "Not really, no." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I-I'm... testing my limits, Sir." ("angry", "narrow", "worried", "down")
    cho @ cheeks blush "And I believe I've reached them!" ("mad", "happyCl", "worried", "mid")
    gen "For real? You are still wearing clothes..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I thought{w=0.2}, if I could go as far as embarrassing myself in front of my headmaster..." ("soft", "narrow", "worried", "down")
    cho @ cheeks blush "Doing the same in front of the school won't feel as bad in comparison." ("annoyed", "narrow", "worried", "down")
    cho "Sir, I don't think I can do this after all." ("soft", "narrow", "worried", "mid")
    cho "Could I get your permission to leave and never come back?" ("angry", "narrow", "worried", "mid")

    menu:
        "\"Yes, but take off those clothes first...\"":
            stop music fadeout 1
            cho @ cheeks blush "Yes! Thank you, Sir!" ("soft", "closed", "worried", "mid")
            cho @ cheeks blush "Even after I've given up -- You're still believing in me!" ("soft", "narrow", "worried", "mid")
            gen "What?{w=0.2} *Ahem*...{w=0.2} I mean..." ("base", xpos="far_left", ypos="head")
            gen "Of course!{w=0.2} I always did!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "I may not like it. But this is all just part of my training..." ("soft", "base", "worried", "R")
            gen "*Uhhhh*... Sure..." ("base", xpos="far_left", ypos="head")
            play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
            cho "It's one of many challenges I have to face before I can call myself a Quidditch champion!" ("soft", "closed", "angry", "mid")
            cho "This is just about facing my inner demons, isn't it?" ("soft", "narrow", "angry", "mid")
            cho "Overcoming my fears..." ("soft", "narrow", "angry", "R")
            cho "Failure, and embarrassment..." ("soft", "closed", "base", "mid")
            cho @ cheeks blush "(Come on, Cho... You can do it!!!)" ("horny", "happyCl", "worried", "mid")
            cho @ cheeks blush "*Ehm*..." ("horny", "narrow", "worried", "down")
            cho @ cheeks blush "What would you like me to do first, [name_genie_cho]?" ("soft", "narrow", "worried", "mid")
            cho @ cheeks blush "Remove my bra..." ("soft", "narrow", "base", "mid")
            cho @ cheeks blush "Or take off my panties?" ("horny", "narrow", "worried", "down")

        "\"Yes, you are dismissed...\"":
            $ states.cho.mood += 6
            stop music fadeout 1
            cho "What?!" ("soft", "wide", "base", "mid")
            cho "But Sir!" ("soft", "base", "worried", "mid")
            gen "You can go now..." ("base", xpos="far_left", ypos="head")
            cho "You can't do that!" ("scream", "narrow", "angry", "mid", trans=hpunch)
            cho "" ("angry", "narrow", "angry", "mid")
            gen "Didn't you just beg me to do just that?" ("angry", xpos="far_left", ypos="head")
            play music "music/GrapeSodaIsFuckingRawbyjrayteam6.ogg" fadein 1 if_changed
            cho "I begged you to help me win the Quidditch cup!" ("clench", "narrow", "angry", "mid")
            cho "And to be my trainer!{w} To be a {b}good{/b} trainer!" ("soft", "narrow", "angry", "mid")
            cho @ cheeks blush "How can I overcome my fear of losing if I can't even do... this!" ("annoyed", "base", "worried", "down")
            cho "You're supposed to encourage me!{w=0.6} Get me through any challenges I'm confronted with." ("soft", "narrow", "angry", "mid")
            gen "Including stripping?" ("base", xpos="far_left", ypos="head")
            cho "Including bloody stripping!" ("scream", "closed", "angry", "mid", trans=hpunch)
            cho "" ("annoyed", "narrow", "angry", "mid")
            gen "To my defence. I got some mixed messages from you earlier..." ("base", xpos="far_left", ypos="head")
            cho "(...)" ("annoyed", "narrow", "angry", "R") # Annoyed
            stop music fadeout 1
            gen "Very well then..." ("base", xpos="far_left", ypos="head")
            gen "Take off your clothes, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
            cho "Yes, Sir!" ("soft", "closed", "base", "mid")
            cho "Would you like me to take off my bra first?" ("soft", "narrow", "angry", "mid")
            cho "Or pull down my panties, so you can get a nice look at my lower half?" ("soft", "narrow", "base", "mid")

    menu:
        gen "First, I'd like you to..." ("base", xpos="far_left", ypos="head")
        "\"Show me those big, juicy \"Quaffles\" of yours!\"":
            play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
            cho @ cheeks blush "*Uhhh*..." ("upset", "wide", "base", "mid")
            gen "Those two mean, hearty \"bludgers\"!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "Sir? Could it be that you are talking about my breasts?" ("soft", "narrow", "worried", "mid")
            gen "Yes indeed! Very good." ("base", xpos="far_left", ypos="head")
            gen "I was hoping you would eventually catch on." ("base", xpos="far_left", ypos="head")
            gen "Also because I ran out of balls to compare them to..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Promise me that you won't laugh when I show you my..." ("soft", "narrow", "worried", "R")
            cho @ cheeks heavy_blush "\"Bludgers\"!" ("mad", "happyCl", "worried", "mid")
            gen "Why would I ever laugh at a pretty girl like you, Miss Chang?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Because they...{w} aren't as big as Hermione's..." ("soft", "narrow", "worried", "downR")
            cho @ cheeks blush "Hers are much closer to {i}Quaffles{/i} than mine..." ("soft", "base", "worried", "mid")
            gen "And there will always be a pair of \"Beaters\" that prefer to play with your...{w} balls." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Only two?..." ("upset", "base", "worried", "downR")
            gen "Don't forget to count those lucky enough to get hit by those \"bludgers\"!" ("grin", xpos="far_left", ypos="head")
            cho "" ("upset", "base", "raised", "mid")
            gen "Speaking of which..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Yes?" ("soft", "base", "worried", "mid")
            gen "I'd like you to hit me with them!" ("angry", xpos="far_left", ypos="head")
            cho @ cheeks blush "With my breasts?" ("open", "wide", "base", "mid")
            gen "Yes! Hit me full force!{w} Take off that bra!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "*Ugh!*..." ("mad", "narrow", "base", "down")
            cho @ cheeks blush "{size=-4}I can't believe I'm actually going to do this!{/size}" ("mad", "happyCl", "worried", "mid")
            cho @ cheeks blush "" ("soft", "narrow", "worried", "mid")
            pause .4

            # Remove bra.
            play sound "sounds/cloth_sound3.ogg"
            $ cho.strip("bra")
            with d3
            pause .8

            cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "mid")
            call ctc

            gen "Simply wonderful, Miss Chang." ("angry", xpos="far_left", ypos="head")
            gen "Those are some stellar breasts you got there." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "(...)" ("base", "narrow", "worried", "downR")
            gen "Some \"outstanding\" boobies!" ("angry", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("annoyed", "narrow", "base", "mid")
            gen "Would you mind if I smack them?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "What?! Of course I would mind!" ("soft", "wide", "base", "mid")
            gen "I just want to beat them around a bit..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "" ("annoyed", "narrow", "angry", "mid")
            gen "After all, they are two soft, meaty \"bludgers\"!" ("grin", xpos="far_left", ypos="head")
            gen "And I'm a \"beater\"!" ("grin", xpos="far_left", ypos="head")

            $ states.gen.stats.quidditch_position = "beater"

            cho "You are childish.{w} That's what you are..." ("soft", "narrow", "angry", "mid")
            gen "You're the one playing games." ("base", xpos="far_left", ypos="head")
            cho "(...)" ("annoyed", "narrow", "angry", "mid")
            cho "Fine...{w} But Only once!" ("soft", "narrow", "angry", "R")
            cho @ cheeks blush "Twice...{w} maybe..." ("mad", "narrow", "worried", "downR")
            gen "That's a hundred percent more than I had hoped for!" ("grin", xpos="far_left", ypos="head")

            call slap_her
            cho @ cheeks blush "*Ouch!*" ("angry", "wide", "base", "mid")
            call slap_her
            call slap_her
            call slap_her
            cho @ cheeks blush "Stop it!" ("scream", "happyCl", "worried", "mid")
            cho @ cheeks blush "That was more than twice!" ("soft", "narrow", "angry", "mid")
            gen "I stopped counting halfway through..." ("base", xpos="far_left", ypos="head")

        "\"Let me catch sight of that 'Snitch!'\"":
            play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
            cho "Don't you mean \"Snatch\", Sir?" ("annoyed", "narrow", "angry", "mid")
            gen "Potato, Potato!" ("grin", xpos="far_left", ypos="head")
            cho "Your motives were nothing but for your own perverted gains, weren't they? From the very start." ("soft", "narrow", "base", "mid") # Annoyed
            gen "More or less..." ("base", xpos="far_left", ypos="head")
            gen "However, I never lied about wanting to help you win the Quidditch cup!" ("base", xpos="far_left", ypos="head")
            gen "(Since I've bet a fortune on it...)" ("angry", xpos="far_left", ypos="head")
            gen "And I wouldn't be able to call myself a man if I was lying!" ("base", xpos="far_left", ypos="head")
            cho "And you'd be called a dead man, if you try to trick me!" ("clench", "narrow", "angry", "mid")
            gen "Well technically I'm a geni--" ("base", xpos="far_left", ypos="head")
            play sound "sounds/kick.ogg"
            cho "" ("annoyed", "narrow", "angry", "mid", trans=vpunch)
            gen "*Aaaaah*!" ("angry", xpos="far_left", ypos="head")
            nar "Cho does a daunting stomp on your desk..."
            cho "Don't think for a second I wouldn't do it! After all of this!" ("scream", "narrow", "angry", "mid")
            cho "" ("angry", "narrow", "angry", "mid")
            play sound "sounds/gulp.ogg"
            gen "*Gulp*" ("angry", xpos="far_left", ypos="head")
            gen "Yes, Ma'am." ("base", xpos="far_left", ypos="head")
            cho "(...)" ("upset", "closed", "base", "mid")
            cho @ cheeks blush "" ("upset", "narrow", "worried", "down")
            pause .4

            # Remove panties.
            play sound "sounds/cloth_sound3.ogg"
            $ cho.strip("panties")
            with d3
            pause .5

            cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "mid")
            call ctc

            cho @ cheeks blush "Happy, Sir?" ("soft", "narrow", "worried", "mid")
            gen "Very." ("base", xpos="far_left", ypos="head")
            gen "Finally I get the appeal of Quidditch." ("grin", xpos="far_left", ypos="head")
            cho "Really?" ("soft", "base", "raised", "mid")
            gen "Yes..." ("base", xpos="far_left", ypos="head")
            gen "You see, I think I've become quite a bit of a seeker myself!" ("grin", xpos="far_left", ypos="head")

            $ states.gen.stats.quidditch_position = "seeker"

            cho "(...)" ("annoyed", "base", "base", "mid")
            gen "And I believe I've just found my very own golden snatch!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "" ("annoyed", "narrow", "angry", "mid")
            gen "You should consider yourself lucky, Miss Chang." ("base", xpos="far_left", ypos="head")
            cho "Why?..." ("soft", "narrow", "raised", "mid")
            gen "It's very pretty." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "*Ugh*..." ("mad", "narrow", "base", "down")


    cho @ cheeks blush "Sir, will that be all then?" ("annoyed", "narrow", "angry", "mid")
    cho "May I go now?" ("soft", "narrow", "angry", "R")
    gen "Haven't you forgotten something?" ("base", xpos="far_left", ypos="head")
    cho "Didn't I do enough for you already?" ("angry", "narrow", "angry", "mid")
    gen "For me, you did more than enough!{w=0.6} I'm more than pleased with what you've shown me..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Ugh*..." ("disgust", "narrow", "base", "down") # Disgusted
    gen "But, wasn't your goal earlier to undress entirely?" ("base", xpos="far_left", ypos="head")
    gen "To prove to yourself that you {b}could{/b} do it?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "{size=-4}I hoped you'd just forget about that...{/size}" ("mad", "narrow", "worried", "down") # Small text.
    gen "Well, I didn't!" ("grin", xpos="far_left", ypos="head")
    gen "I'm here to help you mature -- and boost your confidence." ("base", xpos="far_left", ypos="head")
    gen "A body like yours is nothing you need to hide away!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("base", "narrow", "worried", "mid")
    gen "Don't you think so too?{w} After all the work you put into it?" ("base", xpos="far_left", ypos="head")
    gen "It should be celebrated! And seen by everyone!" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "You're making me blush, [name_genie_cho]..." ("horny", "narrow", "worried", "downR")
    gen "You can do it, [name_cho_genie]! Show me the goods!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes, Sir!" ("angry", "closed", "worried", "mid")
    cho @ cheeks blush "" ("base", "narrow", "worried", "mid")
    pause .4

    # Cho strips completely.
    play sound "sounds/cloth_sound3.ogg"
    hide cho_main
    $ cho.strip("clothes")
    pause 1.2
    call cho_chibi("stand", "on_desk", "on_desk", flip=True)
    pause .4
    play sound "sounds/cloth_sound4.ogg"
    show screen cho_cloth_pile
    pause .6
    call cho_chibi("stand", "on_desk", "on_desk", flip=False)
    cho "" (trans=d3)
    pause .5

    $ states.cho.status.stripping = True
    $ states.cho.status.show_tits = True
    $ states.cho.status.show_pussy = True

    cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "mid")
    call ctc

    gen "See, that wasn't very hard, was it?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "No..." ("soft", "narrow", "base", "down")
    cho "No! You're right!" ("smile", "base", "base", "mid")
    gen "And you have a very beautiful body -- if I might add." ("base", xpos="far_left", ypos="head")
    cho "Thank you, Sir." ("soft", "narrow", "worried", "mid")
    gen "I can see why Hermione is so jealous." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("upset", "base", "base", "mid")
    pause .8
    cho @ cheeks blush "She is?" ("scream", "wide", "base", "mid", trans=vpunch)
    cho @ cheeks heavy_blush "" ("horny", "base", "base", "down")
    gen "Look who perked up all of a sudden." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "She should be jealous!{w=0.6} These thighs could snap a broom in half if I tried hard enough." ("smile", "narrow", "angry", "mid")
    call ctc

    play sound "sounds/gulp.ogg"
    gen "*Gulp!*" ("angry", xpos="far_left", ypos="head")
    gen "I don't doubt it." ("base", xpos="far_left", ypos="head")

    cho "Thank you, [name_genie_cho]." ("base", "closed", "base", "mid")
    gen "For what?" ("base", xpos="far_left", ypos="head")
    cho "For teaching me." ("soft", "narrow", "worried", "downR")
    cho @ cheeks blush "I couldn't have imagined showing myself off like this before... but." ("horny", "narrow", "worried", "downR")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    cho "Well, your methods have clearly worked so far..." ("soft", "narrow", "base", "R")
    cho "And I feel more confident than ever!" ("soft", "wide", "base", "mid")
    gen "That's great news, and hey..." ("base", xpos="far_left", ypos="head")
    gen "If distracting doesn't work, you could just crush your opponents with those thighs of yours." ("base", xpos="far_left", ypos="head")
    cho "That's true..." ("smile", "narrow", "base", "mid")
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    play sound "sounds/08_hop_on_desk.ogg"
    call cho_chibi("stand", "desk", "base", flip=False)

    pause 1

    hide screen blkfade
    with d5
    pause .2

    cho "Will this be all then, Sir?" ("soft", "base", "base", "R")
    gen "Yes Miss Chang, great work today..." ("base", xpos="far_left", ypos="head")
    gen "I doubt you'll have any problems distracting anyone with a body like that." ("base", xpos="far_left", ypos="head")
    gen "You're dismissed." ("base", xpos="far_left", ypos="head")
    cho "Thank you, [name_genie_cho]." ("base", "happyCl", "base", "mid")
    call hide_characters
    hide screen bld1
    with d3
    pause .1

    call cho_walk("door", "base")

    gen "Miss Chang." ("base", xpos="far_left", ypos="head")
    hide screen bld1
    with d3
    pause .3

    call cho_chibi("stand", "door", "base", flip=False)
    with d3
    pause .2

    cho "Yes?" ("soft", "base", "raised", "mid", xpos="base", flip=False)
    gen "Aren't you forgetting about something?" ("base", xpos="far_left", ypos="head")
    cho "Sir?" ("soft", "narrow", "base", "mid")
    gen "You're still naked...{w} I wouldn't go out there if I were you..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Oh, of course!" ("soft", "wide", "base", "mid", trans=hpunch)

    call cho_walk("desk", "base")
    pause .5
    call chibi_emote("thought", "cho")
    pause .8

    # Cho puts clothes back on.
    play sound "sounds/cloth_sound.ogg"
    hide cho_main
    $ cho.wear("all")
    hide screen cho_cloth_pile
    pause .8

    cho @ cheeks blush "(...)" ("disgust", "narrow", "worried", "down", xpos="right", ypos="base")
    cho @ cheeks blush "*Uhm*..." ("soft", "narrow", "worried", "mid")
    if game.daytime:
        cho @ cheeks blush "Have a good day..." ("soft", "base", "base", "R")
    else:
        cho @ cheeks blush "Have a good night..." ("soft", "base", "base", "R")

    # Cho leaves.
    call cho_walk(action="leave")

    gen "(She's so cute...)" ("base", xpos="far_left", ypos="head")
    gen "(And sexy!)" ("grin", xpos="far_left", ypos="head")
    gen "(But also a bit intimidating...)" ("base", xpos="far_left", ypos="head")

    jump end_cho_strip_event

label cc_pf_strip_T2_intro_E3:

    call cc_pf_strip

    gen "[name_cho_genie], how would you like to do another striptease for me?" ("grin", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "mid")
    gen "You did such a phenomenal job last time!" ("grin", xpos="far_left", ypos="head")
    cho "Another strip show?" ("soft", "narrow", "angry", "R")
    gen "Yes Indeed! Come a bit closer..." ("grin", xpos="far_left", ypos="head")
    cho "(...)" ("angry", "narrow", "base", "down")

    call cho_walk("desk", "base")

    cho "Sir, these favours... You said before that they're a part of my training..." ("soft", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    gen "Yes indeed, a very integral part in fact." ("base", xpos="far_left", ypos="head")
    cho "But, they're not the only type of training I'll be receiving, right?" ("annoyed", "narrow", "angry", "mid")
    gen "Expecting me to blow on a whistle and watch you run laps around the pitch all day?" ("base", xpos="far_left", ypos="head")
    gen "You're already a good athlete, if you want to get an edge, then what is required is approaching it differently." ("base", xpos="far_left", ypos="head")
    gen "My job is to figure out every possible angle, and which would result in you winning." ("base", xpos="far_left", ypos="head")
    cho "And seeing me strip is part of that?" ("annoyed", "narrow", "angry", "mid")
    gen "Your sexy and muscular physique is indeed a very useful asset in boosting your chance of success, yes." ("base", xpos="far_left", ypos="head")
    cho "So, the purpose of these favours were never about me repaying you for training me? It's about me learning how to whore myself out?" ("annoyed", "narrow", "angry", "mid")
    gen "Can't it be both?" ("base", xpos="far_left", ypos="head")
    gen "I get to partake in that hot bod of yours and in return, I teach you how to successfully use it on the pitch." ("base", xpos="far_left", ypos="head")
    gen "You've already seen how effective it's been. That Hufflepuffer could barely fly once the broom wasn't the only hard thing between--" ("base", xpos="far_left", ypos="head")
    cho "I get the point." ("open", "narrow", "angry", "mid")
    cho "But what I don't get is why you didn't just tell me this was the goal from the start, I never imagined that my training would involve...{w} this!" ("annoyed", "base", "worried", "down")
    gen "And not give you the opportunity to figure it out for yourself?!" ("base", xpos="far_left", ypos="head")
    gen "If I had told you, you would've never accepted my help to begin with, and you'd be sulking in your dorm and be out of the running for the cup by now." ("base", xpos="far_left", ypos="head")
    cho "You don't know that!" ("annoyed", "narrow", "worried", "downR")
    gen "Or punch a pillow, whatever it is you do when you're mad." ("base", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "narrow", "worried", "mid")
    gen "Now, unless there are any more objections, it's time we get back to your training." ("base", xpos="far_left", ypos="head")
    cho "*Hmph*... I can't believe this could even be considered \"training\"." ("annoyed", "narrow", "angry", "mid")
    gen "Well, it is a \"trainer\" after all..." ("base", xpos="far_left", ypos="head")
    cho "What?" ("annoyed", "narrow", "angry", "mid")
    gen "I'll consider incorporating some more physical training for you in the future." ("base", xpos="far_left", ypos="head")
    gen "Now, less talking, more stripping." ("base", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "narrow", "angry", "mid")
    pause .8

    # Remove top.
    if cho.is_worn("top"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("robe", "top")
        with d3
        pause .5

        cho @ cheeks blush "" ("quiver", "narrow", "worried", "R")
        call ctc

    cho @ cheeks blush "Does Granger do these sorts of things for you too?" ("soft", "base", "worried", "mid")

   # Remove skirt.
    if cho.is_worn("bottom"):
        play sound "sounds/cloth_sound3.ogg"
        hide cho_main
        $ cho.strip("bottom")
        pause 1.2
        play sound "sounds/cloth_sound4.ogg"
        show screen cho_cloth_pile
        pause .4
        cho "" (trans=d3)
        pause .5
        cho @ cheeks heavy_blush "" ("horny", "base", "worried", "mid")
        call ctc

    gen "She does a lot of things for me. You need to be more specific!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "I meant buying \"sexual favours.\"{w} Doing tasks that are, let's say, a little audacious..." ("soft", "narrow", "worried", "downR")
    gen "Are you talking about stripping, girl?" ("base", xpos="far_left", ypos="head")

    cho @ cheeks blush "Yes, Sir..." ("quiver", "narrow", "worried", "downR")
    pause .4

    # Check if Hermione has already stripped for you.
    if not states.her.status.stripping: # Triggers in hg_pf_strip_T3_intro_E2. This check needs to always be no earlier here to make sure Luna is also unlocked.
        if states.cho.ev.inspect_her_body.T2_E3_failed:
            $ _event.cancel()
            jump cc_pf_strip_T2_E3_fail_repeat
        else:
            $ _event.cancel()
            jump cc_pf_strip_T2_E3_fail

    # After you got Hermione to strip.

    $ states.cho.ev.inspect_her_body.T2_E3_complete = True

    gen "She does indeed." ("base", xpos="far_left", ypos="head")
    cho "Really?!{w} You got that cow to take off her clothes?" ("soft", "wide", "base", "mid")
    cho "Did you get any proof?" ("soft", "base", "worried", "mid")
    gen "What?{w} Why would I--" ("base", xpos="far_left", ypos="head")
    cho "To blackmail her!{w} To prove that she's in on this whole \"favour trading\" business too..." ("open", "narrow", "angry", "mid")
    gen "We had an eyewitness, for what it's worth..." ("base", xpos="far_left", ypos="head")
    cho "Seriously?! Who was it?" ("smile", "base", "base", "mid")
    gen "Snape..." ("base", xpos="far_left", ypos="head")
    cho "What?! Professor Snape?" ("scream", "wide", "base", "mid", trans=hpunch)
    cho "" ("smile", "wide", "base", "mid")
    gen "He sort of just walked in on the action.{w} After all, the door wasn't locked..." ("base", xpos="far_left", ypos="head")
    cho "That's too funny! I wish I could have been there!" ("smile", "base", "base", "R")
    gen "She was dancing on my desk, right here, butt naked!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "That sounds sooo embarrassing!" ("soft", "narrow", "worried", "up")
    gen "As far as I know... That door isn't locked right now either..." ("base", xpos="far_left", ypos="head")
    gen "Aren't you scared that Snape might walk in on you too?" ("base", xpos="far_left", ypos="head")
    cho "*Hmm*..." ("annoyed", "base", "base", "R")

    call hide_characters
    show screen blkfade
    with d3
    play sound "sounds/08_hop_on_desk.ogg"
    pause 3

    nar "You watch as Cho slowly climbs onto your desk..."

    call cho_chibi("stand", "on_desk", "on_desk")
    hide screen bld1
    hide screen blkfade
    with d3
    pause .8

    cho "I'm not scared at all, Sir!" ("smile", "narrow", "angry", "mid")
    cho "" ("horny", "narrow", "angry", "mid")
    pause .4

    # Remove bra.
    play sound "sounds/cloth_sound3.ogg"
    $ cho.strip("bra")
    with d3
    pause .5

    cho "" ("horny", "narrow", "angry", "mid")
    call ctc

    cho "It's just Professor Snape, after all..." ("soft", "narrow", "base", "R")
    cho "Everybody knows that he's a creep! Nobody would believe a word he says." ("open", "base", "angry", "down")
    gen "So...{w} what if it's not Snape, but some other teacher who makes their way in here?" ("base", xpos="far_left", ypos="head")
    cho "*Huh*?{w=0.5} Oh no!" ("soft", "wide", "base", "mid")
    cho @ cheeks blush "For a second I forgot we even had other teachers at this school!" ("open", "wide", "worried", "L")
    cho @ cheeks heavy_blush "What if Professor McGonagall stumbles in here while...{w} while I--" ("angry", "happyCl", "worried", "mid")


    call hide_characters
    show screen blkfade
    with d3
    pause 1.0

    play sound "sounds/jump_shoes.ogg"
    call cho_chibi("stand", "desk", "base", flip=True)
    hide screen bld1
    hide screen blkfade
    with d3
    call teleport(position="cho", effect=False)
    pause .5

    call bld
    gen "Don't worry. That won't happen." ("base", xpos="far_left", ypos="head")
    call cho_chibi("stand", "desk", "base")
    with d3
    pause .5

    cho @ cheeks blush "Are you sure, Sir?" ("soft", "narrow", "worried", "mid")
    gen "You have my word..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "O-{w=0.2}okay..." ("soft", "narrow", "worried", "R")
    gen "Now then, Miss Chang!{w} It's time for the grand finale..." ("base", xpos="far_left", ypos="head")
    gen "Take it all off!" ("grin", xpos="far_left", ypos="head")
    gen "I want to see you naked..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "(...)" ("annoyed", "base", "worried", "down")
    cho "Very well, Sir." ("base", "base", "base", "mid")
    pause .4

    # Remove panties + everything else.
    play sound "sounds/cloth_sound3.ogg"
    hide cho_main
    $ cho.strip("clothes")
    pause 1.2
    play sound "sounds/cloth_sound4.ogg"
    show screen cho_cloth_pile
    pause .6

    cho @ cheeks blush "" ("horny", "narrow", "base", "down")
    call ctc

    gen "I've got to say, once again... I'm very impressed by you!" ("angry", xpos="far_left", ypos="head")
    cho "Glad to hear it, [name_genie_cho]." ("smile", "narrow", "base", "mid")
    cho "Catch!" ("base", "base", "base", "L")
    nar "Cho throws her panties onto your desk."
    cho "You can keep them, for now..." ("soft", "narrow", "base", "R")
    gen "I appreciate the notion!" ("grin", xpos="far_left", ypos="head")
    cho "" ("base", "narrow", "base", "mid")
    pause .8

    # Panties Acquired
    $ states.cho.ev.panty_thief.acquired = True

    gen "Well then, Miss Chang..." ("base", xpos="far_left", ypos="head")
    gen "You may leave now.{w} Dismissed." ("base", xpos="far_left", ypos="head")
    cho "Wait, Sir!{w} I can't leave just yet!" ("open", "wide", "base", "mid")
    gen "Why not? Don't tell me you want points now after all..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "No Sir, but...{w} I don't believe we are done here..." ("mad", "base", "worried", "downR")
    gen "We aren't?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "May I request something of you, Sir?" ("soft", "narrow", "worried", "mid")
    gen "Yes?{w} What is it?" ("base", xpos="far_left", ypos="head")

    # Cho asks you to summon Hermione.
    cho @ cheeks blush "Could you please..." ("soft", "base", "worried", "downR")
    cho @ cheeks heavy_blush "*Ehm*..." ("quiver", "narrow", "worried", "downR")
    cho @ cheeks heavy_blush "Could you please summon Hermione?" ("soft", "narrow", "worried", "mid")

    with hpunch
    gen "What?" ("angry", xpos="far_left", ypos="head")
    cho "It's time someone throws \"high and mighty\" Granger off her high horse!" ("open", "narrow", "angry", "mid")
    cho "She's been a pain in my butt for years now..." ("angry", "narrow", "angry", "downR")
    cho "This is going to be my revenge!" ("soft", "narrow", "angry", "mid")
    gen "Are you sure that this is such a good idea? Aren't you scared she'll tattle about it?" ("base", xpos="far_left", ypos="head")
    cho "No.{w} Granger is clever..." ("soft", "closed", "base", "mid")
    cho "She could destroy my reputation, sure..." ("soft", "base", "base", "R")
    cho "But, should that happen, I now have the means to take her down with me!" ("base", "narrow", "angry", "mid")
    cho "I'm not the only one stripping for you, after all." ("soft", "narrow", "base", "mid")
    gen "I suppose you're right..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I can't believe how depraved Granger actually is..." ("horny", "narrow", "angry", "down")
    cho @ cheeks blush "Stripping for her headmaster.{w=0.6} What a slut..." ("soft", "narrow", "angry", "mid")
    gen "Aren't you doing exactly the same?" ("base", xpos="far_left", ypos="head")
    cho "Yes, but I'm not a whore stripping for points, unlike her!" ("open", "closed", "base", "mid")
    gen "Still makes you a slut..." ("base", xpos="far_left", ypos="head")
    cho "I'm untouchable! I'll show that {b}bitch{/b} she can't mess with me!" ("angry", "narrow", "angry", "R")
    cho "This is gonna be so much fun!" ("smile", "narrow", "angry", "mid")

    stop music fadeout 3.0
    call cho_walk(570, "base")
    pause 2.0

    cho "Call her already!" ("annoyed", "narrow", "angry", "R", flip=True, trans=d5)
    gen "I'm on it..." ("base", xpos="far_left", ypos="head")

    hide screen bld1
    show screen blkfade
    with d3
    hide cho_main
    pause 1.0
    hide screen blkfade
    with d3

    call cc_pf_strip_T2_E3_hermione

    jump end_cho_strip_event

label cc_pf_strip_T2_E3_repeat:

    call cc_pf_strip

    gen "[name_cho_genie], why don't you come a bit closer?" ("base", xpos="far_left", ypos="head")
    cho "Of course, [name_genie_cho]..." ("base", "narrow", "base", "mid")

    call cho_walk("desk", "base")

    cho "" ("base", "base", "base", "R", xpos="mid", ypos="base", trans=fade)
    call ctc

    gen "I'm in the mood for another striptease!" ("grin", xpos="far_left", ypos="head")
    cho "You are, are you?" ("soft", "base", "raised", "downR")

    # Remove robe.
    if cho.is_worn("robe"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("robe")
        with d3
        pause .5

        cho "Good, because so am I!" ("base", "narrow", "angry", "mid")
        cho "" ("base", "narrow", "angry", "mid")

    #Remove top.
    if cho.is_worn("top"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("top")
        cho "*Hmm*... You better be enjoying this, Sir." ("soft", "closed", "base", "mid")
        with d3
        pause .5

    #Remove bottoms.
    if cho.is_worn("bottom"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("bottom")
        with d3
        pause .5
        gen "*Argh!* You little minx!" ("angry", xpos="far_left", ypos="head")

    cho "Are we going to invite Granger again?" ("soft", "narrow", "raised", "down")
    cho "I would like to have some fun with her..." ("smile", "narrow", "angry", "mid")
    pause .4

    # Remove bra. (she is wearing underwear at this level in any case)
    if cho.is_worn("bra"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("bra")
        with d3
        pause .5

    gen "The more, the merrier!" ("grin", xpos="far_left", ypos="head")
    cho "" ("base", "narrow", "angry", "mid")
    pause .4

    # Remove panties + all else.
    play sound "sounds/cloth_sound3.ogg"
    $ cho.strip("clothes")
    hide cho_main
    $ cho.strip("clothes")
    pause 1.2
    play sound "sounds/cloth_sound4.ogg"
    show screen cho_cloth_pile
    pause .6
    cho "" (trans=d3)
    call ctc

    cho "Catch, [name_genie_cho]!" ("soft", "base", "base", "mid")
    nar "Cho throws her panties at you."

    # Panties Acquired
    $ states.cho.ev.panty_thief.acquired = True

    gen "Nice!" ("grin", xpos="far_left", ypos="head")
    cho "I'd like to have them back after this, mind you." ("soft", "base", "raised", "R")
    gen "Of course..." ("base", xpos="far_left", ypos="head")
    cho "Anything else you'd like, Sir?" ("base", "base", "base", "mid")

    $ d_flag_01 = False # Cho on desk flag for this event

    menu:
        "\"Hop on my desk!\"":
            $ d_flag_01 = True

            cho "Good idea, [name_genie_cho]!" ("base", "happyCl", "base", "mid")
            call hide_characters
            show screen blkfade
            with d3
            play sound "sounds/08_hop_on_desk.ogg"
            pause 2

            call cho_chibi("stand", "on_desk", "on_desk", flip=False)
            hide screen bld1
            hide screen blkfade
            with d3
            pause 1

            cho "How is the view down there, Sir?" ("base", "narrow", "base", "down")
            gen "Couldn't be any better!" ("grin", xpos="far_left", ypos="head")

            call hide_characters
            hide screen bld1
            with d3
            pause .2

            call cho_chibi("stand", "on_desk", "on_desk", flip=True) # Facing the door.
            with d3
            pause .8
            cho "Now, if you don't mind, Sir..." ("soft", "base", "base", "R", xpos="mid", ypos="base", flip=True)
            cho "I'd like you to call that Gryffindor slut to your office!" ("soft", "base", "base", "L")

        "\"Let Granger have a good look at you!\"":
            cho "I'll make sure of it, Sir!" ("soft", "narrow", "angry", "mid")

            call cho_walk(570, "base")
            cho "Alright, you can call her now." ("soft", "base", "base", "R", xpos="mid", ypos="base", flip=True)


    gen "On it!" ("grin", xpos="far_left", ypos="head")
    pause .8
    cho "(...)" ("annoyed", "narrow", "angry", "L")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    call hide_characters
    hide screen bld1
    with d3
    pause .5

    call cc_pf_strip_T2_E3_hermione_repeat

    jump end_cho_strip_event

label cc_pf_strip_T2_E3_fail:
    # Cho demands that you get Hermione to strip, so Cho has something to blackmail her should anything happen.
    # Cho gets dressed again and storms off.

    $ states.cho.ev.inspect_her_body.T2_E3_failed = True

    gen "Actually, she doesn't..." ("base", xpos="far_left", ypos="head")
    cho "What? But I thought she'd--" ("soft", "wide", "base", "mid")
    cho "Why do you ask me to do these favours, and not Granger?" ("open", "narrow", "angry", "mid", trans=hpunch)
    gen "Let's just say, she isn't as progressive as you...{w} yet." ("base", xpos="far_left", ypos="head")
    cho "You haven't even seen her naked?" ("angry", "base", "base", "mid")
    cho "What favours are you even buying from her?" ("open", "base", "angry", "mid")
    gen "Just chit-chats, mostly..." ("base", xpos="far_left", ypos="head")
    cho "Make her strip too!" ("clench", "narrow", "angry", "mid")
    gen "It's not that easy, girl!" ("angry", xpos="far_left", ypos="head")
    cho "Then get on with it!" ("angry", "closed", "angry", "mid")
    cho "What's the worst that could happen?" ("soft", "narrow", "angry", "R")
    gen "She could report me, and I'd get kicked out of this school, most likely." ("base", xpos="far_left", ypos="head")
    gen "She's reported me to that ministry before..." ("base", xpos="far_left", ypos="head")
    cho "The \"Ministry of Magic\"?" ("open", "base", "raised", "mid")
    cho @ cheeks blush "If they were to regulate the school rules more strictly, my chance of winning the Quidditch cup would be back down to zero!" ("angry", "wide", "worried", "mid")
    cho @ cheeks blush "And if Granger ever was to find out about me stripping for our headmaster, it would mean the end of my Quidditch career for sure!" ("mad", "base", "worried", "downR")
    gen "So? What do you suggest we do?" ("base", xpos="far_left", ypos="head")
    cho "Isn't it obvious?! Ask her to do more advanced favours!" ("soft", "narrow", "angry", "mid")
    cho "If I could get a hold of something to blackmail her with, she'd never dare to report to the ministry!" ("clench", "narrow", "angry", "R")
    gen "That doesn't sound too bad of an idea..." ("base", xpos="far_left", ypos="head")
    cho "Until then, don't expect me to undress for you..." ("soft", "narrow", "angry", "mid")
    gen "(Bollocks...)" ("base", xpos="far_left", ypos="head")
    cho "" ("annoyed", "closed", "angry", "mid")
    pause .5

    # play sound "sounds/cloth_sound.ogg" #The player could technically have taken her top and bottoms off in wardrobe (Unless we change things)
    $ cho.wear("all")
    hide screen cho_cloth_pile
    cho "" ("annoyed", "narrow", "angry", "mid")
    pause .8

    cho "Good day, Sir!" ("soft", "narrow", "angry", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_event

label cc_pf_strip_T2_E3_fail_repeat:
    gen "So, how about that striptease then?" ("base", xpos="far_left", ypos="head")
    cho "Oh, already?" ("open", "base", "base", "mid")
    cho "I didn't think you'd get her to do it so soon." ("smile", "narrow", "base", "R")

    call cho_walk("desk", "base")

    # Remove top.
    if cho.is_worn("top", "robe"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("robe", "top")
        with d3
        pause .5

    gen "Her to do--{w=0.2} I mean, of course, Work smart, not when you're hard and all that..." ("base", xpos="far_left", ypos="head")

    # Remove skirt.
    if cho.is_worn("bottom"):
        play sound "sounds/cloth_sound3.ogg"
        hide cho_main
        $ cho.strip("bottom")
        pause 1.2
        play sound "sounds/cloth_sound4.ogg"
        show screen cho_cloth_pile
        pause .4
        cho "" (trans=d3)
        pause .5
        cho @ cheeks heavy_blush "" ("horny", "base", "worried", "mid")
        call ctc

    cho "I knew she was just putting up a front..." ("smile", "base", "base", "R")
    cho "I bet she shaves down there, just like everyone else..." ("open", "closed", "base", "mid")
    gen "Yeah, probably." ("base", xpos="far_left", ypos="head")
    cho "Wait, what do you mean \"probably\", did Granger strip for you or not?!" ("open", "narrow", "angry", "mid")
    gen "About that..." ("base", xpos="far_left", ypos="head")
    cho "Wait, she didn't?!" ("clench", "narrow", "angry", "mid")
    cho "Then why are you asking me to do this again?" ("angry", "narrow", "angry", "mid")
    gen "Come on, just pop out a titty or something!" ("base", xpos="far_left", ypos="head")
    cho "No!"

    # play sound "sounds/cloth_sound.ogg" #The player could technically have taken her top and bottoms off in wardrobe (Unless we change things)
    $ cho.wear("all")
    hide screen cho_cloth_pile
    cho "" ("annoyed", "narrow", "angry", "mid")
    pause .8

    $ renpy.choice_for_skipping()

    cho "I don't want Granger to report me to the stupid ministry, so unless you get her to take her clothes off--" ("soft", "narrow", "angry", "R")
    cho "I won't be \"poppin\" any titties." ("open", "narrow", "angry", "mid")

    gen "(Maybe if I get Hermione to {b}strip for me{/b}, she won't have the leverage over Cho... )" ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_event

