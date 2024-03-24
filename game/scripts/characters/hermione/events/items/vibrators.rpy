
default ev_her_vibrators_public_return = Event(id="her_vibrators_public_return", label="hg_vibrators_public_return", req="game.daytime==False")

label hg_vibrators:

    # Setup
    $ her_outfit_last.save()
    $ current_payout = 20

    gen "I've got a gift for you, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "A gift?" ("open", "base", "base", "mid",xpos="base",ypos="base")
    gen "Yep, just come closer, close your eyes and put your hand in this box!" ("base", xpos="far_left", ypos="head")
    call her_walk("desk", "base")
    nar "You present the Box-o-fun to Hermione."
    if not states.her.ev.vibrators.seen:
        her "\"Satisfaction guaranteed\"? What does that mean?" ("open", "squint", "base", "mid")
        gen "It means what it says on the box, now close your eyes and put your hand in there." ("base", xpos="far_left", ypos="head")
        her "Alright..." ("open", "closed", "base", "mid")
        play sound "sounds/rummage.ogg"
        nar "Hermione puts a hand in the box and takes out a set of egg-shaped vibrators."
        gen "Interesting... You've chosen well." ("base", xpos="far_left", ypos="head")
        her "Can I open my eyes now?" ("soft", "closed", "base", "mid")
        gen "Oh, yes go right ahead." ("base", xpos="far_left", ypos="head")
    else:
        if states.her.tier < 4: #Fail
            her "This again?" ("annoyed", "base", "base", "mid")
            her "It's not going to be something weird like the last time, is it?" ("annoyed", "happy", "worried", "mid")
            gen "Of course not... Just close your eyes and put your hand in the box." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "squint", "base", "mid")
            her "" ("annoyed", "closed", "base", "mid")
            play sound "sounds/rummage.ogg"
            nar "Hermione rummages around in the box and brings out the egg-shaped vibrators."
            gen "Alright, you can open--" ("base", xpos="far_left", ypos="head")
        else:
            her "Alright..." ("base", "base", "base", "mid")
            her "" ("base", "closed", "base", "mid")
            nar "Hermione rummages around in the box and brings out the egg-shaped vibrators."
            gen "Good choice... Okay, you may open your eyes." ("base", xpos="far_left", ypos="head")

    # Introduction (seen)
    label .intro_seen:

    if not states.her.ev.vibrators.seen:
        # First time (seen)
        $ states.her.ev.vibrators.seen = True

        nar "Hermione opens her eyes, and looks over the objects with suspicion."

        if states.her.tier < 4:
            jump hg_vibrators_fail

        elif states.her.tier < 5:
            her @ cheeks blush "Is that... A vibrator?" ("clench", "squint", "base", "mid")
            gen "Vibrator{b}s{/b}!" ("grin", xpos="far_left", ypos="head")
            gen "All three of these vibrate!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Surely you aren't expecting of me to put those things to use, are you?" ("open", "squint", "base", "mid")
            nar "You hold up the remote, circling your finger suggestively over the power switch."
            gen "What if I am?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I figured as much..." ("disgust", "narrow", "base", "R")
            gen "So, what will it be?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "{size=-4}...{w=0.4} I want twenty points for this.{/size}" ("disgust", "narrow", "base", "down") #small text
            gen "What was that?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I said, I want twenty points..." ("open", "closed", "annoyed", "mid")
            gen "Deal!" ("grin", xpos="far_left", ypos="head")
        else:
            her @ cheeks blush "A vibrator?" ("base", "squint", "base", "mid")
            gen "Indeed! Although, there's more than one!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "R--{w=0.2} really?" ("angry", "base", "base", "mid")
            gen "Aren't you going to thank me for my generosity, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you, [name_genie_hermione]." ("open", "base", "base", "mid")
            gen "Not with words, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            nar "You hold up the remote, circling your finger suggestively over the power switch."
            her @ cheeks blush "You want me to put them to use?" ("open", "squint", "base", "mid")
            gen "If you please." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Okay then..." ("base", "narrow", "base", "mid") #blushing

    else:
        # Repeat (seen)

        nar "Hermione opens her eyes and inspects the vibrators for a moment."

        if states.her.tier < 4:
            jump hg_vibrators_fail_repeat

        if states.her.tier < 5:
            her @ cheeks blush "The vibrators again..." ("normal", "happy", "base", "mid")
            gen "How lucky for you." ("base", xpos="far_left", ypos="head")
            if states.her.ev.vibrators.worn:
                gen "Ready to give them another whirl?" ("base", xpos="far_left", ypos="head")
            else:
                gen "Ready to give them a whirl?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*...{w=0.4} Sure, but only if you pay me twenty points!" ("open", "narrow", "base", "R")
            gen "Yeah, yeah, now get on with it." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "happy", "base", "mid")
        else:
            her @ cheeks blush "I see..." ("base", "squint", "base", "mid")
            gen "That's a lucky pull!" ("grin", xpos="far_left", ypos="head")
            gen "Looks like it might be a shiny, even!" ("grin", xpos="far_left", ypos="head")
            if states.her.ev.vibrators.worn:
                gen "Oh wait, that's just some remaining residue from the last time." ("grin", xpos="far_left", ypos="head")
                gen "Although, you could give them another try to see if the experience increases its rarity!" ("grin", xpos="far_left", ypos="head")
            else:
                gen "Oh wait, that's just some remaining residue from whoever used them previously." ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "Someone else has already used these?" ("open", "narrow", "base", "mid")
                gen "*Err*... Of course not!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "If you say so..." ("base", "narrow", "base", "R")

    # Introduction (worn)
    label .intro_worn:

    if not states.her.ev.vibrators.worn:
        # First time (worn)
        $ states.her.ev.vibrators.worn = True

        if states.her.tier < 5:
            her @ cheeks blush "So...{w=0.4} What am I supposed to do with these?" ("angry", "narrow", "base", "down")

            if hermione.is_any_worn("clothes"):
                gen "Just take your clothes off, and tape the vibrating eggs to your sensitive parts." ("base", xpos="far_left", ypos="head")

                if hermione.is_any_worn("bra", "panties"):
                    her @ cheeks blush "You want me to wear them without any clothes?!" ("clench", "wide", "base", "mid")
                    gen "You can wear them inside your underwear, whatever {i}boats your float{/i}..." ("base", xpos="far_left", ypos="head") # Intentional
                    her @ cheeks blush "It's not--{w=0.2} Okay then..." ("open", "narrow", "base", "mid")
                else:
                    her @ cheeks blush "But then you'll see when I--" ("disgust", "narrow", "base", "mid")
                    her @ cheeks blush "Could I at least wear some underwear?" ("open", "squint", "worried", "R")
                    gen "If you must..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Thank you [name_genie_hermione]..." ("base", "narrow", "base", "down")
            else:
                gen "Just tape them to your bits." ("base", xpos="far_left", ypos="head") # That's fanny
                her @ cheeks blush "Tape it to my bits?!" ("angry", "wide", "base", "mid")
                her @ cheeks blush "You want me to wear them while I'm naked?!" ("angry", "squint", "base", "mid")
                gen "You can put some underwear on top if it makes you feel better..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh...{w=0.4} Okay, I'll do that then." ("open", "squint", "base", "mid")
        else:
            her @ cheeks blush "*Ehm*...{w=0.4} What am I supposed to do with these?" ("open", "narrow", "base", "down")

            if hermione.is_any_worn("clothes"):
                gen "That's easy, just take your clothes off, and tape the vibrating eggs to your sensitive parts." ("grin", xpos="far_left", ypos="head")

                if hermione.is_any_worn("bra", "panties"):
                    her @ cheeks blush "Should I take off my underwear as well?" ("soft", "squint", "base", "mid")
                    gen "Yes please!" ("base", xpos="far_left", ypos="head")

            else:
                gen "Just stick those vibrating things against your breasts and pussy." ("grin", xpos="far_left", ypos="head")

            her @ cheeks blush "I see..." ("open", "squint", "base", "mid")

    else:
        # Repeat (worn)

        if states.her.tier < 5:
            if hermione.is_any_worn("clothes"):
                her @ cheeks blush "Can I put them inside my underwear like before?" ("open", "squint", "base", "mid")
                gen "Sure can." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Thank you, [name_genie_hermione]." ("open", "squint", "base", "mid")
            else:
                her @ cheeks blush "I'll need to wear some underwear over them, of course." ("open", "squint", "base", "R")
                gen "If you must..." ("base", xpos="far_left", ypos="head")
        else:
            if hermione.is_any_worn("clothes"):
                gen "And I want you to be naked..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Certainly, [name_genie_hermione]." ("base", "squint", "base", "mid")

        her @ cheeks blush "Here I go..." ("open", "closed", "base", "mid") #blush

    # Taking clothes off, if any.
    if hermione.is_any_worn("clothes"):

        if hermione.is_worn("robe"):
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("robe")
            with d3
            pause 1

        if hermione.is_worn("top"):
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("top")
            with d3
            pause 1

        if hermione.is_worn("bottom"):
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("bottom")
            with d3
            pause 1

        if hermione.is_any_worn("bra", "panties"): #Removes everything except bra or panties if she's wearing them (maybe this could be done differently)
            $ hermione.strip("clothes")
            $ hermione.wear("bra", "panties")
        else:
            $ hermione.strip("clothes")

    # Additional dialogue for lower levels (Optional)

    if states.her.tier >= 5:
        if hermione.is_worn("bra"):
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("bra")
            with d3
            pause 1

        if hermione.is_worn("panties"):
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("panties")
            with d3
            pause 1

        $ hermione.equip(her_outfit_vibrators_nude)
        with d3
        pause 1

        her @ cheeks blush "Okay... They're attached." ("open", "squint", "base", "mid")
        gen "Firmly?" ("base", xpos="far_left", ypos="head")
        gen "We wouldn't want anything to come loose now, would we?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I--{w=0.2} Yes, they're attached firmly..." ("angry", "squint", "base", "R")
    else:
        her @ cheeks blush "Don't look..." ("angry", "squint", "base", "mid")
        if hermione.is_any_worn("bra", "panties"):
            gen "I've already seen you naked..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I don't want you to see me putting them on!" ("angry", "squint", "worried", "mid")
            gen "Alright, whatever..." ("base", xpos="far_left", ypos="head")
        else:
            gen "Why not?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I need to tape them on..." ("angry", "squint", "worried", "mid")
            gen "So?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Just, don't look okay!" ("angry", "happyCl", "worried", "mid")
            gen "Fine..." ("base", xpos="far_left", ypos="head")

        show screen blkfade
        with d3
        pause .5

        menu:
            "-Peek-":

                if hermione.is_worn("bra"):
                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.strip("bra")
                    with d3
                    pause 1

                if hermione.is_worn("panties"):
                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.strip("panties")
                    with d3
                    pause 1

                her @ cheeks blush "" ("base", "narrow", "base", "down")


                $ hermione.equip([her_nipple_vibrators, her_panties_base_vibrators, her_clit_vibrators])
                hide screen blkfade
                with d5

                her @ cheeks blush "..." ("base", "narrow", "base", "down") #Looks down towards breasts annoyed
                her @ cheeks blush "..." ("base", "base", "base", "mid") #Looks up and sees you
                her @ cheeks blush "[name_genie_hermione]! I asked you not to look!" ("angry", "base", "worried", "mid")

                $ states.her.mood += 5

                gen "Don't blame me..." ("angry", xpos="far_left", ypos="head")
                gen "How long can it take to attach some vibrators?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I'm sorry, I'm not an expert with stuff like this... {w=0.2}Unlike you, obviously..." ("annoyed", "narrow", "base", "R")
                gen "Apology accepted." ("base", xpos="far_left", ypos="head") # Ignores her snarky comment
                her @ cheeks blush "..." ("disgust", "narrow", "base", "mid")

                play sound "sounds/cloth_sound3.ogg"
                $ hermione.equip(her_bra_base_vibrators)
                with d3
                pause 1

            "-Don't-":


                play sound "sounds/cloth_sound3.ogg"
                $ hermione.equip(her_outfit_vibrators)
                pause 2

                her "Okay, you can look, they're inside my underwear now..."
                hide screen blkfade
                with d5

                gen "Great." ("base", xpos="far_left", ypos="head")

    $ _temp_lockout = False

    label .choices:

    menu:
        "-Send her out-" if not _temp_lockout and game.daytime:
            jump hg_vibrators_public

        "-Send her out-" (style="disabled") if _temp_lockout and game.daytime:
            gen "She already said no..." ("base", xpos="far_left", ypos="head")

            jump .choices

        "-Send her out-" (style="disabled") if not game.daytime:
            her "But it's already past curfew..."
            gen "Oh, right..." ("base", xpos="far_left", ypos="head")
            nar "This option is only available during the day."

            jump .choices

        "-Finish early-" if _temp_lockout or not game.daytime:
            jump her_vibrators_nevermind

        "-Have her stay for a personal session-":
            jump hg_vibrators_personal

label her_vibrators_nevermind:
    gen "In that case, that shall do for now." ("base", xpos="far_left", ypos="head")
    her "Really?!" ("angry", "base", "base", "mid")

    if not game.daytime:
        gen "Yes, I've realized that my options are too limited at night." ("base", xpos="far_left", ypos="head")
        her "Options?" ("angry", "base", "base", "mid")
        gen "Yes, I know. It's a difficult concept, but I do in fact have options at times." ("base", xpos="far_left", ypos="head")
        her "..." ("annoyed", "base", "base", "mid")
        gen "You can leave the vibrators here, on my desk." ("base", xpos="far_left", ypos="head")
        gen "Off you go." ("base", xpos="far_left", ypos="head")
    else:
        gen "Yes, you can leave the vibrators with me, if you like." ("base", xpos="far_left", ypos="head")

    if states.her.tier >= 5: #wants to keep them
        her @ cheeks blush "Oh... *Ehm*..." ("soft", "base", "base", "mid")
        if not her_outfit_vibrators.unlocked:
            gen "I'm waiting..."
            her @ cheeks blush "..." ("soft", "base", "base", "mid")
            show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)
            with d5
        else:
            gen "Or you could keep them, of course." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you..." ("soft", "base", "base", "R")
    else:
        her @ cheeks blush "Oh, okay then..." ("soft", "base", "base", "mid")
        show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)
        with d5

    $ hermione.equip(her_outfit_last)
    $ hermione.hide()
    with fade
    pause 1

    if game.daytime:
        her @ cheeks blush "Good day to you, [name_genie_hermione]." ("open", "base", "base", "mid")
        gen "Until next time." ("base", xpos="far_left", ypos="head")
    else:
        her @ cheeks blush "Good night, [name_genie_hermione]." ("open", "base", "base", "mid")
        gen "Good night, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    hide vibrators_floor
    with d5
    jump end_hermione_event

label hg_vibrators_fail:
    her "What on earth is this?!" ("angry", "base", "base", "mid")
    gen "Oh. I guess you haven't seen one of these before." ("base", xpos="far_left", ypos="head")
    gen "Press the button, the one located on the side." ("base", xpos="far_left", ypos="head")
    nar "Hermione examines the device, locates the button and presses it."

    play sound "sounds/click4.ogg"
    play background "sounds/vibrator_low.ogg"

    if states.her.tier < 3:

        her "!!!" ("clench", "wide", "base", "stare") #Wide eyed

        play sound "sounds/drop_plastic.ogg"
        show vibrators_floor at Transform(xpos=436, ypos=413, zoom=0.5)
        with d5

        gen "There it is!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "This... This is a vibrator!" ("angry", "happy", "worried", "mid")
        gen "Vibrator{b}s{/b}, [name_hermione_genie], plural." ("grin", xpos="far_left", ypos="head")
        gen "Now, if you could just put them to use--" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "What!?!" ("angry", "wide", "base", "mid")
        her @ cheeks blush "You expect me to use them?!" ("open", "happy", "angry", "mid")
        gen "Of course!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("clench", "closed", "angry", "mid") #Wide eyed shocked
        gen "Don't you like my gift?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Do I like your gift...?" ("angry", "closed", "angry", "mid")
        her @ cheeks blush "What the hell is wrong with you?!" ("angry", "happy", "annoyed", "mid")

        call her_walk("door", "base")
        call her_walk(action="leave")
        play sound "sounds/door_down.ogg"
        with hpunch
        $ states.her.mood += 20

        gen "...{w=0.4} Did I get the wrong set?" ("base", xpos="far_left", ypos="head")

    else: # Tier 3
        her "What the--" ("angry", "base", "base", "mid")
        her @ cheeks blush "You...{w=0.4} You've bought me a vibrator?" ("angry", "happy", "worried", "mid")
        gen "Of course not...{w=0.4} I've bought an entire box filled with them!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione], this is hardly appropriate!" ("disgust", "happy", "worried", "mid")
        gen "How come?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Because...{w=0.4} Well..." ("annoyed", "happy", "worried", "R")
        gen "A healthy sex life is important to one's mental health. It helps to take the edge off of things." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "But... A headmaster shouldn't be--" ("mad", "happy", "worried", "mid")
        gen "Why not just put them on and give it a spin?" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("angry", "narrow", "worried", "down") #wide
        her @ cheeks blush "You mean right now?!" ("clench", "base", "worried", "mid")
        gen "Of course!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione]!" ("angry", "happy", "angry", "mid")
        gen "What?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I can't believe you would ask me to do such a thing!" ("angry", "narrow", "angry", "mid")
        her @ cheeks blush "I think I should go..." ("angry", "narrow", "base", "R")

        play sound "sounds/drop_plastic.ogg"
        show vibrators_floor at Transform(xpos=436, ypos=413, zoom=0.5)
        with d5

        #Hermione leaves
        call her_walk(action="leave")
        $ states.her.mood += 10

        gen "(Oh well. Was worth a shot...)" ("base", xpos="far_left", ypos="head")
        gen "(She'll come around eventually...)" ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand", 230, "base", flip=True)
    call gen_walk(path=[(230, 470), (440, 470), (450, 430)])
    call gen_chibi(flip=False)
    with d5

    pause 0.5

    play sound "sounds/click4.ogg"
    stop background

    pause 0.5

    hide vibrators_floor
    call gen_chibi("sit_behind_desk")
    with fade

    jump end_hermione_event

label hg_vibrators_fail_repeat:

    if states.her.tier < 3:
        her "[name_genie_hermione]!" ("open", "squint", "annoyed", "mid")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        her "I have already told you, I'm not going to use a vibrator in front of you!" ("angry", "squint", "angry", "mid")
        gen "Vibrator{b}s{/b}." ("base", xpos="far_left", ypos="head")
        her "..." ("disgust", "squint", "angry", "mid")

        play sound "sounds/drop_plastic.ogg"
        show vibrators_floor at Transform(xpos=436, ypos=413, zoom=0.5)
        with d5

        gen "And who said I wanted you to use it in front of me?" ("base", xpos="far_left", ypos="head")
        her "... Tell me with a straight face that you weren't going to ask me that." ("open", "narrow", "angry", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        her "I knew it!" ("open", "narrow", "angry", "R")
        her "I'm out of here!" ("open", "squint", "angry", "mid")

        call her_walk("door", "base")
        call her_walk(action="leave")
        play sound "sounds/door_down.ogg"
        with hpunch
        $ states.her.mood += 20

        gen "(How did she know?)" ("base", xpos="far_left", ypos="head")
    else:
        her "Didn't I already say--" ("open", "base", "angry", "mid")
        gen "Come on, just for a little bit, please?" ("base", xpos="far_left", ypos="head")
        her "Oh, just a little bit? That's fine then." ("grin", "squint", "base", "mid")
        gen "Really?" ("grin", xpos="far_left", ypos="head")
        her "{size=+6}No!{/size}" ("open", "base", "angry", "mid") with hpunch

        play sound "sounds/drop_plastic.ogg"
        show vibrators_floor at Transform(xpos=436, ypos=413, zoom=0.5)
        with d5

        gen "Oh..." ("base", xpos="far_left", ypos="head")
        her "...{w=0.4} I'm leaving." ("annoyed", "happy", "angry", "mid")

        call her_walk("door", "base")

        $ _temp = name_genie_hermione[:2] #Nickname without last 2 letters

        gen "[name_hermione_genie], you forgot the--" ("base", xpos="far_left", ypos="head")

        call her_chibi("stand","door","base", flip=False)
        pause .4

        her "{size=+2}I am not accepting vibrators as a gift from my [_temp]--...{w=0.4} I mean the headmaster!{/size}" ("open", "happy", "angry", "mid")
        gen "So, you're saying, if it somehow turns out I'm not your headmaster--" ("base", xpos="far_left", ypos="head")

        call her_walk("door", "base")
        call her_walk(action="leave")
        play sound "sounds/door_down.ogg"
        with hpunch
        $ states.her.mood += 10

        gen "(Well, that's just rude...)" ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand", 230, "base", flip=True)
    call gen_walk(path=[(230, 470), (440, 470), (450, 430)])
    call gen_chibi(flip=False)

    pause 0.5

    hide vibrators_floor
    call gen_chibi("sit_behind_desk")
    with fade

    jump end_hermione_event

label hg_vibrators_public:
    if not states.her.ev.vibrators.public_complete:
        # First time (public)
        # Flag 'states.her.ev.vibrators.public_complete' is set True in the return event

        gen "You can put on your school uniform now." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "My school uniform?" ("open", "base", "base", "mid")

        if states.her.public_tier >= 5:
            her @ cheeks blush "Don't tell me you're expecting of me to wear them in class?" ("angry", "base", "base", "mid")
            gen "No, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... Thank--" ("angry", "narrow", "base", "down")
            gen "I expect you to wear them outside class as well, for the entire day." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "The entire day?!" ("mad", "base", "base", "stare") #shocked but horny
            gen "That's right." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "But [name_genie_hermione], wearing them for the entire day is--" ("angry", "narrow", "base", "mid")
            gen "{i}Blathering Blatherskite{/i}! I didn't think about chafing!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I wasn't--{w=0.2} I mean, yes, there's no way I could wear them under my clothes for the entire day!" ("grin", "happy", "base", "mid")
            gen "It's settled then. You'll wear them {i}without{/i} clothes." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Wait, that's not--{w=0.2} I have to wear clothes!" ("angry", "happyCl", "base", "mid")
            gen "Didn't you just say, there was no way you could--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "On second thought, I'll be fine!" ("disgust", "squint", "base", "R")
            gen "If you say so... Just don't come back expecting me to kiss your sore nipples better." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I won't!" ("angry", "base", "base", "mid")
            gen "Yeah, don't even think about it...{w=0.4} I would really, really hate that if you did..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I..." ("disgust", "narrow", "base", "mid")
            gen "Like, really hate." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ehm*..." ("soft", "squint", "base", "R")
            gen "I'd be fuming." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("soft", "squint", "base", "mid")
            gen "Oh, one more thing." ("base", xpos="far_left", ypos="head")
            gen "You're not allowed to touch the controllers." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Wait, then how do I control them?" ("angry", "base", "base", "mid")
            gen "You don't. I'll control them myself using the remote, that way you can just focus on enjoying yourself." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You will? But then how am I supposed to know when they'll go off?" ("clench", "base", "base", "mid")
            gen "That's what makes it fun." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What if they go off when there are other students or teachers around?" ("angry", "squint", "base", "mid")
            gen "That's just a risk you'll have to take." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "narrow", "base", "R")
            gen "Come on... It's just some tiny little vibrations. I'm sure you can handle it." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Fine, I'll do it...{w=0.2} But only because you asked..." ("soft", "narrow", "worried", "R")

        elif states.her.public_tier == 4:
            her @ cheeks blush "You want me to wear them in class?!" ("angry", "base", "base", "mid")
            gen "No, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh good, for a moment I thought--" ("base", "squint", "worried", "R")
            gen "I want you to wear them during break time as well!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "" ("angry", "squint", "base", "stare")
            pause .5
            gen "Of course, they should be turned on at all times." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "But that's--{w=0.2} Couldn't I just...{w=0.4} I don't know..." ("upset", "squint", "worried", "mid")
            if states.her.tier < 5:
                gen "Quit complaining, [name_hermione_genie], you're about to earn{number=current_payout} points for your house." ("base", xpos="far_left", ypos="head")
                gen "Surely that's more than enough of an incentive to broaden your sexual education." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I am plenty sexually educated!" ("open", "closed", "annoyed", "mid")
                her @ cheeks blush "W-wait, that's not what I meant--" ("angry", "squint", "base", "stare")
                gen "*Heh*..." ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "I meant--{w=0.2} Well, the problem is--" ("normal", "squint", "base", "R")
                gen "Oh. So, you're considering it at least." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "{size=-4}Why am I even trying...{/size} *sigh*" ("disgust", "narrow", "base", "R")
            else:
                gen "Surely someone like you would have plenty of experience controlling yourself during sexual stimulation." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("disgust", "closed", "worried", "mid")
                gen "I see." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I just don't want people to notice, okay?" ("angry", "base", "base", "mid")
            gen "Then maybe you should consider keeping your legs closed for the time being." ("grin", xpos="far_left", ypos="head")
            gen "Unless you don't mind flashing yourself, that is." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm talking about the sounds!" ("open", "squint", "annoyed", "mid")
            gen "I see... Then let's make a compromise." ("base", xpos="far_left", ypos="head")
            gen "Only turn them on during a class that is noisy enough, that way, no one will be able to hear the buzzing." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "{size=-4}The buzzing is the least of my worries...{/size}" ("disgust", "narrow", "base", "R")
            gen "What was that?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Nothing, I was just thinking what class would work...{w=0.4} Definitely not {i}History of Magic{/i}." ("open", "squint", "worried", "R")
            gen "When in doubt, you could always choose Tonks' class, I'm sure she would appreciate--" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "narrow", "base", "mid") # slight shock
            gen "I mean, I'm sure it's loud enough--{w=0.2} I mean, the class is--" ("angry", xpos="far_left", ypos="head")
            gen "Fuck, I give up. You know what I mean anyway..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Sigh*... I'll figure it out. As long as I'm getting paid, of course." ("angry", "narrow", "base", "mid")
            gen "Sure! Wouldn't have it any other way." ("grin", xpos="far_left", ypos="head")
            gen "See you later then." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("open", "narrow", "base", "R")

        else:
            # Fail if public tier is not high enough.
            $ _temp_lockout = True

            if states.her.tier >= 5: #expecting private session
                her @ cheeks blush "You want me to--{w=0.3} But I thought..." ("soft", "squint", "base", "R")
                gen "*Hmm*?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Nevermind..." ("open", "squint", "worried", "R")
                gen "Off you go then." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Ehm*... Can't I just use them in my dorm instead?" ("soft", "squint", "base", "mid")
                gen "Where's the fun in that?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("annoyed", "squint", "base", "R") #Blush
                her @ cheeks blush "Well, I'm just not sure if wearing them in class is such a good idea..." ("open", "squint", "base", "R")
                gen "Nonsense, I'm sure the seats can handle a bit of wetness." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("annoyed", "squint", "worried", "R") #worried
                gen "Alright, fine, I can see you're hesitant..." ("base", xpos="far_left", ypos="head")
                gen "Let's do something else--" ("base", xpos="far_left", ypos="head")
            else:
                her @ cheeks blush "You want me to use them in class?!" ("angry", "wide", "base", "mid")
                her @ cheeks blush "But [name_genie_hermione]! That's..." ("clench", "squint", "base", "mid")
                gen "Surely you didn't think I just wanted you to wear them like a mere accessory, did you?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "No, but I didn't think you would want me to attend classes wearing them either!" ("clench", "squint", "base", "mid")
                gen "Alright, fair..." ("base", xpos="far_left", ypos="head")
                gen "In that case--" ("base", xpos="far_left", ypos="head")

            jump hg_vibrators.choices

    else:
        # Repeat (public)
        gen "I think you better put your clothes on and head to class." ("base", xpos="far_left", ypos="head")

        if states.her.public_tier >= 5:
            if states.her.ev.vibrators.public_stage <= 1:
                # Tried LOW level before

                her @ cheeks blush "You want me to use them in class again?" ("soft", "squint", "base", "mid")
                gen "Oh no... This time I want you to wear them the entire day." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "The entire day?!" ("angry", "wide", "base", "stare")
                gen "Yep, and you're not allowed to touch the controllers..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "But, [name_genie_hermione]!" ("clench", "base", "worried", "mid")
                her @ cheeks blush "Wearing them through one class is one thing...{w=0.4} But wearing them for the entire day is just..." ("angry", "base", "worried", "mid")
                gen "They won't remain turned on the entire day...{w=0.4} I'm not that cruel." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I thought when you said I can't touch the controls, you--" ("disgust", "squint", "base", "mid")
                gen "What I'm saying is... I'll be controlling them remotely, from here." ("base", xpos="far_left", ypos="head")
                gen "Like this." ("base", xpos="far_left", ypos="head")

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_low.ogg"

                her @ cheeks blush "{heart}*Ah*...{heart}" ("angry", "narrow", "base", "up")

                play sound "sounds/click4.ogg"
                stop background

                her @ cheeks blush "..." ("angry", "narrow", "base", "mid")
                gen "Heh-heh..." ("base", xpos="far_left", ypos="head")
                gen "So, are you ready to learn something new today?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("disgust", "narrow", "base", "down")
                gen "Why the hesitance [name_hermione_genie], you have already worn them once, so you know what to expect." ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "The problem isn't {i}the what{/i}, but {i}when{/i}..." ("angry", "narrow", "base", "R")
                her @ cheeks blush "Who knows what might happen if they go off at the wrong time." ("angry", "narrow", "base", "mid")
                her @ cheeks blush "What if they go off while I'm presenting something in front of the entire class?" ("angry", "closed", "worried", "mid")
                gen "You're talking as if anyone would pay any attention to the curriculum." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("disgust", "narrow", "base", "mid")
                gen "And even in the unlikely event that someone does pay attention, just tell them it's your phone vibrating." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "... Very funny, [name_genie_hermione]." ("disgust", "narrow", "base", "mid")
                gen "(Did I say something funny?)" ("base", xpos="far_left", ypos="head") # Genie isn't aware muggle devices do not work at hogwarts.
                her @ cheeks blush "I guess I could make something up..." ("open", "narrow", "base", "R")
                her @ cheeks blush "Okay...{w=0.4} I'll do it." ("open", "closed", "worried", "mid")
                gen "Excellent!" ("grin", xpos="far_left", ypos="head")
            else:
                # Tried HIGH level before

                her @ cheeks blush "Certainly, [name_genie_hermione]." ("open", "squint", "base", "R")
                gen "Although..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Yes?" ("angry", "base", "base", "mid")
                gen "I've decided to go easy on you this time, so you will know the exact timing when vibrators go off--" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Really? Thank you [name_genie_hermione]!" ("grin", "base", "base", "mid")
                gen "Under one condition..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "...{w=0.4} what is the condition?" ("disgust", "squint", "base", "mid")
                gen "You have to accompany your friends to {i}gobbling stones{/i} again." ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "The what?!" ("angry", "base", "base", "mid")
                gen "{i}Gobbling stones{/i}. It's a game where you grab the stone and put it in your--" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Do you mean {i}Gobstones{/i}?" ("disgust", "squint", "base", "mid")
                gen "That's what I said." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "No, you said--" ("angry", "narrow", "base", "mid")
                her @ cheeks blush "You know what, forget it." ("angry", "narrow", "base", "R")
                gen "Said and done!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("annoyed", "narrow", "base", "mid")
                gen "If my condition isn't satisfactory, I could just turn the vibrators on during lunch break..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "But, that's when all the students gather--" ("angry", "base", "base", "stare")
                her @ cheeks blush "I see what you're doing..." ("annoyed", "narrow", "base", "mid")
                her @ cheeks blush "Alright, fine, {i}Gobstones{/i} it is." ("open", "narrow", "base", "R")
                gen "I knew you were the reasonable one." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Unless..." ("soft", "narrow", "base", "mid") #enticing
                gen "Yes?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "There is some time left before classes start, in case you wanted to check everything is in working order, [name_genie_hermione]?" ("soft", "squint", "base", "mid") # Enticing look
                gen "Clever, but don't think you can get off the hook that easy, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Hmph*..." ("annoyed", "narrow", "base", "R") #annoyed but blushing
                her @ cheeks blush "See you tonight then." ("open", "squint", "base", "R")
                gen "Enjoy!" ("base", xpos="far_left", ypos="head")
        else:
            her @ cheeks blush "You want me to wear them in class again?" ("soft", "squint", "base", "mid") #blush
            gen "Most definitely." ("base", xpos="far_left", ypos="head")
            if states.her.tier < 5:
                her @ cheeks blush "You'll pay me the same as last time, I presume?" ("open", "squint", "base", "R")
                gen "Of course."
            her @ cheeks blush "*Hmm*... Okay then..." ("open", "squint", "base", "R")
            gen "Excellent! I look forward to hearing from you later this evening." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("open", "squint", "base", "R")

    if states.her.tier >= 5:
        # (she is naked on high tiers at this point)
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.equip(her_outfit_vibrators)
        with d3
        pause .5
    else:
        gen "Go on then." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("soft", "narrow", "base", "down") #down

    play sound "sounds/cloth_sound3.ogg"
    $ hermione.equip(her_outfit_default)
    $ hermione.equip(her_bottom_school2)
    $ hermione.equip(her_outfit_vibrators, remove_old=False)
    with d3
    pause .5

    her @ cheeks blush "..." ("soft", "narrow", "base", "R") #looks right, blushing

    call her_walk(action="leave")

    $ ev_her_vibrators_public_return.enqueue()

    jump end_hermione_event

label hg_vibrators_personal:

    $ _temp_premature_finish = False

    gen "Let's turn these things on then, shall we." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Hold on I'm not--" ("mad", "base", "base", "stare")

    play sound "sounds/click4.ogg"
    play background "sounds/vibrator_medium.ogg"


    if states.her.tier >= 5:
        # Note: This scene has CG with Hermione lying on the desk with vibrators, 3 poses, closed legs, spread legs, pushed pelvis in the air (cumming).

        label .high_tier:

        her @ cheeks blush "{heart}*Ah*!!!{heart}" ("grin", "wide", "worried", "stare")
        gen "There it goes." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Did--{w=0.2} *Ah*...{w=0.4} Did you really need to do it so suddenly?" ("angry", "happyCl", "base", "mid")
        gen "Of course, the universe depended on it... It was always destined to happen." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} I can't--{w=0.2} *Ah*...{w=0.4} I think Professor Trelawney would've told me if that was the case--" ("annoyed", "happyCl", "base", "mid")
        her @ cheeks blush "*Ah-Ah*! {w=0.5}Why is this thing so intense?" ("clench", "narrow", "worried", "down")
        gen "Intense? That's just the medium setting." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Medium?! *Ngh*...{w=0.4} No wonder it's--" ("angry", "narrow", "base", "stare")

        menu:
            "-Lower the intensity-":

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_low.ogg"

                her @ cheeks blush "*Ah*...{w=0.4} That's better... Just a little more--" ("base", "closed", "worried", "mid")
                gen "Now-now, let's not get hasty." ("base", xpos="far_left", ypos="head")

            "-Raise the intensity-":

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_high.ogg"

                her @ cheeks blush "{cps=16}*Ahhhhhhhhh*{/cps} [name_genie_hermione]!!" ("disgust", "narrow", "base", "up")
                gen "Oops, my bad! My hand slipped..." ("base", xpos="far_left", ypos="head")

        gen "(Wouldn't want to end it too soon...)" ("base", xpos="far_left", ypos="head")

        play sound "sounds/click4.ogg"
        stop background

        gen "Now, why don't you do me a favour, and lie down on the desk for me?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "You...{w=0.4} You want me to do what?!" ("angry", "wide", "base", "mid")
        gen "Get your butt...{w=0.4} On the desk!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah* W-Why?" ("angry", "squint", "worried", "mid")
        gen "You already know why..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "narrow", "worried", "down")
        gen "I want to see it up close. Can you do that for me, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I...{w=0.3} I suppose..." ("soft", "narrow", "base", "down")
        gen "Go on then, plant those cheeks on the wood." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "If that's what you want... I guess it's fine..." ("normal", "narrow", "base", "down")
        gen "Queue the fade!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "The what--" ("angry", "base", "base", "mid")

        stop music fadeout 1

        #Hermione legs closed
        if game.daytime:
            show her_vibrators_personal hermione1 noshake eyebrows_upset eyes_squint_right mouth_annoyed zorder 15 as cg with fade
        else:
            show her_vibrators_personal hermione1 noshake eyebrows_upset eyes_squint_right mouth_annoyed zorder 15 as cg at color_temperature(1.0) with fade
        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

        gen "I love a good transition to get straight to the point." ("base", xpos="far_left", ypos="head")
        gen "Now, where were we..." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_neutral mouth_open as cg with d5

        her "I'm on the desk...{w=0.4} Just as you asked." # Looks away, pouty face
        gen "Right... Now, let's do a bit of a {i}show and tell{/i}." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_upset eyes_squint_forward mouth_horny as cg with d5

        her "What do you mean?"
        gen "Spread those shapely legs for me, will you?" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_neutral eyes_narrow_right mouth_annoyed as cg with d5

        her "..."

        # Hermione legs open
        show her_vibrators_personal hermione2 eyebrows_worried eyes_squint_right blush_heavy as cg with d5

        gen "There we go.{w=0.8}{nw}" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyes_squint_forward as cg

        gen "There we go.{fast} Now for the telling part." ("base", xpos="far_left", ypos="head")

        play sound "sounds/click4.ogg"
        play background "sounds/vibrator_low.ogg"

        #Hermione legs closed
        show her_vibrators_personal hermione1 eyebrows_upset eyes_wide_crossed mouth_open -noshake as cg with d5

        her "*Ah*!"

        show her_vibrators_personal eyebrows_worried eyes_open_right as cg with d5

        gen "There it is! Now you're doing it." ("base", xpos="far_left", ypos="head")
        gen "Although, the {i}show{/i} part is quite lacking now." ("base", xpos="far_left", ypos="head")
        gen "You're not going to get a good grade unless you do both, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyes_squint_forward mouth_shocked as cg with d5

        her "I--{w=0.2} *Ah*...{w=0.4} I'm being graded for this?"

        gen "Of course... You should know that you get graded for every school activity by now, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_upset eyes_squint_right mouth_horny as cg with d5

        her "I--{w=0.2} *Ah*...{w=0.4} Of course, I know that."

        show her_vibrators_personal eyes_narrow_right mouth_worried as cg with d5

        her "But do I really need to--{w=0.2} *Ehm*...{w=0.4} Well, it's just that it's a bit..."
        gen "A bit what?" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal mouth_annoyed as cg with d5

        her "Degrading..."
        gen "Don't tell me you don't want a good grade?" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_neutral eyes_open_right as cg with d5

        her "I...{w=0.4} Of course I--"

        gen "Then spread those legs already, lest you want the {b}D{/b}... {w=0.2}grading." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_worried eyes_open_forward as cg with d5

        her "Don't you mean--{w=0.2} *Ah*...{w=0.4} {i}Troll{/i}?"
        gen "A Troll? What the--" ("angry", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_upset eyes_narrow_forward mouth_open as cg with d5

        her "It is the grading system used in Hogwarts, I'm sure you--"
        gen "Enough with the dilly-dallying... Close your mouth, and open those legs." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_worried eyes_open_right mouth_annoyed as cg with d5

        her ""
        gen "(First she talks about trolls, then some hogwash... And they call {i}me{/i} the eccentric one.)" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_worried eyes_closed mouth_horny as cg with d5

        her "(You can do this, Hermione...)"

        #Hermione legs open
        show her_vibrators_personal hermione2 mouth_angry effects_wetness_minor as cg with d5

        her "..."
        gen "(She's wet!)" ("angry", xpos="far_left", ypos="head")
        gen "*Ahem*... Very good, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "Now keep them spread like that, and you'll earn yourself a good grade." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_worried eyes_squint_forward mouth_open as cg with d5

        her "Just... Please tell me before you use the remote, okay?"
        gen "Lecturing your headmaster on how to do their job... *Tut-tut*. That will cost you a point..." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal hermione1 eyebrows_upset mouth_shocked as cg with d5

        her "Don't be ridiculous... It's not even a real grade..."
        gen "Yet you still seem to care dearly about it, don't you [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

        #Hermione legs closed
        show her_vibrators_personal hermione1 eyes_squint_right mouth_annoyed as cg with d5

        her "*Hmph*..."

        #Hermione legs open
        show her_vibrators_personal hermione2 mouth_shocked as cg with d5

        her "Just do whatever you want, why don't you."
        gen "That's the plan." ("base", xpos="far_left", ypos="head")

        menu:
            "-Turn the intensity to High-":

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_high.ogg"

                #Hermione legs open
                show her_vibrators_personal hermione2 eyebrows_worried eyes_clenched mouth_shocked blush_heavy as cg with d5

                #her "[name_genie_hermione]!!!{w=0.4}{nw}"

                #Hermione legs closed
                show her_vibrators_personal hermione1 mouth_worried blush_heavy as cg with d5

                #her "[name_genie_hermione]!!!{fast}"

                her "[name_genie_hermione]!!! Turn it down!"

                menu:
                    "-Keep it going-":
                        gen "Legs open, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal hermione1 mouth_open as cg with d5

                        her "*Ah*...{w=0.2} *Ah*...{w=0.2} But--"
                        gen "[name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                        #Hermione legs open
                        show her_vibrators_personal hermione2 as cg with d5

                        gen "Didn't I just warn you about trying to lecture your headmaster?" ("base", xpos="far_left", ypos="head")
                        gen "Besides, you said I can do whatever I want." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal mouth_worried as cg with d5

                        her "Yes, but--{w=0.2} *Ah*...{w=0.4} I just--{w=0.2} *Ah*..."
                        gen "Just what? Out with it already..." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal mouth_angry as cg with d5

                        her "*Ah*...{w=0.2} Please, [name_genie_hermione]! It's too strong...!"
                        gen "Alright, I can turn it down, but who's to say you won't change your mind again?" ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_worried mouth_worried as cg with d5

                        her "*Ah*...{w=0.2} *Ah*...{w=0.2} I'm gonna--"
                        gen "Change your mind?" ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_squint_crossed mouth_angry as cg with d5

                        her "I'm gonna--"

                    "-Turn it down-":
                        gen "Oh? Don't want it to end too soon?" ("base", xpos="far_left", ypos="head")

                        play sound "sounds/click4.ogg"
                        play background "sounds/vibrator_low.ogg"

                        #legs are closed
                        show her_vibrators_personal eyebrows_neutral eyes_closed as cg with d5

                        her "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..."
                        gen "I didn't think you were into edging, it's a quality not every woman knows how to appreciate. I'm glad you do, though." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_wide_forward mouth_angry as cg with d5

                        her"{size=+4}W--{w=0.2}What?!{/size}"

                        show her_vibrators_personal eyebrows_neutral eyes_open_forward as cg with d5

                        her "That is not--"
                        gen "Don't worry! I'm the person holding the controller, after all." ("base", xpos="far_left", ypos="head")
                        gen "If it were anyone else, they might've gotten impatient by now..." ("base", xpos="far_left", ypos="head")
                        gen "But I can do this all day!" ("grin", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_upset eyes_squint_right mouth_open as cg with d5

                        her "[name_genie_hermione], I am not--..."

                        show her_vibrators_personal eyes_squint_forward as cg with d5

                        gen "You're lucky I'm in a good mood,{w=0.2} so I think I'll oblige you,{w=0.2}{nw}" ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal mouth_annoyed as cg

                        gen "You're lucky I'm in a good mood, so I think I'll oblige you,{fast} for being so honest with yourself for once." ("base", xpos="far_left", ypos="head")
                        gen "(She'll love this...)" ("grin", xpos="far_left", ypos="head")
                        gen "[name_hermione_genie],{w=0.2} from now on, you are not allowed to cum!{nw}" ("grin", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_open_forward mouth_worried as cg

                        gen "[name_hermione_genie], from now on, you are not allowed to cum!{fast}" ("grin", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_squint_forward as cg with d5

                        gen "Unless I say so." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_worried eyes_squint_right mouth_shocked as cg with d5

                        her "B--{w=0.2} But--"
                        gen "No butts. {w=0.3}You're now under my command, I say that you shall not cum until I deem it fitting." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_squint_forward mouth_open as cg with d5

                        her "But, [name_genie_hermione]!"
                        gen "(Now she's getting into it...)" ("grin", xpos="far_left", ypos="head")
                        gen "As your headmaster, I have the power over your grades, and shall you fail to meet my expectations... Well--" ("base", xpos="far_left", ypos="head")
                        gen "--Naturally you'll have to be punished!" ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_neutral eyes_wide_forward as cg with d5

                        her "P--{w=0.2} Punished?!"
                        gen "Yes, punished!" ("grin", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_neutral eyes_narrow_forward mouth_angry as cg with d5

                        her "!!!"

                        show her_vibrators_personal eyes_narrow_right as cg with d5

                        gen "(I knew she'd like that one...)" ("grin", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_worried eyes_narrow_forward as cg with d5

                        gen "Now spread your legs!" ("grin", xpos="far_left", ypos="head")


                        show her_vibrators_personal eyes_closed as cg with d5
                        pause 1.5

                        #Hermione legs open
                        show her_vibrators_personal hermione2 eyebrows_worried eyes_squint_forward mouth_annoyed as cg with d5
                        call ctc

                        gen "Prepare yourself, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
                        gen "I could change the intensity at any moment!" ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_wide_forward mouth_open as cg with d5

                        her "You--"
                        gen "Although... I think I'll just leave it like this for a while..." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_closed mouth_horny as cg with d5

                        her "{size=-4}Thank be Merlin... I thought you were being serious for a--{/size}"
                        gen "Just kidding!" ("base", xpos="far_left", ypos="head")

                        play sound "sounds/click4.ogg"
                        play background "sounds/vibrator_high.ogg"

                        show her_vibrators_personal eyes_squint_crossed mouth_angry as cg with d5

                        her "*Ah*!" with hpunch
                        gen "*Heh-Heh*..." ("grin", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_closed as cg with d5

                        her "[name_genie_hermione], please...{w=0.4}{nw}"

                        show her_vibrators_personal mouth_worried as cg

                        her "[name_genie_hermione], please...{fast} If you keep it like this...{w=0.4} I'll...{w=0.4}{nw}"

                        show her_vibrators_personal mouth_shocked as cg

                        her "[name_genie_hermione], please... If you keep it like this... I'll...{fast} I'll--"
                menu:
                    "-Keep it going-":

                        $ _temp_premature_finish = True

                        #Hermione cums once, and then it skips to the end section of the event.
                        show her_vibrators_personal eyes_narrow_crossed as cg

                        her "{size=+5}{heart}{heart}{heart}Cum!!!{heart}{heart}{/size}"
                        gen "Wait, I didn't say you could--" ("angry", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_worried eyes_clenched mouth_open effects_wetness as cg with d5

                        her "*Nnnnngh*--{w=0.8}{nw}" with kissiris

                        #Hermione pelvis up

                        show her_vibrators_personal hermione3 eyebrows_worried eyes_clenched mouth_open effects_wetness as cg with d5

                        pause .4

                        with kissiris
                        with hpunch
                        play sound "sounds/slick_01.ogg"

                        show her_vibrators_personal eyes_ahegao mouth_ahegao effects_squirt as cg with d5

                        her "{heart}Aaaaah!!{heart}{w=0.8}{nw}"

                        show her_vibrators_personal -effects_squirt effects_puddle as cg with d5

                        her "{heart}Aaaaah!!{heart}{fast}"

                        gen "By the great desert--" ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_closed mouth_open as cg with d5

                        #If we could, then her hips could shudder here
                        her "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..."

                        jump .end

                    "-Turn it down-":

                        play sound "sounds/click4.ogg"
                        play background "sounds/vibrator_low.ogg"

                        show her_vibrators_personal eyebrows_upset eyes_squint_forward mouth_angry as cg with d5

                        her "What the--"

                        show her_vibrators_personal mouth_open as cg with d5

                        her "Why did you turn it down!?"
                        gen "............" ("base", xpos="far_left", ypos="head")
                        gen "If you're going to be acting like this, then we'll have to do it my way." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_worried eyes_narrow_forward as cg with d5

                        her "Your--{w=0.2} Your way?"
                        gen "I've been way too lenient with you, first you disobey me... and even when I so graciously granted your wish--" ("angry", xpos="far_left", ypos="head")
                        gen "--Something that I don't even do any more, by the way--" ("base", xpos="far_left", ypos="head")
                        gen "--but you still aren't satisfied!" ("angry", xpos="far_left", ypos="head")
                        gen "So, yes, we're going to do this {b}my{/b} way..." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_open_forward as cg with d5

                        her "[name_genie_hermione]?"
                        gen "You're doing this as a favour to {i}me{/i}, you had best not forget that, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_squint_right mouth_annoyed as cg with d5

                        her "..."
                        gen "This is currently a fairly one-sided experience, therefore in order for it to work for me, I'd like it to not end prematurely..." ("base", xpos="far_left", ypos="head")
                        gen "So you better not cum until I say so." ("base", xpos="far_left", ypos="head")
                        gen "Is that clear?" ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal mouth_horny as cg with d5

                        her "Yes, [name_genie_hermione]..."
                        gen "Good." ("base", xpos="far_left", ypos="head")
                        gen "Expect the unexpected, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_squint_forward as cg with d5

                        her "Expect the...{w=0.4} Unexpected?"
                        gen "That's right...{w=0.4} I could change the intensity at a moment's notice..." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyes_narrow_forward mouth_worried as cg with d5

                        gen "It could remain as is... At a level where you'd be stuck in a state of constant arousal... Enough to keep you on edge, but not enough to bring you over it." ("base", xpos="far_left", ypos="head")

                        play sound "sounds/click4.ogg"
                        play background "sounds/vibrator_medium.ogg"

                        show her_vibrators_personal eyebrows_neutral eyes_narrow_crossed mouth_shocked as cg with d5

                        her "*Ah*!{w=0.6}{nw}"

                        show her_vibrators_personal eyes_squint_forward mouth_open as cg

                        her "*Ah*!{fast}"
                        gen "I could also increase the intensity... Even if for just a moment, to see your face light up in excitement, fighting the urge to let go." ("base", xpos="far_left", ypos="head")

                        show her_vibrators_personal eyebrows_upset eyes_clenched effects_wetness as cg with d5

                        her "[name_genie_hermione]! I'll--"

            "-Turn the intensity to Medium-":

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_medium.ogg"

                # Hermione legs closed
                show her_vibrators_personal hermione1 eyebrows_neutral eyes_closed mouth_shocked as cg with d5

                her "*Ahhhh*!{w=0.8}{nw}" with hpunch

                show her_vibrators_personal eyes_squint_forward mouth_angry as cg

                her "*Ahhhh*!{fast}"

                gen "Something the matter?" ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyes_narrow_right as cg with d5

                her "No! I'm f--{w=0.2} fine!"

                # Hermione legs open
                show her_vibrators_personal hermione2 eyes_squint_right mouth_open as cg with d5

                her "Just--{w=0.2} *Ah*...{w=0.4} Just do w-whatever you want..."
                gen "In that case, I think I'll leave it like this for a bit." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal mouth_horny as cg with d5

                her "O--{w=0.2} Of course..."#annoyed

                show her_vibrators_personal mouth_annoyed as cg with d5
                pause 1

                show her_vibrators_personal eyebrows_worried eyes_closed mouth_annoyed as cg with d5
                pause 1

                show her_vibrators_personal mouth_open as cg with d5

                her "*Ah*..." #Horny

                show her_vibrators_personal eyes_squint_right as cg with d5
                call ctc

                gen "Getting there already, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal mouth_horny as cg with d5

                her "N--{w=0.2}No, of course not!"
                gen "That's good. {w=0.5}Because I don't want you to cum just yet..." ("base", xpos="far_left", ypos="head")
                gen "Not until I say so." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyes_narrow_right mouth_open as cg with d5

                her "That's--{w=0.2} *Ah*...{w=0.4} That's fine by me..."

                show her_vibrators_personal eyes_open_right mouth_worried as cg with d5
                pause .8

                show her_vibrators_personal eyes_closed as cg with d5
                pause .8

                show her_vibrators_personal eyebrows_upset eyes_clenched mouth_angry as cg with d5
                pause .5

                show her_vibrators_personal eyebrows_neutral eyes_closed mouth_horny effects_wetness as cg with d5
                pause .8

                gen "Are you sure? Looks to me as if you're about to cum, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                gen "Or am I mistaken?" ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyebrows_upset mouth_open as cg with d5

                her "That's not--{w=0.2} *ah*...{w=0.4} True..."
                gen "Quit lying, you cannot fool me." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal mouth_horny as cg with d5

                her "*Ah*...{w=0.4} How do you--"
                gen "How do I know?" ("base", xpos="far_left", ypos="head")
                gen "Experience, [name_hermione_genie], experience...{w=0.4} You won't ever find anyone with as much experience as I have..." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyebrows_neutral eyes_clenched as cg with d5

                her "I--{w=0.4} I'm--"

        play sound "sounds/click4.ogg"
        play background "sounds/vibrator_low.ogg"

        show her_vibrators_personal eyebrows_worried eyes_closed mouth_horny as cg with d5

        her "*Mmm*..."
        gen "I've done this enough times to know exactly when someone's about to go over the edge, just so that I can ease up and keep it going for a while longer..." ("base", xpos="far_left", ypos="head")
        gen "And that is the goal for today's lesson..." ("base", xpos="far_left", ypos="head")
        gen "Hold{w=0.3} it{w=0.3} in..." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal mouth_worried as cg with d5

        her "*Ah*...{w=0.4}{nw}"

        show her_vibrators_personal mouth_horny as cg

        her "*Ah*...{fast} *Ah*...{w=0.4}{nw}"

        show her_vibrators_personal mouth_worried as cg

        her "*Ah*... *Ah*...{fast} *Ah..."
        gen "You think you could do that for me?" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal mouth_open as cg with d5

        her "*Ah*...{w=0.4} [name_genie_hermione], I don't know if--"

        play sound "sounds/click4.ogg"
        play background "sounds/vibrator_high.ogg"

        show her_vibrators_personal hermione1 eyebrows_worried mouth_angry as cg with d5

        her "{size=+4}{heart}{heart}{heart}*Ah*!!!{heart}{heart}{/size}"

        play sound "sounds/click4.ogg"
        play background "sounds/vibrator_low.ogg"

        # Hermione legs open
        show her_vibrators_personal hermione2 eyebrows_worried eyes_closed mouth_open as cg with d5

        her "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..."

        show her_vibrators_personal eyes_squint_forward mouth_shocked as cg

        her "[name_genie_hermione]...{w=0.4}{nw}"

        show her_vibrators_personal mouth_worried as cg

        her "[name_genie_hermione]...{fast} Please..."

        gen "Nuh-uh... Not yet, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Patience is a virtue...{w=0.4} It's time you learn that." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyes_closed mouth_angry as cg with d5

        her "But--"
        gen "Remember why you're here, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Our session won't end until I'm satisfied with the results." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_neutral as cg with d5

        her "*Ah*...{w=0.4} *Ah*...{w=0.4} And how...{w=0.4} How do I make sure that you're--{w=0.2} *Ah*...{w=0.4} Satisfied..."
        gen "By doing what I ask of you..." ("base", xpos="far_left", ypos="head")
        gen "Although, I must say..." ("base", xpos="far_left", ypos="head")
        gen "Watching you squirm about, and trying to hold it in, is quite satisfying by itself..." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_worried as cg with d5

        her "You're--{w=0.2} *Ah*...{w=0.4} You find it satisfying, watching me--{w=0.2} *Ah*..."
        gen "I have full control of your fate, of course I'm enjoying it..." ("base", xpos="far_left", ypos="head")
        gen "I haven't had this much power at my fingertips for a long time..." ("base", xpos="far_left", ypos="head")
        her "..."
        gen "How does that make you feel, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal mouth_open as cg with d5

        her "I--{w=0.2} *Ah*...{w=0.4} If deciding my--{w=0.2}Ah*...{w=0.4} My fate would satisfy you..."
        gen "You really are willing to grant me this much control over you?" ("base", xpos="far_left", ypos="head")
        gen "This kind of...{w=0.2} power...{w=0.2} was already taken away from me before, do you think it's wise to allow me to have another taste?" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal mouth_angry as cg with d5

        her "I..."

        show her_vibrators_personal eyebrows_upset as cg with d5

        her "I already said you can--{w=0.2} *Ngh*...{w=0.4} Do whatever you want...{w=0.4} I am not the kind of person to break my word."
        gen "You say that, but the frustration on your face says otherwise..." ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyebrows_worried as cg with d5

        her "N--{w=0.4}No, it's fine... Really!"
        gen "Is it?" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal eyes_clenched as cg with d5

        her "Y--{w=0.2}Yes..."

        menu:
            "-Turn it off-":
                # Ends the event with Hermione not cumming. Mood down slightly

                gen "Okay then, in that case..." ("base", xpos="far_left", ypos="head")

                gen "You shall not cum.{w=0.4}{nw}" ("base", xpos="far_left", ypos="head")

                play sound "sounds/click4.ogg"
                stop background

                gen "You shall not cum.{fast}{w=0.4}{nw}" ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal noshake eyebrows_neutral eyes_wide_forward mouth_shocked as cg with d5

                her "W--{w=0.2} What?!"

                show her_vibrators_personal eyes_squint_right mouth_angry as cg with d5

                her "(He turned it off! How could he!)"

                show her_vibrators_personal eyes_narrow_forward as cg with d5

                her "W--{w=0.2} Why did you--"
                gen "I used my power over you, to do the--" ("base", xpos="far_left", ypos="head")
                gen "--unexpected..." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal mouth_annoyed as cg with d5

                gen "(Why do I always do this when people challenge me... Am I power tripping?)" ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyes_narrow_right as cg with d5

                her "But, I was...{w=0.4} I was about to--"
                gen "You said you wanted to satisfy me, and this is exactly what I needed to feel satisfied." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyebrows_worried eyes_squint_right mouth_horny as cg with d5

                her "But I thought...{w=0.4} Well, I didn't think this would happen..."
                gen "Always expect the unexpected in life, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyes_squint_forward as cg with d5

                her "But--"

                gen "Yes, that's right... This was all a highly elaborate life lesson all along." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyebrows_neutral mouth_annoyed as cg with d5

                her "It was...?"
                gen "Of course, and you did very well, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyes_narrow_forward as cg with d5

                her "..."

                show her_vibrators_personal eyes_squint_right as cg with d5

                her "A-Alright then, whatever you say [name_genie_hermione]..."

                stop music fadeout 1
                show screen blkfade
                with d5

                hide cg
                show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)

                $ hermione.equip(her_outfit_last)
                nar "You watch as Hermione sits up and shimmies to the edge of your desk, planting her feet on the floor, she sways on the spot slightly before she readies herself, and makes her way to the front of your desk."

                hide screen blkfade
                with d5

                her @ cheeks blush "So...{w=0.4} Will that be all?" ("open", "squint", "base", "mid")

                menu:
                    "-Grade her performance-":
                        gen "Not quite, there's one more thing..." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Yes?" ("open", "base", "base", "mid") #Hopeful
                        gen "Your grade!" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "My--" ("soft", "base", "base", "mid") #confused
                        gen "I did mention I was going to grade your performance." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Oh, right..." ("disgust", "narrow", "base", "down") #look full of hope

                        menu:
                            "-Give her a passing grade-":
                                gen "You pass!" ("base", xpos="far_left", ypos="head")
                                her @ cheeks blush "I... do?" ("disgust", "base", "base", "mid")
                                gen "Yes, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                                gen "Just like I requested, you held well until the very end." ("base", xpos="far_left", ypos="head")
                                gen "Of course, you better be ready, because at any moment, I could give you the signal to..." ("base", xpos="far_left", ypos="head")
                                gen "Cum for me!" ("base", xpos="far_left", ypos="head") with vpunch
                                her @ cheeks blush "..." ("angry", "wide", "base", "stare") #worried #shocked
                                gen "Nah, I'm just kidding." ("grin", xpos="far_left", ypos="head")
                                her @ cheeks blush "V-Very funny, [name_genie_hermione]..." ("angry", "squint", "base", "mid")
                                her @ cheeks blush "(I'm so on edge I almost came when he said it...)" ("angry", "happyCl", "base", "mid")
                                her @ cheeks blush "Can I go now?" ("open", "happyCl", "base", "mid")
                                gen "Sure, I won't keep you any longer." ("base", xpos="far_left", ypos="head")
                                her @ cheeks blush "Thank you..." ("soft", "narrow", "base", "down")

                            "-Fail her on her performance-":
                                gen "Now cum!" ("base", xpos="far_left", ypos="head")
                                her @ cheeks blush "*Nnnngh*..." ("angry", "happyCl", "worried", "mid") # whimpers
                                her @ cheeks blush "(Why did I react like this just now...?)" ("angry", "wide", "base", "stare")
                                her @ cheeks blush "I--{w=0.2} I can't..." ("disgust", "happyCl", "base", "mid")
                                gen "Oh, too bad, looks like you failed." ("base", xpos="far_left", ypos="head")
                                her @ cheeks blush "You're joking..." ("disgust", "narrow", "base", "mid")
                                gen "I expected better from you, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                                her @ cheeks blush "Whatever you say [name_genie_hermione]." ("soft", "narrow", "base", "down")
                                gen "That shall do for now, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                                gen "You may leave." ("base", xpos="far_left", ypos="head")

                        if not her_outfit_vibrators.unlocked:
                            her @ cheeks blush "" ("soft", "narrow", "base", "L")
                            nar "For a brief moment, you see Hermione's eyes flicker towards the vibrators left on your desk."
                            gen "Fine, you can take them and finish yourself off, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                            gen "Consider it a gift." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "..." ("base", "narrow", "base", "down") #blushing

                            call her_walk("desk", "base")
                            pause 0.5
                            hide vibrators_floor
                            call unlock_clothing("Congratulations! You have unlocked a new outfit!", her_outfit_vibrators)

                            her @ cheeks blush "{size=-5}Thank you...{/size}" ("open", "narrow", "base", "down")

                        else:
                            her @ cheeks blush "Alright then..." ("open", "narrow", "base", "down")

                            call her_walk("desk", "base")
                            pause 0.5
                            hide vibrators_floor
                            with d5

                            gen "What are you doing?" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "*Ehm*...{w=0.2} Didn't you gift me these?" ("open", "squint", "worried", "mid")
                            gen "I just have told you not to cum unless I say so, what are you planning to do with these exactly?" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "W--{w=0.2} Well, I was hoping..." ("angry", "squint", "worried", "mid")
                            gen "Fine, I'll allow it this time.... Go ahead then." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "Thank you..." ("open", "narrow", "base", "down")

                    "-Forget the grading-":
                        gen "Yes, that shall do for now." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Okay, I guess I'll be leaving now then..." ("disgust", "squint", "base", "R")
                        her "(At least he forgot about that silly grade thing...)" ("disgust", "narrow", "base", "down")

                        if not her_outfit_vibrators.unlocked:
                            her "" ("disgust", "narrow", "base", "L")
                            nar "For a brief moment, you see Hermione's eyes flicker towards the vibrators left on your desk."
                            gen "Fine, you can take them and finish yourself off, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "I wasn't--" ("angry", "base", "base", "mid")
                            gen "Consider it a gift." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "A-Alright..." ("disgust", "squint", "base", "mid") #blushing

                            call her_walk("desk", "base")
                            pause 0.5
                            hide vibrators_floor
                            call unlock_clothing("Congratulations! You have unlocked a new outfit!", her_outfit_vibrators)

                            her @ cheeks blush "{size=-5}Thank you...{/size}" ("base", "narrow", "base", "down")

                        else:

                            call her_walk("desk", "base")
                            pause 0.5
                            hide vibrators_floor
                            with d5

                            gen "I hope you're not planning to use those to finish yourself off." ("base", xpos="far_left", ypos="head")
                            her "What do you mean? Didn't you gift me these?" ("angry", "base", "base", "mid")
                            gen "That I did, but I believe I haven't said you're allowed to cum just yet, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "..." ("disgust", "squint", "base", "mid")
                            gen "Unless..." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "Yes?" ("angry", "base", "base", "mid")
                            gen "Well, I may allow it, as long as you promise to practice edging." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "I wasn't going to--" ("clench", "base", "base", "mid")
                            gen "I expect great things from you, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                            gen "Next time I shall grade you for your performance." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "(So he did remember...)" ("disgust", "base", "base", "R")
                            her @ cheeks blush "Fine, I'll try to find an opportunity to practice in my... chambers." ("angry", "narrow", "base", "down") # Hermione makes an unintentional pun, Genie's influence is rubbing off on her.
                            gen "Splendid!" ("grin", xpos="far_left", ypos="head")
                            gen "That will be all, [name_hermione_genie]. You are dismissed." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "Thank you, [name_genie_hermione]..." ("open", "closed", "base", "mid")
                            gen "Until next time." ("base", xpos="far_left", ypos="head")

                $ states.her.mood += 10
                call her_walk(action="leave")
                jump end_hermione_event

            "-Turn the intensity to Medium-":
                #She cums, but it takes a little longer.

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_medium.ogg"

                show her_vibrators_personal mouth_horny as cg with d5

                her "*Aaaaah*....{w=0.4} Yeeeeesss....."

                show her_vibrators_personal mouth_shocked as cg with d5

                her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
                gen "Now, now. Hold it in, you aren't allowed to get off just yet." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal mouth_open as cg with d5

                her "But--{w=0.2} *Ah*...{w=0.2} I thought this meant I could--"
                gen "I said hold it!" ("base", xpos="far_left", ypos="head")

                her "*Ah*...{w=0.2} *Ah*...{w=0.2}{nw}"

                show her_vibrators_personal eyes_squint_crossed as cg

                her "*Ah*... *Ah*...{fast} [name_genie_hermione],{w=0.2} I can't--"
                gen "Imagine what your peers would say... {i}Hermione Granger, failing a task set by her headmaster! What a disgrace!{/i}" ("base", xpos="far_left", ypos="head")
                gen "I thought you were better than this." ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyes_narrow_crossed mouth_angry as cg with d5

                her "[name_genie_hermione]--{w=0.2} *Ah*...{w=0.4} I can't control it!"
                gen "Yes you can, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyes_clenched as cg with d5

                her "{size=+4}{heart}*Nnngh*!{heart}{/size}"
                gen "Almost there..." ("base", xpos="far_left", ypos="head")
                gen "{size=+5}Now! Cum for me, [name_hermione_genie]!{/size}" ("base", xpos="far_left", ypos="head") with vpunch

            "-Turn the intensity to High-":

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_high.ogg"

                show her_vibrators_personal eyebrows_neutral eyes_wide_crossed mouth_ahegao as cg with d5

                her "{size=+4}{heart}*ohh*!{heart}*ohhhhhh*{heart}{/size}"
                gen "How about now? Is it still fine?" ("base", xpos="far_left", ypos="head")

                show her_vibrators_personal eyebrows_worried eyes_squint_crossed as cg with d5

                her "*Aheeeee*!! [name_genie_hermione], I can't--"
                gen "Answer me!" ("base", xpos="far_left", ypos="head")
                her "*Ahhh*...{w=0.2} *Ahee*...{w=0.2} I..."
                gen "Tell me you want to cum!" ("base", xpos="far_left", ypos="head")
                gen "Say it!" ("angry", xpos="far_left", ypos="head")

                show her_vibrators_personal eyebrows_neutral mouth_shocked as cg with d5

                her "*Ah*...{w=0.4}{size=+4} I want to cum!{/size}{heart}"
                gen "How much do you want it?" ("base", xpos="far_left", ypos="head")
                her "{heart}{heart}{size=+4}A lot, please, [name_genie_hermione], please let me cum!!!{/size}{heart}{heart}"

                show her_vibrators_personal eyebrows_worried mouth_ahegao_wet as cg with d5

                her "{heart}{heart}{size=+4}I need it!!{/size}{heart}{heart}"
                gen "So be it." ("base", xpos="far_left", ypos="head")

                # Turns the switch into overdrive mode
                gen "Skadoosh.{w=0.8}{nw}" ("base", xpos="far_left", ypos="head")

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_overdrive.ogg"

                show her_vibrators_personal eyes_wide_crossed as cg

                gen "Skadoosh.{fast}" ("base", xpos="far_left", ypos="head")



        show her_vibrators_personal hermione3 eyebrows_worried eyes_ahegao mouth_ahegao effects_squirt as cg with d5
        with kissiris
        play sound "sounds/slick_01.ogg"

        her @ cheeks blush "{size=+8}{heart}{heart}Aaaaah!!!!!{heart}{heart}{/size}{w=0.4}{nw}" ("grin", "narrow", "annoyed", "up")

        show her_vibrators_personal -effects_squirt effects_puddle as cg

        her @ cheeks blush "{size=+8}{heart}{heart}Aaaaah!!!!!{heart}{heart}{/size}{fast}" ("grin", "narrow", "annoyed", "up")

        gen "By the great--" ("base", xpos="far_left", ypos="head")

        show her_vibrators_personal effects_squirt as cg with d5
        with kissiris

        play sound "sounds/slick_01.ogg"
        her "{size=+8}{heart}*Ah*!{heart}{/size}{w=0.4}{nw}"

        show her_vibrators_personal -effects_squirt as cg with d5

        her "{size=+8}{heart}*Ah*!{heart}{/size}{fast}"

        show her_vibrators_personal eyes_closed mouth_open as cg with d5

        her "*Mmm*......"

        # End section

        label .end:

        stop background fadeout 2.0
        stop music fadeout 1
        show screen blkfade
        with d5

        her @ cheeks blush "" ("disgust", "squint", "base", "R")

        hide cg
        show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)
        nar "You watch as Hermione sits up and shimmies to the edge of your desk, planting her feet on the floor, she sways on the spot slightly before she readies herself, and makes her way to the front of your desk."
        $ hermione.equip(her_outfit_last)

        hide screen blkfade
        with d5

        her @ cheeks blush "" ("disgust", "squint", "base", "R") #blushing
        call ctc
        her @ cheeks blush "*Ahem*...{w=0.4} So, is that all?" ("open", "squint", "base", "R")
        gen "Yes, that shall do for today." ("base", xpos="far_left", ypos="head")

        menu:
            "-Grade her performance-":
                gen "Oh, wait!" ("base", xpos="far_left", ypos="head")
                gen "I was going to grade you, wasn't I?" ("base", xpos="far_left", ypos="head")
                gen "*Hmm*...{w=0.4} Let's see..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("soft", "base", "base", "mid") #hopeful

                menu:
                    "-Give her a passing grade-":

                        if _temp_premature_finish:
                            gen "Well, I was hoping that you'd be able to last longer than that--" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "..." ("disgust", "narrow", "base", "down") # Sadge
                            gen "--But..." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "...?" ("soft", "squint", "base", "mid") # Looks at genie full of hope
                            gen "I'll still give you a pass!" ("base", xpos="far_left", ypos="head")
                            her "Oh! Thank you [name_genie_hermione]!" ("grin", "base", "base", "mid")
                        else:
                            gen "You pass!" ("base", xpos="far_left", ypos="head")
                            gen "Excellent performance, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                            her "Oh... why thank you, [name_genie_hermione]." ("base", "base", "base", "mid")

                        if not her_outfit_vibrators.unlocked:
                            her "Is there some kind of reward?" ("base", "base", "base", "mid")
                            gen "Reward?" ("base", xpos="far_left", ypos="head")
                            gen "Wasn't having the biggest orgasm of your life enough for you?" ("base", xpos="far_left", ypos="head")
                            her "No, it was-- It's just..." ("angry", "base", "base", "mid")
                            her @ cheeks blush "Well, I was thinking, it's not like I can show this grade off to my classmates, or anything..." ("open", "base", "base", "R")
                            gen "I mean, you could--..." ("grin", xpos="far_left", ypos="head")
                            gen "--but I get the sentiment..." ("base", xpos="far_left", ypos="head")
                            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

                    "-Deny her a passing grade-":

                        gen "You fail!" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "I--{w=0.2} I fail?!" ("angry", "wide", "worried", "stare")
                        her "But [name_genie_hermione]!" ("angry", "wide", "base", "mid")
                        her @ cheeks blush "I did what you asked of me!" ("clench", "base", "worried", "mid")

                        if _temp_premature_finish:
                            gen "No, you did not, you had an orgasm before I gave you the signal to finish." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "But that's because you--" ("angry", "base", "worried", "mid")
                            gen "I don't want to hear your excuses. My decision is final." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "*tsk* That's unfair!" ("disgust", "narrow", "annoyed", "down")
                        else:
                            gen "Indeed, that you did, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "Then why are you giving me a bad grade?" ("angry", "base", "worried", "mid")

                        gen "You seem very distraught by this, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                        gen "I thought you said it wasn't even a real grade." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("disgust", "base", "base", "stare") # Shocked by the realisation that Genie is right
                        gen "Or are you merely looking for my approval?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("disgust", "narrow", "base", "down") # looks away blushing
                        if _temp_premature_finish:
                            gen "You'll have it once you've gained the ability to keep that {i}super soaker{/i} of yours, in check." ("base", xpos="far_left", ypos="head")
                        else:
                            gen "If that's the case, you did a very good job achieving what I required of you. I'm proud of you, truly." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "..." ("soft", "squint", "base", "mid") #embarrased but happy
                            gen "You still fail though." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("annoyed", "narrow", "base", "down") #Annoyed

                        if not her_outfit_vibrators.unlocked:
                            gen "Maybe after you've had some practice you can earn a passing grade." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "Practice?" ("angry", "base", "base", "mid")
                            gen "Yes, so you would be able to hold it in for longer..." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "Right... Practice it is..." ("soft", "narrow", "base", "R")

            "-She's had enough excitement for one day-":
                her @ cheeks blush "Alright. I'll be leaving now..." ("open", "base", "base", "R")

        if not her_outfit_vibrators.unlocked:
            gen "You can take those vibrators with you, if you want." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("soft", "base", "base", "R")

            pause 0.5
            hide vibrators_floor
            $ hermione.hide()
            call unlock_clothing("Congratulations! You have unlocked a new outfit!", her_outfit_vibrators)

            gen "Have fun, and try to not overdo it." ("base", xpos="far_left", ypos="head")
            gen "Or you might end up blind." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "........ *Sigh*" ("base", "narrow", "base", "down")
            her @ cheeks blush "I won't..." ("base", "narrow", "base", "down")
            gen "Who said that?" ("open", xpos="far_left", ypos="head")

        else:
            gen "Don't forget your vibrators." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh, right..." ("disgust", "narrow", "base", "mid")
            call her_walk("desk", "base")
            pause 0.5
            hide vibrators_floor
            with d5

        call her_walk(action="leave")

    else:
        # Tier 4
        # Does not unlock wardrobe item.
        # Uses Doll rather than CG
        # No grading.
        # Hermione leaves early.

        label .low_tier:

        her @ cheeks blush "*Ah*!" ("angry", "wide", "base", "stare")
        her @ cheeks blush "I wasn't ready!! Turn it off!" ("angry", "happyCl", "worried", "stare")
        gen "Forfeiting the points already, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        gen "Well, if you insist." ("base", xpos="far_left", ypos="head")

        play sound "sounds/click4.ogg"
        stop background

        her @ cheeks blush "Wait!" ("angry", "base", "base", "stare")
        gen "*Tsk* *Tsk*" ("base", xpos="far_left", ypos="head")
        gen "Too late. You really should try to be a bit more decisive, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "I thought you were here to earn your house some points. I guess I was wrong." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "closed", "worried", "mid")
        her @ cheeks blush "Just...{w=0.4} Could you set it to the low setting? Please?" ("open", "squint", "worried", "R")
        gen "Low setting, eh? Are you sure you are ready for that?" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes..." ("angry", "squint", "worried", "mid")
        gen "Low setting it is." ("grin", xpos="far_left", ypos="head")

        play sound "sounds/click4.ogg"
        play background "sounds/vibrator_low.ogg"

        her @ cheeks blush "{heart}*Ngh*{heart}!" ("angry", "narrow", "base", "up")
        gen "Better?" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} Yes... {w=0.4}Much better..." ("open", "closed", "base", "up")
        gen "Good, then let's continue from where we left off." ("base", xpos="far_left", ypos="head")
        menu:
            "-Ask her to get on the desk-":
                gen "Why don't you get on the desk for me?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "The desk?!" ("angry", "wide", "base", "stare")
                gen "Yes, the desk... I'd like a closer look at you..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I--{w=0.2} You never said I had to get on the desk." ("angry", "narrow", "worried", "mid")
                gen "Is it that difficult to climb the desk?" ("base", xpos="far_left", ypos="head")
                gen "I've seen you do it before." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "It's not the same when I'm wearing vibrators!" ("clench", "base", "base", "mid")
                gen "I suppose your legs would be a bit shaky." ("base", xpos="far_left", ypos="head")
                gen "(I'm sure that with enough training, she'll be able to climb the desk with these things on.)" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("annoyed", "narrow", "base", "R")
                gen "Then let's have a bit of a chat instead." ("base", xpos="far_left", ypos="head")
            "-Keep it going the way she is-":
                gen "Where was I--" ("base", xpos="far_left", ypos="head")
                gen "Oh right!" ("base", xpos="far_left", ypos="head")
        gen "Tell me, how was your day?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "W--{w=0.2}What?" ("angry", "base", "base", "mid")
        her @ cheeks blush "How was--{w=0.2} *Ah*...{w=0.2} my day?" ("open", "wink", "base", "mid")
        gen "Yes, tell me what you've been up to lately." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "T-This isn't the right time, [name_genie_hermione]." ("angry", "wink", "base", "mid")
        gen "*Hmm*?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I--{w=0.2} *Ah*...{w=0.4} I'm a bit preoccupied..." ("clench", "closed", "worried", "mid")
        gen "Surely you can multitask, I do it all the time." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I--{w=0.2} I just don't want to think about my classmates right now!" ("open", "closed", "worried", "mid")
        gen "I see..." ("base", xpos="far_left", ypos="head")

        $ _vibrator_pissed = False

        menu:
            "-Turn up the intensity-":
                $ _vibrator_pissed = True

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_medium.ogg"

                her @ cheeks blush "{heart}*Ah*!!{heart}" ("grin", "narrow", "worried", "up")
                her @ cheeks blush "T-turn it down, {w=0.3}it's too intense!" ("clench", "happyCl", "worried", "mid")
                gen "Some vibrations too much for you to handle, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "[name_genie_hermione], turn it down this instance, {w=0.5}or I'm leaving!" ("angry", "happyCl", "angry", "stare") #mad
                gen "..." ("base", xpos="far_left", ypos="head")

                play sound "sounds/click4.ogg"
                stop background

                gen "There... {w=0.4}Better?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Hmph*." ("annoyed", "narrow", "angry", "R") #annoyed
                gen "There's no need to be upset, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "There is, if you keep turning it up like that without telling me!" ("angry", "narrow", "angry", "mid")
                gen "I just wanted to steer your thoughts away from your classmates, and it worked!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("annoyed", "narrow", "base", "R")
                gen "Until I brought them up again just now, I guess..." ("base", xpos="far_left", ypos="head")
                gen "Anyway..." ("base", xpos="far_left", ypos="head")

            "-Turn it off-":

                play sound "sounds/click4.ogg"
                stop background

                gen "Well, if that's the case, I suppose we're done here." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "But--" ("angry", "squint", "worried", "stare")
                her @ cheeks blush "What about my points?!" ("angry", "squint", "worried", "mid")
                gen "Your points?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Yes, am I still getting--" ("open", "base", "worried", "mid")

        play sound "sounds/click4.ogg"
        play background "sounds/vibrator_low.ogg"

        her @ cheeks blush "*Ah*..." ("open", "happyCl", "worried", "mid")
        gen "If you want your points, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "You can't just stand there and do nothing." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} W--{w=0.2}What?" ("angry", "squint", "base", "stare") #looks away
        gen "You've heard me--{w=0.4}Look at me when I'm speaking to you, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("soft", "squint", "worried", "mid") #Hermione looks at you, blushing
        gen "Well?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well--{w=0.2} *Ah*...{w=0.4} Well, what?" ("angry", "squint", "worried", "mid")
        gen "You said you didn't want to think about your classmates, why is that?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh...{w=0.4} Right..." ("disgust", "squint", "worried", "mid")
        gen "Don't tell me you've been skipping class!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "What?! No, of course not!" ("angry", "base", "worried", "mid")
        her @ cheeks blush "I've been attending--{w=0.2} *Ah*...{w=0.4} Class...{w=0.2} As per usual." ("open", "squint", "worried", "mid")
        gen "That's good." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Although--{w=0.2} *Ah*...{w=0.4} As you already know, I've arrived late to a couple of them." ("open", "closed", "worried", "mid")
        gen "You have?" ("base", xpos="far_left", ypos="head")
        gen "Why are you being late to your classes?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} That's--{w=0.2} *Ah*...{w=0.4} That's kind of your fault... [name_genie_hermione]... I mean we spend so much time in here and all--" ("angry", "narrow", "base", "R")

        menu:
            # Both result in the event ending.
            "-Be kind-":
                #Mood stays the same
                gen "Oh right..." ("base", xpos="far_left", ypos="head")
                gen "No need to worry, [name_hermione_genie]. You're helping out the headmaster, after all." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh, I wasn't worried about--" ("upset", "squint", "base", "R")
                gen "I'm sure that such a bright girl as yourself is able to keep up with the curriculum anyway." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Ah*...{w=0.4} Yes, so far--" ("open", "closed", "base", "R")
                her @ cheeks blush "So...--{w=0.4} *Mmmm*...{w=0.4} So good..." ("base", "closed", "worried", "mid")
                gen "I appreciate your honesty, any other student would've kept this information from me." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh, well..." ("grin", "closed", "worried", "mid") #blush

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_medium.ogg"

                her @ cheeks blush "*Ah*!" ("angry", "wide", "worried", "stare")
                her @ cheeks blush "[name_genie_hermione]...!" ("angry", "happyCl", "worried", "mid")
                gen "Feels good, doesn't it?" ("base", xpos="far_left", ypos="head")
                gen "Let it be known that your headmaster rewards honesty." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} I--" ("clench", "happyCl", "worried", "mid")

                if _vibrator_pissed:
                    #Event end, low mood penalty

                    her @ cheeks blush "Didn't I tell you to not--{w=0.2} *Ngh*...{w=0.4} Turn it up without telling me!?" ("angry", "narrow", "annoyed", "stare") #Embarrased
                    gen "*Hmm*?" ("base", xpos="far_left", ypos="head")
                    gen "Does it not feel good?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "T-That's not--{w=0.2} The problem!" ("clench", "happyCl", "angry", "mid")
                    her @ cheeks blush "It's--{w=0.2} *Ah*..." ("open", "happyCl", "angry", "mid")
                    her @ cheeks blush "I can't believe you!" ("open", "happyCl", "angry", "stare")

                    # Replaces vibrators in underwear with underwear
                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.strip("accessory0", "accessory1")
                    $ hermione.equip([her_panties_base1, her_bra_base1])
                    with d3
                    pause .5

                    play sound "sounds/drop_plastic.ogg"
                    show vibrators_floor at Transform(xpos=536, ypos=413, zoom=0.5)
                    with d5

                    $ states.her.mood += 10

                    her @ cheeks blush "I wore your stupid vibrators, so I'll have my points now!" ("angry", "narrow", "angry", "mid")
                    gen "Technically they were a gift." ("base", xpos="far_left", ypos="head")

                    hide vibrators_floor
                    with d5

                    call her_walk("desk", "base")
                    play sound "sounds/punch01.ogg"
                    show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)
                    with hpunch

                    her @ cheeks blush "Keep your stupid gift!" ("mad", "narrow", "angry", "mid") # Angry
                    gen "Alright... I suppose I could keep them for now..." ("base", xpos="far_left", ypos="head")

                    call her_walk("mid", "base")
                    call her_chibi(flip=False)
                    with d3

                    her @ cheeks blush "I want my points now..." ("open", "base", "annoyed", "mid")

                    play sound "sounds/click4.ogg"
                    stop background

                    gen "...{w=0.4} Very well, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                else:
                    #Gets wet down her legs and leaves (No mood penalty)

                    her @ cheeks blush "Please, I--" ("angry", "happyCl", "base", "mid")
                    her @ cheeks blush "It's too--{w=0.2} *Ah*...{w=0.4} If you keep this up I won't--" ("open", "happyCl", "worried", "mid")
                    gen "Did you not want a reward for your honesty?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "It's--{w=0.2} It's not that--..." ("angry", "happyCl", "worried", "mid")
                    gen "Don't you think it's a bit impolite to not express gratitude for my generosity?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I--{w=0.2} You didn't have to...{w=0.4} Some points would've been--" ("disgust", "happyCl", "worried", "mid")

                    $ hermione.set_cum(pussy="vibratorp_light")

                    gen "Points? Is that really the only thing you want?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "O--{w=0.2} Of course! Why else would I--" ("angry", "happyCl", "worried", "mid")
                    gen "Looks to me like you're not doing it just for points..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "What are you--{w=0.4} *Ngh*...{w=0.4} implying..." ("disgust", "happyCl", "worried", "mid")
                    her @ cheeks blush "..." ("angry", "narrow", "base", "down") #Wide eyed, looks down
                    gen "Now then, I think it's time we reach the climax of this activity." ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "The climax?!" ("clench", "wide", "base", "mid") #clench

                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.unequip("accessory0", "accessory1")
                    $ hermione.equip([her_panties_base1, her_bra_base1])
                    $ hermione.set_cum(pussy="underwear_light")
                    with d3

                    play sound "sounds/drop_plastic.ogg"
                    show vibrators_floor at Transform(xpos=436, ypos=413, zoom=0.5)
                    with d5

                    gen "What the--" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I--{w=0.2}I'll have those points now." ("disgust", "squint", "base", "L")
                    gen "But we were just getting started!" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "And now we're finished." ("open", "narrow", "base", "R")
                    gen "Are you sure? I've finished plenty of times, and it's usually more--" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "--Finished! We're done here!" ("angry", "happyCl", "annoyed", "mid")

                    nar "Hermione bends over and picks up the vibrators from the ground, slamming them onto your desk."

                    play sound "sounds/punch01.ogg"
                    show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)
                    with hpunch

                    her @ cheeks blush "You can have these back now." ("disgust", "happy", "annoyed", "mid")
                    gen "Are you sure? You can keep them, you know." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "No, thanks..." ("open", "narrow", "angry", "R")

                    call her_walk("mid", "base")
                    call her_chibi(flip=False)
                    with d3

                    gen "I suppose you wouldn't want anyone to find them in your dorm." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "(That's not what I'm worried about...)" ("disgust", "narrow", "base", "R")

                    play sound "sounds/click4.ogg"
                    stop background

                    gen "No worries, just let me know if you feel like using them again." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Sure... If I ever get the sudden urge to ask my headmaster for some vibrators, I'll come and ask..." ("soft", "narrow", "annoyed", "R")
                    gen "Ask and come any time you like!" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "..." ("disgust", "narrow", "base", "mid")
                    her @ cheeks blush "Can I have my points now?" ("open", "happy", "base", "mid")
                    gen "Certainly." ("base", xpos="far_left", ypos="head")

                $ gryffindor += current_payout
                gen "{number=current_payout} points to Gryffindor, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Thanks..." ("annoyed", "narrow", "angry", "R")

                $ hermione.set_cum(None)
                $ hermione.equip(her_outfit_last)
                $ hermione.hide()
                with fade
                pause 1

                her @ cheeks blush "..." ("annoyed", "narrow", "worried", "R")

                call her_walk(action="leave")


            "-Scold her-":
                gen "Blaming your headmaster, are we?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "But... [name_genie_hermione]." ("angry", "squint", "worried", "mid")
                her @ cheeks blush "I'm not to blame if it's you who is keeping me--" ("angry", "squint", "worried", "mid")

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_medium.ogg"

                her @ cheeks blush "Ah!" ("scream", "happyCl", "worried", "mid")
                gen "That's not how you're supposed to speak to your headmaster, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                gen "Tell me you're sorry and won't be late to classes again." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} Alright--" ("open", "happyCl", "worried", "mid")
                her @ cheeks blush "I won't be late for classes again!" ("angry", "happyCl", "worried", "mid")
                gen "And?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "And--{w=0.2} *Ah*...{w=0.4} I--{w=0.2} I--" ("clench", "happyCl", "worried", "mid")

                if _vibrator_pissed:
                    $ states.her.mood += 15

                    her "..." #Wide eyed angry

                    $ hermione.equip([her_panties_base1, her_bra_base1])
                    $ hermione.unequip("accessory0", "accessory1")
                    play sound "sounds/drop_plastic.ogg"
                    show vibrators_floor at Transform(xpos=436, ypos=413, zoom=0.5)
                    with d5

                    her @ cheeks blush "I have told you to not turn it up without letting me know beforehand!" ("clench", "wide", "annoyed", "mid")
                    gen "What?!" ("angry", xpos="far_left", ypos="head")
                    her @ cheeks blush "I can't believe you tried to make me apologise!" ("angry", "base", "angry", "mid")
                    gen "..." ("angry", xpos="far_left", ypos="head")

                    nar "Hermione bends over and picks up the vibrators from the ground, slamming them onto your desk."

                    hide vibrators_floor
                    with d5

                    play sound "sounds/punch01.ogg"
                    show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)
                    with hpunch

                    her @ cheeks blush "My points! Now!" ("open", "base", "annoyed", "mid")
                    gen "Alright, alright... Don't get your panties in a twist." ("angry", xpos="far_left", ypos="head")

                    $ gryffindor += current_payout
                    gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")

                    play sound "sounds/click4.ogg"
                    stop background

                    gen "There, happy?" ("base", xpos="far_left", ypos="head")
                    her "Very!" ("open", "narrow", "angry", "R") # Sarcastic

                    $ hermione.set_cum(None)
                    $ hermione.equip(her_outfit_last)
                    $ hermione.hide()
                    with fade
                    pause 1

                    her @ cheeks blush "*Hmph*!" ("normal", "base", "angry", "mid")

                    call her_walk(action="leave")
                    play sound "sounds/door_down.ogg"
                    with hpunch

                else: #low mood penalty
                    $ states.her.mood += 10

                    $ hermione.set_cum(pussy="vibratorp_light")

                    gen "And now you're getting wet without my permission?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "W--{w=0.2} What?!?" ("angry", "wide", "worried", "down") #looks down #shocked
                    gen "You're not getting off from being scolded, are you?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Getting off from--{w=0.2} Of course not!" ("clench", "wide", "worried", "mid")
                    gen "Then why are you so wet, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

                    $ hermione.set_cum(pussy="vibratorp_heavy")

                    her @ cheeks blush "I'm--{w=0.2} *ah*...{w=0.4} I am not!" ("angry", "squint", "worried", "mid")
                    gen "Clearly you are." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I don't--{w=0.2} *Ahh*...{w=0.4} \"get off\" from being...{w=0.4} *Nhh* scolded!" ("open", "happyCl", "worried", "mid")

                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.equip([her_panties_base1, her_bra_base1])
                    $ hermione.unequip("accessory0", "accessory1")
                    $ hermione.set_cum(pussy="underwear_heavy")
                    with d3

                    gen "What are you--" ("base", xpos="far_left", ypos="head")

                    call her_walk("desk", "base")

                    gen "Hey! We're not done yet!" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Just... Take these back." ("angry", "squint", "worried", "mid")

                    show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)
                    with d5

                    her "Could--{w=0.2} Can I have my points now?" #looking down
                    gen "But we haven't--" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I insist..." ("angry", "closed", "base", "mid")
                    gen "Suit yourself..." ("base", xpos="far_left", ypos="head")

                    $ gryffindor += current_payout
                    gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                    gen "Now, can we get back to--" ("base", xpos="far_left", ypos="head")

                    call her_walk("mid", "base")
                    her @ cheeks blush "" ("angry", "closed", "base", "mid", flip=True, trans=d3)
                    with d3
                    pause .5

                    gen "You could at least have the courtesy to look me in the eyes when I'm speaking to you..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "..." ("angry", "narrow", "worried", "down") #Looking down ashamed
                    gen "Look at me!" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "..." ("angry", "base", "base", "stare")

                    call her_chibi(flip=False)
                    pause .5
                    her @ cheeks blush "" ("angry", "narrow", "worried", "mid", flip=False, trans=d3)
                    with d3
                    pause .5

                    gen "(Why is she still blush-- Oh, I see...)" ("base", xpos="far_left", ypos="head")
                    gen "Okay [name_hermione_genie], you may leave..." ("base", xpos="far_left", ypos="head")

                    $ hermione.set_cum(None)
                    $ hermione.equip(her_outfit_last)
                    with d3

                    her @ cheeks blush "..." ("annoyed", "base", "base", "R")

                    call her_walk(action="leave")
                    gen "(This girl is such a mystery sometimes...)" ("base", xpos="far_left", ypos="head")

                    play sound "sounds/click4.ogg"
                    stop background

        hide vibrators_floor
        with fade

    jump end_hermione_event

label hg_vibrators_public_return:

    #Set since clothing schedule would overwrite
    $ hermione.equip(her_outfit_default)
    $ hermione.equip(her_bottom_school2)
    $ hermione.equip(her_outfit_vibrators, remove_old=False)

    if states.her.public_tier >= 5:

        label .high_tier:

        if not states.her.ev.vibrators.public_stage == 2:
            # First time

            play background "sounds/vibrator_low.ogg" fadein 3 #fades in as she walks inside
            call her_walk("mid", "base", action="enter")

            gen "Finally! What took you--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm so sorry, [name_genie_hermione]!!" ("scream", "happyCl", "worried", "mid", xpos="mid", ypos="base")

            her @ cheeks blush "" ("angry", "happyCl", "worried", "mid")
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("top")
            with d3
            pause 1

            gen "What the--" ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("bra")
            with d3
            pause 1

            gen "[name_hermione_genie]? What is the meaning of this?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft_blink "*Nnnn*--" ("angry", "happyCl", "worried", "R")
            gen "Are you--" ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("bottom", "panties")
            $ hermione.set_cum(pussy="vibrator_pre")
            with d3
            pause 1

            her @ cheeks blush "{heart}{heart}{heart}{size=+10}*Aaaaaaaaaah*!!!!!{/size}{heart}{heart}{heart}" ("open_wide_tongue", "wide", "base", "ahegao") #ahegao

            play sound "sounds/slick_01.ogg"
            with kissiris
            $ hermione.set_cum(pussy="vibrator_squirt")
            with d3
            pause .5
            $ hermione.set_cum(pussy="vibrator_post")
            with d3
            pause .5

            gen "By the great desert--" ("base", xpos="far_left", ypos="head")

            play sound "sounds/slick_01.ogg"
            with kissiris
            $ hermione.set_cum(pussy="vibrator_squirt")
            with d3
            pause .5
            $ hermione.set_cum(pussy="vibrator_post")
            with d3

            her @ cheeks blush "{heart}{size=+5}*Aaaah*!!!{/size}{heart}" ("angry", "happyCl", "base", "up")

            play sound "sounds/slick_01.ogg"
            with kissiris
            $ hermione.set_cum(pussy="vibrator_squirt")
            with d3
            pause .5
            $ hermione.set_cum(pussy="vibrator_post")
            with d3

            her @ cheeks blush "{size=+2}*Ah*!!!{/size}" ("grin", "narrow", "base", "up")

            gen "[name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("angry", "closed", "worried", "mid")
            her @ cheeks blush "At last..." ("grin", "narrow", "base", "stare")
            her @ cheeks blush "These things...{w=0.4} *Ah*...{w=0.4} They turned on as I was walking up the stairs to your tower..." ("angry", "closed", "worried", "stare")
            gen "They--" ("base", xpos="far_left", ypos="head")

            $ hermione.hide()
            with d3

            play sound "sounds/drawer_open.ogg"
            pause 1

            gen "(Whops! I must've switched it on when I put the controller away...)" ("base", xpos="far_left", ypos="head")

            play sound "sounds/cough_male.ogg"
            gen "*Loud cough*{w=0.5}{nw}" ("base", xpos="far_left", ypos="head")

            play sound "sounds/click4.ogg"
            stop background

            gen "*Loud cough*{fast}" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ah*...{w=0.4} F-Finally..." ("angry", "narrow", "base", "down", xpos="base")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.wear("panties")
            $ hermione.set_cum(pussy="vibratorp_heavy")
            with d3
            pause 1

            play sound "sounds/drop_plastic.ogg"
            $ hermione.equip(her_panties_base1)
            $ hermione.unequip("accessory0", "accessory1")
            $ hermione.set_cum(pussy="underwear_heavy")
            show vibrators_floor at Transform(xpos=536, ypos=413, zoom=0.5)
            with d5
            pause .8

            her @ cheeks blush "I can't believe you did that to me...{w=0.4} After everything you've put me through today." ("angry", "narrow", "base", "mid")
            gen "Well... I did warn you that I'd turn them on at any point." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I--{w=0.2} I suppose you did." ("disgust", "narrow", "base", "mid") #looks down
            gen "So...{w=0.4} I assume you've been...{w=0.5} {i}buzzy{/i}?" ("base", xpos="far_left", ypos="head")


            her @ cheeks blush "*Mmm*...{w=0.4} Tell me about it..." ("disgust", "closed", "worried", "mid")
            gen "Isn't that your job?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What? Oh..." ("angry", "narrow", "base", "mid")
            gen "I presume you went to your classes as usual?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course!" ("angry", "base", "base", "mid")
            her @ cheeks blush "Although, the fact I had these... things... strapped to me for the day made everything rather difficult..." ("open", "narrow", "base", "down")
            gen "In what way?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well, first off, I couldn't exactly visit the library after classes, like usual..." ("soft", "narrow", "base", "R")
            her @ cheeks blush "With how quiet it is in there, I'd immediately attract everyone's attention the moment these things start buzzing." ("open", "narrow", "base", "down")
            gen "(Or once you started moaning, more likely...)" ("base", xpos="far_left", ypos="head")
            gen "So, no library visits today. Tell me something interesting, like what happened after you left my office." ("base", xpos="far_left", ypos="head")

            # Transfiguration
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.set_cum(None)
            $ hermione.wear("bottom")
            with d3

            her @ cheeks blush "Well... Once I left, I headed to the first class of the day -- Transfiguration." ("soft", "narrow", "base", "down")
            her @ cheeks blush "And the closer I got to the classroom, the more nervous I got." ("angry", "narrow", "base", "down")
            her @ cheeks blush "I mean... What if professor McGonagall called for me to demonstrate something in front of my classmates?" ("angry", "narrow", "base", "mid")

            menu:
                "-Mock her-":
                    gen "Nervous? Don't you mean excited?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I was not getting excited by wearing the vibrators..." ("open", "narrow", "annoyed", "mid")
                    gen "That's not what I meant." ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "I know that." ("open", "narrow", "angry", "R")
                    gen "I'm talking about you being a bookworm." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "You don't have to spell it out..." ("angry", "narrow", "annoyed", "mid")
                    gen "Just making sure we're on the same page." ("base", xpos="far_left", ypos="head")
                    gen "Of the book." ("base", xpos="far_left", ypos="head")
                    gen "That thing you always read." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "..." ("disgust", "narrow", "annoyed", "mid")
                    her @ cheeks blush "Anyway..." ("open", "narrow", "base", "R")

                "-Push her horny buttons-":
                    call gen_chibi("stand", 225, "base")
                    with d5

                    her @ cheeks blush "...?" ("soft", "base", "base", "mid")

                    call gen_walk(path=[(230, 470), (440, 470), (450, 430)], speed=1.2)

                    pause 0.5

                    play sound "sounds/boing02.ogg"
                    gen "Boop!" ("base", xpos="far_left", ypos="base")
                    her @ cheeks blush "{heart}*Ah*!!!{heart}" ("angry", "base", "base", "stare")
                    her @ cheeks blush "Why did you do that?" ("angry", "narrow", "base", "mid")
                    gen "I don't know, just felt like it." ("base", xpos="far_left", ypos="base")

                    call gen_chibi("stand", 450, 430, flip=False)
                    with d5

                    call gen_walk(path=[(450, 430), (440, 470), (230, 470)], speed=1.2)
                    call gen_chibi("sit_behind_desk")
                    with d5
                    pause 1

                    her @ cheeks blush "*Hmph*... As I was saying..." ("angry", "base", "base", "R")

                "-Let her speak-":
                    pass

            her @ cheeks blush "Since I do look forward to demonstrating all the things I learn." ("open", "closed", "base", "mid")
            gen "*Cough* {size=-4}nerd{/size} *Cough*." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Are you alright [name_genie_hermione]? You've been coughing a lot today." ("upset", "squint", "base", "mid")
            gen "I'm good, just got a nerd stuck down my throat." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I see..." ("disgust", "squint", "base", "mid")
            gen "Please, continue with your boasting." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm not boasting!" ("angry", "narrow", "annoyed", "mid")
            her @ cheeks blush "I'm just trying to provide context about why I often get called up in front of the class." ("disgust", "narrow", "angry", "mid")
            gen "You mean to provide exhibition?" ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.equip(her_bra_base1)
            with d3
            pause 1

            her @ cheeks blush "Do you mean exposition?" ("disgust", "narrow", "base", "mid")
            gen "There's a difference?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes...{w=0.4} Either way, the context is..." ("angry", "narrow", "base", "R")
            her @ cheeks blush "Professor McGonagall spotted my natural talents on the very first day, and has called me up to demonstrate them ever since." ("grin", "narrow", "base", "mid")
            her @ cheeks blush "She noticed right away that I am an expert at practising with magic wands." ("grin", "squint", "base", "mid")
            her @ cheeks blush "Of course, I'd expect no less from such a seasoned witch as her." ("base", "squint", "base", "R")
            gen "Seasoned you say... From teaching the arts of bukkake no doubt..." ("base", xpos="far_left", ypos="head")
            her "In fact, I was the first person to perfectly master turning a rat yellow and ever since then I've been the go-to student to demonstrate--" ("smile", "base", "base", "mid")
            gen "Hold on... A Rat?!" ("base", xpos="far_left", ypos="head")
            her "Yes, why so surprised?" ("open", "base", "base", "mid")
            gen "I don't want to hear about stupid rats, what about the exhibitionism? The vibrators? The guys jacking off onto you, and maybe your teacher as well?" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Jacking-- What on earth are you talking about?!" ("angry", "wide", "base", "mid")
            gen "Isn't this when you're supposed to tell me about the vibrators going off in front of your class?" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "No!" ("angry", "base", "worried", "mid")
            gen "Then what is all this?!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Exposition!" ("angry", "squint", "worried", "mid")
            gen "(Bloody exposition!)" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "I'll just skip forward to after the class..." ("open", "squint", "base", "mid")
            her @ cheeks blush "So, after the class, I slipped away from my friends and waited, time ticking down for my next period." ("open", "base", "base", "R")
            gen "Your--{w=0.2}, Wait, it's that time of the month?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Our next class period!" ("angry", "narrow", "annoyed", "mid")
            gen "Oh, that makes more sense." ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.wear("top")
            with d3

            her @ cheeks blush "..." ("annoyed", "narrow", "base", "R")
            gen "So, the vibrators turned on during your break?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "No, they didn't turn on before our next class either." ("open", "closed", "base", "mid")
            gen "I'm relieved, that would've been pretty anticlimactic..." ("base", xpos="far_left", ypos="head")

            # Charms
            her @ cheeks blush "So, I begrudgingly made my way to charms--" ("open", "closed", "worried", "mid")
            gen "(Bet she's never said that before.)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "--Which is the class I was most worried about." ("disgust", "narrow", "base", "mid")
            gen "What's so bad about Charms?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Professor Flitwick!" ("angry", "base", "base", "mid")
            her @ cheeks blush "With how short he is, I was worried he'd see the vibrator from underneath my skirt." ("open", "squint", "base", "mid")
            gen "See it? You're not expecting extra points for going commando, are you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "He'd see it bulging out inside of my panties!" ("angry", "narrow", "annoyed", "mid")
            gen "Right, so you're worried he'd think you've grown a--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "narrow", "annoyed", "mid") #annoyed
            gen "*Ahem*... Please continue..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well, luckily it never came to that." ("open", "narrow", "base", "R")
            her @ cheeks blush "He had one of the other students help him with today's demonstration for once, so today was a safe day." ("open", "closed", "base", "mid")
            gen "You've already said as much." ("base", xpos="far_left", ypos="head")
            gen "But, enough with the build up..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm getting there!" ("angry", "narrow", "annoyed", "mid")
            her @ cheeks blush "I'm just--{w=0.2} Well, I wanted you to know what went through my head before... You know." ("angry", "narrow", "base", "R")
            gen "Fine, if it makes you feel better, go ahead." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "closed", "base", "mid") #annoyed
            her @ cheeks blush "So, Charms finished, and we went for lunch." ("open", "closed", "base", "mid")
            gen "We? Who's we?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Me and my friends..." ("open", "squint", "base", "mid")
            gen "Oh, right..." ("base", xpos="far_left", ypos="head")
            gen "(I keep forgetting that the nerdy girl archetype has actual friends in this universe...)" ("base", xpos="far_left", ypos="head")

            #Lunch
            her @ cheeks blush "So, we had our lunch... And whilst chatting with my friends, I sort of forgot I was even wearing them... The vibrators, I mean." ("open", "squint", "worried", "R")
            her @ cheeks blush "Which, thinking back on it, I'm sure was your intention this whole damn time..." ("open", "narrow", "base", "mid")
            gen "You caught me." ("base", xpos="far_left", ypos="head")
            gen "(Probably shouldn't tell her I was sleeping the entire time...)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "So, when they decided to go outside and play some {i}gobstones{/i}, they asked me to join them, so I accompanied them as usual." ("open", "squint", "base", "R")

            stop music fadeout 1
            stop weather fadeout 4

            show screen blkfade
            with d5

            show her_vibrators_public_xray zorder 15 as cg # Dynamic displayable (Updates its children every interaction)
            show her_vibrators_public underwear as xray_child # Controls the bottom layer of the Xray CG
            show her_vibrators_public_proxy as xray_overlay # Controls the top layer of the Xray CG

            hide screen blkfade
            with d5

            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
            play weather "sounds/day.ogg" fadein 2 fadeout 2

            gen "I see...{w=0.4} Hold on, this was just past lunchtime you said?" ("base", xpos="far_left", ypos="head")
            her "Yes..." ("base", "base", "base", "mid")
            gen "That's around the time when--" ("base", xpos="far_left", ypos="head")
            her "They turned on!" ("base", "base", "base", "mid")
            gen "--I woke up from my nap!" ("angry", xpos="far_left", ypos="head")
            her "......?" ("base", "base", "base", "mid") # Raised eyebrow
            gen "I-I mean... What you said!" ("grin", xpos="far_left", ypos="head")
        else:
            # Repeat

            call her_walk("mid", "base", action="enter")

            gen "Welcome back." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Good evening, [name_genie_hermione]..." ("open", "squint", "base", "mid", xpos="base", ypos="base")
            gen "How was your day? Did you have another fun trip?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Depends on your definition of fun I guess..." ("open", "squint", "base", "R")
            gen "A day full of sexual tension." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "In that case, I guess it fits the description..." ("soft", "closed", "base", "mid")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("top")
            with d3
            pause 1

            gen "Oh, goodie!" ("base", xpos="far_left", ypos="head")
            gen "Tell me all about it!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well..." ("open", "narrow", "base", "down")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("bottom")
            with d3

            her @ cheeks blush "It all began at lunch..." ("open", "squint", "base", "mid")
            her @ cheeks blush "Since you had instructed me to accompany my friends, I had to try and convince them to go outside again today..." ("open", "squint", "base", "R")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("bra")
            with d3
            pause 0.5

            $ hermione.strip("accessory0")
            with d3

            her @ cheeks blush "It was a bit difficult, initially they were planning to play wizard chess, so I had to really rack my brain to find a good reason why they should play gobstones instead." ("angry", "closed", "base", "R")
            gen "But you succeeded?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "After some convincing, yes." ("open", "narrow", "base", "mid")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.equip(her_bra_base1)
            with d3
            pause 1

            gen "Gotta use those assets to the fullest! Just as I taught--" ("base", xpos="far_left", ypos="head") #Joke on art assets
            her @ cheeks blush "Thank you, I knew that \"Witch weekly\" article I read on the male psyche would come to good use." ("grin", "base", "base", "mid")
            gen "The what?" ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("panties")
            with d3
            pause 1
            $ hermione.strip("accessory1")
            with d3
            pause 1

            play sound "sounds/drop_plastic.ogg"
            show vibrators_floor at Transform(xpos=536, ypos=413, zoom=0.5)
            with d5

            her @ cheeks blush "\"Deciphering the male psyche\"." ("open", "squint", "base", "mid")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.equip(her_panties_base1)
            with d3
            pause 1

            gen "Is this from one of those gossip magazines nobody reads?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "...{w} Gossip magazines?!" ("angry", "base", "base", "mid")

            her @ cheeks blush "I'll have you know that Witch Weekly is a very reputable paper!" ("open", "narrow", "annoyed", "mid")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.wear("bottom")
            with d3
            pause 1

            gen "Alright, I guess I'll take your word for it..." ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.wear("top")
            with d3
            pause 1

            gen "So, you used some mumbo-jumbo from the magazine to convince the boys to head outside again...?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes, in short--" ("open", "narrow", "base", "R")

            stop music fadeout 1
            stop weather fadeout 4

            #CG Hermione outside in the courtyard, in front of Harry and Ron who's playing Gobstones, base facial expression

            show screen blkfade
            with d5

            show her_vibrators_public_xray zorder 15 as cg # Dynamic displayable (Updates its children every interaction)
            show her_vibrators_public underwear as xray_child # Controls the bottom layer of the Xray CG
            show her_vibrators_public_proxy as xray_overlay # Controls the top layer of the Xray CG

            hide screen blkfade
            with d5

            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
            play weather "sounds/day.ogg" fadein 2 fadeout 2

            her "After some convincing, my friends and I finally made our way outside into the courtyard..." ("base", "base", "base", "mid")
            her "Just as we were about to sit down, suddenly, the vibrators turned on." ("base", "base", "base", "mid")

        # This section has a different ending, depending on the player's choices.
        #Optimal order is Medium > Low > High

        $ _vibrator_last = None
        $ _vibrator_low = False
        $ _vibrator_medium = False
        $ _vibrator_high = False

        show vibrator_interface zorder 20

        # First choice
        menu:
            "\"(Right up to the high setting!)\"":
                $ _vibrator_high = True
                $ _vibrator_last = "high"

                show vibrator_interface vibration_high high_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_high.ogg"

                # Worst option

                # Xray turns active once player picks this option, Vibrator shakes, etc.
                show her_vibrators_public nude eyebrows_surprised mouth_shocked eyes_clenched as xray_child
                show her_vibrators_public_proxy eyebrows_surprised mouth_shocked eyes_clenched as xray_overlay

                # TODO sounds

                if not states.her.ev.vibrators.public_stage == 2:
                    # First time
                    her "Since I had forgotten about them, I yelped out in surprise, and my friends stopped and looked at me."
                else:
                    # Repeat

                    her "Even though I was expecting it this time, I was not ready for you to switch it on to the high setting so quickly."
                    her "I tried to stifle myself, but my gasp had the boys look towards me suspiciously."

                show her_vibrators_public eyebrows_neutral eyes_sad mouth_open npc_sus_ron as xray_child
                show her_vibrators_public_proxy eyebrows_neutral eyes_sad mouth_open npc_sus_ron as xray_overlay

                gen "Uh-oh."
                her "I can still picture how their eyes locked onto me... I felt so humiliated, and unable to neither move nor speak..."

                # Hermione looks to the side
                show her_vibrators_public eyebrows_worried blush_heavy mouth_lip_bite eyes_left as xray_child
                show her_vibrators_public_proxy eyebrows_worried blush_heavy mouth_lip_bite eyes_left as xray_overlay

                her "I swear, I could feel the gaze of other students on my back as well."
                gen "You think they realised what was happening?"
                her "*Hmph*... They certainly knew \"something\" was up."

                # Hermione looks forward
                show her_vibrators_public mouth_grossedout2 eyes_forward as xray_child
                show her_vibrators_public_proxy mouth_grossedout2 eyes_forward as xray_overlay

                her "Nevertheless, I finally managed to blurt out \"mosquito\" and it appeared they have bought my excuse."

                show her_vibrators_public -npc_sus_ron as xray_child
                show her_vibrators_public_proxy -npc_sus_ron as xray_overlay

                her "At least I think they did, as they went back to their game..."
                gen "Smooth..."
                her "Thank you, [name_genie_hermione]."
                gen "So, how did it feel?"

                show her_vibrators_public eyes_sad as xray_child
                show her_vibrators_public_proxy eyes_sad as xray_overlay

                her "You mean the vibrators?"
                gen "I mean you standing there... In front of your friends, vibrators going ham on your pussy--"
                her "[name_genie_hermione]!"
                gen "Sorry--"
                gen "Your pussy, {size=+5}and{/size} tits."
                her "Do you have to be so vulgar..."
                gen "Is that not what happened?"
                her "Yes, but--"
                gen "So, what next? You didn't chicken out on me did you?"
                her "Of course not!"

                show her_vibrators_public mouth_upset eyes_closed as xray_child
                show her_vibrators_public_proxy mouth_upset eyes_closed as xray_overlay

                her "You should know exactly what you did--"
                gen "Oh? So this was when I--"

            "\"(Straight up to medium setting!)\"":
                # Best option
                $ _vibrator_medium = True
                $ _vibrator_last = "medium"

                show vibrator_interface vibration_medium medium_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_medium.ogg"

                show her_vibrators_public nude eyebrows_surprised eyes_forward mouth_shocked as xray_child
                show her_vibrators_public_proxy eyebrows_surprised eyes_forward mouth_shocked as xray_overlay

                if not states.her.ev.vibrators.public_stage == 2:
                    her "As they turned on, I was quickly brought back to reality, remembering our \"agreement\"..."
                else:
                    her "Surprised it had already started, I readied myself for the worst..."

                her "Without thinking, I instinctively bit my lip..."

                show her_vibrators_public blush_heavy eyebrows_worried mouth_lip_bite as xray_child
                show her_vibrators_public_proxy blush_heavy eyebrows_worried mouth_lip_bite as xray_overlay

                gen "*Hmm*...{w=0.4} Well, you can't always control these things."
                her "I would've been able to, if you had let me use the controller, [name_genie_hermione]..."
                gen "Guilty..."
                her "After a couple of seconds, I realised what I was doing."

                show her_vibrators_public eyes_down mouth_open npc_sus_ron as xray_child
                show her_vibrators_public_proxy eyes_down mouth_open npc_sus_ron as xray_overlay

                her "Looking over at my friends, praying they didn't see or hear anything, at one point though, I could swear Ron looked over at me..."

                show her_vibrators_public -npc_sus_ron as xray_child
                show her_vibrators_public_proxy -npc_sus_ron as xray_overlay

                her "But as I blinked he was back to playing their game."
                gen "How did that make you feel?"
                her "Oh...{w=0.4} *Ehm*..." ("base", "base", "base", "mid")
                gen "Go on, this is not the time for dishonesty..."
                her "Well, the fact that I had gotten away with it felt a bit exciting, I guess."

                show her_vibrators_public eyes_closed mouth_lip_bite as xray_child
                show her_vibrators_public_proxy eyes_closed mouth_lip_bite as xray_overlay

                her "Still... I was having my privates stimulated in front of my friends, so I couldn't help but feel a bit anxious."
                gen "Guilty that they were missing all the fun no doubt."
                her "That's not what I meant!"

                show her_vibrators_public eyes_down as xray_child
                show her_vibrators_public_proxy eyes_down as xray_overlay

                her "I was feeling anxious because they might find out what I've been putting myself through for the sake of our house!"
                gen "I see... So, not only were they missing all the fun, but also all the points they could earn while doing some favours."
                her "..." ("base", "base", "base", "mid")

                show her_vibrators_public eyes_sad as xray_child
                show her_vibrators_public_proxy eyes_sad as xray_overlay

                her "[name_genie_hermione], you might be seeing all this as just some light-hearted fun, but I can assure you that they would not see it in the same light."
                gen "Your view is based on your idealised version of your friends, or the reality?"
                her "The reality!"

                show her_vibrators_public eyes_closed as xray_child
                show her_vibrators_public_proxy eyes_closed as xray_overlay

                gen "Sure, if you say so, [name_hermione_genie]."
                her "..."
                her "Either way, I didn't have much time to think about my rising anxiousness..."
                gen "Right, so that's when I--"

            "\"(Lowest setting of course!)\"":
                # Average option
                $ _vibrator_low = True
                $ _vibrator_last = "low"

                show vibrator_interface vibration_low low_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_low.ogg"

                show her_vibrators_public nude eyebrows_worried mouth_open as xray_child
                show her_vibrators_public_proxy eyebrows_worried mouth_open as xray_overlay

                if not states.her.ev.vibrators.public_stage == 2:
                    her "Yes...{w=0.4} Luckily, it was just low enough not to startle me and cast suspicion..."
                    her "At first it didn't feel as if what was happening was real, but it soon dawned on me what a terrible situation I had put myself in."

                    show her_vibrators_public nude blush_heavy mouth_lip_bite eyes_left as xray_child
                    show her_vibrators_public_proxy blush_heavy mouth_lip_bite eyes_left as xray_overlay

                    her "I was standing outside, in the middle of a courtyard, my friends right in front me as the vibrators had begun shaking against my private parts..."
                    her "Of course... Knowing you, I had no doubts it had only just begun and there was more to come."
                    gen "You've got me all figured out, huh."
                    her "*Hmph*..."
                else:
                    her "It started with a low hum, and soon the familiar tingling sensation hit me like a bludger."

                    show her_vibrators_public blush_heavy mouth_open eyes_left as xray_child
                    show her_vibrators_public_proxy blush_heavy mouth_open eyes_left as xray_overlay

                    her "It brought my last experience back to life again, and I started doubting if it was a wise decision to put myself through this again."
                    gen "Surely you weren't considering missing out on, possibly, one of the best orgasms of your life."
                    her "I would never be concerned about missing out on such a thing!"
                    gen "Right, of course. There's no way that would happen on my watch."
                    her "..."

                gen "And then what?"

                show her_vibrators_public mouth_open eyes_closed as xray_child
                show her_vibrators_public_proxy mouth_open eyes_closed as xray_overlay

                gen "You didn't try running off, did you?"
                her "..."
                her "No, I didn't run off..."
                gen "There's no need to be embarrassed [name_hermione_genie], completing the task I requested shows your determination and character."
                her "Thanks, I suppose..."

                show her_vibrators_public eyebrows_neutral eyes_crossed as xray_child
                show her_vibrators_public_proxy eyebrows_neutral eyes_crossed as xray_overlay

                gen "That character, of course, being a complete slut who enjoys getting off in front of her friends!"
                her "[name_genie_hermione]!"
                her "..."
                her "I--{w=0.2} I don't appreciate you belittling me, [name_genie_hermione]..."
                gen "You're in the wrong if that's what you've got out of my words."
                gen "Belittling is... {w=0.4}below me..."
                her "..."  #Yeah right
                gen "Even if it wasn't, I'd hardly ever need to belittle someone who is so set on not being true to herself..."

                show her_vibrators_public mouth_lip_bite eyes_big_crossed as xray_child
                show her_vibrators_public_proxy mouth_lip_bite eyes_big_crossed as xray_overlay

                her "..."
                gen "Now, speak the truth... You were enjoying it, weren't you?"
                her "I--"
                her "I was not!"
                gen "(She's such a know-it-all, yet she never learns...)"
                gen "Alright then... Let's keep playing your game, [name_hermione_genie]."
                gen "Tell me, if you weren't enjoying yourself, why didn't you just run off when you had the chance?"

                show her_vibrators_public eyebrows_upset eyes_closed as xray_child
                show her_vibrators_public_proxy eyebrows_upset eyes_closed as xray_overlay

                her "I--{w=0.2} my feet didn't move!"
                gen "Your feet?"
                her "Yes!"

                show her_vibrators_public eyes_clenched as xray_child
                show her_vibrators_public_proxy eyes_clenched as xray_overlay

                her "All these thoughts were racing through my head, and I didn't know what to do, I could barely control my body."
                gen "Right, that's very relatable and all, but--"
                her "It's the truth!"
                gen "Sure, sure, I believe you..."
                gen "So, what were these \"things\" going through your head exactly?"
                her "Oh--{w=0.2} *Ehm*..."
                gen "(She's going to say \"forfeiting the points\" isn't she...)"

                show her_vibrators_public eyes_left as xray_child
                show her_vibrators_public_proxy eyes_left as xray_overlay

                her "I didn't want to forfeit the points!"
                gen "(Nailed it.)"

                show her_vibrators_public eyebrows_worried eyes_down as xray_child
                show her_vibrators_public_proxy eyebrows_worried eyes_down as xray_overlay

                her "I thought that if I had run off, you wouldn't pay me, and it would all be for naught..."
                her "Although, I didn't have much time to consider my options as the decision was being made for me..."
                gen "Made for--"
                gen "Oh, I see."
                gen "That's when I--"

        show vibrator_interface

        # Second choice
        menu:
            "\"(Turned it to the high setting!)\"" if not _vibrator_high:
                # Average option
                $ _vibrator_high = True

                show vibrator_interface vibration_high high_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_high.ogg"

                show her_vibrators_public eyebrows_surprised mouth_shocked eyes_crossed as xray_child
                show her_vibrators_public_proxy eyebrows_surprised mouth_shocked eyes_crossed as xray_overlay

                her "Yes, all of a sudden, the vibrators began vibrating violently!"

                if _vibrator_last == "low":
                    # Strength was set to low before.

                    her "I wasn't ready for it at all. I was expecting it to ramp up slowly!"

                    show her_vibrators_public eyebrows_neutral mouth_open eyes_down as xray_child
                    show her_vibrators_public_proxy eyebrows_neutral mouth_open eyes_down as xray_overlay

                    her "At first I couldn't move due to the shock, but at that point I could feel my legs starting to shake for... {w=0.25}Other reasons..."
                    gen "What other reasons?"
                    her "Well..."
                    gen "Come on, [name_hermione_genie]... We all know what you're here for."
                    her "Fine--"
                else:
                    # Strength was set to medium.
                    her "I was expecting it to go down at this point, not up!"
                    gen "{i}Why not shake things up every once in a while!{/i} That's my motto."
                    her "That's what happened to me..."
                    gen "It did?"

                    show her_vibrators_public eyebrows_neutral mouth_open eyes_down as xray_child
                    show her_vibrators_public_proxy eyebrows_neutral mouth_open eyes_down as xray_overlay

                    her "My legs, they had begun shaking quite a bit."
                    her "Getting caught off guard like that... Made it difficult to compose myself."
                    gen "Pray tell..."

                show her_vibrators_public mouth_lip_bite eyes_sad as xray_child
                show her_vibrators_public_proxy mouth_lip_bite eyes_sad as xray_overlay

                her "I was getting a bit excited, okay?"
                gen "*Heh-heh*..."
                gen "So, what were the boys doing? Surely, they must've noticed their friend going delirious?"
                her "At that point, it was difficult to tell, they were too busy playing with their balls..." ("open", "closed", "base", "mid")

                #Could cut back to room screen

                stop background fadeout 2
                stop background fadeout 2
                hide cg
                with fade
                call weather_sound

                gen "{size=+4}THEY WERE WHAT?!?{/size}" ("angry", xpos="far_left", ypos="head")
                gen "{size=+4}In the middle of the courtyard?! At {b}my{/b} school?!{/size}" ("angry", xpos="far_left", ypos="head")
                her "Where else should they do it?" ("angry", "base", "base", "mid")
                gen "The bathroom?! Their dorm? Anywhere but the courtyard!" ("angry", xpos="far_left", ypos="head")
                her "But [name_genie_hermione], students have been doing it in the courtyard for generations!" ("clench", "base", "worried", "mid")
                gen "Watching them gobbling stones is one thing, but since when was \"ballplay\" in the courtyard acceptable?" ("angry", xpos="far_left", ypos="head")
                her @ cheeks blush "Ballpl--{w=0.4} [name_genie_hermione]... I'm talking about the gobstone balls!" ("open", "base", "annoyed", "mid")
                gen "Gob-- Oh!" ("base", xpos="far_left", ypos="head")
                gen "(The naming conventions make no sense in this universe...)" ("base", xpos="far_left", ypos="head")
                gen "It should be named something different then, like \"Gob-balls\"! {w=0.3}Or something..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("disgust", "narrow", "base", "mid")
                gen "Actually, that sounds even more confusing..." ("base", xpos="far_left", ypos="head")
                gen "What were we talking about again?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Balls?" ("disgust", "base", "base", "mid")
                gen "That's not it..." ("base", xpos="far_left", ypos="head")
                gen "Oh, I remember! Your quaking loin and shaking groin!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Hmph*..." ("disgust", "narrow", "base", "R")

                #Cut back to CG
                show her_vibrators_public_xray zorder 15 as cg
                play weather "sounds/day.ogg" fadein 2 fadeout 2
                play background "sounds/vibrator_high.ogg" fadein 2
                with fade

                gen "So, the vibrators were going at full force on your breasts and pussy, yet the boys didn't suspect a thing?"
                her "I didn't say that..."
                gen "But you just said--"
                her "I said that they were playing with their balls, not that neither of them hadn't caught on to something..."

                show her_vibrators_public eyebrows_worried npc_sus_ron as xray_child
                show her_vibrators_public_proxy eyebrows_worried npc_sus_ron as xray_overlay

                her "One of them kept glancing at me for sure... And I believe he might've been... hard."
                gen "Hard, as in?"
                her "You, above all else, should know exactly what I'm talking about!"
                gen "I hardly know what you're talking about."

                show her_vibrators_public eyes_forward as xray_child
                show her_vibrators_public_proxy eyes_forward as xray_overlay

                her "You're unbelievable... His dick! His dick was hard!"
                her "Happy?!"
                gen "I just wanted to make sure you weren't talking about that {i}gobbledigook{/i} game again."
                her "Gobstones..."
                gen "You're certain he had a hard-on?"

                show her_vibrators_public eyes_down as xray_child
                show her_vibrators_public_proxy eyes_down as xray_overlay

                her "Of course I'm certain! I know what a boner looks like when I see one!"
                gen "Well, perhaps you were just seeing what you wanted to see."
                her "I sure was not!"
                her "He wasn't sly about it at all, and even changed his positioning to have the robes cover it up!"
                gen "Ah yes, the robes... No awkward boners or pokey nipples in sight, not at my school..."
                her "Whatever the case, I think I managed to get away from a very awkward situation..."

                show her_vibrators_public -npc_sus_ron as xray_child
                show her_vibrators_public_proxy -npc_sus_ron as xray_overlay

                her "Even after he went back to focusing on their game... He kept glancing over at me every once in a while."
                her "Which did make things much more difficult, every time he looked over, I'm sure my expression changed into some stupid grimace, trying to cover for what was going on."
                gen "I'm sure it made things harder alright..."
                her "Yes... My situation was getting rocky by the minute, all I could concentrate on was trying to stand as still and be as quiet as possible..."
                gen "And how did that go for you?"
                her "Not very well..."

                show her_vibrators_public eyes_closed mouth_open wetness_vagina as xray_child
                show her_vibrators_public_proxy eyes_closed mouth_open wetness_vagina as xray_overlay

                her "In fact, I was beginning to feel my panties getting drenched--"
                gen "Naturally, you had just seen your friend pop a boner in front of you."
                her "I wasn't getting off from my friends having a boner!"

                show her_vibrators_public mouth_lip_bite as xray_child
                show her_vibrators_public_proxy mouth_lip_bite as xray_overlay

                gen "Getting hard... By looking at you...--"
                her "Moving on!"
                gen "Alright, alright..."
                gen "Please continue."
                her "I don't know if I feel like it, if you're going to continue making these wild accusations..."
                gen "You're the one eho started talking about balls and boners... I hardly have any interest in such things... {w=0.3}Unless it's my own, that is."
                her "..."
                gen "Now then, tell me more about how you, {i}DID NOT{/i} get off from your friend watching you."
                her "*Sigh*..."

                her "Well... At that point, the intensity changed again."
                gen "Oh right, I--"

                $ _vibrator_last = "high"

            "\"(Turned it to the medium setting.)\"" if not _vibrator_medium:
                $ _vibrator_medium = True

                show vibrator_interface vibration_medium medium_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_medium.ogg"

                if _vibrator_last == "high":
                    # Strength was set to high before.

                    show her_vibrators_public eyebrows_neutral eyes_sad effects_shaky_legs as xray_child
                    show her_vibrators_public_proxy eyebrows_neutral eyes_sad effects_shaky_legs as xray_overlay

                    her "Yes, with the intensity going down, I could feel my legs quaking. I had to coax myself from falling to my knees."
                    her "It was as if I had been thrown into a cold lake and my body was only just beginning to get used to the temperature."
                    her "Well, to be honest, I'm not sure what I was feeling."
                    gen "Intense pleasure? Anticipation?"
                    gen "Wait, I know!"
                    gen "Love!"

                    show her_vibrators_public -effects_shaky_legs  as xray_child
                    show her_vibrators_public_proxy -effects_shaky_legs as xray_overlay

                    her "That's... Not it."
                    gen "Damn."

                    show her_vibrators_public eyes_closed mouth_open as xray_child
                    show her_vibrators_public_proxy eyes_closed mouth_open as xray_overlay

                    her "If any of those was the goal, then you shouldn't have thrown me into the deep end right off the bat."
                    her "Honestly, I don't know what you were thinking..."
                    gen "I was going for a splash and ripple effect."
                    her "That's not how it works..."
                    gen "Live and learn I guess..."
                    her "And that's when--"
                else:
                    # Strength was set to low before.

                    show her_vibrators_public eyebrows_surprised eyes_forward mouth_open as xray_child
                    show her_vibrators_public_proxy eyebrows_surprised eyes_forward mouth_open as xray_overlay

                    her "Yes, the speed began ramping up."

                    show her_vibrators_public eyes_down as xray_child
                    show her_vibrators_public_proxy eyes_down as xray_overlay

                    her "And that's when I started panicking a little..."

                    show her_vibrators_public eyebrows_worried eyes_clenched as xray_child
                    show her_vibrators_public_proxy eyebrows_worried eyes_clenched as xray_overlay

                    her "I had second thoughts about this whole deal, about letting my friends see me in this state."
                    her "I was never supposed to let it go this far, I just wanted to earn points for my house and make them happy!"
                    her "And here I was, standing right in front of them while being stimulated all over."

                    #Wet Vagina
                    show her_vibrators_public mouth_lip_bite wetness_vagina as xray_child
                    show her_vibrators_public_proxy mouth_lip_bite wetness_vagina as xray_overlay

                    her "Was I about to let myself orgasm right then and there?"
                    gen "Yes, obviously!"
                    her "Obviously not!"
                    her "But that's when--"
                    gen "Oh, don't tell me--"

                $ _vibrator_last = "medium"

            "\"(Turned it to the low setting.)\"" if not _vibrator_low: #Best option
                $ _vibrator_low = True

                show vibrator_interface vibration_low low_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_low.ogg"

                show her_vibrators_public eyebrows_neutral eyes_forward mouth_open as xray_child
                show her_vibrators_public_proxy eyebrows_neutral eyes_forward mouth_open as xray_overlay

                her "Yes, luckily for me..." ("base", "base", "base", "mid")
                if _vibrator_last == "medium":
                    # Strength was set to medium before.

                    show her_vibrators_public eyes_closed mouth_neutral as xray_child
                    show her_vibrators_public_proxy eyes_closed mouth_neutral as xray_overlay

                    her "It was just enough for me to enjoy myself, and at the same time, not have to worry about being caught."
                else:
                    # Strength was set to high before.

                    show her_vibrators_public eyes_down mouth_neutral as xray_child
                    show her_vibrators_public_proxy eyes_down mouth_neutral as xray_overlay

                    her "After the initial shock, it was finally at a level where I could at the very least lose any suspicion they might've gained towards me..."
                    her "At first, they just looked over at me every once in a while, as if wanting to check up on me, but soon enough they were fully engrossed in their silly game as usual."

                    show her_vibrators_public eyebrows_worried eyes_closed as xray_child
                    show her_vibrators_public_proxy eyebrows_worried eyes_closed as xray_overlay

                    her "I must say, this is one of the few times I'm glad they're so bad at paying attention to their surroundings..."

                her "So, as I stood there with my eyes closed, I began losing myself in the sensations..."
                her "I must admit, it was a quite pleasant feeling... Standing outside, the warm sun against my back... Listening to the sounds of my friends enjoying themselves."
                her "The fact that they were there with me the entire time, it made me feel as if we were sharing this feeling."
                her "Even if in reality, they weren't aware of anything that was going on..."
                gen "Feeling comfortable around your friends is very important, [name_hermione_genie]."
                her "*Hmm*... Yes, although I don't think this is the kind of comfort you're meant to feel around your friends..."
                gen "Unless benefits are added to the equation..."

                show her_vibrators_public eyebrows_worried mouth_lip_bite as xray_child
                show her_vibrators_public_proxy eyebrows_worried mouth_lip_bite as xray_overlay

                her "As I stood there, I slowly became more and more conscious of each and every pulse I felt in my groin."

                #Wet pussy
                show her_vibrators_public wetness_vagina as xray_child
                show her_vibrators_public_proxy wetness_vagina as xray_overlay

                her "I could also feel that I was getting even wetter by the minute..."
                her "Not to the point where it was out of my control, of course, but..."
                gen "Of course."

                show her_vibrators_public eyebrows_worried eyes_sad as xray_child
                show her_vibrators_public_proxy eyebrows_worried eyes_sad as xray_overlay

                her "My breath began to quicken slightly, but I managed to keep it in check, only looking over every once in a while to make sure they weren't suspecting anything."
                her "And that's when you--"
                her "You--"
                gen "Don't tell me..."

                $ _vibrator_last = "low"

        show vibrator_interface

        # Third choice
        menu:
            "\"(I Turned it to the high setting!)\"" if not _vibrator_high:
                $ _vibrator_high = True

                show vibrator_interface vibration_high high_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_high.ogg"

                if _vibrator_last == "medium":
                    # Strength was set to medium before.
                    # Vagina is wet

                    # This is the second best ending. Hermione cums once, but she manages to hide it from her friends.

                    show her_vibrators_public eyebrows_worried eyes_clenched mouth_lip_bite effects_shaky_legs as xray_child
                    show her_vibrators_public_proxy eyebrows_worried eyes_clenched mouth_lip_bite effects_shaky_legs as xray_overlay

                    her "Yes, and as you did, I clenched my legs together."
                    her "I was not about to do the thing I had told myself I would never, ever, do! I tried to keep it together as hard as I could."

                    show her_vibrators_public eyes_sad mouth_open as xray_child
                    show her_vibrators_public_proxy eyes_sad mouth_open as xray_overlay

                    her "I tried looking over at my friends, but as I did, that just made me more aware of how stiff my nipples had become--"
                    her "--how much my legs were shaking, how silly I must've looked, and what they'd think of me if they caught on to what I've got myself into."

                    show her_vibrators_public eyes_clenched as xray_child
                    show her_vibrators_public_proxy eyes_closed as xray_overlay

                    her "I was stuck in an endless cycle of shame and... and--"
                    gen "Lust?"

                    show her_vibrators_public eyes_big_ahegao as xray_child
                    show her_vibrators_public_proxy eyes_big_ahegao as xray_overlay

                    her "And that's when it engulfed me all at once."

                    show her_vibrators_public eyes_big_ahegao mouth_lip_bite tears_ahegao wetness_legs as xray_child
                    show her_vibrators_public_proxy eyes_big_ahegao mouth_lip_bite tears_ahegao wetness_legs as xray_overlay

                    her "Biting down on my lip, I orgasmed right then and there, right in front of them!"
                    her "Something that I never thought I'd do, or wanted to experience within their vicinity."
                    her "My legs were shaking like crazy, I bit my lip so hard I drew blood, but I knew I could not let any noise out because that would give me away."
                    her "Until suddenly--"

                    show screen blkfade

                    play sound "sounds/click4.ogg"
                    stop background
                    stop background
                    stop music fadeout 1.0
                    hide vibrator_interface
                    hide cg
                    call weather_sound

                    her "The vibrators turned off."

                    hide screen blkfade
                    with d3

                    gen "And...{w=0.4} What happened next?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Well..." ("angry", "closed", "base", "mid")
                    her @ cheeks blush "At first I felt fulfilled, almost happy, and bold, I somehow managed to get away without being caught." ("angry", "narrow", "base", "down")
                    her @ cheeks blush "But that feeling was quickly replaced with shame..." ("angry", "closed", "worried", "mid")
                    gen "Shame?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Yes, shame!" ("angry", "narrow", "annoyed", "mid")
                    her @ cheeks blush "This was {b}the{/b} line I couldn't and shouldn't cross, but yet--" ("disgust", "narrow", "worried", "mid")
                    gen "Says who?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Says me!" ("scream", "narrow", "annoyed", "mid")
                    gen "..." ("angry", xpos="far_left", ypos="head")
                    gen "I mean...{w=0.4} You got away with it, didn't you? Surely, it's not such a big deal." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "It is a big deal!" ("angry", "base", "annoyed", "mid")
                    her @ cheeks blush "I'm constantly doing all these deplorable things, way beyond anything I thought I'd ever do, and this is just another step in that direction." ("angry", "narrow", "worried", "R")

                    menu:
                        gen "..." ("base", xpos="far_left", ypos="head")

                        "-Agree with her-":
                            gen "Maybe you're right." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "[name_genie_hermione]?" ("angry", "narrow", "base", "mid")
                            gen "The line never mattered at all." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "How could you say such a thing!?" ("angry", "squint", "annoyed", "mid")
                            gen "Isn't that what you just said?" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "Yes, but you're not supposed to agree with me!" ("open", "narrow", "annoyed", "mid")
                            gen "Why not? It's true, isn't it?" ("base", xpos="far_left", ypos="head")
                            gen "In any case, I don't see how it affects anything." ("base", xpos="far_left", ypos="head")
                            gen "Lines are meant to be crossed, it's how we achieve our true potential." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "But I didn't cross the line! They didn't see!" ("angry", "squint", "annoyed", "mid")
                            gen "It's just a matter of time, either you'll cross that imaginary line or you'll move it forward just enough to tell yourself you never did." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "I-- Well-- *Hmph*... I'd never..." ("open", "narrow", "annoyed", "R") #blushing looking away
                            gen "Keep telling yourself that." ("base", xpos="far_left", ypos="head")
                            gen "Anyhow, your story was satisfying, I think that shall do for today." ("base", xpos="far_left", ypos="head")

                            her @ cheeks blush "..." ("annoyed", "narrow", "base", "down") #looks down still blushing
                        "-Disagree with her-":
                            gen "You didn't cross the line." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "I think I did..." ("angry", "narrow", "worried", "R")
                            gen "You don't want your friends to know what you're doing to earn points for your house, correct?" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "I...{w=0.4} Yes?" ("open", "base", "worried", "mid")
                            gen "Then what does that have to do with you cumming in front of them?" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "But--{w=0.2} Well, I suppose it's not exactly..." ("disgust", "squint", "worried", "mid")
                            gen "Exactly what?" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "Well, I still don't want them to find out that I--" ("open", "squint", "worried", "R")
                            gen "That you're what?" ("base", xpos="far_left", ypos="head")
                            gen "A slut?" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "[name_genie_hermione]!" ("angry", "wide", "base", "mid")
                            gen "I'm sure they wouldn't mind, or maybe they would even be happy to know that you're available to them at any time." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "But that's so wrong..." ("angry", "squint", "worried", "mid")
                            gen "Is it, though? Sharing is caring." ("base", xpos="far_left", ypos="head")
                            gen "In any case, I think we're done here for today." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "*Ehm*... [name_genie_hermione]..." ("disgust", "squint", "worried", "mid")
                            gen "Yes, slut?" ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "... I-- I was just..." ("angry", "narrow", "base", "down")
                else:
                    # Strength was set to low before
                    # This is the best ending. Hermione cums multiple times and the boys take notice, but she gets away with it.
                    # Vagina is wet

                    show her_vibrators_public eyebrows_worried eyes_big_ahegao mouth_ahegao effects_shaky_legs as xray_child
                    show her_vibrators_public_proxy eyebrows_worried eyes_big_ahegao mouth_ahegao effects_shaky_legs as xray_overlay

                    her "All of a sudden, I felt a jolt spread throughout my body, and I moaned out loud, letting everyone in the courtyard hear me, as my body was wrecked by multiple orgasmic waves!"

                    show her_vibrators_public wetness_legs npc_shock_ron npc_shock_harry as xray_child
                    show her_vibrators_public_proxy wetness_legs npc_shock_ron npc_shock_harry as xray_overlay

                    her "As wave after wave hit me the only thing I could hear was my friend's gasps, which at that moment, only made the sensation so much stronger."

                    show her_vibrators_public eyes_clenched mouth_lip_bite as xray_child
                    show her_vibrators_public_proxy eyes_clenched mouth_lip_bite as xray_overlay

                    her "I tried to control myself, but my attempts were futile, my excitement kept flowing down my shaky thighs."
                    her "I could feel each and every pulse across my entire body, first it spread out from my head, then across my breasts, down to my legs, and all the way out to my toes."
                    gen "Damn, you go, girl!"

                    show her_vibrators_public eyebrows_neutral eyes_ahegao as xray_child
                    show her_vibrators_public_proxy eyebrows_neutral eyes_ahegao as xray_overlay

                    her "Completely lost in the moment, I stopped caring about my surroundings, and I simply let go."
                    her "Even the fact that my friends were right there, looking at me, it didn't matter."

                    show her_vibrators_public tears_ahegao mouth_neutral as xray_child
                    show her_vibrators_public_proxy tears_ahegao mouth_neutral as xray_overlay

                    her "My reputation didn't matter either."
                    her "I didn't care what would happen, as long as I could cum and see this through to the very end."
                    her "And that's when they called my name..."

                    show her_vibrators_public eyebrows_worried eyes_crossed mouth_shocked as xray_child
                    show her_vibrators_public_proxy eyebrows_worried eyes_crossed mouth_shocked as xray_overlay

                    her "Their voices brought me back to reality, and I finally took in my surroundings, realizing the situation I was in, but it was too late."

                    show her_vibrators_public no_hermione as xray_child
                    show her_vibrators_public_proxy no_hermione as xray_overlay

                    play sound "sounds/fall.ogg"
                    with hpunch

                    her "My legs finally buckled, as orgasm, after orgasm, had finally taken its toll on my body."
                    her "My friends, seeing this, yelped out in shock, and called my name again."
                    her "And after sitting down on my knees for a moment that felt like an eternity, I finally slumped to the floor and everything went dark."
                    her @ cheeks blush "The only thing I could remember before passing out were the vibrators, finally coming to a stop..." ("angry", "narrow", "base", "down")

                    stop background fadeout 2
                    stop background fadeout 2
                    stop music fadeout 1.0
                    hide vibrator_interface
                    hide cg
                    with fade
                    call weather_sound

                    gen "That's one hell of an orgasm... And here I thought I took that crown." ("base", xpos="far_left", ypos="head")
                    gen "So, is this like a bad ending or what?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "A bad ending?" ("angry", "base", "base", "mid")
                    gen "Didn't they realise what happened to you? Wait, surely you wouldn't be here telling me all this if that was the case." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Well, you know how I said I thought one of them looked over at me?" ("open", "squint", "base", "R")
                    gen "Yeah?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Well, it turns out they had been worried about me." ("angry", "narrow", "base", "down")
                    her @ cheeks blush "Apparently, they had been checking in on me the entire day, feeling something was off." ("soft", "narrow", "base", "down")
                    her @ cheeks blush "I had obviously not been acting myself that day during our lessons..." ("open", "narrow", "base", "down")

                    if not states.her.ev.vibrators.public_stage == 2:
                        her @ cheeks blush "No raising my hand during transfiguration, no helping out with demonstrations during charms..." ("open", "closed", "base", "mid")
                        her @ cheeks blush "So, the reason why they kept looking over was to make sure I was okay." ("annoyed", "closed", "base", "mid")

                    her @ cheeks blush "Of course they wouldn't expect that the reason I wasn't acting myself was because I had strapped vibrators on my body!" ("open", "closed", "base", "mid")
                    gen "*Hmm*... I'm beginning to understand why women think that men are completely oblivious creatures..." ("base", xpos="far_left", ypos="head")
                    gen "Very well [name_hermione_genie], that shall very much do for today." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Oh, okay then..." ("soft", "narrow", "base", "down")

                $ _vibrator_last = "high"

            "\"(I Turned it to the medium setting.)\"" if not _vibrator_medium:
                $ _vibrator_medium = True

                show vibrator_interface vibration_medium medium_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_medium.ogg"

                if _vibrator_last == "low":
                    # Strength was set to low before.
                    # Hermione is denied an orgasm, the boys almost notice.
                    # Vagina is wet

                    show her_vibrators_public eyebrows_upset eyes_clenched mouth_open as xray_child
                    show her_vibrators_public_proxy eyebrows_upset eyes_clenched mouth_open as xray_overlay

                    her "I let out a small squeal--"

                    show her_vibrators_public eyes_sad mouth_lip_bite as xray_child
                    show her_vibrators_public_proxy eyes_sad mouth_lip_bite as xray_overlay

                    her "But I managed to stifle it, just before the boys could notice."

                    show her_vibrators_public eyebrows_worried eyes_down mouth_disappointed as xray_child
                    show her_vibrators_public_proxy eyebrows_worried eyes_down mouth_disappointed as xray_overlay

                    her "This time, though, they really did look concerned, and no wonder... I couldn't help but display something was happening, across my face."

                    show her_vibrators_public eyes_left mouth_neutral as xray_child
                    show her_vibrators_public_proxy eyes_left mouth_neutral as xray_overlay

                    her "Trying to pull myself together, I only managed to muster an apologetic smile and stammer how close of a call it was..."
                    gen "To cum all over them, you mean?"
                    her "No, I meant their game..."

                    show her_vibrators_public mouth_lip_bite as xray_child
                    show her_vibrators_public_proxy mouth_lip_bite as xray_overlay

                    her "Although, you are not entirely incorrect..."

                    #Legs shaking
                    show her_vibrators_public eyes_closed effects_shaky_legs as xray_child
                    show her_vibrators_public_proxy eyes_closed effects_shaky_legs as xray_overlay

                    her "They went back to playing their game just in time, as I felt myself being brought right to the edge..."

                    #Wet down legs
                    show her_vibrators_public wetness_legs as xray_child
                    show her_vibrators_public_proxy wetness_legs as xray_overlay

                    her "My legs were quaking, I was sweating all over, but it wasn't just sweat that was dripping down my legs..."

                    show her_vibrators_public eyes_clenched mouth_open as xray_child
                    show her_vibrators_public_proxy eyes_clenched mouth_open as xray_overlay

                    her "The only thing I could do was to pray they didn't notice it, when suddenly--"

                    show her_vibrators_public eyebrows_surprised eyes_forward mouth_disappointed as xray_child
                    show her_vibrators_public_proxy eyebrows_surprised eyes_forward mouth_disappointed as xray_overlay

                    her "The vibrators went completely still."
                    gen "Oh no!"
                    her "Yes..."

                    show her_vibrators_public eyebrows_neutral eyes_down as xray_child
                    show her_vibrators_public_proxy eyebrows_neutral eyes_down as xray_overlay

                    her "Ending as abruptly as it started, I was left dazed and confused about what had just happened."

                    show her_vibrators_public eyebrows_worried eyes_sad mouth_lip_bite as xray_child
                    show her_vibrators_public_proxy eyebrows_worried eyes_sad mouth_lip_bite as xray_overlay

                    her "My head was still spinning, I had a sudden urge to just plunge my fingers in there and finish the job myself."
                    gen "Did you?"

                    show her_vibrators_public mouth_disappointed as xray_child
                    show her_vibrators_public_proxy mouth_disappointed as xray_overlay

                    her "N-No... With how concerned they were, they most certainly would've noticed me, even if I just as much as buckled my legs together."

                    show her_vibrators_public eyes_closed as xray_child
                    show her_vibrators_public_proxy eyes_closed as xray_overlay

                    her "So I was just left standing there, trying to calm myself, waiting for them to finish their game."

                    show her_vibrators_public mouth_lip_bite as xray_child
                    show her_vibrators_public_proxy mouth_lip_bite as xray_overlay

                    her "I don't think I've ever had to endure anything as agonizing..."
                    her "Never in my life have I been so close to a point where I would happily throw myself at the first person to promise me a release..."
                    her "Never ever been so close..."
                    her @ cheeks blush "...{w=0.4} *Ahem*." ("angry", "squint", "base", "R")

                    stop background fadeout 2
                    stop music fadeout 1.0
                    hide vibrator_interface
                    hide cg
                    with fade
                    call weather_sound

                    gen "..." ("base", xpos="far_left", ypos="head")

                    if not states.her.ev.vibrators.public_stage == 2:
                        gen "No wonder you went off like a fire hose the moment you got in here." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("disgust", "narrow", "base", "down")
                    else:
                        gen "You know, I could flip that switch right now..." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Really?" ("open", "base", "base", "mid")
                        gen "Unfortunately it's not part of today's agenda, but maybe next time." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("annoyed", "base", "base", "R")

                    gen "Very well [name_hermione_genie], I think that shall do for today." ("base", xpos="far_left", ypos="head")
                else:
                    # Strength was set to high before
                    #Hermione is denied an orgasm, the boys doesn't notice.
                    #Vagina is wet

                    show her_vibrators_public eyes_clenched mouth_open as xray_child
                    show her_vibrators_public_proxy eyes_clenched mouth_open as xray_overlay

                    her "Yes, as I was just about to hit my limit--"

                    show her_vibrators_public eyebrows_surprised eyes_crossed as xray_child
                    show her_vibrators_public_proxy eyebrows_surprised eyes_crossed as xray_overlay

                    her "The intensity went down a bit..."

                    show her_vibrators_public eyebrows_worried eyes_ahegao mouth_neutral as xray_child
                    show her_vibrators_public_proxy eyebrows_worried eyes_ahegao mouth_neutral as xray_overlay

                    her "I was ready to go over the edge right then and there, but when the intensity went down, it prolonged that feeling..."
                    gen "It's called \"edging\"."
                    her "I know what it's called..."
                    her "So, I was forced to keep this feeling going..."

                    show her_vibrators_public eyes_closed mouth_lip_bite as xray_child
                    show her_vibrators_public_proxy eyes_closed mouth_lip_bite as xray_overlay

                    her "To keep... \"Edging\"..."
                    gen "*heh-heh*..."

                    #Wet down legs
                    show her_vibrators_public wetness_legs as xray_child
                    show her_vibrators_public_proxy wetness_legs as xray_overlay

                    her "That's when...{w=0.4} Well...{w=0.4} I felt this... intense wetness flowing down my legs..."
                    her "And I must mention, it is rather unusual for me to--"
                    gen "Right, you're one of those \"Rinse and repeat\" kind of girls."
                    her "*Hmph*... And what makes you say that?"
                    gen "Fine, you're a kinky girl who loves being edged and denied an orgasm."
                    her "That's not--"
                    gen "Come on, just admit it..."
                    her "Why would I...--"
                    gen "Just say it...{w=0.4} I'll even give you some points if you do."
                    her "I--{w=0.4} I am a kinky girl..."
                    gen "\"That\"..."
                    her "Who loves being edged..."
                    her "...and denied an orgasm..."
                    gen "Ten points to Gryffindor!"

                    $ gryffindor += 10

                    her "..."
                    gen "What happened next?"

                    #shaking legs
                    show her_vibrators_public mouth_open effects_shaky_legs as xray_child
                    show her_vibrators_public_proxy mouth_open effects_shaky_legs as xray_overlay

                    her "What--{w=0.2} Oh...{w=0.4} Well, it didn't stop there... My legs started shaking, and the wetness continued trickling down my legs..."

                    show her_vibrators_public mouth_lip_bite as xray_child
                    show her_vibrators_public_proxy mouth_lip_bite as xray_overlay

                    her "I began to get worried, if it started leaking any more, it would soon form a puddle, then I'm sure Harry and Ron would notice..."
                    her "There was nothing I could do about it either. The vibrators were still vibrating and edging me, it was really difficult to keep myself from giving in completely."

                    show her_vibrators_public eyes_ahegao as xray_child
                    show her_vibrators_public_proxy eyes_ahegao as xray_overlay

                    her @ cheeks blush "And just as I thought I wouldn't be able to hold it in anymore--" ("angry", "base", "base", "mid")

                    play sound "sounds/click4.ogg"
                    stop background
                    stop background
                    stop music fadeout 1.0
                    hide vibrator_interface
                    hide cg
                    with fade
                    call weather_sound

                    her @ cheeks blush "--The vibrators stopped..." ("angry", "narrow", "base", "down")
                    gen "Denied! I bet you loved that!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "I did not!" ("mad", "squint", "annoyed", "mid")
                    gen "You just admitted to liking it like a minute ago, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "You know, I only said that because you told me to!" ("angry", "closed", "annoyed", "mid") # Stutters because she does not believe her own words.

                    if not states.her.ev.vibrators.public_stage == 2:
                        gen "Yeah, right!" ("base", xpos="far_left", ypos="head")
                        gen "Even when I turned the vibrators on when you were on your way here--" ("base", xpos="far_left", ypos="head")
                        gen "--which was totally on purpose, by the way--" ("base", xpos="far_left", ypos="head")
                        gen "--You kept holding it in, walking from the courtyard all the way up and to my office!" ("base", xpos="far_left", ypos="head")
                        gen "And now you're telling me, that you weren't enjoying it? You launched off like a nuclear missile as you came in, {i}AND{/i} in here!" ("base", xpos="far_left", ypos="head") # Pun
                        her @ cheeks blush "That has nothing to do with my supposed denial kink--" ("soft", "narrow", "annoyed", "R")
                        gen "Then next time I expect you to not hold back!" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Fine! I won't!" ("angry", "narrow", "annoyed", "mid")
                        gen "Great!" ("grin", xpos="far_left", ypos="head")
                        her @ cheeks blush "...{w=0.6}{nw}" ("base", "narrow", "base", "R")
                        her @ cheeks blush "...{fast} Wait, hold on..." ("angry", "wide", "base", "mid")
                        gen "What is it now?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "*Hmph*...{w=0.4} Nothing..." ("angry", "narrow", "annoyed", "R")
                        gen "Good, then I think that shall do for today [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "" ("annoyed", "narrow", "base", "R")
                        call ctc
                    else:
                        gen "If that's the case, why are your legs shaking?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "What?!" ("angry", "narrow", "annoyed", "down") #looks down
                        gen "Got you." ("grin", xpos="far_left", ypos="head")
                        her @ cheeks blush "*Hmph*..." ("annoyed", "narrow", "annoyed", "R")
                        gen "Anyway, you can go finish yourself off in your dorms, I won't deny you any further..." ("base", xpos="far_left", ypos="head")
                        gen "Unless that's what you're into..." ("grin", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("annoyed", "narrow", "base", "down")

                $ _vibrator_last = "medium"

            "\"(I Turned it to the low setting.)\""if not _vibrator_low:
                $ _vibrator_low = True

                show vibrator_interface vibration_low low_disabled

                play sound "sounds/click4.ogg"
                play background "sounds/vibrator_low.ogg"

                # Hermione does not reach orgasm.
                if _vibrator_last == "medium":
                    # Strength was set to medium before. (worst ending)
                    # Vagina is not wet.

                    show her_vibrators_public eyebrows_neutral eyes_forward mouth_neutral as xray_child
                    show her_vibrators_public_proxy eyebrows_neutral eyes_forward mouth_neutral as xray_overlay

                    her "Yes, compared to the start, it almost felt as if they had almost stopped completely."

                    show her_vibrators_public eyes_down mouth_open as xray_child
                    show her_vibrators_public_proxy eyes_down mouth_open as xray_overlay

                    her "I was even able to keep up a conversation with my friends, right until the very end of their game."
                    gen "You were talking with your friends, with the vibrators still on?!"
                    her "Yes?"
                    gen "I thought you'd be ashamed of such a thing."
                    her "It barely tickled!"
                    gen "If you say so..."

                    stop background fadeout 2
                    stop music fadeout 1.0
                    hide vibrator_interface
                    hide cg
                    with fade
                    call weather_sound

                    gen "Well then...{w=0.4} I suppose that shall do for now, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                else: 
                    # Strength was set to high before. (second to worst ending)
                    # Vagina is wet.

                    show her_vibrators_public eyebrows_neutral eyes_closed mouth_open as xray_child
                    show her_vibrators_public_proxy eyebrows_neutral eyes_closed mouth_open as xray_overlay

                    her "Yes, at last the intensity went down, and I let out a sigh of relief."

                    show her_vibrators_public eyes_sad mouth_neutral as xray_child
                    show her_vibrators_public_proxy eyes_sad mouth_neutral as xray_overlay

                    her "The fact that I got excited in front of my friends was bad enough. I am not sure what I would have done if I had gone over the edge in front of them..."
                    gen "(Damn, I hoped she would've been done by then...)"

                    show her_vibrators_public eyes_left mouth_open as xray_child
                    show her_vibrators_public_proxy eyes_left mouth_open as xray_overlay

                    her "The gentle vibrations carried on for quite a while, and didn't stop until the game was almost over."
                    her @ cheeks blush "If I was alone and in a private place, then maybe that would've been enough to push me over, but luckily for me, I managed to keep it together in front of the boys..." ("open", "narrow", "base", "down")

                    stop background fadeout 2
                    stop background fadeout 2
                    stop music fadeout 1.0
                    hide vibrator_interface
                    hide cg
                    with fade
                    call weather_sound

                    if not states.her.ev.vibrators.public_stage == 2:
                        her @ cheeks blush "Of course, it only lasted until you turned them back on while I was on my way here..." ("soft", "narrow", "base", "down")
                        gen "What can I say, I like to keep you on your toes." ("grin", xpos="far_left", ypos="head")
                    else:
                        her @ cheeks blush "Even though you did turn them off a while ago, I can almost feel the vibrations..." ("soft", "narrow", "base", "down")
                        gen "Oh don't worry, they will be back sooner or later, so be ready!" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Sooner or later--{w=0.2} A-Alright..." ("angry", "narrow", "base", "mid")
                    gen "Alas, I think that does it for today." ("base", xpos="far_left", ypos="head")

                $ _vibrator_last = "low"

        # End section
        # Resets CG variables
        hide xray_child
        hide xray_overlay

        if not her_outfit_vibrators.unlocked:
            her @ cheeks blush "What about the... *Ehm*..." ("angry", "narrow", "base", "down")
            gen "Oh, the vibrators? You can keep them." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you..." ("open", "narrow", "base", "down") #Looks right

            hide vibrators_floor
            with d5

            call unlock_clothing("Congratulations! You have unlocked a new outfit!", her_outfit_vibrators)

            her @ cheeks blush "So... How do these things work, exactly? Do I need to charge them or...?" ("open", "squint", "base", "mid")
            gen "... These are magical items, they use magic, not volts." ("base", xpos="far_left", ypos="head")
            gen "(Unless magic volts are a thing?)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh right..." ("angry", "narrow", "base", "down")
            her @ cheeks blush "Good night then, [name_genie_hermione]..." ("open", "squint", "base", "R")
            gen "Farewell and enjoy yourself, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("base", "closed", "base", "mid") #looks down
        else:
            her @ cheeks blush "I can still keep these, right?" ("open", "squint", "base", "mid")
            gen "Of course, as long as you don't mind using them in front of me sometimes." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "No problem..." ("angry", "narrow", "base", "down")

            hide vibrators_floor
            with d5

            her @ cheeks blush "Good night then [name_genie_hermione]..." ("open", "squint", "base", "R")
            gen "Good night, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        $ states.her.ev.vibrators.public_stage = 2
    else:

        label .low_tier:

        call her_walk("mid", "base", action="enter")

        gen "There you are... Where have you been?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "narrow", "base", "stare", xpos="base", ypos="base") #Staring into space
        gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "narrow", "base", "stare")
        gen "You're looking a bit shaken up, did something happen?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I knew this was going to be a mistake... Why would I ever agree to something like this..." ("open", "narrow", "base", "stare") #still staring into space
        gen "Did you get caught?" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "I--{w=0.2} I don't know... Maybe you could tell me." ("disgust", "closed", "base", "mid")
        gen "Did you turn on the vibrators during class, like I requested?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes..." ("disgust", "narrow", "base", "down")
        gen "Tell me what happened." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well, after I exited your office..." ("open", "narrow", "base", "down")
        her @ cheeks blush "I was racking my brain trying to decide when would be the best time to use the vibrators." ("disgust", "narrow", "base", "down")

        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("top")
        with d3

        her @ cheeks blush "I finally decided to set focus on the final lesson for today, \"Muggle Studies\", as that class would be the least likely to cause me any trouble." ("open", "narrow", "base", "down")

        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bottom")
        with d3

        her @ cheeks blush "We are currently studying Muggle Music you see, so it's not really something I need to pay much attention to since I am already familiar with the subject." ("soft", "narrow", "base", "down")

        $ hermione.unequip("accessory0", "accessory1")
        $ hermione.equip([her_panties_base1, her_bra_base1])

        pause .8
        play sound "sounds/drop_plastic.ogg"
        show vibrators_floor at Transform(xpos=536, ypos=413, zoom=0.5)
        with d5

        gen "Always thinking about your academics I see." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Of course..." ("open", "closed", "base", "mid")
        her @ cheeks blush "Although unfortunately for me, I was one of the last students to enter the class, and as usual, the Slytherins took all the spots in the back and I ended up sitting right at the front of the class." ("open", "base", "worried", "R")
        her @ cheeks blush "As you can imagine, it made things much more difficult as I was in view of everyone behind me." ("open", "closed", "worried", "mid")
        her @ cheeks blush "But it was the last lesson for today, so I had to go with my plan..." ("open", "narrow", "base", "R")
        gen "Good to hear, edging yourself for an entire day can't be that healthy..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I meant I didn't want to forfeit the points!" ("open", "narrow", "annoyed", "mid")
        gen "Right... The points... Speaking of, why don't you get to it?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Tsk*..." ("disgust", "narrow", "base", "R") #closed eyes in frustration
        her @ cheeks blush "So, I was trying to time the vibrations with the music--" ("open", "closed", "annoyed", "mid")
        gen "Hold on...{w=0.4} You were doing what?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "You asked me to get to the point... Isn't that what you asked?" ("open", "narrow", "annoyed", "mid")
        gen "Yes, but I only said that because I never imagined that your plan would involve some kind of weird sexual rhythm game." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I didn't want anyone to hear, so what choice did I have?" ("open", "narrow", "annoyed", "mid")
        gen "(Surely there must be some kind of silencing charm...)" ("base", xpos="far_left", ypos="head")
        gen "So, how did this plan of yours work out?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Not as well as I had hoped..." ("annoyed", "narrow", "annoyed", "R")
        her @ cheeks blush "Turning it off and on produced a fair amount of sound, probably more than if I had just left it running..." ("open", "narrow", "annoyed", "down")
        her @ cheeks blush "But in the moment I didn't realise that, so there I was, trying my best to synchronize it with the music--" ("open", "closed", "angry", "mid")
        her @ cheeks blush "And...{w=0.4} Well..." ("annoyed", "narrow", "base", "down")
        gen "You reached the climax before the chorus?" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "That's one way to say it..." ("angry", "narrow", "base", "down")
        gen "The power of music..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "So, anyway--" ("annoyed", "closed", "base", "mid")
        gen "I'm not buying it." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione]?" ("angry", "base", "base", "mid")
        gen "Turning it off and on, causing more sound... Poppycock." ("base", xpos="far_left", ypos="head")
        gen "Unless you're talking about sounds of pleasure, every time you turned it back on, of course." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "That is not it at all!" ("angry", "base", "annoyed", "mid")
        gen "No need to be ashamed, [name_hermione_genie]... It's a perfectly natural reaction." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Hmph*..." ("disgust", "narrow", "annoyed", "R")
        gen "Let me guess..." ("base", xpos="far_left", ypos="head")
        gen "Somebody spotted the only girl who excited about the music?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Perhaps... At least, one of the Slytherins sensed something's amiss with me..." ("angry", "narrow", "base", "R")
        gen "With your back turned?" ("base", xpos="far_left", ypos="head")
        gen "You must've been moving a lot... Which setting did you turn the vibrators to?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I wasn't moving though!" ("angry", "base", "base", "mid") #Ignored
        gen "What did you do to get their attention then?" ("base", xpos="far_left", ypos="head")
        gen "Don't tell me you got the seat wet?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I--{w=0.2} I don't know!" ("angry", "base", "worried", "R")
        gen "I'll take that as a yes..." ("base", xpos="far_left", ypos="head")
        gen "So why do you think he had paid any attention to you?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "{b}She{/b}!!" ("disgust", "squint", "base", "mid")
        her @ cheeks blush "I was leaving the classroom and {b}she{/b} stood in the doorway, giving me the smuggest smirk one can make." ("open", "base", "annoyed", "R")
        her @ cheeks blush "It was not the usual look of disdain that I expect from a Slytherin, no, it was something else..." ("normal", "narrow", "annoyed", "R")
        gen "Sounds like a win-win situation to me!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Are you mad? A Slytherin catching me after--{w=0.2} Doing \"that\" in public?" ("angry", "base", "annoyed", "mid")
        gen "You said it yourself, she didn't look at you with disdain." ("base", xpos="far_left", ypos="head")
        gen "Maybe she even liked what she saw..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I didn't need her approval, especially from a Slytherin!" ("disgust", "base", "annoyed", "mid")
        gen "Sounds to me like you're being unfairly presumptuous, and to make things worse, you were the one judging her for things out of her control, like her house, she wasn't judging you for your actions..." ("base", xpos="far_left", ypos="head")
        gen "Even though you had full control over them, didn't you, [name_hermione_genie]." ("base", xpos="far_left", ypos="head") # Genie means her actions, Hermione thinks he means control over the vibrators in a literal sense
        her @ cheeks blush "I..." ("angry", "base", "base", "mid") # Oh fuck, I can't believe you've done this
        her @ cheeks blush "I'm going to need a moment..." ("disgust", "closed", "base", "R")
        gen "Sure thing." ("base", xpos="far_left", ypos="head")

        show screen blkfade
        with d3
        pause 1

        $ hermione.equip(her_outfit_default)

        hide screen blkfade
        with d3

        # End section
        if states.her.tier < 5: #Receiving points, doesn't unlock vibrators
            $ gryffindor += current_payout
            gen "{number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you..." ("soft", "base", "base", "mid")
            her @ cheeks blush "..." ("normal", "narrow", "base", "down")

            hide vibrators_floor
            with d5

            gen "You can keep the--" ("base", xpos="far_left", ypos="head")

            call her_walk("desk", "base")
            show vibrators_floor at Transform(xpos=340, ypos=355, zoom=0.5)
            with d5

            her @ cheeks blush "No, thanks..." ("open", "squint", "base", "R")
            gen "Or I could just keep them for safekeeping, for now..." ("base", xpos="far_left", ypos="head")

            hide vibrators_floor
            with d3
        else: #Not getting points, unlocks vibrators
            if not her_outfit_vibrators.unlocked:
                gen "You can take those vibrators with you if you want." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("normal", "squint", "base", "R") #Looks right
                her @ cheeks blush "Thank you..." ("open", "squint", "base", "R")

                hide vibrators_floor
                with d5
                call unlock_clothing("Congratulations! You have unlocked a new outfit!", her_outfit_vibrators)

                gen "Don't mention it." ("base", xpos="far_left", ypos="head")
            else:
                gen "Don't forget your vibrators." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Right..." ("open", "narrow", "base", "down")

                hide vibrators_floor
                with d5
        $ states.her.ev.vibrators.public_stage = 1

    call her_walk(action="leave")

    $ states.her.ev.vibrators.public_complete = True
    $ hermione.equip(her_outfit_last)

    jump end_hermione_event
