# Hide all character images (not chibi)
label hide_characters:
    hide hermione_main
    hide luna_main
    hide cho_main
    hide astoria_main
    hide susan_main
    hide tonks_main
    hide snape_main
    hide screen genie_main
    # Do not add transitions. Use one after return.
    return

# Reset menu
label reset_menu_position:

    $ states.menu_pos = (0.5, 0.6)

    return

label bld(action=None):
    if action == "hide":
        hide screen bld1
    else:
        show screen bld1
    with d3

    return

label blktone:
    show screen bld1 # blktone looks stupid without bld1
    show screen blktone
    with d5

    return

label hide_blktone:
    hide screen blktone
    with d5

    return

label blktone_top:
    show screen bld1 # blktone looks stupid without bld1
    show screen blktone # Has higher zorder than normal blktone
    with d5

    return

label hide_blktone_top:
    hide screen blktone
    with d5

    return

label blkfade:
    hide screen bld1
    hide screen blktone
    show screen blkfade
    with d5
    pause.2

    return

label hide_blkfade:
    hide screen blkfade
    with d5

    return

label ctc:
    show screen ctc
    with d3
    pause
    hide screen ctc
    with d1

    return

# Play day/night theme
label music_block:
    if states.room == "main_room":
        if game.daytime:
            play music "music/Brittle Rille.ogg" fadein 1 if_changed
        else:
            play music "music/Music for Manatees.ogg" fadein 1 if_changed
    elif states.room == "snape_office":
        play music "music/the-other-side-of-the-door-by-kevin-macleod-from-filmmusic-io.ogg" fadein 1 if_changed
    return

label unlock_clothing(text="", item="interface/icons/box_blue_1.webp"):

    $ states.menu_pos = (0.5, 0.75)

    show screen clothing_unlock(item)
    show screen blktone
    with d3

    menu:
        "[text]"
        "-Done Reading-":
            pass

    hide screen clothing_unlock
    hide screen blktone
    with d3

    $ item.unlock()

    call reset_menu_position

    return


label describe_mood(name, value):
    if 5 > value >= 1:
        nar "[name] is a little upset with you..."
    elif 10 > value >= 5:
        nar "[name] is upset with you."
    elif 20 > value >= 10:
        nar "[name] is very upset with you."
    elif 30 > value >= 20:
        nar "[name] is mad at you."
    elif 40 > value >= 30:
        nar "[name] is very mad at you."
    elif 50 > value >= 40:
        nar "[name] is furious at you."
    elif value >= 50:
        nar "[name] hates your guts."
    else:
        nar "[name] is calm."
    return


label describe_mood_after_gift(was_negative, mood, change):
    if was_negative and mood == 0:
        call notes
        "She's no longer upset with you."
    elif was_negative and change < 0:
        "But she's still upset with you."
    elif was_negative:
        "She's still upset with you."

    return


label notes():
    play sound "sounds/win_04.ogg"   #Not loud.
    hide screen notes
    show screen notes
    return

label not_implemented():
    "Not implemented."
    return

label end_of_content():
    $ renpy.choice_for_skipping()

    "SilverStudioGames" "This concludes story progression for this character as of version [config.version].\nThere still may be side events and activities that you have missed, but main story won't progress past this point."
    "SilverStudioGames" "We hope you have enjoyed yourself. Stay tuned for more in the future."
    call notes
    nar "All stats have been maxed out. You can now use all of the wardrobe options."

    return
