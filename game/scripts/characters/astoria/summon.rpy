
label summon_astoria:

    $ states.active_girl = "astoria"
    $ states.ast.busy = True

    #call update_states.ast.tier
    call update_astoria

    $ renpy.checkpoint(hard=True)

    # Clothes Events
    call astoria_summon_setup

    label astoria_requests:

    # Reset
    call reset_menu_position
    ast "" (xpos="base",ypos="base")

    menu:
        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if states.ast.mood > 0:
                ast "I have nothing to say." ("annoyed", "narrow", "base", "R")
                jump astoria_requests

            call astoria_chitchat
            jump astoria_talk

        "-Sexual favours-" (icon="interface/icons/small/condom.webp"): # TODO: add 'if states.ast.favors_unlocked' once her story is looked over again 
            if states.ast.mood != 0:
                ast "I don't want to today..." ("annoyed", "narrow", "base", "R")
                nar "Astoria is upset with you."

                jump astoria_requests

            jump astoria_favor_menu

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if states.ast.wardrobe_unlocked:
            hide astoria_main with d1
            call wardrobe
            jump astoria_requests

        "-Wardrobe-" (style="disabled") if not states.ast.wardrobe_unlocked:
            nar "You haven't unlocked this feature yet."
            jump astoria_requests

        "-Give Item-" (icon="interface/icons/small/gift.webp"):
            hide astoria_main with d1
            call gift_menu
            jump astoria_requests

        # Dismiss
        "-Dismiss her-":
            stop music fadeout 3.0

            if game.daytime:
                ast "I will go back to classes then, [name_genie_astoria]." ("base", "base", "base", "mid")
            else:
                ast "Oh, alright. Good night, [name_genie_astoria]." ("base", "base", "base", "mid")

            play sound "sounds/door.ogg"

            jump end_astoria_event

label astoria_talk:
    menu:
        "-Ask about Slytherin Quidditch Team-" (icon="interface/icons/small/quidditch.webp") if states.cho.tier == 2 and states.cho.ev.quidditch.lock_practice and states.cho.ev.quidditch.e6_complete and not states.cho.ev.quidditch.e8_complete:
            gen "Could you help me with something?" ("base", xpos="far_left", ypos="head")
            ast "Depends what it is." ("annoyed", "narrow", "base", "mid")
            ast "And what's in it for me..." ("smile", "closed", "angry", "mid")
            gen "Well, the Slytherin Quidditch team refuses to practise against Ravenclaw." ("base", xpos="far_left", ypos="head")
            ast "And?" ("base", "base", "base", "mid")
            gen "I was wondering if there's something you could do about it." ("base", xpos="far_left", ypos="head")
            ast "Like what?" ("open", "base", "worried", "mid")
            gen "I don't know... Ask them nicely?" ("base", xpos="far_left", ypos="head")
            ast "Yeah right, those guys would never listen to me..." ("base", "narrow", "base", "R")
            ast "And can't you do something about it? You're the headmaster!" ("annoyed", "base", "worried", "mid")
            gen "Well, I can't technically force them to do anything. If I could, then that would make things a lot easier..." ("base", xpos="far_left", ypos="head")
            ast "Ask Snape then, he's the head of Slytherin... If they'd listen to anyone, it'd be him." ("base", "base", "base", "mid")
            if states.cho.ev.quidditch.e9_complete:
                gen "(If only he'd listen to me...)" ("base", xpos="far_left", ypos="head")
            else:
                gen "(I suppose, if there's no other option...)" ("base", xpos="far_left", ypos="head")
            gen "Well, I'll try and think of something..." ("base", xpos="far_left", ypos="head")
            ast "You do that." ("open", "base", "base", "mid")

            jump astoria_talk

        "-Address me only as-":
            menu:
                "-Sir-":
                    label .sir:
                    $ name_genie_astoria = "Sir"
                    ast "Very well, [name_genie_astoria]." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Dumbledore-":
                    label .dumbledore:
                    $ name_genie_astoria = "Dumbledore"
                    ast "Of course, [name_genie_astoria]." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Professor-":
                    label .professor:
                    $ name_genie_astoria = "Professor"
                    ast "Of course, [name_genie_astoria]." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Old man-":
                    label .old_man:
                    $ name_genie_astoria = "Old man"
                    ast "Alrighty, [name_genie_astoria]." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Genie-":
                    label .genie:
                    $ name_genie_astoria = "Genie"
                    ast "What?! You are a genie? For real?" ("grin", "base", "base", "mid")
                    ast "That's so cool!" ("grin", "base", "base", "mid")
                    gen "(Oh right. Nobody is supposed to know that.)" ("base", xpos="far_left", ypos="head")
                    gen "It's just my name, [name_astoria_genie]..." ("base", xpos="far_left", ypos="head")
                    ast "Oh... Okay, [name_genie_astoria]." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Lord Voldemort-":
                    label .lord_voldemort:
                    $ name_genie_astoria = "Lord Voldemort"
                    ast "Voldemort? Like that mean, evil wizard?" ("clench", "narrow", "angry", "mid")
                    ast "You aren't him, are you?" ("clench", "narrow", "angry", "mid")
                    gen "No, just role-playing..." ("base", xpos="far_left", ypos="head")
                    ast "Oh, alrighty then!" ("grin", "base", "base", "mid")
                    ast "[name_genie_astoria]." ("grin", "base", "base", "mid")
                    jump astoria_talk
                "-Daddy-":
                    label .daddy:
                    $ name_genie_astoria = "Daddy"
                    ast "Daddy? Don't you think that's a little weird?" ("clench", "narrow", "angry", "mid")
                    gen "Not at all!" ("base", xpos="far_left", ypos="head")
                    ast "*Hmph*..." ("upset", "narrow", "angry", "mid")
                    ast "Alright, why not... Nobody knows about it anyway." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Master-" (style="disabled") if states.ast.level < 18:
                    label .master_fail:
                    $ name_genie_astoria = "Dumby" # Tricked
                    ast "*Ha-ha-ha-ha*-- you want me to call you master?" ("grin", "base", "base", "mid")
                    ast "That's so dumb!" ("grin", "base", "base", "mid")
                    ast "Oh I know!" ("grin", "base", "base", "mid")
                    ast "How about I'll call you \"Dumby\" instead? It fits you really well." ("grin", "base", "base", "mid")
                    gen "(...)" ("base", xpos="far_left", ypos="head")
                    ast "*Ha-ha-ha-ha*--" ("grin", "base", "base", "mid")
                    gen "Are you done now?" ("base", xpos="far_left", ypos="head")
                    ast "Yes... I'm sorry... {w=1.0}Dumby..." ("grin", "base", "base", "mid")
                    gen "(Damn brat! We'll see who will be laughing later.)" ("angry", xpos="far_left", ypos="head")
                    jump astoria_talk
                "-Master-" if states.ast.level >= 18:
                    label .master:
                    $ name_genie_astoria = "Master"
                    ast "*Ha-ha-ha-ha*-- You want me to call you master?" ("grin", "base", "base", "mid")
                    ast "That's so silly!" ("grin", "base", "base", "mid")
                    gen "(...)" ("base", xpos="far_left", ypos="head")
                    ast "Well alright... M-master--" ("grin", "base", "base", "mid")
                    ast "*Ha-ha-ha-ha*--{w=1.0}{nw}" ("grin", "base", "base", "mid")
                    with hpunch
                    gen "Shut it... Or there will be consequences!" ("angry", xpos="far_left", ypos="head")
                    ast "I'm sorry... It won't happen again, master..." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Custom Input-" (style="disabled") if states.ast.level < 18:
                    gen "(I don't think she's yet ready for that)" ("base", xpos="far_left", ypos="head")
                    jump astoria_talk

                "-Custom Input-" if states.ast.level >= 18:
                    $ temp_name = renpy.input("(Please enter the name.)", name_genie_astoria, ALLOWED_CHARACTERS, length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name.lower() in ("sir", "dumbledore", "professor", "old man", "genie", "lord voldemort", "daddy", "master"):
                        if temp_name.lower() == "master" and states.ast.level < 18:
                            jump astoria_talk.master_fail
                        $ renpy.jump("astoria_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    elif temp_name == "":
                        jump astoria_talk
                    else:
                        $ name_genie_astoria = temp_name
                        ast "*Uhm*... Okay... I will call you [name_genie_astoria]." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Never mind-":
                    jump astoria_talk


        "-From now on, I will refer to you as-":
            menu:
                "-Miss Greengrass-":
                    label .miss_greengrass:
                    $ name_astoria_genie = "Miss Greengrass"
                    ast "Sure, [name_genie_astoria]." ("grin", "base", "base", "mid")
                    jump astoria_talk
                "-Astoria-":
                    label .Astoria:
                    $ name_astoria_genie = "Astoria"
                    ast "Finally getting rid of this formal bullshit? I approve!" ("grin", "base", "base", "mid")
                    jump astoria_talk
                "-Girl-":
                    label .girl:
                    $ name_astoria_genie = "Girl"
                    ast "Okay, [name_genie_astoria]." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Princess-":
                    label .princess:
                    $ name_astoria_genie = "Princess"
                    ast "I really do feel like a princess!" ("grin", "base", "base", "mid")
                    ast "After all, I can do whatever I want!" ("upset", "narrow", "angry", "mid")
                    jump astoria_talk
                "-Cutie-":
                    label .cutie:
                    $ name_astoria_genie = "Cutie"
                    ast "Fine... If you really have to, [name_genie_astoria]." ("clench", "narrow", "angry", "mid")
                    jump astoria_talk
                "-Slave-" (style="disabled") if states.ast.level < 18:
                    label .slave_fail:
                    ast "I'm not your slave, [name_genie_astoria]!" ("upset", "narrow", "angry", "mid")
                    gen "Of course you aren't! We are just playing a game, that's all..." ("base", xpos="far_left", ypos="head")
                    ast "Well, I don't like your games!" ("upset", "narrow", "angry", "mid")
                    ast "Forget it!" ("upset", "narrow", "angry", "mid")
                    jump astoria_talk
                "-Slave-" if states.ast.level >= 18:
                    label .slave:
                    $ name_astoria_genie = "Slave"
                    ast "I'm not your slave, [name_genie_astoria]!" ("upset", "narrow", "angry", "mid")
                    gen "Of course you aren't! We are just playing a game, that's all..." ("base", xpos="far_left", ypos="head")
                    ast "I like games!" ("grin", "base", "base", "mid")
                    ast "Alrighty then!" ("grin", "base", "base", "mid")
                    jump astoria_talk

                "-Custom Input-" (style="disabled") if states.ast.level < 18:
                    gen "(I don't think she's yet ready for that)" ("base", xpos="far_left", ypos="head")
                    jump astoria_talk

                "-Custom Input-" if states.ast.level >= 18:
                    $ temp_name = renpy.input("(Please enter the name.)", name_astoria_genie, ALLOWED_CHARACTERS, length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name.lower() in ("miss greengrass", "girl", "princess", "cutie", "slave"):
                        if temp_name.lower() == "slave" and states.ast.level < 18:
                            jump astoria_talk.slave_fail
                        $ renpy.jump("astoria_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    elif temp_name == "":
                        jump astoria_talk
                    else:
                        $ name_astoria_genie = temp_name
                        ast "That's a bit much, don't you think, [name_genie_astoria]?" ("clench", "narrow", "angry", "mid")
                        gen "Not at all!" ("base", xpos="far_left", ypos="head")
                        gen "I will only call you that when we are alone!" ("base", xpos="far_left", ypos="head")
                        ast "Well... Okay then..." ("base", "base", "base", "mid")
                    jump astoria_talk
                "-Never mind-":
                    jump astoria_talk

        "-Never mind-":
            jump astoria_requests

label astoria_favor_menu:
    menu:
        # "-Level Up-" (icon="interface/icons/small/levelup.webp") if ast_level_up != None:
        #         call luna_level_up(tier=ast_level_up)
        #         jump luna_favor_menu

        "-Personal Favours-" (icon="interface/icons/small/heart_red.webp", style="disabled"):
            # call tutorial("hearts")

            label .personal:

            call not_available

            # $ result = show_events_menu(astoria_favors)

            # if result in ("disabled", "noncompliant"):
            #     "You haven't unlocked this favour opportunity yet."
            #     jump .personal
            # elif result == "exit":
            #     jump astoria_favor_menu
            # else:
            #     $ result.start()

            jump astoria_favor_menu

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled"):
            label .requests:

            call not_available
            
            # $ result = show_events_menu(hermione_requests)

            # if result in ("disabled", "noncompliant"):
            #     "You haven't unlocked this request opportunity yet."
            #     jump .requests
            # elif result == "exit":
            #     jump .skip_points_check
            # else:
            #     $ result.start()

            jump astoria_favor_menu

        "-Spell Training-" (icon="interface/icons/small/spell.webp"):
            call tutorial("hearts")

            label .spells:

            $ result = show_events_menu(astoria_spells)

            if result in ("disabled", "noncompliant"):
                "You haven't unlocked this spell training opportunity yet."
                jump .spells
            elif result == "exit":
                jump astoria_favor_menu
            else:
                $ result.start()

        "-Never mind-":
            jump astoria_requests