
default snape_office = Room("snape_office")

default snape_office_brewing_station_OBJ = RoomObject(snape_office, "snape_office_brewing_station", pos=(367, 325), idle="snape_office_brewing_station_off", focus_mask=None, action=Jump("brewing_station"), tooltip="Brewing Station", zorder=-1)
default snape_office_shelves_OBJ = RoomObject(snape_office, "snape_office_shelves", pos=(695, 240), idle="snape_office_shelves", foreground="snape_office_shelves_anim", focus_mask=None, action=Jump("shelves"), tooltip="Shelves", zorder=-1)
default snape_office_picture_OBJ = RoomObject(snape_office, "snape_office_picture", pos=(879, 219), idle="snape_office_picture", action=Jump("snape_picture"), tooltip="Picture", zorder=-1)
default snape_office_statue_OBJ = RoomObject(snape_office, "snape_office_statue", pos=(541, 137), idle="snape_office_statue", action=Jump("snake_statue"), tooltip="Snake Head", zorder=-1)
default snape_office_desk_OBJ = RoomObject(snape_office, "snape_office_desk", pos=(737, 369), idle="snape_office_desk", action=Jump("snape_at_desk"), tooltip="Snape's Desk", zorder=0)
default snape_office_candelabra_OBJ = RoomObject(snape_office, "snape_office_candelabra", pos=(540, 300), idle="snape_office_candelabra_on", foreground="snape_office_candelabra_anim", focus_mask=None, action=Jump("candelabra"), tooltip="Examine", zorder=0)
default snape_office_door_OBJ = RoomObject(snape_office, "snape_office_door", pos=(185, 307), idle="snape_office_door", action=Jump("snape_office_door"), tooltip="Return to office", zorder=0)

screen snape_office():
    tag room
    zorder 0
    sensitive room_menu_active

    default objects = sorted(snape_office.objects, key=lambda x: x.zorder)

    add "images/rooms/snape_office/bg.webp" zoom 0.5

    for obj in objects:
        imagebutton:
            anchor obj.get_anchor()
            pos obj.get_pos()
            idle obj.get_idle()
            hover obj.get_hover()
            foreground obj.foreground
            background obj.background
            focus_mask obj.focus_mask
            tooltip obj.tooltip
            hovered obj.hovered
            unhovered obj.unhovered
            action obj.action

    add "images/rooms/snape_office/vignette.webp" zoom 0.5

label snape_office:
    call room("snape_office")
    play music "music/the-other-side-of-the-door-by-kevin-macleod-from-filmmusic-io.ogg" fadein 1 if_changed

    if game.daytime:
        $ snape_office_desk_OBJ.set_image("snape_office_desk")
        $ snape_office_brewing_station_OBJ.set_image("snape_office_brewing_station_off")
        $ snape_office_brewing_station_OBJ.foreground = None
    else:
        $ snape_office_desk_OBJ.set_image("snape_desk_work")
        $ snape_office_brewing_station_OBJ.set_image("snape_office_brewing_station_on")
        $ snape_office_brewing_station_OBJ.foreground = "snape_office_brewing_station_anim"

    call gen_walk(action="enter", xpos="door", ypos="base", speed=1.5, flip=True)

    jump quests

label snape_office_menu:
    hide screen bld1
    with d3

    call screen room_menu
