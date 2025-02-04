#
# Narration screens
#

init offset = -1

screen nvl(dialogue, items=None):
    null

# Say screen
#
# The say screen is used to display dialogue to the player. It takes two
# parameters, who and what, which are the name of the speaking character and
# the text to be displayed, respectively. (The who parameter can be None if no
# name is given.)
#
# This screen must create a text displayable with id "what", as Ren'Py uses
# this to manage text display. It can also create displayables with id "who"
# and id "window" to apply style properties.
#
# https://www.renpy.org/doc/html/screen_special.html#say

init python:
    import re
    def text_inner_thought(string, pattern=re.compile(r"\(([^)]+)\)")):
        return re.findall(pattern, string)

screen say(who, what, side_image=None, icon=None):
    zorder 31

    if _windows_hidden:
        use invisible_button(action=SetVariable("_windows_hidden", False))
    else:
        if not renpy.get_screen("choice"):
            use invisible_button(action=Function(ui.saybehavior), keysym="dismiss")

    # TODO: While this works, there might be a better way to add effects based on contents of the dialogue.

    if text_inner_thought(what) and not renpy.showing("cg"):
        add "fade_gradient"

    if side_image:
        add side_image yalign 1.0 yanchor 1.0 zoom 0.5
    else:
        add SideImage()

    window id "window":
        style gui.theme("say_window")

        if _windows_hidden:
            ypos 1000

        if _game_menu_screen:
            use quick_menu

        if who:
            window:
                id "namebox"
                style gui.theme("namebox")
                text who:
                    style gui.theme("say_label")

        text what:
            id "what"
            style gui.theme("say_dialogue")

    if renpy.android:
        button:
            style "empty"

            xysize (235, 100)
            align (0.0, 1.0)
            action Rollback()

            insensitive_child Transform(gui.format("interface/frames/{}/arrow.webp"), xalign=1.0, alpha=0.5)
            add Transform(gui.format("interface/frames/{}/arrow.webp"), xalign=1.0)

        button:
            style "empty"

            xysize (235, 100)
            align (1.0, 1.0)
            action Skip(fast=True, confirm=True)

            add Transform(gui.format("interface/frames/{}/arrow.webp"), xzoom=-1.0)

# Quick menu screen
#
# The quick menu is displayed in-game to provide easy access to the out-of-game menus.

screen quick_menu():
    hbox:
        style_prefix "quick"
        xalign 1.0
        yoffset -30

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Preferences") action ShowMenu("preferences")

style quick_button is default:
    activate_sound "sounds/click3.ogg"
    background None
    xpadding 8
    ypadding 8

style quick_button_text is default:
    size 10
    idle_color "#8888"
    hover_color "#ccc"
    selected_idle_color "#cc08"
    selected_hover_color "#cc0"
    insensitive_color "#4448"

# Choice screen
#
# This screen is used to display the in-game choices presented by the menu
# statement. The one parameter, items, is a list of objects, each with caption
# and action fields.
#
# https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    tag menu
    modal True
    zorder 30

    style_prefix gui.theme("menu")

    default blacklist_screens = {"say", "letter", "bld1"} # Combine sets
    default blacklist_tags = set(get_character_tag(x) for x in states.dolls)

    # Dont add the fade if character or saybox is present (They have their own triggers for fading)
    if not any(renpy.get_screen(x) for x in blacklist_screens) and not any(renpy.showing(x, layer="screens") for x in blacklist_tags):
        add "interface/bld.webp" at fade_hide(0.15)

    window at fade_show_hide(0.15):
        style "empty"
        align states.menu_pos

        vbox:
            spacing 0
            $ choice_width = int(config.screen_width/2)

            $ max_progress = max([len(e.kwargs.get("progress", [])) for e in items])

            for i, entry in enumerate(items, 1):
                $ style_part = entry.kwargs.get("style", None)
                button:
                    xsize choice_width
                    ypadding 5
                    action entry.action
                    sensitive bool(entry.action)
                    if i < 10 and entry.action:
                        keysym ("K_"+str(i), "K_KP"+str(i))

                    fixed:
                        style "empty"

                        if style_part:
                            style_prefix gui.theme("{}_menu".format(style_part))

                        fit_first "height"

                        text entry.caption:
                            xsize choice_width-120 # Leave enough margin for number and icon
                            align (0.5, 0.5)

                        if i < 10 and entry.action:
                            text "{size=-2}[i].{/size}" xpos 5 yalign 0.5

                        $ icon = entry.kwargs.get("icon", None)
                        if icon:
                            add icon xcenter 40 yalign 0.5

                        $ progress = entry.kwargs.get("progress", None)
                        if progress:
                            hbox:
                                spacing 2
                                xpos choice_width - 5
                                align (1.0, 0.5)
                                for i in range(0, max_progress):
                                    if i < len(progress):
                                        add progress[i]
                                    else:
                                        null width 21 # Assume icon width

style menu_text is default:
    hover_color "#fff"
    text_align 0.5
    outlines [(1, "#00000080", 1, 0)]

style dark_menu_text:
    color "#9b8d84"
    insensitive_color "#6c625c"

style light_menu_text:
    color "#f9d592"
    insensitive_color "#ae9566"

style dark_disabled_menu_text:
    color "#6c625c"

style light_disabled_menu_text:
    color "#ae9566"

style menu_button is default:
    activate_sound "sounds/click3.ogg"

style dark_menu_button:
    background "#5d5151e6"
    hover_background "#897e75"
    insensitive_background "#9e8449"

style light_menu_button:
    background "#ac8d5ae6"
    hover_background "#97681f"
    insensitive_background "#d1a02eb3"

# Input screen
#
# This screen is used to display renpy.input. The prompt parameter is used to
# pass a text prompt in.
#
# This screen must create an input displayable with id "input" to accept the
# various input parameters.
#
# https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    zorder 30

    style_prefix "say"
    window:
        id "window"
        style gui.theme("say_window")

        if prompt:
            window:
                style gui.theme("namebox")
                text prompt:
                    style gui.theme("say_label")

        input id "input":
            style gui.theme("say_dialogue")
