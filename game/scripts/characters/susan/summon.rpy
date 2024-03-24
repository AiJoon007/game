
label summon_susan:

    $ states.active_girl = "susan"

    $ states.sus.busy = True

    call update_susan

    $ renpy.checkpoint(hard=True)

    play music "music/teddy-bear-waltz-by-kevin-macleod.ogg" fadein 1 if_changed
    play sound "sounds/door.ogg"

    call sus_chibi("stand","mid","base")
    with d3

    sus "You wanted to see me, [name_genie_susan]?" ("base", "base", "base", "mid", xpos="base", ypos="base")

    label susan_requests:

    sus "" (xpos="base", ypos="base")

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if states.sus.mood > 0:
                sus "I'm sorry, [name_genie_susan], but I don't want to talk right now." ("soft", "happy", "base", "downR")
                jump susan_requests

            call susan_chitchat
            jump susan_talk

        "-Sexual favours-" (icon="interface/icons/small/condom.webp", style="disabled") if False:
            $ TBA_message()
            jump susan_requests

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if states.sus.wardrobe_unlocked:
            hide susan_main with d1
            call wardrobe
            jump susan_requests

        "-Wardrobe-" (style="disabled") if not states.sus.wardrobe_unlocked:
            nar "You haven't unlocked this feature yet."
            jump susan_requests

        "-Give Item-" (icon="interface/icons/small/gift.webp"):
            $ TBA_message()
            jump susan_requests

            # hide susan_main with d1
            # call gift_menu
            # jump susan_requests


        # Dismiss
        "-Dismiss her-":
            if game.daytime:
                sus "I will go back to classes then, [name_genie_susan]." ("base", "base", "shocked", "mid")
            else:
                sus "*Ehm*... Good night then, [name_genie_susan]." ("base", "base", "base", "mid")

            play sound "sounds/door.ogg"

            jump end_susan_event



label susan_talk:
    menu:
        #"--":
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ name_genie_susan = "Sir"
                    sus "Very well, [name_genie_susan]." ("base", "base", "base", "mid")
                    jump susan_talk
                "-Dumbledore-":
                    $ name_genie_susan = "Dumbledore"
                    sus "Okay, [name_genie_susan]." ("soft", "base", "base", "mid")
                    jump susan_talk
                "-Professor-":
                    $ name_genie_susan = "Professor"
                    sus "Of course, [name_genie_susan]." ("base", "base", "base", "mid")
                    jump susan_talk
                "-Old man-":
                    $ name_genie_susan = "Old man"
                    sus "That wouldn't be very polite, Professor." ("soft", "happy", "low", "mid")
                    gen "Don't worry, [name_susan_genie]. I always tell my students to call me silly names." ("base", xpos="far_left", ypos="head")
                    gen "It helps bonding with them!" ("grin", xpos="far_left", ypos="head")
                    sus "If you say so... *Ehm*, [name_genie_susan]." ("normal", "happy", "low", "downL")
                    gen "(And soon I'm going to bond with your tits!)" ("angry", xpos="far_left", ypos="head")
                    jump susan_talk
                "-Genie-":
                    $ name_genie_susan = "Genie"
                    sus "I... *Ehm*--" ("soft", "happy", "base", "mid")
                    sus "Is that something people call you?" ("open", "base", "raised", "mid")
                    gen "Yes-yes--, everybody!" ("base", xpos="far_left", ypos="head")
                    gen "It's perfectly normal!" ("base", xpos="far_left", ypos="head")
                    sus "(...)" ("soft", "base", "base", "mid")
                    sus "O--{w=0.2} Okay then... [name_genie_susan]." ("grin", "happy", "base", "mid")
                    jump susan_talk
                "-Lord Voldemort-":
                    $ name_genie_susan = "Lord Voldemort"
                    sus "Why would you want me to call you that?" ("angry", "happy", "low", "mid")
                    sus "We aren't supposed to mention his name!" ("angry", "happy", "worried", "mid")
                    gen "It's only a name, girl..." ("base", xpos="far_left", ypos="head")
                    sus "It's the name of, you-know-who!" ("disgust", "happy", "worried", "right")
                    sus "That name really creeps me out, Professor!" ("angry", "base", "worried", "mid")
                    gen "I don't want my students to be scared of a name, Susan! It's practice." ("base", xpos="far_left", ypos="head")
                    gen "Come on... say it." ("base", xpos="far_left", ypos="head")
                    sus "...{w=0.4} Okay." ("soft", "narrow", "sad", "down")
                    sus "V--{w=0.2} Voldemort..." ("angry", "happyCl", "sad", "mid")
                    jump susan_talk
                "-Daddy-":
                    $ name_genie_susan = "Daddy"
                    sus @ cheeks blush "Sir, no!" ("angry", "base", "base", "mid")
                    sus @ cheeks blush "I can't possibly call you that!" ("open", "happy", "sad", "mid")
                    gen "But I want you to." ("base", xpos="far_left", ypos="head")
                    gen "There's no harm in calling me Daddy." ("grin", xpos="far_left", ypos="head")
                    sus @ cheeks blush "But that's!--" ("angry", "narrow", "sad", "mid")
                    sus @ cheeks blush "(This is wrong, Susan!)" ("angry", "closed", "sad", "mid")
                    gen "Miss Bones?" ("base", xpos="far_left", ypos="head")
                    sus @ cheeks blush "O--{w=0.2} Okay then... Professor-- *Ehm*... D-Daddy." ("annoyed", "happy", "worried", "stare")
                    jump susan_talk
                "-Master-":
                    $ name_genie_susan = "Master"
                    sus "M--{w=0.2} Master?" ("soft", "base", "base", "stare")
                    sus "I don't think I should call my teachers that." ("soft", "narrow", "base", "downR")
                    gen "No-no--, that's what you should call your teachers nowadays!" ("base", xpos="far_left", ypos="head")
                    gen "But only call me that!" ("base", xpos="far_left", ypos="head")
                    sus "*Ehm*... Very well, [name_genie_susan]." ("soft", "happy", "base", "down")
                    jump susan_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", name_genie_susan, ALLOWED_CHARACTERS, length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        jump susan_talk
                    else:
                        $ name_genie_susan = temp_name
                        sus "*Ehm*... Okay. I will call you [name_genie_susan]." ("base", "base", "base", "mid")
                    jump susan_talk
                "-Never mind-":
                    jump susan_requests


        "-From now on, I will refer to you as-":
            menu:
                "-Miss Bones-":
                    $ name_susan_genie = "Miss Bones"
                    sus "Of course, [name_genie_susan]." ("base", "base", "base", "mid")
                    jump susan_talk
                "-Susan-":
                    $ name_susan_genie = "Susan"
                    sus "Of course, [name_genie_susan]." ("base", "base", "base", "mid")
                    jump susan_talk
                "-Girl-":
                    $ name_susan_genie = "Girl"
                    sus "I'm okay with that, [name_genie_susan]." ("base", "base", "base", "mid")
                    jump susan_talk
                "-Cow-":
                    $ name_susan_genie = "Cow"
                    sus "Why would you want to call me that, [name_genie_susan]?" ("angry", "happy", "low", "mid")
                    sus "The other girls already call me that, and I hate it..." ("angry", "narrow", "low", "down")
                    gen "You poor thing!" ("base", xpos="far_left", ypos="head")
                    gen "You see, if someone like me would call you that, maybe it wouldn't affect you as much." ("base", xpos="far_left", ypos="head")
                    sus "I--... You might be right." ("open", "narrow", "base", "down")
                    sus @ cheeks blush "You can call me a Cow, [name_genie_susan]." ("soft", "narrow", "base", "downR")
                    jump susan_talk
                "-Betsy-":
                    $ name_susan_genie = "Betsy"
                    sus "But, sir... Isn't that... You know..." ("open", "happy", "sad", "mid")
                    gen "You know... What?" ("base", xpos="far_left", ypos="head")
                    sus @ cheeks blush "Isn't that a name you'd give to a-- A cow?" ("open", "happy", "sad", "downR")
                    gen "Oh, is it?" ("base", xpos="far_left", ypos="head")
                    sus @ cheeks blush "*Ehm*... Yes, I think so, at least..." ("open", "happy", "worried", "mid")
                    sus @ cheeks blush "Some of the other girls shouted it at me before..." ("annoyed", "happy", "worried", "down")
                    gen "That's a shame... I thought you'd like it..." ("base", xpos="far_left", ypos="head")
                    sus @ cheeks blush "Oh, well... I suppose as long as it's not ill meaning..." ("open", "happy", "worried", "downR")
                    gen "Of course not!" ("base", xpos="far_left", ypos="head")
                    sus @ cheeks blush "Alright then, you can call me that if you like..." ("soft", "base", "base", "mid")
                    jump susan_talk
                "-Slut-":
                    $ name_susan_genie = "Slut"
                    sus @ cheeks blush "[name_genie_susan]!" ("soft", "wide", "base", "mid")
                    sus @ cheeks blush "You can't be serious!" ("angry", "happy", "base", "mid")
                    gen "Why not. Nobody has to know..." ("base", xpos="far_left", ypos="head")
                    sus @ cheeks blush "How could you even think of me like that!" ("open", "happy", "sad", "downR")
                    sus @ cheeks blush "I'm not a... slut." ("soft", "narrow", "sad", "downR")
                    gen "Of course not. This is just to strengthen your self-esteem." ("base", xpos="far_left", ypos="head")
                    gen "Trust me, I know what I'm doing." ("base", xpos="far_left", ypos="head")
                    gen "Being called a slut always boosts a girl's confidence!" ("base", xpos="far_left", ypos="head")
                    sus @ cheeks blush "R-- Really?" ("soft", "happy", "sad", "mid")
                    gen "Yes. Now... shall we try it?" ("base", xpos="far_left", ypos="head")
                    sus @ cheeks blush "... alright, [name_genie_susan]..." ("base", "happy", "sad", "mid")
                    jump susan_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", name_susan_genie, ALLOWED_CHARACTERS, length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        jump susan_talk
                    else:
                        $ name_susan_genie = temp_name
                        sus "I don't like it, but--" ("base", "base", "base", "mid")
                        sus "Promise you'll only call me that when we are alone." ("base", "base", "base", "mid")
                        gen "Promised!" ("grin", xpos="far_left", ypos="head")
                    jump susan_talk
                "-Never mind-":
                    jump susan_talk


        "-Never mind-":
            jump susan_requests
