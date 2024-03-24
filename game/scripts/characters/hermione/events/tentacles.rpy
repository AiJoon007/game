#Public tentacle scene
label tentacle_scene_intro:
    with d3
    show screen bld1

    if not states.her.ev.sealed_scroll.examined:
        $ states.her.ev.sealed_scroll.examined = True
        gen "(*Hmm*... Let's see if we can get this writing to show...)" ("base", xpos="far_left", ypos="head")
        gen "(It should be something simple like a command word...)" ("base", xpos="far_left", ypos="head")

        $ d_flag_01 = False
        $ d_flag_02 = False
        $ d_flag_03 = False
        label .spell:
        if d_flag_01 and d_flag_02 and d_flag_03:
          jump .after_spell
        menu:
          "\"Open Sesame!\"" if not d_flag_01:
            $ d_flag_01 = True
            gen "...{w=0.8} Guess not..." ("base", xpos="far_left", ypos="head")
            jump .spell
          "\"Hocus Pocus!\"" if not d_flag_02:
            $ d_flag_02 = True
            gen "...{w=0.8} Damn..." ("base", xpos="far_left", ypos="head")
            jump .spell
          "\"Abracadabra!\"" if not d_flag_03:
            $ d_flag_03 = True
            gen "...{w=0.8} ..." ("base", xpos="far_left", ypos="head")
            jump .spell

        label .after_spell:
        gen "Work, you stupid scroll, or I'll throw you in the fire!" ("angry", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        "The scroll" "*Reveals itself*"
        gen "That's what I thought..." ("base", xpos="far_left", ypos="head")

        gen "Now then... Let's find out what this scroll says..." ("base", xpos="far_left", ypos="head")
        gen "\"At the highest point is where I'm hidden\"..." ("base", xpos="far_left", ypos="head")
        gen "(Fuck, it's a riddle...{w=0.4} Guess I deserved that...)" ("angry", xpos="far_left", ypos="head")

        gen "\"At the highest point is where I'm hidden\"--" ("base", xpos="far_left", ypos="head")
        gen "\"A place where you will need this key\"--" ("base", xpos="far_left", ypos="head")
        gen "\"To use this scroll that is forbidden\"--" ("base", xpos="far_left", ypos="head")
        gen "\"You'll need to take a piece of me\"..." ("base", xpos="far_left", ypos="head")

        gen "Key... What k--" ("base", xpos="far_left", ypos="head")
        play sound "sounds/magic1.ogg"
        show screen white
        with d9
        pause 0.9
        hide screen white
        with d5
        gen "*ARGH*!" ("angry", xpos="far_left", ypos="head")
        gen "(Bloody magic...)" ("angry", xpos="far_left", ypos="head")
        gen "(Oh look, a rusty key just popped out from that scroll...)" ("base", xpos="far_left", ypos="head")
        gen "(How convenient...)" ("base", xpos="far_left", ypos="head")
        gen "(Now I'll just have to find where it fits...)" ("base", xpos="far_left", ypos="head")
        jump main_room_menu

    gen "(Okay... So...{w=0.3} What was this scroll supposed to do again?)" ("base", xpos="far_left", ypos="head")
    gen "(Let's see...)" ("base", xpos="far_left", ypos="head")
    if not states.her.ev.sealed_scroll.sample:
        gen "Right, the riddle..." ("base", xpos="far_left", ypos="head")

        label .riddle:
        gen "\"At the highest point is where I'm hidden\"--" ("base", xpos="far_left", ypos="head")
        gen "\"A place where you will need this key\"--" ("base", xpos="far_left", ypos="head")
        gen "\"To use this scroll that is forbidden\"--" ("base", xpos="far_left", ypos="head")
        gen "\"You'll need to take a piece of me\"..." ("base", xpos="far_left", ypos="head")

        menu:
            gen "..." ("base", xpos="far_left", ypos="head")
            "-Continue-":
                pass
            "-Repeat the riddle-":
                jump tentacle_scene_intro.riddle

        gen "(Well... I have the key, now to figure out the rest...)" ("base", xpos="far_left", ypos="head")
        gen "(The highest point... *Hmm*... I wonder where that could be.)" ("base", xpos="far_left", ypos="head")
        jump main_room_menu
    else:
        gen "(Ah, that's it... It's supposed to turn me into some sort of magical tentacle plant...)" ("base", xpos="far_left", ypos="head")
        gen "(I have everything I need to perform the ritual and have some fun with Hermione.)" ("base", xpos="far_left", ypos="head")

        if not game.daytime:
            gen "(*Hmm*... But it's too late for me to use it now. I should do it at dawn, before class has started.)" ("base", xpos="far_left", ypos="head")
            jump main_room_menu
        elif states.her.busy:
            gen "(*Hmm* But Hermione is busy at the moment, I should postpone my plans until tomorrow.)" ("base", xpos="far_left", ypos="head")
            jump main_room_menu

    gen "(I better write her a note first, so she can carry me with her to class...)" ("base", xpos="far_left", ypos="head")
    call gen_chibi("paperwork")
    with d3
    pause 1.0

    # Setup
    $ states.her.busy = True
    $ d_flag_01 = []
    $ d_flag_02 = False

    menu:
        gen "(*Hmm*... how should I start?)" ("base", xpos="far_left", ypos="head")
        "\"Dear Hermione, ...\"":
            $ d_flag_01.append("Dear Hermione,\n\n")
        "\"Dear [name_hermione_genie], ...\"":
            $ d_flag_01.append("Dear [name_hermione_genie],\n\n")
        "\"You, the bimbo, ...\"":
            $ d_flag_01.append("You, the bimbo,\n\n")

    play sound "sounds/scribble.ogg"
    "*Scribble* *Scribble*"

    menu:
        gen "....*Mhmm*...." ("base", xpos="far_left", ypos="head")
        "\"... I had very important business matter to attend to...\"":
            $ d_flag_01.append("I had very important business matter to attend to,")
        "\"... I went out to visit a brothel...\"":
            $ d_flag_01.append("I went out to visit a brothel,")
        "\"... I have turned myself into a plant...\"":
            $ d_flag_01.append("I have turned myself into a plant,")
            $ d_flag_02 = True

    play sound "sounds/scribble.ogg"
    "*Scribble* *Scribble*"

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"... I ask you kindly...\"":
            $ d_flag_01.append("I ask you kindly,")
        "\"... Just listen for once...\"":
            $ d_flag_01.append("just listen for once and")

    play sound "sounds/scribble.ogg"
    "*Scribble* *Scribble*"

    menu:
        gen "... and now..." ("base", xpos="far_left", ypos="head")
        "\"... take this plant with you to your class...\"" if not d_flag_02:
            $ d_flag_01.append("take this plant with you to your class.\n\n")
        "\"... take this plant then shove it up your arse...\"" if not d_flag_02:
            $ d_flag_01.append("take this plant then {b}{s}shove it up your{/s}{/b} bring it to class.\n\n")
            gen "Shove it up your--..." ("grin", xpos="far_left", ypos="head")
            call gen_chibi("sit_behind_desk")
            with d3
            gen "I can't write that!" ("angry", xpos="far_left", ypos="head")
            gen "What if she does it and I get shat on... No, no, no, let me change that." ("base", xpos="far_left", ypos="head")
            call gen_chibi("paperwork")
            with d3
        "\"... take me to class...\"" if d_flag_02:
            $ d_flag_01.append("take me to class.\n\n")

        "\"... shove me up your arse...\"" if d_flag_02:
            $ d_flag_01.append("{b}{s}shove me up your{/s}{/b} take me to class.\n\n")
            gen "Shove me up your--..." ("grin", xpos="far_left", ypos="head")
            call gen_chibi("sit_behind_desk")
            with d3
            gen "I can't write that!" ("angry", xpos="far_left", ypos="head")
            gen "What if she does it and I get shat on... No, no, no, let me change that." ("base", xpos="far_left", ypos="head")
            call gen_chibi("paperwork")
            with d3

    play sound "sounds/scribble.ogg"
    "*Scribble* *Scribble*"

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"... Sincerely, Dombledure.\"":
            $ d_flag_01.append("Sincerely,\nDombledure.")
        "\"... Yours truly, [name_genie_hermione].\"":
            $ d_flag_01.append("Yours truly,\n[name_genie_hermione].")

    $ d_flag_01 = " ".join(d_flag_01)

    call gen_chibi("sit_behind_desk")
    with d3
    pause 1.0
    gen "Yes...{w=0.5} That should do it... Now to call her up here and use that scroll..." ("base", xpos="far_left", ypos="head")
    stop music fadeout 3.0
    show screen blkfade
    with d5
    centered "{size=+7}{color=#cbcbcb}A few moments later...{/color}{/size}"
    call gen_chibi("hide")
    $ desk_OBJ.foreground = "letter_and_plant_on_desk"
    hide screen blkfade
    with d5

    pause 3.0
    call her_walk(action="enter")
    with d3
    pause 1
    her "[name_genie_hermione], my class is about to--" ("open", "base", "worried", "L", trans=d3)
    her "[name_genie_hermione]?" ("open", "squint", "base", "L")
    call her_walk(xpos="mid", ypos="base")
    pause 1.0
    call chibi_emote("thought","hermione")
    pause 2.0
    call chibi_emote("hide", "hermione")
    her "Are we playing hide and seek??" ("annoyed", "base", "angry", "R", trans=d3)
    her "[name_genie_hermione], I really don't have the time--" ("annoyed", "narrow", "angry", "stare")
    hide hermione_main
    hide screen bld1
    with d3
    pause 1.0
    call chibi_emote("exclaim","hermione")
    pause 1.0
    call chibi_emote("hide", "hermione")
    her "..."
    call her_walk(xpos="desk", ypos="base")
    gen "(Yes... She's seen me...)" ("base", xpos="far_left", ypos="head")
    gen "(Take the note!)" ("base", xpos="far_left", ypos="head")
    her "What's with this ugly plant?" ("disgust", "narrow", "angry", "stare", trans=d3)
    with vpunch
    gen "(I'm not ugly!)" ("angry", xpos="far_left", ypos="head")
    gen "(... Just haven't blossomed yet...)" ("base", xpos="far_left", ypos="head")
    pause 1.0
    call her_chibi("stand", flip=True)
    with d3
    her "Professo--...?" ("open", "base", "worried", "L", flip=True, trans=d3)
    her "I thought I heard him for a second..." ("annoyed", "narrow", "worried", "R")
    gen "(Read the note already, would you...)" ("base", xpos="far_left", ypos="head")
    pause 1.0
    call her_chibi("stand", flip=False)
    with d3
    her "Oh, there's also a note, I better read it..." ("open", "base", "base", "down", flip=False, trans=d3)

    gen "(Can't help herself but snoop in other peoples' business, can she...)" ("base", xpos="far_left", ypos="head")
    $ desk_OBJ.foreground = "plant_on_desk"
    with d3
    play sound "sounds/pageflip.ogg"
    her "Oh... It's actually addressed to me..." ("soft", "base", "base", "stare")

    hide hermione_main
    with d3

    # Read letter from Genie
    $ Letter(text=d_flag_01).open()

    her "...................................." ("disgust", "narrow", "angry", "mid", trans=d3)
    her "So I'm a delivery girl as well now?" ("annoyed", "narrow", "angry", "stare")
    her "Well... I suppose I'm already heading that way anyway..." ("annoyed", "closed", "angry", "stare")
    her "I guess he must've checked my schedule for once..." ("annoyed", "narrow", "worried", "R")
    gen "(Herbology class, here I come!)" ("grin", xpos="far_left", ypos="head")

    hide hermione_main
    hide screen plant_on_desk
    call her_chibi("hide")
    show screen blkfade
    with d9

    pause 1.5
    play sound "sounds/door.ogg"
    pause 1
    centered "{size=+7}{color=#cbcbcb}Herbology{/color}{/size}"
    pause 1

    play music "music/hidden-agenda-by-kevin-macleod.ogg" fadein 1 if_changed
    play background "sounds/murmur.ogg" fadein 2 fadeout 2

    spo "In today's class, we will be learning about a plant called Devil's Snare."
    spo "Hermione Granger was kind enough to bring us a pot with an underdeveloped Devil's Snare."
    spo "It's kind of wilted and looks weak but..."
    gen "(Oh fuck you, bitch!)" ("angry", xpos="far_left", ypos="head")
    her "Actually, professor, that was--"
    spo "Miss Granger, please don't interrupt me."
    her "Sorry..."
    spo "Now then..."
    spo "This is an incredibly dangerous plant, known to constrict and kill its prey with its fast and powerful tendrils."
    spo "They are found naturally in caves and swamps as they like dark and damp places and hate sunlight."
    her "Isn't Devil's Snare extremely dangerous?"
    spo "Yes, Miss Granger. At least you're paying attention to what I was saying... Now, please sit down."
    play sound "sounds/giggle2_loud.ogg"
    pause 1.5
    play sound "sounds/shush.ogg"
    her "..........."
    spo "These aren't even a week old, so they would barely be able to stroke you with their tendrils, let alone constrict you."
    spo "Now everyone, pass the samples around so that you all can get a good look."
    her "Professor Sprout, are they supposed to have mouths?"
    spo "Yes Miss Granger, it's how they consume their prey once they have asphyxiated them."
    her "Okay, well, what are the eyes for? I thought they sensed their prey by touch?"
    spo "What are you on about, Miss Granger? Devil's Snare don't have eyes."
    her "This one d--"
    play sound "sounds/crowd_gasp.ogg"
    play sound2 "sounds/plant_burst.ogg"
    stop background
    with vpunch
    pause 2.0
    nar "All of a sudden, you explode outwards in a flash of thick green tentacles."
    her "What's happening?!?"
    play sound "sounds/plant_grab.ogg"
    nar "You quickly bind her wrists and waist..."
    play sound "sounds/gasp.ogg"
    her "I can't move!"
    play sound "sounds/creaking.ogg"
    nar "Then lift her into the air with your powerful appendages..."
    spo "Stay calm, Miss Granger! Devil's Snare will let you go if you don't move!"
    nar "Slinking your slimy tentacles under her top and skirt."
    if not hermione.is_worn("panties"):
        mal "Hey, look, look! She doesn't have panties on!"
        fem "Oh my gosh, so the rumours about her were true?!"
        mal2 "And she brought her own plant sample, I bet she planned this out, what a total slut!"
    her "Oh no..."
    play sound "sounds/cloth_rip.ogg"
    nar "You rip her top off in a flurry of buttons and cotton..."
    her "*Ahhhh*!"
    play sound "sounds/plant_slithering.ogg"
    nar "Sliding your tentacles up her legs and slowly pulling them apart."
    nar "Hermione struggles against you, but her efforts are in vain."
    her "Please no... Not here."
    if hermione.is_worn("panties"):
        nar "The tentacles slowly remove her panties, revealing her pussy to the entire class."
    mal "Wow..."
    fem "This is horrible, someone should do something!"
    mal2 "Professor Sprout says as long as she doesn't move she'll be released."
    play sound "sounds/plant_slithering.ogg"
    nar "You position a large, flowered tentacle above Hermione's head."
    her "What is that!?"
    play sound "sounds/creaking.ogg"
    nar "It suddenly opens to reveal a long slender appendage with an engorged base."
    her "What the hell is that? It looks like a..."
    nar "While she is focused on the dangling limb above her, you move six of your smaller tentacles towards her waist."
    her "Oh god no, someone, please help me! Professor Sprout, do something!"
    spo "Students, stand back!"
    nar "Professor Sprout casts an impressive-looking spell at the mass of writhing tentacles."
    play sound "sounds/magic3.ogg"
    spo "Confringo!"
    play sound "sounds/plop.ogg"
    nar "It strikes the plant forcefully but does nothing."
    spo "What? That should have killed it. It must be magically protected."
    nar "You move three tentacles to Hermione's vagina and start teasing the opening."
    her "Please Professor Sprout, do something! Anything!"
    spo "I'm not sure I can, it has a powerful magical aura protecting it."
    spo "If I try anything more advanced than the spell I just cast, I might hurt you."
    nar "You move two smaller tentacles to her asshole and start teasing the entrance, slowly prying it open."
    her "Then what am I supposed to do?!"
    spo "Just stay as still as possible, and it should eventually let you go..."
    nar "You move a tentacle with a mouth on the end of it to her right breast and latch onto it."
    her "Please, I'm not going to be able to stay still if this keeps going!"
    nar "The three tentacles at the entrance of her vagina suddenly thrust into her."

    play sound "sounds/slick_02.ogg"

    if states.her.public_level > 15:
        call tentacle_1
    else:
        call tentacle_2

    stop background fadeout 3.0

    nar "After everyone leaves the room, your body starts to turn back to normal..."
    gen "That was hot!"
    nar "You notice that something is amiss..."
    gen "What happened to my clothes?!"
    gen "... I was expecting this other-wordly magic to cover the basics of transmutations at the very least."
    gen "Guess I was wrong..."
    gen "I must get out of here before anyone spots me."

    play sound "sounds/run_03.ogg"

    nar "You dash through the castle in a flash and get back to your office where, fortunately, you find some spare clothes lying about."

    $ desk_OBJ.foreground = None
    $ sealed_scroll_ITEM.used = True
    $ sealed_scroll_ITEM.owned = 0

    hide screen blkfade
    with d5

    jump main_room

label tentacle_1: #Public path
    show her_tentacles_public_1 as cg zorder 17
    hide screen blkfade
    with d9
    call ctc

    her "!!!"
    her "What on earth is going on?"
    play background "sounds/slickloop.ogg" fadein 2 fadeout 2
    nar "You slowly begin to move the tentacles in her vagina."
    show her_tentacles_public_2 as cg
    her "Oh..."
    nar "You move a small, mouthed tentacle to her ear so that only she can hear you."
    gen "Enjoying yourself slut?"
    her "Professor!"
    gen "That's right, just do as I say and relax."
    her "How am I supposed to relax?!"
    gen "Well if you're not going to relax, at least try to enjoy it..."
    nar "You start rotating the tentacles in her vagina."
    play sound "sounds/slick_02.ogg"
    show her_tentacles_public_3 as cg
    her "..."
    spo "If you keep thrashing about so much it won't let you go, stay still, girl!"
    her "I-I'm trying!"
    gen "Are you sure you're trying enough? Judging by how much you're moving, I'd say that's quite the opposite."
    gen "Someone might even think that you are enjoying this."
    her "They wouldn't..."
    mal "Who's she talking to?"
    mal2 "I've got no idea, this bitch is crazy."
    gen "Are you sure? Do you think you'll be able to stifle every moan?"
    play sound "sounds/slick_02.ogg"
    nar "You push deeply into her with the three tentacles."
    her "!!!"
    show her_tentacles_public_4 as cg
    gen "Do you think you'll be able to stop your hips from bucking?"
    nar "You give her another powerful thrust."
    play sound "sounds/slick_02.ogg"
    her "{size=-6}{heart}*Ah*{/size}"
    gen "Do you really think that you'll be able to stop yourself from begging me for more?"
    nar "You increase the speed of the tentacles."
    play background "sounds/slickloopfast.ogg" fadein 2 fadeout 2
    her "{size=-3}*mmmmmmm*{/size}"
    gen "I don't think you will. In fact, I know that you won't."
    gen "Because I know what you are. A slut."
    gen "A slut who can only think about getting off when she's being fucked by a plant in front of her classmates."
    stop background fadeout 2
    nar "You stop moving the tentacles."
    gen "Now tell them what you are."
    her "W-w-what? No, please, just don't stop."
    play sound "sounds/creaking.ogg"
    gen "Tell them what you are, and I'll keep going."
    her "I can't... Just keep going..."
    gen "Say it."
    her "{size=-3}I'm a slut.{/size}"
    play background "sounds/slickloop.ogg" fadein 2 fadeout 2
    nar "You start rotating the tentacles in her vagina ever so slowly."
    gen "What was that? I don't think that they heard you. Why don't you say it once more, with feeling."
    her "I'm a slut!"
    play background "sounds/slickloopveryfast.ogg" fadein 2 fadeout 2
    nar "You begin fiercely fucking her vagina."
    her "Yes, yes, I'm a fucking slut. Fuck me harder."
    gen "See that wasn't so hard now was it. How about I give you a little reward."
    her "Wha--"
    show her_tentacles_public_5 as cg
    nar "You thrust a ribbed tentacle deeply into her asshole in one motion."
    play sound "sounds/slick_02.ogg"
    her "!!!"
    her "It's in my ass... I-I'm...{w=0.4} I-I'm cumming."
    nar "You take alternating turns pumping into her ass and pussy."
    her "I'm cumming! It's too much..."
    show her_tentacles_public_6 as cg
    play sound "sounds/slick_01.ogg"
    nar "You feel her body shudder as the orgasm rocks her."
    nar "This only spurs you on to fuck her harder."
    her "Please... no more... I'll faint..."
    nar "You start to feel a strange energy flowing through the vines, moving towards the tips."
    gen "This is it girl, get ready."
    her "... ready?..."
    show her_tentacles_public_7 as cg
    stop background fadeout 2
    play sound "sounds/slick_01.ogg"
    nar "With one final surge you release the pent-up energy in a surge of white sap all over her."
    play sound "sounds/slick_02.ogg"
    gen "By the gods, it's as if each vine is cumming. This is amazing..."
    play sound "sounds/slick_02.ogg"
    nar "The sensations proved too much for Hermione, and she faints, going limp in your tentacles."
    mal "What a slut..."
    fem "That's what I've been telling you!"
    mal2 "Man, I'm going to have to join Gryffindor."
    show screen blkfade
    hide cg
    with d9
    pause.8
    nar "You place Hermione back onto the desk as the plant that you are occupying slowly wilts and dies."
    nar "Professor Sprout quickly runs over."
    spo "Miss Granger, are you okay?"
    her "..."
    spo "Quickly, someone take her to the hospital wing."
    mal "Should we cover her up?"

    # This is the public route, don't change writing please!

    if hermione.is_worn("panties"):
        spo "Oh yes, I suppose you should."
        mal "{size=-4}Damn dude, have you seen her tits?!{/size}"
        nar "*Squeeze* *Squeeze*"
        mal2 "{size=-4}Holy shit, they're soft.{/size}"
        spo "If you two don't stop that at once you'll get expelled."
        mal "S-sorry..."
        mal2 "Sorry professor!"
        spo "Just take her out."
    else:
        spo "No need, if she feels comfortable parading without panties in MY class, then she should be fine being taken naked to the infirmary."
        mal "Are you su--"
        spo "I said take her out!"
        mal "Y-yes ma'am..."

    play sound "sounds/run_04.ogg"

    nar "You hear the boys snickering to each other whilst they carry Hermione out in some unknown direction..."

    spo "Class dismissed!"

    show screen blkfade
    with d9
    pause.8

    return

label tentacle_2: # Personal path
    show her_tentacles_personal_1 as cg zorder 17
    hide screen blkfade
    with d9
    call ctc

    her "What kind of sick plant is this?!"
    play background "sounds/slickloop.ogg" fadein 2 fadeout 2
    nar "You start pumping the tentacles in her vagina slowly..."
    her "Oh..."
    nar "You move a small tentacle with a mouth on the end to her ear so that only she can hear you."
    gen "Enjoying yourself, [name_hermione_genie]?"
    her "Profes--"

    show her_tentacles_personal_2 as cg
    call ctc

    play sound "sounds/slick_02.ogg"
    nar "You quickly force another flowered tentacle into her mouth."
    gen "Now, now [name_hermione_genie], you don't want anyone to find out how much you are enjoying yourself now, do you?"
    her "*Hmmmhhhhhhhhh* !"
    gen "Well, then just do what Miss Sprout says and stay still."
    gen "Just act like this is some horrible accident, that you are just a victim."
    gen "Instead of the slut that you really are..."
    play sound "sounds/slick_02.ogg"
    nar "You start to rotate the tentacles in her vagina."
    gen "!!! *HMMMMM*"
    mal "Wow, I think she's starting to enjoy it."
    fem "Hermione? No way, she's too stuck-up to let boys kiss her, not to mention enjoying sex. {size=-6}With a plant but still...{/size}"
    mal2 "I don't know man, she doesn't look like she hates it."
    play background "sounds/slickloopfast.ogg" fadein 2 fadeout 2
    nar "You increase the speed of the tentacles in her vagina."
    gen "Hear that, [name_hermione_genie]? Your classmates are starting to realise how much you like getting your pussy stuffed."
    her "*NNNNNNNNNm*"
    gen "What was that? Faster you say?"
    gen "You got it, [name_hermione_genie]!"
    show her_tentacles_personal_3 as cg
    play background "sounds/slickloopveryfast.ogg" fadein 2 fadeout 2
    nar "You begin fucking Hermione in earnest."
    her "*Hmmmmm...!!!*"
    nar "The sensation of fucking Hermione in two different holes is almost overwhelming."
    gen "I know you are loving every second of this..."
    gen "... Being fucked in front of your classmates."
    gen "Having your tits and pussy on display..."

    nar "You move a ridged tentacle towards her ass."
    her "*Mm eehh oorr mmmnooo*!"
    play sound "sounds/slick_02.ogg"
    show her_tentacles_personal_4 as cg
    nar "You enter her tight ass. The feeling of being in every hole at once is incredible."
    her "*Mmmmmmmmh*"
    nar "Hermione barely manages a groan, overwhelmed by the sheer amount of pleasure she is currently bombarded with."
    play background "sounds/slickloop.ogg" fadein 2 fadeout 2
    gen "Admit it! You're loving this, aren't you?"
    gen "Having your holes filled in front of your classmates like the whore you are."
    gen "Go on, say it! Tell me what you are!"
    her "*Hmmm aaaaa hhhhhhuuuttt*"
    gen "What was that, I couldn't quite make it out over the sound of you sucking dick."
    her "*Hmmm aaaaa hhhhhhuuuttt*!"
    gen "One last time. Say it like you mean it."
    show her_tentacles_personal_5 as cg
    nar "As she exhales, you quickly remove the tentacle from her mouth."
    her "{size=+5}I'm a slut!{/size}"
    nar "The realisation of what has just occurred hits her like a ton of bricks."
    her "I-I'm cumming... Professor--"
    show her_tentacles_personal_6 as cg
    play sound "sounds/slick_02.ogg"
    nar "You quickly reinsert the tentacle into her mouth, silencing her."
    gen "Good girl. Time for your reward."
    play background "sounds/slickloopveryfast.ogg" fadein 2 fadeout 2
    nar "You quicken the pace as she convulses beneath you."
    show her_tentacles_personal_7 as cg
    play sound "sounds/slick_01.ogg"
    nar "You explode inside of her from every tentacle-like head, filling her up to the brim."
    stop background fadeout 2
    play sound "sounds/slick_02.ogg"
    mal "Told you she was a slut."
    play sound "sounds/slick_02.ogg"
    fem "I guess you were right..."

    show screen blkfade
    with d9
    hide cg

    pause.8
    nar "Professor Sprout quickly runs over."
    spo "Miss Granger, are you okay? Miss Granger!"
    her "..................*Ah*"
    spo ".... She's breathing, thank be Merlin."
    spo "You! Yes, you girls! Take her to the hospital wing at once!"
    fem "W-wha-- But..."
    spo "What are you waiting for!"
    fem "{size=-4}Fine...{/size}"

    play sound "sounds/run_03.ogg"
    pause 3.0

    spo "Class dismissed!"

    return
