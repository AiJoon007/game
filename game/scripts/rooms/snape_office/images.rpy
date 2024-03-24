
image snape_office_desk:
    zoom 0.5

    "images/rooms/snape_office/desk.webp"

image snape_office_statue:
    zoom 0.5

    "images/rooms/snape_office/statue.webp"

image snape_office_picture:
    zoom 0.5

    "images/rooms/snape_office/picture.webp"

image snape_office_shelves:
    zoom 0.5
    size (300, 350)

    "images/rooms/snape_office/shelves.webp"

image snape_office_shelves_anim:
    zoom 0.5
    pos (3, 10)
    yoffset 0
    alpha 1.0

    "images/rooms/snape_office/drip/01.webp"
    pause .2
    "images/rooms/snape_office/drip/02.webp"
    pause .2
    "images/rooms/snape_office/drip/03.webp"
    pause .2
    "images/rooms/snape_office/drip/04.webp"
    easeout_quart 1.25 yoffset 140
    linear 0.33 alpha 0.0
    pause 3.5
    repeat

image snape_office_shelves_alt:
    zoom 0.5
    size (300, 350)

    contains:
        "images/rooms/snape_office/shelves_alt.webp"

image snape_office_brewing_station_off:
    zoom 0.5

    "images/rooms/snape_office/brewing_station_off.webp"

image snape_office_brewing_station_on:
    zoom 0.5
    size (372, 248)

    "images/rooms/snape_office/brewing_station_on.webp"

image snape_office_brewing_station_smoke:
    zoom 0.5
    pos (104, -50)
    alpha 0.33

    "images/rooms/snape_office/smoke/01.webp"
    pause .15
    "images/rooms/snape_office/smoke/02.webp"
    pause .1
    "images/rooms/snape_office/smoke/03.webp"
    pause .1
    "images/rooms/snape_office/smoke/04.webp"
    pause .1
    "images/rooms/snape_office/smoke/05.webp"
    pause .1
    "images/rooms/snape_office/smoke/06.webp"
    pause .1
    "images/rooms/snape_office/smoke/07.webp"
    pause .1
    "images/rooms/snape_office/smoke/08.webp"
    pause .1
    "images/rooms/snape_office/smoke/09.webp"
    pause .11
    "images/rooms/snape_office/smoke/10.webp"
    pause .12
    "images/rooms/snape_office/smoke/11.webp"
    pause .13
    "images/rooms/snape_office/smoke/12.webp"
    pause .14
    "images/rooms/snape_office/smoke/13.webp"
    pause .15
    repeat

image snape_office_brewing_station_bloom:
    zoom 0.5
    pos (65, -20)
    alpha 0.2
    "images/rooms/snape_office/brewing_station_bloom.webp"
    easein 2.5 alpha 0.7
    easeout 2.5 alpha 0.2
    repeat

image snape_office_brewing_station_anim = Fixed("snape_office_brewing_station_smoke", "snape_office_brewing_station_bloom")

image snape_office_candelabra_off:
    zoom 0.5

    "images/rooms/snape_office/candelabra.webp"

image snape_office_candelabra_on:
    zoom 0.5
    size (141, 392)

    "images/rooms/snape_office/candelabra.webp"

image snape_office_candelabra_anim = Fixed("snape_office_candelabra_wax", "snape_office_candelabra_fire")#:

image snape_office_candelabra_wax:
    #contains:
    zoom 0.5
    alpha 1.0
    yoffset 0
    "images/rooms/snape_office/wax/01.webp"
    pause .2
    "images/rooms/snape_office/wax/02.webp"
    pause .2
    "images/rooms/snape_office/wax/03.webp"
    pause .2
    "images/rooms/snape_office/wax/04.webp"
    pause .2
    "images/rooms/snape_office/wax/05.webp"
    easeout_quart 1.0 yoffset 140
    linear 0.33 alpha 0.0
    pause 4
    repeat

image snape_office_candelabra_fire:
    zoom 0.5
    alpha 0.66

    Composite(
        (141, 392),
        (-32, -99), "candle_fire_01",
        (-64, -99), "candle_fire_02",
        (1, -99), "candle_fire_02",
        (-73, -77), "candle_fire_01",
        (10, -77), "candle_fire_01",
        (28, -76), "candle_fire_02",
        (-93, -76), "candle_fire_02",
        (-12, -78), "candle_fire_01",
        (-56, -78), "candle_fire_01",
        )

image snape_office_door:
    zoom 0.5

    "images/rooms/snape_office/door.webp"

image cauldron_off:
    size (114, 114)
    fit "contain"

    "interface/brewing/cauldron_off.webp"

image cauldron_on:
    size (114, 114)
    yoffset 5

    contains:
        fit "contain"

        "interface/brewing/cauldron_on.webp"

    contains:
        xalign 0.5
        ypos 5
        anchor (0.5, 1.0)
        zoom 1.5
        yzoom 0.7
        alpha 0.11

        "images/rooms/snape_office/smoke/01.webp"
        pause .15
        "images/rooms/snape_office/smoke/02.webp"
        pause .1
        "images/rooms/snape_office/smoke/03.webp"
        pause .1
        "images/rooms/snape_office/smoke/04.webp"
        pause .1
        "images/rooms/snape_office/smoke/05.webp"
        pause .1
        "images/rooms/snape_office/smoke/06.webp"
        pause .1
        "images/rooms/snape_office/smoke/07.webp"
        pause .1
        "images/rooms/snape_office/smoke/08.webp"
        pause .1
        "images/rooms/snape_office/smoke/09.webp"
        pause .11
        "images/rooms/snape_office/smoke/10.webp"
        pause .12
        "images/rooms/snape_office/smoke/11.webp"
        pause .13
        "images/rooms/snape_office/smoke/12.webp"
        pause .14
        "images/rooms/snape_office/smoke/13.webp"
        pause .15
        repeat
