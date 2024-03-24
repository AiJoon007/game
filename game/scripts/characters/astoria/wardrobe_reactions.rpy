define ast_requirements = {
    "category upper undergarment": 5,
    "category lower undergarment": 5,
    "category piercings & tattoos": 16,
    "touch head": 4,
    "touch breasts": 12,
    "touch vagina": 18,
    "unequip panties": 15,
    "unequip bra": 15,
    "unequip top": 3,
    "unequip bottom": 3,
    }

define ast_responses = {
    "category_fail": "ast_reaction_category_fail",
    "equip": "ast_reaction_equip",
    "equip_fail": "ast_reaction_equip_fail",
    "unequip": "ast_reaction_unequip",
    "unequip_fail": "ast_reaction_unequip_fail",
    "touch": "ast_reaction_touch",
    "touch_fail": "ast_reaction_touch_fail",
    "equip_outfit": "ast_reaction_equip_outfit",
    "equip_outfit_fail": "ast_reaction_equip_outfit_fail",
    "blacklist": "ast_reaction_blacklist",
    "fallback": "ast_reaction_fallback",
}

label ast_reaction_category_fail(category):
    if category == "upper undergarment":
        ast "Good one sir!" ("smile", "narrow", "base", "mid")
        gen "I wasn't--" ("base", xpos="far_left", ypos="head")
        gen "..." ("base", xpos="far_left", ypos="head")
    elif category == "lower undergarment":
        ast "Why would I do that?" ("base", "narrow", "angry", "R")
        gen "I don't know... Why wouldn't you do it?" ("base", xpos="far_left", ypos="head")
        ast "..." ("base", "narrow", "base", "down")
    elif category == "piercings & tattoos":
        ast "Sounds awesome, but you'll just pick something stupid." ("angry", "narrow", "base", "R")
        gen "I'd never..." ("base", xpos="far_left", ypos="head")
        ast "Lies..." ("clench", "base", "base", "mid")
    return

label ast_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()

        random:
            block:
                ast "Whatever..." ("base", "base", "base", "down")
            block:
                ast "I'm only letting you do this because you didn't snitch on me..." ("open", "closed", "base", "mid")
                gen "Sure..." ("base", xpos="far_left", ypos="head")
            block:
                ast "What's this obsession with petting coming from?" ("open", "narrow", "base", "L")
                gen "*Err*..." ("base", xpos="far_left", ypos="head")
                ast "When people called you eccentric I didn't think they meant bonkers mad..." ("clench", "closed", "base", "down")
    elif what == "breasts":
        $ mouse_heart()

        random:
            block:
                ast "You're really enjoying that, aren't you?" ("base", "narrow", "base", "mid")
                ast "Well I guess you're just a man after all..." ("open", "closed", "base", "mid")
            block:
                ast "Hey!" ("clench", "base", "base", "mid")
                gen "What?" ("base", xpos="far_left", ypos="head")
                ast "..." ("grin", "narrow", "base", "L")
            block:
                ast "Gross..." ("annoyed", "narrow", "base", "mid")
    elif what == "vagina":
        $ mouse_heart()

        random:
            block:
                ast @ cheeks blush "What do you think you're doing?" ("clench", "base", "base", "mid")
                gen "Kissing you?" ("base", xpos="far_left", ypos="head")
                ast "Surely that's against some rule..." ("annoyed", "base", "base", "R")
                gen "Worried about rule breaking all of a sudden, are we?" ("base", xpos="far_left", ypos="head")
                ast "No..." ("base", "narrow", "base", "mid")
            block:
                ast "Aren't you a bold one..." ("base", "narrow", "base", "mid")
            block:
                ast "Thought you could slip past my wards, did you?" ("clench", "base", "base", "mid")
                ast @ cheeks blush "I'll have you know I felt none of that!" ("open", "closed", "base", "mid")

    return

label ast_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        random:
            block:
                ast "Hey!" ("annoyed", "base", "angry", "mid")
            block:
                ast "I'm not your pet, [name_genie_astoria]..." ("clench", "base", "base", "mid")
            block:
                ast "Oh sorry, my hand slipped." ("annoyed", "closed", "angry", "mid")
            block:
                ast "Do that again, and you'll regret it..." ("base", "base", "base", "mid")
            block:
                ast "Stop..." ("base", "base", "base", "mid")
            block:
                ast "Don't!" ("clench", "base", "base", "mid")
                $ mouse_slap()
                ast "Don't!{fast} Do!" ("clench", "narrow", "base", "mid")
                $ mouse_slap()
                ast "Don't! Do!{fast} That!" ("scream", "narrow", "angry", "mid")
                $ mouse_slap()
                ast "Don't! Do! That!{fast} Again!" ("scream", "closed", "angry", "mid")
                $ mouse_slap()
                play sound "sounds/kick.ogg"
                with hpunch
                pause 1.0
                gen "(Ouch, that hurt!)" ("angry", xpos="far_left", ypos="head")

    elif what == "breasts":
        $ mouse_slap()

        random:
            block:
                ast "Hey, cut that out!" ("angry", "narrow", "base", "mid")
            block:
                ast "Ouch, that hurts..." ("base", "base", "angry", "mid")
            block:
                ast "Hey, no nipple twisters..." ("clench", "base", "base", "mid")
            block:
                ast "Bad Touch!" ("upset", "closed", "base", "mid")
            block:
                ast "*EEEH* Don't you have better things to do?" ("scream", "closed", "angry", "mid")
            block:
                ast "{size=+5}What are you doing?{/size}" ("scream", "narrow", "angry", "L")
            block:
                ast "Stop that!" ("upset", "narrow", "base", "mid")

    elif what == "vagina":
        $ mouse_slap()

        random:
            block:
                ast "Hey, that's private property." ("base", "narrow", "angry", "down")
            block:
                ast "Get your filthy hands off me, [name_genie_astoria]." ("upset", "narrow", "base", "mid")
            block:
                ast "Stop it, you creep." ("annoyed", "narrow", "angry", "R")
            block:
                ast "Why would you do that... nasty old man..." ("clench", "narrow", "base", "L")
            block:
                ast "Don't touch me..." ("clench", "base", "base", "mid")
            block:
                ast "Don't be gross, [name_genie_astoria]." ("base", "base", "base", "mid")
            block:
                ast "..." ("clench", "closed", "base", "mid")
    return

label ast_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     ast "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label ast_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     ast "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    random:
        block:
            ast "*Nuh-uh*, I'm not putting that on." ("clench", "closed", "base", "mid")
        block:
            ast "*Pfff* You want me to wear that? In your dreams, old man..." ("annoyed", "narrow", "angry", "R")
        block:
            ast "Don't be such a creep, thanks but no, thanks." ("upset", "narrow", "base", "mid")

    return

label ast_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if states.ast.level > 15:
    #        ast "You want to see my snatch?"
    #        ast "You got it [name_genie_hermione]!"
    #
    return

label ast_reaction_unequip_fail(item):
    if item.type == "panties":
        ast "Like hell I would! Take off your own panties, old man..." ("clench", "closed", "base", "mid")

        show screen blkfade
        with d5

        play sound "sounds/zipper.ogg"
        ast "W-What are you doing?!" ("scream", "narrow", "angry", "L")
        play sound "sounds/kick.ogg"
        with hpunch
        pause 0.5
        ast "Oh my god-- is that...?!" ("upset", "narrow", "base", "mid")
        gen "..." ("grin", xpos="far_left", ypos="head")
        $ mouse_slap()
        with vpunch

        hide screen blkfade
        with d5

        gen "Did you really have to slap me?" ("angry", xpos="far_left", ypos="head")
        ast "You deserved it you perverted... Pervert!" ("scream", "closed", "angry", "mid")

    elif item.type == "bra":
        ast "Why would you even suggest that?" ("clench", "closed", "base", "mid")

    elif item.type == "top":
        ast "Ha! Keep dreaming, old man!" ("smile", "narrow", "base", "mid")

    elif item.type == "bottom":
        ast "My bottoms stay where they are, and that's final!" ("annoyed", "narrow", "angry", "R")
    return

label ast_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     ast "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label ast_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.
    # if item == <DollOutfit Object>:
    #     ast "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    ast "That's way beyond what I would consider dignified." ("annoyed", "narrow", "angry", "R")

    if states.sus.unlocked:
        ast "Consider asking Susan instead." ("base", "narrow", "base", "mid")
        ast "I'm sure she'd enjoy wearing it for you, that cow." ("smile", "narrow", "base", "R")

    return

label ast_reaction_blacklist(item):
    ast "Aren't you demanding too much, [name_genie_astoria]?" ("annoyed", "narrow", "base", "R")

    if "top" in item.blacklist and astoria.is_worn("top"):
        ast "My topmost garment won't work with that." ("upset", "base", "base", "mid")

    if "bottom" in item.blacklist and astoria.is_worn("bottom"):
        ast "Wearing bottoms with this would be a fashion-crime." ("clench", "base", "base", "mid")

    if "bra" in item.blacklist and astoria.is_worn("bra"):
        ast "I'd have to take off my bra." ("base", "base", "base", "down")

    if "panties" in item.blacklist and astoria.is_worn("panties"):
        ast "How do I even wear panties with that?" ("annoyed", "base", "base", "down")

    ast "This is stupid..." ("base", "base", "base", "mid")

    if states.sus.unlocked:
        gen "Perhaps I'll ask Susan instead--" ("base", xpos="far_left", ypos="head")

    ast "J-Just give me that!" ("annoyed", "base", "base", "L")

    return

label ast_reaction_fallback(item):
    if states.ast.level < get_character_requirement("astoria", "unequip top") and not "top" in astoria.blacklist and not item.type == "top":
        $ astoria.equip(ast_top_school1)

    if states.ast.level < get_character_requirement("astoria", "unequip bottom") and not "bottom" in astoria.blacklist and not item.type == "bottom":
        $ astoria.equip(ast_bottom_skirt1)

    if states.ast.level < get_character_requirement("astoria", "unequip bra") and not "bra" in astoria.blacklist and not item.type == "bra":
        $ astoria.equip(ast_bra_basic1)

    if states.ast.level < get_character_requirement("astoria", "unequip panties") and not "panties" in astoria.blacklist and not item.type == "panties":
        $ astoria.equip(ast_panties_basic1)

    ast "Just give me a second, I need to get my clothes back in order." ("open", "base", "base", "R")
    ast "" ("base", "base", "base", "mid")
    return
