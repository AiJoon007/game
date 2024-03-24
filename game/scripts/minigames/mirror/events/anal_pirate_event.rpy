
label anal_pirate_rewards:
    if not card_exist(unlocked_cards, card_maslab):
        call give_reward("Ye plundered a special card from 'er cavern.", "images/cardgame/t1/genie_realm/maslab_v1.webp")
        $ unlocked_cards += [card_maslab]
    return

label anal_pirate_event:
    # Mirror story: A booty at sea
    # TODO: Add pirate outfit

    with d5
    centered "{size=+7}{color=#cbcbcb}Booty at sea{/color}{/size}"

    "This story is a rewrite of the \"Time for anal\" personal favour. And the genie is a pirate? Who knows... Enjoy."

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
        "-Part one-":
            $ d_flag_01 = 0
        "-Part two-":
            $ d_flag_01 = 1
        "-Part three-":
            $ d_flag_01 = 2
        "-Return-":
            $ renpy.end_replay()

    call music_block
    call her_chibi("stand","mid","base")
    call hide_blkfade

    if d_flag_01 == 0:
        call anal_pirate_event_1
    elif d_flag_01 == 1:
        call anal_pirate_event_2
    elif d_flag_01 == 2:
        call anal_pirate_event_3

    hide hermione_main
    call blkfade

    stop music fadeout 1.0
    stop background

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    call hide_blkfade

    her @ cheeks blush "Thank you, captain..." ("grin", "base", "base", "mid",xpos="right",ypos="base", flip=False)
    call her_walk(action="leave")

    call blkfade
    call her_chibi("hide")
    hide screen main_room

    jump anal_pirate_event.choices

label anal_pirate_event_1:
    gen "lass... I'd like you to role-play with me." ("base", xpos="far_left", ypos="head")
    her "captain...?" ("annoyed", "squint", "base", "mid", xpos="right", ypos="base")
    gen "How familiar ye be wit' th' term \"Swabbing ye poop deck\"?" ("base", xpos="far_left", ypos="head")

    her "Ninety galleon points..." ("annoyed", "narrow", "annoyed", "mid")
    gen "Wha'?" ("base", xpos="far_left", ypos="head")
    her "............................." ("disgust", "narrow", "base", "mid_soft")
    gen "Ah, well then lass. Ninety galleon points 'tis." ("base", xpos="far_left", ypos="head")

    call anal_pirate_event_common_1_2

    return

label anal_pirate_event_2:
    gen "lass?" ("base", xpos="far_left", ypos="head")
    her "captain?" ("soft", "base", "base", "mid", xpos="right", ypos="base")
    gen "I shall be takin' ye on another voyage today..." ("base", xpos="far_left", ypos="head")
    her "............." ("open", "squint", "base", "mid")
    gen "Care t' guess wha' th' destination will be?" ("base", xpos="far_left", ypos="head")
    gen "You have t' guess three times to find out." ("base", xpos="far_left", ypos="head")
    her "..........." ("annoyed", "squint", "angry", "mid")
    her "Booty plundering?" ("disgust", "narrow", "base", "mid_soft")
    gen "Wha..........?!" ("angry", xpos="far_left", ypos="head")
    gen "How did ye...?" ("angry", xpos="far_left", ypos="head")
    her "You seem like a booty pirate kind of a man. captain..." ("angry", "base", "angry", "mid")
    gen "I'm not sure you know what that means, lass..." ("base", xpos="far_left", ypos="head")


    call anal_pirate_event_common_1_2

    return

label anal_pirate_event_common_1_2:

    her "..........." ("annoyed", "base", "worried", "R")
    gen "Time to get me ole cannon out..." ("base", xpos="far_left", ypos="head")
    her "................." ("angry", "happyCl", "worried", "mid",emote="sweat")
    call blkfade
    $ desk_OBJ.hidden = True
    play sound "sounds/08_hop_on_desk.ogg"
    pause 2
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    play sound "sounds/boing02.ogg"
    her "!!!" ("angry", "wide", "base", "stare", ypos="head", flip=True)
    play sound "sounds/slap_02.ogg"
    gen "Blistering barnacles!" ("angry", xpos="far_left", ypos="head")
    her @ tears soft_blink "Ouch!" ("mad", "happyCl", "worried", "mid")
    gen "Jus' try t' loosen up a wee, would ye?" ("base", xpos="far_left", ypos="head")
    her @ tears soft "I be tryin'!" ("angry", "base", "base", "mid")
    gen "Aye, wha' if I do this...?" ("base", xpos="far_left", ypos="head")
    play sound "sounds/boing03.ogg"
    her @ tears soft_blink "Ouch! Wha' are ye doin', captain?" ("mad", "happyCl", "worried", "mid")
    gen "Aye, this won't work either..." ("base", xpos="far_left", ypos="head")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "Har har, I reckon I know wha' we should do." ("base", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    menu:
        "{size=-3}\"I reckon I'll raise the anchor 'n jus' set sail!\"{/size}":
            play music "music/pirate.ogg" fadein 1 fadeout 1 if_changed
            play background "sounds/CreakingShip.ogg"

            her "Just set sail, captain?!" ("angry", "wide", "base", "stare", ypos="head", flip=True)
            play sound "sounds/spit.ogg"
            gen "*SPIT!*" ("angry", xpos="far_left", ypos="head")
            her "What are ye doing you Seadog!" ("scream", "happyCl", "worried", "mid")
            her "No, cap'n, Belay that! Ye're nah in open waters--" ("open", "base", "base", "mid")
            gen "No needs, raise the anchor! Heave Ho!" ("base", xpos="far_left", ypos="head")
            play sound "sounds/gltch.ogg"
            with hpunch
            her @ tears soft "ARGH!" ("angry", "base", "base", "mid")
            her @ tears soft_blink "Ouch! Ouch! Ouch!" ("mad", "happyCl", "worried", "mid")
            gen "Nigh-on in! Me ship has left ye harbour lass!" ("angry", xpos="far_left", ypos="head")
            her "No, ye're hurtin' me! Ye be hurtin' me!" ("scream", "happyCl", "worried", "mid")
            gen "Yo-Ho-Ho!" ("angry", xpos="far_left", ypos="head")
            her "Blisterin' Barnacles! It hurts!" ("scream", "happyCl", "worried", "mid")
            gen "Shut it, lass! I be approaching ye secret cavern!" ("angry", xpos="far_left", ypos="head")
            gen "Yer cavern be so tight 'tis completely un-plunderable!" ("angry", xpos="far_left", ypos="head")
            her @ tears soft_blink "Then stop, Scallywag!" ("mad", "happyCl", "worried", "mid")
            gen "Neigh! We needs t' excavate yer cavern a wee!" ("base", xpos="far_left", ypos="head")
            her @ tears soft_blink "But I don't wants ye t'!" ("mad", "happyCl", "worried", "mid")
            gen "Aye? How do ye expect scallywags t' farrg ye up yer arse then?" ("base", xpos="far_left", ypos="head")
            her "Wha' scallywags?" ("shock", "happyCl", "worried", "mid")
            gen "Ye know... scallywags." ("angry", xpos="far_left", ypos="head")
            gen "Argh, Blimey... Me cannon be to wide now." ("angry", xpos="far_left", ypos="head")
            her "Stop then! Avast, captain!" ("open", "happyCl", "worried", "mid")
            her "Change course captain, I've changed me mind! I don't needs ninety galleon points!"
            gen "I reckon I be right on course..." ("angry", xpos="far_left", ypos="head")

            play sound "sounds/gltch.ogg"
            with hpunch
            with kissiris
            her "{size=+5}AAAAAAAAhhhhh!!!{/size}" ("scream", "wide", "base", "stare")
            gen "Yo-Ho-Ho!!!" ("angry", xpos="far_left", ypos="head")

            call her_chibi_scene("sex_slow")
            with d5

            her "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!" ("scream", "wide", "base", "stare")
            gen "Let us pump this wee cavern full o' seamen then, savvy?" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "Aye... , I jus' wants this t' end..." ("scream", "happyCl", "worried", "mid")
            gen "Agh... Ye wants this voyage t' end sooner?" ("angry", xpos="far_left", ypos="head")
            gen "I smell mutiny, do ye want to walk the plank?" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "*sob!* How?" ("shock", "base", "base", "R")
            gen "Ye know..." ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Aye..." ("shock", "base", "base", "R")
            her @ cheeks blush tears soft "I be a wench??" ("clench", "base", "worried", "mid")
            gen "Yes ye be!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "*Sob!* I be a wench..." ("angry", "squint", "base", "mid")
            her "I love t' suck ye pegleg..."
            her @ cheeks blush tears crying "'n now me wee asshole be gettin' ripped t' pieces... *Sob!*" ("angry", "narrow", "base", "dead")
            gen "Shiver Me Timbers!" ("angry", xpos="far_left", ypos="head")
            gen "Agrh! Thar She Blows!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "No! Be it gettin' bigger?! I be like a harpoon!" ("open", "wide", "worried", "stare")
            gen "ARGH!" ("angry", xpos="far_left", ypos="head")

        "{size=-3}\"Lather me cannon balls first. Lubricate me pegleg!\"{/size}":
            her "Oh... Alright..." ("open", "base", "base", "mid", ypos="head", flip=True)
            play music "music/pirate.ogg" fadein 1 fadeout 1 if_changed
            play background "sounds/CreakingShip.ogg"

            call her_chibi_scene("bj")

            hide screen blktone
            hide screen bld1
            call hide_blkfade
            call ctc

            her "*Slurp!* *Slurp!* *Slurp!*"
            gen "Aye... good..." ("base", xpos="far_left", ypos="head")
            her "*Slurp!* *Slurp!* *Slurp!*"
            gen "Yarr, I reckon that be enough. Back on th' ship now." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("sex_pause", trans=fade)

            # On the desk
            her "............." ("open", "base", "base", "mid")
            gen "Aye! Sail, Ho!!" ("angry", xpos="far_left", ypos="head")
            her "Ouch!" ("scream", "happyCl", "worried", "mid")
            gen "Relax lass. Approaching harbour." ("base", xpos="far_left", ypos="head")

            pause.2

            play sound "sounds/gltch.ogg"
            with hpunch
            with kissiris
            her "{size=+5}AAAAAAAAhhhhh!!!{/size}" ("scream", "wide", "base", "stare")

            call her_chibi_scene("sex_slow", trans=d5)
            with d5

            gen "Argh!!!" ("angry", xpos="far_left", ypos="head")
            her "Ye... ye..." ("scream", "wide", "base", "stare")
            her "Ye ship be to great!" ("shock", "happyCl", "worried", "mid")
            gen "Let us pump this wee cavern full o' seamen then, savvy?" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "....................." ("angry", "squint", "base", "mid")
            call ctc

            her @ cheeks blush tears soft "....................." ("shock", "base", "base", "R")
            gen "Ye be fine thar, wench?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Blisterin' Barnacles... Ye be... turnin' me folds inside out... captain." ("clench", "base", "worried", "mid")
            her @ cheeks blush "Me stitches be breaking..." ("angry", "squint", "base", "mid")
            gen "Aye..." ("base", xpos="far_left", ypos="head")
            gen "Maybe me cannon needs swabbin'...?" ("base", xpos="far_left", ypos="head")
            gen "Go below deck, lass. swabb me cannon some more." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Wha'? But..." ("clench", "base", "worried", "mid")
            her @ cheeks blush tears soft "But it be rusty... 'tis been in me bilge." ("shock", "base", "base", "R")
            gen "Aye, 'tis been abaft, but that's nah nigh ye bilge." ("base", xpos="far_left", ypos="head")
            gen "Heave ho landlubber or me ship be sinkin', lass. Swab me cannon some more." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "..........." ("shock", "base", "base", "R")

            # Sucking
            call her_chibi_scene("bj")
            with fade
            call ctc

            her "*Slurp!* *Slurp!* *Slurp!*" (ypos="head", flip=False)
            gen "Aye... good lass..." ("base", xpos="far_left", ypos="head")
            her "*Slurp!* *Slurp!* *Slurp!*"
            gen "Can ye taste yer arse on me cannon?" ("base", xpos="far_left", ypos="head")
            her "*Slurp!* *Slurp!* *Slurp!*"
            gen "Aye, Maybe that be enough." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("sex_slow")
            with fade
            call ctc

            her @ cheeks blush tears soft "*Ah*..." ("shock", "base", "base", "R")
            gen "We be smooth sailing lass?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "It still be hurting..." ("clench", "base", "worried", "mid")
            her "But th' storm has passed."
            gen "I'll adjust th' sails fer now..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ah*... I be greatful, captain." ("angry", "squint", "base", "mid")
            gen "Oh... aye... ye secret cavern be great..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "..........." ("shock", "base", "base", "R")
            gen "Oh... Ye cavern be perfect, lass..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "................" ("shock", "narrow", "base", "down")
            gen "Why are ye bein' so quiet lass?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "'cause 'tis cavern be too shallow for ye ship..." ("clench", "base", "worried", "mid")
            her "'n I jus' wants ye t' cum sooner, captain..."
            gen "So ye stifle yer cries o' pain?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "Aye captain. *Sob!*" ("angry", "narrow", "base", "dead")
            gen "Nah on me ship lass." ("base", xpos="far_left", ypos="head")
            gen "Sob, scream 'n cry as much as ye wish!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "B-but--" ("clench", "base", "worried", "mid")
            gen "That shall make me cannon ready t' fire in ye broadside." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "be this true? *Sob!*" ("angry", "narrow", "base", "dead")
            her @ cheeks blush tears soft "*Sob!* Me hull! *Sob!* It be taking in water! *Sob!*" ("shock", "base", "base", "R")
            gen "Aye, ye ship be sinking... ye booty be mine." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "*SOB!*" ("angry", "squint", "base", "mid")
            gen "Ye poor wee sprog..." ("base", xpos="far_left", ypos="head")
            gen "A grand, wicked pirate be plunderin' yer booty!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "*SOB!* Yeees! *SOB!*" ("scream", "squint", "base", "mid")
            gen "Take me seamen!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "No, I'm scared! *SOB!*" ("scream", "happyCl", "worried", "mid")

        "{size=-3}\"Let me oil ye up.\"{/size}":
            play music "music/pirate.ogg" fadein 1 fadeout 1 if_changed
            call her_chibi_scene("sex_pause", trans=fade)
            her "oil, cap'n?!" ("angry", "wide", "base", "stare")
            gen "Blimey! Just stay still." ("base", xpos="far_left", ypos="head")
            "*Squeeze!*"
            her "Ahhh! Shiver me timbers, tis cold!" ("scream", "happyCl", "worried", "mid")
            nar "Ye thoroughly oil 'er cavern."
            gen "Sail ho!" ("base", xpos="far_left", ypos="head")
            her "Nay, cap'n, wait! Maybe--" ("angry", "base", "worried", "mid")
            nar "Alas! Ye align thee tip of yer cannon with 'er slimey winky cavern and push fore."

            pause.2

            play sound "sounds/gltch.ogg"
            with hpunch
            with kissiris
            her @ tears soft "ARGH!" ("shock", "base", "base", "mid")
            nar "Yer ship fully docked in her as thee oil does its job."
            gen "Farrg me!" ("angry", xpos="far_left", ypos="head")


            call her_chibi_scene("sex_slow", trans=d5)

            her @ tears soft_blink "Ouch! Ouch! Ouch!" ("mad", "happyCl", "worried", "mid")
            her "No, ye're hurtin' me! Ye be hurtin' me!" ("scream", "happyCl", "worried", "mid")
            gen "*Argh* Farrg, I can nah pull out!" ("angry", xpos="far_left", ypos="head")
            her "Sink me! It hurts!" ("scream", "happyCl", "worried", "mid")
            gen "Then stop clenching on me so hard, ye wench!" ("angry", xpos="far_left", ypos="head")
            gen "Yer cavern be so tight I can nah even move!" ("angry", xpos="far_left", ypos="head")
            her @ tears soft_blink "Do somethin'!" ("mad", "happyCl", "worried", "mid")
            gen "I be tryin', wench!" ("angry", xpos="far_left", ypos="head")
            her @ tears soft "Then try harder!" ("scream", "base", "angry", "mid")
            call slap_her
            her @ tears soft "..........!" ("scream", "wide", "worried", "mid")
            gen "Shut th' Davy Jones' locker up, strumpet!" ("angry", xpos="far_left", ypos="head")
            gen "'tis..." ("angry", xpos="far_left", ypos="head")
            call slap_her
            gen "'tis...{fast} yer..." ("angry", xpos="far_left", ypos="head")
            call slap_her
            gen "'tis... yer...{fast} bloody..." ("angry", xpos="far_left", ypos="head")
            call slap_her
            gen "'tis... yer... bloody... {fast}fault!" ("angry", xpos="far_left", ypos="head")
            call slap_her
            pause 1.0
            play sound "sounds/plop.ogg"
            with hpunch

            call her_chibi_scene("sex_pause", trans=d5)
            pause 1.0
            gen "Oh, 'tis worked." ("base", xpos="far_left", ypos="head")

            her @ cheeks blush tears soft "*sob!*" ("mad", "base", "angry", "down")
            her @ cheeks blush tears soft "... me cavern... me poor cavern... *sob*" ("mad", "base", "angry", "mid")
            gen "In that case, let's try it again." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "No! Avast! Cap'n!" ("open", "wide", "worried", "mid")
            her @ cheeks blush tears soft "I 'ave changed me mind!"
            gen "'twill be fine this time, trust me..." ("base", xpos="far_left", ypos="head")

            play sound "sounds/gltch.ogg"
            with hpunch
            with kissiris
            her "{size=+5}AAAAAAAAhhhhh!!!{/size}" ("scream", "wide", "base", "stare")
            gen "YARR!!!" ("angry", xpos="far_left", ypos="head")

            call her_chibi_scene("sex_slow", trans=d5)

            her "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!" ("scream", "wide", "base", "stare")
            gen "I shall pump this wee cavern full o' seamen then, savvy?" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "Aye... , I jus' wants this t' end..." ("scream", "happyCl", "worried", "mid")
            gen "Agh... Ye wants 'tis t' end sooner?" ("angry", xpos="far_left", ypos="head")
            gen "Help me out then!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "*sob!* How?" ("shock", "base", "base", "R")
            gen "Ye know..." ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Oh..." ("shock", "base", "base", "R")
            her @ cheeks blush tears soft "I be a wench??" ("clench", "base", "worried", "mid")
            gen "Aye ye be!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "*Sob!* I be a wench..." ("angry", "squint", "base", "mid")
            her "I love t' suck pegleg..."
            her @ cheeks blush tears crying "'n now me wee cavern be gettin' ripped apart... *Sob!*" ("angry", "narrow", "base", "dead")
            gen "Aye! Aye!" ("angry", xpos="far_left", ypos="head")
            gen "Agrh! AYE!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "No! Be it gettin' bigger?! I be yellow-bellied!" ("open", "wide", "worried", "stare")
            gen "ARGH!" ("angry", xpos="far_left", ypos="head")

    menu:
        "-Sink her vessel, fill her up-":
            gen "Argh!" ("angry", xpos="far_left", ypos="head")
            play sound "sounds/fuse.ogg"
            her "No! AH!" ("scream", "wide", "base", "stare", ypos="head", flip=True)
            play sound "sounds/cannon.ogg"
            call cum_block
            gen "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}" ("angry", xpos="far_left", ypos="head")

            call her_chibi_scene("sex_cum_in", trans=d5)

            play sound "sounds/cannon.ogg"
            call cum_block
            call ctc

            her @ cheeks blush tears messy "AH! ME BILGE IS FILLING UP! Sink Me!{heart}{heart}{heart}" ("open", "wide", "worried", "stare")
            gen "Aye, ye wench! I be shooting me cannons!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "Me hull is splintering, spare me Captain!" ("angry", "squint", "base", "mid")
            gen "Ye're nah sunk yet!" ("angry", xpos="far_left", ypos="head")
            play sound "sounds/cannon.ogg"
            with hpunch
            her @ cheeks blush tears messy "No, I be already full! Stop cummin', ye bastard!" ("scream", "wide", "worried", "stare")
            gen "Shut th' farrg up, wench! Ye still be afloat!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "No! Me stomach! Me ship will capsize!" ("scream", "squint", "base", "mid")
            play sound "sounds/cannon.ogg"
            with hpunch
            gen "ARGH!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "No! I reckon me bilge be flooded... I must get t' me pumps." ("open", "wide", "worried", "stare")
            play sound "sounds/cannon.ogg"
            with hpunch
            play sound "sounds/burp.ogg"
            her @ tears messy "{size=+7}*BURP!*!!!!!{/size}" ("full", "wide", "worried", "stare")
            her @ tears messy "......................." ("full", "base", "base", "mid")
            her "............."
            play sound "sounds/gulp.ogg"
            her "{size=+7}*GULP!*{/size}" ("cum", "happyCl", "worried", "mid")
            her @ cheeks blush tears messy "*SOB!* I HATE YOU..." ("angry", "squint", "base", "mid")
            her @ cheeks blush tears messy "{size=+5}I HATE YE'N AND YER RUSTY OLE CANNON!{/size}" ("scream", "base", "angry", "mid")
            her "{size=+5}I HATE YE'N! YE HEAR ME?!{/size}"
            gen "Agh... Dead men tell no tales, wench!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "*sob!* *Sob!*..." ("angry", "squint", "base", "mid")

            # After cum inside
            call her_chibi_scene("sex_cum_in_done", trans=d5)

            her @ cheeks blush tears crying "*Sob!*..." ("angry", "narrow", "base", "dead")
            gen "Whew!... I reckon me gunpowder needs restocking in the next harbour.' it be." ("base", xpos="far_left", ypos="head")
            gen "Ye afloat lass?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "Aye... *Sob!*" ("angry", "narrow", "base", "dead")
            gen "Is that sea water in ye eyes?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "Me bilge is flooded, but me pumps be workin, captain..." ("angry", "narrow", "base", "dead")
            gen "Aye, ye took me cannonfire broadside, Ye be a well built vessel..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "Thank ye captain..." ("angry", "narrow", "base", "dead")
            hide screen bld1
            with d3
            call ctc

            call her_chibi_scene("sex_cum_in_done", trans=d5)
            pause.8

            $ hermione.zorder = 15 # Reset zorder

            her @ cheeks blush tears mascara "I apologise for saying that I hate you, captain..." ("base", "base", "base", "R", ypos="head", flip=True)
            her @ cheeks blush tears mascara "And your cannon is not rusty..."
            her @ cheeks blush tears mascara "I don't know what's gotten into me..." ("grin", "narrow", "worried", "mid_soft")
            gen "My cannonfire!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush tears mascara "I suppose it's when you call me a \"wench\". I know that it's just roleplay..." ("grin", "narrow", "worried", "mid_soft")
            gen "Aye, sure..." ("base", xpos="far_left", ypos="head")
            gen "Does it still hurt?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears mascara "A little..." ("open", "narrow", "worried", "mid_soft")
            her @ cheeks blush tears mascara "I also feel full and warm inside..." ("grin", "closed", "base", "mid")
            gen "You plan to keep it in? My cum I mean." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears mascara "Aye.." ("grin", "narrow", "base", "mid_soft")
            her @ cheeks blush tears mascara "I hope I won't spring a leak during my classes..."
            gen "Well, good luck on your voyage." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears mascara "Can I get paid now please?" ("grin", "closed", "base", "mid")

        "-Spread yer cannon fire o'er er hull-{#LINT_IGNORE}":
            play sound "sounds/fuse.ogg"
            gen "*argh*" ("angry", xpos="far_left", ypos="head")
            gen "{size=+6}Fire!{/size}" ("angry", xpos="far_left", ypos="head")
            hide screen bld1
            with d3

            call cum_block
            play sound "sounds/cannon.ogg"
            with hpunch

            call her_chibi_scene("sex_cum_out", trans=d5)

            call cum_block
            call ctc

            her "*Ah*...{heart}{heart}{heart}" ("silly", "narrow", "base", "dead", ypos="head", flip=True)
            gen "Aye!!! All over yer hold!" ("angry", xpos="far_left", ypos="head")
            her "*Ah*... No, me hull!" ("silly", "narrow", "annoyed", "up")
            hide screen bld1
            with d3
            play sound "sounds/cannon.ogg"
            call cum_block
            with hpunch
            call ctc

            call her_chibi_scene("sex_cum_in_done", trans=d5)
            pause.8

            gen "Well, I'm done... You can get off my ship now." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Yes, captain..." ("silly", "base", "worried", "mid", ypos="head", flip=True)
            gen "You feeling alright?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Yes, captain. It still hurts a little, but..." ("shock", "base", "base", "R")
            gen "But what?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "But in a good way... captain." ("silly", "base", "worried", "mid")
            gen "In a good way, *huh*?" ("base", xpos="far_left", ypos="head")
            gen "Heh... You naughty, little pirate." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Can I my get my share of the booty now, captain?" ("silly", "base", "worried", "mid")

    return

label anal_pirate_event_3:

    gen "How about another booty plunderin, lass?" ("base", xpos="far_left", ypos="head")
    her "Of course, captain." ("base", "narrow", "base", "up", xpos="right", ypos="base")
    gen "Raise anchor, you little tart!" ("grin", xpos="far_left", ypos="head")

    stop music fadeout 1.0
    hide hermione_main
    call blkfade
    $ desk_OBJ.hidden = True

    her "........" ("annoyed", "base", "worried", "R", ypos="head", flip=True)
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    her "..........." ("open", "base", "base", "mid")
    play sound "sounds/gltch.ogg"
    with hpunch
    with kissiris
    her "Ooooohhhhhhhhhhhh....{heart}" ("scream", "wide", "base", "stare")

    call her_chibi_scene("sex_slow", trans=d5)

    gen "Oh, ye-es!" ("angry", xpos="far_left", ypos="head")
    her "*Ah*..." ("soft", "narrow", "annoyed", "up")
    gen "It seems like yer cavern be a bit more welcomin', lass." ("base", xpos="far_left", ypos="head")
    her "*Ah*... It still be a bit tight." ("base", "narrow", "base", "mid_soft")
    her "'n , jus' call me \"wench\", captain." ("base", "squint", "base", "mid")
    gen "*Agh*! Ye wench! Ye always get me wit' yer words!" ("angry", xpos="far_left", ypos="head")

    play music "music/pirate.ogg" fadein 1 fadeout 1 if_changed
    play background "sounds/CreakingShip.ogg"
    her "*Ah*... *Ah*..." ("open", "closed", "base", "mid")
    her "*Ah*..."
    her "captain?" ("base", "narrow", "base", "mid_soft")
    gen "Aye, wench?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*..." ("angry", "base", "base", "mid")
    her "Would ye settle down fer me, captain?" ("angry", "narrow", "base", "down")
    with hpunch
    gen "{size=+9} WHAT?!{/size}" ("angry", xpos="far_left", ypos="head")
    gen "Don't tell me ye're expecting cargo, lass!" ("angry", xpos="far_left", ypos="head")
    her "Ye seamen don't put no cargo in me bilge, captain..." ("angry", "wink", "base", "mid")
    gen "Wha' be this natter o' settlin down then?" ("base", xpos="far_left", ypos="head")
    her "Ye misunderstood me captain." ("angry", "base", "base", "mid")
    her "I meant t' say, would ye stop plunderin for a lass {size=+5}like{/size} me?" ("angry", "narrow", "base", "down")
    her "I would ne'er propose t' a scallywag wit' his pegleg in me arse, captain..." ("angry", "happyCl", "worried", "mid",emote="sweat")
    gen "Good. 'cause I don't reckon any scallywag would be able t' say \"neigh\" to you lassie." ("base", xpos="far_left", ypos="head")
    her "*Ah*{heart}..." ("open", "closed", "base", "mid")
    her "Wha' I meant-- *Ah*{heart}... {w}t' say was-- *Ah*{heart}... {w}do ye reckon any pirate would ever-- *Ah*{heart}... {w}leave th' sea fer a lass like me?" ("angry", "narrow", "base", "down")
    gen "*huh*?" ("base", xpos="far_left", ypos="head")
    her "I mean, wit' all that booty plunderin happenin' lately... *ah*{heart}..." ("angry", "narrow", "base", "down")
    her "I can nah help but feel like me hull is scratched... leakin even."
    her "'n in a no way untarnished..."
    her "Who would wants t' settle fer a lass like that." ("angry", "base", "base", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "{size=-3}\"I would leave me ship in a heartbeat!\"{/size}":
            her "What?" ("open", "base", "base", "mid", ypos="head", flip=True)
            gen "Aye, if only a lass like ye would board me ship..." ("base", xpos="far_left", ypos="head")
            her "... Aye...{heart}" ("base", "base", "base", "R")
            her ".............." ("base", "happy", "base", "mid")
            her "Aye if only a lass like I, cap'n? So, why neigh me?" ("soft", "base", "base", "mid")
            gen "*huh*?" ("base", xpos="far_left", ypos="head")
            gen "Wha' do ye mean \"why\", wench?" ("base", xpos="far_left", ypos="head")
            gen "Ye be right out of harbour 'n ye only just set sail..." ("base", xpos="far_left", ypos="head")
            gen "Tight cabin, shimering tits, 'n wet wee powder pan..." ("base", xpos="far_left", ypos="head")
            her "*Ah*...{heart}" ("open", "closed", "base", "mid")
            gen "Ye will make some lucky scallywag a mighty happy one, some day, wench." ("base", xpos="far_left", ypos="head")
            gen "*Ehm*, I mean, lass." ("base", xpos="far_left", ypos="head")
            her "No, \"wench\" be good. you be calling me that more, captain." ("silly", "narrow", "annoyed", "up")
            gen "Thar, ye see? Ye be a great catch, I be tellin' ye, wench." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "*Ah*...{heart} Thank you, captain." ("angry", "narrow", "base", "dead")
            gen "*huh*?" ("base", xpos="far_left", ypos="head")
            gen "Ye helm be leakin." ("base", xpos="far_left", ypos="head")

        "{size=-3}\"A pirate not plunderin t' be wit' ye be o' th' picture\"{/size}":
            her @ cheeks blush tears crying "I be thinkin that..." ("shock", "narrow", "base", "down", ypos="head", flip=True)
            gen "Oh... I jus' love that wee cavern o' yers!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "....................." ("angry", "narrow", "base", "dead")
            her "Aye... Aft all th' thin's I had t' do fer me crew..."
            her @ cheeks blush tears messy "... nah one we pirate would leave th' sea fer me..." ("angry", "squint", "base", "mid")
            gen "Oh, they be leavin th's sea fer ye alright!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "Wha'? But ye said..." ("open", "wide", "worried", "stare")
            gen "T' plunder yer cave, lass. But they'd go back t' sea." ("base", xpos="far_left", ypos="head")
            gen "But as a cannon swabber ye be a great catch!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "Aye?" ("open", "wide", "worried", "stare")
            gen "Ye pullin' me pegleg?!" ("base", xpos="far_left", ypos="head")
            gen "Young, hot 'n slutty. Ye could 'ave any scallywag ye wants!" ("base", xpos="far_left", ypos="head")
            gen "Or a landlubber or whatever ye be after..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "I reckon ye may be right, captain." ("base", "narrow", "worried", "mid_soft")
            gen "I always be right, wench." ("base", xpos="far_left", ypos="head")
            gen "Now wiggle that wee arse o' yers a wee." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Like this?" ("silly", "base", "worried", "mid")
            gen "Aye, that be a good wench." ("base", xpos="far_left", ypos="head")
            her "I be a wench, aren't I?" ("silly", "narrow", "base", "dead")
            gen "Ye jus' sold me yer asshole fer ninety galleon points. What ye be calling that?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "Yes, yes...{heart} I be nothing but a wench...{heart}" ("silly", "base", "worried", "mid")
            gen "Ye helm be leakin." ("base", xpos="far_left", ypos="head")

    her "Not only me helm, captain...{heart}{heart}{heart}" ("silly", "narrow", "base", "dead")
    gen "Not just ye helm?" ("base", xpos="far_left", ypos="head")
    her "I'm cumming captain...{heart}{heart}{heart}" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "Agh! My cock!" ("angry", xpos="far_left", ypos="head")
    gen "Relax your muscles a little, would you?" ("angry", xpos="far_left", ypos="head")
    her "BUT I'M CUMMING!{heart}{heart}{heart}" ("open", "happyCl", "worried", "mid")
    gen "Fine! 'ave it yer way wench!" ("angry", xpos="far_left", ypos="head")
    with hpunch
    her "{size=+7}*Ah-ah-aha*!!! I'm cumming!!!{/size}" ("scream", "wide", "base", "stare")
    gen "{size=+7}Argh!{/size}" ("angry", xpos="far_left", ypos="head")

    play sound "sounds/fuse.ogg"
    gen "!!!" ("angry", xpos="far_left", ypos="head")
    menu:
        "-Sink 'er vessel, fill her up-":

            call her_chibi_scene("sex_cum_in", trans=d5)

            play sound "sounds/cannon.ogg"
            call cum_block
            with hpunch
            call ctc

            her "!!!" ("scream", "wide", "base", "stare", ypos="head", flip=True)
            gen "Shiver me timbers! Argh!" ("base", xpos="far_left", ypos="head")
            her "*Ah*!{heart} 'tis fillin' me up!{heart} me bilge is takin in water!{heart}" ("silly", "narrow", "annoyed", "up")
            gen "'tis nah water, wench!" ("base", xpos="far_left", ypos="head")
            play sound "sounds/cannon.ogg"
            call cum_block
            with hpunch
            her @ cheeks blush tears crying "Ah! I BE A WENCH!!!!{heart}{heart}{heart}" ("scream", "happyCl", "worried", "mid")
            play sound "sounds/cannon.ogg"
            with hpunch
            gen "*Agh*!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "*Ah*...{heart} yer seamen, captain...{heart}" ("open", "wide", "worried", "stare")
            gen "Aye, my seamen..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "*Ah*...{heart}" ("angry", "squint", "base", "mid")
            gen "......" ("base", xpos="far_left", ypos="head")

        "-Spread yer cannon fire o'er er hull-{#LINT_IGNORE}":
            hide screen bld1
            with d3

            play sound "sounds/cannon.ogg"

            call her_chibi_scene("sex_cum_out", trans=d5)

            call cum_block
            with hpunch
            call ctc

            her "*Ah-aha*! Ye're cummin'! {heart}{heart}{heart}" ("silly", "narrow", "base", "dead", ypos="head", flip=True)
            gen "{size=+7}Aye I do, wench{/size}" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "Blisterin' Barnacles, me too! Me too!" ("scream", "happyCl", "worried", "mid")
            gen "{size=+7}FARRRGIN' WENCH!{/size}" ("angry", xpos="far_left", ypos="head")
            play sound "sounds/cannon.ogg"
            call cum_block
            with hpunch
            her @ cheeks blush tears crying "*Ah*...{heart} yer cum...{heart}" ("angry", "narrow", "base", "dead")
            her "Ye covered me whole deck{heart}{heart}{heart}"
            gen "Aye!!! All o'er yer hull!" ("angry", xpos="far_left", ypos="head")
            play sound "sounds/cannon.ogg"
            with hpunch
            her "Shiver me timbers... 'tis so hot!" ("silly", "narrow", "annoyed", "up")

    #Ending
    call hide_characters
    show screen blkfade
    with d7

    call her_chibi_scene("sex_pause", trans=fade)

    gen "Well, tis been intense..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "*Ah-ha*...{heart} *Ah*...{heart}" ("grin", "narrow", "base", "dead", ypos="head", flip=True)
    gen "Ye be fine lass?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "I reckon so... I be nah sure..." ("grin", "narrow", "base", "dead")
    her @ cheeks blush tears messy "I reckon I may still be leakin', captain." ("grin", "narrow", "base", "dead")
    her @ cheeks blush tears messy "Or maybe nah..." ("grin", "narrow", "base", "dead")
    her "Everythin' be in a daze... 'n me legs feel so weak..."
    her "Can I jus' get paid now, captain?"

    stop music fadeout 1.0

    return
