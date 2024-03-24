
default wardrobe_music = False
default wardrobe_chitchats = True
default wardrobe_autosave = False
default wardrobe_suppress_warnings = False
default wardrobe_randomise_color = False
default wardrobe_global_color = False

# Used as custom order for the sorting
define wardrobe_subcategories_sorted = {
    "hair": 5, "shirts": 5, "skirts": 5, "pantyhose": 5, "slot1": 5, "panties": 5, "save": 5,
    "earrings": 4, "sweaters": 4, "trousers": 4, "stockings": 4, "bikini panties": 4, "load": 4,
    "neckwear": 3, "dresses": 3, "shorts": 3, "socks": 3, "schedule": 3,
    "one-piece suits": 2, "import": 2,
    "robes": 1, "export": 1,
    "gloves": 0, "pubes": 0, "delete": 0,
    "other": -1,
}

define wardrobe_categories = ("head", "piercings & tattoos", "upper body", "upper undergarment", "lower body", "lower undergarment", "legwear", "misc")
define wardrobe_outfit_schedule = ("day", "night", "cloudy", "rainy", "snowy")

init python:

    _lock = False

    def preload_wardrobe_assets():
        global _lock, _predicted
        _lock = True
        renpy.start_predict_screen("wardrobe")
        c = get_character_object(states.active_girl)
        d = [v[0] for i in c.wardrobe_list for v in i.get_layers(i._hash).values()]
        renpy.start_predict(*d, "interface/wardrobe/*.webp")
        _predicted = d
        _lock = False

    def rebuild_wardrobe_icons(items, subcat):
        if not settings.get("multithreading"):
            return

        if subcat == "import":
            return

        for i in items.get(subcat, []):
            i.build_button(subcat)

    def lock_wardrobe_icon(icon):
        if not settings.get("multithreading"):
            return icon

        lock = bool(DollThread._count)

        return gray_tint(icon) if lock else icon

    def randomise_wardrobe_color(cloth):

        def _func(cloth):
            if not cloth is None:
                if wardrobe_randomise_color and cloth.color:
                    col_len = len(cloth.color)
                    col = []

                    for i in range(col_len):
                        if col_len == 1:
                            col.append(tetriadic_colors[0])
                        elif col_len == 2:
                            col.append(double_colors[i-1])
                        elif col_len == 3:
                            col.append(triadic_colors[i-1])
                        else:
                            try:
                                col.append(tetriadic_colors[i-1])
                            except:
                                col.append(col[-1].rotate_hue(0.33))

                    cloth.set_color(col)

                    if wardrobe_global_color:
                        for outfit in char_active.outfits:
                            rebuild = False

                            for i in outfit.group:
                                if not (i.id, i.type) == (cloth.id, cloth.type):
                                    continue

                                if len(cloth.color) != len(i.color):
                                    print(f"Mismatched color lens:\n{cloth}\n{i}")
                                    renpy.notify("Error!")
                                    continue

                                i.set_color(cloth.color)
                                i.is_stale()
                                rebuild = True

                            if rebuild:
                                outfit.is_stale()

                    rebuild_wardrobe_icons(category_items, current_subcategory)

        if settings.get("multithreading"):
            thread = DollThread(target=_func, args=(cloth,), interval=0.05)
            thread.start()
        else:
            _func(cloth)
            renpy.restart_interaction()

    # @functools.cache # Cache resets on wardrobe exit
    def set_wardrobe_categories(current_category):
        category_items = OrderedDict(
            sorted(
                [
                    (subcat, [item for item in items if item.unlocked])
                    for subcat, items in wardrobe_subcategories.get(current_category, {}).items()
                ],
                key=lambda x: wardrobe_subcategories_sorted.get(x[0], 0),
                reverse=True
            )
        )
        return category_items

style loading_text:
    color "#ffffff"
    size 64

style loading_trivia_text:
    color "#ffffff"
    size 24

layeredimage loading:
    always "gui_fade"
    always Transform(Text("Loading", style="loading_text"), align=(0.5, 0.4))
    always "loading_spinner"

image loading_spinner:
    align (0.5, 0.5)

    Text("{unicode}╞▰═════════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═▰════════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞══▰═══════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═══▰══════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞════▰═════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═════▰════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞══════▰═══╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═══════▰══╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞════════▰═╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═════════▰╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═════════▰╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞════════▰═╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═══════▰══╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞══════▰═══╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═════▰════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞════▰═════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═══▰══════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞══▰═══════╡{/unicode}", style="loading_text")
    pause 0.1
    Text("{unicode}╞═▰════════╡{/unicode}", style="loading_text")
    pause 0.1
    repeat

label wardrobe:
    $ renpy.call_in_new_context("_wardrobe")
    return

label _wardrobe:
    $ renpy.config.skipping = None
    $ _game_menu_screen = None
    $ _skipping = False
    $ renpy.suspend_rollback(True)
    show loading zorder 1000

    # Ensure there's no thread in use before assigning a new one.
    while _lock:
        $ renpy.pause(0.5, hard=True)

    $ renpy.invoke_in_thread(preload_wardrobe_assets)

    # Await thread return
    # Note: renpy.pause must be called from within the main thread
    while _lock:
        $ renpy.pause(0.5, predict=True)

    hide loading

    # $ renpy.scene("screens")
    # show expression screenshot.image
    call wardrobe_menu

    show screen main_room
    show screen ui_top_bar
    $ _game_menu_screen = "save"
    $ _skipping = True
    $ renpy.stop_predict(_predicted)
    $ del _predicted
    $ renpy.suspend_rollback(False)
    $ renpy.block_rollback()
    return

screen wardrobe(xx, yy):
    tag wardrobe
    zorder 24
    add "gui_fade"

    if renpy.mobile:
        use close_button_background
    use close_button

    fixed:
        use wardrobe_menu(xx, yy)
        if current_category == "outfits":
            use wardrobe_outfit_menuitem(20, 50)
        elif current_subcategory != None:
            use wardrobe_menuitem(20, 50)

label wardrobe_menu():
    python:

        char_active = get_character_object(states.active_girl)
        char_outfit = get_character_outfit(states.active_girl, type="last")
        char_outfit.save()

        wardrobe_subcategories = char_active.wardrobe

        if renpy.android:
            wardrobe_subcategories.update( { "outfits": { k:char_active.outfits for k in {"load", "save", "delete", "schedule"} } } )
        else:
            wardrobe_subcategories.update( { "outfits": { k:char_active.outfits for k in {"load", "save", "delete", "schedule", "import", "export"} } } )

        # Defaults
        current_category = "head"
        category_items = set_wardrobe_categories(current_category)
        current_subcategory = list(category_items.keys())[0] if category_items else ""
        current_item = char_active.get_equipped_wardrobe_item(category_items, current_subcategory)
        last_track = renpy.music.get_playing()
        rebuild_wardrobe_icons(category_items, current_subcategory)

    if wardrobe_music:
        play music "music/Spring_In_My_Step.ogg" fadein 1 if_changed

    label .after_init:

    hide gui_fade

    if not renpy.get_screen("wardrobe"):
        show screen wardrobe(662, 50)
    $ renpy.hide(get_character_tag(states.active_girl))
    $ renpy.config.skipping = None
    $ _game_menu_screen = None
    $ _skipping = False
    $ renpy.suspend_rollback(True)
    $ renpy.block_rollback()

    # Note to self: Do not use a python: block, because
    # renpy cannot return to the middle of a python block
    # while mixing python and renpy scope
    # https://github.com/renpy/renpy/issues/959

    $ _choice = ui.interact()

    if _choice[0] == "category":
        if not current_category == _choice[1]:
            if wardrobe_check_category(_choice[1]):
                $ current_category = _choice[1]

                $ category_items = set_wardrobe_categories(current_category)
                $ current_subcategory = list(category_items.keys())[0] if category_items else ""

                if current_category == "outfits":
                    $ char_active.clear_outfit_button_cache()

                $ current_item = char_active.get_equipped_wardrobe_item(category_items, current_subcategory)

                $ char_active.wear("all")
                if current_category in ("lower undergarment", "upper undergarment"):
                    $ char_active.strip("top", "bottom", "robe", "accessory")
                elif current_category == "piercings & tattoos":
                    $ char_active.strip("top", "bottom", "robe", "accessory", "bra", "panties", "stockings", "gloves")
            else:
                $ wardrobe_react("category_fail", _choice[1])

            $ rebuild_wardrobe_icons(category_items, current_subcategory)

    elif _choice[0] == "subcategory":
        if not current_subcategory == _choice[1]:
            $ current_subcategory = _choice[1]

            if current_category == "outfits":
                $ char_active.clear_outfit_button_cache()

            $ current_item = char_active.get_equipped_wardrobe_item(category_items, current_subcategory)

            $ rebuild_wardrobe_icons(category_items, current_subcategory)

    elif _choice[0] == "equip":
        ### CLOTHING ###
        if isinstance(_choice[1], DollCloth):
            if _choice[1].type == "hair" and char_active.is_equipped_item(_choice[1]):
                play sound "sounds/fail.ogg"
                $ renpy.notify("Hair cannot be removed.")
            else:

                if char_active.is_equipped_item(_choice[1]):
                    # UNEQUIP
                    if wardrobe_check_unequip(_choice[1]):
                        $ wardrobe_react("unequip", _choice[1])
                        $ char_active.unequip(_choice[1])

                        if current_item:
                            $ current_item.clear_button_cache()
                            $ current_item.build_button()

                        $ current_item = None
                    else:
                        $ wardrobe_react("unequip_fail", _choice[1])
                else:
                    # EQUIP
                    if wardrobe_check_equip(_choice[1]):
                        $ wardrobe_react("equip", _choice[1])

                        # Blacklist handling
                        if not wardrobe_check_blacklist(_choice[1]):
                            $ wardrobe_react("blacklist", _choice[1])

                        $ _choice[1].mark_as_seen()
                        $ char_active.equip(_choice[1])

                        if current_item:
                            $ current_item.clear_button_cache()
                            $ current_item.build_button()

                        $ current_item = _choice[1]
                        $ current_item.clear_button_cache()
                        $ current_item.build_button()

                        if wardrobe_fallback_required(_choice[1]):
                            # Has to be called regardless of player preference.
                            $ renpy.call(get_character_response(states.active_girl, "fallback"), _choice[1])
                    else:
                        $ wardrobe_react("equip_fail", _choice[1])

        ### OUTFIT ###
        elif isinstance(_choice[1], DollOutfit):
            $ _outfit = char_active.create_outfit(temp=True)

            if _outfit == _choice[1]:
                $ renpy.notify("Load failed: Outfit already equipped.")
            else:
                if wardrobe_check_equip_outfit(_choice[1]):

                    if not _outfit.exists():
                        $ _confirmed = wardrobe_suppress_warnings or renpy.call_screen("confirm", "Discard unsaved changes and load this outfit?")

                        if _confirmed:
                            $ wardrobe_react("equip_outfit", _choice[1])
                            $ char_active.equip(_choice[1])
                            $ current_item = _choice[1]
                        else:
                            $ renpy.notify("Load failed: Cancelled by user.")
                    else:
                        $ wardrobe_react("equip_outfit", _choice[1])
                        $ char_active.equip(_choice[1])
                        $ current_item = _choice[1]
                else:
                    $ wardrobe_react("equip_outfit_fail", _choice[1])

    elif _choice[0] == "setcolor":
        python:
            current_item.set_color(_choice[1])
            current_item.clear_button_cache()
            current_item.build_button()

            if wardrobe_global_color:
                for outfit in char_active.outfits:
                    rebuild = False

                    for i in outfit.group:
                        if not i.id == current_item.id:
                            continue

                        i.set_color(current_item.color)
                        i.is_stale()
                        rebuild = True

                    if rebuild:
                        outfit.is_stale()

    elif _choice[0] == "touch":
        if wardrobe_check_touch(_choice[1]):
            $ wardrobe_react("touch", _choice[1])
        else:
            $ wardrobe_react("touch_fail", _choice[1])

    elif _choice[0] == "addoutfit":
        python:
            _outfit = char_active.create_outfit(temp=True)

            if _outfit.exists():
                renpy.notify("Save failed: Outfit already exists.")
            else:
                if _choice[1]:
                    _index = char_active.outfits.index(_choice[1])
                    _confirmed = wardrobe_suppress_warnings or renpy.call_screen("confirm", "Overwrite this outfit?")

                    if _confirmed:
                        _old_outfit = char_active.outfits[_index]
                        _old_schedule = _old_outfit.schedule.copy()

                        _outfit = char_active.create_outfit()
                        _outfit.delete() # Removes it from list only
                        _outfit.schedule = _old_schedule

                        char_active.outfits[_index] = _outfit
                        _outfit.build_button(current_subcategory)
                        renpy.notify("Overwritten.")
                    else:
                        renpy.notify("Save failed: Cancelled by user.")

                else:
                    _outfit = char_active.create_outfit()
                    _outfit.build_button(current_subcategory)
                    renpy.notify("Outfit Saved.")

                current_item = char_active.get_equipped_wardrobe_item(category_items, current_subcategory)

            category_items = set_wardrobe_categories(current_category)

    elif _choice[0] == "deloutfit":
        python:
            _confirmed = wardrobe_suppress_warnings or renpy.call_screen("confirm", "Delete this outfit?")

            if _confirmed:
                _choice[1].delete()
                category_items = set_wardrobe_categories(current_category)
                renpy.notify("Outfit Deleted.")

    elif _choice[0] == "export":
        python:
            filename = renpy.input("Save as:", datetime.datetime.now().strftime("%d %b %Y-%H%M%S"))

            if not filename.endswith(".png"):
                filename += ".png"

            _choice[1].export_data(filename)
            achievements.unlock("export")

    elif _choice[0] == "import":
        $ _outfit = char_active.import_outfit(_choice[1])

    elif _choice[0] == "schedule":
        $ renpy.call_screen("wardrobe_schedule_menuitem", _choice[1])

    elif _choice == "music":
        python:
            if wardrobe_music:
                wardrobe_music = False
                renpy.music.play(last_track)
            else:
                wardrobe_music = True
                renpy.music.play("music/Spring_In_My_Step.ogg", fadein=1)

    elif _choice == "randomise":
        python:
            _confirmed = False

            _outfit = char_active.create_outfit(temp=True)

            if not _outfit.exists():
                _confirmed = wardrobe_suppress_warnings or renpy.call_screen("confirm", "Randomise Outfit?\n{size=-6}Unsaved changes will be lost.{/size}")

                if not _confirmed:
                    renpy.notify("Advice: If you want to keep an outfit, save it.")
                    renpy.jump("wardrobe_menu.after_init")

            progress = get_character_progression(states.active_girl)

            if wardrobe_randomise_color:
                # Set once per interaction
                tetriadic_colors = [Color("%06x" % random.randint(0, 0xFFFFFF))]
                triadic_colors = [tetriadic_colors[0].rotate_hue(0.25)]
                double_colors = [tetriadic_colors[0], tetriadic_colors[0].rotate_hue(0.5)]

                for i in range(1, 3):
                    col = tetriadic_colors[0].rotate_hue((i * 90.0) / 360.0)
                    tetriadic_colors.append(col)

                    col = triadic_colors[i-1].rotate_hue((i * 75.0) / 360.0)
                    triadic_colors.append(col)

            for k in dict(char_active.states).keys():
                valid_choices = [x for x in char_active.wardrobe_list if (istype(x, (DollCloth, DollClothDynamic, DollMakeup)) and x.type == k and x.unlocked and progress >= x.level)]

                if k == "panties":
                    if not progress >= get_character_requirement(states.active_girl, "category lower undergarment"):
                        continue

                    if progress >= get_character_requirement(states.active_girl, "unequip panties"):
                        valid_choices += [None]
                elif k == "bra":
                    if not progress >= get_character_requirement(states.active_girl, "category upper undergarment"):
                        continue

                    if progress >= get_character_requirement(states.active_girl, "unequip bra"):
                        valid_choices += [None]
                elif k == "top":
                    if progress >= get_character_requirement(states.active_girl, "unequip top"):
                        valid_choices += [None]
                elif k == "bottom":
                    if progress >= get_character_requirement(states.active_girl, "unequip bottom"):
                        valid_choices += [None]
                elif any(k.startswith(type) for type in ("piercing", "tattoo")):
                    if not progress >= get_character_requirement(states.active_girl, "category piercings & tattoos"):
                        continue

                    valid_choices += [None]
                elif k == "hair":
                    pass
                elif k in char_active.body_layers:
                    pass
                else:
                    valid_choices += [None]

                if valid_choices:
                    cloth = random.choice(valid_choices)

                    if cloth:
                        randomise_wardrobe_color(cloth)
                        char_active.equip(cloth)
                    else:
                        char_active.unequip(k)

            if current_item:
                current_item.clear_button_cache()
                current_item.build_button(current_subcategory)

            current_item = char_active.get_equipped_wardrobe_item(category_items, current_subcategory)

            if current_item:
                current_item.clear_button_cache()
                current_item.build_button(current_subcategory)

    else: #_choice == "Close":
        python:
            _confirmed = False

            if wardrobe_autosave:
                _outfit = char_active.create_outfit()
            else:
                _outfit = char_active.create_outfit(temp=True)

                if not _outfit.exists():
                    renpy.notify("Advice: If you want to keep an outfit, save it.")
                    _confirmed = wardrobe_suppress_warnings or renpy.call_screen("confirm", "Exit without saving?\n{size=-6}Unsaved changes will be lost.{/size}")

                    if not _confirmed:
                        renpy.jump("wardrobe_menu.after_init")

                    char_active.equip(char_outfit)

                    if wardrobe_global_color:
                        for cloth in char_outfit.group:
                            for outfit in char_active.outfits:
                                rebuild = False

                                for i in outfit.group:
                                    if not (i.id, i.type) == (cloth.id, cloth.type):
                                        continue

                                    i.set_color(cloth.color)
                                    i.is_stale()
                                    rebuild = True

                                if rebuild:
                                    outfit.is_stale()

            renpy.hide_screen("wardrobe")
            char_active.wear("all")
            renpy.play('sounds/door2.ogg')

            if wardrobe_music:
                renpy.music.play(last_track)

            DollThread.stop_all()

            enable_game_menu()
            renpy.return_statement()

    jump .after_init

screen wardrobe_menu(xx, yy):
    tag wardrobe
    zorder 24
    style_prefix "wardrobe"

    default icon_bg = Frame(gui.format("interface/frames/{}/iconmed.webp"), 6, 6)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/wardrobe.webp")

    window:
        pos (xx, yy)
        xysize (344, 507)
        #background panel

        use invisible_button()

        # Main Categories
        grid 2 4:
            ypos 108
            xoffset -36
            xspacing 200 + 72
            yspacing 18

            for i, category in enumerate(wardrobe_categories):
                if wardrobe_check_category(category):
                    $ icon = Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/{}/{}.webp".format(states.active_girl, category), zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5)), icon_frame)
                else:
                    $ icon = Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/{}/{}.webp".format(states.active_girl, category), zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5), matrixcolor=SaturationMatrix(0.0)), icon_frame)
                $ icon_xoffset = -18 if (i % 2) == 0 else 18

                button:
                    focus_mask None
                    xysize (72, 72)
                    background lock_wardrobe_icon(icon)
                    activate_sound "sounds/scroll.ogg"
                    tooltip category
                    sensitive (not bool(DollThread._count))
                    action Return(["category", category])
                    if current_category == category:
                        xoffset icon_xoffset

        # Outfits and Studio
        hbox:
            $ icon_yoffset = -18

            pos (92, 18)
            spacing 18
            # Outfits Manager
            button:
                focus_mask None
                xysize (72, 72)
                background lock_wardrobe_icon(Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/outfits.webp", zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5)), icon_frame))
                tooltip "Outfits Manager"
                sensitive (not bool(DollThread._count))
                action Return(["category", "outfits"])
                if current_category == "outfits":
                    yoffset icon_yoffset

            # Studio
            if not renpy.android:
                button:
                    focus_mask None
                    xysize (72, 72)
                    background Fixed(icon_bg, Transform("interface/wardrobe/icons/categories/studio.webp", zoom=0.45, anchor=(0.5, 0.5), align=(0.5, 0.5)), icon_frame)
                    tooltip "Photo Studio"
                    action Function(renpy.call_in_new_context, "studio", states.active_girl)

        add panel

        # Character image cut to the size of the wardrobe
        add char_active.image:
            yoffset -6
            corner1 (184, 218)
            corner2 (924, 1200)
            zoom 0.45
            anchor (0.5, 1.0)
            align (0.5, 1.0)

        # Easter Egg (Headpats, boobs, pussy)
        button style "empty" xysize (120, 80) xalign 0.525 ypos 60 action Return(["touch", "head"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 238 action Return(["touch", "breasts"])
        button style "empty" xysize (120, 60) xalign 0.525 ypos 360 action Return(["touch", "vagina"])

        button:
            focus_mask None
            xysize (72, 72)
            align (0.0, 1.0)
            offset (10, -10)
            background lock_wardrobe_icon(Transform("interface/wardrobe/icons/random.webp", size=(72,72)))
            tooltip "Randomise Outfit"
            sensitive (not DollThread._count)
            action Return("randomise")

        use dropdown_menu(name="Options", pos=(12, 56)):
            textbutton "Music":
                style gui.theme("dropdown")
                tooltip "My immortal."
                selected wardrobe_music
                action Return("music")
            textbutton "Chit-chats":
                style gui.theme("dropdown")
                tooltip "{color=#35aae2}[states.active_girl]{/color} will make comments regarding your poor fashion tastes."
                action ToggleVariable("wardrobe_chitchats", True, False)
            textbutton "Outfits Scheduling":
                style gui.theme("dropdown")
                tooltip "{color=#35aae2}[states.active_girl]{/color} will automatically wear outfits\nbased on set schedule, time of day and weather."
                action [ToggleVariable(f"states.{states.active_girl[:3]}.wardrobe_scheduling", True, False), If((current_category == "outfits" and current_subcategory == "schedule"), Return(["subcategory", "save"]))]
            textbutton "Outfits Autosave":
                style gui.theme("dropdown")
                tooltip "Outfits will be automatically saved upon exit."
                action ToggleVariable("wardrobe_autosave", True, False)
            textbutton "Colour Synchronisation":
                style gui.theme("dropdown")
                tooltip "When changing colours of an item, apply it to all outfits with the same item."
                action ToggleVariable("wardrobe_global_color", True, False)
            textbutton "Colour Randomisation":
                style gui.theme("dropdown")
                tooltip "When randomising outfits, randomise colours as well."
                action ToggleVariable("wardrobe_randomise_color", True, False)
            textbutton "Prompts Suppression":
                style gui.theme("dropdown")
                tooltip "Disables warnings and prompts asking you to confirm certain actions. (Not recommended)"
                action ToggleVariable("wardrobe_suppress_warnings", True, False)

screen wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 24
    style_prefix "wardrobe"

    default icon_size = (96, 96)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default icon_transparent = Frame("interface/color_picker/checker.webp", tile=True)
    default panel = gui.format("interface/frames/{}/panel.webp")

    window:
        pos (xx, yy)
        xysize (560, 454)
        background panel

        use invisible_button()

        text "[current_category]" size 22 xalign 0.5 ypos 65

        # Colours
        if current_item and current_item.color:
            hbox:
                spacing 2
                xanchor 1.0
                pos (552, 61)

                # Colour picker
                button:
                    xysize (32, 32)
                    tooltip "Dye clothing"
                    action Return(["setcolor", 0])
                    add "interface/wardrobe/icons/brush.webp":
                        xysize (32, 32)

        # Subcategory icons
        hbox:
            spacing 5
            pos (12, 108)

            for subcategory in category_items.keys():
                $ icon = lock_wardrobe_icon("interface/wardrobe/icons/{}.webp".format(subcategory))

                button:
                    focus_mask None
                    xysize (72, 72)
                    background Transform(icon, size=(72, 72), fit="contain", alpha=0.65)
                    selected_background Transform(icon, size=(72, 72), fit="contain", )
                    selected (subcategory == current_subcategory)
                    tooltip subcategory
                    sensitive (not bool(DollThread._count))
                    action Return(["subcategory", subcategory])

        # # Item icons
        # if not menu_items:
        #     text "Nothing here yet" size 24 align (0.5, 0.6)
        # else:
        vpgrid:
            cols 5
            spacing 5
            pos (28, 192)
            xysize (507, 308)
            mousewheel True
            scrollbars "vertical"

            style_prefix gui.theme("wardrobe")

            for item in category_items.get(current_subcategory, []):
                add item.button

screen wardrobe_outfit_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 24
    style_prefix "wardrobe"

    default icon_size = (96, 168)
    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default panel = gui.format("interface/frames/{}/panel.webp")

    window:
        pos (xx, yy)
        xysize (560, 454)
        background panel

        use invisible_button()

        text "[current_category]" size 22 xalign 0.5 ypos 65

        # Subcategory icons
        hbox:
            spacing 5
            pos (8, 108)

            for subcategory in category_items.keys():
                $ icon = lock_wardrobe_icon("interface/wardrobe/icons/{}.webp".format(subcategory))
                $ action = Return(["subcategory", subcategory])

                if subcategory == "schedule" and not get_character_scheduling(states.active_girl):
                    $ icon = gray_tint(icon)
                    $ action = Confirm("Outfit scheduling is currently disabled,\nwould you like to turn it on?", [SetVariable(f"states.{states.active_girl[:3]}.wardrobe_scheduling", True), Return(["subcategory", subcategory])])

                button:
                    focus_mask None
                    xysize (72, 72)
                    background Transform(icon, alpha=0.65, xsize=72, fit="contain")
                    selected_background Transform(icon, xsize=72, fit="contain")
                    selected (subcategory == current_subcategory)
                    sensitive (not bool(DollThread._count))
                    tooltip subcategory
                    action action

        # Outfit icons
        vpgrid:
            cols 5
            spacing 5
            pos (28, 192)
            xysize (507, 308)

            # if renpy.android:
            #     mousewheel "horizontal"
            #     scrollbars "horizontal"
            # else:
            mousewheel True
            scrollbars "vertical"
            style_prefix gui.theme("wardrobe")

            # Add empty slot
            if current_subcategory == "save":
                textbutton "Save":
                    focus_mask None
                    xysize icon_size
                    insensitive_background "#0000001A"
                    idle_background "#00000033"
                    text_align (0.5, 0.5)
                    sensitive (not bool(DollThread._count))
                    action Return(["addoutfit", None])

            if current_subcategory == "import":
                for item in list_outfit_files():
                    add item
            else:

                for item in reversed(category_items.get(current_subcategory, [])):
                    add item.button

screen wardrobe_schedule_menuitem(item):
    tag dropdown
    zorder 24

    default mpos = renpy.get_mouse_pos()

    use invisible_button(action=Return(), alternate=Show("wardrobe_schedule_menuitem", item=item))

    window:
        style "empty"
        pos mpos
        #use invisible_button(action=NullAction(), alternate=Return())

        frame:
            style "empty"
            background "#00000080"
            padding (5, 5, 5, 5)

            vbox:
                spacing 0
                for i in wardrobe_outfit_schedule:
                    $ boolean = "" if item.schedule[i] else "Not "
                    $ caption = "{}worn during the {}".format(boolean, i) if i in ("day", "night") else "{}worn in {} weather".format(boolean, i)
                    textbutton i:
                        style gui.theme("dropdown")
                        tooltip caption
                        action [ToggleDict(item.schedule, i, True, False), item.clear_button_cache, Function(item.build_button, current_subcategory)]

style wardrobe_window is empty

style wardrobe_button is empty:
    foreground None
    hover_foreground "#ffffff80"
    activate_sound "sounds/click.ogg"

style wardrobe_button_text:
    color "#fff"
    insensitive_color "#808080"
    size 20
    outlines [ (2, "#000", 0, 0) ]

style wardrobe_item_caption:
    color "#fff"
    size 14
    outlines [ (1, "#000", 0, 0) ]

style dark_wardrobe_window is wardrobe_window
style dark_wardrobe_button is wardrobe_button
style darK_wardrobe_button_text is wardrobe_button_text
style dark_wardrobe_item_caption is wardrobe_item_caption
style dark_wardrobe_vscrollbar is dark_vscrollbar

style light_wardrobe_window is wardrobe_window
style light_wardrobe_button is wardrobe_button
style light_wardrobe_button_text is wardrobe_button_text
style light_wardrobe_item_caption is wardrobe_item_caption
style light_wardrobe_vscrollbar is light_vscrollbar
