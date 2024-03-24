init python:
    def wardrobe_check_category(category):
        req = get_character_requirement(states.active_girl, "category {}".format(category))
        flag = get_character_progression(states.active_girl)

        return (flag >= req)

    def wardrobe_check_touch(what):
        req = get_character_requirement(states.active_girl, "touch {}".format(what))
        flag = get_character_progression(states.active_girl)

        return (flag >= req)

    def wardrobe_check_equip(item):
        req = item.level
        flag = get_character_progression(states.active_girl)

        return (flag >= req)

    def wardrobe_check_unequip(item):
        req = get_character_requirement(states.active_girl, "unequip {}".format(item.type))
        flag = get_character_progression(states.active_girl)

        return (flag >= req)

    def wardrobe_check_equip_outfit(item):
        req = max((i.level for i in item.group))
        flag = get_character_progression(states.active_girl)

        has_bra = any(i.type == "bra" for i in item.group)
        has_panties = any(i.type == "panties" for i in item.group)

        if not has_bra:
            req = max(req, get_character_requirement(states.active_girl, "unequip bra"))

        if not has_panties:
            req = max(req, get_character_requirement(states.active_girl, "unequip panties"))

        if any(i.type.startswith(("piercing", "tattoo")) for i in item.group):
            req = max(req, get_character_requirement(states.active_girl, "category piercings & tattoos"))

        return (flag >= req)

    def wardrobe_check_blacklist(item):
        if not item.blacklist:
            return True

        req = max( ( get_character_requirement(states.active_girl, "unequip {}".format(i)) for i in item.blacklist ) )
        flag = get_character_progression(states.active_girl)

        return (flag >= req)

    def wardrobe_fallback_required(item):
        fallbacks = {"top", "bottom", "bra", "panties"}
        char = get_character_object(states.active_girl)
        req = [get_character_requirement(states.active_girl, "unequip {}".format(i)) for i in fallbacks if not char.is_equipped(i) and not i in char.blacklist]

        if not req:
            return False

        req = max(req)
        flag = get_character_progression(states.active_girl)

        return not (flag >= req)

    def wardrobe_react(what, arg):
        global _skipping
        if wardrobe_chitchats:
            _skipping = True
            renpy.suspend_rollback(False)
            renpy.block_rollback()
            renpy.call_in_new_context(get_character_response(states.active_girl, what), arg)
        return
