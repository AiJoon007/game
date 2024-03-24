default seventh_floor = Room("seventh_floor")

default seventh_door_OBJ = RoomObject(seventh_floor, "door", pos=(540, 374), anchor=(0.5, 1.0), idle="seventh_door", action=Jump("room_of_requirement"), tooltip="Enter", hidden=True)
default seventh_fire_basin_OBJ = RoomObject(seventh_floor, "fire_basin", pos=(478, 434), anchor=(0.5, 1.0), idle="seventh_fire_basin", action=None)
default seventh_fire_basin_right_OBJ = RoomObject(seventh_floor, "fire_basin", pos=(602, 434), anchor=(0.5, 1.0), idle="seventh_fire_basin_right", action=None)

screen seventh_floor():
    tag room
    zorder 0
    sensitive room_menu_active

    default objects = sorted(seventh_floor.objects, key=lambda x: x.zorder)

    add "images/rooms/seventh_floor/bg.webp" zoom 0.5

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

label seventh_floor:
    call room("seventh_floor")
    call reset_menu_position
    play music "music/the-chamber-by-kevin-macleod.ogg" fadein 1 fadeout 3 if_changed
    call gen_chibi("stand", -100, "base")
    call gen_walk(xpos="left_mid", ypos="base", speed=1.5)

    if not states.map.seventh_floor.visited:
        $ states.map.seventh_floor.visited = True

        gen "So... The diary mentioned he was walking around here." ("base", xpos="far_left", ypos="head")

        call gen_walk("right", speed=1.5)

        gen "I can definitely sense a strong magical energy in this place..." ("base", xpos="far_left", ypos="head")

        call gen_walk("left_mid", speed=1.5)

        gen "Maybe if I... Or I could..." ("base", xpos="far_left", ypos="head")

        call gen_walk("right", speed=1.5)
        pause .6
        call gen_chibi(flip=False)

        gen "..." ("base", xpos="far_left", ypos="head")
        gen "I could be in my office jacking off right now!" ("angry", xpos="far_left", ypos="head")

        $ seventh_door_OBJ.hidden = False
        with d5

        call gen_chibi("stand_alt", flip=False)
        pause.8

        gen "Well then... Will you look at that!" ("grin", xpos="far_left", ypos="head")

    call screen room_menu
