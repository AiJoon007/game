define sus_requirements = {
    "category upper undergarment": 5,
    "category lower undergarment": 5,
    "category piercings & tattoos": 16,
    "touch head": 4,
    "touch breasts": 12,
    "touch vagina": 18,
    "unequip panties": 6,
    "unequip bra": 6,
    "unequip top": 3,
    "unequip bottom": 3,
    }

define sus_responses = {
    "category_fail": "sus_reaction_category_fail",
    "equip": "sus_reaction_equip",
    "equip_fail": "sus_reaction_equip_fail",
    "unequip": "sus_reaction_unequip",
    "unequip_fail": "sus_reaction_unequip_fail",
    "touch": "sus_reaction_touch",
    "touch_fail": "sus_reaction_touch_fail",
    "equip_outfit": "sus_reaction_equip_outfit",
    "equip_outfit_fail": "sus_reaction_equip_outfit_fail",
    "blacklist": "sus_reaction_blacklist",
    "fallback": "sus_reaction_fallback",
}

label sus_reaction_category_fail(category):

    if category == "upper undergarment":
        sus @ cheeks blush "M--{w=0.2} my underwear? W-- {w=0.2}Why do you require me to--{w=0.2} *Ehm*..." ("angry", "happy", "sad", "down")
    elif category == "lower undergarment":
        sus @ cheeks blush "M--{w=0.2} my underwear? W--{w=0.2} Why do you require me to--{w=0.2} *Ehm*..." ("soft", "happy", "sad", "downR")
    elif category == "piercings & tattoos":
        sus @ cheeks blush "W--{w=0.2} What would people... Sir, I don't want to be made f--{w=0.2} fun of..." ("angry", "happy", "sad", "right")
    sus @ cheeks blush "" ("normal", "happy", "sad", "mid")
    return

label sus_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()
    else:
        $ mouse_heart()

    if what == "head":
        $ mouse_headpat()

        random:
            sus "S--{w=0.2} Sir..." ("soft", "base", "base", "mid")
            sus "A--{w=0.2} Are you s-sure this is appropriate?" ("open", "base", "base", "right")
            sus @ cheeks blush "Professor, p--{w=0.2} please..." ("base", "base", "sad", "downR")

    elif what == "breasts":
        $ mouse_heart()

        random:
            sus @ cheeks blush "W--{w=0.2} Why are you..." ("soft", "happy", "sad", "stare")
            sus @ cheeks blush "P--{w=0.2} please, it's embarrassing..." ("angry", "happy", "sad", "downR")
            sus @ cheeks blush "D--{w=0.2} don't... Don't look at me, sir..." ("soft", "closed", "sad", "mid")
    elif what == "vagina":
        $ mouse_heart()

        random:
            sus @ cheeks blush "M--{w=0.2} My..." ("soft", "happy", "sad", "stare")
            sus @ cheeks blush "S--{w=0.2} Sir..." ("soft", "closed", "sad", "mid")
            sus @ cheeks blush "P--{w=0.2} please sir, it's embarrassing..." ("base", "happy", "sad", "downR")

    return

label sus_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        sus @ cheeks blush "*Eeek*!" ("angry", "happyCl", "sad", "mid")
        sus @ cheeks blush "I'm sorry sir, you scared me..." ("angry", "base", "sad", "mid")
        gen "(Poor thing isn't used to human touch...)" ("base", xpos="far_left", ypos="head")

    elif what == "breasts":
        $ mouse_slap()

        sus @ cheeks blush "Please...{w=0.4} Don't bully me [name_genie_susan]." ("angry", "happy", "sad", "down")

    elif what == "vagina":
        $ mouse_slap()

        sus @ cheeks blush "No! Please don't make me do this in front of everyone again..." ("angry", "happyCl", "sad", "mid")
        gen "Do what?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "N--{w=0.2} nothing [name_genie_susan], forgive me." ("angry", "wide", "sad", "stare")
        gen "(...)" ("base", xpos="far_left", ypos="head")

    return

label sus_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     sus "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"

    # TODO: Blacklist fallbacks have to be added.
    return

label sus_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     sus "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    sus @ cheeks blush "I--{w=0.2} I..." ("soft", "happy", "base", "right")
    gen "You don't like it?" ("base", xpos="far_left", ypos="head")
    sus @ cheeks blush "It's not like t-that, I just..." ("angry", "happy", "worried", "right")
    gen "Not comfortable wearing it?" ("base", xpos="far_left", ypos="head")
    sus @ cheeks blush "*Uh-huh*" ("normal", "happy", "worried", "down")
    gen "Okay, maybe later then." ("base", xpos="far_left", ypos="head")

    return

label sus_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if states.sus.level > 15:
    #        sus "You want to see my snatch?"
    #        sus "You got it [name_genie_hermione]!"
    #
    return

label sus_reaction_unequip_fail(item):
    if item.type == "panties":
        sus @ cheeks blush "I'm N--{w=0.2} not comfortable with that, [name_genie_susan]..." ("open", "happy", "sad", "right")

    elif item.type == "bra":
        sus @ cheeks blush "P--{w=0.2} please, I can't be D--{w=0.2} doing that, [name_genie_susan]..." ("soft", "happy", "worried", "down")

    elif item.type == "top":
        sus @ cheeks blush "I don't know if this is a good idea..." ("annoyed", "happy", "sad", "mid")
        gen "You have nothing to be ashamed of." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "S--{w=0.2} Sorry, I can't..." ("soft", "happyCl", "worried", "mid")

    elif item.type == "bottom":
        sus @ cheeks blush "I--{w=0.2} I can't..." ("open", "happyCl", "sad", "mid")
        gen "It's okay, we'll work on your confidence first." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "Thank you..." ("soft", "happy", "base", "mid")
    return

label sus_reaction_equip_outfit(item):
    ########################
    ## Default Schoolgirl ##
    ########################
    if item == sus_outfit_default:
        gen "Could you put on your regular school uniform for me?" ("base", xpos="far_left", ypos="head")
        sus "Of course, [name_genie_susan]." ("base", "base", "base", "mid")
        sus "I'll just go and change real quick..." ("open", "base", "base", "right")

    ##########################
    ## Muggle Casual Outfit ##
    ##########################
    elif item == sus_outfit_muggle_casual1:
        gen "Could you put on your normal clothing for me?" ("base", xpos="far_left", ypos="head")
        sus "What do you--{w=0.2} *Ehm*...{w=0.4} Which clothing, [name_genie_susan]?" ("soft", "happy", "raised", "mid")
        gen "The boring sweater one, and the jeans." ("base", xpos="far_left", ypos="head")
        sus "My muggle clothing?" ("open", "base", "raised", "mid")
        gen "Sure!" ("base", xpos="far_left", ypos="head")
        sus "Okay then." ("base", "base", "base", "mid")

    ########################
    ## Lingerie Outfit 1 ##
    ########################
    elif item == sus_outfit_lace1:
        gen "Could you put on this lingerie for me please?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "Okay...{w=0.4} One moment [name_genie_susan]." ("base", "narrow", "base", "downR")

    ##############################
    ## Latex Underwear Outfit 1 ##
    ##############################
    elif item ==sus_outfit_latex1:
        gen "Put your latex underwear on for me." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "The--{w=0.2} The latex, but it's so tight..." ("soft", "narrow", "base", "down")
        gen "I know! Perfectly enhances your greatest features!" ("base", xpos="far_left", ypos="head")
        gen "Or squishes them, rather..." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "Alright, if you say so..." ("base", "narrow", "base", "down")

    ################
    ## Priestess Outfit ##
    ################
    elif item ==sus_outfit_priestess:
        gen "How about you put on this Priestess outfit for me?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "A--{w=0.2} A Priestess outfit, [name_genie_susan]?" ("soft", "narrow", "base", "mid")
        gen "Indeed." ("grin", xpos="far_left", ypos="head")
        sus @ cheeks blush "Why would you-- I mean... Sorry, but I'm a bit confused." ("open", "narrow", "base", "down")
        gen "Luckily, you've got me here for guidance." ("grin", xpos="far_left", ypos="head")
        gen "Now put the dress on." ("grin", xpos="far_left", ypos="head")
        sus @ cheeks blush "Oh--{w=0.2} Okay then..." ("open", "narrow", "base", "mid")

    else:
        gen "Could you put this on for me?" ("base", xpos="far_left", ypos="head")
        sus "Of course [name_genie_susan]..." ("base", "base", "base", "mid")

    # TODO: Blacklist fallbacks have to be added.
    return

label sus_reaction_equip_outfit_fail(item):
    ########################
    ## Lingerie Outfit 1 ##
    ########################
    if item == sus_outfit_lace1:
        gen "Could you put on this lingerie for me please?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "L--{w=0.2} Lingerie!?" ("angry", "wide", "shocked", "mid")
        gen "Yep." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "I--{w=0.2} I--{w=0.2} Why would you ask me to--" ("angry", "happyCl", "worried", "mid")
        gen "...{w=0.4} Maybe some other time then." ("base", xpos="far_left", ypos="head")

    ##############################
    ## Latex Underwear Outfit 1 ##
    ##############################
    elif item ==sus_outfit_latex1:
        gen "Put your latex underwear on for me." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "The-- The what?!?" ("angry", "wide", "shocked", "mid")
        gen "These!" ("grin", xpos="far_left", ypos="head")
        sus @ cheeks blush "Oh, heavens!" ("clench", "wide", "base", "down")
        sus @ cheeks blush "I can't wear these!" ("open", "happyCl", "worried", "mid")
        gen "Of course you can! I made sure to have them made specifically for your size of--" ("base", xpos="far_left", ypos="head")
        gen "I mean, your size!" ("angry", xpos="far_left", ypos="head")
        sus @ cheeks blush "..." ("annoyed", "happy", "sad", "mid")
        gen "Oh, you meant can't as in won't." ("base", xpos="far_left", ypos="head")
        gen "Alright... Never mind then." ("base", xpos="far_left", ypos="head")
    ######################
    ## Priestess Outfit ##
    ######################
    elif item ==sus_outfit_priestess:
        gen "Put on this Priestess outfit for me will you?" ("base", xpos="far_left", ypos="head")
        sus "A what, sorry?"
        gen "This dress, here." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "B-- But, [name_genie_susan]!" ("angry", "wide", "shocked", "mid")
        sus @ cheeks blush "S-- Surely wearing that would be s--{w=0.2} sacrilegious!" ("open", "happyCl", "worried", "mid")
        gen "Sacre-- what?" ("base", xpos="far_left", ypos="head")
        gen "Sorry, I don't speak French." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "I-- I am not a Priestess, [name_genie_susan]." ("soft", "happy", "sad", "down")
        gen "What does that have to do with wearing a dress?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "S-- Sorry, [name_genie_susan]... I think I better not."("soft", "happy", "sad", "right")
        gen "Sacrebleu..." ("base", xpos="far_left", ypos="head")

    else:
        sus "I--{w=0.2} I..." ("angry", "happy", "sad", "mid")
        gen "You don't like it?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "It's not t-that I--{w=0.2} I just..." ("soft", "happyCl", "sad", "mid")
        gen "Not comfortable wearing it?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "*Uh-huh*" ("soft", "happy", "sad", "down")
        gen "Okay, maybe later then." ("base", xpos="far_left", ypos="head")

    return

label sus_reaction_blacklist(item):
    sus "B--{w=0.2} but..." ("angry", "happy", "sad", "mid")
    gen "But what?" ("base", xpos="far_left", ypos="head")

    if "top" in item.blacklist and susan.is_worn("top"):
        sus "I would feel cold without my top..." ("annoyed", "happy", "sad", "down")

    if "bottom" in item.blacklist and susan.is_worn("bottom"):
        sus @ cheeks blush "I c--{w=0.2} can't take off my bottoms." ("open", "happy", "sad", "down")
        gen "Can't or won't?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "Won't..." ("annoyed", "happy", "sad", "mid")
        gen "Come off it, I'm sure you'll like it." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "..." ("soft", "happy", "base", "right")

    if "bra" in item.blacklist and susan.is_worn("bra"):
        gen "Let me guess, you aren't comfortable without a bra?" ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "*uh-huh*" ("soft", "happy", "sad", "down")
        sus @ cheeks blush "" ("soft", "happy", "sad", "mid")

    if "panties" in item.blacklist and susan.is_worn("panties"):
        sus @ cheeks blush "M--{w=0.2} My panties..." ("angry", "happy", "sad", "down")
        gen "Oh, right... Yeah, you'd need to do something about those..." ("base", xpos="far_left", ypos="head")
        sus @ cheeks blush "I'd have to--{w=0.4} To..." ("soft", "happy", "sad", "downR")

    gen "How about just giving it a try?" ("base", xpos="far_left", ypos="head")
    gen "If you don't like it, you can always change back, would that be okay?" ("base", xpos="far_left", ypos="head")
    sus @ cheeks blush "Alright..." ("base", "happy", "base", "down")
    sus @ cheeks blush "" ("base", "happy", "base", "mid")

    return

label sus_reaction_fallback(item):
    if states.sus.level < get_character_requirement("susan", "unequip top") and not "top" in susan.blacklist and not item.type == "top":
        $ susan.equip(sus_top_school1)

    if states.sus.level < get_character_requirement("susan", "unequip bottom") and not "bottom" in susan.blacklist and not item.type == "bottom":
        $ susan.equip(sus_bottom_school1)

    if states.sus.level < get_character_requirement("susan", "unequip bra") and not "bra" in susan.blacklist and not item.type == "bra":
        $ susan.equip(sus_bra_base1)

    if states.sus.level < get_character_requirement("susan", "unequip panties") and not "panties" in susan.blacklist and not item.type == "panties":
        $ susan.equip(sus_panties_base1)

    sus "Just give me a second, I need to get my clothes back in order." ("open", "base", "base", "right")
    sus "" ("base", "base", "base", "mid")
    return
