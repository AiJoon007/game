
default boxing_ring = Room("boxing_ring")
default boxing_ring_lights = False

screen boxing_ring():
    tag room
    zorder 0
    sensitive False

    # default objects = sorted(boxing_ring.objects, key=lambda x: x.zorder)

    add "images/rooms/boxing_ring/bg.webp" zoom 0.5
    add "boxing_ring crowd_back" zoom 0.5
    add "images/rooms/boxing_ring/stands.webp" zoom 0.5
    add "boxing_ring flash_back"
    add "images/rooms/boxing_ring/ring.webp" zoom 0.5

    # for obj in objects:
    #     imagebutton:
    #         anchor obj.get_anchor()
    #         pos obj.get_pos()
    #         idle obj.get_idle()
    #         hover obj.get_hover()
    #         foreground obj.foreground
    #         background obj.background
    #         focus_mask obj.focus_mask
    #         tooltip obj.tooltip
    #         hovered obj.hovered
    #         unhovered obj.unhovered
    #         action obj.action

screen boxing_ring_overlay():
    tag room_overlay
    zorder 7

    add "boxing_ring microphone" zoom 0.5
    add "images/rooms/boxing_ring/vignette.webp" zoom 0.5
    add "boxing_ring dust" zoom 0.5

    if boxing_ring_lights:
        add "images/rooms/boxing_ring/lights.webp" zoom 0.5

    add "boxing_ring flash_front"
    add "boxing_ring crowd_front" zoom 0.5

    if not boxing_ring_lights:
        add "black" alpha 0.5

# label snape_office:
#     call room("snape_office")
#     play music "music/the-other-side-of-the-door-by-kevin-macleod-from-filmmusic-io.ogg" fadein 1 if_changed

#     if game.daytime:
#         $ snape_office_desk_OBJ.set_image("snape_office_desk")
#         $ snape_office_brewing_station_OBJ.set_image("snape_office_brewing_station_off")
#         $ snape_office_brewing_station_OBJ.foreground = None
#     else:
#         $ snape_office_desk_OBJ.set_image("snape_desk_work")
#         $ snape_office_brewing_station_OBJ.set_image("snape_office_brewing_station_on")
#         $ snape_office_brewing_station_OBJ.foreground = "snape_office_brewing_station_anim"

#     call gen_walk(action="enter", xpos="door", ypos="base", speed=1.5, flip=True)

#     jump quests
