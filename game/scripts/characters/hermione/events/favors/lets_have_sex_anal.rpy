

### Hermione Anal Sex###

### Anal Sex Event 1 ###

label hg_anal_sex_1_intro:
    $ states.her.status.anal = True
    $ current_payout = 90

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]...?" ("annoyed", "happy", "base", "mid", flip=True)
    gen "How familiar are you with the term \"Anal Sex\"?" ("base", xpos="far_left", ypos="head")
    her "What?!" ("soft", "wide", "worried", "mid")
    gen "Answer the question..." ("base", xpos="far_left", ypos="head")
    her "Ninety house points..." ("annoyed", "narrow", "annoyed", "mid")
    gen "Seriously?" ("base", xpos="far_left", ypos="head")
    her "Yes!" ("mad", "happyCl", "worried", "mid")
    her "............................." ("disgust", "narrow", "base", "mid")
    gen "Well alright then. Ninety house points it is." ("base", xpos="far_left", ypos="head")

    show screen blkfade
    with d5
    pause.2

    #Stop wind and thunder sounds
    stop weather fadeout 4

    # Hermione Setup
    hide hermione_main

    if _temp_outfit_choice == "naked":
        show her_sex_personal lean_back mouth_annoyed eyes_base_r eyebrows_worried as cg
    else:
        show her_sex_personal lean_back shirt skirt mouth_annoyed eyes_base_r eyebrows_worried as cg

    show her_sex_personal lean_back as cg zorder 17:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0

    hide screen blkfade
    with d5

    her "..........."

    show her_sex_personal lean_back as cg:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0
        ease_quad 3.0 offset (-230, -100) zoom 0.5 rotate -15

    gen "Let's see..."

    show her_sex_personal mouth_angry eyes_happycl eyebrows_worried as cg
    her "................."
    gen "*Hmm*..."

    show her_sex_personal mouth_angry eyes_wide_stare eyebrows_base as cg
    her "!!!"
    gen "Oh, come on!"
    show her_sex_personal mouth_mad eyes_happycl eyebrows_worried tears_soft_blink as cg
    her "Ouch!"
    gen "Just try to loosen up a little, would you?"
    show her_sex_personal mouth_angry eyes_base_mid eyebrows_base tears_soft as cg
    her "I'm trying!"
    gen "Okay, what if I do this...?"

    show her_sex_personal lean_forward caress as cg:
        offset (-230, -100)
        zoom 0.5
        rotate -15
        ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

    show her_sex_personal mouth_mad eyes_happycl eyebrows_worried tears_soft_blink as cg
    her "Ouch! What are you doing, [name_genie_hermione]?"
    gen "Yeah, this won't work either..."
    gen "*Hmm*..."
    gen "Alright, I think I know what we should do."

    label .choices:

    menu:
        gen "..."
        "\"I think I'll spit on it and just force it in!\"":
            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
            show her_sex_personal mouth_clench eyes_wide_r eyebrows_base tears_none as cg
            her "Force it in, [name_genie_hermione]?!"
            play sound "sounds/spit.ogg" #Sound of spiting.
            gen "*SPIT*!"
            show her_sex_personal mouth_disgust eyes_happycl eyebrows_worried as cg
            her "*Eeeeeew*!"
            show her_sex_personal mouth_clench eyes_happy_r eyebrows_worried as cg
            her "No, [name_genie_hermione], wait! Maybe if I just relax--"
            gen "No need, here I come!"
            with hpunch
            show her_sex_personal mouth_mad eyes_wide_mid eyebrows_worried tears_soft as cg
            her "AAAAH!"
            show her_sex_personal mouth_open eyes_happycl eyebrows_worried tears_soft_blink as cg
            her "Ouch! Ouch! Ouch!"
            gen "Almost in!"
            show her_sex_personal mouth_scream eyes_wide_r eyebrows_base tears_soft as cg
            her "No, you're hurting me! You are hurting me!"
            gen "Almost! Almost!"
            show her_sex_personal mouth_clench eyes_happycl eyebrows_worried as cg
            her "Ah! It hurts!"
            gen "Shut it, [name_hermione_genie]! I'm doing you a favour!"
            gen "Your anus is so tight it's completely unfuckable!"
            show her_sex_personal mouth_mad eyes_happycl eyebrows_worried tears_soft_blink as cg
            her "Then stop, please!"

            show her_sex_personal caress_grin as cg

            gen "No! We need to loosen up your asshole a little!"

            show her_sex_personal mouth_mad eyes_narrow_mid eyebrows_worried tears_soft as cg
            her "But I don't want you to!"
            gen "Really? How do you expect people to fuck you up your ass, then?"
            show her_sex_personal mouth_clench eyes_wide_r eyebrows_worried tears_soft as cg
            her "What people?"

            show her_sex_personal caress as cg
            gen "You know... people."

            gen "*Argh*, dammit... My dick is hurting too now."
            show her_sex_personal mouth_open eyes_happycl eyebrows_worried tears_soft_blink as cg
            her "Stop then! Stop, [name_genie_hermione]!"
            show her_sex_personal mouth_angry eyes_narrow_r eyebrows_base tears_soft as cg
            her "I've changed my mind! I don't need these points!"
            gen "I think I'm almost..."


            play sound "sounds/gltch.ogg"
            with hpunch
            with kissiris
            show her_sex_personal mouth_open_wide_tongue eyes_wide_ahegao eyebrows_base tears_soft as cg
            her "{size=+5}*AAAAAAAAhhhhh*!!!{/size}"
            gen "YES!!!"

            show her_sex_personal caress_grin as cg

            gen "Let us pump this little asshole full of semen then, shall we?"

            play background "sounds/slickloop.ogg" fadein 2

            show her_sex_personal mouth_open eyes_happycl eyebrows_worried cheeks_blush tears_soft_blink as cg
            her "Yes...{w=0.4} Please, I just want this to end..."
            gen "*Agh*...{w=0.4} You want this to end sooner?"
            gen "Help me out then!"
            show her_sex_personal mouth_mad eyes_happy_down eyebrows_base cheeks_blush tears_soft as cg
            her "*sob*! How?"

            show her_sex_personal caress as cg
            gen "You know..."

            show her_sex_personal mouth_upset eyes_happy_down eyebrows_base cheeks_blush tears_soft as cg
            her "Oh..."
            show her_sex_personal mouth_angry eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "I am a whore??"

            show her_sex_personal caress_grin as cg
            gen "Yes you are!"

            show her_sex_personal mouth_annoyed eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "*Sob*! I am a whore..."
            show her_sex_personal mouth_open eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "I love to suck cock..."
            show her_sex_personal mouth_mad eyes_narrow_mid eyebrows_base cheeks_blush tears_soft as cg
            her "And now my tiny asshole is getting ripped apart... *Sob!*"
            gen "*Ah*! Yes!"

            play background "sounds/slickloopfast.ogg"

            show her_sex_personal mouth_clench eyes_wide_down eyebrows_worried cheeks_blush tears_soft as cg
            her "No! Is it getting bigger?! I'm scared!"
            gen "*ARGH*!"

        "\"Suck me off first. Lubricate my cock!\"":
            show her_sex_personal mouth_angry eyes_narrow_down eyebrows_base tears_none as cg
            her "Oh... Alright..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

            hide cg
            call her_chibi_scene("bj", trans=fade)

            her "*Slurp*! *Slurp*! *Slurp*!"
            gen "Yes... good..."
            her "*Slurp*! *Slurp*! *Slurp*!"
            gen "Alright, I think that's enough. Back on the desk now."

            if _temp_outfit_choice == "naked":
                show her_sex_personal lean_forward caress mouth_open eyes_base_mid eyebrows_base as cg zorder 17:
                    transform_anchor True
                    anchor (0.0, 0.0)
                    offset (-65, -240)
                    zoom 0.45
                    rotate -4
            else:
                show her_sex_personal skirt shirt lean_forward caress mouth_open eyes_base_mid eyebrows_base as cg zorder 17:
                    transform_anchor True
                    anchor (0.0, 0.0)
                    offset (-65, -240)
                    zoom 0.45
                    rotate -4
            with fade

            gen "Let's see now..."
            her "............."
            gen "Yes! Almost!"
            show her_sex_personal mouth_mad eyes_happycl eyebrows_annoyed cheeks_blush as cg
            her "Ouch!"
            gen "Relax. Almost in."

            play sound "sounds/gltch.ogg"
            with kissiris
            show her_sex_personal mouth_open_wide_tongue eyes_base_ahegao eyebrows_base cheeks_blush as cg
            her "{size=+5}*AAAAAAAAhhhhh*!!!{/size}"

            show her_sex_personal caress_grin as cg

            gen "YES!!!"
            show her_sex_personal mouth_clench eyes_wide_up eyebrows_base cheeks_blush as cg
            her "My...{w=0.4} my..."
            show her_sex_personal mouth_angry eyes_happycl eyebrows_worried cheeks_blush as cg
            her "It hurts!"
            gen "Let's pump this little asshole full of semen then, shall we?"
            show her_sex_personal mouth_angry eyes_happy_mid eyebrows_base cheeks_blush as cg
            her "....................."

            show her_sex_personal caress as cg

            show her_sex_personal mouth_angry eyes_base_r eyebrows_base cheeks_blush tears_soft as cg
            her "....................."
            gen "You alright there, [name_hermione_genie]?"
            show her_sex_personal mouth_clench eyes_base_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3} You are...{w=0.3} Stretching me out from the inside... [name_genie_hermione]."
            show her_sex_personal mouth_angry eyes_happy_mid eyebrows_base cheeks_blush as cg
            her "And it still hurts..."
            gen "*Hmm*..."
            gen "Maybe not enough lubrication...?"
            gen "Come on down, [name_hermione_genie]. Suck my dick some more."
            show her_sex_personal mouth_clench eyes_base_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "What? But..."
            show her_sex_personal mouth_disgust eyes_happy_r eyebrows_base cheeks_blush tears_soft as cg
            her "But it's dirty... It's been inside already."
            gen "Yes, it's been inside, but that doesn't mean it's dirty."
            gen "Come on now, [name_hermione_genie]. Suck it some more."
            show her_sex_personal mouth_annoyed eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "..........."

            hide cg
            call her_chibi_scene("bj", trans=fade)


            her "*Slurp*! *Slurp*! *Slurp*!"
            gen "Yes...{w=0.4} good..."
            her "*Slurp*! *Slurp*! *Slurp*!"
            gen "Can you taste your ass on my dick?"
            her "*Slurp*! *Slurp*! *Slurp*!"
            gen "Alright, Maybe that's enough."

            show screen blkfade
            with d3

            pause .8
            play sound "sounds/gltch.ogg"
            with kissiris
            pause 1

            if _temp_outfit_choice == "naked":
                show her_sex_personal lean_forward caress mouth_clench eyes_narrow_mid eyebrows_base cheeks_blush tears_soft as cg zorder 17:
                    transform_anchor True
                    anchor (0.0, 0.0)
                    offset (-65, -240)
                    zoom 0.45
                    rotate -4
            else:
                show her_sex_personal skirt shirt lean_forward caress mouth_clench eyes_narrow_mid eyebrows_base cheeks_blush tears_soft as cg zorder 17:
                    transform_anchor True
                    anchor (0.0, 0.0)
                    offset (-65, -240)
                    zoom 0.45
                    rotate -4

            hide screen blkfade
            with fade

            her "*Ah*..."
            gen "Better now?"
            show her_sex_personal mouth_open eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "It still hurts..."
            show her_sex_personal mouth_soft eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "But I think I will be fine..."
            gen "I'll take it slow for now..."

            play background "sounds/slickloop.ogg" fadein 2
            show her_sex_personal mouth_mad eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.4} thank you, [name_genie_hermione]."
            gen "Oh...{w=0.3} yes...{w=0.3} this feels great..."
            show her_sex_personal mouth_angry eyes_narrow_mid eyebrows_base cheeks_blush tears_soft as cg
            her "..........."
            gen "*Ah*...{w=0.3} So tight..."
            show her_sex_personal mouth_angry eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "................"
            gen "Why are you being so quiet [name_hermione_genie]?"
            show her_sex_personal mouth_disgust eyes_narrow_r eyebrows_worried cheeks_blush tears_soft as cg
            her "Because this is painful..."
            show her_sex_personal mouth_disgust eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "And I just want you to cum sooner, [name_genie_hermione]..."
            gen "So you stifle your cries of pain?"
            show her_sex_personal mouth_angry eyes_narrow_stare eyebrows_base cheeks_blush tears_soft as cg
            her "Yes [name_genie_hermione]. *Sob*!"
            gen "Don't do that."
            gen "Sob, scream, and cry as much as you wish!"
            show her_sex_personal mouth_disgust eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "B-but--"
            gen "That will make me cum sooner."
            show her_sex_personal mouth_open eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "Really? *Sob*!"
            show her_sex_personal mouth_open eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "*Sob*! It hurts! *Sob*! It hurts so much! *Sob*!"
            gen "Yes, yes..."
            show her_sex_personal mouth_angry eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "*SOB*!"
            gen "You poor girl..."
            gen "A Big, evil man is violating your asshole!"
            show her_sex_personal mouth_upset eyes_happycl eyebrows_base cheeks_blush tears_soft_blink as cg
            her "*SOB*!{w=0.3} *SOB*!"
            gen "*Argh*!"
            show her_sex_personal mouth_clench eyes_narrow_r eyebrows_worried cheeks_blush tears_soft as cg
            her "No, I'm scared! *SOB*!"

        "\"Let's use some lubrication.\"{size=-2}(Item){/size}" (style="disabled") if anal_lube_ITEM.owned <= 0:
            gen "(I don't have any lube left. I'm gonna have to be more creative.)"
            jump hg_anal_sex_1_intro.choices

        "\"Let's use some lubrication.\" {size=-2}(Item){/size}" if anal_lube_ITEM.owned > 0:
            $ anal_lube_ITEM.owned -= 1

            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
            show her_sex_personal mouth_angry eyes_wide_stare eyebrows_base tears_none as cg
            her "Lubrication, [name_genie_hermione]?!"
            gen "*Shhh*... Just stay still."

            play sound "sounds/slick_01.ogg"

            "*Squeeze*!"
            show her_sex_personal mouth_scream eyes_happycl eyebrows_worried as cg


            show her_sex_personal lean_back hold as cg
            with d3

            show her_sex_personal mouth_clench eyes_happycl eyebrows_worried as cg
            her "Ahhh! It's cold!"
            nar "You thoroughly lubricate her asshole."
            gen "That should do it."
            show her_sex_personal mouth_angry eyes_base_mid eyebrows_worried as cg
            her "No, [name_genie_hermione], wait! Maybe--"

            show her_sex_personal lean_forward caress as cg
            with d3
            nar "You push Hermione forward and align the tip of your dick with her lubricated winky star..."

            play sound "sounds/gltch.ogg"
            with hpunch
            with kissiris

            show her_sex_personal mouth_open_wide_tongue eyes_wide_up eyebrows_worried cheeks_blush tears_soft as cg
            her "*ARGH*!"
            nar "Your cock fully penetrates her asshole as the lubrication does its job."

            show her_sex_personal caress_grin as cg
            gen "Holy shit!"

            show her_sex_personal mouth_mad eyes_happycl eyebrows_worried cheeks_blush tears_soft_blink as cg
            her "Ouch! Ouch! Ouch!"
            show her_sex_personal mouth_mad eyes_wide_down eyebrows_worried cheeks_blush tears_soft as cg
            her "No, you're hurting me! You are hurting me!"

            show her_sex_personal caress as cg
            gen "*Argh* Fuck, I can't pull out!"

            show her_sex_personal mouth_open eyes_base_down eyebrows_worried cheeks_blush tears_soft as cg
            her "Ah! It hurts!"
            gen "Then stop clenching on me so hard, [name_hermione_genie]!"
            gen "Your anus is so tight I can't even move!"
            show her_sex_personal mouth_mad eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "Please, do something!"
            gen "I'm trying, [name_hermione_genie]!"
            show her_sex_personal mouth_clench eyes_wide_r eyebrows_annoyed cheeks_blush tears_soft as cg
            her "Then try harder!"
            call slap_her
            show her_sex_personal mouth_angry eyes_happycl eyebrows_base cheeks_blush tears_soft as cg
            her "..........!"
            gen "Shut the hell up, whore!"
            show her_sex_personal mouth_disgust eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg

            gen "It's..."
            call slap_her
            show her_sex_personal mouth_disgust eyes_wide_mid eyebrows_base cheeks_blush tears_soft as cg

            gen "It's...{fast} your..."
            call slap_her
            show her_sex_personal mouth_mad eyes_wide_mid eyebrows_base cheeks_blush tears_soft as cg

            gen "It's... your...{fast} bloody..."
            call slap_her
            show her_sex_personal mouth_mad eyes_wide_up eyebrows_base cheeks_blush tears_soft as cg

            gen "It's... your... bloody... {fast}fault!"
            call slap_her
            pause 1.0
            play sound "sounds/plop.ogg"
            with hpunch
            pause 1.0
            show her_sex_personal mouth_angry eyes_happy_down eyebrows_base cheeks_blush tears_soft as cg

            gen "Oh, it worked!"

            show her_sex_personal mouth_normal eyes_happycl eyebrows_worried cheeks_blush tears_soft_blink as cg
            her "*Sob*!"
            show her_sex_personal mouth_open eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "...{w=0.3} My asshole...{w=0.3} My poor asshole... *sob*"

            show her_sex_personal caress_grin as cg
            gen "Let's try it again..."

            show her_sex_personal mouth_disgust eyes_wide_r eyebrows_worried cheeks_blush tears_soft as cg
            her "No! Stop, [name_genie_hermione]!"
            show her_sex_personal mouth_mad eyes_wide_r eyebrows_worried cheeks_blush tears_soft as cg
            her "I've changed my mind! I don't need these points!"
            gen "It will be fine this time, trust me..."

            play sound "sounds/gltch.ogg"
            with kissiris
            show her_sex_personal mouth_scream eyes_wide_up eyebrows_base cheeks_blush tears_soft as cg
            her "{size=+5}AAAAAAAAhhhhh!!!{/size}"
            gen "YES!!!"

            show her_sex_personal mouth_mad eyes_base_down eyebrows_worried cheeks_blush as cg

            gen "Let us pump this little asshole full of semen then, shall we?"

            play background "sounds/slickloop.ogg" fadein 2

            show her_sex_personal mouth_clench eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3} Please, I just want this to end..."
            gen "*Agh*...{w=0.3} You want this to end sooner?"
            gen "Help me out then!"
            show her_sex_personal mouth_angry eyes_narrow_r eyebrows_base cheeks_blush tears_soft as cg
            her "*Sob* How?"
            gen "You know..."
            show her_sex_personal mouth_angry eyes_base_r eyebrows_base cheeks_blush tears_soft as cg
            her "Oh..."
            show her_sex_personal mouth_open eyes_narrow_r eyebrows_worried cheeks_blush tears_soft as cg
            her "I am a whore??"
            gen "Yes you are!"
            show her_sex_personal mouth_angry eyes_happy_down eyebrows_base cheeks_blush tears_soft as cg
            her "*Sob*! I am a whore..."
            show her_sex_personal mouth_upset eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "I love to suck cock..."
            show her_sex_personal mouth_upset eyes_happycl eyebrows_worried cheeks_blush tears_soft_blink as cg
            her "And now my tiny asshole is getting ripped apart... *Sob*!"
            gen "Yes! Yes!"
            gen "*Argh*! Yes!"
            show her_sex_personal mouth_clench eyes_happy_r eyebrows_worried cheeks_blush tears_soft as cg
            her "No! Is it getting bigger?! I'm scared!"

    menu:
        "-Fill her up-":
            $ states.her.status.anal_creampie = True

            gen "Here it comes!"
            show her_sex_personal mouth_clench eyes_wide_r eyebrows_worried cheeks_blush tears_soft as cg
            her "No, wait!"

            play background "sounds/slickloopfast.ogg"
            nar "You start pumping your cock deep into Hermione's asshole with renewed vigour."

            show her_sex_personal mouth_clench eyes_happycl eyebrows_base cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3} *Ah*...{w=0.3} Please...{w=0.3} Not inside my--{w=0.2} *Ah*..."

            play background "sounds/sexloopveryfast.ogg"
            nar "Not showing the girl any mercy, you thrust your hips even harder against her, pushing your cock down to the hilt into her ass."
            gen "That's it slut, take this!"

            with hpunch
            play sound "sounds/slick_01.ogg"
            gen "{size=+7}*Argh*!!!{/size}"
            show her_sex_personal mouth_clench eyes_wide_mid eyebrows_worried cheeks_blush tears_soft as cg


            call cum_block

            play sound "sounds/slick_02.ogg"
            gen "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}"

            call cum_block

            show her_sex_personal mouth_angry eyes_narrow_up eyebrows_worried cheeks_blush tears_soft as cg
            her "*AH*! IT'S FILLING ME UP!{heart}{heart}{heart}"
            gen "Yes, you whore! Yes!"
            show her_sex_personal mouth_mad eyes_wide_mid eyebrows_base cheeks_blush tears_soft as cg
            her "It hurts, it hurts!"
            gen "Shut up!"

            play sound "sounds/slick_02.ogg"
            call cum_block

            show her_sex_personal mouth_angry eyes_happycl eyebrows_worried cheeks_blush tears_soft_blink as cg
            her "No, I am already full! Stop cumming, you bastard!"
            gen "Shut the fuck up, slut! I am not done yet!"
            show her_sex_personal mouth_clench eyes_narrow_up eyebrows_worried cheeks_blush tears_soft as cg
            her "No! Please! My stomach! I will explode!"
            show her_sex_personal mouth_angry eyes_happy_r eyebrows_base cheeks_blush tears_soft as cg
            her "Stop! I'm going to throw up!"

            show her_sex_personal mouth_angry eyes_base_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "Please no more, or I'll--"
            stop background fadeout 2
            play sound "sounds/slick_02.ogg"
            pause .8

            play sound "sounds/burp.ogg"
            show her_sex_personal mouth_full eyes_happycl eyebrows_worried cheeks_blush tears_soft as cg
            her "{size=+7}*BURP*!!!!!!{/size}"
            show her_sex_personal mouth_full eyes_happy_mid eyebrows_base cheeks_blush tears_soft as cg
            her "......"
            show her_sex_personal mouth_full eyes_happy_down eyebrows_base cheeks_blush tears_soft as cg
            her "......{fast}......"
            play sound "sounds/gulp.ogg" #Sound of gulping down a liquid.
            show her_sex_personal mouth_normal eyes_happycl eyebrows_worried tears_soft_blink as cg
            her "{size=+7}*GULP*!{/size}"
            show her_sex_personal mouth_open_tongue eyes_narrow_mid eyebrows_worried tears_soft as cg

            call ctc
            gen "That felt great..."

            show her_sex_personal bent_over grab as cg:
                anchor (0.0, 0.0)
                offset (-65, -240)
                zoom 0.45
                rotate -4
                easein 1.0 offset (0, -480) rotate 0
            with vpunch

            play sound "sounds/slick_02.ogg"
            show her_sex_personal after as cg

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_light as cg
            else:
                show her_sex_personal cum_ass_skirt_light as cg
            with kissiris

            show her_sex_personal mouth_soft eyes_narrow_mid eyebrows_base cheeks_blush tears_soft as cg:
                offset (0, -480)
                rotate 0
                ease_quad 3.0 offset (-60, -620) zoom 0.55

            nar "Hermione collapses onto your desk and your dick finally slides out of her cum filled ass."
            show her_sex_personal cum_pussy_light as cg
            nar "As she lies there for a moment, you watch as her asshole convulses, and your semen slowly beginning to leak out onto the floor."

            show her_sex_personal mouth_angry eyes_happy_r eyebrows_base cheeks_blush tears_soft as cg
            her "*SOB*! I HATE YOU..."
            show her_sex_personal mouth_clench eyes_base_down eyebrows_annoyed cheeks_blush tears_soft as cg
            her "{size=+5}I HATE YOU AND YOUR NASTY OLD COCK!{/size}"
            gen "*Agh*...{w=0.3} Shut it, [name_hermione_genie]!"

            show her_sex_personal cum_pussy_heavy as cg
            nar "Hermione clenches her ass again, and you watch as another glob of cum leaks out."

            show her_sex_personal mouth_upset eyes_happycl eyebrows_worried cheeks_blush tears_soft_blink as cg
            her "*Sob*!{w=0.4} *Sob*!..."
            gen "Whew!... I think that was the last of it."
            gen "You alright?"
            show her_sex_personal mouth_angry eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "Yes...{w=0.4} *Sob*!"
            show her_sex_personal mouth_soft eyes_narrow_r eyebrows_base cheeks_blush tears_soft as cg
            her "My butt hurts, but I am alright, [name_genie_hermione]..."
            gen "Well, you took my dick stoically, all things considered..."
            show her_sex_personal mouth_base eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "Thank you, [name_genie_hermione]..."
            call ctc

            show her_sex_personal mouth_open eyes_narrow_r eyebrows_base cheeks_blush tears_soft as cg
            her "I apologise for saying that I hate you, [name_genie_hermione]..."
            show her_sex_personal mouth_angry eyes_narrow_down eyebrows_worried cheeks_blush as cg
            her "Your cock is not nasty..."
            show her_sex_personal mouth_open eyes_narrow_down eyebrows_worried cheeks_blush as cg
            her "I suppose when you call me a \"whore\" you don't actually mean it..."
            gen "Right..."
            show her_sex_personal mouth_grin eyes_narrow_mid eyebrows_worried cheeks_blush as cg
            her "I don't know what's gotten into me..."

            gen "My dick!"

            show her_sex_personal mouth_base eyes_narrow_up eyebrows_base cheeks_blush as cg
            her "*Mmm*..."
            gen "Oh yes...{w=0.3} Your asshole...{w=0.3} Is it still hurting?"
            show her_sex_personal mouth_base eyes_narrow_down eyebrows_worried cheeks_blush as cg
            her "A little..."
            show her_sex_personal mouth_grin eyes_narrow_down eyebrows_base cheeks_blush as cg
            her "But I also feel full and warm inside..."
            gen "So you're planning on keeping it in? My cum, I mean."
            show her_sex_personal mouth_base eyes_narrow_down eyebrows_base cheeks_blush as cg
            her "If I can..."

            if game.daytime:
                show her_sex_personal mouth_soft eyes_narrow_l eyebrows_base cheeks_blush as cg
                her "I hope it won't start leaking too much during my classes..."
            else:
                show her_sex_personal mouth_soft eyes_narrow_l eyebrows_base cheeks_blush as cg
                her "I hope it won't start leaking too much before I get to my dorms..."

            gen "Well, good luck on your journey."
            show her_sex_personal mouth_base eyes_narrow_r eyebrows_base cheeks_blush as cg
            her "Can I get paid now, please?"

            gen "Of course..."

            show screen blkfade
            with d5

            nar "You step back and give Hermione's ass a last glance, her asshole still convulses slightly as your cum continues to dribble onto the ground."
            nar "After standing up she touches it as if to check that it's still intact."
            nar "With a sigh of relief, she readies herself and then makes her way to the front of your desk."

        "-Push her down and coat her ass-":

            gen "(Let's coat this bitch!!)"

            show her_sex_personal bent_over grab as cg:
                anchor (0.0, 0.0)
                offset (-65, -240)
                zoom 0.45
                rotate -4
                easein 1.0 offset (0, -480) rotate 0
            with vpunch

            pause 1.0

            #Could add some sound effect here
            show her_sex_personal mouth_soft eyebrows_base eyes_wide_r cheeks_blush as cg:
                offset (0, -480)
                rotate 0
                ease_quad 3.0 offset (-60, -620) zoom 0.55

            show her_sex_personal mouth_mad eyes_happy_stare eyebrows_worried cheeks_blush tears_soft as cg

            play background "sounds/slickloopfast.ogg"
            nar "You push Hermione down onto the desk and fuck her with renewed vigour."

            show her_sex_personal mouth_mad eyes_base_up eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3} *Ah*...{w=0.3} Please--"

            play background "sounds/sexloopveryfast.ogg"
            nar "Not showing the girl any mercy, you thrust your hips hard against her, pushing your cock down to the hilt into her ass."

            show her_sex_personal mouth_angry eyes_narrow_r eyebrows_base cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3} *Ah*...{w=0.3} [name_genie_hermione]..."
            show her_sex_personal mouth_angry eyes_narrow_stare eyebrows_base cheeks_blush tears_soft as cg
            her "You're...{w=0.3} *Ah*...{w=0.3} You're tearing me apart..."
            gen "You ain't seen nothing yet, [name_hermione_genie]!"

            play background "sounds/sexloopfast.ogg"
            nar "You slow down your thrusting until finally..."
            show her_sex_personal mouth_mad eyes_narrow_r eyebrows_base cheeks_blush tears_soft as cg
            her "What are you--"
            stop background
            play sound "sounds/slick_02.ogg"
            pause .3
            play sound "sounds/pop01.ogg"

            show her_sex_personal cum_outside2 as cg

            pause .4
            show her_sex_personal mouth_open_tongue eyes_narrow_up eyebrows_worried cheeks_blush tears_soft as cg
            her "{heart}Ng--{w=0.2} *Ah*...{heart}"

            gen "{size=+5}That's it whore, take this!{/size}"


            gen "{size=+7}*Argh*!!!{/size}"

            show her_sex_personal cum_outside as cg

            call cum_block
            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_light as cg
            else:
                show her_sex_personal cum_ass_skirt_light as cg
            with d5

            play sound "sounds/slick_02.ogg"
            show her_sex_personal mouth_open_tongue eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "*Aaah*...{heart}{heart}{heart}"
            show her_sex_personal cum_outside2 as cg
            gen "{size=+5}Yes!!! All over your ass!{/size}"
            show her_sex_personal cum_outside as cg

            call cum_block
            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_heavy as cg
            else:
                show her_sex_personal cum_ass_skirt_heavy as cg
            with d5

            play sound "sounds/slick_02.ogg"
            show her_sex_personal mouth_base eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.4} It's so hot!"
            show her_sex_personal after as cg
            call ctc


            gen "Well, I'm done...{w=0.4} You can get off my desk now."
            show her_sex_personal mouth_soft eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "Yes, [name_genie_hermione]...{w=0.3} Just...{w=0.3} Give me a minute..."
            gen "You feeling alright?"
            show her_sex_personal mouth_soft eyes_narrow_r eyebrows_base cheeks_blush tears_soft as cg
            her "It still hurts a little, but..."
            gen "But what?"
            show her_sex_personal mouth_soft eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "But in a good way... [name_genie_hermione]."
            gen "In a good way, *huh*?"
            gen "*Heh*...{w=0.3} You cute, little minx."
            show her_sex_personal mouth_angry eyes_narrow_r eyebrows_base cheeks_blush tears_soft as cg
            her "Can I get paid now, [name_genie_hermione]?"

            gen "Certainly!"

            show screen blkfade
            with d5

            nar "You step back and watch as Hermione tries her best to steady herself."
            nar "After finally standing up, she touches her ass as if to check that it's still intact."
            nar "With a sigh of relief, she readies herself and then makes her way to the front of your desk."

    jump end_hg_pf_sex

### Anal Sex Event 2 ###

label hg_anal_sex_2_intro:
    $ states.her.status.anal = True
    $ current_payout = 90

    gen "How about another ass-fucking, [name_hermione_genie]?"
    her "Of course, [name_genie_hermione]." ("base", "narrow", "base", "up", flip=True)
    gen "*Hngh*! You little minx!"

    show screen blkfade
    with d5
    pause.2

    #Stop wind and thunder sounds
    stop weather fadeout 4

    her "........"
    gen "*Hmm*..."
    her "..........."

    play sound "sounds/gltch.ogg"
    with kissiris

    # Hermione Setup
    if _temp_outfit_choice == "naked":
        show her_sex_personal lean_back hold mouth_grin eyes_wide_up eyebrows_base as cg zorder 17:
            transform_anchor True
            anchor (0.0, 0.0)
            offset (-500, -650)
            rotate (15)
            zoom 1.0
    else:
        show her_sex_personal lean_back hold skirt shirt mouth_grin eyes_wide_up eyebrows_base as cg zorder 17:
            transform_anchor True
            anchor (0.0, 0.0)
            offset (-500, -650)
            rotate (15)
            zoom 1.0

    hide screen blkfade
    with d5

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her "*Ooooohhhhhhhhhhhh*....{heart}"

    show her_sex_personal as cg:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0
        ease_quad 3.0 offset (-230, -100) zoom 0.5 rotate -15

    gen "Oh, ye-es!"

    show her_sex_personal mouth_grin eyes_narrow_mid eyebrows_worried as cg
    her "*Ah*..."
    gen "It seems like your butthole has become a bit more welcoming, [name_hermione_genie]."
    gen "I'm going to start moving now..."

    play background "sounds/slickloop.ogg" fadein 2
    call ctc

    show her_sex_personal mouth_soft eyes_closed eyebrows_base as cg
    her "*Ah*...{w=0.3} It...{w=0.3} It still hurts a little."
    gen "Yet you're doing it anyway..."
    show her_sex_personal mouth_open eyes_narrow_down eyebrows_base as cg
    her "*Ah*...{w=0.3} *Ah*...{w=0.3} Yes..."
    show her_sex_personal mouth_base eyes_narrow_down eyebrows_base as cg
    her "I suppose I am..."
    gen "Although that is what I'd expect from such a--"
    if name_hermione_genie == "Whore":
        show her_sex_personal mouth_base eyes_narrow_mid eyebrows_base as cg
        her "I am a whore after all... I'm here to do whatever it is you need..."
        show her_sex_personal hold_grin as cg
        gen "That you are..."
    else:
        show her_sex_personal mouth_grin eyes_narrow_down eyebrows_base cheeks_blush as cg
        her "Please [name_genie_hermione]...{w=0.3} Call me a \"whore\"..."
        show her_sex_personal hold_grin as cg
        gen "*He-Heh*...{w=0.3} You don't have to ask me twice!"
    gen "Now bend over, so I can fuck your ass more easily, whore!"

    show her_sex_personal lean_forward caress as cg:
        offset (-230, -100)
        zoom 0.5
        rotate -15
        ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

    play background "sounds/sexloopfast.ogg" fadein 2

    show her_sex_personal mouth_open eyes_closed eyebrows_base as cg
    her "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*..."
    show her_sex_personal mouth_base eyes_narrow_r eyebrows_base as cg
    her "*Mmm*...{w=0.3} So aggressive..."

    show her_sex_personal caress_grin as cg
    if name_genie_hermione == "Master":
        gen "That's what you deserve for being such a slut!"
    elif name_genie_hermione == "Daddy":
        gen "That's what you get for being such a naughty girl!"

    show her_sex_personal mouth_base eyes_narrow_mid eyebrows_base cheeks_blush as cg
    her "..."
    show her_sex_personal mouth_normal eyes_narrow_r eyebrows_base cheeks_blush as cg
    her "...{fast}..."
    show her_sex_personal mouth_open eyes_narrow_r eyebrows_worried cheeks_blush as cg
    her "[name_genie_hermione]?"

    show her_sex_personal caress as cg
    gen "Yes, whore?"

    show her_sex_personal mouth_angry eyes_narrow_mid eyebrows_base cheeks_blush as cg
    her "*Ehm*..."
    show her_sex_personal mouth_angry eyes_happy_down eyebrows_base cheeks_blush as cg
    her "Would you marry me, [name_genie_hermione]?"
    with hpunch

    stop background fadeout 2

    gen "{size=+9}WHAT?!{/size}"
    gen "Don't tell me you're pregnant, [name_hermione_genie]!"
    if not states.her.status.creampie:
        show her_sex_personal mouth_soft eyes_narrow_down eyebrows_worried cheeks_blush as cg
        her "I can't get pregnant the way we are doing it, [name_genie_hermione]..."
        gen "Good point..."
    else:
        gen "We witchers are infertile!"
        show her_sex_personal mouth_disgust eyes_narrow_r eyebrows_worried cheeks_blush as cg
        her "Right..."
        show her_sex_personal mouth_soft eyes_narrow_down eyebrows_worried cheeks_blush as cg
        her "Well, I suppose I'll just have to trust you on that, [name_genie_hermione]..."
        gen "If you're so worried, I could just fuck you like this from now on..."

    play background "sounds/sexloopfast.ogg"

    show her_sex_personal mouth_angry eyes_base_mid eyebrows_base cheeks_blush as cg
    her "*Ah*..."
    gen "So, what is this talk of marriage then?"
    show her_sex_personal mouth_clench eyes_narrow_r eyebrows_base cheeks_blush as cg
    her "You misunderstood me, [name_genie_hermione]."
    show her_sex_personal mouth_soft eyes_narrow_mid eyebrows_base cheeks_blush as cg
    her "I meant to say, would you marry a girl {size=+5}like{/size} me?"
    show her_sex_personal mouth_base eyes_narrow_l eyebrows_worried cheeks_blush as cg
    her "I would never propose to a man with his cock in my ass, [name_genie_hermione]..."
    gen "Good. Because I don't think any man would be able to say {i}no{/i}."

    if not _temp_outfit_choice == "naked":
        nar "You grab Hermione's top and quickly pull it and her bra over her head, revealing her tits..."

        play sound "sounds/cloth_sound3.ogg"

        show her_sex_personal -shirt as cg
        with d3

    show her_sex_personal mouth_grin eyes_narrow_r eyebrows_worried cheeks_blush as cg
    pause 1
    show her_sex_personal mouth_base eyes_narrow_down eyebrows_base cheeks_blush as cg
    her "*Ah*{heart}..."
    show her_sex_personal mouth_soft eyes_narrow_r eyebrows_base cheeks_blush as cg
    her "What I meant--{w=0.2} *Ah*{heart}...{w=0.3} to say was--{w=0.2} *Ah*{heart}...{w=0.3} Do you think someone would ever--{w=0.2} *Ah*{heart}..."
    gen "*Huh*?"
    show her_sex_personal mouth_soft eyes_narrow_down eyebrows_worried cheeks_blush as cg
    her "I mean, with all the things that have been happening lately--{w=0.2} *Ah*{heart}..."
    show her_sex_personal mouth_normal eyes_closed eyebrows_worried cheeks_blush as cg
    her "I can't help but feel unclean...{w=0.3} Damaged even..."
    show her_sex_personal mouth_annoyed eyes_happy_down eyebrows_worried cheeks_blush as cg
    her "And in a no way innocent."
    show her_sex_personal mouth_disgust eyes_narrow_down eyebrows_base cheeks_blush as cg
    her "Who would want a wife like that?"

    menu:
        gen "..."
        "\"I would marry you in a heartbeat!\"":
            show her_sex_personal mouth_soft eyes_base_r eyebrows_base cheeks_blush as cg
            her "What?"
            gen "Well, hypothetically speaking of course..."
            show her_sex_personal mouth_base eyes_narrow_r eyebrows_base cheeks_blush as cg
            her "...{w=0.3} of course.{heart}"
            show her_sex_personal mouth_base eyes_narrow_down eyebrows_base cheeks_blush as cg
            her ".............."
            show her_sex_personal mouth_normal eyes_happy_r eyebrows_base cheeks_blush as cg
            her "But why do you say that, [name_genie_hermione]?"
            gen "*Huh*?"
            gen "What do you mean {i}why{/i}, [name_hermione_genie]?"
            gen "You are young and attractive..."
            gen "Tight asshole, full tits and a wet little pussy..."
            show her_sex_personal mouth_soft eyes_narrow_r eyebrows_worried cheeks_blush as cg
            her "...{heart}"
            gen "You will make some lucky guy a very happy man one day, whore."
            if name_hermione_genie == "Whore":
                show her_sex_personal mouth_grin eyes_narrow_up eyebrows_annoyed cheeks_blush as cg
                her "*Mmm*...{w=0.3} I love it when you call me that..."
            else:
                gen "*Uhm*... I mean, [name_hermione_genie]."
                show her_sex_personal mouth_grin eyes_narrow_up eyebrows_annoyed cheeks_blush as cg
                her "No, {i}whore{/i} is good. Call me that, [name_genie_hermione]."
            gen "See?{w=0.3} You are a great catch, I'm telling you, whore."
            show her_sex_personal mouth_grin eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "*Ah*...{heart}{w=0.3} Thank you, [name_genie_hermione]."
            gen "*Huh*?"
            gen "Are you crying?"

        "\"Marriage is out of the picture for you.\"":
            show her_sex_personal mouth_angry eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "That's what I thought..."
            gen "Oh...{w=0.3} I just love that little asshole of yours!"
            show her_sex_personal mouth_angry eyes_narrow_stare eyebrows_base cheeks_blush tears_soft as cg
            her "....................."
            her "Yes...{w=0.3} After all the things I had to do for my house..."
            show her_sex_personal mouth_angry eyes_happy_mid eyebrows_base cheeks_blush tears_soft as cg
            her "...{w=0.3} No one will ever want me."
            gen "Oh, they will want you alright!"
            show her_sex_personal mouth_open eyes_wide_stare eyebrows_worried cheeks_blush tears_soft as cg
            her "What?{w=0.3} But you said..."
            gen "Marriage, [name_hermione_genie]...{w=0.3} Marriage is impossible for you."
            gen "But as a man-pleaser you are a great catch!"
            show her_sex_personal mouth_open eyes_wide_stare eyebrows_worried cheeks_blush tears_soft as cg
            her "Really?"
            gen "Are you kidding me?!"
            gen "Young, hot, and slutty. You could have any man you want!"
            show her_sex_personal mouth_base eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "I think you may be right, [name_genie_hermione]."
            gen "I know I am right, whore."
            gen "Now wiggle that little ass of yours a little."
            show her_sex_personal mouth_angry eyes_base_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "Like this?"

            play background "sounds/sexloopveryfast.ogg"
            show her_sex_personal caress_grin as cg
            gen "Yes, that's a good whore."

            show her_sex_personal mouth_angry eyes_narrow_stare eyebrows_base cheeks_blush as cg
            her "I am a whore, aren't I?"
            gen "You just sold me your asshole for ninety house points...{w=0.3} What would you call that?"
            show her_sex_personal mouth_angry eyes_base_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "Yes, yes...{heart}{w=0.3} I am a whore...{heart}"
            gen "Are you crying?"

    show her_sex_personal mouth_angry eyes_narrow_stare eyebrows_base cheeks_blush tears_soft as cg
    her "Amongst other things, [name_genie_hermione]...{heart}{heart}{heart}"
    gen "Amongst other things?"
    show her_sex_personal mouth_smile eyes_narrow_up eyebrows_annoyed cheeks_blush tears_soft as cg
    her "I'm cumming [name_genie_hermione]...{heart}{heart}{heart}"
    gen "*Agh*! My cock!"
    gen "Relax your muscles a little, would you?"
    show her_sex_personal mouth_open eyes_happycl eyebrows_worried cheeks_blush tears_soft_blink as cg
    her "BUT I'M CUMMING!{heart}{heart}{heart}"
    gen "Fine! Have it your way, whore!"

    show her_sex_personal bent_over grab as cg:
        offset (-65, -240)
        zoom 0.45
        rotate -4
        easein 1.0 offset (0, -480) rotate 0
    with vpunch

    pause 1.0

    #Could add some sound effect here
    show her_sex_personal mouth_open eyebrows_base eyes_wide_r cheeks_blush as cg:
        offset (0, -480)
        rotate 0
        ease_quad 3.0 offset (-60, -620) zoom 0.55

    show her_sex_personal mouth_angry eyes_wide_r eyebrows_base cheeks_blush tears_soft as cg

    play background "sounds/sexloopveryfast.ogg"
    nar "You push Hermione down onto the desk... Pumping your cock deep inside her ass, your pelvis smacks loudly against her cheeks."

    show her_sex_personal mouth_mad eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
    her "*Ah-hah*...{w=0.3} So deep..."
    show her_sex_personal mouth_angry eyes_narrow_stare eyebrows_worried cheeks_blush tears_soft as cg
    her "{size=+7}I'm--{w=0.3} I'm cumming [name_genie_hermione]!!!{/size}"
    gen "{size=+7}Me too!{/size}"

    menu:
        gen "!!!"
        "-Fill her up-":
            $ states.her.status.anal_creampie = True

            show her_sex_personal cum_inside as cg

            gen "{size=+7}TAKE THIS, WHORE!!!{/size}"

            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal cum_pussy_light mouth_grin eyes_narrow_stare eyebrows_base cheeks_blush tears_soft as cg
            her "!!!"

            gen "{size=+15}Yes! *Argh*!{/size}"

            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal mouth_angry eyes_narrow_up eyebrows_annoyed cheeks_blush tears_soft as cg
            her "*Ah*!{heart} It's filling me up!{heart} I can feel it!{heart}"

            gen "{size=+15}Shut up, whore!{/size}"
            show her_sex_personal mouth_crooked_smile eyes_narrow_mid eyebrows_base cheeks_blush tears_soft as cg
            her "{size=+7}*Ah*! I AM A WHORE!!!!{heart}{heart}{heart}{/size}"
            gen "{size=+15}*Argh*!{/size}"

            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal cum_pussy_heavy mouth_angry eyes_happycl eyebrows_base cheeks_blush as cg

            pause 1

            show her_sex_personal mouth_base eyes_narrow_r eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*...{heart}{w=0.3} your cum, [name_genie_hermione]...{heart}"
            gen "*Ah*...{w=0.3} Yes..."
            show her_sex_personal mouth_base eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*...{w=0.3}{heart}"
            gen "Well... Suppose it's time for you to get your points..."

            play sound "sounds/slick_02.ogg"

            if _temp_outfit_choice == "naked":
                show her_sex_personal after cum_ass_light mouth_grin eyes_narrow_up eyebrows_base cheeks_blush tears_soft as cg
            else:
                show her_sex_personal after cum_ass_skirt_light mouth_grin eyes_narrow_up eyebrows_base cheeks_blush tears_soft as cg
            with kissiris

            her "{heart}*Ngh*!{heart}"

            show screen blkfade
            with d5

            nar "You step back and give Hermione's ass a last glance, her asshole still convulses slightly as your cum continues to dribble onto the ground."
            nar "After a couple of moments, she pushes herself up, off your desk..."
            nar "Before making her way to the front of your desk, you notice her prodding her butthole gently."
            nar "You swear you see a slight smile across her face for a brief moment, but before you know it, she has already readied herself and made her way to the front of your desk."

        "-Cum all over her-":
            show her_sex_personal cum_outside2 as cg


            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            gen "{size=+7}*Argh*!!!{/size}"
            show her_sex_personal mouth_mad eyes_narrow_r eyebrows_worried cheeks_blush tears_soft as cg


            show her_sex_personal cum_outside as cg
            call cum_block

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_outside cum_ass_light mouth_grin eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            else:
                show her_sex_personal cum_outside cum_ass_skirt_light mouth_grin eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg

            play sound "sounds/slick_02.ogg"
            her "*Ah-aha*! You're cumming! {heart}{heart}{heart}"

            show her_sex_personal after as cg

            gen "{size=+7}Yes I am, whore!{/size}"
            show her_sex_personal mouth_crooked_smile eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*, me too!"
            gen "{size=+7}FUCKING SLUT!{/size}"

            show her_sex_personal mouth_crooked_smile eyes_narrow_stare eyebrows_base cheeks_blush tears_soft as cg
            her "*Ah*...{heart} your cum...{heart}"
            show her_sex_personal mouth_grin eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "It's all over--{heart}{heart}{heart}"

            if _temp_outfit_choice == "naked":
                gen "{size=+7}Yes!!! All over your ass!{/size}"
            else:
                gen "{size=+7}Yes!!! All over your clothes!{/size}."

            show her_sex_personal mouth_grin eyes_narrow_r eyebrows_worried cheeks_blush as cg

            call cum_block

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_outside cum_ass_heavy mouth_grin eyes_narrow_mid eyebrows_worried cheeks_blush as cg
            else:
                show her_sex_personal cum_outside cum_ass_skirt_heavy mouth_grin eyes_narrow_mid eyebrows_worried cheeks_blush as cg

            play sound "sounds/slick_02.ogg"
            show her_sex_personal mouth_grin eyes_narrow_mid eyebrows_worried cheeks_blush as cg

            show her_sex_personal after as cg
            call ctc

            show her_sex_personal mouth_grin eyes_narrow_down eyebrows_worried cheeks_blush as cg
            her "{heart}{heart}*Mmm*...{heart}{heart}"
            gen "Well, this was intense..."
            show her_sex_personal mouth_crooked_smile eyes_narrow_down eyebrows_base cheeks_blush tears_soft as cg
            her "*Ah-ha*...{heart} *Ah*...{heart}"
            gen "Are You alright, [name_hermione_genie]?"
            show her_sex_personal mouth_grin eyes_narrow_stare eyebrows_base cheeks_blush tears_soft as cg
            her "I think so...{w=0.3} I'm not sure..."
            show her_sex_personal mouth_base eyes_narrow_r eyebrows_base cheeks_blush tears_soft as cg
            her "I think I may still be cumming, [name_genie_hermione]."
            show her_sex_personal mouth_grin eyes_narrow_mid eyebrows_worried cheeks_blush tears_soft as cg
            her "Or maybe not..."
            show her_sex_personal mouth_grin eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "Everything is in a daze...{w=0.3} And my legs feel so weak..."
            if game.daytime:
                gen "Well you better get on your feet, so you can receive your payment, [name_hermione_genie]... You've still got lessons to get to."
            else:
                gen "Then I better get to awarding you your points, so you can get some rest..."
            show her_sex_personal mouth_grin eyes_narrow_r eyebrows_worried cheeks_blush tears_soft as cg
            her "Oh...{w=0.3} Of course [name_genie_hermione]..."

            show screen blkfade
            with d5

            nar "You step back and watch as Hermione tries her best to steady herself."
            nar "After finally getting up, she touches her ass and you swear you see her smile for a brief moment."
            nar "She then readies herself and makes her way to the front of your desk."

    jump end_hg_pf_sex

### Anal Sex Repeat ###

label hg_anal_sex_3:

    $ states.her.status.anal = True
    $ current_payout = 90

    ### Will be added with Missionary pose ###
    #gen "Let's see... How shall we do this..."
    #her "[name_genie_hermione]?"
    #menu:
        #"-Flip her onto the desk-":
            #jump hg_sex_missionary_anal
        #"-Take her from behind-":
            #pass

    ##Doggystyle Anal scene setup##

    show screen blkfade
    with d5
    pause.2

    #Stop wind and thunder sounds
    stop weather fadeout 4

    if _temp_outfit_choice == "naked":
        show her_sex_personal lean_back hold mouth_base eyes_narrow_r eyebrows_base as cg zorder 17:
            transform_anchor True
            anchor (0.0, 0.0)
            offset (-500, -650)
            rotate (15)
            zoom 1.0
    else:
        show her_sex_personal lean_back hold shirt skirt mouth_base eyes_narrow_r eyebrows_base as cg zorder 17:
            transform_anchor True
            anchor (0.0, 0.0)
            offset (-500, -650)
            rotate (15)
            zoom 1.0

    hide screen blkfade
    with d5

    her "..........."

    show her_sex_personal lean_back as cg:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0
        ease_quad 3.0 offset (-230, -100) zoom 0.5 rotate -15

    gen "Let's see now..."
    nar "You align your cock and place it against Hermione's Butthole."
    menu:
        "-Ask her if she's ready-":
            gen "Ready?"
            show her_sex_personal mouth_soft eyes_narrow_r eyebrows_base as cg
            her "As I'll ever--"
        "-Less talking, more fucking-":
            pass

    play sound "sounds/gltch.ogg"
    with kissiris

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    show her_sex_personal mouth_grin eyes_wide_up eyebrows_base as cg
    her "*Ooooohhhhhhhhhhhh*....{heart}"

    show her_sex_personal hold_grin as cg
    gen "*Ah*...{w=0.4} Finally!"

    show her_sex_personal mouth_grin eyes_narrow_mid eyebrows_base cheeks_blush as cg
    her "*Mmm*..."

    play background "sounds/slickloop.ogg" fadein 2
    call ctc

    show her_sex_personal mouth_soft eyes_narrow_mid eyebrows_worried cheeks_blush as cg
    her "*Ah*..."

    show her_sex_personal hold as cg
    gen "*Hmm*... This does feel a lot easier than before, you haven't pre-lubed your butthole have you [name_hermione_genie]?"

    show her_sex_personal mouth_angry eyes_narrow_down eyebrows_base cheeks_blush as cg
    her "*Ah*...{w=0.4} *Ehm*..."

    show her_sex_personal hold_grin as cg
    gen "I knew it...{w=0.4} You've been expecting this..."
    gen "So eager to take your headmasters cock, you had to lube yourself before even entering my office."

    show her_sex_personal hold as cg
    gen "So, where is it? I didn't see you bring it in."

    show her_sex_personal mouth_soft eyes_narrow_mid eyebrows_base cheeks_blush as cg
    her "*Ah*...{w=0.4} *Ah*...{w=0.4} I--{w=0.2} I left it outside your door [name_genie_hermione]..."
    gen "You don't say..."
    gen "Aren't you worried what people might think if they saw a bottle of lube out there?"
    show her_sex_personal mouth_soft eyes_closed eyebrows_base cheeks_blush as cg
    her "*Ah*...{w=0.4} *Ah*...{w=0.4} No, [name_genie_hermione]..."
    show her_sex_personal mouth_open eyes_narrow_mid eyebrows_worried cheeks_blush as cg
    her "They--{w=0.2} *Ah*...{w=0.4} They would probably hear my--{w=0.4} *Ah*...{w=0.2} moaning through the door anyway, so why--{w=0.2} *Ah*...{w=0.4} Why even bother..."

    menu:
        "-Chastise her-":
            gen "So, you don't care at all?"
            show her_sex_personal mouth_base eyes_narrow_down eyebrows_base cheeks_blush as cg
            her "*Ah*...{w=0.4} I don't, [name_genie_hermione]..."
            gen "What if one of your Gryffindor friends suddenly turned up outside my door?"
            show her_sex_personal mouth_open eyes_narrow_r eyebrows_worried cheeks_blush as cg
            her "They--{w=0.2} *Ah*...{w=0.4} They wouldn't..."
            gen "Are you sure? I mean, it's not like the door is locked or anything..."
            gen "Anyone could walk in here!"
            if game.daytime:
                random:
                    block:
                        show her_sex_personal mouth_soft eyes_narrow_down eyebrows_base cheeks_blush as cg
                        her "*Ah*...{w=0.4} I'm sure they're still having lunch right now..."
                    block:
                        show her_sex_personal mouth_soft eyes_narrow_down eyebrows_base cheeks_blush as cg
                        her "*Ah*...{w=0.4} They should be in the library studying at the moment..."
                    block:
                        show her_sex_personal mouth_soft eyes_narrow_down eyebrows_base cheeks_blush as cg
                        her "*Ah*...{w=0.4} They're probably still busy playing Gobstones..."
            else:
                show her_sex_personal mouth_soft eyes_narrow_down eyebrows_base cheeks_blush as cg
                her "*Ah*...{w=0.4} They should still be in the common room..."

            gen "What if I told you that I requested them to be here?"
            show her_sex_personal mouth_clench eyes_happy_r eyebrows_base cheeks_blush as cg
            her "*Ah*...{w=0.4} You...{w=0.4} You wouldn't..."
            gen "Don't you think it's about time they saw exactly what lengths you've gone through to help your house?"
            show her_sex_personal mouth_angry eyes_happy_mid eyebrows_annoyed cheeks_blush as cg
            her "*Ah*...{w=0.3} [name_genie_hermione]...{w=0.3} I told you...{w=0.3} They can't--"
            gen "I bet you'd like nothing more than one of your friends walking through that door to see you taking my dick up your ass..."
            show her_sex_personal mouth_clench eyes_happycl eyebrows_base cheeks_blush as cg
            her "Please [name_genie_hermione]... Don't tell me you've--"

            play background "sounds/sexloopfast.ogg"

            nar "You start fucking Hermione's asshole with renewed determination."
            nar "Her pleads are soon drowned out by the slapping of her cheeks as you push your cock deep inside her with every stroke."
            show her_sex_personal mouth_open eyes_happycl eyebrows_annoyed cheeks_blush as cg
            her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
            gen "Although... With how loud you're moaning, I'd be surprised if I'd even need to call them up here..."
            show her_sex_personal mouth_open eyes_happycl eyebrows_annoyed cheeks_blush as cg
            her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
            gen "I bet the entire castle can hear your moans and cheeks slapping..."
            show her_sex_personal mouth_angry eyes_happycl eyebrows_worried cheeks_blush as cg
            her "*Ah*...{w=0.2} *Ah*...{w=0.2} They--{w=0.2} *Ah*...{w=0.4} They wouldn't...."
            gen "Do you think they'd recognize the sound of your voice, [name_hermione_genie]?"
            show her_sex_personal mouth_upset eyes_happycl eyebrows_worried cheeks_blush as cg
            her "*Ah*...{w=0.4} Of course they--"
            gen "Of course they would..."
            gen "With how wet you've been lately..."
            gen "There's no doubt you've been touching yourself in class..."
            show her_sex_personal mouth_angry eyes_closed eyebrows_worried cheeks_blush as cg
            her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*...{w=0.2}"
            gen "And that bottle of lube you brought with you... Did you bring that with you to class as well?"
            show her_sex_personal mouth_angry eyes_closed eyebrows_annoyed cheeks_blush as cg
            her "*Ah*...{w=0.4} *Ah*...{w=0.4} I..."
            gen "What else have you brought to class lately?"
            menu:
                "\"A butt-plug?\"":
                    show her_sex_personal mouth_clench eyes_narrow_down eyebrows_base cheeks_blush as cg
                    her "A... A Butt-plug?!"
                "\"Anal beads?\"":
                    show her_sex_personal mouth_clench eyes_narrow_down eyebrows_base cheeks_blush as cg
                    her "A-- Anal beads?!"
            show her_sex_personal mouth_disgust eyes_narrow_r eyebrows_base cheeks_blush as cg
            her "Of course I haven't!"
            gen "*Hmm*...{w=0.4} Could've fooled me [name_hermione_genie]...{w=0.4} You don't normally get used to taking it in the ass this easily..."
            show her_sex_personal mouth_upset eyes_narrow_l eyebrows_worried cheeks_blush as cg
            her "*Hmph*..."
            show her_sex_personal mouth_open eyes_narrow_l eyebrows_worried cheeks_blush as cg
            her "I suppose I'm just a natural..."
            gen "Clearly..."
            gen "Well then, let's put that to the test, shall we!"

        "-Reward her bravery-":
            gen "I suppose you wouldn't mind me going all out on you then..."
            gen "After all, it's not like you'd be able to moan loud enough for anyone to hear you through the window..."
            show her_sex_personal mouth_open eyes_closed eyebrows_base cheeks_blush as cg
            her "*Ah*...{w=0.2} Of course...{w=0.4} Go ahead, [name_genie_hermione]..."

            play background "sounds/slickloopfast.ogg"

            nar "You start fucking Hermione with renewed determination."
            nar "Noticing Hermione trying to stifle her moans, you push your cock deep inside her ass, and with each insertion, your body smacks hard against her cheeks."

            play background "sounds/sexloopfast.ogg"

            show her_sex_personal mouth_disgust eyes_happycl eyebrows_worried cheeks_blush as cg
            her "*Ah*...{w=0.2} *Ah*...{w=0.2} [name_genie_hermione]..."
            gen "That's it [name_hermione_genie]..."
            gen "Don't be afraid to show how much you're enjoying this..."
            show her_sex_personal mouth_open eyes_happycl eyebrows_base cheeks_blush as cg
            her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."

            nar "Hermione begins moaning even louder as her previous worries slowly fades away and turn into pleasure."

            call slap_her

            show her_sex_personal mouth_grin eyes_narrow_up eyebrows_base cheeks_blush as cg
            her "*Ah*..."
            gen "*Hmm*... Surely, we can do better than that..."

            call slap_her

            show her_sex_personal mouth_grin eyes_happy_up eyebrows_base cheeks_blush as cg
            her "{size=+2}*Ah*!{/size}"
            gen "That's better..."

            call slap_her
            call slap_her
            call slap_her

            show her_sex_personal mouth_open_tongue eyes_narrow_up eyebrows_base cheeks_blush as cg
            her "{size=+5}*Ah*!!!{/size}"

            gen "There it is!"
            gen "Well... I suppose you were right [name_hermione_genie]..."

            call slap_her

            show her_sex_personal mouth_grin eyes_happycl eyebrows_base cheeks_blush as cg
            her "{size=+2}*Ah*!{/size}"

            gen "If anyone had heard you we'd probably know by now..."
            show her_sex_personal mouth_open eyes_happycl eyebrows_base cheeks_blush as cg
            her "I..."
            gen "Although maybe I haven't gone all out on you yet..."
            show her_sex_personal mouth_soft eyes_narrow_mid eyebrows_base cheeks_blush as cg
            her "*Ah*... Surely, you must have..."
            gen "Well, you're about to find out!"

    show her_sex_personal bent_over grab as cg:
        offset (-230, -100)
        zoom 0.5
        rotate -15
        easein 1.0 offset (0, -480) rotate 0
    with vpunch

    pause 1.0

    #Could add some sound effect here
    show her_sex_personal mouth_open eyebrows_base eyes_wide_r cheeks_blush as cg:
        offset (0, -480)
        rotate 0
        ease_quad 3.0 offset (-60, -620) zoom 0.55

    show her_sex_personal mouth_grin eyes_narrow_r eyebrows_base cheeks_blush as cg


    play background "sounds/sexloopveryfast.ogg"
    nar "You push Hermione down onto the desk and begin fucking her asshole rapidly..."
    show her_sex_personal mouth_soft eyes_narrow_up eyebrows_base cheeks_blush as cg
    her "*Ah*...{w=0.3} [name_genie_hermione]!"
    show her_sex_personal mouth_grin eyes_narrow_up eyebrows_base cheeks_blush as cg
    her "You're...{w=0.3} You're gonna break me!"
    gen "I've already broken you, [name_hermione_genie]!"
    gen "Every time I've called you to my office you arrive here without a moment of hesitation."
    show her_sex_personal mouth_grin eyes_happycl eyebrows_base cheeks_blush as cg
    her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
    gen "Even after the things I've done to you...{w=0.3} You can't wait to get back in here and do it again..."
    gen "To suck your headmaster's cock as if your life depended on it..."
    show her_sex_personal mouth_grin eyes_narrow_mid eyebrows_base cheeks_blush as cg
    her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
    gen "Have him fuck you so hard that you can't help but yell out in pleasure..."
    show her_sex_personal mouth_grin eyes_narrow_up eyebrows_base cheeks_blush as cg
    her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
    gen "Take his dick so far up your ass that you can barely keep any rational thoughts in your head."
    nar "Hermione clenches her ass around your cock as you keep berating her."
    gen "And you can't even pretend that you're not enjoying it anymore..."
    gen "Every time I call you a slut--"
    with vpunch
    show her_sex_personal mouth_crooked_smile eyes_narrow_up eyebrows_base cheeks_blush as cg
    her "*Ngh*..."
    gen "Or a whore..."
    with vpunch
    show her_sex_personal mouth_grin eyes_narrow_up eyebrows_worried cheeks_blush as cg
    her "*Ngh*..."
    gen "I can feel your body twitch in excitement."
    gen "Is that the only thing you want now? To be nothing but a cum dumpster for your headmaster?"
    show her_sex_personal mouth_angry eyes_narrow_mid eyebrows_base cheeks_blush as cg
    her "..."
    gen "To just come in here the moment I call for you..."
    gen "With the only purpose of squeezing out as much semen as you can."
    show her_sex_personal mouth_angry eyes_narrow_down eyebrows_base cheeks_blush as cg
    her "I..."
    gen "To have me fill your ass until you can't walk... Or cover you in it just so you can smell it during class..."
    gen "You should be ashamed of yourself!"
    show her_sex_personal mouth_angry eyes_base_mid eyebrows_base cheeks_blush as cg
    her "I--"
    gen "Admit it!"
    show her_sex_personal mouth_angry eyes_happycl eyebrows_base cheeks_blush as cg
    her "{size=+5}I'm cumming [name_genie_hermione]!{/size}"
    gen "Oh, no you don't!"

    call slap_her
    pause .3

    play sound "sounds/slick_01.ogg"
    with kissiris
    show her_sex_personal mouth_grin eyes_narrow_up eyebrows_base cheeks_blush as cg
    her "{size=+2}*Ah*!{/size}"

    call slap_her
    call slap_her
    pause .3

    play sound "sounds/slick_01.ogg"
    with kissiris
    show her_sex_personal mouth_soft eyes_narrow_mid eyebrows_base cheeks_blush as cg
    her "{size=+2}*Mmm*!{/size}"

    gen "You slut! Now take what you came for!"

    menu:
        "-Fill that greedy hole!-":
            $ states.her.status.anal_creampie = True

            show her_sex_personal cum_inside as cg

            gen "{size=+7}TAKE my cum!!!{/size}"

            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal cum_pussy_light mouth_grin eyes_narrow_mid eyebrows_base cheeks_blush tears_soft as cg
            her "!!!"

            gen "{size=+15}Yes! *Argh*!{/size}"

            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal mouth_angry eyes_narrow_up eyebrows_annoyed cheeks_blush tears_soft as cg
            her "*Ah*!{heart} Yes!{heart} Fill my tight little ass, [name_genie_hermione]!{heart}"

            gen "{size=+15}Argh! Yes!{/size}"
            show her_sex_personal mouth_crooked_smile eyes_narrow_mid eyebrows_base cheeks_blush tears_soft as cg
            her "{size=+7}*Ah*! Fill your cum dumpster!!!!{heart}{heart}{heart}{/size}"
            gen "{size=+15}*Argh*!{/size}"

            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal cum_pussy_heavy mouth_angry eyes_happycl eyebrows_base cheeks_blush as cg

            pause 1

            show her_sex_personal mouth_grin eyes_narrow_r eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*...{heart}{w=0.3} My ass is so full...{heart}"
            gen "*Ah*...{w=0.3} And you better keep it in there, slut."
            show her_sex_personal mouth_base eyes_narrow_down eyebrows_worried cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3} *Ah*...{w=0.3} yes [name_genie_hermione]...{heart}"
            gen "*Hmm*... I think it's time for you to receive your points [name_hermione_genie]..."

            play sound "sounds/slick_02.ogg"

            if _temp_outfit_choice == "naked":
                show her_sex_personal after cum_ass_light mouth_grin eyes_narrow_up eyebrows_base cheeks_blush tears_soft as cg
            else:
                show her_sex_personal after cum_ass_skirt_light mouth_grin eyes_narrow_up eyebrows_base cheeks_blush tears_soft as cg
            with kissiris

            her "{heart}*Ngh*!{heart}"

            show screen blkfade
            with d5

            nar "You step back and watch as your cum starts leaking out of Hermione's ass before she clenches her cheeks to keep it inside of her."
            nar "She then gets off your desk and readies herself, and then makes her way to the front of your desk."
            nar "You notice that her walk is slightly more purposeful than usual as she does her best to keep your cum from leaking out."

        "-Coat her with your cum!-":
            show her_sex_personal cum_outside2 as cg


            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            gen "{size=+7}*Argh*!!!{/size}"
            show her_sex_personal mouth_mad eyes_narrow_r eyebrows_worried cheeks_blush as cg


            show her_sex_personal cum_outside as cg
            call cum_block

            if _temp_outfit_choice == "naked":
                show her_sex_personal after cum_ass_light mouth_grin eyes_narrow_down eyebrows_base cheeks_blush as cg
            else:
                show her_sex_personal after cum_ass_skirt_light mouth_grin eyes_narrow_down eyebrows_base cheeks_blush as cg

            play sound "sounds/slick_02.ogg"
            her "*Ah-aha*! Yes [name_genie_hermione] cover me in cum! {heart}{heart}{heart}"

            gen "{size=+7}You greedy slut!{/size}"
            show her_sex_personal mouth_crooked_smile eyes_narrow_mid eyebrows_worried cheeks_blush as cg
            her "*Ah*, Yes!"

            show her_sex_personal mouth_crooked_smile eyes_narrow_stare eyebrows_base cheeks_blush as cg
            her "*Ah*...{heart} your cum...{heart}"
            show her_sex_personal mouth_grin eyes_narrow_down eyebrows_base cheeks_blush as cg
            her "I can smell it--{heart}{heart}{heart}"

            if _temp_outfit_choice == "naked":
                gen "{size=+7}Yes!!! All over your ass!{/size}"
            else:
                gen "{size=+7}Yes!!! All over your clothes!{/size}."

            show her_sex_personal mouth_grin eyes_narrow_r eyebrows_worried cheeks_blush as cg


            show her_sex_personal cum_outside as cg
            call cum_block

            if _temp_outfit_choice == "naked":
                show her_sex_personal after cum_ass_heavy mouth_grin eyes_narrow_mid eyebrows_worried cheeks_blush as cg
            else:
                show her_sex_personal after cum_ass_skirt_heavy mouth_grin eyes_narrow_mid eyebrows_worried cheeks_blush as cg

            play sound "sounds/slick_02.ogg"
            call ctc

            show her_sex_personal mouth_soft eyes_closed eyebrows_worried cheeks_blush as cg
            her "{heart}{heart}*Mmm*...{heart}{heart}"
            gen "That's it, every last drop..."
            show her_sex_personal mouth_crooked_smile eyes_narrow_down eyebrows_base cheeks_blush as cg
            her "*Ah-ha*...{heart} *Ah*...{heart}"
            show her_sex_personal mouth_grin eyes_narrow_stare eyebrows_base cheeks_blush as cg
            her "Every...{w=0.4} Last..."
            show her_sex_personal mouth_base eyes_narrow_mid eyebrows_base cheeks_blush as cg
            her "*Mmm*..."
            gen "[name_hermione_genie]?"
            show her_sex_personal mouth_base eyes_narrow_down eyebrows_base cheeks_blush as cg
            her "..."
            if game.daytime:
                gen "You've got classes to get to..."
            else:
                gen "*Err*... Perhaps you should go get some rest..."
            show her_sex_personal mouth_soft eyes_narrow_down eyebrows_worried cheeks_blush as cg
            her "Oh...{w=0.3} Of course [name_genie_hermione]..."
            show her_sex_personal mouth_base eyes_narrow_mid eyebrows_worried cheeks_blush as cg
            her "Just give me a moment..."

            show screen blkfade
            with d5

            nar "Hermione lies on your desk for a moment before finally pushing herself up."
            nar "You watch as she sneakily tries to brush some of your cum off with her finger and lick it off."
            nar "Noticing that you were looking, she then readies herself and hurriedly makes her way to the front of your desk."

    jump end_hg_pf_sex
