image boxing_ring crowd_back:
    subpixel True
    "images/rooms/boxing_ring/crowd_back.webp"
    anchor (0.5, 0.0)
    xoffset 540
    linear 2.0 xzoom 0.99 yzoom 1.04
    linear 2.0 xzoom 1.0 yzoom 1.0
    repeat

image boxing_ring crowd_front:
    subpixel True
    "images/rooms/boxing_ring/crowd_front.webp"
    anchor (0.5, 0.0)
    xoffset 540
    linear 2.0 xzoom 0.99 yzoom 1.02
    linear 2.0 xzoom 1.0 yzoom 1.0
    repeat

image boxing_ring microphone:
    subpixel True
    transform_anchor True
    anchor (0.5, 0.0)
    yoffset -100
    xoffset 618

    "images/rooms/boxing_ring/microphone.webp"

    parallel:
        ease_quad 2.0 rotate -4
        ease_quad 2.0 rotate 4

        repeat

    parallel:
        ease_quad 3.0 yoffset 0

image boxing_ring flash_back:
    subpixel True

    pos (300, 200)
    anchor (0.5, 0.5)
    zoom 0.0
    alpha 0.12
    "gui/main_menu/sparkle.webp"
    easeout 0.1 zoom 3.0
    easeout 0.1 zoom 0.0

    pause 1

    pos (500, 100)
    anchor (0.5, 0.5)
    zoom 0.0
    easeout 0.1 zoom 2.0
    easeout 0.1 zoom 0.0

    pause 1.5

    pos (800, 400)
    anchor (0.5, 0.5)
    zoom 0.0
    easeout 0.1 zoom 2.5
    easeout 0.1 zoom 0.0

    pause 2

    pos (700, 150)
    anchor (0.5, 0.5)
    zoom 0.0
    easeout 0.1 zoom 2.0
    easeout 0.1 zoom 0.0

    pause 1.5

    pos (900, 250)
    anchor (0.5, 0.5)
    zoom 0.0
    easeout 0.1 zoom 2.0
    easeout 0.1 zoom 0.0

    pause 1

    repeat

image boxing_ring flash_front:
    subpixel True

    pos (320, 600)
    anchor (0.5, 0.5)
    zoom 0.0
    alpha 0.24
    "gui/main_menu/sparkle.webp"
    easeout 0.1 zoom 5.0
    easeout 0.1 zoom 0.0

    pause 4

    pos (900, 550)
    anchor (0.5, 0.5)
    zoom 0.0
    alpha 0.24
    "gui/main_menu/sparkle.webp"
    easeout 0.1 zoom 5.0
    easeout 0.1 zoom 0.0

    pause 1

    repeat

image boxing_ring dust:
    subpixel True

    "images/rooms/boxing_ring/dust.webp"
    anchor (0.5, 0.0)
    xoffset 540
    alpha 0.25
    ytile 3

    parallel:
        ease_quad 3.0 xoffset 520
        ease_quad 3.0 xoffset 540
        repeat

    parallel:
        ease_quad 7.0 yoffset -25
        ease_quad 7.0 yoffset 0
        repeat
