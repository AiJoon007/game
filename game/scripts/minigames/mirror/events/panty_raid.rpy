
# Mirror story: Panty raid
label panty_raid:

    with d5
    centered "{size=+7}{color=#cbcbcb}Panty Raid{/color}{/size}\n\n{color=#cbcbcb}Based on a story written by {size=+4}WaxerRed{/size}\n{size=-4}Proofreading & Editing by Lineup, Johnny and LoafyLemon\nImplementation by Lineup and LoafyLemon{/size}{/color}"

    label .choices:

    # Setup
    $ hermione.equip(her_outfit_default)
    $ game.daytime = True
    $ game.weather = "clear"
    stop weather
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    menu:
        "For the best experience it is recommended to play the story in chronological order."
        "{size=-4}Part one{/size}\n-Defiance-{#LINT_IGNORE}":
            $ pathvalue = 0
        "{size=-4}Part two{/size}\n-Acceptance-{#LINT_IGNORE}":
            $ pathvalue = 1
        "{size=-4}Part three{/size}\n-Realization-{#LINT_IGNORE}":
            $ pathvalue = 2
        "{size=-4}Part four{/size}\n-Obedience-{#LINT_IGNORE}":
            $ pathvalue = 3
        "-Return-":
            $ renpy.end_replay()

    call music_block

    if pathvalue == 0:
        # Part 1
        call her_chibi("stand","mid","base")
        call hide_blkfade

        her "Hello [name_genie_hermione]." ("open", "base", "base", "mid", xpos="right", ypos="base", trans=d3, flip=False)
        her "" ("base")
        gen "Good day [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "How would you feel about going out and earning thirty-five points for your house today?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I would love to...{w=0.3} as long as it doesn't involve me humiliating myself in front of my peers." ("open", "base", "base", "R")
        her @ cheeks blush "" ("normal")
        gen "Well then, perhaps today is your lucky day." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Really?" ("open", "base", "base", "mid")
        her @ cheeks blush "" ("soft")
        gen "Yes! In fact, you may wish to remain as unseen as possible during your activities today." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "(That doesn't sound suspicious at all...)" ("disgust", "narrow", "worried", "down")
        her @ cheeks blush "" ("normal", "base", "base", "mid")
        gen "I would very much like for you to recover one of the most revered and sacred objects in this academy...{w=0.5} No, in the world!" ("grin", xpos="far_left", ypos="head")
        her "Oh! You want me to recover a magical artefact?" ("open", "base", "base", "mid")
        her "" ("normal", "base", "base", "mid")
        gen "Something like that..." ("base", xpos="far_left", ypos="head")
        her "" ("normal", "base", "base", "mid")
        her "I am glad you're finally asking me to properly utilise my abilities as one of Hogwarts' top students." ("open", "closed", "base", "mid")
        her "{size=-4}I only wish you would have asked this of me sooner...{/size}" ("open", "narrow", "base", "R_soft")
        her "You can count on me, [name_genie_hermione]! I am happy to perform a task such as this one." ("smile", "base", "base", "mid")
        her "" ("base", "base", "base", "mid")
        gen "Great! Now all the information I have for this \"artefact\" is an ancient riddle..." ("base", xpos="far_left", ypos="head")
        gen "Are you ready?" ("base", xpos="far_left", ypos="head")
        her "Of course, [name_genie_hermione]." ("open", "base", "base", "mid_soft")
        her "" ("base")
        gen "Good, here we go..." ("base", xpos="far_left", ypos="head")
        gen "\"I am sought by many,{w=0.2} yet the same number already possess me\"." ("base", xpos="far_left", ypos="head")
        her "" ("soft", "happy", "base", "mid")
        gen "\"The more I am used, the more valuable I become\"." ("base", xpos="far_left", ypos="head")
        her "The sword of Gryffindor..." ("open", "closed", "base", "mid")
        her "no, wait..." ("angry", "wide", "worried", "shocked")
        her "... the elder wand?" ("base", "base", "base", "mid")
        her "" ("disgust")
        gen "I am not done yet [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "Sorry..." ("soft", "narrow", "worried", "down")
        her "" ("normal", "base", "base", "mid")
        gen "\"The only thing man covet more than my form is the secret I hid\"." ("base", xpos="far_left", ypos="head")
        her "*Hmm*..." ("upset", "base", "base", "R")
        her "" ("normal", "base", "base", "mid")
        gen "... \"Sometimes I am plain and white, but I look my best when skimpy and black\"." ("base", xpos="far_left", ypos="head")
        her "" ("normal", "happy", "base", "mid")
        gen "No wait! \"skimpy and pink\"." ("angry", xpos="far_left", ypos="head")
        her "This is an ancient riddle...?" ("open", "squint", "angry", "mid")
        her "" ("upset", "base", "base", "R")
        gen "Hush girl..." ("base", xpos="far_left", ypos="head")
        gen "\"In order to find me you must get close to earth, then look up to the heavens\"." ("base", xpos="far_left", ypos="head")
        her "..." ("upset", "base", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "\"No schoolgirl fetish would be complete without me\"." ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]...?!" ("open", "squint", "angry", "mid")
        gen "\"The answer is on page 74, Spell {i}seitnaP{/i} backwards\"." ("grin", xpos="far_left", ypos="head")
        her "PROFESSOR!" ("scream", "squint", "angry", "mid")
        her "" ("angry", "squint", "angry", "mid")
        gen "Yes?{w=0.5} Did you figure it out?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "If you wanted to see my...{w=0.3} *ahem*{w=0.3} {i}undergarments{/i}, you could have just asked..." ("disgust", "squint", "base", "mid")
        her @ cheeks blush "{size=-4}You didn't have to make the whole story up to grab my attention...{/size}" ("upset", "narrow", "base", "R_soft")
        gen "By Merlin's beard! I think you've got it girl...{w=0.5} {size=-4}for the most part at least.{/size}" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione], my classes start soon, can we just get it over with, so I can get my points and leave?" ("open", "closed", "base", "mid")
        her "" ("upset", "narrow", "base", "mid_soft")
        gen "Such eagerness...{w=0.3} but where's the challenge in handing me your own?" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Sorry, you wanted me to hand you a pair?" ("open", "wide", "base", "mid")
        gen "Of course, but not yours silly girl..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("angry")
        gen "This is meant to be a treasure hunt! Go find someone's panties out in the world and then bring them to me." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "But, [name_genie_hermione]?!" ("shock", "squint", "angry", "mid")
        her @ cheeks blush "" ("angry")
        gen "You're a bright young gal, I'm sure you'll think of something... Make haste!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "......." ("disgust")
        pause 1.0
        her "" ("soft", "narrow", "worried", "down")
        gen "What are you standing there for?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Isn't there any other way I coul--" ("soft", "narrow", "base", "mid_soft")
        gen "No." ("base", xpos="far_left", ypos="head")
        her "{size=-4}... fine.{/size}" ("soft", "narrow", "worried", "down")

        call her_walk(action="leave")

        show screen blkfade
        with d3

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Three hours later...{/color}{/size}"

        $ game.daytime = False
        call music_block

        pause 1.0
        call hide_blkfade

        play sound "sounds/knocking.ogg"
        "*Knock-knock-knock*"
        pause 1.0
        gen "Enter!" ("base", xpos="far_left", ypos="head")

        call her_walk(action="enter", xpos="mid", ypos="base")

        her "Good evening, [name_genie_hermione]." ("open", "base", "base", "R")
        her "" ("normal", "base", "base", "R")
        gen "Hello again, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush ""
        gen "Did you finish your assignment?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "about that..." ("soft", "narrow", "base", "R_soft")

        call her_walk("desk", "base")

        "She elegantly drops a pair of frilly pink panties on your desk."
        her @ cheeks blush "And for extra credit..." ("soft", "narrow", "worried", "down")
        hide screen bld1
        hide hermione_main
        with d3
        "She adds a matching pink lingerie bra to the spoils on your desk."
        show screen bld1 with d3
        gen "You absolute minx!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("normal", "base", "base", "R")
        gen "You've outdone yourself [name_hermione_genie], how did you manage this feat?" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "I would prefer not to talk about it..." ("disgust", "narrow", "worried", "down")
        gen "Well, you can certainly colour me impressed." ("grin", xpos="far_left", ypos="head")
        her "Does that mean I've earned some extra house points?" ("open", "base", "base", "R")
        gen "I think the situation calls for it..." ("base", xpos="far_left", ypos="head")
        her "" ("smile", "base", "base", "R")
        gen "Ninety points to Gryffi--{w=0.5}{nw}" ("grin", xpos="far_left", ypos="head")
        gen "Ninety points to Gryffi--{fast} wait a second..." ("angry", xpos="far_left", ypos="head")
        her "" ("smile", "base", "base", "mid")
        nar "You take another look at the panties and notice something unusual."
        her "" ("base", "base", "base", "mid")
        nar "Both panties and bra have a small piece of paper tied to them."
        her "" ("normal", "base", "base", "mid")
        nar "You reach out and grab the closest pair of panties, then study the paper."
        her "" ("normal", "base", "base", "R")
        "8.99$\n{size=-3}Thank you for shopping with us and hope to see you back soon!{/size}\nMadam Mafkin{#LINT_IGNORE}"
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]?" ("crooked_smile", "closed", "base", "mid")
        gen "Why is there a price tag on these?" ("base", xpos="far_left", ypos="head")
        her "...!" ("angry", "wide", "base", "stare")
        her "Uh.... Well, the person I bough--{w=0.3} *ahem*{w=0.2} {size=+2}BORROWED{/size} these from must have forgotten to take the price tag off." ("open", "happy", "base", "mid")
        her "" ("normal")
        gen "I see...{w=0.3} Well, whoever you took them from must be a bit slow to forget something like that, don't you agree?" ("base", xpos="far_left", ypos="head")
        her "Uhh..." ("normal", "narrow", "worried", "down")
        gen "I would even dare to call them...{w=0.2} a moron." ("base", xpos="far_left", ypos="head")
        her "..." ("upset")
        her "" ("upset", "base", "worried", "R")
        gen "A bloated...{w=0.2} Scatterbrained,{w=0.2} moron!" ("grin", xpos="far_left", ypos="head")
        her "{size=+4}[name_genie_hermione]!{/size}" ("open", "squint", "angry", "mid")
        her "" ("normal")
        gen "Yes, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her "Fine..." ("annoyed", "narrow", "annoyed", "mid")
        her "it was me!" ("angry", "narrow", "worried", "down")
        her "I couldn't do it, so I bought them at the shop..." ("disgust")
        gen "So...{w=0.5} You're the bloated, scatterbrained moron then?" ("base", xpos="far_left", ypos="head")
        her "Sir, this has been embarrassing enough...{w=0.5} Can I just go back to my dormitory please?" ("disgust", "narrow", "base", "mid_soft")
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

        menu:
            "-Cheaters never prosper-":
                gen "I must say I am disappointed with your actions, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her "I am so sorry [name_genie_hermione]..." ("disgust", "narrow", "worried", "down")
                her "" ("disgust", "narrow", "base", "mid_soft")
                gen "Not only did you disobey me, but you also tried to trick me - your headmaster - into thinking these belonged to some colleague of yours." ("base", xpos="far_left", ypos="head")
                her "it won't happen again..." ("disgust", "narrow", "worried", "down")
                her "" ("disgust", "narrow", "base", "mid_soft")
                gen "For your own sake it better doesn't, or I will have to take action." ("angry", xpos="far_left", ypos="head")
                her "" ("disgust", "narrow", "worried", "down")
                gen "Dismissed." ("base", xpos="far_left", ypos="head")
                her "Yes sir."

            "-Yes, they do-":
                gen "I must say...{w=0.3} I am impressed with your courage, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her "I am sorry [name_genie_hermione]. I wo--" ("disgust", "narrow", "worried", "down")
                her "Wait what?" ("shock", "base", "worried", "mid")
                her "" ("soft", "base", "worried", "mid")
                gen "I never imagined you'd possess such \"out of the box\" problem-solving!" ("base", xpos="far_left", ypos="head")
                her "Really?" ("open", "base", "worried", "mid")
                her "" ("soft", "base", "worried", "mid")
                gen "You fumbled the landing, but otherwise cheated like a pro!" ("grin", xpos="far_left", ypos="head")
                her "Thank you..." ("soft", "base", "worried", "mid")
                her "(I guess...?)" ("soft", "narrow", "base", "R_soft")
                her "" ("soft", "base", "worried", "R")
                gen "Now, I won't overburden you with compliments..." ("base", xpos="far_left", ypos="head")
                her "" ("soft", "base", "worried", "mid")
                gen "Take your house points and go...{w=0.5} Thirty-five points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "{size=+4}Really?!{/size}{w=0.2} Thank you so much [name_genie_hermione]!" ("smile", "base", "base", "mid")

                call her_walk("mid", "base")

                gen "I hope next time you do better though." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "(Next time...?!)" ("shock", "wide", "worried", "shocked", flip=True)
                her @ cheeks blush "(Think about the points Hermione, the points......)" ("angry", "happyCl", "worried", "mid", flip=True)

        call her_walk(action="leave")

        show screen blkfade with d3
        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}End of part one{/color}{/size}"
        jump panty_raid.choices

    if pathvalue == 1:
        # Part 2
        call hide_blkfade
        pause 1.5
        play sound "sounds/knocking.ogg"
        "*Knock-knock-knock*"
        pause 1.0
        gen "Come in!" ("base", xpos="far_left", ypos="head")

        call her_walk(action="enter", xpos="mid", ypos="base")

        her "Hello [name_genie_hermione], you called?" ("open", "base", "base", "mid", xpos="right", ypos="base", trans=d3, flip=False)
        her "" ("base")
        gen "Hello to you too, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Say...{w=0.3} would you like to earn some points today, girl?" ("grin", xpos="far_left", ypos="head")
        her "Possibly..." ("open")
        her "But that depends on the task required of me." ("open", "closed", "base", "mid")
        her "" ("soft", "base", "base", "R")
        gen "I would like you to try yourself at that \"treasure hunt\" again." ("base", xpos="far_left", ypos="head")
        her "*Sigh* I knew that sooner or later, you would ask me about it, [name_genie_hermione]..." ("open", "closed", "base", "mid")
        her "Do I have a choice?" ("upset", "base", "worried", "mid")
        gen "Certainly, if you don't mind those \"Slytherin Harlots\" taking the house cup!" ("grin", xpos="far_left", ypos="head")
        her "I Do mind..." ("upset", "narrow", "base", "down")
        her "" ("upset", "base", "worried", "mid")
        gen "Then you'd better head on out and steal some girl's panties!" ("grin", xpos="far_left", ypos="head")
        her "{size=-4}... one hundred points{/size}" ("open", "base", "worried", "R")
        her "" ("upset")
        gen "Thirty-five." ("base", xpos="far_left", ypos="head")
        her "... seventy-five points." ("open", "happyCl", "worried", "mid")
        her "" ("upset")
        gen "Forty..." ("base", xpos="far_left", ypos="head")
        her "... fifty points." ("upset")
        gen "Forty-five..." ("base", xpos="far_left", ypos="head")
        her "Fine." ("disgust", "narrow", "base", "R_soft")
        her "" ("upset", "base", "base", "R")
        gen "We got a deal then, splendid!" ("grin", xpos="far_left", ypos="head")
        her "" ("normal", "base", "base", "mid")
        gen "You're free to go now." ("base", xpos="far_left", ypos="head")
        her "Thank you [name_genie_hermione]." ("open", "base", "base", "mid")

        call her_walk("door", "base")

        call bld
        gen "Oh and one more thing..." ("base", xpos="far_left", ypos="head")
        her "Yes?" ("soft", "base", "base", "R", flip=True)
        gen "Make sure they're not new this time." ("base", xpos="far_left", ypos="head")
        her "... okay." ("disgust", "narrow", "worried", "down", flip=True)
        hide hermione_main
        hide screen bld1
        with d3
        pause 0.5

        play sound "sounds/door.ogg"
        call her_chibi("hide")
        with d3
        pause 1.0

        show screen blkfade
        with d3
        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Four hours later...{/color}{/size}"
        $ game.daytime = False
        call music_block

        pause 1.0

        call hide_blkfade
        pause.5

        call her_walk(action="enter", xpos="desk", ypos="base")

        play sound "sounds/kick.ogg"
        "She drops a slightly used pair of plain panties on your desk."
        her @ cheeks blush "" ("soft", "base", "base", "R", flip=False)
        gen "I don't see any tags, that's good. Did you learn from your previous error?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes sir..." ("disgust", "narrow", "worried", "down")
        her @ cheeks blush "" ("soft", "narrow", "worried", "down")

        menu:
            "-Let her Go-":
                gen "Well, quality leaves a bit to be desired, but it's a good step forward." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "" ("soft", "base", "base", "mid")
                gen "Forty-five points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Thank you, [name_genie_hermione]." ("open", "base", "base", "mid")
                her @ cheeks blush "Am I free to go now?" ("soft", "base", "base", "mid")
                gen "Yes, you are free to go." ("base", xpos="far_left", ypos="head")

                call her_walk("mid", "base")

                play sound "sounds/sniff.ogg"
                gen "{size=-4}Such nice fragrance, I wonder to whom these belong?{/size}" ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush ".........(I'm sorry Ginny)........." ("disgust", "narrow", "worried", "down", flip=True)

                call her_walk(action="leave")

            "-Ask for details-":
                gen "So, who was the lucky lady?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "No one." ("open", "base", "worried", "R")
                her @ cheeks blush "" ("soft")
                gen "Come on now." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Umm*...{w=0.3} Does that really matter?" ("open", "base", "base", "mid")
                her @ cheeks blush "" ("soft")
                gen "It does to me." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*sigh*" ("soft", "happyCl", "worried", "mid")
                her @ cheeks blush "It was Ginny, sir..." ("open", "base", "worried", "mid")
                her @ cheeks blush "" ("soft")
                gen "Interesting...{w=0.5} I don't know who that is." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "She's a sister of one of my friends..." ("open", "base", "worried", "R")
                her @ cheeks blush "" ("normal")
                gen "Is she hot? Or cute?" ("base", xpos="far_left", ypos="head")
                her "..." ("soft", "narrow", "worried", "down")
                gen "Well?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I guess she is kind of both..." ("soft")
                gen "(Splendid! Maybe she can introduce her to me sometimes)" ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "" ("soft", "base", "base", "mid")
                gen "So, how did you do it?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I offered to do her laundry along with mine this week..." ("open", "narrow", "worried", "down")
                her @ cheeks blush "" ("soft")
                gen "And?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "And whilst I was working, I grabbed one of her...{w=0.4} panties...{w=0.3} and shoved them in my pocket." ("soft", "narrow", "base", "R_soft")
                gen "And?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "If she asks what happened to them... I will just say that they had gotten lost in the wash." ("soft", "narrow", "base", "mid_soft")
                her @ cheeks blush "" ("normal")
                gen "And?" ("base", xpos="far_left", ypos="head")
                her " And... that's really it." ("open", "base", "base", "mid")
                her "" ("normal")
                gen "How dull.{w=0.5} forty-five stupid house points to Gryffindor." ("angry", xpos="far_left", ypos="head")
                her "Do those count the same as regular points?" ("annoyed")
                gen "I suppose..." ("base", xpos="far_left", ypos="head")
                her "Goodnight then, sir." ("open", "base", "base", "mid")

                call her_walk("door", "base")

                gen "{size=-4}Ginny...{w=1.0} it's time for you to meet {i}George{/i}.{/size}{w=0.2}{nw}" ("base", xpos="far_left", ypos="head")
                call gen_chibi("jerk_off_behind_desk")
                play sound "sounds/zipper.ogg"
                gen "{size=-4}Ginny... It's time for you to meet {i}George{/i}.{/size}{fast}" ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "" ("angry", "wide", "worried", "shocked", flip=True)
                pause 0.8
                her @ cheeks blush "(I'd better leave now...)" ("disgust", "base", "base", "R", flip=True)
                hide hermione_main
                hide screen bld1
                with d3
                pause 0.5

                call her_chibi("leave")

        call blkfade

        stop music fadeout 1.0

        call gen_chibi("sit_behind_desk")
        centered "{size=+7}{color=#cbcbcb}End of part two{/color}{/size}"
        jump panty_raid.choices

    elif pathvalue == 2:
        # Part 3
        call hide_blkfade
        pause 1.0
        play sound "sounds/knocking.ogg"
        "*Knock-knock-knock*"
        pause 0.5
        her "I'm coming in."

        call her_walk(action="enter", xpos="mid", ypos="base")

        gen "Well, well, well... if it isn't my favourite minx!" ("grin", xpos="far_left", ypos="head")
        her "Good morning to you too, [name_genie_hermione]." ("open", "closed", "base", "mid", xpos="right", ypos="base", trans=d3, flip=False)
        her "" ("base", "base", "base", "mid")
        gen "What brings you here this time?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well... I..." ("open", "base", "base", "R")
        her @ cheeks blush "" ("upset")
        gen "Don't you worry, I'm just teasing you." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("normal", "base", "base", "mid")
        gen "But we've made it quite a habit by now, didn't we?" ("base", xpos="far_left", ypos="head")
        gen "You, coming here every morning and asking for points..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("normal", "base", "worried", "mid")
        gen "... for which in return you bring me panties of that colleague of yours..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("normal", "narrow", "base", "down")
        gen "... I wonder if she realised by now that a washing machine can only eat so many panties." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("soft", "narrow", "base", "R_soft")
        gen "but surely that's something worth risking your reputation over, am I right?" ("base", xpos="far_left", ypos="head")
        her "..." ("annoyed", "narrow", "base", "R_soft")
        gen "I'll take that as a yes." ("grin", xpos="far_left", ypos="head")
        gen "You know what to do, off you go." ("base", xpos="far_left", ypos="head")
        her "Fine." ("open", "closed", "base", "mid")
        her "" ("annoyed", "narrow", "base", "mid_soft")
        gen "That a girl." ("grin", xpos="far_left", ypos="head")

        call her_walk(action="leave")

        call blkfade

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}A few hours later...{/color}{/size}"
        $ game.daytime = False
        call music_block

        pause 1.0
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base")

        gen "Hello [name_hermione_genie], looking good." ("grin", xpos="far_left", ypos="head")
        her "Uh-huh... Sir, if I'm not mistaken... {w=0.3}Hogwarts does not have a \"linguistics\" class, do we?" ("open", "narrow", "worried", "mid_soft")
        her "" ("upset")
        gen "(Why is she asking me?{w=0.3} Oh Right, \"headmaster Rumbleboar\")" ("base", xpos="far_left", ypos="head")
        gen "Do you really think we have a class you wouldn't know about?" ("base", xpos="far_left", ypos="head")
        her "True... Then, do you know of how many \"Connies\" attend Hogwarts?" ("open", "base", "base", "mid")
        her "" ("normal")
        her "There aren't any in Gryffindor or Ravenclaw, I believe, but I'm not sure for some of the other houses." ("open", "base", "base", "mid_soft")
        her "" ("normal")
        gen "I feel as though there's some context missing." ("base", xpos="far_left", ypos="head")
        her "*Ehm*... alright, so...{w=0.5} I was in the Gryffindor girl's dorm, working on my \"task\"." ("open")
        her "" ("normal")
        gen "The perfect hunting grounds." ("base", xpos="far_left", ypos="head")
        her "I am astonished that I'll have to agree with you, but yes... I had the pick of the litter with no absence of choice.{w=0.3} Speaking of..." ("open", "closed", "base", "mid")

        call her_walk("desk", "base")

        play sound "sounds/cloth_sound.ogg"
        "She drops a bunched-up ball of about half a dozen girls' panties on your desk, coming in an array of different sizes, designs, and colours."
        her @ cheeks blush "I usually don't conduct such a shotgun approach to work, although..." ("open", "base", "base", "mid")
        her @ cheeks blush "" ("soft")
        gen "In this instance it appears to have served you well. Full marks for stealing panties from your schoolmates." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "It would have flustered me if I hadn't told my dorm mates time and time again that it is all of our responsibilities to keep our dorm tidy." ("annoyed", "base", "base", "R")
        her "Loss of their undergarments is expected when leaving said property strewn around as if a hurricane blew through their drawers." ("open", "base", "base", "mid")
        her "" ("soft")
        gen "Yes, Yes... But how does this connect back to a Connie?" ("base", xpos="far_left", ypos="head")
        her "Right... Well, I obviously chose a time at which I believed all my dorm mates would be gone." ("open", "happyCl", "worried", "mid")
        her @ cheeks blush "But just as I was shoving the last pair into my bag, Katie Bell walked in..." ("angry", "narrow", "base", "down")
        her @ cheeks blush "She caught me red-handed!" ("disgust", "narrow", "worried", "down")
        her "" ("normal", "narrow", "worried", "mid_soft")
        gen "Or silky handed!{w=1.0}{nw}" ("grin", xpos="far_left", ypos="head")
        gen "Or silky handed!{fast}... panty handed?" ("base", xpos="far_left", ypos="head")
        her "" ("normal", "narrow", "worried", "down")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Sounded better in my head...{w=0.5} give me a minute, and I'll come up with something that works..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I've never been more embarrassed in my entire life!" ("normal", "narrow", "worried", "mid_soft")
        her "" ("annoyed", "narrow", "base", "R_soft")
        gen "Pff, as if you've never said {i}that{/i} before." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I mean it! I was mortified, standing there clutching her panties while stumbling over my words for an excuse." ("open", "narrow", "worried", "mid_soft")
        her @ cheeks blush "" ("upset")
        gen "And what did she do?" ("base", xpos="far_left", ypos="head")
        her "Well... That's the odd thing, while I was floundering like a fish, she was just grinning at me. Then she said, and I quote..." ("open", "base", "base", "mid")
        her "\"I always had a feeling about you Granger... But if you want them, you'll need to do me a favour. Meet me tonight and we can help with Connie's Linguistics homework\"." ("open", "base", "base", "R")
        her "" ("base", "base", "base", "mid")
        gen "Connie's linguist?-{w=1.0}{nw}" ("base", xpos="far_left", ypos="head")
        gen "Connie's linguist?-{fast} Oh, I see..." ("grin", xpos="far_left", ypos="head")
        her "As embarrassing as the circumstances were, I would never turn down a request to help a student with homework! But I don't think we have a linguistics class or what Connie she was--" ("open", "narrow", "worried", "mid_soft")
        her "" ("soft", "base", "base", "mid")
        gen "{i}Cunnilingus{/i} [name_hermione_genie]... She was asking for Cunnilingus." ("grin", xpos="far_left", ypos="head")
        her "*Huh*? But she said she wanted study help."
        gen "It was a metaphor... She was assuming you were a bit more worldly than you really are." ("base", xpos="far_left", ypos="head")
        her "I am plenty worldly!" ("angry", "base", "angry", "mid")
        her "..." ("upset", "narrow", "angry", "R")
        her "" ("upset", "base", "worried", "mid")
        pause 0.5
        her "... What's Cunnilingus?" ("open", "base", "worried", "mid")
        her "" ("upset")
        gen "*Sigh*, she was asking for Dinner beneath the bridge." ("base", xpos="far_left", ypos="head")
        her "Dinner? But if she wanted to eat with me why didn't she--" ("open", "base", "base", "mid")
        her "" ("upset")
        gen "Metaphor, [name_hermione_genie]... She wanted you to sip from her furry cup." ("base", xpos="far_left", ypos="head")
        her "*huh*?" ("open", "narrow", "worried", "mid_soft")
        her "" ("upset")
        gen "Muff Diving..." ("base", xpos="far_left", ypos="head")
        her "" ("upset", "base", "worried", "mid")
        gen "Munch her carpet..." ("base", xpos="far_left", ypos="head")
        her "" ("clench", "closed", "angry", "mid")
        gen "Deluxe wash..." ("base", xpos="far_left", ypos="head")
        her "Stop not making any sense!" ("clench", "base", "angry", "mid")
        her "" ("annoyed")
        gen "Are you really supposed to be this school's top student? She was asking you to eat her out." ("base", xpos="far_left", ypos="head")
        her "Eat her what out?" ("open")
        her "" ("annoyed", "narrow", "angry", "R")
        gen "Alright... work with me. She wanted you...{w=1.0} Still with me here?" ("base", xpos="far_left", ypos="head")
        her "Yes obviously..." ("open", "closed", "angry", "mid")
        her "(Does he think I'm an idiot?)" ("annoyed", "narrow", "angry", "R")
        gen "Okay then repeat after me." ("base", xpos="far_left", ypos="head")
        her "" ("annoyed", "base", "base", "mid_soft")
        gen "She wanted you..." ("base", xpos="far_left", ypos="head")
        her "She wanted me..." ("open", "base", "base", "mid_soft")
        her "" ("normal")
        gen "To take your tongue..." ("base", xpos="far_left", ypos="head")
        her "Thake myh tonghue?" ("open_tongue")
        her "" ("open_wide_tongue", "squint", "base", "mid")
        pause 1.0
        gen "And stick it in her vagina!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "{size=+8}WHAT?!{/size}" ("shock", "wide", "base", "stare")
        her @ cheeks blush "Why would she want that?!" ("shock", "wide", "base", "mid")
        her @ cheeks blush "" ("angry")
        gen "Because in my experience it feels awesome...{w=0.5}{nw}" ("grin", xpos="far_left", ypos="head")
        gen "Because in my experience it feels awesome...{fast} Wait, did that make it sound like I have a vagin--" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "You're wrong! She-- She--" ("shock", "closed", "angry", "mid")
        her @ cheeks blush "" ("angry", "happyCl", "worried", "mid")
        gen "What? Never done it before?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "{size=+4}OF COURSE NOT!{/size}" ("angry", "base", "angry", "mid")
        gen "I mean, I assumed you didn't have any real friends... But to get to your age and never eat another girl out? How shameful." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Not everyone in this school is as gross as you!" ("angry", "narrow", "annoyed", "mid")
        gen "well, there's one way to prove me wrong. Go find Katie and ask her yourself." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("annoyed", "narrow", "annoyed", "mid")
        her "Maybe I will..." ("open", "closed", "angry", "mid")
        her "" ("upset", "narrow", "annoyed", "mid")
        her "She will surely--" ("open", "closed", "base", "mid")
        her "{size=+4}HOLD ON!{/size}" ("scream", "wide", "base", "stare")
        her "" ("shock")
        gen "What?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I-I-I-I-I..." ("angry", "wide", "base", "mid")
        gen "Just spit it out!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I was so nervous with her that I just said yes! She'll be expecting me soon!" ("mad", "narrow", "base", "down")
        gen "You better get to it then, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "But I-- But I-- I couldn't--" ("shock", "narrow", "worried", "down")
        her @ cheeks blush "" ("angry")
        her @ cheeks blush "I'll just have to inform her that it was a misunderstanding, yes that will have to do." ("shock", "narrow", "base", "mid_soft")
        her @ cheeks blush "" ("angry", "narrow", "base", "mid_soft")
        gen "Sure, and risk her spilling the beans to your entire dorm that the proud Hermione Granger steals girls' panties." ("grin", xpos="far_left", ypos="head")
        her "..." ("soft", "narrow", "worried", "down")
        her @ cheeks blush "" ("soft", "closed", "angry", "mid")
        gen "Hey, for sixty points would you let me watch--" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Absolutely not!" ("scream", "base", "angry", "mid")
        her @ cheeks blush "" ("angry", "base", "angry", "mid")
        gen "That's a bummer..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("angry", "narrow", "angry", "R")
        gen "You can go then." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("annoyed")
        her @ cheeks blush "......" ("annoyed", "base", "worried", "mid")
        her @ cheeks blush "What about the points, sir?" ("open", "narrow", "worried", "mid_soft")
        her @ cheeks blush "" ("annoyed", "base", "worried", "mid")
        gen "Oh yes, right..." ("base", xpos="far_left", ypos="head")
        gen "Forty-five points to Gryffindor!" ("base", xpos="far_left", ypos="head")
        her "Thank you sir..." ("open", "narrow", "worried", "mid_soft")
        her "" ("upset", "base", "base", "R")
        pause 0.5

        call her_walk("mid", "base")

        gen "{i}Bon appetit!{/i}" ("grin", xpos="far_left", ypos="head")
        her "" ("open", "base", "base", "R", flip=True)
        pause 0.5
        her "..." ("angry", "base", "base", "mid", flip=True)
        her @ cheeks blush "(What did I get myself into this time...?)" ("angry", "narrow", "base", "down", flip=True)

        call her_walk(action="leave")

        call blkfade

        stop music fadeout 1.0

        pause 1.0
        play sound "sounds/knocking.ogg"
        "*Knock-knock-knock*"
        pause 1.0
        fem "Who is it?"
        pause 0.5
        her "It's me... Hermione Granger."
        play sound "sounds/door.ogg"
        her "Hello Katie I--"
        play sound "sounds/giggle2.ogg"
        "Katie" "Hey there sweet cheeks. {heart}{w=0.5} I have been waiting for you. {heart}{heart}{heart}"
        her "We need to talk--"
        "Katie" "I know exactly what we need. {heart}"
        play sound "sounds/slap_03.ogg"
        nar "Katie grabs Hermione and pulls her in the room{nw}"
        play sound "sounds/door2.ogg"
        nar "Katie grabs Hermione and pulls her into the room{fast}, then shuts the door."
        pause 1.0
        play sound "sounds/09_lock.ogg"
        pause 0.5
        her "Why did you lock the door...?!"
        play sound "sounds/cloth_sound.ogg"
        nar "Katie starts taking off her clothes."
        her "Wha-wha-what-t-t are you d-doing?!"
        play sound "sounds/giggle.ogg"
        "Katie" "Aren't you talkative today?{w=0.5} I would save my breath if I were you. {heart}{heart}{heart}"
        "Katie" "I'm quite{w=0.2} {heart}horny{heart}{w=0.2} so you might be stuck here for a while."
        play sound "sounds/push_on_bed.ogg"
        nar "She pushes Hermione onto the bed." with vpunch
        her "{size=+4}W-wait?!{/size}"
        play sound "sounds/sit_on_bed.ogg"
        nar "Then she swiftly straddles her face in cowgirl position." with hpunch
        play sound "sounds/gltch.ogg"
        her "..........!!!"
        her "*Hmph*"
        play sound "sounds/gasp2.ogg"
        "Katie" "Ahh!{heart} {w=0.5}So much better... {heart}{heart}{heart}"
        "Katie" "I'll start moving now.{w=0.5} You ready?"
        her "*Nwh*!!!"
        play sound "sounds/giggle3.ogg"
        "Katie" "I'll take that as a yes. {heart}{heart}{heart}"
        play sound "sounds/jump_on_bed.ogg"
        her "*Hmph{cps=10}hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh{/cps}*{nw}" with vpunch
        pause 1.0
        centered "{size=+7}{color=#cbcbcb}End of part three{/color}{/size}"
        jump panty_raid.choices

    elif pathvalue == 3:
        # Part 4
        centered "{size=+7}{color=#cbcbcb}A couple of months after the \"linguistics\" incident...{/color}{/size}"
        call hide_blkfade
        pause 1.0

        call her_walk(action="enter", xpos="mid", ypos="base")

        her "Hello, [name_genie_hermione].{heart}" ("smile", "wink", "base", "mid", xpos="right", ypos="base", trans=d3, flip=False)
        her "" ("smile", "base", "base", "mid")
        gen "[name_hermione_genie]! My favourite slut." ("grin", xpos="far_left", ypos="head")
        gen "I have another riddle for you." ("base", xpos="far_left", ypos="head")
        her "Oh, this ought to be fun." ("grin")
        her "Could you make it a {i}hard one{/i} [name_genie_hermione]?" ("open_wide_tongue")
        her "" ("smile")
        gen "You'll enjoy this one for sure...{w=0.5} Ready?" ("grin", xpos="far_left", ypos="head")
        her "Ready!" ("smile", "happyCl", "base", "mid")
        her "" ("base", "base", "base", "mid")
        gen "\"I am as soft and pure as a kitten, though far more desirable\"." ("base", xpos="far_left", ypos="head")
        her "*Hmm*..." ("base", "base", "base", "R")
        her "Boobs?{w=0.5} Titjob?" ("soft", "base", "base", "mid")
        her "" ("smile", "base", "base", "mid")
        gen "No. In this case, contrary to a titjob, it being both small and tight is usually preferred." ("base", xpos="far_left", ypos="head")
        her "Sex?" ("grin", "narrow", "base", "mid_soft")
        her "" ("base", "narrow", "base", "mid_soft")
        gen "Nope...{w=0.5} \"While boys may want me, they wouldn't be caught dead ever just buying me for themselves\"." ("base", xpos="far_left", ypos="head")
        her "Well that definitely rules out sex." ("open", "base", "base", "R")
        her "" ("base")
        gen "\"The less of me there is, the more... desirable... I become to behold\"." ("base", xpos="far_left", ypos="head")
        her "Oh! Oh! Panties!" ("crooked_smile", "closed", "base", "mid")
        her "" ("base", "base", "base", "mid")
        gen "Spot on." ("grin", xpos="far_left", ypos="head")
        her "Mine or someone else's?" ("smile", "happy", "base", "mid_soft")
        gen "Someone else's if you don't mind, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "On it! I'll be back soon..." ("base", "base", "base", "mid")

        call her_walk(action="leave")

        call blkfade

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"
        $ game.daytime = False
        call music_block

        pause 1.0
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base")

        her "Hello [name_genie_hermione], I hope I didn't keep you waiting for too long..." ("smile", "happy", "base", "mid_soft")

        call her_walk("desk", "base")

        her @ cheeks blush "I had a little...{w=0.3} \"setback\"{w=0.3} if you know what I mean..." ("grin", "narrow", "base", "mid_soft")
        her @ cheeks blush "" ("base")
        pause 0.5
        hide screen bld1
        hide hermione_main
        with d3
        "She drops a pair of laced white panties on your desk."
        show screen bld1 with d3
        gen "No trouble at all [name_hermione_genie]...{w=0.5} And you have excellent taste as always." ("base", xpos="far_left", ypos="head")
        play sound "sounds/sniff.ogg"
        gen "These smell fantastic!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "You're too kind [name_genie_hermione]." ("grin", "happy", "base", "mid_soft")
        hide screen bld1
        hide hermione_main
        with d3
        pause 1.0
        call gen_chibi("jerk_off_behind_desk")
        play sound "sounds/zipper.ogg"
        nar "You take your cock out and start stroking it..."
        call gen_chibi("jerk_off_behind_desk")
        her @ cheeks blush "Mmmm, [name_genie_hermione] need any help with that?" ("base", "squint", "base", "mid")
        gen "These already feel a little damp in the middle. Why don't you tell me why that is?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh you know, girls will be girls and all." ("grin", "narrow", "base", "mid_soft")
        gen "You know, charming the panties off someone is just a figure of speech." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Not anymore... I'd like to think Katie was quite pleased with me." ("smile", "narrow", "base", "mid_soft")
        gen "Katie? Katie Bell? The same delicious dyke that wanted you to clam joust with her?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Maybe..." ("smile", "narrow", "base", "R_soft")
        her @ cheeks blush "Although, Katie keeps raising the fee every time I ask." ("smile", "happyCl", "base", "mid")
        her @ cheeks blush "" ("open")
        her @ cheeks blush "Not that I mind, but my tongue can get quite sore sometimes." ("open_tongue")
        her @ cheeks blush "Especially since we've started the \"linguistics\" thing." ("open_wide_tongue", "squint", "worried", "up")
        her @ cheeks blush "" ("open_wide_tongue", "squint", "worried", "up")
        gen "Ugh!" ("angry", xpos="far_left", ypos="head")
        call cum_block
        call gen_chibi("cum_behind_desk")
        her @ cheeks blush "" ("open_wide_tongue", "narrow", "base", "mid_soft")
        pause 1.5
        call gen_chibi("cum_behind_desk_done")
        her @ cheeks blush "Oh, poor [name_genie_hermione], I had no idea you were so pent up. You can start calling me out more than twice a day if that isn't enough." ("soft", "narrow", "worried", "mid_soft")
        gen "During the day? But what about your classes?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Hmm*? Oh well, missing one or two wouldn't hurt... Especially if the headmaster has an important \"assignment\" for me." ("base", "narrow", "base", "mid_soft")
        gen "I'll consider it... Now let's circle back to you, Katie, and your binge of her minge." ("base", xpos="far_left", ypos="head")
        her "Professor... How dare you... I would never even think to shamelessly do something so heinous with a classmate and give you all the juicy details..." ("annoyed", "base", "base", "R")
        her @ cheeks blush "For less than forty house points." ("grin", "wink", "base", "mid")
        her @ cheeks blush "" ("base", "narrow", "base", "mid_soft")
        gen "Maybe next time [name_hermione_genie]. I'm a little... spent for tonight." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "We both know you could go for longer if you wanted to..." ("soft", "narrow", "base", "mid_soft")
        her @ cheeks blush "but you're right, we'll leave it for later." ("base", "happy", "base", "mid_soft")
        her @ cheeks blush "See you tomorrow [name_genie_hermione]." ("smile", "wink", "base", "mid")

        call her_walk(action="leave")

        pause 1.0
        gen "... *Hmm*...{w=1.0} I don't think I ever gave her points." ("base", xpos="far_left", ypos="head")
        pause 0.5

        show screen blkfade with d9
        stop music fadeout 5.0

        call gen_chibi("sit_behind_desk")
        centered "{size=+7}{color=#cbcbcb}End of part four{/color}{/size}"
        jump panty_raid.choices
