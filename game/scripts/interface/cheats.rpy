
default cheat_wardrobe_alpha = False

default skip_duel = False
default experimental_cheats = False

label cheats:

    if not renpy.seen_label("cheats"):
        "Uncle Good Advice" "{b}Attention!{/b}\nSome cheats can cause bugs and writing inconsistencies, use at your own risk."

    menu:
        "-Inventory-":
            label .general:

            menu:
                "-Add 500 Gold-" (icon="interface/icons/small/gold.webp"):
                    $ game.gold += 500
                    jump cheats.general
                "-Get all gifts-" (icon="interface/icons/small/gift.webp"):
                    python:
                        for i in inventory.get_instances_of_type("gift"):
                            i.owned = i.limit
                    nar "Added 100 of each gift item to the inventory."
                "-Get all potions-" (icon="interface/icons/small/potion.webp"):
                    python:
                        for i in inventory.get_instances_of_type("potion"):
                            i.owned = i.limit
                    nar "Added 100 of each potion item to the inventory."
                "-Get all ingredients-" (icon="interface/icons/small/potion.webp"):
                    python:
                        for i in inventory.get_instances_of_type("ingredient"):
                            i.owned = i.limit
                    nar "Added 100 of each ingredient item to the inventory."
                "-Get all scrolls-" (icon="interface/icons/small/spell.webp"):
                    python:
                        for i in inventory.get_instances_of_type("scroll"):
                            i.owned = i.limit
                    nar "Added all scrolls to the inventory."
                "-Get all books-" (icon="interface/icons/small/book.webp"):
                    python:
                        for i in inventory.get_instances_of_type("book"):
                            i.owned = i.limit
                    nar "Added all books to the inventory."
                "-Get all decorations-" (icon="interface/icons/small/gold.webp"):
                    python:
                        for i in inventory.get_instances_of_type("decoration"):
                            i.owned = i.limit
                    nar "Added all decorations to the inventory."
                "-Get all quest items-" (icon="interface/icons/small/potion.webp"):
                    menu:
                        "Uncle Good Advice" "{color=#ff8000}Attention!{/color} You may receive items that are not intended to be used in your time line, or may be experimental. Do you still wish to proceed?"

                        "-Yes-":
                            pass
                        "-No-":
                            jump cheats.general
                    python:
                        for i in inventory.get_instances_of_type("quest"):
                            i.owned = i.limit

                    nar "Added all quest items to the inventory."
                "-Get all outfits-" (icon="interface/icons/small/wardrobe.webp"):
                    menu:
                        "Uncle Good Advice" "{color=#ff8000}Attention!{/color} You may receive outfits that are not intended to be used in your time line, may be experimental, or are duplicates of the already existing outfits. Do you still wish to proceed?"

                        "-Yes-":
                            pass
                        "-No-":
                            jump cheats.general

                    python:
                        for i in states.dolls:
                            for x in getattr(renpy.store, i).outfits:
                                if not x.hidden:
                                    x.unlock()

                    # Add relevant quest items to the inventory
                    $ poker_outfit_ITEM.owned = 1
                    $ ball_outfit_ITEM.owned = 1
                    $ maid_outfit_ITEM.owned = 1

                    nar "Added all outfits to the wardrobe."
                "-Back-":
                    jump cheats
            jump cheats.general

        "-Characters-":
            label .characters:

            menu:
                "-Tonks-" (icon="interface/icons/small/tonks.webp") if states.ton.unlocked:
                    label .tonks:
                    menu:
                        "-Reset mood- ([states.ton.mood])" if states.ton.mood != 0:
                            $ states.ton.mood = 0
                            nar "Tonks is no longer mad at you."
                        "-Increase Friendship- ([states.ton.level])" if states.ton.level < 100:
                            $ states.ton.level += 5
                            nar "Tonks likes you more..."
                        "-Decrease Friendship- ([states.ton.level])" if states.ton.level > 0:
                            $ states.ton.level -= 5
                            nar "Tonks likes you less..."
                        "-Back-":
                            jump cheats.characters
                    jump cheats.tonks

                "-Hermione-" (icon="interface/icons/small/hermione.webp") if states.her.unlocked:
                    label .hermione:
                    menu:
                        "-Reset mood- ([states.her.mood])" if states.her.mood != 0:
                            $ states.her.mood = 0
                            nar "Hermione is no longer mad at you."
                        "-Increase Whoring- ([states.her.level])" (icon="interface/icons/small/heart_red.webp") if states.her.level < 24:
                            $ states.her.level += 1
                            nar "Hermione became more depraved..."
                        "-Decrease Whoring- ([states.her.level])" (icon="interface/icons/small/heart_black.webp") if states.her.level > 0:
                            $ states.her.level += -1
                            nar "Hermione recovered some of her dignity."
                        "-Increase Reputation- ([states.her.public_level])" (icon="interface/icons/small/star_yellow.webp") if states.her.public_level < 24:
                            $ states.her.public_level += 1
                            nar "Hermione became more depraved..."
                        "-Decrease Reputation- ([states.her.public_level])" (icon="interface/icons/small/star_empty.webp") if states.her.public_level > 0:
                            $ states.her.public_level += -1
                            nar "Hermione recovered some of her dignity."
                        "-Back-":
                            jump cheats.characters
                    jump cheats.hermione

                "-Cho-" (icon="interface/icons/small/cho.webp") if states.cho.unlocked:
                    label .cho:
                    menu:
                        "-Reset mood- ([states.cho.mood])" if states.cho.mood != 0:
                            $ states.cho.mood = 0
                            nar "Cho is no longer mad at you."
                        "-Increase Whoring- ([states.cho.level])" (icon="interface/icons/small/heart_red.webp") if states.cho.level < 24:
                            $ states.cho.level += 1
                            nar "Cho became more depraved..."
                        "-Decrease Whoring- ([states.cho.level])" (icon="interface/icons/small/heart_black.webp") if states.cho.level > 0:
                            $ states.cho.level += -1
                            nar "Cho recovered some of her dignity."
                        "-Increase Reputation- ([states.cho.public_level])" (icon="interface/icons/small/star_yellow.webp") if states.cho.public_level < 24:
                            $ states.cho.public_level += 1
                            nar "Cho became more depraved..."
                        "-Decrease Reputation- ([states.cho.public_level])" (icon="interface/icons/small/star_empty.webp") if states.cho.public_level > 0:
                            $ states.cho.public_level += -1
                            nar "Cho recovered some of her dignity."
                        "-Back-":
                            jump cheats.characters
                    jump cheats.cho

                "-Luna-" (icon="interface/icons/small/luna.webp") if states.lun.unlocked:
                    label .luna:
                    menu:
                        "-Reset mood- ([states.cho.mood])" if states.lun.mood != 0:
                            $ states.lun.mood = 0
                            nar "Luna is no longer mad at you."
                        "-Increase Whoring- ([states.lun.level])" (icon="interface/icons/small/heart_red.webp") if states.lun.level < 24:
                            $ states.lun.level += 1
                            nar "Luna became more depraved..."
                        "-Decrease Whoring- ([states.lun.level])" (icon="interface/icons/small/heart_black.webp") if states.lun.level > 0:
                            $ states.lun.level += -1
                            nar "Luna recovered some of her dignity."
                        # "-Increase Reputation- ([lun_reputation])" (icon="interface/icons/small/star_yellow.webp") if lun_reputation < 24:
                        #     $ lun_reputation += 1
                        #     nar "Luna became more depraved..."
                        # "-Decrease Reputation- ([lun_reputation])" (icon="interface/icons/small/star_empty.webp") if lun_reputation > 0:
                        #     $ lun_reputation += -1
                        #     nar "Luna recovered some of her dignity."
                        "-Back-":
                            jump cheats.characters
                    jump cheats.luna

                "-Astoria-" (icon="interface/icons/small/astoria.webp") if states.ast.unlocked:
                    label .astoria:
                    menu:
                        "-Reset mood-" if states.ast.mood != 0:
                            $ states.ast.mood = 0
                            nar "Astoria is no longer mad at you."
                        "-Increase Whoring-" (icon="interface/icons/small/heart_red.webp") if states.ast.level < 24:
                            $ states.ast.level += 1
                            nar "Astoria likes you more..."
                        "-Decrease Whoring-" (icon="interface/icons/small/heart_black.webp") if states.ast.level > 0:
                            $ states.ast.level += -1
                            "Astoria likes you less..."
                        # "-Increase Reputation- ([states.ast.public_level])" (icon="interface/icons/small/star_yellow.webp") if states.ast.public_level < 24:
                        #     $ states.ast.public_level += 1
                        #     nar "Astoria became more depraved..."
                        # "-Decrease Reputation- ([states.ast.public_level])" (icon="interface/icons/small/star_empty.webp") if states.ast.public_level > 0:
                        #     $ states.ast.public_level += -1
                        #     nar "Astoria recovered some of her dignity"
                        "-Back-":
                            jump cheats.characters
                    jump cheats.astoria

                "-Susan-" (icon="interface/icons/small/huff.webp") if states.sus.unlocked:
                    label .susan:
                    menu:
                        "-Reset mood- ([states.cho.mood])" if states.sus.mood != 0:
                            $ states.sus.mood = 0
                            nar "Susan is no longer mad at you."
                        "-Increase Whoring- ([states.sus.level])" (icon="interface/icons/small/heart_red.webp") if states.sus.level < 24:
                            $ states.sus.level += 1
                            nar "Susan became more depraved..."
                        "-Decrease Whoring- ([states.sus.level])" (icon="interface/icons/small/heart_black.webp") if states.sus.level > 0:
                            $ states.sus.level += -1
                            nar "Susan recovered some of her dignity."
                        # "-Increase Reputation- ([sus_reputation])" (icon="interface/icons/small/star_yellow.webp") if sus_reputation < 24:
                        #     $ sus_reputation += 1
                        #     nar "Susan became more depraved..."
                        # "-Decrease Reputation- ([sus_reputation])" (icon="interface/icons/small/star_empty.webp") if sus_reputation > 0:
                        #     $ sus_reputation += -1
                        #     nar "Susan recovered some of her dignity."
                        "-Back-":
                            jump cheats.characters
                    jump cheats.susan

                "-Back-":
                    jump cheats

        "-House Points-":
            label .points:

            menu:
                "-Add 200 Slytherin Points-" (icon="interface/icons/small/slyt.webp"):
                    $ slytherin = clamp(slytherin+200, 1, 999999)
                    call update_ui_points
                    nar "Added 200 points to Slytherin!"
                "-Remove 200 Slytherin Points-" (icon="interface/icons/small/slyt.webp"):
                    $ slytherin = clamp(slytherin-200, 1, 999999)
                    call update_ui_points
                    nar "Removed 200 points from Slytherin!"
                "-Add 200 Gryffindor Points-" (icon="interface/icons/small/gryf.webp"):
                    $ gryffindor = clamp(gryffindor+200, 1, 999999)
                    call update_ui_points
                    nar "Added 200 points to Gryffindor!"
                "-Remove 200 Gryffindor Points-" (icon="interface/icons/small/gryf.webp"):
                    $ gryffindor = clamp(gryffindor-200, 1, 999999)
                    call update_ui_points
                    nar "Removed 200 points from Gryffindor!"
                "-Add 200 Ravenclaw Points-" (icon="interface/icons/small/rave.webp"):
                    $ ravenclaw = clamp(ravenclaw+200, 1, 999999)
                    call update_ui_points
                    nar "Added 200 points to Ravenclaw!"
                "-Remove 200 Ravenclaw Points-" (icon="interface/icons/small/rave.webp"):
                    $ ravenclaw = clamp(ravenclaw-200, 1, 999999)
                    call update_ui_points
                    nar "Removed 200 points from Ravenclaw!"
                "-Add 200 Hufflepuff Points-" (icon="interface/icons/small/huff.webp"):
                    $ hufflepuff = clamp(hufflepuff+200, 1, 999999)
                    call update_ui_points
                    nar "Added 200 points to Hufflepuff!"
                "-Remove 200 Hufflepuff Points-" (icon="interface/icons/small/huff.webp"):
                    $ hufflepuff = clamp(hufflepuff-200, 1, 999999)
                    call update_ui_points
                    nar "Removed 200 points from Hufflepuff!"
                "-Reset all points-":
                    $ slytherin = 1
                    $ gryffindor = 1
                    $ ravenclaw = 1
                    $ hufflepuff = 1
                    call update_ui_points
                    nar "House points reset!"
                "-Back-":
                    jump cheats
            jump cheats.points

        "-Progression-":
            label .progression:

            menu:
                "-Unlock all Mirror Stories-":
                    python:
                        for i in mirror.items:
                            i.unlocked = True
                    nar "Unlocked all mirror stories."

                # "-Hermione-":
                #     jump cheats.progression

                # "-Cho-" if states.her.tier >= 2:
                #     jump cheats.progression

                "-Back-":
                    jump cheats
            jump cheats.progression

        "-Experimental-":
            label .experimental:

            if not config.developer and not experimental_cheats:
                "Uncle Good Advice" "{color=#7a0000}Warning!{/color} These cheats are highly experimental and are not supposed to be used during a normal playthrough, there's a high chance they {u}will break the game{/u}, but you're the boss."

                menu:
                    "Uncle Good Advice" "Will you take full responsibility for your actions?\n(You will receive no technical support if you encounter any issues)"

                    "-Yes-":
                        $ experimental_cheats = True
                        nar "Experimental cheats have been unlocked."
                    "-No-":
                        "Uncle Good Advice" "Smart choice."
                        jump cheats

            menu:
                "-Genie Outfits-":
                    label .genie:
                    menu:
                        "-Use Default Outfit-":
                            show genie robes
                            hide genie
                            with None

                            gen robes "Swag." ("grin", xpos="far_left", ypos="head")
                        "-Use Santa Outfit-":
                            show genie santa
                            hide genie
                            with None

                            gen santa "Cool." ("grin", xpos="far_left", ypos="head")
                            nar "Disclaimer: Outfits will not be displayed during CG scenes and for chibi animations."
                        "-Back-":
                            jump cheats.characters
                    jump cheats.genie
                "{size=-4}-Wardrobe Transparency Slider- (Is enabled: [cheat_wardrobe_alpha]){/size}" (icon="interface/icons/small/wardrobe.webp"):
                    $ cheat_wardrobe_alpha = not cheat_wardrobe_alpha

                "-Unequip all clothes-":
                    python:
                        for i in states.dolls:
                            getattr(renpy.store, i).unequip("clothes")

                    nar "All characters are now naked."

                "-Unlock all characters-" (icon="interface/icons/small/talk.webp"):
                    $ states.sna.unlocked = True
                    $ states.ton.unlocked = True
                    $ states.her.unlocked = True
                    $ states.cho.unlocked = True
                    $ states.ast.unlocked = True
                    $ states.sus.unlocked = True
                    $ states.lun.unlocked = True
                    # ginny_unlocked = True
                    # voldermort_unlocked = True
                    # hagrid_unlocked = True

                    nar "All characters have been unlocked."

                "-Unlock all wardrobes-" (icon="interface/icons/small/wardrobe.webp"):
                    $ states.ton.wardrobe_unlocked = True
                    $ states.her.wardrobe_unlocked = True
                    $ states.cho.wardrobe_unlocked = True
                    $ states.ast.wardrobe_unlocked = True
                    $ states.sus.wardrobe_unlocked = True
                    $ states.lun.wardrobe_unlocked = True
                    # ginny_wardrobe_unlocked = True
                    # voldemort_wardrobe_unlocked = True
                    # hagrid_wardrobe_unlocked = True

                    nar "All wardrobes have been unlocked."

                "-Permanent body alteration-":
                    label .alteration:

                    # Note: itertools.cycle breaks Ren'py so we have to rely on a good 'ol if statement
                    # *Sigh* I wish we had match statement in python 2 :(
                    #
                    # Years later: Python 3 switch cases are finally here, but are not usable in renpy. :(

                    default _curr_breast_type = 0
                    default _curr_ass_type = 0

                    menu:
                        "Hermione Breasts ([_curr_breast_type])" (icon="interface/icons/small/hermione.webp"):
                            python:
                                if _curr_breast_type == 0:
                                        hermione.equip(her_chest_breasts1)
                                        _curr_breast_type = 1
                                elif _curr_breast_type == 1:
                                        hermione.equip(her_chest_breasts2)
                                        _curr_breast_type = 2
                                elif _curr_breast_type == 2:
                                        hermione.equip(her_chest_breasts3)
                                        _curr_breast_type = 3
                                elif _curr_breast_type == 3:
                                        hermione.unequip("chest")
                                        _curr_breast_type = 0

                            jump cheats.alteration

                        "Hermione Ass ([_curr_ass_type])" (icon="interface/icons/small/hermione.webp"):
                            python:
                                if _curr_ass_type == 0:
                                        hermione.equip(her_hips_ass1)
                                        _curr_ass_type = 1
                                elif _curr_ass_type == 1:
                                        hermione.equip(her_hips_ass2)
                                        _curr_ass_type = 2
                                elif _curr_ass_type == 2:
                                        hermione.equip(her_hips_ass3)
                                        _curr_ass_type = 3
                                elif _curr_ass_type == 3:
                                        hermione.unequip("hips")
                                        _curr_ass_type = 0

                            jump cheats.alteration

                        "-Back-":
                            jump cheats.experimental

                "-Back-":
                    jump cheats
            jump cheats.experimental

        "-Never mind-":
            jump main_room_menu


### Hermione ###

label .hermione_skip_intro:

    $ states.gen.ev.intro.bird_examined = True
    $ states.gen.ev.intro.desk_examined = True
    $ states.gen.ev.intro.cupboard_examined = True
    $ states.gen.ev.intro.door_examined = True
    $ states.gen.ev.intro.fireplace_examined = True

    $ wine_ITEM.owned = 5
    $ firewhisky_ITEM.owned = 5

    $ states.cupboard_rummaged_times = 6
    $ game.day = 13

    $ achievements.unlock("start", True)

    $ states.gen.ev.intro.e1_complete = True
    $ states.gen.ev.intro.e2_complete = True
    $ states.gen.ev.intro.e3_complete = True
    $ states.gen.ev.intro.e4_complete = True

    $ states.sna.ev.intro.e1_complete   = True
    $ states.sna.ev.intro.e2_complete   = True
    $ states.sna.ev.intro.e3_complete   = True
    $ states.sna.ev.intro.duel_complete = True
    $ states.sna.ev.intro.e4_complete   = True
    $ states.sna.ev.intro.e5_complete   = True

    $ states.sna.ev.hangouts.hermione_e1 = True
    $ states.sna.ev.hangouts.hermione_e2 = True
    $ states.sna.ev.hangouts.tonks_e1 = True
    $ states.sna.ev.hangouts.tonks_e2 = True
    $ states.sna.ev.hangouts.tonks_e3 = True

    $ states.ton.ev.intro.e1_complete = True
    $ states.ton.ev.intro.e2_complete = True
    $ states.ton.ev.intro.e3_complete = True

    $ states.her.ev.intro.convinced = True

    $ states.her.ev.intro.e1_complete = True
    $ states.her.ev.intro.e2_complete = True
    $ states.her.ev.intro.e3_complete = True
    $ states.her.ev.intro.e4_complete = True
    $ states.her.ev.intro.e5_complete = True
    $ states.her.ev.intro.e6_complete = True

    $ letter_hg_1.open(silent=True)
    $ letter_hg_2.open(silent=True)
    $ letter_work_unlock.open(silent=True)
    $ letter_favors.open(silent=True)

    $ states.sna.unlocked = True
    $ achievements.unlock("unlocksna", True)

    $ states.ton.unlocked = True
    $ achievements.unlock("unlockton", True)

    $ states.her.unlocked = True
    $ achievements.unlock("unlockher", True)
    $ states.her.ev.tutoring.unlocked = True
    $ states.her.favors_unlocked = True
    $ states.her.wardrobe_unlocked = True
    $ states.paperwork_unlocked = True

    # Simulate points gains
    $ slytherin = gryffindor
    $ gryffindor = int(slytherin*0.5)
    $ hufflepuff = int(gryffindor*1.1)
    $ ravenclaw = int(gryffindor*1.3)

    return

# label .hermione_skip_T1:
#     $ states.her.tier = 2
#     $ states.her.level = 1
#     return

# label .hermione_skip_T2:
#     $ states.her.tier = 3
#     $ states.her.level = 9
#     $ states.her.status.voyer = True
#     return

# label .hermione_skip_T3:
#     $ states.her.tier = 4
#     $ states.her.level = 12
#     $ states.her.status.stripping = True
#     return

# label .hermione_skip_T4:
#     $ states.her.tier = 5
#     $ states.her.level = 18
#     $ states.her.status.kissing = True
#     return

# label .hermione_skip_T5:
#     $ states.her.tier = 6
#     $ states.her.level = 21
#     $ states.her.status.blowjob = True
#     return


# ### Cho ###

# label .cho_skip_intro:
#     if game.day < 16:
#         $ game.day = 16
#     $ states.cho.ev.intro.e1_complete = True
#     $ states.cho.ev.intro.e2_complete = True
#     $ states.sna.ev.hangouts.cho_e1 = True
#     $ states.cho.ev.intro.e4_complete = True
#     $ achievements.unlock("unlockcho", True)
#     $ states.cho.unlocked = True
#     return

# label .cho_skip_quiz:
#     $ states.cho.ev.quiz.complete = True
#     $ states.cho.ev.quidditch.e1_complete = True
#     $ states.cho.ev.quidditch.e2_complete = True
#     $ states.cho.ev.quidditch.position = "above"
#     $ states.cho.ev.quidditch.lock_training = False
#     $ states.cho.favors_unlocked = True
#     return
