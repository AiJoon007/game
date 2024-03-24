label enlarge_poster:
    show image "#00000080" as underlay
    show image Image(poster_OBJ.decoration.image) zorder 25 at truecenter as poster

    call ctc

    hide poster
    hide underlay
    with d3

    jump main_room_menu

# Xmas 2022 - Decoration

default naughty_list_commentary = False

label naughty_list:

    python:
        # This code retrieves user name and displays it on a leaderboard-like
        # list for funsies, the variable is discarded afterwards.
        _username = None
        _d = [(i, get_character_progression(i)) for i in states.dolls if get_character_unlock(i)]
        _d.append(["Snape", states.sna.level])

        try:
            _username = os.getenv("USERNAME")

            if not _username:
                _username = os.getlogin()

            # Windows returns an empty string when it encounters an error,
            # in ucrtbase.dll, and we need to catch that.
            if not _username:
                raise Exception("Cannot retrieve user name, using the fallback.")

            _username = _username.split(" ")[0].capitalize()
            _d.append([_username, 999])

        except:
            _d.append(["Genie", 999])

        _d.sort(key=lambda x: x[1], reverse=True)

    show screen naughty_list(_d)
    with d3

    if not naughty_list_commentary:
        $ naughty_list_commentary = True

        pause 1.0

        if _username is None:
            gen "I'm on the first place, nice!" ("base", xpos="far_left", ypos="head")
        else:
            gen "List checks out... But who the fuck is [_username]?" ("base", xpos="far_left", ypos="head")

    call ctc

    hide screen naughty_list
    with d3

    python:
        del _username

    jump main_room_menu

screen naughty_list(d):
    zorder 25

    add "#00000080"
    add "naughty_list scroll" fit "cover" at truecenter

    vbox:
        align (0.51, 0.66)
        spacing 2

        for i, (name, _) in enumerate(d, start=1):

            fixed:
                fit_first True
                add "naughty_list spacer" size (156, 21)
                text "[i]" pos (6, 3)
                text "[name]" xalign 0.5 yoffset 3
