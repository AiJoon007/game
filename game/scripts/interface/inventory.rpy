init python:
    def inventory_sortfilter(item, sortby="A-z", filtering=None):
        if filtering == "Owned":
            item = [x for x in item if x.owned > 0]

        # Always sort alphabetically first.
        item = sorted(item, key=lambda x: natsort_key(x.name))

        if sortby == "z-A":
            item = sorted(item, key=lambda x: natsort_key(x.name), reverse=True)
        elif current_sorting == "Available":
            item = sorted(item, key=lambda x: x.owned is True, reverse=True)
        elif current_sorting == "Unavailable":
            item = sorted(item, key=lambda x: x.owned is False)

        return item

default inventory_mode = 0 # 0 - Inventory, 1 - gifts

####################################
############# Menu #################
####################################

label inventory:
    $ gui.in_context("inventory_menu")
    jump main_room_menu

label inventory_menu(xx=150, yy=90):
    # Inventory dictionary

    python:

        if inventory_mode == 0:
            inventory_dict = {
                "Gifts": inventory.get_instances_of_type("gift"),
                "Books": inventory.get_instances_of_type("book"),
                "Scrolls": inventory.get_instances_of_type("scroll"),
                "Ingredients": inventory.get_instances_of_type("ingredient"),
                "Potions": inventory.get_instances_of_type("potion"),
                "Decorations": inventory.get_instances_of_type("decoration"),
                "Quest Items": inventory.get_instances_of_type("quest"),
            }
        elif inventory_mode == 1:
            inventory_dict = {
                "Gifts": inventory.get_instances_of_type("gift"),
                "Potions": inventory.get_instances_of_type("potion"),
                "Quest Items": inventory.get_instances_of_type("quest"),
            }

        items_shown = 36
        current_page = 0
        current_category = next(iter(inventory_dict.keys()))
        current_filter = "Owned"
        current_sorting = "Available"

        category_items = inventory_dict[current_category]
        menu_items = inventory_sortfilter(category_items, current_sorting, current_filter)
        menu_items_length = len(menu_items)
        current_item = next(iter(menu_items), None)

    show screen inventory(xx, yy)

    label .after_init:

    $ _choice = ui.interact()

    if _choice[0] == "select":
        $ current_item = _choice[1]
    elif _choice[0] == "category":
        python:
            current_category = _choice[1]
            category_items = inventory_dict[current_category]
            menu_items = inventory_sortfilter(category_items, current_sorting, current_filter)
            menu_items_length = len(menu_items)

            if current_category == "Decorations":
                menu_items = sorted(menu_items, key=lambda x: x.placement.id)

            current_page = 0
            current_item = next(iter(menu_items), None)

    elif _choice == "inc":
        $ current_page += 1
    elif _choice == "dec":
        $ current_page += -1
    elif _choice == "sort":
        python:
            if current_sorting == "A-z":
                current_sorting = "z-A"
            elif current_sorting == "z-A":
                current_sorting = "Available"
            elif current_sorting == "Available":
                current_sorting = "Unavailable"
            else:
                current_sorting = "A-z"
            menu_items = inventory_sortfilter(category_items, current_sorting, current_filter)
            menu_items_length = len(menu_items)

            if current_category == "Decorations":
                menu_items = sorted(menu_items, key=lambda x: x.placement.id)

            current_page = 0

            if not current_item or not menu_items_length:
                current_item = next(iter(menu_items), None)

    elif _choice == "filter":
        python:
            if current_filter == None:
                current_filter = "Owned"
            else:
                current_filter = None
            menu_items = inventory_sortfilter(category_items, current_sorting, current_filter)
            menu_items_length = len(menu_items)

            if current_category == "Decorations":
                menu_items = sorted(menu_items, key=lambda x: x.placement.id)

            current_page = 0

            if not current_item or not menu_items_length:
                current_item = next(iter(menu_items), None)

    elif _choice == "use":
        python:
            enable_game_menu()
            current_item.use()
    elif _choice == "give":

        if current_item.type == "gift":
            if get_character_gifted(states.active_girl):
                show screen blktone
                with d3
                gen "I already gave her a gift today. Don't want to spoil her too much..." ("base", xpos="far_left", ypos="head")
                hide screen blktone
                with d3
            else:
                hide screen inventory
                $ renpy.call(get_character_gift_label(states.active_girl), current_item)
                show screen inventory(xx, yy)
        elif current_item.type == "potion":
            if not states.active_girl in current_item.usable_on:
                show screen blktone
                with d3
                gen "(Something tells me this potion won't work on [states.active_girl].)" ("base", xpos="far_left", ypos="head")
                nar "Perhaps in the future..."
                hide screen blktone
                with d3
            elif not game.daytime:
                show screen blktone
                with d3
                gen "(Some grander force tells me I should give it to her during daytime only.)" ("base", xpos="far_left", ypos="head")
                hide screen blktone
                with d3
            elif get_character_mood(states.active_girl) > 0:
                show screen blktone
                with d3
                gen "(I don't think it's a good idea to give it to her when she's still upset with me...)" ("base", xpos="far_left", ypos="head")
                gen "(I should wait for her to calm down first.)" ("base", xpos="far_left", ypos="head")
                hide screen blktone
                with d3
            elif states.active_girl == "hermione" and not states.her.favors_convinced_stage == 2 and is_in_lead(gryffindor):
                show screen blktone
                with d3

                gen "[name_hermione_genie], what would you say--" ("base", xpos="far_left", ypos="head")
                her "I'm sorry professor but I don't need your help at the moment."
                her "My house is already in the lead points wise."
                gen "Figures..." ("base", xpos="far_left", ypos="head")

                call tutorial("points")

                hide screen blktone
                with d3
            else:
                python:
                    enable_game_menu()
                    inventory_mode = 0
                    current_item.give(states.active_girl)
        elif current_item.type == "quest":
            if not states.active_girl in current_item.usable_on:
                show screen blktone
                with d3
                gen "(Something tells me I cannot give this item to [states.active_girl].)" ("base", xpos="far_left", ypos="head")
                nar "Perhaps in the future..."
                hide screen blktone
                with d3
            #TODO Add daytime check for buttplug give item event
                #show screen blktone
                #with d3
                #gen "(Some grander force tells me I should give it to her during daytime only.)" ("base", xpos="far_left", ypos="head")
                #hide screen blktone
                #with d3
            elif get_character_mood(states.active_girl) > 0:
                show screen blktone
                with d3
                gen "(I don't think it's a good idea to give it to her when she's still upset with me...)" ("base", xpos="far_left", ypos="head")
                gen "(I should wait for her to calm down first.)" ("base", xpos="far_left", ypos="head")
                hide screen blktone
                with d3
            elif states.active_girl == "hermione" and not states.her.favors_convinced_stage == 2 and is_in_lead(gryffindor):
                show screen blktone
                with d3

                gen "[name_hermione_genie], I have something for you--" ("base", xpos="far_left", ypos="head")
                her "I'm sorry professor but I don't need your help at the moment."
                her "My house is already in the lead points wise."
                gen "Figures..." ("base", xpos="far_left", ypos="head")

                call tutorial("points")

                hide screen blktone
                with d3
            else:
                python:
                    enable_game_menu()
                    inventory_mode = 0
                    current_item.give(states.active_girl)

    else:
        hide screen inventory
        return

    jump .after_init

screen inventory(xx, yy):
    tag inventory
    zorder 15
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background
    use close_button(key=["inventory", "game_menu"])

    fixed:
        if settings.get("animations"):
            at gui_animation
        use inventory_menu(xx, yy)
        use inventory_menuitem(xx, yy)

screen inventory_menu(xx, yy):
    window:
        style "empty"
        style_prefix gui.theme('achievements')
        pos (xx, yy)
        xysize (207, 454)

        use invisible_button()

        add gui.format("interface/achievements/{}/panel_left.webp")

        vbox:
            pos (6, 41)
            for category in iter(inventory_dict.keys()):
                vbox:
                    textbutton category:
                        style "empty"
                        xsize 195 ysize 16
                        text_xalign 0.5
                        if current_category == category:
                            background gui.format("interface/achievements/{}/highlight_left.webp")
                        else:
                            hover_background gui.format("interface/achievements/{}/highlight_left.webp")
                            action Return(["category", category])
                    add gui.format("interface/achievements/{}/spacer_left.webp")

            # Gold & Tokens
            null height 16
            text "{color=#daa520}Gold{/color} {outlinecolor=#ffffff00}[game.gold]{/outlinecolor}" size 12 outlines [ (2, "#000", 0, 0) ] xalign 0.1 xanchor 0
            add gui.format("interface/achievements/{}/spacer_left.webp")
            text "{color=#2055da}Tokens{/color} {outlinecolor=#ffffff00}[tokens]{/outlinecolor}" size 12 outlines [ (2, "#000", 0, 0) ] xalign 0.1 xanchor 0
            add gui.format("interface/achievements/{}/spacer_left.webp")

        vbox:
            style_prefix gui.theme('achievements_filters')
            pos (6, 384)
            if current_filter == None:
                textbutton "Show: All" action Return("filter")
            else:
                textbutton "Show: [current_filter]" action Return("filter")
            textbutton "Sort by: [current_sorting]" action Return("sort")

screen inventory_menuitem(xx, yy):
    window:
        style "empty"
        style_prefix gui.theme()
        pos (xx+217, yy-53)
        xysize (560, 507)

        use invisible_button()

        add "interface/achievements/inventory.webp"
        add gui.format("interface/achievements/{}/panel.webp")

        #Western Egg
        button xsize 90 ysize 60 action Play("sound", "sounds/plushie.ogg") xalign 0.5 style "empty"

        text "Inventory" size 22 xalign 0.5 ypos 65

        #text "Unlocked: "+str(len([x for x in menu_items if x[1][3] is True]))+"/[menu_items_length]" size 12 pos (24, 70)

        # Page counter
        if menu_items_length > items_shown:
            hbox:
                xanchor 1.0
                pos (540, 24)
                spacing 5
                add "interface/page.webp" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown))) ypos 44 size 16
            vbox:
                pos (570, 186)
                spacing 10

                imagebutton:
                    idle gui.format("interface/frames/{}/arrow_up.webp")
                    if not current_page <= 0:
                        hover image_hover(gui.format("interface/frames/{}/arrow_up.webp"))
                        action Return("dec")

                imagebutton:
                    idle Transform(gui.format("interface/frames/{}/arrow_up.webp"), yzoom=-1)
                    if current_page < math.ceil((menu_items_length-1)/items_shown)-1:
                        hover Transform(image_hover(gui.format("interface/frames/{}/arrow_up.webp")), yzoom=-1)
                        action Return("inc")

        # Add items
        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 9) % 4
                $ col = i % 9
                frame:
                    style "empty"
                    xsize 48
                    ysize 48
                    pos (24+58*(col), 113+58*(row))
                    add gui.format("interface/achievements/{}/iconbox.webp")

                    if not current_item == None and current_item.id == menu_items[i].id:
                        add "interface/achievements/glow.webp" align (0.5, 0.5) zoom 0.105 alpha 0.7 at rotate_circular

                    if menu_items[i].owned > 0:
                        $ image_zoom = crop_image_zoom(menu_items[i].get_image(), 42, 42)
                    else:
                        $ image_zoom = crop_image_zoom(menu_items[i].get_image(), 42, 42, True)

                    add image_zoom align (0.5, 0.5)

                    button:
                        style gui.theme("overlay_button")
                        background "interface/achievements/glass_iconbox.webp"
                        xsize 46 ysize 46
                        action Return(["select", menu_items[i]])
                        tooltip menu_items[i].name

                    if menu_items[i].limit > 1 and menu_items[i].owned > 0:
                        if menu_items[i].infinite:
                            text "{unicode}∞{/unicode}" size 20 align (0.1, 0.1) offset(-1, -9) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                        else:
                            text str(menu_items[i].owned) size 10 align (0.1, 0.1) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                    elif current_category == "Decorations":
                        if menu_items[i].in_use:
                            add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-3, -3) zoom 0.5
                    elif current_category in ("Books", "Quest Items"):
                        if menu_items[i].used:
                            add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-3, -3) zoom 0.5

                    if inventory_mode == 1 and (not menu_items[i].givable or not states.active_girl in menu_items[i].usable_on):
                        add "#b2000040"

        if menu_items_length <= 0:
            text "Nothing here yet" align (0.5, 0.5) anchor (0.5, 0.5) size 24

        if current_item:
            frame:
                style "empty"
                xsize 96
                ysize 96
                pos (24, 375)
                add gui.format("interface/achievements/{}/icon_selected.webp")
                if current_item.owned > 0:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84)
                else:
                    $ image_zoom = crop_image_zoom(current_item.get_image(), 84, 84, True)
                add image_zoom align (0.5, 0.5)
                add "interface/achievements/glass_selected.webp" pos (6, 6)

                if current_category in {"Gifts", "Ingredients", "Potions"}:
                    if current_item.owned > 0:
                        if current_item.infinite:
                            text "{unicode}∞{/unicode}" size 30 align (0.1, 0.1) offset(-2, -10) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                        else:
                            text str(current_item.owned) size 14 align (0.1, 0.1) color "#FFFFFF" outlines [ (1, "#000", 0, 0) ]
                elif current_category == "Decorations":
                    if current_item.in_use:
                        add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-6, -6)
                elif current_category in ("Books", "Quest Items"):
                    if current_item.used:
                        add "interface/topbar/icon_check.webp" anchor (1.0, 1.0) align (1.0, 1.0) offset (-6, -6)

                if inventory_mode == 1 and (not current_item.givable or not states.active_girl in current_item.usable_on):
                    add "#b2000040"

            add gui.format("interface/achievements/{}/highlight.webp") pos (112, 375)
            add gui.format("interface/achievements/{}/spacer.webp") pos (120, 398)
            hbox:
                spacing 5
                xalign 0.5
                text current_item.name ypos 380 size 16 xoffset 45

            $ frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)

            if (inventory_mode == 0 and current_item.usable) or (inventory_mode == 1 and current_item.givable):
                textbutton "[current_item.caption]":
                    style "inventory_button"
                    background frame
                    xalign 0.89
                    xoffset 45
                    ypos 374
                    sensitive (current_item.owned > 0)
                    if inventory_mode == 0:
                        action Return("use")
                    elif inventory_mode == 1:
                        action Return("give")

            hbox:
                pos (132, 407)
                xsize 410
                text current_item.desc size 12

style inventory_button:
    xysize (90, 26)
    hover_foreground "#ffffff1F"

style inventory_button_text:
    outlines []
    align (0.5, 0.5)
    size 16
