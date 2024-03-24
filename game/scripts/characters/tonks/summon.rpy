
label summon_tonks:

    $ states.active_girl = "tonks"

    $ states.ton.busy = True

    call update_ton_tier
    call update_tonks

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    play sound "sounds/door.ogg"

    $ renpy.checkpoint(hard=True)

    # Clothes Events
    call tonks_summon_setup

    label tonks_requests:

    # Reset
    call reset_menu_position
    ton "" (xpos="base",ypos="base")

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if states.ton.mood > 0:
                ton "I have a headache right now, let's talk later."
                jump tonks_requests

            call tonks_chitchat
            jump tonks_talk


        # Favours
        "-Sexual favours-" (icon="interface/icons/small/condom.webp"):
            jump tonks_favor_menu

        # Fireplace Chats
        "-Let's hang-" (icon="interface/icons/small/toast.webp") if (wine_ITEM.owned > 0 and not states.ton.ev.hangouts.wine_intro) or firewhisky_ITEM.owned > 0:
            jump tonks_hangout

        "-Let's hang-" (icon="interface/icons/small/toast.webp", style="disabled") if (firewhisky_ITEM.owned < 1 and states.ton.ev.hangouts.wine_intro):
            gen "(I don't have any firewhisky...)" ("base", xpos="far_left", ypos="head")
            jump tonks_requests

        "-Let's hang-" (icon="interface/icons/small/toast.webp", style="disabled") if (wine_ITEM.owned < 1 and not states.ton.ev.hangouts.wine_intro):
            gen "(I don't have any wine...)" ("base", xpos="far_left", ypos="head")
            jump tonks_requests

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if states.ton.wardrobe_unlocked:
            hide tonks_main with d1
            call wardrobe

            # Hair fix
            $ tonks_haircolor = [c for c in tonks.get_equipped("hair").color]
            jump tonks_requests

        "-Wardrobe-" (style="disabled") if not states.ton.wardrobe_unlocked:
            nar "You haven't unlocked this feature yet."
            jump tonks_requests

        "-Give Item-" (icon="interface/icons/small/gift.webp"):
            hide tonks_main with d1
            call gift_menu
            jump tonks_requests

        # Dismiss
        "-Never mind-":
            stop music fadeout 3.0

            if game.daytime:
                ton "Alright, back to work then..."
            else:
                ton "Sweet dreams, [name_genie_tonks]."

            play sound "sounds/door.ogg"

            jump end_tonks_event


# Tonks level up
label update_ton_tier:
    if states.ton.tier == 1 and states.ton.ev.hangouts.favors_e2:
        $ ton_level_up = 1

    return

label tonks_level_up(tier=None):

    call bld
    if tier == 1:
        gen "(Time to teach those students something useful!)" ("grin", xpos="far_left", ypos="head")

    $ states.ton.tier = tier+1
    $ ton_level_up = None

    pause.5
    nar "Tonks has reached level [states.ton.tier]!"

    call update_ton_tier

    return


# Tonks Requests Menu
label tonks_favor_menu:
    # call update_tonks_favors

    menu:
        "-Level Up-" (icon="interface/icons/small/levelup.webp") if ton_level_up != None:
            call tonks_level_up(tier=ton_level_up)
            jump tonks_requests

        "-Personal Favours-" (icon="interface/icons/small/heart_red.webp", style="disabled"):
            label .favors:

            call not_available
            jump tonks_favor_menu

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp") if game.daytime and states.ton.requests_unlocked:
            label .requests:

            $ result = show_events_menu(tonks_requests)

            if result in ("disabled", "noncompliant"):
                "You haven't unlocked this request opportunity yet."
                jump .requests
            elif result == "exit":
                jump tonks_favor_menu
            else:
                $ result.start()

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled") if not game.daytime or not states.ton.requests_unlocked:
            if not states.ton.requests_unlocked:
                nar "You haven't unlocked this feature yet."
            elif not game.daytime:
                nar "Public requests are available during the day only."

            jump tonks_favor_menu

        "-Never mind-":
            jump tonks_requests
