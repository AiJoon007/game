define cho_requirements = {
    "category upper undergarment": 5,
    "category lower undergarment": 5,
    "category piercings & tattoos": 16,
    "touch head": 4,
    "touch breasts": 10, #Start of Gryffindor match leadup tier
    "touch vagina": 15, #Highest level of Gryffindor match leadup tier
    "unequip panties": 15,
    "unequip bra": 15,
    "unequip top": 4,
    "unequip bottom": 4,
    }

define cho_responses = {
    "category_fail": "cho_reaction_category_fail",
    "equip": "cho_reaction_equip",
    "equip_fail": "cho_reaction_equip_fail",
    "unequip": "cho_reaction_unequip",
    "unequip_fail": "cho_reaction_unequip_fail",
    "touch": "cho_reaction_touch",
    "touch_fail": "cho_reaction_touch_fail",
    "equip_outfit": "cho_reaction_equip_outfit",
    "equip_outfit_fail": "cho_reaction_equip_outfit_fail",
    "blacklist": "cho_reaction_blacklist",
    "fallback": "cho_reaction_fallback",
}

label cho_reaction_category_fail(category):

    if category == "upper undergarment":
        random:
            block:
                cho "You want to pick my underwear?" ("disgust", "narrow", "angry", "mid")
                cho "I don't think so." ("open", "narrow", "angry", "R")

            cho "Unless we're doing exercises, I don't see why you want me to change my underwear..." ("disgust", "base", "angry", "R")
            cho "I'm perfectly fine with the underwear I'm already wearing, thank you..." ("base", "base", "base", "mid")
    elif category == "lower undergarment":
        random:
            block:
                cho "My underwear?" ("disgust", "base", "raised", "mid")
                cho "Why do you want me to change them exactly?" ("angry", "narrow", "angry", "mid")

            block:
                cho "Are we doing something that requires me to change my underwear?" ("annoyed", "narrow", "raised", "mid")
                gen "I just thought I could pick some for you to wear." ("base", xpos="far_left", ypos="head")
                cho "Well... You thought wrong." ("upset", "narrow", "angry", "mid")

            cho @ cheeks blush "*Err*... You want me to do what?" ("disgust", "base", "angry", "mid")
    elif category == "piercings & tattoos":
        random:
            cho "Yeah, that's not happening..." ("annoyed", "narrow", "angry", "R")
            cho "No, thank you..." ("annoyed", "narrow", "base", "mid")
            cho "My body is already perfect without such things..." ("smile", "closed", "base", "mid")

    return

label cho_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()

        if states.cho.level < 10: #Pre Slytherin match (after hufflepuff match)
            random:
                cho "Are you measuring my height or something?" ("annoyed", "narrow", "base", "mid")
                cho "Is this supposed to encourage me?" ("disgust", "closed", "base", "mid")
                cho "You'd usually only pet a dog when they do well with their training, you know that, right?" ("open", "narrow", "raised", "mid")
                cho "What next? A treat?" ("soft", "narrow", "base", "R")
        elif states.cho.level < 16: # Pre Gryffindor match (after Slytherin match)
            random:
                cho @ cheeks blush "*Hmm*... Well, I suppose this is fine... You did help me beat those Slytherins after all." ("soft", "closed", "base", "mid")
                cho @ cheeks blush "Thank you, but don't we have other things to focus on?" ("open", "narrow", "base", "R")

                block:
                    cho @ cheeks blush "Yes, I do believe I've deserved some praise..." ("base", "base", "base", "mid")
                    cho @ cheeks blush "Although petting is a bit out there as a reward..." ("soft", "base", "base", "R")
        elif states.cho.level < 22: #Post Gryffindor match (start of tier)
            random:
                cho @ cheeks blush "I could get used to this..." ("base", "narrow", "base", "R")
                cho @ cheeks blush "Thank you [name_genie_cho]..." ("open", "narrow", "base", "down")

                block:
                    cho @ cheeks blush "Is this supposed to be my reward, [name_genie_cho]?" ("soft", "narrow", "base", "mid")
                    cho @ cheeks blush "I was expecting more coming from you..." ("open", "narrow", "base", "downR")
        else: #22+ #Post Gryffindor match (end of tier)
            random:
                cho @ cheeks blush "Are you sure there isn't anywhere else you could distribute that praise?" ("smile", "narrow", "base", "mid")
                cho @ cheeks blush "I'm glad you're so proud of me [name_genie_cho]..." ("base", "narrow", "base", "mid")
                cho @ cheeks blush "*Mmm*..." ("horny", "closed", "base", "mid")


    elif what == "breasts":
        $ mouse_heart()

        if states.cho.level < 16: # Before Gryffindor match
            random:
                cho @ cheeks blush "Kissing them for good luck are we?" ("smile", "narrow", "base", "mid")

                block:
                    cho "*Mmm*..." ("horny", "closed", "base", "mid")
                    cho @ cheeks blush "..." ("disgust", "narrow", "base", "mid")
                block:
                    cho @ cheeks blush "My Quaffles are quite perfect aren't they?" ("grin", "narrow", "base", "mid")
                    cho @ cheeks heavy_blush "*Ugh*... Why did I just call them that..." ("disgust", "narrow", "base", "downR")
                block:
                    cho @ cheeks blush "*Mmm*... Feel how firm those bad girls are?" ("base", "narrow", "base", "mid")
                    cho @ cheeks blush "That's the reward from years of hard training..." ("grin", "closed", "base", "mid")
        else:
            random:
                cho "*Mmm*..." ("horny", "closed", "base", "mid")
                cho @ cheeks blush "Thank you [name_genie_cho]..." ("soft", "narrow", "base", "mid")
                cho @ cheeks blush "Glad you appreciate them as much as I do..." ("smile", "wink", "base", "mid")

    elif what == "vagina":
        $ mouse_heart()

        if states.cho.level < 16: #Before Gryffindor match
            random:
                cho @ cheeks blush "*Hmm*... I can appreciate a man who goes for what he wants no matter what..." ("base", "narrow", "base", "mid")
                cho @ cheeks blush "Such speed... Fancy yourself a seeker, do you?" ("smile", "narrow", "base", "mid")
                cho @ cheeks blush "*Hmm*... Surely such a move must count as a foul..." ("smile", "wink", "base", "mid")
        else:
            random:
                block:
                    cho @ cheeks blush "Found one of the goal posts did you?" ("base", "narrow", "base", "mid")
                    cho @ cheeks blush "There's two more you know..." ("smile", "wink", "base", "mid")

                cho @ cheeks blush "Careful or I might lock my thighs around your neck and keep you there..." ("soft", "narrow", "base", "mid")


    return

label cho_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        random:
            cho "Don't touch my hair..." ("clench", "base", "base", "mid")
            cho "Bad [name_genie_cho]..." ("annoyed", "base", "angry", "mid")
            cho "No touch!" ("open", "closed", "angry", "mid")
            cho "Don't...{w=0.4} Pet...{w=0.4} me..." ("soft", "narrow", "angry", "mid")

    elif what == "breasts":
        $ mouse_slap()

        random:
            block:
                cho "[name_genie_cho]?!" ("mad", "base", "angry", "mid")
                cho "This isn't a part of our training..." ("clench", "base", "angry", "mid")
            cho "Nice try..." ("smile", "narrow", "angry", "mid")
            cho "What are you doing?!" ("disgust", "wide", "base", "mid")
            cho "Too slow..." ("crooked_smile", "narrow", "angry", "mid")

    elif what == "vagina":
        $ mouse_slap()

        random:
            cho "Hands where I can see them!" ("angry", "base", "angry", "mid")
            cho "You'd have to be a lot faster to get even close to getting away with that..." ("crooked_smile", "narrow", "angry", "mid")
            cho "Nice try..." ("soft", "narrow", "angry", "mid")
            cho "No foul plays, [name_genie_cho]..." ("angry", "narrow", "angry", "mid")

    return

label cho_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     cho "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label cho_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     cho "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    random:
        cho "There's no way I would wear that." ("upset", "narrow", "angry", "mid")
        cho "I am not wearing that..." ("upset", "closed", "base", "mid")

        block:
            cho "Put it on yourself..." ("open", "base", "angry", "mid")
            gen "I don't think it would fit." ("base", xpos="far_left", ypos="head")
            cho "Well, tough luck..." ("annoyed", "narrow", "angry", "R")

        block:
            cho "Ask Granger to wear it, why don't you..." ("open", "closed", "angry", "mid")
            gen "It's made for your size." ("base", xpos="far_left", ypos="head")
            cho "What is that supposed to mean?" ("soft", "base", "angry", "mid")
            gen "..." ("angry", xpos="far_left", ypos="head")

    return

label cho_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if states.cho.level > 15:
    #        cho "You want to see my snatch?"
    #        cho "You got it [name_genie_hermione]!"
    #
    return

label cho_reaction_unequip_fail(item):
    if item.type == "panties":

        random:
            block:
                cho "You want me to take off my underwear?" ("upset", "narrow", "angry", "mid")
                cho @ cheeks blush "How is that supposed to help with my training?" ("open", "closed", "angry", "mid")
            block:
                cho "You want me to stand here without underwear?" ("disgust", "narrow", "base", "mid")
                cho "Yeah, in your dreams [name_genie_cho]..." ("annoyed", "narrow", "angry", "R")
            block:
                cho "Take your own underwear off, why don't you..." ("disgust", "narrow", "angry", "mid")
                gen "What's to say I'm wearing any?" ("base", xpos="far_left", ypos="head")
                cho "..." ("angry", "closed", "angry", "mid")

    elif item.type == "bra":
        random:
            cho @ cheeks blush "I bet that Gryffindor cow happily stands here with her tits out, but that doesn't mean I will..." ("disgust", "base", "angry", "R")

            block:
                cho @ cheeks blush "You want me to flash you my tits?" ("angry", "wide", "base", "mid")
                gen "I want you to take it off and keep it off..." ("base", xpos="far_left", ypos="head")
                cho "No way!" ("clench", "narrow", "angry", "mid")

    elif item.type == "top":
        cho "I'm sorry if you don't like my choice of clothes, [name_genie_cho]..." ("annoyed", "narrow", "angry", "R")

    elif item.type == "bottom":
        cho "I'm sorry if you don't like my choice of clothes, [name_genie_cho]..." ("open", "narrow", "angry", "downR")
    return

label cho_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.

    ########################
    ## Default Schoolgirl ##
    ########################
    if item == cho_outfit_default:
        gen "Could you put on your normal school uniform?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Sure." ("soft", "base", "base", "mid")
            cho "Let me just go change real quick." ("open", "base", "base", "R")
        elif states.cho.level < 10:
            cho "My regular school uniform?" ("open", "narrow", "raised", "mid")
            gen "That's the one." ("base", xpos="far_left", ypos="head")
            cho "Alright, give me a moment..." ("soft", "narrow", "base", "mid")
        elif states.cho.level < 16:
            cho "With the vest and all?" ("soft", "narrow", "raised", "mid")
            gen "Yep." ("base", xpos="far_left", ypos="head")
            cho "*Hmm*...{w=0.3} Is this some sort of trick?" ("annoyed", "narrow", "raised", "mid")
            gen "Nope, I just like keeping up the traditions." ("base", xpos="far_left", ypos="head")
            cho "Yeah right..." ("open", "narrow", "base", "R")
            gen "..." ("base", xpos="far_left", ypos="head")
            cho "Oh, You were serious! Okay then..." ("disgust", "narrow", "base", "mid")
        else: #16+
            cho "*Hmm*...{w=0.3} It's a bit constricting..." ("annoyed", "narrow", "base", "down")
            gen "In what way?" ("base", xpos="far_left", ypos="head")
            cho "You know...{w=0.3} The tie and all..." ("soft", "narrow", "base", "mid")
            gen "I don't get it..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Never mind..." ("open", "narrow", "base", "down")

    ###############################
    ## Clear Day (School no vest)##
    ###############################
    elif item == cho_outfit_s_clearday:
        gen "Could you wear your school uniform for me? But leave the vest off." ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Leave the vest off?" ("soft", "base", "raised", "mid")
            gen "Yes please." ("base", xpos="far_left", ypos="head")
            cho "Alright then, if you say so [name_genie_cho]." ("open", "base", "base", "mid")
        elif states.cho.level < 10:
            cho "Sure thing [name_genie_cho], I was getting bored with what I was wearing anyway..." ("smile", "narrow", "base", "R")
        elif states.cho.level < 16:
            cho "Yes... That's probably a good idea..." ("soft", "narrow", "base", "down")
            gen "It is?" ("base", xpos="far_left", ypos="head")
            cho "Of course... I mean, I mean... What if my clothes caught fire?" ("grin", "narrow", "base", "mid")
            cho "The faster I could get them off, the less likely I am to burn my skin." ("grin", "closed", "base", "mid")
            gen "(Is she making up reasons to wear less clothes now?)" ("base", xpos="far_left", ypos="head")
        else: #16+
            cho "Do I have to?" ("annoyed", "narrow", "base", "down")
            gen "What do you mean, do you have to?" ("base", xpos="far_left", ypos="head")
            cho "Well, the buttons are so difficult to get off... I'd much rather wear something less constricting." ("open", "closed", "base", "mid")
            gen "You could just say that you want to show off that toned body of yours." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "[name_genie_cho], I am not that self-centred..." ("base", "narrow", "base", "R")
            gen "..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I only show it off for the benefit of others, not myself." ("crooked_smile", "narrow", "base", "mid")
            gen "*Heh*... Good one." ("base", xpos="far_left", ypos="head")
            cho "..." ("smile", "narrow", "base", "R") #smiles
            gen "Well, if that's the case, then I'd like to see that bod, wearing the school shirt." ("base", xpos="far_left", ypos="head")
            cho "*Hmph*... Alright then..." ("soft", "closed", "base", "mid") #not actually mad


    #############################################################
    ## Clear Night (Blue sweater with yellow stripe and jeans) ##
    #############################################################
    elif item == cho_outfit_s_clearnight:
        gen "Could you put on the striped sweater and your jeans?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Of course, [name_genie_cho]." ("base", "base", "base", "mid")
            cho "I do prefer jeans a lot more compared to skirts." ("smile", "base", "base", "mid")
            gen "Really? I would never have guessed..." ("base", xpos="far_left", ypos="head")
        elif states.cho.level < 10:
            cho "Of course, [name_genie_cho]." ("base", "base", "base", "mid")
            cho "I do prefer jeans a lot more, compared to skirts." ("smile", "narrow", "base", "mid")
            gen "Really? Why is that?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Oh... *Err*..." ("soft", "base", "base", "mid")
            cho @ cheeks blush "They just... Fit me a lot better." ("angry", "narrow", "base", "mid")
            gen "*Uhu*..." ("base", xpos="far_left", ypos="head")
        elif states.cho.level < 16:
            cho "*Hmm*... Jeans, they're not that flexible, are they?" ("soft", "narrow", "base", "down")
            gen "I suppose not, why?" ("base", xpos="far_left", ypos="head")
            cho "Oh, nothing [name_genie_cho]... I was just thinking out loud." ("angry", "base", "base", "mid")
        else: #16+
            cho "My butt does look good in jeans, don't you think?" ("smile", "narrow", "base", "mid")
            gen "Absolutely!" ("base", xpos="far_left", ypos="head")

    ###############################
    ## Snowy (Sweater and Jeans) ##
    ################################
    elif item == cho_outfit_s_snow:
        gen "Could you put on your sweater and jeans?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Do you like my sweater, [name_genie_cho]?" ("smile", "base", "base", "mid")
            gen "*Err*... Sure!" ("base", xpos="far_left", ypos="head")
            gen "(Although I much prefer a pair of tight jeans on your shapely butt!)" ("grin", xpos="far_left", ypos="head")
            cho "Thank you, I'll put them on then." ("base", "base", "base", "mid")
        elif states.cho.level < 10:
            cho "Of course [name_genie_cho], as long as I don't get too sweaty." ("smile", "wink", "base", "mid")
            gen "Too sweaty?" ("base", xpos="far_left", ypos="head")
            cho "Sweaty, sweater... Get it?" ("smile", "narrow", "base", "mid")
            gen "...{w} Never make jokes like that ever again..." ("base", xpos="far_left", ypos="head")
            cho "Oh... Okay then..." ("angry", "narrow", "base", "mid")
        elif states.cho.level < 16:
            cho "You know, I think I should probably get a new pair of jeans one of these days." ("open", "narrow", "base", "R")
            gen "Really? Why is that?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I've just had them for a while... And with all the squats I've been doing..." ("soft", "narrow", "base", "down")
            cho @ cheeks blush "Well, they don't fit like they used to." ("open", "closed", "worried", "mid")
            gen "I think they look great!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "Really?" ("angry", "base", "base", "mid")
            gen "Of course! You should definitely keep wearing them." ("base", xpos="far_left", ypos="head")
            gen "Unless they're so tight that they could split open at any minute, of course." ("base", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "Unless they're... Well, I suppose..." ("soft", "narrow", "base", "down")
            cho "Just give me a moment, and I'll change..." ("base", "base", "base", "mid")
        else: #16+
            cho "Sure thing, [name_genie_cho]." ("base", "base", "base", "mid")
            cho "By the way, do you know why jeans are superior to skirts?" ("smile", "narrow", "base", "mid")
            gen "Tell me." ("base", xpos="far_left", ypos="head")
            cho "You can't see the butt-jiggle if you spank someone, and they are wearing a skirt." ("smile", "narrow", "base", "mid")
            gen "Would you be able to stealthily flash your panties when wearing jeans, though?" ("base", xpos="far_left", ypos="head")
            cho "No, but if your jeans are tight enough, then you can show off some camel-toe, without the risk of getting reprimanded." ("base", "narrow", "base", "R")
            gen "You've certainly thought this through..." ("base", xpos="far_left", ypos="head")

    #################################
    ## Overcast (Hoodie and Jeans) ##
    #################################
    elif item == cho_outfit_s_overcast:
        gen "Could you wear the hoodie with your jeans?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Do you like my hoodie, [name_genie_cho]?" ("open", "base", "base", "mid")
            gen "Of course... It's very tomboy-ish!" ("base", xpos="far_left", ypos="head")
            cho "It is?" ("angry", "narrow", "base", "stare")
            gen "That's not meant as an insult, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
            cho "Really? I always thought--" ("disgust", "narrow", "base", "mid")
            gen "Even if it was, if you like it, then your opinion is the only one that matters." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Yes, that's true... And I do like it." ("soft", "narrow", "base", "down")
            cho "Give me a moment, and I'll change." ("base", "base", "base", "mid")
        elif states.cho.level < 10:
            cho "You know, someone once mistook me for a guy when I wore these." ("annoyed", "narrow", "base", "down")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            cho "Yes! I mean, how could they have thought that?" ("angry", "narrow", "raised", "mid")
            gen "*Hmm*... Yes, that's a very good question..." ("base", xpos="far_left", ypos="head")
            gen "I mean, you're clearly not..." ("base", xpos="far_left", ypos="head")
            cho "..." ("annoyed", "narrow", "base", "mid")
            gen "Alright then, if you feel validated enough... Could you put it on?" ("base", xpos="far_left", ypos="head")
            cho "Oh, right... Of course [name_genie_cho]." ("angry", "base", "base", "mid")
        elif states.cho.level < 16:
            cho "*Hmm*... Don't you think it's weird for me to wear masculine clothing, [name_genie_cho]?" ("soft", "narrow", "base", "R")
            gen "Of course not, why would it be?" ("base", xpos="far_left", ypos="head")
            cho "Well, I don't really see many of the other girls wearing hoodies." ("soft", "narrow", "base", "mid")
            gen "They probably just don't want to hide their hair." ("base", xpos="far_left", ypos="head")
            cho "Then just don't put the hood on." ("disgust", "narrow", "base", "mid")
            gen "If you're never going to put the hood on, then why get a hoodie in the first place?" ("base", xpos="far_left", ypos="head")
            cho "... I never thought about that..." ("angry", "base", "base", "stare")
            gen "... So, could you put it on or what?" ("base", xpos="far_left", ypos="head")
            cho "Oh, right... One moment, [name_genie_cho]." ("angry", "base", "base", "mid")
        else: #16+
            cho "Jeans, [name_genie_cho]?" ("soft", "base", "base", "mid")
            gen "Or would you prefer the freeing feeling of a skirt?" ("base", xpos="far_left", ypos="head")
            cho "Of course not! In fact, I have quite the nostalgic fondness for jeans." ("base", "narrow", "base", "R")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Yes... Did I ever tell you about the first time a pair of my jeans split open, right in the crotch area?" ("smile", "narrow", "base", "mid")
            gen "I'm not-- Wait, did you say \"the first time\"?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "It was pretty embarrassing... But also quite exciting..." ("base", "closed", "base", "mid")
            gen "Well... I suppose that explains a few things..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "..." ("smile", "closed", "base", "mid")

    #####################################
    ## Rainy (School outfit with cloak)##
    #####################################
    elif item == cho_outfit_s_rain:
        gen "Could you put on your regular school uniform, and your cloak as well?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Alright, just give me one moment [name_genie_cho]..." ("base", "base", "base", "mid")
        elif states.cho.level < 10:
            cho "I suppose I could... Although, how is wearing the cloak supposed to help me with Quidditch?" ("soft", "narrow", "raised", "mid")
            gen "What do you mean? I'm just asking you to wear it, that's all." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Oh... *Ehm*... Never mind..." ("annoyed", "base", "base", "R")
            cho @ cheeks blush "Just give me a moment, and I'll put it on..." ("open", "closed", "base", "mid")
        elif states.cho.level < 16:
            cho "My cloak?" ("soft", "base", "base", "mid")
            gen "Yes, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Wouldn't you rather I wear something more... I don't know..." ("open", "narrow", "base", "R")
            gen "More? How much else could you put on after that?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "That's not--" ("angry", "base", "base", "mid")
            cho @ cheeks blush "Alright then, one moment [name_genie_cho]... Let me just change, real quick." ("open", "narrow", "base", "R")
        else: #16+
            cho @ cheeks blush "You want to cover me up?" ("upset", "narrow", "raised", "mid")
            gen "*Err*..." ("base", xpos="far_left", ypos="head")
            cho "You know how much I despise wearing clothes!" ("angry", "closed", "worried", "mid")
            gen "Really? I just thought you enjoyed not wearing any." ("base", xpos="far_left", ypos="head")
            cho "Same thing." ("annoyed", "narrow", "raised", "R")
            gen "Then just think about how nice it will feel when you finally get to take it all off." ("base", xpos="far_left", ypos="head")
            cho "..." ("soft", "narrow", "base", "down")
            cho "Alright then... I suppose I could put it on... For now..." ("smile", "narrow", "base", "mid")

    ########################
    ## Cheerleader ##
    ########################
    elif item == cho_outfit_cheerleader: #Req 10 whoring
        gen "Could you wear the cheerleader outfit for me?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 16:
            cho "The cheerleader outfit..." ("soft", "narrow", "base", "down")
            cho "You want me to cheer for myself or what?" ("angry", "narrow", "raised", "mid")
            gen "*Heh-Heh*...{w=0.2} Yeah, that sounds funny..." ("grin", xpos="far_left", ypos="head")
            cho "Fine..." ("disgust", "narrow", "base", "mid")
        else: # 16+
            cho "The cheerleader outfit?" ("open", "narrow", "base", "mid")
            cho "But isn't that a bit below me?" ("annoyed", "base", "base", "mid")
            gen "Blow me? Yes, please!" ("grin", xpos="far_left", ypos="head")
            cho "...{w} Fine." ("disgust", "narrow", "base", "mid")

    ##################
    ## Misty Outfit ##
    ##################
    elif item == cho_outfit_misty: #Req 15 (no bra)
        gen "Put on the misty cosplay for me will you?" ("base", xpos="far_left", ypos="head")
        cho "*Hmm*... A cosplay..." ("open", "base", "base", "down")
        gen "Yup, gotta catch them all." ("base", xpos="far_left", ypos="head")
        cho "Catch all of what?" ("soft", "base", "raised", "mid")
        gen "The pokemens." ("base", xpos="far_left", ypos="head")
        cho "*Huh*?" ("annoyed", "narrow", "raised", "mid")
        gen "And the pokewomens..." ("base", xpos="far_left", ypos="head")
        cho "The what?" ("open", "narrow", "raised", "mid")
        gen "To train them is my cause." ("base", xpos="far_left", ypos="head")
        cho "..." ("normal", "narrow", "base", "mid")
        gen "Just put it on will you?" ("base", xpos="far_left", ypos="head")
        cho "Alright..." ("open", "narrow", "base", "mid")

    ##################
    ## Party Outfit ##
    ##################
    elif item == cho_outfit_party: #Req 16 (bottom) (clothing event unlock)
        gen "Can you put on the party outfit?" ("base", xpos="far_left", ypos="head")
        cho "Something we're celebrating?" ("smile", "base", "base", "mid")
        gen "Yes." ("base", xpos="far_left", ypos="head")
        cho "What is it?" ("base", "base", "raised", "mid")
        gen "How good you'll look in the outfit." ("base", xpos="far_left", ypos="head")
        gen "Now put it on!" ("grin", xpos="far_left", ypos="head")
        cho "Alright, one moment." ("base", "base", "base", "R")

    ###################
    ## Sailor Outfit ##
    ###################
    elif item == cho_outfit_sailor: #Req 18 (bottom, panties)
        gen "I've got this sailor's outfit with your name on it!" ("grin", xpos="far_left", ypos="head")
        cho "Looks more like a slutty sailor outfit..." ("annoyed", "narrow", "raised", "down")
        cho "I doubt any seamen would actually wear something like this..." ("open", "narrow", "base", "mid")
        gen "Yeah, the semen goes on this outfit, not inside it..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "They go-- Oh...{w=0.3} I see..." ("disgust", "narrow", "base", "down")
        menu:
            "\"And call me captain from now!\"":
                $ name_genie_cho = "Captain"
                cho @ cheeks blush "Alright Captain!" ("soft", "narrow", "base", "mid")
            "\"Now set sail!\"":
                cho @ cheeks blush "Yes [name_genie_cho]!" ("soft", "narrow", "base", "mid")

    ############################
    ## Japanese School Outfit ##
    ############################
    elif item == cho_outfit_j_school: #Req 4 (top, bottom)
        gen "Could you put on the Japanese schoolgirl uniform?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 10:
            cho "*Hmm*... It's a bit..." ("disgust", "narrow", "base", "down")
            gen "A bit what?" ("base", xpos="far_left", ypos="head")
            cho "I don't know..." ("clench", "narrow", "worried", "down")
            gen "Cute?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Yes..." ("annoyed", "narrow", "base", "mid")
            gen "I'm sure you'll look great in it then!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "...{w=0.3} Alright, fine..." ("disgust", "narrow", "base", "down")
        elif states.cho.level < 16:
            cho "*Hmm*... I guess this is what I'd be wearing if my family had stayed in Asia..." ("soft", "narrow", "base", "down")
            gen "I thought you said you weren't Japanese?" ("base", xpos="far_left", ypos="head")
            cho "There's only one Wizard school in Asia, and it's in Japan... Surely, you'd know this...." ("disgust", "narrow", "base", "mid")
            gen "Oh!" ("base", xpos="far_left", ypos="head")
            gen "(How small is the wizard community? These numbers don't add up...)" ("base", xpos="far_left", ypos="head")
            gen "*Err*... I'm just a bit forgetful, that's all..." ("base", xpos="far_left", ypos="head")
            cho "Right...{w=0.3} Well, just give me a moment to change then..." ("annoyed", "narrow", "base", "mid")
        else: # 16+
            cho "Did they send you this from Japan?" ("open", "base", "base", "mid")
            gen "I had it custom-made!" ("base", xpos="far_left", ypos="head")
            cho "You did?" ("clench", "narrow", "base", "down")
            cho "And here I thought it was an official uniform..." ("angry", "narrow", "base", "down")
            gen "What can I say, I'm quite knowledgeable about these types of uniforms... I've got quite the collection of images." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I bet you do..." ("disgust", "narrow", "base", "downR")
            cho @ cheeks blush "Alright, let's see if I look like any of the girls in those pictures of yours..." ("base", "narrow", "base", "mid")

    ###################
    ## Bikini Outfit ##
    ###################
    elif item == cho_outfit_bikini: #req 14 (bra, panties)
        gen "I've got this bikini for you to wear today." ("base", xpos="far_left", ypos="head")
        if states.cho.level < 16:
            cho @ cheeks blush "A Bikini?" ("soft", "narrow", "base", "mid")
            gen "Yep, this one..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("soft", "narrow", "base", "down")
            cho @ cheeks blush "Are you sure this is not just some scrap material you had lying around?" ("angry", "narrow", "base", "down")
            gen "I mean... It might've been made from that." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Figures..." ("disgust", "narrow", "base", "downR")
            cho @ cheeks blush "Well, I suppose it's better than being naked..." ("soft", "narrow", "base", "mid")
        else: # 16+
            cho "A Bikini?" ("soft", "base", "base", "mid")
            gen "Yep, this one..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I see..." ("base", "narrow", "base", "down")
            cho @ cheeks blush "Well, I do look great in a bikini..." ("open", "closed", "base", "mid")
            gen "I'm still waiting for the beach episode." ("base", xpos="far_left", ypos="head")
            cho "The what?" ("angry", "base", "base", "mid")
            gen "Never mind..." ("base", xpos="far_left", ypos="head")
            cho "Alright... Just give me a moment to put it on." ("soft", "narrow", "base", "down")

    ##########################
    ## Lace Lingerie Outfit ##
    ##########################
    elif item == cho_outfit_lacelingerie: #req 14 (bra)
        gen "Could you put on this lace underwear set?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 16:
            cho @ cheeks blush "This is lingerie isn't it?" ("soft", "narrow", "base", "down")
            gen "Well spotted." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I can't say this is the type of underwear I usually like to wear." ("normal", "narrow", "base", "mid")
            gen "Well, there's underwear for different purposes..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "And lingerie's purpose is?" ("open", "narrow", "base", "downR")
            gen "To bring out the sexy!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I see..." ("soft", "narrow", "base", "down")
            cho @ cheeks blush "Well, if that's the goal, then I suppose I'll have to wear it." ("open", "closed", "base", "mid")
            cho @ cheeks blush "Prepare to meet your maker, sexiness!" ("grin", "narrow", "base", "mid")
        else: #16+
            cho @ cheeks blush "Lingerie..." ("soft", "narrow", "base", "down")
            cho @ cheeks blush "So these types of underwear really does it for men do they?" ("open", "base", "base", "downR")
            gen "Yep!" ("base", xpos="far_left", ypos="head")
            gen "Women too!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "*Hmm*...{w=0.3} Well, I better put it on then..." ("base", "narrow", "base", "down")

    ##################
    ## Dress Outfit ##
    ##################
    elif item == cho_outfit_dress1: #req 12 (top)
        gen "I've got the perfect dress for you to wear." ("base", xpos="far_left", ypos="head")
        cho "A dress?" ("base", "base", "raised", "mid")
        gen "Yep, this one!" ("base", xpos="far_left", ypos="head")
        cho "*Hmm*...{w=0.3} Red and gold..." ("normal", "base", "base", "down")
        gen "Nice isn't it?" ("base", xpos="far_left", ypos="head")
        cho "I...{w=0.3} Yes, thank you [name_genie_cho]..." ("open", "narrow", "base", "down")
        cho "I'll put it on now then shall I." ("open", "base", "base", "mid")

    ####################
    ## Trainee Outfit ##
    ####################
    elif item == cho_outfit_trainee: #req 10 (top) (Part of clothing event)
        gen "I've got the perfect outfit for you to wear when you exercise, mind putting it on?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 16:
            cho @ cheeks blush "Did you get a size too small on purpose?" ("disgust", "narrow", "base", "down")
            gen "What do you mean?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "That tank top would slide up any time I try to do stretches..." ("angry", "narrow", "base", "mid")
            gen "Sounds like a bonus to me." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("annoyed", "narrow", "base", "down")
            cho @ cheeks blush "Alright, fine..." ("open", "narrow", "base", "down")
        else : #16+
            cho @ cheeks blush "What kind of exercises do you have in mind exactly?" ("open", "narrow", "base", "mid")
            gen "Ones that show off your ass mainly." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Figures..." ("base", "narrow", "base", "R")
            cho @ cheeks blush "Give me a moment to put it on then..." ("base", "base", "base", "mid")

    ################
    ##  Smurfette ##
    ################
    elif item == cho_outfit_smurfette: #req 15 (no bra, no panties)
        gen "I've got this smurfette Cosplay for you to wear." ("base", xpos="far_left", ypos="head")
        if states.cho.level < 16:
            cho "Smurf... What?" ("soft", "narrow", "raised", "mid")
            gen "Ette." ("base", xpos="far_left", ypos="head")
            cho "*Huh*?" ("annoyed", "base", "base", "mid")
            gen "She's that cute blond one in the smurfs." ("base", xpos="far_left", ypos="head")
            cho "Alright..." ("open", "narrow", "base", "R")
            cho "Well I suppose it doesn't look too bad..." ("open", "narrow", "base", "down")
            cho "That hat is a bit silly though... Promise you won't laugh at me..." ("disgust", "narrow", "base", "mid")
            gen "Promise..." ("base", xpos="far_left", ypos="head")
            cho "Okay, just give me a moment to go change then..." ("soft", "base", "base", "mid")
        else: # 16+
            cho "Who's that?" ("soft", "base", "raised", "mid")
            gen "She's the blonde girl." ("base", xpos="far_left", ypos="head")
            cho "*Huh*?" ("angry", "narrow", "base", "mid")
            gen "Come on, she was the only female Smurf for the first five seasons. I know they look similar but surely--" ("base", xpos="far_left", ypos="head")
            cho "I don't know what a Smurf is." ("disgust", "narrow", "base", "mid")
            gen "Oh... That makes more sense..." ("base", xpos="far_left", ypos="head")
            gen "Well, they're these tiny blue creatures that live in the woods." ("base", xpos="far_left", ypos="head")
            cho "Like a pixie?" ("open", "base", "base", "mid")
            gen "Smurfs are only blue, but I guess they're the same size." ("base", xpos="far_left", ypos="head")
            cho "Pixies are only blue as well..." ("angry", "narrow", "base", "mid")
            gen "Pretty sure they're not, what do they teach you in history class here?" ("base", xpos="far_left", ypos="head")
            cho "History? We were told they were blue in our Care of magical creatures class." ("angry", "narrow", "base", "mid")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            gen "(The gene pool must've got fucked after generations of inbreeding...)" ("base", xpos="far_left", ypos="head")
            gen "(Such a shame...)" ("base", xpos="far_left", ypos="head")
            gen "Whatever the case... I'd like you to wear this cosplay outfit for me." ("base", xpos="far_left", ypos="head")
            cho "Oh... Alright..." ("open", "narrow", "base", "mid")

    ######################
    ## Space Jam Outfit ##
    ######################
    elif item == cho_outfit_toon: #req 4
        gen "Put on this space Jam outfit for me will you?" ("base", xpos="far_left", ypos="head")
        cho "This outfit doesn't look very space themed to me..." ("soft", "narrow", "raised", "mid")
        gen "It's not about space!" ("base", xpos="far_left", ypos="head")
        gen "It's Basketball themed!" ("base", xpos="far_left", ypos="head")
        cho "Basket... Then why does it have space in the name?" ("soft", "narrow", "raised", "mid")
        gen "I don't know, why does Quidditch have Quid and ditch in the name if it's not about throwing money on the ground?" ("base", xpos="far_left", ypos="head")
        cho "*Err*...{w} I'll just put this on then, shall I?" ("disgust", "narrow", "base", "mid")

    ####################
    ## Chun-Li Outfit ##
    ####################
    elif item == cho_outfit_chun_li: #req 16 (tattoo's)
        gen "I've got this cosplay outfit for you to wear." ("base", xpos="far_left", ypos="head")
        cho "Cosplay?" ("open", "base", "raised", "mid")
        gen "Yeah, it's a video-- *Err*... Famous female martial artist." ("base", xpos="far_left", ypos="head")
        cho "Oh? What's her name?" ("smile", "base", "base", "mid")
        gen "Chun-Li!" ("base", xpos="far_left", ypos="head")
        cho "*Hmm*... Not sure if I've heard of her." ("soft", "base", "base", "mid")
        gen "(Like everyone in this castle...)" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I suppose the costume looks quite well-made." ("open", "base", "base", "down")
        gen "Finest silk in the country!" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Alright, I'll wear it... Even though that tattoo is a bit..." ("base", "narrow", "base", "down")
        gen "A bit what? A bit too awesome?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "So... You really don't know what it says." ("soft", "narrow", "base", "mid")
        gen "Not the faintest idea." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Well... I suppose that's a good thing..." ("soft", "narrow", "base", "R")

    ##################
    ## Police Woman ##
    ##################
    elif item == cho_outfit_police: #req 10 (bottoms)
        gen "Put on the police cosplay uniform will you?" ("base", xpos="far_left", ypos="head")
        cho "Police?" ("soft", "base", "raised", "mid")
        gen "Yeah, check out the sweet shades on this one. Aren't they cool?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Trying to take away the focus on that short top?" ("open", "narrow", "base", "down")
        gen "No clue what you're talking about..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "*Hmm*..." ("base", "narrow", "base", "down")
        gen "You know, the police are some of the most well-respected people in muggle society..." ("base", xpos="far_left", ypos="head")
        gen "I know how much you love that stuff." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "They are?" ("open", "base", "base", "mid")
        gen "Sure!" ("base", xpos="far_left", ypos="head")
        cho "Alright then... If you say so." ("base", "base", "base", "mid")

    ###################
    ## Bunny Costume ##
    ###################
    elif item == cho_outfit_bunny: #req 15 (no bra, no panties)
        gen "I've got this bunny costume for you to put on." ("base", xpos="far_left", ypos="head")
        cho "A bunny costume?" ("soft", "base", "base", "mid")
        cho @ cheeks blush "Do you really think a bunny costume would suit me?" ("open", "base", "base", "R")
        gen "Of course! Why wouldn't it?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Well, I thought that you'd need bigger--" ("upset", "narrow", "base", "down")
        cho @ cheeks blush "I mean, of course it will suit me!" ("angry", "closed", "angry", "mid")
        cho @ cheeks blush "Hand it over!" ("angry", "base", "base", "mid")

    ######################
    ## Reindeer Costume ##
    ######################
    elif item == cho_outfit_reindeer: #req 15 (no bra, no panties)
        gen "How about you put on this reindeer costume for me?" ("base", xpos="far_left", ypos="head")
        cho "A reindeer costume?" ("soft", "base", "raised", "mid")
        gen "That's right. This one right here..." ("base", xpos="far_left", ypos="head")
        cho "*Hmm*... I suppose I could--" ("soft", "narrow", "base", "down")
        cho "Hold on, there's a--" ("clench", "narrow", "base", "down")
        cho @ cheeks blush "{size=-4}There's a hole in this...{/size}" ("base", "narrow", "base", "down")
        gen "Something wrong?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I'm fine, let me just put it on..." ("soft", "narrow", "base", "down")
        cho @ cheeks blush "" ("soft", "narrow", "base", "mid")

    ###################
    ## Virgin Killer ##
    ###################
    elif item == cho_outfit_virgin_killer: #req 14 (no bra, no panties)
        gen "I've got this jumper I'd like you to put on." ("base", xpos="far_left", ypos="head")
        cho "A jumper?" ("soft", "base", "base", "mid")
        gen "Yup, is that surprising?" ("base", xpos="far_left", ypos="head")
        cho "*Hmm*... I suppose I would've imagined something more--" ("open", "base", "base", "R")
        gen "Here you go." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Oh... It's one of those." ("open", "narrow", "base", "down")
        gen "Do you like it?" ("base", xpos="far_left", ypos="head")
        gen "I thought it would enhance your features." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "*Hmm*... If you say so..." ("base", "narrow", "base", "down")
        cho @ cheeks blush "Alright, just give me a moment to put it on." ("base", "base", "base", "mid")

    ##########################
    ## Sheer Nightie Outfit ##
    ##########################
    elif item == cho_outfit_sheer_nightie: #Req 16 (panties)
        gen "I've not this nightie for you to wear." ("base", xpos="far_left", ypos="head")
        cho "A nightie?" ("soft", "base", "base", "mid")
        gen "That's right." ("base", xpos="far_left", ypos="head")
        gen "This one, right here." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "...{w=0.4} It's see-through." ("horny", "narrow", "base", "down")
        gen "I know... Quite the lifehack isn't it?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "A lifehack?" ("horny", "base", "raised", "mid")
        gen "Well, if you were completely naked, then that would be indecent..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Oh... I see..." ("smile", "narrow", "base", "down")
        cho @ cheeks blush "Well, I better wear it then... For the sake of decency..." ("smile", "wink", "base", "mid")

    ##########################
    ## Sporty Bikini Outfit ##
    ##########################
    elif item == cho_outfit_sporty_bikini: #Req 12 (panties)
        gen "I've got this sporty bikini for you to wear." ("base", xpos="far_left", ypos="head")
        cho "A sporty bikini?" ("soft", "base", "base", "mid")
        gen "Yeah! You're into that sort of thing, aren't you?" ("base", xpos="far_left", ypos="head")
        cho "I suppose I do look good in a bikini..." ("base", "narrow", "base", "down")
        gen "I was talking about sports, but sure!" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Oh..." ("angry", "narrow", "base", "mid")
        cho @ cheeks blush "Well, I suppose I could wear it when exercising." ("base", "base", "base", "mid")
        gen "I was thinking you could wear it now." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "... Alright then." ("smile", "base", "base", "mid")

    #######################
    ## Club Dress Outfit ##
    #######################
    elif item == cho_outfit_club_dress: #Req 16 (panties)
        gen "I've got this dress for you to wear." ("base", xpos="far_left", ypos="head")
        cho "*Hmm*... A dress, you say?" ("base", "narrow", "base", "mid")
        gen "Yep, it's this one, right here." ("base", xpos="far_left", ypos="head")
        cho "Very nice..." ("smile", "narrow", "base", "down")
        gen "Yes, I thought you might like it." ("base", xpos="far_left", ypos="head")
        cho "Really? Seems like you know me better than I thought..." ("smile", "narrow", "base", "mid")
        gen "You see... When you're moving about, this dress will slide up your body quite easily." ("base", xpos="far_left", ypos="head")
        gen "So, if you ever wanted to give someone a peek, you could just blame it on the dress." ("base", xpos="far_left", ypos="head")
        cho "I need to make excuses to flaunt my physique now?" ("upset", "narrow", "base", "mid")
        gen "That's not what I--" ("base", xpos="far_left", ypos="head")
        cho "*Giggles*" ("base", "base", "base", "mid")
        cho "Don't worry [name_genie_cho]...{w=0.4} I'm just messing with you." ("smile", "base", "base", "mid")

    # TODO: Blacklist fallbacks have to be added.
    return

label cho_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.

    ########################
    ## Cheerleader ##
    ########################
    if item == cho_outfit_cheerleader: #Req 10 whoring
        gen "Could you wear the cheerleader outfit for me?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Cheerleader--{w=0.4} [name_genie_cho]!" ("clench", "narrow", "base", "mid")
            gen "what?" ("base", xpos="far_left", ypos="head")
            cho "I am a real athlete!" ("disgust", "narrow", "angry", "mid")
            cho "I do not mingle with the cheerleading squad..." ("annoyed", "narrow", "angry", "R")
            gen "Now, now [name_cho_genie]... Cheerleaders are athletes as well." ("base", xpos="far_left", ypos="head")
            gen "Their role is just as important as yours." ("base", xpos="far_left", ypos="head")
            cho "Don't make me laugh..." ("open", "closed", "angry", "mid")
            cho "The only thing they're good at is distracting the audience from the game." ("annoyed", "narrow", "angry", "mid")
            gen "Well, when you put it--{w=0.3} *Err*... No, their role is very important!" ("base", xpos="far_left", ypos="head")
            gen "What else are you supposed to look at during half-time?" ("base", xpos="far_left", ypos="head")
            cho "Yeah... I'd rather not, thanks..." ("open", "narrow", "angry", "R")
        else: # < 10
            cho "No, thanks... I'd rather not put on anything that those talentless posers are wearing." ("annoyed", "closed", "angry", "down")
            gen "Oh, come on... Cheerleading requires plenty of talent!" ("base", xpos="far_left", ypos="head")
            cho "Like what? the art of flailing pompoms around?" ("soft", "narrow", "angry", "mid")
            gen "Coordination, spirit, and a positive attitude." ("base", xpos="far_left", ypos="head")
            gen "These are all important things you need to be a good Cheerleader." ("base", xpos="far_left", ypos="head")
            cho "*Pff*... Those things come naturally to me anyway..." ("open", "narrow", "base", "R")
            gen "{size=-4}Ability to take constructive criticism...{/size}" ("base", xpos="far_left", ypos="head")
            cho "*Huh*?" ("soft", "narrow", "base", "mid")
            gen "Never mind..." ("base", xpos="far_left", ypos="head")

    ##################
    ## Misty Outfit ##
    ##################
    elif item == cho_outfit_misty: #Req 15 (no bra)
        gen "Put on this misty cosplay for me will you?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "What on earth is this?!" ("angry", "wide", "base", "down")
            gen "Misty cosplay..." ("base", xpos="far_left", ypos="head")
            cho "Who?" ("disgust", "narrow", "angry", "mid")
            gen "She's a gym leader." ("base", xpos="far_left", ypos="head")
            cho "Who wears something like this at the gym?!" ("clench", "narrow", "raised", "down")
            gen "Well, she does, obviously... Although it's more of an everyday clothing." ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "narrow", "base", "mid")
            cho "Yeah, no, thank you..." ("annoyed", "narrow", "angry", "R")
        elif states.cho.level < 10:
            cho "A cosplay?" ("open", "base", "raised", "mid")
            cho "Whoa... Who is this Misty girl to be wearing something like this?" ("open", "base", "raised", "down")
            gen "She's a trainer, much like me." ("base", xpos="far_left", ypos="head")
            cho "Really?" ("clench", "narrow", "base", "mid")
            gen "Yup." ("base", xpos="far_left", ypos="head")
            cho "What kind of sport is it for her to be wearing this?" ("annoyed", "narrow", "raised", "down")
            gen "Well, they basically have these animals fight against each other." ("base", xpos="far_left", ypos="head")
            cho "What?!" ("angry", "wide", "raised", "mid")
            cho "Like cock fighting? Isn't that illegal?" ("clench", "narrow", "worried", "mid")
            gen "I don't think there are any cocks involved... I'm not sure what kind of fiction you've been reading." ("base", xpos="far_left", ypos="head")
            cho "What?" ("angry", "base", "base", "mid")
            gen "Are you going to put it on or what?" ("base", xpos="far_left", ypos="head")
            cho "I'd rather not..." ("annoyed", "narrow", "base", "down")
            gen "Fine..." ("base", xpos="far_left", ypos="head")
        else: # < 15
            cho "This top has no bra with it..." ("open", "narrow", "base", "down")
            gen "Do you need one?" ("base", xpos="far_left", ypos="head")
            cho "Excuse me?" ("soft", "narrow", "angry", "mid")
            gen "(Oh, shit...)" ("angry", xpos="far_left", ypos="head")
            gen "What I meant to say was--" ("base", xpos="far_left", ypos="head")
            cho "..." ("annoyed", "base", "angry", "mid")
            gen "Never mind..." ("base", xpos="far_left", ypos="head")

    ##################
    ## Party Outfit ##
    ##################
    elif item == cho_outfit_party: #Req 16 (bottom) (clothing event unlock, this is a fallback)
        gen "Can you put on the party outfit?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "The... Party outfit?" ("open", "base", "raised", "mid")
            gen "Yeah... This one..." ("base", xpos="far_left", ypos="head")
            cho "..." ("normal", "base", "base", "down")
            cho "[name_genie_cho]!" ("angry", "wide", "base", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            cho "What do you mean what? This outfit has no underwear!" ("upset", "narrow", "angry", "mid")
            gen "I mean... It covers the important bits, does it not?" ("base", xpos="far_left", ypos="head")
            gen "Maybe not from every angle but if you were careful not to--" ("base", xpos="far_left", ypos="head")
            cho "I am not wearing this!" ("angry", "narrow", "angry", "mid")
            gen "Alright, No partying for you, I guess..." ("base", xpos="far_left", ypos="head")
        elif states.cho.level < 10:
            cho "This outfit has no underwear!" ("angry", "base", "base", "down")
            gen "Oh... It doesn't?" ("base", xpos="far_left", ypos="head")
            cho "It does not..." ("disgust", "narrow", "base", "mid")
            cho "I am not going to stand around casually in an outfit without underwear..." ("annoyed", "narrow", "base", "R")
            gen "I do it all the time, I don't see what the problem is." ("base", xpos="far_left", ypos="head")
            cho "You're not wearing any..." ("mad", "narrow", "base", "mid")
            gen "Making the Scotts proud..." ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "narrow", "base", "mid")
        else: # < 16
            cho "This outfit is way too slutty..." ("open", "narrow", "base", "down")
            cho @ cheeks blush "My nipples would poke right through this..." ("soft", "narrow", "base", "down")
            gen "Counting on it..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Yeah, I'm going to have to pass on this one..." ("angry", "narrow", "base", "down")

    ###################
    ## Sailor Outfit ##
    ###################
    elif item == cho_outfit_sailor: #Req 18 (bottom, panties)
        gen "I've got this sailor's outfit with your name on it!" ("grin", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Why would I put on a sailor's outfit?" ("soft", "narrow", "base", "mid")
            gen "Say that again once you've seen it!" ("grin", xpos="far_left", ypos="head")
            cho "I'd rather not..." ("disgust", "narrow", "base", "mid")
        elif states.cho.level < 10:
            cho "Why would I put on a sailor's outfit in here?" ("soft", "narrow", "raised", "mid")
            gen "Because you'd look great in it!" ("grin", xpos="far_left", ypos="head")
            cho "... Is that the only reason?" ("disgust", "base", "base", "mid")
            gen "Yep, now put it on!" ("grin", xpos="far_left", ypos="head")
            cho "... I'll pass..." ("annoyed", "narrow", "base", "R")
        else: # < 18
            cho "They were this outfit at sea do they?" ("open", "narrow", "raised", "down")
            gen "Nope, the semen goes on this outfit, not in it." ("base", xpos="far_left", ypos="head")
            cho "Wait... So, it's like a fetish thing?" ("clench", "wide", "base", "mid")
            gen "*Err*... I mean, it was just a joke. Get it, because semen sounds like--" ("base", xpos="far_left", ypos="head")
            cho "I am not putting on some fetish thing for you!" ("disgust", "base", "angry", "mid")
            gen "It's not..." ("base", xpos="far_left", ypos="head")
            cho "..." ("annoyed", "narrow", "angry", "mid")
            gen "Yeah, I guess it kind of is..." ("base", xpos="far_left", ypos="head")

    ############################
    ## Japanese School Outfit ##
    ############################
    elif item == cho_outfit_j_school: #Req 4 (top, bottom)
        gen "Could you put on the Japanese schoolgirl uniform?" ("base", xpos="far_left", ypos="head")
        cho "[name_genie_cho], I'm not Japanese..." ("annoyed", "narrow", "angry", "mid")
        gen "So?" ("base", xpos="far_left", ypos="head")
        cho "Why do you want me to put on a Japanese school uniform?" ("upset", "narrow", "angry", "mid")
        gen "(I better tread carefully...)" ("base", xpos="far_left", ypos="head")
        menu:
            "\"Japanese schoolgirls are hot!\"":
                cho "What?!" ("angry", "base", "angry", "mid")
                gen "*Err*... I mean, in the videos I've watched..." ("angry", xpos="far_left", ypos="head")
                cho "I am not putting this on, just so you can live out some fantasy of yours..." ("mad", "narrow", "angry", "mid")
                gen "It's not...{w=0.3} Fine..." ("base", xpos="far_left", ypos="head")
            "\"It's a new design I'm proposing to a Japanese wizarding school!\"":
                cho "Mahoutokoro?" ("soft", "narrow", "raised", "mid")
                gen "See, I knew you were Japanese!" ("base", xpos="far_left", ypos="head")
                cho "That's the name of the school..." ("disgust", "narrow", "angry", "mid")
                gen "Oh..." ("base", xpos="far_left", ypos="head")
                gen "So, are you putting it on or not?" ("base", xpos="far_left", ypos="head")
                cho "I am not..." ("annoyed", "narrow", "base", "mid")

    ###################
    ## Bikini Outfit ##
    ###################
    elif item == cho_outfit_bikini: #req 14 (bra, panties)
        gen "I've got this bikini for you to wear today." ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "A what?!" ("clench", "wide", "base", "mid")
            gen "Well... It's technically a two-piece set..." ("base", xpos="far_left", ypos="head")
            gen "These ones..." ("base", xpos="far_left", ypos="head")
            cho "What on earth is wrong with you?" ("scream", "narrow", "angry", "down")
            cho "Putting on a regular bikini in your office would be bad enough but this!" ("angry", "base", "angry", "mid")
            gen "Define regular..." ("base", xpos="far_left", ypos="head")
            cho "..." ("mad", "narrow", "angry", "mid")
            gen "Alright, whatever... Forget I said anything..." ("base", xpos="far_left", ypos="head")
        elif states.cho.level < 10:
            cho "A bikini? Why would I--" ("angry", "narrow", "base", "mid")
            gen "This one..." ("base", xpos="far_left", ypos="head")
            cho "[name_genie_cho]!" ("clench", "narrow", "base", "down")
            gen "What?" ("base", xpos="far_left", ypos="head")
            cho "How is this meant to be a bikini?" ("angry", "base", "angry", "down")
            cho "This would barely cover my... It would barely cover anything!" ("disgust", "narrow", "base", "down")
            gen "Don't be silly, it covers plenty..." ("base", xpos="far_left", ypos="head")
            cho "I am not wearing it..." ("annoyed", "narrow", "angry", "mid")
        else: # < 14
            gen "This one..." ("base", xpos="far_left", ypos="head")
            cho "This barely covers anything!" ("angry", "narrow", "base", "down")
            gen "I think you'll find that the purpose of a bikini is to in fact to cover..." ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "narrow", "base", "mid")
            cho "I'm not going to stand around in your office wearing something like this..." ("open", "closed", "base", "mid")
            gen "Fine, don't wear it then..." ("base", xpos="far_left", ypos="head")

    ##########################
    ## Lace Lingerie Outfit ##
    ##########################
    elif item == cho_outfit_lacelingerie: #req 14 (bra, panties)
        gen "Could you put on this lace underwear set?" ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Lace what?" ("soft", "narrow", "raised", "mid")
            gen "Underwear!" ("base", xpos="far_left", ypos="head")
            gen "These ones..." ("base", xpos="far_left", ypos="head")
            cho "This is Lingerie!" ("disgust", "wide", "base", "down")
            gen "I mean, what did you expect when I said--" ("base", xpos="far_left", ypos="head")
            cho "I am not changing my underwear for you!" ("disgust", "base", "angry", "mid")
            cho "Especially into something like this!" ("soft", "narrow", "angry", "down")
            cho "I can't believe you'd ask me to do this..." ("disgust", "base", "angry", "mid")
            gen "I was just testing you! And you failed [name_cho_genie]!" ("base", xpos="far_left", ypos="head")
            cho "A Test?! What kind of test was that supposed to be?" ("angry", "narrow", "base", "mid")
            gen "*Err*... A test of virtue!" ("base", xpos="far_left", ypos="head")
            cho "*Huh*?" ("angry", "base", "raised", "mid")
            cho "Isn't having virtue supposed to be a positive thing?" ("annoyed", "narrow", "angry", "mid")
            gen "Did I say virtue? I meant modesty!" ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "narrow", "angry", "mid")
            gen "Just put them on already before you fail another test!" ("base", xpos="far_left", ypos="head")
            cho "I think I'll have to take the fail on this one..." ("normal", "narrow", "angry", "mid")
        elif states.cho.level < 10:
            cho @ cheeks blush "This is lingerie..." ("disgust", "narrow", "base", "down")
            gen "That it is... Well spotted, seeker." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "You can see completely through it..." ("angry", "narrow", "base", "down")
            gen "I know!" ("base", xpos="far_left", ypos="head")
            gen "Isn't it great?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I am not wearing this." ("soft", "closed", "angry", "mid")
            gen "(Damn... I thought I'd caught that snatch...)" ("base", xpos="far_left", ypos="head")
        else: # < 14
            cho @ cheeks blush "This is lingerie..." ("normal", "narrow", "base", "down")
            cho @ cheeks blush "Isn't this something you'd wear to please a partner?" ("annoyed", "narrow", "base", "mid")
            gen "I mean..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("normal", "narrow", "base", "mid")
            gen "What if I said it would help with aero dynamics?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Does it?" ("open", "narrow", "raised", "mid")
            gen "*Err*...{w} Yes?" ("base", xpos="far_left", ypos="head")
            cho "You don't even sound convinced yourself..." ("disgust", "narrow", "base", "mid")
            gen "So is that a yes, or?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "It is--" ("open", "closed", "base", "mid")
            gen "Nice!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "Not..." ("soft", "narrow", "base", "downR")
            gen "Dang..." ("base", xpos="far_left", ypos="head")

    ##################
    ## Dress Outfit ##
    ##################
    elif item == cho_outfit_dress1: #req 12 (top)
        gen "I've got the perfect dress for you to wear." ("base", xpos="far_left", ypos="head")
        cho "A dress?" ("soft", "base", "base", "mid")
        gen "Yep, this one!" ("base", xpos="far_left", ypos="head")
        cho "[name_genie_cho]!" ("clench", "narrow", "base", "down")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        gen "You love it?" ("base", xpos="far_left", ypos="head")
        cho "Is this some sort of joke?" ("disgust", "narrow", "base", "mid")
        gen "What? Did I get the wrong size?" ("base", xpos="far_left", ypos="head")
        gen "I didn't buy some Chinese knock off did I?" ("base", xpos="far_left", ypos="head")
        cho "No, that's the problem." ("angry", "narrow", "base", "mid")
        cho "My mother would be so mad she saw me wearing such a cheap knock off..." ("disgust", "base", "base", "down")
        gen "Cheap! I'll have you know I paid--" ("base", xpos="far_left", ypos="head")
        cho "..." ("disgust", "narrow", "base", "mid")
        gen "Alright fine... Have it your way..." ("base", xpos="far_left", ypos="head")

    ####################
    ## Trainee Outfit ##
    ####################
    elif item == cho_outfit_trainee: #req 10 (top) (Part of clothing event, this is a fallback)
        gen "I've got the perfect outfit for you to wear when you exercise, mind putting it on?" ("base", xpos="far_left", ypos="head")
        cho "It's a bit small, don't you think?" ("annoyed", "base", "base", "down")
        gen "Is it?" ("base", xpos="far_left", ypos="head")
        cho "That tank top doesn't look like it would go down far enough..." ("soft", "narrow", "base", "down")
        gen "Nonsense, a little bit of airflow doesn't hurt anyone..." ("base", xpos="far_left", ypos="head")
        cho "*Hmm*... I'd rather wear my normal clothing..." ("annoyed", "narrow", "base", "mid")

    ################
    ##  Smurfette ##
    ################
    elif item == cho_outfit_smurfette: #req 15 (no bra, no panties) (part of event unlock, this is a fallback)
        gen "I've got this smurfette Cosplay for you to wear." ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "A Cosplay?" ("angry", "narrow", "base", "mid")
            gen "Yep, she's that cute--" ("base", xpos="far_left", ypos="head")
            cho "I am not putting on some cosplay for you..." ("annoyed", "narrow", "angry", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
        else: # 4+
            gen "I've got this smurfette Cosplay for you to wear." ("base", xpos="far_left", ypos="head")
            cho "[name_genie_cho], this outfit has no underwear." ("angry", "narrow", "base", "mid")
            gen "I mean, you never saw it in the show..." ("base", xpos="far_left", ypos="head")
            cho "I am not putting it on..." ("annoyed", "narrow", "angry", "mid")

    ######################
    ## Space Jam Outfit ##
    ######################
    elif item == cho_outfit_toon: #req 4
        gen "I think It's time you wear an outfit for a real sport for once." ("base", xpos="far_left", ypos="head")
        cho "What do you mean real sport?" ("angry", "narrow", "base", "mid")
        gen "One that isn't played riding cleaning appliances." ("base", xpos="far_left", ypos="head")
        cho "Quidditch is a real sport [name_genie_cho]!" ("angry", "narrow", "base", "mid")
        gen "Yeah, yeah, sure it is..." ("base", xpos="far_left", ypos="head")
        gen "Now put this on and show me what a real athlete should look like." ("base", xpos="far_left", ypos="head")
        cho "I'd rather not, seeing that Quidditch isn't a real sport... Which would make me not a real athlete..." ("annoyed", "narrow", "angry", "mid")
        gen "... Well, you're the one who said it..." ("base", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "narrow", "angry", "R")

    ####################
    ## Chun-Li Outfit ##
    ####################
    elif item == cho_outfit_chun_li: #req 16 (tattoo's)
        gen "I've got this cosplay outfit for you to wear." ("base", xpos="far_left", ypos="head")
        cho "cosplay?" ("normal", "base", "raised", "mid")
        if states.cho.level < 4:
            cho "I'm not putting on a cosplay outfit for you..." ("angry", "narrow", "base", "mid")
            gen "Why not?" ("base", xpos="far_left", ypos="head")
            cho "Just look at it!" ("mad", "base", "base", "down")
            cho "Even the armour has got nipples on it." ("disgust", "narrow", "angry", "down")
            gen "Indeed, some fine eye for detail!" ("base", xpos="far_left", ypos="head")
            cho "I'm not wearing it..." ("disgust", "base", "angry", "mid")
        elif states.cho.level < 10:
            cho "Why is this so revealing?" ("disgust", "narrow", "base", "down")
            gen "All good cosplays are." ("base", xpos="far_left", ypos="head")
            cho "Really?" ("annoyed", "narrow", "angry", "mid")
            gen "Why else do you think there are so many photos like that out there?" ("base", xpos="far_left", ypos="head")
            cho "*Hmm*..." ("annoyed", "narrow", "base", "R")
            cho "I think I'll pass..." ("open", "closed", "base", "mid")
            cho "" ("normal", "base", "base", "mid")
        else: # 10+
            cho "What's with that Tattoo?!" ("clench", "wide", "base", "down")
            gen "It's a dragon!" ("base", xpos="far_left", ypos="head")
            gen "Pretty sweet isn't--" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Not that one, the other one!" ("annoyed", "narrow", "angry", "down")
            gen "Oh, yeah, that one's pretty cool too, I suppose." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Do you even know what it says?" ("open", "narrow", "angry", "mid")
            gen "I don't know... Strength? Vigour?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I am not wearing it..." ("angry", "narrow", "base", "R")

    ##################
    ## Police Woman ##
    ##################
    elif item == cho_outfit_police: #req 10 (bottoms)
        gen "I've got this cosplay for you to wear." ("base", xpos="far_left", ypos="head")
        cho "Cosplay?" ("normal", "base", "raised", "mid")
        gen "Yeah." ("base", xpos="far_left", ypos="head")
        cho "I don't know about that..." ("disgust", "narrow", "base", "R")
        gen "Did I say cosplay? I meant uniform!" ("base", xpos="far_left", ypos="head")
        cho "*Hmm*... Let me see it." ("annoyed", "narrow", "base", "mid")
        gen "This one." ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "I don't know about that [name_genie_cho]..." ("disgust", "narrow", "base", "down")
            cho "Looks a lot like cosplay to me..." ("disgust", "narrow", "base", "down")
            gen "So what? I'm sure you'll look great in it." ("base", xpos="far_left", ypos="head")
            cho "I think I'll pass..." ("open", "narrow", "base", "R")
        else: # 4+
            cho "Why is this top so small?" ("angry", "narrow", "base", "down")
            gen "To put more focus on your breasts, obviously." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "My--{w=0.2} Didn't you say this was a uniform?" ("disgust", "narrow", "angry", "mid")
            cho @ cheeks blush "Why would a uniform put focus--" ("open", "closed", "angry", "mid")
            gen "Well... The cosplay version--" ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "narrow", "raised", "mid")
            gen "What I meant to say was..." ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "base", "angry", "mid")
            gen "Alright then... Maybe some other time." ("base", xpos="far_left", ypos="head")

    ###################
    ## Bunny Costume ##
    ###################
    elif item == cho_outfit_bunny: #req 15 (no bra, no panties)
        gen "How about you take the leap and wear something that shows off your figure for a change?" ("base", xpos="far_left", ypos="head")
        cho "What?!" ("disgust", "base", "base", "mid")
        gen "A bunny costume!" ("grin", xpos="far_left", ypos="head")
        gen "Get it? Take the leap?" ("grin", xpos="far_left", ypos="head")
        cho "..." ("disgust", "base", "base", "stare")
        gen "Cause that's what bunnies do." ("base", xpos="far_left", ypos="head")
        gen "Well, technically they hop, but--" ("base", xpos="far_left", ypos="head")
        cho "I sincerely hope you're joking..." ("open", "narrow", "angry", "mid")
        gen "Yes, so why aren't anyone laughing?" ("base", xpos="far_left", ypos="head")
        cho "Oh... Thank Merlin..." ("disgust", "closed", "worried", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        cho "..." ("base", "base", "base", "mid")
        gen "(Wait...)" ("base", xpos="far_left", ypos="head")

    ######################
    ## Reindeer Costume ##
    ######################
    elif item == cho_outfit_reindeer: #req 15 (no bra, no panties)
        gen "What do you say about putting on this reindeer costume?" ("base", xpos="far_left", ypos="head")
        cho "A reindeer costume? Is this like a Christmas thing?" ("soft", "base", "raised", "mid")
        gen "Something like that." ("base", xpos="far_left", ypos="head")
        gen "Here you go." ("base", xpos="far_left", ypos="head")
        cho "Well, that's kind of-- Hold on..." ("angry", "narrow", "base", "down")
        cho @ cheeks blush "There's a hole in the crotch!" ("mad", "base", "base", "mid")
        gen "Oh, really?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Surely you're not expecting--" ("angry", "base", "angry", "mid")
        gen "Of course not! It must've happened during shipping!" ("angry", xpos="far_left", ypos="head")
        gen "Those bloody owls and their claws!" ("angry", xpos="far_left", ypos="head")
        cho "If Owls did that, then what's up with the mistletoe right above it?!" ("annoyed", "narrow", "angry", "mid")
        gen "*Err*... I asked for it to be the centrepiece, so they must've thought I meant the centre of the costume!" ("angry", xpos="far_left", ypos="head")
        cho "Then shouldn't it be on the stomach?" ("open", "narrow", "angry", "mid")
        cho "Hold on... I can see the seams around this hole, no owl could--" ("angry", "base", "base", "mid")
        gen "Let me see!" ("open", xpos="far_left", ypos="head")
        gen "Oh, you're right!" ("angry", xpos="far_left", ypos="head")
        gen "This isn't at all what I asked for!" ("angry", xpos="far_left", ypos="head")
        gen "I'm going to have to give that seamstress a piece of my mind!" ("angry", xpos="far_left", ypos="head")
        cho "..." ("disgust", "narrow", "base", "mid")

    ###################
    ## Virgin Killer ##
    ###################
    elif item == cho_outfit_virgin_killer: #req 14 (no bra, no panties)
        gen "Ever heard of a virgin killer?" ("base", xpos="far_left", ypos="head")
        cho "Can't say that I have, is it some kind of drink?" ("soft", "base", "base", "mid")
        gen "Good guess, but no. It's a type of jumper." ("base", xpos="far_left", ypos="head")
        cho "I see... Why are you telling me this?" ("open", "narrow", "raised", "mid")
        gen "Well, I've heard that they're the rage these days, so I got you one." ("base", xpos="far_left", ypos="head")
        cho "Oh, well, that's very kind of you." ("base", "base", "base", "mid")
        gen "Here you go." ("base", xpos="far_left", ypos="head")
        cho "..." ("disgust", "narrow", "base", "down")
        cho @ cheeks blush "*Ehm*... Did you actually look at this before you decided to give it to me?" ("open", "narrow", "base", "down")
        gen "Not really, why?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Well, it's a bit revealing." ("upset", "narrow", "base", "mid")
        gen "What?! Really?" ("base", xpos="far_left", ypos="head")
        gen "But I spent so much money on it!" ("base", xpos="far_left", ypos="head")
        gen "Are you sure it's that bad?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Yeah, it's pretty bad alright." ("angry", "narrow", "base", "down")
        gen "Well, I guess I'll have to try to return it... Damn!" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "" ("angry", "narrow", "base", "mid")

    ##########################
    ## Sheer Nightie Outfit ##
    ##########################
    elif item == cho_outfit_sheer_nightie: #Req 16 (panties)
        gen "I've not this nightie for you to wear." ("base", xpos="far_left", ypos="head")
        cho "A nightie?" ("soft", "base", "base", "mid")
        gen "That's right." ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "Why on earth would I put on a nightie if I'm not going to bed?" ("disgust", "base", "base", "mid")
            gen "It's like breakfast for dinner, sometimes you've just got to do something to keep things different." ("base", xpos="far_left", ypos="head")
            cho "Breakfast for dinner?!" ("angry", "wide", "base", "stare")
            cho "Are you crazy?" ("mad", "wide", "base", "mid")
            gen "I mean, it might be a bit quirky, but--" ("base", xpos="far_left", ypos="head")
            cho "Doing something like that would completely mess up my metabolism!" ("mad", "narrow", "base", "mid")
            cho "My daily routine!" ("mad", "happyCl", "base", "mid")
            gen "I see... You're one of those people." ("base", xpos="far_left", ypos="head")
        elif states.cho.level < 10:
            cho "Isn't that a little bit weird?" ("open", "narrow", "raised", "mid")
            gen "Really? And here I thought nighties were common..." ("base", xpos="far_left", ypos="head")
            cho "They are, if you're about to go to bed!" ("angry", "wink", "base", "mid")
            gen "...{w=0.4} *Yawn*." ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "narrow", "base", "mid")
            gen "No?" ("base", xpos="far_left", ypos="head")
            cho "No." ("disgust", "narrow", "base", "mid")
        else: # < 15
            gen "This one, in particular." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "But, [name_genie_cho]!" ("angry", "base", "base", "down")
            cho @ cheeks blush "These are see-through!" ("angry", "narrow", "base", "down")
            gen "So?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "How would wearing these be any different to just standing here in the nude?" ("angry", "narrow", "base", "mid")
            gen "Would you rather do that instead?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "..." ("angry", "narrow", "base", "downR") #blush
            gen "Alright fine, never mind then..." ("base", xpos="far_left", ypos="head")

    ##########################
    ## Sporty Bikini Outfit ##
    ##########################
    elif item == cho_outfit_sporty_bikini: #Req 12 (panties)
        gen "I've got this sporty bikini for you to wear." ("base", xpos="far_left", ypos="head")
        if states.cho.level < 4:
            cho "A what?!" ("angry", "wide", "base", "stare")
            gen "A bikini, that's sporty..." ("base", xpos="far_left", ypos="head")
            gen "You're into that sort of thing, are you not?" ("base", xpos="far_left", ypos="head")
            cho "Bikinis?!" ("angry", "wide", "base", "mid")
            cho "Why would you think a bikini is an appropriate gift?" ("angry", "wink", "angry", "mid")
            gen "Well, it said \"sporty\" in the name, so I thought you'd like it." ("base", xpos="far_left", ypos="head")
            cho "*Ugh*..." ("disgust", "narrow", "angry", "mid")
        elif states.cho.level < 10:
            cho "A Bikini?" ("angry", "base", "base", "mid")
            gen "Yes, a sporty one!" ("base", xpos="far_left", ypos="head")
            cho "Well, that's a bit of a weird gift, but I suppose it could be useful..." ("soft", "narrow", "base", "R")
            gen "That's what I figured." ("base", xpos="far_left", ypos="head")
            gen "Here you are." ("base", xpos="far_left", ypos="head")
            cho "!!!" ("angry", "wide", "base", "down")
            cho "[name_genie_cho], what is up with these bikini bottoms!" ("angry", "narrow", "base", "mid")
            gen "Pretty cool, right?" ("base", xpos="far_left", ypos="head")
            gen "Now, if you could just put them--" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I think I'll pass." ("angry", "closed", "base", "mid")
            gen "And here I thought you were the sporty type..." ("base", xpos="far_left", ypos="head")
        else: # < 12
            cho "Alright... Let me see it..." ("soft", "narrow", "base", "mid")
            gen "Here you are." ("base", xpos="far_left", ypos="head")
            cho "*Hmm*... The top looks nice... Although the bikini bottoms are a bit revealing, don't you think?" ("soft", "narrow", "raised", "down")
            gen "Are they? They don't seem that revealing to me." ("base", xpos="far_left", ypos="head")
            cho "Just look at the back!" ("angry", "narrow", "base", "mid")
            gen "The back?" ("base", xpos="far_left", ypos="head")
            cho "Yes, the back!" ("angry", "narrow", "base", "mid")
            gen "Seems fine to me... I doubt I'll ever see them from the back, anyway." ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "narrow", "base", "mid")

    #######################
    ## Club Dress Outfit ##
    #######################
    elif item == cho_outfit_club_dress: #Req 16 (panties)
        if states.cho.level < 4:
            gen "I've got a dress for you to wear." ("base", xpos="far_left", ypos="head")
            cho "A dress?" ("soft", "narrow", "base", "mid")
            gen "That's right..." ("base", xpos="far_left", ypos="head")
            gen "It's this one right here." ("base", xpos="far_left", ypos="head")
            cho "... Are you serious?" ("angry", "base", "base", "down")
            gen "What do you mean? Don't you like my gift?" ("base", xpos="far_left", ypos="head")
            cho "This would barely go down past my..." ("angry", "base", "base", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            cho "*Ahem*... Thank you [name_genie_cho]... But I'll have to refuse." ("angry", "closed", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
        elif states.cho.level < 10:
            gen "I've got a dress for you to wear." ("base", xpos="far_left", ypos="head")
            cho "A dress?" ("soft", "narrow", "base", "mid")
            gen "That's right..." ("base", xpos="far_left", ypos="head")
            gen "It's this one right here." ("base", xpos="far_left", ypos="head")
            cho "Whoa... Looks very tight..." ("angry", "base", "base", "down")
            gen "Some would say aerodynamic..." ("base", xpos="far_left", ypos="head")
            cho "You want me to wear this during Quidditch?!" ("angry", "wide", "base", "mid")
            gen "That's not what I--" ("base", xpos="far_left", ypos="head")
            cho "I refuse!" ("angry", "closed", "angry", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
        else: # < 16
            gen "I've got this dress for you to wear." ("base", xpos="far_left", ypos="head")
            cho "A dress?" ("open", "base", "base", "mid")
            gen "Yes, it's this one right here..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "It's--" ("soft", "narrow", "base", "down")
            gen "Nice, isn't it?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I suppose... Although, what's up with those panties?" ("soft", "narrow", "base", "down")
            gen "What about them?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "They're pretty much see-through." ("disgust", "narrow", "base", "down")
            gen "Oh... I suppose they are..." ("base", xpos="far_left", ypos="head")
            gen "So... You'll wear them, right?" ("base", xpos="far_left", ypos="head")
            if states.cho.level < 13:
                cho @ cheeks heavy_blush "*Hmm*...{w=0.4} I think I'll pass..." ("open", "closed", "base", "mid")
            else:
                cho @ cheeks heavy_blush "*Hmm*...{w=0.4} Maybe some other time..." ("open", "closed", "base", "mid")

    else:
        random:
            cho "I am not wearing that..." ("clench", "closed", "base", "mid")
            cho "Thanks but no, thanks..." ("base", "base", "base", "mid")
            cho "You actually think I'd put on something like that?" ("angry", "base", "base", "mid")
            cho "Do I look like Granger [name_genie_cho]? I am not wearing something like that..." ("disgust", "narrow", "base", "mid")
            cho "This is too much." ("mad", "closed", "base", "mid")

    return

label cho_reaction_blacklist(item):
    cho "Is that really necessary, [name_genie_cho]?"

    if "top" in item.blacklist and cho.is_worn("top"):
        cho "My upper garment won't fit with this."

    if "bottom" in item.blacklist and cho.is_worn("bottom"):
        cho "Forget about my bottoms, no way they'd fit."

    if "bra" in item.blacklist and cho.is_worn("bra"):
        cho "I don't know if I can wear a bra with it."

    if "panties" in item.blacklist and cho.is_worn("panties"):
        cho "Seems as if I would need to take off my panties first to wear this."

    cho "You're asking a lot, [name_genie_cho], you know that?"
    gen "Come on Cho, you're my favourite {size=-6}snatch grabber{/size} in training!" ("base", xpos="far_left", ypos="head")
    cho "What was that?"
    gen "I said. You're my favourite snitch catcher in training." ("base", xpos="far_left", ypos="head")
    cho "*Sigh* Alright, if it means this much to you [name_genie_cho]..."
    gen "Hell yes!" ("grin", xpos="far_left", ypos="head")

    return

label cho_reaction_fallback(item):
    if states.cho.level < get_character_requirement("cho", "unequip top") and not "top" in cho.blacklist and not item.type == "top":
        $ cho.equip(cho_top_school1)

    if states.cho.level < get_character_requirement("cho", "unequip bottom") and not "bottom" in cho.blacklist and not item.type == "bottom":
        $ cho.equip(cho_bottom_school1)

    if states.cho.level < get_character_requirement("cho", "unequip bra") and not "bra" in cho.blacklist and not item.type == "bra":
        $ cho.equip(cho_bra_basic1)

    if states.cho.level < get_character_requirement("cho", "unequip panties") and not "panties" in cho.blacklist and not item.type == "panties":
        $ cho.equip(cho_panties_basic1)

    cho "Just give me a second, I need to get my clothes back in order." ("open", "base", "base", "R")
    cho "" ("base", "base", "base", "mid")
    return
