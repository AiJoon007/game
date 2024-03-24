

### Tier 2 ###

label hg_pf_grope_breasts_T2:
    stop music fadeout 1.0
    call her_chibi_scene("grope_tits", trans=d7)
    pause.8

    her "!!!" ("normal", "wide", "worried", "shocked")
    nar "Hermione takes a hesitant step back..."

    her @ cheeks blush "!!!?" ("mad", "wide", "base", "stare", ypos="head", trans=hpunch)
    call ctc

    nar "Hermione tries to pull away from you, but you hold her firmly by her breasts..."

    her @ cheeks blush "??!" ("base", "narrow", "base", "up")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 #SEX THEME. if_changed
    her @ cheeks blush "[name_genie_hermione], what are you--?" ("angry", "happyCl", "worried", "mid",emote="sweat")
    nar "She tries to pull away again."
    nar "You squeeze her tits like a vice."

    her @ cheeks blush "[name_genie_hermione], you're hurting me!" ("angry", "squint", "base", "mid")
    gen "Then stand still, [name_hermione_genie]!" ("angry", xpos="far_left", ypos="head")
    her "B-but..." ("soft", "wide", "base", "stare")
    gen "All I want to do is squeeze your tits a little, then you will get your points!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "B-but... This is..." ("disgust", "narrow", "base", "down")
    gen "Just stand still..." ("base", xpos="far_left", ypos="head")
    gen "Go to your happy place or something..." ("base", xpos="far_left", ypos="head")
    her "M-my happy place...?" ("angry", "wink", "base", "mid")
    nar "You feel the girl's shapely breasts in your palms..."

    her "............................" ("shock", "happyCl", "worried", "mid", ypos="head")

    menu:
        "-Squeeze her tits with all of your strength-":
            $ states.her.mood += 6
            nar "You put strength into your hold..."
            her @ cheeks blush "My........." ("disgust", "narrow", "base", "down")
            nar "You squeeze her tits even harder..."
            her "[name_genie_hermione], you're hurting them..." ("shock", "happyCl", "worried", "mid")
            gen "Be quiet [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Ouch........." ("disgust", "narrow", "base", "down")
            nar "You squeeze her ample tits with all your strength."
            her @ cheeks blush "Ah! It hurts!" ("angry", "squint", "base", "mid")
            her @ cheeks blush "They're gonna burst! Please stop it!" ("angry", "squint", "base", "mid")
            gen "They are not going to burst, you silly girl..." ("base", xpos="far_left", ypos="head")
            nar "You loosen your grip slightly..."
            her "It hurts..." ("shock", "happyCl", "worried", "mid")
            gen "You'll be fine..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "........." ("annoyed", "narrow", "angry", "R")

            jump end_hg_pf_grope

        "-Give her tits a tender massage-":
            $ states.her.mood += 3
            nar "You start massaging Hermione's breasts through her clothes..."
            her "[name_genie_hermione]...?" ("shock", "happyCl", "worried", "mid")
            gen "The points, [name_hermione_genie]... You need the points. Concentrate on that." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes..." ("annoyed", "narrow", "angry", "R")
            her @ cheeks blush "Yes, for the honour of the Gryffindor house..." ("angry", "happyCl", "worried", "mid")
            "*Squeeze-squeeze*"
            nar "You keep massaging her tits..."
            nar "You give one of her breasts a few pinches trying to locate the nipple..."
            her "[name_genie_hermione]... You're pinching me...?" ("shock", "happyCl", "worried", "mid")
            nar "Your attempts prove to be fruitless, though... The fabric of her clothes is quite thick..."
            her @ cheeks blush "Gryffindor........." ("angry", "happyCl", "worried", "mid")

            jump end_hg_pf_grope

        "-Let her go and give her the points-":
            gen "Well, if you're going to make a drama out of this, you might as well leave..." ("base", xpos="far_left", ypos="head")
            nar "You unhand the girl's breasts..."
            her @ cheeks blush "Thank you..." ("soft", "closed", "base", "mid")
            gen "But you didn't earn it today..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..............." ("annoyed", "base", "angry", "mid")

            jump end_hg_pf_grope

### Tier 3 ###

label hg_pf_grope_breasts_T3: # Hermione gets mad if you slap them.
    call her_chibi_scene("behind_desk_front", trans=d7)
    $ hermione.strip("robe", "accessory")

    if states.her.status.stripping:
        menu:
            "\"First, lift up your top!\"" if hermione.is_worn("top"):
                her "[name_genie_hermione]?!" ("clench", "base", "base", "mid")
                gen "What? It's not like I haven't seen them before..." ("base", xpos="far_left", ypos="head")
                her "But!" ("clench", "narrow", "base", "down")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
                gen "I just want to massage them a little..." ("base", xpos="far_left", ypos="head")
                her "..............................." ("annoyed", "narrow", "base", "down")
                her "Promise me you will be gentle with them." ("soft", "narrow", "base", "mid_soft")
                gen "Sure..." ("base", xpos="far_left", ypos="head")

                call her_chibi_scene("behind_desk_front_show_tits", trans=d5)
                with d5

                gen "Nice...{w} Now take it off will you?" ("base", xpos="far_left", ypos="head")

                $ hermione.strip("top")
                call her_chibi_scene("behind_desk_front", trans=d5)
                with d3

                gen "Very good..." ("base", xpos="far_left", ypos="head")
                her "..." ("soft", "narrow", "base", "R", trans=d5)

                if hermione.is_worn("bra"):
                    gen "Now your bra..." ("base", xpos="far_left", ypos="head")

                    $ hermione.strip("bra")
                    her "..." ("annoyed", "narrow", "base", "mid")

            "\"Yes, let me feel them!\"":
                pass

    pause.5

    menu:
        gen "(Let's see now...)" ("base", xpos="far_left", ypos="head")
        "-Grab them-":
            jump hg_pf_grope_breasts_T3_continue

        "-Slap them-":
            pass


    # Event fails
    nar "You give Hermione's tits a loud slap!"
    call slap_her

    $ states.her.mood += 10
    her @ cheeks blush "!!!" ("scream", "wide", "base", "stare")
    her @ cheeks blush "Ouch! It hurts! *SOB*!" ("angry", "base", "worried", "mid")
    gen "Did you like it though?" ("base", xpos="far_left", ypos="head")
    her "Did I... \"like it\", [name_genie_hermione]...?" ("annoyed", "narrow", "annoyed", "mid")
    her "What girl in her right mind would like to be treated this way?" ("angry", "narrow", "annoyed", "mid")

    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    $ hermione.wear("all")

    hide screen blkfade

    her @ cheeks blush tears soft "You are a mean and demented old man!" ("angry", "base", "angry", "mid", xpos="mid", ypos="base")
    gen "............" ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    gen "(Well, no points for Gryffindor then...)" ("base", xpos="far_left", ypos="head")

    jump end_hermione_event

label hg_pf_grope_breasts_T3_continue:
    call her_chibi_scene("grope_tits", trans=d7)
    call ctc

    her ".............................." ("angry", "narrow", "base", "down")
    gen "You have great tits, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "...................................." ("angry", "narrow", "base", "down")
    gen "You like it when I squeeze them like this?" ("base", xpos="far_left", ypos="head")
    her "Excuse me, [name_genie_hermione], but you are confusing me with one of those lowly harlots again..." ("upset", "closed", "base", "mid")
    her "I am only letting you fondle me because I am getting paid for it..." ("upset", "closed", "base", "mid")
    her "Not because I enjoy it..." ("upset", "closed", "base", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "So, you're more like a prostitute then..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]!" ("angry", "wide", "base", "stare")
    her "Prostitutes are paid to have sex with men..." ("angry", "wide", "base", "stare")
    her "I'd never do something like that!" ("upset", "closed", "base", "mid")

    nar "You squeeze one of the girl's tits tightly and give the other a couple of firm tugs."

    her "*Ah*..." ("open", "happyCl", "worried", "mid")
    gen "Enjoying yourself, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

    her "[name_genie_hermione], I am only doing this--" ("upset", "closed", "base", "mid")

    nar "You squeeze both of her tits with force..."

    her "*Ah*..." ("shock", "happyCl", "worried", "mid")
    gen "Tell me you like this, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], I am only letting you do this to me because--" ("open", "happyCl", "worried", "mid")
    gen "I know, I know..." ("base", xpos="far_left", ypos="head")
    gen "You are starting to sound like a broken record." ("base", xpos="far_left", ypos="head")
    her "...." ("annoyed", "narrow", "annoyed", "mid")

    jump end_hg_pf_grope

### Tier 4 ###

label hg_pf_grope_breasts_T4:
    stop music fadeout 1.0
    call her_chibi_scene("behind_desk_front", trans=d7)
    pause.8

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    $ hermione.strip("robe", "accessory")

    if hermione.is_worn("top"):
        nar "But before you manage to grab them, Hermione shifts to start undoing her clothes..."

        her @ cheeks blush "..." ("base", "narrow", "worried", "down", trans=d3)

        menu:
            "\"That's right, take it off!\"":
                $ hermione.strip("top")
                with d3

                if hermione.is_worn("bra"):
                    gen "Show them to me at once!" ("grin", xpos="far_left", ypos="head")
                    her "......."
                    $ hermione.strip("bra")
                pass

            "\"No, leave it on.\"":

                gen "I want to massage them with your top on..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh, I see..." ("open", "base", "base", "R")
                jump hg_pf_grope_breasts_T4_clothed

    elif hermione.is_worn("bra"):
        nar "But before you manage to grab them, Hermione shifts to start undoing her bra..."
        $ hermione.strip("bra")
        her @ cheeks blush "" ("base", "narrow", "worried", "down")
        call ctc
        gen "Very good..." ("base", xpos="far_left", ypos="head")


    jump hg_pf_grope_breasts_T4_naked

label hg_pf_grope_breasts_T4_naked:
    stop music fadeout 1.0
    call her_chibi_scene("behind_desk_front", trans=d7)
    call ctc

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    hide hermione_main
    her @ cheeks blush "" ("base", "narrow", "worried", "mid", xpos="mid", ypos="base")
    call ctc

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Grab them-":
            jump hg_pf_grope_breasts_T4_continue

        "-Slap them-":
            pass

    nar "You give Hermione's tits a loud slap!"
    call slap_her

    her @ cheeks blush "!!!" ("scream", "wide", "base", "stare")
    her @ cheeks blush "Ouch!" ("angry", "base", "worried", "mid")
    her "[name_genie_hermione], what did you do that for?"
    gen "Dunno... Seemed like a good idea..." ("base", xpos="far_left", ypos="head")
    gen "Did you like it?" ("base", xpos="far_left", ypos="head")
    her "... Of course not, [name_genie_hermione]." ("annoyed", "closed", "base", "mid")
    gen "Let's try this again, then." ("base", xpos="far_left", ypos="head")
    her "What?" ("annoyed", "base", "base", "mid")
    call slap_her

    her @ cheeks blush "!!!" ("scream", "wide", "base", "stare")
    her "Ouch! Stop hurting me!"
    gen "Admit that you enjoy it, and I will." ("base", xpos="far_left", ypos="head")
    her "But I don't..." ("disgust", "narrow", "base", "down")
    her "And if you plan to keep on doing this to me, [name_genie_hermione]..."
    her "... then I think I should leave." ("annoyed", "narrow", "annoyed", "mid")
    gen "Fine, fine..." ("base", xpos="far_left", ypos="head")

    jump hg_pf_grope_breasts_T4_continue

label hg_pf_grope_breasts_T4_clothed:
    call her_chibi_scene("grope_tits", trans=d7)
    call ctc

    #">Hermione stands in front of you expectantly..."
    #">You reach out for her ample breasts..."
    #">And start massaging them firmly..."

    "*squeeze-squeeze-squeeze*"

    her @ cheeks blush "................" ("base", "narrow", "base", "up", xpos="mid", ypos="base")

    menu:
        "\"Do you enjoy this, [name_hermione_genie]?\"":
            her @ cheeks blush "What...?" ("base", "base", "base", "R")
            her @ cheeks blush "Oh, I don't mind it..." ("base", "base", "base", "R")
            "*squeeze-squeeze-squeeze*"
            nar "You keep massaging her soft tits..."

            if states.her.tier <= 5:
                her @ cheeks blush "I mean, this isn't a big deal, as long as I am getting paid..." ("base", "narrow", "base", "up")
                if hermione.is_worn("top"):
                    nar "You keep on massaging her tits through her clothes..."
                her @ cheeks blush "A small price to pay for the honour of my house, really......{heart}" ("soft", "base", "base", "R")
            else:
                gen "Really? It seems to me as if you love it." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I wouldn't say that I love it..." ("base", "narrow", "base", "up")
                nar "You keep on massaging her tits through her uniform..."
                gen "What would you say then, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I just like it, {size=-4}a lot{heart}{/size}" ("base", "narrow", "base", "up")

            jump hg_pf_grope_breasts_T4_continue

        "-Pull on them abruptly with force-":
            nar "You give Hermione's tits a sudden but firm pull..."
            with vpunch
            her @ cheeks blush "Ouch..." ("angry", "happyCl", "worried", "mid",emote="sweat")
            nar "You pull on her tits again. This time much stronger."
            with vpunch
            her @ cheeks blush "Ouch! [name_genie_hermione], what are you trying to do...?" ("angry", "happyCl", "worried", "mid",emote="sweat")
            nar "You jerk the girl down by her tits with all your strength..."
            with vpunch
            with vpunch
            nar "Hermione almost loses balance..."
            her @ cheeks blush "*Panting* What are you doing, [name_genie_hermione]...?" ("open", "base", "base", "R")
            her @ cheeks blush "You don't need to be so rough with me....{heart}" ("base", "base", "base", "R")

            jump hg_pf_grope_breasts_T4_continue

label hg_pf_grope_breasts_T4_continue:
    call her_chibi_scene("grope_tits", trans=d7)
    call ctc

    her "*Ah*..." ("open", "narrow", "worried", "down")

    nar "You squeeze her tits a few more times, then give them a firm tug..."

    her "*Ah*... [name_genie_hermione]..." ("open", "base", "base", "mid")
    gen "What? You enjoy this, don't you?" ("base", xpos="far_left", ypos="head")
    her "No... I..." ("angry", "base", "base", "mid")
    gen "Don't you lie to your headmaster, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")

    nar "You squeeze her tits again..."

    her "*Ah*..." ("open", "narrow", "worried", "down")
    her "I am not lying, [name_genie_hermione]..." ("open", "narrow", "worried", "down")
    her "Why would I enjoy this?" ("open", "base", "base", "mid")
    gen "I don't know [name_hermione_genie]. You tell me." ("base", xpos="far_left", ypos="head")

    nar "You keep massaging her breasts..."

    her "*Ah*... I..." ("open", "base", "base", "mid")
    gen "Yes, what is it?" ("base", xpos="far_left", ypos="head")
    her "It's... It's nothing, [name_genie_hermione]..." ("angry", "base", "base", "mid")
    gen "Oh, I think it's something." ("base", xpos="far_left", ypos="head")
    gen "I think you like me squeezing your tits like this." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], please..." ("angry", "narrow", "base", "down")

    if game.daytime:
        her "Classes are about to start..." ("angry", "narrow", "base", "down")
    else:
        her "It's getting late..." ("angry", "narrow", "base", "down")

    her "Can I go now, [name_genie_hermione]? Please?" ("angry", "base", "base", "mid")

    gen "Sure, go ahead..." ("base", xpos="far_left", ypos="head")
    pause 2
    her "..............." ("angry", "narrow", "base", "down")
    pause.2

    her "[name_genie_hermione], you're... Still... Holding me." ("angry", "base", "base", "mid")
    gen "Oh, right... my bad." ("base", xpos="far_left", ypos="head")


    jump end_hg_pf_grope
