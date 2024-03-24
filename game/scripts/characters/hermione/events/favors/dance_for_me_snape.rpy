

### Tier 3 ###

# Invite Snape

label hg_pf_strip_T3_snape: # Fails
    hide hermione_main
    with d3

    gen "[name_hermione_genie]... Before you start, I have one more favour to ask of you." ("base", xpos="far_left", ypos="head")

    her "Of course, [name_genie_hermione]." ("open", "closed", "base", "mid", xpos="base", ypos="base")
    gen "Do you think you could go and fetch professor Snape for me?" ("base", xpos="far_left", ypos="head")
    her "... Professor Snape?" ("annoyed", "squint", "base", "mid")
    her "May I ask why, [name_genie_hermione]?" ("annoyed", "squint", "base", "mid")
    gen "Oh, I just think you could use a bigger audience for your striptease performance." ("base", xpos="far_left", ypos="head")
    her "My striptease performance...?!!" ("shock", "wide", "base", "stare")
    her "Are you completely out of your mind, [name_genie_hermione]?" ("angry", "base", "angry", "mid")
    her "Wasn't it enough that I've had to embarrass myself in front my teacher once before?" ("open", "base", "angry", "mid")
    her "And now you expect me to do it again... But willingly?!" ("scream", "closed", "angry", "mid")
    gen "I wouldn't put it that way, I just figured--" ("base", xpos="far_left", ypos="head")
    her "I'm leaving!" ("angry", "base", "angry", "mid")

    call her_walk(action="leave")

    $ states.her.mood += 15

    # Event resets. (No progress)
    $ _event.cancel()

    jump end_hermione_event


### Tier 4 ###

# Invite Snape

label hg_pf_strip_T4_snape:

    $ _wearing_clothes = False #Check if she has to put clothing back on at the end

    $ _flogging_known = False
    $ _potter_known = False
    $ _weasley_known = False
    $ _butt_known = False

    if not states.her.ev.dance_for_me.snape_invited:
        $ states.her.ev.dance_for_me.snape_invited = True

        hide hermione_main
        with d3

        gen "[name_hermione_genie], before you start..." ("base", xpos="far_left", ypos="head")

        her "Yes, [name_genie_hermione]?" ("open", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        gen "I think it'd be a good idea if you went and fetched professor Snape." ("base", xpos="far_left", ypos="head")
        her "... Professor Snape?" ("annoyed", "squint", "base", "mid")
        if hermione.is_any_worn("top", "bottom", "panties", "bra"): #Other items may not fit the category of "clothes"
            $ _wearing_clothes = True
            gen "Yes, I figured that you might want to include him in the audience for your striptease performance." ("base", xpos="far_left", ypos="head")
            her "I'd want to include--{w=0.2} During my striptease performance...?!!" ("shock", "wide", "base", "stare")
        else:
            gen "Yes, I figured that you might want to include him in the audience for your performance." ("base", xpos="far_left", ypos="head")
            her "I'd want him to--{w=0.2} During my performance...?!!" ("shock", "wide", "base", "stare")
        her @ cheeks blush "With all due respect, [name_genie_hermione]..." ("angry", "base", "angry", "mid")
        her "{size=-5}(Which I currently have little left for you...){/size}" ("normal", "squint", "angry", "mid")
        her "I refuse to degrade myself for professor Snape's amusement!" ("scream", "closed", "angry", "mid")
        gen "No, no, you've got it all wrong, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "*Hmm*...?" ("soft", "squint", "base", "mid")
        gen "I figured it was implied, but I wanted to give you an opportunity to find out just how dirty professor Snape can get with his students." ("base", xpos="far_left", ypos="head")
        her "!!!" ("open", "base", "base", "stare")
        gen "If you had a better idea of the types of favours he's currently selling..." ("base", xpos="far_left", ypos="head")
        her "Then I'd be able to stay ahead of Slytherin in points, no problem..." ("open", "squint", "base", "stare")
        gen "Precisely..." ("base", xpos="far_left", ypos="head")
        her "I--{w=0.4} I should've known..." ("soft", "squint", "worried", "mid")
        her "I apologise for doubting your intentions, [name_genie_hermione]..." ("soft", "base", "worried", "mid")
        gen "No worries [name_hermione_genie], I should've made it more clear." ("base", xpos="far_left", ypos="head")
        gen "Now, will you go find professor Snape, and bring him here?" ("base", xpos="far_left", ypos="head")
        if hermione.is_any_worn("top", "bottom", "panties", "bra"): #Other items may not fit the category of "clothes"
            her "But--{w=0.2} *Ehm*...{w=0.4} Undressing in front of Snape..." ("annoyed", "base", "worried", "mid")
        else:
            her "But--{w=0.2} *Ehm*...{w=0.4} Performing in front of Snape..." ("annoyed", "base", "worried", "mid")
        her "I'm not sure if--" ("angry", "base", "worried", "mid")
        gen "Yes, it's not an easy task... I am aware of that, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "But if anyone is strong-willed--" ("base", xpos="far_left", ypos="head")
        gen "(And slutty...)" ("base", xpos="far_left", ypos="head")
        gen "--Enough to do it, it'd be you...{w=0.4} Unless you know some other Gryffindor student who'd be up for the task?" ("base", xpos="far_left", ypos="head")
        her "That's true... I am the only one who could do it..." ("open", "narrow", "base", "down")
        gen "In that case, if you truly want Gryffindor to have a chance at winning the cup, then I'm afraid you'll have to muster up the courage to--" ("base", xpos="far_left", ypos="head")
        her "Yes, I must do it!" ("scream", "closed", "angry", "mid")
        her "I {b}have{/b} to do it, for Gryffindor!" ("scream", "closed", "angry", "mid")
        gen "There's that Gryffindor resolve that I love!" ("grin", xpos="far_left", ypos="head")
        gen "Now then [name_hermione_genie], if you're ready... Put on a big smile, fetch professor Snape, and make your house proud!" ("grin", xpos="far_left", ypos="head")
        her "Right away [name_genie_hermione]!" ("smile", "base", "angry", "mid")

    else:
        hide hermione_main
        with d3

        gen "Hold on, [name_hermione_genie]... Before you start." ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]?" ("open", "closed", "base", "mid", xpos="base", ypos="base", trans=d3)
        gen "Why don't you go and fetch professor Snape?" ("base", xpos="far_left", ypos="head")
        her "... Professor Snape?" ("annoyed", "squint", "base", "mid")
        if hermione.is_any_worn("top", "bottom", "panties", "bra"): #Other items may not fit the category of "clothes"
            $ _wearing_clothes = True
            gen "Yes, I figured it may be a good time for you to perform another striptease for us both." ("base", xpos="far_left", ypos="head")
        else:
            gen "Yes, I figured it may be a good time for you to dance for us both again." ("base", xpos="far_left", ypos="head")
        her "Again, [name_genie_hermione]?" ("annoyed", "squint", "base", "mid")
        gen "Yes, [name_hermione_genie]... Don't you think it would help to know where your competition is currently at?" ("base", xpos="far_left", ypos="head")
        her "But... Don't you think I've learned enough, last time I did this?" ("annoyed", "base", "worried", "R")
        gen "I wouldn't have suggested it, if that's what I thought." ("base", xpos="far_left", ypos="head")
        her "Very well, [name_genie_hermione]..." ("annoyed", "narrow", "worried", "R")

    call her_walk(action="leave")

    show screen blkfade
    with d5

    stop music fadeout 1.0
    pause 2
    nar "Hermione returns with Snape a few moments later."

    play sound "sounds/door.ogg"
    call her_chibi("stand","desk","base")
    call sna_chibi("stand","mid","base")
    hide screen blkfade
    with d5
    pause.5

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    sna "Genie--{w=0.2} I mean Albus...{w=0.4} You wanted to see me?" ("snape_01", xpos="base", ypos="base")
    gen "Severus! Yes, I wanted to ask if you were in the mood for a little striptease." ("base", xpos="far_left", ypos="head")
    sna "Oh...?" ("snape_05")
    sna "Miss Granger here will be performing, I presume?"
    her ".............." ("angry", "happyCl", "worried", "mid", emote="sweat", xpos="mid", ypos="base")
    gen "Yes, our little minx is more than happy to take off her clothes for our entertainment." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "............" ("annoyed", "happyCl", "worried", "mid", emote="sweat")
    gen "Aren't you, Miss Granger?" ("base", xpos="far_left", ypos="head")
    pause.5

    her "" ("angry", "happy", "worried", "R")
    pause 1

    her "" ("angry", "happy", "worried", "mid")
    pause 1.5

    her "Yes, sir." ("angry", "narrow", "worried", "mid", emote="sweat")
    gen "Well then, better get started." ("base", xpos="far_left", ypos="head")
    hide hermione_main
    with d3
    pause.2
    sna "" ("snape_13")
    pause.8

    $ hermione.strip("robe", "accessory")
    hide snape_main
    show screen blkfade
    with d5

    play sound "sounds/08_hop_on_desk.ogg" #Sound of the desk squeaking.
    pause 3
    call her_chibi("dance","on_desk","on_desk")
    call sna_chibi("stand","desk_close","desk_close")

    her "............." ("open", "closed", "base", "mid", ypos="head", flip=False)
    sna "......................"
    gen ".........................."

    hide screen blkfade
    with d5
    pause.8

    gen "So... Severus... How's life?" ("base", xpos="far_left", ypos="head")
    sna "Well, you know... Same old, same old..." ("snape_09")
    sna "The students are causing me grief, as usual..." ("snape_06")
    sna "In fact, Miss Granger here, has managed to cause me more stress than any other student..." ("snape_03")
    pause.2
    her "..............................." ("base", "narrow", "base", "R", xpos="mid", ypos="base")
    gen "Oh, I am sure she is very sorry about that..." ("base", xpos="far_left", ypos="head")
    her "{size=-4}(Not even a little bit!){/size}" ("base", "narrow", "annoyed", "R")
    gen "And I'm sure she'll make up for it today... Won't you, Miss Granger?" ("base", xpos="far_left", ypos="head")
    pause.2

    her "*Ehm*... Yes sir." ("grin", "narrow", "base", "mid")
    pause.2

    nar "Hermione starts to sway her hips seductively."

    if hermione.is_worn("top"):
        nar "She then reaches for her top, and tosses it on the floor..."
        $ hermione.strip("top")
        play sound "sounds/cloth_sound3.ogg"
        pause.5
    call ctc

    #TODO should this section have a repeat variant?
    her @ cheeks blush "..................." ("soft", "narrow", "base", "down")
    sna "*Hmm*... You are being suspiciously quiet, Miss Granger." ("snape_05")
    her @ cheeks blush "{size=-4}(Oh no! Is he onto us?){/size}" ("angry", "squint", "base", "R")
    her @ cheeks blush "I'm just doing what is expected from a student..." ("open", "squint", "worried", "R", emote="sweat")
    sna "Aren't you going to lecture me on the \"corruption that is taking over Hogwarts\" like you've done every other day during classes?" ("snape_03")
    gen "Severus..." ("base", xpos="far_left", ypos="head")
    sna "No, Albus... I want to hear what {i}little miss perfect{/i} has to say." ("snape_03")
    her "..." ("annoyed", "narrow", "base", "down")
    sna "Well?" ("snape_03")
    her "Oh, of course I won't lecture you, professor Snape... After all, trading sexual favours for house points is common practice at Hogwarts." ("open", "squint", "worried", "L", emote="sweat")
    sna "Oh! It's \"Professor Snape\" now, is it?" ("snape_03")
    sna "What happened to \"Snape'o'doodle\" and \"Professor Snivellus\"??!" ("snape_10")
    gen "{size=-5}({i}Snape'o'doodle{/i}...{w=0.4} *Heh*--{w=0.2} That's funny.){/size}" ("grin", xpos="far_left", ypos="head")
    her "..." ("annoyed", "narrow", "annoyed", "down", emote="sweat")
    sna "Yes, I am well aware of what you've been calling me behind my back, you wretched girl!" ("snape_08")
    her "Well, maybe it's warranted... Have you considered--" ("open", "narrow", "angry", "down", emote="angry")
    sna "{size=+2}What did you just say?!{/size}" ("snape_10")
    sna "How dare you to speak to your superiors this way?" ("snape_10")
    sna "Who do you think you are? You filthy mudbl--" ("snape_15")
    her "Headmaster, one of your staff members is verbally abusing me!" ("scream", "closed", "angry", "mid")
    sna "Verbally abusing--{w=0.2} You have some nerve, girl!" ("snape_08")
    sna "Albus, are you truly going to allow such insolent behaviour from a student?" ("snape_10")
    her "Professor, please don't listen to him! He's just trying to manipulate you." ("disgust", "narrow", "angry", "mid")
    sna "Know your place girl, or your so-called abuse will be anything but verbal." ("snape_10")

    menu:
        "\"Miss Granger, show some respect!\"":
            $ states.her.mood += 9
            her "What?" ("angry", "base", "worried", "stare")
            her "But, sir!" ("mad", "base", "worried", "mid")
            gen "And calm yourself." ("base", xpos="far_left", ypos="head")
            her "*Tsk*!" ("upset", "narrow", "base", "mid_soft")
            gen "Remember what we discussed... Focus on that task..." ("base", xpos="far_left", ypos="head")
            her "Fine..." ("disgust", "narrow", "base", "R")
            if hermione.is_worn("bottom"):
                gen "And take off your bottoms already, would you?" ("base", xpos="far_left", ypos="head")
                her "......." ("annoyed", "narrow", "angry", "R")
            sna "..........." ("snape_13")

        "\"Severus, you started this.\"": #Flogging
            $ _flogging_known = True

            sna "What? Me?!" ("snape_10")
            her "Thank you sir." ("grin", "closed", "base", "mid")
            sna "Albus, you are spoiling the girl! She must be taught a lesson!" ("snape_08")
            gen "Severus..." ("base", xpos="far_left", ypos="head")
            gen "Did you hit your head?!" ("angry", xpos="far_left", ypos="head")
            sna "I beg your pardon?" ("snape_03")
            if hermione.is_any_worn("clothes"):
                gen "The girl is already stripping for you!" ("angry", xpos="far_left", ypos="head")
            else:
                gen "The girl is already putting on a show for you!" ("angry", xpos="far_left", ypos="head")
            gen "What else could you possibly ask for?" ("angry", xpos="far_left", ypos="head")
            sna "*Tsk*... Perhaps a flogging--" ("snape_16")
            gen "Severus!" ("angry", xpos="far_left", ypos="head")
            sna "Alright, alright, I see your point..." ("snape_17")
            gen "Miss Granger, are you alright?" ("base", xpos="far_left", ypos="head")
            gen "Shall we end it for today?" ("base", xpos="far_left", ypos="head")
            her "It's okay sir... I agreed to do this after all." ("open", "happy", "base", "mid")
            if hermione.is_worn("bottom"):
                gen "Alright then, in that case you may take off your bottoms!" ("base", xpos="far_left", ypos="head")
                her "Yes sir..." ("soft", "base", "base", "mid")

        "\"Both of you, calm yourselves.\"":
            gen "You, tall-dark-and-handsome, calm down a bit, would you?" ("base", xpos="far_left", ypos="head")
            sna "I beg your pardon?" ("snape_03")
            her "Yes! You tell him--" ("open", "narrow", "angry", "R")
            gen "That goes for you as well, you perverted little minx!" ("base", xpos="far_left", ypos="head")
            if hermione.is_worn("bottom"):
                gen "And take your bottoms off already." ("base", xpos="far_left", ypos="head")
            else:
                gen "And keep doing what you're here for!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am not perverted..." ("angry", "narrow", "worried", "mid")
            if hermione.is_worn("bottom"):
                gen "Your bottoms, Miss Granger!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "......" ("annoyed", "narrow", "worried", "down")
            sna "............." ("snape_13")

        "-Unleash your rage {size=-2}(Hardcore){/size}-" if game.difficulty >= 3: #Hardcore difficulty dialogue.
            $ states.her.mood += 18
            gen "Both of you..." ("base", xpos="far_left", ypos="head")
            stop music
            with hpunch
            gen "Shut the fuck up!!!" ("angry", xpos="far_left", ypos="head")
            gen "You!... You, good for nothing, dungeon-dwelling, crooked-nosed-wannabe-wizard!" ("angry", xpos="far_left", ypos="head")
            with hpunch
            sna "(...)" ("snape_11")
            her "(... Yikes!)" ("angry", "wink", "base", "mid")
            sna "(What did he just say to me?!)" ("snape_08")
            gen "Shut your stupid mouth, or I will send you flying out that bloody window!" ("angry", xpos="far_left", ypos="head")
            if hermione.is_worn("bottom"):
                gen "That bitch is already stripping for you, so what more do you want?!" ("angry", xpos="far_left", ypos="head")
                her "That B--{w=0.2} Bitch?!" ("shock", "wide", "base", "stare")
                gen "And you... Stripper-whore!" ("angry", xpos="far_left", ypos="head")
                gen "Do what you are paid to do, and start stripping already!!!" ("angry", xpos="far_left", ypos="head")
            else:
                gen "That bitch is already butt-naked, so what more do you want?!" ("angry", xpos="far_left", ypos="head")
                her "That B--{w=0.2} Bitch?!" ("shock", "wide", "base", "stare")
                gen "And you... Stripper-whore!" ("angry", xpos="far_left", ypos="head")
                gen "Do what you are paid to do!" ("angry", xpos="far_left", ypos="head")
            her "......" ("angry", "closed", "angry", "mid", emote="angry")
            sna "............." ("snape_05")
            her "..." ("mad", "squint", "angry", "mid")

            play music "music/Dark Fog.ogg" fadein 1 if_changed

    pause.5

    if hermione.is_worn("bottom"):
        nar "Hermione swiftly takes off her bottoms, showing off her shapely ass."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bottom")
        pause .5
        call ctc

        sna "*Hmm*..."
        her @ cheeks blush "........................" ("disgust", "narrow", "worried", "R")
        gen "Yes, much better!" ("base", xpos="far_left", ypos="head")

    if hermione.is_worn("bra") and hermione.is_worn("panties"):
        nar "Hermione keeps on dancing, now wearing nothing but her underwear."
    elif hermione.is_worn("bra"):
        nar "Hermione keeps on dancing, now wearing nothing but her bra."
    elif hermione.is_worn("panties"):
        nar "Hermione keeps on dancing, now wearing nothing but her panties."
    else:
        nar "Hermione keeps on dancing, as if the previous interaction never occurred."

    gen "Now then... If we're all feeling calm, collected... And focused." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("annoyed", "narrow", "base", "down")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Severus, let's talk about that Potter boy.\"": #Potter
            $ _potter_known = True
            her "(.....?)" ("soft", "base", "base", "mid")
            sna "What about him?" ("snape_09")
            gen "Is he still causing you grief?" ("base", xpos="far_left", ypos="head")
            sna "Oh..." ("snape_04")
            sna "Not really, no..." ("snape_01")
            sna "To be honest, I never really had a problem with the boy himself..." ("snape_06")
            sna "Although I did plan to make his life here miserable because of his father..." ("snape_03")
            sna "But lately, I have way more interesting projects to occupy myself with..." ("snape_02")
            her "..................." ("disgust", "squint", "base", "R")

        "\"Severus, anything you'd like to get off your chest?\"": #Weasley
            $ _weasley_known = True

            sna "Is this really the best time to ask such questions?" ("snape_05")
            gen "I don't see why not..." ("base", xpos="far_left", ypos="head")
            gen "Now tell me... Anyone been causing you trouble lately?" ("base", xpos="far_left", ypos="head")
            sna "*Hmph*... Well, I suppose there's the Weasley twins..." ("snape_09")
            gen "Really? Who doesn't love twins?" ("base", xpos="far_left", ypos="head")
            sna "If they were female, perhaps..." ("snape_23")
            her @ cheeks blush "....." ("disgust", "narrow", "base", "down")
            gen "So, what kind of trouble have they been causing?" ("base", xpos="far_left", ypos="head")
            sna "It doesn't matter... They'll get what is coming to them, eventually..." ("snape_09")
            gen "A revenge plot? Cool! What do you have in mind?" ("base", xpos="far_left", ypos="head")
            her "!!!" ("angry", "squint", "base", "mid")
            sna "*Hmm*... It's not exactly something I'm willing to discuss with the \"present company\"." ("snape_06")
            her "*Tsk*!" ("angry", "narrow", "angry", "down")
            sna "All I can say, is that it involves a girl that they're very close to..." ("snape_13")
            her "{size=-5}(Ginny...?){/size}" ("angry", "squint", "worried", "stare")
            gen "I see... So, it's a revenge-fuck type of situation?" ("base", xpos="far_left", ypos="head")
            sna "!!?" ("snape_08")
            sna "Albus, please... Not in front of the girl!" ("snape_17")
            gen "Alright, alright..." ("base", xpos="far_left", ypos="head")

        "\"Severus, tell me what grade you'd give Miss Granger's butt.\"": #Butt
            $ _butt_known = True

            sna "What grade?" ("snape_05")
            her @ cheeks blush "............" ("disgust", "squint", "worried", "stare")
            gen "Yes! How do you normally grade her papers?" ("base", xpos="far_left", ypos="head")
            sna "*Hmm*..." ("snape_13")
            sna "\"Outstanding\"..." ("snape_13")
            her @ cheeks blush "You perverted--" ("angry", "happyCl", "angry", "mid")
            sna "That's the grade I'm usually forced to put on her papers..." ("snape_13")
            sna "That said... How shall I grade something like this..." ("snape_13")
            pause.1
            nar "Professor Snape gives Hermione's buttocks an appraising look..."
            sna "I'd say..." ("snape_13")
            her @ cheeks blush "............?!" ("angry", "narrow", "annoyed", "down")
            sna "\"Dreadful\"..." ("snape_09")
            her "(What?!)" ("shock", "wide", "base", "stare")
            sna "Look at that pitiful thing. Tiny and skinny... That's a boy's butt." ("snape_09")
            her "It is not a boy's--" ("angry", "squint", "annoyed", "R", emote="angry")
            sna "Truly?" ("snape_09")
            her "Of course not!" ("disgust", "narrow", "annoyed", "R")
            sna "Then I suppose there must be some other magic at hand to have caused this... Deformation." ("snape_09")
            sna "Miss Granger..." ("snape_09")
            sna "Remind me... What potion contains two shrivel figs, four daisy roots, five hairy caterpillars, four leeches, and a rat spleen?" ("snape_09")
            her "*Ehm*... A shrinking solution? But what does--" ("disgust", "narrow", "base", "R")
            sna "That's right..." ("snape_23")
            sna "Perhaps you accidentally sat in one..." ("snape_23")
            her "*Hmph*" ("angry", "narrow", "annoyed", "down")

    gen "Miss Granger, I'm not seeing much happening..." ("base", xpos="far_left", ypos="head")
    her "Right..." ("open", "base", "worried", "mid")

    if hermione.is_worn("bra"):
        gen "Why don't you take off your bra?" ("base", xpos="far_left", ypos="head")
        her "............." ("open", "narrow", "worried", "down")
        nar "Hermione undoes her bra and then lets it fall to the floor."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bra")
        pause .5
        call ctc
    else:
        nar "Hermione cups her breasts playfully, squeezing them in the process."

    gen "Alright! Finally getting to the good stuff!" ("base", xpos="far_left", ypos="head")
    sna "*Hmm*..." ("snape_13")
    her "........" ("annoyed", "closed", "base", "mid")

    $ _watch = False #Played watch variant.
    $ _masturbate = False #Jacked off at any point.
    $ _masturbate_finished = False #Jacked off until completion.

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Start jerking off-":
            jump hg_pf_strip_T4_snape_masturbate
        "-Just keep on watching-":
            jump hg_pf_strip_T4_snape_watch
label hg_pf_strip_T4_snape_masturbate:
    $ _masturbate = True
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed

    call hide_characters
    show screen blkfade
    with d5
    pause.2

    her "Sir?!" ("open", "wide", "base", "stare")
    gen "It's alright, Miss Granger..."
    sna "Oh, we're doing this now, are we?"
    sna "Well then... Don't mind if I do."

    play sound "sounds/cloth_sound3.ogg"
    pause .8

    her "!!!" ("open", "wide", "base", "stare")

    call gen_chibi("jerk_off","behind_desk","base")
    call her_chibi("dance_pause","on_desk","on_desk")
    call sna_chibi("jerk_off","desk_close", "desk_close")
    hide screen blkfade
    with d5
    call ctc
    if states.her.tier < 5: # Hermione is not okay with it.
        her "Guys--{w=0.2} *Ehm*... I mean, sirs! *Ehm*...{w=0.4} Professors!" ("angry", "wide", "base", "stare")
        gen "Don't you mind us, Miss Granger... Just keep doing your thing." ("base", xpos="far_left", ypos="base")
        her "But..." ("angry", "wide", "base", "stare")
        her @ cheeks blush "No! I refuse to dance, when those things are pointed at me!" ("angry", "happyCl", "worried", "mid")
        her @ cheeks blush "You need to put them away, or the dance is over!" ("angry", "happyCl", "annoyed", "mid")
        gen "You aren't in any position to give us orders, Miss Granger." ("base", xpos="far_left", ypos="base")
        her @ cheeks blush "That was not an order, sir... It was an ultimatum." ("disgust", "squint", "angry", "mid", emote="angry")

        menu:
            "\"Alright Severus, let's be civil...\"": # Jumps to watch variant.
                hide hermione_main
                with d3
                pause.2
                sna "I see Miss Granger has managed to remain exceptionally stubborn in every situation..." ("snape_03")
                call hide_characters
                with d5

                call gen_chibi("sit_behind_desk")
                call sna_chibi("stand","desk","base")
                with fade
                pause.3

                jump hg_pf_strip_T4_snape_watch
            "\"*Psst*, Hermione! Remember why you're doing this!\"": # Hermione tries to push on, but fails.
                $ states.her.mood += 15

                her "{size=-5}What are you-- Oh... Right...{/size}" ("open", "wide", "base", "stare")
                her @ cheeks blush "...{w}...{w}{nw}" ("angry", "happyCl", "worried", "mid")
                her @ cheeks blush "......{fast} No, I can't! This is just not worth it!" ("disgust", "happyCl", "worried", "stare")

                call hide_characters
                show screen blkfade
                with d5

                call gen_chibi("sit_behind_desk")
                call her_chibi("stand","desk","base")
                call sna_chibi("stand","mid","base")

                nar "Hermione jumps off the desk."

                hide screen blkfade
                with d5

                sna "Well, this was awfully anticlimactic..." ("snape_03")
                gen "You don't say..." ("angry", xpos="far_left", ypos="head")
                sna "Well, since the show is over, I suppose I may as well find some fun elsewhere... I will talk to you later, Albus." ("snape_03")
                gen "Severus..." ("base", xpos="far_left", ypos="head")
                sna "Miss Granger..." ("snape_04")
                her "Professor..." ("disgust", "narrow", "worried", "R")

                call sna_walk(action="leave")

                her "...................." ("annoyed", "narrow", "base", "dead", xpos="mid", ypos="base")

                her "I'd like my points now..." ("open", "narrow", "base", "dead")
                gen "Have you not forgotten something?" ("base", xpos="far_left", ypos="head")
                her "...?" ("annoyed", "narrow", "base", "mid_soft")
                gen "The reason why you did this in the first place, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her "..." ("soft", "narrow", "base", "mid")
                gen "The whole point was so that you could see just how far Professor Snape would take things." ("base", xpos="far_left", ypos="head")
                her "Oh... Right..." ("disgust", "narrow", "worried", "mid")

                jump hg_pf_strip_T4_snape_results

    $ _masturbate_finished = True

    her @ cheeks blush "{size=-5}Focus on the task...{/size}" ("angry", "closed", "worried", "stare")
    sna "What was that?" ("snape_05")
    her @ cheeks blush "Oh, don't mind me, sir... I'm just being silly..." ("clench", "closed", "worried", "mid", emote="sweat")
    sna "*Hmm*...?" ("snape_05")
    her @ cheeks blush "Go ahead, please continue touching yourself in front of me..." ("disgust", "closed", "worried", "mid", emote="sweat")
    her @ cheeks blush "I do not mind it at all..." ("soft", "closed", "worried", "mid", emote="sweat")
    sna "Right..." ("snape_01")

    call hide_characters
    play sound "sounds/MaleClearThroat.ogg"
    gen "*clears throat*"

    her @ cheeks blush "*Ahem*...{w=0.2} Please...{w=0.2} Allow me to--{w=0.2} assist you..." ("open", "squint", "worried", "stare", emote="sweat")

    call her_chibi("dance","on_desk","on_desk")

    nar "You keep jerking off, while Hermione awkwardly dances in front of you both."
    her @ cheeks blush "(Please... Just finish already...)" ("open", "narrow", "worried", "stare", emote="sweat")
    nar "Hermione squeezes her breasts, and shakes her hips in an attempted seductive manner."

    gen "That's it, Miss Granger... Very good." ("base", xpos="far_left", ypos="base")
    sna "*Ahem*! Acceptable performance..." ("snape_12")
    her @ cheeks blush "...." ("soft", "closed", "worried", "mid")
    gen "*Heh*..." ("base", xpos="far_left", ypos="base")
    gen "So... How would you grade her tits?" ("base", xpos="far_left", ypos="base")
    her @ cheeks blush "......" ("annoyed", "closed", "base", "mid")
    sna "*Hmm*......" ("snape_20")
    her @ cheeks blush "........" ("annoyed", "closed", "base", "mid")
    sna "I'd say they \"Exceed expectations\"..." ("snape_12")
    her @ cheeks blush "!!!" ("open", "squint", "base", "stare")
    gen "Really? I'm surprised you'd grade them so high." ("base", xpos="far_left", ypos="base")
    sna "As an honourable man, I do give credit where it's due..." ("snape_12")
    her @ cheeks blush "(*Ugh*... I can't stand him... Honourable, my ass...)" ("angry", "narrow", "base", "stare")
    her "(Better finish this up, quickly...)" ("annoyed", "closed", "base", "mid", cheeks="blush")
    pause.1

    if hermione.is_worn("panties"):
        nar "Hermione bends over and slides her panties down."
        nar "Her movements lack grace..."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("clothes")
        pause.5
        call ctc

        nar "But a pretty pussy is always a welcome sight nonetheless..."
        nar "You show your appreciation by stroking your cock even faster..."
    else:
        $ hermione.strip("clothes")

    sna "Yes..." ("snape_20")
    sna "Now shake that ass for me, you harlot!"
    her "......." ("annoyed", "closed", "annoyed", "mid", cheeks="none")
    pause .5

    nar "All of a sudden, Hermione breaks into a series of rather complex pirouettes."
    sna "Yes, such grace..." ("snape_19")
    sna "That lithe, flexible body!" ("snape_20")
    her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}" ("soft", "closed", "annoyed", "mid")

    nar "Hermione seems very focused on her dancing routine."

    sna "Yes, and now another pirouette!" ("snape_19")
    sna "Magnificent!"
    sna "I would applaud you, but one of my hands is very busy at the moment." ("snape_13")
    gen "{size=-4}(Was that an attempt at a joke?){/size}" ("base", xpos="far_left", ypos="base")
    gen "{size=-4}(Aroused Snape is weird...){/size}" ("base", xpos="far_left", ypos="base")
    show screen blkfade
    with d5

    nar "She then performs another set of movements, and pirouettes..."
    nar "Once finished, she gives a little curtsy bow to an imaginary audience..."
    nar "And then exhaustedly slumps down onto the desk."

    call her_chibi("sit_naked","on_desk","on_desk")

    call hide_characters
    hide screen blkfade
    with d5
    call ctc
    her "Whew... This was--" ("base", "closed", "worried", "mid")
    with hpunch

    gen "*ARGH*! YOU FUCKING WHORE!" ("angry", xpos="far_left", ypos="base")

    call her_chibi("sit_naked_shocked","on_desk","on_desk")

    call cum_block
    call gen_chibi("cum","behind_desk","base")
    pause.2

    $ hermione.set_cum(face="light")
    pause 0.7
    $ hermione.set_cum(breasts="light")
    pause 1
    $ hermione.set_cum(hair="light")

    her "??!!!" ("shock", "wide", "base", "stare")
    her "" ("angry", "happyCl", "worried", "mid")
    call ctc

    sna "Good job, harlot!" ("snape_18")
    sna "Here is your reward!" ("snape_21")

    call cum_block
    call sna_chibi("cum","desk_close","desk_close")
    pause.2

    $ hermione.set_cum(face="heavy")
    pause 0.7
    $ hermione.set_cum(breasts="heavy", body="heavy")
    pause 1
    $ hermione.set_cum(crotch="light")

    her "!!!!!!!!!!!" ("shock", "wide", "base", "stare")
    call ctc

    sna "..." ("snape_22")
    gen "Look at that, she's completely covered!" ("grin", xpos="far_left", ypos="base")
    her "..............................." ("soft", "narrow", "worried", "up")

    sna "*Ha-ha-ha*! This is magnificent!" ("snape_21")
    gen "I know, right!?" ("grin", xpos="far_left", ypos="base")

    call gen_chibi("cum_done","behind_desk","base")
    call sna_chibi("cum_done","desk_close","desk_close")

    sna "Yes... We should do this more often." ("snape_22")
    her @ cheeks blush "................." ("soft", "narrow", "worried", "down")

    sna "*Ahem*... I mean, I deem this performance acceptable..." ("snape_20")
    her @ cheeks blush "*Ugh*... Thank you......... Professor." ("soft", "narrow", "base", "R")
    sna "No Miss Granger, you don't understand..." ("snape_20")
    her @ cheeks blush "...........?" ("soft", "narrow", "base", "R")
    sna "That's how I'd grade it...." ("snape_22")
    sna "\"Acceptable\"..." ("snape_10")
    stop music

    her @ cheeks blush "{size=+5}Wait, what?!!!{/size}" ("angry", "squint", "base", "stare")
    sna "Indeed... Quite a few things could use some improvement..." ("snape_09")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    her "I cannot believe this!" ("clench", "base", "angry", "mid", emote="angry")
    pause.5

    call hide_characters
    show screen blkfade
    with d5

    nar "Hermione jumps off your desk furiously."
    pause 2
    hide hermione_main

    call sna_chibi("hold_dick","mid","base")
    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base", flip=True)

    hide screen blkfade
    with d5
    call ctc

    her "I demand a higher grade than that!" ("soft", "base", "angry", "L", xpos="right", ypos="base", flip=True)
    sna "You do not demand a grade, Miss Granger... You earn it!" ("snape_09")
    her "I did earn it!" ("clench", "narrow", "annoyed", "L")
    her "And could you at least have the decency to stop touching yourself when partaking in such an important discussion, professor!" ("annoyed", "narrow", "angry", "down")
    sna "*Tch*..." ("snape_12")
    hide hermione_main
    with d3

    gen "(Are they for real?)" ("base", xpos="far_left", ypos="head")
    pause.2

    show screen blkfade
    with d5

    nar "You watch Snape, who's still got his dick hanging out, argue with the cum-covered Hermione about her imaginary grade."
    nar "After a while, he agrees to change Hermione's grade from \"acceptable\" to \"Exceeds expectations\"."
    nar "He then tucks his dick back into his robes, and beats a hasty retreat before Hermione has a chance to start another argument."
    pause 1

    call sna_chibi("stand","mid","base")

    hide screen blkfade
    with d5

    call sna_walk(action="leave")
    call her_chibi("stand","desk","base", flip=False)

    gen "Good job, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]..." ("open", "base", "base", "mid", flip=False)
    gen "Now then..." ("base", xpos="far_left", ypos="head")

    jump hg_pf_strip_T4_snape_results

label hg_pf_strip_T4_snape_watch:
    $ _watch = True

    her @ cheeks blush "I will just keep on dancing then..." ("soft", "closed", "base", "mid")

    call her_chibi("dance","on_desk","on_desk")

    nar "Hermione squeezes her breasts and shakes her hips slightly..."

    gen "That's it, Miss Granger... Very good." ("base", xpos="far_left", ypos="head")
    sna "*Ahem*! Acceptable performance..." ("snape_12")
    her "...." ("soft", "closed", "worried", "mid")
    gen "*Heh*..." ("base", xpos="far_left", ypos="head")
    gen "So... How would you grade her tits?" ("base", xpos="far_left", ypos="head")
    her "......" ("annoyed", "closed", "base", "mid")
    sna "*Hmm*......" ("snape_20")
    her "........" ("annoyed", "closed", "base", "mid")
    sna "I'd say they \"Exceed expectations\"..." ("snape_12")
    her "!!!" ("angry", "squint", "base", "stare")
    gen "Really? I'm surprised you'd grade them so high." ("base", xpos="far_left", ypos="head")
    sna "As an honourable man, I do give credit where it's due..." ("snape_02")
    her "(*Ugh*... I can't stand him... Honourable, my ass...)" ("angry", "narrow", "base", "stare")
    her "(Better finish this up, quickly...)" ("annoyed", "closed", "base", "mid")
    pause.1

    if hermione.is_worn("panties"):

        nar "Hermione bends over and slides her panties down."
        nar "Her movements lack grace..."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("clothes")
        pause.5
        call ctc

        nar "But a pretty pussy is always a welcome sight nonetheless..."
        nar "Or a plump ass, in the case of the present company..."
    else:
        $ hermione.strip("clothes")

    sna "Yes..." ("snape_20")
    sna "Now shake that ass for me, you harlot!"
    her "......." ("angry", "happyCl", "worried", "mid")
    pause .5

    nar "All of a sudden, Hermione breaks into a series of rather complex pirouettes."
    sna "Yes, such grace..." ("snape_20")
    sna "That lithe, flexible body!" ("snape_20")
    her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}" ("grin", "closed", "angry", "mid")

    nar "Hermione seems very focused on her dancing routine."

    sna "Yes, and now another pirouette!" ("snape_20")
    sna "Magnificent!"

    show screen blkfade
    with d5

    nar "She then performs another set of movements, and pirouettes..."
    nar "Once finished, she gives a little curtsy bow to an imaginary audience..."
    nar "And then exhaustedly slumps down onto the desk."

    call her_chibi("sit_naked","on_desk","on_desk")

    call hide_characters
    hide screen blkfade
    with d5
    call ctc

    sna "Good job, harlot!" ("snape_22")
    her @ cheeks blush "............." ("soft", "narrow", "base", "R")

    if game.daytime:
        sna "Well, my class is about to start, so I will be leaving now." ("snape_22")
        sna "Don't you have potion class with me today, Miss Granger?" ("snape_22")
        her @ cheeks blush "Yes..." ("disgust", "narrow", "base", "down")
        sna "Well, don't be late, girl..." ("snape_22")
        sna "Albus..." ("snape_02")
        gen "See you soon, Severus." ("grin", xpos="far_left", ypos="head")
    else:
        sna "Well, it is getting rather late... I think I will be leaving now." ("snape_22")
        sna "Good night, Albus." ("snape_22")
        gen "Severus." ("base", xpos="far_left", ypos="head")
        sna "Harlot." ("snape_22")
        her "Professor..." ("disgust", "narrow", "base", "down")

    call sna_walk(action="leave")
    pause.5


    gen "Good job, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]..." ("normal", "happyCl", "worried", "mid")
    gen "Now then..." ("base", xpos="far_left", ypos="head")

    jump hg_pf_strip_T4_snape_results
label hg_pf_strip_T4_snape_results:

    if _wearing_clothes:
        her "One moment, [name_genie_hermione]... Let me just put something on..." ("angry", "narrow", "base", "down")
        if _masturbate_finished:
            her "I'd also like to clean this off as soon as possible if you don't mind..." ("normal", "narrow", "worried", "mid")
            gen "Certainly..." ("base", xpos="far_left", ypos="head")

    else:
        if _masturbate_finished:
            her "One moment, [name_genie_hermione]... I'd like to clean myself as soon as possible..." ("normal", "narrow", "worried", "mid")
            gen "Certainly..." ("base", xpos="far_left", ypos="head")
        else:
            her "One moment, [name_genie_hermione]... I just need a second to collect my thoughts..." ("normal", "narrow", "worried", "mid")
            gen "Certainly..." ("base", xpos="far_left", ypos="head")


    show screen blkfade
    with d5

    $ hermione.set_cum(None)
    $ hermione.wear("all")
    call hide_characters

    call her_chibi("stand","desk","base", flip=False)

    hide screen blkfade
    with d3


    stop music fadeout 1.0

    gen "Ready?" ("base", xpos="far_left", ypos="head")
    her "Yes, I'm ready [name_genie_hermione]." ("open", "closed", "base", "mid", trans=d3)
    gen "I'd say that was a great success." ("base", xpos="far_left", ypos="head")
    her "You think so, [name_genie_hermione]?" ("soft", "base", "base", "mid")
    gen "Most certainly." ("base", xpos="far_left", ypos="head")
    gen "Now, why don't you tell me what you've learned?" ("base", xpos="far_left", ypos="head")

    if _flogging_known:
        her "Well, I've learned that he doesn't seem to have any problems with hitting his students..." ("open", "closed", "base", "mid")
        gen "*Hmm*... I'd say that his statement isn't exactly conclusive enough to make that assumption." ("base", xpos="far_left", ypos="head")
        her "*Hmph*... Perhaps..." ("annoyed", "narrow", "base", "R")
        gen "Anything else?" ("base", xpos="far_left", ypos="head")

    if _potter_known:
        her "I've learned that he finally stopped targeting Harry..." ("open", "closed", "base", "mid")
        her "Probably due to being busy with all the favour trading..." ("annoyed", "narrow", "base", "R")
        her "So I suppose there's at least one positive thing about those Slytherin girls whoring themselves out..." ("base", "narrow", "base", "R")
        gen "Anything else?" ("base", xpos="far_left", ypos="head")

    if _weasley_known:
        her "I've learned that he's been eyeing up a student outside of Slytherin..." ("annoyed", "base", "base", "R")
        gen "Really? What gave you that idea?" ("base", xpos="far_left", ypos="head")
        her "From what he said about the Weasley twins..." ("annoyed", "narrow", "base", "mid")
        her "Unless they've got some friend in Slytherin... Which I highly doubt..." ("open", "closed", "base", "mid")
        her "He must've been talking about--" ("angry", "narrow", "base", "R")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        her "*Hmm*... Nevermind..." ("annoyed", "base", "base", "R")
        gen "Anything else?" ("base", xpos="far_left", ypos="head")

    if _butt_known:
        her "I've learned that he's got absolutely zero depth perception..." ("annoyed", "narrow", "angry", "R")
        gen "Really? What makes you say that?" ("base", xpos="far_left", ypos="head")
        her "He called my butt dreadful!" ("open", "base", "angry", "mid")
        her @ cheeks blush "And that it's like that of a boy's!" ("disgust", "closed", "angry", "mid")
        if _watch:
            gen "He did mention that your breasts exceeded his expectations." ("base", xpos="far_left", ypos="head")
            her "He never commented on their size." ("annoyed", "base", "base", "mid")
            gen "That is true..." ("base", xpos="far_left", ypos="head")
        else:
            gen "Yes, how could he say such things... That just isn't true." ("base", xpos="far_left", ypos="head")
            her "Thank you [name_genie_hermione]... Although I was trying to get validated..." ("open", "base", "base", "R")
        gen "Anything else?" ("base", xpos="far_left", ypos="head")

    her "*Hmm*... Let me think..." ("open", "base", "base", "R")

    if _masturbate:
        if not states.her.ev.dance_for_me.snape_masturbate_stage1:
            $ states.her.ev.dance_for_me.snape_masturbate_stage1 = True
            her "Well... I learned that guys don't seem to mind masturbating together..." ("open", "narrow", "base", "R")
            gen "I just thought I'd better see just how far he would go." ("base", xpos="far_left", ypos="head")
            if states.her.tier < 5:
                her "Quite far it appears..." ("annoyed", "narrow", "base", "mid")
                her "If I hadn't ended it, he probably would've gone all the way..." ("angry", "narrow", "base", "down")
                gen "I suppose we'll never know..." ("base", xpos="far_left", ypos="head")
                her "..." ("annoyed", "narrow", "base", "R")
        else:
            her "Well... I learned that you two masturbating over me has become a frequent occurrence..." ("open", "narrow", "base", "R")
            gen "At least now you know just how far he's willing to go." ("base", xpos="far_left", ypos="head")
            her "(Like I didn't know that already...)" ("annoyed", "narrow", "base", "mid")
            if states.her.tier < 5:
                her "Once again, I don't doubt he would've seen it through to the end, had I not ended it." ("open", "closed", "base", "mid")
                gen "Well, you never know..." ("base", "base", "base", "mid")
                her "..." ("annoyed", "narrow", "base", "R")
    if _masturbate_finished:
        if not states.her.ev.dance_for_me.snape_masturbate_stage2:
            $ states.her.ev.dance_for_me.snape_masturbate_stage2 = True
            if not states.her.status.cumshot:
                $ states.her.status.cumshot = True #Cum on her body for the first time
                her @ cheeks blush "Still... I've never let somebody do that to me before... Let alone two people." ("angry", "base", "base", "R")
                gen "Do what?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Ejaculate...{w=0.4} On my body..." ("open", "narrow", "base", "down")
                gen "I see..." ("base", xpos="far_left", ypos="head")
                her "Oh well... At least now I know what Snape expects from something like this..." ("open", "closed", "base", "mid")
            else:
                her @ cheeks blush "Even then, I didn't think that you'd go as far as finishing on me..." ("angry", "base", "base", "mid")
                her "Although in hindsight, I probably should've known..." ("open", "narrow", "base", "R")
        else:
            her @ cheeks blush "I'm not really sure why I allowed it to go all the way to you both finishing on me again..." ("annoyed", "base", "base", "mid")
            her "I already know just how much Snape expects from a student performing a task like this." ("open", "closed", "base", "mid")
            gen "Then more the reason to see it through." ("base", xpos="far_left", ypos="head")
            her "I suppose..." ("open", "narrow", "base", "R")

    if _watch:
        gen "Did Severus act the way you expected?" ("base", xpos="far_left", ypos="head")
        her "Yes, he's just as self-absorbed and perverted as he's ever been." ("open", "narrow", "angry", "mid")
        random:
            her "Calling a girl a harlot... Such a typical thing for him to say..." ("angry", "narrow", "angry", "R")
            her "There's no doubt, with how easily he threw out terms like \"shake those titties, you harlot\", that the Slytherin girls must be shaking theirs at him frequently." ("angry", "narrow", "angry", "R")
            her "He barely flinched when I squeezed my breasts, which tells me he's used to that sort of thing..." ("angry", "narrow", "angry", "R")
            block:
                her "The way he carries himself, is of a man who expects his students to act a certain way... I almost feel sorry for the Slytherin girls..." ("angry", "narrow", "angry", "R")
                her "Almost." ("base", "narrow", "angry", "R")

    if states.her.tier == 4:
        her "May I have my points now?" ("open", "closed", "base", "mid")
        gen "Certainly." ("base", xpos="far_left", ypos="head")
    else:
        gen "Alright then, I believe that we're done here for today." ("base", xpos="far_left", ypos="head")
        gen "Unless there's anything else?" ("base", xpos="far_left", ypos="head")
        her "..." ("annoyed", "narrow", "base", "R")
        gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her "Oh... No, not that I can think of at this moment, [name_genie_hermione]." ("angry", "base", "base", "mid")
        gen "Very well... You've certainly earned your points today." ("base", xpos="far_left", ypos="head")
        her "Oh, right... The points..." ("angry", "mid", "base", "mid")

    jump end_hg_pf_strip
