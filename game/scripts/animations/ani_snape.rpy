
image ch_sna walk:
    "characters/snape/chibis/snape_01.webp"
    pause .18
    "characters/snape/chibis/snape_02.webp"
    pause .18
    "characters/snape/chibis/snape_01.webp"
    pause .18
    "characters/snape/chibis/snape_03.webp"
    pause .18
    repeat

image ch_sna stand:
    "characters/snape/chibis/snape_stand.webp"

image ch_sna stand_shocked:
    "characters/snape/chibis/shocked/01.webp"

image ch_sna hold_dick:
    "characters/snape/chibis/masturbating/02.webp"

image ch_sna jerk_off:
    "characters/snape/chibis/masturbating/01.webp"
    pause .2
    "characters/snape/chibis/masturbating/02.webp"
    pause .2
    "characters/snape/chibis/masturbating/03.webp"
    pause .2
    "characters/snape/chibis/masturbating/04.webp"
    pause .2
    repeat

image ch_sna cum:
    size (300,500)
    contains:
        "ch_sna jerk_off"
    contains:
        zoom 2
        yoffset -360
        xoffset -980
        alpha 1
        "characters/snape/chibis/masturbating/sperm_01.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_02.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_03.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_04.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_05.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_06.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_07.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_08.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_09.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_10.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_11.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_12.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_13.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_14.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_15.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_16.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_17.webp"
        pause .1
        "characters/snape/chibis/masturbating/sperm_18.webp"
        pause 2
        linear .2 alpha 0
        pause .5
        repeat

image ch_sna cum_done:
    size (300,500)
    contains:
        "characters/snape/chibis/masturbating/02.webp"
    contains:
        zoom 2
        yoffset -360
        xoffset -980
        "characters/snape/chibis/masturbating/sperm_18.webp"

#TODO Add Snape chibi wand cast actions
image ch_sna wand_idle:
    "characters/snape/chibis/wand_idle/wand_idle_1.webp"
    pause.1
    "characters/snape/chibis/wand_idle/wand_idle_2.webp"
    pause.1
    "characters/snape/chibis/wand_idle/wand_idle_3.webp"
    pause.1
    "characters/snape/chibis/wand_idle/wand_idle_2.webp"
    pause.1
    repeat

image ch_sna wand_defend:
    "characters/snape/chibis/wand_defend/wand_defend_1.webp"
    pause.1
    "characters/snape/chibis/wand_defend/wand_defend_2.webp"
    pause.1
    "characters/snape/chibis/wand_defend/wand_defend_3.webp"
    pause.1
    "characters/snape/chibis/wand_defend/wand_defend_2.webp"
    pause.1
    repeat

# Snape sitting in front of fireplace, right side
image snape_toast_goblet:
    "characters/snape/chibis/drinking/01.webp"
    pause 2
    "characters/snape/chibis/drinking/02.webp"
    pause .2
    "characters/snape/chibis/drinking/03.webp"
    pause .2
    "characters/snape/chibis/drinking/04.webp"
    pause 1
    "characters/snape/chibis/drinking/03.webp"
    pause .2
    "characters/snape/chibis/drinking/01.webp"
    pause 3
    repeat

image snape_desk_work:
    zoom 0.5
    size (554, 426)
    yoffset -9

    contains:
        "characters/snape/chibis/desk_working/01.webp"
        pause .2
        "characters/snape/chibis/desk_working/02.webp"
        pause .2
        "characters/snape/chibis/desk_working/03.webp"
        pause .2
        "characters/snape/chibis/desk_working/02.webp"
        pause .3
        "characters/snape/chibis/desk_working/01.webp"
        pause .2
        "characters/snape/chibis/desk_working/02.webp"
        pause .1
        "characters/snape/chibis/desk_working/01.webp"
        pause .2
        "characters/snape/chibis/desk_working/03.webp"
        pause .3
        repeat

    contains:
        ypos 36

        "images/rooms/snape_office/lamp/01.webp"
        pause .2
        "images/rooms/snape_office/lamp/02.webp"
        pause .2
        "images/rooms/snape_office/lamp/03.webp"
        pause .2
        repeat

    contains:
        ypos 36
        alpha 0.33

        "images/rooms/snape_office/lamp/glow.webp"
        easeout_bounce 1.5 alpha 0.18
        easein_bounce 1.5 alpha 0.33
        repeat

image snape_desk_idle:
    zoom 0.5
    size (554, 426)
    yoffset -9

    contains:
        "characters/snape/chibis/desk_working/idle2.webp"

    contains:
        ypos 36

        "images/rooms/snape_office/lamp/01.webp"
        pause .2
        "images/rooms/snape_office/lamp/02.webp"
        pause .2
        "images/rooms/snape_office/lamp/03.webp"
        pause .2
        repeat

    contains:
        ypos 36
        alpha 0.33

        "images/rooms/snape_office/lamp/glow.webp"
        easeout_bounce 1.5 alpha 0.18
        easein_bounce 1.5 alpha 0.33
        repeat

image snape_desk_work_idle:
    zoom 0.5
    size (554, 426)
    yoffset -9

    contains:
        "characters/snape/chibis/desk_working/idle.webp"

    contains:
        ypos 36

        "images/rooms/snape_office/lamp/01.webp"
        pause .2
        "images/rooms/snape_office/lamp/02.webp"
        pause .2
        "images/rooms/snape_office/lamp/03.webp"
        pause .2
        repeat

    contains:
        ypos 36
        alpha 0.33

        "images/rooms/snape_office/lamp/glow.webp"
        easeout_bounce 1.5 alpha 0.18
        easein_bounce 1.5 alpha 0.33
        repeat

image ch_sna snape_jizz_covered:
    "characters/snape/chibis/jizz_covered/jizz.webp"
