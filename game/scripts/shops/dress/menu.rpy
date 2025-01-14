
init python:
    def shop_dress_sortfilter(item, sortby="Price (Asc)", filtering=None):
        # Always sort alphabetically first.
        item = sorted(item, key=lambda x: natsort_key(x.name))

        if sortby == "Price (Asc)":
            item = sorted(item, key=lambda x: x.price, reverse=False)
        elif current_sorting == "Price (Desc)":
            item = sorted(item, key=lambda x: x.price, reverse=True)
        if sortby == "Lewdness (Asc)":
            item = sorted(item, key=lambda x: get_outfit_score(x), reverse=False)
        elif current_sorting == "Lewdness (Desc)":
            item = sorted(item, key=lambda x: get_outfit_score(x), reverse=True)
        return item

label shop_dress:
    $ gui.in_context("shop_dress_menu")
    return

label shop_dress_menu:

    python:
        current_sorting = "Price (Asc)"
        category_items = {"hermione": hermione.outfits, "tonks": tonks.outfits, "cho": cho.outfits, "luna": luna.outfits, "astoria": astoria.outfits, "susan": susan.outfits}
        current_category = "hermione"
        store_cart = set()
        menu_items = shop_dress_sortfilter([x for x in category_items.get(current_category, []) if bool(x.unlocked == False and x.price > 0 and not x in store_cart)], current_sorting)
        current_item = next(iter(menu_items), None)
        parcel_callbacks = []

    show screen shop_dress()

    label .after_init:

    $ _choice = ui.interact()

    if _choice[0] == "category":
        $ current_category = _choice[1]
        $ menu_items = shop_dress_sortfilter([x for x in category_items.get(current_category, []) if bool(x.unlocked == False and x.price > 0 and not x in store_cart)], current_sorting)
        $ current_item = next(iter(menu_items), None)
    elif _choice[0] == "buy":
        show screen blktone
        with d3
        if game.gold < _choice[1].price:
            gen "(I don't have enough gold.)" ("base", xpos="far_left", ypos="head")
        else:
            if len(store_cart) < 5:
                $ renpy.call("purchase_outfit", _choice[1])

                play sound "sounds/money.ogg"
                $ game.gold -= _choice[1].price
                $ store_cart.add(_choice[1])
                $ menu_items = shop_dress_sortfilter([x for x in category_items.get(current_category, []) if bool(x.unlocked == False and x.price > 0 and not x in store_cart)], current_sorting)
                $ current_item = next(iter(menu_items), None)

                if len(store_cart) < 5:
                    maf "Anything else?"
                else:
                    maf "That was your fifth order, sir, I'm afraid it will have to be your last one."
            else:
                maf "I'm sorry luv but that's as much as you can order for now."
        hide screen blktone
        with d3

    elif _choice == "sort":
        if current_sorting == "Price (Asc)":
            $ current_sorting = "Price (Desc)"
        elif current_sorting == "Price (Desc)":
            $ current_sorting = "Lewdness (Asc)"
        elif current_sorting == "Lewdness (Asc)":
            $ current_sorting = "Lewdness (Desc)"
        elif current_sorting == "Lewdness (Desc)":
            $ current_sorting = "Price (Asc)"

        $ menu_items = shop_dress_sortfilter([x for x in category_items.get(current_category, []) if bool(x.unlocked == False and x.price > 0 and not x in store_cart)], current_sorting)
    else: # Close
        if len(store_cart) < 5:
            show screen blktone
            with d3
            menu:
                maf "Are you finished shopping, dearie?"

                "-Yes, I'm done-":
                    pass
                "-Not yet-":
                    hide screen blktone
                    with d3
                    jump .after_init

        if store_cart:
            $ transit_time = len(store_cart)+1
            $ packaging_fee = 45 + ( (len(store_cart)-1) * 20 )

            menu:
                maf "If you pay extra, I could hire a bunch of elves to speed things up..."
                "\"Fine. ([packaging_fee] gold)\"" if game.gold >= packaging_fee:
                    $ game.gold -= packaging_fee
                    $ transit_time = int(transit_time/2)
                "\"Fine. ([packaging_fee] gold)\"" (style="disabled") if game.gold < packaging_fee:
                    maf "Sorry luv, but it appears you have no gold left."
                "-No thanks-":
                    pass

            hide screen shop_dress
            hide screen blktone

            $ _tmp = "tomorrow" if transit_time == 1 else "in about {} days".format(str(transit_time))
            maf "You can expect a parcel [_tmp]."

            # Executes callbacks upon receival of the parcel.
            $ curry = renpy.curry(execute_callbacks)(parcel_callbacks) if parcel_callbacks else None
            $ parcel_callbacks = []
            $ Parcel(contents=[(k, 1) for k in store_cart], wait=transit_time, func=curry).send()
            
            return
        else:
             gen "Nothing has caught my eye I'm afraid." ("base", xpos="far_left", ypos="head")
             maf "Maybe next time."
             return

    jump .after_init

screen shop_dress():
    tag shop_dress
    zorder 15
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background
    use close_button

    fixed:
        if settings.get("animations"):
            at gui_animation

        use shop_dress_menu()
        use shop_dress_menuitem()

screen shop_dress_menu():
    tag shop_menu
    zorder 15
    style_prefix "shop"

    default icon_bg = gui.format("interface/achievements/{}/iconbox.webp")
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/panel_left.webp")
    default highlight = gui.format("interface/achievements/{}/highlight_left_b.webp")

    window:
        pos (150, 90)
        xysize (207, 454)
        background panel

        use invisible_button()

        vbox:
            pos (6, 6)
            for category in category_items.keys():
                if get_character_unlock(category):
                    $ icon = Fixed(icon_bg, Frame( Transform("interface/icons/head/{}.webp".format(category), fit="contain"), xysize=(42, 42), offset=(3, 3)), "interface/achievements/glass_iconbox.webp")

                    vbox:
                        textbutton category:
                            style "empty"
                            xysize (195, 48)
                            text_align (0.6, 0.5)
                            text_xanchor 0.5
                            text_size 20

                            foreground icon
                            hover_background highlight
                            selected_background highlight
                            selected (current_category == category)
                            action Return(["category", category])

                        add gui.format("interface/frames/{}/spacer_left.webp")

        vbox:
            style_prefix gui.theme('achievements_filters')

            pos (6, 384)
            button action None
            textbutton "Sort by: [current_sorting]" action Return("sort")

screen shop_dress_menuitem():

    tag shop_menuitem
    zorder 16
    style_prefix "shop"

    default icon_size = (144, 288)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/panel.webp")

    window:
        pos (367, 37)
        xysize (560, 501)
        background panel

        use invisible_button()

        text "Shop" size 22 xalign 0.5 ypos 65

        if current_item:

            frame:
                xalign 0.5
                ypos 412

                vbox:
                    xalign 0.5
                    add gui.format("interface/achievements/{}/highlight.webp")# pos (112, 375)
                    add gui.format("interface/achievements/{}/spacer.webp")# pos (120, 398)
                    text "[current_item.desc]" size 12 yoffset 6

                text "[current_item.name]" xalign 0.5 ypos 3 size 16

                $ frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)

                textbutton "Buy":
                    style "inventory_button"
                    background frame
                    xalign 0.95
                    action Return(["buy", current_item])

        vpgrid:
            rows 1
            xspacing 5
            yspacing 2
            draggable True
            mousewheel "horizontal"
            scrollbars "horizontal"
            xmaximum 512
            ypos 106
            xalign 0.5

            at transform:
                mesh True

            for item in menu_items:
                $ icon = Transform(item.image, crop=(215, 0, 680, 1200), mesh=True, gl_pixel_perfect=True)
                $ is_modded = item.is_modded()
                $ is_affordable = bool(game.gold >= item.price)

                button:
                    style "shop_outfit_button"
                    xysize icon_size
                    background Transform(icon, xsize=144, ysize=288, fit="contain", anchor=(0.5, 1.0), align=(0.5, 1.0), yoffset=-6)
                    selected (current_item == item)
                    action SetVariable("current_item", item)

                    add icon_frame

                    if is_affordable:
                        text "{color=#daa520}G{/color} [item.price]" xalign 0.5 ypos 10 color "#ffffff" outlines [ (1, "#000", 0, 0) ] style "shop_outfit_text"
                    else:
                        text "{color=#daa520}G{/color} {color=#ff0000}[item.price]{/color}" xalign 0.5 ypos 10 color "#ffffff" outlines [ (1, "#000", 0, 0) ] style "shop_outfit_text"

                    if config.developer:
                        $ outfit_score = get_outfit_score(item)
                        text "{color=#fff}score{/color} [outfit_score]" align (0.1, 0.98) color "#ffffff" outlines [ (1, "#000", 0, 0) ] size 8

                    hbox:
                        offset (5, -5)
                        align (0.0, 1.0)

                        if is_modded:
                            text "M" color "#00b200"

style shop_window is empty

style shop_outfit_button is empty:
    foreground None
    hover_foreground "#ffffff80"
    selected_foreground "#ffffff40"
    activate_sound "sounds/click.ogg"

style shop_outfit_button_text is default:
    size 14

style shop_outfit_text:
    size 20
