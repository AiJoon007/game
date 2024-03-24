define ton_requirements = {
    "category upper undergarment": 10,
    "category lower undergarment": 10,
    "category piercings & tattoos": 60,
    "touch head": 50,
    "touch breasts": 20,
    "touch vagina": 40,
    #"unequip panties": 6, # Tonks does not use panties unequip limits.
    #"unequip bra": 6, # Tonks does not use bra unequip limits.
    "unequip top": 20,
    "unequip bottom": 20,
    }

define ton_responses = {
    "category_fail": "ton_reaction_category_fail",
    "equip": "ton_reaction_equip",
    "equip_fail": "ton_reaction_equip_fail",
    "unequip": "ton_reaction_unequip",
    "unequip_fail": "ton_reaction_unequip_fail",
    "touch": "ton_reaction_touch",
    "touch_fail": "ton_reaction_touch_fail",
    "equip_outfit": "ton_reaction_equip_outfit",
    "equip_outfit_fail": "ton_reaction_equip_outfit_fail",
    "blacklist": "ton_reaction_blacklist",
    "fallback": "ton_reaction_fallback",
}

label ton_reaction_category_fail(category):

    if category == "upper undergarment":
        random:
            ton "*Hmm*... You'd like that, wouldn't you?" ("horny", "narrow", "base", "mid")
            ton "If you behave, then maybe I'll let you take a peek later, [name_genie_tonks]..." ("soft", "narrow", "base", "mid")
            ton "Patience dear..." ("grin", "wink", "raised", "mid")
            block:
                ton "These crystal orbs are yet to predict that I would ever allow you to ask such a thing..." ("open", "closed", "shocked", "mid")
                gen "They might just need a good dusting..." ("base", xpos="far_left", ypos="head")
                ton "Perhaps... But not right now..." ("soft", "narrow", "base", "mid")
    elif category == "lower undergarment":
        random:
            ton "You want me to put on underwear? Now, that's asking a bit much, don't you think?" ("crooked_smile", "narrow", "base", "mid")
            ton "Like the Scottish say, I'd rather let it feel the breeze." ("grin", "narrow", "base", "mid")
            ton "Underwear? Don't make me laugh..." ("base", "base", "base", "down")
            ton "You'd have to do better than that if you want this kitty to come out and play..." ("base", "narrow", "base", "mid")
    elif category == "piercings & tattoos":
        random:
            ton "I decide where such things go..." ("open", "base", "base", "mid")
            ton "You'd like that, wouldn't you? I think I'd keep such decisions for myself, thank you." ("soft", "base", "base", "R")
            ton "*Hmm*... I'd be such a bad girl if I let you do that..." ("annoyed", "closed", "base", "mid")
            ton "What would you think of me if I let you do that?" ("horny", "narrow", "base", "down")
    return

label ton_reaction_touch(what):
    if what == "head":
        $ mouse_headpat()

        random:
            ton "Is this what you do to our students? A bit tame, don't you think?" ("soft", "narrow", "base", "mid")
            ton "Surely this is not an appropriate method of rewarding your subordinate..." ("horny", "narrow", "base", "R")
            ton "Does this mean I'm your favourite student?" ("grin", "base", "raised", "mid")
            ton "Teacher, I mean..." ("base", "narrow", "base", "downR")
            ton "Such a weird custom, but I'll allow it..." ("horny", "closed", "base", "mid")
            block:
                ton "How naughty... How could I have ever allowed such indecent behaviour..." ("disgust", "narrow", "base", "mid")
                ton "Don't you dare touch my elbows next..." ("soft", "narrow", "base", "mid")

    elif what == "breasts":
        $ mouse_heart()

        random:
            ton "*Mmm*..." ("base", "narrow", "base", "up")
            ton "Trying to get put in detention are we?" ("grin", "narrow", "base", "mid")
            ton "*Tsk*... How naughty... And with an employee, no less." ("horny", "narrow", "base", "mid")
            block:
                ton "I don't remember this being part of the job description..." ("horny", "narrow", "shocked", "down")
                ton "But I'll look the other way for now..." ("grin", "closed", "base", "mid")
    elif what == "vagina":
        $ mouse_heart()

        random:
            ton "A gentleman usually doesn't kiss on the lips, but I'll allow it..." ("soft", "closed", "base", "mid")
            ton "*Hmm*...{w=0.3} Did I feel some tongue? Must've been my imagination..." ("horny", "narrow", "base", "down")
            ton "Is this one part of the extracurricular activities in my work contract?" ("grin", "narrow", "raised", "mid")
            ton "I didn't expect to receive a bonus today... What a nice surprise..." ("grin", "narrow", "raised", "mid")
    return

label ton_reaction_touch_fail(what):
    if what == "head":
        $ mouse_slap()

        random:
            ton "Stop that." ("angry", "narrow", "shocked", "mid")
            ton "Do you know how long it takes to model my hair like that?" ("annoyed", "narrow", "base", "mid")
            ton "There are two things a man shouldn't touch, her wallet and her hair." ("open", "narrow", "angry", "mid")
            ton "Don't get any funny ideas." ("soft", "narrow", "base", "mid")
            block:
                ton "Hey, don't do that!" ("open", "narrow", "base", "mid")
                ton "Let me pet you instead." ("base", "narrow", "angry", "mid")
                $ mouse_headpat()
                pause 0.35
                $ mouse_headpat()
                pause 0.35
                $ mouse_headpat()
                ton "Good boy!" ("horny", "narrow", "base", "mid")

    elif what == "breasts":
        $ mouse_slap()

        random:
            ton "That's not how a headmaster should treat their subordinates." ("annoyed", "narrow", "base", "mid")
            ton "Let's keep it civil, okay?" ("open", "narrow", "angry", "mid")
            ton "Someone fancy themselves a bit of a bad boy?" ("base", "narrow", "angry", "mid")
            ton "Hey, those are my fun bags... Don't be naughty." ("soft", "narrow", "angry", "mid")
            ton "Hey now, someone's getting a bit ahead of themselves." ("annoyed", "narrow", "base", "mid")
            ton "Those aren't for you to play with..." ("open", "narrow", "base", "mid")

    elif what == "vagina":
        $ mouse_slap()

        random:
            ton "You have to earn it first." ("annoyed", "narrow", "angry", "mid")
            ton "If you'd like to keep these hands intact, I suggest you stop it right now, [name_genie_tonks]." ("soft", "narrow", "angry", "mid")
            ton "Hey, who said you had permission to approach the chamber of secrets?" ("grin", "narrow", "angry", "mid")
            ton "That place is reserved for good boys and girls..." ("annoyed", "narrow", "angry", "mid")
            ton "That forest is forbidden entry for newbies... Let's get to know each other a bit better first..." ("soft", "narrow", "base", "mid")

    return

label ton_reaction_equip(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     ton "This <specific item description> looks awesome! I'll wear this <specific item description> with pride!"
    return

label ton_reaction_equip_fail(item):
    ### Add specific clothing reactions here.
    # if item == <DollCloth Object>:
    #     ton "I won't wear <specific item description> because!"
    # else:
    # <indent code below to be used as a fallback>

    random:
        ton "Not yet, big boy..." ("soft", "narrow", "angry", "mid")
        ton "It does look nice, but you need to deserve it..." ("grin", "narrow", "angry", "mid")
        ton "*Hmm*... What would you think of me if I wore this?... Later, perhaps." ("soft", "narrow", "base", "mid")

    return

label ton_reaction_unequip(item):
    ### Example
    # if item.type == "panties":
    #    if states.ton.level > 15:
    #        ton "You want to see my snatch?"
    #        ton "You got it [name_genie_hermione]!"
    #
    return

label ton_reaction_unequip_fail(item):

    ### Bra and panties checks are not in use, as Tonks doesn't mind NOT wearing underwear.
    # if item.type == "panties":
    #     ton "I'm n-not comfortable with that, sir..."

    # elif item.type == "bra":
    #     ton "P-please, I don't want to..."

    if item.type == "top":
        ton "Someone's being naughty... I might have to give you a spanking for that." ("grin", "narrow", "angry", "mid")
        ton "Just kidding! Sure, have a quick look, [name_genie_tonks]." ("grin", "narrow", "raised", "mid")
        $ char_active.strip("top", "robe")
        ton "" ("base", "base", "base", "mid")
        pause 1.0
        ton "" ("base", "closed", "base", "down")
        pause 1.0
        ton "" ("grin", "narrow", "base", "mid")
        $ char_active.wear("top", "robe")
        gen "What gives?!" ("angry", xpos="far_left", ypos="head")
        ton "Time's up." ("base", "wink", "base", "mid")
        gen "......" ("base", xpos="far_left", ypos="head")
        ton "" ("base", "base", "base", "mid")

    elif item.type == "bottom":

        random:
            ton "I thought patience came with old age..." ("base", "base", "raised", "R")
            ton "What's the point in that? You already know what's under there, don't you?" ("soft", "narrow", "base", "mid")
            ton "You could do with learning some restraint... Perhaps I need to teach you a thing or two..." ("grin", "narrow", "base", "mid")
            ton "Eager, are we? Well, I can't say I blame you..." ("open", "closed", "base", "mid")
    return

label ton_reaction_equip_outfit(item):
    ### Add specific Outfit reactions here.

    ##################
    ## Auror Outfit ##
    ##################
    if item == ton_outfit_default:
        gen "Could you put on your regular clothing for me?" ("base", xpos="far_left", ypos="head")
        ton "You mean my Auror uniform?" ("open", "base", "raised", "mid")
        gen "Is that what it is?" ("base", xpos="far_left", ypos="head")
        ton "Well... It meets all the requirements of an Auror uniform." ("base", "narrow", "base", "R")
        ton "Of course I made my own adjustments to it..." ("horny", "narrow", "base", "down")
        gen "Like not wearing underwear?" ("base", xpos="far_left", ypos="head")
        ton "Well... The ministry didn't mention any underwear requirements, so..." ("base", "narrow", "base", "mid")
        gen "Perverts the lot of them..." ("base", xpos="far_left", ypos="head")
        ton "I'll just put it on then shall I." ("base", "base", "base", "mid")

    ###################
    ## School Outfit ##
    ###################
    elif item == ton_outfit_school:
        gen "Feeling like revisiting your student days for a bit?" ("base", xpos="far_left", ypos="head")
        ton "Are you planning on spanking me over your knee, headmaster?" ("soft", "narrow", "base", "mid")
        gen "I--{w=0.4} Was that something that happened during your school days?" ("base", xpos="far_left", ypos="head")
        ton "I wish..." ("base", "narrow", "base", "R")
        gen "No, what I meant was..." ("base", xpos="far_left", ypos="head")
        gen "I've got this school uniform for you to wear today." ("base", xpos="far_left", ypos="head")
        ton "Is it a sexy school uniform?" ("base", "narrow", "raised", "mid")
        gen "You know me too well..." ("base", xpos="far_left", ypos="head")
        ton "Alright, let me just put it on for you then... Headmaster..." ("horny", "narrow", "base", "mid")

    ##################
    ## Flag Bikinis ##
    ##################
    elif item == ton_outfit_bikini_1:
        gen "You know what would be kinda crazy?" ("base", xpos="far_left", ypos="head")
        ton "what?" ("base", "base", "base", "mid")
        gen "If you like... Just stood in my office wearing this bikini..." ("base", xpos="far_left", ypos="head")
        ton "Are you asking or is this a hypothetical?" ("base", "narrow", "base", "R")
        gen "What if I'm hypothetically asking?" ("base", xpos="far_left", ypos="head")
        ton "Well if you were then I'd probably say yes, that is a pretty crazy thing to ask." ("soft", "base", "base", "mid")
        gen "But you'd still do it, right?" ("base", xpos="far_left", ypos="head")
        ton "Sure, why not..." ("base", "base", "base", "mid")
    elif item == ton_outfit_bikini_2:
        gen "Do you believe what they say about stripes making you look slimmer?" ("base", xpos="far_left", ypos="head")
        ton "I've never really had the need to think about that." ("base", "base", "base", "mid")
        gen "I was thinking we could give it a test and see if those big titties of yours would look any different." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*?" ("soft", "base", "base", "mid")
        gen "With this striped bikini!" ("base", xpos="far_left", ypos="head")
        ton "You could just have asked me in a normal way to put it on." ("soft", "base", "base", "mid")
        gen "Well... That's not as fun..." ("base", xpos="far_left", ypos="head")
    elif item == ton_outfit_bikini_3:
        gen "I've got this bikini with the UK flag on it for you to wear." ("base", xpos="far_left", ypos="head")
        ton "Oh? Any particular reason." ("base", "base", "raised", "mid")
        gen "I think you'd look quite spiffing in it..." ("base", xpos="far_left", ypos="head")
        ton "I guess that's a good enough reason..." ("base", "narrow", "base", "R")
    elif item == ton_outfit_bikini_4:
        gen "Miss Tonks, have you ever experienced true freedom?" ("base", xpos="far_left", ypos="head")
        ton "Every time I take my bra off." ("grin", "narrow", "base", "R")
        gen "Well today--" ("grin", xpos="far_left", ypos="head")
        gen "*Err*... Well, this is awkward." ("base", xpos="far_left", ypos="head")
        gen "I got this Bikini with the US flag on it for you to wear." ("base", xpos="far_left", ypos="head")
        ton "A bikini? Why not body paint?" ("soft", "narrow", "base", "mid")
        gen "*Hmm*... Maybe next time, but this will have to do for now..." ("base", xpos="far_left", ypos="head")
        ton "Alright then." ("base", "base", "base", "mid")

    ######################
    ## Skimpy Swimsuits ##
    ######################
    elif item == ton_outfit_swimsuit_1:
        gen "Did anyone tell you how good you look in a swimsuit?" ("base", xpos="far_left", ypos="head")
        ton "Yes, why?" ("soft", "base", "raised", "mid")
        gen "Why you're about to hear it again once you put this on." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... Clever boy..." ("base", "narrow", "base", "R")
    elif item == ton_outfit_swimsuit_2:
        gen "I've got this striped swimsuit for you to wear." ("base", xpos="far_left", ypos="head")
        ton "In here?" ("soft", "base", "raised", "mid")
        gen "Yes, unless today is the day of the beach episode." ("base", xpos="far_left", ypos="head")
        ton "Beach episode?" ("open", "base", "base", "mid")
        gen "Yes please..." ("base", xpos="far_left", ypos="head")
        ton "*Huh*?" ("upset", "base", "raised", "mid")
        gen "... For the fan service." ("base", xpos="far_left", ypos="head")
        ton "Okay then..." ("soft", "narrow", "base", "down")
        ton "I'll just put this on shall I?" ("base", "base", "base", "mid")
    elif item == ton_outfit_swimsuit_3:
        gen "How about you put on this swimsuit for me?" ("base", xpos="far_left", ypos="head")
        ton "*Hmm*?" ("base", "narrow", "raised", "down")
        ton "Is this the American flag?" ("soft", "base", "base", "down")
        gen "Fuck yes it is..." ("base", xpos="far_left", ypos="head")
        gen "Now put this on and make your country proud!" ("base", xpos="far_left", ypos="head")
        ton "But I'm not..." ("soft", "base", "base", "down")
        gen "For your country!" ("base", xpos="far_left", ypos="head")
        ton "Alright then." ("base", "closed", "base", "mid")
        ton "" ("base", "base", "base", "mid")

    ###################
    ## Casual Outfit ##
    ###################
    elif item == ton_outfit_casual:
        gen "Could you put on this sexy casual outfit?" ("base", xpos="far_left", ypos="head")
        ton "Most certainly..." ("grin", "wink", "base", "mid")
        ton "These leggings are very much my style, I must say." ("grin", "narrow", "base", "mid")
        gen "Is it because they show off every single curve of your body?" ("base", xpos="far_left", ypos="head")
        ton "How did you know?" ("soft", "wide", "shocked", "mid")
        gen "Lucky guess..." ("base", xpos="far_left", ypos="head")

    #############
    ## Nightie ##
    #############
    elif item == ton_outfit_nightie:
        gen "I've got this nightie for you to wear." ("base", xpos="far_left", ypos="head")
        ton "Why not just ask me to take all of my clothes off?" ("open", "base", "base", "down")
        gen "Why because that would be indecent!" ("base", xpos="far_left", ypos="head")
        play sound "sounds/giggle2_loud.ogg"
        ton "*Giggles*" ("base", "closed", "base", "mid")
        ton "I suppose I'll have to wear it then..." ("base", "wink", "base", "mid")
        ton "In the name of decency." ("grin", "base", "base", "mid")

    ##################
    ## Bunny outfit ##
    ##################
    elif item == ton_outfit_bunny:
        gen "I've got this sexy bunny outfit for you to wear today." ("base", xpos="far_left", ypos="head")
        ton "What's with you boys and bunny costumes?" ("soft", "narrow", "raised", "R")
        gen "Do you even have to ask?" ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... I suppose the ears are kind of--" ("open", "narrow", "base", "down")
        gen "It highlights the shape of the ass!" ("base", xpos="far_left", ypos="head")
        ton "Of course that's why." ("soft", "narrow", "base", "down")
        ton "Very well..." ("base", "base", "base", "mid")

    ###################
    ## Dressing Gown ##
    ###################
    elif item == ton_outfit_dressing_gown:
        gen "You looked pretty hot in that dressing gown last time." ("base", xpos="far_left", ypos="head")
        ton "Why thank you... I usually sleep naked, but I thought I should probably not be as casual outside my office..." ("soft", "narrow", "base", "mid")
        gen "I'd like for you to wear it inside my office." ("base", xpos="far_left", ypos="head")
        ton "Of course you do..." ("soft", "narrow", "base", "R")
        ton "Well I suppose wearing it more often won't hurt." ("soft", "base", "base", "mid")

    #################
    ## Silky Dress ##
    #################
    elif item == ton_outfit_silky:
        gen "I've got you one of the most splendid and luxurious outfits that I could find." ("base", xpos="far_left", ypos="head")
        ton "Luxurious you say?" ("soft", "base", "raised", "mid")
        gen "Why yes... Made by the finest silk, no less." ("base", xpos="far_left", ypos="head")
        ton "Silk? Now that's--" ("grin", "wide", "base", "mid")
        ton "Oh, I see why you've got it..." ("soft", "narrow", "base", "down")
        gen "To spoil my favourite teacher?" ("base", xpos="far_left", ypos="head")
        ton "..." ("soft", "narrow", "base", "mid")
        gen "Don't tell Snape." ("base", xpos="far_left", ypos="head")
        ton "It's pretty much see-through." ("soft", "narrow", "base", "mid")
        gen "Is it? I had no idea!" ("base", xpos="far_left", ypos="head")
        ton "..." ("base", "narrow", "base", "R")
        gen "And here I spent so much money on it!" ("base", xpos="far_left", ypos="head")
        ton "I didn't say that was a bad thing." ("base", "narrow", "base", "mid")
        ton "Give me a moment to put it on." ("base", "base", "base", "mid")

    ##################
    ## Skimpy Dress ##
    ##################
    elif item == ton_outfit_skimpy_dress:
        gen "I've got a dress for you to wear today." ("base", xpos="far_left", ypos="head")
        ton "Oh?" ("soft", "base", "base", "mid")
        gen "This one." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... I can see why you picked it." ("base", "narrow", "base", "down")
        ton "It might be hard to keep my nipples covered in this one, but I'll try." ("base", "base", "base", "mid")
        gen "Please don't." ("base", xpos="far_left", ypos="head")

    ################
    ## Club Dress ##
    ################
    elif item == ton_outfit_club_dress:
        gen "I've got this club dress for you to wear." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... Are you planning on taking me out to dance?" ("soft", "narrow", "base", "mid")
        gen "These hips are meant for pushing, not dancing, I'm afraid..." ("base", xpos="far_left", ypos="head")
        gen "No, I got you this one purely because of how sexy you'd look in it." ("base", xpos="far_left", ypos="head")
        ton "As if you'd get me an outfit for any other purpose..." ("base", "narrow", "base", "R")
        play sound "sounds/giggle2_loud.ogg"
        ton "*Giggles*" ("grin", "narrow", "base", "R")
        ton "Well, you could try, but I'm sure I'll look sexy in it either way." ("base", "closed", "base", "mid")
        gen "Is that a challenge?" ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... Go ahead." ("soft", "base", "base", "mid")
        ton "But first, let's judge the sexiness factor of this one..." ("base", "base", "base", "mid")

    #####################
    ## Succubus Outfit ##
    #####################
    elif item == ton_outfit_succubus:
        gen "Could you put on the succubus outfit?" ("base", xpos="far_left", ypos="head")
        ton "Outfit? What on earth do you mean?" ("soft", "base", "raised", "mid")
        gen "The one with the wings and stuff." ("base", xpos="far_left", ypos="head")
        ton "Oh... Why something like that can't be done with an outfit, I'll have to grow some wings myself." ("grin", "wink", "base", "mid")
        gen "You will have to what?!" ("base", xpos="far_left", ypos="head")
        play sound "sounds/giggle2_loud.ogg"
        ton "*Giggles*" ("grin", "narrow", "base", "mid")
        gen "Oh, you're just messing with me..." ("base", xpos="far_left", ypos="head")
        ton "..." ("grin", "base", "base", "R")
        gen "You are...{w=0.4} Aren't--" ("base", xpos="far_left", ypos="head")
        play sound "sounds/magic3.ogg"
        $ tonks.equip(item)
        ton "" ("horny", "narrow", "base", "mid")
        with flash

    #####################
    ## Cavegirl Outfit ##
    #####################
    elif item == ton_outfit_cavegirl:
        gen "I've got the perfect outfit for you to wear when clubbing." ("base", xpos="far_left", ypos="head")
        gen "Here..." ("base", xpos="far_left", ypos="head")
        ton "Clubbing? Are you sure?" ("upset", "narrow", "base", "down")
        gen "As in smash things with a club." ("base", xpos="far_left", ypos="head")
        ton "What?" ("clench", "narrow", "base", "mid")
        gen "Trust me, you'd be on the floor laughing if you had watched the cartoon." ("base", xpos="far_left", ypos="head")
        ton "Did the person in this cartoon also have one of their breasts exposed?" ("soft", "base", "raised", "down")
        gen "I wish..." ("base", xpos="far_left", ypos="head")
        ton "So I'll just be fulfilling some fantasy of yours then?" ("soft", "narrow", "base", "mid")
        gen "Pretty much..." ("base", xpos="far_left", ypos="head")
        ton "Alright then..." ("horny", "narrow", "base", "mid")

    #####################
    ## Pullover Outfit ##
    #####################
    elif item  == ton_outfit_pullover:
        gen "Could you put on your pullover outfit for me?" ("base", xpos="far_left", ypos="head")
        ton "A pullover?" ("soft", "base", "raised", "mid")
        ton "But what if some handsome vampire turned up?" ("annoyed", "narrow", "base", "R")
        gen "What?" ("base", xpos="far_left", ypos="head")
        ton "My neck would be totally covered!" ("disgust", "narrow", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Some of your thighs should still be visible if that's a concern..." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... I suppose... It's not ideal, but I guess it will have to do." ("base", "narrow", "base", "mid")

    #################
    ### Elf Outfit ##
    #################
    elif item == ton_outfit_elf:
        gen "You've been so helpful lately, so I've got you an outfit." ("base", xpos="far_left", ypos="head")
        ton "That's very--" ("base", "wide", "base", "mid")
        ton "What's this?" ("soft", "base", "raised", "down")
        gen "Why, it's an elf costume, of course." ("base", xpos="far_left", ypos="head")
        gen "For Santa's sexy little helper." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... And you're supposed to be Santa, I suppose?" ("base", "narrow", "raised", "mid")
        gen "Why of course... Although you're free to handle Santa's sack if you like." ("base", xpos="far_left", ypos="head")

    ####################
    ### Ribbon Outfit ##
    ####################
    elif item == ton_outfit_ribbon:
        gen "Ever wrapped yourself up tightly before?" ("base", xpos="far_left", ypos="head")
        ton "Of course... Although I usually have another person do it for me." ("grin", "wink", "base", "mid")
        gen "Well today I'd like you to wrap yourself up for me like a present!" ("base", xpos="far_left", ypos="head")
        ton "You sure you'd want that?" ("soft", "base", "raised", "mid")
        gen "Of course!" ("base", xpos="far_left", ypos="head")
        ton "But what if you've been too naughty this year for you to unwrap me?" ("soft", "narrow", "raised", "mid")
        gen "I'll just have you unwrap yourself in that case." ("base", xpos="far_left", ypos="head")
        ton "*Hmph*... That's cheating..." ("soft", "base", "base", "R")

    ##################
    ### Xmas Outfit ##
    ##################
    elif item == ton_outfit_xmas:
        gen "Miss Tonks, you know what the best thing about Christmas is?" ("base", xpos="far_left", ypos="head")
        ton "The presents?" ("base", "base", "raised", "mid")
        gen "After that." ("base", xpos="far_left", ypos="head")
        ton "The food?" ("soft", "base", "base", "mid")
        gen "Not that." ("base", xpos="far_left", ypos="head")
        ton "The company?" ("grin", "base", "raised", "mid")
        gen "The sexy Christmas outfits!" ("base", xpos="far_left", ypos="head")
        ton "I should've guessed... So, you've got me something like that to wear I assume?" ("horny", "narrow", "base", "mid")
        gen "Yes, put this on for me will you?" ("base", xpos="far_left", ypos="head")
        ton "Very well..." ("base", "base", "base", "mid")

    ##################
    ## Santa Outfit ##
    ##################
    elif item == ton_outfit_santa:
        gen "Ho-Ho-Ho!" ("grin", xpos="far_left", ypos="head")
        ton "Yes?" ("soft", "base", "base", "mid")
        gen "No, I'm doing a Santa laugh!" ("base", xpos="far_left", ypos="head")
        ton "Oh, I see!" ("grin", "base", "raised", "mid")
        gen "Anyway, I've got this sexy Santa costume for you to wear." ("grin", xpos="far_left", ypos="head")
        ton "*Mmm*... Say no more..." ("horny", "narrow", "base", "mid")

    ###################
    ## Lady D Outfit ##
    ###################
    elif item == ton_outfit_lady_D:
        gen "I've got this Lady D outfit for you to wear." ("base", xpos="far_left", ypos="head")
        ton "Lady D?" ("soft", "base", "raised", "mid")
        ton "Does it come with a strap-on or something?" ("horny", "narrow", "base", "mid")
        gen "What... No, it's a fictional character..." ("base", xpos="far_left", ypos="head")
        ton "A fictional character... With a strap-on?" ("grin", "narrow", "base", "mid")
        gen "What's with you and... Oh, I see the confusion..." ("base", xpos="far_left", ypos="head")
        gen "No, it's this outfit." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... Very imposing..." ("base", "narrow", "base", "down")
        ton "Although it would've been even more so with a strap-on..." ("grin", "base", "base", "mid")
        gen "..." ("angry", xpos="far_left", ypos="head")
        play sound "sounds/giggle2_loud.ogg"
        ton "*Giggles*" ("grin", "wink", "base", "mid")

    #########################
    ## Police Woman Outfit ##
    #########################
    elif item == ton_outfit_police:
        gen "Remember that time when you showed up in a sexy Police outfit and I thought you were the magic police?" ("base", xpos="far_left", ypos="head")
        ton "No?" ("soft", "base", "raised", "mid")
        gen "Maybe that was a dream..." ("base", xpos="far_left", ypos="head")
        gen "Anyway, It would be pretty sweet if you put this on for me." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*..." ("base", "narrow", "base", "down")
        ton "Why not..." ("soft", "base", "base", "mid")

    #####################
    ## Wrestling Coach ##
    #####################
    elif item == ton_outfit_wrestling_coach:
        gen "Could you put on this sports coach outfit for me?" ("base", xpos="far_left", ypos="head")
        ton "Sports coach? There are other sports than Quidditch?" ("soft", "base", "raised", "mid")
        gen "...{w=0.4} Excuse me?" ("base", xpos="far_left", ypos="head")
        ton "I'm just joking, I know there are other sports." ("base", "base", "base", "R")
        ton "Although I'm not that of a big fan of Gobstones and Wizard Chess myself." ("open", "narrow", "base", "mid")
        ton "They don't have any sexy uniforms." ("horny", "narrow", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "I'm talking about real sports... Like Football and Basketball." ("base", xpos="far_left", ypos="head")
        ton "Never heard of it." ("open", "base", "base", "mid")
        gen "Volleyball?" ("base", xpos="far_left", ypos="head")
        ton "Nope." ("annoyed", "base", "base", "mid")
        gen "Tennis?" ("base", xpos="far_left", ypos="head")
        ton "No clue." ("upset", "base", "base", "mid")
        gen "You're missing out..." ("base", xpos="far_left", ypos="head")
        gen "Beach Volleyball is a sight to behold." ("base", xpos="far_left", ypos="head")
        ton "Do you wear swimsuits?" ("soft", "base", "base", "mid")
        gen "Hell yeah!" ("base", xpos="far_left", ypos="head")
        ton "I might need to look it up then..." ("horny", "narrow", "base", "R")
        gen "So, could you put on the outfit?" ("base", xpos="far_left", ypos="head")
        ton "The what?" ("soft", "base", "base", "mid")
        ton "Oh, yes... Certainly." ("base", "base", "base", "mid")

    #####################
    ## Mechanic Outfit ##
    #####################
    elif item == ton_outfit_mechanic:
        gen "You know, I think you would look great in this mechanic attire." ("base", xpos="far_left", ypos="head")
        ton "A mechanic you say?" ("open", "base", "raised", "mid")
        ton "I don't know what kind of school mechanics attend, or what kind of magic they use, but I sure do like their fashion taste." ("horny", "base", "base", "down")
        ton "Sure, I'll wear it." ("base", "narrow", "base", "mid")
        gen "Splendid." ("base", xpos="far_left", ypos="head")

    #####################
    ## Tuxedo (Office) ##
    #####################
    elif item == ton_outfit_office:
        gen "Time to suit up." ("base", xpos="far_left", ypos="head")
        ton "Hmm? Are we expecting company." ("open", "narrow", "base", "mid")
        gen "No, but I'd like you to wear something as if we were one." ("base", xpos="far_left", ypos="head")
        ton "Were... one?" ("soft", "narrow", "raised", "mid")
        gen "A company." ("grin", xpos="far_left", ypos="head")
        ton "..." ("soft", "narrow", "raised", "mid")
        gen "I've got a suit for you to wear." ("base", xpos="far_left", ypos="head")
        ton "A suit? And here I thought I'd escaped the dreary fashion sense of the ministry..." ("annoyed", "narrow", "base", "mid")
        ton "Very well, as long as I don't have to act professional..." ("base", "narrow", "base", "R")

    # TODO: Blacklist fallbacks have to be added.
    return

label ton_reaction_equip_outfit_fail(item):
    ### Add specific Outfit reactions here.

    ###################
    ## School Outfit ##
    ###################
    # if item == ton_outfit_school:

    ##################
    ## Flag Bikinis ##
    ##################
    # elif item == ton_outfit_bikini_1:
    # elif item == ton_outfit_bikini_2:
    # elif item == ton_outfit_bikini_3:
    # elif item == ton_outfit_bikini_4:

    #####################
    ## Skimpy Swimsuit ##
    #####################
    # elif item == ton_outfit_swimsuit_1:
    # elif item == ton_outfit_swimsuit_2:
    # elif item == ton_outfit_swimsuit_3:

    ###################
    ## Casual Outfit ##
    ###################
    # elif item == ton_outfit_casual:

    #############
    ## Nightie ##
    #############
    # elif item == ton_outfit_nightie:

    ##################
    ## Bunny outfit ##
    ##################
    # elif item == ton_outfit_bunny:

    ###################
    ## Dressing Gown ##
    ###################
    # elif item == ton_outfit_dressing_gown:

    #################
    ## Silky Dress ##
    #################
    # elif item == ton_outfit_silky:

    ##################
    ## Skimpy Dress ##
    ##################
    # elif item == ton_outfit_skimpy_dress:

    ################
    ## Club Dress ##
    ################
    # elif item == ton_outfit_club_dress:

    #####################
    ## Succubus Outfit ##
    #####################
    # elif item == ton_outfit_succubus:

    #####################
    ## Cavegirl Outfit ##
    #####################
    # elif item == ton_outfit_cavegirl:

    #####################
    ## Pullover Outfit ##
    #####################
    #elif item  == ton_outfit_pullover:

    #################
    ### Elf Outfit ##
    #################
    # elif item == ton_outfit_elf:

    ####################
    ### Ribbon Outfit ##
    ####################
    # elif item == ton_outfit_ribbon:

    ##################
    ### Xmas Outfit ##
    ##################
    # elif item == ton_outfit_xmas:

    ##################
    ## Santa Outfit ##
    ##################
    # elif item == ton_outfit_santa:

    ###################
    ## Lady D Outfit ##
    ###################
    # elif item ==ton_outfit_lady_D:

    #####################
    ## Wrestling Coach ##
    #####################

    #####################
    ## Tuxedo (Office) ##
    #####################
    #elif item == ton_outfit_office:
        #gen "I think it's time you dressed a bit more smartly."
        #ton "*Hmm*... Am I not clever enough for you?"
        #gen "That's not it, I've got a suit I'd like you to wear."
        #ton "I see..."
        #ton "Looks like something the bozos at the ministry would wear."
        #gen "Still, I'm sure you'd look great in it."
        #ton "Sweetie... I look good in anything I wear."
        #gen "You sure about that?"
        #ton "Nice try..."
        #ton "Convincing me to wear it just so that I get to prove a point won't work on me."
        #gen "Damn."
    #elif item == ton_outfit_wrestling_coach:
        #gen "Could you put on this sports coach outfit for me?" ("base", xpos="far_left", ypos="head")
        #ton "Something wrong with my current clothes?"
        #gen "*Err*..." ("base", xpos="far_left", ypos="head")
        #ton "Sorry but this doesn't show off my figure enough."
        #gen "Yeah, I didn't know what I was--" ("base", xpos="far_left", ypos="head")
        #gen "(Wait, did she say it doesn't show it off enough?)" ("base", xpos="far_left", ypos="head")
    # <indent code below to be used as a fallback>

    ton "It looks lovely, but you'd have to prove yourself a bit more before I put that on..." ("grin", "narrow", "annoyed", "mid")

    return

label ton_reaction_blacklist(item):
    ton "*Oooh* that's racy!"

    if "top" in item.blacklist and tonks.is_worn("top"):
        ton "I'd need to take off my top."

    if "bottom" in item.blacklist and tonks.is_worn("bottom"):
        ton "It would be very unfashionable to wear a bottom garment with that."

    if "bra" in item.blacklist and tonks.is_worn("bra"):
        ton "My girls would definitely appreciate me letting them breathe."
        gen "Your tits, you mean." ("grin", xpos="far_left", ypos="head")
        ton "Now, now, don't get needy, my dear headmaster."

    if "panties" in item.blacklist and tonks.is_worn("panties"):
        ton "There's not a single pair of panties in the world that would fit this."

    gen "Well, what's the verdict?" ("base", xpos="far_left", ypos="head")
    ton "Simply put-- I love it."
    gen "Jackpot!" ("grin", xpos="far_left", ypos="head")

    return

label ton_reaction_fallback(item):
    if states.ton.level < get_character_requirement("tonks", "unequip top") and not "top" in tonks.blacklist and not item.type == "top":
        $ tonks.equip(ton_top_auror)

    if states.ton.level < get_character_requirement("tonks", "unequip bottom") and not "bottom" in tonks.blacklist and not item.type == "bottom":
        $ tonks.equip(ton_bottoms_leggings)

    # if states.ton.level < get_character_requirement("tonks", "unequip bra") and not "bra" in tonks.blacklist and not item.type == "bra":
    #     $ tonks.equip(None)

    # if states.ton.level < get_character_requirement("tonks", "unequip panties") and not "panties" in tonks.blacklist and not item.type == "panties":
    #     $ tonks.equip(None)

    ton "Just give me a second, I need to get my clothes back in order." ("open", "base", "base", "R")
    ton "" ("base", "base", "base", "mid")
    return
