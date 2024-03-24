
### Quests ###

# Add any event triggers to this list.
# Only one event can play for each day/night (this might change.)
# Add date specific events at the start of the list (create the date if it's not there.)

label quests:

    $ renpy.choice_for_skipping()

    if states.room == "main_room":
        #
        # DAY-BASED EVENTS
        #

        if game.day >= 1:
            if game.daytime:
                if not states.gen.ev.intro.e2_complete and states.gen.ev.intro.bird_examined and states.gen.ev.intro.desk_examined and states.gen.ev.intro.cupboard_examined and states.gen.ev.intro.door_examined and states.gen.ev.intro.fireplace_examined:
                    jump genie_intro_E2
            else:
                if not states.sna.ev.intro.e1_complete:
                    jump snape_intro_E1

        if game.day >= 2:
            if game.daytime:
                if not states.gen.ev.intro.e3_complete:
                    jump genie_intro_E3
            else:
                if ss_event_pause == 0 and not states.sna.ev.intro.e2_complete:
                    # Snape's second visit.
                    jump snape_intro_E2

        if game.day >= 3:
            if game.daytime:
                if not states.gen.ev.intro.e4_complete:
                    jump genie_intro_E4
            else:
                if ss_event_pause == 0 and not states.sna.ev.intro.e3_complete:
                    # Day of the duel.
                    jump snape_intro_E3


        if game.day >= 4:
            if game.daytime:
                pass
            else:
                if ss_event_pause == 0 and not states.sna.ev.intro.e5_complete:
                    # You bother decide to just "roll with it"... Snape summon unlocked.
                    jump snape_intro_E5

        if game.day >= 5:
            if game.daytime:
                if hg_event_pause == 0 and not states.her.ev.intro.e1_complete:
                    # Hermione shows up for the first time.
                    jump hermione_intro_E1

        if game.day >= 6:
            if game.daytime:
                if hg_event_pause == 0 and states.sna.ev.hangouts.hermione_e1 and not states.her.ev.intro.e2_complete:
                    # Second visit from Hermione. Says she sent a letter to the Ministry.
                    jump hermione_intro_E2
            else:
                pass

        if game.day >= 7:
            if game.daytime:
                pass
            else:
                if hg_event_pause == 0 and states.sna.ev.hangouts.hermione_e2 and not states.her.ev.intro.e3_complete:
                    # Takes place after first special event with Snape, where he just complains about Hermione.
                    # Hermione might have failed a test...
                    jump hermione_intro_E3

        if game.day >= 8:
            if game.daytime:
                pass
            else:
                if hg_event_pause == 0 and states.her.ev.intro.e3_complete and not states.her.ev.intro.e4_complete:
                    # She failed a test and cries.
                    jump hermione_intro_E4

        if game.day >= 9:
            if game.daytime:
                if hg_event_pause == 0 and states.her.ev.intro.e4_complete and not states.her.ev.intro.e5_complete:
                    # Hermione asks to be tutored. Summon unlocked!
                    jump hermione_intro_E5

        if game.day >= 10:
            if game.daytime:
                if nt_event_pause == 0 and states.her.ev.intro.e5_complete and not states.ton.ev.intro.e1_complete:
                    # Tonks visits for the first time.
                    jump tonks_intro_E1
            else:
                if states.ton.ev.intro.e1_complete and not states.ton.ev.intro.e2_complete:
                    # Tonks has found no evidence so far.
                    jump tonks_intro_E2

        if game.day >= 11:
            if game.daytime:
                pass
            else:
                if nt_event_pause == 0 and states.sna.ev.hangouts.tonks_e1 and not states.ton.ev.intro.e3_complete:
                    # Tonks becomes a teacher. Summon unlocked!
                    jump tonks_intro_E3

        if game.day >= 13:
            if game.daytime:
                if hg_event_pause == 0 and states.her.ev.intro.e5_complete and states.sna.ev.hangouts.tonks_e1 and states.her.ev.intro.convinced and not states.her.ev.intro.e6_complete:
                    # Hermione wants to buy favours. Favours unlocked!
                    jump hermione_intro_E6

        if is_puzzle_box_in_fireplace():
            $ states.fireplace_started = False
            $ fireplace_OBJ.foreground = "glow_effect_fireplace"
        elif fireplace_OBJ.foreground == "glow_effect_fireplace":
            $ fireplace_OBJ.foreground = None

        #
        # CARDGAME - EVENTS
        #

        if geniecard_level < 2 and states.sna.ev.cardgame.stage >= 3 and states.her.ev.cardgame.stage >= 3 and states.twi.ev.cardgame.stage >= 2:
            if not game.daytime:
                $ letter_cards_tier2.send()

        #
        # CHO CHANG - EVENTS
        #

        if cc_event_pause == 0:
            if game.daytime:

                if not states.cho.ev.intro.e1_complete and states.her.tier >= 2:
                    # Cho intro
                    jump cho_intro_E1

                if states.cho.ev.quidditch.hufflepuff_stage == "start":
                    $ game.weather = "clear"
                    stop weather
                    $ states.cho.ev.quidditch.hufflepuff_stage = "return"
                    jump hufflepuff_match
                elif states.cho.ev.quidditch.slytherin_stage == "start":
                    $ game.weather = "clear"
                    stop weather
                    $ states.cho.ev.quidditch.slytherin_stage = "return"
                    jump slytherin_match
                elif states.cho.ev.quidditch.gryffindor_stage == "start":
                    $ game.weather = "clear"
                    stop weather
                    $ states.cho.ev.quidditch.gryffindor_stage = "return"
                    jump gryffindor_match

                if states.cho.tier == 1:
                    # Lee Jordan gets knocked out cold
                    if states.cho.ev.quidditch.hufflepuff_training and not states.cho.ev.quidditch.e3_complete:
                        jump cho_quid_E3

                elif states.cho.tier == 2:
                    # Hermione refuses to commentate for Slytherin match.
                    if states.cho.ev.quidditch.slytherin_failed and not states.cho.ev.quidditch.e6_complete:
                        jump cho_quid_E6

                elif states.cho.tier == 3:
                    # Genie decides to get the broom.
                    if states.cho.ev.quidditch.gryffindor_training and not states.cho.ev.quidditch.e12_complete:
                        jump cho_quid_E12

                    # Informs the player that all preparations are complete
                    if states.cho.ev.quidditch.e11_complete and states.cho.ev.quidditch.e12_complete and not states.cho.ev.quidditch.e13_complete:
                        jump cho_quid_E13

            else:
                # Introduction
                if states.cho.ev.intro.e1_complete and not states.cho.ev.intro.e2_complete:
                    jump cho_intro_E2

                # Quidditch training matches
                if states.cho.ev.quidditch.in_progress:
                    $ states.cho.ev.quidditch.in_progress = False

                    if states.cho.tier == 1:
                        # Hufflepuff
                        jump cc_ht_return
                    elif states.cho.tier == 2:
                        # Slytherin
                        jump cc_st_return
                    elif states.cho.tier == 3:
                        # Gryffindor
                        jump cc_gt_return

                    # Note: The return events now get jumped to right after the main match events.

            $ play_potion_return("cho")

        #
        # SUSAN BONES - EVENTS
        #

        if sb_event_pause == 0:
            if game.daytime:
                # Introduction
                if states.ton.ev.hangouts.susan_e1 and not states.sus.ev.intro.e1_complete:
                    jump susan_intro_E1

            $ play_potion_return("susan")

        #
        # ASTORIA GREENGRASS - EVENTS
        #

        # Astoria events not triggered by a date.
        if ag_event_pause == 0:
            if game.daytime:
                # Introduction
                if states.ast.ev.intro.e2_ask_hermione and states.ast.ev.intro.e2_ask_snape and not states.ast.ev.intro.e3_complete:
                    $ states.ast.ev.intro.e2_complete = True
                    jump astoria_intro_E3
                if states.ton.ev.hangouts.astoria_e1 and not states.ast.ev.intro.e4_complete:
                    jump astoria_intro_E4
            else:
                # Introduction
                if states.sus.ev.intro.e1_complete and not states.ast.ev.intro.e1_complete:
                    jump astoria_intro_E1

            $ play_potion_return("astoria")

        #
        # NYMPHADORA TONKS - EVENTS
        #

        # Tonks events not triggered by a date.
        if nt_event_pause == 0:

            $ play_potion_return("tonks")

        #
        # HERMIONE GRANGER - EVENTS
        #

        if hg_event_pause == 0:

            $ play_potion_return("hermione")

        #
        # LUNA LOVEGOOD - EVENTS
        #

        if ll_event_pause == 0:
            if not states.lun.ev.intro.e1_complete and states.her.tier >= 3:
                if not game.daytime:
                    # Luna barges into your office sleepwalking.
                    jump luna_intro_E1

            if states.lun.ev.intro.e1_complete and not states.lun.ev.intro.e2_complete:
                if game.daytime:
                    jump luna_intro_E2

            if states.lun.ev.spectrespecs.e1_complete and not states.lun.ev.quibbler.stocked:
                if game.daytime:
                    jump spectrespecs_E2_reminder

            $ play_potion_return("luna")
    elif states.room == "snape_office":

        if game.daytime:
            if not states.map.snape_office.intro_e2:
                # Genie searches the office
                jump potions_intro_E1

            if not states.map.snape_office.intro_e3 and states.map.snape_office.intro_e2:
                # Genie gets caught by the painting.
                jump potions_intro_E2
        else:
            if not states.map.snape_office.intro_e3:
                # (Optional) Genie gets caught by Snape. (E0 can play either before or after E1)
                jump potions_intro_E0

    $ eventqueue.start()

    # All quest events should somehow end with a jump to the main room day/night cycle
    # If no quest event is triggered, resume normally from the main room
    call music_block
    call screen room_menu
