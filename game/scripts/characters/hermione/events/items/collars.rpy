

### Hermione Collar Event ###

label hg_collars:

    # Setup
    $ her_outfit_last.save() #Saves current clothing

    if hermione.is_worn("robe"):
        gen "Before I show you what we're doing today... Why don't you take those robes off and make yourself comfortable." ("base", xpos="far_left", ypos="head")
        her "Alright..." ("soft", "squint", "base", "mid")
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")
        with d3
        gen "Now then..." ("base", xpos="far_left", ypos="head")

    if hermione.is_worn("top"):
        gen "I've got something for you to put on..." ("base", xpos="far_left", ypos="head")
        her "Right..." ("open", "happy", "base", "mid")
        gen "But first, I'll need you to remove your top, or it might get caught in your clothing." ("base", xpos="far_left", ypos="head")

        if states.her.tier == 1:
            if states.her.status.show_bra or states.her.status.show_panties:
                her "You want me to remove my top?" ("soft", "happy", "worried", "R")
                gen "Yes please..." ("base", xpos="far_left", ypos="head")
                her "I'm getting paid for this, right?" ("open", "narrow", "base", "down")
                gen "Of course." ("base", xpos="far_left", ypos="head")
                her "Fine..." ("open", "closed", "base", "mid")

                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("top")
                pause .5

                her "Alright then... Now what?" ("soft", "narrow", "base", "R")
            else: #FAIL
                her "My top?" ("angry", "wide", "base", "mid")
                gen "Yes, your top... Is that going to be a problem?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "W-- Why do you need me to remove it?" ("clench", "narrow", "base", "down")
                gen "It's just phase one of today's favour..." ("base", xpos="far_left", ypos="head")
                her "Phase one... What's phase two?" ("angry", "squint", "base", "mid")
                gen "You'll see once you've taken that top off." ("base", xpos="far_left", ypos="head")
                her "..." ("disgust", "narrow", "base", "mid")
                her "No, I'm sorry [name_genie_hermione]... But I don't think I will." ("annoyed", "narrow", "base", "R")
                gen "(Damn... Maybe I should get her more used to taking her top off before doing this...)" ("base", xpos="far_left", ypos="head")

                jump hermione_requests

        elif states.her.tier == 2:
            her "*Hmm*... Alright... As long as you're paying me..." ("annoyed", "happy", "base", "R")
            gen "Of course..." ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("top")
            pause .5

            her "There...{w=0.4} Happy?" ("open", "closed", "base", "mid")

            gen "Very." ("base", xpos="far_left", ypos="head")
            gen "Now..." ("base", xpos="far_left", ypos="head")

        elif states.her.tier == 3:
            her "My top?" ("soft", "squint", "base", "mid")
            gen "Yes... It is vitally important for this to succeed." ("base", xpos="far_left", ypos="head")
            her "What are we doing?" ("angry", "squint", "base", "mid")
            gen "You'll see..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*..." ("annoyed", "base", "base", "R")
            her "Alright... As long as you're paying me..." ("open", "closed", "base", "mid")
            gen "Of course..." ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("top")
            pause .5

            gen "Great... So..." ("base", xpos="far_left", ypos="head")

        else:
            her "Alright..." ("base", "squint", "base", "mid")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("top")
            pause .5

            gen "Excellent... Now..." ("base", xpos="far_left", ypos="head")

    # Remove (one) collar from the inventory
    $ collar_ITEM.owned -= 1

    if not states.her.ev.magic_collar.worn:
        $ states.her.ev.magic_collar.worn = True

        gen "I've got this collar that I'd like you to wear." ("base", xpos="far_left", ypos="head")
        her "A collar?" ("open", "happy", "base", "mid")
        her "What kind of collar is it?" ("angry", "narrow", "base", "mid")
        gen "What do you mean? It's just a normal collar!" ("base", xpos="far_left", ypos="head")
        her "..." ("normal", "narrow", "base", "mid")
        gen "Alright... It's a magic collar." ("base", xpos="far_left", ypos="head")
        her "Of course it is..." ("open", "narrow", "base", "R")
        her "So, what does it do then?" ("open", "closed", "base", "mid")
        gen "It will permanently transform itself to show you your true self!" ("base", xpos="far_left", ypos="head")

        if states.her.level < 4:
            her "My true self?" ("soft", "squint", "base", "mid")
            gen "Yep..." ("base", xpos="far_left", ypos="head")
            her "So, like fortune-telling?" ("open", "narrow", "base", "mid")
            gen "More like present-telling." ("base", xpos="far_left", ypos="head")
            her "Sounds silly... But alright then." ("soft", "narrow", "base", "R")
            her "How much am I being paid for this?" ("open", "narrow", "base", "mid")
            gen "Let's say thirty points..." ("base", xpos="far_left", ypos="head")
            her "Thirty points to put on a collar?" ("open", "base", "base", "stare")
            gen "Yep..." ("base", xpos="far_left", ypos="head")

            her "Okay then... I didn't think earning points were going to be this easy but go ahead." ("grin", "closed", "base", "mid")
            her "Put it on me and tell me what it says!" ("smile", "base", "base", "mid")

            $ current_payout = 30

        elif states.her.level < 10:
            her "My true self?" ("soft", "base", "worried", "R")
            gen "Exactly..." ("base", xpos="far_left", ypos="head")
            her "I see..." ("open", "narrow", "worried", "R")
            gen "You're not worried what it might say, are you?" ("base", xpos="far_left", ypos="head")
            her "Of course not!" ("soft", "closed", "annoyed", "mid")
            her "Although..." ("disgust", "happy", "base", "R")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            her "I want Thirty points for this..." ("open", "closed", "base", "mid")
            gen "*Hmm*... Just to put on a magic collar?" ("base", xpos="far_left", ypos="head")
            gen "And here I thought you weren't worried about it..." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "base", "R")
            gen "Very well, [name_hermione_genie]... Thirty points, it is." ("base", xpos="far_left", ypos="head")

            $ current_payout = 30

        elif states.her.level < 13: #stripped
            her "As if... You've probably just made it say \"pervert\" or something like that to mess with me..." ("clench", "narrow", "base", "R")
            gen "Pervert? As if I'd ever do something like that." ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "annoyed", "mid")
            gen "Okay, maybe I would..." ("base", xpos="far_left", ypos="head")
            gen "But I can assure you, I've done nothing of the sort." ("base", xpos="far_left", ypos="head")
            her "*Hmm*..." ("annoyed", "narrow", "base", "R")
            her "In that case... I want twenty points." ("open", "closed", "annoyed", "mid")
            gen "Twenty points it is..." ("base", xpos="far_left", ypos="head")

            $ current_payout = 20

        elif states.her.level < 19: #Handjob
            her @ cheeks blush "What's that supposed to mean?" ("angry", "happy", "base", "mid")
            gen "You know..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "No... I don't." ("angry", "narrow", "base", "mid")
            her @ cheeks blush "Please enlighten me." ("soft", "narrow", "annoyed", "mid")
            gen "Why don't I just put in on you, and we can find out for ourselves?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I--{w=0.4} I don't want to!" ("angry", "closed", "worried", "mid")
            gen "Worried it might say something you don't like?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course not!" ("soft", "squint", "worried", "R")
            her @ cheeks blush "I'd just think I should get paid to put up with your shenanigans!" ("angry", "closed", "worried", "mid")
            gen "That's fair... But since it's just shenanigans after all... Ten point should be enough, should it not?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "narrow", "base", "down")
            gen "Go on then, it's just a silly little collar." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Fine, ten points it is..." ("open", "closed", "worried", "mid")

            $ current_payout = 10

        elif states.her.level < 22: #BJ
            her "I'm sure we'll both know what it's going to say..." ("disgust", "narrow", "base", "R")
            gen "Yeah?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Come on, sir..." ("disgust", "narrow", "base", "mid")
            her @ cheeks blush "I've taken my clothes off in this office..." ("angry", "closed", "base", "mid")
            her @ cheeks blush "I'm sure you've made it say something to try and degrade me..." ("open", "narrow", "annoyed", "R")
            gen "Of course not, this collar tells no lies!" ("base", xpos="far_left", ypos="head")
            gen "I'm sure it'll call you a hero thanks to the number of points you've earned for your house." ("base", xpos="far_left", ypos="head")
            gen "That's what you're doing this for after all, this collar will merely confirm it." ("base", xpos="far_left", ypos="head")
            her "Well, if that's the case... I suppose since I can't tell anyone about all this, it would at least be nice to know for sure..." ("open", "closed", "base", "mid")

        elif states.her.level < 25: #Sex (24=max)
            her @ cheeks blush "My true self is it?" ("base", "narrow", "base", "R")
            gen "Yep!" ("base", xpos="far_left", ypos="head")
            gen "Now you finally won't have to take my word on how much of a slut you are." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Sir!" ("angry", "base", "base", "mid")
            gen "Come on, it'll be fun!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I-- I don't know about this..." ("angry", "narrow", "base", "down")
            gen "Don't be silly... Here, Let me just put this around your neck..." ("base", xpos="far_left", ypos="head")

    else:
        gen "I've got my hands on another magic collar for you." ("base", xpos="far_left", ypos="head")
        her "Another one?" ("open", "happy", "base", "mid")
        gen "Yes, I have the feeling something might've changed, so I thought we could try another one." ("base", xpos="far_left", ypos="head")

        if states.her.level < 4:
            her "*Hmm*... Well, I doubt it..." ("normal", "base", "base", "R")
            her "Will I get another thirty points?" ("soft", "base", "base", "mid")
            gen "Of course." ("base", xpos="far_left", ypos="head")
            her "Okay, then why not..." ("base", "closed", "base", "mid")

            $ current_payout = 30

        elif states.her.level < 10:
            her @ cheeks blush "I'm sure it'll just say the same thing as before..." ("open", "closed", "base", "mid")
            gen "Well, I wouldn't be so sure if I were you..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ahem*... Although I wouldn't mind some points." ("open", "happy", "base", "R")
            gen "Figured..." ("base", xpos="far_left", ypos="head")
            gen "Alright then, Miss Granger..." ("base", xpos="far_left", ypos="head")
            gen "How does thirty points sound to you?" ("base", xpos="far_left", ypos="head")
            her "Acceptable..." ("open", "closed", "base", "mid")

            $ current_payout = 30

        elif states.her.level < 13: #stripped
            her @ cheeks blush "I want twenty points!" ("angry", "closed", "base", "mid")
            gen "Worried it might show something different this time?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "No, I just think it's a waste of time if I went all the way here not to get anything for it." ("open", "happy", "base", "R")
            gen "I suppose that's true..." ("base", xpos="far_left", ypos="head")
            gen "Very well, twenty points it is." ("base", xpos="far_left", ypos="head")

            $ current_payout = 20

        elif states.her.level < 19: #Handjob
            her @ cheeks blush "Well of course you'd think that..." ("open", "narrow", "base", "R")
            her @ cheeks blush "I want ten points for this..." ("soft", "happy", "base", "mid")
            gen "Of course..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Good... Then put it on me and let's get this over with..." ("disgust", "closed", "base", "mid") #bit worried

            $ current_payout = 10

        elif states.her.level < 22: #BJ
            her "Well... Seeing the things I've done in here, I'm sure it can't be good..." ("disgust", "narrow", "base", "R")
            gen "I'm sure it will recognize why you're doing all this." ("base", xpos="far_left", ypos="head")
            her "*Hmm*..." ("annoyed", "narrow", "base", "R") #worried

        elif states.her.level < 25: #Sex (24=max)
            gen "I want to see exactly how much of a slut you are in writing." ("base", xpos="far_left", ypos="head")
            her "Sir!" ("annoyed", "narrow", "worried", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            her "How could you say such a thing?" ("soft", "narrow", "worried", "mid")
            gen "The collar don't lie... Just let me put it on you and we'll see it for ourselves." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "worried", "R")

    gen "Let's see now..." ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand", 210, "base")
    with d3
    call gen_walk(path=[(230, 470), (380, 470), (420, 430)])

    pause 0.5

    play sound "sounds/collar_click.ogg"
    $ hermione.equip(her_neckwear_basic_collar)
    gen "There we go..." ("base", xpos="far_left", ypos="head")

    call gen_walk(path=[(420, 430), (380, 470), (230, 470), (200, 430)])
    call gen_chibi(flip=True)
    with d3
    pause 0.5
    call gen_chibi("sit_behind_desk")
    with d3

    if states.her.level < 10:
        her "Alright then... What does it say?" ("base", "base", "base", "mid") #confident
        gen "Hold on a moment... Something's fading into view." ("base", xpos="far_left", ypos="head")
    else: # > 10
        her @ cheeks blush "Is... Is it working?" ("open", "closed", "base", "down") #a bit worried
        gen "Not yet..." ("base", xpos="far_left", ypos="head")
        gen "Hold on... Something's fading into view." ("base", xpos="far_left", ypos="head")
        her "What does it say?" ("open", "happy", "base", "mid") #a bit worried

    menu:
        "-Tell her she's a slave-" if states.her.status.anal:
            jump slave_scene
        "-Tell her she's a whore-" if states.her.status.sex:
            jump whore_scene
        "-Tell her she's a slut-" if states.her.status.blowjob or states.her.tier > 5:
            jump slut_scene
        "-Tell her she's a flasher-" if states.her.status.stripping:
            jump flasher_scene
        "-Tell her she's a good girl-":
            jump good_girl_scene

label slut_scene:

    play sound "sounds/flashbang.ogg"
    $ hermione.equip(her_neckwear_slut_collar)
    $ name_hermione_genie = "Slut"
    with flashbulb

    gen "A slut!" ("grin", xpos="far_left", ypos="head")
    her @ tears soft "What!?!" ("angry", "base", "base", "stare")
    her @ tears soft "Is that what it says?!" ("angry", "base", "base", "mid")
    gen "You come here nearly every day and do unspeakable things. A normal girl doesn't gobble her headmaster's cock and ask for seconds." ("base", xpos="far_left", ypos="head")
    her @ tears soft_blink "I knew it... How will I be able to live this down?" ("open", "happyCl", "base", "mid")
    gen "You won't. You'll have to embrace it." ("base", xpos="far_left", ypos="head")
    her @ tears soft "Embrace it!?" ("angry", "base", "base", "stare")
    gen "There's no coming back for a slut like you... Even if I leave, you'll just find some other cock to please." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]... That's not true!" ("angry", "happyCl", "worried", "mid",emote="sweat")
    gen "Don't act like you don't already know this...{w} You know that deep down, you're a filthy slut." ("base", xpos="far_left", ypos="head")
    her "I am not!" ("angry", "happyCl", "worried", "stare")
    gen "Suck my cock." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "... What?" ("angry", "happy", "base", "mid")
    gen "Come here..." ("base", xpos="far_left", ypos="head")
    gen "And, Suck....{w=0.4} My....{w=0.4} Cock...{w=0.4} Slut!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("annoyed", "narrow", "worried", "R")
    hide hermione_main
    with d3

    call her_walk("desk", "base", reduce=0.8)
    show screen blkfade
    with d3

    stop music fadeout 1.0

    nar "Hermione walks over and kneels before you as you pull out your cock from beneath your robes."

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 #HERMIONE if_changed
    call her_chibi_scene("bj_pause")

    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d3
    call ctc

    call bld

    gen "That's a good little slut..." ("base", xpos="far_left", ypos="head")
    gen "Now, if you want to suck my cock, I expect you to ask nicely." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What? Isn't it bad enough that the stupid collar said that I'm a slut! Just let me suck your cock!" ("clench", "happy", "base", "up", ypos="head")
    gen "Well, that's exactly it, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    gen "Sluts beg for cock!" ("base", xpos="far_left", ypos="head")
    gen "I expect you to beg!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("normal", "happyCl", "worried", "mid")
    her @ cheeks blush "Please [name_genie_hermione], let me suck your cock." ("open", "happyCl", "base", "mid")
    gen "*Hmm*... That was \"almost\" good enough...{w=0.4} Try again." ("base", xpos="far_left", ypos="head")
    gen "Put some effort into it!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Pretty please [name_genie_hermione], please let me suck your big beautiful cock." ("angry", "squint", "worried", "up")

    menu:
        "-Throat fuck-":
            gen "Good Slut..." ("base", xpos="far_left", ypos="head")
            gen "Here's your reward!" ("base", xpos="far_left", ypos="head")
            nar "Without missing a beat, you force your cock into her mouth and to the entrance of her throat."

            call her_chibi_scene("bj")
            with d3

            her @ cheeks blush "!!!" ("shock", "happyCl", "annoyed", "stare")
            nar "You feel her push back against your legs."
            gen "Now, now [name_hermione_genie]... Good sluts know how to relax their throat..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*eeettss-hhooooo-hhhhggggg*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "Let's go?" ("base", xpos="far_left", ypos="head")
            gen "Yeah, let's go!" ("base", xpos="far_left", ypos="head")
            her "..." ("open_wide_tongue", "closed", "angry", "mid")
            nar "Hermione's throat relaxes and allows you to enter."
            gen "*Ughhh*! Your throat feels so good..." ("base", xpos="far_left", ypos="head")
            gen "But that's to be expected from a hungry hole like yours... Isn't that right, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            nar "Rolling her eyes, Hermione continues taking your cock deep into her throat."
            her @ cheeks blush "*Slurp*! *Gltch*! *Gulp*!" ("open_wide_tongue", "narrow", "base", "stare_soft")
            gen "I asked you a question." ("base", xpos="far_left", ypos="head")
            her "*Cough*" ("open_wide_tongue", "wide", "worried", "up")
            her "*hhyyym-aaaa-hhhhtttt*" ("open_wide_tongue", "wide", "worried", "up")
            gen "What was that [name_hermione_genie]? I couldn't hear you over the sounds of you swallowing my cock." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*hhhhyyyyyym-aaaaaaa-hhhhhhhhttttttt*!" ("open_wide_tongue", "happyCl", "annoyed", "stare")
            nar "The vibrations from her throat as she tries to form a sentence sends a shiver down your shaft."
            gen "*Ugh* Once more... I'm not sure I caught that." ("angry", xpos="far_left", ypos="head")

            call her_chibi_scene("bj_pause")
            with d3

            her "{size=+10}I said yes, alright?!{/size}" ("mad", "narrow", "annoyed", "up")
            hide hermione_main
            gen "Yes indeed!" ("base", xpos="far_left", ypos="head")
            gen "Now, get back to sucking!" ("base", xpos="far_left", ypos="head")
            nar "Hermione impales her mouth once again down the shaft of your cock and begins bobbing her head even faster."

            call her_chibi_scene("bj")
            with d3

        "-Let her suck you off-":
            gen "Well, if you insist [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            nar "Hermione takes you into her waiting mouth."

            call her_chibi_scene("bj")
            with d3

            gen "See... Don't you feel better now that you have a cock in your mouth?" ("base", xpos="far_left", ypos="head")
            her "*Mmmmm*..." ("open_tongue", "narrow", "base", "up")
            gen "Admit it, you love this." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "stare_soft")
            gen "You love being used as my plaything." ("base", xpos="far_left", ypos="head")
            her "*Gulp*! *Gobble*! *Gobble*!" ("open_wide_tongue", "closed", "angry", "mid")
            gen "You might act all upset about people truly finding out what you really are." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Gulp*! *Gobble*! *Slurp*!" ("open_wide_tongue", "closed", "base", "mid_soft")
            gen "But deep down, you're the happiest when you don't have to act as if you're not a massive slut." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Slurp*! *Gobble*!" ("open_wide_tongue", "closed", "angry", "mid")
            gen "After all, the collar confirmed it..." ("base", xpos="far_left", ypos="head")
            gen "Didn't it?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("open_wide_tongue", "closed", "worried", "mid")
            gen "I asked you a question, slut." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj_pause")
            with d3

            nar "Hermione hurriedly takes your cock out of her mouth."
            her @ cheeks blush "*Ahem*...{w=0.4} If that's what the collar says..." ("soft", "narrow", "worried", "R")
            gen "Good to hear you finally admit it. Now, back in the mouth." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes [name_genie_hermione]..." ("open", "base", "worried", "up")
            nar "Hermione takes you back into her mouth with renewed effort."

            call her_chibi_scene("bj")
            with d3

    gen "*Ughhh*, I'm getting close, girl." ("base", xpos="far_left", ypos="head")
    gen "Get ready." ("base", xpos="far_left", ypos="head")
    call her_chibi_scene("bj_pause")
    nar "Hermione pulls your cock out of her mouth hastily, ready to receive her reward."
    gen "Here it comes!" ("angry", xpos="far_left", ypos="head")
    call cum_block

    call her_chibi_scene("bj_cum_out", trans=d5)
    $ hermione.set_cum(hair="light")
    her "!!!" ("angry", "wide", "base", "up")

    gen "Your reward, you Filthy...{w=0.4} Cumslut!" ("angry", xpos="far_left", ypos="head")
    gen "{size=+4}Aaaah!!{/size}" ("angry", xpos="far_left", ypos="head")
    nar "You explode across her face, covering her in your cum."

    call cum_block
    $ hermione.set_cum(hair="heavy")
    her "..." ("angry", "base", "base", "stare")

    call her_chibi_scene("bj_cum_out_done")
    nar "Watching as it slowly begins trickling down her face..."

    $ hermione.set_cum(face="light")
    her "..." ("angry", "happyCl", "base", "stare")

    $ hermione.set_cum(face="heavy")
    her "..." ("angry", "wide", "base", "up")
    gen "Ah..." ("angry", xpos="far_left", ypos="head")

    gen "Who's a good slut?" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "I am..." ("open", "narrow", "worried", "R")
    gen "Good girl..." ("base", xpos="far_left", ypos="head")

    if not her_neckwear_slut_collar.unlocked:
        $ her_neckwear_slut_collar.unlock()

        gen "Well now that we've established who you really are... I've got a present for you!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "A present? What is it?" ("soft", "happy", "base", "up")
        gen "That lovely collar on your neck, I'm giving it to you as a reminder of who you are." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "You're expecting me to keep it?" ("angry", "narrow", "base", "stare")
        gen "Most certainly..." ("base", xpos="far_left", ypos="head")
        gen "You are \"my\" slut, and you will do well to remember it...{w=0.4} Now get out of my office." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "...{w=0.4} Fine." ("angry", "narrow", "base", "down")

        call give_reward("A new collar has been unlocked in the wardrobe!")

    show screen blkfade
    with d5

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","mid", flip=False)

    hide screen blkfade
    with d5

    her @ cheeks blush "Can I get a towel or something to clean my face?" ("open", "happy", "base", "R", ypos="base", trans=d3)
    gen "Why? Worried someone's going to see how much of a slut you are?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You can't be serious!" ("upset", "happy", "worried", "stare")
    gen "I am... And if you ever want to suck my cock again, you will do as I say." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "...{w} Yes [name_genie_hermione]." ("annoyed", "narrow", "base", "R")
    gen "Well then...{w=0.4} Get going." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        her @ cheeks blush "Bye then... [name_genie_hermione]." ("open", "narrow", "base", "mid_soft")
    else:
        her "Good night then... [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
    gen "Until next time...{w=0.4} Slut." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("base", "narrow", "worried", "down")

    call her_walk(action="leave")

    jump end_hermione_event


label whore_scene: #(locked behind public reputation and last sex event)

    #Sex scene where she begs genie to cum inside her
    #Genie yells at her and makes her admit she is a whore
    #He cums inside her

    play sound "sounds/flashbang.ogg"
    $ hermione.equip(her_neckwear_whore_collar)
    $ name_hermione_genie = "Whore"
    with flashbulb

    gen "You are a--" ("base", xpos="far_left", ypos="head")
    her @ tears soft "Am I a slut?" ("angry", "base", "base", "mid", ypos="base")
    gen "*Err*..." ("base", xpos="far_left", ypos="head")
    her "Pansy Parkinson has been telling everyone that I'm a slut!" ("open", "narrow", "worried", "R")
    gen "Really? Why is this Pansy Parkinson calling you a slut?" ("base", xpos="far_left", ypos="head")
    her "I think she might know something..." ("angry", "narrow", "base", "down")
    her @ cheeks blush "She's going to ruin my reputation! What will people think when they find out what I've been doing with my ninety-year-old Professor?" ("disgust", "closed", "worried", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    her "I'll be known as a slut for the rest of my life!" ("scream", "happyCl", "worried", "mid")
    her @ tears soft_blink "I'll never be able to get a good job..." ("scream", "happyCl", "worried", "mid")
    her @ tears soft_blink "My friends will hate me..." ("angry", "happyCl", "worried", "mid")
    her "Please... The collar isn't telling you that I'm a slut, is it, [name_genie_hermione]?" ("angry", "wide", "worried", "mid")
    gen "Well, you'll be happy to know that this Parkinson girl is incorrect, Miss Granger." ("base", xpos="far_left", ypos="head")
    gen "The collar doesn't say that you're a slut..." ("base", xpos="far_left", ypos="head")
    her @ tears soft "Oh, thank heavens..." ("grin", "base", "worried", "mid")
    gen "You're worse than a slut...{w=0.4} You're a whore!" ("grin", xpos="far_left", ypos="head")
    her "What? A whore?!" ("angry", "wide", "worried", "stare")
    gen "Why indeed!" ("grin", xpos="far_left", ypos="head")
    gen "A slut is someone who enjoys sex... A whore is someone who's selling themselves for materialistic gains!" ("base", xpos="far_left", ypos="head")
    gen "As long as someone pays you one way or the other, you couldn't care less, could you?" ("base", xpos="far_left", ypos="head")
    her "I--{w=0.2} I--{w=0.2} I--" ("clench", "happyCl", "worried", "mid")
    gen "I bet you'd beg your precious little friends to fuck you if I wasn't around, as long as it would benefit you..." ("base", xpos="far_left", ypos="head")
    gen "Look at what you've become, nothing more than the school bicycle... Willing to give everyone a happy ride." ("base", xpos="far_left", ypos="head")
    gen "I wouldn't be worried about your friends finding out what you're doing in here. They're probably just waiting for a turn themselves..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione] please...{w=0.4} You're being mean." ("shock", "happyCl", "worried", "mid")
    gen "Oh, is the little whore getting upset? Don't worry, I'll make you feel all better." ("base", xpos="far_left", ypos="head")
    her "...How can you say that after--" ("angry", "happyCl", "worried", "mid")
    gen "Come over here and bend over." ("base", xpos="far_left", ypos="head")
    her "You can't be serious! After what you just said?!" ("angry", "squint", "worried", "stare")
    gen "I am serious... A good little whore should present her naked body for the client whenever he requires it..." ("base", xpos="far_left", ypos="head")
    her "..." ("disgust", "happyCl", "base", "down")
    gen "Now be a good whore and come over here...{w=0.4} I'll be sure to give you what you want." ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base", reduce=0.8)
    show screen blkfade
    with d3

    stop music fadeout 1.0

    nar "Hermione hesitates for just a moment before following your instructions."
    if hermione.is_any_worn("top", "bottom", "bra", "panties"):
        play sound "sounds/cloth_sound3.ogg"
        nar "While looking away, she strips down until standing butt naked in front of you, wearing nothing but the collar."

    $ hermione.strip("clothes")
    #nar "Throwing the collar to the floor she quickly walks over to your desk, then bends over and presents herself."
    $ hermione.wear("neckwear")

    call her_chibi_scene("sex_pause")
    hide screen blkfade
    with d3

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    gen "Such a good little whore you are...{w=0.4} Now, say aloud what you truly want..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("annoyed", "narrow", "worried", "down")
    her @ cheeks blush "Please [name_genie_hermione]..." ("open", "narrow", "worried", "down")
    gen "Please what?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=-4}Please...{w=04} Fuck me...{/size}" ("disgust", "base", "worried", "R")
    gen "I'm not sure I heard you... Speak up [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=+5}Please fuck me [name_genie_hermione]!{/size}" ("scream", "happyCl", "base", "stare")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "Not bad..." ("grin", xpos="far_left", ypos="head")

    hide hermione_main
    with d3

    nar "You take a firm grip of Hermione's hips and thrust into her sopping pussy."

    play sound "sounds/gltch.ogg"
    with kissiris

    call her_chibi_scene("sex")
    play background "sounds/slickloop.ogg" fadein 2

    her @ cheeks blush "{heart}*Ah*...{heart}" ("open_tongue", "happyCl", "worried", "mid")
    gen "*Argh*...{w=0.4} How is your pussy still so tight?" ("base", xpos="far_left", ypos="head")
    gen "I thought that you would have loosened up after all the guys you've fucked." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "[name_genie_hermione]..." ("disgust", "happyCl", "worried", "mid")
    gen "Don't try and act coy with me [name_hermione_genie]... We both know what you're up to when the lights go out." ("base", xpos="far_left", ypos="head")
    gen "Just admit what you are." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=-4}A whore...{/size}" ("soft", "narrow", "worried", "up")
    gen "Who's a good little whore?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=+5}Me! I'm a whore!{/size}" ("open_wide_tongue", "narrow", "base", "up")
    gen "That's right... Just like the collar said..." ("base", xpos="far_left", ypos="head")
    gen "Now beg me..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{heart}*Ah*...{heart}{w=0.4} B--{w=0.2} Beg you?" ("grin", "narrow", "base", "up_soft")
    gen "Beg me to cum inside your pussy, to pay you in semen." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I...{w=0.4} {heart}*Ah*...{heart}" ("soft", "narrow", "base", "up_soft")
    gen "Do it whore!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Ah*...{w=0.4} Please fill my pussy with your thick... {heart}cum!{heart}" ("grin", "narrow", "base", "dead")
    gen "That's a good little whore...{w=0.4} Now, who else have you practised that line with, I wonder?" ("base", xpos="far_left", ypos="head")
    gen "Is it just me, or do you beg every other boy you screw with to cum inside you?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{heart}{heart}{heart}..." ("angry", "narrow", "base", "dead")
    gen "Tell me girl." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I--{w=0.2} {heart}*Ah*...{heart}{w=0.4} I beg every boy that fucks me to cum inside!" ("soft", "narrow", "worried", "up_soft")
    gen "Such a fucking whore...{w=0.4} You disgust me..." ("base", xpos="far_left", ypos="head")

    play sound "sounds/spit.ogg"
    call ctc
    play background "sounds/sexloopfast.ogg"

    nar "You spit on your shaft to lube it up even further and then thrust your hips hard into Hermione's pussy."
    her @ cheeks blush "I-- {w=0.2} I'm...{w=0.4} *Ah*...{w=0.4} I'm cumming!" ("open_wide_tongue", "base", "worried", "ahegao")
    gen "Well I think I might join you then." ("base", xpos="far_left", ypos="head")

    play background "sounds/sexloopveryfast.ogg"
    nar "You increase your pumping of Hermione's pussy."

    gen "Here's your payment, whore. You've earned it!" ("angry", xpos="far_left", ypos="head")
    nar "You push yourself all the way in and start shooting off deep into her womb."

    gen "{size=+7}*Argh*, Yes!!!{/size}"
    call cum_block
    play sound "sounds/slick_01.ogg"
    stop background fadeout 2
    call her_chibi_scene("sex_cum_in")

    play sound "sounds/slick_01.ogg"
    with kissiris
    her @ cheeks blush "!!!" ("grin", "wide", "worried", "stare")

    gen "That's it, take it all you fucking whore!" ("angry", xpos="far_left", ypos="head")
    call cum_block
    play sound "sounds/slick_01.ogg"

    call her_chibi_scene("sex_cum_in_done")

    gen "Ah..." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush tears crying "..." ("grin", "narrow", "base", "dead")
    gen "Well?" ("base", xpos="far_left", ypos="head")
    gen "Show some gratitude, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "...{w=0.4} Thank you, [name_genie_hermione]." ("base", "narrow", "worried", "stare")
    gen "\"Thank you...\"{w=0.4} For what? Don't be shy, slut." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Thank you for...{w}{nw}" ("open", "closed", "worried", "stare")
    her @ cheeks blush "Thank you for...{fast} Cumming in my pussy..." ("base", "happy", "worried", "mid")
    gen "You're welcome girl. A good whore should always be grateful." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes [name_genie_hermione]..." ("base", "closed", "base", "mid")
    hide hermione_main

    show screen blkfade
    with d3

    $ hermione.equip(her_outfit_last)

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")

    nar "Hermione gets to her feet and walks to the front of your desk."

    # This is to check if the player already unlocked the collar before
    # and does not have it equipped in their outfit
    # and so it does make sense from a narration standpoint.
    if not hermione.is_equipped_item(her_neckwear_whore_collar):
        play sound "sounds/collar_click.ogg"
        nar "You grab her by the collar, swiftly unlocking it and taking it off of her."

    hide screen blkfade
    with d3

    if not her_neckwear_whore_collar.unlocked:
        gen "Well then... Seeing as how you said thank you... I have a present for you." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "A present?" ("soft", "wink", "worried", "mid_soft", trans=d3)
        gen "Yes, it's a lovely piece of jewellery to commemorate your self-acceptance." ("base", xpos="far_left", ypos="head")

        nar "You present Hermione the collar you have taken off her neck a moment ago."

        her @ cheeks blush "The collar? You're giving it to me?" ("open", "happy", "base", "mid")
        her @ cheeks blush "And how is that supposed to be a piece of jewellery?" ("annoyed", "narrow", "base", "R")
        gen "It's a piece of metal to adorn your neck is it not?" ("base", xpos="far_left", ypos="head")
        gen "Pretty sure that's what a necklace is..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "And you expect me to wear this?" ("soft", "narrow", "worried", "mid")
        gen "Of course. We both know what a whore you are... Why not wear it with pride..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Around my neck?" ("clench", "narrow", "worried", "mid")
        gen "Well, we could always tattoo it across your forehead..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "A collar it is then..." ("annoyed", "narrow", "base", "down")
        her @ cheeks blush "I'll wear it if I really have to..." ("soft", "narrow", "base", "down")
        gen "And proudly!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "... *Hmph*!" ("annoyed", "narrow", "base", "R")

        call give_reward("A new collar has been unlocked in the wardrobe!")

    her @ cheeks blush "Goodbye then, [name_genie_hermione]." ("soft", "narrow", "base", "R")
    gen "Goodbye [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    jump end_hermione_event


label slave_scene:

    play sound "sounds/flashbang.ogg"
    $ hermione.equip(her_neckwear_slave_collar)
    $ name_hermione_genie = "Slave"
    $ name_genie_hermione = "Master"
    with flashbulb

    her "It doesn't say slut, does it?" ("open", "narrow", "base", "R")
    gen "Don't be silly... Why would it say that,{w=0.5} slave?" ("base", xpos="far_left", ypos="head")
    her "Oh good..." ("base", "base", "worried", "mid")
    her "Wait. What did you just call me?" ("upset", "wide", "base", "mid")
    gen "You're a slave, Miss Granger. Specifically, {b}my{/b} slave..." ("base", xpos="far_left", ypos="head")
    her "What are you talking about?" ("angry", "happy", "worried", "mid")
    gen "It's obvious isn't it?" ("base", xpos="far_left", ypos="head")
    her "No, it's not!" ("open", "happyCl", "annoyed", "R")
    gen "You come in here whenever I order you to..." ("base", xpos="far_left", ypos="head")
    her "..." ("angry", "narrow", "angry", "R")
    gen "You please me whenever I ask..." ("base", xpos="far_left", ypos="head")
    her "..." ("annoyed", "narrow", "worried", "R")
    gen "Shall I go on?" ("base", xpos="far_left", ypos="head")
    her "That's not true!" ("angry", "narrow", "worried", "down")
    gen "Oh really? Then when was the last time you ever said {b}no{/b} to me?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well, I--" ("open", "narrow", "worried", "R")
    gen "Exactly... You became my slave a long time ago, just accept it." ("base", xpos="far_left", ypos="head")
    her "Just because I care about my house it doesn't mean--" ("angry", "happyCl", "worried", "mid",emote="sweat")
    gen "Oh please... We have been through this already." ("base", xpos="far_left", ypos="head")
    gen "When was the last time you actually cared about acquiring those silly points of yours?" ("base", xpos="far_left", ypos="head")
    her "Sir, they are not silly--" ("open", "happyCl", "worried", "R", emote="sweat")
    gen "Silence. I'm not finished." ("base", xpos="far_left", ypos="head")
    her "..." ("angry", "base", "worried", "mid")
    gen "The facts are speaking against you, and very loudly, my dear slave girl." ("base", xpos="far_left", ypos="head")
    gen "Almost as loud as you're calling my name when I fill that tight pussy of yours." ("grin", xpos="far_left", ypos="head")
    her "..." ("angry", "happyCl", "worried", "R",emote="sweat")
    gen "You know what I think?" ("base", xpos="far_left", ypos="head")
    gen "I think you are scared to admit that what you truly want from life is to be controlled and be taken care of, like a faithful puppy, or a slave." ("base", xpos="far_left", ypos="head")
    gen "But so be it. I'll give you a choice." ("base", xpos="far_left", ypos="head")
    gen "If you are so adamant that you are not my slave, then turn around and get the fuck out of this office and never come back." ("base", xpos="far_left", ypos="head")
    gen "Or." ("base", xpos="far_left", ypos="head")
    gen "Beg me to fuck you silly like a good slave would." ("base", xpos="far_left", ypos="head")

    her @ cheeks blush tears soft "I..." ("soft", "base", "base", "stare") # Tears welling up
    gen "Don't give me that look. We both know that you enjoyed me using you like a cock-sleeve." ("base", xpos="far_left", ypos="head")
    gen "You even let me fuck you in the ass, and you loved every second of it!" ("angry", xpos="far_left", ypos="head")
    gen "I am not scared to admit what I enjoy, are you?" ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "..." ("normal", "narrow", "base", "down") # Hermione's thoughts are racing
    her @ cheeks blush "......." ("normal", "narrow", "worried", "stare") # Hermione is having a hard time thinking
    her @ cheeks blush "................." ("normal", "narrow", "worried", "dead") # Hermione expresion turns to dead, stares into nothing
    her @ cheeks blush "C-Can you fuck me..." ("soft", "narrow", "worried", "dead") # stares into nothing
    her @ cheeks blush "... Please?" ("angry", "narrow", "worried", "dead") # looks at genie (eyes dead)

    gen "What was that?" ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "Please fuck me sir!!!{heart}{heart}{heart}" ("grin", "narrow", "worried", "dead") # screams, eyes closed

    gen "So be it." ("base", xpos="far_left", ypos="head")

    if hermione.is_any_worn("top", "bottom", "bra", "panties"):
        gen "Now, be a good slave and take those silly clothes off and bend over my desk..." ("base", xpos="far_left", ypos="head")
    else:
        gen "Now be a good slave and bend over my desk." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("smile", "narrow", "base", "stare")

    call her_walk("desk", "base", reduce=0.8)
    show screen blkfade
    with d3

    stop music fadeout 1.0

    if hermione.is_any_worn("top", "bottom", "bra", "panties"):
        play sound "sounds/cloth_sound3.ogg"
        nar "Hermione takes off her clothes and bends over your desk, leaving herself bare."

    $ hermione.strip("clothes")
    $ hermione.wear("neckwear")

    call her_chibi_scene("sex_pause")
    hide screen blkfade
    with d3

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    gen "That's a good slave." ("base", xpos="far_left", ypos="head")
    gen "Now ask me nicely to fuck that tight ass of yours." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Please sir, please fuck my ass." ("soft", "happy", "worried", "R", ypos="head")
    gen "Good girl." ("base", xpos="far_left", ypos="head")
    nar "You thrust your full length into Hermione in one motion."

    play sound "sounds/gltch.ogg"
    with kissiris
    her @ cheeks blush "{heart}*Ah*...{heart}" ("open_tongue", "happy", "base", "ahegao")

    nar "Hermione's ass gripping tightly around your cock, you begin pushing in and out of her."
    call her_chibi_scene("sex")
    play background "sounds/slickloop.ogg" fadein 2

    gen "Your ass is very tight today... Enjoying being broken in?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes sir, I... I love it." ("base", "narrow", "base", "up")
    gen "Good, then make sure to keep your hole nice and tight." ("base", xpos="far_left", ypos="head")
    nar "You pick up speed and begin to fuck her ass in earnest."
    gen "Now tell me girl. Who do you belong to?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You." ("open", "narrow", "worried", "stare")
    gen "Good, and who am I?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Professor Dumbledore." ("base", "narrow", "base", "up")

    call slap_her

    nar "You unleash a firm slap across her buttocks."
    her @ cheeks blush "" ("open_tongue", "happyCl", "base", "up")
    call ctc
    gen "That's not who I am to you [name_hermione_genie]...{w=0.4} To you, I am your master." ("base", xpos="far_left", ypos="head")
    gen "Do you understand now?" ("base", xpos="far_left", ypos="head")
    her @ tears soft "Yes..." ("angry", "base", "base", "stare")

    call slap_her

    nar "You give Hermione another powerful slap, leaving a bright red mark across her cheeks."
    gen "Yes what?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "Yes, master...{heart}{heart}" ("angry", "happyCl", "base", "mid")

    gen "Good...{w=0.4} You're a fast learner." ("base", xpos="far_left", ypos="head")
    gen "Now, if I'm your master...{w=0.4} Then what does that make you?" ("base", xpos="far_left", ypos="head")
    her @ tears soft "{size=-7}A--{w=0.2} A slave...{/size}" ("soft", "narrow", "base", "stare")
    gen "Speak up girl!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "I am a slave..." ("angry", "base", "worried", "mid")

    call slap_her
    nar "You give Hermione yet another strong slap across her buttocks."

    gen "That's right... But not just some common slave." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "N--{w=0.4} No?" ("angry", "narrow", "worried", "stare") # confused
    gen "No, of course not..." ("base", xpos="far_left", ypos="head")
    gen "You're my {i}personal{/i} slave." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I--{w=0.2} I think I'm about to cum [name_genie_hermione]..." ("angry", "narrow", "worried", "R")

    call slap_her
    nar "You give Hermione a fierce slap across her left buttock."

    gen "I am your master, and I will decide when you are allowed to cum. Got it?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Please [name_genie_hermione]!" ("angry", "happyCl", "base", "mid")
    gen "Not...{w=0.4} Yet!{w} Not until I say so..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Please...{w=0.4}, I beg of you, [name_genie_hermione], I can't hold it!{heart}" ("angry", "narrow", "worried", "up")
    gen "Then you better put some effort into it if you want me to finish sooner." ("base", xpos="far_left", ypos="head")

    play background "sounds/sexloop.ogg"
    nar "Hermione starts pushing back against you, rotating her hips and massaging your shaft as you thrust into her."

    gen "Yes! That's a good slave...{w=0.4} You're doing great." ("base", xpos="far_left", ypos="head")

    nar "Gripping tightly onto Hermione's hips, you impale her down to the hilt of your throbbing member."

    gen "*Ughhh*..." ("angry", xpos="far_left", ypos="head")

    call her_chibi_scene("sex_cum_in")

    nar "You let out a load groan and start cumming inside Hermione."
    play sound "sounds/slick_01.ogg"
    stop background fadeout 2

    her @ cheeks blush "[name_genie_hermione]{heart}{heart}... I--{w=0.2} I--{heart}" ("grin", "base", "base", "ahegao")
    gen "Cum for your master, slut! Cum your brains out!" ("angry", xpos="far_left", ypos="head")
    play sound "sounds/slick_01.ogg"
    with kissiris
    her @ cheeks blush "{heart}*Ah*!!{heart}" ("smile", "narrow", "base", "up")

    gen "That's right, take it all you dirty girl!" ("base", xpos="far_left", ypos="head")

    call cum_block
    play sound "sounds/slick_01.ogg"
    nar "You continue to shoot ropes of cum into her asshole."

    her @ cheeks blush "{heart}*Ah*...{w=0.4}{heart}*Ah*...{w=0.4}{heart}*Ah*...{w=0.4}{heart} Thank you, thank you sir..." ("open", "happyCl", "worried", "mid")

    call slap_her

    call her_chibi_scene("sex_cum_in_done")

    gen "What was that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "[name_genie_hermione]! Thank you, [name_genie_hermione], thank you [name_genie_hermione].{heart}{heart}{heart}" ("grin", "narrow", "base", "dead")
    gen "That's right, [name_hermione_genie]... Know your place..." ("base", xpos="far_left", ypos="head")

    nar "Hermione closes her eyes as she rides out the last of her orgasm."

    gen "On your knees [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "W--{w=0.2} What?" ("soft", "happy", "worried", "R")
    gen "No questions." ("base", xpos="far_left", ypos="head")
    gen "Get off the desk and onto your knees." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes, [name_genie_hermione]..." ("angry", "narrow", "base", "down")

    nar "Hermione pulls herself off of your dick, turns around, and kneels in front of you."

    call her_chibi_scene("bj_pause")
    with fade

    gen "Let's see how much you've learned today." ("base", xpos="far_left", ypos="head")
    gen "Tell me again...{w=0.4} What are you?" ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "A slave." ("base", "narrow", "worried", "down") # Alternative: "A stupid sandwich." lol
    gen "Who do you belong to?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "To you, [name_genie_hermione]." ("open", "happy", "base", "up")

    if not her_neckwear_slave_collar.unlocked:
        $ her_neckwear_slave_collar.unlock()

        gen "That's right... And because you've been such a good slave, I'm going to give you a present." ("base", xpos="far_left", ypos="head")
        her "A present, [name_genie_hermione]?" ("soft", "happy", "base", "up")
        gen "The collar you're wearing... I want you to keep it." ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]! Thank you, [name_genie_hermione]!" ("angry", "happy", "base", "up")

        call give_reward("A new collar has been unlocked in the wardrobe!")

        gen "Now... On your feet." ("base", xpos="far_left", ypos="head")
    else:
        gen "That's right. Now clean me up slut, I don't have the entire day." ("base", xpos="far_left", ypos="head")

        call her_chibi_scene("bj")
        nar "Hermione looks up at you with eyes devoid of any resistance, then engulfs your entire shaft, sloppily licking and sucking on it, doing her best to please her master..."
        nar "After your penis is thoroughly cleaned, you let go of her."

    show screen blkfade
    with d3

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","mid","base")

    hide screen blkfade
    with d3

    her "..." ("base", "narrow", "worried", "down") # Look of adoration, waiting for a command
    gen "What is it? Speak up." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]. I was wondering if...--" ("soft", "narrow", "worried", "down")
    gen "--If You could get house points for this? *Ha-ha-ha*, of course not...{w=0.5} Slaves aren't getting paid, that's what makes them slaves." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I suppose you're right..." ("soft", "narrow", "base", "R")
    gen "Now be on your way, I will call for you if I need anything." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]!" ("soft", "closed", "base", "mid")

    if her_outfit_last.has_any_type("clothes"):
        nar "Hermione grabs the pile of clothes lying nearby, not even bothering to put them back on."

    call her_walk(action="leave")

    $ hermione.equip(her_outfit_last)

    jump end_hermione_event

label flasher_scene:

    gen "You're..." ("base", xpos="far_left", ypos="head")
    gen "A flasher!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What?!" ("angry", "wide", "base", "mid")

    play sound "sounds/flashbang.ogg"
    $ hermione.equip(her_neckwear_flasher_collar)
    $ hermione.strip("top", "bra")
    $ name_hermione_genie = "Flasher"
    with flashbulb
    her "Aaah!!!"

    if hermione.is_any_equipped("top", "bra"):
        nar "Hermione blinks, and looks down as her vision returns."

        if hermione.is_equipped("top", "bra"):
            her @ cheeks blush "What happened to my clothes?!" ("mad", "narrow", "base", "down", trans=d3)
        elif hermione.is_equipped("top"):
            her @ cheeks blush "Where has my top gone?!" ("mad", "narrow", "base", "down", trans=d3)
        elif hermion.is_equipped("bra"):
            her @ cheeks blush "Where is my bra?!" ("mad", "narrow", "base", "down", trans=d3)

        gen "*Hah-hah*!! Bringing out your true self are you?" ("base", xpos="far_left", ypos="head")

        if states.her.level < 16:
            her @ cheeks blush "This isn't funny!" ("angry", "narrow", "angry", "R")
            gen "I'm sure you'll get it back once you take the collar off." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmph*..." ("annoyed", "narrow", "base", "down")
    else:
        her @ cheeks blush "Why did it do that?!" ("angry", "narrow", "base", "dead", trans=d3)
        nar "Hermione blinks, and looks down as her vision returns."

    her @ cheeks blush "What are these strings?" ("angry", "narrow", "base", "down")
    gen "I would be careful with those if I were you--" ("base", xpos="far_left", ypos="head")
    nar "Hermione tugs at the strings hanging from the collar."
    her @ cheeks blush tears soft_blink "Ow-ow-ow!!" ("angry", "happyCl", "base", "mid")

    if states.her.level < 16: #Before she'd wear piercings
        her @ cheeks blush "They're... They're attached to my nipples!" ("mad", "narrow", "base", "mid")
        gen "Indeed they are." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "B-- But..." ("clench", "narrow", "worried", "down")
    else:
        gen "Told you..." ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "I can't believe a magic collar would--" ("clench", "narrow", "base", "down")
    gen "So... A flasher, eh?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What?" ("angry", "squint", "base", "mid")
    gen "That's what the collar says." ("base", xpos="far_left", ypos="head")

    if states.her.level < 19:
        her @ cheeks blush "I'm... I'm not a flasher!" ("disgust", "narrow", "annoyed", "R")
        nar "You watch as the strings of the collar move slightly by Hermione's words."
        her @ cheeks blush "The collar must be broken!" ("open", "closed", "annoyed", "mid")
        her @ cheeks blush "I'm only doing this for--" ("annoyed", "narrow", "base", "mid")
        gen "Agreed." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Huh*?" ("disgust", "base", "base", "mid")
    else:
        her @ cheeks blush "*Ehm*..." ("disgust", "base", "base", "mid")

    gen "The collar must be broken..." ("base", xpos="far_left", ypos="head")
    gen "I guess exhibitionist wouldn't fit on it." ("base", xpos="far_left", ypos="head")
    nar "As if on command, the collar tugs the strings slightly, causing Hermione to jerk up."
    her @ cheeks blush "Ow!" ("angry", "wide", "base", "stare")
    gen "I'll take that as a confirmation..." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Where...{w=0.4} Where did you get this thing from?" ("angry", "base", "base", "mid")
    gen "*Err*... Some magic shop." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Magic shop?" ("disgust", "narrow", "base", "mid")
    gen "Well...{w=0.4} Not \"the\" magic shop...{w} That's back in my world." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Huh*?" ("open", "base", "worried", "mid")
    gen "Although I must say I'm a bit disappointed..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You're disappointed? You've just had the collar label me a flasher!" ("open", "narrow", "annoyed", "R") #annoyed
    gen "The collar hasn't labelled you anything... It merely showed your true self." ("base", xpos="far_left", ypos="head")

    if hermione.is_any_worn("clothes"):
        gen "I'm disappointed because I assumed it would strip you completely..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Strip me--" ("open", "base", "base", "mid")

        play sound "sounds/flashbang.ogg"
        $ hermione.strip("clothes")
        $ hermione.wear("neckwear")
        with flashbulb

        her @ cheeks blush "What the--" ("clench", "base", "base", "down")
        gen "There it is! Your true self!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("annoyed", "base", "base", "mid")
    else:
        gen "Well... The collar didn't need to do much, did it... Seeing your current state of undress..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("annoyed", "base", "base", "mid")

    gen "Well then... Now that the collar has told us how much you enjoy showing off your naked body..." ("base", xpos="far_left", ypos="head")
    gen "I want to hear it from you..." ("base", xpos="far_left", ypos="head")

    if states.her.level < 19: # Won't admit it
        her @ cheeks blush "Hear... Hear what from me?" ("disgust", "happy", "base", "mid")
        gen "Tell me how much you're enjoying flaunting your naked body." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I...{w=0.4} I am just doing it for the points, [name_genie_hermione]!" ("angry", "happyCl", "worried", "R")
        nar "The collar once more tugs on the strings, making Hermione gasp."
        her @ cheeks blush "*Ah*..." ("soft", "happyCl", "base", "mid") #Horny
        her @ cheeks blush "..." ("disgust", "narrow", "base", "stare") #embarrased
        gen "Really?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes, I--" ("angry", "narrow", "base", "down")
        nar "The collar tugs even harder, Hermione seemingly fighting conflicting emotions."
        her @ cheeks blush "Ow!" ("angry", "happyCl", "base", "stare")
        gen "Come on [name_hermione_genie]... Even the collar knows that you're lying..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "S--{w=0.2} Sorry [name_genie_hermione]... But I cannot." ("disgust", "narrow", "worried", "stare")
        nar "As if trying to teach her a lesson, the collar pulls its strings with all its might, making Hermione yelp with pain."
        her @ cheeks blush tears soft_blink "Ouch!" ("scream", "happyCl", "worried", "mid")
        gen "Sounds more like you {i}don't want to{/i}, rather than {i}cannot{/i} admit it..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears soft "..." ("annoyed", "narrow", "worried", "R")
        gen "Very well then, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "You may take the collar off." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Thank you [name_genie_hermione]..." ("soft", "narrow", "worried", "down")

    elif states.her.level < 22: # Hesitates but will eventually admit it
        her @ cheeks blush "You... You want me to say that I..." ("open", "happy", "base", "R")
        gen "Enjoy showing off your body..." ("base", xpos="far_left", ypos="head")

        if states.her.status.public_stripping:
            gen "That you like when people are watching you, especially when you're naked." ("base", xpos="far_left", ypos="head")
        else:
            gen "That you like showing yourself off to me..." ("base", xpos="far_left", ypos="head")

        her @ cheeks blush "I..." ("disgust", "narrow", "base", "down")
        nar "You watch as the strings of the collar slowly begin to pull on itself as Hermione hesitates."
        her @ cheeks blush "I..." ("soft", "narrow", "base", "down")
        nar "The strings, now completely stretched, begins tugging on Hermione's nipples."
        her @ cheeks blush "Alright I do enjoy it okay!" ("angry", "happyCl", "worried", "mid")
        nar "As the words leave Hermione's lips, the strings return to their dormant state."
        her @ cheeks blush "*Phew*..." ("soft", "narrow", "worried", "down")
        gen "Now was that so hard?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("annoyed", "narrow", "base", "R")
        her @ cheeks blush "I only said it because of this stupid--" ("open", "closed", "annoyed", "mid")

        call slap_her
        nar "The strings slap her breasts in unison."

        her @ cheeks blush "Ouch!" ("angry", "wide", "worried", "stare")
        gen "*Heh-heh*..." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Can I take this off now?" ("open", "narrow", "annoyed", "R")
        gen "Yes, you may take the collar off now, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Thank you [name_genie_hermione]..." ("open", "narrow", "base", "mid")

    else: #Openly admits it, proves it to you
        nar "You watch as the strings attached to her new nipple piercings tug and pull, making her nipples harden."
        her @ cheeks blush "I love it!" ("grin", "narrow", "base", "down")
        nar "The collar, happy with the answer, relaxes its strings."

        gen "Oh?" ("base", xpos="far_left", ypos="head")

        her @ cheeks blush "I mean... If the magic collar says so, then it must be true..." ("grin", "narrow", "base", "mid")
        gen "I...{w=0.4} Yes, although I didn't think you'd be so hasty to admit it." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Let's give you some confirmation then..." ("base", "narrow", "base", "mid")
        gen "What are you--" ("base", xpos="far_left", ypos="head")
        hide hermione_main

        stop music fadeout 1.0

        call her_walk("desk", "base", reduce=0.8)
        show screen blkfade
        with d3

        play sound "sounds/08_hop_on_desk.ogg" #Sound of the desk squeaking.
        pause 3
        gen "!!!!!!" ("angry", xpos="far_left", ypos="head")
        nar "Hermione, waiving away your questioning look, walks over and climbs onto your desk..."

        call her_chibi("dance_pause","on_desk","on_desk")

        hide screen blkfade
        with fade
        pause.5

        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 #HERMIONE if_changed

        gen "Miss Granger!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Is this enough proof for you?" ("grin", "narrow", "base", "down")
        nar "Hermione stares into your face, cheeks flushed with colour as she spreads her wet pussy..."

        gen "Ten points to Gryffindor!" ("grin", xpos="far_left", ypos="head")
        $ gryffindor += 10

        her @ cheeks blush "Thank you, [name_genie_hermione]..." ("grin", "narrow", "base", "mid")
        nar "With a sensual step, Hermione turns around then bends down, showing you her ass and pussy in vivid details."

        gen "Holy shit! This feels like a strip-club!" ("grin", xpos="far_left", ypos="head")
        gen "Another Ten points to Gryffindor!" ("grin", xpos="far_left", ypos="head")
        $ gryffindor += 10

        show screen blkfade
        with d5

        nar "Hermione prances around your desk for a moment, and shows herself off from every angle..."

        her @ cheeks blush "Now if you don't mind..." ("grin", "closed", "base", "mid")

        play sound "sounds/08_hop_on_desk.ogg"
        nar "Hermione gets off your desk."
        call her_chibi("stand","desk","base")

        hide screen blkfade
        with d5

        her @ cheeks blush "I believe you got your proof..." ("smile", "narrow", "base", "mid")
        gen "What proof..." ("base", xpos="far_left", ypos="head")
        gen "Oh! Yes... Well done, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "I haven't felt more convinced in my life." ("grin", xpos="far_left", ypos="head")

    play sound "sounds/collar_click.ogg"
    her @ cheeks blush "Good, then let me just take this thing off..." ("grin", "narrow", "base", "down")

    play sound "sounds/flashbang.ogg"
    $ hermione.equip(her_outfit_last)
    with flashbulb

    her "Whoa!" ("soft", "base", "base", "down")
    her "The strings disappeared!" ("soft", "happy", "base", "mid")
    gen "Convenient..." ("base", xpos="far_left", ypos="head")
    her "Is that everything, then?" ("open", "base", "base", "R")
    gen "Yes, [name_hermione_genie]... That shall do for today." ("base", xpos="far_left", ypos="head")

    if states.her.level < 19:
        $ gryffindor += current_payout
        gen "{number=current_payout} points to Gryffindor, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")

    if not her_neckwear_flasher_collar.unlocked:
        $ her_neckwear_flasher_collar.unlock()
        gen "You may keep that collar by the way." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Really?" ("open", "base", "base", "mid")

        if states.her.level < 19:
            her "What if I don't want it..." ("disgust", "narrow", "base", "R")
            gen "We both know you want it." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "base", "mid")
            gen "I'll put it to the side for now..." ("base", xpos="far_left", ypos="head")
        else:
            gen "Certainly..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright then..." ("open", "narrow", "base", "R")
            her @ cheeks blush "Just let me know when you want me to put it on..." ("open", "closed", "base", "mid")

        call give_reward("A new collar has been unlocked in the wardrobe!")

    if game.daytime:
        her @ cheeks blush "Have a Good day." ("soft", "base", "base", "R")
        gen "Good day... [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    else:
        her @ cheeks blush "Have a Good night." ("soft", "base", "base", "R")
        gen "Good night... [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    jump end_hermione_event

label good_girl_scene:

    nar "With a brief flash of light, the collar changes its form..."

    play sound "sounds/flashbang.ogg"
    $ hermione.equip(her_neckwear_good_girl_collar)
    $ hermione.strip("top")
    with flashbulb

    gen "It says you're a Good girl." ("base", xpos="far_left", ypos="head")

    if states.her.level < 4:
        her "Just as I thought..." ("grin", "closed", "base", "mid")
        her "I am a model student after all." ("open", "closed", "base", "mid")
        gen "(*Hmm*... The collar must be broken... I've been scammed!)" ("angry", xpos="far_left", ypos="head")
        her "[name_genie_hermione]?" ("soft", "base", "base", "mid")

    elif states.her.level < 10:
        her "That's nice." ("base", "squint", "worried", "mid")
        her "Must be because of how I've been earning all these points for my house." ("open", "closed", "worried", "mid")
        gen "Yep, I'm sure that's it..." ("base", xpos="far_left", ypos="head")
        gen "(Such a waste of thirty points...)" ("base", xpos="far_left", ypos="head")
        her "So... I put it on, can I have my--" ("soft", "base", "base", "mid")
        gen "Yes, yes... You'll get your stupid points..." ("base", xpos="far_left", ypos="head")

    elif states.her.level < 19:
        her "It does?" ("soft", "base", "base", "mid")
        gen "Indeed it does... Guess there was nothing to be worried about." ("base", xpos="far_left", ypos="head")
        her "Alright then..." ("base", "base", "worried", "R")
        gen "{size=-4}Such a waste of points... Why did I get this stupid thing?{/size}" ("base", xpos="far_left", ypos="head")

        if hermione.is_any_worn("top", "bra"):
            her "*Hmm*..." ("annoyed", "base", "base", "mid")
            her "Well then... Before I go." ("open", "closed", "base", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            her "I thought that since you're paying me and all, I should at least show you my breasts..." ("open", "closed", "base", "down")
            gen "That seems fair." ("grin", xpos="far_left", ypos="head")

            stop music fadeout 1.0

            $ hermione.strip("bra")
            with d3
            play sound "sounds/cloth_sound3.ogg"
            pause 2.0

            if states.her.level < 13:
                her "..." ("annoyed", "base", "base", "mid")
                her "There you are then..." ("open", "base", "base", "R")
            else:
                her @ cheeks blush "Do you like them, [name_genie_hermione]." ("open", "base", "base", "mid")
                gen "Do you even have to ask?" ("grin", xpos="far_left", ypos="head")
                gen "Of course I do, they're great!" ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "Thank you [name_genie_hermione]..." ("base", "closed", "base", "mid")

            call music_block

        else: #Not wearing either top nor bra
            her "So... Am I still getting paid?" ("base", "base", "base", "mid")
            her "I'm a bit confused..." ("base", "base", "base", "mid")
            gen "Yes [name_hermione_genie]... You'll get your points..." ("base", xpos="far_left", ypos="head")

    else: #19+ Not being paid.
        her "Really, [name_genie_hermione]?" ("open", "wide", "worried", "mid")
        gen "That's right! Must be because of all the things you've been doing to help your friends." ("base", xpos="far_left", ypos="head")
        her "Thank heavens... I was so worried..." ("soft", "happyCl", "worried", "mid")
        gen "Of course! Not everyone would have been able to achieve what you have..." ("base", xpos="far_left", ypos="head")
        her @ tears soft "*sob*... I guess not..." ("angry", "base", "base", "mid")
        gen "It takes some real strength and determination!" ("base", xpos="far_left", ypos="head")
        her "You really think so [name_genie_hermione]?" ("soft", "narrow", "base", "down")
        gen "I do! you're a good girl, Miss Granger..." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
        gen "Once Gryffindor wins the house cup, everyone will be so happy." ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]... I can't wait!" ("base", "happyCl", "base", "mid")
        gen "*Sigh*" ("base", xpos="far_left", ypos="head") # Genie sighs because he was hoping that Hermione would present herself or something because the collar did nothing.
        her "Is something the matter, [name_genie_hermione]?" ("base", "happyCl", "base", "mid")
        gen "It's nothing. Don't worry about it." ("base", xpos="far_left", ypos="head")

    if states.her.level < 19:
        $ gryffindor += current_payout
        gen "{number=current_payout} points to Gryffindor, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]." ("base", "happy", "base", "mid")

    ## End section ##

    her "Is that everything, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Yes, that shall do for today..." ("base", xpos="far_left", ypos="head")
    her "Alright then." ("base", "base", "base", "R")

    $ hermione.equip(her_outfit_last)
    with fade

    if not her_neckwear_good_girl_collar.unlocked:
        $ her_neckwear_good_girl_collar.unlock()

        gen "Oh... You can keep that collar, by the way..." ("base", xpos="far_left", ypos="head")
        her "Really?" ("open", "base", "base", "mid")
        gen "Yeah, sure, Why not... Should give me a good reminder to be more careful making decisions..." ("base", xpos="far_left", ypos="head")
        gen "(Maybe I should sell her some more favours until I give her another one...)" ("base", xpos="far_left", ypos="head")
        her "Thank you [name_genie_hermione]..." ("base", "base", "base", "mid")
        gen "(At least I can enjoy watching her wearing it...)" ("base", xpos="far_left", ypos="head")
        her "Just let me know if you need anything." ("open", "happy", "base", "mid")

        call give_reward("A new collar has been unlocked in the wardrobe!")

    if game.daytime:
        her "Have a Good day." ("grin", "base", "base", "mid")
    else:
        her "Have a Good night." ("grin", "base", "base", "mid")
    gen "You too [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    jump end_hermione_event
