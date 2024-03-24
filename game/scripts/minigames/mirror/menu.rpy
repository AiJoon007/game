init python:
    def mirror_sortfilter(item, sortby="A-z", filtering=None):
        if filtering == "Locked":
            item = [x for x in item if x.is_unlocked()]
        elif filtering == "Unlocked":
            item = [x for x in item if x.is_unlocked() is True]

        # Always sort alphabetically first.
        item = sorted(item, key=lambda x: natsort_key(x.name))

        if sortby == "z-A":
            item = sorted(item, key=lambda x: natsort_key(x.name), reverse=True)

        return item

label mirror:
    $ gui.in_context("mirror_menu")
    call screen room_menu

label mirror_menu(xx=150, yy=90):

    python:
        mirror_categories = mirror.get_tags()

        items_shown = 36
        current_page = 0
        current_category = mirror_categories[0]
        current_filter = "Unlocked"
        current_sorting = "A-z"

        menu_items = mirror_sortfilter(mirror.get_instances_of_tag(current_category), current_sorting, current_filter)
        menu_items_length = len(menu_items)
        current_item = next(iter(menu_items), None)

    show screen mirror(xx, yy)

    label .after_init:
    $ _choice = ui.interact()

    if _choice[0] == "select":
        $ current_item = _choice[1]
        $ current_item.seen = True
    elif _choice[0] == "category":
        $ current_category = _choice[1]

        $ menu_items = mirror_sortfilter(mirror.get_instances_of_tag(current_category), current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = next(iter(menu_items), None)
    elif _choice == "inc":
        $ current_page += 1
    elif _choice == "dec":
        $ current_page += -1
    elif _choice == "filter":
        if current_filter == "Unlocked":
            $ current_filter = None
        elif current_filter == None:
            $ current_filter = "Unlocked"

        $ menu_items = mirror_sortfilter(mirror.get_instances_of_tag(current_category), current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = next(iter(menu_items), None)
    elif _choice == "sort":
        if current_sorting == "A-z":
            $ current_sorting = "z-A"
        else:
            $ current_sorting = "A-z"

        $ menu_items = mirror_sortfilter(mirror.get_instances_of_tag(current_category), current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = next(iter(menu_items), None)
    elif _choice[0] == "play":
        $ _choice[1].play()
        $ renpy.jump_out_of_context("mirror")
    else:
        $ enable_game_menu()
        hide screen mirror
        return

    jump .after_init

screen mirror(xx, yy):
    tag mirror
    zorder 30
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background

    use close_button

    fixed:
        if settings.get("animations"):
            at gui_animation
        use mirror_menu(xx, yy)
        use mirror_menuitem(xx, yy)

screen mirror_menu(xx, yy):
    window:
        style "empty"
        style_prefix gui.theme('achievements')
        pos (xx, yy)
        xysize (207, 454)

        use invisible_button()

        add gui.format("interface/achievements/{}/panel_left.webp")

        vbox:
            style_prefix gui.theme('achievements_categories')
            pos (6, 41)
            for category in mirror_categories:
                vbox:
                    textbutton category:
                        selected (current_category == category)
                        action Return(["category", category])

                    add gui.format("interface/achievements/{}/spacer_left.webp")
        vbox:
            style_prefix gui.theme('achievements_filters')
            pos (6, 384)

            if current_filter == None:
                textbutton "Show: All" action Return("filter")
            else:
                textbutton "Show: [current_filter]" action Return("filter")
            textbutton "Sort by: [current_sorting]" action Return("sort")

screen mirror_menuitem(xx, yy):
    window:
        style "empty"
        pos (xx+217, yy-53)
        xysize (560, 507)
        use invisible_button()

        #add "interface/achievements/star.webp"
        add gui.format("interface/achievements/{}/panel.webp")

        text "Mirror of Erised" size 22 xalign 0.5 ypos 65

        # Add items
        viewport:
            style_prefix gui.theme()
            draggable True
            mousewheel "vertical"
            scrollbars "vertical"
            maximum (512, 290)
            pos (24, 113)
            vbox:
                style_prefix "mirror"
                for ev in menu_items:
                    $ authors = ", ".join(ev.authors)
                    $ is_unlocked = ev.is_unlocked()
                    button:
                        ysize 30
                        selected_background Transform(gui.format("interface/achievements/{}/highlight.webp"), ysize=26)
                        selected (current_item == ev)
                        sensitive is_unlocked
                        xfill True
                        action Return(["select", ev])
                        if is_unlocked and not ev.seen:
                            text "NEW" style "wardrobe_item_caption" anchor (1.0, 1.0) align (1.0, 1.0) offset (-5, -5)
                        if ev.played:
                            add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-5, -5) zoom 0.7
                        vbox:
                            text ev.name
                            text "By {}".format(authors) size 10
                            add gui.format("interface/achievements/{}/spacer_left.webp")


        if menu_items_length <= 0:
            text "Nothing here yet" align (0.5, 0.5) anchor (0.5, 0.5) size 24

        if current_item:
            frame:
                xalign 0.5
                ypos 412

                vbox:
                    xalign 0.5
                    add gui.format("interface/achievements/{}/highlight.webp")
                    add gui.format("interface/achievements/{}/spacer.webp")
                    vbox:
                        yoffset 6
                        xmaximum 400
                        text "[current_item.desc]" size 12
                        text "Tags:{}".format(", ".join(current_item.tags)) size 10

                text "[current_item.name]" xalign 0.5 ypos 3 size 16

                textbutton "Play":
                    xalign 0.95
                    text_size 16
                    sensitive current_item.is_unlocked()
                    action Return(["play", current_item])

style mirror_button is empty

style mirror_button_text:
    color "#402313"
    insensitive_color "#40231380"
    hover_color "#FFF"
    outlines []

style mirror_text is mirror_button_text:
    color "#402313"
    insensitive_color "#40231380"
    hover_color "#FFF"
    outlines []
