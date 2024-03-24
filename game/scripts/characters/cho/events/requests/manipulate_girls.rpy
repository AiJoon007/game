

### Manipulate the enemy female Quidditch players ###

### Start ###
label cc_pr_manipulate_girls_start:

    cho "" (xpos="right", ypos="base", trans=fade)

    if not states.cho.ev.manipulate_girls.t3_e1_complete: # Completed Alicia Spinnet?
        # Alicia Spinnet

        if not states.cho.ev.spy_on_girls.t3_e2_complete:
            # Return if player has not spied on Alicia just yet.
            gen "Let’s try and manipulate the girls on the enemy team!" ("base", xpos="far_left", ypos="head")
            cho "You're expecting me to just jump in blind?" ("angry", "base", "base", "mid")
            cho "I don't know any of these girls, how do you expect me to manipulate them in any way without knowing what I'm dealing with?" ("annoyed", "wide", "base", "mid")
            gen "Good point, perhaps we should consider spying on them a bit beforehand." ("base", xpos="far_left", ypos="head")

            cho "" (xpos="base", ypos="base", trans=fade)

            $ _event.cancel()
            jump cho_favor_menu

        gen "I think it's time to manipulate the female members of the enemy team a bit, and see if we can find some way to distract them during the game." ("base", xpos="far_left", ypos="head")
        cho "And how do you suggest we do that?" ("annoyed", "base", "raised", "mid")
        gen "Well, the Slytherin \"brutes\" seemed to think they had a pretty good chance to get with you during the last game." ("base", xpos="far_left", ypos="head")
        cho "They're idiots though, I barely had to do anything." ("soft", "base", "base", "R")
        gen "Which means it's even more important to try and entice those girls before the match itself..." ("base", xpos="far_left", ypos="head")
        cho "..." ("disgust", "base", "raised", "down")
        gen "It's all about throwing them off their game, like you said..." ("base", xpos="far_left", ypos="head")
        gen "If the girls won't get thrown off by you wearing some outfit, then maybe an emotional... bond... would be more appropriate." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Don't you think we'd have an easier time focusing on the boys?" ("upset", "base", "base", "mid")
        gen "Sometimes the hard route is the right one to take... You shouldn't dismiss it." ("base", xpos="far_left", ypos="head")
        gen "(Since those girls sound freaky...)" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "But Harry is the seeker and Ron is the keeper... Wouldn't it be more useful if--" ("open", "wide", "base", "mid")
        gen "I'm certain my reasoning is correct here, are you questioning your trainer?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("upset", "base", "base", "R")
        cho "No..." ("open", "base", "base", "R")
        gen "Great, then off you go..." ("grin", xpos="far_left", ypos="head")
        gen "Time to make your team proud!" ("grin", xpos="far_left", ypos="head")
        gen "Pride is important!" ("grin", xpos="far_left", ypos="head")
        cho "...{w} I suppose..." ("soft", "base", "base", "mid")
        cho "Wish me luck..." ("horny", "base", "base", "mid")
        gen "Good luck..." ("grin", xpos="far_left", ypos="head")

    elif not states.cho.ev.manipulate_girls.t3_e2_complete: # Completed Katie Bell - Part 1?
        # Katie Bell - Part 1

        if not states.cho.ev.spy_on_girls.t3_e3_complete:
            # Return if player has not spied on Katie just yet.
            gen "Let's try and manipulate--" ("base", xpos="far_left", ypos="head")
            cho "I'm going to stop you right there..." ("soft", "base", "angry", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            cho "There's no way I'll try this again before I know more about the girls." ("annoyed", "base", "angry", "mid")
            gen "Why? I thought it went great with the Spinnet girl!" ("base", xpos="far_left", ypos="head")
            cho "She cornered me!" ("scream", "wide", "angry", "mid")
            gen "And?" ("base", xpos="far_left", ypos="head")
            cho "I'm not going to attempt the other two unless I know a bit more about them..." ("upset", "base", "angry", "R")
            gen "Fine..." ("base", xpos="far_left", ypos="head")


            cho "" (xpos="base", ypos="base", trans=fade)

            $ _event.cancel()
            jump cho_favor_menu

        gen "One down, two to go..." ("base", xpos="far_left", ypos="head")
        gen "I think it's time to manipulate one of the other Gryffindor girls." ("base", xpos="far_left", ypos="head")
        cho "Who do you want me to target this time?" ("open", "base", "raised", "mid")
        gen "Katie Bell!" ("base", xpos="far_left", ypos="head")
        cho "So, we're still set on targeting the girls?" ("upset", "base", "raised", "mid")
        gen "Of course, I'm sure we got but a taste last time...{w=0.4} No pun intended." ("grin", xpos="far_left", ypos="head")
        cho "..." ("angry", "closed", "base", "mid")
        gen "I hope you've  remembered what you learned from her. This girl likes being treated rough, so show some assertiveness with her, and I'm sure she'll fall for you." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Okay..." ("open", "narrow", "base", "down") #looking down a bit worried
        gen "Assertiveness!" ("grin", xpos="far_left", ypos="head")
        cho "..." ("clench", "base", "raised", "mid") #Changes from worried looking down to looking at genie
        cho "Yes, I will!" ("mad", "base", "raised", "mid")
        gen "Great, off you go!" ("grin", xpos="far_left", ypos="head")

    elif not states.cho.ev.manipulate_girls.t3_e3_complete: # Completed Katie Bell - Part 2?
        # Katie Bell - Part 2

        # No return here since it's just a continuation of previous Katie event.

        gen "Follow that girl again!" ("base", xpos="far_left", ypos="head")
        cho "Sir?" ("mad", "base", "raised", "mid")
        gen "I mean... Today's mission is to follow that Bell girl again..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "But... isn't one time enough?" ("disgust", "narrow", "base", "mid")
        cho @ cheeks blush "My butt is still sore from last time..." ("clench", "narrow", "base", "downR")
        gen "There can never be too much of a good thing." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Fine..." ("open", "narrow", "base", "down")
        gen "Excellent, make sure to come back with an extensive report as usual B." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Got it..." ("soft", "base", "base", "mid")

    elif not states.cho.ev.manipulate_girls.t3_e4_complete: # Completed Angelina Johnson?
        # Angelina Johnson

        if not states.cho.ev.spy_on_girls.t3_e4_complete:
            # Return if player has not spied on Angelina just yet.
            gen "Let's try and manipulate--" ("base", xpos="far_left", ypos="head")
            cho "I'm going to stop you right there..." ("soft", "base", "angry", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            cho "There's no way I’ll try this again before I know more about the girls." ("annoyed", "base", "angry", "mid")
            gen "Fine..." ("base", xpos="far_left", ypos="head")

            cho "" (xpos="base", ypos="base", trans=fade)

            $ _event.cancel()
            jump cho_favor_menu

        gen "You seem to have gotten to know the Gryffindor girls quite well by now, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
        gen "If you're not careful, you might turn into one yourself." ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "As if... Ravenclaw always comes first!" ("angry", "base", "base", "mid")
        gen "You do? No shame in that!" ("grin", xpos="far_left", ypos="head")
        gen "So...{w=0.4} Today we're up against their team Captain, Angelina Johnson." ("base", xpos="far_left", ypos="head")
        gen "Once you've managed to bond with her, I'm sure you'll have no problem winning the cup." ("base", xpos="far_left", ypos="head")
        cho "Yes!" ("grin", "closed", "base", "mid")
        cho "We're so close, I can almost taste it!" ("horny", "happyCl", "base", "mid")
        gen "I'm sure you will!" ("grin", xpos="far_left", ypos="head")
        gen "Now, go get her..." ("grin", xpos="far_left", ypos="head")
        cho "Yes [name_genie_cho]!" ("smile", "base", "base", "R")
    else:
        # Repeatable events.

        gen "Let's manipulate those girls some more!" ("base", xpos="far_left", ypos="head")
        cho "More? Haven't I done it enough already?" ("clench", "base", "raised", "mid")
        gen "There's always room for more bonding." ("base", xpos="far_left", ypos="head")
        cho "Okay then..." ("open", "base", "raised", "down")
        gen "Make sure to bring me your report as usual B." ("base", xpos="far_left", ypos="head")
        cho "Yes [name_genie_cho]!" ("base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_event

### Return Events ###

### Tier 3 (pre Gryffindor) ###

label cc_pr_manipulate_girls_T3_alicia:

    $ states.cho.ev.manipulate_girls.t3_e1_complete = True
    # Alicia Spinnet
    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho @ cheeks blush "" ("normal", "narrow", "base", "down", xpos="mid", ypos="base", trans=fade)

    gen "Back so soon? I wasn't expecting you for another hour." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("normal", "narrow", "base", "down") #Blushing
    gen "Are you alright? How did it go with the girls?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Fine..." ("open", "narrow", "base", "down") #Blush
    gen "So, did you manage to connect with them in an emotional way?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("annoyed", "closed", "base", "mid")
    gen "Miss Chang?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "You could say that." ("upset", "narrow", "base", "mid")
    gen "Tell me what happened." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well..." ("disgust", "base", "base", "R")
    cho @ cheeks blush "My plan was to try and approach Alicia Spinnet without the other two around." ("open", "base", "base", "down")
    cho @ cheeks blush "So, I gestured her to come over to me as the other two entered the changing room..." ("open", "base", "raised", "mid")
    gen "Nicely done. Splitting up the group makes it less likely they'll gang up on you." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "That's what I thought... and I felt pretty confident in my plan as she approached me." ("soft", "closed", "base", "mid")
    cho @ cheeks blush "But before I even got a word out, she had come up and kissed me on the lips!" ("quiver", "base", "raised", "mid")
    gen "Whoa, wait what?" ("angry", xpos="far_left", ypos="head")
    gen "I thought the plan was for you to make the advances here..." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "You and me both!" ("clench", "base", "raised", "mid")
    gen "Do you know why she just came up and kissed you like that?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well, apparently she saw me when I entered the girls' bathroom..." ("horny", "base", "base", "R")
    cho @ cheeks blush "She must've assumed that I had followed her there to get in on the action..." ("annoyed", "narrow", "base", "mid")
    gen "Smart girl. She figured out you were perving on her!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "I'm not perving on anybody! I only followed her into that bathroom to gather information!" ("horny", "happyCl", "angry", "mid")
    gen "But I'm sure you liked sneaking a peek at her moist muff, regardless." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "How was I to know she wasn't wearing any panties..." ("clench", "closed", "angry", "mid") # annoyed
    gen "Be that as it may, this Alicia girl seems to be one step ahead of us..." ("base", xpos="far_left", ypos="head")
    gen "So, what happened next, B?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "She started kissing me again, and placed a hand on one of my butt cheeks..." ("angry", "narrow", "base", "down")
    gen "Correction, she's two steps ahead of us..." ("base", xpos="far_left", ypos="head")
    gen "Sounds to me like you got a fan on the Gryffindor team..." ("base", xpos="far_left", ypos="head")
    gen "That girl has the hots for you, that's for sure!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "*Tzzs!*... Those sluts would probably make out with anybody..." ("clench", "closed", "raised", "downR")
    gen "Tongue or no tongue?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Sorry?" ("normal", "base", "raised", "mid") #Blush, shocked
    gen "Did she slip you any tongue or what?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "How is that relevant to anything?" ("upset", "base", "base", "downR")
    gen "Did she though?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("normal", "base", "raised", "down") #blush
    gen "I knew it!" ("grin", xpos="far_left", ypos="head")
    gen "I hope you were at least courteous enough to return the favour..." ("grin", xpos="far_left", ypos="head")
    gen "Tongue kissing and a butt squeeze... Now that's what I'd call a true challenger!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("base", "narrow", "base", "down") #Glaring
    gen "What happened next?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "She broke off the kiss and slapped my butt cheek, before running off to the changing rooms." ("angry", "base", "base", "mid")
    gen "Sounds to me like a job well done, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "But I didn't even do anything!" ("clench", "wide", "base", "mid")
    gen "Yet you achieved exactly what I asked of you, you formed an emotional bond with her." ("base", xpos="far_left", ypos="head")
    gen "Now we only have to do the same with the other two..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "So that's what this emotional bonding is all about? Getting them to kiss me?" ("mad", "narrow", "raised", "mid")
    gen "Not kissing specifically..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("annoyed", "closed", "base", "down")
    gen "And now I'd like you to entice the other two as well." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Sure, no problem... I'll just walk up to one of them, and they'd throw themselves at me, just like Spinnet did!" ("normal", "narrow", "angry", "R") #Sarcastic
    gen "Great plan!" ("base", xpos="far_left", ypos="head")
    gen "But for now, you better get some rest and ready yourself to take on the other two." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("disgust", "narrow", "base", "down")
    gen "Don't look so dejected, [name_cho_genie]. You had a beautiful girl kiss you today... surely you can't be disappointed by that?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "It's...{w=0.4} it's not that...{w=0.4} I'm just used to it being me who..." ("annoyed", "closed", "base", "mid")
    cho @ cheeks blush "..." ("upset", "closed", "base", "mid") #Blush
    cho @ cheeks heavy_blush "Never mind, good night then." ("normal", "base", "base", "downR")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_katie_part1:

    $ states.cho.ev.manipulate_girls.t3_e2_complete = True

    # Katie Bell - Part 1

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho @ cheeks blush "..." ("normal", "narrow", "base", "down", xpos="mid", ypos="base", trans=fade)

    gen "[name_cho_genie]?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("normal", "narrow", "base", "down")
    gen "Hello?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Oh... Sorry [name_genie_cho]!" ("upset", "closed", "base", "mid") #face more focused still blushing
    gen "What's the report. Did you manage to bond with the girl?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Of course..." ("angry", "narrow", "base", "down")
    gen "Then how did it go? Tell me all the details!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "All the details..." ("upset", "closed", "base", "mid")
    cho @ cheeks blush "So...{w=0.4} Much like before, my plan was to follow Katie as she wandered off, away from the others." ("open", "base", "base", "mid")
    cho @ cheeks blush "And to no surprise... She was once again making her way down towards the lake." ("soft", "narrow", "base", "R")
    cho @ cheeks blush "So I ran up to her and questioned her about where she was headed, and she responded that she was just going for a walk to clear her head." ("open", "narrow", "base", "mid")
    gen "Yeah right..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "That's what I said..." ("clench", "narrow", "base", "R")
    cho @ cheeks blush "So, to try and catch her off guard, I bluntly asked her if she wasn't going for another round with those tentacles." ("open", "base", "raised", "mid")
    gen "Whoa, right to the point!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes, although she didn't even respond to it, and just started walking again..." ("angry", "base", "base", "mid")
    cho @ cheeks blush "So I pushed her further, and asked what the Gryffindor house would think if they knew..." ("soft", "base", "angry", "mid")
    cho @ cheeks blush "But she just kept walking, completely ignoring me." ("upset", "base", "angry", "mid")
    cho @ cheeks blush "I wasn't able to get through to her at all until I said that I would snitch to her captain, unless she did something for me." ("clench", "narrow", "base", "mid")
    cho @ cheeks blush "That's when she stopped in her tracks, eyed me up and down and asked what her punishment was going to be." ("disgust", "base", "base", "down")
    gen "Such a naughty girl!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "I know! That's not at all where I was going with the conversation." ("open", "wide", "angry", "mid")
    cho @ cheeks blush "What I hadn't realised during my failed attempts at confronting her, it that she had been leading me off the path." ("clench", "base", "base", "downR")
    cho @ cheeks blush "Because just as I was about to reply, I felt something tighten around my waist, and suddenly, I found myself dangling several feet off the ground!" ("open", "wide", "base", "mid")
    cho @ cheeks blush "That's when I realised, she had led me all the way to the Whomping Willow!" ("clench", "happyCl", "angry", "mid")
    gen "The whomping what?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "That darn tree, students are told to stay away from..." ("upset", "base", "angry", "mid")
    cho @ cheeks blush "It had grabbed both Katie and me, and then lifted us into the air... I thought we were done for." ("angry", "narrow", "base", "mid")
    cho @ cheeks blush "And for a brief moment, we just dangled there, until the silence was cut short by a loud snapping sound and a yell." ("clench", "base", "base", "mid")
    gen "Terrifying!" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "It was! Until I realised the tree wasn't even trying to kill us..." ("upset", "closed", "angry", "mid")
    cho @ cheeks blush "It had started to vigorously lash its branches about, smacking Katie...{w} and to my horror, she was thoroughly enjoying the whole thing." ("disgust", "base", "base", "mid")
    gen "A spanking tree? Seriously?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes!{w=0.4} And I'm sure this wasn't her first time doing this!" ("clench", "base", "raised", "mid")
    cho @ cheeks blush "I couldn't believe what I was seeing, I just stared at her in disbelief..." ("disgust", "base", "base", "down")
    cho @ cheeks blush "And at that moment, the tree--" ("upset", "happyCl", "angry", "mid")
    cho @ cheeks blush "Smacked one of its branches across my breasts and stomach..." ("clench", "base", "angry", "mid")
    gen "Surely a little bit of spanking wouldn't bother a girl as tough as you, would it?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Of course it doesn't! I've taken plenty of bruises playing Quidditch, I was just taken by surprise..." ("disgust", "base", "base", "mid")
    cho @ cheeks blush "Once I got over that initial shock, the tree swiftly moved me, right up next to Katie." ("mad", "narrow", "base", "downR")
    cho @ cheeks blush "And I watched as it continuously smacked her with its branches..." ("soft", "happyCl", "base", "down")
    gen "I bet she knew you were looking." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Obliviously... No doubt she was enjoying it even more than the spanking." ("annoyed", "base", "angry", "mid")
    cho @ cheeks blush "And seeing that she was enjoying the attention so much, I decided to revert back to the original plan..." ("angry", "base", "base", "R")
    cho @ cheeks blush "Your plan..." ("disgust", "base", "base", "down")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "To form an emotional bond with her instead..." ("disgust", "closed", "base", "mid")
    gen "Finally took that stick out of your butt, did you?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "What? There was no stick up my butt!" ("mad", "base", "angry", "mid")
    gen "Figuratively speaking...{w=0.4} All that matters is that you finally accepted that you were enjoying yourself." ("base", xpos="far_left", ypos="head")
    gen "Now you can forever cherish this moment with Katie... and that spanking willow." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Whomping, Sir." ("annoyed", "narrow", "angry", "mid")
    cho @ cheeks heavy_blush "And I just took it for what it was... Endurance training! There's nothing wrong with that..." ("upset", "base", "base", "mid")
    gen "Whatever you want to call it, I do it at least once or twice a day, myself." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Anyhow... After a couple more minutes, the tree finally stopped smacking us, and I was able to catch my breath..." ("angry", "base", "base", "mid")
    gen "Sounds like a great workout." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes, it was a workout and a half, that's for sure!" ("horny", "base", "base", "down")
    gen "Then maybe we should incorporate it into your training." ("base", xpos="far_left", ypos="head")
    cho "But Sir, the Whomping Willow is still extremely dangerous!" ("mad", "wide", "raised", "mid")
    cho "Everybody knows to stay as far away from it as possible!" ("open", "wide", "base", "mid")
    gen "Because of a little ass spanking? Don't be silly..." ("base", xpos="far_left", ypos="head")
    gen "That Katie girl sure took it like a champ... you need to be fearless as well, next time that tree spanks you red!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Next time?" ("clench", "base", "base", "mid")
    gen "Just agree on a safe-word, if it gets too much." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "It's a tree! It's not going to agree to anything!" ("clench", "wide", "base", "mid")
    cho @ cheeks blush "She tricked me into this!" ("scream", "base", "angry", "R")
    gen "..." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "I bet I ruined it anyway..." ("annoyed", "base", "angry", "R")
    cho @ cheeks blush "Because as soon as the tree lowered us back to the ground, Katie rushed off." ("upset", "base", "base", "downR")
    cho @ cheeks blush "So I couldn't even talk to her..." ("clench", "base", "base", "down")
    gen "You're kidding me? Talking would've just ruined it at that point!" ("grin", xpos="far_left", ypos="head")
    gen "You just had an amazing experience together, and didn't exchange a word throughout the entire thing. There's no better emotional bonding than that..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("mad", "happyCl", "base", "down") #Blushing
    gen "Well, I'd say we're one step closer to taking on the Lions for the finals." ("base", xpos="far_left", ypos="head")
    gen "I'm confident you'll be able to tame those lionesses by then." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "I...{w=0.4} of course..." ("open", "happyCl", "base", "mid") #Smiles and blushes
    gen "You should take some rest now..." ("base", xpos="far_left", ypos="head")
    gen "You look beat." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Very well... Good night then." ("annoyed", "narrow", "base", "down")
    gen "Until next time." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_katie_part2:

    $ states.cho.ev.manipulate_girls.t3_e3_complete = True

    # Katie Bell - Part 2

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "Welcome back, any progress?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "If your goal was to get my ass red raw again then sure, plenty of progress..." ("angry", "narrow", "base", "R")
    gen "Progress is progress... So, what went down today?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I followed Katie again... just as you wanted..." ("annoyed", "base", "base", "down")
    cho @ cheeks blush "I attempted to strike up another conversation, but just like last time, she wasn't really up for chatting..." ("open", "base", "base", "mid")
    cho @ cheeks blush "So, since she was giving me the silent treatment, I asked her if this was another attempt of hers to trick me again." ("open", "closed", "base", "mid")
    cho @ cheeks blush "But she simply shrugged and said that if I was to join her again, then I should just be quiet and follow her..." ("open", "base", "raised", "mid")
    gen "And, did you?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well, yes..." ("disgust", "base", "base", "down")
    cho @ cheeks blush "Since she put it like that, how could I refuse? I'd look like a total wimp!" ("upset", "base", "angry", "mid")
    cho "I mean... It's only a giant, half-conscious, murderous tree... What's the worst that could happen?" ("annoyed", "base", "angry", "mid")
    cho @ cheeks blush "Having said that...{w=0.4} It ended up being even more intense than last time!" ("clench", "base", "base", "R")
    cho @ cheeks blush "Maybe Katie jinxed it this time around... or she forgot to jinx it... who knows." ("soft", "base", "base", "down")
    cho @ cheeks blush "It yanked us into the air with such speed, even I wasn't ready for it!" ("angry", "base", "raised", "mid")
    cho @ cheeks blush "I had to fight its grip, to at least get some form of control back..." ("horny", "base", "base", "downR")
    cho @ cheeks blush "But that was easier said than done, as the tree had already snaked some of its branches underneath my clothes... sliding them right off my body." ("soft", "narrow", "base", "down")
    gen "Nice! Just like that?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well, I tried to grab them... But it had already moved its branches away from me..." ("mad", "base", "base", "mid")
    gen "What happened to your reflexes... Are you being bested by a tree now?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "No. I simply let it do its thing to...{w=0.4} impress Katie..." ("upset", "narrow", "base", "downR")
    cho @ cheeks heavy_blush "I'm sure she didn't mind that her clothing got taken off as well... that slut." ("open", "wide", "angry", "mid")
    gen "(As well?)" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Just eyeing me up and down like a piece of meat... And that's when..." ("clench", "base", "base", "R")
    gen "Yes?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "That's when the tree threw one of its branches about and swung it at us, smacking our butts..." ("soft", "happyCl", "base", "mid")
    gen "Got to bless mother nature!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "And It just kept doing it, over and over, until our cheeks turned all red..." ("clench", "base", "base", "downR")
    cho @ cheeks blush "It was as if my body had caught on fire!" ("horny", "narrow", "base", "down")
    cho @ cheeks blush "As it continued, Katie looked up at me and reached out to grab my hand..." ("soft", "narrow", "base", "down")
    cho @ cheeks blush "And as I finally managed to grab it, the tree smacked us hard across our cheeks." ("angry", "narrow", "base", "downR")
    cho @ cheeks blush "And with that pain came a sudden rush of relief as Katie tightened her hand around mine." ("smile", "narrow", "base", "down")
    gen "An orgasm, Miss Chang?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "It...{w=0.4} yes, I think she might've." ("upset", "base", "base", "mid")
    gen "Still too early to admit it?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Too early to admit what?" ("mad", "base", "base", "mid")
    gen "Never mind... did anything else happen after that?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Not much, as far as I recall..." ("base", "base", "base", "downR")
    cho @ cheeks blush "All I remember is the tree lowering us to the ground and the sound of Katie's breathing..." ("soft", "closed", "base", "mid")
    cho @ cheeks blush "I just laid there for a while, catching my breath, until the only thing I could hear was the sound of the surrounding forest..." ("open", "closed", "base", "mid")
    gen "Almost sounds poetic." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Once I recovered, I turned to face Katie, but once again, she had already gone..." ("angry", "narrow", "base", "down")
    gen "Now that's how it's done!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Thank you!" ("smile", "base", "base", "mid")
    gen "That shall be all for today..." ("base", xpos="far_left", ypos="head")
    gen "You may leave now. Dismissed." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Good night then." ("base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_angelina:

    $ states.cho.ev.manipulate_girls.t3_e4_complete = True

    # Angelina Johnson
    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho @ cheeks blush "" ("normal", "narrow", "base", "down", xpos="mid", ypos="base", trans=fade)

    if game.weather == "rain":
        gen "Whoa, you're soaking!" ("angry", xpos="far_left", ypos="head")
        cho @ cheeks blush "Oh, yes... I guess my clothes ended up a little wet..." ("base", "narrow", "base", "down") #Blushing
    else:
        gen "Welcome back..." ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("normal", "base", "base", "downR")
        gen "You look soaked." ("angry", xpos="far_left", ypos="head")
        cho @ cheeks blush "Oh, yes... I guess my clothes ended up a little wet..." ("base", "narrow", "base", "down") #Blushing
        gen "How? It's not even raining!" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "*Ehm*..." ("disgust", "narrow", "base", "mid")

    gen "So, do you have that report for me?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I...{w=0.3} yes..." ("horny", "base", "base", "downR")
    gen "I'm waiting [name_cho_genie]... give me the {i}deets{/i}." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Of course!" ("open", "happyCl", "base", "mid")
    cho @ cheeks blush "Well...{w=0.4} I went to see if I could catch Angelina talking to Madam Hooch again." ("soft", "base", "base", "down")
    cho @ cheeks blush "I was determined to get the full context of what was going on this time!" ("open", "base", "base", "mid")
    cho @ cheeks blush "I immediately went and hid in the boys changing room as soon as they had gone for lunch to listen in." ("soft", "base", "base", "L")
    cho @ cheeks blush "Although I got there a bit early, and they were still in the showers, touching each other, and gossiping..." ("upset", "base", "base", "mid")
    gen "Hooch and Johnson?!" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "No, the girls on the Gryffindor team!" ("clench", "narrow", "base", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "So, doing my best to eavesdrop on their conversation, I went up to that hole I told you about." ("angry", "closed", "base", "mid")
    cho "After a while, as Angelina brought up the subject of spying to the other two, Alicia replied that she was already aware." ("open", "base", "base", "mid")
    cho "Katie then chimed in, saying she knew about it as well." ("soft", "base", "base", "mid")
    cho "Which seemed to surprise Angelina at first, but she then moved on, saying that they need to form some sort of plan." ("open", "base", "base", "mid")
    gen "I bet Miss Johnson didn't think her friends had been keeping anything secret from her..." ("base", xpos="far_left", ypos="head")
    cho "For sure..." ("soft", "base", "base", "R")
    gen "So, did they come up with a plan?" ("base", xpos="far_left", ypos="head")
    cho "Well, sort of..." ("open", "narrow", "base", "down")
    cho "Katie had obviously already thought about it, since she immediately responded that she knew exactly how to deal with it..." ("soft", "base", "base", "mid")
    cho "But as I waited to find out what it was, they suddenly went quiet, and I couldn't hear any of them." ("angry", "base", "raised", "mid")
    gen "Left for the changing room?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "That's what I thought, until I removed my ear from the hole to have a look..." ("disgust", "base", "base", "down")
    cho @ cheeks blush "No, they hadn't left... when I took a peek through the hole I found all three of them staring back at me..." ("open", "wide", "base", "mid")
    gen "Busted!" ("grin", xpos="far_left", ypos="head")
    gen "So what did you do, run away?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "At first I just sort of stood there in shock, not knowing what to do..." ("clench", "narrow", "base", "down")
    cho @ cheeks blush "Until Angelina angrily beckoned me to get in there." ("clench", "base", "base", "downR")

    gen "There goes our plan to separate them from each other..." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "Let me finish!" ("angry", "happyCl", "base", "mid")
    cho @ cheeks blush "Once I got in there, and before Angelina got a chance to do anything, Spinnet came up to me..." ("upset", "base", "base", "down")
    cho @ cheeks blush "And just like before, she leaned in and kissed me!" ("normal", "wide", "base", "mid")
    gen "Nice! And you kissed her back?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Of course! I wasn't about to blow my cover, was I?" ("upset", "base", "angry", "mid")
    gen "Of course..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "As she kissed me, Angelina shouted at her, asking what the hell she was doing." ("mad", "closed", "base", "mid")
    cho @ cheeks blush "Alicia then broke off the kiss and turned to her, asking what the problem was..." ("soft", "narrow", "base", "downR")
    cho @ cheeks blush "Angelina just sort of stared, dumbfounded at us, until she shouted that I'm the seeker of an enemy team." ("clench", "base", "base", "mid")
    gen "..." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "I honestly thought it was over at that point, but that's when Katie chimed in--" ("soft", "closed", "base", "down")
    cho @ cheeks blush "--Telling Angelina off for being mean. And saying that it's unfair that I don't have a group of girls to play with after practice like she does." ("base", "narrow", "base", "downR")
    gen "Nice... you got both Spinnet and Bell on your side! Told you that bonding with them would do it!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "I...{w=0.3} I suppose so." ("base", "happyCl", "base", "mid") #Smiles
    cho @ cheeks blush "Angelina still didn't look convinced though, and just stood there with her arms crossed, while staring at me..." ("soft", "base", "base", "downR")
    cho @ cheeks blush "So as an attempt at convincing her... I grabbed Alicia's head and pressed her lips against mine..." ("smile", "base", "angry", "mid")
    cho @ cheeks blush "Which was enough to grab Katie's attention, and she moved up behind me to try and pull my top off." ("soft", "wink", "base", "mid")
    gen "Nicely done!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Of course I didn't let her..." ("annoyed", "base", "base", "R")
    gen "Why not? What about your cover?" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "Because...{w=0.3} I...{w=0.4} Well, I didn't blow it, okay!?" ("open", "base", "angry", "downR")
    cho @ cheeks blush "I wasn't going to let her undress me like that... Instead, I grabbed her hands and put them under my bra to let her play with my breasts." ("horny", "narrow", "base", "down")
    cho @ cheeks blush "Luckily she didn't seem to think much of it and began massaging them." ("soft", "narrow", "base", "mid")
    cho @ cheeks blush "Angelina on the other hand, was not convinced... And she told the other girls to step aside..." ("angry", "base", "base", "down")
    cho @ cheeks blush "Which they did...{w=0.4} Both Alicia and Katie jumped back when Angelina approached me, while staring me down." ("disgust", "base", "base", "mid")
    gen "Scary..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I don't think I've ever had a girl scrutinize me like that..." ("horny", "base", "base", "down")
    gen "Especially a naked one..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "She then smirked at me, and said that I must truly be something special if her girls would just throw themselves at me as eagerly as they did." ("soft", "base", "base", "mid")
    cho @ cheeks blush "I didn't really know how to respond to that, so I instinctively took a step back against the wall just as she leaned in and pressed her lips against mine..." ("horny", "closed", "base", "mid")
    cho @ cheeks blush "Which took me by such surprise, I tripped and slid down onto the wet floor." ("upset", "closed", "base", "mid")
    gen "Ouch..." ("base", xpos="far_left", ypos="head")
    gen "(Those Lionesses are animals!)" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "She didn't even apologize, and just looked down at me, telling me that I kiss like a high-schooler..." ("mad", "base", "base", "mid")
    cho @ cheeks blush "That said... didn't stop her from crouching down for another... although this time she put her tongue in there." ("angry", "base", "base", "mid")
    gen "Straight in there!" ("grin", xpos="far_left", ypos="head")
    gen "I hope you returned the favour!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "I tried to... but as I attempted it, she stopped and stood back up." ("upset", "narrow", "base", "R")
    cho @ cheeks blush "So I tried doing the same, but when I steadied myself to get up, she put her foot beneath my skirt and pressed it against my panties, which made me slide back down onto the floor." ("open", "wide", "base", "mid")
    gen "..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Then, turning back to the others, she started chastising them even further, about how she was still mad at them for doing what they did..." ("open", "base", "base", "mid")
    cho @ cheeks blush "But when doing so, she also started rubbing her foot up and down against my panties." ("disgust", "base", "base", "down")
    cho @ cheeks blush "Both Katie and Alicia didn't seem to notice, since their focus was on defending themselves." ("horny", "base", "base", "downR")
    cho @ cheeks blush "I don't remember exactly what they were saying at that point..." ("angry", "happyCl", "base", "mid")
    gen "(not surprising...)" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "During their argument, She just kept rubbing me, more and more, until... Well..." ("horny", "closed", "base", "mid")
    cho @ cheeks blush "I just...{w} couldn't...{w} hold it in any more!" ("soft", "closed", "base", "mid") #ahegao?
    gen "Don't tell me she made you--" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "She made me orgasm as I lay there on the ground!" ("horny", "base", "base", "up")
    cho @ cheeks blush "Which they all soon realised, and they suddenly stopped arguing to look at me..." ("clench", "base", "base", "up")
    cho @ cheeks heavy_blush "Angelina's expression even changed into a smile, and she pressed her foot down even harder, telling me I'd been a naughty girl..." ("disgust", "wide", "base", "mid")
    cho @ cheeks blush "And that the other two shouldn't have been so selfish to keep me all for themselves." ("disgust", "narrow", "base", "downR")
    cho @ cheeks blush "She then stepped off me, and made her way out of the showers, beckoning the other two to come with her." ("clench", "base", "base", "mid")
    cho @ cheeks blush "Which they did... Although before doing so, they caught a last look at me, and giggled happily." ("mad", "narrow", "base", "mid")
    gen "Nice..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "What do you mean, nice?" ("mad", "base", "angry", "mid")  #large text
    cho @ cheeks blush "She humiliated me!" ("open", "base", "angry", "mid")  #large text
    gen "She was testing you..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "She was..." ("clench", "wide", "base", "down")
    gen "Yes...{w=0.4} Not only that...{w=0.4} I think you passed!" ("grin", xpos="far_left", ypos="head")
    gen "Maybe I underestimated those girls... they aren't easy to boss around, that's for sure..." ("base", xpos="far_left", ypos="head")
    gen "But no matter..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("upset", "happyCl", "base", "mid") #pout
    gen "We shall see soon enough what comes from this..." ("base", xpos="far_left", ypos="head")
    gen "In any case, what has happened has happened." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "You reckon I ruined it?" ("upset", "narrow", "base", "mid") #worried
    gen "Of course not, you did great!" ("base", xpos="far_left", ypos="head")
    gen "But you can't let them take charge like that during the game." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes [name_genie_cho]." ("open", "narrow", "base", "down")
    gen "Good!" ("base", xpos="far_left", ypos="head")
    gen "One step closer towards sipping at the fizzy cup!" ("base", xpos="far_left", ypos="head")
    cho "You don't drink from--" ("clench", "base", "base", "mid")
    gen "Better ready yourself [name_cho_genie]. The finals are looming ever so closer." ("base", xpos="far_left", ypos="head")
    gen "You got this." ("base", xpos="far_left", ypos="head")
    cho "Thanks..." ("soft", "narrow", "base", "downR") #smiles
    gen "Now, time for some rest." ("base", xpos="far_left", ypos="head")
    cho "Yes, good night then [name_genie_cho]." ("open", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event
