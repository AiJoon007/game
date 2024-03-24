
# Maid Job
label her_maid_job:

    if not states.her.ev.maid.intro_complete:
        $ states.her.ev.maid.intro_complete = True
        her "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
        gen "I think it's about time we got someone to clean up this place." ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]?" ("open", "squint", "base", "mid", xpos="right", ypos="base")
        gen "Don't you think it's about time that someone set a good example and cleaned up this castle?" ("base", xpos="far_left", ypos="head")
        if states.her.level < 4:
            her "Finally you've come to your senses..." ("base", "closed", "base", "mid")
            her "Of course I'll help!" ("base", "base", "base", "mid")
            gen "Great, then I've got this maid's outfit for you!" ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "narrow", "base", "down")
            her "What is this?!" ("clench", "squint", "base", "down")
            gen "A maid's outfit!" ("base", xpos="far_left", ypos="head")
            gen "You'll need it for the cleaning you're about to do." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione], this isn't what I thought you meant..." ("disgust", "squint", "base", "mid")
            gen "You'll get paid in points, of course..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*..." ("upset", "narrow", "base", "R")
            gen "And I suppose you'll technically be working for me, so you can get paid for your work..." ("base", xpos="far_left", ypos="head")
            her "That's good I suppose..." ("open", "squint", "base", "R")
            gen "Although I'm technically not supposed to hire students, so I'll have to hold on to your payment for now." ("base", xpos="far_left", ypos="head")
            her "Right..." ("angry", "squint", "base", "mid")
            gen "So... You'll do it?" ("base", xpos="far_left", ypos="head")
            her "I suppose I could..." ("normal", "squint", "base", "R")
            gen "Great!" ("base", xpos="far_left", ypos="head")
            gen "Return here in the evening to drop off your payment and tell me how it went." ("base", xpos="far_left", ypos="head")
            if not is_in_lead(gryffindor):
                her "Alright..." ("open", "base", "base", "mid")
                her "Let me just put this on..." ("angry", "squint", "base", "mid")
            else: #Gryffindor is in the lead
                her "Oh, you want me to do it now?" ("open", "squint", "base", "mid")
                gen "Of course, why else would I bring it up?" ("base", xpos="far_left", ypos="head")
                her "But... We're in the lead right now." ("angry", "base", "base", "mid")
                gen "So?" ("base", xpos="far_left", ypos="head")
                her "So... There's no need for me to earn any points at the moment." ("grin", "base", "base", "mid")
                gen "Right..." ("base", xpos="far_left", ypos="head")

                hide hermione_main
                with d3

                call tutorial("points")

                $ _event.cancel()
                jump hermione_favor_menu.odd_jobs
                
        elif states.her.level < 13:
            her "Cleaned up, [name_genie_hermione]?" ("angry", "base", "base", "mid")
            gen "Yes, so you better put this on..." ("base", xpos="far_left", ypos="head")
            her "A maid's outfit?" ("angry", "narrow", "base", "down")
            her "Of course this is what you meant..." ("angry", "narrow", "base", "mid")
            gen "You'll get paid in points, of course." ("base", xpos="far_left", ypos="head")
            her "*Hmm*...{w=0.4} Alright, In that case, I suppose I could do it." ("angry", "closed", "base", "mid")
            gen "Excellent... Although you'll have to return any monetary payments to me." ("base", xpos="far_left", ypos="head")
            her "I do?" ("clench", "base", "base", "mid")
            gen "You think I could just hire students to do these things?" ("base", xpos="far_left", ypos="head")
            her "*Ehm*..." ("angry", "base", "base", "mid")
            gen "No, I think it'd be best if I held on to it for now." ("base", xpos="far_left", ypos="head")
            her "Right..." ("open", "base", "base", "mid")
            gen "Return here in the evening to drop off your payment and tell me how it went." ("base", xpos="far_left", ypos="head")
            if not is_in_lead(gryffindor):
                her "Alright..." ("open", "squint", "base", "R")
                her "Let me just put this on..." ("angry", "squint", "base", "mid")
            else: #Gryffindor is in the lead
                her "Oh, you want me to do it now?" ("open", "squint", "base", "mid")
                gen "Of course, why else would I bring it up?" ("base", xpos="far_left", ypos="head")
                her "But... We're in the lead right now." ("angry", "base", "base", "mid")
                gen "So?" ("base", xpos="far_left", ypos="head")
                her "So... There's no need for me to earn any points at the moment." ("grin", "base", "base", "mid")
                gen "Right..." ("base", xpos="far_left", ypos="head")
                hide hermione_main
                with d3

                call tutorial("points")

                $ _event.cancel()
                jump hermione_favor_menu.odd_jobs
        else: #13+
            her "I'm not sure what you--" ("angry", "base", "base", "mid")
            gen "I want you to put this on!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "A maid's outfit?" ("angry", "narrow", "base", "down")
            gen "Yep!" ("base", xpos="far_left", ypos="head")
            gen "You'll get paid in points, of course." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... Why not... This castle could use some cleaning where the house elves can't reach." ("open", "closed", "base", "mid")
            gen "That's the spirit!" ("base", xpos="far_left", ypos="head")
            gen "Just make sure you return here in the evening to give me your payments and tell me how it went." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Give you my what?" ("open", "base", "base", "mid")
            gen "Payments." ("base", xpos="far_left", ypos="head")
            gen "This will have to stay off the books, so I'll have to hold on to it for now." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... Right..." ("open", "closed", "base", "mid")
            if states.her.level >= 16:
                her @ cheeks blush "Let me just put this on..." ("angry", "base", "base", "mid")
            else:
                if not is_in_lead(gryffindor):
                    her @ cheeks blush "Let me just put this on..." ("angry", "base", "base", "mid")
                else: #Gryffindor in the lead
                    her "Oh, you want me to do it now?" ("open", "squint", "base", "mid")
                    gen "Of course, why else would I bring it up?" ("base", xpos="far_left", ypos="head")
                    her "But... We're in the lead right now." ("angry", "base", "base", "mid")
                    gen "So?" ("base", xpos="far_left", ypos="head")
                    her "So... There's no need for me to earn any points at the moment." ("grin", "base", "base", "mid")
                    gen "Right..." ("base", xpos="far_left", ypos="head")
                    hide hermione_main
                    with d3

                    call tutorial("points")

                    $ _event.cancel()
                    jump hermione_favor_menu.odd_jobs

    else:
        her "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
        random:
            gen "I'd like you to go out and make me some money... *Err*... I mean, go out and earn some points." ("base", xpos="far_left", ypos="head")
            gen "Time to earn some more points for your house, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "Time for you to head out and help clean the castle." ("base", xpos="far_left", ypos="head")
            gen "I've got a feather duster with your name on it, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "Put this on for me will you?" ("base", xpos="far_left", ypos="head")

        if states.her.level < 4:
            if not is_in_lead(gryffindor):
                her "*Hmph!*..." ("upset", "base", "annoyed", "mid", xpos="right", ypos="base")
            else:
                her "No, thank you, [name_genie_hermione]." ("open", "squint", "base", "mid", xpos="right", ypos="base")
                gen "What do you mean, no?" ("angry", xpos="far_left", ypos="head")
                her "We're in the lead right now... There's no need for me to earn any points at the moment." ("grin", "base", "base", "mid")
                gen "Right..." ("base", xpos="far_left", ypos="head")
                hide hermione_main
                with d3

                call tutorial("points")

                $ _event.cancel()
                jump hermione_favor_menu.odd_jobs
        elif states.her.level < 16:
            if not is_in_lead(gryffindor):
                her "Alright..." ("angry", "base", "base", "mid", xpos="right", ypos="base")
            else:
                her "We're in the lead right now... There's no need for me to earn any points at the moment." ("grin", "base", "base", "mid", xpos="right", ypos="base")
                gen "Right..." ("base", xpos="far_left", ypos="head")
                hide hermione_main
                with d3

                call tutorial("points")

                $ _event.cancel()
                jump hermione_favor_menu.odd_jobs
        elif states.her.level < 22:
            her "Of course, [name_genie_hermione]..." ("base", "squint", "base", "mid", xpos="right", ypos="base")
        else: #22+
            her "As you wish, [name_genie_hermione]." ("base", "base", "base", "mid",xpos="right",ypos="base")

    show screen blkfade
    with d5
    # Setup
    $ maid_outfit_ITEM.used = True
    play sound "sounds/cloth_sound.ogg"
    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_maid)
    hide screen blkfade
    with d5

    pause 2.5
    hide hermione_main
    with d3

    gen "Off you go then..." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    $ states.her.busy = True
    $ current_job = "maid"

    jump main_room_menu

label her_maid_job_return:

    python:
        progress_factor = math.log(states.her.tier + states.cho.tier + states.ton.tier + states.lun.tier + game.day)
        payment = int(progress_factor * random_gold)
    
    $ hermione.equip(her_outfit_maid)

    call her_walk(action="enter", xpos="mid", ypos="base")

    gen "[name_hermione_genie]... Did you complete your task?" ("base", xpos="far_left", ypos="head")
    her "I did." ("open", "base", "base", "mid", xpos="right", ypos="base", trans=dissolve)

    menu:
        "\"How was your day?\"":
            if states.her.level < 4:
                random:
                    block:
                        her "Do I really have to keep doing this?" ("normal", "narrow", "base", "R_soft")
                        gen "What do you mean, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                        her "It's so degrading... I had to clean other students' dorms!" ("open", "narrow", "worried", "down")
                        gen "You can stop any time." ("base", xpos="far_left", ypos="head")
                        her "I can?" ("soft", "narrow", "worried", "mid_soft")
                        gen "Certainly, I'll just get one of those Slytherin floozies that you are always on about." ("grin", xpos="far_left", ypos="head")
                        gen "I'm sure that they'd jump at the chance to make some points for their house." ("base", xpos="far_left", ypos="head")
                        gen "They'd probably even do it for next to nothing, if not free." ("base", xpos="far_left", ypos="head")
                        her "Fine, I get your point...." ("upset", "closed", "base", "mid")
                        her "Can I get my points now?" ("angry", "closed", "angry", "mid")
                        gen "Certainly, ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
                    block:
                        her "I think you need to start enforcing harsher punishment for sexual harassment." ("mad", "base", "angry", "mid")
                        gen "Why's that?" ("base", xpos="far_left", ypos="head")
                        her "Some Slytherin boys kept wolf whistling at me as I was scrubbing the floors." ("mad", "base", "angry", "mid")
                        gen "Just see it as a compliment [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                        her "As if any Slytherin would be capable of such a thing... They're just doing it to embarrass me." ("mad", "base", "angry", "mid")
                        gen "Whatever you say [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                        her "*Hmph*...{w=0.4} Can I get my points now?" ("angry", "closed", "angry", "mid")
                        gen "Certainly, ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
                    block:
                        her "Dreadful... Peeves kept blowing air underneath my skirt!" ("clench", "narrow", "base", "down")
                        gen "Who?" ("base", xpos="far_left", ypos="head")
                        her "That da--{w=0.3} That poltergeist!" ("angry", "closed", "annoyed", "mid")
                        her "It's bad enough that I had to clean the corridors..." ("upset", "happy", "annoyed", "mid")
                        her @ cheeks blush "But the fact that he's able to do that thanks to this dress..." ("clench", "closed", "base", "mid")
                        gen "Doesn't your regular uniform have a skirt?" ("base", xpos="far_left", ypos="head")
                        her "..." ("disgust", "squint", "base", "mid")
                        her "Can I have my points now?" ("clench", "narrow", "base", "R")
                        gen "Of course... Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
            elif states.her.level < 13:
                random:
                    block:
                        her "It was as normal a day of cleaning rooms could be." ("open", "base", "base", "mid")
                        her "Although considering that I'm supposed to be in class during the day, I guess it's not that normal." ("soft", "base", "base", "R")
                        gen "Don't worry [name_hermione_genie], you'll get your points." ("base", xpos="far_left", ypos="head")
                        gen "Just think of how happy your friends will be when they win the house cup this year." ("base", xpos="far_left", ypos="head")
                        her "I suppose..." ("open", "base", "base", "R")
                        gen "Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
                    block:
                        her "It was fine I suppose..." ("soft", "base", "base", "R")
                        gen "Nothing else to tell me? What were you tasked to do today?" ("base", xpos="far_left", ypos="head")
                        her "*Ehm*..." ("open", "narrow", "base", "down")
                        her "Well, I was tasked to clean the boys' changing room..." ("angry", "closed", "base", "mid")
                        gen "Right..." ("base", xpos="far_left", ypos="head")
                        her "They really should've told me when... How am I supposed to know when they're not using it?" ("clench", "narrow", "base", "down")
                        gen "Ten points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                        her "..." ("angry", "base", "base", "mid")
                    block:
                        her "Professor Snape had me sort his potion ingredients all day..." ("open", "narrow", "base", "mid")
                        gen "Doesn't sound too bad..." ("base", xpos="far_left", ypos="head")
                        her "He asked me to put everything on the highest shelves..." ("disgust", "narrow", "base", "mid")
                        her "When I asked him why, he told me not to question his organization system..." ("angry", "narrow", "base", "mid")
                        her "As if he had one to begin with... He was probably just wanted a peek up my skirt." ("open", "closed", "annoyed", "mid")
                        her "..." ("upset", "narrow", "base", "mid")
                        her "Can I have my points now?" ("angry", "narrow", "base", "mid")
                        gen "Of course... Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
            elif states.her.level < 22:
                random:
                    block:
                        her "It was pretty uneventful." ("open", "base", "base", "R")
                        her "I suppose I should feel more annoyed by the other students staring at me, but it doesn't bother me that much." ("open", "base", "base", "R")
                        gen "Good to hear." ("base", xpos="far_left", ypos="head")
                        her "I am helping the school after all..." ("base", "closed", "base", "mid")
                        gen "That you are... Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
                    block:
                        her "I had to dust all the shelves in the library today." ("open", "closed", "base", "mid")
                        gen "That doesn't sound too bad..." ("base", xpos="far_left", ypos="head")
                        her "Well I got yelled at by Miss Pince for no reason." ("upset", "squint", "base", "mid")
                        her "She kept telling me that the other students needed to work on their studies and that I kept distracting them." ("clench", "narrow", "base", "mid")
                        her "Yet she didn't tell me to stop cleaning..." ("annoyed", "narrow", "base", "mid")
                        gen "Sound like a job well done to me... Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
                        her "..." ("angry", "squint", "base", "mid")
                    block:
                        her "Pretty uneventful." ("open", "base", "base", "R")
                        her "I cleaned the prefects' bathroom today, so there weren't really that many people around." ("soft", "base", "base", "mid")
                        her @ cheeks blush "Although one of the mermaid portraits kept blowing me kisses." ("open", "squint", "base", "R")
                        gen "Was she attractive?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("normal", "squint", "base", "mid")
                        her @ cheeks blush "As attractive as a mermaid can be I suppose..." ("normal", "squint", "base", "mid")
                        gen "Nicely done... Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
            else: #22+
                random:
                    block:
                        her @ cheeks blush "It was fine... I cleaned the staffroom today..." ("open", "closed", "base", "mid")
                        her @ cheeks blush "Professor Snape seemed to think it was really funny to have me Scourgify his robes constantly as he continued spilling tea on himself..." ("angry", "narrow", "base", "R")
                        gen "Well, I suppose that comes with the job." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "That's what he said..." ("angry", "narrow", "base", "down")
                        gen "Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
                    block:
                        her "Good, although I didn't really get much work done today." ("open", "narrow", "base", "R")
                        gen "Oh...{w=0.4} Why's that?" ("base", xpos="far_left", ypos="head")
                        her "Well...{w=0.4} I was asked to help the house elves and every time I started doing something one of them would come and do it for me." ("angry", "squint", "base", "mid")
                        her "Constantly apologizing for not having done it yet and bowing to me..." ("open", "narrow", "base", "mid")
                        gen "(Uh-oh...)" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "It was kind of cute to be honest." ("base", "squint", "base", "R")
                        gen "Well then, I assume you still got paid?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Oh...{w=0.4} Yes [name_genie_hermione]..." ("angry", "base", "base", "mid")
                        gen "Great! Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
                    block:
                        gen "Tell me what you've been doing." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "I've been cleaning professor Tonks' office..." ("open", "base", "base", "mid")
                        her @ cheeks blush "The things she keeps in there..." ("angry", "narrow", "base", "down")
                        her @ cheeks blush "Why I hope none of the other students get detention with her." ("open", "closed", "base", "mid")
                        gen "Found anything interesting?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "*Hmm*... Not sure if she'd like it if I told you..." ("angry", "narrow", "base", "R")
                        gen "(As if I couldn't already guess...)" ("base", xpos="far_left", ypos="head")
                        gen "Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")

        "-Dismiss her-":
            gen "Great, then that will be all for now." ("base", xpos="far_left", ypos="head")
            gen "Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")

    her "Thank you, [name_genie_hermione]." ("open", "base", "base", "mid")
    her "Here's the payment." ("open", "base", "base", "mid")
    nar "You receive {number=payment} gold coins."

    $ gryffindor+= 10
    $ game.gold += payment

    call her_walk(action="leave")

    $ hermione.equip(her_outfit_last)

    $ states.her.busy = True
    $ current_job = None

    jump main_room_menu

#Send Hermione to work, promoting the card game.

