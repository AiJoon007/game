default room_of_requirement = Room("room_of_requirement")

default ror_door_OBJ = RoomObject(room_of_requirement, "door", pos=(897, 315), idle="door_idle_night", action=Jump("main_room"), tooltip="Return to office")
default ror_mirror_OBJ = RoomObject(room_of_requirement, "mirror", pos=(180, 492), anchor=(0.5, 1.0), idle="mirror", hover="mirror_hover", action=Jump("mirror"), tooltip="Look into the mirror")

default mirror_image = Null()

screen room_of_requirement():
    tag room
    zorder 0
    sensitive room_menu_active

    default objects = sorted(room_of_requirement.objects, key=lambda x: x.zorder)

    add "images/rooms/room_of_requirement/corridor.webp" xzoom -1.0

    # Show a copy of chibi screen in the mirror
    $ mirror_chibi = renpy.get_screen("genie_chibi")
    if mirror_chibi:
        add mirror_chibi.copy() xzoom -1 xoffset 450-config.screen_width

    add mirror_image

    add "images/rooms/room_of_requirement/bg.webp"

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

screen room_of_requirement_overlay():
    zorder 5
    add "images/rooms/room_of_requirement/foreground.webp"

label room_of_requirement:
    show screen blkfade
    with d3

    call music_block

    call room("room_of_requirement")

    if not states.map.room_of_requirement.intro_e1:
        $ states.map.room_of_requirement.intro_e1 = True

        call gen_chibi("stand","door","base",flip=False)
        hide screen blkfade
        with d3

        stop music fadeout 1.0
        stop weather
        play sound "sounds/door.ogg"
        gen "..." ("base", xpos="far_left", ypos="head")
        play music "music/RoomOfReqIntro.ogg" if_changed
        call gen_chibi("stand","door","base")
        gen "It's just a room filled with a bunch of crap..." ("angry", xpos="far_left", ypos="head")
        call gen_chibi("stand","door","base",flip=False)
        gen "And a mirror?" ("base", xpos="far_left", ypos="head")

        call gen_walk("left", "base")

        call bld
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Odd, it appears the source of the magic is emanating from this mirror..." ("base", xpos="far_left", ypos="head")

        # Single line, doesn't deserve a defined character speaker.
        "Male Voice" "So you've found the mirror of Erised..."

        play sound "sounds/MaleGasp.ogg"
        stop music fadeout 1.0
        gen "Dumbledore!" ("angry", xpos="far_left", ypos="head")
        play sound "sounds/soft_wind.ogg"
        call sna_chibi("stand","door","base")
        call gen_chibi("stand", flip=True)
        gen "*Cough* I mean... Yes Severus, it is I...{w} \"Dumbledore\"." ("grin", xpos="far_left", ypos="head")
        gen "I'm so glad to be back..." ("base", xpos="far_left", ypos="head")
        sna "....." ("snape_05")
        gen "Worth a shot..." ("base", xpos="far_left", ypos="head")
        play music "music/song18.ogg" fadein 4 fadeout 1 if_changed
        sna "I'm quite certain I told you to stay in your office... For how long have you been roaming the school grounds?" ("snape_06")
        gen "This is the first time... hence why I was so lost." ("base", xpos="far_left", ypos="head")
        sna "....." ("snape_05")
        gen "Only for the past week or so..." ("base", xpos="far_left", ypos="head")
        sna "....." ("snape_07")
        gen "Yeah pretty much since the moment I got here." ("base", xpos="far_left", ypos="head")
        sna "*Sigh* Well, at least it doesn't appear you've been caught...{w} yet." ("snape_06")
        sna "So I wont stop you as long as you refrain from any of your...{w=0.6} weird requests or comments to other staff members." ("snape_05")
        gen "...." ("base", xpos="far_left", ypos="head")

        if clothing_store_intro_done:
            sna "....." ("snape_03")
            gen "I might have ordered a few oddities from Madam Mafkin..." ("base", xpos="far_left", ypos="head")
            sna "Hahahah... That old hag?" ("snape_28")
            sna "She's nuts, she can sew that's for damn sure but she'd never know nor care... do whatever you want with her." ("snape_01")
            gen "(I'd rather not...)" ("base", xpos="far_left", ypos="head")
            sna "Continuing where I left off." ("snape_09")

        sna "Now, this mirror that you've found..." ("snape_01")
        sna "I thought Albus would've moved it out of the school after the last incident..." ("snape_22")
        call gen_chibi("stand", flip=False)
        with d3
        show screen bld1

        gen "What kind of incident? It's just some dusty old mirror... why would Dumbledore care about it? And what's going on with this room?" ("base", xpos="far_left", ypos="head")
        sna "I don't know about the room, I'm more concerned by this mirror. Why don't you have a look in it and tell me what you see?" ("snape_01")
        gen "*Squints* Just seems like an old mirror to me, a bit dusty and cloudy thou... hold on a minute." ("base", xpos="far_left", ypos="head")

        $ mirror_image = "images/rooms/room_of_requirement/agrabah.webp"

        sna "....." ("snape_23")
        gen "... I see myself... I've won the house cup!" ("angry", xpos="far_left", ypos="head")
        sna "Really?" ("snape_05")
        gen "No, I can see myself in Agrabah. I'm surrounded by a harem of women all dedicated to pleasing me." ("base", xpos="far_left", ypos="head")
        sna "You really are nothing more than a sexual deviant are you?" ("snape_02")
        gen "Pretty much." ("base", xpos="far_left", ypos="head")
        sna "The mirror is known as the mirror of Erised, or Desire backwards..." ("snape_09")
        gen "Very clever..." ("grin", xpos="far_left", ypos="head")
        sna "Quite... in short, it's designed to show you your deepest desire... but by your comment I'm sure you already got that." ("snape_05")
        gen "Your magic might be foreign to me but this seems like nothing more than a party trick, I already know what I desire." ("base", xpos="far_left", ypos="head")
        sna "Well, it would be quite dull... if you didn't include the changes I made that had it locked up in the first place." ("snape_20")
        gen "I could probably make a good guess already but please, do tell..." ("base", xpos="far_left", ypos="head")
        sna "The intended purpose was far too boring, so I modified the enchantment. This would be incredibly difficult for a lesser wizard, but genius like I am..." ("snape_23")
        gen "Booooring." ("base", xpos="far_left", ypos="head")
        sna "It's a porn creator..." ("snape_03")

        $ mirror_image = Null()

        call gen_chibi("stand_shocked", flip=True)
        gen "A what?!" ("open", xpos="far_left", ypos="head")

        sna "A porn creator. Well, technically it's used to let you live out your fantasies, be they impure or not. So not necessarily porn." ("snape_01")
        gen "And you didn't tell me a thing like this existed?" ("open", xpos="far_left", ypos="head")
        sna "Well, it didn't exist until I made it... and I thought it was moved or destroyed." ("snape_26")

        call gen_chibi("stand", flip=False)
        gen "Get out." ("angry", xpos="far_left", ypos="head")

        sna "What?" ("snape_05")
        gen "I said get out, I found it so I get to keep it." ("grin", xpos="far_left", ypos="head")
        sna "But, I thought maybe I could move..." ("snape_06")
        gen "It's staying right where it is, I've been getting incredibly bored lately and might consider roaming the school a bit more... actually, I feel the urge to take a trip to the girls dormitory right now." ("angry", xpos="far_left", ypos="head")
        sna "Fine, it stays. Please don't... just remember that it will take time for it to reshape and create imagery so check back every now and then." ("snape_06")
        gen "Noted... Out. Now." ("base", xpos="far_left", ypos="head")

        hide snape_main
        hide screen bld1
        call give_reward("You've unlocked the room of requirement","images/rooms/room_of_requirement/mirror_hover.webp")
        $ achievements.unlock("mirror")
        call sna_chibi("hide")
        call gen_chibi("hide")
    else:
        $ mirror_image = Null()
        play music "music/song18.ogg" fadein 4 fadeout 1 if_changed
        call gen_chibi("stand", "door", "base", flip=False)
        call hide_blkfade

        call gen_walk(200, "base")

    $ mirror_image = "images/rooms/room_of_requirement/agrabah.webp"
    call gen_chibi("stand", "left", "base", flip=False)
    call hide_blkfade
    call screen room_menu
