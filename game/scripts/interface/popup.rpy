transform popup_animation(time=4.0, xx=-200):
    on start:
        xoffset xx
    on show:
        xoffset xx
        linear 0.5 xoffset absolute(0)
        pause time
        linear 0.5 xoffset absolute(xx)

screen popup_window(msg="", xpos=0, ypos=60):
    tag popup_window
    zorder 100

    style_prefix gui.theme()

    timer 5.0 action Hide("popup_window")
    frame:
        at popup_animation
        pos (xpos, ypos)

        text msg align (0.5, 0.5) size 12

label give_reward(text="You found something!", gift="interface/icons/box_blue_2.webp", sound=True):
    if sound:
        play sound "sounds/win2.ogg"

    show screen gift(gift)
    show screen notes
    with d3

    # It has to be a renpy.say function in order to evaluate text tags i.e "You found [item.name]".
    $ renpy.say(None, text)

    hide screen gift
    hide screen notes
    with d3

    return

label modal_popup(title, entry, img=None, confirm="Ok"):
    $ disable_game_menu()
    play sound "sounds/pop01.ogg"
    call screen modal_popup(title, entry, img, confirm)
    $ enable_game_menu()
    return

screen modal_popup(title, entry, img, confirm):
    modal True

    add "gui_fade"

    frame:
        style_prefix gui.theme()
        xsize 518
        align (0.5, 0.5)
        padding (12 + 6, 6, 12 + 6, 12 + 6)

        vbox:
            spacing 12
            first_spacing 0

            fixed:
                ysize 24
                add gui.format("interface/achievements/{}/highlight.webp") xalign 0.5
                add gui.format("interface/achievements/{}/spacer.webp") align (0.5, 1.0)
                text title size 16 xalign 0.5 yalign 0.5

            if img and renpy.loadable(img):
                add img xalign 0.5

            text entry size 12

            textbutton confirm align (1.0, 1.0) action Return(True)
