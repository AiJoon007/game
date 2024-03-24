
label cupboard:
    if game.day == 1:
        if not states.gen.ev.intro.cupboard_examined:
            $ states.gen.ev.intro.cupboard_examined = True
            $ cupboard_OBJ.idle = "cupboard_idle"
            call gen_chibi("stand","behind_desk","base", flip=False)
            with d5
            pause.2

            call bld
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
            gen "A cupboard..." ("base", xpos="far_left", ypos="head")
            gen "Maybe I should rummage through this one later..." ("base", xpos="far_left", ypos="head")
            call gen_chibi("sit_behind_desk")
        else:
            gen "Looks like any other cupboard, maybe a bit dustier." ("base", xpos="far_left", ypos="head")

        if states.gen.ev.intro.bird_examined and states.gen.ev.intro.desk_examined and states.gen.ev.intro.cupboard_examined and states.gen.ev.intro.door_examined and states.gen.ev.intro.fireplace_examined:
            jump genie_intro_E2
        else:
            jump main_room_menu

    if states.cupboard_rummaged:
        if game.daytime:
            nar "You have already searched the cupboard today."
        else:
            nar "You have already searched the cupboard tonight."
        jump main_room_menu

    $ states.cupboard_rummaged = True # Resets every day/night.
    $ states.cupboard_rummaged_times += 1  # Stat counter.

    $ cupboard_OBJ.idle = "cupboard_open"
    call gen_chibi("rummage", 160, 459, flip=False) # Note: Flip is inconsistent
    with d3
    show screen bld1
    with d3

    nar "You rummage through the cupboard for a while..."

    $ random_percent = renpy.random.randint(1, 100)

    # Dueling potion
    if game.day <= 3 and states.cupboard_rummaged_times in [1,2]:
        $ states.healing_potions += 1
        call give_reward("You found some sort of healing potion...","interface/icons/item_potion.webp")
        $ cupboard_OBJ.idle = "cupboard_idle"
        call gen_chibi("sit_behind_desk")
        jump main_room_menu

    # Dumbledore card
    if game.day >= 26 and states.cardgame.unlocked and random_percent <= 40 and not card_exist(unlocked_cards,card_dumbledore) :
        call give_reward("You have found a special card!", "images/cardgame/t1/special/dumbledore_v1.webp")
        $ unlocked_cards += [card_dumbledore]
        $ cupboard_OBJ.idle = "cupboard_idle"
        call gen_chibi("sit_behind_desk")
        jump main_room_menu

    # Map
    if not states.map.unlocked and states.her.favors_unlocked:
        $ states.map.unlocked = True
        call give_reward("You found a map of the school grounds.", "interface/icons/generic_scroll.webp")

        gen "What's this? A map?" ("base", xpos="far_left", ypos="head")
        $ cupboard_OBJ.idle = "cupboard_idle"
        call gen_chibi("sit_behind_desk")

        call tutorial("map")

        gen "Sweet! That will be useful." ("grin", xpos="far_left", ypos="head")
        jump main_room_menu

    # Randomly drop something
    call rum_block(drop_item_from_cupboard(random_percent))
    $ cupboard_OBJ.idle = "cupboard_idle"
    call gen_chibi("sit_behind_desk")
    jump main_room_menu

label rum_block(item):
    if isinstance(item, int):
        $ game.gold += item
        call give_reward("You found [item] gold...", "interface/icons/gold.webp")

    elif item == "nothing":
        nar "You found nothing of value..."

    else:
        $ item.owned += 1

        if item == wine_ITEM:
            call give_reward("You found a bottle of wine from professor Dumbledore's personal stash...", item)
        elif item == firewhisky_ITEM:
            call give_reward("You found a bottle of firewhisky from professor Dumbledore's personal stash...", item)
        else:
            call give_reward("You found [item.name]...", item)

        call tutorial("inventory")

    hide screen gift
    with d3

    return

init python:
    def drop_item_from_cupboard(random_percent):
        drop_list = [item for item in inventory.get_instances_of_type("gift") if item.unlocked]

        dr = max(states.cupboard_rummaged_times - game.day, 0) * 2 # Frequent rummaging penalty
        progress_factor = math.log(states.her.tier + states.cho.tier + states.ton.tier + states.lun.tier + game.day)

        if firewhisky_ITEM.unlocked and firewhisky_ITEM.owned < 1:
            return firewhisky_ITEM
        elif wine_ITEM.owned < 1:
            return wine_ITEM

        if game.difficulty == 1:
            # Easy
            # Soft diminishing returns, more rubber banding. Guaranteed item drop.
            if game.gold < int(170 * math.log(game.day)) and random_percent <= 56 - dr:
                return int(progress_factor * random_gold)
            else:
                filtered_list = [x for x in drop_list if x.owned <= 5]
                random_item = renpy.random.choice(filtered_list if filtered_list else drop_list)
                return random_item

        elif game.difficulty == 2:
            # Normal
            # Fair diminishing returns, soft rubber banding. High chance for item drop. (Recommended)
            if game.gold < int(120 * math.log(game.day)) and random_percent <= 38 - dr:
                return int(progress_factor * random_gold)
            else:
                filtered_list = [x for x in drop_list if x.owned <= 3]
                random_item = renpy.random.choice(filtered_list if filtered_list else drop_list)

                if int(120 * math.log(game.day)) / 3 < random_item.price:
                    chance = max(6 - (random_item.owned * 5), 1)
                elif game.gold > random_item.price:
                    chance = max(65 - (random_item.owned * 15), 5)
                else:
                    chance = max(95 - (random_item.owned * 10), 15)

                if random_percent <= chance - dr:
                    return random_item
                else:
                    return "nothing"

        elif game.difficulty == 3:
            # Hard
            # Harsh diminishing returns, no rubber banding. Chance for item drop.
            if game.gold < int(90 * math.log(game.day)) and random_percent <= 33 - dr:
                return int(progress_factor * random_gold)
            else:
                random_item = renpy.random.choice(drop_list)

                if int(90 * math.log(game.day)) / 3 < random_item.price:
                    chance = max(3 - (random_item.owned * 5), 1)
                elif game.gold > random_item.price:
                    chance = max(40 - (random_item.owned * 15), 0)
                else:
                    chance = max(75 - (random_item.owned * 10), 5)

                if random_percent <= chance - dr:
                    return random_item
                else:
                    return "nothing"
