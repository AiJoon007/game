

### Manipulate the enemy female Quidditch players ###

### Start ###
label cc_pr_spy_girls_start:

    cho "" (xpos="right", ypos="base", trans=fade)

    if not states.cho.ev.spy_on_girls.t3_e1_complete: # Completed shower event?
        # Shower event - looking through the glory hole

        if not states.cho.ev.spy_on_boys.t3_e1_complete:
            # Player has not spied on boys just yet.

            gen "Time for some good old espionage!" ("base", xpos="far_left", ypos="head")
            gen "For this mission -- I'd like you to spy on the girls of the Gryffindor team." ("base", xpos="far_left", ypos="head")
            gen "When they're alone..." ("base", xpos="far_left", ypos="head")
            cho "When they're alone, [name_genie_cho]?" ("open", "narrow", "raised", "mid")
            cho "I can't get into their common room... You should know that." ("soft", "narrow", "base", "R")
            gen "There are plenty of other places where girls hang out and gossip..." ("base", xpos="far_left", ypos="head")
            gen "Want to make a guess of where I'm thinking of?" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("disgust", "narrow", "base", "mid") #Blushes
            gen "That's right, the women's changing room!" ("grin", xpos="far_left", ypos="head")
            cho "Fine...{w=0.4} I'll see what I can do." ("open", "closed", "base", "mid")
            gen "Excellent!" ("grin", xpos="far_left", ypos="head")
            cho "" ("annoyed", "base", "base", "mid")
            gen "Report back to me as usual, C." ("base", xpos="far_left", ypos="head")
            cho "\"C\", [name_genie_cho]?" ("soft", "base", "raised", "mid")
            gen "It's your spy name!" ("grin", xpos="far_left", ypos="head")
            cho "My spy name, [name_genie_cho]?" ("soft", "narrow", "base", "mid")
            cho "The C stands for \"Cho\", I presume?" ("smile", "narrow", "base", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            gen "No, not your name...{w=0.4} I'm not that unimaginative..." ("base", xpos="far_left", ypos="head")
            cho "" ("annoyed", "narrow", "base", "mid")
            gen "C is your cup-size, is it not?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "My cup-size?!" ("angry", "wide", "base", "mid")
            gen "That's right." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "But that's not even correct! Mine is--" ("disgust", "happyCl", "base", "mid")
            cho @ cheeks blush "I mean...{w=0.4} Where do you get all these ideas from, seriously!?" ("upset", "narrow", "angry", "R")
            gen "So what's your actual size then?{w} B?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("annoyed", "narrow", "worried", "down") #Blushes
            cho @ cheeks heavy_blush "Yes, it's B..." ("soft", "narrow", "angry", "downR") #Blushes and glances to the side
            gen "Noted..." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "You're such an old pervert, you know that, right?" ("annoyed", "narrow", "angry", "mid")

        else:
            # Player has spied on the boys

            gen "Time for some more espionage..." ("base", xpos="far_left", ypos="head")
            gen "This time we'll be targeting the girls!" ("grin", xpos="far_left", ypos="head")
            cho "The girls? Anyone in particular you want me to spy on, [name_genie_cho]?" ("soft", "narrow", "raised", "mid")
            gen "Why one, when you could do all of them at once?" ("grin", xpos="far_left", ypos="head")
            cho "All at once?" ("clench", "base", "base", "mid")
            gen "That's what I said..." ("base", xpos="far_left", ypos="head")
            gen "Their changing room should be a good place to start." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "You can't be serious!" ("mad", "happyCl", "worried", "mid")
            gen "I know! I surprise myself with how good my plans are sometimes..." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "I'm gonna get caught for sure..." ("disgust", "base", "worried", "down") # small text
            cho "..." ("annoyed", "base", "angry", "down")
            cho "I'll see what I can do..." ("annoyed", "narrow", "angry", "mid")
            gen "Excellent." ("grin", xpos="far_left", ypos="head")

        gen "Now, to the gadgets..." ("base", xpos="far_left", ypos="head")
        gen "I've got this great new invention... It's a vibrating magical rod that--" ("grin", xpos="far_left", ypos="head")
        cho "A vibrating what?" ("open", "base", "raised", "mid")
        gen "You could have let me finish, and I would have told you..." ("base", xpos="far_left", ypos="head")
        cho "Wouldn't something like an extendable ear make more sense for eavesdropping?" ("open", "narrow", "base", "mid")
        gen "Not unless it vibrates..." ("base", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "narrow", "angry", "mid")
        gen "You don't want it?" ("base", xpos="far_left", ypos="head")
        cho "I'll manage without, [name_genie_cho]." ("annoyed", "narrow", "base", "mid")
        gen "Suit yourself..." ("base", xpos="far_left", ypos="head")
        gen "Anyway, you'd better get a move on." ("base", xpos="far_left", ypos="head")
        gen "I expect your report this evening, B!" ("base", xpos="far_left", ypos="head")
        gen "Good luck!" ("base", xpos="far_left", ypos="head")
        cho "Thanks..." ("open", "narrow", "angry", "R")

    elif not states.cho.ev.spy_on_girls.t3_e2_complete: # Completed Alicia Spinnet?
        # Spy on Alicia Spinnet

        gen "Ready for some more espionage, B?" ("base", xpos="far_left", ypos="head")
        cho "I suppose..." ("soft", "narrow", "base", "mid")
        cho "Who's the target?" ("open", "narrow", "raised", "mid")
        gen "Let's do the spinner girl--" ("base", xpos="far_left", ypos="head")
        gen "I mean... Let's do Miss Spinnet next." ("base", xpos="far_left", ypos="head")
        cho "Alicia?" ("soft", "base", "raised", "mid")
        gen "Yes... I suggest you try and spy on her when she's not with the other two." ("base", xpos="far_left", ypos="head")
        cho "Why just her?" ("soft", "narrow", "base", "mid")
        gen "It's the best way to get to know a person, wouldn't you agree." ("base", xpos="far_left", ypos="head")
        gen "Maybe she's putting up a front with her friends." ("base", xpos="far_left", ypos="head")
        cho "If you say so..." ("annoyed", "base", "base", "R")
        gen "Off you go, and good luck!" ("base", xpos="far_left", ypos="head")
        cho "Thanks, [name_genie_cho]." ("base", "base", "base", "mid")

    elif not states.cho.ev.spy_on_girls.t3_e3_complete: # Completed Katie Bell?
        # Spy on Katie Bell

        gen "Ready for some more espionage, B?" ("base", xpos="far_left", ypos="head")
        cho "Of course!" ("base", "base", "base", "mid")
        gen "Which one of the girls from the Gryffindor team have we yet to spy on?" ("base", xpos="far_left", ypos="head")
        cho "Well, I could spy on Katie..." ("open", "base", "raised", "R")
        gen "Katie... Who?{w=0.5} That name doesn't ring a bell..." ("base", xpos="far_left", ypos="head")
        cho "Katie Bell, [name_genie_cho]." ("soft", "narrow", "base", "mid")
        gen "(...)" ("base", xpos="far_left", ypos="head")
        gen "Just keep it quiet when you go after her... We're on a spy mission, after all." ("base", xpos="far_left", ypos="head")
        gen "I don't want you to ring Katie's bell just yet. We'll get to that later..." ("grin", xpos="far_left", ypos="head")
        cho "Ring her... Bell, [name_genie_cho]?" ("open", "narrow", "raised", "mid")
        gen "Never mind... Off you go." ("base", xpos="far_left", ypos="head")
        cho "Very well... Until later then." ("base", "base", "base", "mid")

        call cho_walk("door", "base")

        gen "Oh, wait... I forgot about the gadgets!" ("angry", xpos="far_left", ypos="head")

        call cho_walk(action="leave")

        gen "(Damn, she must've not heard me...)" ("base", xpos="far_left", ypos="head")

        # End early, cho already left!

        jump end_cho_event

    elif not states.cho.ev.spy_on_girls.t3_e4_complete: # Completed Angelina Johnson?
        # Spy on Angelina Johnson

        gen "Ready for some more espionage, B?" ("base", xpos="far_left", ypos="head")
        cho "I suppose... I assume you want me to go after the girls again?" ("soft", "base", "base", "mid")
        gen "You'd be correct with that assumption..." ("base", xpos="far_left", ypos="head")
        cho "Well, there's only one member I haven't spied on yet, which would be A--" ("open", "base", "base", "R")
        with hpunch
        gen "{b}Johnson!{/b}" ("angry", xpos="far_left", ypos="head") # large text
        cho "..." ("disgust", "narrow", "base", "mid")
        gen "Sorry. Couldn't help myself..." ("base", xpos="far_left", ypos="head")
        cho "I meant to say Angelina, but yes... her." ("annoyed", "narrow", "base", "mid")
        gen "She's their team captain, isn't she?" ("base", xpos="far_left", ypos="head")
        gen "I can't stress enough that today's performance is of the utmost importance." ("base", xpos="far_left", ypos="head")
        cho "..." ("soft", "base", "base", "mid")
        gen "You can't get caught when you spy on her Johnson--" ("angry", xpos="far_left", ypos="head")
        gen "I mean-- when you spy on Johnson..." ("angry", xpos="far_left", ypos="head")
        cho "Of course... So, what--" ("open", "base", "base", "mid")
        gen "Utmost!" ("angry", xpos="far_left", ypos="head")
        cho "" ("upset", "base", "base", "mid")
        gen "Importance!" ("angry", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "narrow", "base", "mid")
        gen "So are you ready, B?" ("base", xpos="far_left", ypos="head")
        cho "Yes, I'm ready..." ("soft", "narrow", "angry", "R")
        gen "Don't get spotted!" ("base", xpos="far_left", ypos="head")
        cho "Until later then..." ("open", "closed", "base", "mid")

    else:
        gen "Let's spy on those girls some more!" ("base", xpos="far_left", ypos="head")
        cho "Again? I've already spied on them all..." ("soft", "base", "raised", "mid")
        gen "You can never get enough intel." ("base", xpos="far_left", ypos="head")
        gen "Make sure to bring me your report as usual B." ("base", xpos="far_left", ypos="head")
        cho "Of course." ("base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_event

### Tier 3 (pre Gryffindor) ###

label cc_pr_spy_girls_T3_showers:
    # Showers - looking through the glory hole

    $ states.cho.ev.spy_on_girls.t3_e1_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "Welcome back!{w=0.3} What's the report, B?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("annoyed", "narrow", "angry", "downR") #Blushing looking away
    gen "Did you get any juicy info that we could use against the Gryffindor girls?" ("base", xpos="far_left", ypos="head")
    cho "No juicy info per se..." ("open", "closed", "base", "mid")
    gen "Then how'd it go, anything you could tell me?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well... I went to spy on them in the showers, just as you asked me..." ("soft", "narrow", "worried", "R")
    cho "I found a hole in one of the walls, actually..." ("annoyed", "narrow", "raised", "mid")
    gen "That's unfortunate, I'll have to look into filling that hole at some point..." ("base", xpos="far_left", ypos="head")
    gen "So what were they talking about if it wasn't Quidditch?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Ehm*... There wasn't much talking at all..." ("disgust", "narrow", "base", "downR")
    cho @ cheeks blush "They were too preoccupied with kissing, and touching each other." ("open", "happyCl", "base", "mid")
    gen "I knew it!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Hmph*..." ("annoyed", "narrow", "angry", "mid") #annoyed
    gen "Makes you wish those girls were on your own team, doesn't it?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Yeah right..." ("annoyed", "narrow", "angry", "downR") #annoyed glancing to the right #blush
    gen "What else did they do?" ("base", xpos="far_left", ypos="head")
    cho "Not a lot to be honest..." ("open", "closed", "base", "mid")
    cho "I wasn't going to stay until they were done..." ("annoyed", "narrow", "angry", "mid")
    gen "Why not? What's the worst that could happen?" ("base", xpos="far_left", ypos="head")
    gen "They'd catch you and ask for you to join in?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Pfff*...{w=0.3} As if...{w=0.3} They'd never let one of their opponents in on anything they were doing." ("soft", "narrow", "angry", "downR")
    gen "At least you considered it." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "I didn't say that." ("mad", "narrow", "angry", "mid")
    cho @ cheeks blush "I had no idea they were so lewd..." ("annoyed", "narrow", "angry", "R")
    cho "I'm worried that there's little I could do in terms of clothing that would distract them..." ("open", "closed", "worried", "mid")
    cho "Seeing how they were crawling over each other's naked bodies..." ("annoyed", "narrow", "angry", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "You should've stayed for longer... Perhaps you could've learned a thing or two." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("annoyed", "narrow", "angry", "R")
    gen "Anyway... I'll think of something..." ("base", xpos="far_left", ypos="head")
    cho "Okay..." ("soft", "closed", "base", "mid")
    gen "Mission accomplished, B!" ("angry", xpos="far_left", ypos="head")
    gen "You may go now..." ("base", xpos="far_left", ypos="head")
    cho "Good night, [name_genie_cho]." ("annoyed", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event

## Alicia Spinnet ##
label cc_pr_spy_girls_T3_alicia:

    $ states.cho.ev.spy_on_girls.t3_e2_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    # Cho returns blushing with a vacant expression on her face
    gen "Ready for your report, B..." ("base", xpos="far_left", ypos="head")
    gen "What's the {i}sitch{/i}?" ("base", xpos="far_left", ypos="head")
    cho "The \"sitch\", [name_genie_cho]?" ("soft", "narrow", "raised", "mid")
    gen "What's the situation?" ("base", xpos="far_left", ypos="head")
    gen "Did you manage to spy on Miss Spinnet?" ("base", xpos="far_left", ypos="head")
    cho "I did..." ("open", "closed", "raised", "mid")
    gen "Great, tell me what happened." ("base", xpos="far_left", ypos="head")
    cho "She's been assisting the Weasley twins -- by drawing in more customers to their shop." ("open", "narrow", "base", "mid")
    gen "How kind." ("base", xpos="far_left", ypos="head")
    cho "I wouldn't call it that..." ("soft", "narrow", "base", "R")
    cho "The only reason she's assisting them, is because they promised they'd behave during Quidditch." ("open", "narrow", "raised", "mid")

    # Has player sent Hermione to work with the Twins, promoting the cardgame?
    if not states.her.ev.promote_cardgame.first_time:
        gen "(I thought Hermione was helping them with that already...)" ("base", xpos="far_left", ypos="head")

    cho "And she sure doesn't seem to have any problems enticing people." ("soft", "narrow", "base", "mid")
    gen "So, how does she do it?" ("base", xpos="far_left", ypos="head")
    cho "Well... If I didn't know better, I'd say she must be using some kind of hypnosis." ("annoyed", "narrow", "angry", "R")
    gen "Hypnosis? Now that sounds completely absurd." ("base", xpos="far_left", ypos="head")

    # Has player started imperius curse training?
    if states.ast.ev.imperio_with_tonks.completed_once:
        gen "She's not using that im-perv-ius curse, is she?" ("base", xpos="far_left", ypos="head")
        cho "The Imperius curse?" ("open", "narrow", "raised", "mid")
        gen "That's what I said..." ("base", xpos="far_left", ypos="head")
        cho "Of course not. That spell is illegal!{w=0.8} She'd be thrown into a cell in Azkaban for it..." ("soft", "narrow", "angry", "mid")
        gen "That's-- *Ehm*...{w=0.3} correct.{w=0.5} Straight into prison..." ("base", xpos="far_left", ypos="head")
        cho "But no... I haven't seen her with a wand in hand..." ("open", "closed", "base", "mid")
    else:
        cho "That's why I said, \"if I didn't know any better\"..." ("open", "closed", "base", "mid")

    cho "I saw her whisper something into another student's ear..." ("soft", "closed", "base", "mid")
    cho "And as if on command -- they immediately followed her into the girls' toilets." ("soft", "narrow", "angry", "mid")
    gen "A girl who takes what she wants... I respect that." ("grin", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "So, what was she doing with them?" ("base", xpos="far_left", ypos="head")
    cho "Do you really have to ask, [name_genie_cho]?" ("open", "narrow", "raised", "mid")
    cho "Surely you're able to guess what they did in there..." ("soft", "closed", "base", "mid")
    gen "No, I have no idea!" ("grin", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "Isn't that why you're here?{w=0.4} to tell me..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "She was doing lewd stuff with the student, obviously..." ("soft", "narrow", "angry", "R")
    gen "Such as?" ("grin", xpos="far_left", ypos="head")
    cho "So predictable..." ("disgust", "closed", "angry", "mid")
    cho "Well, since I knew you'd ask... I did sneak in after her, and got a glimpse of her kneeling inside one of the stalls..." ("soft", "narrow", "angry", "mid")
    cho @ cheeks blush "And whoever was in there with her wasn't being quiet... That's for sure." ("annoyed", "narrow", "angry", "R")
    gen "I should get her number." ("base", xpos="far_left", ypos="head")
    cho "Her what?" ("annoyed", "narrow", "angry", "mid")
    gen "Never mind...{w=0.4} So is that all that you saw?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Ehm*... Yes...{w=0.5} That was it..." ("quiver", "narrow", "base", "down") #Blushing
    cho @ cheeks blush "As I said, I could only see her bottom, from underneath that stall..." ("open", "narrow", "base", "downR") #Blushing
    gen "Your face says otherwise... Is that really everything you saw?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "When I say bottom... She wasn't wearing any panties, [name_genie_cho]..." ("disgust", "happyCl", "worried", "mid") #Blushing
    cho @ cheeks blush "She was also..." ("soft", "narrow", "worried", "mid") #Blushing
    cho @ cheeks blush "She was also really wet down there..." ("horny", "narrow", "worried", "downR") #Blushing
    gen "There it is..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "I just thought I'd tell you, since she was making a huge mess on the floor!" ("soft", "narrow", "angry", "mid")
    cho @ cheeks blush "That's all..." ("annoyed", "narrow", "angry", "mid")
    gen "Of course, thanks for letting me know." ("base", xpos="far_left", ypos="head")
    gen "You've done a great job today, B!" ("base", xpos="far_left", ypos="head")
    gen "Although, I still think my gadgets -- especially the magic rod -- would've been a great help for this mission." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("annoyed", "narrow", "angry", "R") #Blushing
    gen "I could let you borrow it, to figure out how it works." ("base", xpos="far_left", ypos="head")
    gen "It's very useful, you know." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "I'm good, thanks..." ("soft", "narrow", "angry", "mid")
    cho @ cheeks blush "I think I'll just head straight to bed, if you don't mind." ("soft", "narrow", "base", "downR")

    call cho_walk(xpos="door", ypos="base")

    pause .8
    call bld
    gen "Changed your mind?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "N-- No, Good night!" ("open", "happyCl", "base", "mid", xpos="base", flip=True) # head

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event


## Katie Bell ##
label cc_pr_spy_girls_T3_katie:

    $ states.cho.ev.spy_on_girls.t3_e3_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)

    gen "Mission successful?" ("base", xpos="far_left", ypos="head")
    gen "What did you learn about Katie Bell?" ("base", xpos="far_left", ypos="head")
    cho "She's a freak!" ("soft", "narrow", "angry", "mid") # angry
    gen "Whoa, that's a bit uncalled-for, don't you think?" ("base", xpos="far_left", ypos="head")
    gen "I'm sure she looks perfectly fine." ("base", xpos="far_left", ypos="head")
    cho "No, not her looks... what she's been doing." ("open", "closed", "angry", "mid") # blush
    cho "I followed her all the way down to the lake today. And then hid behind a tree to observe her." ("open", "narrow", "angry", "mid")
    gen "Something wrong with a little swim?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "No, but...{w=0.5} she went in there butt-naked!" ("disgust", "narrow", "base", "mid")
    gen "Butt-naked? Did they open up a nude-beach without telling me?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Of course they haven't!" ("angry", "base", "base", "mid")
    gen "Shame..." ("base", xpos="far_left", ypos="head")
    cho "Once she had taken her clothes off -- she slowly walked into the water -- and then just vanished beneath the surface." ("open", "narrow", "base", "mid")
    gen "That's...{w=0.4} odd..." ("base", xpos="far_left", ypos="head")
    gen "Perhaps she's a mermaid?" ("grin", xpos="far_left", ypos="head")
    cho "I highly doubt that, seeing that she has legs..." ("open", "closed", "base", "mid")
    cho "Although, for a moment, I did consider that the mermaids living there -- might have used their songs to charm her..." ("soft", "base", "raised", "up")
    gen "Well, that's not concerning at all..." ("base", xpos="far_left", ypos="head")
    cho "She did resurface a couple of moments later though... just as I began to worry..." ("annoyed", "base", "base", "mid")
    cho "But she emerged with a huge splash -- as she had been lifted into the air by some giant tentacles!" ("soft", "base", "angry", "mid")
    gen "Whoa, tentacles!" ("angry", xpos="far_left", ypos="head")
    gen "Wait, you're seriously not making this up? Since when do Mermaids have tentacles?" ("base", xpos="far_left", ypos="head")
    cho "I highly doubt it was them..." ("open", "closed", "base", "mid")
    cho "I've told you, she's a freak!" ("soft", "narrow", "angry", "mid")
    gen "So she's into tentacles, *huh*?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes... Gross, slimy, green tentacles..." ("disgust", "narrow", "angry", "down")
    cho "She must've used some charm... It was as if the lake had come to life!" ("clench", "narrow", "angry", "R")
    gen "Shiver me timbers!" ("angry", xpos="far_left", ypos="head")
    gen "What a fearless woman, to meddle with such magic?!" ("angry", xpos="far_left", ypos="head")
    gen "What was it doing to her?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Ugh* Do I really have to tell you..." ("disgust", "narrow", "angry", "R")
    gen "With as much detail as possible, thank you." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Fine..." ("annoyed", "narrow", "angry", "down")
    cho "They were holding her body stationary in the air -- whilst more of its tentacles were working their way around -- squeezing her breasts." ("soft", "closed", "base", "mid")
    gen "Classic tentacle move!" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "As it... {w=0.5} continued...{w=0.8} the tentacles grabbed her around the waist and began moving her body up and down -- with another one wrapping itself around her legs." ("clench", "narrow", "worried", "mid")
    cho @ cheeks blush "She almost looked like a doll being puppeteered by those giant arms..." ("soft", "narrow", "angry", "mid")
    gen "And she was letting it do this willingly?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes, she seemed to thoroughly enjoy being its...{w=0.8} toy to play with." ("clench", "narrow", "base", "downR")
    cho "She looked as if possessed! Being held up in the air like that, with her eyes rolled back into her head." ("soft", "narrow", "angry", "mid")
    cho @ cheeks blush "Then I watched another tentacle slip through her legs -- which was enough to bring her over the edge, I think." ("mad", "narrow", "raised", "down")
    gen "Impressive..." ("base", xpos="far_left", ypos="head")
    gen "Sounds to me like a mission accomplished!" ("grin", xpos="far_left", ypos="head")
    cho "Mission... What?" ("soft", "narrow", "raised", "mid")
    gen "I'm sure you've just learned more about her than even her closest friends." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("annoyed", "narrow", "base", "mid")
    gen "She's a girl who likes it dirty, and takes it rougher than even the toughest sea dog can muster!" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "If you say so, [name_genie_cho]..." ("soft", "narrow", "base", "R")
    gen "A pervert who doesn't give a hoot about foreplay." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("annoyed", "narrow", "angry", "mid")
    gen "And you definitely know not to entice her with any sort of seaweed." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Can I go now?" ("annoyed", "narrow", "angry", "R")
    gen "Yes, you may leave..." ("base", xpos="far_left", ypos="head")
    gen "Good job today, [name_cho_genie]." ("grin", xpos="far_left", ypos="head")
    cho "Thanks..." ("soft", "closed", "base", "mid")
    cho "Good Night." ("normal", "narrow", "base", "mid")
    gen "Until next time." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event

## Angelina Johnson ##
label cc_pr_spy_girls_T3_angelina:

    $ states.cho.ev.spy_on_girls.t3_e4_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("normal", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "Ready for your report, B... lay on me!" ("grin", xpos="far_left", ypos="head")
    cho "Don't you mean lay \"it\" on me, [name_genie_cho]?" ("soft", "narrow", "raised", "mid")
    gen "I'm pretty sure I'm right..." ("base", xpos="far_left", ypos="head")
    gen "But before that, tell me how everything went with Miss Johnson!" ("base", xpos="far_left", ypos="head")
    cho "Well enough, I'd say..." ("open", "narrow", "raised", "down")
    cho "I stayed behind after practice, to see if I could follow her once they were done changing their clothes." ("smile", "narrow", "angry", "mid")
    cho "To my surprise, she didn't head back to the castle like the others, but went to the referee's office instead..." ("base", "narrow", "angry", "mid")
    gen "The Referee?" ("base", xpos="far_left", ypos="head")
    cho "Madam Hooch's office, [name_genie_cho]." ("soft", "base", "raised", "mid")
    cho "I managed to eavesdrop on their conversation, although I only caught the tail end of it..." ("open", "base", "base", "L")
    cho @ cheeks blush "I suspect Madam Hooch might know what they've been doing in the showers after the game..." ("base", "narrow", "angry", "mid")
    cho "Angelina was talking about how she couldn't believe that she and her friends were being spied on like that." ("open", "base", "base", "up")
    cho @ cheeks blush "Madam Hooch just laughed it off and told her she should take it as a compliment." ("grin", "happyCl", "base", "mid")
    gen "Good to know my staff knows how to diffuse a situation..." ("base", xpos="far_left", ypos="head")
    cho "Angelina sure didn't see it that way -- and stormed right out her office..." ("base", "narrow", "angry", "mid")
    gen "You sure she wasn't talking about--" ("base", xpos="far_left", ypos="head")
    cho "[name_genie_cho]... If Madam Hooch is spying on them, then Angelina might get the idea to entice her into helping them during the finals!" ("annoyed", "narrow", "base", "mid")
    gen "*Hmm*... Not a bad idea, now that I think about it..." ("base", xpos="far_left", ypos="head")
    gen "We should try that as well." ("grin", xpos="far_left", ypos="head")
    cho "No! I don't want to win by cheating!" ("clench", "narrow", "angry", "mid")
    gen "Yes, because distracting hardly counts as cheating..." ("base", xpos="far_left", ypos="head")
    cho "Well of course it doesn't! It's within the rules!" ("open", "closed", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    cho "We need to do something about it, before Angelina tries to take advantage of the situation..." ("soft", "narrow", "angry", "mid")
    gen "I'll... figure something out..." ("base", xpos="far_left", ypos="head")
    cho "You'd better!" ("annoyed", "narrow", "angry", "mid") #Angry
    cho "So... are we done here?" ("base", "narrow", "raised", "mid") #smiles and focuses on genie
    gen "Yes, mission successful, [name_cho_genie]!" ("grin", xpos="far_left", ypos="head")
    gen "We'll have that girl wrapped around our--" ("base", xpos="far_left", ypos="head")
    gen "I mean... around your finger, soon enough..." ("grin", xpos="far_left", ypos="head")
    cho "Counting on it!" ("soft", "narrow", "raised", "mid")
    cho "Good night, [name_genie_cho]." ("base", "narrow", "base", "mid")

    #cho leaves
    call cho_walk(action="leave")

    gen "(Wrapped around your finger...{w} good one...)" ("grin", xpos="far_left", ypos="head")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event
