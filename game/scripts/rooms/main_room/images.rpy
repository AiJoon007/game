
image fireplace_fire:
    animation
    offset (-24, -6)
    "images/rooms/main_room/fireplace/fireplace_fire_01.webp"
    pause.1
    "images/rooms/main_room/fireplace/fireplace_fire_02.webp"
    pause.1
    "images/rooms/main_room/fireplace/fireplace_fire_03.webp"
    pause.1
    "images/rooms/main_room/fireplace/fireplace_fire_04.webp"
    pause.1
    "images/rooms/main_room/fireplace/fireplace_fire_05.webp"
    pause.1
    "images/rooms/main_room/fireplace/fireplace_fire_06.webp"
    pause.1
    "images/rooms/main_room/fireplace/fireplace_fire_07.webp"
    pause.1
    "images/rooms/main_room/fireplace/fireplace_fire_08.webp"
    pause.1
    repeat

image glow_effect:
    animation
    "images/animation/glow_effect/glow_1.webp"
    pause.1
    "images/animation/glow_effect/glow_2.webp"
    pause.1
    "images/animation/glow_effect/glow_3.webp"
    pause.1
    "images/animation/glow_effect/glow_4.webp"
    pause.2
    "images/animation/glow_effect/glow_3.webp"
    pause.1
    "images/animation/glow_effect/glow_2.webp"
    pause.1
    "images/animation/glow_effect/glow_4.webp"
    pause.2
    "images/animation/glow_effect/glow_3.webp"
    pause.1
    "images/animation/glow_effect/glow_2.webp"
    pause.1
    "images/animation/glow_effect/glow_1.webp"
    pause.1
    repeat

image glow_effect_fireplace:
    zoom 0.5
    align (0.5, 0.5)
    offset (0, 30)
    alpha 0.5

    "glow_effect"

image candle_fire_01:
    animation
    "images/rooms/main_room/candles/fire_01.webp"
    pause.1
    "images/rooms/main_room/candles/fire_02.webp"
    pause.1
    "images/rooms/main_room/candles/fire_03.webp"
    pause.1
    "images/rooms/main_room/candles/fire_04.webp"
    pause.1
    "images/rooms/main_room/candles/fire_05.webp"
    pause.1
    "images/rooms/main_room/candles/fire_06.webp"
    pause.1
    "images/rooms/main_room/candles/fire_07.webp"
    pause.1
    "images/rooms/main_room/candles/fire_08.webp"
    pause.1
    "images/rooms/main_room/candles/fire_09.webp"
    pause.1
    "images/rooms/main_room/candles/fire_10.webp"
    choice:
        pause.1
    choice:
        pause.2
    choice:
        pause.15
    repeat

image candle_fire_02:
    animation
    "images/rooms/main_room/candles/fire_01.webp"
    pause.1
    "images/rooms/main_room/candles/fire_04.webp"
    pause.1
    "images/rooms/main_room/candles/fire_03.webp"
    pause.1
    "images/rooms/main_room/candles/fire_02.webp"
    pause.1
    "images/rooms/main_room/candles/fire_08.webp"
    pause.1
    "images/rooms/main_room/candles/fire_06.webp"
    pause.1
    "images/rooms/main_room/candles/fire_07.webp"
    pause.1
    "images/rooms/main_room/candles/fire_05.webp"
    pause.1
    "images/rooms/main_room/candles/fire_10.webp"
    pause.1
    "images/rooms/main_room/candles/fire_09.webp"
    choice:
        pause.1
    choice:
        pause.2
    choice:
        pause.15
    repeat

image phoenix_idle:
    animation
    zoom 0.5

    "images/rooms/main_room/phoenix/phoenix_01.webp"
    pause 2
    "images/rooms/main_room/phoenix/phoenix_02.webp"
    pause.15
    "images/rooms/main_room/phoenix/phoenix_03.webp"
    pause.15
    "images/rooms/main_room/phoenix/phoenix_02.webp"
    pause.15
    "images/rooms/main_room/phoenix/phoenix_01.webp"
    pause.15
    "images/rooms/main_room/phoenix/phoenix_02.webp"
    pause.15
    "images/rooms/main_room/phoenix/phoenix_03.webp"
    pause.15
    "images/rooms/main_room/phoenix/phoenix_02.webp"
    pause.15
    "images/rooms/main_room/phoenix/phoenix_01.webp"
    pause 10
    repeat

image phoenix_hover:
    zoom 0.5

    "images/rooms/main_room/phoenix/phoenix_hover.webp"

image phoenix_feather:
    animation
    zoom 0.5
    pause 10
    alpha 1.0
    "images/rooms/main_room/phoenix/feather_ani/pho_01.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_02.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_03.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_04.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_05.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_06.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_07.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_08.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_09.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_10.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_11.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_12.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_13.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_14.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_15.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_16.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_17.webp"
    pause.15
    "images/rooms/main_room/phoenix/feather_ani/pho_18.webp"
    pause 10
    linear .5 alpha 0.0
    repeat

image phoenix_food:
    zoom 0.5

    "images/rooms/main_room/phoenix/food.webp"

image door_idle:
    zoom 0.5

    "images/rooms/main_room/door/door_idle.webp"

image door_hover:
    zoom 0.5

    "images/rooms/main_room/door/door_hover.webp"

image fireplace_idle:
    zoom 0.5

    "images/rooms/main_room/fireplace/fireplace_idle.webp"

image fireplace_idle_shadow:
    zoom 0.5

    "images/rooms/main_room/fireplace/fireplace_w_shadow.webp"

image fireplace_hover:
    zoom 0.5

    "images/rooms/main_room/fireplace/fireplace_hover.webp"

image owl_idle:
    animation
    zoom 0.5

    "images/rooms/main_room/mail/owl_idle_01.webp"
    pause.1
    "images/rooms/main_room/mail/owl_idle_02.webp"
    pause.1
    "images/rooms/main_room/mail/owl_idle_03.webp"
    pause.15
    "images/rooms/main_room/mail/owl_idle_02.webp"
    pause.1
    "images/rooms/main_room/mail/owl_idle_01.webp"
    pause 7
    repeat

image owl_letter:
    animation
    zoom 0.5

    "images/rooms/main_room/mail/owl_01.webp"
    pause.1
    "images/rooms/main_room/mail/owl_02.webp"
    pause.1
    "images/rooms/main_room/mail/owl_03.webp"
    pause.15
    "images/rooms/main_room/mail/owl_02.webp"
    pause.1
    "images/rooms/main_room/mail/owl_01.webp"
    pause 7
    repeat

image owl_letter_hover:
    zoom 0.5

    "images/rooms/main_room/mail/owl_hover.webp"

image parcel:
    "images/rooms/main_room/parcel/idle.webp"

image cupboard_idle:
    zoom 0.5
    "images/rooms/main_room/cupboard/cupboard_w_shadow.webp"

image cupboard_open:
    zoom 0.5
    "images/rooms/main_room/cupboard/cupboard_open.webp"

image main_room_idle_day:
    zoom 0.5
    "images/rooms/main_room/bg_day.webp"

image main_room_idle_night:
    zoom 0.5
    "images/rooms/main_room/bg_night.webp"

image candle_left:
    zoom 0.5

    "images/rooms/main_room/candles/candleM.webp"

image candle_right:
    zoom 0.5

    "images/rooms/main_room/candles/candle.webp"

image candle_fire: #Candle fire.
    animation
    "images/rooms/main_room/candles/fire_01.webp"
    pause.1
    "images/rooms/main_room/candles/fire_04.webp"
    pause.1
    "images/rooms/main_room/candles/fire_03.webp"
    pause.1
    "images/rooms/main_room/candles/fire_02.webp"
    pause.1
    "images/rooms/main_room/candles/fire_08.webp"
    pause.1
    "images/rooms/main_room/candles/fire_06.webp"
    pause.1
    "images/rooms/main_room/candles/fire_07.webp"
    pause.1
    "images/rooms/main_room/candles/fire_05.webp"
    pause.1
    "images/rooms/main_room/candles/fire_10.webp"
    pause.1
    "images/rooms/main_room/candles/fire_09.webp"
    pause.1
    repeat

image desk_empty:
    zoom 0.5

    "images/rooms/main_room/desk_empty.webp"

image chair_right:
    zoom 0.5

    "images/rooms/main_room/chair_right.webp"

image chair_left:
    zoom 0.5

    "images/rooms/main_room/chair_left.webp"

image letter_on_desk:
    zoom 0.5

    "/images/rooms/main_room/desk/letter.webp"

image plant_on_desk:
    zoom 0.5

    "/images/rooms/main_room/desk/plant.webp"

image letter_and_plant_on_desk:

    contains:
        zoom 0.5

        "/images/rooms/main_room/desk/letter.webp"

    contains:
        zoom 0.5

        "/images/rooms/main_room/desk/plant.webp"

image desk_dumbledore:
    zoom 0.5

    "images/rooms/main_room/dum.webp"

image halloween_chandelier:
    animation

    contains:
        anchor (0.5, 0.0)
        "images/rooms/main_room/decorations/halloween_chandelier.webp"

    contains:
        offset (-266, 6)
        "candle_fire_01"

    contains:
        offset (-102, 51)
        "candle_fire_02"

    contains:
        offset (62, 4)
        "candle_fire_02"

    ease_quad 6.0 rotate 18
    ease_quad 6.0 rotate -18

    repeat

image halloween_fireplace_jackolanterns:
    offset (36, 78)
    "images/rooms/main_room/decorations/halloween_fireplace2.webp"

image halloween_window_monster:
    animation
    "images/rooms/main_room/decorations/halloween_monster/0.webp"
    pause 3
    "images/rooms/main_room/decorations/halloween_monster/1.webp"
    pause 0.1
    "images/rooms/main_room/decorations/halloween_monster/2.webp"
    pause 0.1
    "images/rooms/main_room/decorations/halloween_monster/3.webp"
    pause 0.25
    "images/rooms/main_room/decorations/halloween_monster/2.webp"
    pause 0.1
    "images/rooms/main_room/decorations/halloween_monster/1.webp"
    pause 0.25
    "images/rooms/main_room/decorations/halloween_monster/2.webp"
    pause 0.1
    "images/rooms/main_room/decorations/halloween_monster/3.webp"
    pause 0.5
    "images/rooms/main_room/decorations/halloween_monster/2.webp"
    pause 0.1
    "images/rooms/main_room/decorations/halloween_monster/1.webp"
    pause 0.1

    repeat

image halloween_cupboard_caskets:
    offset (12, 318)

    "images/rooms/main_room/decorations/halloween_cupboard2.webp"

image halloween_chair_caskets:
    offset (55, 105)
    "images/rooms/main_room/decorations/halloween_chair.webp"

image halloween_bats_trophy:
    offset (-74, -34)
    "images/rooms/main_room/decorations/bats_trophy.webp"

image halloween_lamp_left:
    offset (-10, -6)
    "images/rooms/main_room/decorations/halloween_lamp/left.webp"

image halloween_lamp_left_glow:
    zoom 0.5
    offset (-111, -81)

    contains:
        animation
        alpha 0.9

        "images/rooms/main_room/decorations/halloween_lamp/glow.webp"

        pause 2.0
        ease_bounce 3.0 alpha 0.75
        ease_bounce 1.0 alpha 0.9

        repeat

    contains:
        "images/rooms/main_room/decorations/halloween_lamp/filament.webp"

image halloween_lamp_right:
    offset (-10, -6)
    "images/rooms/main_room/decorations/halloween_lamp/right.webp"

image halloween_lamp_right_glow:
    zoom 0.5
    offset (-111, -81)

    contains:
        animation
        alpha 0.9

        "images/rooms/main_room/decorations/halloween_lamp/glow.webp"

        choice:
            pause 2.0
        choice:
            pause 3.0
        choice:
            pause 1.5

        ease_bounce 3.0 alpha 0.75
        ease_bounce 1.0 alpha 0.9

        repeat

    contains:
        "images/rooms/main_room/decorations/halloween_lamp/filament.webp"

image snow_owl_idle:
    zoom 0.5
    offset (-3, -3)

    "images/rooms/main_room/decorations/snow_owl/idle_0.webp"
    pause.1
    "images/rooms/main_room/decorations/snow_owl/idle_1.webp"
    pause.1
    "images/rooms/main_room/decorations/snow_owl/idle_2.webp"
    pause.15
    "images/rooms/main_room/decorations/snow_owl/idle_1.webp"
    pause.1
    "images/rooms/main_room/decorations/snow_owl/idle_0.webp"
    pause 7
    repeat

image snow_owl_letter:
    zoom 0.5
    offset (-3, -3)

    "images/rooms/main_room/decorations/snow_owl/letter_0.webp"
    pause.1
    "images/rooms/main_room/decorations/snow_owl/letter_1.webp"
    pause.1
    "images/rooms/main_room/decorations/snow_owl/letter_2.webp"
    pause.15
    "images/rooms/main_room/decorations/snow_owl/letter_1.webp"
    pause.1
    "images/rooms/main_room/decorations/snow_owl/letter_0.webp"
    pause 7
    repeat

image snow_owl_letter_hover:
    zoom 0.5
    offset (-3, -3)

    "images/rooms/main_room/decorations/snow_owl/letter_hover.webp"

image small_owl_idle:
    zoom 0.5
    offset (-1, -3)

    "images/rooms/main_room/decorations/small_owl/idle_0.webp"
    pause.1
    "images/rooms/main_room/decorations/small_owl/idle_1.webp"
    pause.1
    "images/rooms/main_room/decorations/small_owl/idle_2.webp"
    pause.15
    "images/rooms/main_room/decorations/small_owl/idle_1.webp"
    pause.1
    "images/rooms/main_room/decorations/small_owl/idle_0.webp"
    pause 7
    repeat

image small_owl_letter:
    zoom 0.5
    offset (-1, -3)

    "images/rooms/main_room/decorations/small_owl/letter_0.webp"
    pause.1
    "images/rooms/main_room/decorations/small_owl/letter_1.webp"
    pause.1
    "images/rooms/main_room/decorations/small_owl/letter_2.webp"
    pause.15
    "images/rooms/main_room/decorations/small_owl/letter_1.webp"
    pause.1
    "images/rooms/main_room/decorations/small_owl/letter_0.webp"
    pause 7
    repeat

image small_owl_letter_hover:
    zoom 0.5
    offset (-1, -3)

    "images/rooms/main_room/decorations/small_owl/letter_hover.webp"

image xmas_lights_static:

    contains:
        alpha 0.5
        "images/rooms/main_room/decorations/xmas_lights/underlay.webp"

    contains:
        "xmas_lights_set1_bulbs"

    contains:
        "xmas_lights_set2_bulbs"

    contains:
        "images/rooms/main_room/decorations/xmas_lights/base.webp"

    contains:
        "xmas_lights_set1_glow"

    contains:
        "xmas_lights_set2_glow"

image xmas_lights_alternate:
    contains:
        alpha 0.5
        "images/rooms/main_room/decorations/xmas_lights/underlay.webp"

    contains:
        animation
        alpha 1.0
        "xmas_lights_set1_bulbs"
        linear 0.5 alpha 0.5
        linear 0.5 alpha 1.0
        repeat

    contains:
        animation
        alpha 0.5
        "xmas_lights_set2_bulbs"
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0.5
        repeat

    contains:
        "images/rooms/main_room/decorations/xmas_lights/base.webp"

    contains:
        animation
        alpha 1.0
        "xmas_lights_set1_glow"
        linear 0.5 alpha 0.0
        linear 0.5 alpha 1.0
        repeat

    contains:
        animation
        alpha 0.0
        "xmas_lights_set2_glow"
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0.0
        repeat

image xmas_lights_cycle:
    contains:
        alpha 0.5
        "images/rooms/main_room/decorations/xmas_lights/underlay.webp"

    contains:
        animation
        matrixcolor HueMatrix(0)
        "xmas_lights_set1_bulbs"
        linear 18.0 matrixcolor HueMatrix(360)
        repeat

    contains:
        animation
        matrixcolor HueMatrix(0)
        "xmas_lights_set2_bulbs"
        linear 18.0 matrixcolor HueMatrix(360)
        repeat

    contains:
        "images/rooms/main_room/decorations/xmas_lights/base.webp"

    contains:
        animation
        matrixcolor HueMatrix(0)
        "xmas_lights_set1_glow"
        linear 18.0 matrixcolor HueMatrix(360)
        repeat

    contains:
        animation
        matrixcolor HueMatrix(0)
        "xmas_lights_set2_glow"
        linear 18.0 matrixcolor HueMatrix(360)
        repeat

image xmas_lights_pulse:
    contains:
        alpha 0.5
        "images/rooms/main_room/decorations/xmas_lights/underlay.webp"

    contains:
        animation
        alpha 1.0
        "xmas_lights_set1_bulbs"
        easeout 3.5 alpha 0.0
        pause 3
        easein 3.5 alpha 1.0
        pause 3
        repeat

    contains:
        animation
        alpha 1.0
        "xmas_lights_set2_bulbs"
        easeout 3.5 alpha 0.0
        pause 3
        easein 3.5 alpha 1.0
        pause 3
        repeat

    contains:
        "images/rooms/main_room/decorations/xmas_lights/base.webp"

    contains:
        animation
        alpha 1.0
        "xmas_lights_set1_glow"
        easeout 3.5 alpha 0.0
        pause 3
        easein 3.5 alpha 1.0
        pause 3
        repeat

    contains:
        animation
        alpha 1.0
        "xmas_lights_set2_glow"
        easeout 3.5 alpha 0.0
        pause 3
        easein 3.5 alpha 1.0
        pause 3
        repeat

image xmas_wreaths:
    pos (35, -65)

    "images/rooms/main_room/decorations/xmas_wreaths.webp"

image xmas_giftchair:
    pos (35, 108)

    "images/rooms/main_room/decorations/xmas_giftchair.webp"

image xmas_window_santa_doodle:
    size (2160, 1200)
    contains:
        animation
        size (240, 108)
        subpixel True
        offset (640, 460)

        contains:
            fit "fill"
            "xmas_window_santa_base"
        contains:
            animation
            fit "fill"
            "xmas_window_santa_light"

            linear 0.5 alpha 0.1
            linear 0.5 alpha 1.0
            repeat

        linear 10.0 xoffset 1000
        pause 10.0
        repeat

image xmas_window_santa = AlphaMask("xmas_window_santa_doodle", "xmas_window_santa_mask")
