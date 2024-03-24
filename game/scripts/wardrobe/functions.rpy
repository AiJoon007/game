init -1 python:
    def get_character_progression(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(states, f"{key[:3]}").level

    def get_character_scheduling(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(states, f"{key[:3]}").wardrobe_scheduling

    def get_character_requirement(key, type):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(renpy.store, key[:3]+"_requirements").get(type, 0)

    def get_character_response(key, type):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(renpy.store, key[:3]+"_responses").get(type)

    def get_character_object(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(store, key)

    def get_character_outfit(key, type="default"):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(store, "{}_outfit_{}".format(key[:3], type))

    def get_character_body(key, type="default"):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(store, "{}_body_{}".format(key[:3], type))

    def get_character_outfit_req(key, item):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))

        if not isinstance(item, DollOutfit):
            raise TypeError("'{}' is not a DollOutfit instance.".format(item))

        req = ["{}: {}".format(i.type, i.level) for i in item.group]
        has_bra = any(i.type == "bra" for i in item.group)
        has_panties = any(i.type == "panties" for i in item.group)

        if not has_bra:
            req += ["NO BRA: {}".format(get_character_requirement(key, "unequip bra"))]

        if not has_panties:
            req += ["NO PANTIES: {}".format(get_character_requirement(key, "unequip panties"))]
        print("\n".join(req))

    def get_character_tag(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return "{}_main".format(key)

    def get_character_sayer(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(store, key[:3])

    def get_character_gift_label(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return "give_{}_gift".format(key[:3])

    def get_character_potion_check_label(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return "{}_potion_check".format(key[:3])

    def get_character_potion_check(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(store, "{}_potion_check".format(key[:3]))

    def get_character_unlock(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(states, f"{key[:3]}").unlocked

    def get_character_gifted(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(states, f"{key[:3]}").gifted

    def get_character_mood(key):
        if not key in states.dolls:
            raise KeyError("'{}' character is undefined.".format(key))
        return getattr(states, f"{key[:3]}").mood

    def get_outfit_score(outfit):
        """Returns outfit 'lewdness' score"""

        score = 0

        for i in outfit.group:
            score += i.level//2

        if not outfit.has_type("bra"):
            score += 3

            if not outfit.has_type("top"):
                score += 6

        if not outfit.has_type("panties"):
            score += 6

            if not outfit.has_type("bottom"):
                score += 12

        if not outfit.has_type("top"):
            score += 4

        if not outfit.has_type("bottom"):
            score += 4

        # if outfit.has_type("buttplug"):
        #     score += 9

        if outfit.has_type("makeup"):
            score += 1

        if outfit.has_type("tattoo"):
            score += 2

        if outfit.has_type("piercing"):
            score += 3

        return score

    def mouse_slap():
        """Causes the mouse to be moved away from current position and displays a smoke effect"""
        renpy.play('sounds/slap.ogg')
        renpy.stop_predict_screen("gfx_effect")
        x, y = renpy.get_mouse_pos()
        xx = x+random.randint(-100, 100)
        yy = y+random.randint(-100, 100)
        renpy.show_screen("gfx_effect", start_x=x, start_y=y, target_x=xx, target_y=yy, img="smoke", xanchor=0.1, yanchor=0.7, zoom=0.2, duration=0.15)
        renpy.set_mouse_pos(xx, yy, duration=0.1)

    def mouse_headpat():
        """Causes the mouse to be moved away from current position and displays a heart effect"""
        renpy.play('sounds/slap_03.ogg')
        renpy.stop_predict_screen("gfx_effect")
        x, y = renpy.get_mouse_pos()
        xx, yy = x, y-15
        img = At(Text("*pat*", size=16, color="#000000CC", outlines=[(1, "#FFFFFFCC", 0, 0)]), random_rotation)
        renpy.hide_screen("gfx_effect")
        renpy.show_screen("gfx_effect", start_x=x, start_y=y, target_x=xx, target_y=yy, img=img, xanchor=0.5, yanchor=0.65, zoom=1.0, timer=0.35)

    def mouse_heart():
        """Causes the mouse to be moved away from current position and displays a heart effect"""
        renpy.play('sounds/kiss.ogg')
        renpy.stop_predict_screen("gfx_effect")
        x, y = renpy.get_mouse_pos()
        renpy.show_screen("gfx_effect", start_x=x, start_y=y, target_x=x, target_y=y, img="love_heart", xanchor=0.45, yanchor=0.65, zoom=0.2, timer=0.45)

    def wardrobe_fail_hint(value):
        """Displays required whoring/friendship/affection level."""
        word_list = {"tonks": "friendship", "astoria": "affection", "susan": "confidence", "luna": "corruption", "cho": "recklessness", "hermione": "whoring"}
        word = word_list.get(states.active_girl, "whoring")

        if game.cheats or game.difficulty <= 2:
            renpy.show_screen("blktone")
            renpy.with_statement(d3)
            renpy.say(None, "{size=+6}> Try again at "+word+" level {color=#7a0000}"+str(value)+"{/color}.{/size}")
            renpy.hide_screen("blktone")
            renpy.with_statement(d3)
        return

    def list_outfit_files():

        @functools.cache
        def build_button(rp):
            style = "wardrobe_button"
            child = Fixed(Transform(rp, xsize=96, fit="contain", yalign=1.0, yoffset=-6), Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6), xysize=(96, 168))
            action = Return(["import", rp])
            hover_foreground = "#ffffff80"

            return Button(child=child, action=action, hover_foreground=hover_foreground, style=style)

        path = f"{config.gamedir}/outfits/"

        if not os.path.exists(path):
            os.makedirs(path)

        files = []
        for f in os.listdir(path):
            fp = os.path.join(path, f)
            rp = os.path.relpath(fp, config.gamedir)

            if os.path.isfile(os.path.join(path, f)) and f.endswith(".png"):
                files.append(build_button(rp))

        return files
