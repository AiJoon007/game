#
# History screen
#
# This is a screen that displays the dialogue history to the player. While
# there isn't anything special about this screen, it does have to access the
# dialogue history stored in _history_list.
#
# https://www.renpy.org/doc/html/history.html

init offset = -1

screen history():

    tag menu

    # Avoid predicting this screen, as it can be very large
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix gui.theme("history")

        has vbox
        spacing 12

        default last_who = ""

        for entry in _history_list:
            vbox:
                xfill True
                spacing 12

                if not last_who == entry.who:
                    hbox:
                        spacing 12

                        if "icon" in entry.show_args:
                            $ icon = entry.show_args["icon"]
                            add Fixed(gui.format("interface/achievements/{}/iconbox.webp"), Transform("interface/icons/head/{}.webp".format(icon), xzoom=-1, size=(40, 40), align=(0.5, 0.5)), fit_first=True)

                        if entry.who:
                            text entry.who:
                                style "history_name"
                                substitute False

                                if "color" in entry.who_args:
                                    color entry.who_args["color"]

                vbox:
                    spacing 6
                    $ what = renpy.filter_text_tags(entry.what, allow=gui.history_allow_tags)

                    text what:
                        substitute False

            $ last_who = entry.who

        if not _history_list:
            label _("The dialogue history is empty.")


# Tags that are allowed to be displayed on the history screen
define gui.history_allow_tags = ("number", "heart", "unicode")

# Height of a history screen entry, or None for variable height at the cost of performance
define gui.history_height = None #117

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text:
    color "#402313"

style history_window is empty:
    xfill True
    ysize gui.history_height
    padding (0,6)

style history_name:
    align (0.1, 0.5)
    size 22

style history_name_text:
    text_align 1.0

style history_text:
    text_align 0.0

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
