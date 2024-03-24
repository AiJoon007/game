
label day_start:
    show screen blkfade
    hide snape_main
    hide genie_main
    hide tonks_main
    hide cho_main
    hide hermione_main
    hide astoria_main
    hide susan_main
    hide luna_main
    with dissolve

    python:

        # Reset room objects
        candleL_OBJ.foreground = None
        candleR_OBJ.foreground = None
        states.fireplace_started = False
        fireplace_OBJ.foreground = None
        states.bird_fed = False
        states.bird_petted = False
        phoenix_OBJ.foreground = None # Removes seeds image
        states.cupboard_rummaged = False

        # Reset gift flags
        states.ton.gifted = False
        states.her.gifted = False
        states.lun.gifted = False
        states.cho.gifted = False
        states.ast.gifted = False
        states.sus.gifted = False

        # Reset chit-chat flags
        states.sna.chatted = False
        states.ton.chatted = False
        states.her.chatted = False
        states.lun.chatted = False
        states.cho.chatted = False
        states.ast.chatted = False
        states.sus.chatted = False

        # Tick Event timers
        ss_event_pause = max(ss_event_pause-1, 0)
        ss_summon_pause = max(ss_summon_pause-1, 0)
        nt_event_pause = max(nt_event_pause-1, 0)
        nt_summon_pause = max(nt_summon_pause-1, 0)
        hg_event_pause = max(hg_event_pause-1, 0)
        hg_summon_pause = max(hg_summon_pause-1, 0)
        ll_event_pause = max(ll_event_pause-1, 0)
        ll_summon_pause = max(ll_summon_pause-1, 0)
        cc_event_pause = max(cc_event_pause-1, 0)
        cc_summon_pause = max(cc_summon_pause-1, 0)
        ag_event_pause = max(ag_event_pause-1, 0)
        ag_summon_pause = max(ag_summon_pause-1, 0)
        sb_event_pause = max(sb_event_pause-1, 0)
        sb_summon_pause = max(sb_summon_pause-1, 0)

        # Reset busy flags (Based on current tick)
        states.sna.busy = True # bool(ss_summon_pause)
        states.ton.busy = bool(nt_summon_pause)
        states.her.busy = bool(hg_summon_pause)
        states.lun.busy = bool(ll_summon_pause)
        states.cho.busy = bool(cc_summon_pause)
        states.ast.busy = bool(ag_summon_pause)
        states.sus.busy = bool(sb_summon_pause)

        # Improve Mood
        if game.difficulty == 1:   # Easy difficulty
            val = 3
        elif game.difficulty == 2: # Normal difficulty
            val = 2
        elif game.difficulty == 3: # Hardcore difficulty
            val = 1

        states.ton.mood = max(states.ton.mood-val, 0)
        states.her.mood = max(states.her.mood-val, 0)
        states.lun.mood = max(states.lun.mood-val, 0)
        states.cho.mood = max(states.cho.mood-val, 0)
        states.ast.mood = max(states.ast.mood-val, 0)
        states.sus.mood = max(states.sus.mood-val, 0)

        # Game flags
        game.day += 1
        game.weather = "random"
        game.daytime = True

        # Randomisers
        random_gold = renpy.random.randint(8, 40)
        random_map_loc = renpy.random.randint(1, 5)

        # Send salary every 7th day
        if game.day % 7 == 0:
            if states.paperwork_reports >= 1:
                letter_work_report.send()
            if not states.twi.ev.cardgame.first_random:
                states.twi.ev.cardgame.interest = True

        # Pass time
        mailbox.tick()
        eventqueue.tick()

    # Update map locations
    call set_her_map_location()
    call set_lun_map_location()
    call set_cho_map_location()
    call set_ast_map_location()
    call set_sus_map_location()
    #TODO: Add Tonks map location
    #TODO: Add Snape map location

    # Reset appearances and sprites
    call update_luna
    call update_astoria
    call update_hermione
    call update_susan
    call update_cho
    call update_tonks
    call update_snape
    call update_genie

    call room(states.room, stop_sound=False, hide_screens=False)

    # Equip scheduled outfits
    if states.lun.wardrobe_scheduling:
        $ luna.equip_random_outfit()
    if states.ast.wardrobe_scheduling:
        $ astoria.equip_random_outfit()
    if states.her.wardrobe_scheduling:
        $ hermione.equip_random_outfit()
    if states.sus.wardrobe_scheduling:
        $ susan.equip_random_outfit()
    if states.cho.wardrobe_scheduling:
        $ cho.equip_random_outfit()
    if states.ton.wardrobe_scheduling:
        $ tonks.equip_random_outfit()

    hide screen blkfade
    hide screen bld1
    hide screen blktone
    with dissolve

    # Points gains
    call points_changes
    call update_ui_points

    $ renpy.force_autosave(True)

    label day_resume:

    # Start Quests
    jump quests

    $ renpy.choice_for_skipping()

    call screen room_menu

label night_start:

    show screen blkfade
    hide snape_main
    hide genie_main
    hide tonks_main
    hide cho_main
    hide hermione_main
    hide astoria_main
    hide susan_main
    hide luna_main
    with dissolve

    python:

        # Reset room objects
        if not candleL_OBJ.foreground:
            candleL_OBJ.get_action()()
        if not candleR_OBJ.foreground:
            candleR_OBJ.get_action()()
        states.cupboard_rummaged = False

        # Reset chit-chat flags
        states.sna.chatted = False
        states.ton.chatted = False
        states.her.chatted = False
        states.lun.chatted = False
        states.cho.chatted = False
        states.ast.chatted = False
        states.sus.chatted = False

        # Reset busy flags (Based on current tick)
        states.sna.busy = bool(ss_summon_pause)
        states.ton.busy = bool(nt_summon_pause)
        states.her.busy = bool(hg_summon_pause)
        states.lun.busy = bool(ll_summon_pause)
        states.cho.busy = bool(cc_summon_pause)
        states.ast.busy = bool(ag_summon_pause)
        states.sus.busy = bool(sb_summon_pause)

        # Game flags
        game.weather = "random"
        game.daytime = False

        # Randomisers
        random_gold = renpy.random.randint(8, 40)
        random_map_loc = renpy.random.randint(1, 5)

    # Update map locations
    call set_her_map_location()
    call set_lun_map_location()
    call set_cho_map_location()
    call set_ast_map_location()
    call set_sus_map_location()
    #TODO: Add Tonks map location
    #TODO: Add Snape map location

    # Reset appearances and sprites
    call update_luna
    call update_astoria
    call update_hermione
    call update_susan
    call update_cho
    call update_tonks
    call update_snape
    call update_genie

    call room(states.room, stop_sound=False, hide_screens=False)

    # Equip scheduled outfits
    if states.lun.wardrobe_scheduling:
        $ luna.equip_random_outfit()
    if states.ast.wardrobe_scheduling:
        $ astoria.equip_random_outfit()
    if states.her.wardrobe_scheduling:
        $ hermione.equip_random_outfit()
    if states.sus.wardrobe_scheduling:
        $ susan.equip_random_outfit()
    if states.cho.wardrobe_scheduling:
        $ cho.equip_random_outfit()
    if states.ton.wardrobe_scheduling:
        $ tonks.equip_random_outfit()

    hide screen blkfade
    hide screen bld1
    hide screen blktone
    with dissolve

    $ renpy.force_autosave(True)

    label night_resume:

    # Start Quests
    jump quests

    $ renpy.choice_for_skipping()

    call screen room_menu
