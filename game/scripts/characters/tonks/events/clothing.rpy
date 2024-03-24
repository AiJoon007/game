label tonks_summon_setup:

    # Reset doll state
    $ tonks.wear("all")
    $ tonks.set_cum(None)
    $ tonks.animation = None

    if not states.ton.ev.random_strip.complete and states.cho.ev.inspect_her_body.T3_E3_complete and states.ton.level >= 20 and tonks.is_any_worn("top", "bottom", "bra", "panties"):
        $ states.ton.ev.random_strip.complete = True #TODO use to make event not repeat

        $ tonks.strip("clothes")
        call ton_walk(action="enter", xpos="mid", ypos="base")

        play sound "sounds/scratch.ogg"
        with hpunch
        gen "!!!" ("angry", xpos="far_left", ypos="head")

        ton @ cheeks heavy_blush hair horny "" ("grin", "base", "base", "mid", xpos="mid", ypos="base", trans=d5)
        call ctc

        ton @ cheeks heavy_blush hair horny "Hello, [name_genie_tonks]." ("soft", "narrow", "raised", "mid")
        gen "You're naked!" ("grin", xpos="far_left", ypos="head")
        ton @ cheeks heavy_blush hair horny "I am?" ("soft", "narrow", "raised", "mid")
        ton @ cheeks heavy_blush hair horny "Oh... Yes it appears so..." ("grin", "narrow", "shocked", "down")
        ton @ cheeks heavy_blush hair horny "Is that a problem, [name_genie_tonks]?" ("annoyed", "narrow", "raised", "mid")
        ton @ cheeks heavy_blush hair horny "Am I going to get fired for inappropriate behaviour?" ("annoyed", "narrow", "base", "down")
        ton @ cheeks heavy_blush hair horny "Are you going to report me to the ministry?" ("base", "narrow", "raised", "down")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Have you been drinking Wine?" ("base", xpos="far_left", ypos="head")

        play sound "sounds/giggle2_loud.ogg"
        ton @ cheeks heavy_blush hair horny "*Giggles*" ("grin", "narrow", "base", "stare")
        ton @ cheeks heavy_blush hair horny "Maybe..." ("grin", "wink", "base", "mid")

        gen "One of the students could have seen you..." ("base", xpos="far_left", ypos="head")
        ton @ cheeks heavy_blush hair horny "Oh, I would love for them to see me like this..." ("horny", "narrow", "shocked", "R")
        ton @ cheeks heavy_blush hair horny "Why don't you invite one to your office?" ("soft", "narrow", "shocked", "mid")

        if states.ast.ev.imperio_with_tonks.completed_once:
            gen "You'd like that wouldn't you..." ("base", xpos="far_left", ypos="head")
            ton @ cheeks heavy_blush hair horny "Very much!" ("base", "narrow", "base", "mid")
            gen "Like that Astoria girl you're so infatuated with?" ("base", xpos="far_left", ypos="head")
            gen "Want me to call her up here to have her shame you on your bad behaviour?" ("base", xpos="far_left", ypos="head")
            ton @ cheeks heavy_blush hair horny "Oh, yes please!" ("horny", "base", "base", "mid")
            gen "But this sudden behaviour isn't about her is it?" ("base", xpos="far_left", ypos="head")
            ton @ cheeks heavy_blush hair horny "*Hmm*... Is it that obvious?" ("base", "narrow", "base", "R")

        gen "Miss Chang?" ("base", xpos="far_left", ypos="head")
        ton @ cheeks heavy_blush hair horny "*Mmm*..." ("base", "narrow", "base", "stare")
        gen "Would you like me to bring her up here so you could rub your bodies together some more?" ("base", xpos="far_left", ypos="head")
        ton @ cheeks heavy_blush hair horny "Yes please!" ("grin", "narrow", "base", "stare")
        gen "You sure you're ready to find out just how flexible she is?" ("base", xpos="far_left", ypos="head")
        ton @ cheeks heavy_blush hair horny "Yes!" ("crooked_smile", "base", "base", "stare")

        gen "(Although that's probably not the best idea in her current state...)" ("base", xpos="far_left", ypos="head")
        gen "(Doesn't mean I can't tease her a bit though...)" ("grin", xpos="far_left", ypos="head")
        gen "I bet you'd love that..." ("base", xpos="far_left", ypos="head")

        menu:
            "-Play nice-":
                gen "How about a bonus instead?" ("grin", xpos="far_left", ypos="head")
                ton @ cheeks heavy_blush hair horny "A bonus? For showing off my body to my own boss?" ("soft", "narrow", "raised", "mid")
                gen "That's right." ("base", xpos="far_left", ypos="head")

                play sound "sounds/giggle2_loud.ogg"
                ton @ cheeks heavy_blush hair horny "*Giggles*" ("grin", "narrow", "raised", "stare")

                ton @ cheeks heavy_blush hair horny "I've always wanted to find out my worth." ("grin", "base", "base", "stare")
                gen "Alright then... Let's see, how much are you worth to me..." ("base", xpos="far_left", ypos="head")

                menu:
                    "-Zero gold-" if game.gold <= 0:
                        gen "Zero gold." ("base", xpos="far_left", ypos="head")
                        ton @ cheeks heavy_blush hair horny "Seriously?" ("soft", "narrow", "raised", "mid")
                        gen "Yes, I'm a cheap bastard." ("base", xpos="far_left", ypos="head")
                        ton @ cheeks heavy_blush hair horny "Clearly..." ("upset", "narrow", "base", "mid")

                    "-One gold-" if game.gold > 0:
                        gen "A single gold coin, if anything..." ("base", xpos="far_left", ypos="head")
                        ton @ cheeks heavy_blush hair horny "(Bastard... How humiliating.)" ("soft", "narrow", "worried", "up")
                        gen "Well?" ("base", xpos="far_left", ypos="head")
                        ton @ cheeks heavy_blush hair horny "Yes?" ("disgust", "narrow", "raised", "mid")
                        gen "Shouldn't you be thanking me for this generous valuation?" ("base", xpos="far_left", ypos="head")
                        ton @ cheeks heavy_blush hair horny "Oh... Thank you so much, [name_genie_tonks]." ("annoyed", "narrow", "base", "stare")
                        gen "Don't mention it, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")
                        $ game.gold -= 1

                    "-Twenty gold-" if game.gold >= 20:
                        gen "How does twenty gold sound?" ("base", xpos="far_left", ypos="head")
                        ton @ cheeks heavy_blush hair horny "(*Hmm*... I kind of expected more.)" ("annoyed", "narrow", "raised", "downR")
                        ton @ cheeks heavy_blush hair horny "Thank you, [name_genie_tonks]." ("soft", "narrow", "base", "mid")
                        gen "No, [name_tonks_genie]... Thank you." ("grin", xpos="far_left", ypos="head")
                        $ game.gold -= 20

                    "-A hundred gold-" if game.gold >= 100:
                        gen "Does one hundred gold sound nice to you?" ("base", xpos="far_left", ypos="head")
                        gen "With a body like that, you could earn a fortune at a strip club!" ("grin", xpos="far_left", ypos="head")
                        ton @ cheeks heavy_blush hair horny "Really..." ("horny", "narrow", "shocked", "mid")
                        ton @ cheeks heavy_blush hair horny "You think a noble teacher and auror like me, would quit her highly regarded job to become a cheap stripper?" ("grin", "narrow", "shocked", "mid")
                        gen "Well, no. I still want to keep you as a teacher." ("base", xpos="far_left", ypos="head")
                        gen "I merely suggested that you could." ("base", xpos="far_left", ypos="head")
                        ton @ cheeks heavy_blush hair horny "Maybe the duelling stage could find some extra use..." ("base", "narrow", "shocked", "stare")
                        ton @ cheeks heavy_blush hair horny "Perhaps some extra curricular activities for a couple of my favourite students could be arranged..." ("horny", "narrow", "raised", "up")
                        gen "I'm sure they would all love to watch their perverted teacher strip!" ("grin", xpos="far_left", ypos="head")
                        $ game.gold -= 100

                gen "Now..." ("base", xpos="far_left", ypos="head")

            "-Scold her-":
                gen "But you know what I have to do, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                gen "What were you thinking, walking into your boss' office, completely naked?" ("base", xpos="far_left", ypos="head")
                ton @ cheeks heavy_blush hair horny "I'm terribly sorry, [name_genie_tonks]..." ("open", "narrow", "base", "down")
                gen "How's this befitting for a teacher..." ("angry", xpos="far_left", ypos="head")
                gen "That surely calls for some punishment, don't you think?" ("grin", xpos="far_left", ypos="head")
                ton @ cheeks heavy_blush hair horny "You are so right, [name_genie_tonks]!" ("horny", "narrow", "base", "stare")

                # This section will be under some public check
                # gen "I should make you the school's cum-dumpster instead. How would you like that position?" ("base", xpos="far_left", ypos="head")
                # gen "Boys lining up in front of the school toilets, waiting their turn to dump their cum into their teacher's mouth, day after day!" ("base", xpos="far_left", ypos="head")
                # ton "You're making me so wet, [name_genie_tonks]!" ("base", "base", "base", "ahegao")
                # ton "Maybe some day I'll get bored of my current position here at Hogwarts... you never know..." ("horny", "base", "raised", "mid")
                # gen "I'm not done with your punishment, Miss [name_tonks_genie]!" ("base", xpos="far_left", ypos="head")
                gen "You went to this school, didn't you? Which house were you in?" ("base", xpos="far_left", ypos="head")
                ton @ cheeks heavy_blush hair horny "My house? I was in Hufflepuff, but why--" ("disgust", "base", "raised", "mid")
                gen "Very well then..." ("base", xpos="far_left", ypos="head")
                gen "Minus ten points from Hufflepuff!" ("base", xpos="far_left", ypos="head")
                $ hufflepuff -=10
                ton @ cheeks heavy_blush hair upset "What? But [name_genie_tonks]! I'm not even a student--" ("disgust", "base", "base", "mid", trans=hpunch)
                gen "Also--" ("base", xpos="far_left", ypos="head")

        menu:
            "-Those clothes stay off!-":
                $ tonks.unequip("clothes")

                ton @ cheeks heavy_blush hair horny "*Hmm*?" ("soft", "narrow", "raised", "down")
                gen "That's right... If they're so bothersome, why bother wearing them at all?" ("base", xpos="far_left", ypos="head")
                gen "When you're in here with me I want you on full display!" ("base", xpos="far_left", ypos="head")
                ton @ cheeks heavy_blush hair horny "Of course [name_genie_tonks]..." ("soft", "narrow", "base", "down") #Horny
                ton @ cheeks heavy_blush hair horny "If you would allow me to put my clothes back on at any time, just let me know..." ("soft", "narrow", "base", "downR")

            "-Get dressed!-":
                gen "No teacher of mine will strut around naked...{w} unless I say so!" ("base", xpos="far_left", ypos="head")
                ton @ cheeks heavy_blush hair horny "Yes [name_genie_tonks]..." ("open", "narrow", "shocked", "down")
                gen "Now, put your clothes back on..." ("base", xpos="far_left", ypos="head")
                ton @ cheeks heavy_blush hair horny "*Ehm*... Okay..." ("soft", "base", "base", "down")

                play sound "sounds/magic4.ogg"
                $ tonks.wear("all")
                ton "" (trans=morph)
                ton @ cheeks heavy_blush hair horny "" ("soft", "narrow", "base", "mid")

                if states.gen.ev.tonks.metamorphmagi_aware:
                    gen "...{w} You used your meta-whatsit ability just then didn't you?" ("base", xpos="far_left", ypos="head")
                    ton @ cheeks heavy_blush hair horny "You can tell?" ("soft", "narrow", "base", "down")
                    gen "Whatever, just wear your actual clothing next time..." ("base", xpos="far_left", ypos="head")
                else:
                    gen "Much better..." ("base", xpos="far_left", ypos="head")
                    ton @ cheeks heavy_blush hair horny "..." ("soft", "narrow", "base", "downR")

        gen "Now, get back to your room and think about what you've done..." ("base", xpos="far_left", ypos="head")
        ton @ cheeks heavy_blush hair horny "Yes [name_genie_tonks]..." ("open", "narrow", "base", "down") #look down, blush

        #Tonks leaves
        call ton_walk(action="leave")

        gen "(Hold on... Didn't I call her here for another reason...)" ("base", xpos="far_left", ypos="head")
        gen "(I suppose it'll have to wait till tomorrow...)" ("base", xpos="far_left", ypos="head")

        jump end_tonks_event

    if states.ton.wardrobe_scheduling:
        $ tonks.equip_random_outfit()

    play sound "sounds/door.ogg"
    call ton_chibi("stand","mid","base")
    with d3

    #Tonks greeting.
    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed

    if states.ton.mood > 0:
        if 5 > states.ton.mood >= 1:
            ton "Yes, [name_genie_tonks]?" ("open", "base", "base", "R", xpos="base", ypos="base", trans=d3)
            ton "" ("base", "base", "base", "R")
        elif 10 > states.ton.mood >= 5:
            ton "I have classes to teach, please be quick." ("upset", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 20 > states.ton.mood >= 10:
            ton "Make it quick, [name_genie_tonks]..." ("upset", "base", "base", "R", xpos="base", ypos="base", trans=d3)
        elif 30 > states.ton.mood >= 20:
            ton "What do you want, \"[name_genie_tonks]\", I'm busy." ("mad", "base", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif 40 > states.ton.mood >= 30:
            ton "..............." ("upset", "base", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif 50 > states.ton.mood >= 40:
            ton "Please stop wasting my time." ("upset", "closed", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif states.ton.mood >= 50:
            ton "You have the nerve to call me here after what you did." ("upset", "base", "angry", "mid", xpos="base", ypos="base", trans=d3)

        call describe_mood("Tonks", states.ton.mood)
        call tutorial("moodngifts")
    else:
        ton "You called, [name_genie_tonks]?" ("base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
    return
