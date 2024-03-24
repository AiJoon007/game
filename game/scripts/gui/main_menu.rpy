#
# Main/game menu screens
#

init offset = -1

# Main menu screen
#
# Used to display the main menu when Ren'Py starts.
#
# https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    # This empty frame darkens the main menu
    frame:
        pass

    vbox:
        spacing gui.navigation_spacing * 2
        yoffset gui.navigation_padding
        align (1.0, 0.0)
        xsize 300

        add "game_title" zoom 0.75 xalign 0.5

    if prerelease:
        text "TEST-ONLY" at transform:
            rotate 45

    vbox:
        spacing gui.navigation_spacing * 2
        yoffset -gui.navigation_padding
        align (1.0, 1.0)

        fixed:
            xysize (300, 75)

            imagebutton:
                idle Transform("discord_idle", alpha=0.5, zoom=0.5)
                hover Transform("discord_idle", alpha=0.75, zoom=0.55)
                focus_mask None
                pos (0.333, 0.5)
                anchor (0.5, 0.5)
                action OpenURL("https://discord.gg/UbQeTCJ5RW")
                tooltip "Discord"

            imagebutton:
                idle Transform("patreon_idle", alpha=0.5, zoom=0.5)
                hover Transform("patreon_idle", alpha=0.75, zoom=0.55)
                focus_mask None
                pos (0.666, 0.5)
                anchor (0.5, 0.5)
                action OpenURL("https://www.patreon.com/SilverStudioGames")
                tooltip "Patreon"

        fixed:
            xysize (300, 30)

            vbox:
                xoffset -100 - gui.navigation_padding
                yalign 0.5
                at transform:
                    alpha 0.6
                if prerelease:
                    text "Pre-release":
                        style "main_menu_version"

                text "[config.version]":
                    style "main_menu_version"

            imagebutton:
                idle Transform("silverstudiogames_idle", alpha=0.5, zoom=0.5)
                hover Transform("silverstudiogames_idle", alpha=0.75, zoom=0.55)
                focus_mask None
                align (0.5, 0.5)
                action OpenURL("https://www.silverstudiogames.org")

    use navigation

image main_menu_bg:
    alpha 0.5
    "#000"

style main_menu_frame is empty
style main_menu_vbox is vbox

style main_menu_frame:
    xalign 1.0
    xsize 300 # 234
    yfill True
    background "main_menu_bg"

style main_menu_text is gui_text:
    color gui.accent_color
    xalign 1.0

style main_menu_title is main_menu_text:
    size 42

style main_menu_version is main_menu_text:
    color "#fff"
    outlines [(1, "#000000", 1, 0)]


# Game menu screen
#
# This lays out the basic common structure of a game menu screen. It's called
# with the screen title, and displays the background, title, and navigation.
#
# The scroll parameter can be None, or one of "viewport" or "vpgrid". When
# this screen is intended to be used with one or more children, which are
# transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        if gui.theme() == "light":
            background "#00000040"
        else:
            background "#00000080"

        hbox:
            box_reverse True
            spacing 25

            # Reserve space for the navigation section
            frame:
                style "game_menu_navigation_frame"

            frame:
                # Content frame uses GUI theme
                style gui.theme("game_menu_content_frame")
                style_prefix gui.theme()

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        frame:
                            style "empty"
                            padding (15, 15, 15, 15)
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude

                else:
                    frame:
                        style "empty"
                        padding (15, 15, 15, 15)
                        transclude

    use navigation(title)

    label title anchor (0.5, 0.5) align (0.9, 0.15)

    if main_menu and not title == "Updater":
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty:
    padding (25, 100, 25, 25)
    xfill True
    yfill True

style game_menu_navigation_frame is empty:
    xsize 250
    yfill True

style game_menu_content_frame is empty:
    xsize 755

style dark_game_menu_content_frame is dark_gui_frame:
    take game_menu_content_frame

style light_game_menu_content_frame is light_gui_frame:
    take game_menu_content_frame

style game_menu_viewport is gui_viewport

style game_menu_scrollbar is gui_vscrollbar

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side is gui_side:
    spacing 9

style game_menu_label is gui_label:
    xpos 50
    ysize 100

style game_menu_label_text is gui_label_text:
    color gui.accent_color
    size 42
    yalign 0.5

# Navigation screen
#
# This screen is included in the main and game menus, and provides navigation
# to other menus, and to start the game.

screen navigation(title=None):

    default show_quick_start = False
    default show_dev_start = False
    default is_sensitive = not bool(title == "Updater")

    key "keydown_K_LSHIFT" action SetLocalVariable("show_quick_start", True)
    key "keyup_K_LSHIFT" action SetLocalVariable("show_quick_start", False)

    if config.developer:
        key "keydown_K_LCTRL" action SetLocalVariable("show_dev_start", True)
        key "keyup_K_LCTRL" action SetLocalVariable("show_dev_start", False)

    vbox:
        style_prefix "navigation"

        if main_menu:
            yalign 1.0
            yoffset -105 - gui.navigation_padding * 2
        else:
            yalign 0.5

        transclude

        null height 28 # Half button height

        if main_menu:
            if not title:

                if not renpy.mobile:
                    if version_float(UPDATE_VER) > version_float():
                        textbutton "Install updates" action InstallUpdates() style_prefix "update_available" sensitive (not prerelease)
                    else:
                        textbutton "Check for updates" action CheckUpdates(300) sensitive (not prerelease)
                    text "[UPDATE_HINT]" size 8 color "#fff" xalign 0.5

                if show_quick_start:
                    textbutton _("Quick Start") action Start("start_quick") sensitive is_sensitive
                elif show_dev_start:
                    textbutton _("Developer Start") action Start("start_dev") sensitive is_sensitive keysym "ctrl_mousedown_1"
                else:
                    textbutton _("Start") action Start() sensitive is_sensitive
            else:
                textbutton _("Return") action Return() sensitive is_sensitive

        else:
            textbutton _("Return") action Return() sensitive is_sensitive
            textbutton _("History") action ShowMenu("history") sensitive is_sensitive
            textbutton _("Save") action ShowMenu("save") sensitive is_sensitive

        textbutton _("Load") action ShowMenu("load") sensitive is_sensitive
        textbutton _("Preferences") action ShowMenu("preferences") sensitive is_sensitive

        if main_menu:
            textbutton _("Mods") sensitive (bool(mods_list) and is_sensitive) action ShowMenu("mods")
            textbutton _("Credits") action Jump("credits") sensitive is_sensitive
            if not renpy.mobile:
                textbutton _("Quit") action Quit(confirm=not main_menu) sensitive is_sensitive
        else:
            textbutton _("Help") action ShowMenu("help") sensitive is_sensitive
            textbutton _("Quit to menu") action MainMenu() sensitive is_sensitive

style navigation_vbox:
    xsize 250
    spacing gui.navigation_spacing
    xoffset -150
    xpos 1.0
    xanchor 0.5

style navigation_button is gui_button:
    # size_group "navigation"
    background None
    xalign 0.5

style navigation_button_text is gui_button_text:
    background None
    size 19
    xalign 0.5
    idle_color Color('#888')
    hover_color '#fff'
    selected_color '#fff'
    insensitive_color Color('#888', alpha=0.5)
