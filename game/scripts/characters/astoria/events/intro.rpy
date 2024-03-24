

### Astoria Intro ###

### Event 1 ###
# Tonks tells you about a student that has used the Imperius curse at school.
# You need to ask Snape and Hermione to help find the student.

label astoria_intro_E1:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"

    ton "[name_genie_tonks], may I come in?"
    ton "It's quite urgent..."

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Yes, come in!\"":
            ton "Thank you..."

        "\"Not now!\"":
            ton "I'm sorry [name_genie_tonks], but I'm afraid this can't wait."
            gen "(Then why even ask?)" ("base", xpos="far_left", ypos="head")
            ton "I'm coming in..."

    # Tonks walks in.
    call ton_walk(action="enter", xpos="desk", ypos="base")

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton "Good evening, [name_genie_tonks]." ("base", "base", "base", "mid", xpos="mid", ypos="base")
    gen "[name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
    ton "I'm terribly sorry for bursting in like this!" ("open", "base", "raised", "R")
    gen "What in the world got you so flustered?" ("base", xpos="far_left", ypos="head")
    ton "We might be in big trouble, [name_genie_tonks]!" ("open", "base", "worried", "mid")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
    gen "Miss Tonks... Have you been a bad girl?" ("grin", xpos="far_left", ypos="head")
    ton "I'm not joking, [name_genie_tonks]!" ("soft", "base", "annoyed", "mid")
    ton "Something terrible has happened at school today!" ("open", "closed", "annoyed", "R")
    ton "I believe one of our students has conducted some highly illegal activities against another student!" ("normal", "base", "annoyed", "downR")
    ton "We have to take action!{w=0.6} The last thing we need is for this to reach the Ministry's attention!" ("open", "base", "angry", "mid")
    gen "So? Isn't it your task to cover up that sort of stuff?" ("base", xpos="far_left", ypos="head")
    ton "Yes, but..." ("upset", "base", "worried", "down")
    ton "Please, [name_genie_tonks]! I can't cover this up all on my own!" ("open", "base", "worried", "mid")
    ton "I require your help..." ("upset", "base", "worried", "mid")
    gen "My help, you say?" ("base", xpos="far_left", ypos="head")
    ton "Yes..." ("base", "base", "worried", "down")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"How exactly can I help you?\"":
            pass

        "\"I'm busy right now...\"":
            ton "Busy with what exactly?" ("open", "base", "raised", "mid")
            gen "...................." ("base", xpos="far_left", ypos="head")
            ton "[name_genie_tonks]?" ("mad", "base", "angry", "mid")
            gen "Please give me a minute... I'm still thinking..." ("base", xpos="far_left", ypos="head")
            ton "We don't have time for this!" ("normal", "base", "angry", "mid")
            gen "I have all the time in the world, darling..." ("base", xpos="far_left", ypos="head")
            gen "I'm immortal..." ("base", xpos="far_left", ypos="head")
            ton "Could you please just listen to me?" ("mad", "closed", "angry", "mid")

        "\"What's in it for me?\"":
            ton "Are you seriously asking me that?" ("clench", "shocked", "shocked", "stare")
            ton "If this doesn't get dealt with immediately, they'll have us both locked up in a cell in Azkaban, do you hear me?!" ("mad", "base", "angry", "mid")
            gen "Loud and clear..." ("base", xpos="far_left", ypos="head")
            gen "I'll be locked up in a cell - together with you..." ("base", xpos="far_left", ypos="head")
            gen "I can think of many fates worse than that, if I'm honest." ("grin", xpos="far_left", ypos="head")
            ton "Weren't you so scared of that very thing before?" ("open", "base", "raised", "mid")
            gen "Not when I'm accompanied by someone as lovely as you!" ("grin", xpos="far_left", ypos="head")
            ton "................" ("annoyed", "base", "annoyed", "R")
            ton "You are clearly insane!" ("open", "base", "angry", "mid") # Annoyed
            ton "Fine... Tell me what you want so we can continue..." ("upset", "base", "base", "mid")
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

            $ d_flag_01 = False

            label astoria_intro_E1_choices:

            menu:
                gen "How about you..." ("base", xpos="far_left", ypos="head")
                "\"Pull on my finger...\"" if d_flag_01 == False:
                    $ d_flag_01 = True
                    ton "I'm sorry?" ("open", "base", "raised", "mid")
                    gen "Come on. It's an old trick we Genies like to do!" ("grin", xpos="far_left", ypos="head")
                    gen "It's harmless, I swear..." ("base", xpos="far_left", ypos="head")
                    ton "............." ("upset", "base", "angry", "R")
                    ton "Very well..." ("open", "closed", "base", "mid")
                    pause.2

                    # Tonks walks over.
                    call hide_characters
                    hide screen bld1
                    show screen blkfade
                    with d3

                    # Genie and Tonks stand behind the desk.
                    $ genie_chibi.zorder = 1
                    $ tonks_chibi.zorder = 1
                    call ton_chibi("stand", 280, 470)
                    call gen_chibi("stand", 180, 470)
                    hide screen blkfade
                    with fade
                    pause.8

                    call bld
                    gen "Now pull it." ("grin", xpos="far_left", ypos="head")
                    ton ".................................." ("disgust", "base", "annoyed", "down", xpos="far_right", ypos="head")
                    gen "Try a bit harder..." ("base", xpos="far_left", ypos="head")
                    ton ".............................................." ("normal", "base", "angry", "down")
                    call bld("hide")
                    pause.2
                    with hpunch
                    pause.5

                    call bld
                    gen "Why isn't this working?!" ("angry", xpos="far_left", ypos="head")
                    gen "(Oh, that's right...)" ("base", xpos="far_left", ypos="head")
                    gen "(I forgot we Genies are unable to fart...)" ("base", xpos="far_left", ypos="head")
                    ton "Are we done here?" ("open", "closed", "base", "mid")
                    gen "Want to give it one more try?" ("base", xpos="far_left", ypos="head")
                    ton "I think not..." ("open", "base", "annoyed", "R")
                    ton "I expected a bit more from a Genie..." ("upset", "base", "annoyed", "down")
                    ton "How very disappointing..." ("open", "closed", "base", "mid")
                    gen "Sorry about that..." ("base", xpos="far_left", ypos="head")
                    gen "May I ask you for something else?" ("base", xpos="far_left", ypos="head")
                    ton "Still? Even after disappointing me like this?" ("upset", "base", "annoyed", "mid")
                    gen "Please?" ("base", xpos="far_left", ypos="head")
                    ton "*Ugh*... Fine..." ("upset", "narrow", "annoyed", "R")
                    show screen blkfade
                    hide screen bld1
                    with d3

                    $ genie_chibi.zorder = 2 # Default
                    $ tonks_chibi.zorder = 3 # Default
                    call gen_chibi("sit_behind_desk")
                    call ton_chibi("stand","desk","base")

                    hide screen blkfade
                    ton "" ("upset", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

                    jump astoria_intro_E1_choices

                #"\"Blow me!\"":
                #    ton "Blow you? With my mouth?" ("base", "base", "base", "mid")
                #    gen "Yes, please." ("base", xpos="far_left", ypos="head")
                #    ton "On your dick, I imagine?" ("base", "base", "base", "mid")
                #    gen "Yes, if you would..." ("grin", xpos="far_left", ypos="head")
                #    ton "Very well..." ("base", "base", "base", "mid")
                #    ton "Get it out for me, would you..." ("base", "base", "base", "mid") # Naughty look
                #    gen "!!!" ("grin", xpos="far_left", ypos="head")
                    # Tonks walks over.
                    # Blkfade.
                    # Genie and Tonks stand behind the desk.
                    # Genie has his dick in hand, jerking off.

                #    nar "To your surprise, Tonks \"blows\" a gust of wind over \"your cock\"..."
                #    ton "There, all done." ("base", "base", "base", "mid")
                #    gen ".............." ("base", xpos="far_left", ypos="head")
                #    ton "What? I did what you asked for... I blew your cock..." ("base", "base", "base", "mid")
                #    gen "......................" ("base", xpos="far_left", ypos="head")
                #    ton "Now, could we get back to discussing what I came here for in the first place?" ("base", "base", "base", "mid")
                #    gen "Fine. I know when I'm outwitted..." ("base", xpos="far_left", ypos="head")
                #    ton "I will suck your delicious cock some other time, [name_genie_tonks]... I promise!" ("base", "base", "base", "mid")
                #    ton "But right now, we simply don't have time to fool around, I'm afraid..." ("base", "base", "base", "mid")

                "\"Send Nudes.\"":
                    $ letter_nt_1.send()

                    ton "Nudes, [name_genie_tonks]?" ("annoyed", "base", "raised", "mid")
                    gen "Yes! Send me some nude pictures of yourself!" ("grin", xpos="far_left", ypos="head")
                    gen "A poster, maybe?" ("grin", xpos="far_left", ypos="head")
                    ton "Oh..." ("upset", "base", "base", "down")
                    ton "A poster, you say?..." ("horny", "base", "base", "mid")
                    ton "What are you going to do with it? Put it on your wall and jerk off to it?" ("horny", "base", "angry", "mid")
                    gen "You can count on that!" ("grin", xpos="far_left", ypos="head")
                    ton "Hold on!{w} Are you going to hang it up here? In your office?!" ("open", "wide", "shocked", "stare")
                    gen "Sure... It's not like there are that many other rooms I can go to..." ("base", xpos="far_left", ypos="head")
                    ton @ hair horny "Oh my... I'll have to put a concealment charm on it then..." ("upset", "base", "worried", "R")
                    gen "A what charm?" ("base", xpos="far_left", ypos="head")
                    ton "Only you will be able to see its true form... Everyone else..." ("open", "base", "base", "mid")
                    ton "Well they'll just see some dull landscape or another..." ("normal", "base", "base", "downR")
                    gen "So, I've got this wart on my--" ("base", xpos="far_left", ypos="head")
                    ton "I shall send you an owl with it tomorrow morning, [name_genie_tonks]." ("base", "base", "base", "mid")
                    gen "Sweet!" ("grin", xpos="far_left", ypos="head")
                    ton "Now, here is what I'll require your help with..." ("open", "closed", "base", "mid")

    ton "This girl I've told you about, Susan Bones?" ("soft", "base", "shocked", "mid")
    ton "The one with--" ("base", "base", "base", "R")
    gen "With the giant tits!" ("grin", xpos="far_left", ypos="head")
    ton "... The one with the unfortunate luck of being a constant target of bullying and harassment!" ("mad", "closed", "base", "mid") # Annoyed
    gen "Yes, that too..." ("base", xpos="far_left", ypos="head")
    gen "Well, it's not the first time I've had to cover up a murder..." ("base", xpos="far_left", ypos="head")
    ton "She's not dead!" ("open", "base", "angry", "mid")
    gen "Injured?" ("base", xpos="far_left", ypos="head")
    ton "Thankfully not..." ("upset", "base", "base", "R")
    gen "And most importantly... Her tits haven't been shrunk?" ("base", xpos="far_left", ypos="head")
    ton "Don't be silly..." ("open", "closed", "base", "mid")
    gen "Then how bad could it be?" ("base", xpos="far_left", ypos="head")
    ton "She's been a target of an \"unforgivable curse\"!" ("open", "base", "worried", "mid")
    gen "A curse?..." ("base", xpos="far_left", ypos="head")
    gen "Like...{w=0.5} The c-word?" ("base", xpos="far_left", ypos="head")
    ton "No! A magical curse!{w} Not an insult..." ("mad", "closed", "annoyed", "mid")
    ton "If you are caught having cast any of the unforgivable curses, then you'll be sent straight to Azkaban!" ("open", "shocked", "worried", "mid")
    ton "Where you'll spend the rest of your days, sharing a room with a whole bunch of Dementors!" ("upset", "base", "angry", "mid")
    gen "Dement-{w=0.6}ors?" ("base", xpos="far_left", ypos="head")
    gen "So it's like a nursing home?" ("base", xpos="far_left", ypos="head")
    ton "No, I've told you before!" ("mad", "closed", "angry", "mid")
    ton "Azkaban is a prison! With Dementors roaming all over it..." ("open", "narrow", "annoyed", "mid")
    ton "Believe me, you wouldn't want to be around them, I'll tell you that much..." ("open", "base", "angry", "R")
    gen "(Does she hate old people as well now?)" ("base", xpos="far_left", ypos="head")
    ton "Should the ministry find out about what has happened to... Miss Bones." ("upset", "shocked", "worried", "R")
    gen "*He-he-he*..." ("grin", xpos="far_left", ypos="head")
    ton "Which they most certainly will, as her aunt is head of The ministry's department for \"Magical Law Enforcement\"..." ("open", "closed", "worried", "down")
    gen "So, are we in trouble?" ("base", xpos="far_left", ypos="head")
    ton "Not yet..." ("open", "closed", "worried", "mid")
    ton "Luckily, I was able to erase Susan's memory of the whole ordeal, using the \"obliviate\" charm." ("mad", "base", "worried", "downR")
    gen "You can do that? Neat..." ("base", xpos="far_left", ypos="head")
    ton "But, if this should happen to her again, I doubt there is much I could do to prevent her from telling her aunt right away..." ("open", "base", "worried", "R")

    gen "So what do you suggest we do?" ("base", xpos="far_left", ypos="head")
    ton "Find the student who cursed her, and then talk some sense into her so that she never does it again..." ("open", "closed", "base", "mid")
    gen "Find{w=0.2}.{w=0.2}.{w=0.2}.{w=0.8} her?" ("base", xpos="far_left", ypos="head")
    ton "Yes! Susan said she heard a girl's voice in her head - while she was under the influence of the \"imperius\" curse..." ("open", "base", "angry", "mid")
    gen "In her head?" ("base", xpos="far_left", ypos="head")
    ton "Yes, and the voice instructed her{w=0.2}.{w=0.2}.{w=0.2}.{w=0.8} to lift up her top." ("upset", "base", "worried", "R")
    gen "Now that's my kind of curse!" ("grin", xpos="far_left", ypos="head")
    gen "Why haven't anybody told me about this tit revealing curse before?" ("grin", xpos="far_left", ypos="head")
    ton "That isn't the only--{w=0.4} The imperius curse can make people do so many other {b}unspeakable things{/b}!" ("open", "closed", "angry", "mid")
    ton "I have no doubt that someone as sweet and good-hearted as Susan wouldn't know how to defend herself against it..." ("open", "base", "worried", "mid")
    ton "So... She showed her breasts to a bunch of other students...{w=0.4} Unfortunately..." ("upset", "base", "worried", "R")
    gen "I wish I could have been there to stop it!" ("base", xpos="far_left", ypos="head")
    ton "Of course you do..." ("open", "closed", "base", "mid")
    ton "That's sadly all the information I can share..." ("annoyed", "base", "annoyed", "down")
    ton "Nobody there saw who might have cursed her..." ("open", "base", "worried", "mid")

    gen "So, my role in this would be to interrogate every female in this school... Yes, that sounds like a good plan." ("base", xpos="far_left", ypos="head")
    ton "Please, leave interrogations to me..." ("disgust", "base", "base", "mid")
    gen "Then I'll assemble a search party!" ("base", xpos="far_left", ypos="head")
    gen "I'll ask Snape, I'm sure he wouldn't mind... And how about Miss Granger?" ("base", xpos="far_left", ypos="head")
    ton "*Hmm*... Yes, perhaps Snape could prove himself useful for once..." ("open", "base", "base", "down")
    ton "I don't know about Miss Granger... If you ask her, then you'd have to ensure that she keeps quiet at all costs!" ("normal", "base", "raised", "down")
    ton "The ministry can't know about this!" ("open", "base", "angry", "mid")
    gen "Yes, Yes..." ("base", xpos="far_left", ypos="head")
    ton "I should get going... There are a couple of students I'd like to question." ("open", "base", "worried", "R")
    gen "Good luck." ("base", xpos="far_left", ypos="head")
    ton "Talk to you soon, [name_genie_tonks]." ("normal", "base", "base", "mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    gen "(I should definitely get Snape on this...)" ("base", xpos="far_left", ypos="head")
    gen "(And Granger...)" ("base", xpos="far_left", ypos="head")
    gen "(Or I could jerk off instead!)" ("grin", xpos="far_left", ypos="head")
    gen "(Yes, that seems like a good idea right now!)" ("grin", xpos="far_left", ypos="head")

    $ states.ton.busy = True
    $ states.ast.ev.intro.e1_complete = True

    call music_block
    jump main_room_menu


### Event 2 - Hermione ###
# You ask Hermione to find the student.

label astoria_intro_E2_hermione:
    gen "I require your help with something." ("base", xpos="far_left", ypos="head")
    gen "Miss Tonks came by earlier and informed me about a student making a ruckus." ("base", xpos="far_left", ypos="head")
    gen "I-- *Uhm*...{w} She thought maybe you could be of help finding her?" ("base", xpos="far_left", ypos="head")
    her "Of course, Sir." ("base", "happyCl", "base", "mid")
    gen "Apparently a student got hit by an \"unforgivable curse\" here at the school." ("base", xpos="far_left", ypos="head")
    her "AN unforgivable CURSE!!!" ("scream", "wide", "base", "stare", trans=hpunch)
    her "AT our school?!" ("shock", "wide", "base", "mid")
    her "SOMEONE COULD BE DEAD!" ("scream", "wide", "base", "R")
    her "OR TORTURED!!" ("disgust", "happyCl", "worried", "mid")
    her "OR WORSE!!!" ("angry", "squint", "worried", "mid")
    her "Exp--" ("disgust", "base", "worried", "stare")
    gen "Expelled?" ("base", xpos="far_left", ypos="head")
    her "Exploited!" ("angry", "squint", "worried", "mid")
    gen "really?" ("base", xpos="far_left", ypos="head")
    her "Those are the only things that can happen with an unforgivable curse, [name_genie_hermione]!" ("open", "base", "worried", "mid")
    gen "Of course... I'm just making sure you were aware of them..." ("base", xpos="far_left", ypos="head")
    gen "So, how does it work exactly?" ("base", xpos="far_left", ypos="head")
    her "You're asking me?" ("open", "base", "base", "mid")
    gen "Yes... I need to make sure you've done your studies." ("base", xpos="far_left", ypos="head")
    her "Sir, It's one of the first lessons we ever received in defence against the dark arts." ("open", "closed", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    her "*Sigh*... The curse lowers the target's inhibitions, making them more prone to follow the command, depending on the skill of the user casting it or their own mental resolve not to abide by the command." ("open", "closed", "base", "mid")
    gen "You could've just said it's like a suggestion spell." ("base", xpos="far_left", ypos="head")
    her "Sorry?"
    gen "Never played D&D?" ("base", xpos="far_left", ypos="head")
    her "..."
    gen "(And here I thought she was a nerd...)" ("base", xpos="far_left", ypos="head")
    gen "In any case... One's been cast somewhere in the school." ("base", xpos="far_left", ypos="head")
    gen "And I need your help finding out who did it..." ("base", xpos="far_left", ypos="head")
    her "Why do you need my help?" ("open", "base", "worried", "mid")
    her "Surely you're able to detect them?" ("annoyed", "base", "base", "mid")
    gen "Unfortunately not... I must have been... Asleep... When the thing happened..." ("base", xpos="far_left", ypos="head")
    gen "I missed my chance, so to speak..." ("base", xpos="far_left", ypos="head")
    her "So, how do you expect me to find out who did it?" ("soft", "base", "base", "R")
    gen "I'm certain that it's the work of another student..." ("base", xpos="far_left", ypos="head")
    gen "(or Snape has finally snapped...)" ("base", xpos="far_left", ypos="head")
    gen "so I'll need you to go undercover to find out who cast it." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Really? You're depending on me to find a criminal within our school?" ("soft", "narrow", "base", "down")
    gen "If it's not too much troub--" ("base", xpos="far_left", ypos="head")
    her "I'd be honoured, [name_genie_hermione]!" ("scream", "closed", "base", "mid")
    her "It's no doubt the work of one of those despicable Slytherins..." ("open", "closed", "angry", "mid")
    gen "I'm sure she--" ("base", xpos="far_left", ypos="head")
    her "She? So, it's one of those Slytherin sluts?" ("open", "base", "angry", "mid")
    gen "Well... From what I heard, it was cast by a female--" ("base", xpos="far_left", ypos="head")
    her "I knew it!" ("scream", "closed", "angry", "mid")
    her "Nothing would give me greater pleasure than to see scum like that sent to Azkaban..." ("angry", "narrow", "angry", "R")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Just find her...\"":
            her "Very well, Sir..." ("soft", "base", "base", "R")

        "\"No one's getting sent to Azkaban...\"":
            gen "By the gods, [name_hermione_genie], what's wrong with you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What are you talking about, [name_genie_hermione]?" ("open", "base", "base", "R")
            her "Everyone knows that life in Azkaban is the punishment for casting an unforgivable curse..." ("open", "closed", "base", "mid")
            gen "I've been given special permission to punish them as I see fit." ("base", xpos="far_left", ypos="head")
            her "Oh..." ("annoyed", "base", "base", "mid")
            her "So no Azkaban?" ("soft", "base", "base", "R")
            gen "Not unless they've killed someone..." ("base", xpos="far_left", ypos="head")
            her "Really? So, there's still a chance?" ("base", "narrow", "base", "mid_soft")
            gen "Only if you find a body..." ("base", xpos="far_left", ypos="head")
            her "Yay!" ("smile", "happyCl", "base", "mid")

    her "Consider it done, [name_genie_hermione]!" ("open", "closed", "base", "mid")

    call her_walk(action="leave")

    call bld
    if states.ast.ev.intro.e2_ask_snape:
        gen "I wonder if she'll find her before Snape..." ("base", xpos="far_left", ypos="head")
    else:
        gen "I should probably tell Snape as well..." ("base", xpos="far_left", ypos="head")

    $ states.her.busy = True
    $ states.ast.ev.intro.e2_ask_hermione = True

    call music_block
    jump main_room_menu


### Event 2 - Snape ###
# You ask Snape to find the student.

label astoria_intro_E2_snape:
    gen "Tonks came by earlier and informed me about one of the students causing trouble." ("base", xpos="far_left", ypos="head")
    sna "Really?" ("snape_03") #No xpos change.
    sna "Why are you telling me?" ("snape_04")
    gen "Apparently somebody got hit by something called an \"unforgivable\" curse at the school..." ("base", xpos="far_left", ypos="head")

    play sound "sounds/scratch.ogg"
    sna "" ("snape_11")
    with hpunch
    call ctc
    gen "...{w} Severus?" ("base", xpos="far_left", ypos="head")

    sna "This isn't good..." ("snape_08")
    gen "She worries that the ministry might find out about it if we don't do anything." ("base", xpos="far_left", ypos="head")
    sna "This really isn't good..." ("snape_07")
    sna "If they send an auror here they might find out what we've been doing!" ("snape_10")

    gen "Didn't they already do that?" ("base", xpos="far_left", ypos="head")
    sna "We got lucky with Tonks, but if they were to send another Auror to investigate..." ("snape_03")
    sna "Then they might get wind of all the favour trading that we've been doing as well." ("snape_10")
    sna "Fucking our students isn't something teachers are supposed to do, genie!" ("snape_25")
    sna "We can't risk receiving any more attention on the matter."
    sna "If an auror finds out what's going on here, then we're both going to Azkaban!" ("snape_16")
    gen "All three of us, you mean." ("base", xpos="far_left", ypos="head")
    gen "So, what are we going to do about it then?" ("base", xpos="far_left", ypos="head")
    sna "We'll just have to make sure that no more curses are cast..." ("snape_01")
    gen "How would we manage to do that?" ("base", xpos="far_left", ypos="head")
    gen "There's not some kind of spell history stored in a wand is there?" ("base", xpos="far_left", ypos="head")
    sna "Of course not... If that was the case, I would've snapped mine a long time ago." ("snape_24")
    sna "We have to find out who's been casting them." ("snape_24")
    sna "Normally the real Dumbledore would be able to detect who had cast them, but seeing as how you're here instead..." ("snape_06")
    sna "We'll have to find them the old-fashioned way." ("snape_10")
    gen "So you want me to launch a manhunt?" ("base", xpos="far_left", ypos="head")
    sna "Are you crazy? We can't let anyone know what's happened. All the students will panic, thinking someone's been murdered..." ("snape_16")
    sna "Although it's more likely that it's just imperio or crucio that's been cast." ("snape_24")
    gen "Impervius! That's the one!" ("base", xpos="far_left", ypos="head")
    sna "Figured..." ("snape_01")
    sna "I'll start the search immediately. In the meantime, just stay here and keep yourself busy." ("snape_10")
    gen "You don't want my help?" ("base", xpos="far_left", ypos="head")
    sna "Not really... I'll get this situation under control on my own." ("snape_02")
    if states.ast.ev.intro.e2_ask_hermione:
        gen "And with Miss Granger's help..." ("base", xpos="far_left", ypos="head")
        sna "Have you told her about this?!" ("snape_03")
        gen "Sure... She seemed eager to help." ("base", xpos="far_left", ypos="head")
        sna "Of course she did..." ("snape_06")
        sna "(You bloody fool...)" ("snape_35")
        gen "(Such a drama queen...)" ("base", xpos="far_left", ypos="head")
    else:
        gen "Right..." ("base", xpos="far_left", ypos="head")
        sna "Don't you worry, I'll find that student in no time. You shall see..." ("snape_02")

    call sna_walk(action="leave")

    if states.ast.ev.intro.e2_ask_hermione:
        gen "(I wonder if he'll find her before Miss Granger...)" ("base", xpos="far_left", ypos="head")
    else:
        gen "(I should probably ask Miss Granger as well...)" ("base", xpos="far_left", ypos="head")

    $ states.sna.busy = True
    $ states.ast.ev.intro.e2_ask_snape = True

    call music_block
    jump main_room_menu


### Event 3 ###
# Hermione brings Astoria to you.
# Snape scolds her and Tonks gives her detention.

label astoria_intro_E3:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"
    gen "(...)" ("base", xpos="far_left", ypos="head")

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"What?\"":
            pass
        "\"Not now...\"":
            pass

    with hpunch
    femv "Stop pulling me!"
    her "Shut it already!"
    femv "Why did you drag me here?"
    her "You know very well why, you--"
    femv "Let me go you filthy mudblo--"
    play sound "sounds/kick.ogg"

    gen "Who's there?" ("base", xpos="far_left", ypos="head")
    her "*Shhhhh*- now!"
    gen "..." ("base", xpos="far_left", ypos="head")
    her "It's Hermione Granger, Sir."
    her "Although... I'm not alone."
    gen "Come in." ("base", xpos="far_left", ypos="head")

    call her_walk(action="enter", xpos="500", ypos="base")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    her "Hello sir." ("normal", "happy", "base", "mid", xpos="mid", ypos="base")
    gen "I thought you said you weren't alone?" ("base", xpos="far_left", ypos="head")
    her "I'm not." ("annoyed", "narrow", "base", "R_soft")
    hide hermione_main
    hide screen bld1
    with d3
    pause.2

    call her_chibi("stand", 500, "base", flip=True)
    pause.5

    her "Get in here, Astoria!" ("annoyed", "narrow", "angry", "R", flip=True)
    ast "{size=+2}{b}No!{/b}{/size}"
    her "Do you want to make this worse?" ("scream", "closed", "base", "mid", trans=hpunch)
    ast "No..."
    hide hermione_main
    hide screen bld1
    with d3
    pause.1

    call her_chibi("stand", 500, "base", flip=False)
    pause.2

    play sound "sounds/door.ogg"
    call ast_chibi("stand","door","base")
    with d3
    pause.8

    # Astoria enters.
    call ast_walk("desk", "base")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed

    $ astoria.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")
    $ hermione.set_face(mouth="normal", eyes="closed", eyebrows="base", pupils="mid")

    show CG ast_intro astoria hermione as cg zorder 17:
        zoom 0.5
    with fade

    ast "..." ("annoyed", "base", "worried", "R", xpos="right", ypos="base")

    gen "..."
    gen "And who's this?"
    her "Astoria Greengrass, Sir." ("open", "narrow", "annoyed", "mid", flip=False, xpos="base", ypos="base")
    her "You asked me to bring you the person who cast the unforgivable curse, Sir." ("soft", "narrow", "annoyed", "R")
    her "And here she is." ("grin", "base", "angry", "mid")
    gen "I thought it would be some angsty girl who listens to death metal - or something..."
    gen "Not some innocent looking--"
    ast "I am not!" ("clench", "narrow", "angry", "mid")
    ast "You don't know what you're talking about, you ancient old man!" ("annoyed", "narrow", "angry", "R")
    gen "(Oh, you have no idea...)"

    her "What's going to be her punishment, Sir?" ("soft", "base", "angry", "mid")
    ast "Punishment? I didn't do anything!" ("clench", "base", "worried", "mid")
    her "You know very well what you did!" ("angry", "closed", "angry", "mid")
    her "Sir, I overheard her boasting about it in the library - to a group of Slytherins." ("annoyed", "narrow", "worried", "mid_soft")
    her "By the sounds of it, she used Imperio to control another student!" ("annoyed", "base", "base", "mid")
    ast "I did not!" ("annoyed", "base", "worried", "L")

    her "Shall I go fetch a vial of veritaserum from Professor Snape, sir?" ("grin", "base", "base", "mid")
    ast "V--{w=0.2} Veritaserum?!" ("clench", "base", "worried", "mid")
    ast "That's illegal!" ("clench", "base", "base", "mid")
    her "Not when you've been casting unforgivable curses - you evil little witch!" ("grin", "narrow", "angry", "R")
    ast "Fine!" ("clench", "closed", "angry", "mid")
    ast "I'll tell you what happened, Sir..." ("open", "narrow", "base", "mid")
    ast "But only if this Gryffindor leaves!" ("annoyed", "narrow", "base", "mid")
    her "Not a chance!" ("angry", "closed", "angry", "mid")

    $ d_flag_01 = False

    menu:
        "\"You're dismissed, Miss Granger!\"":
            her "What?!" ("open", "wide", "worried", "shocked")
            pass

        "\"Go and fetch Snape!\"":
            $ d_flag_01 = True
            pass

    hide cg
    with fade
    her "But Sir, I'd really like to know what her punishment is going to be!" ("angry", "base", "base", "mid")

    gen "That's none of your concern." ("base", xpos="far_left", ypos="head")
    her "Yes it is! And I demand to be rewarded!" ("angry", "closed", "angry", "mid")
    her "Given that I was the one who caught her, I think it's only fair!" ("annoyed", "base", "angry", "mid")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")

        "\"Not now, Miss Granger...\"":
            gen "We'll talk about your reward later..." ("base", xpos="far_left", ypos="head")
            her "But!" ("disgust", "narrow", "worried", "down")
            gen "No butts..." ("base", xpos="far_left", ypos="head") # deliberate.
            her "*Hmph*" ("annoyed", "narrow", "angry", "R")
            her "Fine..." ("open", "closed", "angry", "mid")
            $ states.her.mood += 12

        "\"How about some house points?\"":
            her "*Hmm*..." ("annoyed", "narrow", "angry", "R")
            her "How many house points?" ("soft", "base", "angry", "mid")

            menu:
                gen "(...)" ("base", xpos="far_left", ypos="head")
                "\"How about ten?\"":
                    her "Ten?" ("disgust", "base", "worried", "mid")
                    her "I expected more for this, Professor!" ("open", "base", "angry", "mid")
                    gen "Take 'em or leave 'em..." ("base", xpos="far_left", ypos="head")
                    her "..." ("annoyed", "narrow", "angry", "R")
                    her "Very well..." ("open", "closed", "base", "mid")
                    $ states.her.mood += 6
                    $ gryffindor += 10

                "\"You'll get twenty.\"":
                    her "..." ("annoyed", "base", "base", "R")
                    her "I suppose that's fair." ("open", "closed", "base", "mid")
                    $ states.her.mood = 0
                    $ gryffindor += 20

    her "In a few days, everyone at Hogwarts will know what happened to her..." ("grin", "base", "angry", "mid")
    her "When she's sent to Azkaban!" ("soft", "squint", "angry", "mid")
    gen "Nobody's going anywhere, except for you, Miss Granger..." ("base", xpos="far_left", ypos="head")

    if d_flag_01:
        gen "Now go and fetch Snape for me." ("base", xpos="far_left", ypos="head")
    else:
        gen "You may leave..." ("base", xpos="far_left", ypos="head")

    her "..." ("annoyed", "narrow", "angry", "R")
    ast "*cough*... {size=-4}mudblood...{/size}" ("annoyed", "narrow", "angry", "R", xpos="mid", ypos="base", trans=dissolve)
    her "*Tzzzs!*..." ("angry", "closed", "angry", "mid")
    if d_flag_01:
        her "I'll go {i}fetch{/i} professor Snape then..." ("annoyed", "narrow", "angry", "R")
    else:
        her "I'll go back to class then..." ("annoyed", "narrow", "angry", "R")
    her "Good day, Professor." ("open", "base", "angry", "mid")
    stop music fadeout 2.0

    call her_walk(action="leave")
    pause.2

    ast "..." ("annoyed", "base", "base", "L")
    gen "..." ("base", xpos="far_left", ypos="head")

    ast "Now what, sir?" ("annoyed", "base", "worried", "mid")
    if d_flag_01:
        gen "You'll find out when professor Snape gets here." ("base", xpos="far_left", ypos="head")
    else:
        gen "You'll find out once I've summoned professor Snape." ("base", xpos="far_left", ypos="head")
        gen "Give me a second..." ("base", xpos="far_left", ypos="head")
    ast "..." ("annoyed", "narrow", "worried", "down")
    ast "(Better him than any of the other teachers...)" ("clench", "narrow", "base", "down")

    $ snape_chibi.zorder = 4 # In front of Astoria
    call sna_walk(action="enter", xpos="mid", ypos="base")

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    ast "" ("annoyed", "base", "worried", "R")
    sna "You wanted to see me?" ("snape_09", xpos=600, ypos="base")
    ast "..." ("annoyed", "narrow", "worried", "L")
    sna "Astoria?!" ("snape_05")
    sna "Why is one of my students in your office? Don't tell me you..." ("snape_03")
    gen "It's not that sort of visit." ("base", xpos="far_left", ypos="head")
    sna "Really? Then what's she doing here?" ("snape_01")
    gen "She's the one who cast that curse." ("base", xpos="far_left", ypos="head")
    sna "Truthfully? A Slytherin?" ("snape_05")
    sna "I expect better than this from my students, Miss Greengrass..." ("snape_10")

    sna "The very first lesson I give you is...{w=0.4} Don't--" ("snape_08")
    sna "Get--" ("snape_08", trans=hpunch)
    sna "Caught!" ("snape_15", trans=hpunch)
    pause.5

    sna "Do you have anything to say for yourself?" ("snape_10")
    ast "I-I'm sorry, sir... It won't happen again." ("clench", "narrow", "base", "down")
    sna "Who did you cast it on you little idiot?" ("snape_32")
    ast "Susan Bones, Sir..." ("annoyed", "narrow", "base", "down")
    sna "The Hufflepuff cow--" ("snape_44")
    sna "*Ahem*..." ("snape_09")
    gen "..." ("base", xpos="far_left", ypos="head")
    sna "That cowardly Hufflepuff girl?" ("snape_38")
    ast "Yes." ("open", "narrow", "worried", "L")
    ast "I... might have used Imperio to embarrass her a little..." ("smile", "narrow", "worried", "mid")
    sna "Well as long as you only cast it once..." ("snape_09")
    sna "We have to make sure this stays under wraps." ("snape_34")
    sna "Miss Greengrass, you will not mention this incident to any other student or teacher, am I clear?" ("snape_35")
    ast "Yes Sir, I promise..." ("annoyed", "narrow", "worried", "down")
    sna "You should count yourself lucky that the ministry hasn't been notified..." ("snape_31")
    sna "Miss Tonks has been kind enough to wipe the co--" ("snape_01")
    sna "Susan's memory of the event." ("snape_03")
    sna "You owe her big time..." ("snape_25")
    ast "Of course..." ("annoyed", "narrow", "worried", "L")
    sna "I'll leave her punishment to the two of you..." ("snape_04")
    sna "I have someone--" ("snape_09")
    sna "*Uhm*... I've got an appointment to attend to in my office." ("snape_35")
    gen "Naturally..." ("base", xpos="far_left", ypos="head")
    sna "Until next time... Albus." ("snape_09")
    gen "And Albus to you--" ("base", xpos="far_left", ypos="head")
    gen "I mean..." ("angry", xpos="far_left", ypos="head")
    gen "Until next time!" ("grin", xpos="far_left", ypos="head")
    sna "..." ("snape_04")

    # Snape leaves and runs into Tonks.
    stop music fadeout 1
    call sna_walk(660,"base")

    # Equip Tonks default clothing.
    $ ton_outfit_last.save() # Store current outfit.
    $ tonks.equip(ton_outfit_default)

    play sound "sounds/door.ogg"
    call ton_chibi("stand",780,"base")
    with d3
    pause.2

    call ast_chibi("stand","desk","base", flip=True)
    with d3

    ton @ hair neutral "Snape. How good to see you!" ("soft", "shocked", "base", "mid", xpos="far_right", ypos="head")
    sna "Save your compliments for someone else... I'm in a bit of a hurry." ("snape_03", xpos="far_right", ypos="head")
    ton "Still mad at me for taking your post?" ("base", "base", "angry", "mid")
    ton @ hair horny "I'd be willing to compensate you for it, you know..." ("horny", "base", "base", "mid")
    sna "..." ("snape_12")
    gen "*Ahem*..." ("base", xpos="far_left", ypos="head")
    sna "Would you mind?" ("snape_12")
    ton "Sure...{heart}" ("horny", "base", "angry", "mid")
    sna "Stepping aside." ("snape_18")
    ton "Oh, okay..." ("annoyed", "closed", "base", "mid")

    call sna_walk(action="leave")
    pause.2
    $ snape_chibi.zorder = 2 # Reset zorder

    call ton_walk(500,"base")
    call ast_chibi("stand","desk","base", flip=False)
    with d3

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    pause.1
    ast "" ("annoyed", "base", "base", "mid", trans=dissolve)
    ton @ hair neutral "Hello, Professor." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=dissolve)

    ton "Astoria? What are you doing here?" ("upset", "base", "worried", "L")
    ton "You didn't cause any mischief, I hope." ("open", "narrow", "base", "L")
    ast "Of course not." ("annoyed", "base", "worried", "down")
    ton "Wait. Is she the one who cursed Miss Bones?" ("clench", "wide", "shocked", "stare")
    ton "" ("upset", "base", "worried", "mid")
    gen "Yep." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "(Oh shit!)" ("horny", "base", "raised", "L")

    ast "I'm really sorry! I promise I won't ever cast it again!" ("open", "narrow", "base", "R")
    ton "Really? It was you who cast the spell?" ("grin", "base", "raised", "L")
    ast "..." ("annoyed", "narrow", "worried", "down")
    ton "It couldn't possibly have been someone as cute as you!" ("soft", "base", "raised", "down")
    ast "..." ("clench", "narrow", "worried", "down") # Embarrassed, stares down.
    ast "Please don't send me to Azkaban!" ("scream", "closed", "base", "mid")
    ast "" ("annoyed", "narrow", "base", "down")
    ton "Don't worry, It won't come to that..." ("grin", "narrow", "base", "down")
    ton "The ministry isn't going to lock away such a cute little thing like yourself..." ("base", "base", "base", "L")
    ton "{size=+2}Over a little harmless fun.{/size} {heart}" ("horny", "base", "shocked", "L")

    ton "It's just the Imperius curse." ("grin", "base", "raised", "R")
    ton "Most students don't have the guts to cast Crucio on another person..." ("base", "narrow", "base", "down")
    ton "Let alone Avada Kedavra..." ("soft", "closed", "shocked", "mid")

    gen "..." ("base", xpos="far_left", ypos="head")
    ton "So, you had some fun with Susan, I gather?" ("base", "narrow", "base", "L")
    ton "Want to tell me what you made her do?" ("horny", "base", "angry", "L")
    gen "(Doesn't she already know that?)" ("base", xpos="far_left", ypos="head")
    ast "I might have made her show her boobs to some students..." ("annoyed", "narrow", "base", "R")
    ton "*Ha-ha-ha-ha*!" ("silly", "happyCl", "base", "mid", trans=hpunch)
    ast "Only for a second!" ("clench", "base", "base", "mid")
    gen "(What's going on here?)" ("base", xpos="far_left", ypos="head")
    ton "Is that all?" ("open", "base", "raised", "L")
    ton "You probably did Susan some good then..." ("crooked_smile", "base", "raised", "mid")
    ton "She sure needs to loosen up a bit." ("soft", "base", "base", "R")

    ton "She always has been very sensitive about her body for some reason." ("base", "base", "raised", "mid")
    ast "So I'm not going to get in trouble?" ("open", "base", "worried", "mid")
    ton "I didn't say that... You still cast a very serious spell..." ("base", "base", "annoyed", "L")
    ast "" ("annoyed", "base", "base", "mid")
    ton "A couple of hours of detention with me should be an appropriate punishment for casting an unforgivable curse." ("open", "base", "base", "L")
    ton "Wouldn't you agree, Professor?" ("base", "base", "raised", "mid")

    $ d_flag_01 = False

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Seems reasonable to me.\"":
            ast "Really? Only detention?" ("smile", "base", "base", "mid")
            ton "I'm very much looking forward to it." ("base", "happyCl", "base", "mid")
            ast "Wicked!" ("clench", "narrow", "angry", "down")

        "\"Why don't you just reward her at this point...\"":
            $ d_flag_01 = True

            ast "What?" ("smile", "base", "angry", "mid")
            ton "*Hmm*... I agree." ("horny", "base", "raised", "L")
            gen "Miss Tonks, I was being sarcastic..." ("base", xpos="far_left", ypos="head")
            ton "But you're right though, Professor!" ("grin", "base", "shocked", "mid")
            ton "Casting the Imperius curse at her age is no easy task!" ("open", "closed", "base", "mid")
            ton "A girl with that type of...{w=0.3} talent, is a rare thing." ("horny", "base", "raised", "L") # Horny
            ton "I would say, fifty points for Slytherin should be appropriate." ("base", "base", "annoyed", "mid")
            ast "!!!" ("clench", "base", "base", "mid")
            gen "(If Hermione hears about this - she'll {i}Abra Kadabra{/i} my head off!)" ("angry", xpos="far_left", ypos="head")
            gen "(And not the one on my shoulders...)" ("angry", xpos="far_left", ypos="head")
            ton "But you'll still have to visit me for detention." ("open", "base", "annoyed", "L")
            ast "I guess I can do that..." ("smile", "base", "base", "R")
            ton "Wonderful." ("base", "happyCl", "base", "mid")
            $ slytherin += 50

    ton "That should be all for now, Miss Greengrass." ("open", "base", "base", "L")
    ast "..." ("annoyed", "base", "base", "down")
    if game.daytime:
        ton "Have a great day, cutie." ("base", "happyCl", "base", "mid")
        ast "*Uhm*...{w=0.3} Right..." ("open", "base", "base", "mid")
    else:
        ton "Have a good night, cutie." ("base", "happyCl", "base", "mid")
        ast "*Uhm*...{w=0.3} Good night then." ("open", "base", "base", "mid")

    # Astoria leaves.
    stop music fadeout 1
    call hide_characters
    call ast_chibi("stand","desk","base", flip=True)
    hide screen bld1
    with d3
    pause.1

    call ast_walk(action="leave")
    pause.1

    call ton_walk("desk","base")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
    ton "She's {size=+5}so cute!{/size} Isn't she? {heart}" ("base", "base", "raised", "R", xpos="mid", ypos="base")

    if d_flag_01:
        gen "You gave her fifty house points..." ("base", xpos="far_left", ypos="head")
        gen "For what you previously described as a serious crime?" ("angry", xpos="far_left", ypos="head")
        ton "I know! I shouldn't have rewarded her, but..." ("upset", "closed", "worried", "mid")
        ton "Did you see how her face lit up!" ("grin", "narrow", "raised", "mid")
        ton "I thought we were supposed to encourage our students, [name_genie_tonks]." ("upset", "base", "shocked", "down")
        gen "Don't put this on me..." ("base", xpos="far_left", ypos="head")
        ton "Fine, maybe I got a bit too excited..." ("mad", "base", "worried", "mid")

    else:
        gen "A couple of hours of detention..." ("base", xpos="far_left", ypos="head")
        gen "For what you previously described as a serious crime?" ("base", xpos="far_left", ypos="head")
        ton "Did I go too soft on her?" ("upset", "base", "worried", "mid")
        gen "Oh, don't get me wrong. I couldn't care less about this school." ("base", xpos="far_left", ypos="head")
        gen "I'm not even supposed to be here..." ("base", xpos="far_left", ypos="head")
        ton "Fair enough..." ("normal", "base", "raised", "R")

    gen "We should have a chat about this Astoria girl..." ("base", xpos="far_left", ypos="head")
    gen "Discuss the severity of her... \"detention\"." ("base", xpos="far_left", ypos="head")
    ton "Of course, [name_genie_tonks]." ("annoyed", "base", "raised", "downR")
    ton "Let's discuss it over a drink...{heart}" ("grin", "closed", "base", "mid")
    gen "Naturally..." ("base", xpos="far_left", ypos="head")
    gen "Until next time, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")
    ton "Until next time!{heart}" ("base", "happyCl", "base", "mid")
    stop music fadeout 1

    call ton_walk(action="leave")

    call bld
    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "(I feel like I'm actually starting to run this damn school.)" ("base", xpos="far_left", ypos="head")
    gen "(This isn't what I signed up for...)" ("base", xpos="far_left", ypos="head")

    # Reset Tonks.
    $ tonks.equip(ton_outfit_last)

    $ states.her.busy = True
    $ states.sna.busy = True
    $ states.ton.busy = True

    $ states.ast.ev.intro.e3_complete = True

    call music_block
    jump main_room_menu


### Tonks Hangout Event 1 ###
# Tonks wants to teach Astoria the Imperius curse.

label nt_he_astoria_E1:
    ton "So about this girl." ("open", "closed", "base", "mid")
    gen "You're going to have to be more specific." ("base", xpos="far_left", ypos="head")
    ton "Astoria Greengrass." ("open", "wide", "base", "mid")
    gen "Ah yes, the hot-headed one." ("base", xpos="far_left", ypos="head")
    ton "Yes, she's pretty cute isn't she..." ("base", "happyCl", "base", "mid")
    ton @ hair horny "I wouldn't mind giving her a thorough robe inspection - if you know what I'm saying." ("horny", "base", "raised", "mid")
    ton @ hair neutral "This girl...{w=0.5} she's special...{w=0.8} different..." ("open", "base", "base", "R")
    gen "You've got the hots for this girl?" ("base", xpos="far_left", ypos="head")
    ton "She's a Slytherin!" ("mad", "base", "raised", "mid")
    gen "People keep saying that, as if I'd know what the problem is." ("base", xpos="far_left", ypos="head")
    ton "Oh yes... I guess I'm a teacher now - so I should be more impartial..." ("upset", "base", "raised", "down")
    ton "Old habits, I suppose." ("soft", "base", "base", "R")
    ton "But no, it's not that." ("open", "base", "base", "mid")

    ton "This girl, you see... She's cursed... And it's quite a hefty curse at that!" ("open", "narrow", "worried", "R")
    gen "You don't say..." ("base", xpos="far_left", ypos="head")
    #ton "This girl is cursed... and it's quite a problem." ("base", "base", "base", "mid")
    #gen "Don't you mean this cursed girl {i}is{/i} a problem?" ("base", xpos="far_left", ypos="head")
    #ton "No, she's cursed. Quite a hefty curse at that!" ("base", "base", "base", "mid")
    #gen "..." ("base", xpos="far_left", ypos="head")
    ton "Her family - the Greengrass family - is quite infamous in the wizarding world." ("open", "base", "base", "L")
    ton "They're known for being a very high-class family of witches and wizards..." ("open", "base", "raised", "R")
    ton "Some of them are very stuck-up and spoiled, for that reason." ("upset", "base", "base", "R")
    ton "It's quite the norm for most pure-blood families, actually." ("open", "closed", "base", "mid")
    gen "Get to the point..." ("base", xpos="far_left", ypos="head")
    ton "*Sigh*" ("disgust", "base", "base", "down")
    ton "One of the Greengrass' ancestors was put under a blood curse, and I fear that parts of this curse have trickled down through the generations and surfaced in Astoria." ("upset", "base", "worried", "mid")
    ton "Its original purpose was to bring down the family and make them appear weak in the eyes of the wizarding community." ("normal", "base", "base", "R")
    ton "Every now and then one of the family members would become frail and live a short life." ("normal", "closed", "worried", "mid")
    gen "Oh shit..." ("base", xpos="far_left", ypos="head")
    ton "Yeah..." ("upset", "base", "worried", "down")
    gen "Hey, at least it's not the other way round, am I right..." ("base", xpos="far_left", ypos="head")
    gen "Immortality can be quite the curse too, you know..." ("base", xpos="far_left", ypos="head")
    ton "Yes, I can see how much you're hurting inside..." ("normal", "base", "base", "R")
    ton "The opportunity to have sex with some of the most attractive women in all of history must really suck." ("soft", "base", "raised", "mid")
    gen "I'll live with it..." ("base", xpos="far_left", ypos="head")

    ton "Fortunately this curse has faded after many generations, but in turn it appears to have evolved into something else..." ("open", "closed", "base", "mid")
    gen "How would you know?" ("base", xpos="far_left", ypos="head")
    ton "I'm an auror..." ("base", "shocked", "base", "mid")
    gen "Is that your answer for everything now?" ("base", xpos="far_left", ypos="head")
    ton "Just trust me..." ("open", "closed", "base", "mid")
    ton "The nature of it is quite familiar to me." ("open", "base", "base", "R")
    ton "I have strong reasons to believe that this girl is..." ("upset", "closed", "angry", "R")
    ton "She's..." ("upset", "base", "worried", "down")
    gen "She's what?" ("base", xpos="far_left", ypos="head")
    ton "She's asexual!" ("mad", "shocked", "worried", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton "You don't believe me?" ("mad", "narrow", "base", "down")
    gen "Oh no, I believe you." ("base", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Mind explaining to me what asexual's supposed to mean?" ("base", xpos="far_left", ypos="head")
    ton "You don't know?" ("open", "shocked", "raised", "mid")
    ton "Well, that's not too surprising... All things considered." ("normal", "narrow", "base", "L")
    ton "It means she experiences no sexual desires or attractions. To anything!" ("annoyed", "narrow", "shocked", "mid")
    gen "What?!" ("angry", xpos="far_left", ypos="head")
    ton "I know!" ("mad", "base", "worried", "mid")
    gen "By the great desert sands... That's a curse worse than death." ("base", xpos="far_left", ypos="head")
    ton "The curse has seemingly gone from killing off random members of their family to preventing new members from being born." ("upset", "base", "base", "R")
    gen "Magic doesn't make any fucking sense in this universe..." ("base", xpos="far_left", ypos="head")
    ton "Hey, it makes perfect sense!" ("open", "base", "angry", "mid")
    ton "..." ("upset", "base", "worried", "R")
    ton "In any case, I'd like to keep an eye on her - if you don't mind." ("open", "base", "angry", "mid")
    gen "Go right ahea--" ("base", xpos="far_left", ypos="head")
    ton "Maybe even teach her how to cast Imperio properly." ("annoyed", "base", "base", "R")
    gen "..." ("base", xpos="far_left", ypos="head")
    with hpunch
    gen "Hold on a second...{w=0.8} what?!" ("angry", xpos="far_left", ypos="head")
    gen "You want to teach this {b}sadist{/b} how to cast those illegal curses?" ("angry", xpos="far_left", ypos="head")
    gen "That's what caused all this trouble in the first place!" ("base", xpos="far_left", ypos="head")
    ton "Don't worry, I'm just gonna teach her the basics..." ("open", "closed", "base", "mid")
    ton "I won't allow her to go out and curse students at random." ("mad", "closed", "annoyed", "mid")
    ton "But... Maybe this can help ignite that \"sexual urge\" - deep inside of her..." ("mad", "base", "raised", "R")
    ton "She clearly isn't ready to do it with some boy..." ("open", "base", "raised", "mid")
    ton "Or you, for that matter." ("upset", "base", "raised", "R")
    gen "If she's really cursed with \"Asexuality\" - then I don't want to have her anywhere close to me." ("base", xpos="far_left", ypos="head")
    ton "It's not contagious, you numpty!" ("open", "base", "annoyed", "mid")
    ton "Have you not been paying attention? It's a family curse!" ("mad", "base", "angry", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "That being said, I'd rather have her do it with me..." ("base", "base", "raised", "R")
    gen "Are we still talking about the im-pervio thingy?" ("base", xpos="far_left", ypos="head")
    ton "Yes..." ("soft", "narrow", "raised", "downR")
    gen "So your goal is to get rid of this curse she's inherited by somehow awakening her sexuality?" ("base", xpos="far_left", ypos="head")
    ton "It might not be that easy, but I think it would be a good start." ("open", "base", "base", "L")
    ton "I must at least know if my theory is correct..." ("normal", "base", "base", "R")
    gen "I don't see how this im-pervio thing plays into it, but if you say so..." ("base", xpos="far_left", ypos="head")
    ton "I'll speak to Miss Greengrass." ("open", "base", "base", "mid")
    ton "I doubt she'll have many objections..." ("base", "happyCl", "base", "mid")

    nar "You ask Tonks to explain asexuality to you some more..."
    nar "You still can't wrap your mind around the fact that such a horrible thing exists..."

    $ states.ton.ev.hangouts.astoria_e1 = True

    call music_block
    jump end_tonks_hangout_points


### Event 4 ###
# Astoria summon unlock.
# If you pick the wrong choice, Astoria won't return for a week and ignores you.

label astoria_intro_E4:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"
    gen "(...)" ("base", xpos="far_left", ypos="head")

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Who is it?\"":
            ast "Professor, may I come in?"
            gen "It's that accursed, cursed girl!" ("angry", xpos="far_left", ypos="head")
            ast "Sir?"

        "\"Not now...\"":
            ast "But, Professor Tonks told me you wanted to speak with me."
            gen "She did?" ("base", xpos="far_left", ypos="head")
            ast "Yes."

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Come in.\"":
            ast "..."
            pass

        "\"I'm busy.\"":
            ast "*Uhm*..."
            ast "Very well, Sir."
            ast "I shall be back tomorrow..."
            gen "..." ("base", xpos="far_left", ypos="head")

            $ ag_event_pause += 1
            $ states.ast.busy = True

            jump main_room_menu

    call ast_walk("desk","base")
    pause.2

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    ast "Hello, Professor." ("smile", "base", "base", "mid", xpos="mid", ypos="base")
    ast "Professor Tonks told me to talk to you, Sir." ("open", "base", "base", "R")
    gen "....................." ("base", xpos="far_left", ypos="head")
    gen "She did?" ("base", xpos="far_left", ypos="head")
    ast "Yes, Sir..." ("annoyed", "base", "base", "mid")
    gen "(Shit, was I supposed to do something with her?)" ("base", xpos="far_left", ypos="head")
    ast "...................." ("annoyed", "base", "base", "R")
    gen "(Oh that's right. Freeing her from her curse...)" ("base", xpos="far_left", ypos="head")
    ast "Sir, If there's nothing you need of me, then I'd like to leave..." ("open", "narrow", "base", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"What about your detention?\"":
            ast "Oh..." ("clench", "base", "base", "down")
            gen "If I recall correctly, we have yet to discuss your punishment." ("base", xpos="far_left", ypos="head")
            ast "So you didn't forget about that..." ("clench", "base", "worried", "mid")
            pass

        "\"You still need to be punished!\"":
            ast "Punished?!" ("clench", "base", "base", "mid")
            ast "I thought I was only getting detention?" ("open", "base", "worried", "mid")
            gen "Yes, detention." ("base", xpos="far_left", ypos="head")
            pass

        "\"Fine by me...\"": # Fails.
            ast "I'll head back to the dungeons then." ("smile", "base", "base", "R")
            gen "See ya." ("base", xpos="far_left", ypos="head")

            # Astoria leaves.
            call ast_walk(action="leave")

            gen "(Oh, wait! Her punishment!)" ("angry", xpos="far_left", ypos="head")
            gen "(I'd better not mention this to Tonks...)" ("base", xpos="far_left", ypos="head")
            gen "(I'm sure Astoria will come back for her punishment eventually...)" ("base", xpos="far_left", ypos="head")

            $ ag_event_pause += 7 # Returns a week later.

            jump main_room_menu

    gen "It's just a couple of sessions with your teacher." ("base", xpos="far_left", ypos="head")
    gen "I'm sure you'll enjoy it!" ("grin", xpos="far_left", ypos="head")
    ast "If you say so, Sir." ("open", "closed", "base", "mid")
    ast "..." ("annoyed", "narrow", "base", "R")
    ast "Would it be okay if I go there some other time?" ("open", "base", "base", "mid")
    gen "Are you trying to weasel yourself out of your punishment?" ("base", xpos="far_left", ypos="head")
    ast "No?" ("annoyed", "base", "base", "mid")
    ast "It's just that... I really don't have time right now..." ("open", "base", "base", "down")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "I'll allow it. But just this once!" ("base", xpos="far_left", ypos="head")
    ast "Thank you!" ("smile", "closed", "base", "mid")
    gen "You're dismissed..." ("base", xpos="far_left", ypos="head")
    ast "..." ("grin", "base", "angry", "R")

    # Astoria leaves.
    call ast_walk(action="leave")

    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "(I am way too good to my students.)" ("base", xpos="far_left", ypos="head")
    gen "(Who wouldn't want to be in detention with that nympho?)" ("grin", xpos="far_left", ypos="head")
    gen "(That girl should consider herself lucky...)" ("base", xpos="far_left", ypos="head")

    $ states.ast.busy = True

    $ states.ast.unlocked = True
    $ states.ast.wardrobe_unlocked = True # TODO: Move to a proper event once they've been added.
    $ achievements.unlock("unlockast", True)
    call popup("{size=-4}You can now summon Astoria into your office.{/size}", "Character unlocked!", "interface/icons/head/astoria.webp")

    $ states.ast.ev.intro.e4_complete = True

    jump main_room_menu
