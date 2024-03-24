

### Tonks Hangout Event ###

label tonks_hangout:

    call setup_fireplace_hangout(char="tonks")##

    $ tonks.strip("robe") # Takes off robe

    if firewhisky_ITEM.owned >= 1:
        $ firewhisky_ITEM.owned -= 1

    $ ton_eventqueue_hangouts_drinking.start()

    label tonks_hangout_continue:
        hide screen bld1
        with fade
        call bld

    ### Intro Events ###

    # Hermione
    if states.her.ev.intro.e5_complete and not states.her.ev.intro.convinced:
        jump nt_he_hermione_E1 # Persuade Hermione to sell favors.

    # Susan
    if states.her.tier >= 2 and states.ton.level >= 20 and not states.ton.ev.hangouts.susan_e1:
        $ ag_event_pause += 2 # Astoria intro happens in 2 days.
        jump nt_he_susan_E1 # Starts Susan/Astoria intro.

    # Astoria
    if states.ast.ev.intro.e3_complete and not states.ton.ev.hangouts.astoria_e1:
        jump nt_he_astoria_E1

    # (Quidditch) Ask Tonks for help with Slytherins.
    if states.cho.ev.quidditch.e6_complete and not states.cho.ev.quidditch.e8_complete:
        jump cho_quid_E8

    ### General Events ###

    if states.her.tier >= 2 and not states.ton.ev.hangouts.favors_e1:
        jump nt_he_favors_E1 # Unlocks Public Requests.
    if states.ton.public_level >= 4 and states.ton.level >= 20 and not states.ton.ev.hangouts.favors_e2:
        jump nt_he_favors_E2 # Tonks Tier 2 available.


    ### Snape Stories ###

    $ ton_eventqueue_hangouts_story.start()

    label end_tonks_hangout:

    $ d_flag_01 = "afternoon" if game.daytime else "evening"

    if states.ton.level < 100:
        call notes
        nar "You spend the [d_flag_01] hanging out with Tonks.\n>Your relationship with her has improved."
    else:
        nar "You spend the [d_flag_01] hanging out with Tonks."

    label end_tonks_hangout_points:

    if states.ton.level < 100: # max
        if states.fireplace_started: # Tonks is feeling hot.
            $ states.ton.level += 2

        if game.difficulty < 2:      #Easy difficulty
            $ states.ton.level += 5
        elif game.difficulty == 2:   #Normal
            $ states.ton.level += 4
        else:                        #Hardcore
            $ states.ton.level += 3

    if states.ton.level > 100:
        $ states.ton.level = 100

    $ hufflepuff += renpy.random.randint(5, 15)

    $ tonks.wear("all")
    $ chair_OBJ.hidden = False
    $ fireplace_OBJ.foreground = None

    hide screen with_tonks_animated

    if game.daytime:
        jump night_start
    else:
        jump day_start


label nt_he_wine_intro:
    call bld
    gen "Care for a drink?" ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "Of course, [name_genie_tonks]." ("base", "base", "shocked", "mid", ypos="head", flip=False)
    ton "Hit me!" ("horny", "base", "base", "down")
    pause.1

    # Show wine
    call give_gift("You hand over the bottle you found in the cupboard to professor Tonks...", wine_ITEM)

    ton "Wine?" ("open", "base", "raised", "down")
    ton "Don't you have anything stronger?" ("upset", "base", "base", "R")
    gen "Like what?" ("base", xpos="far_left", ypos="head")
    ton "How about firewhisky? Got any of that?" ("open", "base", "base", "mid")
    gen "I'm afraid not..." ("base", xpos="far_left", ypos="head")
    ton "What a bummer. I guess wine will do for today." ("upset", "base", "worried", "down")
    gen "(Maybe there is some of that other stuff stored in the cupboard as well...)" ("base", xpos="far_left", ypos="head")

    # Make firewhisky available in the cupboard and store
    $ firewhisky_ITEM.unlocked = True
    $ states.ton.ev.hangouts.wine_intro = True

    jump tonks_hangout_continue


label nt_he_firewhisky_intro:
    call bld
    gen "Look what I've got!" ("grin", xpos="far_left", ypos="head")
    pause.1

    # Show firewhisky
    call give_reward("You hand over a bottle of firewhisky to Tonks...", gift="interface/icons/firewhisky.webp", sound=False)

    ton "Finally, the good stuff!" ("horny", "base", "base", "down", ypos="head", flip=False)
    ton "I'm glad you brought out some firewhisky this time..." ("base", "base", "base", "down")
    ton "Wine makes me giggly, and hinders my judgment." ("base", "base", "base", "L")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton "Got a frog in your throat?" ("open", "base", "raised", "mid")
    gen "No, I was just waiting for an opening." ("base", xpos="far_left", ypos="head")
    ton "Sorry, I guess I talk a lot once I get going..." ("mad", "base", "shocked", "R")
    ton "Bottoms up." ("horny", "base", "base", "down")
    play sound "sounds/gulp.ogg"
    ton "*Gulp*{w=0.6}{nw}" ("base", "closed", "worried", "mid", trans=hpunch)
    ton "*Cough* *Cough*" ("open", "happyCl", "shocked", "stare")
    ton "Yeah, that was a mistake." ("mad", "base", "base", "down")
    gen "I don't drink whisky that often, but even I know not to down it in one..." ("base", xpos="far_left", ypos="head")
    ton "*Mmm*... that's the stuff." ("horny", "narrow", "base", "down")
    gen "Are you even listening?" ("base", xpos="far_left", ypos="head")

    jump tonks_hangout_continue


label nt_he_firewhisky_E1:
    call bld
    gen "Another glass of firewhisky?" ("base", xpos="far_left", ypos="head")
    ton "Fill 'er up." ("horny", "base", "base", "up", ypos="head", flip=False)
    ton "..." ("base", "base", "shocked", "down")
    ton "A little bit more..." ("open", "base", "raised", "down")
    ton "A bit more..." ("horny", "base", "angry", "down")
    ton "That's it, cheers." ("base", "base", "base", "mid")

    if not _event_completed:
        if game.daytime:
            gen "Boring lessons ahead?" ("base", xpos="far_left", ypos="head")
            ton "Not particularly, why?" ("open", "base", "base", "mid")
            gen "You might regret going back to classes after drinking this much." ("base", xpos="far_left", ypos="head")
            ton "Oh, don't you worry, [name_genie_tonks]." ("silly", "happyCl", "base", "mid")
            ton "I could down this entire bottle without anybody being able to notice a thing." ("horny", "base", "base", "L")
            gen "You're one glass in and swaying like a buoy..." ("base", xpos="far_left", ypos="head")
            ton "*Hick* Oh well..." ("open", "base", "base", "ahegao", trans=hpunch)
            ton "No risk, no fun!" ("horny", "base", "base", "mid")
        else:
            gen "Long day?" ("base", xpos="far_left", ypos="head")
            ton "Not in particular, why?" ("open", "wide", "raised", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "No reason..." ("base", xpos="far_left", ypos="head")

    jump tonks_hangout_continue


label nt_he_firewhisky_E2:
    call bld
    gen "More firewhisky?" ("base", xpos="far_left", ypos="head")
    ton "Thought you'd never ask..." ("horny", "base", "base", "down", ypos="head", flip=False)

    jump tonks_hangout_continue


label nt_he_firewhisky_E3:
    call bld
    gen "Want to get drunk?" ("base", xpos="far_left", ypos="head")

    ton "Of course." ("base", "narrow", "shocked", "down", ypos="head", flip=False)
    if game.daytime:
        ton "I'm not going to regret this, am I?" ("clench", "base", "raised", "downR")
        ton "Hopefully my students won't notice..." ("grin", "narrow", "base", "downR")
    else:
        ton "I'd never say no to that!" ("horny", "base", "base", "down")

    jump tonks_hangout_continue


label nt_he_firewhisky_E4:
    ton "Bottoms up." ("base", "narrow", "base", "mid", ypos="head", flip=False)
    play sound "sounds/gulp.ogg"
    ton "*Gulp*{w=0.8}{nw}" ("scream", "closed", "base", "mid")
    play sound "sounds/gulp.ogg"
    ton "*Gulp*{w=0.8}{nw}" ("scream", "closed", "worried", "mid")
    play sound "sounds/gulp.ogg"
    ton "*Gulp*{w=0.8}{nw}" ("scream", "closed", "worried", "mid")
    ton "*Aaaaaaaahhhh!!!*..." ("silly", "closed", "base", "ahegao", trans=vpunch)
    gen "....................." ("base", xpos="far_left", ypos="head")

    jump tonks_hangout_continue



### Events ###

label nt_he_favors_E1:
    ton "So, [name_genie_tonks]... What's the going rate around here, then?" ("open", "base", "raised", "mid", ypos="head", flip=False)
    gen "Going rate?" ("base", xpos="far_left", ypos="head")
    ton "How much do you pay your students to fool around?" ("base", "narrow", "annoyed", "mid")
    gen "Oh... It depends on what you want them to do." ("base", xpos="far_left", ypos="head")
    ton "How much for a lap dance?" ("soft", "narrow", "raised", "mid")
    gen "Again, it depends on the student." ("base", xpos="far_left", ypos="head")
    ton "..." ("upset", "base", "base", "R")
    gen "But if I had to guess, I'd say about twenty-five points." ("base", xpos="far_left", ypos="head")
    ton "Unbelievable that you've managed to convince these girls to offer themselves up to you, for a bunch of imaginary points..." ("base", "narrow", "annoyed", "R")
    gen "Works for the internet..." ("base", xpos="far_left", ypos="head")
    ton "The what?" ("open", "base", "raised", "mid")
    gen "A place you go when you want to procrastinate..." ("base", xpos="far_left", ypos="head")
    gen "Or you happen to be sitting on the toilet..." ("base", xpos="far_left", ypos="head")
    gen "Anyway, you can't just ask for a lap dance straight away, You have to butter them up first." ("base", xpos="far_left", ypos="head")
    ton "How so?" ("mad", "base", "raised", "mid")
    gen "Well, most of them aren't going to do whatever you say from the get go..." ("base", xpos="far_left", ypos="head")
    gen "You have to slowly earn their trust over time and start out small..." ("base", xpos="far_left", ypos="head")
    ton "*Awww*... Really? Can't I just cheat a bit?" ("upset", "base", "worried", "L")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Just take it slow, I'm sure you'll find a cute boy who'll be willing to do whatever you want anyway." ("base", xpos="far_left", ypos="head")
    ton "..." ("upset", "base", "base", "R")
    ton "But what if I want a girl?" ("horny", "base", "raised", "mid")
    gen "(...!)" ("angry", xpos="far_left", ypos="head")
    gen "Whatever floats your boat." ("base", xpos="far_left", ypos="head")

    $ states.ton.requests_unlocked = True
    call popup("You can now ask Tonks to do \"Public Requests\" with her students!", "Congratulations!", "interface/icons/head/tonks.webp")

    $ states.ton.ev.hangouts.favors_e1 = True

    jump end_tonks_hangout_points


label nt_he_favors_E2:
    ton "You know, [name_genie_tonks]... I overheard a couple of students whispering about me..." ("open", "base", "raised", "mid", ypos="head", flip=False)
    gen "Finally..." ("grin", xpos="far_left", ypos="head")
    ton "I walked past a group of boys the other day..." ("open", "base", "base", "R")
    ton "One straight up called me a slut, whilst the others snickered at me..." ("open", "base", "base", "down")
    gen "Oh?" ("base", xpos="far_left", ypos="head")
    ton "So, I turned around and told him that such behaviour could earn him detention..." ("base", "wink", "base", "mid")
    ton "Of course, word has it that detention with me is rather enjoyable..." ("horny", "base", "base", "mid")
    ton "And I believe that group of boys knew that fact as well..." ("base", "base", "angry", "R")
    gen "Sounds like it's about time we step it up a notch." ("base", xpos="far_left", ypos="head")
    ton "And behave even riskier?" ("open", "shocked", "shocked", "mid")
    ton "Who do you think you're asking, exactly?" ("open", "closed", "base", "mid")
    gen "So...{w=0.3} Is that a yes?" ("base", xpos="far_left", ypos="head")
    ton "Fuck yes!" ("grin", "narrow", "shocked", "mid")
    ton "I want those boys to call me all sorts of names... And do it straight to my face!" ("horny", "base", "angry", "mid")
    gen "Promise me you'll reward them if they do." ("grin", xpos="far_left", ypos="head")
    ton "I promise, [name_genie_tonks]." ("base", "wink", "base", "mid")

    call popup("Tonks can now reach the next level!", "Congratulations!", "interface/icons/head/tonks.webp", sound=False)

    $ states.ton.ev.hangouts.favors_e2 = True

    jump end_tonks_hangout_points



### Tonks Auror Stories ###

label nt_he_story_intro_E1:
    ton "Thanks for accepting my job application by the way." ("base", "base", "base", "mid", ypos="head", flip=False)
    gen "I didn't really have that much choice in the matter." ("base", xpos="far_left", ypos="head")
    ton "Oh, yeah..." ("grin", "narrow", "base", "downR")
    ton "..." ("annoyed", "base", "base", "R")
    ton "I'll do well...{w=0.4} you'll see." ("open", "base", "base", "down")
    ton "After all, I was taught by one of the best aurors there is." ("base", "base", "raised", "mid")
    ton "So, don't get me wrong... I do wish to teach those students a couple of useful things while I'm here..." ("annoyed", "base", "shocked", "mid")
    ton "Teaching a class of beginners should be a breeze." ("base", "narrow", "base", "mid")
    gen "I never said I doubted your abilities." ("base", xpos="far_left", ypos="head")
    ton "Maybe I'll give you a demonstration some day..." ("horny", "base", "raised", "mid")
    ton "And I'm not talking about my intellectual abilities..." ("horny", "base", "base", "down")
    gen "I'm a well for all kinds of knowledge!" ("grin", xpos="far_left", ypos="head")

    if game.daytime:
        ton "Anyway, I have to go prepare for classes." ("open", "base", "base", "R")
    else:
        ton "Anyway, I think I'm gonna go hit the sack." ("open", "base", "base", "R")

    if _events_completed_any: # We're past the wine intro
        gen "There's more firewhisky where this came from, so feel free to stop by any time to talk about your progress." ("base", xpos="far_left", ypos="head")
        ton "I'll never say no to a free drink." ("base", "base", "base", "down")
    else:
        gen "There's more wine where this came from, so feel free to stop by any time to talk about your progress." ("base", xpos="far_left", ypos="head")
        ton "Please, no more wine! You better have some firewhisky next time." ("open", "base", "worried", "mid")
        gen "Oh, right. I'll make sure to get some." ("base", xpos="far_left", ypos="head")
        ton "Good!" ("base", "base", "base", "mid")

    ton "And I'll keep you updated on the academics as usual." ("base", "base", "base", "mid")
    gen "(That's not the kind of progress I meant...)" ("base", xpos="far_left", ypos="head")

    jump end_tonks_hangout


label nt_he_story_intro_E2:
    call bld
    gen "You mentioned an auror last time if I'm not mistaken." ("base", xpos="far_left", ypos="head")
    ton "Moody?" ("annoyed", "wide", "shocked", "mid", ypos="head", flip=False)
    gen "Not in particular." ("base", xpos="far_left", ypos="head")
    ton "What?" ("mad", "base", "raised", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton "You talking about Mad-eye?" ("upset", "base", "raised", "mid")
    gen "I can see perfectly fine, dear." ("base", xpos="far_left", ypos="head")
    ton "I'm talking about Alastor Moody, my mentor." ("open", "narrow", "annoyed", "mid")
    gen "Oh, of course." ("base", xpos="far_left", ypos="head")
    gen "(His parents must have hated him...)" ("base", xpos="far_left", ypos="head")
    gen "Anything you'd like to tell me about him?" ("base", xpos="far_left", ypos="head")
    ton "Well, he's a bit of a weirdo, but he knows his stuff." ("open", "closed", "annoyed", "mid")
    ton "I guess if you're as paranoid as him, you'll end up knowing everything there is about the craft..." ("open", "base", "base", "R")
    gen "Paranoid of what?" ("base", xpos="far_left", ypos="head")
    ton "Dark wizards." ("mad", "narrow", "base", "mid")
    gen "So...{w=0.3} He's a racist?" ("base", xpos="far_left", ypos="head")
    ton "No, but he's old... I think he should just retire, to be honest." ("open", "base", "base", "downR")
    ton "His methods have gotten progressively more nefarious..." ("open", "narrow", "annoyed", "R")
    ton "Some would argue he should lock up himself, for all the things that he did to catch his targets..." ("mad", "narrow", "base", "down")
    gen "And you?" ("grin", xpos="far_left", ypos="head")
    ton "Me? What about me?" ("upset", "narrow", "annoyed", "mid")
    gen "You wouldn't say what we do is unethical as well?" ("base", xpos="far_left", ypos="head")
    ton "Did you start drinking before I got here?" ("open", "narrow", "annoyed", "L")
    gen "I never stopped..." ("base", xpos="far_left", ypos="head")
    ton "..." ("annoyed", "closed", "base", "up")

    jump end_tonks_hangout


label nt_he_story_intro_E3:
    ton "Do you always happen to have a bottle ready for me?" ("base", "base", "raised", "down")
    gen "For you, always." ("grin", xpos="far_left", ypos="head")
    ton "I don't even have to visit the Hog's Head to get a drink anymore..." ("base", "narrow", "annoyed", "R")
    gen "Why go anywhere when you've got a magic cupboard that fills itself with alcohol." ("base", xpos="far_left", ypos="head")
    ton "It does?" ("open", "wide", "raised", "mid")
    gen "At least I think that's how it works..." ("base", xpos="far_left", ypos="head")
    gen "I may be a Genie, but I can't just turn water into wine... or whisky." ("base", xpos="far_left", ypos="head")
    gen "(At least not in this world...)" ("base", xpos="far_left", ypos="head")
    ton "Yeah, that would be impressive." ("silly", "happyCl", "base", "mid")
    ton "I haven't found a single wizard that could do that." ("open", "closed", "shocked", "mid")
    gen "Ah yes. Because all those cunning bachelors are already taken...{w} or gay..." ("base", xpos="far_left", ypos="head")
    ton "No. Single as in... No one can do it." ("open", "narrow", "base", "mid")
    ton "It's almost impossible to summon drinks and food out of thin air." ("open", "base", "base", "R")
    ton "The best they can do is conjure water out of the surrounding humidity." ("upset", "base", "base", "R")
    gen "That's oddly limiting... Genies can conjure food with a snap of a finger." ("base", xpos="far_left", ypos="head")
    ton "I'm sure you could..." ("silly", "happyCl", "base", "mid")

    nar "You brag about your almighty powers in front of the witch..."

    jump end_tonks_hangout


label nt_he_story_intro_E4:
    ton "I've been so busy lately... The days here fly by faster than a Firebolt." ("open", "closed", "worried", "mid", ypos="head", flip=False)
    gen "I'm not sure I know that... Spell?" ("base", xpos="far_left", ypos="head")
    ton "It's a broom..." ("upset", "base", "base", "mid")
    gen "Oh, I see... I'm not really that into brooms." ("base", xpos="far_left", ypos="head")
    gen "Or anything that is inconveniently stiff and long to ride on..." ("base", xpos="far_left", ypos="head")
    ton "Well, I don't mind that... Most witches don't." ("grin", "base", "base", "R")
    gen "You should ask me about my knowledge of flying carpets instead!" ("grin", xpos="far_left", ypos="head")
    gen "I can tell you everything about the newest model." ("grin", xpos="far_left", ypos="head")
    ton "Do you own one yourself? A flying carpet?" ("silly", "base", "base", "mid")
    gen "No... But a friend of mine does." ("base", xpos="far_left", ypos="head")
    gen "It's more of a pet, actually." ("base", xpos="far_left", ypos="head")
    gen "Technically they are sentient beings..." ("base", xpos="far_left", ypos="head")
    ton "Yes, I've heard of that... How interesting." ("silly", "happyCl", "base", "mid")
    ton "So...{w=0.4} Would you like that? Own a pet, that is..." ("base", "base", "angry", "mid")
    gen "Sure. Why do you ask?" ("base", xpos="far_left", ypos="head")
    ton "Just out of curiosity..." ("horny", "base", "base", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    nar "You keep thinking about what Tonks meant by that, whilst she eyes you up expectantly..."

    jump end_tonks_hangout


label nt_he_story_intro_E5:
    call bld
    gen "You still haven't told me anything about your time as an auror..." ("base", xpos="far_left", ypos="head")
    ton "Well, what would you like to know?" ("open", "wide", "raised", "mid", ypos="head", flip=False)
    gen "That \"moody\" guy taught you, you said. You could start there." ("base", xpos="far_left", ypos="head")
    ton "Well, the job of an auror is a bit different now than how it was ten or so years ago." ("open", "base", "base", "R")
    ton "I studied to become an auror with the hopes of taking down evil wizards." ("annoyed", "base", "annoyed", "down")
    gen "Sounds like a nineties B movie to me." ("base", xpos="far_left", ypos="head")
    ton "A what?" ("normal", "shocked", "raised", "mid")
    gen "Never mind... Continue." ("base", xpos="far_left", ypos="head")
    ton "In any case... That's not at all how the job is anymore." ("mad", "base", "base", "R")
    gen "Was it ever?" ("base", xpos="far_left", ypos="head")
    ton "That's what they told me..." ("annoyed", "base", "annoyed", "R") #'tell' to 'told'
    ton "But right now, it's mostly droves of paperwork." ("open", "closed", "annoyed", "mid")
    ton "Back in the day, they never used to bother with it." ("upset", "base", "base", "mid")
    gen "Don't you have people for that sort of thing?" ("base", xpos="far_left", ypos="head")
    ton "We're our own division, and are supposed to follow strict guidelines set by the ministry." ("open", "closed", "base", "mid")
    ton "There was too much bad stuff happening for anyone to lecture the aurors though..." ("normal", "base", "annoyed", "R")
    gen "Then why did you stay?" ("base", xpos="far_left", ypos="head")
    ton "I'm here, aren't I?" ("upset", "base", "raised", "mid")
    ton "Why do you think I jumped on the opportunity to teach here?" ("open", "base", "base", "mid")
    gen "(You kind of created that opportunity yourself...)" ("base", xpos="far_left", ypos="head")
    ton "I learned a lot, though, and I always wanted to use that knowledge to teach others..." ("base", "narrow", "base", "mid")
    ton "I just didn't think I was up for it yet. Not until I stepped through these halls again..." ("open", "base", "base", "mid")
    ton "It made me realise how much I've missed being here." ("grin", "wide", "shocked", "mid")

    jump end_tonks_hangout


label nt_he_story_E6:
    ton "Did I ever tell you about the time we arrested a vampire?" ("open", "wide", "base", "mid", ypos="head", flip=False)
    gen "You haven't even told me about your \"defence against the dark arts\" training yet, but sure, go ahead..." ("base", xpos="far_left", ypos="head")
    ton "Right... Well, there was this vampire guy." ("soft", "base", "base", "R")
    ton "We spent ages looking for him, and found that he had been disguising himself as a headmaster of a muggle school." ("mad", "narrow", "base", "downR")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton "It was quite disgusting what he was doing to the students actually..." ("annoyed", "closed", "angry", "mid")
    ton "He even brought over some of the teachers... They're never going to be the same..." ("disgust", "closed", "angry", "R")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton "Corrupted... Forever..." ("soft", "closed", "angry", "mid")
    gen "(Not sure if I should feel bad at this point...)" ("base", xpos="far_left", ypos="head")
    ton "Kind of hot, though... don't you think?" ("horny", "wink", "angry", "mid")
    gen "(Never mind...)" ("base", xpos="far_left", ypos="head")
    ton "The immense power vampires have over their prey..." ("horny", "base", "raised", "ahegao")
    ton "It's a shame that they're slaves to their own urges." ("open", "closed", "worried", "mid")
    gen "(Well... there's that bad feeling I felt before.)" ("base", xpos="far_left", ypos="head")
    ton "I get it though. Some aspects of it, at least..." ("upset", "base", "base", "R")

    jump end_tonks_hangout


label nt_he_story_intro_E7:
    call bld
    gen "Now, I'm starting to feel like you've been avoiding the subject of your auror training." ("base", xpos="far_left", ypos="head")
    ton "Is it that obvious?" ("mad", "base", "base", "R", ypos="head", flip=False)
    gen "You brought up vampires last time without even saying hello." ("base", xpos="far_left", ypos="head")
    ton "Vampires are interesting..." ("soft", "base", "worried", "downR")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton "Fine, I didn't want to talk about some of Moody's teaching methods..." ("open", "closed", "base", "mid")
    ton "They tend to be quite... unconventional." ("clench", "base", "base", "R")
    gen "Like how?" ("base", xpos="far_left", ypos="head")
    ton "Well..." ("upset", "base", "shocked", "down")
    ton "Moody very much believed in learning by doing." ("open", "base", "base", "mid")
    gen "Sounds reasonable enough..." ("base", xpos="far_left", ypos="head")
    ton "This is defence against dark magic we're speaking of..." ("open", "base", "raised", "mid")
    ton "Some of the spells and situations he put me in are borderline -- if not completely -- illegal." ("open", "base", "angry", "mid")
    gen "Surely in a controlled environment where there's no harm to both parties..." ("base", xpos="far_left", ypos="head")
    ton "Well... That was true most of the time..." ("clench", "base", "base", "R")
    ton "(I can't believe I'm talking about this...)" ("upset", "base", "worried", "down")
    ton "(The ministry will kick Moody out faster than a Blast-ended Skrewt going off if I'm not careful...)" ("mad", "base", "worried", "R")

    jump end_tonks_hangout


label nt_he_story_E8:
    ton "I'll tell you about this one time when Moody went a bit too far." ("normal", "base", "base", "downR", ypos="head", flip=False)
    gen "Where did this sudden urge of sharing come from?" ("base", xpos="far_left", ypos="head")
    ton "Oh, I've been wanting to spill the beans about this for ages. I just didn't want to get anyone in trouble at the ministry..." ("normal", "closed", "base", "mid")
    gen "What's to say I won't get you into trouble?" ("base", xpos="far_left", ypos="head")
    ton "You won't... Would you?" ("open", "shocked", "worried", "mid")
    gen "No..." ("base", xpos="far_left", ypos="head")
    ton "Right..." ("upset", "closed", "base", "mid")
    ton "Anyway, he once brought in this werewolf that we had put in custody." ("mad", "base", "base", "down")
    gen "He did what?!?" ("angry", xpos="far_left", ypos="head")
    ton "See, I knew you'd react like that." ("disgust", "narrow", "shocked", "down")
    gen "No, I was just taken by surprise... I didn't know they existed." ("base", xpos="far_left", ypos="head")
    ton "Of course they do, silly!" ("soft", "narrow", "annoyed", "R")
    ton "So, he brought in this werewolf... apparently quite harmless comparatively." ("open", "base", "base", "R")
    gen "Compared to what? A dog?" ("base", xpos="far_left", ypos="head")
    ton "Compared to werewolves like Fenrir Greyback..." ("upset", "closed", "angry", "L")
    gen "Oh yeah..." ("base", xpos="far_left", ypos="head")
    gen "That...{w=0.4} Guy..." ("base", xpos="far_left", ypos="head")
    ton "Moody had worked out a deal with this guy..." ("open", "base", "base", "mid")
    ton "To see how I would react in a real life situation where he would turn." ("annoyed", "base", "angry", "mid")
    gen "Turn where?" ("base", xpos="far_left", ypos="head")
    ton "Into a werewolf." ("clench", "closed", "angry", "mid")
    gen "Of course." ("base", xpos="far_left", ypos="head")
    ton "So, the thing is... We hadn't taken into account that it was mating season for them..." ("mad", "narrow", "base", "down")
    gen "You don't say!" ("grin", xpos="far_left", ypos="head")
    ton "The guy wasn't that interested in biting me, that's for sure." ("soft", "base", "base", "downR")
    ton "So you can see why I wasn't so keen on reporting it. More of an embarrassing situation sort of thing than anything else." ("open", "base", "base", "R")
    ton "And it was totally our fault, I should've recognised the signs straight away... When they're turned they're largely driven by their instincts." ("open", "base", "shocked", "down")
    gen "I see." ("base", xpos="far_left", ypos="head")
    ton "Dated him for a while..." ("horny", "base", "base", "R")
    gen "You did what?" ("angry", xpos="far_left", ypos="head")
    ton "Satiated my need for a dominant male relationship for a couple of months, that's for sure..." ("base", "narrow", "angry", "down")
    gen "(That explains a few things...)" ("base", xpos="far_left", ypos="head")

    jump end_tonks_hangout


label nt_he_story_intro_E9:
    ton "Being an auror was quite a stressful job, you know." ("open", "closed", "shocked", "mid", ypos="head", flip=False)
    gen "I--" ("base", xpos="far_left", ypos="head")
    ton "The ministry was mostly concerned about the criminals making up for their crimes." ("open", "base", "angry", "mid")
    ton "But I was more concerned about the victims involved." ("open", "closed", "base", "mid")
    ton "So, sometimes there would be a situation that I'd take into my own hands." ("open", "closed", "shocked", "mid")
    gen "Such as?" ("base", xpos="far_left", ypos="head")
    ton "Well, there was this one guy that used a love potion..." ("normal", "narrow", "base", "R")
    gen "A love potion, too bad they aren't real..." ("base", xpos="far_left", ypos="head")
    ton "Of course they're real, and quite effective as well." ("open", "wide", "base", "mid")
    ton "Also... highly illegal." ("soft", "closed", "base", "mid")
    gen "Oh, of course..." ("base", xpos="far_left", ypos="head")
    ton "Anyway..." ("open", "base", "base", "L")
    ton "He could've ended up in prison... But the law isn't black and white like that." ("open", "base", "base", "mid")
    gen "So you're saying that his intentions were good?" ("base", xpos="far_left", ypos="head")
    ton "In this instance, the woman in question was in an abusive relationship." ("open", "base", "base", "R")
    ton "And the guy knew that the boyfriend was the jealous type..." ("open", "base", "base", "mid")
    gen "I see, so he fed her the potion to get her out of it." ("base", xpos="far_left", ypos="head")
    ton "Right... I mean, jealousy isn't that bad in a playful relationship. But it wasn't like that." ("normal", "base", "base", "downR")
    gen "Wait a second, how did you even know the guy wasn't just saying this because the potion is illegal?" ("base", xpos="far_left", ypos="head")
    ton "Because I used truth serum." ("grin", "base", "raised", "mid")
    gen "And that isn't illegal or regulated as well?" ("base", xpos="far_left", ypos="head")
    ton "As I said... The law is more complicated than that, and in certain instances, using a truth serum would be the right thing to do." ("mad", "base", "base", "mid")
    ton "And to be honest, who was he going to tell... It's not like he had the moral high ground." ("annoyed", "closed", "base", "mid")
    gen "I see, then how did the situation end up?" ("base", xpos="far_left", ypos="head")
    ton "The girl got out of the abusive relationship and requested to have her memory adjusted." ("open", "wide", "shocked", "mid")
    gen "And that's--" ("base", xpos="far_left", ypos="head")
    ton "That's fine... We do it to muggles all the time." ("open", "base", "base", "R")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "(Where do these people draw the line... making someone fall in love with you just like that?)" ("base", xpos="far_left", ypos="head")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    jump end_tonks_hangout


label nt_he_story_intro_E10:
    call bld
    gen "Settled in okay?" ("base", xpos="far_left", ypos="head")
    ton "Yes, I finally feel like I've found some sort of daily routine." ("grin", "wide", "base", "mid", ypos="head", flip=False)
    ton "This school brings back so many memories. It's like, every time I turn a corner, I expect to see one of my old classmates." ("open", "base", "shocked", "R")
    gen "So, good memories?" ("base", xpos="far_left", ypos="head")
    ton "Mostly, it's a bit different now." ("base", "narrow", "shocked", "down")
    gen "In what way?" ("base", xpos="far_left", ypos="head")
    ton "Well, there wasn't any of this favour business going on for one." ("horny", "base", "base", "R")
    ton "But the students and teachers were pretty much the same." ("base", "base", "raised", "down")
    gen "So, what was the real old man like?" ("base", xpos="far_left", ypos="head")
    ton "Unobtrusive..." ("open", "base", "raised", "R")
    gen "What does that mean?" ("base", xpos="far_left", ypos="head")
    ton "I only really saw him during larger festivities, he mostly spent his time in this office." ("open", "base", "base", "down")
    gen "So that's why Snape wanted me to stay put..." ("base", xpos="far_left", ypos="head")

    jump end_tonks_hangout


label nt_he_story_E11:
    $ states.gen.ev.tonks.metamorphmagi_aware = True
    call bld
    gen "Tell me more about your time at Hogwarts, as a student..." ("base", xpos="far_left", ypos="head")
    ton "Of course, [name_genie_tonks]." ("base", "base", "base", "mid", ypos="head", flip=False)
    ton "Well, as you may or may not know. I'm a metamorphmagus." ("open", "base", "base", "R") #metamorphmagus is a latin based word, therefore "-us" is the singular version and "-i" is the plural
    ton "It means I can change my physical appearance at will." ("base", "base", "raised", "mid")
    gen "Sounds useful." ("base", xpos="far_left", ypos="head")
    ton "It can be." ("base", "base", "base", "L")
    ton "Since you can't reprimand me about it, I might as well tell you a bit about it." ("open", "base", "raised", "mid")
    gen "I'm still your boss." ("base", xpos="far_left", ypos="head")
    ton "You gonna put me in detention?" ("horny", "base", "base", "mid")
    ton "Or put me over your knee and spank me?" ("horny", "base", "angry", "mid")
    gen "Don't tempt me." ("grin", xpos="far_left", ypos="head")
    ton "There was this time when I changed into professor Snape." ("grin", "narrow", "base", "mid")
    gen "Why Snape?" ("base", xpos="far_left", ypos="head")
    ton "Well, he was the most likely not to be in the staff room. Which is where I wanted to get in." ("grin", "narrow", "base", "R")
    gen "Why's that?" ("base", xpos="far_left", ypos="head")
    ton "He never leaves the dungeons does he?" ("open", "wide", "raised", "mid")
    ton "Just take one look at his pasty face, and you'll see..." ("mad", "base", "base", "downR")
    ton "Don't tell him I said that..." ("clench", "base", "base", "mid")
    gen "..." ("grin", xpos="far_left", ypos="head")
    ton "So... I changed into professor Snape and went towards the staff room..." ("base", "base", "annoyed", "R")
    gen "Isn't the staff room just full of boring old teachers?" ("base", xpos="far_left", ypos="head")
    ton "My goal wasn't to speak with the teachers..." ("open", "closed", "base", "mid")
    ton "I was trying to get a key to the prefects' bathroom." ("base", "base", "angry", "mid")
    gen "And you couldn't just turn into a prefect, and get in there that way?" ("base", xpos="far_left", ypos="head")
    ton "Well, that would've been the clever thing to do..." ("open", "base", "raised", "R")
    ton "Although, like everything else in this school, the bathroom has a password and not a key..." ("normal", "closed", "annoyed", "mid")
    ton "Of course I didn't know that... I had just heard rumours about the bathroom." ("clench", "narrow", "worried", "R")
    gen "So did you manage to get in there in the end?" ("base", xpos="far_left", ypos="head")
    ton "Oh yeah, it was easy!" ("base", "wink", "base", "mid")
    ton "Once I knew about the password, I just had to pretend to be one of the prefects, and ask another for it." ("open", "wide", "base", "mid")
    gen "Smart..." ("base", xpos="far_left", ypos="head")

    jump end_tonks_hangout


label nt_he_story_E12:
    call bld
    gen "Tell me more about that shapeshifting ability of yours..." ("base", xpos="far_left", ypos="head")
    ton "Of course..." ("base", "wide", "shocked", "mid", ypos="head", flip=False)
    ton "Most of my escapades were kind of one-trick ponies." ("open", "base", "base", "R")
    gen "Sounds pretty foolproof to me..." ("base", xpos="far_left", ypos="head")
    gen "I mean, how many other students could change their appearance?" ("base", xpos="far_left", ypos="head")
    ton "None, that's why. Process of elimination." ("upset", "base", "raised", "downR")
    gen "So you got punished without any sort of proof?" ("base", xpos="far_left", ypos="head")
    ton "No, but they set up countermeasures after the time when--" ("open", "base", "raised", "R")
    ton "I shouldn't really talk about it. They never confronted me about it, so fessing up now isn't going to do me any good." ("mad", "narrow", "worried", "down")
    gen "Not a word leaves this office." ("base", xpos="far_left", ypos="head")
    ton "Do you think I'm weird?" ("open", "narrow", "shocked", "down")
    gen "Everyone is a bit... weird..." ("base", xpos="far_left", ypos="head")
    ton "Fine, I'll tell you." ("base", "closed", "shocked", "down")
    ton "You might have noticed that I'm a bit more comfortable with my sexuality than most people." ("open", "base", "base", "mid")
    gen "(Oh, here we go!)" ("grin", xpos="far_left", ypos="head")
    ton "I already told you about the whole werewolf thing, and the power play fantasies with the vampire..." ("open", "base", "base", "R")
    gen "Well, you didn't phrase it that bluntly before, but I got the gist." ("base", xpos="far_left", ypos="head")
    ton "Well, just like many weird or odd sexual preferences, they're often deeply embedded with experiences from your youth." ("open", "base", "worried", "L")
    ton "So for me, there was this one time where I pretended to be a teacher..." ("open", "base", "worried", "mid")
    ton "As in, I literally took over their lesson when they were ill." ("mad", "base", "base", "down")
    gen "How did you manage that, weren't the students notified of their leave beforehand?" ("base", xpos="far_left", ypos="head")
    ton "No. There was just a note on the door, so I ripped it off before the class got there." ("open", "closed", "base", "mid")
    gen "Seems like a flawed system..." ("base", xpos="far_left", ypos="head")
    ton "Yeah, afterwards, a lot of the teachers changed the way they do it. Not the new ones though..." ("grin", "base", "base", "downR")
    gen "You haven't told me which class this was. Did you turn into Snape and teach potions?" ("base", xpos="far_left", ypos="head")
    ton "Of course not! Snape would've made my life hell, and I wasn't going to make someone hurt themself." ("open", "base", "annoyed", "down")
    ton "It was charms..." ("mad", "base", "base", "down")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    ton "I had been practising some charms, and taught myself a couple on my own, like the one for invisibility..." ("crooked_smile", "base", "base", "down")
    gen "Impressive." ("base", xpos="far_left", ypos="head")
    ton "Thanks... Normally, you wouldn't learn that one until much later, so you'd easily be able to dispel it." ("silly", "happyCl", "base", "mid")
    gen "But you decided it was a good idea to teach it anyway?" ("base", xpos="far_left", ypos="head")
    ton "I didn't say it was a good idea." ("mad", "base", "base", "mid")
    ton "It didn't end up working anyway..." ("upset", "base", "worried", "R")
    ton "Instead of the charm making the students' whole body transparent, it just made their clothes vanish!" ("open", "closed", "base", "mid")
    ton "Whilst it wasn't intentional, the memory of it still excites me a bit." ("base", "base", "base", "down")
    ton "And that's where that particular fetish came from..." ("soft", "base", "base", "mid")
    gen "Hold on, there's a spell to make only the clothes invisible?" ("angry", xpos="far_left", ypos="head")
    ton "That's what you focus on?" ("open", "base", "raised", "mid")
    gen "Well, yeah! Sound to me like you invented a new spell that no one's ever heard of..." ("base", xpos="far_left", ypos="head")
    gen "And it can make people's clothing invisible?! That's kind of a big deal!" ("angry", xpos="far_left", ypos="head")
    ton "It's not a new spell... it was just novice wizards and witches not being powerful enough to cast it properly..." ("upset", "wide", "shocked", "mid")
    ton "Similarly to splinching." ("clench", "base", "raised", "R")
    gen "(That sounds disgusting...)" ("base", xpos="far_left", ypos="head")
    ton "Anyway, the teachers played it off as an accident... though poor Flitwick had his magical abilities questioned by the students for a while." ("upset", "base", "shocked", "down")
    ton "And they tried to set up some more countermeasures towards my abilities at that point." ("open", "base", "annoyed", "R")
    ton "Not that they worked that well... After that, I was a bit more selective with my usage, and actually thought about the consequences a bit before using it." ("mad", "narrow", "annoyed", "R")
    gen "Well, you do start thinking more about others as you get older..." ("base", xpos="far_left", ypos="head")
    ton "Yeah... Well, my sexual drive started to take the upper hand on my decisions from that point on, so it evened out." ("base", "happyCl", "base", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    jump end_tonks_hangout
