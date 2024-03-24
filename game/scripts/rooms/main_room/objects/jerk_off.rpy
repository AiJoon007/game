
default jerk_off_choice = None # Last jerk-off fantasy

label jerk_off:
    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause 1

    gen "(How should I finish this thing?)" ("base", xpos="far_left", ypos="head")

    label .choice:
    menu:
        "-Hermione's panties!-" if states.her.ev.panty_thief.acquired:
            $ jerk_off_choice = "hermione"
            $ states.her.ev.panty_thief.soaked = True

        "-LOCKED-" (style="disabled") if not states.her.ev.panty_thief.acquired:
            nar "You lack the item required for this option."
            jump .choice

        "-Cho's panties!-" if states.cho.ev.panty_thief.acquired:
            $ jerk_off_choice = "cho"
            $ states.cho.ev.panty_thief.soaked = True

        "-LOCKED-" (style="disabled") if not states.cho.ev.panty_thief.acquired:
            nar "You lack the item required for this option."
            jump .choice

        "-On the floor!-":
            $ jerk_off_choice = renpy.random.choice(["jasmine", "lara"])

    nar "You decide to spend some time by jerking off..."

    if jerk_off_choice == "hermione":
        nar "You fantasise about Hermione..."
    elif jerk_off_choice == "cho":
        nar "You fantasise about Cho..."
    elif jerk_off_choice == "jasmine":
        nar "You fantasise about Princess Jasmine..."
    elif jerk_off_choice == "lara":
        nar "You fantasise about Lara Croft..."

    gen "Yes... That's a good slut!" ("angry", xpos="far_left", ypos="head")
    pause.5

    nar "You are ready to cum..."
    pause.2

    if jerk_off_choice == "hermione":
        gen "Suck my almighty cock, you little whore!!!" ("angry", xpos="far_left", ypos="head")
    elif jerk_off_choice == "cho":
        gen "Suck my almighty cock, you exotic goddess!!!" ("angry", xpos="far_left", ypos="head")
    elif jerk_off_choice == "jasmine":
        gen "Suck my almighty cock, you princess-whore!!!" ("angry", xpos="far_left", ypos="head")
    elif jerk_off_choice == "lara":
        gen "Suck my almighty cock, you whore!!!" ("angry", xpos="far_left", ypos="head")

    hide screen blktone
    call gen_chibi("cum_behind_desk")
    with hpunch
    pause 1

    if jerk_off_choice == "hermione":
        nar "You cum all over Hermione's panties, and then use them to wipe the cum off the floor..."
        call gen_chibi("cum_behind_desk_done")
    elif jerk_off_choice == "cho":
        nar "You cum all over Cho's panties, and then use them to wipe the cum off the floor..."
        call gen_chibi("cum_behind_desk_done")
    else:
        nar "You cum on the floor."

    call gen_chibi("cum_behind_desk_done")
    pause.2

    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "(This was a pretty sweet jerk-off session...)" ("base", xpos="far_left", ypos="head")
    gen "(Back to being productive!)" ("base", xpos="far_left", ypos="head")

    call gen_chibi("sit_behind_desk")

    if game.daytime:
        jump night_start
    else:
        jump day_start
