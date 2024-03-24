
label map_attic:
    if states.her.ev.sealed_scroll.sample:
        gen "(I have no reason to go there anymore.)" ("base", xpos="far_left", ypos="head")

        jump desk
    else:
        $ states.her.ev.sealed_scroll.sample = True

        gen "(The attic, *huh*...)" ("base", xpos="far_left", ypos="head")
        gen "(I guess I could check it out.)" ("base", xpos="far_left", ypos="head")

        stop music fadeout 3.0
        stop weather fadeout 3.0

        pause 1.0
        play sound "sounds/run_04.ogg"
        play weather "sounds/wind_long_loop.ogg" fadein 2 fadeout 2

        nar "You find your way through the winding staircases to the attic door."
        gen "*Hmm*... hopefully this is the right place to use that key." ("base", xpos="far_left", ypos="head")
        play background "sounds/pulse.ogg"
        nar "As you approach the door, the lock begins to glow..."
        nar "Looking down at the key in your hand, you notice the same glow around the key..."
        gen "Well, this has to be it then..." ("base", xpos="far_left", ypos="head")
        stop background fadeout 2.0
        play sound "sounds/09_lock.ogg"
        pause 2.0
        play sound "sounds/door.ogg"
        nar "After unlocking the door, you're presented with a dusty room filled with random junk and knick-knacks."
        play sound "sounds/cough_male.ogg"
        gen "...*Cough* *Cough*..." ("open", xpos="far_left", ypos="head")
        gen "This room is just filled with random junk and knick-knacks!" ("angry", xpos="far_left", ypos="head")
        gen "(So now what... Am I supposed to take a piece of something and use with this scroll?)" ("base", xpos="far_left", ypos="head")
        gen "(I don't even know what the scroll is supposed to do, how am I going to find what it wants me to use!)" ("base", xpos="far_left", ypos="head")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "(Screw it... I'm just going to cheat and check the item description in my inventory.)" ("base", xpos="far_left", ypos="head")
        gen "(Let's see what it says...)" ("base", xpos="far_left", ypos="head")
        gen "(Turns the user into a magical tentacle plant with the usage of living plant material.)" ("base", xpos="far_left", ypos="head")
        gen "Well, well... that could be useful..." ("base", xpos="far_left", ypos="head")
        gen "So I guess this tentacle plant should be here somewhe--" ("base", xpos="far_left", ypos="head")
        nar "As you scan the room, you notice a slender piece of vine poking out from behind some crates, as if to avoid the light."
        gen "This must be it." ("base", xpos="far_left", ypos="head")
        play sound "sounds/slash.ogg"
        nar "You make a clean cut, when suddenly...{nw}"
        play sound "sounds/mondead.ogg"
        nar "You make a clean cut, when suddenly...{fast}"
        gen "I better get the fuck out of here." ("angry", xpos="far_left", ypos="head")
        play sound "sounds/mon.ogg"
        nar "As you shut the door, you hear the room erupt in a series of loud crashes and growling."

        play sound "sounds/run_04.ogg"
        nar "You hastily make your way towards your office."

        call gen_walk(action="enter")

        stop weather
        call music_block

        gen "(A tentacle plant and a body-bending magical scroll, *huh*...)" ("base", xpos="far_left", ypos="head")
        gen "(Maybe I could use it to have some fun with Miss Granger...)" ("grin", xpos="far_left", ypos="head")

        menu:
            gen "(Question is... Should I use it now, or save it for later?)" ("base", xpos="far_left", ypos="head")
            "-Use it now-":
                if game.daytime:
                    if not states.her.busy:
                        gen "Yes, there's no time like the present..." ("grin", xpos="far_left", ypos="head")
                        gen "I'll just grab a seat first." ("base", xpos="far_left", ypos="head")

                        call blkfade
                        call gen_chibi("sit_behind_desk")
                        call hide_blkfade

                        jump tentacle_scene_intro
                    else:
                        gen "(On second thought... She's probably busy right now.)" ("base", xpos="far_left", ypos="head")
                else:
                    gen "(It's a bit late... Miss Granger won't be having any classes right now...)" ("base", xpos="far_left", ypos="head")
            "-Save for later-":
                pass

        gen "(I'll just store this in my inventory for now...)" ("base", xpos="far_left", ypos="head")

        call blkfade
        call gen_chibi("sit_behind_desk")
        call hide_blkfade

        jump main_room_menu

label map_forest:
    if game.daytime:
        gen "I shouldn't be leaving the castle during the day. It's too risky..." ("base", xpos="far_left", ypos="head")
        jump desk

    call outskirts_of_hogwarts

    gen "Let's see what I can find out here..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Search the area-":
            $ ran = renpy.random.random()
            if ran < 0.3:
                nar "You search around the forest and manage to find an odd-looking herb."
                gen "This must be wormwood." ("base", xpos="far_left", ypos="head")
                menu:
                    "-Take the wormwood-":
                        nar "You gain 1 wormwood."
                        $ potion_inv.add("ing_wormwood")
                    "-Leave it-":
                        pass
                nar "Finding nothing else of interest, you return to your office."
                jump return_office
            elif ran < 0.6:
                nar "You search around the forest and manage to find an odd-looking herb."
                gen "This must be Knotgrass." ("base", xpos="far_left", ypos="head")
                menu:
                    "-Take the Knotgrass-":
                        nar "You gain 1 Knotgrass."
                        $ potion_inv.add("ing_knotgrass")
                    "-Leave it-":
                        pass
                nar "Finding nothing else of interest, you return to your office."
                jump return_office
            else:
                nar "You search around the forest but find nothing of interest."
                jump return_office


label map_lake:
    if game.daytime:
        gen "I shouldn't be leaving the castle during the day. It's too risky..." ("base", xpos="far_left", ypos="head")
        jump desk

    call outskirts_of_hogwarts

    gen "Let's see what I can find out here..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Search the area-":
            $ ran = renpy.random.random()
            if ran < 0.3:
                nar "You search around the lake and manage to find an slender, green vine."
                gen "This must be Niffler's fancy." ("base", xpos="far_left", ypos="head")
                menu:
                    "-Take the Niffler's fancy-":
                        nar "You gain 1 Niffler's fancy."
                        $ potion_inv.add("ing_niffler_fancy")
                    "-Leave it-":
                        pass
                nar "Finding nothing else of interest, you return to your office."
                jump return_office
            elif ran < 0.6:
                nar "You search around the lake and manage to find an exposed root that looks similar to ginger."
                gen "This must be Root of Aconite." ("base", xpos="far_left", ypos="head")
                menu:
                    "-Take the Root of Aconite-":
                        nar "You gain 1 Root of Aconite."
                        $ potion_inv.add("ing_aconite_root")
                    "-Leave it-":
                        pass
                nar "Finding nothing else of interest, you return to your office."
                jump return_office
            else:
                nar "You search around the lake but find nothing of interest."
                jump return_office


label gryffindor_dormitories:
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Gryffindor's Dormitory{/color}{/size}"

    menu:
        "-Search the area-":#Cat Hair
            $ ran = renpy.random.random()
            if ran < 0.3:
                nar "You search around the dorms and manage to find a clump of bright orange fur."
                gen "This must belong to some sort of animal." ("base", xpos="far_left", ypos="head")
                menu:
                    "-Take the Fur-":
                        nar "You gain 1 Cat Fur."
                        $ potion_inv.add("ing_cat_hair")
                    "-Leave it-":
                        pass
                nar "Finding nothing else of interest you return to your office."
                jump return_office
            else:
                nar "You search around the dorms but find nothing of interest."
                jump return_office


label ravenclaw_dormitories:
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Ravenclaw's Dormitory{/color}{/size}"

    menu:
        "-Search the area-":#Luna's Hair
            $ ran = renpy.random.random()
            if ran < 0.3:
                nar "You search around the dorms and manage to find a comb with some hair in it."
                gen "This must be someone's hair." ("base", xpos="far_left", ypos="head")
                menu:
                    "-Take the hair-":
                        nar "You gain 1 Luna's Hair."
                        $ potion_inv.add("ing_luna_hair")
                    "-Leave it-":
                        pass
                nar "Finding nothing else of interest you return to your office."
                jump return_office
            else:
                nar "You search around the dorms but find nothing of interest."
                jump return_office

# Unreachable code
#
# label map_pitch:
#     if states.map.quidditch_pitch.unlocked:
#         hoo "Hello Professor Dumbledore, nice to see you out of your office today."
#         hoo "What brings you down to the Quidditch pitch today?"
#         gen "Quidditch, what sort of name is that?" ("base", xpos="far_left", ypos="head") #put in low talking tone
#         hoo "What was that?"
#         gen "Nothing, just commenting about the weather." ("base", xpos="far_left", ypos="head") #Maybe change this
#         hoo "Well I'm glad that you're here. I wanted to have words with you about a problem that I'm having at the moment."
#         gen "What's wrong?" ("base", xpos="far_left", ypos="head")
#         hoo "Attendance at quidditch matches has slowly been declining over the last couple of months."
#         hoo "Students just don't seem to want to turn up to watch their teams play. It's affecting team morale."
#         gen "And how would you like to fix this?" ("base", xpos="far_left", ypos="head")
#         hoo "Perhaps we could make attendance to the match mandatory."
#         gen "I don't think it would work. If I did that you would just end up with a lot of disgruntled students booing your own team." ("base", xpos="far_left", ypos="head")
#         gen "If poor attendance is affecting morale I would hate to think what that would do to the players." ("base", xpos="far_left", ypos="head")
#         hoo "Well then what do you suggest?"
#         gen "You need a way to attract and excite the crowd. To get the students here and to get them cheering." ("base", xpos="far_left", ypos="head")
#         gen "What you need is a cheerleading team." ("base", xpos="far_left", ypos="head")
#         hoo "A what?"
#         gen "A team of girls to dance and cheer for their team. To get their fellow students brimming with enthusiasm." ("base", xpos="far_left", ypos="head")
#         hoo "I'm not sure Sir, Hogwarts has always been a traditional school."
#         hoo "Something like this goes in the face of that legacy."
#         gen "Well if you feel that way then I think you might just have to accept the declining number of students watching the game." ("base", xpos="far_left", ypos="head")
#         hoo "Fine, but I'm not comfortable with a team of these \"\Cheerleaders\"\. At most I'd be comfortable with one girl dancing." #Maybe adjust this so that there is a team
#         gen "Well I think I have the perfect candidate. I'll send her over next practice session to try out." ("base", xpos="far_left", ypos="head")
#         hoo "Okay, just make sure she's wearing something appropriate."
#         jump return_office
#     else:
#         nar "You look around the open field but can't see any students or teachers."
#         gen "Mustn't be a practice day." ("base", xpos="far_left", ypos="head")
#         jump return_office

label outskirts_of_hogwarts:
    call blkfade
    call gen_chibi("stand","desk","base")
    call hide_blkfade

    call gen_walk(action="leave")
    call blkfade

    stop music fadeout 1.0

    centered "{size=+7}{color=#cbcbcb}Outskirts of Hogwarts{/color}{/size}"

    $ renpy.scene("screens")

    play music "sounds/night.ogg" fadein 1 fadeout 1 #NIGHT SOUNDS. if_changed

    show her_ball outskirts as cg
    pause.3
    call hide_blkfade
    pause.8
    play sound "sounds/steps_grass.ogg"
    show her_ball outskirts g1 as cg

    return

label return_office:
    call hide_characters
    show screen blkfade
    with d3

    pause.8

    jump main_room
