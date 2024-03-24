default ev_her_small_plug = Event(id="ev_her_small_plug", label="hg_butt_plugs_small_return", req="game.daytime==False")
default ev_her_medium_plug = Event(id="ev_her_medium_plug", label="hg_butt_plugs_medium_return", req="game.daytime==False")
default ev_her_large_plug = Event(id="ev_her_large_plug", label="hg_butt_plugs_large_return", req="game.daytime==False")

label hg_butt_plugs_fail:
    jump end_hermione_event

label hg_butt_plugs:

    # Setup
    $ her_outfit_last.save() #Saves current clothing

    $ current_payout = 55 # Default payout

    if not her_buttplug_small1.unlocked:
        gen "{size=-4}(I could ask her to wear a butt plug around the school today.){/size}" ("base", xpos="far_left", ypos="head")
    else:
        gen "{size=-4}(I feel like making her walk around with a butt plug again!){/size}" ("base", xpos="far_left", ypos="head")

    gen "{size=-4}(But which one?){/size}" ("base", xpos="far_left", ypos="head")

    label .plug_choice:

    menu:
        "-Small, regular-":
            if not her_buttplug_small1.unlocked:
                # First time with small butt plug

                gen "[name_hermione_genie], I want you to do something different today..." ("base", xpos="far_left", ypos="head")
                her "..........." ("soft", "base", "base", "mid",xpos="right",ypos="base")
                nar "You pull a large-sized butt plug out from under your desk and place it in front of her."

                if states.her.level < 15:
                    gen "Today, I want you to wear a butt plug around the school." ("base", xpos="far_left", ypos="head")
                    her "You want me to...{w=0.4} What?!" ("angry", "wide", "worried", "mid")
                    gen "Wear a--" ("base", xpos="far_left", ypos="head")
                    her "[name_genie_hermione_], I can't believe you'd do this!" ("angry", "happyCl", "worried", "mid")
                    her "I'm leaving!" ("angry", "base", "worried", "R")

                    call her_walk(action="leave")

                    $ states.her.mood += 6

                    jump hg_butt_plugs_fail

                $ her_buttplug_small1.unlock()
                $ ev_her_small_plug.enqueue()

                her "and what is that supposed to be? Some sort of animal tail?" ("open", "squint", "base", "mid")
                gen "Not exactly, it's a butt plug. I want you to wear it while you attend class today." ("base", xpos="far_left", ypos="head")

                stop music
                with hpunch

                her "{size=+5}What?!!{/size}" ("shock", "wide", "base", "stare")

                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

                her "You expect me to put that massive thing in my..." ("angry", "base", "angry", "mid")
                her "and then parade myself around the school!?"
                gen "It just looks like a fake tail, No one will be able to tell what it really is." ("base", xpos="far_left", ypos="head")
                her "{size=+5}That's not the point!{/size}" ("scream", "closed", "angry", "mid")
                her "I'm not going to put that ridiculous thing anywhere near my butt!"
                her "We are done here, [name_genie_hermione]!" ("angry", "base", "angry", "mid",emote="angry")
                gen "Alright, alright, calm down..." ("base", xpos="far_left", ypos="head")
                her "I most certainly will not, [name_genie_hermione]! That thing is beyond absurd!" ("scream", "closed", "angry", "mid")
                gen "Alright, fine, maybe I underestimated how large it is..." ("base", xpos="far_left", ypos="head")
                her "You think [name_genie_hermione]?! I'd like to see you try and fit it up your--" ("angry", "base", "angry", "mid")
                gen "Alright, alright..." ("base", xpos="far_left", ypos="head")
                her "........." ("annoyed", "narrow", "annoyed", "mid")
                gen "How about we try one a little less... ambitious?" ("base", xpos="far_left", ypos="head")
                her "............" ("upset", "closed", "base", "mid")
                gen "I'm willing to give Gryffindor fifty-five points." ("base", xpos="far_left", ypos="head")
                gen "And all I ask for..." ("base", xpos="far_left", ypos="head")
                her "..........?" ("annoyed", "squint", "base", "mid")

                nar "You pull out a small-sized butt plug from your desk."

                gen "Is that you wear this to class..." ("base", xpos="far_left", ypos="head")
                her "!!!" ("angry", "base", "angry", "mid")
                gen "Oh, come on... Just a harmless little baby one." ("base", xpos="far_left", ypos="head")
                her "..." ("disgust", "narrow", "base", "mid_soft")
                gen "Fifty-five house points..." ("base", xpos="far_left", ypos="head")
                her ".............." ("annoyed", "narrow", "angry", "R")
                her "Fine." ("annoyed", "narrow", "annoyed", "mid")
                gen "Fantastic." ("base", xpos="far_left", ypos="head")
                gen "Will you be putting it in now then?" ("base", xpos="far_left", ypos="head")
                her "........" ("annoyed", "narrow", "angry", "R")
                her "I'll do it in the girls' bathroom, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
                gen "*Hmm*... Alright, I'll see you tonight then." ("base", xpos="far_left", ypos="head")
            else:
                $ ev_her_small_plug.enqueue()
                # Repeat with small butt plug
                if states.her.level > 21:
                    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    gen "What do you think about wearing a butt pl--?" ("base", xpos="far_left", ypos="head")
                    her "I'll do it." ("grin", "base", "base", "R",xpos="right",ypos="base")
                    gen "You're eager." ("base", xpos="far_left", ypos="head")
                    her "Well... I mean, I've sort of grown fond of how it feels..." ("open", "narrow", "worried", "down")
                    gen "Excellent... Go have fun then!" ("base", xpos="far_left", ypos="head")
                    nar "You pull out the small-sized butt plug and hand it to her."
                    nar "Hermione turns around and lifts her skirt giving you a full view as she inserts it."
                    her "{heart}*Ah*{heart}..." ("grin", "narrow", "annoyed", "up")
                    her "I will, [name_genie_hermione]. Thank you." ("base", "happyCl", "base", "mid")

                elif states.her.level >= 19:
                    nar "You pull out the large-sized butt plug."
                    gen "Ready to try out \"the dragon\" yet?" ("base", xpos="far_left", ypos="head")
                    stop music fadeout 1.0
                    her "What?" ("scream", "wide", "base", "mid",xpos="right",ypos="base")
                    her "Of course not! That thing would tear me--" ("scream", "closed", "angry", "mid")
                    nar "You put the large-sized butt plug back and pull out the small-sized butt plug instead."
                    gen "How about this one then?" ("base", xpos="far_left", ypos="head")
                    her "Oh, okay then!" ("smile", "happyCl", "base", "mid",emote="happy")
                    gen "You'll do it that easily?" ("base", xpos="far_left", ypos="head")
                    her "Well, for fifty-five house points I'd be crazy not to." ("base", "closed", "base", "mid")
                    her "Plus, I don't hate the way it feels..." ("open", "base", "base", "R")
                    nar "You hand her the butt plug."
                    gen "Why don't you put it in now?" ("base", xpos="far_left", ypos="head")
                    her "You want me to put it in now? in front of you?!" ("scream", "wide", "base", "mid")
                    gen "I don't see the harm in it." ("base", xpos="far_left", ypos="head")
                    her "Well... It does save me having to visit the girls' bathroom before class..." ("annoyed", "narrow", "worried", "down")
                    her "Alright then, I'll do it... But I want an extra five points!" ("smile", "base", "base", "R")
                    gen "Done." ("base", xpos="far_left", ypos="head")
                    $ current_payout += 5
                    her "Well...{w=0.4} here it goes." ("smile", "base", "base", "R")
                    nar "Hermione lifts her skirt and pushes it in rather slowly."

                    play sound "sounds/gltch.ogg"
                    with kissiris

                    her "{heart}*Ah*{heart}..." ("grin", "narrow", "annoyed", "up")
                    her "I better head to class..." ("soft", "happy", "base", "R")
                    gen "See you tonight [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                    her "{size=-5}({heart}it feels so good{heart}){/size}" ("grin", "narrow", "annoyed", "up")

                else:
                    gen "Today's favour shall be..." ("base", xpos="far_left", ypos="head")
                    her "........." ("angry", "base", "base", "mid",xpos="right",ypos="base")
                    gen "Wearing your favourite little butt plug to class!" ("base", xpos="far_left", ypos="head")
                    her "... again?" ("angry", "narrow", "base", "down")
                    gen "Sure, why not?" ("base", xpos="far_left", ypos="head")
                    gen "And another fifty-five house points for the Gryffindor house, of course." ("base", xpos="far_left", ypos="head")
                    her ".........." ("annoyed", "base", "worried", "R")
                    gen "So... Are you okay with that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                    her "I suppose so..." ("annoyed", "narrow", "angry", "R")
                    nar "You pull out the small-sized butt plug and hand it to her."
                    gen "Fantastic! See you after class." ("base", xpos="far_left", ypos="head")

        "-Medium, magical-":
            if not her_buttplug_small1.unlocked:
                # Requires small butt plug event.
                gen "(I don't think she's ready for that yet.)" ("base", xpos="far_left", ypos="head")
                jump .plug_choice

            if not her_buttplug_medium1.unlocked:
                # First time with the medium-sized butt plug.
                gen "[name_hermione_genie], I want you to try something different today..." ("base", xpos="far_left", ypos="head")
                her "..........." ("soft", "base", "base", "mid",xpos="right",ypos="base")
                nar "You pull the medium-sized butt plug out from under your desk and place it in front of her."

                if states.her.level < 19:
                    gen "Today, I want you to wear a butt plug around the school." ("base", xpos="far_left", ypos="head")
                    her "You want me to...{w=0.4} What?!" ("angry", "wide", "worried", "mid")
                    gen "Wear a--" ("base", xpos="far_left", ypos="head")
                    her "[name_genie_hermione_], I can't believe you'd do this!" ("angry", "happyCl", "worried", "mid")
                    her "I'm leaving!" ("angry", "base", "worried", "R")

                    call her_walk(action="leave")

                    $ states.her.mood += 6

                    jump hg_butt_plugs_fail

                $ her_buttplug_medium1.unlock()
                $ ev_her_medium_plug.enqueue()

                her "And what is this supposed to be?" ("open", "squint", "base", "mid")
                gen "Can't you tell? It's a butt plug! They shouldn't be new to you at this point." ("base", xpos="far_left", ypos="head")
                her "..." ("annoyed", "narrow", "annoyed", "mid")
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                her "Surely, you can't be expecting me to have that large tail sticking out around the school!" ("annoyed", "base", "angry", "mid")
                gen "I can and do expect you to, unless you want our little trading game to come to a halt..." ("base", xpos="far_left", ypos="head")
                her "But it's so long! everyone will be able to see it!" ("normal", "happyCl", "worried", "mid")
                gen "That's the point, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                her "..........." ("angry", "happyCl", "worried", "mid",emote="sweat")
                her "I want a hundred points." ("annoyed", "base", "angry", "mid")

                menu:
                    "\"Fine, but I expect you to put it in now.\"":
                        $ current_payout = 100

                        her "What? Right now!?." ("angry", "happyCl", "worried", "mid")
                        her "In front of you?" ("angry", "wink", "base", "mid")
                        gen "You said you wanted a hundred points [name_hermione_genie]... It's more than fair." ("base", xpos="far_left", ypos="head")
                        her "*Ugh*...{w=0.4} Fine." ("angry", "narrow", "base", "down")
                        nar "You hand her the butt plug."
                        her "{size=-7}It's so big...{/size}" ("clench", "narrow", "base", "down")
                        nar "Hermione lifts her skirt and presses the butt plug against her asshole."
                        her "*Ughh*...{w=0.4} It's too big." ("shock", "happyCl", "worried", "mid")
                        her "It won't fit!" ("open", "happyCl", "worried", "mid")
                        gen "Try spitting on it." ("base", xpos="far_left", ypos="head")
                        her "........." ("angry", "narrow", "base", "down")

                        play sound "sounds/spit.ogg"

                        nar "She spits on the end of the butt plug and attempts to insert it again."

                        her "It doesn't work, It's just too bi--" ("angry", "base", "base", "mid")

                        stop music
                        play sound "sounds/gltch.ogg"
                        with hpunch
                        with kissiris

                        her "{size=+5}!!!!{/size}" ("shock", "wide", "base", "stare")

                        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

                        her "............." ("angry", "base", "base", "mid")
                        her "..." ("angry", "narrow", "base", "down")
                        her "Well...{w=0.4} I Better get to....{w=0.4} Class..." ("angry", "wink", "base", "mid")
                        gen "See you tonight [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                    "\"You'll get seventy points.\"":
                        $ current_payout = 70

                        her "*Hmph*..." ("annoyed", "narrow", "angry", "R")
                        her "Alright then, just don't expect me to show it to you!" ("angry", "base", "angry", "mid")
                        gen "As long as you wear it to class, you'll get your seventy points." ("base", xpos="far_left", ypos="head")
                        nar "You hand her the butt plug."
                        her "Will that be all [name_genie_hermione]?." ("annoyed", "narrow", "annoyed", "mid")
                        gen "Yes [name_hermione_genie], see you tonight." ("base", xpos="far_left", ypos="head")
                        her "{size=-5}(Not even a hundred points...){/size}" ("annoyed", "narrow", "angry", "R")
            else:
                # Repeat with medium butt plug
                $ ev_her_medium_plug.enqueue()
                if states.her.level < 21:
                    gen "Today my gracious request will be..." ("base", xpos="far_left", ypos="head")
                    her "........." ("angry", "base", "base", "mid",xpos="right",ypos="base")
                    gen "That you wear everyone's favourite magical butt plug to class!" ("base", xpos="far_left", ypos="head")
                    her "...{w=0.4} Again?" ("angry", "narrow", "base", "down")
                    gen "Why not? It will be the easiest fifty-five points you'll ever earn!" ("base", xpos="far_left", ypos="head")
                    her ".........." ("annoyed", "base", "worried", "R")
                    gen "Do you have a problem with it, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                    her "I suppose not..." ("annoyed", "narrow", "angry", "R")
                    nar "You hand her the butt plug."
                    gen "Fantastic! See you after class." ("base", xpos="far_left", ypos="head")

                elif states.her.level < 23:
                    nar "You pull out the butt plug."
                    gen "Ready to try out the phoenix again?" ("base", xpos="far_left", ypos="head")

                    if states.her.ev.buttplugs.medium_question == False:
                        $ states.her.ev.buttplugs.medium_question = True

                        her "Oh... I suppose so." ("soft", "happy", "base", "R",xpos="right",ypos="base")
                        her "But is it alright if I ask you something first?" ("open", "narrow", "worried", "down")
                        gen "What's that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                        her "Don't you worry about us getting caught?" ("annoyed", "base", "base", "mid")
                        gen "Why would I?" ("base", xpos="far_left", ypos="head")
                        her "Well, it's just that...{w=0.4} Making me wear something like this draws a lot of attention." ("open", "base", "worried", "R")
                        her "And what if someone realises that it's you who's making me do all this..." ("open", "base", "worried", "mid")
                        gen "You're expecting someone would ever suspect the great {i}Albis Dumbledorf{/i}?" ("base", xpos="far_left", ypos="head")
                        her "Well..." ("annoyed", "base", "worried", "R")
                        gen "Don't worry about it. If anyone asks, just tell them you're going through an exhibitionist stage." ("base", xpos="far_left", ypos="head")
                        her "..." ("annoyed", "base", "worried", "mid")
                        gen "Speaking of which..." ("base", xpos="far_left", ypos="head")
                        nar "You hand her the butt plug."
                        her "Right." ("base", "narrow", "worried", "down")
                        nar "Hermione lifts her skirt, and pushes it in gently, taking her time."

                    else:
                        her "Oh, alright then..." ("open", "narrow", "worried", "down",xpos="right",ypos="base")
                        her "*Ahem*...{w=0.4} If you pay me an additional ten points, I'll show you as I put it in." ("soft", "happy", "base", "R")
                        menu:
                            "\"Done\"":
                                $ current_payout += 10
                                her "Thank you [name_genie_hermione], you won't regret it..." ("open", "base", "base", "R")

                            "\"Five is all I can do.\"":
                                $ current_payout += 5
                                her "*Hmm*... Alright, fine..." ("annoyed", "narrow", "angry", "R")
                                her "But you better appreciate it..." ("base", "squint", "base", "mid")
                                gen "I'm sure I will." ("base", xpos="far_left", ypos="head")

                        nar "You hand her the butt plug."
                        her "Well... Here goes..." ("base", "narrow", "worried", "down")
                        nar "Hermione lifts her skirt, and pushes it in gently, taking her time."

                    her "{heart}{heart}{heart}*Ah*{heart}{heart}{heart}..." ("grin", "narrow", "annoyed", "up")
                    her "I better...{w=0.4}*Ah*...{w=0.4} Head to class..." ("soft", "happy", "base", "R")
                    gen "See you tonight, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                    her "{size=-5}({heart}So...{w=0.4} Good...{heart}){/size}" ("grin", "narrow", "annoyed", "up")

                else:
                    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    gen "What do you think about wearing a butt pl--?" ("base", xpos="far_left", ypos="head")
                    her "I'll do it." ("grin", "base", "base", "R",xpos="right",ypos="base")
                    gen "You're eager. I haven't even said which one yet..." ("base", xpos="far_left", ypos="head")
                    her "Oh... Can it be the one with the phoenix tail?" ("open", "narrow", "worried", "down")
                    her "Please..." ("soft", "happy", "base", "R")
                    gen "Well, seeing as how you asked so nicely..." ("base", xpos="far_left", ypos="head")
                    nar "You hand her the butt plug."
                    nar "Hermione lifts her skirt giving you a full view as she inserts it."
                    her "{heart}*Ah*{heart}..." ("grin", "narrow", "annoyed", "up")
                    her "Thank you [name_genie_hermione]!" ("open", "base", "base", "R")
                    her "{size=-5}({heart}it feels so good... I might have to buy my own...{heart}){/size}" ("grin", "narrow", "annoyed", "up")

        "-Large, magical-":
            if not her_buttplug_medium1.unlocked or not states.her.status.anal:
                # Requires medium butt plug event.
                gen "(I don't think she's ready for that yet.)" ("base", xpos="far_left", ypos="head")
                jump .plug_choice

            if not her_buttplug_large1.unlocked:
                # First time with large butt plug
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

                gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                gen "What do you think about wearing a butt pl--?" ("base", xpos="far_left", ypos="head")
                her "I'll do it." ("grin", "base", "base", "R",xpos="right",ypos="base")
                gen "You're eager. I haven't even said which one yet..." ("base", xpos="far_left", ypos="head")
                her "Oh... Can it be the big one... With the long tail..." ("open", "narrow", "worried", "down")
                her "Please..." ("soft", "happy", "base", "R")
                gen "Well, seeing as how you did ask for the big one..." ("base", xpos="far_left", ypos="head")
                nar "You hand her the large-sized butt plug."
                her "!!!" ("angry", "narrow", "base", "down")
                her "This isn't the one I meant [name_genie_hermione]..." ("angry", "narrow", "base", "down")
                gen "Didn't you ask for the big one?" ("base", xpos="far_left", ypos="head")
                her "I did--" ("grin", "narrow", "annoyed", "up")
                gen "Well, this is the {b}big{/b} one." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "But, [name_genie_hermione]... I don't even think this will fit." ("disgust", "base", "base", "mid")
                gen "Never say never!" ("base", xpos="far_left", ypos="head")
                her "You can't be serious!" ("scream", "narrow", "worried", "down")
                her "This thing is ridiculous!" ("open", "closed", "base", "mid")
                gen "You said the same thing about the smaller one." ("base", xpos="far_left", ypos="head")
                her "That was different..." ("disgust", "narrow", "base", "down")
                gen "Come off it." ("base", xpos="far_left", ypos="head")

                gen "You did great, taking my cock up your ass!" ("grin", xpos="far_left", ypos="head")

                her @ cheeks blush "[name_genie_hermione]!" ("shock", "wide", "base", "mid")
                gen "Come on..." ("base", xpos="far_left", ypos="head")
                her "This is too much [name_genie_hermione]! even your cock isn't this {b}thick{/b}..." ("open", "narrow", "angry", "R")
                gen "Nothing a little spit can't solve!" ("base", xpos="far_left", ypos="head")
                her "Don't be ridiculous! This is beyond spit!" ("open", "closed", "base", "mid")
                her "Unless you have some sort of actual {i}lubricant{/i} in your possession, I don't think I'll be letting this thing anywhere near my--" ("open", "base", "angry", "mid")

                menu:
                    "-Use anal lube-" if anal_lube_ITEM.owned > 0: #Success

                        $ her_buttplug_large1.unlock()
                        $ ev_her_large_plug.enqueue()

                        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                        gen "Well, it just so happens that I recently came across the solution to your problem." ("base", xpos="far_left", ypos="head")
                        her "The solution?" ("disgust", "wink", "base", "mid")
                        gen "Here." ("base", xpos="far_left", ypos="head")

                        call give_gift("You hand hermione the jar of anal lubricant.",anal_lube_ITEM)

                        her "!!!" ("clench", "wide", "base", "stare")
                        her "I wasn't being serious, [name_genie_hermione]!" ("scream", "base", "angry", "mid")
                        gen "Didn't you say you needed some lube to do it? I've got you some, right here." ("base", xpos="far_left", ypos="head")
                        her "Yes, but I didn't actually expect you to have a jar of lube in your desk!" ("open", "narrow", "angry", "R")
                        gen "Really? You didn't think I'd foresee this occasion?" ("base", xpos="far_left", ypos="head")
                        her "..." ("annoyed", "base", "angry", "mid")
                        her "*Ugh*...{w=0.4} fine. I'll {b}try{/b} to fit it in." ("disgust", "narrow", "worried", "down")
                        her "But I'm not promising anything!" ("open", "closed", "base", "mid")
                        gen "That's all I ask." ("base", xpos="far_left", ypos="head")
                        nar "You hand Hermione the large butt plug."
                        her "I still don't think this is going to work..." ("open", "base", "base", "mid")
                        nar "Hermione slowly coats the massive butt plug with lube."
                        her "There's barely even enough here to cover it..." ("open", "narrow", "worried", "down")
                        her "(There's no way this thing will fit.)" ("disgust", "narrow", "base", "down")
                        nar "Hermione slowly places the lubed up butt plug to her anus."
                        her "I'm telling you, [name_genie_hermione], this isn't going to--" ("open", "closed", "base", "mid")
                        her @ cheeks blush "{size=+10}!!!{/size}" ("soft", "wide", "base", "stare",trans=hpunch)
                        her "{size=+10}It's moving!{/size}" ("disgust", "happyCl", "worried", "mid")
                        gen "Really?" ("base", xpos="far_left", ypos="head")
                        her "{size=+5}*Ugh*...{/size}" ("disgust", "happyCl", "worried", "mid")
                        her "{size=+5}It's forcing its way inside me....{/size}" ("open", "wide", "worried", "shocked")
                        her "*Ah*..." ("shock", "happyCl", "worried", "mid")
                        her "It's...{w=0.3} It's..." ("open", "wide", "base", "stare")

                        play sound "sounds/bottle.ogg"

                        her @ cheeks blush "" ("soft", "narrow", "annoyed", "up")
                        call ctc

                        her @ cheeks blush "{size=+5}incredible!{/size}" ("soft", "narrow", "annoyed", "up")

                        her "............." ("disgust", "narrow", "annoyed", "up")
                        gen "Are you alright, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                        her ".........................." ("soft", "narrow", "base", "up")
                        her "*Ah*... Y--{w=0.2} yes..." ("open", "narrow", "base", "mid_soft")
                        gen "Fantastic! I'll see you after class then." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "............." ("disgust", "narrow", "worried", "down")
                        nar "Hermione slowly leaves your office, barely able to walk in a straight line."

                    "-Use anal lube-" (style="disabled") if anal_lube_ITEM.owned == 0: #Fail, wears small or medium-sized instead

                        gen "I'm afraid I do not have that..." ("base", xpos="far_left", ypos="head")
                        her "Well then, I think I better be off to class then." ("open", "closed", "base", "mid")
                        her @ cheeks blush "{size=-2}unless {size=-2}you {size=-2}have {size=-2}the {size=-2}smaller {size=-2}one?{/size}{/size}{/size}{/size}{/size}{/size}{heart}" ("soft", "narrow", "base", "R_soft")
                        menu:
                            "-Take out the small-sized butt plug-":
                                $ ev_her_small_plug.enqueue()
                                gen "It just so happens that I do!" ("grin", xpos="far_left", ypos="head")
                                nar "You hand her the small-sized butt plug."
                            "-Take out the medium-sized butt plug-":
                                $ ev_her_medium_plug.enqueue()
                                gen "It just so happens that I do!" ("grin", xpos="far_left", ypos="head")
                                nar "You hand her the medium-sized butt plug."
                                her @ cheeks blush "This, this isn't the small one." ("open", "narrow", "base", "down")
                                gen "It's smaller in comparison..." ("grin", xpos="far_left", ypos="head")
                                her @ cheeks blush "True...{w=0.4} Here I go then..." ("soft", "narrow", "base", "mid")

                        her @ cheeks blush "{heart}*Ah*{heart}..." ("silly", "narrow", "annoyed", "up")
                        her @ cheeks blush "Thank you, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
                        her @ cheeks blush "{size=-5}({heart}it feels so good... I might have to buy my own...{heart}){/size}" ("soft", "narrow", "annoyed", "up")
                        hide hermione_main
                        with d3
                        pause.2


                        gen "(Maybe I could buy some lube to help me with my--{w=0.2} *Ahem*, {i}her{/i} friction problems...)" ("base", xpos="far_left", ypos="head")

            else:
                $ ev_her_large_plug.enqueue()
                # Repeat with large butt plug
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                gen "How do you feel about wearing another butt plug to class today?" ("base", xpos="far_left", ypos="head")
                her "..." ("base", "base", "base", "R",xpos="right",ypos="base")
                her "Which one?" ("grin", "base", "base", "mid")
                gen "How about the big one again?" ("base", xpos="far_left", ypos="head")
                her "Really?" ("open", "narrow", "worried", "down")
                her "Do I have to?" ("soft", "happy", "base", "R")
                gen "You didn't seem to hate wearing it last time..." ("base", xpos="far_left", ypos="head")
                her "..." ("open", "narrow", "worried", "down")
                her "{size=-5}alright then...{/size}" ("open", "narrow", "worried", "down")
                nar "You hand her the butt plug."
                nar "You watch it magically wriggle its way inside her eager butthole."

                her "{heart}*Ah*{heart}..." ("grin", "narrow", "annoyed", "up")
                gen "(Didn't even need any lube...)" ("base", xpos="far_left", ypos="head")
                her "Thank you, [name_genie_hermione]!" ("base", "narrow", "base", "mid_soft")
                her "{size=-5}({heart}it feels so good... I might have to buy my own...{heart}){/size}" ("soft", "narrow", "annoyed", "up")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_butt_plugs_small_return:

    call her_walk(action="enter", xpos="mid", ypos="base")

    if states.her.level < 19:
        random:
            block:
                # Got distracted
                gen "[name_hermione_genie], how did it go?" ("base", xpos="far_left", ypos="head")
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                her "It was awful... of course..." ("annoyed", "squint", "angry", "mid",xpos="right",ypos="base")
                gen "Just tell me what happened, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                her "I've never been so uncomfortable in my life [name_genie_hermione]!" ("disgust", "narrow", "base", "mid_soft")
                her "I wasn't able to focus on anything all day!" ("annoyed", "narrow", "annoyed", "mid")
                gen "Why's that?" ("base", xpos="far_left", ypos="head")
                her "Whenever I was sitting down in class it just kept prodding me..." ("annoyed", "narrow", "angry", "R")
                her "So naturally I had to adjust the way I was sitting, [name_genie_hermione]..."
                her "but that just made it worse..." ("annoyed", "narrow", "angry", "R")
                gen "Do you think anyone else noticed you?" ("base", xpos="far_left", ypos="head")
                her "I've got no idea..." ("annoyed", "narrow", "annoyed", "mid")
                her "I could hardly think straight... Let alone pay attention to anyone around me." ("annoyed", "narrow", "annoyed", "mid")
                gen "So it felt good then?" ("base", xpos="far_left", ypos="head")
                her "Good?" ("open", "base", "base", "mid")
                her "If you call getting your butt prodded all day good..." ("annoyed", "narrow", "worried", "down")
                her "Then sure." ("annoyed", "narrow", "annoyed", "up")
                her "Also... Being this distracted during class could really damage my grades." ("angry", "base", "base", "mid")
                gen "I wouldn't worry about that. Just think of Gryffindor!" ("base", xpos="far_left", ypos="head")
                her "Speaking of Gryffindor..." ("annoyed", "narrow", "annoyed", "mid", xpos="right",ypos="base",trans=fade)
                gen "Oh yes, you're quite right." ("base", xpos="far_left", ypos="head")

            block:
                # Flashed a few Ravenclaw girls by accident
                gen "[name_hermione_genie], how did it go?" ("base", xpos="far_left", ypos="head")
                her "It went well, [name_genie_hermione]..." ("open", "base", "base", "mid",xpos="right",ypos="base")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "Barely anybody noticed that I was wearing it..."
                her @ cheeks blush "... Except for a few girls from Ravenclaw..." ("open", "base", "base", "mid")
                gen "What happened?" ("base", xpos="far_left", ypos="head")
                her "I was walking down the hall, on my way to potions class..." ("open", "closed", "base", "mid")
                her "And suddenly a gust of wind came and blew my skirt up..." ("upset", "wink", "base", "mid")
                gen "A gust of wind? inside?" ("base", xpos="far_left", ypos="head")
                her "It must have been from a window..." ("soft", "base", "base", "R")
                her "Anyway... The three girls walking behind me may have... seen it." ("open", "narrow", "worried", "down")
                gen "How do you know?" ("base", xpos="far_left", ypos="head")
                her "I heard them giggling afterwards..." ("clench", "narrow", "base", "down")
                gen "Maybe they had just heard a funny joke." ("base", xpos="far_left", ypos="head")
                her "..." ("clench", "narrow", "base", "mid")
                gen "In any case... Sounds like a job well done." ("base", xpos="far_left", ypos="head")

            block:
                # Caught by Moaning Myrtle
                gen "[name_hermione_genie], how did it go?" ("base", xpos="far_left", ypos="head")
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                her "Awful, [name_genie_hermione]. Simply awful..." ("scream", "happyCl", "worried", "mid",xpos="right",ypos="base")
                gen "What happened?" ("base", xpos="far_left", ypos="head")
                her "Moaning Myrtle happened!" ("normal", "happyCl", "worried", "mid")
                gen "{i}Moaning Mittle{/i}?" ("base", xpos="far_left", ypos="head")
                her "That pesky little ghost!" ("annoyed", "narrow", "angry", "R")
                her "This thing left me so frustrated that during my free period I went to the girls toilets to--" ("annoyed", "narrow", "angry", "R")
                her "*Ahem*... Relieve myself..." ("annoyed", "base", "worried", "R")
                her "When all of a sudden that annoying ghost poked her head through the door!" ("scream", "closed", "angry", "mid")
                her "As if it weren't bad enough that she saw me..." ("open", "narrow", "worried", "down")
                her "She then started yelling \"Hermione has a butt plug\" to everyone in the toilets!" ("scream", "base", "angry", "mid",emote="angry")
                her "Luckily the stalls were empty! Imagine if they weren't!" ("annoyed", "narrow", "annoyed", "mid")
                gen "Well, it certainly sounds like you've earned your points." ("base", xpos="far_left", ypos="head")

    elif states.her.level < 21:
        random:
            block:
                # Flashed Luna in the library
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "Of course." ("open", "base", "base", "mid",xpos="right",ypos="base")
                gen "Excellent... So, did anyone notice?" ("base", xpos="far_left", ypos="head")
                her "*Ehm*... Well..." ("base", "narrow", "worried", "down")
                her "I might've shown someone..." ("base", "narrow", "base", "mid_soft")
                her "I was in the library fetching some books when Luna started talking at me..."
                her "I didn't see her at first, but she had been reading at one of the desks."
                her "She just started chatting at me like without even a hello like she usually does." ("open", "base", "base", "R")
                her "Talking about something nonsensical as always..." ("soft", "base", "base", "R")
                her "Well, during her blabbering she suddenly went quiet and when I looked over, she was staring at my butt." ("soft", "base", "base", "mid")
                gen "Buttsted!" ("base", xpos="far_left", ypos="head")
                her "Yes... Well, at first I was hoping that I got away with it... Until... Well..." ("base", "narrow", "base", "R")
                gen "Well?" ("base", xpos="far_left", ypos="head")
                her "Well, I figured that even if she saw it..."
                her "It wouldn't matter, as no one would believe her..."
                gen "Right..." ("base", xpos="far_left", ypos="head")
                her "So I thought I might as well give her a proper look... And I feigned dropping my quill..." ("grin", "base", "base", "R")
                gen "Go on..." ("base", xpos="far_left", ypos="head")
                her "Then I turned around in front of her..." ("base", "narrow", "worried", "down")
                her "And bent over..."
                her "Giving her a full view..." ("base", "narrow", "base", "up")
                gen "I see..." ("base", xpos="far_left", ypos="head")
                gen "So she saw how the tail was attached?" ("base", xpos="far_left", ypos="head")
                her "*Hmm*... Maybe, [name_genie_hermione]..." ("soft", "happy", "base", "R")
                her "She was too stunned to say anything."
                gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
                her "Knowing her, she might've just thought I grew a tail or something..." ("base", "narrow", "base", "mid_soft")
                gen "Either way, it sounds like you've earned your points and then some." ("base", xpos="far_left", ypos="head")

            block:
                # Couldn't focus and touched herself during class
                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "I did, [name_genie_hermione]..." ("open", "closed", "base", "mid",xpos="right",ypos="base")
                her "Although I'm still not sure how I feel about all of this..." ("annoyed", "base", "worried", "R")
                her "I was barely able to pay attention during class..." ("annoyed", "base", "worried", "R")
                her "I don't think I could even tell you which potion we were taught today..." ("open", "base", "base", "mid")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "Me, Hermione Granger..." ("open", "narrow", "worried", "down")
                her "Not learning in class." ("angry", "narrow", "base", "down")
                gen "You could always try relieving yourself in between lessons." ("base", xpos="far_left", ypos="head")
                her "Oh, I've tried that... But it doesn't work..." ("angry", "base", "base", "mid")
                her "It just makes the next class even more difficult..."
                her "After potions finished, I went to my room to... calm myself..." ("open", "base", "base", "R")
                her "But it just made Herbology worse..." ("open", "narrow", "worried", "down")
                her "I just had to touch myself during the later half of the class..." ("clench", "narrow", "base", "down")
                gen "During class?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Yeah...{w=0.4} Do you...{w=0.4} *Ehm*... Do you think anyone noticed, [name_genie_hermione]?" ("open", "happy", "base", "mid")

                menu:
                    "\"Noticed? Of course not, [name_hermione_genie]!\"":
                        her @ cheeks blush ".............." ("base", "base", "base", "R")
                        her "Hopefully you're right, [name_genie_hermione]..." ("base", "narrow", "worried", "down")
                        her "I did try to be as discreet as possible..."
                        her "I don't think..." ("soft", "narrow", "annoyed", "up")
                        her "Well, I {b}hope{/b} I wasn't making too much noise..." ("grin", "base", "base", "R")
                        her "[name_genie_hermione], can I get paid now, please?" ("base", "narrow", "base", "mid_soft",xpos="right",ypos="base",trans=fade)
                        her "......"

                    "\"Of course they noticed!\"":
                        gen "Do you honestly believe that no one noticed you touching yourself?" ("base", xpos="far_left", ypos="head")
                        her @ tears soft_blink "I was afraid that you would say that, [name_genie_hermione]..." ("mad", "happyCl", "worried", "mid")
                        gen "To think that you'd do such a thing, surrounded by your classmates..." ("base", xpos="far_left", ypos="head")
                        her @ tears soft_blink "........" ("mad", "happyCl", "worried", "mid")
                        gen "You're lucky that nobody called you out on it..." ("base", xpos="far_left", ypos="head")
                        her @ tears soft "[name_genie_hermione], can I get paid now, please?" ("angry", "base", "base", "mid",xpos="right",ypos="base",trans=fade)

                gen "Certainly." ("base", xpos="far_left", ypos="head")

            block:
                # Nothing happened
                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "Yes, [name_genie_hermione]. I did." ("open", "closed", "base", "mid",xpos="right",ypos="base")
                gen "Great. Tell me more." ("base", xpos="far_left", ypos="head")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "Well, there's not much to tell..." ("open", "base", "base", "mid")
                her "I attended classes..."
                her "Tried to take notes."
                her "All in all it was a fairly regular day..."
                her "Well as regular as it could have been with a plug up my butt." ("annoyed", "narrow", "angry", "R")
                gen "And nobody noticed?" ("base", xpos="far_left", ypos="head")
                her "I don't think so, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
                gen "Well I suppose something interesting can't happen every day." ("base", xpos="far_left", ypos="head")
                her "..." ("annoyed", "base", "base", "R",xpos="right",ypos="base",trans=fade)

    else:
        random:
            block:
                # Pleasured herself in class
                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "Yes I did, [name_genie_hermione]." ("base", "base", "base", "mid",xpos="right",ypos="base")
                gen "Well? How was your day?" ("base", xpos="far_left", ypos="head")
                her "Great, [name_genie_hermione]... Just... great." ("base", "narrow", "base", "up")
                gen "Go on..." ("base", xpos="far_left", ypos="head")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "I managed to work out how to deal with this thing being inside me all day..." ("soft", "happy", "base", "R")
                gen "Really? Do tell..." ("base", xpos="far_left", ypos="head")
                her "At first, I was going about it the wrong way..." ("open", "base", "base", "R")
                her "I just tried to ignore it." ("open", "closed", "base", "mid")
                her "And to pay attention in class..."
                her "But that didn't work at all..." ("upset", "wink", "base", "mid")
                her "I was just too--{w=0.4} Distracted..." ("base", "narrow", "worried", "down")
                her "So I thought to myself that I've just got to focus on it..." ("base", "narrow", "base", "up")
                her "Block out everything else..." ("base", "narrow", "worried", "down")
                her "... Embrace it..." ("grin", "narrow", "base", "dead")
                gen "And how did you do that?" ("base", xpos="far_left", ypos="head")
                her "Well, at first, I tried rocking my hips, which worked for a bit..." ("base", "narrow", "base", "mid_soft")
                her "But after some time of doing so, it wasn't really enough..." ("base", "narrow", "base", "mid_soft")
                her "That's when I finally tried sitting right on the edge of my chair while rocking my hips..." ("base", "squint", "base", "mid")
                her "{heart}{heart}{heart}" ("soft", "narrow", "annoyed", "up")
                gen "So you worked out how to pleasure yourself in class." ("base", xpos="far_left", ypos="head")
                her "I did, [name_genie_hermione]..." ("base", "narrow", "worried", "down")
                her "Although I worry that if I do it too often it will really start to affect my grades..."
                gen "Well, I'm sure that missing a class or two isn't enough for you not to be able to catch up." ("base", xpos="far_left", ypos="head")
                her "One or two?" ("angry", "wink", "base", "mid")
                gen "Yes, I--" ("base", xpos="far_left", ypos="head")
                gen "Hold on, you're saying that you spent all of today's classes pleasuring yourself?" ("base", xpos="far_left", ypos="head")
                her ".........." ("soft", "narrow", "annoyed", "up")
                her "" (xpos="right",ypos="base",trans=fade)
                gen "Nice work, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

            block:
                # Colin Creevey took an upskirt photo
                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "Yes I did, [name_genie_hermione]." ("base", "base", "base", "mid", xpos="right", ypos="base")
                her "Although...{w=0.4} *Ehm*..." ("open", "base", "worried", "mid")
                gen "Yes?" ("base", xpos="far_left", ypos="head")
                her "Well, I may have gotten a bit more attention than I had hoped for..." ("disgust", "narrow", "base", "down")
                her "..............." ("clench", "narrow", "base", "down")
                gen "Right, so tell me what happened." ("base", xpos="far_left", ypos="head")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "I might have had a few photos taken..." ("open", "narrow", "worried", "down")
                gen "Photos?" ("base", xpos="far_left", ypos="head")
                her "Well, I was in the library, minding my own business..." ("annoyed", "closed", "base", "mid")
                her "I was browsing the bookshelves and saw that they'd finally acquired a copy of Zygmunt Budge's book of potions."
                her "And I sort of forgot I had the plug in and everything."
                her "As it was on the bottom shelf, I quickly kneeled down to grab it..." ("annoyed", "base", "base", "mid")
                her "When all of a sudden I heard the flash of a camera!" ("annoyed", "narrow", "angry", "R")
                her "I turned around and there was Colin Creevey..."
                her "With the biggest grin on his face!"
                gen "You let your photo be taken?!" ("base", xpos="far_left", ypos="head")
                her "I didn't let it happen! He did it without my consent!" ("scream", "base", "angry", "mid", emote="angry")
                her "Luckily I managed to grab him and made him promise not to show anyone the photo..." ("open", "narrow", "worried", "down")
                her "... In exchange, I did have to let him take a few more though..."
                gen "You... Let him take more pictures? Wouldn't that make it worse?" ("base", xpos="far_left", ypos="head")
                her "Of course not [name_genie_hermione], Gryffindors are always true to their word!" ("annoyed", "closed", "base", "mid")
                her "Although the thought did cross my mind...." ("open", "narrow", "worried", "down")
                her "If he released them then I'm sure that any time someone saw me they'd try and see whether or not I had a plug inside me..." ("base", "narrow", "worried", "down")
                her "In any case, I'm certain that he won't release any of those photos!" ("open", "closed", "base", "mid")
                gen "If you say so..." ("base", xpos="far_left", ypos="head")
                her "He's not an idiot... He'd know that if he were to spread those photos around, it would tarnish not just my reputation but Gryffindor as a whole." ("clench", "narrow", "base", "down")
                her "" ("base", "narrow", "base", "mid_soft")
                gen "Very well... In that case, it sounds like a job well done [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

            block:
                # Flashed students on her way to class
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "Yes, I did [name_genie_hermione]..." ("base", "squint", "base", "mid", xpos="right", ypos="base")
                gen "Did anyone notice?" ("base", xpos="far_left", ypos="head")
                her "*Hmm*...{w=0.4} Maybe..."
                her "I may have gotten a little too confident..."
                gen "Do tell..." ("base", xpos="far_left", ypos="head")
                her "Well, I was walking to divination class and ended up in front of a group of students..." ("open", "closed", "base", "mid")
                her "And seeing as how they were behind me on the stairs, they may have been able to... See it." ("base", "narrow", "base", "mid_soft")
                gen "You're not expecting me to grant you extra points for showing them, are you?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Of course not, [name_genie_hermione]." ("base", "base", "base", "R")
                gen "Then why do it?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I don't know... As I said, I was probably being a bit too confident..." ("open", "happy", "base", "mid")
                gen "Well, hopefully they didn't see it then." ("base", xpos="far_left", ypos="head")
                her "*Hmm*...{w=0.4} Well, I wouldn't count on it... As I couldn't help looking back to find out..." ("grin", "narrow", "base", "dead")
                her "And...{w=0.4} Well...{w=0.4} Judging by their eyes, they probably did see it..." ("soft", "narrow", "annoyed", "up")
                gen "So...{w=0.4} What you're saying is that you wanted to make sure that they saw it?" ("base", xpos="far_left", ypos="head")
                gen "Sounds to me like you're enjoying students seeing you like this..." ("base", xpos="far_left", ypos="head")
                her "If that's what you want to believe..." ("open", "base", "base", "R")
                gen "Well done, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her "" ("base", "narrow", "worried", "down")

    $ gryffindor += current_payout
    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    call her_walk(action="leave")

    jump end_hermione_event

label hg_butt_plugs_medium_return:

    call her_walk(action="enter", xpos="mid", ypos="base")

    if not states.her.ev.buttplugs.magic_known:
        jump .magic_show

    if states.her.level <= 21:
        random:
            block:
                # Stood in front during potions class
                gen "[name_hermione_genie], how's your day been?" ("base", xpos="far_left", ypos="head")
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                her "Awful...{w=0.4} Simply awful..." ("annoyed", "squint", "angry", "mid",xpos="right",ypos="base")
                gen "What happened?" ("base", xpos="far_left", ypos="head")
                her "Professor Snape happened, [name_genie_hermione]!" ("annoyed", "narrow", "angry", "R")
                her "I've never been so embarrassed in my life!" ("annoyed", "narrow", "annoyed", "mid")
                gen "Severus? What did he do this time?" ("base", xpos="far_left", ypos="head")
                her "Well, apparently I dared to suggest there was a better way to properly crush a Sopophorous bean..." ("annoyed", "narrow", "angry", "R")
                her "So of course, he made me stand in front of the class and show them \"how it's done\"..."
                gen "What's wrong with that?" ("base", xpos="far_left", ypos="head")
                her "He obviously knew about my situation because he made me do it facing away from the class..." ("annoyed", "narrow", "annoyed", "mid")
                gen "You sure? How could he have known?" ("base", xpos="far_left", ypos="head")
                her "I don't know, you tell me! Why else would he make me do that?" ("disgust", "narrow", "base", "down")
                gen "..." ("base", xpos="far_left", ypos="head")
                gen "So, do you think anyone noticed?" ("base", xpos="far_left", ypos="head")
                her "I--{w=0.2} I don't know... I was trying my best to not let it slip out as my legs were shaking, and to crush the bean as fast as possible..." ("clench", "narrow", "base", "down")
                gen "At least you got to show how a lady handles a bean." ("base", xpos="far_left", ypos="head")
                her "*Hmph*..." ("annoyed", "narrow", "base", "down")
                gen "Well, it sounds like you earned your points." ("base", xpos="far_left", ypos="head")
                her "......." ("annoyed", "narrow", "worried", "down")

            block:
                # Flashed some Hufflepuffs
                gen "[name_hermione_genie], how did it go?" ("base", xpos="far_left", ypos="head")
                her "It went well, [name_genie_hermione]..." ("open", "base", "base", "mid",xpos="right",ypos="base")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "A group of students from Hufflepuff even complimented me on it..."
                her "... They said that it looked cute..." ("grin", "base", "base", "R")
                gen "Did anything else happen?" ("base", xpos="far_left", ypos="head")
                her "Well, seeing as how they were so nice..." ("base", "narrow", "worried", "down")
                her "I might have flicked my skirt up for them..." ("soft", "happy", "base", "R")
                gen "You showed it to them?" ("base", xpos="far_left", ypos="head")
                her "Well, they were so kind and all..." ("open", "base", "base", "R")
                her "And they could already see most of it..." ("base", "narrow", "worried", "down")
                gen "Did they say anything else about it?" ("base", xpos="far_left", ypos="head")
                her "No... But the looks on their faces said a lot..." ("base", "narrow", "base", "mid_soft")
                gen "Well, it sounds like a job well done..." ("base", xpos="far_left", ypos="head")

            block:
                # Cat swatting it
                label .magic_show:

                $ states.her.ev.buttplugs.magic_known = True

                gen "[name_hermione_genie], how did it go?" ("base", xpos="far_left", ypos="head")
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                her "What on earth did you do to this thing?!" ("scream", "happyCl", "worried", "mid",xpos="right",ypos="base")
                gen "What happened?" ("base", xpos="far_left", ypos="head")
                her "Why did you not tell me this \'thing\' was cursed!" ("normal", "happyCl", "worried", "mid")
                gen "Cursed?" ("base", xpos="far_left", ypos="head")
                her "It vibrates!" ("annoyed", "narrow", "angry", "R")
                gen "Really?" ("base", xpos="far_left", ypos="head")
                her "When something else touches it..." ("annoyed", "narrow", "angry", "R")
                gen "Wouldn't your skirt set it off then?" ("base", xpos="far_left", ypos="head")
                her "I think it has to be alive..." ("annoyed", "base", "worried", "R")
                her "All I know is that when my cat Crookshanks swatted at it, it went off!" ("scream", "closed", "angry", "mid")
                her "It was ridiculous! I was barely able to stand..." ("open", "happyCl", "worried", "mid")
                her "The vibrations were so intense that my knees gave out, and I collapsed onto my bed!" ("angry", "narrow", "base", "down")
                gen "(Is she making this up?)" ("base", xpos="far_left", ypos="head")
                gen "Well... I'll be sure to inspect it thoroughly and remove this curse..." ("base", xpos="far_left", ypos="head")
                her "Oh... *Ehm*... No, it's fine really [name_genie_hermione], you can leave it the way it is." ("clench", "narrow", "base", "down")
                gen "Alright then... good work [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    elif states.her.level <= 23:
        random:
            block:
                # Luna played with it in the library

                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                gen "[name_hermione_genie], did you have fun?" ("base", xpos="far_left", ypos="head")
                her "*Ehm*... I suppose you could say that." ("base", "narrow", "worried", "down",xpos="right",ypos="base")
                gen "Anything interesting happen?" ("base", xpos="far_left", ypos="head")
                her "Yes... Well, I might've... *Ehm*..." ("base", "narrow", "worried", "down")
                her "Had someone..." ("base", "happyCl", "worried", "mid")
                her "Touch it." ("base", "narrow", "base", "mid_soft")
                gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
                her "It was Luna Lovegood." ("grin", "base", "base", "R")
                her "We ended up sitting next to each other in the library." ("soft", "base", "base", "R")
                her "And we were talking about school, clothes..."
                her "Well, I was, she was going on about--"
                gen "Yes, yes, spit it out..." ("base", xpos="far_left", ypos="head")
                her "Well, she said that she thought my tail was cute..." ("grin", "base", "base", "R")
                gen "Go on..." ("base", xpos="far_left", ypos="head")
                her "Then she asked so politely if she could touch it..." ("base", "narrow", "worried", "down")
                her "I could hardly say no..." ("open", "base", "base", "R")
                her "So I... Let her spend the next ten minutes or so... Toying with it..." ("soft", "happy", "base", "R")
                gen "I see..." ("base", xpos="far_left", ypos="head")
                her "I don't think she realised and how it made me feel..." ("soft", "narrow", "annoyed", "up")
                her "It felt so good that it was hard to keep it in." ("soft", "narrow", "annoyed", "up")
                gen "Keep what in?" ("base", xpos="far_left", ypos="head")
                her "My voice..."
                gen "Right..." ("base", xpos="far_left", ypos="head")
                gen "Well, it sounds like you've earned your points and then some." ("base", xpos="far_left", ypos="head")

            block:
                # Friend played with it

                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "I did, [name_genie_hermione]." ("open", "closed", "base", "mid",xpos="right",ypos="base")
                her "Only... *Ehm*..." ("grin", "base", "base", "R")
                gen "What is it this time [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                her "Well... One of my friends..." ("base", "base", "base", "mid")
                her @ cheeks blush "Well, I told her about the tail..." ("base", "base", "base", "R")
                her "And how it works..."
                gen "Just say it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her "Well, we decided to skip Herbology class together..." ("open", "base", "base", "R")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "And then she sort of grabbed it..." ("grin", "narrow", "annoyed", "up")
                her "And she just played with it aggressively..." ("grin", "narrow", "base", "dead")
                her "I was a mess afterwards..."
                gen "And did you return the favour?" ("grin", xpos="far_left", ypos="head")

                if states.her.status.public_kissing:
                    her @ cheeks blush "*Err*... maybe..." ("open", "happy", "base", "mid")
                    gen "What did you do?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Well, I don't want to say too much [name_genie_hermione]." ("base", "base", "base", "R")
                    her "But after she saw what it was doing to me..."
                    her "She insisted that I let her have a go..."
                    her "And that's all I'll say..." ("base", "narrow", "worried", "down")
                    gen "*Hmm*... I suppose you've earned your points [name_hermione_genie], even if you are secretive about it..." ("base", xpos="far_left", ypos="head")
                else:
                    her "... No." ("open", "narrow", "worried", "down")
                    gen "Why not?" ("base", xpos="far_left", ypos="head")
                    her "Well, I don't mind letting her touch the tail [name_genie_hermione]." ("annoyed", "base", "base", "mid")
                    her "But anything else..."
                    gen "Very good [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

            block:
                # Called a slut by Slytherin girls
                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "Yes, [name_genie_hermione]. I did." ("annoyed", "narrow", "angry", "R",xpos="right",ypos="base")
                gen "Great. Tell me more." ("base", xpos="far_left", ypos="head")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "Well, there's not much to tell..." ("open", "narrow", "worried", "down")
                her "I attended classes..."
                her "Studied for the upcoming potions test..."
                her "It was a normal day except for coming across a group of nasty Slytherin tramps..." ("annoyed", "narrow", "angry", "R")
                her "I was minding my business on the way to class when they called me a \"butt slut\"." ("angry", "narrow", "base", "down")
                gen "I see... So, you gave them a piece of your mind?" ("base", xpos="far_left", ypos="head")
                her "And sink to their level?" ("annoyed", "narrow", "angry", "R")
                gen "Well, I suppose it's for the best." ("base", xpos="far_left", ypos="head")


    elif states.her.level >= 24:
        random:
            block:
                # Groped by students

                gen "[name_hermione_genie], how was your day?" ("base", xpos="far_left", ypos="head")
                her "Awful... I was attacked by a group of rabid students, [name_genie_hermione]." ("scream", "closed", "angry", "mid",xpos="right",ypos="base")
                gen "Attacked? By How many?" ("base", xpos="far_left", ypos="head")
                her "Six!" ("annoyed", "base", "angry", "mid")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "Although maybe the word \"attacked\" is a slight exaggeration... They cornered me at least." ("open", "base", "worried", "R")
                gen "So, what happened?" ("base", xpos="far_left", ypos="head")
                her "Well, I was sitting in the library, minding my own business..." ("annoyed", "narrow", "angry", "R")
                her "I must've not been careful enough to hide the tail as all of a sudden, a group of students came out of nowhere." ("angry", "happyCl", "worried", "mid")
                her "They started asking me all these questions..." ("angry", "happyCl", "worried", "mid")
                her "\"Is it fluffy\"?" ("annoyed", "narrow", "angry", "R")
                her "\"Why are you wearing it\"?" ("angry", "narrow", "base", "down")
                her "\"Does it feel nice\"?" ("base", "narrow", "worried", "down")
                her "\"Can we touch it\"?" ("base", "narrow", "worried", "down")
                her "\"Can you make it wag\"..." ("angry", "wink", "base", "mid")
                gen "Sounds like reasonable enough things to ask..." ("base", xpos="far_left", ypos="head")
                gen "So, what did you tell them?" ("base", xpos="far_left", ypos="head")
                her "I didn't tell them anything!" ("upset", "closed", "base", "mid")
                gen "You didn't--" ("base", xpos="far_left", ypos="head")
                her "We were in the library for crying out loud..." ("upset", "closed", "base", "mid")
                her "Instead, I made them promise to keep quiet and not let anyone know about it..." ("upset", "closed", "base", "mid")
                her "And in exchange I let them touch it for a bit..." ("open", "narrow", "worried", "down")
                her "{heart}{heart}{heart}" ("soft", "narrow", "annoyed", "up")
                gen "So... Instead of answering some innocent questions... You let them touch your butt plug..." ("base", xpos="far_left", ypos="head")
                her "It sounds sinister when you put it like that." ("annoyed", "narrow", "angry", "R")
                her "All I did was take them to a secluded part of the library and let them touch my tail..."
                gen "Well that's alright then..." ("base", xpos="far_left", ypos="head")
                her "......." ("base", "narrow", "worried", "down")
                gen "So, did you enjoy it?" ("base", xpos="far_left", ypos="head")
                her ".........." ("angry", "base", "base", "mid")
                her "Truthfully [name_genie_hermione].... It was one of the most pleasurable experiences of my life..." ("grin", "narrow", "base", "dead")
                her "All their hands touching it..." ("soft", "narrow", "annoyed", "up")
                her "Taking turns..." ("grin", "narrow", "annoyed", "up")
                her "All the while it was vibrating away..." ("base", "narrow", "worried", "down")
                her "I nearly passed out." ("silly", "narrow", "base", "dead")
                her "Especially when one of them pulled at it a bit..." ("silly", "narrow", "annoyed", "up")
                her "..." ("grin", "narrow", "annoyed", "up")
                gen "Nice work, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

            block:
                # Glory hole with Female Student

                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "Yes I did, [name_genie_hermione]..." ("base", "base", "base", "mid",xpos="right",ypos="base")
                her "Did you know there are holes between the stalls in the girls' bathroom?" ("soft", "base", "base", "mid")
                gen "I did not, but What does that have to do with your butt plug?" ("base", xpos="far_left", ypos="head")
                her "Well, I noticed that the hole is the same height as the tail..." ("grin", "base", "base", "R")
                her "..............." ("grin", "happyCl", "worried", "mid")
                gen "Go on, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
                her "I might have put it through..." ("base", "narrow", "worried", "down")
                gen "What?" ("base", xpos="far_left", ypos="head")
                her "Well, I was in the stall finishing up..." ("base", "base", "base", "R")
                her "When a girl entered the other stall."
                her "I wasn't sure, but I thought that it may have been a Slytherin..." ("upset", "wink", "base", "mid")
                her "So I decided to press my cheeks to the wall and stick my tail through to freak her out!" ("smile", "base", "base", "R")
                gen "Freak her out?" ("base", xpos="far_left", ypos="head")
                her "Yeah!" ("grin", "base", "base", "R")
                her "At first she didn't do anything, and I thought she must've been stunned by the sight, but after I gave it a little wiggle, instead of running off she tugged on it..." ("grin", "base", "base", "R")
                her "I was worried she was going to pull it out, but she just stood there, and eventually, she started to play with it..." ("open", "base", "base", "R")
                her "I didn't really know what to feel in case it was actually a Slytherin doing it." ("open", "base", "base", "R")
                her "She was stroking it... flicking it... I even think she may have licked it..." ("soft", "narrow", "annoyed", "up")
                her "... Imagine that... a Slytherin, licking something that was inside my..."
                her "It was incredible... I could barely stand while it happened..."
                gen "Sounds like you had a good time." ("base", xpos="far_left", ypos="head")
                gen "Did you find out if it was a Slytherin or not?" ("base", xpos="far_left", ypos="head")
                her "Unfortunately not... [name_genie_hermione]." ("open", "base", "worried", "mid")
                her "Although truth be told, I'm not sure if I want to know..." ("open", "base", "worried", "mid")
                #Maybe this section could be a check in the future if we feel it's appropriate
                #her "It was at lunch, in the great hall." ("open", "closed", "base", "mid")
                #her "I was walking past the Slytherin table on my way to sit down..." ("open", "closed", "base", "mid")
                #her "when I saw that little... vixen, Astoria Greengrass." ("base", "squint", "base", "mid")
                #her "she couldn't take her eyes off of it..."
                #her "imagine that... Astoria Greengrass... pure-blood, licking my..." ("grin", "narrow", "annoyed", "up")
                #her "{heart}........{heart}" ("soft", "narrow", "annoyed", "up")
                #gen "It sounds like you've earned your points today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                gen "*Hmm*... That's too bad, perhaps you'll see them at that hole again some time." ("base", xpos="far_left", ypos="head")
                gen "Either way, you've surely earned your points." ("base", xpos="far_left", ypos="head")
                her "...{size=-7}(I would have done this for free...){/size}" ("base", "narrow", "worried", "down")

            block:
                play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
                her "Yes, I did [name_genie_hermione]..." ("base", "squint", "base", "mid",xpos="right",ypos="base")
                gen "Anything interesting happen?" ("base", xpos="far_left", ypos="head")
                her "Yes!"
                her "I was walking down the hall and there were some students behind me..." ("base", "narrow", "base", "mid_soft")
                her "And swear I could hear them whispering to each other..."
                her "So I thought I may as well give them something to talk about..." ("base", "squint", "base", "mid")
                her "So I stopped and pretended to tie my shoelaces, keeping my knees straight and bending over as far as I could..." ("base", "narrow", "base", "mid_soft")
                gen "You exposed yourself in the middle of a corridor, just like that?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Expose? I'm not sure I know what you mean...{w=0.4} I was tying my shoelaces........" ("base", "base", "base", "R")
                gen "Very good, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")

    $ gryffindor += current_payout
    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    call her_walk(action="leave")

    jump end_hermione_event

label hg_butt_plugs_large_return:

    call her_walk(action="enter", xpos="mid", ypos="base")

    random:
        block:
            # Student tried to pull it out
            gen "[name_hermione_genie], how was your day?" ("base", xpos="far_left", ypos="head")
            her "Awful, the worst thing possible happened!" ("scream", "closed", "angry", "mid",xpos="right",ypos="base")
            gen "The worst thing? Worse than someone catching you with a tail up your butt?" ("base", xpos="far_left", ypos="head")
            her "Yes, believe it or not." ("annoyed", "base", "angry", "mid")
            gen "Now you've got me intrigued." ("base", xpos="far_left", ypos="head")
            gen "What happened?" ("base", xpos="far_left", ypos="head")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
            her "Well... I was walking down to Hogsmeade as we had the afternoon off..." ("open", "base", "worried", "R")
            her "And I thought I was alone, but one of the Slytherin students suddenly rushed up behind me..." ("annoyed", "narrow", "angry", "R")
            her "And I didn't even have enough time to react before he..." ("angry", "happyCl", "worried", "mid")
            her "He..." ("annoyed", "narrow", "angry", "R")
            her "Before he shouted \"Let it rip!\" and tugged on my tail!" ("angry", "narrow", "base", "down")
            gen "He did what?" ("base", xpos="far_left", ypos="head")
            her "I know! How dare he!" ("clench", "narrow", "worried", "down")
            gen "Ten points to Slytherin!" ("base", xpos="far_left", ypos="head")
            $ slytherin += 10
            her "What?!" ("scream", "wide", "angry", "mid")
            her "Why are you giving points to Slytherin?!" ("angry", "wide", "angry", "mid")
            gen "Such a one-liner ought to be rewarded!" ("base", xpos="far_left", ypos="head")
            her "But [name_genie_hermione]! I'm doing this so that Gryffindor can get ahead of Slytherin!" ("upset", "base", "angry", "mid")
            gen "Oh, right..." ("base", xpos="far_left", ypos="head")
            gen "Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
            $ gryffindor += 10
            her "*Hmm*... But now Ravenclaw and Hufflepuff are both behind..." ("open", "narrow", "worried", "down")
            gen "Enough about the points. Tell me more about your behind." ("base", xpos="far_left", ypos="head")
            her "My-- Oh right..." ("annoyed", "narrow", "angry", "R")
            gen "What happened next?" ("base", xpos="far_left", ypos="head")
            her "Well... I would normally not say this, but I'm glad the plug is as big as it is." ("open", "narrow", "worried", "down")
            gen "Didn't budge one bit, I assume." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "base", "down")
            her "Can I have my points now?" ("open", "narrow", "worried", "down")
            gen "Certainly." ("base", xpos="far_left", ypos="head")
            gen "Nice work, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        block:
            # Hermione is a Dragon
            gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
            her "Yes I did, [name_genie_hermione]..." ("base", "base", "base", "mid", xpos="right", ypos="base")
            her "I found the perfect opportunity to show it off today." ("soft", "base", "base", "mid")
            gen "Show it off? You actually showed it off to someone this time?" ("base", xpos="far_left", ypos="head")
            her "I did..." ("grin", "base", "base", "R")
            her "..............." ("grin", "happyCl", "worried", "mid")
            gen "Go on, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
            her "Well, we're currently studying Dragons in our care of magical creatures lessons." ("base", "narrow", "base", "down")
            gen "Right?" ("base", xpos="far_left", ypos="head")
            her "Well, I thought it was a great opportunity to give a demonstration how female Dragons attract their mates.." ("base", "base", "base", "R")
            her "You're kidding..."
            her "Nope, I was wearing a dragon's head and everything!" ("grin", "wink", "base", "mid")
            her "They didn't suspect a thing about where the tail was attached!" ("smile", "base", "base", "R")
            gen "Did they touch it?" ("base", xpos="far_left", ypos="head")
            her "They did..." ("base", "base", "base", "R")
            her "And... Well, since I was role-playing a female dragon in heat..." ("grin", "base", "base", "R")
            her "You could probably guess the rest..." ("grin", "base", "base", "R")
            gen "I'll be expecting a dragon egg on my desk in the next few months..." ("grin", xpos="far_left", ypos="head")
            her "What?! No, it just got a bit heated, that's all!" ("clench", "wide", "base", "R")
            gen "I know, I just wanted to hear you say it." ("grin", xpos="far_left", ypos="head")
            gen "I suppose you better get some points, although I assume you've already earned a couple during that lesson." ("base", xpos="far_left", ypos="head")
            her "A couple..." ("grin", "base", "base", "R")
            gen "You sure have good imagination to come up with and do something like this... [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "Thank you [name_genie_hermione]..." ("grin", "base", "base", "R")
            gen "Imagine dragons..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*?"
            gen "Nevermind..." ("base", xpos="far_left", ypos="head")

        block:
            # Rides Hippogriff with it inside
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
            gen "[name_hermione_genie], did you complete your task?" ("base", xpos="far_left", ypos="head")
            her "Yes, I did [name_genie_hermione]..." ("base", "squint", "base", "mid",xpos="right",ypos="base")
            gen "Anything interesting happen?" ("base", xpos="far_left", ypos="head")
            her "Yes... As you probably know, you can't really sit very well with this thing inside."
            gen "Can't say that I have first-hand experience..." ("base", xpos="far_left", ypos="head")
            her "Right..."
            gen "So, what happened? I thought you'd expect you'd need to sit down at some point." ("base", xpos="far_left", ypos="head")
            her "I did, although..."
            her "I completely forgot that we were going to ride the Hippogriffs today..." ("base", "narrow", "base", "mid_soft")
            gen "When you say ride--" ("base", xpos="far_left", ypos="head")
            her "As in on their backs..."
            gen "Oh, Good... Can never be too careful these days..." ("base", xpos="far_left", ypos="head")
            her "It was quite an experience to say the least..."
            gen "Very good, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")

    $ gryffindor += current_payout
    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    call her_walk(action="leave")

    jump end_hermione_event
