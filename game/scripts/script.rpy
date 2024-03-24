
label start:
    python:
        version = version_float()
        renpy.block_rollback()

    if prerelease:
        call modal_popup("Attention!", "This pre-release version of the game comes with some quirks and instability. Brace yourself for potential bugs, unexpected crashes, missing content, and oddities in gameplay. While we’ve done our best to iron out issues, be prepared for a less-than-smooth experience. \n\nHelp us improve by reporting any problems you encounter via Discord.\n\nProceed only if you acknowledge the above.", "interface/warning.webp")

    jump start_wt

label start_quick:
    python:
        version = version_float()
        game.difficulty = 2
        states.ton.level = 5
        states.sna.level = 5
        states.map.unlocked = True
        game.cheats = True

        renpy.block_rollback()

    if prerelease:
        call modal_popup("Attention!", "This pre-release version of the game comes with some quirks and instability. Brace yourself for potential bugs, unexpected crashes, missing content, and oddities in gameplay. While we’ve done our best to iron out issues, be prepared for a less-than-smooth experience. \n\nHelp us improve by reporting any problems you encounter via Discord.\n\nProceed only if you acknowledge the above.", "interface/warning.webp")

    jump skip_to_hermione

label start_dev:
    python:
        version = version_float()
        game.difficulty = 2
        game.cheats = True
        game.gold = 100000
        states.map.unlocked = True
        states.sna.unlocked = True
        states.ton.unlocked = True
        states.her.unlocked = True
        states.cho.unlocked = True
        states.ast.unlocked = True
        states.sus.unlocked = True
        states.lun.unlocked = True
        states.ton.wardrobe_unlocked = True
        states.her.wardrobe_unlocked = True
        states.cho.wardrobe_unlocked = True
        states.ast.wardrobe_unlocked = True
        states.sus.wardrobe_unlocked = True
        states.lun.wardrobe_unlocked = True
        states.her.level = states.cho.level = states.lun.level = states.ast.level = states.sus.level = 24
        states.sna.level = 100
        states.ton.level = 100

        states.her.ev.yule_ball.e1_complete = True
        states.her.ev.yule_ball.e2_complete = True
        states.her.ev.yule_ball.e3_complete = True
        states.her.ev.yule_ball.e4_complete = True

        states.map.room_of_requirement.intro_e1 = True
        states.map.seventh_floor.unlocked = True
        states.map.seventh_floor.visited = True
        seventh_door_OBJ.hidden = False

        states.map.snape_office.visited = True

        states.map.snape_office.station_examined = True
        states.map.snape_office.shelves_examined = True
        states.map.snape_office.picture_examined = True
        states.map.snape_office.statue_examined = True
        states.map.snape_office.desk_examined = True
        states.map.snape_office.candelabra_examined = True

        states.map.snape_office.intro_e1 = True
        states.map.snape_office.intro_e2 = True
        states.map.snape_office.intro_e2_stage = 2
        states.map.snape_office.intro_e3 = True

        states.cho.ev.intro.e1_complete = True
        states.cho.ev.intro.e2_complete = True
        states.cho.ev.intro.e4_complete = True
        states.sna.ev.hangouts.cho_e1 = True

        states.paperwork_unlocked = True

        store.states.lun.ev.intro.e1_complete = True
        store.states.lun.ev.intro.e2_complete = True

        for i in mirror.items:
            i.unlocked = True

        for i in inventory.items:
            i.owned = i.limit

        for i in states.dolls:
            for x in getattr(renpy.store, i).outfits:
                if not x.hidden:
                    x.unlock()

        renpy.block_rollback()

    jump skip_to_hermione
