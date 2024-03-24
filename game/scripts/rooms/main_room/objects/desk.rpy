
label desk:
    if game.day == 1:
        if not states.gen.ev.intro.desk_examined:
            $ states.gen.ev.intro.desk_examined = True
            $ desk_OBJ.idle = "ch_gen sit_behind_desk"
            call bld
            gen "A desk of some sort..." ("base", xpos="far_left", ypos="head")
            gen "And a letter..." ("base", xpos="far_left", ypos="head")
            gen "Mailed to a certain \"Albus Dumbledore\"." ("base", xpos="far_left", ypos="head")

            menu:
                gen "Should I open it?" ("base", xpos="far_left", ypos="head")
                "-Read the letter-":
                    call bld
                    gen "Of course I will!" ("grin", xpos="far_left", ypos="head")
                "-Leave it be-":
                    call bld
                    gen "Hell no!" ("angry", xpos="far_left", ypos="head")
                    gen "Of course I will read it!" ("grin", xpos="far_left", ypos="head")

            # First letter from Hermione
            $ desk_OBJ.foreground = None
            $ letter_hg_1.open()

            gen "*Ehm*........." ("base", xpos="far_left", ypos="head")
            gen "What?" ("base", xpos="far_left", ypos="head")
            gen "................................." ("base", xpos="far_left", ypos="head")
        else:
            gen "I've already checked the desk." ("base", xpos="far_left", ypos="head")

        if states.gen.ev.intro.bird_examined and states.gen.ev.intro.desk_examined and states.gen.ev.intro.cupboard_examined and states.gen.ev.intro.door_examined and states.gen.ev.intro.fireplace_examined:
            jump genie_intro_E2
        else:
            jump main_room_menu

    #Define hints variable
    $ ball_hint = None

    # TODO: Refactor. Low priority.

    call update_character_map_locations


    #Screens
    play sound "sounds/scroll.ogg"
    show screen desk_menu
    with d1

    $ _choice = ui.interact()

    hide screen desk_menu
    #Do NOT add a transition here!


    #Hermione
    if _choice == "hermione" and states.her.busy:
        if game.daytime:
            nar "Hermione is taking classes."
            jump main_room_menu
        else:
            nar "Hermione is already asleep."
            jump main_room_menu
    elif _choice == "hermione" and not states.her.busy:
        if states.her.map_location  == "forest":
            nar "Hermione is currently at the Forbidden Forest.\n>Would you like to go there?"
            menu:
                "-Yes, pay her a visit-":
                    jump hermione_map_BJ
                "-No, summon her to your office-":
                    pass

        jump summon_hermione

    #Luna
    elif states.lun.unlocked and _choice == "luna" and states.lun.busy:
        if game.daytime:
            nar "Luna is taking classes."
            jump main_room_menu
        else:
            nar "Luna is already asleep."
            jump main_room_menu
    elif states.lun.unlocked and _choice == "luna" and not states.lun.busy:
        jump summon_luna

    #Astoria
    elif states.ast.busy and _choice == "astoria":
        if game.daytime:
            nar "Astoria is taking classes."
            jump main_room_menu
        else:
            nar "Astoria is already asleep."
            jump main_room_menu
    elif not states.ast.busy and _choice == "astoria": #Summoning after intro events done.
        jump summon_astoria

    #Susan
    elif _choice == "susan" and states.sus.busy:
        if game.daytime:
            nar "Susan is taking classes."
            jump main_room_menu
        else:
            nar "Susan is already asleep."
            jump main_room_menu
    elif _choice == "susan" and not states.sus.busy:
        jump summon_susan

    #Cho
    elif _choice == "cho" and states.cho.busy:
        if game.daytime:
            nar "Cho is taking classes."
            jump main_room_menu
        else:
            nar "Cho is already asleep."
            jump main_room_menu
    elif _choice == "cho" and not states.cho.busy:
        jump summon_cho

    #Snape
    elif _choice == "snape" and states.sna.busy:
        nar "Professor Snape is unavailable."
        if game.daytime:
            jump main_room_menu
        else:
            jump main_room_menu
    elif _choice == "snape" and not states.sna.busy:
        jump summon_snape

    #Tonks
    elif _choice == "tonks" and states.ton.busy:
        nar "Tonks is unavailable."
        if game.daytime:
            jump main_room_menu
        else:
            jump main_room_menu
    elif _choice == "tonks" and not states.ton.busy:
        jump summon_tonks

    #Close
    elif _choice == "Close":
        jump main_room_menu
    elif _choice in {"snape_office", "seventh_floor", "map_lake", "map_forest", "map_attic", "clothing_store", "item_store", "ravenclaw_dormitories", "gryffindor_dormitories"}:
        call gen_chibi("stand", "desk", "base")
        with d3
        call gen_walk(action="leave", speed=1.5)

    $ renpy.jump(_choice)

screen desk_menu():
    tag desk_interface

    zorder 5

    #Background
    add "interface/desk/_bg_.webp"

    if states.map.unlocked:
        use map_screen

    # Ugly hands
    # add "interface/desk/_hands_.webp" xpos 0 ypos -30

    use crystal_ball
    use watch

    #Book
    if item_store_intro_done:
        add "interface/desk/book.webp" xalign 1.0 xpos 1080 ypos 0
        imagebutton:
            xpos 1080
            ypos 0
            xalign 1.0
            idle "interface/desk/book.webp"
            hover "interface/desk/book_hover.webp"
            hovered SetVariable("ball_hint", "book")
            keysym "inventory"
            unhovered SetVariable("ball_hint", None)
            action Return("inventory")

    #Tissue Box
    add "interface/desk/tissues.webp" xalign 1.0 xpos 1080 ypos 320
    imagebutton:
        xpos 1080
        ypos 320
        xalign 1.0
        idle "interface/desk/tissues.webp"
        hover "interface/desk/tissues_hover.webp"
        hovered SetVariable("ball_hint", "jerk_off")
        keysym "fap"
        unhovered SetVariable("ball_hint", None)
        action Return("jerk_off")

    #Work
    if states.paperwork_unlocked:
        imagebutton:
            xpos -10
            ypos 0
            xalign 0.0
            idle "interface/desk/work.webp"
            hover "interface/desk/work_hover.webp"
            hovered SetVariable("ball_hint", "work")
            keysym "work"
            unhovered SetVariable("ball_hint", None)
            action Return("paperwork")

    #Cards
    if states.cardgame.unlocked: #Or letter_cards_unlock.read #Day 26+
        imagebutton:
            xpos 0
            ypos 600
            xalign 0.0
            yalign 1.0
            idle "interface/desk/cards.webp"
            hover "interface/desk/cards_hover.webp"
            hovered SetVariable("ball_hint", "cards")
            unhovered SetVariable("ball_hint", None)
            action Return("deck_builder")

    #exit
    imagebutton:
        xanchor 0.5
        yanchor 1.0
        xpos 510
        ypos 600
        idle "interface/desk/exit_mask.webp"
        hover "interface/desk/exit.webp"
        hovered SetVariable("ball_hint", "exit")
        unhovered SetVariable("ball_hint", None)
        action Return("Close")

    #Night Overlay
    if not game.daytime:
        add "interface/desk/_night_overlay_.webp"

    use close_button


screen crystal_ball():
    tag desk_interface

    zorder 8

    add "interface/desk/crystal_ball.webp" xpos 268 ypos 0
    if not ball_hint == None:
        add "interface/desk/hints/glow.webp" xpos 268+40
        add "interface/desk/hints/"+str(ball_hint)+ ".webp" xpos 268+125 xanchor 0.5

screen watch():
    #Day/Night Clock
    add "interface/desk/watch.webp" xpos 603 ypos 0
    imagebutton:
        xpos 603
        ypos 0
        idle "interface/desk/watch.webp"
        hover "interface/desk/watch_hover.webp"
        unhovered SetVariable("ball_hint", None)
        keysym "sleep"
        hovered If(game.daytime, SetVariable("ball_hint", "doze_off"), SetVariable("ball_hint", "sleep"))
        action If(game.daytime, Return("night_start"), Return("day_start"))

    $ watch_x = 603 +67
    $ watch_y = 35

    if game.weather == "rain":
        add "interface/desk/watch/rain.webp" xpos watch_x ypos watch_y
    elif game.weather in ("snow", "blizzard"):
        add "interface/desk/watch/snow.webp" xpos watch_x ypos watch_y
    elif game.weather == "storm":
        add "interface/desk/watch/storm.webp" xpos watch_x ypos watch_y
    else:
        if game.daytime:
            add "interface/desk/watch/sun.webp" xpos watch_x ypos watch_y
        else:
            add "interface/desk/watch/moon.webp" xpos watch_x ypos watch_y

    if game.daytime:
        add "interface/desk/watch/day.webp" xpos watch_x+40 ypos watch_y+6 xanchor 0.5
    else:
        add "interface/desk/watch/night.webp" xpos watch_x+40 ypos watch_y+6 xanchor 0.5

label paperwork:
    if letter_work_report in mailbox.get_letters():
        gen "(I need to get paid first.)" ("base", xpos="far_left", ypos="head")
        jump main_room_menu

    call weather_sound

    if not renpy.music.is_playing("weather"):
        call music_block
    else:
        stop music fadeout 1.0

    call gen_chibi("paperwork")
    with d3
    nar "You do some paperwork."

    call paperwork_progress_chapter

    if not game.daytime and game.moon:
        call paperwork_full_moon

    call gen_chibi("sit_behind_desk")

    if game.daytime:
        jump night_start
    else:
        jump day_start

label paperwork_report_check:
    # Check if a report was completed
    if states.paperwork_chapters >= 4:
        nar "You've completed a report."
        $ states.paperwork_chapters = 0
        $ states.paperwork_reports += 1
        $ states.paperwork_reports_times += 1

    return

label paperwork_progress_chapter(message = ""):
    $ states.paperwork_chapters += 1
    call notes

    if states.paperwork_chapters == 1:
        "[message]You finished one chapter so far."
    else:
        "[message]You finished {number=states.paperwork_chapters} chapters so far."

    call paperwork_report_check
    return

label paperwork_full_moon:
    call paperwork_progress_chapter("The Full moon makes you feel more productive.\n")
    return

label paperwork_concentration:
    call paperwork_progress_chapter("You maintain perfect concentration during your work and finish another chapter of the report.\n")
    return

label paperwork_speedwriting:
    call paperwork_progress_chapter("You use your Speedwriting skills and finish another chapter of the report.\n")
    return

screen gui_tooltip(img=None, xx=335, yy=210):
    add img xpos xx ypos yy
    zorder 3
