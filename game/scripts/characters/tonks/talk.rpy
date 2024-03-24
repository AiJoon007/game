label tonks_talk:
    menu:
        "-Ask for help with Quidditch-" (icon="interface/icons/small/quidditch.webp") if states.cho.tier == 2 and states.cho.ev.quidditch.e6_complete and not states.cho.ev.quidditch.e8_complete:
            gen "Got a moment?" ("base", xpos="far_left", ypos="head")
            ton "Sure, just make it quick..." ("open", "base", "base", "mid")
            gen "I have a problem with--" ("base", xpos="far_left", ypos="head")
            ton "[name_genie_tonks], aren't you forgetting about something?" ("open", "closed", "base", "mid")
            ton "You should offer a lady a drink, before burdening her with your problems..." ("base", "base", "base", "mid")
            gen "(Is there {b}any{/b} teacher in this school that has no problems with alcohol...?)" ("base", xpos="far_left", ypos="head")

            if firewhisky_ITEM.owned >= 1:
                gen "I got drinks." ("base", xpos="far_left", ypos="head")
                ton "What are we waiting for then?" ("horny", "base", "base", "mid")

                jump tonks_hangout
            else:
                gen "I'm out of firewhisky." ("base", xpos="far_left", ypos="head")
                ton "That's a shame, I guess our talk will have to wait." ("open", "base", "base", "R")
                ton "" ("base", "base", "base", "R")

                jump tonks_talk

        "-Get naked!-" if states.ton.ev.random_strip.complete and tonks.is_any_worn("top", "bottom", "robe"):
            gen "Get naked, [name_tonks_genie]!" ("base", xpos="far_left", ypos="head")
            ton "Of course, [name_genie_tonks]." ("horny", "base", "base", "mid")
            hide tonks_main
            with d3

            $ tonks.strip("clothes")
            pause.8

            ton "Do you like it, [name_genie_tonks]?" ("horny", "base", "raised", "mid")
            ton "The exposed body of one of your subordinates?" ("open", "base", "raised", "mid")
            gen "I do, [name_tonks_genie]!" ("angry", xpos="far_left", ypos="head")
            gen "You should teach like that!" ("grin", xpos="far_left", ypos="head")
            ton "*Hmm*..." ("base", "base", "base", "R")
            ton "I like the way you think, [name_genie_tonks]!" ("horny", "base", "base", "mid")
            jump tonks_talk

        "-Get dressed-" if states.ton.ev.random_strip.complete and not tonks.is_any_worn("top", "bottom", "robe"):
            gen "Put on some clothes, would you..." ("base", xpos="far_left", ypos="head")
            gen "This is a school, after all." ("base", xpos="far_left", ypos="head")
            ton "Do I have to?" ("annoyed", "narrow", "base", "mid")
            gen "If you consider yourself a proper teacher..." ("base", xpos="far_left", ypos="head")
            hide tonks_main
            with d3

            $ tonks.wear("all")
            pause.8

            ton "..." ("base", "narrow", "base", "R")
            jump tonks_talk

        "-Address me only as-":
            menu:
                "-Sir-":
                    label .sir: # Local label unavailable from global scope
                    $ name_genie_tonks = "Sir"
                    ton "Of course, [name_genie_tonks]." ("base", "base", "base", "mid")

                "-Dumbledore-":
                    label .dumbledore:
                    $ name_genie_tonks = "Dumbledore"
                    ton "Sure thing, [name_genie_tonks]." ("base", "base", "base", "mid")

                "-Professor-":
                    label .professor:
                    $ name_genie_tonks = "Professor"
                    ton "Alright, [name_genie_tonks]." ("base", "base", "base", "mid")

                "-Old man-":
                    label .old_man:
                    $ name_genie_tonks = "Old man"
                    ton "I have to say, for your age you're in really great shape..." ("soft", "base", "base", "down")
                    gen "That's part of the benefits of being immortal...{w=0.4} Your body doesn't age." ("base", xpos="far_left", ypos="head")
                    ton "You're lucky then... I've had men that were a couple of hundred years old, whose bodies were quite fragile..." ("open", "base", "base", "R")
                    gen "All mortals? How did they get that old?" ("base", xpos="far_left", ypos="head")
                    ton "Ever heard of the \"Philosopher's stone\"?" ("base", "narrow", "base", "mid")
                    gen "Is it a tiny, red, stone-looking gem, that lengthens the owner's life?" ("base", xpos="far_left", ypos="head")
                    gen "It's called the \"sorcerer's stone\" in my world, however." ("base", xpos="far_left", ypos="head")
                    ton "Really? Why is that?" ("open", "base", "raised", "mid")
                    gen "I have no clue..." ("base", xpos="far_left", ypos="head")
                    ton "I thought genies were \"all knowing\" beings?" ("open", "base", "angry", "mid")
                    ton "I guess you really are an \"old man\", Genie..." ("base", "base", "base", "mid")
                    gen "..............." ("base", xpos="far_left", ypos="head")

                "-Genie-":
                    label .genie:
                    $ name_genie_tonks = "Genie"
                    ton "Of course." ("base", "base", "base", "mid")
                    gen "Sweet." ("grin", xpos="far_left", ypos="head")
                    ton "Will I get my three wishes too?" ("open", "base", "base", "mid")
                    ton @ hair horny "Or would I have to rub your \"thing\" first?" ("horny", "base", "base", "mid")
                    gen "My lamp?" ("base", xpos="far_left", ypos="head")
                    ton "I was talking about your--" ("base", "base", "base", "R")
                    with hpunch
                    gen "My lamp!!!" ("angry", xpos="far_left", ypos="head")
                    gen "Shit, where even is that thing?" ("angry", xpos="far_left", ypos="head")
                    gen "I must have lost it when I got to this place!" ("angry", xpos="far_left", ypos="head")
                    ton "Do you even need it?" ("open", "base", "raised", "mid")
                    gen "Of course I need it! What sort of question is that, woman?!" ("angry", xpos="far_left", ypos="head")
                    ton "(................)" ("mad", "base", "base", "down")
                    gen "How would you like to suddenly be robbed of your house?!" ("angry", xpos="far_left", ypos="head")
                    ton "(I guess I can jerk him off some other time...)" ("mad", "base", "worried", "R")
                    gen "If you find a golden, shiny looking lamp, return it to me..." ("base", xpos="far_left", ypos="head")
                    ton "Sure, [name_genie_tonks]..." ("upset", "base", "base", "R")

                "-Lord Voldemort-":
                    label .lord_voldemort:
                    $ name_genie_tonks = "Lord Voldemort"
                    ton "Bold of you to say his name out loud... Who even told you about the dark lord?" ("open", "base", "angry", "mid")
                    gen "I've read the stories..." ("base", xpos="far_left", ypos="head")
                    ton "So you know this wizard did some terrible things in his lifetime?" ("open", "base", "angry", "R")
                    gen "Did he corrupt young witches for his own twisted pleasure?" ("base", xpos="far_left", ypos="head")
                    ton "You could say that... He corrupted many witches and wizards alike." ("upset", "base", "base", "mid")
                    gen "....................." ("base", xpos="far_left", ypos="head")
                    gen "So he was \"Bi\" is what you're saying?" ("base", xpos="far_left", ypos="head")
                    ton "What? No." ("open", "wide", "shocked", "stare")
                    ton "I mean, I'm not really sure if someone like him would have even be capable of loving anything..." ("mad", "base", "worried", "R")
                    ton "All that mattered to him was power, and achieving his own immortality..." ("open", "base", "angry", "mid")
                    gen "Both fairly overrated once you have it, if you ask me..." ("base", xpos="far_left", ypos="head")
                    ton "You don't say..." ("base", "base", "raised", "mid")
                    gen "I bet all he secretly wanted was to have a wife, and a kid that loved him..." ("base", xpos="far_left", ypos="head")
                    ton "Voldemort, having a child? Are you serious?" ("open", "wide", "shocked", "stare")
                    gen "Of course not." ("base", xpos="far_left", ypos="head")
                    gen "Once you're immortal, the last thing you need is some annoying brat on your mind..." ("base", xpos="far_left", ypos="head")
                    gen "All we really want to do is waste the majority of our existence with mindless sex!" ("grin", xpos="far_left", ypos="head")
                    ton @ hair horny "Oh my..." ("horny", "base", "base", "mid")
                    gen "And sometimes a bit of kinky role-play..." ("base", xpos="far_left", ypos="head")
                    gen "Are you going to call me \"Lord Voldemort\" now or what?" ("base", xpos="far_left", ypos="head")
                    ton "Fine... I will call you, [name_genie_tonks], if it makes you happy..." ("base", "base", "base", "mid")
                    gen "Yippee!" ("grin", xpos="far_left", ypos="head")

                "-Daddy-":
                    label .daddy:
                    $ name_genie_tonks = "Daddy"
                    ton "Well, you do look about thrice as old as me..." ("base", "base", "raised", "mid")
                    ton "Crazy to think you geezers get to bang all those young, sexy, innocent witches here..." ("open", "base", "base", "R")
                    gen "(Geezers?)" ("base", xpos="far_left", ypos="head")
                    gen "But I thought you didn't mind it?" ("base", xpos="far_left", ypos="head")
                    ton "Oh, I don't mind at all, [name_genie_tonks]!" ("horny", "base", "base", "mid")

                "-Lover-" (style="disabled") if states.ton.level < 60:
                    label .lover_fail:
                    ton "You mean that you \"love how well we work together\", right?" ("base", "narrow", "raised", "mid")
                    gen "*Err*..." ("base", xpos="far_left", ypos="head")
                    gen "Sure." ("base", xpos="far_left", ypos="head")
                    ton "Don't you lie to me young man, an Auror is trained to see right through that stuff." ("open", "narrow", "base", "mid")
                    gen "\"Young man\"? I'm literally over ten thousand years old." ("base", xpos="far_left", ypos="head")
                    ton "Right." ("soft", "base", "base", "R")
                    gen "Also technically not a man..." ("base", xpos="far_left", ypos="head")
                    gen "I just have the bits of a man."
                    gen "Can't reproduce though... So, that's a bit odd." ("base", xpos="far_left", ypos="head")
                    gen "Not that I'm complaining, it made it easier to spend that much time inside the lamp." ("base", xpos="far_left", ypos="head")
                    gen "I feel like I'm oversharing now..." ("base", xpos="far_left", ypos="head")
                    ton "Just a little bit." ("base", "narrow", "base", "R")
                    gen "Well, I suppose that's what lovers do, am I right?" ("base", xpos="far_left", ypos="head")
                    ton "Nice try..." ("base", "narrow", "base", "mid")

                "-Lover-" if states.ton.level >= 60:
                    label .lover:
                    $ name_genie_tonks = "Lover"
                    ton "As you wish, \"Lover boy\"..." ("horny", "narrow", "base", "mid")
                    gen "Just \"Lover\" is fine." ("base", xpos="far_left", ypos="head")
                    ton "Yes my love..." ("base", "narrow", "base", "mid")
                    gen "..." ("base", xpos="far_left", ypos="head")

                "-Master-" (style="disabled") if states.ton.level < 60:
                    label .master_fail:
                    ton "No." ("base", "base", "base", "R")
                    gen "What?- Why not?" ("base", xpos="far_left", ypos="head")
                    ton "Because... that title has to be earned!" ("horny", "base", "angry", "mid")
                    gen "Seriously?" ("base", xpos="far_left", ypos="head")
                    ton "Yes... Show me that you're worth if you want to be my master, and I'll gladly become your bitch!" ("open", "base", "angry", "mid")
                    gen "!!!" ("angry", xpos="far_left", ypos="head")
                    ton "Until then you can forget about it..." ("base", "base", "base", "mid")
                    gen "...................." ("base", xpos="far_left", ypos="head")

                "-Master-" if states.ton.level >= 60:
                    label .master:
                    $ name_genie_tonks = "Master"
                    ton "Yes, [name_genie_tonks]." ("open", "base", "base", "mid")
                    gen "(...)" ("base", xpos="far_left", ypos="head")
                    ton "" ("base", "base", "raised", "mid")
                    call ctc
                    gen "(...?)" ("base", xpos="far_left", ypos="head")
                    gen "You have permission to speak?" ("base", xpos="far_left", ypos="head")
                    ton "Thank you, [name_genie_tonks]." ("base", "base", "base", "down")
                    gen "(I could get used to that.)" ("grin", xpos="far_left", ypos="head")

                "-Custom Input--" (style="disabled") if states.ton.level < 60:
                    gen "(I don't think she's yet ready for that)" ("base", xpos="far_left", ypos="head")

                "-Custom Input-" if states.ton.level >= 60:
                    $ temp_name = renpy.input("(Please enter the name.)", name_genie_tonks, ALLOWED_CHARACTERS, length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name.lower() in ("sir", "dumbledore", "professor", "old man", "genie", "lord voldemort", "daddy", "master"):
                        if temp_name.lower() == "master" and states.ton.level < 60:
                            jump tonks_talk.master_fail
                        $ renpy.jump("tonks_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    else:
                        $ name_genie_tonks = temp_name
                        ton "*Hmm*... [name_genie_tonks]... I like it." ("horny", "base", "raised", "mid")
                    jump tonks_talk

                "-Never mind-":
                    pass

            jump tonks_talk

        "-From now on, I will address you as-":
            menu:
                "-Tonks-":
                    label .tonks: # Local label unavailable from global scope.
                    $ name_tonks_genie = "Tonks"
                    ton "Sure, [name_genie_tonks]." ("base", "base", "base", "mid")

                "-Nymphadora-":
                    $ name_tonks_genie = "Nymphadora"
                    label .nymphadora:
                    ton "*Ugh*--" ("mad", "base", "angry", "R")
                    ton "Really, [name_genie_tonks]?" ("open", "base", "angry", "mid")
                    ton "I hate that name..." ("open", "base", "worried", "R")
                    gen "Well you better get used to hearing it then, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                    ton "................" ("upset", "base", "angry", "R")

                "-Nympho-":
                    label .nympho:
                    $ name_tonks_genie = "Nympho"
                    ton "You think I'm a nympho, [name_genie_tonks]?" ("horny", "base", "raised", "mid")
                    ton "A filthy, sex-craving maniac? Someone who wouldn't shy away from fulfilling every single one of her fantasies?" ("grin", "base", "shocked", "mid")
                    ton "Yes... That does sound like me, doesn't it?" ("base", "base", "base", "R")

                "-Bitch-":
                    label .bitch:
                    $ name_tonks_genie = "Bitch"
                    ton "*Hi-hi*" ("base", "base", "base", "R")
                    ton "If only you knew..." ("horny", "base", "raised", "R")
                    gen "(...)" ("base", xpos="far_left", ypos="head")
                    gen "(What does she mean by that?)" ("angry", xpos="far_left", ypos="head")

                #"-Fuck Puppet-":
                    #label .fuck_puppet_fail:
                    #ton "A what?" ("soft", "wide", "shocked", "mid")
                    #gen "A fuck puppet." ("base", xpos="far_left", ypos="head")
                    #ton "So that's all that I'm good for, is it?" ("open", "narrow", "angry", "mid")
                    #ton "Just another puppet for you to fuck?" ("open", "closed", "angry", "mid")
                    #gen "That's right... And such a fine puppet as well." ("base", xpos="far_left", ypos="head")
                    #ton "*Hmph*... Sorry, but this puppet comes with a brain included." ("annoyed", "narrow", "angry", "R")

                "-Fuck Puppet-":
                    label .fuck_puppet:
                    $ name_tonks_genie = "Fuck Puppet"
                    ton "A fuck puppet?" ("open", "base", "raised", "mid")
                    ton "So you want me to be your personal toy?" ("horny", "base", "base", "mid")
                    gen "Wouldn't anyone." ("base", xpos="far_left", ypos="head")
                    ton "Such a charmer..." ("base", "base", "raised", "R")
                    ton "Of course, [name_genie_tonks]... you can call me that if you like." ("horny", "base", "base", "mid")

                #"-Slut-":
                    #label .slut_fail:
                    #ton "You're not my dad, I can dress however I like!" ("open", "narrow", "angry", "R")
                    #gen "..." ("base", xpos="far_left", ypos="head")
                    #ton "Don't ask..." ("open", "closed", "worried", "mid")
                    #gen "I wasn't going to." ("base", xpos="far_left", ypos="head")

                "-Slut-":
                    $ name_tonks_genie = "Slut"
                    ton "Maybe I am..." ("base", "narrow", "base", "R")
                    ton "Although I'd rather get called \"fashionable\"." ("base", "narrow", "base", "mid")
                    gen "Weird thing to say in bed, but I ain't judging." ("base", xpos="far_left", ypos="head")
                    ton "Oh, you mean like that..." ("grin", "narrow", "raised", "mid")
                    ton "In that case, I'm the \"sluttiest slut\" of them all." ("base", "narrow", "base", "mid")

                #"-Whore-": #Todo put under public checks
                    #label .whore_fail:
                    #ton "A what?!" ("clench", "wide", "shocked", "mid")
                    #gen "Whore." ("base", xpos="far_left", ypos="head")
                    #ton "You can't call me that!" ("open", "wide", "angry", "mid")
                    #gen "Why not!? That's what you're here for, isn't it?" ("base", xpos="far_left", ypos="head")
                    #ton "Yes, but a title like that has to be earned!" ("open", "closed", "angry", "mid")
                    #gen "You-- Hold on, what did you say?" ("base", xpos="far_left", ypos="head")
                    #ton "I've not slept around enough to have the privilege of you calling me that." ("annoyed", "base", "angry", "R")
                    #gen "I feel like this relationship of ours is backwards for some reason..." ("base", xpos="far_left", ypos="head")

                "-Whore-": #Todo put under public checks
                    label .whore:
                    $ name_tonks_genie = "Whore"
                    ton @ hair horny "Hmm... I'm a \"whore\" now, am I?" ("horny", "base", "raised", "mid")
                    gen "That's what I pay you for."
                    ton @ hair horny "You pay me to--" ("soft", "narrow", "base", "mid")
                    ton @ hair horny "Well, I suppose I do spend a lot of my time on the clock... Enticing my pupils..." ("horny", "narrow", "base", "R")
                    ton "But I can assure you it's to encourage them to do better during class." ("base", "narrow", "base", "R")
                    gen "Sure... Doesn't make you less of a whore, though."
                    ton "*Mmm*... Alright, fine, If calling me a whore is the punishment for being a good teacher, then you can call me a whore any day..." ("horny", "narrow", "base", "mid")

                "-Cunt-" (style="disabled") if states.ton.level < 60:
                    label .cunt_fail:
                    ton "[name_genie_tonks], I'm used to getting insulted by my many previous lovers..." ("base", "base", "raised", "mid")
                    ton "Truth be told I bloody love it!" ("open_wide_tongue", "base", "base", "ahegao")
                    ton "But we aren't close enough for that yet, don't you think?" ("open", "base", "worried", "mid")
                    ton "Maybe we should wait with that until we know each other a bit better." ("base", "base", "worried", "R")
                    gen "Of course.{w} And I will respect that." ("base", xpos="far_left", ypos="head")
                    ton "I'm glad.{w} You are a very polite man, [name_genie_tonks]..." ("base", "base", "base", "mid")
                    gen "..........................." ("base", xpos="far_left", ypos="head")

                "-Cunt-" if states.ton.level >= 60:
                    label .cunt:
                    $ name_tonks_genie = "Cunt"
                    ton "*Uuuh*, [name_genie_tonks]..." ("base", "base", "raised", "mid")
                    ton "You better not call me that in front of a student..." ("open", "base", "base", "mid")
                    gen "What if I do?" ("grin", xpos="far_left", ypos="head")
                    ton @ hair horny "Do it, I dare you!" ("horny", "base", "base", "mid")

                "-Slave-"(style="disabled") if states.ton.level < 60:
                    label .slave_fail:
                    ton "To who?" ("soft", "base", "raised", "mid")
                    gen "To whom." ("grin", xpos="far_left", ypos="head")
                    ton "Who?" ("soft", "base", "raised", "mid")
                    gen "To me." ("base", xpos="far_left", ypos="head")
                    ton "*Giggles*" ("grin", "closed", "base", "mid")
                    ton "No, I don't think so, [name_genie_tonks]." ("base", "base", "base", "mid")

                "-Slave-" if states.ton.level >= 60:
                    label .slave:
                    $ name_tonks_genie = "Slave"
                    ton "Does this mean I have to be obedient?" ("soft", "narrow", "raised", "mid")
                    gen "Isn't that the point of an employee?" ("base", xpos="far_left", ypos="head")
                    ton "I suppose, although you pay me for that." ("open", "narrow", "base", "R")
                    gen "In that case, I'll pay you to be my slave!" ("grin", xpos="far_left", ypos="head")
                    ton "I don't think that's how it works..." ("base", "narrow", "base", "R")
                    gen "Oh..."("base", xpos="far_left", ypos="head")
                    ton "Also, if you're doing this as a role-play thing, a slave is usually spoken down on." ("base", "narrow", "base", "mid")
                    gen "Oh, right!" ("base", xpos="far_left", ypos="head")
                    ton "And--" ("open", "base", "base", "mid")
                    gen "Shut up Slave, only speak when you're spoken to!" ("base", xpos="far_left", ypos="head")
                    ton "You are speaking to me..." ("soft", "narrow", "raised", "mid")
                    gen "Oh, so I am." ("base", xpos="far_left", ypos="head")
                    ton "For a genie, I thought you'd be a bit more educated on this topic." ("open", "closed", "base", "mid")
                    gen "Filling my existence with mindless sex helps me forget my troubled past." ("base", xpos="far_left", ypos="head")
                    ton "That's... concerning." ("open", "base", "base", "mid")
                    ton "At least it's better that you're doing it to forget, rather than it being some power fantasy to stick the middle finger to humanity and your creator." ("base", "base", "base", "mid")
                    gen "Yep." ("base", xpos="far_left", ypos="head")
                    gen "Now give me ten push-ups, slave!" ("base", xpos="far_left", ypos="head")

                "-Custom Input--" (style="disabled") if states.ton.level < 60:
                    gen "(I don't think she's yet ready for that)" ("base", xpos="far_left", ypos="head")

                "-Custom Input-" if states.ton.level >= 60:
                    $ temp_name = renpy.input("(Please enter the name.)", name_tonks_genie, ALLOWED_CHARACTERS, length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name.lower() in ("tonks", "nymphadora", "nympho", "fuck puppet", "bitch", "cunt"):
                        if temp_name.lower() == "cunt" and states.ton.level < 60:
                            jump tonks_talk.cunt_fail
                        $ renpy.jump("tonks_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    else:
                        $ name_tonks_genie = temp_name
                        ton "*Hmm*..." ("base", "base", "base", "R")
                        ton "Alright." ("base", "base", "base", "mid")
                        gen "Really? You don't mind?" ("base", xpos="far_left", ypos="head")
                        ton "Not at all, [name_genie_tonks]." ("horny", "base", "raised", "mid")
                        ton "I've been called quite many things by my lovers!" ("base", "base", "base", "R")
                        gen "I'm your lover now?" ("grin", xpos="far_left", ypos="head")
                        ton "Never say never." ("base", "base", "base", "mid")
                "-Never mind-":
                    pass
            jump tonks_talk

        "-Never mind-":
            jump tonks_requests
