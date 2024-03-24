define her_requirements = {
    "category upper undergarment": 5,
    "category lower undergarment": 5,
    "category piercings & tattoos": 16,
    "touch head": 4,
    "touch breasts": 12,
    "touch vagina": 18,
    "unequip panties": 15,
    "unequip bra": 14,
    "unequip top": 3,
    "unequip bottom": 3,
    }

define her_responses = {
    "category_fail": "her_reaction_category_fail",
    "equip": "her_reaction_equip",
    "equip_fail": "her_reaction_equip_fail",
    "unequip": "her_reaction_unequip",
    "unequip_fail": "her_reaction_unequip_fail",
    "touch": "her_reaction_touch",
    "touch_fail": "her_reaction_touch_fail",
    "equip_outfit": "her_reaction_equip_outfit",
    "equip_outfit_fail": "her_reaction_equip_outfit_fail",
    "blacklist": "her_reaction_blacklist",
    "fallback": "her_reaction_fallback",
}

label her_reaction_category_fail(category):

    if category == "upper undergarment":
        random:
            her "I'd rather keep the underwear I have on already, thank you very much..." ("annoyed", "closed", "angry", "mid")
            block:
                her "You want me to change my underwear?" ("angry", "wide", "base", "mid")
                her "Why on earth would I do that?" ("open", "base", "angry", "R")
            block:
                her "Change my--" ("soft", "wide", "base", "mid")
                her "I'm not changing my underwear for you..." ("clench", "closed", "angry", "mid")
    elif category == "lower undergarment":
        random:
            her "I'm not going to let you ogle at my underwear..." ("angry", "happy", "angry", "mid")
            her "I don't believe there's anything wrong with my current underwear..." ("open", "base", "annoyed", "mid")
            her "[name_genie_hermione], I don't think this is part of our arrangement..." ("soft", "base", "annoyed", "mid")
    elif category == "piercings & tattoos":
        if states.her.level >= 12:
            her "*Ehm*... Do I have to?" ("annoyed", "squint", "base", "mid")
            her "Isn't it supposed to hurt?" ("upset", "base", "base", "R")
        elif states.her.level >= 6:
            her "You can look all you want, but I will not have such things done to my body..." ("normal", "base", "annoyed", "mid")
        else:
            #under naked level
            her "You want me to what?" ("open", "wide", "base", "mid")
            her "I will not put such things on my body..." ("clench", "base", "base", "mid")

    return

label her_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()

        if states.her.level >= 20:
            #craving it
            random:
                her @ cheeks blush "*Mmm*..." ("base", "closed", "base", "mid")
                her @ cheeks blush "Does this mean I've been a good girl, [name_genie_hermione]?" ("crooked_smile", "narrow", "base", "mid")
                her @ cheeks blush "Thank you [name_genie_hermione]..." ("base", "happy", "base", "mid")
        elif states.her.level >= 16:
            #enjoying it
            random:
                her @ cheeks blush "I guess I could get used to this..." ("soft", "closed", "base", "mid")
                her @ cheeks blush "*Hmm*... This does feel kind of nice..." ("open", "closed", "worried", "mid")
                her @ cheeks blush "..." ("base", "closed", "base", "mid")
        elif states.her.level >= 12:
            #enjoying it a bit
            random:
                her @ cheeks blush "..." ("normal", "happyCl", "base", "mid")
                her @ cheeks blush "I'm only letting you do this because I have to..." ("open", "squint", "annoyed", "mid")
                her @ cheeks blush "*Ehm*... Do you do this to every student?" ("base", "closed", "base", "mid")
        elif states.her.level >= 8:
            #confused
            random:
                her "*Ehm*... Isn't petting your student a bit weird?" ("upset", "happyCl", "base", "mid")
                her "Okay then... I guess this is what we're doing now..." ("disgust", "squint", "base", "mid")
                her "Is there something in my hair?" ("soft", "base", "base", "mid")
        else: # >= 4
            #annoyed but letting you
            random:
                her "Are you petting me?" ("disgust", "base", "base", "mid")
                her "Did you just...{w=0.4} Whatever..." ("annoyed", "narrow", "base", "R")
                her "Why are you doing that?" ("clench", "base", "base", "R")

    elif what == "breasts":
        $ mouse_heart()

        if states.her.level >= 20:
            random:
                her @ cheeks blush "*Mmm*...{w=0.4} Lower..." ("base", "closed", "base", "mid")
                her @ cheeks blush "I'm glad you're enjoying them so much, [name_genie_hermione]." ("base", "narrow", "base", "mid")
                her @ cheeks blush "*Ah*..." ("open", "closed", "base", "mid")
                her @ cheeks blush "Please be gentle..." ("soft", "closed", "base", "mid")
        elif states.her.level >= 16:
            random:
                her @ cheeks blush "So, I guess this is part of our arrangement now..." ("base", "narrow", "base", "down")
                her @ cheeks blush "Oh! Hey, at least give me a warning first." ("soft", "squint", "base", "mid")
                her @ cheeks blush "Your hands not good enough anymore?" ("base", "squint", "base", "R")
                her @ cheeks blush "Hey... These things are sensitive, you know..." ("grin", "narrow", "base", "down")
        else: # >= 12
            random:
                her @ cheeks blush "Why are you kissing my..." ("angry", "base", "base", "mid")
                her @ cheeks blush "I didn't say you could...{w=0.4} Never mind..." ("clench", "closed", "base", "mid")
                her @ cheeks blush "I thought I was supposed to get points for this..." ("annoyed", "base", "base", "mid")
                her @ cheeks blush "I guess a small kiss is fine..." ("annoyed", "base", "base", "R")
                her @ cheeks blush "That's not my cheek..." ("disgust", "narrow", "base", "mid")
    elif what == "vagina":
        $ mouse_heart()

        if hermione.is_worn("bottom"):
            # Bottoms only OR Bottoms AND panties
            random:
                her "Naughty..." ("grin", "narrow", "base", "mid")
                her @ cheeks blush "*Mmm*... Want to see what's underneath, do you?" ("base", "narrow", "base", "mid")
                her "Got your eye on something?" ("base", "narrow", "base", "mid")
        elif hermione.is_worn("panties"):
            # Panties only
            random:
                her @ cheeks blush "*Mmm*... Shall I take off my panties?" ("open", "closed", "base", "mid")
                her @ cheeks blush "You're going to make my panties wet if you keep doing that..." ("soft", "narrow", "base", "mid")
        else:
            # NO bottoms AND NO panties
            random:
                her @ cheeks blush "*Ah*..." ("open_tongue", "closed", "base", "mid")
                her @ cheeks blush "*Mmm*..." ("soft", "closed", "base", "mid")
                her @ cheeks blush "More..." ("open", "closed", "base", "mid")
                her @ cheeks blush "Keep going [name_genie_hermione]..." ("smile", "closed", "base", "mid")
            ##This could play after touching her enough times this wardrobe session##
            #her "*Nnngh*..." ("base", "base", "base", "mid")
            #with kissiris

    return

label her_reaction_touch_fail(what):

    if what == "head":
        $ mouse_slap()
        random:
            her "Stop that!" ("angry", "wide", "angry", "mid")
            her "[name_genie_hermione]!" ("open", "narrow", "angry", "L")
            her "Unhand me..." ("mad", "wide", "angry", "mid")
            her @ cheeks blush "Stop it please..." ("open", "happyCl", "angry", "mid")
            her "Hands off me." ("clench", "narrow", "angry", "mid")
    elif what == "breasts":
        $ mouse_slap()
        random:
            her "No touching!" ("open", "narrow", "angry", "L")
            her @ cheeks blush "Bad [name_genie_hermione]!" ("annoyed", "happyCl", "angry", "L")
            her "Hands to yourself." ("clench", "base", "angry", "R")
            her "Cut it out..." ("open", "narrow", "angry", "mid")
            her "Hands off me." ("mad", "wide", "angry", "mid")
    elif what == "vagina":
        $ mouse_slap()
        random:
            her "Stop that!" ("angry", "wide", "angry", "mid")
            her "[name_genie_hermione]!" ("open", "narrow", "angry", "L")
            her "Unhand me..." ("mad", "wide", "angry", "mid")
            her @ cheeks blush "Stop it please..." ("open", "happyCl", "angry", "mid")
            her "Hands off me." ("clench", "narrow", "angry", "mid")
    return

label her_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     her "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label her_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     her "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    random:
        her "I am not wearing that..." ("annoyed", "base", "angry", "down")
        her "Thanks. but no, thanks..." ("annoyed", "happyCl", "angry", "R")
        her "You actually think I'd put on something like that?" ("annoyed", "wide", "angry", "mid")
        her "I'm not some Slytherin skank [name_genie_hermione], ask them to humiliate themselves for your amusement..." ("open", "narrow", "angry", "L")
        her "This is too much." ("annoyed", "narrow", "angry", "R")

    return

label her_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if states.her.level > 15:
    #        her "You want to see my snatch?"
    #        her "You got it [name_genie_hermione]!"
    #
    return

label her_reaction_unequip_fail(item):

    if item.type == "panties":
        random:
            block:
                her "I'm not going to flash you anything!" ("clench", "narrow", "angry", "mid")
                her "{size=-4}Pervert...{/size}" ("annoyed", "narrow", "angry", "R")
            block:
                her "Take off my panties?! No way!" ("clench", "narrow", "angry", "mid")
                her "" ("annoyed", "narrow", "angry", "down")
            block:
                her "I am not taking off my panties!" ("clench", "narrow", "angry", "mid")
                her "" ("annoyed", "narrow", "angry", "mid")

    elif item.type == "bra":
        random:
            block:
                her "I'm not going to flash you anything!" ("clench", "narrow", "angry", "mid")
                her "{size=-4}Pervert...{/size}" ("annoyed", "narrow", "angry", "R")
            block:
                her "Take off my bra?! No way!" ("clench", "narrow", "angry", "mid")
                her "" ("annoyed", "narrow", "angry", "down")
            block:
                her "I am not taking off my bra!" ("clench", "narrow", "angry", "mid")
                her "" ("annoyed", "narrow", "angry", "mid")

    elif item.type == "top":
        her "Take my top off? Are you crazy?" ("annoyed", "narrow", "angry", "L")

    elif item.type == "bottom":
        her "Take my bottoms off, just so that you can ogle my ass? No, thank you." ("open", "narrow", "angry", "mid")
    return

label her_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.

    ########################
    ## Default Schoolgirl ##
    ########################
    if item == her_outfit_default:
        gen "Could you put on your regular school uniform?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 10:
            her "Of course, [name_genie_hermione]." ("open", "base", "base", "mid")
            her "Let me go and change real quick..." ("soft", "base", "base", "R")
        elif states.her.level < 19:
            her "Alright, [name_genie_hermione]." ("base", "base", "base", "mid")
            her "Let me go and change real quick..." ("open", "base", "base", "R")
        elif states.her.level < 22:
            her "Are you sure, [name_genie_hermione]?" ("open", "base", "base", "mid")
            her "My regular school uniform..." ("soft", "base", "base", "R")
            her "You don't even want me to remove my tie or show off any cleavage?" ("open", "squint", "worried", "mid")
            gen "No, [name_hermione_genie]... No cleavage today." ("base", xpos="far_left", ypos="head")
            her "(Is he up to something?)" ("normal", "narrow", "base", "R")
            her "(Maybe this is a test of some sort...)" ("clench", "squint", "base", "stare")
            her "Okay then, let me change it real quick." ("clench", "squint", "base", "R")
        else: #22+
            her "That old thing?" ("clench", "base", "base", "mid")
            her "Is this some silly joke, [name_genie_hermione]?" ("annoyed", "narrow", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "(I don't know...{w=0.3} Is it?)" ("base", xpos="far_left", ypos="head")
            her "This is unacceptable!" ("open", "closed", "annoyed", "mid")
            her "It doesn't even show any skin!" ("clench", "closed", "annoyed", "mid")
            gen "(...)" ("base", xpos="far_left", ypos="head")
            her "It's an insult to my breast, [name_genie_hermione]!!!" ("open", "squint", "annoyed", "mid")
            gen "*Gasps* {w=0.9}I would never... [name_hermione_genie]!" ("angry", xpos="far_left", ypos="head")

            $ temp_word = renpy.random.choice(["marvellous", "magnificent", "breathtaking", "wonderful", "spectacular", "sensational", "glorious", "beautiful", "lovely", "bananas"])

            gen "Your tits are [temp_word]!" ("angry", xpos="far_left", ypos="head")

            her "And yet you want me to wear those... Rags!" ("annoyed", "base", "annoyed", "mid")
            gen "Are you going to put the rags on, or not?" ("base", xpos="far_left", ypos="head")
            her "*Ugh*, fine! Let me change it real quick." ("upset", "closed", "annoyed", "mid")

    ###############################
    ## Clear Day (School no vest)##
    ###############################
    elif item == her_outfit_s_clearday:
        gen "Could you wear your school uniform for me? But leave the vest off." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "Certainly, [name_genie_hermione]." ("open", "squint", "base", "mid")
            her "I'd usually only take it off if it's hot outside... When it isn't, I always make a point to wear the vest." ("normal", "closed", "base", "mid")
            her "But you are the headmaster, after all, so I'll wear it without the vest if I must." ("open", "closed", "base", "mid")
            her "Let me just go and change, [name_genie_hermione]." ("open", "base", "base", "R")
        elif states.her.level < 13:
            her "Alright, [name_genie_hermione]." ("open", "squint", "base", "mid")
            her "Let me go and change it real quick." ("soft", "base", "base", "R")
        elif states.her.level < 22:
            her "Of course, [name_genie_hermione]." ("base", "squint", "base", "mid")
            her "I will just change it right here if you don't mind..." ("open", "closed", "base", "mid")
        else: #22+
            her "Just my school shirt and tie?" ("open", "base", "base", "mid")
            gen "Yes, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Do you want me to tie the shirt around my breasts?" ("base", "narrow", "base", "mid")
            gen "No, put it on properly." ("base", xpos="far_left", ypos="head")
            her "Properly, [name_genie_hermione]?" ("annoyed", "squint", "worried", "mid")
            gen "You know, buttons, and everything." ("base", xpos="far_left", ypos="head")
            her "Can I leave some buttons open, [name_genie_hermione]?" ("open", "squint", "worried", "mid")
            gen "I'm afraid not, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Okay then... Let me just change it real quick." ("annoyed", "narrow", "base", "R")

    ##################################################
    ## Clear Night (Jeans and muggle top with vest) ##
    ##################################################
    elif item == her_outfit_s_clearnight:
        gen "Could you wear your normal clothing, the one with jeans and the top with the vest?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "Of course!" ("base", "happy", "base", "mid")
            her "You should've seen the look on Malfoy's face when he saw me buy it in a muggle shop." ("smile", "closed", "base", "mid")
            her "It was right outside the leaky cauldron, you see." ("crooked_smile", "squint", "base", "R")
            her "He looked as if he had bitten into a--" ("smile", "happyCl", "base", "mid")
            gen "I don't need your life story, just put it on..." ("base", xpos="far_left", ypos="head")
            her "*Hmph*... Fine." ("upset", "squint", "base", "mid")
        elif states.her.level < 13:
            her "OK, [name_genie_hermione]." ("base", "base", "base", "mid")
            her "Let me put it on." ("open", "happy", "base", "mid")
        elif states.her.level < 22:
            her "Just my regular muggle clothing, [name_genie_hermione]?" ("soft", "squint", "base", "mid")
            gen "Indeed." ("base", xpos="far_left", ypos="head")
            her "If you say so..." ("open", "base", "base", "R")
        else: #22+
            her "My muggle clothing, [name_genie_hermione]?" ("open", "squint", "base", "L")
            gen "Yeah, that one!" ("base", xpos="far_left", ypos="head")
            her "It's a bit... Too normal, don't you think?" ("soft", "squint", "base", "mid")
            gen "I don't see how that's a bad thing..." ("base", xpos="far_left", ypos="head")
            her "Alright then... Let me put it on real quick." ("open", "narrow", "base", "down")

    ################################
    ## Snowy (Jeans and pullover) ##
    ################################
    elif item == her_outfit_s_snow:
        gen "Could you put on your regular clothing, the one with jeans and pullover?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "As you wish, [name_genie_hermione]." ("base", "squint", "base", "mid")
            her "I do love wearing it." ("base", "happyCl", "base", "mid")
            gen "Why's that?" ("base", xpos="far_left", ypos="head")
            her "My mother made it for me." ("base", "happy", "base", "R")
            gen "I see...{w} Is she as hot--" ("base", xpos="far_left", ypos="head")
            her "Let me go and change real quick." ("soft", "happy", "base", "R")
        elif states.her.level < 13:
            her "Glad you care about my health [name_genie_hermione]... This office does get a little bit cold sometimes." ("base", "closed", "base", "mid")
            gen "Ah yes... Your health is important... I wouldn't be able to summon you if you caught a cold, would I?" ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "squint", "base", "mid")
            her "I'll just go and change it then... [name_genie_hermione]." ("open", "base", "base", "R")
        elif states.her.level < 22:
            her "My mother made that jumper for me, you know..." ("open", "closed", "base", "mid")
            her "I wonder what she'd say if she knew I rarely wear it anymore..." ("soft", "closed", "base", "mid")
            gen "She'd probably be proud that you're not relying on her giving you clothes anymore." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Somehow, I doubt that..." ("normal", "squint", "base", "R")
        else: #22+
            her "That old thing?" ("annoyed", "base", "base", "mid")
            her "It's a bit boring, don't you think?" ("open", "squint", "base", "R")
            gen "I think you look great in it!" ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Alright then." ("soft", "narrow", "base", "mid")

    ##########################################
    ## Overcast (School skirt and pullover) ##
    ##########################################
    elif item == her_outfit_s_overcast:
        gen "Could you put on your regular clothing, the one with the school skirt and pullover?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "The pullover does go well with the school skirt, don't you think?" ("base", "squint", "base", "mid")
            gen "It would look good even without the skirt on in my opinion." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "How nice, I'll let my mother know you said--" ("base", "closed", "base", "mid")
            her @ cheeks blush "Wait, what did you say?" ("soft", "wide", "base", "mid")
            gen "I said it looks good." ("base", xpos="far_left", ypos="head")
            her "Oh... Okay then..." ("open", "happy", "base", "mid")
            her "Give me a moment to let me change." ("open", "base", "base", "R")
        elif states.her.level < 13:
            her "The skirt and pullover?" ("open", "squint", "base", "mid")
            gen "That's what I just said..." ("base", xpos="far_left", ypos="head")
            her "Okay, just making sure." ("soft", "squint", "base", "mid")
            her "One moment please..." ("base", "base", "base", "R")
        elif states.her.level < 22:
            her "Is it cold in here?" ("open", "squint", "base", "L")
            her "I guess I didn't notice..." ("normal", "base", "base", "down")
            her "One moment..." ("open", "base", "base", "mid")
        else: #22+
            her "Skirt and pullover..." ("normal", "squint", "base", "stare")
            her "A little bit of home..." ("normal", "squint", "base", "stare")
            gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "Oh... Sorry!" ("base", "base", "base", "mid")
            her "One moment..." ("open", "squint", "base", "mid")

    #####################################
    ## Rainy (School outfit with cloak)##
    #####################################
    elif item == her_outfit_s_rain:
        gen "Could you put on your regular school uniform, and your cloak as well?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "I wanted to talk to you about this actually..." ("open", "closed", "base", "mid")
            gen "(Oh, here we go...)" ("base", xpos="far_left", ypos="head")
            her "The cloak doesn't cover the head, so when it rains it just ends up in your hair." ("annoyed", "squint", "base", "mid")
            her "I always end up having to dry it using magic, which makes it go all frizzy." ("upset", "narrow", "base", "R")
            gen "Isn't your hair already--" ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "mid")
            gen "I mean... Great point [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Thank you..." ("base", "closed", "base", "mid")
            gen "Now. can you put it on?" ("base", xpos="far_left", ypos="head")
            her "...{w=0.4} Fine..." ("normal", "base", "base", "R")
        elif states.her.level < 13:
            her "Certainly, [name_genie_hermione]..." ("base", "base", "base", "mid")
            her "Just let me go and change real quick." ("open", "base", "base", "R")
        elif states.her.level < 22:
            her "You suddenly want me to cover up now?" ("angry", "narrow", "base", "R")
            menu:
                "\"Yes, your body disgusts me, and I'm doing everyone a favour...\"":
                    her "What!?" ("clench", "wide", "base", "mid")
                "\"Of course not...\"":
                    gen "I'd just like you to wear it... Is that so much to ask?" ("base", xpos="far_left", ypos="head")
                    her "I guess not..." ("upset", "base", "base", "R")
            gen "Don't be silly... Just put it on..." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "mid")
            her "Alright..." ("open", "narrow", "base", "mid")
        else: #22+
            her "*Hmm*... I don't really like wearing the cloak..." ("upset", "base", "base", "down")
            gen "Why's that?" ("base", xpos="far_left", ypos="head")
            gen "(As if I don't know the answer...)" ("base", xpos="far_left", ypos="head")
            her "It covers all the good bits!" ("soft", "closed", "annoyed", "mid")
            gen "Really? It doesn't look like it does..." ("base", xpos="far_left", ypos="head")
            her "What do you mean? You can barely see any--" ("annoyed", "narrow", "annoyed", "mid")
            gen "Your face is perfectly visible..." ("base", xpos="far_left", ypos="head")
            her "Oh... Such a charmer..." ("base", "squint", "annoyed", "R")
            her "Well... Since you're putting it that way..." ("smile", "wink", "base", "mid")
            her "" ("smile", "base", "base", "mid")

    ###################
    ## Pajama Outfit ##
    ###################
    elif item == her_outfit_pajama:
        gen "Could you put on your Pyjamas for me?" ("base", xpos="far_left", ypos="head")
        if game.daytime:
            her "My pyjamas?" ("annoyed", "base", "worried", "mid")
            her "But it's the middle of the day!" ("clench", "base", "worried", "mid")
            gen "So?" ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "base", "base", "mid")
            her "Alright, fine... I'm not going to argue with you." ("open", "squint", "worried", "R")
        else:
            her "My pyjamas?" ("open", "base", "base", "mid")
            if states.her.level < 13:
                her "You want me to sleep in here?" ("angry", "squint", "base", "mid")
            else: #13+
                her "Am I supposed to sleep over tonight?" ("open", "squint", "base", "mid")
            gen "Of course not..." ("base", xpos="far_left", ypos="head")
            gen "I'd just like you to put it on." ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "base", "mid")
            her "Alright then..." ("open", "base", "base", "mid")

    ########################
    ## Cheerleader Normal ##
    ########################
    elif item == her_outfit_cheerleader_1: #Req 10 whoring
        gen "Could you wear the cheerleader outfit for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 19:
            her "Gryffindor colours, I presume?" ("open", "closed", "base", "mid")
            gen "We'll see..." ("base", xpos="far_left", ypos="head")
            her "...{w=0.4} Fine." ("annoyed", "closed", "base", "mid")
        elif states.her.level < 22:
            her "*Hmm*... Alright then..." ("base", "happy", "worried", "R")
            her "I'll just change it here, shall I?" ("base", "narrow", "base", "mid")
            gen "That's the spirit." ("base", xpos="far_left", ypos="head")
        else: #22+
            her "That thing is so silly..." ("base", "squint", "base", "R")
            her "You sure you don't want to get a giant lion's head to go with it?" ("crooked_smile", "narrow", "base", "mid")

            random:
                her "Or perhaps some Raven's feathers?!" ("smile", "narrow", "base", "R")
                her "Or some Snake fangs?!" ("smile", "narrow", "base", "R")
                her "Or face paint, so I could look like a badger?!" ("smile", "narrow", "base", "R")

            gen "I mean, if I could find something like that, sure!" ("base", xpos="far_left", ypos="head")
            her "You can't be serious, [name_genie_hermione]!" ("open", "wide", "worried", "stare")
            gen "Wear it, or I will have you go naked!" ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "closed", "base", "mid")
            her @ cheeks blush "{size=-5}(How exciting!){/size}" ("base", "closed", "base", "mid")
            her @ cheeks blush "I will wear it if I absolutely have to..." ("open", "squint", "base", "mid")
            her @ cheeks blush "{size=-5}Do I?{/size}" ("grin", "base", "base", "L")
            gen "Yes." ("base", xpos="far_left", ypos="head")
            her "*Tzzz--* Your loss..." ("annoyed", "base", "base", "R")

    ######################
    ## Cheerleader Lewd ##
    ######################
    elif item == her_outfit_cheerleader_2: #Req 16 whoring (top)
        gen "Could you put on the cheerleader outfit for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "Of course!" ("smile", "base", "base", "mid")
            gen "Great, here you go!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "[name_genie_hermione], did you hand me the wrong outfit?" ("open", "squint", "base", "mid")
            gen "Let me see..." ("base", xpos="far_left", ypos="head")
            gen "Looks correct to me..." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]... This is not the official cheerleader outfit..." ("soft", "narrow", "base", "mid")
            gen "Oh, I see why you were confused then... Yes. this one has indeed had some improvements." ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "squint", "base", "R")
            gen "So, will you put it on?" ("base", xpos="far_left", ypos="head")
            her "Alright, fine..." ("angry", "squint", "base", "mid")
        else: #22+
            her "Of course!" ("smile", "happy", "base", "mid")
            gen "Excellent, here you are..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "How naughty... Although I doubt you'd be able to focus on the match if the cheerleaders wore these..." ("soft", "narrow", "base", "down")
            gen "Good point..." ("base", xpos="far_left", ypos="head")
            gen "I'm sure people would get excited..." ("base", xpos="far_left", ypos="head")
            her "I'm sure they would..." ("base", "squint", "base", "R")
            her "Go-Go Gryffindor!" ("smile", "squint", "base", "mid")

    #################
    ## Fishnet Outfit
    #################
    elif item == her_outfit_fishnet: #Req 19 (panties, top)
        gen "Could you please wear--" ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "A fishnet outfit?" ("angry", "squint", "base", "down")
            her "[name_genie_hermione]... Isn't this a bit..." ("annoyed", "squint", "base", "mid")
            gen "A bit what?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well, it's fetish gear, isn't it?" ("open", "base", "base", "R")
            gen "I'd say it's closer to lingerie than fetish gear." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Alright, fine... I'll wear it then." ("annoyed", "closed", "base", "mid")
        else: #22+
            her "A fishnet outfit?" ("soft", "squint", "base", "down")
            her @ cheeks blush "*Hmm*... My nipples would stick right through this..." ("base", "narrow", "base", "down")
            gen "I think that's the point." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright, just give me a moment, and I'll put it on for you..." ("soft", "base", "base", "mid")

    ######################
    ## Fishnet One-Piece ##
    ######################
    elif item == her_outfit_fishnet_onepiece: #Req 19 (top)
        gen "Could you put on the fishnet one-piece for me?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "The fishnet one-piece?" ("angry", "base", "base", "mid")
        if states.her.level < 22:
            her @ cheeks blush "*Hmm*... Lingerie..." ("angry", "narrow", "base", "down")
            gen "Yep..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "And I suppose I shouldn't ask where you got such an outfit from..." ("open", "narrow", "base", "down")
            gen "Probably shouldn't..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright..." ("soft", "narrow", "base", "down")
            her @ cheeks blush "Well, I suppose I'll wear it if I have to..." ("base", "closed", "base", "mid")
        else: #22+
            her @ cheeks blush "Lingerie?! How dare you [name_genie_hermione]!" ("angry", "narrow", "annoyed", "down")
            gen "..." ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Why didn't you ask me to put this on sooner?" ("angry", "narrow", "annoyed", "mid")
            gen "Listen here you--" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "*Giggles*..." ("grin", "squint", "base", "mid")

    ##################
    ## Latex Outfit ##
    ##################
    elif item == her_outfit_latex: #Req 19 (top)
        gen "Could you put on this latex outfit for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "Latex outfit?" ("open", "squint", "base", "mid")
            her @ cheeks blush "Whoa... This is skin tight!" ("clench", "narrow", "base", "down")
            gen "I know! Glad you're as excited as I am!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I... How do you put this on?" ("disgust", "base", "base", "mid")
            gen "Using lots of patience I reckon..." ("base", xpos="far_left", ypos="head")
            her "As if you have any of that..." ("open", "base", "annoyed", "R")
            her @ cheeks blush "Well... Here it goes." ("open", "base", "base", "mid")
        else: #22+
            her @ cheeks blush "*Hmm*... Well, I can't say something as skin tight as this doesn't excite me a little bit..." ("base", "narrow", "base", "mid")
            her @ cheeks blush "I might as well not be wearing anything with how little this leaves to the imagination." ("smile", "narrow", "base", "mid")
            gen "Like that's a bad thing..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I knew you'd say that... Alright then, give me a moment..." ("angry", "base", "base", "R")

    #######################
    ## Slutty Schoolgirl ##
    #######################
    elif item == her_outfit_slutty_schoolgirl: #Req 19 (top, Bottom)
        gen "Could you put on this school uniform for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "My school uniform?" ("angry", "base", "worried", "mid")
            her "Is this some sort of test?" ("clench", "squint", "base", "mid")
            gen "No, not a test. I'd just like you to put it on..." ("base", xpos="far_left", ypos="head")
            her "(*Hmm*... I feel like he's trying to trick me...)" ("normal", "base", "base", "R")
            gen "Just put it on..." ("base", xpos="far_left", ypos="head")
            her "Alright then..." ("open", "squint", "base", "mid")
            her @ cheeks blush "Oh... I see... That makes more sense.)" ("open", "base", "base", "down")
            gen "Is there something wrong?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "No, it's all good... Just give me a moment..." ("open", "base", "base", "mid")
            her @ cheeks blush "" ("base", "base", "base", "mid")
        else: #22+
            her "My school uniform?" ("open", "squint", "worried", "mid")
            her "But that thing is so boring..." ("clench", "closed", "worried", "mid")
            gen "Not this one..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... That one..." ("open", "base", "base", "down")
            her @ cheeks blush "Well, I suppose I could put that one on..." ("base", "base", "base", "R")
            her "One moment..." ("base", "base", "base", "mid")

    ##################
    ## Witch Outfit ##
    ##################
    elif item == her_outfit_witch: #Req 10 (top)
        gen "Put on this witch outfit for me, will you?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 13:
            her "Witch outfit?" ("open", "squint", "base", "mid")
            gen "The one I have right here." ("base", xpos="far_left", ypos="head")
            her "Sir, this is not a witch outfit..." ("disgust", "narrow", "base", "mid")
            gen "Of course it is... I see this kind of outfit all the time in the shops." ("base", xpos="far_left", ypos="head")
            her "In the... What shops exactly?" ("angry", "narrow", "base", "mid")
            gen "Next to the nurse outfits." ("base", xpos="far_left", ypos="head")
            her "Sir... Are you talking about the Cosplay section?" ("clench", "squint", "base", "mid")
            gen "That's the one!" ("base", xpos="far_left", ypos="head")
            her "Figures..." ("disgust", "closed", "base", "mid")
            her "I would've thought an actual wizard would get mad about the muggle interpretation of a witch..." ("open", "narrow", "base", "R")
            gen "I think it's flattering." ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "closed", "base", "mid")
            gen "So..." ("base", xpos="far_left", ypos="head")
            her "So?" ("upset", "base", "base", "mid")
            gen "You putting it on or what?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "If I have to..." ("normal", "squint", "base", "R")
            gen "You do." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Fine..." ("open", "base", "base", "down")
            her "Give me a moment to let me change." ("open", "base", "base", "R")
        elif states.her.level < 22:
            her "Witch outfit?" ("soft", "squint", "base", "mid")
            gen "The one I have right here." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh, I see..." ("angry", "narrow", "base", "down")
            her @ cheeks blush "Of course you'd want me to wear something like that..." ("clench", "closed", "base", "mid")
            her @ cheeks blush "To think it'd be a regular witches outfit..." ("open", "narrow", "base", "R")
            her @ cheeks blush "Well... I suppose I could put it on." ("normal", "base", "base", "down")
            her @ cheeks blush "One moment please..." ("normal", "squint", "base", "mid")
        else: #22+
            her "Witch outfit?" ("open", "squint", "base", "mid")
            gen "The one I have right here." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("grin", "base", "base", "down")
            her @ cheeks blush "Well... While real witches' outfits don't look like this, I do like this muggle interpretation..." ("crooked_smile", "narrow", "base", "mid")
            gen "Actually, I had this custom-made..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... You did, did you?" ("grin", "narrow", "base", "mid")
            her "Looks like someone's gotten their hands on a particular kind of muggle magazine..." ("crooked_smile", "wink", "base", "mid")
            gen "No idea what you're talking about..." ("base", xpos="far_left", ypos="head")
            gen "Just put it on will you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course [name_genie_hermione], as you wish..." ("base", "narrow", "base", "mid")

    #######################
    ## Lara Croft Outfit ##
    #######################
    elif item == her_outfit_croft: #Req 10 (top, bottom)
        gen "Could you put on this archaeologist outfit for me?" ("base", xpos="far_left", ypos="head")
        her "A what?" ("open", "squint", "base", "mid")
        gen "This one..." ("base", xpos="far_left", ypos="head")
        if states.her.level < 13:
            gen "Worn by the great Lara Croft!" ("base", xpos="far_left", ypos="head")
            her "Someone you know?" ("soft", "base", "base", "mid")
            gen "Indeed... I'm a massive fan." ("base", xpos="far_left", ypos="head")
            gen "(Especially of the fan service...)" ("base", xpos="far_left", ypos="head")
            her "Must be a great woman then, seeing your reaction." ("base", "closed", "base", "mid")
            gen "A great woman indeed! Went cave exploring with her a couple of times..." ("grin", xpos="far_left", ypos="head")
            gen "Good times..." ("base", xpos="far_left", ypos="head")
            her "I wonder why I haven't heard of her..." ("angry", "base", "base", "R")
            her "Well... I suppose I could wear it since you speak so highly of her." ("open", "closed", "base", "mid")
            her "Give me a moment to let me change." ("open", "base", "base", "R")
        elif states.her.level < 22:
            gen "Lara Croft looks stunning in it, so I think you'd probably fill it just as well." ("base", xpos="far_left", ypos="head")
            her "Fill it?" ("angry", "squint", "base", "mid")
            gen "Fit it..." ("base", xpos="far_left", ypos="head")
            her "I guess I'll have to look up this Archaeologist..." ("open", "happy", "base", "R")
            gen "Please do, she's got a lot of material out there for you to enjoy." ("base", xpos="far_left", ypos="head")
            gen "\"Goons raid her\" is one of my favourites." ("base", xpos="far_left", ypos="head")
            her "Sounds fascinating." ("open", "squint", "base", "mid")
            her "Well, hopefully I'll do her clothing justice." ("open", "base", "base", "down")
            her "Just give me a minute to put it on..." ("base", "base", "base", "mid")
        else: #22+
            gen "I'm sure Lara Croft would love to see someone wear her famous outfit." ("base", xpos="far_left", ypos="head")
            gen "Although last time I saw her, she couldn't wait to take it off..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Take it off?" ("open", "squint", "base", "R")
            gen "Indeed... She's quite famous in certain circles, you know." ("base", xpos="far_left", ypos="head")
            gen "Let's just say if you're anyone in the world of archaeology, then you've heard about Lara Croft..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("base", "narrow", "base", "down")
            gen "I'd delve her cavern any--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Okay, okay... Just don't call me Lara once I put it on..." ("clench", "narrow", "base", "mid")

    #######################
    ## Heart Slut Outfit ##
    #######################
    elif item == her_outfit_hslut: #Req 19 (top, panties, bra)
        gen "Put on this burlesque outfit for me, will you?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her @ cheeks blush "A burlesque outfit?" ("open", "base", "base", "mid")
            gen "Yes, this one to be exact..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... {w=0.4} Well, I must say it's quite creative..." ("angry", "narrow", "base", "down")
            gen "You should see those pasties spin..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("clench", "squint", "base", "mid")
            gen "How 'bout it?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright fine... Just give me a moment." ("angry", "squint", "base", "R")
            her @ cheeks blush "" ("angry", "squint", "base", "mid")
        else: #22+
            her @ cheeks blush "A burlesque outfit?" ("angry", "narrow", "base", "down")
            her @ cheeks blush "Strippers wear these, right?" ("open", "closed", "base", "mid")
            gen "Sometimes..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What do you mean sometimes?" ("soft", "narrow", "base", "mid")
            gen "Put it on, and I'll change that answer to a yes..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "How cheeky...{w=0.4} Alright then..." ("base", "narrow", "base", "R")

    #######################
    ## Ms. Marvel Outfit ##
    #######################
    elif item == her_outfit_msmarv: #Req 10 (top, stockings)
        gen "I've got this Cosplay outfit I'd like you to wear." ("base", xpos="far_left", ypos="head")
        if states.her.level < 13:
            her "Cosplay, [name_genie_hermione]?" ("open", "squint", "base", "mid")
            gen "Miss Marvel... One of my favourites!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... Well, I can certainly see why..." ("disgust", "narrow", "base", "down")
            her @ cheeks blush "Alright fine..." ("open", "closed", "worried", "mid")
            her @ cheeks blush "Just give me a moment to change." ("normal", "base", "base", "R")
        elif states.her.level < 22:
            her @ cheeks blush "Cosplay, [name_genie_hermione]?" ("angry", "squint", "base", "mid")
            gen "Yes... A miss Marvel cosplay, to be precise." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I see..." ("soft", "narrow", "base", "down")
            her @ cheeks blush "And why do you want me to wear this cosplay exactly?" ("open", "squint", "base", "R")
            gen "I believe it would enhance your physical traits." ("base", xpos="far_left", ypos="head")
            her "Sorry?" ("annoyed", "squint", "base", "mid")
            gen "You heard me..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Well, I suppose I could put it on..." ("soft", "squint", "base", "R")
            her "One moment please..." ("open", "squint", "base", "mid")
            her "" ("normal", "squint", "base", "mid")
        else: #22+
            her "Cosplay, [name_genie_hermione]?" ("base", "squint", "base", "mid")
            gen "Yes, this Miss Marvel cosplay..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... My nipples are sure to poke through in this..." ("soft", "narrow", "base", "down")
            gen "That's the idea..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well... I guess it can't be helped..." ("open", "closed", "annoyed", "mid")
            her @ cheeks blush "I suppose I'll just... *Ehm*... Suit up..." ("open", "squint", "base", "mid")
            her @ cheeks blush "" ("base", "squint", "base", "mid")

    #################
    ## Tifa Outfit ##
    #################
    elif item == her_outfit_tifa: #Req 10 (top, bottom)
        gen "Could you put on this Tifa Cosplay outfit?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 19:
            her "Cosplay, [name_genie_hermione]?" ("open", "squint", "base", "mid")
            gen "Indeed, a Tifa Lockheart cosplay!" ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Can't say I know who that is..." ("normal", "squint", "base", "R")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "She's from Final Fantasy..." ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("upset", "happy", "base", "mid")
            gen "Sorry... I should've been more specific..." ("base", xpos="far_left", ypos="head")
            gen "Final Fantasy Seven is the one you'd probably know her from." ("base", xpos="far_left", ypos="head")
            her "*Ehm*..." ("clench", "squint", "base", "mid")
            gen "Oh... Come on... it was so good it even got a remake!" ("base", xpos="far_left", ypos="head")
            gen "And let me tell you... They really did a great job on those assets..." ("base", xpos="far_left", ypos="head")
            her "I don't--" ("annoyed", "squint", "base", "mid")
            gen "...{w=0.4} Just put it on will you." ("base", xpos="far_left", ypos="head")
            her "Oh-- Okay..." ("mad", "squint", "base", "mid")
            her "One moment..." ("soft", "squint", "base", "mid")
        else: #19+
            her "A Cosplay outfit..." ("base", "squint", "base", "mid")
            gen "Indeed, none other than the hottest game babe of 1997!" ("base", xpos="far_left", ypos="head")
            her "I see..." ("base", "narrow", "base", "R")
            her "Alright then... Just give me a moment to put it on." ("open", "happy", "base", "mid")

    ##################################
    ## Teddy Outfit (short nightie) ##
    ##################################
    elif item == her_outfit_teddy: #Req 16 (top)
        gen "Could you put on this nightgown?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her @ cheeks blush "This is lingerie..." ("angry", "base", "base", "down")
            gen "Indeed it is..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Isn't this what couples put on to look sexy for their partner?" ("mad", "narrow", "base", "mid")
            gen "I mean..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Sir... I'm doing this to help--" ("open", "closed", "annoyed", "mid")
            gen "Putting this on will help your house." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "How? You're not exactly giving me any points..." ("annoyed", "narrow", "base", "mid")
            gen "No... But it surely aids with the tasks that do..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "base", "base", "mid")
            her @ cheeks blush "Alright, fine..." ("open", "narrow", "base", "R")
            her @ cheeks blush "Just give me a moment to put it on." ("soft", "narrow", "base", "mid")
        else: #22+
            her @ cheeks blush "Lingerie..." ("soft", "narrow", "base", "down")
            gen "Quite observant of you, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well, I suppose if wearing this helps you build up... *Ehm*..." ("open", "closed", "annoyed", "mid")
            gen "No, do finish that sentence please." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What I meant is... If it means I'll be able to finish my tasks faster..." ("annoyed", "squint", "base", "R")
            her @ cheeks blush "Just... I'll just put it on..." ("disgust", "squint", "base", "mid")
            gen "Good plan..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "" ("normal", "squint", "base", "mid")

    ####################
    ## Nightie Outfit ##
    ####################
    elif item == her_outfit_nightie: #Req 13 (top)
        gen "Can you put on this nightie for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 19:
            her @ cheeks blush "This is a nightie is it?" ("clench", "narrow", "base", "down")
            gen "Yep... Completely ordinary nightgown." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Nice try... I can see it's see-through." ("angry", "narrow", "base", "mid")
            gen "Oh... Isn't that what they're like normally?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Sigh*... Whatever... Let's just get this over with..." ("normal", "closed", "annoyed", "mid")
            her @ cheeks blush "" ("normal", "base", "annoyed", "mid")
        elif states.her.level < 22:
            her "A nightie you say?" ("open", "squint", "worried", "mid")
            gen "Indeed." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... Well I suppose I could wear it..." ("normal", "base", "base", "down")
            her @ cheeks blush "Just give me a moment to put it on." ("soft", "base", "base", "mid")
        else: #22+
            her @ cheeks blush "Not much left for the imagination with this one..." ("soft", "narrow", "base", "down")
            gen "I mean... We need you to stay modest, don't we?" ("base", xpos="far_left", ypos="head")
            gen "Can't be having you stand around naked, that'd be shameful!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("normal", "closed", "worried", "mid")
            her @ cheeks blush "Well I better put it on then..." ("open", "closed", "base", "mid")
            her @ cheeks blush "" ("base", "base", "base", "mid")

    #######################
    ## Latex dress Outfit ##
    #######################
    elif item == her_outfit_latex_dress: #Req 19 (top)
        gen "Put on this latex dress for me." ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her @ cheeks blush "A latex dress?" ("open", "squint", "base", "mid")
            her @ cheeks blush "I can't believe you actually want me to wear this..." ("soft", "narrow", "base", "R")
            her @ cheeks blush "Fine...{w=0.4} Here it goes..." ("open", "closed", "annoyed", "mid")
        else: #22+
            her @ cheeks blush "*Hmm*..." ("base", "narrow", "base", "down")
            her @ cheeks blush "And I thought latex gloves were hard to put on..." ("open", "closed", "base", "mid")
            gen "It's worth it if you don't want to get splashed." ("base", xpos="far_left", ypos="head")
            gen "Although maybe you don't mind getting splashed by--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well...{w=0.4} I suppose I could put it on if you really want me to." ("normal", "squint", "annoyed", "mid")
            her @ cheeks blush "One moment...{w=0.4} *Ehm*...{w=0.4} One minute please." ("open", "narrow", "base", "down")

        show screen blkfade
        with d5
        pause .8

        her "Alright... Let's see..."
        her "It's... Quite tight..."
        play sound "sounds/creaking02.ogg"
        pause 1
        her "How am I even supposed to--"
        play sound "sounds/creaking02.ogg"
        pause 1
        her "Alright, I think I got it..."
        play sound "sounds/creaking01.ogg"
        pause 2
        play sound "sounds/slap_04.ogg"
        her "Ouch!"

        hide screen blkfade
        her @ cheeks blush "" ("angry", "squint", "base", "mid")

    #####################
    ## Egyptian Outfit ##
    #####################
    elif item == her_outfit_egypt: #Req 19 (top)
        gen "Put on this Egyptian-themed outfit for me, will you?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "Why am I suspecting this is not your ordinary--" ("open", "closed", "worried", "mid")
            gen "Here you go..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "squint", "base", "down")
            her @ cheeks blush "Why am I not surprised..." ("open", "narrow", "base", "mid")
            her "Sir, do you actually believe they wear this in Egypt?" ("angry", "narrow", "base", "R")
            gen "Of course I do... Quite fashionable when I was there." ("base", xpos="far_left", ypos="head")
            gen "I even had a pair of those wristbands myself..." ("base", xpos="far_left", ypos="head")
            gen "Couldn't force myself to take them off!" ("base", xpos="far_left", ypos="head")
            her "Alright... I guess I'll wear it..." ("open", "closed", "worried", "mid")
            her "One moment..." ("soft", "squint", "base", "mid")
        else: #22+
            her "Egyptian-themed, you say?" ("soft", "happy", "base", "mid")
            gen "Yeah, this one right here..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I see..." ("normal", "happy", "base", "down")
            gen "Cleopatra wore this quite proudly, I'll have you know..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("soft", "closed", "worried", "mid")
            her "Well, I wouldn't want to displease the great Cleopatra..." ("normal", "base", "base", "R")
            her @ cheeks blush "Hopefully I'll do it justice..." ("open", "squint", "base", "mid")
            her @ cheeks blush "One moment please..." ("base", "base", "base", "mid")

    ##############
    ## Swimsuit ##
    ##############
    elif item == her_outfit_swimsuit: #Req 13 (top)
        gen "I've got this swimsuit I'd like you to wear." ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "A swimsuit..." ("open", "squint", "base", "mid")
            her "I guess I could put it on." ("soft", "narrow", "base", "R")
            her "Although, it's a bit weird as I assume I'm not going swimming..." ("disgust", "closed", "worried", "mid")
            gen "I'm sure we can find a way to get it wet no problem..." ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "wide", "base", "mid")
            her @ cheeks blush "Why I'm not quite sure what you mean by that..." ("open", "closed", "base", "mid")
            her @ cheeks blush "But if I'm expected to put it on for the sake of--" ("soft", "closed", "base", "mid")
            gen "Just put it on, will you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ahem*...{w=0.4} Okay then." ("clench", "narrow", "base", "R")
            her @ cheeks blush "Just give me a moment..." ("open", "squint", "base", "mid")
        else: #22+
            her @ cheeks blush "A swimsuit..." ("open", "base", "base", "R")
            her @ cheeks blush "Are you expecting me to get wet today?" ("open", "closed", "base", "mid")
            gen "Can never be too careful..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well... If that's the case, then I better put it on..." ("open", "narrow", "base", "R")

    #####################
    ## Bioshock Outfit ##
    #####################
    elif item == her_outfit_bioshock: #Req 14 (no bra)
        gen "Can you put on this Elisabeth Cosplay outfit?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 18:
            her "A cosplay outfit?" ("open", "base", "base", "mid")
            gen "Yep... Ever heard of her?" ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Can't say that I have." ("upset", "squint", "base", "mid")
            gen "She's from a video--" ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "mid")
            gen "I mean... She's a famous, *ugh*... Witch?" ("base", xpos="far_left", ypos="head")
            her "..." ("base", "base", "base", "mid")
            gen "(Phew, that was close...)" ("base", xpos="far_left", ypos="head")
            her "A corset!" ("clench", "wide", "worried", "down")
            gen "*Uh-oh*..." ("base", xpos="far_left", ypos="head")
            her "Aren't these supposed to make it really hard to breathe?" ("angry", "closed", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Have you seen your waste-line?" ("base", xpos="far_left", ypos="head")
            gen "A corset is hardly going to hinder you from breathing..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "closed", "base", "mid")
            her @ cheeks blush "I guess that's true." ("open", "happy", "base", "R")
            gen "Great... So, no complaints then?" ("base", xpos="far_left", ypos="head")
            her "*Hmm*... I suppose not..." ("angry", "closed", "base", "mid")
            her "..." ("normal", "base", "base", "R")
            gen "So... Are you putting it on?" ("base", xpos="far_left", ypos="head")
            her "Oh...{w=0.4} Alright..." ("angry", "squint", "base", "mid")
            her "" ("base", "squint", "base", "mid")
        elif states.her.level < 22:
            her "A cosplay..." ("open", "squint", "base", "mid")
            her "*Hmm*... I like the necklace." ("soft", "squint", "base", "L")
            gen "I like the corset!" ("base", xpos="far_left", ypos="head")
            her "Of course you do..." ("normal", "closed", "base", "mid")
            her "Alright, I suppose I can put it on..." ("soft", "base", "base", "R")
            gen "Wait a second, they forgot the coin purse!" ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("upset", "squint", "base", "mid")
            gen "There's supposed to be a coin purse for you to store silver coins in..." ("base", xpos="far_left", ypos="head")
            her "Oh... So, you don't want me to wear it?" ("angry", "squint", "base", "mid")
            gen "Of course I do... You'll just have to store the coins in a pocket or something..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... There doesn't seem to be any pockets..." ("upset", "narrow", "base", "down")
            gen "Well... I'm sure you'll find somewhere to put them." ("base", xpos="far_left", ypos="head")
            her "Right..." ("disgust", "narrow", "base", "down")
            her @ cheeks blush "Well... Let's see if I can get into this corset to start with..." ("angry", "squint", "base", "R")
            her "" ("base", "squint", "base", "mid")
        else: #22+
            her "A cosplay..." ("open", "squint", "base", "mid")
            gen "Indeed... And she's quite the popular one as well..." ("base", xpos="far_left", ypos="head")
            gen "You should see what zone did with her..." ("base", xpos="far_left", ypos="head")
            her "Who?" ("soft", "squint", "base", "mid")
            gen "*Err*... I meant, you should see the zone she's--" ("base", xpos="far_left", ypos="head")
            gen "What I meant to say was..." ("base", xpos="far_left", ypos="head")
            gen "Just... Put it on, will you?" ("base", xpos="far_left", ypos="head")
            her "Alright." ("grin", "narrow", "base", "R")
            her "" ("base", "squint", "base", "mid")

    #####################
    ## Yennefer Outfit ##
    #####################
    elif item == her_outfit_yennefer: #Req 10
        gen "I got this Yennefer Cosplay that I'd like you to put on." ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "Who?" ("normal", "squint", "base", "mid")
            gen "*Sigh*...{w=0.4}  Yennefer... {w=0.4} From the witcher." ("base", xpos="far_left", ypos="head")
            her "Oh...{w=0.4}  Her..." ("open", "squint", "base", "R")
            her "(No clue who that is, but I better not offend him...)" ("normal", "narrow", "base", "down")
            gen "(I guess she picked Triss.)" ("base", xpos="far_left", ypos="head")
            her "You... Like this Yennefer character, then?" ("clench", "squint", "base", "mid")
            gen "(She did pick Triss!)" ("base", xpos="far_left", ypos="head")
            gen "I mean... Shouldn't I?" ("base", xpos="far_left", ypos="head")
            gen "(I only did the one playthrough... Maybe Triss was the right choice... Should I have save scummed--)" ("base", xpos="far_left", ypos="head")
            her "*Err*... No, you definitely should..." ("open", "squint", "base", "R")
            gen "..." ("base", xpos="far_left", ypos="head")
            her "..." ("clench", "narrow", "base", "L")
            her "I'll just put it on shall I?" ("angry", "closed", "base", "mid")
            gen "*Err*... Yes... You do that..." ("base", xpos="far_left", ypos="head")
            her "Okay then." ("base", "closed", "base", "down")
            her "" ("base", "base", "base", "down")
        else: #22+
            her "This is quite the intricate outfit..." ("angry", "narrow", "base", "down")
            gen "A Classy outfit for a classy lady." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... Well, thank you..." ("base", "closed", "base", "mid")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            gen "Oh... Yes, put it on for me, will you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "As you wish." ("open", "squint", "base", "R")
            her @ cheeks blush "One moment..." ("base", "squint", "base", "mid")

    ################
    ## Ball Dress ##
    ################
    elif item == her_outfit_ball: #Req 14 (no bra) (ball happens on lvl 15)
        if not states.her.ev.yule_ball.e4_complete:
            gen "Could you put on this dress?" ("base", xpos="far_left", ypos="head")
            her "*Hmm*... This looks expensive..." ("soft", "squint", "base", "down")
            gen "I had it custom-made!" ("base", xpos="far_left", ypos="head")
            gen "(As if my other purchases haven't been...)" ("base", xpos="far_left", ypos="head")
            her "I do like a pearl necklace..." ("soft", "narrow", "base", "down")
            gen "I knew it... Well, I'm always happy to give you one, as long as you don't tell anyone about it." ("base", xpos="far_left", ypos="head")
            gen "We wouldn't want anyone to know the headmaster gave a student a pearl necklace, do we?" ("base", xpos="far_left", ypos="head")
            her "Of course." ("open", "closed", "base", "mid")
            her "Well, let's put it on then..." ("soft", "happy", "base", "mid")
            her @ cheeks blush "" ("base", "happy", "base", "mid")
        else:
            gen "What did Hermione Granger say when she got to the ball?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "{size=-4}This dress...{/size}" ("soft", "narrow", "base", "down")
            gen "*Gag* *Cough* *Cough*" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("base", "narrow", "base", "down")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Well, I thought it was funny..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("base", "narrow", "base", "down")
            gen "Miss Granger?" ("base", xpos="far_left", ypos="head")
            gen "(Looks like she's zoned out...)" ("base", xpos="far_left", ypos="head")
            gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Huh*?" ("angry", "squint", "base", "mid")
            her @ cheeks blush "Oh... Sorry sir, let me just put it on..." ("open", "base", "base", "R")
            gen "Never mind the dress, what about my joke?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Sorry?" ("soft", "base", "base", "mid")
            gen "...{w=0.4} Whatever... Just put it on..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright." ("base", "base", "base", "mid")

    ##################
    ## Bunny Outfit ##
    ##################
    elif item == her_outfit_bunny: #Req 19 (top, stockings)
        gen "I've got this bunny costume I'd like you to wear." ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "A bunny costume?" ("soft", "squint", "base", "mid")
            her "Where do you even get these ideas from?" ("angry", "narrow", "base", "stare")
            gen "In some junk mail, showing a mansion full of attractive and scantily clad women." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I see..." ("soft", "closed", "base", "mid")
            her @ cheeks blush "It does look a little bit tight, but I suppose I'll wear it for you..." ("open", "narrow", "base", "down")
            gen "(Hugh success!)" ("grin", xpos="far_left", ypos="head") #Like Hugh Hefner
        else: # 22+
            her @ cheeks blush "A bunny costume?" ("open", "base", "base", "mid")
            gen "I thought we could get it on like rabbits." ("base", xpos="far_left", ypos="head")
            her "*Huh*? Get what on?" ("annoyed", "squint", "base", "mid")
            gen "*Heh-heh*... You know..." ("grin", xpos="far_left", ypos="head")
            her "..." ("annoyed", "base", "base", "mid")
            her @ cheeks blush "..." ("annoyed", "squint", "base", "stare")
            gen "(She knows...)" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Sir, I'm--" ("open", "closed", "base", "mid")
            gen "Just put the thing on." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright..." ("open", "narrow", "base", "down")

    ######################
    ## Reindeer Costume ##
    ######################
    elif item == her_outfit_reindeer: #Req 19 (top, stockings)
        gen "I've got this reindeer costume for you to wear." ("base", xpos="far_left", ypos="head")
        her "You want me to dress up like a reindeer?" ("soft", "base", "base", "mid")
        gen "Of course, 'Tis the season, after all." ("base", xpos="far_left", ypos="head")
        her "I just thought that you'd want me to wear something... You know..." ("annoyed", "base", "base", "R")
        gen "Here's the costume." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh, Now it makes sense..." ("open", "narrow", "base", "down")
        gen "So you'll wear it?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "If wearing it is what you want me to do..." ("soft", "narrow", "base", "R")
        gen "Yes please!" ("base", xpos="far_left", ypos="head")

    ###############################
    ## Poker Outfit (token shop) ##
    ###############################
    elif item == her_outfit_poker: #Req 19 (panties, bra)
        gen "I spent some tokens getting this outfit for you..." ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her @ cheeks blush "Whoa..." ("soft", "narrow", "base", "down")
            gen "I know... Quite intricate, is it not?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You... you want me to wear this?" ("normal", "closed", "base", "mid")
            gen "I mean, I am a winner after all..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... I'm not so sure about that..." ("soft", "narrow", "base", "R")
            gen "Sounds like jealousy to--" ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "mid")
            gen "*Ahem*... Just put it on, will you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "...{w=0.4} Fine." ("base", "narrow", "base", "R")
        else: #22+
            her "You won this did you?" ("open", "narrow", "base", "down")
            gen "Indeed." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "How do I know you didn't just have it made for me?" ("open", "narrow", "base", "mid")
            gen "You think I'd be able to come up with something like this?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "narrow", "base", "R")
            gen "Okay... I probably would..." ("base", xpos="far_left", ypos="head")
            gen "You're just going to have to trust me on this one..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... Well then, it'd be a shame if the prize went to waste..." ("base", "narrow", "base", "mid")
            her @ cheeks blush "Just give me a moment to put it on..." ("open", "base", "base", "mid")

    #################
    ## Maid Outfit ##
    #################
    elif item == her_outfit_maid: #Req 4
        gen "Could you put on this maid's outfit?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 13:
            her "You want me to clean your office now too?" ("clench", "narrow", "base", "mid")
            gen "Well... Let's just have you wear the outfit for now..." ("base", xpos="far_left", ypos="head")
            her "*Ugh*... Maid's outfits are so silly..." ("disgust", "narrow", "base", "mid")
            her "Well... Here it goes, I guess..." ("disgust", "narrow", "base", "R")
        elif states.her.level < 22:
            her "*Hmm*..." ("upset", "narrow", "base", "down")
            her @ cheeks blush "I presume your reason for wanting me to put it on isn't related to cleaning..." ("open", "narrow", "base", "mid")
            gen "I mean..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Figured..." ("open", "closed", "worried", "mid")
            her @ cheeks blush "Oh... Well, I guess it can't be helped..." ("soft", "narrow", "base", "down")
            her @ cheeks blush "One moment please..." ("open", "narrow", "base", "mid")
        else: #22+
            her @ cheeks blush "*Hmm*... Is it one of those \"Sexy\" maid's outfits?" ("soft", "narrow", "base", "down")
            gen "It depends..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What is that supposed to mean?" ("clench", "squint", "base", "mid")
            gen "It depends on who wears it... I think I'd be able to make a judgment whilst seeing you with it on." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Charmed...{w} Alright, just let me get changed, so we can find out..." ("base", "narrow", "base", "R")
            her @ cheeks blush "" ("base", "squint", "base", "mid")

    #########################
    ## Sling Bikini Outfit ##
    #########################
    elif item == her_outfit_bikini3: #Req 17 (panties, bra)
        gen "Put on this bikini for me will you?" ("base", xpos="far_left", ypos="head")
        her "*Hmm*... A bikini, you say?" ("normal", "narrow", "base", "R")
        gen "Yep, this one right here..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Right...{w} Why would I even expect something normal?" ("angry", "narrow", "base", "down")
        gen "Looks normal to me..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "It's held up by chains, How is that normal to you?" ("disgust", "narrow", "base", "mid")
        gen "I mean, perhaps you wouldn't see it at the beach exactly..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Then where would you?" ("normal", "narrow", "base", "R")
        gen "A strip--{w=0.3} I mean... The Vegas strip!" ("base", xpos="far_left", ypos="head")
        her "They wear these on the Vegas strip do they?" ("open", "narrow", "annoyed", "mid")
        gen "Of course, it's pretty hot there so why wouldn't--" ("base", xpos="far_left", ypos="head")
        her "You're lying..." ("open", "closed", "annoyed", "mid")
        gen "What?!" ("angry", xpos="far_left", ypos="head")
        gen "(She's seen through my clever ruse... Impossible!)" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush "Give me the real reason why you want me to wear this." ("upset", "base", "annoyed", "mid")
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "The \"real\" reason... Or I'm not putting it on..." ("angry", "narrow", "base", "mid")
        gen "The--" ("base", xpos="far_left", ypos="head")
        gen "(Hold on... This isn't in the script...)" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I'm waiting..." ("annoyed", "closed", "annoyed", "mid")
        gen "One moment..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/pageflip.ogg"
        gen "(Alright, let's see what's going on here...)" ("base", xpos="far_left", ypos="head")
        play sound "sounds/pageflip.ogg"
        gen "(\"Genie fights Snape using magic... #TODO add explanation to this later...\")" ("base", xpos="far_left", ypos="head")
        gen "(That's the tutorial, so it must be further in...)" ("base", xpos="far_left", ypos="head")
        play sound "sounds/pageflipback.ogg"
        gen "(Genie fucks Hermione in the Ass...)" ("base", xpos="far_left", ypos="head")

        if states.her.status.anal:
            gen "(*Heh-heh*... Why am I not doing this right now, exactly?)" ("base", xpos="far_left", ypos="head")
        else:
            gen "(Whops... Spoilers...)" ("base", xpos="far_left", ypos="head")

        gen "(*Hmm*... I've gone too far... Well... In the script at least.)" ("base", xpos="far_left", ypos="head")
        play sound "sounds/pageflip.ogg"
        pause .3
        play sound "sounds/pageflip.ogg"
        pause .3
        play sound "sounds/pageflip.ogg"
        pause .3
        gen "(There we go... The wardrobe section...)" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Still waiting... I'm going to need a real reason soon, or I'm not putting it on..." ("angry", "closed", "annoyed", "mid")
        gen "(*Aha*! I knew it!)" ("grin", xpos="far_left", ypos="head")
        gen "(Genie comes up with another bullshit reason... Hermione thinks for a moment and then accepts it as the truth!)" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Three...{w=1} Two--" ("open", "closed", "annoyed", "mid")
        gen "Wait a minute, the script says--" ("angry", xpos="far_left", ypos="head")
        her "One..." ("open", "narrow", "annoyed", "mid")
        gen "*Err*... Your tits would look great in it!" ("angry", xpos="far_left", ypos="head")
        her "...{w} Well then..." ("base", "narrow", "annoyed", "mid")
        gen "(Ah fuck... I can't believe she's done this...)" ("base", xpos="far_left", ypos="head")
        her "In that case--" ("open", "closed", "annoyed", "mid")
        play sound "sounds/magic4.ogg"
        with kissiris
        her "..." ("normal", "base", "base", "stare")
        gen "What the..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "They wear these on the Vegas strip do they?" ("open", "base", "base", "mid")
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Hmm*... Well, I suppose I'll put it on then..." ("grin", "closed", "base", "mid")
        gen "(What just...)" ("base", xpos="far_left", ypos="head")
        gen "(*Hmm*... The developers must've patched it...{w=0.4} There's my immersion ruined...)" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Just give me a moment..." ("open", "base", "base", "mid")
        her @ cheeks blush "" ("base", "base", "base", "mid")

    ###########################
    ## Leather Bikini Outfit ##
    ###########################
    elif item == her_outfit_bikini2: #Req 16 (panties, bra)
        gen "Put on this bikini for me." ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "What kind of bikini are we talking about?" ("open", "narrow", "base", "mid")
            gen "This leather one here." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("open", "narrow", "base", "down")
            her @ cheeks blush "Well I guess it has some coverage..." ("normal", "narrow", "base", "down")
            gen "I'm sure I could adjust it to be smaller if you'd like." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Err*... No, it's fine... I'll just put it on as is..." ("angry", "closed", "base", "mid")
            gen "You sure? Just say the word, and I'll have it--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "No, we're good. Just give me a moment to put it on." ("open", "squint", "worried", "R")
        else: # 22+
            her @ cheeks blush "A bikini?" ("open", "squint", "base", "R")
            gen "Yep, I've got this leather one for you to wear today." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "A leather bikini in the headmaster's office..." ("base", "narrow", "base", "down")
            gen "That's right..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... One moment please..." ("open", "squint", "base", "mid")


    ########################
    ## Rave Bikini Outfit ##
    ########################
    elif item == her_outfit_bikini1: #Req 18 (panties, bra)
        gen "I've got this bikini for you to wear today." ("base", xpos="far_left", ypos="head")
        her "A bikini?" ("open", "base", "base", "mid")
        gen "Yep... This one right here." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "This is supposed to be a bikini is it?" ("open", "narrow", "base", "down")
        gen "Should fall within that definition, yes." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "And here I thought bikinis were supposed to protect your modesty..." ("open", "closed", "base", "mid")
        gen "(Your modesty went out the window a long time ago.)" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well... I suppose it does cover the important bits..." ("soft", "narrow", "base", "down")
        gen "(Is she trying to convince herself out of it or the other way around?)" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Just give me a moment to put it on, [name_genie_hermione]..." ("normal", "narrow", "base", "R")

    ################################
    ## Pizza Slut Outfit (mirror) ##
    ################################
    elif item == her_outfit_pizza: #Req 19 (top, panties)
        gen "Put this pizza on." ("base", xpos="far_left", ypos="head")
        her "Put it--" ("annoyed", "squint", "base", "mid")
        her "..." ("angry", "squint", "base", "mid")
        her "Where did you even get something like this?" ("disgust", "narrow", "base", "mid")
        her "It's not real pizza, right?" ("angry", "narrow", "base", "mid")
        gen "It materialized from a dream." ("base", xpos="far_left", ypos="head")
        her "It did what from where?" ("mad", "happy", "base", "mid")
        gen "Yeah, better not question it..." ("base", xpos="far_left", ypos="head")
        her "But sir, conjuring food breaks the laws of transfiguration!" ("open", "squint", "base", "mid")
        gen "What counts as food, really?" ("base", xpos="far_left", ypos="head")
        her "What?" ("disgust", "base", "base", "mid")
        gen "If you put it on your body then it's not food... it's clothes." ("base", xpos="far_left", ypos="head")
        gen "It's the intention of use that matters..." ("base", xpos="far_left", ypos="head")
        her "I'm not sure that's how it works..." ("open", "narrow", "base", "R")
        gen "..." ("base", xpos="far_left", ypos="head")
        her "..." ("annoyed", "squint", "base", "mid")
        her "Don't question it?" ("open", "narrow", "base", "mid")
        gen "Don't question it." ("base", xpos="far_left", ypos="head")
        gen "Now, are you putting on these clothes for me or what?" ("base", xpos="far_left", ypos="head")
        her "*Hmm*..." ("annoyed", "narrow", "base", "down")
        her "I guess I could do it, using a sticking charm..." ("angry", "narrow", "base", "R")
        gen "What's a stick going to--" ("base", xpos="far_left", ypos="head")

        # Equips the item early.
        play sound "sounds/magic4.ogg"
        $ hermione.equip(item)

        her "Expoximise!" ("scream", "happy", "base", "mid", trans=flashbulb)
        her "" ("normal", "happy", "base", "mid")

    ###################
    ## Ribbon Outfit ##
    ###################
    elif item == her_outfit_ribbon: #Req 18 (bra, panties)
        gen "I've got this thing that I'd like you to wrap for me." ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "Is it me?" ("open", "narrow", "base", "mid")
            gen "When did you become so good at guessing?" ("angry", xpos="far_left", ypos="head")
            her "It wasn't exactly hard..." ("annoyed", "narrow", "base", "mid")
            gen "It could be if you put these ribbons on." ("grin", xpos="far_left", ypos="head")
            her "*Ugh*..." ("disgust", "narrow", "base", "mid")
            her @ cheeks blush "Alright, fine... Just don't tug at the ends." ("open", "narrow", "base", "R")
            gen "Of course..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "One moment..." ("open", "narrow", "base", "mid")
        else: # 22+
            her @ cheeks blush "Alright, let me just take my clothes off..." ("angry", "narrow", "base", "R")
            gen "I didn't say it was you!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "It's not?" ("clench", "squint", "base", "mid")
            gen "...{w=0.4} Alright, it is..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Okay then, just give me a--" ("open", "closed", "base", "mid")
            gen "Wrap it tight!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Very well..." ("open", "squint", "base", "R")
    ######################
    ## Christmas Outfit ##
    ######################
    elif item == her_outfit_xmas: #Req 13 (top, bottom)
        gen "I'm feeling festive today so could you put on the Christmas outfit?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 22:
            her "A Christmas--" ("open", "squint", "base", "mid")
            her @ cheeks blush "Right..." ("soft", "narrow", "base", "down")
            gen "Specifically designed to jingle some balls." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Charming..." ("open", "narrow", "base", "R")
            her @ cheeks blush "Is this really what you imagine a proper Christmas-themed outfit is?" ("angry", "narrow", "base", "down")
            gen "I mean... Mrs Claus probably doesn't wear it... Although she probably should." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Why would I even ask..." ("disgust", "closed", "base", "mid")
            gen "Because if she did, then Santa would probably come more than once a--" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Fine!" ("clench", "narrow", "base", "mid")
            gen "I wasn't finished..." ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "I'll put it on..." ("open", "narrow", "base", "R")
            gen "But... My joke..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "" ("base", "narrow", "base", "mid")
        else: #22+
            her @ cheeks blush "Looks a bit naughty--" ("soft", "narrow", "base", "down")
            gen "Yet I'm sure Santa would put you on the good list if you wore it..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... I doubt that..." ("base", "narrow", "base", "R")
            her @ cheeks blush "Well... I'm doing this to make my house happy, so surely it'd even out." ("open", "closed", "base", "mid")
            gen "I'm sure it will." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Just give me a moment to put it on..." ("base", "narrow", "base", "mid")

    #####################
    ## Wrestling Robes ##
    #####################
    elif item == her_outfit_wrestling: #Req 3 (robe, bra, panties, misc)
        gen "I've got these wrestling robes for you to wear today." ("base", xpos="far_left", ypos="head")
        if states.her.level < 13:
            her "Wrestling robes?" ("soft", "base", "base", "mid")
            her "Why do you want me to wear wrestling robes, exactly?" ("disgust", "narrow", "base", "mid")
            gen "Wrestle obviously, let me just call for your opponent." ("base", xpos="far_left", ypos="head")
            her "What?!" ("mad", "wide", "base", "mid")
            gen "No, while that would be fun, I'd just like you to wear it." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "base", "mid")
            her "Alright, as long as you don't make me wrestle..." ("open", "narrow", "base", "mid")
        else: #13+
            her "Wrestling robes?" ("soft", "base", "base", "mid")
            gen "Yeah, although you'd take them off when you actually start wrestling." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You're not trying to trick me into doing mud wrestling are you?" ("disgust", "narrow", "base", "mid")
            gen "Well now that you bring it up..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Never mind, forget I said it!" ("angry", "happy", "base", "mid")
            her @ cheeks blush "Just let me put these on..." ("soft", "narrow", "base", "down")
            her @ cheeks blush "" ("soft", "narrow", "base", "mid")
    # TODO: Blacklist fallbacks have to be added.
    return

label her_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.

    ########################
    ## Cheerleader Normal ##
    ########################
    if item == her_outfit_cheerleader_1: #Req 10 whoring
        gen "Could you wear the cheerleader outfit for me?" ("base", xpos="far_left", ypos="head")

        her "Cheerleader outfit?" ("upset", "base", "base", "mid")
        her "Sir, I am not some floozy cheerleader..." ("open", "closed", "base", "mid")
        her "Their attire shows way too much skin for my liking..." ("open", "squint", "base", "R")
        gen "Come on, it's just your stomach..." ("base", xpos="far_left", ypos="head")
        her "Sorry [name_genie_hermione] but I'll have to decline..." ("normal", "squint", "base", "mid")

    ######################
    ## Cheerleader Lewd ##
    ######################
    elif item == her_outfit_cheerleader_2: #Req 16 whoring (top)
        gen "Could you put on the cheerleader outfit for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 10:
            her "Cheerleader outfit?" ("upset", "base", "base", "mid")
            her "Sir, I am not some floozy cheerleader..." ("open", "closed", "base", "mid")
            her "Their attire shows way too much skin for my liking..." ("open", "squint", "base", "R")
            gen "Come on, surely it's not that bad." ("base", xpos="far_left", ypos="head")
            her "Sorry [name_genie_hermione] but I'll have to decline..." ("normal", "squint", "base", "mid")
        else: # < 16
            her "Of course!" ("smile", "happyCl", "base", "mid")
            her "Go-Go Gryffindor!" ("grin", "squint", "base", "mid")
            gen "Here you go!" ("base", xpos="far_left", ypos="head")
            her "What on earth..." ("clench", "squint", "base", "down")
            her "Sir, this is not the official cheerleading attire!" ("angry", "closed", "base", "mid")
            gen "Oh... I could've sworn it was..." ("base", xpos="far_left", ypos="head")
            her "I am not wearing this..." ("disgust", "base", "base", "R")

    #################
    ## Fishnet Outfit
    #################
    elif item == her_outfit_fishnet: #Req 19 (panties, top)
        gen "Could you please wear--" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "What? Oh, what's this?" ("soft", "squint", "base", "L")
            gen "It's a fishnet--" ("base", xpos="far_left", ypos="head")
            her "Oh, I get it!" ("open", "wide", "base", "mid")
            her "This isn't really a hobby I considered pursuing, [name_genie_hermione]..." ("open", "closed", "base", "mid")
            her "But if you say it will help me with my grades, then I'll try my best." ("smile", "squint", "base", "mid")
            gen "Wait what?" ("base", xpos="far_left", ypos="head")
            her "I will go down to the lake later and try it out, if that's okay with you, [name_genie_hermione]." ("open", "base", "base", "R")
            gen "(...)" ("base", xpos="far_left", ypos="head")
            gen "(Wait, does she want to go fishing with it...?)" ("base", xpos="far_left", ypos="head")
        elif states.her.level < 10:
            her "What on earth... This top is so revealing!" ("angry", "wide", "angry", "mid")
            gen "Yes, glad you noticed! Now if you don't mind just--" ("grin", xpos="far_left", ypos="head")
            her "I'm not going to wear it! You can see everything in this! My nipples would poke right through it!!!" ("scream", "base", "angry", "mid")
            gen "I wouldn't mind if they did..." ("base", xpos="far_left", ypos="head")
            her "That's just... typical!" ("clench", "base", "angry", "R")
            her "You disgust me, [name_genie_hermione]!" ("disgust", "base", "angry", "mid")
            gen "Alright-- Yeesh... Forget I said anything." ("base", xpos="far_left", ypos="head")
        else: # < 19
            her "A fishnet outfit?" ("angry", "happy", "base", "mid")
            gen "Indeed!" ("base", xpos="far_left", ypos="head")
            her "I didn't know they made bottoms like this!" ("disgust", "base", "base", "down")
            gen "They don't usually... I had it made custom just for you!" ("base", xpos="far_left", ypos="head")
            her "You did, did you?" ("open", "narrow", "base", "mid")
            gen "Yes, so if you could just--" ("base", xpos="far_left", ypos="head")
            if states.her.level < 13:
                her "Well, that's too bad because I won't be wearing it..." ("disgust", "base", "base", "R")
            else:
                her "This is practically fetish gear, [name_genie_hermione]..." ("soft", "happy", "base", "mid")
                gen "I mean..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I am not wearing something like this..." ("open", "base", "base", "R")

    ######################
    ## Fishnet One-Piece ##
    ######################
    elif item == her_outfit_fishnet_onepiece: #Req 19 (top)
        gen "Could you put on the fishnet one-piece for me?" ("base", xpos="far_left", ypos="head")
        her "The what?" ("angry", "squint", "base", "mid")
        if states.her.level < 4:
            her "What on earth is this!?" ("scream", "base", "angry", "down")
            gen "Fishnet... One-piece?" ("base", xpos="far_left", ypos="head")
            her "Are you actually expecting me to wear this?" ("angry", "base", "angry", "mid")
            gen "*Err*... No, I wanted to have you convert it into a fishnet for me!" ("angry", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "annoyed", "mid")
            her "You literally just asked me to put it on..." ("open", "base", "annoyed", "mid")
            gen "Oh... Did I?" ("angry", xpos="far_left", ypos="head")
            her "Yes..." ("upset", "base", "angry", "mid")
            gen "So..." ("base", xpos="far_left", ypos="head")
            her "No!" ("angry", "base", "angry", "mid")
        elif states.her.level < 10:
            her "Fishnet--" ("soft", "narrow", "base", "down")
            her "Sir, I am not wearing something so..." ("angry", "base", "base", "down")
            gen "Glamorous?" ("base", xpos="far_left", ypos="head")
            gen "Enchanting?" ("base", xpos="far_left", ypos="head")
            gen "Alluring?" ("base", xpos="far_left", ypos="head")
            her "Revealing..." ("annoyed", "base", "annoyed", "mid")
            gen "Right, was just about to say that one." ("base", xpos="far_left", ypos="head")
            gen "Just think of yourself as a fish inside a--" ("base", xpos="far_left", ypos="head")
            her "No... Just... No..." ("disgust", "base", "annoyed", "R")
        else: # < 19
            her @ cheeks blush "This is Lingerie!" ("angry", "narrow", "base", "down")
            gen "Well spotted!" ("base", xpos="far_left", ypos="head")
            gen "Now if you could just--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am not putting on lingerie for you..." ("angry", "closed", "base", "mid")

    ##################
    ## Latex Outfit ##
    ##################
    elif item == her_outfit_latex: #Req 19 (top)
        gen "Could you put on this latex outfit for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 10:
            her "Latex--" ("soft", "happy", "base", "mid")
            her "Sir, you can't be serious!" ("angry", "wide", "annoyed", "mid")
            gen "I'm not hearing a no." ("base", xpos="far_left", ypos="head")
            her "I can't believe I'd even have to--" ("clench", "squint", "angry", "mid")
            her "No! I am not putting on this disgusting--" ("scream", "closed", "angry", "mid")
            gen "Alright, Alright... A simple \"no\" would've sufficed..." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "base", "angry", "mid")
        elif states.her.level < 13:
            her "Latex?" ("open", "wide", "base", "mid")
            her "You actually expect me to wear something like this?" ("clench", "base", "annoyed", "mid")
            gen "I don't see why not. You're perfectly fine being naked." ("base", xpos="far_left", ypos="head")
            her "But this..." ("disgust", "narrow", "base", "down")
            her "This would make me look like some cheap--" ("disgust", "narrow", "annoyed", "down")
            gen "Alright, fine... Don't wear it then..." ("base", xpos="far_left", ypos="head")
        else: # < 19
            her "Latex?" ("angry", "squint", "base", "mid")
            her "How do you even put this on?" ("disgust", "narrow", "annoyed", "down")
            gen "No clue, although I'd assume it's no different to a condom..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "wide", "base", "mid")
            her @ cheeks blush "Yeah, I'm not putting this on..." ("open", "closed", "annoyed", "mid")
            gen "Did I say condom? I meant... *Err*..." ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("upset", "base", "base", "R")
            gen "Fine... Never mind then..." ("base", xpos="far_left", ypos="head")

    #######################
    ## Slutty Schoolgirl ##
    #######################
    elif item == her_outfit_slutty_schoolgirl: #Req 19 (top, Bottom)
        gen "Could you put on this school uniform for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "Most certainly... The school uniform is a staple within this institution, and I'll wear it with--" ("open", "closed", "base", "mid")
            gen "Here you go." ("base", xpos="far_left", ypos="head")
            her "Pride..." ("normal", "squint", "base", "down")
            her "What have you done?!" ("shock", "wide", "base", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It's cut all weird... Wait, what's wrong with this skirt?" ("clench", "base", "base", "down")
            gen "You like it?" ("base", xpos="far_left", ypos="head")
            her "What do you mean do I like it?" ("scream", "happy", "angry", "mid")
            gen "I knew you would--" ("base", xpos="far_left", ypos="head")
            her "You've desecrated our school uniform!" ("mad", "base", "angry", "mid")
            gen "..." ("angry", xpos="far_left", ypos="head")
            her "I shall not put on this... this--" ("angry", "base", "angry", "down")
            gen "Alright fine..." ("base", xpos="far_left", ypos="head")
        elif states.her.level < 13:
            her "Why would you..." ("clench", "squint", "base", "down")
            gen "What?" ("base", xpos="far_left", ypos="head")
            her "This is...{w=0.4} You've completely ruined our school uniform!" ("angry", "happyCl", "angry", "mid")
            gen "I have?" ("angry", xpos="far_left", ypos="head")
            gen "Looks like an improvement to me..." ("base", xpos="far_left", ypos="head")
            her "I am not putting this on... It's an insult to our school!" ("clench", "base", "angry", "R")
            gen "(Looks like I crossed some arbitrary line with this one...)" ("base", xpos="far_left", ypos="head")
        else: # < 19
            her "This..." ("angry", "base", "base", "down")
            gen "I know it's great isn't it?" ("base", xpos="far_left", ypos="head")
            her "This..." ("mad", "narrow", "base", "down")
            her "Why would you do this to our school uniform?" ("soft", "closed", "base", "mid")
            her @ cheeks blush "The students wear this with pride... It's a staple of our great institution." ("normal", "squint", "base", "mid")
            her @ cheeks blush "And you've turned it into--" ("upset", "narrow", "base", "down")
            gen "I know... Quite an improvement, isn't it?" ("grin", xpos="far_left", ypos="head")
            her "I'm sorry, but I am not putting this on, [name_genie_hermione]..." ("open", "closed", "base", "mid")
            gen "Suit yourself..." ("base", xpos="far_left", ypos="head")

    ##################
    ## Witch Outfit ##
    ##################
    elif item == her_outfit_witch: #Req 10 (top)
        gen "Put on this witch outfit for me will you?" ("base", xpos="far_left", ypos="head")
        her "A witch outfit?" ("soft", "base", "base", "mid")
        her "Sir, I'm not sure..." ("open", "squint", "base", "R")
        her "As a muggle-born, I usually only wear casual muggle wear when the school uniform doesn't suffice." ("normal", "squint", "base", "mid")
        gen "Perhaps it's time to widen your wardrobe selection then." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "I refuse!" ("open", "closed", "base", "mid")
            her "" ("normal", "base", "base", "mid")
        else: # < 10
            her "*Hmm*... If you say so..." ("normal", "squint", "base", "mid")
            gen "Excellent, here you go..." ("base", xpos="far_left", ypos="head")
            her "What on earth is this!?" ("clench", "squint", "worried", "down")
            gen "A witch outfit?" ("base", xpos="far_left", ypos="head")
            her "This looks like what some muggle bimbo would put on at Halloween..." ("angry", "narrow", "base", "mid")
            gen "Excellent! So, since it's muggle wear I assume you'd feel more comfortable putting it--" ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "base", "mid")
            her "Did you not hear what I just said?" ("open", "happyCl", "annoyed", "mid")
            gen "You usually only wear casual muggle wear when the school uniform--" ("base", xpos="far_left", ypos="head")
            her "Yes, but I said this looks like some slutified Halloween outfit!" ("angry", "squint", "angry", "mid")
            gen "*He-heh*... Slutified..." ("base", xpos="far_left", ypos="head")
            her "I am not wearing it..." ("upset", "base", "annoyed", "mid")

    #######################
    ## Lara Croft Outfit ##
    #######################
    elif item == her_outfit_croft: #Req 10 (top, bottom)
        gen "Could you put on this archaeologist outfit for me?" ("base", xpos="far_left", ypos="head")
        her "A what?" ("soft", "squint", "base", "mid")
        gen "This one..." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "What is this?!" ("open", "wide", "base", "down")
            gen "An archaeologist outfit?" ("base", xpos="far_left", ypos="head")
            gen "Well, at least it's an artist's representation of what one might look like." ("base", xpos="far_left", ypos="head")
            her "What kind of archaeologist would be wearing something like this?" ("clench", "squint", "annoyed", "mid")
            gen "Why none other than the great Lara Croft!" ("base", xpos="far_left", ypos="head")
            her "Who?" ("disgust", "squint", "base", "mid")
            gen "Lara Croft! The world's most famous Archaeologist!" ("base", xpos="far_left", ypos="head")
            her "What kind of archaeologist is she to be wearing this?" ("normal", "slit", "base", "mid")
            gen "The kind that delves into ancient temples looking for rare artefacts!" ("base", xpos="far_left", ypos="head")
            her "Well I must say that attire such as this is hardly necessary to--" ("open", "closed", "annoyed", "mid")
            gen "I'll have you know that she's an expert in her field!" ("base", xpos="far_left", ypos="head")
            gen "I've experienced her... *Err*... expertise in taking care of delicate and ancient artefacts first hand!" ("base", xpos="far_left", ypos="head")
            her "Oh, sorry [name_genie_hermione]!" ("mad", "squint", "base", "mid")
            her "I meant no disrespect, I'd just rather wear something a bit more..." ("upset", "squint", "base", "R")
            her @ cheeks blush "*Ehm*..." ("clench", "base", "base", "mid")
            gen "Whatever you say, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        else: # < 10
            her "Hmm... When I think of an archaeologist outfit, I don't think of something so..." ("soft", "base", "worried", "down")
            gen "Triangular?" ("base", xpos="far_left", ypos="head")
            her "No, I was going to say revealing..." ("disgust", "squint", "base", "mid")
            gen "It's not \"that\" revealing..." ("base", xpos="far_left", ypos="head")
            gen "It had to look that way, because... *Err*... She explores volcanoes and stuff..." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "base", "mid")
            gen "Limitations of the engine..." ("base", xpos="far_left", ypos="head")
            her "The what?" ("upset", "base", "worried", "mid")
            gen "Never mind... Forget it..." ("base", xpos="far_left", ypos="head")

    #######################
    ## Heart Slut Outfit ##
    #######################
    elif item == her_outfit_hslut: #Req 19 (top, panties, bra)
        gen "Put on this burlesque outfit for me will you?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "A what?" ("clench", "wide", "worried", "mid")
            gen "Burlesque outfit, it's--" ("base", xpos="far_left", ypos="head")
            her "What the hell is wrong with you?" ("mad", "base", "angry", "mid")
            gen "What do you mean?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Just look at it!" ("scream", "base", "angry", "mid")
            her @ cheeks blush "What are these heart things even supposed to be?" ("clench", "base", "annoyed", "down")
            gen "Oh, they're called pasties. They go on the top of your nipples." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "squint", "worried", "stare")
            gen "You see, if you move your breasts in a circulation motion, these little things spin around." ("base", xpos="far_left", ypos="head")
            with hpunch
            her @ cheeks blush "What?!" ("shock", "wide", "angry", "mid")
            gen "I know!" ("grin", xpos="far_left", ypos="head")
            gen "Pretty clever, right?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Sir, how could you ask me to wear something like this?!" ("angry", "happy", "angry", "R")
            her @ cheeks blush "I am not putting this on..." ("clench", "narrow", "annoyed", "mid")
        elif states.her.level < 13:
            her @ cheeks blush "Burlesque--" ("clench", "base", "base", "mid")
            her @ cheeks blush "My word!" ("soft", "base", "annoyed", "down")
            gen "A piece of art is it not?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You're expecting me to wear this?" ("clench", "wide", "base", "mid")
            gen "Heck yes!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well you can take that expectation and.... and..." ("open", "closed", "annoyed", "mid")
            gen "And what?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am not wearing this for you..." ("clench", "closed", "base", "mid")
            her @ cheeks blush "" ("normal", "base", "base", "mid")
        else: # < 19
            her @ cheeks blush "A Burlesque outfit?" ("normal", "squint", "base", "mid")
            gen "Indeed... And it's got heart shaped pasties and everything!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "base", "base", "down")
            her @ cheeks blush "You actually want me to put this on?" ("open", "squint", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course you do... Why'd I even ask..." ("normal", "narrow", "base", "R")
            her @ cheeks blush "But... Isn't this what strippers wear, [name_genie_hermione]?" ("open", "closed", "worried", "mid")
            gen "Well, some do... on occasion. I guess it depends..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "... [name_genie_hermione], I'm not a stripper..." ("disgust", "squint", "base", "mid")
            gen "Sure could've fooled me..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I only did that because you paid..." ("open", "closed", "base", "mid")
            gen "Go on..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm sorry sir, but it's too much..." ("angry", "squint", "base", "mid")
            gen "(You're in denial [name_hermione_genie]... Well, I'm sure she'll come around soon enough.)" ("base", xpos="far_left", ypos="head")

    #######################
    ## Ms. Marvel Outfit ##
    #######################
    elif item == her_outfit_msmarv: #Req 10 (top, stockings)
        gen "I've got this Cosplay outfit I'd like you to wear." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "Cosplay, [name_genie_hermione]?" ("clench", "base", "worried", "mid")
            gen "Indeed... It's a Miss--" ("base", xpos="far_left", ypos="head")
            her "I am not wearing it..." ("open", "closed", "annoyed", "mid")
            gen "What? Why not?" ("base", xpos="far_left", ypos="head")
            her "Are you actually expecting me to put on a cosplay outfit for you?" ("angry", "base", "annoyed", "mid")
            gen "I mean..." ("base", xpos="far_left", ypos="head")
            her "I'll stick to normal clothing thank you very much..." ("open", "base", "annoyed", "R")
        else: # < 10
            her "Cosplay outfit, [name_genie_hermione]?" ("normal", "base", "worried", "mid")
            gen "Indeed... It's a Ms Marvel cosplay." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Can't say that I know it..." ("upset", "squint", "base", "R")
            gen "Here you go..." ("base", xpos="far_left", ypos="head")
            her "Oh My... This thing is skin tight..." ("open", "wide", "worried", "down")
            gen "Not too unusual for cosplay..." ("base", xpos="far_left", ypos="head")
            her "I can't put this thing on..." ("clench", "squint", "worried", "mid")
            gen "Oh come on... Just use some powder, and I'm sure it'll slip right--" ("base", xpos="far_left", ypos="head")
            her "I \"won't\" put this thing on..." ("angry", "base", "annoyed", "mid")
            gen "... Then why didn't you just say so..." ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "base", "base", "R")

    #################
    ## Tifa Outfit ##
    #################
    elif item == her_outfit_tifa: #Req 10 (top, bottom)
        gen "Could you put on this Tifa Cosplay outfit?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "Cosplay, [name_genie_hermione]?" ("clench", "base", "worried", "mid")
            gen "Indeed!" ("base", xpos="far_left", ypos="head")
            her "I am not wearing it..." ("open", "closed", "annoyed", "mid")
            gen "What? Why not?" ("base", xpos="far_left", ypos="head")
            her "Are you actually expecting me to put on a cosplay outfit for you?" ("angry", "base", "annoyed", "mid")
            gen "I mean..." ("base", xpos="far_left", ypos="head")
            her "I'll stick to normal clothing thank you very much..." ("open", "base", "annoyed", "R")
        else: # < 10
            her "What's a Tifa, [name_genie_hermione]?" ("soft", "base", "base", "mid")
            gen "What's a-- Who doesn't know--" ("base", xpos="far_left", ypos="head")
            gen "Tifa Lockheart!" ("base", xpos="far_left", ypos="head")
            her "Who?" ("upset", "squint", "worried", "mid")
            gen "*sigh*... I can't believe it..." ("base", xpos="far_left", ypos="head")
            her "Is that a relative of Gilderoy Lockhart?" ("open", "squint", "base", "mid")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            her "Gilderoy... One of the teachers..." ("angry", "squint", "base", "mid")
            gen "No idea who you're talking about..." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "closed", "worried", "mid")
            gen "Are you putting it on or what?" ("base", xpos="far_left", ypos="head")
            her "*Err*... It's a bit revealing..." ("disgust", "narrow", "worried", "down")
            gen "Come on, it's only your stomach..." ("base", xpos="far_left", ypos="head")
            her "That's not what I'm referring to..." ("angry", "narrow", "base", "R")
            gen "Alright fine... Don't wear it then..." ("base", xpos="far_left", ypos="head")

    ##################################
    ## Teddy Outfit (short nightie) ##
    ##################################
    elif item == her_outfit_teddy: #Req 16 (top)
        gen "Could you put on this nightgown?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "This... This is completely transparent!" ("clench", "squint", "annoyed", "down")
            gen "Oh come on, it's hardly even translucent." ("base", xpos="far_left", ypos="head")
            her "I can see the wrinkles on your hand through it..." ("disgust", "squint", "angry", "mid")
            gen "That's just the folds of the fabric." ("base", xpos="far_left", ypos="head")
            her "I am not wearing this..." ("angry", "base", "angry", "mid")
        elif states.her.level < 13:
            her "*Ehm*... Isn't a nightgown supposed to..." ("disgust", "narrow", "base", "down")
            gen "Supposed to what, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "You know..." ("clench", "narrow", "base", "down")
            her @ cheeks blush "Cover your body." ("open", "closed", "annoyed", "mid")
            gen "Isn't it?" ("base", xpos="far_left", ypos="head")
            her "It barely covers anything..." ("upset", "narrow", "base", "mid")
            her "And what it does cover is almost completely see-through." ("open", "squint", "annoyed", "mid")
            gen "I mean, it's lingerie, that's what--" ("base", xpos="far_left", ypos="head")
            her "I am not wearing it..." ("mad", "squint", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
        else: # < 16
            her @ cheeks blush "*Err*... You want me to wear lingerie?" ("open", "base", "base", "R")
            gen "Yes." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "May I ask you why?" ("normal", "squint", "base", "mid")
            gen "Don't you want to look sexy for me?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "For you-- Sir, that is not why I'm doing this..." ("clench", "closed", "base", "mid")
            gen "Did I say for me? I meant--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Too late..." ("angry", "base", "annoyed", "R")
            gen "(Damn...)" ("base", xpos="far_left", ypos="head")

    ####################
    ## Nightie Outfit ##
    ####################
    elif item == her_outfit_nightie: #Req 13 (top)
        gen "Can you put on this nightie for me?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "What is this?!" ("angry", "base", "annoyed", "down")
            gen "A nightie?" ("base", xpos="far_left", ypos="head")
            her "It's see-through!" ("scream", "squint", "base", "mid")
            gen "Oh... Is it? I didn't \"see\" that." ("base", xpos="far_left", ypos="head")
            her "I am not putting that on..." ("mad", "narrow", "angry", "mid")
        else: # < 13
            her "What's supposed to make this piece of garment a nightie exactly?" ("angry", "narrow", "base", "down")
            gen "Well... It's a thin, and soft material that you put on at night." ("base", xpos="far_left", ypos="head")
            her "Isn't a nightie meant to cover you?" ("normal", "narrow", "annoyed", "mid")
            gen "I mean it sort of does..." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "closed", "annoyed", "mid")
            her "Yeah, I'm going to have to decline on this one..." ("clench", "closed", "base", "mid")
            her "" ("normal", "base", "base", "mid")

    #######################
    ## Latex dress Outfit ##
    #######################
    elif item == her_outfit_latex_dress: #Req 19 (top)
        gen "Put on this latex dress for me." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "Latex dress?" ("angry", "squint", "base", "stare")
            her "I didn't know you could make a dress out of--" ("open", "squint", "worried", "mid")
            gen "Here you go." ("base", xpos="far_left", ypos="head")
            her "Are you crazy?!" ("clench", "wide", "base", "down")
            her "What's wrong with you, [name_genie_hermione]?!" ("scream", "squint", "annoyed", "mid")
            gen "What do you--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am not putting that thing on..." ("disgust", "happyCl", "base", "mid")
        elif states.her.level < 13:
            her "Latex dress?" ("angry", "narrow", "base", "stare")
            gen "This one." ("base", xpos="far_left", ypos="head")
            her "This..." ("clench", "squint", "base", "down")
            gen "Pretty unique isn't it?" ("base", xpos="far_left", ypos="head")
            her "This looks like someone ripped an oversized balloon." ("disgust", "squint", "annoyed", "mid")
            gen "Balloon? I was going to say it looks more like a--" ("base", xpos="far_left", ypos="head")
            her "... {w} Like a what?" ("angry", "squint", "annoyed", "mid")
            gen "Never mind..." ("base", xpos="far_left", ypos="head")
            gen "So will you wear--" ("base", xpos="far_left", ypos="head")
            her "No!" ("scream", "closed", "annoyed", "mid")
            her "" ("normal", "squint", "annoyed", "mid")
        else: # < 19
            her @ cheeks blush "[name_genie_hermione], this is fetish gear isn't it?" ("annoyed", "base", "base", "R")
            gen "I mean..." ("base", xpos="far_left", ypos="head")
            gen "I wouldn't exactly call it..." ("base", xpos="far_left", ypos="head")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "From a certain point of view, maybe..." ("base", xpos="far_left", ypos="head")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Yeah okay, I got nothing..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am not putting this on..." ("open", "closed", "base", "mid")
            her @ cheeks blush "" ("normal", "base", "base", "mid")

    #####################
    ## Egyptian Outfit ##
    #####################
    elif item == her_outfit_egypt: #Req 19 (top)
        gen "Put on this Egyptian-themed outfit for me will you?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 13:
            her "Egyptian-themed? What's that supposed to mean?" ("upset", "squint", "worried", "mid")
            gen "You know... The type of clothing that they'd wear in Egypt." ("base", xpos="far_left", ypos="head")
            gen "Well, at least back when I was there." ("base", xpos="far_left", ypos="head")
            her "You've been to Egypt, [name_genie_hermione]?" ("soft", "squint", "base", "mid")
            gen "Of course!" ("base", xpos="far_left", ypos="head")
            gen "And let me tell you... Cleopatra was quite the sight to behold!" ("base", xpos="far_left", ypos="head")
            her "Did you see a bust of her there?" ("base", "base", "worried", "mid")
            gen "Quite a bit more than just her bust." ("base", xpos="far_left", ypos="head")
            her "A statue?" ("open", "base", "base", "mid")
            gen "A what? No, I've met-- I mean... Yes, I saw a statue of her!" ("base", xpos="far_left", ypos="head")
            her "I see... Well, let me have a look..." ("base", "squint", "base", "mid")
            gen "Here you go." ("base", xpos="far_left", ypos="head")
            her "What the--" ("normal", "wide", "base", "down")
            her "Surely this can't be what they wore, [name_genie_hermione]!" ("clench", "base", "base", "down")
            gen "Oh, I'm quite certain they did..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "There's barely any material to cover... *Ehm*..." ("disgust", "squint", "base", "mid")
            gen "I mean, it's quite hot there..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Sorry sir, but this-- I can't-- No offence but--" ("disgust", "squint", "base", "R")
            gen "Alright... fine." ("base", xpos="far_left", ypos="head")
        else: # < 19
            her "Egyptian-themed?" ("soft", "squint", "worried", "mid")
            gen "Yeah, this one." ("base", xpos="far_left", ypos="head")
            her "Sir... I thought Egyptians covered their skin from the sun..." ("upset", "narrow", "base", "mid")
            gen "Poppycock." ("base", xpos="far_left", ypos="head")
            gen "If you did, then you wouldn't be able to get an even tan." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "base", "mid")
            her "Sorry [name_genie_hermione] but this is too much..." ("open", "closed", "annoyed", "mid")
            her "" ("normal", "base", "annoyed", "mid")

    ##############
    ## Swimsuit ##
    ##############
    elif item == her_outfit_swimsuit: #Req 13 (top)
        gen "I've got this swimsuit I'd like you to wear." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "A swimsuit?" ("angry", "happy", "base", "mid")
            her "Am I expected to go swimming with you?" ("clench", "squint", "base", "mid")
            gen "I just thought you'd look good in one." ("base", xpos="far_left", ypos="head")
            her "What?!" ("clench", "squint", "worried", "mid")
            her "You want me to wear it in here?" ("disgust", "squint", "base", "mid")
            gen "Yes, I'd like you to put it on for when you're--" ("base", xpos="far_left", ypos="head")
            her "Why would I stand around in a swimsuit in your office?" ("angry", "happy", "annoyed", "mid")
            gen "As I said, I think you'd look good in it..." ("base", xpos="far_left", ypos="head")
            her "Well, your opinion on how I'd look isn't going to convince me to put on a swimsuit in here..." ("angry", "squint", "base", "R")
        else: # < 13
            her "*Err*... You want me to put on a swimsuit in your office?" ("angry", "squint", "base", "mid")
            gen "Yes." ("base", xpos="far_left", ypos="head")
            her "Wouldn't that be kind of weird?" ("clench", "narrow", "base", "mid")
            gen "I don't see why it would..." ("base", xpos="far_left", ypos="head")
            her "I mean... There's not really a pool or anything in here..." ("disgust", "base", "worried", "L")
            gen "Yeah... No complimentary chocolate, either." ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("upset", "squint", "base", "mid")
            gen "Never mind..." ("base", xpos="far_left", ypos="head")
            gen "Would you put it on if there was a pool in here?" ("base", xpos="far_left", ypos="head")
            her "*Ehm*... Maybe?" ("angry", "squint", "base", "mid")
            gen "(*Hmm*... Now where would I fit a pool?)" ("base", xpos="far_left", ypos="head")
            gen "(Perhaps it'd be easier just to try and convince her some other time...)" ("base", xpos="far_left", ypos="head")

    #####################
    ## Bioshock Outfit ##
    #####################
    elif item == her_outfit_bioshock: #Req 14 (no bra)
        gen "Can you put on this Elisabeth Cosplay outfit?" ("base", xpos="far_left", ypos="head")
        her "Cosplay, [name_genie_hermione]?" ("clench", "base", "worried", "mid")
        gen "Indeed!" ("base", xpos="far_left", ypos="head")
        her "I am not wearing it..." ("open", "closed", "annoyed", "mid")
        gen "What? Why not?" ("angry", xpos="far_left", ypos="head")
        her "Firstly... Why would I put on a cosplay outfit in your office?" ("angry", "base", "annoyed", "mid")
        gen "I mean..." ("base", xpos="far_left", ypos="head")
        her "Secondly... There's not even a bra for this... Cosplay." ("open", "closed", "annoyed", "mid")
        gen "There's a corset though... Surely--" ("base", xpos="far_left", ypos="head")
        her "I'll stick to normal clothing thank you very much..." ("open", "base", "annoyed", "R")

    #####################
    ## Yennefer Outfit ##
    #####################
    elif item == her_outfit_yennefer: #Req 10
        gen "I got this Yennefer Cosplay that I'd like you to put on." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "Cosplay, [name_genie_hermione]?" ("clench", "base", "worried", "mid")
            gen "Yep, she's from the--" ("base", xpos="far_left", ypos="head")
            her "I am not wearing it..." ("open", "closed", "annoyed", "mid")
            gen "You didn't even let me finish!" ("angry", xpos="far_left", ypos="head")
            her "I am not putting on some random cosplay for you..." ("open", "narrow", "annoyed", "mid")
            gen "Whatever... I picked Triss anyway." ("base", xpos="far_left", ypos="head")
            her "What?" ("soft", "squint", "base", "mid")
            gen "Alright, I didn't..." ("base", xpos="far_left", ypos="head")
        else: # < 10
            her "A Cosplay?" ("normal", "base", "base", "mid")
            gen "Yep, Yennefer from the Witcher." ("base", xpos="far_left", ypos="head")
            her "A witch?" ("soft", "squint", "base", "mid")
            her "Well, I suppose I could--" ("open", "closed", "base", "mid")
            gen "That's kind of offensive, actually." ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("clench", "squint", "base", "mid")
            gen "She's a sorceress, not a witch." ("base", xpos="far_left", ypos="head")
            her "I see..." ("angry", "narrow", "base", "R")
            her "(What is he even talking about...)" ("angry", "narrow", "base", "down")
            gen "You better make up for what you just said by wearing this for me..." ("base", xpos="far_left", ypos="head")
            her "What?" ("angry", "squint", "base", "mid")
            gen "Calling her a witch... Witches are usually old women or hags, you know." ("base", xpos="far_left", ypos="head")
            her "Sir..." ("disgust", "base", "worried", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            her "I'm a witch!" ("angry", "base", "annoyed", "mid")
            gen "But the video ga-- I mean books... Yes, I've read them, you know!" ("angry", xpos="far_left", ypos="head")
            her "..." ("annoyed", "base", "annoyed", "mid")
            gen "Okay... You got me... I didn't." ("base", xpos="far_left", ypos="head")
            her "Sir, do I have to wear this?" ("open", "closed", "annoyed", "mid")
            gen "No... I don't deserve it..." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "mid")
            gen "Don't look at me!" ("base", xpos="far_left", ypos="head")

    ################
    ## Ball Dress ##
    ################
    elif item == her_outfit_ball: #Req 14 (no bra)
        gen "Could you put on this dress?" ("base", xpos="far_left", ypos="head")
        her "Sir, this dress has no...{w=0.4} *Ehm*...{w=0.4} Support." ("disgust", "narrow", "base", "down")
        gen "Sorry?" ("base", xpos="far_left", ypos="head")
        her "You know..." ("clench", "narrow", "worried", "R")
        gen "Oh... I see..." ("base", xpos="far_left", ypos="head")
        gen "Well, your breasts should do, shouldn't they?" ("base", xpos="far_left", ypos="head")
        her "What?!" ("angry", "wide", "base", "mid")
        her "Sir, I'm not putting on some dress without my bra..." ("angry", "squint", "annoyed", "mid")
        gen "Why not?" ("base", xpos="far_left", ypos="head")
        gen "It's all covered, isn't it?" ("base", xpos="far_left", ypos="head")
        her "Yes, but--" ("mad", "closed", "base", "mid")
        her "Why am I explaining myself to you?" ("soft", "happyCl", "annoyed", "mid")
        her "I am not wearing it..." ("normal", "squint", "annoyed", "mid")

    ##################
    ## Bunny Outfit ##
    ##################
    elif item == her_outfit_bunny: #Req 19 (top, stockings)
        gen "I've got this bunny costume I'd like you to wear." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "A what?!" ("disgust", "wide", "base", "mid")
            gen "A Bunny costume." ("base", xpos="far_left", ypos="head")
            her "Why would you even own such a thing?" ("open", "squint", "annoyed", "mid")
            gen "Own? I bought it for you, of course!" ("base", xpos="far_left", ypos="head")
            her "You bought me a bunny costume?" ("angry", "narrow", "annoyed", "mid")
            gen "...{w=0.4} No?" ("base", xpos="far_left", ypos="head")
            gen "It's just a prank, bro! {w=0.3} *Err*....{w=0.3} No!{w=0.3} Snape dared me to try and make you wear it!" ("base", xpos="far_left", ypos="head")
            her "Professor Snape did?" ("upset", "squint", "annoyed", "mid")
            gen "...{w=0.4} Yes?" ("base", xpos="far_left", ypos="head")
            her "Well, that kind of humour is very much like him..." ("soft", "squint", "annoyed", "R")
            gen "(When in doubt, blame Snape!)" ("base", xpos="far_left", ypos="head")
        elif states.her.level < 13:
            her "*Err*... You're joking, right?" ("clench", "narrow", "base", "mid")
            her "Surely you don't expect me to put on something so--" ("open", "closed", "annoyed", "mid")
            gen "*Hah-Ha*... Yeah, I'm a bit of a hop-timist sometimes!" ("base", xpos="far_left", ypos="head")
            her "What?" ("clench", "squint", "base", "mid")
            gen "*Heh*...{w=0.3} Never mind." ("base", xpos="far_left", ypos="head")
        else: # < 19
            her @ cheeks blush "*Ehm*..." ("annoyed", "squint", "base", "R")
            her @ cheeks blush "It's a bit much, don't you think?" ("disgust", "narrow", "base", "down")
            gen "Don't be silly... Just hop right into it." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... I think I'll pass." ("angry", "closed", "base", "mid")
            her @ cheeks blush "" ("normal", "squint", "base", "R")

    ######################
    ## Reindeer Costume ##
    ######################
    elif item == her_outfit_reindeer: #Req 19 (top, stockings)
        if states.her.level < 4:
            gen "Ever considered dressing up like a reindeer?" ("base", xpos="far_left", ypos="head")
            her "Why on earth would I consider doing something like that?" ("open", "base", "base", "mid")
            gen "No reason..." ("base", xpos="far_left", ypos="head")
        else: # < 13
            gen "Put on this reindeer costume for me will you?" ("base", xpos="far_left", ypos="head")
            her "A reindeer costume?" ("soft", "base", "base", "mid")
            gen "Yep, this one right here." ("base", xpos="far_left", ypos="head")
            her "Looks-- Hold on, there's a hole in it!" ("angry", "narrow", "base", "down")
            gen "Of course there is, how else would you be able to wear it?" ("base", xpos="far_left", ypos="head")
            her "Not that kind of hole, there's a hole in the-- the--" ("angry", "narrow", "base", "mid")
            gen "Let me see." ("base", xpos="far_left", ypos="head")
            gen "Oh, would you look at that." ("base", xpos="far_left", ypos="head")
            gen "Must be some kind of manufacturing error... Those darn elves, I tell you..." ("base", xpos="far_left", ypos="head")
            her "House elves made this?!" ("open", "narrow", "angry", "mid")
            gen "Santa's elves, house elves, is there a difference?" ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "angry", "mid")
            gen "*Err*... It was a joke, since it's a Christmas costume. Of course elves didn't make it!" ("angry", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "angry", "mid")
            gen "I mean, if elves had made it, I'm sure they wouldn't have missed this giant hole." ("base", xpos="far_left", ypos="head")
            her "*Sigh*..." ("disgust", "narrow", "angry", "R")
            gen "(Crisis averted)." ("base", xpos="far_left", ypos="head")

    ###############################
    ## Poker Outfit (token shop) ##
    ###############################
    elif item == her_outfit_poker: #Req 19 (panties, bra)
        gen "I spent some tokens getting this outfit for you..." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "And you're expecting me to just wear this thing because you've won it?" ("open", "narrow", "annoyed", "mid")
            her "(Does he think he can play me like he plays games?)" ("clench", "narrow", "base", "R")
            gen "But, I won... fair and square..." ("angry", xpos="far_left", ypos="head")
            her "Well, I'm not some prize for you to win in a game..." ("open", "narrow", "annoyed", "mid")
            gen "Actually--" ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "base", "annoyed", "mid")
            gen "Alright... Never mind then..." ("base", xpos="far_left", ypos="head")
        elif states.her.level < 13:
            her "And you winning it means that I'm supposed to wear it?" ("angry", "narrow", "annoyed", "mid")
            gen "Pretty sure that's how it works." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... I don't think so..." ("disgust", "narrow", "annoyed", "R")
            her "You may be a winner [name_genie_hermione] but that sure doesn't give you some privilege to make me wear--" ("open", "closed", "annoyed", "mid")
            her "Whatever this...{w=0.4} Thing... Is supposed to be." ("angry", "narrow", "annoyed", "mid")
            gen "(Damn it...)" ("base", xpos="far_left", ypos="head")
        else: # < 19
            her "*Err*... Am I supposed to be some kind of prize for you winning games?" ("clench", "narrow", "base", "R")
            gen "I mean, this outfit was practically made for you..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "narrow", "base", "mid")
            gen "Come on... Surely, you can't resist basking in my glory." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "mid")
            her "Well, I'm sorry but it looks to me as if you spent your hard-earned tokens on a piece of fabric." ("open", "narrow", "base", "R")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "(Guess even a smidge of my fame is too much for her...)" ("base", xpos="far_left", ypos="head")

    #################
    ## Maid Outfit ##
    #################
    elif item == her_outfit_maid: #Req 4
        gen "Could you put on this maid's outfit?" ("base", xpos="far_left", ypos="head")
        her "A maid's outfit?" ("upset", "squint", "base", "mid")
        her "Isn't cleaning part of the house elves' job?" ("open", "closed", "annoyed", "mid")
        her "(Not that I approve of this horrible house elf enslavement...)" ("annoyed", "closed", "annoyed", "mid")
        gen "I mean, I'd be fine if you just--" ("base", xpos="far_left", ypos="head")
        her "I have no time to clean up your mess, you'll have to do that yourself..." ("open", "happy", "annoyed", "mid")
        gen "(I don't think there are enough tissues in this world for that.)" ("base", xpos="far_left", ypos="head")
        gen "Very well, Miss Granger..." ("base", xpos="far_left", ypos="head")

    #########################
    ## Sling Bikini Outfit ##
    #########################
    elif item == her_outfit_bikini3: #Req 17 (panties, bra)
        gen "Put on this bikini for me will you." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "A bikini?!" ("shock", "wide", "base", "mid")
            gen "Wow, excited much?" ("grin", xpos="far_left", ypos="head")
            gen "Well then, here you go!" ("grin", xpos="far_left", ypos="head")
            her "Sir!" ("clench", "wide", "base", "down")
            her "What are these chains?!" ("angry", "wide", "base", "down")
            gen "Oh, those!" ("base", xpos="far_left", ypos="head")
            gen "They are the straps I believe." ("base", xpos="far_left", ypos="head")
            gen "Pretty cool, right?" ("base", xpos="far_left", ypos="head")
            her "Cool?!" ("angry", "wide", "angry", "mid")
            gen "Is that not how you say it anymore?" ("base", xpos="far_left", ypos="head")
            gen "I'm not really up to date with the \"lingo\" these days." ("base", xpos="far_left", ypos="head")
            her "Are you crazy?!" ("scream", "squint", "annoyed", "mid")
            gen "I mean... at least I didn't say \"Tubular\"." ("base", xpos="far_left", ypos="head")
            her "Asking me to wear a normal bikini is bad enough, but this..." ("disgust", "closed", "angry", "mid")
            gen "*Huh*? Looks pretty normal to me... From where I'm from--" ("base", xpos="far_left", ypos="head")
            gen "I mean--" ("angry", xpos="far_left", ypos="head")
            her "Then you probably need to get your eyes checked..." ("angry", "base", "angry", "mid")
            her "Because this bikini you got me would surely never be an appropriate--" ("angry", "base", "angry", "R")
            gen "Fine... Whatever..." ("base", xpos="far_left", ypos="head")
        elif states.her.level < 13:
            her "A bikini?" ("disgust", "squint", "base", "mid")
            gen "Indeed... This one right here..." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "wide", "base", "down")
            her @ cheeks blush "[name_genie_hermione], You can't be serious!" ("open", "closed", "annoyed", "mid")
            gen "About what? It's a bikini, is it not?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "These straps are made of chains! Surely that wouldn't even help to keep them on..." ("angry", "narrow", "annoyed", "down")
            gen "I'm sure you'll find a way..." ("base", xpos="far_left", ypos="head")
            her "I won't!" ("scream", "closed", "annoyed", "mid")
            gen "Don't put yourself down like that... I'm sure some spell would--" ("base", xpos="far_left", ypos="head")
            her "I won't, because I'm not putting it on..." ("angry", "narrow", "angry", "mid")
            gen "Oh...{w=0.4} Right..." ("base", xpos="far_left", ypos="head")
        else: # < 17
            her "A bikini?" ("base", "base", "base", "mid")
            her "Well, I suppose that wouldn't be too--" ("base", "base", "base", "mid")
            gen "This one..." ("base", xpos="far_left", ypos="head")
            her "That one?" ("base", "base", "base", "mid")
            her "Sir, are you sure this is..." ("base", "base", "base", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            her "*Ehm*... I mean, it looks a bit..." ("base", "base", "base", "mid")
            gen "A bit what?" ("base", xpos="far_left", ypos="head")
            her "*Ehm*..." ("base", "base", "base", "mid")
            gen "Come on, it's not that bad... Just put it on." ("base", xpos="far_left", ypos="head")
            her "I...{w} No, I'm sorry... It's too much..." ("base", "base", "base", "mid")

    ###########################
    ## Leather Bikini Outfit ##
    ###########################
    elif item == her_outfit_bikini2: #Req 16 (panties, bra)
        gen "Put on this bikini for me." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "For you?!" ("disgust", "base", "annoyed", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            her "Sir, I'm not some doll for you to dress up!" ("scream", "closed", "annoyed", "mid")
            her "Especially not in something like a bikini!" ("angry", "narrow", "angry", "mid")
            gen "(She's not? Then what the fuck is this wardrobe UI for?)" ("base", xpos="far_left", ypos="head")
            gen "My mistake I guess..." ("base", xpos="far_left", ypos="head")
        else: # < 16
            her @ cheeks blush "You want me to put on a bikini?" ("upset", "squint", "base", "mid")
            gen "Yeah, this leather one." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "A leather bikini?!?" ("clench", "narrow", "base", "down")
            gen "I'm sure it's not real leather..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That... That's not the point!" ("open", "closed", "worried", "mid")
            gen "Oh... I'm sorry, it usually is with this type of thing..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You actually expect me to--" ("angry", "squint", "base", "mid")
            gen "I didn't ship it from anywhere, it's made locally." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "[name_genie_hermione], I don't care about where you got it from... It's the fact that--" ("angry", "narrow", "worried", "mid")
            gen "Jeez, perhaps you need to take a good look at yourself then." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What?" ("clench", "squint", "base", "mid")
            gen "Spending a bit more is worth it if it supports your local community." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "squint", "base", "mid")
            gen "Stimulating the economy and all that stuff..." ("base", xpos="far_left", ypos="head")
            if states.her.level < 13:
                her @ cheeks blush "I'm not wearing it for the fact that it's a bikini... It's weird..." ("annoyed", "squint", "base", "R")
                gen "(*Heh-heh*... Stimulating...)" ("grin", xpos="far_left", ypos="head")
                gen "Anyway, so you're putting it on or what?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I am not..." ("normal", "narrow", "base", "mid")
            else: # < 16:
                her @ cheeks blush "I don't want to put on a bikini in your office." ("open", "closed", "base", "mid")
                her @ cheeks blush "Standing in my underwear is weird enough..." ("annoyed", "squint", "base", "R")
                gen "Whatever you say [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

    ########################
    ## Rave Bikini Outfit ##
    ########################
    elif item == her_outfit_bikini1: #Req 18 (panties, bra)
        gen "I've got this bikini for you to wear today." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "A bikini?!" ("clench", "wide", "worried", "mid")
            gen "Yep, this one right here." ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "squint", "base", "down")
            gen "Pretty neat, isn't it?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Where's the rest of it?!" ("disgust", "wide", "base", "mid")
            gen "What do you mean the rest? Isn't a bikini supposed to only come in two pieces?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Isn't a bikini supposed to-- Oh... I don't know..." ("angry", "squint", "annoyed", "mid")
            with hpunch
            her @ cheeks blush "Cover your privates?!" ("scream", "closed", "annoyed", "mid")
            gen "Doesn't it do that?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "There's barely any fabric to cover anything!" ("disgust", "base", "annoyed", "mid")
            gen "Very environmentally friendly isn't it?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am not wearing this..." ("mad", "base", "annoyed", "mid")
        elif states.her.level < 13:
            her @ cheeks blush "A bikini?" ("clench", "squint", "worried", "mid")
            gen "This one..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That... That one?!" ("angry", "squint", "base", "down")
            gen "Yep... Now, if you could just--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am not wearing this..." ("disgust", "narrow", "base", "mid")
            gen "Why not?!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "What do you think?" ("angry", "base", "annoyed", "mid")
            gen "Oh... I see..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Finally, you get it..." ("open", "closed", "annoyed", "mid")
            gen "I'd gladly help you tie it around your back if you can't reach." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "That's not why!" ("annoyed", "base", "annoyed", "mid")
            her @ cheeks blush "*Grr*... I can't believe you..." ("clench", "narrow", "base", "R")
            her @ cheeks blush "I am not wearing this... This excuse of a bikini..." ("annoyed", "closed", "base", "mid")
            gen "Well excuuuuuse me, princess..." ("base", xpos="far_left", ypos="head")
        else: # < 18
            her @ cheeks blush "A bikini?" ("open", "squint", "base", "mid")
            gen "This one." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That one?" ("angry", "narrow", "base", "down")
            gen "Yes, that one." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Really?" ("angry", "squint", "base", "mid")
            gen "Really..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Are you sure--" ("angry", "squint", "base", "mid")
            gen "I am--...{w=0.4} How long are you going to keep this up?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "squint", "base", "R")
            her @ cheeks blush "Sir, surely this kind of bikini..." ("normal", "closed", "base", "mid")
            her @ cheeks blush "Why it looks like something you might wear at..." ("angry", "narrow", "base", "down")
            gen "At what, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ehm*..." ("upset", "narrow", "base", "mid")
            gen "A porn shoot?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I...{w=0.4} Yes." ("angry", "narrow", "base", "mid")
            gen "You've watched porn [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What?!" ("clench", "squint", "base", "mid")
            gen "You just agreed with what I said... Which means you've watched porn before." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I...{w=0.4} I have not!" ("annoyed", "closed", "annoyed", "mid")
            her @ cheeks blush "I swear, I've never--" ("open", "closed", "annoyed", "mid")
            gen "Look, I'm not judging." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "But..." ("clench", "squint", "worried", "mid")
            her @ cheeks blush "You...{w=0.4} Sorry [name_genie_hermione], but this outfit is too much..." ("open", "narrow", "worried", "R")

    ################################
    ## Pizza Slut Outfit (mirror) ##
    ################################
    elif item == her_outfit_pizza: #Req 19 (top, panties)
        gen "Put this pizza on." ("base", xpos="far_left", ypos="head")
        if states.her.level < 13:
            her "Put it on, [name_genie_hermione]?" ("normal", "squint", "base", "mid")
            gen "Yes, put it on." ("base", xpos="far_left", ypos="head")
            her "Do you want me to heat it up?" ("open", "squint", "worried", "mid")
            gen "No, I want you to put it on." ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("annoyed", "squint", "base", "mid")
            gen "Put... it--" ("base", xpos="far_left", ypos="head")
            gen "You know what... Forget it." ("base", xpos="far_left", ypos="head")
        else: # < 19
            her "Put it on, [name_genie_hermione]?" ("normal", "squint", "base", "mid")
            gen "Yes..." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "squint", "base", "mid")
            her "..." ("normal", "squint", "base", "stare")
            her "Surely you can't be serious..." ("disgust", "squint", "base", "mid")
            her "You want me to wear...{w=0.4} Pizza?" ("angry", "narrow", "base", "down")
            her "Where on earth did you get an idea like this?" ("open", "closed", "worried", "mid")
            gen "In a dream." ("base", xpos="far_left", ypos="head")
            her "...{w} Then it will stay that way..." ("normal", "narrow", "base", "R")
            gen "(Such a pizzawork that one...)" ("base", xpos="far_left", ypos="head")

    ###################
    ## Ribbon Outfit ##
    ###################
    elif item == her_outfit_ribbon: #Req 18 (bra, panties)
        gen "I've got this thing that I'd like you to wrap for me." ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "You want me to wrap a gift for you?" ("annoyed", "squint", "base", "mid")
            gen "Yes..." ("base", xpos="far_left", ypos="head")
            her "I guess I could do that..." ("open", "closed", "base", "mid")
            gen "Here are the ribbons..." ("base", xpos="far_left", ypos="head")
            her "Thank you." ("base", "base", "base", "mid")
            gen "Go on..." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione], you've not provided me any wrapping paper..." ("open", "squint", "base", "mid")
            her "Or whatever it is you wanted me to wrap." ("open", "base", "base", "mid")
            gen "My mistake... I should've been more clear." ("base", xpos="far_left", ypos="head")
            gen "You won't need any paper, the ribbons should do." ("base", xpos="far_left", ypos="head")
            her "Right... but what about--" ("angry", "base", "base", "mid")
            gen "Now take your clothes off and tie those ribbons around yourself." ("base", xpos="far_left", ypos="head")
            her "..." ("clench", "wide", "base", "mid")
            her "You want me to what?!" ("disgust", "base", "annoyed", "mid")
            gen "Take your clothes--" ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione], are you crazy?!" ("scream", "happyCl", "annoyed", "mid")
            gen "You've learnt how to tie a knot, have you not?" ("base", xpos="far_left", ypos="head")
            gen "If it's an issue I suppose I could--" ("base", xpos="far_left", ypos="head")
            her "You want me to take my clothes off and only wear a ribbon?!" ("clench", "base", "annoyed", "mid")
            gen "Ribbons actually... There's two of them." ("base", xpos="far_left", ypos="head")
            her "Oh... Then I suppose it's fine then!" ("disgust", "narrow", "annoyed", "R")
            gen "I knew you'd come around sooner rather than--" ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "base", "angry", "mid")
            gen "Ah... Sarcasm... My most loyal friend yet also my greatest enemy..." ("base", xpos="far_left", ypos="head")
        elif states.her.level < 13:
            her "And that gift is?" ("open", "narrow", "base", "mid")
            gen "It's you!" ("base", xpos="far_left", ypos="head")
            her "*Ugh*..." ("disgust", "narrow", "base", "R")
            her "You really expect me to gift wrap myself?" ("annoyed", "closed", "annoyed", "mid")
            gen "Yep." ("base", xpos="far_left", ypos="head")
            gen "But don't worry. I'll unwrap my present myself." ("base", xpos="far_left", ypos="head")
            her "Gross..." ("annoyed", "narrow", "base", "R")
            gen "Don't put yourself down like that." ("base", xpos="far_left", ypos="head")
            her "I am not putting this on..." ("open", "narrow", "annoyed", "mid")
            gen "Why not?" ("angry", xpos="far_left", ypos="head")
            her "I am not some gift for you to unwrap, [name_genie_hermione]..." ("disgust", "narrow", "base", "mid")
            gen "Worst birthday ever..." ("base", xpos="far_left", ypos="head")
        else: # < 18
            her "It's me isn't it?" ("disgust", "narrow", "base", "mid")
            gen "It's--" ("grin", xpos="far_left", ypos="head")
            gen "How did you know?" ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "mid")
            gen "Am I really that predicable?" ("base", xpos="far_left", ypos="head")
            her "Yes..." ("normal", "narrow", "base", "mid")
            gen "Well... take this for predictable..." ("base", xpos="far_left", ypos="head")
            gen "I want you to tie it around your naked body!" ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "base", "mid")
            gen "Don't tell me you knew that too?" ("base", xpos="far_left", ypos="head")
            her "I mean..." ("open", "closed", "base", "mid")
            gen "*Hmm*... In that case, I want you to..." ("base", xpos="far_left", ypos="head")
            gen "Tie it around your tits so hard it squeezes them together!" ("grin", xpos="far_left", ypos="head")
            her "..." ("clench", "wide", "base", "mid")
            gen "Didn't expect that one, did you?" ("grin", xpos="far_left", ypos="head")
            her "I am not doing that!" ("open", "base", "annoyed", "mid")
            gen "(Oh, shit...)" ("base", xpos="far_left", ypos="head")
            gen "What about doing it loosely?" ("base", xpos="far_left", ypos="head")
            her "..." ("upset", "base", "annoyed", "mid")
            gen "Yeah, yeah... Fine... Not like it's my birthday or anything..." ("base", xpos="far_left", ypos="head")

    ######################
    ## Christmas Outfit ##
    ######################
    elif item == her_outfit_xmas: #Req 13 (top, bottom)
        gen "I'm feeling festive today so could you put on the Christmas outfit?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her @ cheeks blush "What is wrong with this outfit?!" ("clench", "squint", "worried", "down")
            her @ cheeks blush "Surely this isn't appropriate holiday attire!" ("angry", "narrow", "annoyed", "mid")
            gen "I don't know... Might jingle a couple of balls..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What did you just say?!" ("clench", "squint", "base", "mid")
            gen "Bells... I said bells..." ("base", xpos="far_left", ypos="head")
            gen "Come on, just put the thing on. I'm sure that Santa would give us a white Christmas if you did." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I think I'll pass..." ("open", "base", "annoyed", "R")
            gen "(Balls...)" ("base", xpos="far_left", ypos="head")
        else: # < 13
            her @ cheeks blush "Are those horns?" ("disgust", "narrow", "base", "down")
            gen "Antlers actually..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Antlers..." ("upset", "narrow", "base", "down")
            her @ cheeks blush "And a bell..." ("annoyed", "narrow", "base", "down")
            her @ cheeks blush "Are you trying to make me to look like some sort of reindeer?" ("angry", "closed", "annoyed", "mid")
            gen "Cute, aren't they?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "narrow", "annoyed", "mid")
            gen "You'd be like a sexy reindeer!" ("grin", xpos="far_left", ypos="head")
            gen "Actually, that does sound a bit--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm not putting this on..." ("angry", "closed", "annoyed", "mid")

    #####################
    ## Wrestling Robes ##
    #####################
    elif item == her_outfit_wrestling: #Req 3 (robe, bra, panties, misc)
        gen "I've got these wrestling robes for you to wear today." ("base", xpos="far_left", ypos="head")
        her "Wrestling--" ("angry", "base", "base", "mid")
        her "[name_genie_hermione], these would show off my underwear!" ("clench", "narrow", "base", "down")
        gen "So? You showed off a lot more in the mirror." ("base", xpos="far_left", ypos="head")
        her "In the what?" ("angry", "base", "base", "mid")
        gen "Oh yeah... You wouldn't know about that..." ("base", xpos="far_left", ypos="head")
        gen "Never mind then..." ("base", xpos="far_left", ypos="head")

    else:
        random:
            her "I am not wearing that..." ("annoyed", "base", "angry", "down")
            her "Thanks, but no thanks..." ("annoyed", "happyCl", "angry", "R")
            her "You actually think I'd put on something like that?" ("annoyed", "wide", "angry", "mid")
            her "I'm not some Slytherin skank [name_genie_hermione], ask them to humiliate themselves for your amusement..." ("open", "narrow", "angry", "L")
            her "This is too much." ("annoyed", "narrow", "angry", "R")

    return

label her_reaction_blacklist(item):
    her "I would have to take off some of my clothes to fit into this..." ("disgust", "base", "base", "down")

    if "top" in item.blacklist and hermione.is_worn("top"):
        her "My top won't fit at all." ("open", "narrow", "angry", "mid")

    if "bottom" in item.blacklist and hermione.is_worn("bottom"):
        her "The bottoms I'm wearing won't be of much use." ("open", "narrow", "angry", "mid")

    if "bra" in item.blacklist and hermione.is_worn("bra"):
        her @ cheeks blush "Wearing a bra with this would be impossible." ("annoyed", "narrow", "angry", "L")

    if "panties" in item.blacklist and hermione.is_worn("panties"):
        her @ cheeks blush "And how in the world am I supposed to wear panties with this?" ("angry", "narrow", "angry", "mid")

    gen "Pretty please?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Fine, I'll wear it... but I'm putting my old clothes back on once you change your mind." ("annoyed", "narrow", "angry", "R")

    return

label her_reaction_fallback(item):
    if states.her.level < get_character_requirement("hermione", "unequip top") and not "top" in hermione.blacklist and not item.type == "top":
        $ hermione.equip(her_top_school1)

    if states.her.level < get_character_requirement("hermione", "unequip bottom") and not "bottom" in hermione.blacklist and not item.type == "bottom":
        $ hermione.equip(her_bottom_school1)

    if states.her.level < get_character_requirement("hermione", "unequip bra") and not "bra" in hermione.blacklist and not item.type == "bra":
        $ hermione.equip(her_bra_base1)

    if states.her.level < get_character_requirement("hermione", "unequip panties") and not "panties" in hermione.blacklist and not item.type == "panties":
        $ hermione.equip(her_panties_base1)

    her "Just give me a second, I need to get my clothes back in order." ("open", "base", "base", "R")
    her "" ("base", "base", "base", "mid")
    return
