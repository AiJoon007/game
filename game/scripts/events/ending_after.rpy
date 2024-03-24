
# After the ending when Dumbledore has returned and the original credits have played
# the player gets a choice to either end the game or return to before the ending happened

# Genie gets stuck in the cosmos not being able to go anywhere
label ending_after:
    $ game.daytime = False

    call blkfade

    $ renpy.scene("screens")

    centered "{size=+7}{color=#cbcbcb}Somewhere outside of time and space...{/color}{/size}\n\n{#LINT_IGNORE}"
    play music "music/epic-unease-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed # noloop
    pause 3
    g2 "Where... where am I...?" with d5
    g2 "Am I dead...? Is this the end...?"
    g2 "Genies aren't supposed to die, are they?"
    g12 "No wait...{w=0.4} This is different...{w=0.4} What is this feeling?"
    g12 "I feel..."
    show screen white
    pause .1
    hide screen white
    g14 "Everything!" with hpunch
    g14 "The...{w=0.4} The cosmic power is running through me!"
    g14 "I can see it...{w=0.4} The universe...{w=0.4} No...{w=0.4} Multiple universes... all around me."
    g14 "But...{w=0.4} Why?"
    g14 "Why am I not back yet!?"
    show screen white
    pause .1
    hide screen white
    play sound "sounds/thunder_2.ogg"
    play background "sounds/pulse.ogg"
    g15 "*ARGH*!" with hpunch
    g15 "My form is being pulled in multiple directions!"
    g15 "If I don't get out of here I'll be torn apart!"
    stop background fadeout 4
    show screen white
    pause .1
    hide screen white
    g14 "Wait...{w=0.8} I know..." with d3
    g14 "This...{w=0.4} It must be my magic!"
    g14 "I need to focus where I want to be... Or I'll be stuck...{w=0.4} Stuck here forever!"
    g14 "Stupid... life choices!"
    play background "sounds/pulse.ogg"
    g14 "Focus..."
    g14 "I just left a bunch of sluts at that school!"
    g14 "But... I need to get home!"

    # Choose to end the game or continue playing
    menu:
        g14 "What should I do?"
        "-Go home, to Agrabah!\n{size=-4}(exit to main menu){/size}-":
            g14 "Yes, that is probably for the best..."
            show screen white
            pause .1
            hide screen white
            play sound "sounds/thunder_2.ogg"
            g15 "Agrabah... here I come! You better prepare yourself..." with hpunch

            stop background fadeout 4
            stop music fadeout 10
            call big_bang

            $ renpy.full_restart()

        "-Cause a time paradox at Hogwarts-":
            g14 "On the other hand..."
            g14 "Who doesn't love..."
            show screen white
            pause .1
            hide screen white
            play sound "sounds/thunder_2.ogg"
            g15 "Who doesn't love...{fast} a good old time paradox!" with hpunch
            g15 "It better be worth it...{w=0.4} Here I go!"

            stop background fadeout 4
            stop music fadeout 10
            call big_bang

            # Genie stands in the forest before he's about to leave
            show her_ball outskirts g1 m1 as cg
            play background "sounds/night.ogg" fadein 1
            pause.5
            call hide_blkfade

            gen "Goodbye, world of bizarre magic..." ("base", xpos="far_left", ypos="head")
            gen "Goodbye, my whor--" ("base", xpos="far_left", ypos="head")
            gen "Wait..." ("base", xpos="far_left", ypos="head")

            # Record scratch, music stops
            show her_ball outskirts g1 -m1 as cg
            stop background fadeout 1.5
            play sound "sounds/scratch.ogg"
            with hpunch

            gen "What the fuck am I doing..." ("angry", xpos="far_left", ypos="head")
            gen "Why leave now when I'm the king of a castle filled with women ready to serve!?" ("angry", xpos="far_left", ypos="head")

            # Heading back to the castle
            play background "sounds/night.ogg" fadein 1
            call blkfade
            hide cg

            $ renpy.scene("screens")

            play sound "sounds/steps_grass.ogg"
            pause .5

            nar "You hastily make your way back to the castle, wondering what kind of impulse made you want to leave in the first place..."
            stop background fadeout 3

            if "public" in states.her.ev.yule_ball.variant:
                play music "music/court-of-the-queen-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
                nar "Arriving at the great hall, you glance through the doors and spot Hermione who's currently enjoying the attention she's receiving from some of the other students."
                nar "You decide it's probably best to head back to your office... But before you get the chance to slip into the shadows, Hermione has already begun making her way in your direction."
                nar "As she enters the hallway, you notice some Slytherin students looking in your direction, smirks spreading across their faces."

                $ hermione.equip(her_outfit_ball)
                her @ cheeks blush "Back so soon?" ("base", "happy", "base", "L", ypos="head", flip=False)
                gen "I... *Err*...{w=0.4} had a change of heart." ("base", xpos="far_left", ypos="head")
                her "I see... Yes, it is quite cold outside tonight, isn't it?" ("base", "base", "base", "mid")
                gen "Yes...{w=0.5} that's it." ("base", xpos="far_left", ypos="head")

                nar "Standing there in silence, looking at Hermione, you can't help but struggle with what to say."
                nar "Hermione looks at you expectantly and breaks the silence by extending one of her arms to you."

                her @ cheeks blush "Care for a dance?" ("open", "squint", "base", "mid")
                gen "I...{w=0.5} of course!" ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("base", "base", "base", "mid")
                nar "With your arms wrapped around Hermione's waist, the two of you begin moving along with the music."
                nar "As some time passes, it's very clear that the Slytherin students are looking at you both through the doorway."
                gen "Miss Granger..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Yes?" ("base", "narrow", "base", "stare_soft")
                play sound "sounds/slap_03.ogg"
                her @ cheeks blush "..." ("soft", "happyCl", "base", "up")
                her @ cheeks blush "Hey! At least warn me!" ("clench", "narrow", "annoyed", "L")
                nar "Swiftly taking your hand away from Hermione's butt, you give a quick smirk towards your audience."
                her @ cheeks blush "I didn't say stop..." ("soft", "narrow", "base", "L")
                gen "Of course..." ("grin", xpos="far_left", ypos="head")
                nar "Without a moments hesitation you lift her dress up, holding it against her back and leaving her panties exposed."
                her @ cheeks blush "Sir..." ("crooked_smile", "base", "base", "down") #could change the sirs here to the name that the player has set for Hermione to call you
                nar "Now firmly gripping her butt with your other hand, you begin to massage her cheeks whilst moving along with the music."
                her @ cheeks blush "..." ("grin", "narrow", "worried", "up") #Look of pleasure
                nar "Your hand finds its way back down, pulling Hermione's panties down with it."
                her @ cheeks blush "Sir...{w=0.4} what are you doing?" ("open", "happyCl", "base", "stare")
                gen "You seem a little bit tense... Just giving you a hand..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "But... What if someone notices..." ("annoyed", "base", "base", "R")
                nar "Ignoring her pleas you begin rubbing your fingers between her thighs, not bothering to be discreet."
                her @ cheeks blush "*Ah*...{w} Sir..." ("open", "happyCl", "base", "mid")
                nar "As you move your hand higher up her thighs, Hermione's breathing quickens and a wetness begins to spread across the side of your hand, her legs shaking slightly as she tries to keep it together."
                her @ cheeks blush "Sir...{w=0.4} I..." ("open", "happyCl", "base", "down")
                nar "With the music soon coming to a close, you shift your hand and begin stroking against her vagina with even more vigour than before."
                her @ cheeks blush "Sir...{w=0.3} *Ah*...{w=0.5} they'll...{w=0.2} they'll hear me..." ("mad", "happyCl", "base", "L")
                gen "You better \"come\" quietly then..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Sir... this isn't the time for..." ("open", "happyCl", "base", "mid")
                nar "As the music reaches its peak, Hermione moves one of her hands off your back and puts it against her mouth to quickly try and stifle herself."
                her "*Mmmmf*..."
                with hpunch
                with kissiris
                stop music fadeout 6 #It's a bit sudden and quiet but not sure what to do instead
                nar "Hermione shudders in your arms and then quickly lets go as the music comes to an end."
                her @ cheeks blush "*Ah*...{w=0.8}*Ah*...{w=0.8}*Ah*..." ("soft", "happyCl", "base", "mid")
                nar "With a quick glance towards the doorway, you notice some Slytherin students have blocked it with their backs towards you."
                gen "You look tired girl, you'd better pull yourself together..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Yes...{w=0.3} *Ah*...{w=0.6} I just need to...{w=0.3} catch my breath..." ("open", "squint", "worried", "L")
                gen "Perhaps sooner rather than later, the music has stopped..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh...{w=0.3} *Ah*...{w=0.3} I didn't even notice..." ("open", "happy", "worried", "mid")
                nar "Hermione moves to stand up but stumbles as she tries to compose herself..."
                nar "As she gets on her feet, she looks up and notices the backs of the Slytherins in the doorway. She spins around to look at you, a red colour quickly spreading across her cheeks."
                her @ cheeks blush "I...{w=0.3} I think I'd better head off to bed then..." ("mad", "squint", "base", "stare_soft") #Worried #Sheepish looking
                gen "Sounds like a good idea..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Okay then..." ("soft", "squint", "worried", "R") # smiles
                her @ cheeks blush "Good night..." ("base", "squint", "worried", "mid")
                gen "Good night, Miss Granger." ("base", xpos="far_left", ypos="head")


                # Back in the office
                call room("main_room")
                call gen_chibi("hide")
                call hide_blkfade
                pause 1.0
                play sound "sounds/door.ogg"
                call gen_chibi("stand","door","base",flip=False)
                with d3
                pause 0.3

                gen "Good night princess..." ("base", xpos="far_left", ypos="head")

                call blkfade

                # Next day
                $ game.daytime = True
                call music_block

                centered "{size=+7}{color=#cbcbcb}The next morning...{/color}{/size}"
                call hide_blkfade

                # Snape enters and walks up to desk
                call sna_walk(action="enter", xpos="desk")
                gen "What did I tell you about knocking!" ("angry", xpos="far_left", ypos="head")
                sna "Who rule..." ("snape_03", ypos="head")
                sna "You motherfucker..." ("snape_01")
                sna "I knew it!" ("snape_02")
                sna "I knew you couldn't make yourself leave yet." ("snape_02")
                gen "Hey, it's not my fault this place has so many--" ("grin", xpos="far_left", ypos="head")
                gen "I have urges, okay?" ("angry", xpos="far_left", ypos="head")
                sna "How very uncharacteristic of you..." ("snape_01")
                sna "But good news nonetheless..." ("snape_02")
                sna "So I take it that you have... unfinished business to complete before you depart?" ("snape_37")
                gen "A headmaster can't just up and leave before the school year is over, can he?" ("base", xpos="far_left", ypos="head")
                gen "Also, I'm getting quite fond of the place... Not that I want to pick out curtains or anything." ("base", xpos="far_left", ypos="head")
                sna "..." ("snape_45")
                sna "Very well... Our little scheme continues." ("snape_02")
                sna "Although at the moment I've got a class to attend to." ("snape_01")
                call sna_walk("door")
                gen "Yes... I also have very important business to get on with..." ("base", xpos="far_left", ypos="head")
                sna "I'm sure you do..." ("snape_01")
                call sna_walk(action="leave")

                jump main_room
            else:
                play music "music/court-of-the-queen-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
                nar "Arriving at the great hall, you decide to take a quick glance through the doorway before heading back to your office."
                nar "Hermione is currently looking out one of the windows and is not aware of your presence."
                nar "You glance over at the high table and lock eyes with Snape, who quickly stands up and then slides towards you."
                sna "Good evening sir...{w=0.5} I...{w=0.8} I didn't expect you so soon." ("snape_29", ypos="head")
                gen "Hello again Severus." ("base", xpos="far_left", ypos="head")
                gen "I have returned..." ("base", xpos="far_left", ypos="head")
                sna "*Ahem*...{w=0.4} I see..." ("snape_06")
                sna "Well...{w=0.5} Here it goes..." ("snape_04")
                sna "Who...{w=0.5} Who rules?" ("snape_09")
                gen "..." ("base", xpos="far_left", ypos="head")
                sna "............." ("snape_25")
                sna "..." ("snape_26")
                gen "Robin Williams." ("grin", xpos="far_left", ypos="head")
                sna "You motherfucker!" ("snape_20") #Epic handshake meme (jk)
                gen "..." ("grin", xpos="far_left", ypos="head")
                sna "..." ("snape_12")
                sna "About the thing I said earlier." ("snape_12")
                gen "Yes?" ("base", xpos="far_left", ypos="head")
                sna "The whole friend thing..." ("snape_14")
                gen "Ah... Yes..." ("base", xpos="far_left", ypos="head")
                gen "I mean, I was leaving and all that--" ("base", xpos="far_left", ypos="head")
                sna "No...{w=0.4} Even that being the case... I did mean it...{w=0.4} good ones are hard to come by." ("snape_24")
                gen "Well... even if you didn't mean it, I bet you ain't never had a friend like me." ("grin", xpos="far_left", ypos="head")
                sna "Ain't that true...{w=0.3}" ("snape_45")
                sna "So...{w=0.4} You're staying then?" ("snape_46")
                gen "Can't just leave in the middle of the school year, can I? What kind of headmaster would do that?" ("grin", xpos="far_left", ypos="head")
                sna "Is that so..." ("snape_47")
                gen "There are still plenty of girls that haven't seen me at my best!" ("grin", xpos="far_left", ypos="head")
                sna "There it is..." ("snape_02")
                sna "Well then...{w=0.4} Business as usual tomorrow?" ("snape_05")
                gen "Business as usual..." ("base", xpos="far_left", ypos="head")
                sna "{size=-4}Fuck yes!{/size}" ("snape_47")
                gen "What did you say?" ("base", xpos="far_left", ypos="head")
                sna "Nothing..." ("snape_38")
                gen "Okay then..." ("base", xpos="far_left", ypos="head")
                gen "In that case, I'll head back to my office." ("base", xpos="far_left", ypos="head")

                $ hermione.equip(her_outfit_ball)
                nar "As Snape slides back towards the teacher's table, Hermione notices your presence and quickly starts walking towards you."
                nar "Before you can even attempt to slip into the shadows again, she's already come through the doorway with one of her arms held out in front of her."
                her @ cheeks blush "Care for a dance?" ("base", "happy", "base", "L", ypos="head", flip=False) # smiles
                gen "I...{w=0.4} Oh, what the hell... Why not." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("base", "narrow", "base", "down") # smiles
                nar "With your arms wrapped around Hermione's waist, the two of you begin moving along with the music."
                nar "After some time passes, you can't help but look down at her butt sticking out below your hands."
                gen "Miss Granger..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Yes?" ("open", "base", "base", "L")
                nar "You move your hands down to Hermione butt, and she smiles and tightens her grip around you."
                nar "Gently resting your hands against her cheeks you return to slowly moving along with the music."
                her @ cheeks blush "Sir..." ("base", "base", "base", "mid")
                gen "Yes, Miss Granger?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Could..." ("normal", "closed", "base", "mid")
                her @ cheeks blush "Why can't this moment go on forever?" ("soft", "base", "worried", "mid")
                gen "We both know that everything has to come to an end..." ("base", xpos="far_left", ypos="head")
                gen "But hopefully I've been able to teach you how to cherish every moment." ("base", xpos="far_left", ypos="head")
                nar "Hermione tightens her arms even more as you continue the dance in silence."
                nar "After a while, her grip lessens slightly as she shifts her head to look up at you."
                her @ cheeks blush "I..." ("open", "squint", "base", "mid")
                her @ cheeks blush "I just wanted to say that...{w=0.5} I'm glad I have you." ("open", "happyCl", "worried", "mid")
                gen "Where's this suddenly coming from, Miss Granger?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I don't know... It's just..." ("upset", "happy", "base", "L")
                her @ cheeks blush "I've had this bad feeling in my stomach all day." ("soft", "closed", "base", "stare")
                her @ cheeks blush "It's stayed there until now...{w} But now it's finally feeling as if the pain has started to go away..." ("upset", "happy", "base", "R")
                nar "Not knowing how to respond, you stand there in silence for a moment until Hermione pulls you towards her and you both begin moving along with the music once more."
                nar "After what only feels like seconds, the music comes to a close and Hermione takes a step back to look up at you."
                gen "You look tired girl... You'd better head off to bed...{w=0.4} There's always tomorrow." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh, yes... I suppose so..." ("soft", "base", "base", "mid")
                her @ cheeks blush "Good night then..." ("base", "happy", "base", "R")
                gen "Good night." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh... wait,{w=0.3} Before I go..." ("open", "happyCl", "base", "mid")
                gen "Yes?" ("base", xpos="far_left", ypos="head")
                play sound "sounds/kiss.ogg"
                with kissiris
                #Heart animation on screen?
                her @ cheeks blush "..." ("base", "narrow", "worried", "mid")
                gen "What was that for?" ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "Nothing, I just felt like you earned it." ("base", "base", "base", "R")
                her @ cheeks blush "See you tomorrow..." ("base", "base", "worried", "mid")
                gen "Good night, Miss Granger." ("base", xpos="far_left", ypos="head")

                stop music fadeout 1
                call blkfade
                pause 3.0
                # Back in the office
                call room("main_room")
                call gen_chibi("hide")
                call hide_blkfade
                pause 1.0
                play sound "sounds/door.ogg"
                call gen_chibi("stand","door","base",flip=False)
                with d3
                pause 0.3

                gen "Good night princess..." ("base", xpos="far_left", ypos="head")

                call blkfade

                jump day_start

label big_bang:
    show screen big_bang
    with Fade(0.7, 0.5, 0.7, color='#fff')
    play background "sounds/rumble.ogg" fadein 2
    pause 3
    show screen big_bang(True)
    play sound "sounds/bang.ogg"
    pause 1.5
    #with Move((0, 25), (0, -25), 0.2, bounce=True, repeat=True, delay=1.0)
    pause 12
    stop background fadeout 2
    hide screen big_bang
    with d5
    return

screen big_bang(bang=False):
    zorder 10

    add Solid("#000")

    if bang:
        add "images/misc/bang.webp":
            at transform:
                zoom 0.0
                anchor (0.5, 0.5)
                pos (540, 300)
                on show:
                    easeout 15.0 zoom 3
    else:
        add "glow_effect" zoom 0.2 anchor (0.5, 0.5) align (0.5, 0.5)
