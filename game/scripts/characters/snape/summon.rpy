

label summon_snape:
    play music "music/Dark Fog.ogg" fadein 1 if_changed
    play sound "sounds/door.ogg"
    call sna_chibi("stand","mid","base")
    with d3

    $ renpy.checkpoint(hard=True)

    sna "Yes, what is it?" ("snape_01",xpos="base",ypos="base", trans=d3)

    label snape_ready:
        pass

    menu:
        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            call snape_chitchat

            label .talk:
            menu:
                "-Ask him to help Tonks-" if states.ast.ev.intro.e1_complete and not states.ast.ev.intro.e3_complete:

                    if states.ast.ev.intro.e2_ask_snape:
                        sna "I'm still on the lookout, Genie." ("snape_01")
                        sna "If I find the little maggot that casts those spells..." ("snape_10")
                        jump .talk

                    $ states.sna.busy = True
                    $ states.ast.ev.intro.e2_ask_snape = True
                    $ ag_event_pause = 2
                    jump astoria_intro_E2_snape

                "-Try solving the Quidditch Quarrel-" (icon="interface/icons/small/quidditch.webp") if states.cho.tier == 2 and states.cho.ev.quidditch.e6_complete and not states.cho.ev.quidditch.e9_complete and not states.cho.ev.quidditch.e8_complete:
                    if game.daytime:
                        gen "I wanted to talk to you about the upcoming Quidditch game." ("base", xpos="far_left", ypos="head")
                        sna "I don't really have time right now..." ("snape_05")
                        if wine_ITEM.owned >= 1:
                            gen "I got drinks." ("base", xpos="far_left", ypos="head")
                        else:
                            gen "I'll get us drinks." ("base", xpos="far_left", ypos="head")
                        sna "Tempting, but it'll have to be in the evening... work and all that." ("snape_06")
                        gen "Fine." ("base", xpos="far_left", ypos="head")
                        jump .talk
                    else:
                        gen "So about that upcoming Quidditch game..." ("base", xpos="far_left", ypos="head")

                        if wine_ITEM.owned >= 1:
                            sna "Whatever it is, it can wait, let's sit down first, shall we." ("snape_01")
                            call setup_fireplace_hangout(char="snape")
                            
                            call bld
                            gen "Want to do the honours?" ("base", xpos="far_left", ypos="head")
                            sna "With pleasure!" ("snape_02", ypos="head")
                            pause.1

                            call give_gift("You hand over the bottle you found in the cupboard to professor Snape...", wine_ITEM)
                            $ states.gen.stats.hangouts_with_snape += 1
                            $ wine_ITEM.owned -= 1

                            jump cho_quid_E9
                        else:
                            sna "I hope you have some wine at least?" ("snape_01")
                            gen "I hoped you'd bring your own for once." ("base", xpos="far_left", ypos="head")
                            sna "I see..." ("snape_04")
                            sna "I guess you don't need my help after all." ("snape_31")
                            gen "(Bloody alcoholic...)" ("base", xpos="far_left", ypos="head")
                            jump .talk

                "-Address me only as-" if states.her.ev.intro.e6_complete:
                    call snape_nicknames_genie
                    jump .talk

                "-From now on, I will refer to you as-" if states.her.ev.intro.e6_complete:
                    call snape_nicknames
                    jump .talk

                "-Never mind-":
                    jump snape_ready


        # Fireplace Chats
        "-Let's hang-" (icon="interface/icons/small/toast.webp") if wine_ITEM.owned >= 1 and not game.daytime:
            jump snape_hangout

        "-Let's hang-" (icon="interface/icons/small/toast.webp", style="disabled") if wine_ITEM.owned < 1 or game.daytime:
            if game.daytime:
                gen "(I'm not sharing my booze with Snape while he still has to teach classes...)" ("base", xpos="far_left", ypos="head")
                gen "(I better ask him during the evening to get drunk...)" ("base", xpos="far_left", ypos="head")
            elif wine_ITEM.owned < 1:
                gen "(I don't have any more wine...)" ("base", xpos="far_left", ypos="head")
            jump snape_ready

        # Cardgame
        "-Let's Duel-" (icon="interface/icons/small/cards.webp") if states.cardgame.unlocked:
            jump snape_duel_menu

        # Dismiss
        "-Never mind-":
            stop music fadeout 1.0

            if game.daytime:
                sna "Alright, back to work then..."
            else:
                sna "Goodnight then."

            play sound "sounds/door.ogg"

            $ states.sna.busy = True

            hide snape_main
            call sna_chibi("hide")
            with d3

            jump main_room_menu
