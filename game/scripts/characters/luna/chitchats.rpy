label luna_chitchat:

    if states.lun.chatted:
        return

    $ states.lun.chatted = True

    # Story related chitchats

    if states.lun.ev.intro.e2_complete and not states.lun.ev.spectrespecs.e3_complete and thequibbler_ITEM.owned < 1:
        lun "Have you acquired a copy of the magazine yet?" ("open", "base", "raised", "mid")
        gen "Not yet." ("base", xpos="far_left", ypos="head")
        lun "I'm sure somebody in the castle should have a copy." ("base", "base", "base", "R")
        gen "Can't you give me--" ("base", xpos="far_left", ypos="head")
        lun "Oh I'm so happy, my daddy will be ecstatic once he hears that {b}the{/b} Albus Dumbledore is buying his magazine." ("smile", "happyCl", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "(Guess I should have a gander around the castle and see if anyone can get me a copy....)" ("base", xpos="far_left", ypos="head")
        return

    if states.lun.ev.spectrespecs.e2_complete and not states.lun.ev.spectrespecs.e3_complete:
        lun "Have you acquired a copy of the magazine yet?" ("open", "base", "raised", "mid")
        gen "I have!" ("base", xpos="far_left", ypos="head")
        lun "Great!" ("smile", "happyCl", "base", "mid")
        lun "What did you think?" ("base", "base", "base", "mid")
        gen "Oh, I haven't read it yet." ("base", xpos="far_left", ypos="head")
        lun "Oh..." ("soft", "base", "base", "R")
        lun "Then let me know what you think once you've read it." ("open", "base", "base", "mid")
        return

    if states.lun.tier == 1:

        random:
            block:
                lun "We were brewing a Draught of Peace during today's potions lesson, which reminded me of an article in The Quibbler about Valerian root." ("soft", "base", "base", "mid")
                lun "It described the root's calming properties and how when you chew on it, it will produce the same effect as the potion." ("open", "base", "base", "mid")
                lun "I brought this fact up to professor Snape, but he just laughed and prompted me to have at it." ("normal", "base", "base", "mid")
                lun "So I tried chewing on one... And let me tell you... I've never felt so relaxed in my life." ("grin", "base", "base", "mid")

            block:
                lun "I had a strange dream last night..." ("soft", "base", "base", "mid")
                lun "I was alone, sitting by a tree, when suddenly a rabbit carrying a pocket-watch jumped by..." ("open", "base", "base", "mid")
                lun "Must've been the cheese I ate before going to bed..." ("open", "base", "base", "down")

            block:
                lun "Acid pops are my favourite." ("crooked_smile", "base", "base", "mid")
                lun "I always make sure to get some when I'm in Hogsmeade." ("base", "wink", "base", "mid")
                lun "" ("base", "base", "base", "mid")

            block:
                lun "I was a bit disappointed when I found out that the Thestrals live deep inside the forbidden forest." ("annoyed", "base", "base", "R")
                lun "I'm hoping I'll be able to ride one someday..." ("grin", "base", "base", "mid")

            block:
                lun "[name_genie_luna]...{w=0.4} There's something I've been meaning to ask you." ("open", "closed", "base", "mid")
                lun "Could we avoid putting up so many mistletoes during the holiday celebrations?" ("soft", "base", "base", "mid")
                lun "It would highly decrease the risk of a Nargle infestation." ("open", "base", "base", "mid")

            block:
                lun "Why are there no school trips at Hogwarts?" ("open", "base", "raised", "mid")
                lun "I'd love to take one to Sweden and look for the Crumple-Horned Snorkack." ("grin", "base", "base", "mid")

            block:
                lun "[name_genie_luna], you really need to do something about Peeves." ("annoyed", "base", "base", "R")
                lun "He's been following me around chanting \"Loony Luna, Loony Luna, who would ever do yah\"..." ("open", "base", "base", "R")

            block:
                lun "I spotted some wrackspurts in one of the broom closets the other day." ("open", "closed", "base", "mid")
                lun "You might wonder what I was doing in there." ("angry", "closed", "base", "mid")
                lun "Inspecting the brooms for wrackspurts of course!" ("angry", "base", "base", "mid")

            block:
                lun "I hope we'll be able to contain this infestation within the school." ("open", "closed", "base", "mid")
                lun "I'm a bit worried it might spread to Hogsmeade during one of our student outings." ("annoyed", "base", "base", "R")

            block:
                lun "[name_genie_luna], do you think wrackspurts could spread to animals?" ("open", "wide", "base", "mid")
                lun "No, don't say anything... I can't bear the thought of it!" ("open", "happyCl", "base", "mid")

    elif states.lun.tier == 2:

        random:
            lun "[name_genie_luna], Is it supposed to feel really good when you rub your thighs together?" ("soft", "base", "raised", "mid")

            block:
                lun "My whole idea of wrackspurts got shattered once I found out they don't only attack people." ("open", "happyCl", "base", "mid")
                lun "But they also hide in clothes!" ("open", "wide", "base", "mid")
                lun "I found a sock completely filled with them once!" ("open", "wide", "base", "mid")

            block:
                lun "I feel like I could've nipped this infestation in the bud if only my proposal of mandatory spectrespecs had gone through." ("open", "closed", "base", "mid")
                lun "At least we can count ourselves lucky to have such a great headmaster here to help deal with this unfortunate situation." ("base", "narrow", "base", "mid")

            block:
                lun "I used to think that wrackspurts could only fly small distances." ("open", "base", "base", "mid")
                lun "But then I saw some on the ceiling in Tonks' classroom!" ("clench", "wide", "base", "mid")
                lun "I wonder if she was trying to fend them off with defensive magic..." ("open", "base", "base", "R")

            block:
                lun "I still can't believe you've managed to channel the wrackspurts though your penis, [name_genie_luna]." ("grin", "base", "base", "mid")
                lun "You've got to teach me how to do that!" ("base", "wink", "base", "mid")

            block:
                lun "Are you able to cast other magic through your penis, [name_genie_luna]?" ("open", "base", "raised", "mid")
                lun "We should try it sometime!" ("grin", "base", "base", "mid")

            block:
                lun "I can't help but imagine what a patronus would look like when bursting through the tip of a penis..." ("base", "closed", "base", "mid")
                lun "...{w=0.4} Is that a weird thing to be imagining?" ("soft", "base", "base", "mid")

            block:
                lun "I'm still not so sure I'll ever be able to get rid of these spurts myself..." ("annoyed", "narrow", "base", "down")
                lun "If it requires a lot of focus, that is...{w=0.4} I'm not very good at that." ("soft", "narrow", "base", "R")

            block:
                lun "Are you sure we shouldn't clean your desk, [name_genie_luna]?" ("soft", "base", "raised", "mid")
                lun "Or are you worried the wrackspurts might spread elsewhere if we move them?" ("open", "base", "base", "mid")

            block:
                lun "Can you inspect my body today, [name_genie_luna]?" ("angry", "base", "raised", "mid")
                lun "Can you?" ("angry", "wide", "base", "mid")
                lun "Please." ("angry", "wide", "base", "mid")

    elif states.lun.tier == 3:

        random:
            lun "*Ehm*...{w=0.4} Hypothetically...{w=0.4} What would a person do if they got some wrackspurts stuck to their underwear?" ("open", "base", "base", "R")
            lun "I'm so glad that the inspection was successful...{w=0.4} I don't know what would've done if we didn't make any progress..." ("base", "narrow", "base", "R")

            block:
                lun @ cheeks blush "Is it possible for someone to possess magical fingers, [name_genie_luna]?" ("soft", "base", "base", "mid")
                lun @ cheeks blush "You know, like how some people are born with innate magical abilities." ("open", "closed", "base", "mid")
                lun @ cheeks blush "It would explain a lot about what I felt when you touched me down there..." ("soft", "narrow", "base", "R")

            block:
                lun @ cheeks blush "That thing I felt on my back when you helped me..." ("open", "base", "base", "R")
                lun "*Hmm*... Nevermind..." ("base", "narrow", "base", "down")

            block:
                lun "I've been trying to figure out if there's any other sensitive areas on my body." ("open", "base", "base", "down")
                lun "But doing so isn't that simple when you're ticklish..." ("annoyed", "base", "base", "down")

            block:
                lun "I've been thinking...{w=0.4} Since my nipples get hard sometime, perhaps I'd be able to expel the wrackspurts through them like you do through your penis." ("soft", "base", "raised", "mid")

            block:
                lun "The wrackspurts appear to have been building up even faster than normal recently." ("soft", "narrow", "base", "R")
                lun "I wonder why..." ("soft", "base", "base", "down")

            block:
                lun "I will become the greatest master baiter ever!" ("smile", "closed", "base", "mid")
                lun "You watch me!" ("base", "wink", "base", "mid")

            block:
                lun "You said that my naked body helped you release the spurts...{w=0.4} What did you mean by that exactly?" ("soft", "base", "raised", "mid")

            block:
                lun "How come you're so skilled at unhooking a woman's bra, [name_genie_luna]?" ("open", "base", "base", "down")
            lun "Wait, what am I saying...{w=0.4} Of course the great Albus Dumbledore can do it with ease..." ("angry", "wide", "base", "mid")

    # elif states.lun.tier == 4:

        # lun "My fingers just aren't big enough to get rid of these spurts properly."
        # lun "I hope well be able to find even more ways to get rid of them."

        # lun "I can't believe how slippery it got down there when you had me touch myself."
        # lun "A bunch of slimy buggers is what they are!"

    return
