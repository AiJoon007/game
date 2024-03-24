define lun_requirements = {
    "category upper undergarment": 7,
    "category lower undergarment": 7,
    "category piercings & tattoos": 13,
    # "touch head":
    # "touch breasts":
    # "touch vagina":
    "unequip panties": 7,
    "unequip bra": 7,
    "unequip top": 4,
    "unequip bottom": 4,
    }

define lun_responses = {
    "category_fail": "lun_reaction_category_fail",
    "equip": "lun_reaction_equip",
    "equip_fail": "lun_reaction_equip_fail",
    "unequip": "lun_reaction_unequip",
    "unequip_fail": "lun_reaction_unequip_fail",
    "touch": "lun_reaction_touch",
    "touch_fail": "lun_reaction_touch_fail",
    "equip_outfit": "lun_reaction_equip_outfit",
    "equip_outfit_fail": "lun_reaction_equip_outfit_fail",
    "blacklist": "lun_reaction_blacklist",
    "fallback": "lun_reaction_fallback",
}

label lun_reaction_category_fail(category):

    if category == "upper undergarment":
        lun "Is this part of our Wrackspurt research [name_genie_luna]?" ("open", "base", "raised", "mid")
        gen "*Err*... I just thought maybe you could... Never mind..." ("base", xpos="far_left", ypos="head")
    elif category == "lower undergarment":
        lun "Is this part of our Wrackspurt research [name_genie_luna]?" ("soft", "base", "base", "mid")
        gen "*Err*... I just thought maybe you could... Never mind..." ("base", xpos="far_left", ypos="head")
    elif category == "piercings & tattoos":

        random:
            lun "Daddy says that ink should only be used on paper and not on your body..." ("open", "closed", "annoyed", "mid")

            block:
                lun "I'm not sure if that's such a good idea [name_genie_luna]..." ("open", "closed", "base", "mid")
                gen "Why's that?" ("base", xpos="far_left", ypos="head")
                lun "It might attract Nifflers into the castle..." ("normal", "base", "annoyed", "mid")
                gen "..." ("base", xpos="far_left", ypos="head")
            block:
                lun "Isn't it supposed to hurt?" ("upset", "wide", "base", "mid")
                gen "I'm sure there's some magical mumbo jumbo that would make it painless..." ("base", xpos="far_left", ypos="head")
                lun "*Hmm*... I'm not sure..." ("annoyed", "base", "base", "R")
    return

label lun_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()

        if states.lun.tier == 5:
            random:
                lun @ cheeks blush "*Mmm*..." ("soft", "closed", "base", "mid")
                lun @ cheeks blush "*Hmm*... I could've sworn you said that we should focus on more sensitive areas..." ("base", "narrow", "base", "down")

                block:
                    lun @ cheeks blush "*Ah*..." ("open", "closed", "base", "mid")
                    lun @ cheeks blush "Sorry, you just took me by surprise..." ("base", "narrow", "base", "mid")

        elif states.lun.tier == 4:
            random:
                block:
                    lun "*Mmm*... That's strange..." ("annoyed", "base", "base", "mid")
                    lun "How come I'm feeling good in other places when it's my head you're touching?" ("grin", "narrow", "base", "mid")
                block:
                    lun "Pat, pat, pat." ("base", "happyCl", "base", "mid")
                    gen "..." ("base", xpos="far_left", ypos="head")
                block:
                    lun @ cheeks blush "Thank you, [name_genie_luna]..." ("soft", "narrow", "base", "downR")
                    lun @ cheeks blush "I feel like I get a big boost of happiness when you pat me for some reason..." ("base", "narrow", "base", "mid")
                    lun @ cheeks blush "Maybe that's why animals enjoy it so much too..." ("grin", "base", "base", "mid")
        elif states.lun.tier == 3:
            random:
                lun "Is my head another one of those sensitive areas you spoke about?" ("open", "base", "raised", "mid")
                lun "I don't think there's anywhere for me to release the Wrackspurts from up there, but thank you anyway..." ("base", "narrow", "base", "mid")
                lun "Are you sure this technique is working [name_genie_luna]?" ("annoyed", "base", "raised", "mid")
        elif states.lun.tier == 2:
            random:
                lun "*Hmm*... I'm not getting any of that tingly sensation up there but it does feel kind of nice..." ("soft", "base", "base", "up")
                block:
                    lun "Thank you [name_genie_luna]." ("crooked_smile", "base", "base", "mid")
                    lun "I'm so glad you decided to let me help with your research." ("smile", "happyCl", "base", "mid")
                block:
                    lun "Are you feeling stressed [name_genie_luna]?" ("soft", "base", "base", "mid")
                    gen "*Huh*?" ("base", xpos="far_left", ypos="head")
                    lun "Feel free to pet me any time you like if it helps." ("base", "closed", "base", "mid")
                    gen "*Err*... Thanks..." ("base", xpos="far_left", ypos="head")

        else: #Tier 1
            random:
                lun "I think I lost a pencil up there, let me know if you find it." ("soft", "base", "base", "up")
                lun "I already checked for Nargles this morning but I suppose you can't be too careful..." ("base", "base", "base", "down")

                block:
                    lun "Thank you [name_genie_luna]." ("grin", "closed", "base", "mid")
                    lun "Other students look at me weird if I try to pet them, so I'm glad I didn't do something weird again..." ("angry", "base", "base", "downR")


    elif what == "breasts":
        $ mouse_heart()

        if states.lun.tier == 5:
            random:
                lun @ cheeks blush "Don't forget to kiss the other one too! She gets awfully jealous if her sister gets all the attention." ("base", "base", "base", "down")
                lun @ cheeks blush "*Ah*... Thank you for helping me [name_genie_luna]..." ("soft", "closed", "base", "mid")
                block:
                    lun "*Mmm*... Why does something so bad feel so good?" ("grin", "closed", "base", "mid")
                    gen "The backsprats?" ("base", xpos="far_left", ypos="head")
                    lun "*Huh*?" ("open", "base", "base", "mid")
                    lun @ cheeks blush "Oh... Yes, those pesky little things..." ("soft", "base", "base", "downR")

        elif states.lun.tier == 4:
            random:
                lun @ cheeks blush "Come... Come out already..." ("soft", "closed", "base", "mid")
                block:
                    lun @ cheeks blush "*Mmm*... How come I don't really see any of the Wrackspurts coming out from here?" ("disgust", "narrow", "base", "mid")
                    gen "*Err*..." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "It feels really good so why aren't any of them coming out?" ("annoyed", "base", "base", "mid")
                block:
                    lun @ cheeks blush "*Ah*... {w=0.4} Your methods are quite the something [name_genie_luna]..." ("open", "closed", "base", "mid")
                    lun @ cheeks blush "I could never have imagined that getting rid of those pests would end up being so..." ("base", "closed", "base", "mid")
                    lun @ cheeks blush "Enjoyable..." ("grin", "narrow", "base", "mid")

        elif states.lun.tier == 3:
            random:
                block:
                    lun "You really were right about these things being sensitive..." ("open", "base", "base", "down")
                    lun "Can't believe I hadn't figured this out earlier." ("base", "base", "base", "downR")
                block:
                    lun @ cheeks blush "*Ah*... Is everyone this sensitive in around this spot?" ("soft", "closed", "base", "mid")
                    gen "Women are a lot more sensitive than men most of the time..." ("base", xpos="far_left", ypos="head")
                    lun "Oh... That's so sad..." ("angry", "base", "base", "mid")
                block:
                    lun @ cheeks blush "..." ("soft", "base", "base", "mid")
                    gen "How did that feel?" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "*Ehm*... It felt very nice [name_genie_luna]..." ("open", "narrow", "base", "downR")
        #elif states.lun.tier == 2: This would only be useful if there was another check if you've done event 2 to have it show before T3
        else: # T1 and T2
            random:
                lun "Are you looking for the Himalayan Lesser Spotted Breast Imp? It's okay [name_genie_luna], it's not their migration season." ("grin", "base", "base", "down")
                lun "..." ("soft", "base", "raised", "mid")
                block:
                    lun "*Hi-Hi*..." ("grin", "closed", "base", "mid")
                    lun "Sorry [name_genie_luna], your beard is tickling me..." ("smile", "base", "base", "mid")

    elif what == "vagina":
        $ mouse_heart()

        if states.lun.tier == 5:
            random:
                lun @ cheeks blush "*Ah*... S-so good... How did I ever live without this?" ("normal", "closed", "base", "mid")
                lun @ cheeks blush "*Mmm*... Nasty... Wrackspurts..." ("base", "closed", "base", "mid")
                lun @ cheeks blush "Please... Help me get rid of them again..." ("crooked_smile", "narrow", "base", "mid")
        elif states.lun.tier == 4:
            random:
                lun @ cheeks blush "Whoa... I didn't think just using your mouth could produce such a strong response." ("open", "wide", "base", "mid")
                lun @ cheeks blush "*Ah*... It's almost like a ripple of water... Except running through my body..." ("soft", "closed", "base", "mid")
                lun @ cheeks blush "*Mmm*... Those nasty Wrackspurts... I can feel them getting agitated already..." ("grin", "narrow", "base", "downR")
        elif states.lun.tier == 3:
            random:
                lun @ cheeks blush "*Ohhhh*... This is going to be my new happy memory when I have to summon a patronus!" ("base", "narrow", "base", "down")
                lun "Weren't I supposed to be learning how to do this myself?" ("angry", "base", "raised", "mid")
                block:
                    lun "*Oohhh*... Why are your lips cold?" ("clench", "wide", "base", "mid")
                    gen "Why are your lips cold?" ("base", xpos="far_left", ypos="head")
                    lun "*Huh*?" ("upset", "base", "raised", "mid")
        # elif states.lun.tier == 2:This would only be useful if there was another check if you've done event 2 to have it show before T3
        else: # T1 and T2
            random:
                block:
                    lun "*Hi-Hi*..." ("grin", "happyCl", "base", "mid")
                    lun "That's not my cheek, silly..." ("crooked_smile", "narrow", "base", "mid")
                block:
                    lun "Is this a lesson on the dementor's kiss?" ("open", "base", "raised", "mid")
                    lun "I always thought it was done through the mouth." ("soft", "base", "base", "downR")
                block:
                    lun "*Ooohh*..." ("grin", "base", "base", "up")
                    lun "I don't think anyone has ever kissed me there before... How strange..." ("grin", "closed", "base", "mid")
    return

label lun_reaction_touch_fail(what): #Not used
    if what == "head":
        $ mouse_slap()

        gen "Ouch! Why would you do that?!" ("angry", xpos="far_left", ypos="head")
        lun "Oh! I'm terribly sorry, [name_genie_luna], I used to play this game with my father and..."
        gen "I don't need to hear it..." ("base", xpos="far_left", ypos="head")
        lun "...as you wish [name_genie_luna]."

    elif what == "breasts":
        $ mouse_slap()

        lun "*Giggles* [name_genie_luna] stop that! It tickles."

    elif what == "vagina":
        $ mouse_slap()

        lun "*Ah* [name_genie_luna], please don't tease me, wrackspurts have been terribly active today, and I'm barely able to withhold as it is."

    return

label lun_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     lun "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label lun_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     lun "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    lun "*Hmm*..." ("annoyed", "base", "base", "mid")
    gen "What?" ("base", xpos="far_left", ypos="head")
    lun "There's a weird aura surrounding this piece of garment." ("open", "closed", "base", "mid")
    lun "It seems to be affecting the Wrackspurts, as if they're multiplying!" ("disgust", "base", "base", "mid")
    if states.lun.level < 4:
        lun "I'm sorry [name_genie_luna] but I can't wear that... Not until we find a way of dealing with them." ("open", "closed", "base", "mid")
    else:
        lun "I'm sorry [name_genie_luna] but I can't wear that... Not until we find a better strategy of dealing with them." ("open", "closed", "base", "mid")
    gen "(I guess that means she's not ready yet.)" ("base", xpos="far_left", ypos="head")

    return

label lun_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if states.lun.level > 15:
    #        lun "You want to see my snatch?"
    #        lun "You got it [name_genie_hermione]!"
    #
    return

label lun_reaction_unequip_fail(item):
    if item.type == "panties": #probably won't play since category unlocks same level as she can take them off
        lun "I'm sorry [name_genie_luna] but my panties are my one and only defence against wrackspurts." ("open", "closed", "base", "mid")

    elif item.type == "bra": #probably won't play since category unlocks same level as she can take them off
        lun "*Giggles*" ("grin", "closed", "base", "mid")
        gen "What's so funny?" ("base", xpos="far_left", ypos="head")
        lun "Oh... It's nothing..." ("base", "base", "base", "R")

    elif item.type == "top":
        lun "Are we going to continue the research, [name_genie_luna]?" ("open", "base", "raised", "mid")
        gen "Not right now..." ("base", xpos="far_left", ypos="head")
        lun "Oh... Then let me know when you're ready..." ("base", "base", "base", "R")

    elif item.type == "bottom":
        lun "Are we going to continue the research, [name_genie_luna]?" ("upset", "base", "raised", "mid")
        gen "Not right now..." ("base", xpos="far_left", ypos="head")
        lun "Oh... Then let me know when you're ready..." ("base", "base", "base", "R")

    return

label lun_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.

    ## Unequip top/bottom, 4. Bra/panties, 7##
    ##0-3 Talk, 4-6 inspect, 7-9 masturbate##

    ########################
    ## Default Schoolgirl ##
    ########################
    if item == lun_outfit_default: #Req 0
        gen "Can you put on your regular school uniform for me?" ("base", xpos="far_left", ypos="head")
        gen "Nice and proper please." ("base", xpos="far_left", ypos="head")
        if states.lun.level < 4:
            gen "No wands in your hair... No weird stuff..." ("base", xpos="far_left", ypos="head")
            lun "Weird stuff, [name_genie_luna]?" ("annoyed", "narrow", "base", "mid")
            gen "*Err*... Nothing extra outside the regular uniform, I mean..." ("base", xpos="far_left", ypos="head")
            lun "What about my underwear?" ("angry", "base", "base", "mid")
            gen "Your underwear [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
            lun "I didn't get those with the uniform, so can I still wear them?" ("normal", "base", "base", "mid")
            gen "(Is this girl for real?)" ("base", xpos="far_left", ypos="head")
            lun "[name_genie_luna]?" ("soft", "base", "raised", "mid")
            gen "I guess?" ("base", xpos="far_left", ypos="head")
            lun "Okay, I'll keep them on then." ("grin", "happyCl", "base", "mid")
            gen "(Wait... Taking them off was a real option?)" ("base", xpos="far_left", ypos="head")
        elif states.lun.level < 7:
            lun "Thank you [name_genie_luna]." ("grin", "base", "base", "mid")
            gen "For what?" ("base", xpos="far_left", ypos="head")
            lun "Keeping me safe from the wrackspurts!" ("grin", "wink", "base", "mid")
            gen "That's not..." ("base", xpos="far_left", ypos="head")
            gen "Just put the thing on..." ("base", xpos="far_left", ypos="head")
            lun "Yes, [name_genie_luna]!" ("base", "base", "base", "mid")
        else: #7+
            lun "Do you mean like how the other students wear theirs [name_genie_luna]?" ("soft", "base", "base", "stare")
            gen "... Yes?" ("base", xpos="far_left", ypos="head")
            lun "Will that give the Wrackpurts a harder time getting to me?" ("angry", "wink", "base", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            lun "Is the theory that they won't be able to differentiate me from any of the other girls?" ("open", "base", "raised", "mid")
            gen "*Err*... Sure..." ("base", xpos="far_left", ypos="head")
            lun "Interesting idea [name_genie_luna]... Let's try it." ("base", "base", "base", "mid")

    #######################
    ## Quirky Schoolgirl ##
    #######################
    elif item == lun_outfit_default_quirky: #Req 0
        gen "Can you put on your school uniform for me?" ("base", xpos="far_left", ypos="head")
        gen "And wear it the way you did the first time we met." ("base", xpos="far_left", ypos="head")
        lun "On the day I was sorted into Ravenclaw?" ("open", "base", "raised", "mid")
        lun "I'm not sure I remember how I wore it..." ("open", "base", "base", "down")
        gen "*Err*... No, I meant the one when you came into my office, when you told me about the spurts." ("base", xpos="far_left", ypos="head")
        lun "Oh... Then why didn't you say so!" ("grin", "happyCl", "base", "mid")
        lun "One moment, [name_genie_luna]." ("base", "base", "base", "mid")

    #######################
    ## Slutty Schoolgirl ##
    #######################
    elif item == lun_outfit_school_slut:  #Req 7 (no bra)
        gen "Put on your school uniform for me will you?" ("base", xpos="far_left", ypos="head")
        gen "This one with the tied top and short skirt." ("base", xpos="far_left", ypos="head")
        lun "You're so smart [name_genie_luna]!" ("grin", "wink", "base", "mid")
        gen "I am?" ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "This way you'll get to the affected areas so much quicker!" ("base", "wink", "base", "mid")
        gen "Oh, yes, that's it!" ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "We should make this the standard school uniform!" ("smile", "base", "base", "mid")
        gen "*Hmm*... I'll think about it..." ("base", xpos="far_left", ypos="head")

    ###################
    ## Pyjama Outfit ##
    ###################
    elif item == lun_outfit_pajama: #Req 0
        gen "Put on your pyjamas for me." ("base", xpos="far_left", ypos="head")
        if game.daytime:
            lun "You can do that?" ("angry", "wide", "base", "mid")
            gen "Do what?" ("base", xpos="far_left", ypos="head")
            lun "Wear pyjamas during the day!" ("mad", "narrow", "base", "mid")
            gen "Yes? Why wouldn't you be able to? I'm wearing this robe all the time, and I'm nowhere near a bath." ("base", xpos="far_left", ypos="head")
            lun "If you say so [name_genie_luna]..." ("angry", "base", "base", "mid")
        else:
            lun "My pyjamas?" ("soft", "base", "raised", "mid")
            gen "Yes, [name_luna_genie]... Please put them on for me." ("base", xpos="far_left", ypos="head")
            lun "But, there's no bed in here..." ("angry", "narrow", "base", "mid")
            gen "No bed?" ("base", xpos="far_left", ypos="head")
            lun "Yes, why would I put it on if I'm not going to sleep?" ("angry", "wink", "base", "mid")
            gen "I mean, if you put them on now, there's one less thing to do before you go to bed." ("base", xpos="far_left", ypos="head")
            lun "That's true!" ("grin", "base", "base", "stare")
            lun "I should wear them all the time, then I'd never need to change!" ("base", "base", "base", "mid")
            gen "Well... I wouldn't go that far, just put them on for now." ("base", xpos="far_left", ypos="head")
            lun "Alright, [name_genie_luna]." ("base", "wink", "base", "mid")

    ##################################
    ## Loose-fitting Nightie Outfit ##
    ##################################
    elif item == lun_outfit_nightie1: #Req 7 (no bra, no panties)
        gen "Put on this nightie for me [name_luna_genie]." ("base", xpos="far_left", ypos="head")
        gen "And skip the underwear." ("base", xpos="far_left", ypos="head")
        lun "No underwear [name_genie_luna]?" ("soft", "base", "worried", "mid")
        lun "But what if the wrackspurts get in there?" ("angry", "base", "worried", "mid")
        gen "I'm sure we'll be able to deal with them if that happens, don't you think?" ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "Alright then..." ("grin", "base", "base", "mid")

    ####################
    ## Nightie Outfit ##
    ####################
    elif item == lun_outfit_nightie2: #Req 7 (no bra, no panties)
        gen "Put on this nightie for me [name_luna_genie]." ("base", xpos="far_left", ypos="head")
        gen "And skip the underwear." ("base", xpos="far_left", ypos="head")
        lun "No underwear [name_genie_luna]?" ("soft", "base", "worried", "mid")
        gen "Yes, this way I'll be able to see if the spurts get in there." ("base", xpos="far_left", ypos="head")
        lun "But how are you supposed to see them without the glasses [name_luna_genie]?" ("soft", "base", "base", "mid")
        gen "I'm sure I'd be able to tell if they did, even without the glasses." ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "Alright then..." ("base", "narrow", "base", "mid")

    ######################
    ## Lace Lingerie set##
    ######################
    elif item == lun_outfit_lace1: #Req 7 (bra, panties)
        gen "Put on this lace lingerie for me will you?" ("base", xpos="far_left", ypos="head")
        lun "These are pretty..." ("soft", "base", "base", "down")
        lun "But don't you think the Nargles would try to hide in them?" ("angry", "base", "base", "mid")
        gen "*Err*... Don't you mean the spurts?" ("base", xpos="far_left", ypos="head")
        lun "No [name_genie_luna]...{w=0.4} Nargles loves anything with roses on them..." ("soft", "narrow", "base", "mid")
        lun "Although now that you mention it, Nargles and Wrackspurts don't like each other so perhaps it's a good time to test that theory." ("grin", "base", "base", "mid")

    ########################
    ## Rave Bikini Outfit ##
    ########################
    elif item == lun_outfit_bikini3: #Req 7 (bra, panties)
        gen "I've got a bikini with your name on it." ("base", xpos="far_left", ypos="head")
        lun "You do?" ("soft", "wide", "base", "mid")
        lun "But it's so small... Where does the name even fit?" ("soft", "base", "base", "down")
        gen "Figuratively speaking of course." ("base", xpos="far_left", ypos="head")
        lun "Oh, I see..." ("soft", "narrow", "base", "mid")
        lun "Give me a moment to put it on then..." ("base", "narrow", "base", "mid")

    ##############
    ## Swimsuit ##
    ##############
    elif item == lun_outfit_swimsuit: #Req 7 (no bra, no panties)
        gen "Put on this swimsuit for me will you?" ("base", xpos="far_left", ypos="head")
        lun "But what about the one-eyed trouser snake?" ("angry", "narrow", "base", "mid")
        gen "What?" ("base", xpos="far_left", ypos="head")
        lun "It said in the quibbler that putting on a swimsuit could attract the one-eyed trouser snake." ("clench", "base", "base", "mid")
        gen "The... Oh, I see..." ("base", xpos="far_left", ypos="head")
        gen "(Smut writers and their terrible euphemisms...)" ("base", xpos="far_left", ypos="head")
        gen "*Err*... Didn't the magazine mention that the... *Ahem*... Snake is valuable?" ("base", xpos="far_left", ypos="head")
        lun "It is?" ("angry", "base", "base", "stare")
        gen "Of course, the spit of the one-eyed trouser snake is heavily sought after." ("base", xpos="far_left", ypos="head")
        lun "Really?" ("mad", "base", "base", "mid")
        gen "Certainly... In fact, some people can't get enough of it." ("base", xpos="far_left", ypos="head")
        lun "Oh, I didn't know that!" ("grin", "narrow", "base", "stare")
        lun "You think we could extract some?" ("grin", "base", "base", "mid")
        gen "I'm sure we could if it shows up..." ("base", xpos="far_left", ypos="head")
        lun "Marvellous!" ("smile", "base", "base", "mid")

    ############
    ## Muggle ##
    ############
    elif item == lun_outfit_muggle: #No req
        gen "Put on this maggle outfit for me..." ("base", xpos="far_left", ypos="head")
        lun "Muggle outfit, [name_genie_luna]?" ("soft", "base", "raised", "mid")
        gen "Yes, that's it!" ("base", xpos="far_left", ypos="head")
        lun "I like the skirt!" ("smile", "base", "base", "down")
        gen "Is that sarcasm?" ("base", xpos="far_left", ypos="head")
        lun "No?" ("soft", "base", "base", "mid")
        gen "Then great!" ("base", xpos="far_left", ypos="head")
        lun "Let me just put it on..." ("grin", "base", "base", "mid")

    ######################
    ## Flight Attendant ##
    ######################
    elif item == lun_outfit_flight_attendant: #Req 7 (No Bra, lewd panties)
        gen "Put on this flight attendant outfit for me will you?" ("base", xpos="far_left", ypos="head")
        lun "Flight attendant?" ("soft", "base", "raised", "mid")
        gen "Yeah, it's a job those muggles do." ("base", xpos="far_left", ypos="head")
        lun "There's a job that exists just to attend flying?" ("open", "base", "base", "stare")
        gen "No... Attend people during flight." ("base", xpos="far_left", ypos="head")
        lun "Sounds dangerous..." ("clench", "base", "base", "down")
        gen "(Explaining this to her will probably take all day...)" ("base", xpos="far_left", ypos="head")
        gen "Just forget what it's for, it's not essential for your education..." ("base", xpos="far_left", ypos="head")
        lun "Oh... Alright then." ("angry", "base", "base", "mid")
        lun "..." ("base", "base", "base", "R")
        gen "I still want you to put it on though..." ("base", xpos="far_left", ypos="head")
        lun "Oh, Alright!" ("grin", "base", "base", "mid")

    ############
    ## Summer ##
    ############
    elif item == lun_outfit_summer: #Req 7 (No Bra)
        gen "I've got this great summer outfit for you to wear!" ("base", xpos="far_left", ypos="head")
        gen "It's pretty hot!" ("base", xpos="far_left", ypos="head")
        if game.daytime:
            lun "It is? I didn't notice!" ("angry", "base", "base", "stare")
            gen "Weather's pretty warm too!" ("base", xpos="far_left", ypos="head")
            lun "*Huh*?" ("soft", "base", "base", "mid")
            gen "Better put this on right away!" ("base", xpos="far_left", ypos="head")
        else:
            lun "It is? But the sun isn't even out!" ("angry", "base", "base", "L")
            gen "What I meant was... Tomorrow might be hot! So better put it on now!" ("base", xpos="far_left", ypos="head")
        lun "Oh, alright then!" ("angry", "base", "base", "mid")

    ############
    ## Casual ##
    ############
    elif item == lun_outfit_casual: #Req 0
        gen "Could you put on something more casual?" ("base", xpos="far_left", ypos="head")
        lun "Casual, [name_genie_luna]?" ("soft", "base", "raised", "mid")
        gen "Yeah, something that doesn't show too much skin." ("base", xpos="far_left", ypos="head")
        gen "(What the hell is wrong with me?)" ("base", xpos="far_left", ypos="head")
        lun "Oh, of course, I could put on my Casual clothing." ("grin", "base", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")


    #################
    ## Party Dress ##
    #################
    elif item == lun_outfit_party: #Req 7 (No Bra)
        gen "This dress seems odd enough to suit you." ("base", xpos="far_left", ypos="head")
        gen "Why don't you put it on?" ("base", xpos="far_left", ypos="head")
        lun "Odd [name_genie_luna]?" ("angry", "narrow", "base", "mid")
        gen "In a good way..." ("base", xpos="far_left", ypos="head")
        lun "I love it!" ("grin", "base", "base", "down")
        lun "I've got the same one at home!" ("smile", "happyCl", "base", "mid")
        gen "You... You do?" ("base", xpos="far_left", ypos="head")
        lun "I do!" ("grin", "wink", "base", "mid")
        gen "(Didn't that Mafkin lady make this outfit?)" ("base", xpos="far_left", ypos="head")
        gen "(Must've been too hard even for her to create something like this...)" ("base", xpos="far_left", ypos="head")
        lun "One moment, let me put it on." ("base", "base", "base", "mid")

    #########################
    ## Harley Quinn Outfit ##
    #########################
    elif item == lun_outfit_harley_quinn: # Req 7 (No Bra, No Panties)
        gen "I've got this Harley Quinn costume for you to wear." ("base", xpos="far_left", ypos="head")
        lun "*Hmm*?" ("soft", "base", "base", "mid")
        lun "Harley Quinn?" ("open", "base", "raised", "mid")
        gen "Yes, you know, the super villain... *Err*... Villainess." ("base", xpos="far_left", ypos="head")
        lun "*Huh*?" ("normal", "base", "raised", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "(Guess she's one of those marvel fans...)" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Put it on and call me puddin'!)\"":
                $ name_genie_luna = "Puddin'"
                lun "Puddin'?" ("soft", "base", "base", "mid")
                gen "Yes?" ("base", xpos="far_left", ypos="head")
                lun "Alright then..." ("base", "base", "base", "mid")
            "\"(Just put it on!)\"":
                lun "Alright..." ("base", "base", "base", "mid")

    ###########################
    ## Police Officer Outfit ##
    ###########################
    elif item == lun_outfit_police: #Req 7 (No Bra)
        gen "Put on the police cosplay uniform will you?" ("base", xpos="far_left", ypos="head")
        lun "Police costume?" ("soft", "base", "raised", "mid")
        gen "Yeah..." ("base", xpos="far_left", ypos="head")
        gen "Gotta maintain some order around here." ("base", xpos="far_left", ypos="head")
        lun "Oh... Are police some kind of muggle law enforcer?" ("open", "base", "base", "stare")
        gen "Yes they--" ("base", xpos="far_left", ypos="head")
        gen "Surely the governmental forces of the world are prevalent enough for you to know what the police are?" ("base", xpos="far_left", ypos="head")
        lun "Like, the ministry of magic?" ("upset", "base", "base", "mid")
        gen "(This is just plain ignorance at this point...)" ("base", xpos="far_left", ypos="head")
        gen "Just put it on, will you?" ("base", xpos="far_left", ypos="head")
        lun "Alright." ("base", "base", "base", "mid")

    ###################
    ## Bunny Costume ##
    ###################
    elif item == lun_outfit_bunny: #Req 7 (No underwear)
        gen "Put on this bunny costume for me, will you?" ("base", xpos="far_left", ypos="head")
        lun "A bunny!" ("smile", "base", "base", "stare")
        lun "I love bunnies!" ("smile", "happyCl", "base", "mid")
        gen "Great!" ("grin", xpos="far_left", ypos="head")
        lun "They're so cute--" ("grin", "happyCl", "base", "mid")
        gen "So you'll--" ("base", xpos="far_left", ypos="head")
        lun "So fluffy--" ("grin", "happyCl", "base", "mid")
        gen "I'm glad you--" ("base", xpos="far_left", ypos="head")
        lun "And I love when they hug your leg!" ("smile", "base", "base", "mid")
        gen "...{w=0.2} I don't think--" ("base", xpos="far_left", ypos="head")
        lun "Even my patronus is shaped like a hare!" ("smile", "narrow", "base", "mid")
        gen "Just put on the costume, will you?" ("base", xpos="far_left", ypos="head")
        lun "Okay!" ("grin", "base", "base", "mid")

    ######################
    ## Reindeer Costume ##
    ######################
    elif item ==lun_outfit_reindeer: #Req 7 (No underwear)
        gen "Put on this reindeer costume for me, will you?" ("base", xpos="far_left", ypos="head")
        lun "A Christmas reindeer costume!" ("grin", "base", "base", "mid")
        gen "That's right!" ("base", xpos="far_left", ypos="head")
        lun "Hold on!" ("angry", "base", "base", "mid")
        lun "There's a hole with a mistletoe above it!" ("clench", "base", "base", "mid")
        gen "So?" ("base", xpos="far_left", ypos="head")
        lun "That's where the nargles like to hide!" ("angry", "base", "worried", "mid")
        lun "I can't wear this!" ("angry", "happyCl", "worried", "mid")
        gen "Bloody--" ("base", xpos="far_left", ypos="head")
        lun "Unless..." ("mad", "base", "base", "stare")
        gen "Unless?" ("base", xpos="far_left", ypos="head")
        lun "Are you implying that the hole will draw in the wrackspurts, just so the nargles could ambush them?" ("angry", "base", "base", "mid")
        gen "*Err*... Sure!" ("base", xpos="far_left", ypos="head")
        lun "That's brilliant!" ("smile", "base", "base", "mid")
        lun "Let me put it on." ("grin", "base", "base", "mid")
    # TODO: Blacklist fallbacks have to be added.
    return

label lun_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.

    #######################
    ## Slutty Schoolgirl ##
    #######################
    if item == lun_outfit_school_slut:  #Req 7 (no bra)
        gen "Put on your school uniform for me will you?" ("base", xpos="far_left", ypos="head")
        gen "This one with the tied top and short skirt." ("base", xpos="far_left", ypos="head")
        lun "But [name_genie_luna]!" ("angry", "wide", "base", "mid")
        lun "This doesn't have a bra!" ("angry", "wide", "base", "mid")
        gen "So?" ("base", xpos="far_left", ypos="head")
        lun "Surely I shouldn't be standing here without a bra on?" ("mad", "narrow", "base", "mid")
        if states.lun.level < 4:
            gen "(Maybe I've gone too far...)" ("base", xpos="far_left", ypos="head")
            lun "The wrackpurts would most certainly get to me!" ("angry", "closed", "base", "mid")
            gen "Right..." ("base", xpos="far_left", ypos="head")
            gen "(Maybe I could convince her once we've found a way to deal with them...)" ("base", xpos="far_left", ypos="head")
        else:
            gen "Why not?" ("base", xpos="far_left", ypos="head")
            lun "If I stood here for too long without a bra, then I don't doubt they'd get to me!" ("angry", "closed", "worried", "mid")
            gen "Who?" ("base", xpos="far_left", ypos="head")
            lun "The Wrackspurts!" ("angry", "wink", "base", "mid")
            gen "Oh..." ("base", xpos="far_left", ypos="head")
            gen "(Maybe I could convince her once she's more confident about dealing with the spurts...)" ("base", xpos="far_left", ypos="head")

    ##################################
    ## Loose-fitting Nightie Outfit ##
    ##################################
    elif item == lun_outfit_nightie1: #Req 7 (no bra, no panties)
        gen "Put on this nightie for me [name_luna_genie]." ("base", xpos="far_left", ypos="head")
        gen "And skip the underwear." ("base", xpos="far_left", ypos="head")
        if states.lun.level < 4:
            lun "But [name_genie_luna]!" ("angry", "wide", "base", "mid")
            lun "The wrackpurts would be able to get in there if I were to not wear any underwear." ("clench", "wink", "base", "mid")
            gen "I'm sure we'll be able to deal with that if it comes down to it..." ("base", xpos="far_left", ypos="head")
            lun "*Hmm*... I'm not so sure about that..." ("disgust", "base", "base", "mid")
        else:
            lun "Is this part of the inspection?" ("soft", "narrow", "base", "mid")
            gen "Yes... Well, you see, the spurts... *Err*..." ("base", xpos="far_left", ypos="head")
            lun "[name_genie_luna]... I'd rather not make myself a target of those things, standing here without underwear would surely bring them all to attention." ("angry", "wink", "base", "mid")
            gen "It'd bring something to attention, that's for sure." ("base", xpos="far_left", ypos="head")
            lun "Alright, then I better not." ("angry", "narrow", "base", "mid")
            gen "Wait, I was only--" ("base", xpos="far_left", ypos="head")
            gen "(Dammit...)" ("base", xpos="far_left", ypos="head")

    ####################
    ## Nightie Outfit ##
    ####################
    elif item == lun_outfit_nightie2: #Req 7 (no bra, no panties)
        gen "Put on this nightie for me [name_luna_genie]." ("base", xpos="far_left", ypos="head")
        gen "And skip the underwear." ("base", xpos="far_left", ypos="head")
        if states.lun.level < 4:
            lun "But [name_genie_luna]!" ("angry", "wide", "base", "mid")
            lun "What about the Wrackspurts?" ("clench", "wink", "base", "mid")
            gen "What do you mean, what about the spurts?" ("base", xpos="far_left", ypos="head")
            lun "They'll be able to get in there if I'm not wearing any underwear!" ("clench", "base", "base", "mid")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            gen "(Doesn't she mean, get out?)" ("base", xpos="far_left", ypos="head")
            lun "I think it's probably best if I keep myself protected..." ("disgust", "base", "base", "mid")
        else:
            lun "Is this part of the inspection?" ("soft", "narrow", "base", "mid")
            gen "Yes... Well, you see, the spurts... *Err*..." ("base", xpos="far_left", ypos="head")
            lun "[name_genie_luna]... Don't you think they'd easily be able to fly in there if I'm not wearing any underwear?" ("angry", "wink", "base", "mid")
            gen "I don't see how that's a problem, it feels nice, does it not?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "*Ehm*... Does that matter?" ("soft", "narrow", "base", "mid")
            gen "(Is there even a right answer here?)" ("base", xpos="far_left", ypos="head")
            menu:
                "\"No.\"":
                    lun "That's what I thought... I better keep myself safe then..." ("soft", "narrow", "base", "R")
                    gen "Right... Wait, what was the question?" ("base", xpos="far_left", ypos="head")
                    lun "..." ("soft", "base", "base", "mid")
                "\"Yes.\"":
                    lun "Are you alright [name_genie_luna]?" ("angry", "narrow", "base", "mid")
                    gen "Never been better, why?" ("base", xpos="far_left", ypos="head")
                    lun "*Hmm*... Are you sure the wrackspurts haven't affected your brain?" ("annoyed", "narrow", "base", "mid")
                    gen "Doubt it... Although people do tell me I think with my penis sometimes." ("base", xpos="far_left", ypos="head")
                    lun "Surely it's not a good idea to give them an open landing strip." ("soft", "narrow", "base", "mid")
                    gen "We'll just deal with it if it happens." ("base", xpos="far_left", ypos="head")
                    lun "*Hmm*... I'm not so sure about that." ("annoyed", "narrow", "base", "R")
                    gen "Well, that's your loss [name_luna_genie]..." ("base", xpos="far_left", ypos="head")
            gen "(Damn... Maybe I'll be able to convince her once she's more confident about dealing with them.)" ("base", xpos="far_left", ypos="head")

    ######################
    ## Lace Lingerie set##
    ######################
    elif item == lun_outfit_lace1: #Req 7 (bra, panties)
        gen "Put on this lace lingerie for me will you?" ("base", xpos="far_left", ypos="head")
        lun "But [name_genie_luna]!" ("mad", "base", "base", "down")
        lun "These got roses on them!" ("angry", "narrow", "base", "down")
        gen "So?" ("base", xpos="far_left", ypos="head")
        lun "The Nargles would surely try and hide in them if I put this on!" ("clench", "happyCl", "base", "mid")
        gen "(How many of these made up things does she believe in?)" ("base", xpos="far_left", ypos="head")

    ########################
    ## Rave Bikini Outfit ##
    ########################
    elif item == lun_outfit_bikini3: #Req 7 (bra, panties)
        gen "Put on this bikini for me will you?" ("base", xpos="far_left", ypos="head")
        lun "I'm sorry [name_genie_luna] but I can't wear this right now." ("upset", "narrow", "base", "down")
        gen "Why not?" ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "Oh... *Ehm*..." ("soft", "narrow", "base", "down")
        lun @ cheeks blush "I'd rather we continue with our research..." ("angry", "closed", "base", "mid")
        nar "You watch as Luna grinds her legs together."
        gen "I see... Some other time then, perhaps." ("base", xpos="far_left", ypos="head")

    ##############
    ## Swimsuit ##
    ##############
    elif item == lun_outfit_swimsuit: #Req 7 (no bra, no panties)
        gen "I've got a swimsuit for you to wear." ("base", xpos="far_left", ypos="head")
        lun "Are we going swimming?" ("soft", "narrow", "raised", "mid")
        gen "No, I just thought you could wear it in here." ("base", xpos="far_left", ypos="head")
        lun "Inside?" ("angry", "base", "base", "stare")
        gen "*Err*... Yes?" ("base", xpos="far_left", ypos="head")
        lun "..." ("soft", "wide", "base", "stare")
        gen "Hello?" ("base", xpos="far_left", ypos="head")
        lun "..." ("soft", "wide", "base", "stare")
        gen "(I think I just blew her mind...)" ("base", xpos="far_left", ypos="head")
        gen "[name_luna_genie]?" ("base", xpos="far_left", ypos="head")
        lun "..." ("soft", "wide", "base", "stare")
        gen "[name_luna_genie]!" ("base", xpos="far_left", ypos="head")
        lun "Oh, sorry [name_genie_luna] what did you say?" ("angry", "wide", "base", "mid")
        gen "Nevermind... Forget it." ("base", xpos="far_left", ypos="head")

    ######################
    ## Flight Attendant ##
    ######################
    elif item == lun_outfit_flight_attendant: #Req 7 (No Bra)
        gen "Put on this flight attendant outfit for me will you?" ("base", xpos="far_left", ypos="head")
        lun "But [name_genie_luna], I'd have to take off my bra for this!" ("mad", "wide", "base", "mid")
        gen "So?" ("base", xpos="far_left", ypos="head")
        lun "Haven't you heard of the nipple biting mouth suckers?!" ("clench", "base", "base", "mid")
        gen "Oh, yes, of course I have!" ("base", xpos="far_left", ypos="head")
        gen "Although perhaps you could remind me..." ("base", xpos="far_left", ypos="head")
        lun "The plant... Professor Sprout told us to watch out for them, as they're quite rowdy this time of year." ("angry", "wink", "base", "mid")
        gen "Rowdy you say?" ("base", xpos="far_left", ypos="head")
        lun "Yes, she's showed me a great many times how dangerous they can be around nipples." ("angry", "closed", "base", "mid")
        gen "I see..." ("base", xpos="far_left", ypos="head")

    ############
    ## Summer ##
    ############
    elif item == lun_outfit_summer: #Req 7 (No Bra)
        gen "I've got this summer outfit for you to put on." ("base", xpos="far_left", ypos="head")
        gen "Since it's pretty hot you should probably wear it without your bra on." ("base", xpos="far_left", ypos="head")
        lun "Take off my bra?" ("soft", "base", "base", "mid")
        lun "Well that might be a problem..." ("upset", "base", "base", "down")
        gen "Why's that?" ("base", xpos="far_left", ypos="head")
        lun "Well... It's a bit embarrassing actually..." ("angry", "narrow", "base", "R")
        lun "My latch got stuck on it..." ("disgust", "base", "base", "downL")
        gen "Your... latch?" ("base", xpos="far_left", ypos="head")
        lun "Yes [name_genie_luna]..." ("angry", "base", "worried", "mid")
        gen "Sounds more like artificial content gating to me..." ("base", xpos="far_left", ypos="head")
        lun "Sorry?" ("angry", "base", "raised", "mid")
        gen "Don't worry... They know what I meant..." ("base", xpos="far_left", ypos="head")
        lun "*Hmm*..." ("normal", "base", "base", "R")

    #################
    ## Party Dress ##
    #################
    elif item == lun_outfit_party: #Req 7 (No Bra)
        gen "I've got the perfect dress for you to wear!" ("base", xpos="far_left", ypos="head")
        lun "Really? Exciting!" ("grin", "base", "base", "mid")
        gen "Yes, I can't wait to see what your nipples will look like in this!" ("base", xpos="far_left", ypos="head")
        lun "My... Nipples [name_genie_luna]?" ("soft", "wink", "base", "mid")
        gen "Yes, you'd have to take your bra off for this one... It's the only way." ("base", xpos="far_left", ypos="head")
        lun "*Hmm*... I'm not sure that's the proper way of wearing a dress..." ("soft", "wink", "base", "mid")
        gen "What do you--" ("base", xpos="far_left", ypos="head")
        gen "(Since when did she start caring about how to wear clothes properly?)" ("base", xpos="far_left", ypos="head")

    #########################
    ## Harley Quinn Outfit ##
    #########################
    elif item == lun_outfit_harley_quinn: # Req 7 (No Bra, No Panties)
        gen "I've got this Harley Quinn costume for you to wear." ("base", xpos="far_left", ypos="head")
        lun "*Hmm*?" ("soft", "base", "raised", "mid")
        lun "Harley Quinn?" ("open", "base", "raised", "mid")
        gen "Yes, she's--" ("base", xpos="far_left", ypos="head")
        lun "But sir, this costume has no underwear!" ("angry", "wide", "base", "mid")
        lun "Surely, I can't go around without any on!" ("mad", "happyCl", "base", "mid")
        gen "Why not?" ("base", xpos="far_left", ypos="head")
        lun "The wrack--" ("angry", "wide", "base", "mid")
        gen "Not those things again!" ("base", xpos="far_left", ypos="head")

    ###########################
    ## Police Officer Outfit ##
    ###########################
    elif item == lun_outfit_police: #Req 7 (No Bra)
        gen "Put on the police cosplay uniform will you?" ("base", xpos="far_left", ypos="head")
        lun "Police?" ("soft", "base", "raised", "mid")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        lun "I'm not sure what that is..." ("upset", "narrow", "raised", "mid")
        gen "What do you--" ("base", xpos="far_left", ypos="head")
        gen "I'm talking about this kind of uniform..." ("base", xpos="far_left", ypos="head")
        lun "Oh!!" ("open", "wide", "base", "mid")
        gen "(Now she's got it...)" ("base", xpos="far_left", ypos="head")
        lun "But [name_genie_luna]... This outfit doesn't have a bra!" ("clench", "narrow", "base", "mid")
        gen "I'm sure the outfit is tight enough to keep them contained, don't you think?" ("base", xpos="far_left", ypos="head")
        lun "I'm more worried about what could find its way into it..." ("annoyed", "narrow", "base", "down")
        gen "(And here I thought she wanted some hands-on experience.)" ("base", xpos="far_left", ypos="head")
        lun "(Can't let those wrackspurts get to me...)" ("disgust", "narrow", "base", "R")

    ###################
    ## Bunny Costume ##
    ###################
    elif item == lun_outfit_bunny: #Req 7 (No Underwear)
        gen "I've got this bunny costume for you to wear." ("base", xpos="far_left", ypos="head")
        lun "Oooooh! I love bunnies!" ("grin", "base", "base", "mid")
        gen "Great, here you go!" ("grin", xpos="far_left", ypos="head")
        lun "Hold on... Is this everything?" ("angry", "base", "base", "mid")
        gen "*Err*... Yes?" ("base", xpos="far_left", ypos="head")
        lun "But, there are no paws!" ("clench", "base", "base", "mid")
        gen "Paws?" ("base", xpos="far_left", ypos="head")
        lun "Yes! And no whiskers either!" ("angry", "base", "base", "mid")
        gen "No--{w=0.2} It's not that kind of costume!" ("base", xpos="far_left", ypos="head")
        lun "Oh..." ("upset", "narrow", "worried", "down")
        gen "So, will you--" ("base", xpos="far_left", ypos="head")
        lun "*Sigh*..." ("upset", "narrow", "worried", "down") #Sad
        gen "(I'll just ask again some other time...)" ("base", xpos="far_left", ypos="head")

    ######################
    ## Reindeer Costume ##
    ######################
    elif item == lun_outfit_reindeer: #Req 7 (No Underwear)
        gen "I've got this reindeer costume for you to wear." ("base", xpos="far_left", ypos="head")
        lun "Oh! Like a Christmas reindeer!" ("grin", "base", "raised", "mid")
        gen "Well, I don't think the existence of the animal relies on the holiday--" ("base", xpos="far_left", ypos="head")
        lun "..." ("grin", "base", "base", "mid")
        gen "Yes, like a Christmas reindeer..." ("base", xpos="far_left", ypos="head")
        lun "Yay!" ("smile", "happyCl", "base", "mid")
        lun "Let me see the costume!" ("smile", "base", "base", "mid")
        gen "Here you go!" ("base", xpos="far_left", ypos="head")
        lun "Ooh! This is so--" ("grin", "narrow", "base", "down")
        lun "Hold on! There's a hole in it!" ("clench", "narrow", "base", "down")
        gen "Yes, but it's meant to be--" ("base", xpos="far_left", ypos="head")
        lun "I can't wear this." ("angry", "base", "base", "mid")
        gen "What! Why not?" ("base", xpos="far_left", ypos="head")
        lun "If your clothing's got a hole, you should make sure to return it for refund or replacement!" ("open", "closed", "base", "mid")
        lun "That's what my dad always told me!" ("grin", "base", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "(I am not going to attempt explaining this to her now...)" ("base", xpos="far_left", ypos="head")
        gen "(Maybe she'll forget about it later...)" ("base", xpos="far_left", ypos="head")

    else:
        lun "This outfit seems to have wrackspurts all over it!" ("mad", "base", "base", "down")
        gen "(I don't remember cumming on this piece of garment...)" ("base", xpos="far_left", ypos="head")
        gen "(!!!)" ("angry", xpos="far_left", ypos="head")
        gen "(Could it be--...)" ("angry", xpos="far_left", ypos="head")
        lun "Are you okay [name_genie_luna]? You look pale." ("angry", "base", "raised", "mid")
        gen "Yes, I'm fine. I guess you can stay in your clothes... for now." ("base", xpos="far_left", ypos="head")

    return

label lun_reaction_blacklist(item):
    lun "Will that really help? With the wrackspurts, I mean." ("soft", "narrow", "base", "mid")

    if "top" in item.blacklist and luna.is_worn("top"):
        lun "I would need to remove my top." ("open", "base", "base", "down")

    if "bottom" in item.blacklist and luna.is_worn("bottom"):
        lun "I don't think I could wear bottoms with this..." ("upset", "narrow", "base", "down")

    if "bra" in item.blacklist and luna.is_worn("bra"):
        lun "It seems no bra can fit in this garment." ("open", "base", "base", "down")

    if "panties" in item.blacklist and luna.is_worn("panties"):
        lun "The Wrackspurts would have a feast as I would not be able to wear panties with this." ("upset", "narrow", "base", "down")

    gen "Trust me, I know what I'm doing." ("base", xpos="far_left", ypos="head")
    lun "If you say so [name_genie_luna]." ("base", "base", "base", "mid")

    return

label lun_reaction_fallback(item):
    if states.lun.level < get_character_requirement("luna", "unequip top") and not "top" in luna.blacklist and not item.type == "top":
        $ luna.equip(lun_top_school1)

    if states.lun.level < get_character_requirement("luna", "unequip bottom") and not "bottom" in luna.blacklist and not item.type == "bottom":
        $ luna.equip(lun_top_school2)

    if states.lun.level < get_character_requirement("luna", "unequip bra") and not "bra" in luna.blacklist and not item.type == "bra":
        $ luna.equip(lun_bra_base1)

    if states.lun.level < get_character_requirement("luna", "unequip panties") and not "panties" in luna.blacklist and not item.type == "panties":
        $ luna.equip(lun_panties_base1)

    lun "Just give me a second, I need to get my clothes back in order." ("open", "base", "base", "R")
    lun "" ("base", "base", "base", "mid")
    return
