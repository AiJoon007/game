
# Temp flag used to test against clothed character state, it is reset at the end of the event.
default _no_clothes = False

label potion_ass_make:

    call give_reward("You have successfully created a new potion!", ass_potion_ITEM)

    gen "There we go." ("base", xpos="far_left", ypos="head")
    play sound "sounds/sniff.ogg"
    gen "Smells pretty good!" ("base", xpos="far_left", ypos="head")
    gen "I bet Hermione will love this one." ("base", xpos="far_left", ypos="head")
    return

label her_potion_ass_give:

    if hermione.is_worn("robe"):
        gen "Before we begin... Why don't you take those robes off and make yourself comfortable." ("base", xpos="far_left", ypos="head")
        her "Alright..." ("soft", "squint", "base", "mid")
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")
        with d3
        gen "Now then..." ("base", xpos="far_left", ypos="head")
    else:
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "Yes [name_genie_hermione]?" ("open", "base", "base", "mid")

    $ current_payout = 20

    gen "I've got a potion that I'd like you to try." ("base", xpos="far_left", ypos="head")
    gen "For some house points of course..." ("base", xpos="far_left", ypos="head")
    nar "You take out the potion and hand it to Hermione."
    call her_chibi("hold_potion","mid","base")
    with d3

    if not states.her.ev.potions.ass_expand_drank:
        her "A potion?" ("soft", "squint", "base", "mid")
        gen "Yep, a pretty powerful one at that." ("base", xpos="far_left", ypos="head")
        if states.her.level < 19:
            her "Is it dangerous?" ("disgust", "squint", "worried", "mid")
            gen "Of course not!" ("base", xpos="far_left", ypos="head")
            her "*Hmm*..." ("normal", "narrow", "base", "down")
            her "If you say so." ("angry", "closed", "worried", "mid")
            gen "So you'll drink it?" ("base", xpos="far_left", ypos="head")
            her "I suppose... As long as you pay me." ("open", "narrow", "base", "down")
            gen "Naturally..." ("base", xpos="far_left", ypos="head")
            nar "Hermione takes a quizzical sniff of the potion before bringing it to her mouth."
        else:
            her @ cheeks blush "*Hmm*... Powerful you say..." ("base", "narrow", "base", "down")
            her "Alright then, let's have a taste." ("grin", "closed", "base", "mid")
            gen "Great!" ("base", xpos="far_left", ypos="head")
            her "" ("grin", "base", "base", "mid")
            gen "Here you go!" ("base", xpos="far_left", ypos="head")
            nar "Hermione takes a quick sniff of the potion before bringing it to her mouth..."

        call her_chibi("sniff_potion","mid","base")
        pause 0.2
        play sound "sounds/sniff.ogg"
        pause 0.6
        call her_chibi("hold_potion","mid","base")

        gen "Bottoms up!" ("base", xpos="far_left", ypos="head")
    else: #Drank
        her "Another one? How do you have time to make these?" ("open", "squint", "base", "mid")
        gen "Potion making is easy when you've been practising for as long as I have." ("base", xpos="far_left", ypos="head")
        her "I see..." ("soft", "squint", "base", "mid")
        gen "Go on, I think you'll enjoy this one." ("base", xpos="far_left", ypos="head")
        gen "Just have a whiff and see for yourself." ("base", xpos="far_left", ypos="head")
        nar "Hermione takes a quick sniff of the potion."

        call her_chibi("sniff_potion","mid","base")
        pause 0.2
        play sound "sounds/sniff.ogg"
        pause 0.6
        call her_chibi("hold_potion","mid","base")

        her @ cheeks blush "Another butt expansion potion?" ("open", "squint", "base", "R") #Neutral face
        gen "That's right." ("base", xpos="far_left", ypos="head")
        if states.her.level < 19:
            her @ cheeks blush "My butt looked ridiculous last time..." ("annoyed", "narrow", "base", "mid")
            if states.her.ev.potions.ass_expand_complete:
                gen "Well, that's a matter of opinion, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            else:
                gen "I'm sure it looked fine..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*..." ("normal", "narrow", "base", "down")
            gen "You'll still drink it right?" ("base", xpos="far_left", ypos="head")
            her "I guess..." ("open", "narrow", "base", "down")
            gen "Great!" ("base", xpos="far_left", ypos="head")
        else: #19+
            her "I mean... I guess it wasn't so bad." ("base", "narrow", "base", "down")
        gen "Enjoy!" ("base", xpos="far_left", ypos="head")
        nar "Hermione takes a last glance at the potion and brings it up to her mouth."

    her "Here I go..." ("angry", "closed", "base", "mid")


    call her_chibi("drink_potion","mid","base")
    pause 0.6
    play sound "sounds/gulp.ogg"
    pause 0.8
    call her_chibi("stand","mid","base")
    nar "Hermione drinks the potion with a series of gulps."


    if not states.her.ev.potions.ass_expand_drank:
        if states.her.level < 19:
            her "That didn't taste so bad!" ("base", "squint", "base", "mid")
            her "What was it?" ("base", "base", "base", "mid")
        else: #19+
            her "*Ahhh*... That was tasted great! What was it?" ("base", "squint", "base", "mid")
        gen "The effects should become apparent soon enough." ("base", xpos="far_left", ypos="head")
        her "Alright." ("open", "base", "base", "R")

    else: #Drank
        her "*Hmm*... This potion does taste pretty good..." ("base", "closed", "base", "mid")

    gen "Now, then..." ("base", xpos="far_left", ypos="head")

    #Send her to class, or
    #Tell her to take off her bottoms/Wait and see what happens
    menu:
        "-Send her to class-":
            if not states.her.ev.potions.ass_expand_drank:
                gen "You should probably head back to class for now..." ("base", xpos="far_left", ypos="head")
                her "To class, but what about the--" ("angry", "squint", "base", "mid")
                nar "Hermione goes white as she starts to feel her body churn."
                her "*Hngh*!" ("disgust", "wide", "worried", "stare")
                gen "Something wrong?" ("base", xpos="far_left", ypos="head")
                her "What-- What's the intended effect of this potion [name_genie_hermione]?" ("angry", "squint", "base", "mid")
                gen "Let's just say it's meant to distribute your assets a little bit differently." ("base", xpos="far_left", ypos="head")
                her "My--" ("angry", "squint", "worried", "mid")
                play sound "sounds/slap.ogg"
                nar "Hermione's body suddenly jolts forward as if someone slapped her from behind."
                her "Ouch!" ("scream", "happy", "base", "stare")
                her "Something slapped me!" ("mad", "base", "base", "mid")
                her "Is it supposed to do this?" ("angry", "happy", "base", "mid")
                gen "I'm sure it's fine, just go back to class for now." ("base", xpos="far_left", ypos="head")
            elif states.her.ev.potions.ass_expand_public_complete:
                gen "You should probably head back to class for now..." ("base", xpos="far_left", ypos="head")
            elif states.her.ev.potions.ass_expand_complete:
                her @ cheeks blush "So... I assume you want to--" ("open", "base", "base", "R")
                her @ cheeks blush "I mean, am I to receive another massage?" ("soft", "closed", "base", "mid")
                gen "Not today [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                her "Then what--" ("clench", "base", "base", "mid")
                nar "Hermione jumps on the spot slightly as the potion begins taking effect."
                her "Ouch!" ("angry", "happyCl", "worried", "mid")
                gen "No... I think this time I'd rather you head back to class." ("base", xpos="far_left", ypos="head")
            else: #Drank but failed public variant before
                gen "I'd like you to go to class this time..." ("base", xpos="far_left", ypos="head")

            if states.her.status.public_stripping: ## Triggers public return event ##

                if not states.her.ev.potions.ass_expand_drank:
                    her "Alright..." ("angry", "squint", "base", "R")
                    gen "Let me know how it went!" ("base", xpos="far_left", ypos="head")
                    her "Yes, [name_genie_hermione]..." ("angry", "narrow", "base", "down")
                    her "See you later then." ("angry", "narrow", "base", "R")

                else:
                    her @ cheeks blush "You want me to..." ("open", "base", "base", "mid")
                    gen "Go to class, yes..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Alright..." ("open", "squint", "base", "R")
                    if states.her.ev.potions.ass_expand_public_complete:
                        her @ cheeks blush "I suppose I've already done it before... How bad could it be?" ("open", "closed", "base", "mid")
                        gen "That's the spirit." ("base", xpos="far_left", ypos="head")
                    gen "Make sure to tell me how it went..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Okay." ("open", "squint", "base", "mid")

                hide hermione_main
                with d3
                pause .4
                call her_walk("door")

                play sound "sounds/slap_02.ogg"
                her @ cheeks blush "Oooh!" ("angry", "base", "base", "stare", flip=True)

                #Hermione leaves
                call her_walk(action="leave")

                # Set Return event
                $ ass_potion_ITEM.set_active("hermione")

                jump end_hermione_event

            else: ## Doesn't trigger public return event ##
                if not states.her.ev.potions.ass_expand_drank:
                    her "*Ehm*... I'm not sure I--" ("angry", "squint", "worried", "mid")
                    play sound "sounds/slap.ogg"
                    her "" ("clench", "wide", "base", "mid")
                    nar "Another jolt goes through Hermione's body as she jumps on the spot."
                    her "I-- I'm sorry [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid")
                    her @ cheeks blush "If this potion is doing what I think it's--" ("open", "happyCl", "worried", "mid")
                    play sound "sounds/slap.ogg"
                    her @ cheeks blush "Ow!" ("angry", "wide", "worried", "stare")
                    gen "Alright fine... You don't have to go to class for today..." ("base", xpos="far_left", ypos="head")
                    gen "{number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")

                    $ gryffindor += current_payout
                    her @ cheeks blush "Thank you..." ("angry", "happyCl", "base", "mid")

                    call her_walk(action="leave")

                    play sound "sounds/boing02.ogg"
                    pause .2
                    her "Merlin's beard!"
                    gen "..." ("base", xpos="far_left", ypos="head")

                    $ states.her.ev.potions.ass_expand_drank = True
                    jump end_hermione_event
                else:
                    if states.her.level < 19:
                        her "You want me to what?!" ("angry", "squint", "worried", "mid")
                        gen "Go to class!" ("base", xpos="far_left", ypos="head")
                        gen "Isn't that what you're supposed to do in school?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Not when you've just drunk a potion like this!" ("clench", "squint", "worried", "mid")
                        gen "I suppose you might not fit on the chairs that well..." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "That is not the reason..." ("annoyed", "narrow", "annoyed", "mid")
                        her @ cheeks blush "I can't believe you're asking me to expose myself like this..." ("angry", "narrow", "base", "R")
                        her @ cheeks blush "I'll have my points--" ("angry", "closed", "annoyed", "mid")
                        nar "Hermione's body jolts once more."
                        play sound "sounds/slap.ogg"
                        her "Ouch!" ("scream", "wide", "base", "stare")
                    else:
                        her @ cheeks blush "You want me to go to class when--" ("angry", "narrow", "base", "down")
                        nar "Hermione's body jolts once more."
                        play sound "sounds/slap.ogg"
                        her @ cheeks blush "*Ah*..." ("soft", "narrow", "base", "up")
                        her @ cheeks blush "" ("angry", "narrow", "base", "mid") #blush
                        gen "I think your classmates would appreciate the view." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "I..." ("disgust", "narrow", "base", "down")
                        play sound "sounds/slap.ogg"
                        her @ cheeks blush "*Ah*..." ("open", "happyCl", "base", "mid")
                        her @ cheeks blush "No... I'm sorry but I'm not going to let them see me like that..." ("angry", "narrow", "base", "mid")
                        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

                    gen "Very well [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    gen "{number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")

                    $ gryffindor += current_payout

                    her @ cheeks blush "Thank you..." ("angry", "closed", "base", "mid")
                    gen "Until next time." ("base", xpos="far_left", ypos="head")

                    call her_walk(action="leave")
                    $ states.her.ev.potions.ass_expand_drank = True
                    jump end_hermione_event

        "-Tell her to take off her clothes-" if hermione.is_any_worn("top", "bra", "bottom", "panties"):
            $ _no_clothes = True #Took off clothing (reset at end)

            gen "Why don't you take off your clothes for me?" ("base", xpos="far_left", ypos="head")
            if states.her.level < 15:
                her @ cheeks blush "You want me to take off my..." ("open", "narrow", "base", "down")
                gen "Your clothes, yes..." ("base", xpos="far_left", ypos="head")
            else:
                her @ cheeks blush "So that's how it is, is it..." ("open", "squint", "base", "R")
                her @ cheeks blush "You should really tell me these things up front [name_genie_hermione]..." ("open", "closed", "base", "down")
                her @ cheeks blush "But I suppose I could do that, even though I was only meant to drink the potion..." ("base", "closed", "base", "mid")

        "-Wait and see what happens-" if not hermione.is_any_worn("top", "bra", "bottom", "panties"):

            gen "Just stand right there for a moment will you?" ("base", xpos="far_left", ypos="head")
            her "Doing this again are we?" ("open", "closed", "base", "mid")
            gen "Just waiting for the potion to kick in..." ("base", xpos="far_left", ypos="head")
            her "Right..." ("soft", "squint", "base", "R")

    if not states.her.ev.potions.ass_expand_drank:
        her @ cheeks blush "Could you at least give me a hint of what it's supposed to do?" ("soft", "squint", "base", "mid")
        gen "Well that wouldn't be very fun would it..." ("base", xpos="far_left", ypos="head")
        gen "I'm sure you'll feel it any minute now." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Feel? What do you mean by--" ("angry", "base", "worried", "mid")
        nar "Hermione goes white as she starts to feel her body churn."
        her "What's going on?!" ("disgust", "wide", "base", "stare")
        her "It's as if my insides are moving!" ("disgust", "happy", "base", "stare")
        if states.her.level < 19:
            her "My butt... It's--" ("clench", "squint", "base", "down")
            play sound "sounds/slap.ogg"
            if hermione.is_any_worn("top", "bottom", "panties"):
                nar "Hermione suddenly jolts forward as if she were hit by something on her butt."
                her @ cheeks blush "Ouch!" ("mad", "happyCl", "worried", "stare")
                her @ cheeks blush "S--{w=0.2} Something's happening to it, [name_genie_hermione]!" ("clench", "happy", "worried", "down")
                gen "You'd probably want to take off your clothes right about now..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "My--{w=0.2} You've only paid me to drink the potion, why would I--" ("angry", "closed", "worried", "mid")
                gen "Trust me, it's for your own good..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "For my...{w=0.6}{nw}" ("annoyed", "narrow", "worried", "down") #wide eyed
                her @ cheeks blush "For my...{fast} Wait, surely you haven't..." ("clench", "base", "worried", "stare") #wide eyed

                if hermione.is_any_worn("top", "bra"):
                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.strip("top", "bra")
                    pause .5

                her @ cheeks blush "" ("clench", "narrow", "worried", "down")
                gen "[name_hermione_genie]! Stripping in your headmaster's office, how indecent!" ("grin", xpos="far_left", ypos="head")

                if hermione.is_any_worn("bottom", "panties"):
                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.strip("bottom", "panties")

                $ hermione.strip("clothes")


                gen "Just from a potion that's meant to spank you a little!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Wait, so it's not going to--" ("disgust", "squint", "worried", "down")
            else: #Not wearing top, bottom or panties
                nar "With a smacking sound, Hermione jumps on the spot as her bare cheeks are slapped hard."
                her @ cheeks blush "{size=+4}Ouch!!!{/size}" ("angry", "happyCl", "base", "mid")
                her @ cheeks blush "What was that?" ("angry", "squint", "base", "mid")

                if hermione.is_any_worn("clothes"):
                    nar "Hermione goes over her belongings, trying to find the source."

                    if hermione.is_any_worn("accessory", "stockings", "garterbelt"):
                        play sound "sounds/cloth_sound3.ogg"
                        $ hermione.strip("accessory", "stockings", "garterbelt")
                        call ctc

                    play sound "sounds/slap.ogg"

                    her @ cheeks blush "{size=+4}OW!!!{/size}" ("angry", "happyCl", "base", "mid")
                    her @ cheeks blush "Where is that coming from??" ("angry", "squint", "base", "mid")

                $ hermione.strip("clothes")

                gen "It appears the potion is working." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "It-- Hold on, is it--" ("angry", "wide", "base", "mid")

            $ hermione.equip(her_hips_ass1)
            play sound "sounds/boing05.ogg"
            with d3

            her @ cheeks blush "I knew it..." ("disgust", "narrow", "base", "down")
            gen "That's weird... Must've brewed the potion wrong..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right... As if you didn't know this was going to happen." ("open", "narrow", "annoyed", "R")
            gen "I assure you I had no idea [name_hermione_genie], it was only meant to spank you a little." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Then how come it's--" ("soft", "narrow", "annoyed", "down")

            $ hermione.equip(her_hips_ass2)
            play sound "sounds/boing05.ogg"
            with d3

            her @ cheeks blush "[name_genie_hermione]!" ("angry", "base", "worried", "down")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It did it again!" ("disgust", "happyCl", "worried", "mid")
            gen "Well, it is an untested potion to be fair... You'll have to expect some side effects." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Side effects? But you assured me this potion was--" ("clench", "narrow", "worried", "down")

            $ hermione.equip(her_hips_ass3)
            play sound "sounds/boing04.ogg"
            with d3

            her @ cheeks blush "Merlin's beard!" ("disgust", "wide", "base", "down")
            gen "Nice..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You told me this potion was safe!" ("scream", "happyCl", "annoyed", "mid")
            gen "I said it wasn't dangerous." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "How am I supposed to sit down with this?" ("angry", "base", "annoyed", "mid")
            gen "I'm sure you'll manage." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmph*..." ("annoyed", "narrow", "annoyed", "R")
            her @ cheeks blush "" ("annoyed", "narrow", "annoyed", "down")
            nar "Hermione glances down at her new exterior in disbelief."
        else: # 19+
            her @ cheeks blush "And my ass, it feels so... Good." ("base", "narrow", "base", "up")
            nar "You start to notice Hermione's ass jiggling slightly."
            her @ cheeks blush "Something is happening with my body, [name_genie_hermione]!" ("grin", "narrow", "base", "down")
            play sound "sounds/slap.ogg"
            her @ cheeks blush "*Ah*..." ("open_tongue", "narrow", "base", "up")
            nar "Hermione jolts forward as if her ass were spanked by an invisible force."
            gen "*Heh-Heh*..." ("grin", xpos="far_left", ypos="head")
            if hermione.is_any_worn("top", "bottom", "panties"):
                gen "You'd probably want to take off your clothes right about now..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "My--{w=0.2} Oh...{w=0.4} I see!" ("angry", "base", "base", "stare")

                if hermione.is_any_worn("top", "bra"):
                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.strip("top", "bra")
                    pause .5

                    gen "Very good..." ("base", xpos="far_left", ypos="head")

                if hermione.is_any_worn("bottom", "panties"):
                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.strip("bottom", "panties")

                $ hermione.strip("clothes")

                her @ cheeks blush "..." ("grin", "narrow", "base", "down")
                her @ cheeks blush "So, when will is it supposed to happen?" ("grin", "wink", "base", "mid")
                gen "When is what supposed to happen?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "When is my butt supposed to grow?" ("grin", "narrow", "base", "mid")
                gen "Your butt? Why, I just wanted to see if I could get you to take your clothes off!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "What, so it won't actually--" ("angry", "base", "base", "down")
            else: #Not wearing top, bottom or panties
                gen "That means the potion is working..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "It's--" ("soft", "squint", "base", "stare")
                her @ cheeks blush "oooooh!!" ("open", "base", "base", "stare") #Realization
                gen "Now you're getting it." ("base", xpos="far_left", ypos="head")
                play sound "sounds/slap.ogg"
                her @ cheeks blush "Ouch!" ("angry", "happyCl", "base", "mid")
                her @ cheeks blush "Why's it doing that?!" ("annoyed", "happyCl", "worried", "mid")

                if hermione.is_any_worn("clothes"):
                    nar "Hermione goes over her belongings, trying to find the source."

                    if hermione.is_any_worn("bra", "accessory", "stockings", "garterbelt"):
                        play sound "sounds/cloth_sound3.ogg"
                        $ hermione.strip("bra", "accessory", "stockings", "garterbelt")
                        call ctc

                    play sound "sounds/slap.ogg"

                    her @ cheeks blush "{size=+4}*Ah*....{/size}" ("open_tongue", "narrow", "base", "up")
                    her @ cheeks blush "What's doing this to me?" ("grin", "narrow", "base", "down")

                $ hermione.strip("clothes")

                gen "I don't... *Err*.... I brewed it to do that!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "You brewed it to-- I thought it was meant to make it--" ("disgust", "narrow", "base", "down")

            $ hermione.equip(her_hips_ass1)
            play sound "sounds/boing05.ogg"
            with d3

            her @ cheeks blush "Grow..." ("open", "base", "base", "down")
            gen "..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "You're almost too predictable sometimes..." ("base", "narrow", "base", "R")
            gen "*Heh-heh*." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Although... I would've thought that you'd make the potion more powerful than this..." ("open", "narrow", "base", "down")
            her @ cheeks blush "Did I not drink enough of it?" ("open", "squint", "base", "mid")
            gen "You underestimate me, girl..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What do you--" ("soft", "narrow", "base", "down")

            $ hermione.equip(her_hips_ass2)
            play sound "sounds/boing05.ogg"
            with d3

            her @ cheeks blush "Whoa!" ("angry", "base", "base", "down")
            gen "There it goes!" ("base", xpos="far_left", ypos="head")
            gen "More like what you expected?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes..." ("soft", "base", "base", "R")
            gen "Well you expected wrong... We're not done yet, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "We're--" ("mad", "base", "base", "mid")

            $ hermione.equip(her_hips_ass3)
            play sound "sounds/boing04.ogg"
            with d3

            her @ cheeks blush "Merlin's beard!" ("scream", "wide", "base", "down")
            her @ cheeks blush "It's humongous!" ("angry", "base", "base", "down")
            gen "There's that Pixar mom look I was going for!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*..." ("soft", "base", "base", "down")
            her @ cheeks blush "I get that the potion is supposed to make my butt larger..." ("soft", "squint", "base", "mid")
            her @ cheeks blush "But why does it suddenly feel so good?" ("soft", "wink", "base", "mid")
            her @ cheeks blush "" ("base", "narrow", "base", "down")
            nar "Hermione looks down at her newly acquired asset, smiling to herself."
            gen "*Hmm*... It's not supposed to, but I guess every case is different." ("base", xpos="far_left", ypos="head")
    else: #Drank
        nar "Hermione's face turns into a grimace as the potion begins taking effect."
        her @ cheeks blush "There's that weird feeling again... Are you sure it's supposed to do this?" ("disgust", "squint", "base", "stare")
        gen "I mean, the potion hasn't even started to take effect yet..." ("base", xpos="far_left", ypos="head")
        if hermione.is_any_worn("top", "bra", "bottom", "panties"):
            gen "Speaking of, you'd probably want to take some of those clothes off right about now." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... Alright..." ("angry", "base", "base", "mid")

            if hermione.is_any_worn("top", "bra"):
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("top", "bra")
                pause .5

                gen "Very good..." ("base", xpos="far_left", ypos="head")

            if hermione.is_any_worn("bottom", "panties"):
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("bottom", "panties")
                pause .5

            $ hermione.strip("clothes")

            gen "Now let's wait and see..." ("base", xpos="far_left", ypos="head")
        else: #Not wearing top, bra, bottom or panties
            her @ cheeks blush "Right..." ("annoyed", "narrow", "base", "down")
            if hermione.is_any_worn("clothes"):
                nar "Hermione goes over her belongings, and begins taking some of them off."

                if hermione.is_any_worn("accessory", "stockings", "garterbelt"):
                    $ hermione.strip("accessory", "stockings", "garterbelt")
                    gen "What are you doing?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Just getting myself more comfortable..." ("angry", "narrow", "base", "down")
                    her @ cheeks blush "Is that okay?" ("angry", "squint", "worried", "mid")
                    gen "I suppose..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Great... My skin gets so sensitive after drinking this..." ("soft", "narrow", "worried", "down")
                else:
                    gen "What are you doing?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I just thought... *Ehm*... My skin got so sensitive before..." ("angry", "squint", "worried", "mid")
                    gen "It's that sensitive?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "*Ehm*... Yes..." ("angry", "narrow", "base", "down")
                    gen "Alright then... Go ahead..." ("base", xpos="far_left", ypos="head")
            $ hermione.strip("clothes")
        her @ cheeks blush "This potion sure is taking its time..." ("angry", "narrow", "base", "down")
        gen "Patience, [name_hermione_genie]... We'll see the effects kicking in soon enough..." ("base", xpos="far_left", ypos="head")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Any minute now..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("normal", "closed", "base", "down")
        her @ cheeks blush "Nothing is--" ("disgust", "narrow", "base", "mid")
        nar "Hermione suddenly jolts forward once more as if she were hit hard on her butt."
        play sound "sounds/slap.ogg"
        if states.her.level < 19:
            her @ cheeks blush "Ouch!" ("clench", "happyCl", "worried", "mid")
            her @ cheeks blush "Why is this potion so aggressive?" ("disgust", "narrow", "annoyed", "down")
            gen "Beats me...{w}..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "narrow", "base", "mid") #pout

            nar "You start to notice Hermione's ass increasing in size."

            $ hermione.equip(her_hips_ass1)
            play sound "sounds/boing05.ogg"
            with d3

            gen "There it goes!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "This feels so strange..." ("disgust", "narrow", "base", "down")
            gen "I think you look great!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "If only this was as big as it's going to--" ("annoyed", "narrow", "worried", "down")

            $ hermione.equip(her_hips_ass2)
            play sound "sounds/boing05.ogg"
            with d3

            her @ cheeks blush "Get..." ("disgust", "narrow", "worried", "down")
            gen "Now you look even greater!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Thanks I suppose..." ("annoyed", "narrow", "base", "R")
            gen "As in there's even more of you now." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I understood what you--" ("disgust", "narrow", "annoyed", "down")

            $ hermione.equip(her_hips_ass3)
            play sound "sounds/boing04.ogg"
            with d3

            her @ cheeks blush "..." ("angry", "narrow", "worried", "down")
            gen "The greatest even!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "My skin feels so tight..." ("angry", "closed", "worried", "mid")
            gen "*Hmm*... Perhaps mixing in some lizard tails would do it..." ("base", xpos="far_left", ypos="head")
            nar "Hermione shifts her posture a little bit as she regains her balance."
            her @ cheeks blush "Ow-ow-ow!" ("angry", "happyCl", "worried", "mid")
        else: # 19+
            her @ cheeks blush "*Ah*!" ("scream", "squint", "base", "stare")
            gen "*Heh-heh*..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It hit me again... Did you mean to make the potion do this?" ("clench", "base", "base", "stare")
            gen "Perhaps." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I figured..." ("angry", "narrow", "base", "R")

            $ hermione.equip(her_hips_ass1)
            play sound "sounds/boing05.ogg"
            with d3

            her @ cheeks blush "Someone of your skill level would surely be able to counteract this sort of side effect." ("angry", "narrow", "base", "R") #Doesn't notice growth
            gen "You call it a side effect, I call it an added bonus." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I guess..." ("base", "closed", "base", "mid")
            her @ cheeks blush "So when is it supposed to start--" ("open", "squint", "base", "mid")

            $ hermione.equip(her_hips_ass2)
            play sound "sounds/boing05.ogg"
            with d3

            her @ cheeks blush "Whoa!" ("open", "wide", "base", "down")
            her @ cheeks blush "How is it so big already?" ("angry", "base", "base", "down")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "It already grew once before." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It did? I didn't even notice..." ("angry", "happy", "base", "mid")
            gen "So... How does it feel?" ("base", xpos="far_left", ypos="head")
            gen "Describe it to me." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It... It feels very nice and cushiony..." ("soft", "base", "base", "down")
            her @ cheeks blush "But I think it got bigger before." ("soft", "wink", "base", "mid")
            gen "Disappointed, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "No, I was just expecting it to--" ("angry", "base", "base", "mid")

            $ hermione.equip(her_hips_ass3)
            play sound "sounds/boing04.ogg"
            with d3

            her @ cheeks blush "" ("grin", "base", "base", "down")
            call ctc
            gen "Or just impatient?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("angry", "narrow", "base", "down")

    ## Ass Grope/Massage Section ##

    if not states.her.ev.potions.ass_expand_complete:
        if states.her.level < 19:
            gen "Now then...{w=0.4} How about a massage?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "A-- A massage?" ("clench", "squint", "worried", "mid")
            gen "Yes, surely you must feel tense after what that potion did to you..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Wait, you want to massage my--" ("angry", "squint", "base", "stare") #wide eyed
            gen "I'll give you another twenty points for it..." ("base", xpos="far_left", ypos="head")

            $ current_payout += 20 #40 total

            her @ cheeks blush "*hmph*..." ("annoyed", "narrow", "annoyed", "L")
            gen "Come on now, surely you must be a little bit curious..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I--" ("angry", "narrow", "base", "L")
            if states.her.level < 15:
                her @ cheeks blush "I want thirty extra points for it..." ("angry", "happyCl", "annoyed", "mid")
                gen "Thirty points to receive a massage?" ("base", xpos="far_left", ypos="head")
                gen "No... Twenty points, take it or leave it." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Fine..." ("annoyed", "narrow", "annoyed", "down")
            else:
                her @ cheeks blush "Alright..." ("annoyed", "narrow", "base", "down")
        else:
            her @ cheeks blush "[name_genie_hermione]?" ("angry", "narrow", "base", "mid")
            her @ cheeks blush "Could... Do you think you could massage me?" ("angry", "closed", "worried", "mid")
            gen "Massage you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Massage my butt I mean..." ("disgust", "base", "base", "R")
            gen "Your--{w=0.2} Why of course [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you..." ("angry", "closed", "base", "mid")
    else: #Repeat
        if states.her.level < 19:
            gen "But until we try that... I suppose I could give you another massage." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "happyCl", "base", "mid")
            gen "For another twenty extra points of course..." ("base", xpos="far_left", ypos="head")
            $ current_payout += 20 #40 total
            her @ cheeks blush "Fine..." ("disgust", "narrow", "base", "R")
        else:
            gen "Well then, how about another massage?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I--{w=0.4} Yes please..." ("angry", "narrow", "base", "mid")
            gen "Great, then get that ass over here." ("base", xpos="far_left", ypos="head")

    #Hermione walks to desk
    call her_walk("desk")

    show screen blkfade

    nar "Hermione makes her way over to your desk, her ass bouncing up and down as she moves, and then presents herself to you."
    pause .8

    #Genie before groping chibi
    call her_chibi_scene("behind_desk_back")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    if states.her.level < 19:
        her @ cheeks blush "Please be gentle, [name_genie_hermione]..." ("angry", "base", "base", "R", xpos="mid", ypos="base", flip=True, trans=d3)
        gen "Certainly... It is a massage is it not?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("angry", "narrow", "base", "down") #pout

        call her_chibi_scene("grope_ass_back")
        with d3
        nar "You grab Hermione's engorged buttocks with your hands and give them a light squeeze."
        call her_chibi_scene("behind_desk_back")
        with d3

        her @ cheeks blush "*Ah*..." ("open", "happyCl", "base", "stare")
        her @ cheeks blush "..." ("disgust", "squint", "worried", "stare")  #Wide
        gen "Was that a moan, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "N-- No...{w=0.4} It's...{w=0.4} Your hands are cold!" ("disgust", "narrow", "worried", "R") #annoyed #glance
        gen "I see..." ("base", xpos="far_left", ypos="head")
        gen "In that case I'll continue..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Wait--" ("clench", "base", "base", "R")

        call her_chibi_scene("grope_ass_back")
        with d3
        nar "You begin to firmly stroke her ass cheeks with your open palms."

        her @ cheeks blush "" ("annoyed", "happyCl", "worried", "mid") #happycl #annoyed #blush
        pause .8
        nar "Grabbing the sides of her waist, you start kneading her cheeks with your thumbs."
        gen "These cheeks, so soft... Yet so firm..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ehm*..." ("angry", "narrow", "base", "down")
        nar "You give her cheeks a quick squeeze."
        her @ cheeks blush "[name_genie_hermione]!" ("disgust", "narrow", "base", "R")
        gen "How did that feel, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I... {w=0.4} Good?" ("open", "squint", "worried", "down")
        gen "You don't sound very convinced..." ("base", xpos="far_left", ypos="head")
        gen "I didn't take you for such a spoiled girl, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "You could at least act a little bit more grateful..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "What do you--" ("angry", "happy", "worried", "mid")
        nar "You firmly dig into her cheeks with your thumbs, making her clench up from the surprise."
        her @ cheeks blush "Ouch!" ("disgust", "happyCl", "annoyed", "mid")
        her @ cheeks blush "I thought this was supposed to be a massage!" ("angry", "narrow", "annoyed", "R")
        gen "Then try and relax a bit, would you?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "narrow", "annoyed", "R") #annoyed
        her @ cheeks blush "...{fast} Fine." ("open", "narrow", "annoyed", "stare") #annoyed
        her @ cheeks blush "..." ("base", "narrow", "worried", "L") #closed eyes
        gen "Good... Now let's see what your final verdict will be..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("base", "closed", "worried", "mid")
        nar "You begin moving your hands up and down her thighs, lightly brushing against the underside of her butt."
        nar "Hermione doesn't respond, but you feel her muscles relax a bit more as you continue rubbing her."
        her @ cheeks blush "" ("base", "closed", "base", "mid")
        nar "Moving your hand up again, you resume massaging her soft cheeks..."
        her @ cheeks blush "*Mmm*..." ("soft", "closed", "worried", "mid") #closed eyes #blush
        nar "Hermione let's out an involuntary moan of pleasure..."
        gen "(*Hngh*... What I'd do to stick my dick in between those cheeks.)" ("angry", xpos="far_left", ypos="head")
        nar "You pull her cheeks apart to reveal her puckered butthole, and then quickly let go before she notices..."
        gen "(It looks so tight with her ass like this!)" ("angry", xpos="far_left", ypos="head")
        gen "(I've got to know what it feels like...)" ("base", xpos="far_left", ypos="head")
    else: # 19+
        her @ cheeks blush "Please hurry [name_genie_hermione]... Massage my butt cheeks..." ("angry", "base", "base", "R", xpos="mid", ypos="base", flip=True, trans=d3)
        gen "*Hmm*... I'm not so sure if I should do it now..." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Please!" ("disgust", "happyCl", "base", "mid")
        her @ cheeks blush "I need it!" ("angry", "happyCl", "base", "mid")
        gen "Very well [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

        call her_chibi_scene("grope_ass_back")
        with d3
        nar "You grab Hermione's engorged buttocks with your hands and give them a light squeeze."

        her @ cheeks blush "..." ("grin", "narrow", "base", "stare") #blank stare horny
        gen "Well this potion certainly is effective." ("base", xpos="far_left", ypos="head")
        nar "You begin to firmly stroke her ass with your open palms."
        her @ cheeks blush "*Mmm*..." ("smile", "narrow", "base", "stare")
        gen "(I barely even touched her yet...)" ("base", xpos="far_left", ypos="head")
        nar "Continuing the massage, you begin kneading her soft cheeks with your thumbs..."
        her @ cheeks blush "[name_genie_hermione]..." ("base", "narrow", "base", "stare")
        nar "Grabbing the sides of her waist, you move your thumbs in a circular motion, giving her a squeeze each time you close your palm."
        her @ cheeks blush "*Ah*..." ("open", "closed", "base", "mid")
        nar "Lightening your grip, you slowly slide your hands alongside the sides of her figure and move them underneath her cheeks."
        her @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} You...{w=0.3} You're..." ("soft", "closed", "worried", "mid")
        nar "Hermione begins to breathe heavily as you grab her cheeks firmly with your thumbs."
        nar "You pull them apart to reveal her butthole and then proceed to watch them jiggle as you let go."
        her @ cheeks blush "" ("soft", "narrow", "worried", "stare") #pleasure
        pause .8
        nar "Seeing her puckered hole gives you an idea."

    $ states.her.ev.potions.ass_expand_complete = True

    menu:
        "-Stick a finger in there-":
            nar "You spread her cheeks open again to expose that tight hole."
            gen "Let's see how sensitive you really are..." ("base", xpos="far_left", ypos="head")
            nar "You start teasing the rim with your finger, gently circling it."
            if not states.her.status.anal: #Fail
                if not states.her.ev.potions.ass_expand_tried_fingering:
                    her @ cheeks blush "what do you--" ("base", "narrow", "base", "stare") #confused

                    play sound "sounds/gltch.ogg"

                    her @ cheeks blush "!!!" ("clench", "wide", "base", "stare") #wide eyed
                    nar "You feel Hermione clench up around your finger as you insert it into her butthole."
                    her @ cheeks blush "What are you doing?!?" ("scream", "happyCl", "worried", "R")
                    gen "What does it feel like I'm doing?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "You... You've put something in me!" ("angry", "happyCl", "annoyed", "mid")
                    gen "That's right..." ("base", xpos="far_left", ypos="head")
                    nar "You wiggle your finger inside Hermione's butthole."
                    her @ cheeks blush "" ("angry", "wide", "base", "stare") #wide eyed #blush
                    gen "So, how sensitive is--" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Pull it out!" ("scream", "happyCl", "base", "stare")
                    gen "But--" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Now!" ("scream", "happyCl", "annoyed", "mid")
                    gen "Fine..." ("base", xpos="far_left", ypos="head")

                    play sound "sounds/pop01.ogg"

                else: #Tried to finger her Ass before
                    her @ cheeks blush "Wait, you don't mean--" ("angry", "wide", "base", "stare")

                    play sound "sounds/gltch.ogg"

                    her @ cheeks blush "!!!" ("clench", "happyCl", "annoyed", "mid") #wide eyed
                    nar "You feel Hermione clench up around your finger as you insert it into her butthole."
                    her @ cheeks blush "[name_genie_hermione], what are you doing!" ("scream", "happyCl", "annoyed", "mid")
                    gen "I stuck my finger in your butthole, feels good doesn't it?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "No! I can't believe you're doing this again!" ("scream", "happy", "annoyed", "R")
                    her @ cheeks blush "Pull it out!" ("clench", "squint", "annoyed", "R")
                    gen "One moment..." ("base", xpos="far_left", ypos="head")
                    nar "You wiggle your finger inside Hermione's butthole."
                    her @ cheeks blush "Now!" ("scream", "base", "annoyed", "mid")
                    gen "Alright, fine..." ("base", xpos="far_left", ypos="head")

                # Fail End section #
                show screen blkfade
                with d3

                hide hermione_main
                call her_chibi("stand","desk","base")
                call gen_chibi("sit_behind_desk")

                hide screen blkfade
                with d5

                if states.her.level < 19: #When she cares about points
                    her @ cheeks blush "I'll have those points now..." ("angry", "narrow", "annoyed", "mid", xpos="base", ypos="base", flip=False, trans=d3)
                    gen "But..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "No... No buts!" ("scream", "squint", "angry", "mid")
                    gen "Alright... {number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I can't believe you..." ("angry", "narrow", "annoyed", "R")
                else:
                    her @ cheeks blush "I can't believe you..." ("angry", "narrow", "base", "R", xpos="base", ypos="base", flip=False, trans=d3) #blush
                    gen "Sorry, I got a bit ahead of myself..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "" ("angry", "base", "worried", "mid") #surprised by your apology
                    pause .8
                    gen "I should've put two in the pink, one in the--" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "*Grrr*!" ("angry", "narrow", "annoyed", "mid")

                call her_walk(action="leave", speed=2.0)
                play sound "sounds/door_down.ogg"
                with hpunch
                $ states.her.mood += 20

                if not _no_clothes:
                    if states.her.level < 19:
                        gen "..." ("base", xpos="far_left", ypos="head")
                    else:
                        gen "Was it something I said?" ("base", xpos="far_left", ypos="head")
                else:
                    pause 0.5

                    gen "You forgot your..." ("base", xpos="far_left", ypos="head")
                    call her_walk(action="enter")

                    pause .5
                    play sound "sounds/cloth_sound.ogg"
                    $ hermione.wear("all")
                    pause .4
                    call her_walk(action="leave")
                    play sound "sounds/door_down.ogg"
                    with hpunch

                    pause 1.0

                    gen "{cps=3}...{/cps}" ("base", xpos="far_left", ypos="head")
                    gen "No buts next time, got it." ("base", xpos="far_left", ypos="head")

                $ hermione.unequip("hips")
                $ states.her.ev.potions.ass_expand_drank = True
                $ states.her.ev.potions.ass_expand_tried_fingering = True
                $ _no_clothes = False #Took off main clothing check reset
                jump end_hermione_event

            else: #Success
                if not states.her.ev.potions.ass_expand_tried_fingering:
                    her @ cheeks blush "[name_genie_hermione] please... I'm too sensitive. If you do that, I'm not sure I'll be able to control myself." ("mad", "narrow", "worried", "R")
                    gen "That's unfortunate..." ("base", xpos="far_left", ypos="head")
                    nar "You slowly pull your finger away from her asshole."
                    her @ cheeks blush "Thank you--" ("base", "closed", "worried", "mid")
                    nar "And then fully insert it."

                    play sound "sounds/gltch.ogg"

                    her @ cheeks blush "..." ("grin", "base", "base", "ahegao")
                    gen "What was it you said about control?" ("base", xpos="far_left", ypos="head")
                    nar "You wiggle your finger inside Hermione's butthole."
                    her @ cheeks blush "" ("grin", "happyCl", "base", "stare")
                    pause .8
                    nar "You keep going and suddenly feel her tense up around your finger."
                    gen "Such a anal slut... I wonder what you'll do once I try this." ("base", xpos="far_left", ypos="head")
                    nar "You pull your finger out slightly and without warning start pumping it in and out of her puckered asshole."

                    play background "sounds/slickloop.ogg" fadein 2

                    her @ cheeks blush "!!!" ("open_tongue", "base", "base", "ahegao")
                    nar "As you continue your barrage on the girl's hole, you feel her shaking, desperately trying to keep her composure."
                    her @ cheeks blush "Please [name_genie_hermione]..." ("grin", "happyCl", "base", "mid")
                    her @ cheeks blush "I can't take it any longer..." ("angry", "narrow", "base", "dead")
                else:
                    her @ cheeks blush "Please [name_genie_hermione]... Not again... I can't take it..." ("angry", "narrow", "base", "stare")
                    gen "You shouldn't put yourself down so much [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    nar "You poke Hermione's asshole with your finger, sticking the tip in just slightly."
                    her @ cheeks blush "*Ngh*... [name_genie_hermione]..." ("clench", "narrow", "base", "up")
                    gen "What was that?" ("base", xpos="far_left", ypos="head")
                    nar "You take the tip of your finger out again and start teasing the entrance of her butthole..."
                    gen "That's odd... I thought you said you couldn't take it, but the tip of my finger sure found it easy to penetrate you, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    nar "You circle the entrance of her butthole with your finger, and Hermione's words trail off into sounds of pleasure..."
                    her @ cheeks blush "*Mmmm*... [name_genie_hermione]..." ("mad", "closed", "base", "mid")
                    gen "Let's try this again then shall we..." ("base", xpos="far_left", ypos="head")
                    nar "You put your finger up against her puckered hole once more and give it a gentle push."

                    play sound "sounds/gltch.ogg"

                    her @ cheeks blush "[name_genie_hermione]!" ("grin", "narrow", "base", "up")
                    gen "Look who suddenly woke up for the event." ("base", xpos="far_left", ypos="head")
                    nar "You begin pumping your finger in and out of Hermione's ass with increasing ease."

                    play background "sounds/slickloop.ogg" fadein 2

                    her @ cheeks blush "oooh...." ("grin", "squint", "base", "stare")
                    gen "You sure are taking it pretty well [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "*Ah*...{w=0.4} Maybe I--{w=0.2}  *Ah*..." ("soft", "happyCl", "base", "mid")
                    her @ cheeks blush "Maybe I've finally gotten used to--{w=0.2} *Ah*..." ("soft", "happyCl", "base", "stare")
                    gen "Gotten used to having your ass filled?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("soft", "closed", "worried", "stare")
                    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
                    nar "Not missing a beat, you stick your finger down to the hilt inside Hermione's ass."

                    play sound "sounds/gltch.ogg"
                    pause .4

                    her @ cheeks blush "[name_genie_hermione]!!!" ("angry", "happyCl", "base", "stare")
                    her @ cheeks blush "[name_genie_hermione], it's too much!!!" ("clench", "happyCl", "worried", "stare")
                    her @ cheeks blush "Please!" ("soft", "narrow", "worried", "up")


                menu:
                    "-Keep Going-": #Hermione cums


                        gen "What was that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

                        nar "Pushing Hermione over your desk, you finger her ass vigorously."
                        call her_chibi_scene("lie_on_desk_fingering_slow")

                        play background "sounds/slickloopfast.ogg"

                        nar "Increasing the pace, Hermione now begins dripping with excitement."
                        her @ cheeks blush "Please..." ("grin", "narrow", "base", "dead")

                        gen "Please what?" ("base", xpos="far_left", ypos="head")

                        play sound "sounds/gltch.ogg"

                        nar "You insert a second finger."
                        her @ cheeks blush "*Ah*...{w} Please...{w} Stop...{w} You'll break me!" ("smile", "narrow", "base", "dead")

                        call her_chibi_scene("lie_on_desk_fingering_slow")
                        play background "sounds/slickloopveryfast.ogg"

                        nar "Grabbing her hip with your other hand, you relentlessly finger-fuck her asshole."
                        her @ cheeks blush "...{w=0.03}{nw}" ("open_tongue", "base", "base", "up")
                        her @ cheeks blush "...{fast}" ("open_wide_tongue", "base", "base", "ahegao")
                        nar "And suddenly, you feel her body go limp as her asshole relentlessly quivers around your fingers."
                        her @ cheeks blush "*Ah*!" ("smile", "base", "worried", "ahegao")
                        stop background fadeout 2

                        call her_chibi_scene("lie_on_desk_fingering_cumming")
                        with d3

                        play sound "sounds/slick_01.ogg"
                        with kissiris
                        pause .8

                        her @ cheeks blush "" ("smile", "happyCl", "worried", "mid")

                        play sound "sounds/slick_01.ogg"
                        with kissiris
                        pause .8

                        play sound "sounds/slick_01.ogg"
                        with kissiris

                        her @ cheeks blush "" ("smile", "narrow", "base", "up")
                        call her_chibi_scene("lie_on_desk_fingering_pause_ahegao")
                        with d5

                        gen "There...{w=0.4} Wasn't that nice?" ("base", xpos="far_left", ypos="head")
                        nar "Hermione shakes slightly in your hands as you stop fingering her, and you watch as a streak of liquid starts going down her thigh."

                        call her_chibi_scene("lie_on_desk_fingering_pause")
                        with d5

                        her @ cheeks blush "Yes...{w=0.4} *Hngh*...{w=0.4} [name_genie_hermione]." ("grin", "happyCl", "base", "dead")
                        call her_chibi_scene("lie_on_desk")
                        with d5
                        her @ cheeks blush "*Mmm*..." ("base", "narrow", "worried", "dead") #look of pleasure
                        gen "... {w} Good girl." ("base", xpos="far_left", ypos="head")

                    "-Let go of her-":
                        gen "Well, If that's the case!" ("base", xpos="far_left", ypos="head")
                        stop background fadeout 2

                        her @ cheeks blush "*Ah*...{w=0.4} Be careful--" ("mad", "narrow", "worried", "R")
                        nar "With a small yelp and popping sound, you quickly pull your finger out of her asshole."

                        play sound "sounds/pop01.ogg"
                        with kissiris

                        her @ cheeks blush "*Ngh*!!!" ("grin", "narrow", "base", "up") #wide #blush
                        gen "What was that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "*Ah*...{w=0.4} Nevermind." ("disgust", "narrow", "worried", "up")


                #End section
                show screen blkfade
                with d5

                nar "Standing there for a moment, you begin feeling Hermione's breathing slow down..."
                nar "Finally after a couple of minutes, once her ass shrunk back down, she straightens her back and makes it to the front of your desk..."

                call her_chibi("stand","desk","base", flip=False)
                call gen_chibi("sit_behind_desk")
                hide hermione_main

                hide screen blkfade
                with d5

                call music_block

                gen "Well then... You best be off to class." ("base", xpos="far_left", ypos="head")

                if not _no_clothes:
                    her @ cheeks blush "Alright..." ("base", "narrow", "base", "down", xpos="base", ypos="base", flip=False, trans=d3)
                    $ hermione.wear("all")
                else: #Took of main clothing
                    her @ cheeks blush "Alright... Just give me a moment..." ("base", "narrow", "base", "down", xpos="base", ypos="base", flip=False, trans=d3)
                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.wear("all")
                    pause .5
                    her "There we go..." ("base", "wink", "base", "mid")
                    her "" ("base", "base", "base", "mid")


                gen "Now hurry up... I have things to attend to." ("base", xpos="far_left", ypos="head")
                if states.her.level < 19:
                    her "*Ehm*... What about my points?" ("soft", "wink", "base", "mid")
                    gen "Oh right... The points..." ("base", xpos="far_left", ypos="head")
                    gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                else:
                    gen "Oh, I almost forgot, {number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                    her "Oh right... The points.... Thank you." ("soft", "wink", "base", "mid")

                nar "Hermione, still a bit dazed, stumbles slightly as she makes her way to your door."

                call her_walk("mid", "base")
                pause .2
                play sound "sounds/jump_shoes.ogg"

                her @ cheeks blush "*Ahem*..." ("angry", "squint", "base", "R", flip=True, trans=d3)

                call her_walk("door", "base")
                pause.2

                her @ cheeks blush "Bye then..." ("angry", "narrow", "base", "L", flip=True, trans=d3)

                call her_walk(action="leave")

                $ states.her.ev.potions.ass_expand_drank = True
                $ states.her.ev.potions.ass_expand_tried_fingering = True
                $ _no_clothes = False #Took off main clothing check reset
                $ hermione.unequip("hips")
                jump end_hermione_event

        "-Let go of her-":
            gen "(Probably shouldn't push it...)" ("base", xpos="far_left", ypos="head")
            gen "Well, I suppose that's enough for now..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... Okay!" ("angry", "base", "base", "stare") #happyclosed
            nar "You give her cheeks one last squeeze and then let go of her."
            her @ cheeks blush "..." ("soft", "squint", "base", "stare") #surprised

            call music_block

            #End section
            gen "Well you best be off to class." ("base", xpos="far_left", ypos="head")
            if states.her.status.public_stripping:
                her @ cheeks blush "Alright..." ("open", "narrow", "base", "down") #surprised
            else:
                her @ cheeks blush "... With my butt looking like this?" ("soft", "narrow", "base", "down")
                gen "I'm sure no one will be able to tell." ("base", xpos="far_left", ypos="head")
            gen "Now hurry up... I have things to attend to." ("base", xpos="far_left", ypos="head")

            show screen blkfade
            with d5

            $ hermione.equip(her_hips_ass2)

            nar "As Hermione's straightens her back, you watch as her ass begins shrinking in size."
            nar "With a short sigh, she then walks up to the front of your desk."

            $ hermione.equip(her_hips_ass1)

            call her_chibi("stand","desk","base", flip=False)
            call gen_chibi("sit_behind_desk")
            hide hermione_main

            hide screen blkfade
            with d5

            $ hermione.unequip("hips")

            her @ cheeks blush "So, is that it [name_genie_hermione]?" ("open", "squint", "base", "R", xpos="base", ypos="base", flip=False, trans=d3)
            if states.her.level < 19:
                gen "Unless there's something else you wanted..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Ehm*..." ("angry", "narrow", "base", "down")
                her @ cheeks blush "The points." ("angry", "squint", "base", "mid")
                gen "Oh right, the points!" ("base", xpos="far_left", ypos="head")
                gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Thank you, I'll head back to class then..." ("soft", "base", "base", "R")
            else:
                gen "Yes... No, wait, I almost forgot!" ("base", xpos="far_left", ypos="head")
                gen "{number=current_payout} to Gryffindor!" ("base", xpos="far_left", ypos="head")
                her "Oh right... The points.... Thank you." ("soft", "narrow", "base", "down")

            if not states.her.status.anal: #didn't expect you to push further
                gen "You're welcome by the way..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "[name_genie_hermione]?" ("soft", "base", "base", "mid")
                gen "For the massage." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh... Thank you [name_genie_hermione]." ("annoyed", "squint", "base", "R")
                gen "Off you go." ("base", xpos="far_left", ypos="head")
                if not _no_clothes:
                    her @ cheeks blush "Alright." ("soft", "wink", "base", "mid")
                else: #Took of main clothing
                    her @ cheeks blush "One moment please..." ("soft", "wink", "base", "mid")

                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.wear("all")
                    pause .5

            else: #Expected you to push further
                her @ cheeks blush "..." ("annoyed", "narrow", "base", "down")
                gen "Is everything okay [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh... Yes, I'm fine, [name_genie_hermione]..." ("soft", "narrow", "base", "down")
                gen "Good." ("base", xpos="far_left", ypos="head")
                if not _no_clothes:
                    gen "Off you go then." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Right..." ("annoyed", "narrow", "base", "R")
                else: #Took of main clothing
                    her @ cheeks blush "I suppose I'll just put this back on then..." ("annoyed", "narrow", "base", "down")

                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.wear("all")
                    pause .5

                her @ cheeks blush "Off I go..." ("open", "base", "base", "R")

            her @ cheeks blush "Bye then, [name_genie_hermione]..." ("open", "closed", "base", "mid")
            gen "Bye [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

            call her_walk(action="leave")
            $ states.her.ev.potions.ass_expand_drank = True
            $ _no_clothes = False #Took off main clothing check reset
            jump end_hermione_event


##Send Hermione to class Ass expand Return event##
label her_potion_ass_return:

    #Hermione enters the office, and walks to the front of the desk
    call her_walk("desk", "base", action="enter")

    if states.her.public_level < 19:
        her @ cheeks blush "That was so humiliating..." ("disgust", "narrow", "base", "down")
        gen "Hello to you too..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Why did you have to give me that potion the day Professor Snape has us go to Hogsmeade?" ("open", "closed", "annoyed", "mid")
        gen "Go to what?" ("base", xpos="far_left", ypos="head")
        her "To Hogsmeade!" ("open", "base", "angry", "mid")
        her "Although, I suppose you may not have been aware of that..." ("clench", "squint", "base", "R")
        her "Professor Snape usually sends us down to Hogsmeade to acquire the necessary potion supplies for the month." ("open", "closed", "annoyed", "mid")
        gen "How lazy can a man get..." ("base", xpos="far_left", ypos="head")
        her "Sorry, [name_genie_hermione]... I probably should've told you about it." ("disgust", "narrow", "base", "down")
        her "You know I'd normally tell you these things but..." ("angry", "narrow", "base", "R")
        gen "But?" ("base", xpos="far_left", ypos="head")
        her "Well... Getting out of that classroom once a month is usually what lets me get through..." ("disgust", "closed", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        her "I promise we're still learning a lot about ingredients and such in J. Pippin's!" ("angry", "squint", "base", "mid")
        her "At least the ones who actually make it there do..." ("angry", "narrow", "base", "R")
        her "The Slytherin's just see it as an opportunity to take the day off." ("open", "narrow", "annoyed", "R")
        gen "Sounds to me like you've had a great day then." ("base", xpos="far_left", ypos="head")
        gen "Professor Snape and the Slytherins is like the top of the list of things you constantly complain about." ("base", xpos="far_left", ypos="head")
        her "I don't always complain about them!" ("disgust", "squint", "annoyed", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        her "That said... I'd normally enjoy the free time as you mentioned... But manoeuvring that... *Err*..." ("angry", "squint", "worried", "R")
        gen "Dump truck?" ("base", xpos="far_left", ypos="head")
        her "..." ("disgust", "base", "base", "mid")
        her "Yes, that..." ("disgust", "squint", "base", "mid")
        her "We didn't even get all the way down to Hogsmeade, which is normally where the Slytherins would leave the group before they took notice..." ("open", "squint", "annoyed", "R")
        her "I was just about to give them a piece of my mind, but this thing made me lose my balance and fall onto the ground..." ("angry", "narrow", "angry", "down")
        her "And to no surprise, they stopped in their tracks howling with laughter..." ("angry", "narrow", "angry", "R")
        gen "Surely some Slytherin students trying to make a scene isn't enough to--" ("base", xpos="far_left", ypos="head")
        her "Of course not!" ("angry", "closed", "annoyed", "mid")
        her @ cheeks blush "But they're not the only ones who have been starting at it." ("annoyed", "narrow", "annoyed", "R")
        her @ cheeks blush "Me falling over on the way to Hogsmeade wasn't exactly a one-time occurrence..." ("open", "narrow", "annoyed", "down")
        her @ cheeks blush "Whilst other people weren't openly laughing at it, I could still hear them whispering and giggling..." ("angry", "narrow", "base", "down")
        her @ cheeks blush "I felt as if I was going to die from embarrassment..." ("disgust", "closed", "base", "mid")
        gen "They're just jealous." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Are they, [name_genie_hermione]?" ("disgust", "narrow", "base", "mid")
        gen "Well... Maybe not the falling over part." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("annoyed", "narrow", "base", "down")
        her @ cheeks blush "Can I have my points now?" ("open", "closed", "base", "mid")
        gen "Of course [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
        gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "... Thank you." ("base", "squint", "base", "mid")
    else:
        her @ cheeks blush "Hello [name_genie_hermione]..." ("base", "narrow", "base", "R")
        gen "Back so soon?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I... Yes..." ("base", "narrow", "base", "down")
        gen "Very well... So, how's your day been?" ("base", xpos="far_left", ypos="head")
        gen "Anything interesting happen?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well..." ("base", "closed", "base", "mid")

        show her_potions_public_expand_ass_a1 as cg zorder 17:
            fit "cover"
        with fade

        her @ cheeks blush "In today's \"History of magic\" lesson, I was asked by professor Binns to help outline the timeline of the Witch hunts of the 14th century on the blackboard..." ("open", "closed", "base", "mid")
        gen "Sounds dreadfully boring..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "History of magic is not boring, [name_genie_hermione]!" ("angry", "squint", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Okay, maybe it's a little bit boring..." ("angry", "narrow", "base", "R")
        her @ cheeks blush "But it's important!" ("annoyed", "base", "base", "mid")
        gen "Boring but important... Got it." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Anyhow... I'd usually be very pleased to be given such an opportunity." ("open", "base", "base", "R")
        her @ cheeks blush "Although seeing the circumstances..." ("angry", "narrow", "base", "down")
        gen "I bet you were even more pleased than usual!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("base", "narrow", "base", "down")
        her @ cheeks blush "So of course I accepted and went up to help him..." ("open", "closed", "base", "mid")

        show her_potions_public_expand_ass_a2 as cg:
            fit None
            offset (0, -200)
            zoom 0.5
            pause 1.5
            ease_quad 5.0 zoom 1.0 offset (-2600, -1000)
        with fade

        her @ cheeks blush "And it didn't take long until the other students noticed my..." ("angry", "narrow", "base", "R")

        show her_potions_public_expand_ass_a2 as cg:
            ease 6.0 zoom 0.75 offset (-2100, -500)

        gen "Defined derrière!" ("grin", xpos="far_left", ypos="head")

        show her_potions_public_expand_ass_a2 as cg:
            ease_quad 30.0 zoom 0.25 offset (0, 0)

        her @ cheeks blush "That's one way to say it..." ("base", "narrow", "base", "down")
        her @ cheeks blush "Once I had finished, I realised almost everyone had been staring at me the entire time instead of the blackboard..." ("base", "narrow", "base", "R")
        her @ cheeks blush "I doubt any of them learnt a thing about the Witch hunts..." ("open", "narrow", "base", "R")
        gen "Well... What's happened, happened." ("base", xpos="far_left", ypos="head")
        gen "No need to dwell on it..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione], the witch hunts were--" ("angry", "base", "base", "mid")
        gen "Not the witch hunts [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh... Right..." ("disgust", "base", "base", "mid")
        gen "Well, you've certainly deserved your points." ("base", xpos="far_left", ypos="head")
        gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "... Thank you." ("base", "narrow", "base", "down")

    hide cg
    with fade

    gen "That will be all for today..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Okay..." ("open", "base", "base", "mid")
    gen "Until next time [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    $ states.her.ev.potions.ass_expand_drank = True
    $ states.her.ev.potions.ass_expand_public_complete = True

    jump end_hermione_event
