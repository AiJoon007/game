
image snitch:
    "images/CG/cho_quidditch2/snitch_0.webp" with dissolve
    pause 0.2
    "images/CG/cho_quidditch2/snitch_1.webp" with dissolve
    pause 0.2
    repeat

image CG quidditch background:
    subpixel True

    contains:
        zoom 0.5
        "images/CG/cho_quidditch2/background.webp"

    contains:
        anchor (0.5, 0.5)
        rotate -45

        contains:
            "images/CG/cho_quidditch2/scroll.webp"
            offset (0, 0)
            xtile 12
            ytile 6

            linear 0.75 offset(-396, 0) # Placeholder; Once images implemented finished, we need to recalculate the values so it's not jittery.

            repeat

image CG quidditch cho_flashing:
    subpixel True

    contains:
        zoom 0.25
        "images/CG/cho_hufflepuff/background.webp"

    contains:
        zoom 0.25
        "images/CG/cho_hufflepuff/clouds.webp"

        yoffset -25
        ease 2.5 yoffset 0
        ease 2.5 yoffset -25
        repeat

    contains:
        zoom 0.25
        "images/CG/cho_hufflepuff/cho.webp"

        yoffset -35
        ease 2.5 yoffset 35
        ease 2.5 yoffset -35
        repeat

image CG quidditch cho_sitting entry:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-600, 600)
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/cho_sitting.webp"

        block:
            ease 5.0 zoom 0.3 offset (50, -5)
            ease 5.0 zoom 0.25 offset (-50, 35)
            repeat

    contains:
        "snitch"
        pos (630, -90)
        zoom 0.3

        parallel:
            yoffset absolute(110)
            ease_back 1.5 yoffset absolute(90) zoom 0.3+0.01
            ease_back 1.5 yoffset absolute(110) zoom 0.3-0.01
            repeat

        parallel:
            xoffset absolute(110)
            ease 1.5 xoffset absolute(90)
            ease 1.5 xoffset absolute(110)
            repeat

image CG quidditch cho_sitting:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-50, 35)
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/cho_sitting.webp"

        ease 5.0 zoom 0.3 offset (50, -5)
        ease 5.0 zoom 0.25 offset (-50, 35)

        repeat

    contains:
        "snitch"
        pos (630, -90)
        zoom 0.3

        parallel:
            yoffset absolute(110)
            ease_back 1.5 yoffset absolute(90) zoom 0.3+0.01
            ease_back 1.5 yoffset absolute(110) zoom 0.3-0.01
            repeat

        parallel:
            xoffset absolute(110)
            ease 1.5 xoffset absolute(90)
            ease 1.5 xoffset absolute(110)
            repeat

image CG quidditch cho_standing:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-50, 35)
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/cho_standing.webp"

        ease 5.0 zoom 0.3 offset (50, -5)
        ease 5.0 zoom 0.25 offset (-50, 35)

        repeat

    contains:
        "snitch"
        pos (630, -90)
        zoom 0.3

        parallel:
            yoffset absolute(110)
            ease_back 1.5 yoffset absolute(90) zoom 0.3+0.01
            ease_back 1.5 yoffset absolute(110) zoom 0.3-0.01
            repeat

        parallel:
            xoffset absolute(110)
            ease 1.5 xoffset absolute(90)
            ease 1.5 xoffset absolute(110)
            repeat

image CG quidditch cho_standing_smile:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-50, 35)
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/cho_standing_smile.webp"

        ease 5.0 zoom 0.3 offset (50, -5)
        ease 5.0 zoom 0.25 offset (-50, 35)

        repeat

    contains:
        "snitch"
        pos (630, -90)
        zoom 0.3

        parallel:
            yoffset absolute(110)
            ease_back 1.5 yoffset absolute(90) zoom 0.3+0.01
            ease_back 1.5 yoffset absolute(110) zoom 0.3-0.01
            repeat

        parallel:
            xoffset absolute(110)
            ease 1.5 xoffset absolute(90)
            ease 1.5 xoffset absolute(110)
            repeat

image CG quidditch cho_standing_ahegao:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-50, 35)
        align (0.5, 0.5)

        contains:
            align (0.5, 0.5)
            "images/CG/cho_quidditch2/cho_standing_ahegao.webp"

        contains:
            "images/CG/cho_quidditch2/squirt.webp"

            parallel:
                pos (-100, 300)
                ease 2.0 pos (-800, 2040)
                repeat

            parallel:
                linear 0.5 alpha 1.0
                pause 1.5
                alpha 0.0
                repeat

        block:
            ease 5.0 zoom 0.3 offset (50, -5)
            ease 5.0 zoom 0.25 offset (-50, 35)
            repeat

    contains:
        "snitch"
        pos (630, -90)
        zoom 0.3

        parallel:
            yoffset absolute(110)
            ease_back 1.5 yoffset absolute(90) zoom 0.3+0.01
            ease_back 1.5 yoffset absolute(110) zoom 0.3-0.01
            repeat

        parallel:
            xoffset absolute(110)
            ease 1.5 xoffset absolute(90)
            ease 1.5 xoffset absolute(110)
            repeat

image CG quidditch cho_standing_panties:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-50, 35)
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/cho_standing_panties.webp"

        ease 5.0 zoom 0.3 offset (50, -5)
        ease 5.0 zoom 0.25 offset (-50, 35)

        repeat

    contains:
        "snitch"
        pos (630, -90)
        zoom 0.3

        parallel:
            yoffset absolute(110)
            ease_back 1.5 yoffset absolute(90) zoom 0.3+0.01
            ease_back 1.5 yoffset absolute(110) zoom 0.3-0.01
            repeat

        parallel:
            xoffset absolute(110)
            ease 1.5 xoffset absolute(90)
            ease 1.5 xoffset absolute(110)
            repeat

image CG quidditch cho_standing_panties_down:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-50, 35)
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/cho_standing_panties_down.webp"

        ease 5.0 zoom 0.3 offset (50, -5)
        ease 5.0 zoom 0.25 offset (-50, 35)

        repeat

    contains:
        "snitch"
        pos (630, -90)
        zoom 0.3

        parallel:
            yoffset absolute(110)
            ease_back 1.5 yoffset absolute(90) zoom 0.3+0.01
            ease_back 1.5 yoffset absolute(110) zoom 0.3-0.01
            repeat

        parallel:
            xoffset absolute(110)
            ease 1.5 xoffset absolute(90)
            ease 1.5 xoffset absolute(110)
            repeat

image CG quidditch cho_standing_snitch:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-50, 35)
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/cho_standing_snitch.webp"

        ease 5.0 zoom 0.3 offset (50, -5)
        ease 5.0 zoom 0.25 offset (-50, 35)

        repeat

image CG quidditch cho_sitting_snitch:
    subpixel True

    contains:
        "CG quidditch background"

    contains:
        zoom 0.25
        offset (-50, 35)
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/cho_sitting_snitch.webp"

        ease 5.0 zoom 0.3 offset (50, -5)
        ease 5.0 zoom 0.25 offset (-50, 35)

        repeat

image cho_quidditch2 slide cho_siting entry:

    contains:
        "images/CG/cho_quidditch2/slide/background.webp"

    contains:
        subpixel True
        ysize 376
        fit "contain"
        "images/CG/cho_quidditch2/slide/cho_sitting.webp"

        align (0.0, 0.5)
        easein_cubic 3.0 xalign 0.5 xoffset -50

        block:
            xoffset -50
            ease 5.0 xoffset 50
            ease 5.0 xoffset -50
            repeat

    contains:
        "images/CG/cho_quidditch2/slide/lines.webp"

image cho_quidditch2 slide cho_siting:

    contains:
        "images/CG/cho_quidditch2/slide/background.webp"

    contains:
        subpixel True
        ysize 376
        fit "contain"
        "images/CG/cho_quidditch2/slide/cho_sitting.webp"

        align (0.5, 0.5)

        block:
            xoffset -50
            ease 5.0 xoffset 50
            ease 5.0 xoffset -50
            repeat

    contains:
        "images/CG/cho_quidditch2/slide/lines.webp"

image cho_quidditch2 slide cho_standing:

    contains:
        "images/CG/cho_quidditch2/slide/background.webp"

    contains:
        ysize 376
        fit "contain"
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/slide/cho_standing.webp"

        block:
            xoffset -25
            ease 5.0 xoffset 25
            ease 5.0 xoffset -25
            repeat

    contains:
        "images/CG/cho_quidditch2/slide/lines.webp"

image cho_quidditch2 slide cho_standing_panties:

    contains:
        "images/CG/cho_quidditch2/slide/background.webp"

    contains:
        ysize 376
        fit "contain"
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/slide/cho_standing_panties.webp"

        block:
            xoffset -25
            ease 5.0 xoffset 25
            ease 5.0 xoffset -25
            repeat

    contains:
        "images/CG/cho_quidditch2/slide/lines.webp"

image cho_quidditch2 slide cho_standing_panties_down:

    contains:
        "images/CG/cho_quidditch2/slide/background.webp"

    contains:
        ysize 376
        fit "contain"
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/slide/cho_standing_panties_down.webp"

        block:
            xoffset -25
            ease 5.0 xoffset 25
            ease 5.0 xoffset -25
            repeat

    contains:
        "images/CG/cho_quidditch2/slide/lines.webp"

image cho_quidditch2 slide cho_sitting_snitch:

    contains:
        "images/CG/cho_quidditch2/slide/background.webp"

    contains:
        ysize 376
        fit "contain"
        align (0.5, 0.5)
        "images/CG/cho_quidditch2/slide/cho_sitting_snitch.webp"

        block:
            xoffset -25
            ease 5.0 xoffset 25
            ease 5.0 xoffset -25
            repeat

    contains:
        "images/CG/cho_quidditch2/slide/lines.webp"

# Image definitions

image cho_cg quidditch pose1 base:
    size (3840, 2880)

    contains: # BG
        "images/CG/cho_quidditch/background.webp"

    contains:
        contains: # Cho head
            "images/CG/cho_quidditch/pose1/head_1.webp"

        contains: # Cho eyes
            "images/CG/cho_quidditch/pose1/eyes_1.webp"
            choice:
                pause 4
            choice:
                pause 3
            choice:
                pause 2
            "images/CG/cho_quidditch/pose1/eyes_2.webp"
            pause 0.25
            repeat

        contains: # Cho eyebrows
            "images/CG/cho_quidditch/pose1/eyebrows_1.webp"

        contains: # Cho body
            "images/CG/cho_quidditch/pose1/body.webp"

        parallel:
            yoffset absolute(110)

            ease_back 2.5 yoffset absolute(50)
            ease_back 2.5 yoffset absolute(110)
            repeat

        parallel:
            xoffset absolute(-15)
            ease 1.5 xoffset absolute(15) xzoom 0.98 yzoom 0.995
            ease 1.5 xoffset absolute(-15) xzoom 1.0 yzoom 1.0
            repeat

    contains: # Overlay
        "images/CG/cho_quidditch/overlay.webp"

image cho_cg quidditch pose1 open:
    size (3840, 2880)

    contains: # BG
        "images/CG/cho_quidditch/background.webp"

    contains:
        contains: # Cho head
            "images/CG/cho_quidditch/pose1/head_2.webp"

        contains: # Cho eyes
            "images/CG/cho_quidditch/pose1/eyes_1.webp"
            choice:
                pause 4
            choice:
                pause 3
            choice:
                pause 2
            "images/CG/cho_quidditch/pose1/eyes_2.webp"
            pause 0.25
            repeat

        contains: # Cho eyebrows
            "images/CG/cho_quidditch/pose1/eyebrows_2.webp"

        contains: # Cho body
            "images/CG/cho_quidditch/pose1/body.webp"

        parallel:
            yoffset absolute(110)

            ease_back 2.5 yoffset absolute(50)
            ease_back 2.5 yoffset absolute(110)
            repeat

        parallel:
            xoffset absolute(-15)
            ease 1.5 xoffset absolute(15) xzoom 0.98 yzoom 0.995
            ease 1.5 xoffset absolute(-15) xzoom 1.0 yzoom 1.0
            repeat

    contains: # Overlay
        "images/CG/cho_quidditch/overlay.webp"

image cho_cg quidditch pose1 run:
    size (3840, 2880)

    contains: # BG
        "images/CG/cho_quidditch/background.webp"

    contains:
        contains: # Cho head
            "images/CG/cho_quidditch/pose1/head_1.webp"

        contains: # Cho eyes
            "images/CG/cho_quidditch/pose1/eyes_3.webp"
            choice:
                pause 4
            choice:
                pause 3
            choice:
                pause 2
            "images/CG/cho_quidditch/pose1/eyes_2.webp"
            pause 0.25
            repeat

        contains: # Cho eyebrows
            "images/CG/cho_quidditch/pose1/eyebrows_1.webp"

        contains: # Cho body
            "images/CG/cho_quidditch/pose1/body.webp"

        contains:
            "snitch"

            parallel:
                yoffset absolute(700)
                ease_back 0.5 yoffset absolute(500) zoom 1.0+0.25
                ease_back 0.5 yoffset absolute(700) zoom 1.0-0.2
                repeat

            parallel:
                xoffset absolute(150)
                easein_quint 0.7 xoffset absolute(300)
                easein_quint 0.75 xoffset absolute(15)
                repeat

        parallel:
            pause 1.0
            ease 3.0 pos (-4000, -2000) zoom 0.25

    contains: # Overlay
        "images/CG/cho_quidditch/overlay.webp"

image cho_cg quidditch pose2 smirk:
    size (3840, 2880)

    contains: # BG
        "images/CG/cho_quidditch/background.webp"

    contains:
        contains: # Cho head
            "images/CG/cho_quidditch/pose2/head_3.webp"

        contains: # Cho eyes
            "images/CG/cho_quidditch/pose2/eyes_1.webp"
            choice:
                pause 4
            choice:
                pause 3
            choice:
                pause 2
            "images/CG/cho_quidditch/pose2/eyes_2.webp"
            pause 0.25
            repeat

        contains: # Cho eyebrows
            "images/CG/cho_quidditch/pose2/eyebrows_1.webp"

        contains: # Cho body
            "images/CG/cho_quidditch/pose2/body.webp"

        parallel:
            yoffset absolute(110)

            ease_back 2.5 yoffset absolute(50)
            ease_back 2.5 yoffset absolute(110)
            repeat

        parallel:
            xoffset absolute(-15)
            ease 1.5 xoffset absolute(15) xzoom 0.98 yzoom 0.995
            ease 1.5 xoffset absolute(-15) xzoom 1.0 yzoom 1.0
            repeat

    contains: # Overlay
        "images/CG/cho_quidditch/overlay.webp"

image cho_cg quidditch pose2 slap_left:
    size (3840, 2880)

    contains: # BG
        "images/CG/cho_quidditch/background.webp"

    contains:
        contains: # Cho head
            "images/CG/cho_quidditch/pose2/head_1.webp"
            pause 2
            "images/CG/cho_quidditch/pose2/head_3.webp" with dissolve

        contains: # Cho eyes
            "images/CG/cho_quidditch/pose2/eyes_1.webp"
            choice:
                pause 4
            choice:
                pause 3
            choice:
                pause 2
            "images/CG/cho_quidditch/pose2/eyes_2.webp"
            pause 0.25
            repeat

        contains: # Cho eyebrows
            "images/CG/cho_quidditch/pose2/eyebrows_3.webp"
            pause 2
            "images/CG/cho_quidditch/pose2/eyebrows_2.webp" with dissolve

        contains: # Cho body
            "images/CG/cho_quidditch/pose2/body.webp"

        contains: # Slaps
            "images/CG/cho_quidditch/pose2/handprint_left.webp"

        parallel:
            yoffset absolute(110)

            ease_back 2.5 yoffset absolute(50)
            ease_back 2.5 yoffset absolute(110)
            repeat

        parallel:
            xoffset absolute(-15)
            ease 1.5 xoffset absolute(15) xzoom 0.98 yzoom 0.995
            ease 1.5 xoffset absolute(-15) xzoom 1.0 yzoom 1.0
            repeat

    contains: # Overlay
        "images/CG/cho_quidditch/overlay.webp"

image cho_cg quidditch pose2 slap_right:
    size (3840, 2880)

    contains: # BG
        "images/CG/cho_quidditch/background.webp"

    contains:
        contains: # Cho head
            "images/CG/cho_quidditch/pose2/head_1.webp"
            pause 2
            "images/CG/cho_quidditch/pose2/head_3.webp" with dissolve

        contains: # Cho eyes
            "images/CG/cho_quidditch/pose2/eyes_1.webp"
            choice:
                pause 4
            choice:
                pause 3
            choice:
                pause 2
            "images/CG/cho_quidditch/pose2/eyes_2.webp"
            pause 0.25
            repeat

        contains: # Cho eyebrows
            "images/CG/cho_quidditch/pose2/eyebrows_3.webp"
            pause 2
            "images/CG/cho_quidditch/pose2/eyebrows_2.webp" with dissolve

        contains: # Cho body
            "images/CG/cho_quidditch/pose2/body.webp"

        contains: # Slaps
            "images/CG/cho_quidditch/pose2/handprint_left.webp"

        contains: # Slaps
            "images/CG/cho_quidditch/pose2/handprint_right.webp"

        parallel:
            yoffset absolute(110)

            ease_back 2.5 yoffset absolute(50)
            ease_back 2.5 yoffset absolute(110)
            repeat

        parallel:
            xoffset absolute(-15)
            ease 1.5 xoffset absolute(15) xzoom 0.98 yzoom 0.995
            ease 1.5 xoffset absolute(-15) xzoom 1.0 yzoom 1.0
            repeat

    contains: # Overlay
        "images/CG/cho_quidditch/overlay.webp"

image cho_cg quidditch pose2 base:
    size (3840, 2880)

    contains: # BG
        "images/CG/cho_quidditch/background.webp"

    contains:
        contains: # Cho head
            "images/CG/cho_quidditch/pose2/head_1.webp"

        contains: # Cho eyes
            "images/CG/cho_quidditch/pose2/eyes_3.webp"
            choice:
                pause 4
            choice:
                pause 3
            choice:
                pause 2
            "images/CG/cho_quidditch/pose2/eyes_2.webp"
            pause 0.25
            repeat

        contains: # Cho eyebrows
            "images/CG/cho_quidditch/pose2/eyebrows_3.webp"

        contains: # Cho body
            "images/CG/cho_quidditch/pose2/body.webp"

        parallel:
            yoffset absolute(110)

            ease_back 2.5 yoffset absolute(50)
            ease_back 2.5 yoffset absolute(110)
            repeat

        parallel:
            xoffset absolute(-15)
            ease 1.5 xoffset absolute(15) xzoom 0.98 yzoom 0.995
            ease 1.5 xoffset absolute(-15) xzoom 1.0 yzoom 1.0
            repeat

    contains: # Overlay
        "images/CG/cho_quidditch/overlay.webp"

image cho_cg quidditch pose2 open:
    size (3840, 2880)

    contains: # BG
        "images/CG/cho_quidditch/background.webp"

    contains:
        contains: # Cho head
            "images/CG/cho_quidditch/pose2/head_2.webp"

        contains: # Cho eyes
            "images/CG/cho_quidditch/pose2/eyes_1.webp"
            choice:
                pause 4
            choice:
                pause 3
            choice:
                pause 2
            "images/CG/cho_quidditch/pose2/eyes_2.webp"
            pause 0.25
            repeat

        contains: # Cho eyebrows
            "images/CG/cho_quidditch/pose2/eyebrows_2.webp"

        contains: # Cho body
            "images/CG/cho_quidditch/pose2/body.webp"

        parallel:
            yoffset absolute(110)

            ease_back 2.5 yoffset absolute(50)
            ease_back 2.5 yoffset absolute(110)
            repeat

        parallel:
            xoffset absolute(-15)
            ease 1.5 xoffset absolute(15) xzoom 0.98 yzoom 0.995
            ease 1.5 xoffset absolute(-15) xzoom 1.0 yzoom 1.0
            repeat

    contains: # Overlay
        "images/CG/cho_quidditch/overlay.webp"
