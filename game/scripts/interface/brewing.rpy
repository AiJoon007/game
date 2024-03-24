init python:
    def brewing_sortfilter(item, sortby="A-z", filtering=None):
        # if filtering == "Locked":
        #     item = filter(lambda x: x.is_unlocked(), item)
        # elif filtering == "Unlocked":
        #     item = filter(lambda x: x.is_unlocked() is True, item)

        # Always sort alphabetically first.
        item = sorted(item, key=lambda x: natsort_key(x.name))

        if sortby == "z-A":
            item = sorted(item, key=lambda x: natsort_key(x.name), reverse=True)

        return item

label brewing:
    $ gui.in_context("brewing_menu")
    return

label brewing_menu(xx=150, yy=90):

    python:
        items_shown = 36
        current_filter = "Unlocked"
        current_sorting = "A-z"

        menu_items = brewing_sortfilter(inventory.get_instances_of_type("potion"), current_sorting, current_filter)
        menu_items_length = len(menu_items)
        current_item = next(iter(menu_items), None)

    show screen brewing(xx, yy)

    label .after_init:
    $ _choice = ui.interact()

    if _choice[0] == "select":
        $ current_item = _choice[1]
    elif _choice == "filter":
        if current_filter == "Unlocked":
            $ current_filter = None
        elif current_filter == None:
            $ current_filter = "Unlocked"

        $ menu_items = brewing_sortfilter(inventory.get_instances_of_type("potion"), current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_item = next(iter(menu_items), None)
    elif _choice == "sort":
        if current_sorting == "A-z":
            $ current_sorting = "z-A"
        else:
            $ current_sorting = "A-z"

        $ menu_items = brewing_sortfilter(inventory.get_instances_of_type("potion"), current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        #$ current_item = next(iter(menu_items), None)
    elif _choice[0] == "make":
        if _choice[1].has_ingredients():
            play sound "sounds/bubble.ogg"
            $ _choice[1].make()
        else:
            gen "It appears I'm missing some key ingredients..." ("base", xpos="far_left", ypos="head")
    else:
        $ enable_game_menu()
        hide screen brewing
        return

    jump .after_init

screen brewing(xx, yy):
    tag brewing
    zorder 15
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background

    use close_button

    fixed:
        if settings.get("animations"):
            at gui_animation
        use brewing_menu(xx, yy)
        use brewing_menuitem(xx, yy)

screen brewing_menu(xx, yy):
    window:
        style "empty"
        style_prefix gui.theme('achievements')
        pos (xx, yy)
        xysize (207, 454)

        use invisible_button()

        add gui.format("interface/achievements/{}/panel_left.webp")

        vpgrid:
            rows 1
            yfill True

            vbox:
                style_prefix gui.theme('achievements_categories')
                pos (6, 6)
                for i in menu_items:
                    frame:
                        style "empty"
                        xysize (195, 50)

                        vbox:
                            textbutton i.name:
                                xysize (195, 46)
                                text_align (0.6, 0.5)
                                text_xanchor 0.5
                                text_size 12
                                if current_item == i:
                                    background gui.format("interface/achievements/{}/highlight_left_b.webp")
                                else:
                                    hover_background gui.format("interface/achievements/{}/highlight_left_b.webp")
                                selected (current_item == i)
                                action Return(["select", i])

                            add gui.format("interface/achievements/{}/spacer_left.webp")

                        $ image_zoom = crop_image_zoom(i.get_image(), 42, 42)

                        button:
                            style gui.theme("overlay_button")
                            background gui.format("interface/achievements/{}/iconbox.webp")
                            foreground "interface/achievements/glass_iconbox.webp"
                            xysize (48, 48)
                            add image_zoom align (0.5, 0.5)

                        if i.owned > 0:
                            text str(i.owned) size 10 align (0.02, 0.1) color "#ffffff" outlines [ (1, "#000", 0, 0) ]
        vbox:
            style_prefix gui.theme('achievements_filters')
            pos (6, 384)

            if current_filter == None:
                textbutton "Show: All" action Return("filter")
            else:
                textbutton "Show: [current_filter]" action Return("filter")
            textbutton "Sort by: [current_sorting]" action Return("sort")

screen brewing_menuitem(xx, yy):
    default turned_on = False
    default drop_ingredients = False

    window:
        style "empty"
        pos (xx+217, yy-53)
        xysize (560, 507)
        use invisible_button()

        #add "interface/achievements/star.webp"
        add gui.format("interface/achievements/{}/panel.webp")

        if turned_on:
            add "interface/brewing/bg_on.webp" align (0.5, 1.0) xsize 548 fit "contain" yoffset -6
        else:
            add "interface/brewing/bg_off.webp" align (0.5, 1.0) xsize 548 fit "contain" yoffset -6

        text "Brewing Station" size 22 xalign 0.5 ypos 65

        if current_item:
            vbox:
                xsize 560
                pos (24, 113)
                spacing 5

                text "[current_item.desc]" size 12
                text "Usable on:" size 12
                hbox:
                    for c in current_item.usable_on:
                        add "interface/icons/head/{}.webp".format(c) size (24, 24)

            hbox:
                spacing 10
                pos (24, 270)

                for ingredient in current_item.recipe:
                    frame:
                        style "empty"
                        xysize (48, 48)
                        add gui.format("interface/achievements/{}/iconbox.webp")

                        if ingredient.owned > 0:
                            $ image_zoom = crop_image_zoom(ingredient.get_image(), 42, 42)
                        else:
                            $ image_zoom = crop_image_zoom(ingredient.get_image(), 42, 42, True)

                        add image_zoom align (0.5, 0.5)

                        button:
                            style gui.theme("overlay_button")
                            background "interface/achievements/glass_iconbox.webp"
                            xsize 46 ysize 46
                            action NullAction()
                            tooltip ingredient.name

                        if ingredient.owned > 0:
                            if ingredient.infinite:
                                text "{unicode}∞{/unicode}" size 20 align (0.1, 0.1) offset(-1, -9) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                            else:
                                text str(ingredient.owned) size 10 align (0.1, 0.1) color "#ffffff" outlines [ (1, "#000", 0, 0) ]
                        else:
                            text str(ingredient.owned) size 10 align (0.1, 0.1) color "#ff0000" outlines [ (1, "#000", 0, 0) ]

            frame:
                style "empty"
                xysize (64, 64)
                pos (464, 254)

                add gui.format("interface/achievements/{}/iconbox.webp") size (64, 64)

                if current_item.owned > 0:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 52, 52)
                else:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 52, 52, True)

                add image_zoom align (0.5, 0.5)

                button:
                    style gui.theme("overlay_button")
                    background Transform("interface/achievements/glass_iconbox.webp", size=(64, 64))
                    xysize (64, 64)
                    action NullAction()
                    tooltip current_item.name

                if current_item.owned > 0:
                    text str(current_item.owned) size 14 align (0.1, 0.1) color "#ffffff" outlines [ (1, "#000", 0, 0) ]

            imagebutton:
                if current_item.has_ingredients():
                    at transform:
                        subpixel True

                        on hover:
                            easeout_bounce 0.77 rotate 2 xoffset 3
                            easeout_bounce 0.77 rotate -2 xoffset -3
                            repeat

                        on idle:
                            linear 0.33 rotate 0 xoffset 0

                idle "cauldron_off"
                focus_mask None
                pos (381, 311)
                anchor (0.5, 0.5)
                action Return(["make", current_item])
                if current_item.has_ingredients():
                    hover image_hover("cauldron_on")
                    hovered [Play("background", "sounds/brewing_idle.ogg"), SetLocalVariable("turned_on", True)]
                    unhovered [Stop("background"), SetLocalVariable("turned_on", False)]
                else:
                    hover image_hover("cauldron_off")

            if turned_on:
                add "interface/brewing/glow.webp":
                    at transform:
                        align (0.5, 1.0)
                        xsize 548
                        fit "contain"
                        yoffset -6

                        alpha 0.1
                        linear 2.0 alpha 1.0
                        linear 1.5 alpha 0.1
                        repeat
