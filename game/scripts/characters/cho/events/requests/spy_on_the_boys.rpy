
### Manipulate the enemy male Quidditch players ###


### Start ###
label cc_pr_spy_boys_start:

    cho "" (xpos="right", ypos="base", trans=fade)

    if not states.cho.ev.spy_on_boys.t3_e1_complete: # Completed spying on the Weasley Twins?
        # Weasley Twins - handing over candies that turn people into blueberries

        if not states.cho.ev.spy_on_girls.t3_e1_complete:
            # Player has not spied on girls just yet.

            gen "Time to target the boys for a classic espionage mission C." ("base", xpos="far_left", ypos="head")
            cho "C? Is that some sort of spy name?" ("soft", "base", "base", "mid")
            gen "Yep! C is the perfect spy name for you." ("base", xpos="far_left", ypos="head")
            cho "Where do you get all these ideas from... seriously." ("annoyed", "base", "base", "mid")
            gen "That's your cup-size, is it not?" ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "wide", "base", "mid") #Blushes
            cho "You're such an old pervert, you know that, right?" ("soft", "base", "angry", "mid")
            cho "And it's B cup actually..." ("open", "base", "base", "downR") #Blushes and glances to the side
            gen "Noted..." ("grin", xpos="far_left", ypos="head")
            cho "So..." ("annoyed", "base", "base", "down") #pondering
            gen "Yes?" ("base", xpos="far_left", ypos="head")

        else:
            # Player has spied on the girls

            gen "Let's target the boys this time for some good ole espionage B." ("base", xpos="far_left", ypos="head")

        cho "Where does this obsession with nicknames come from?" ("open", "base", "raised", "mid")
        gen "Where does it come from....?" ("base", xpos="far_left", ypos="head")
        cho "Where does this obsession with nicknames come from... [name_genie_cho]?" ("annoyed", "base", "raised", "mid")
        gen "No-no... You don't get it, we use code words here..." ("base", xpos="far_left", ypos="head")
        gen "This is a secret operation!" ("base", xpos="far_left", ypos="head")
        cho "You want me to give you a nickname?" ("annoyed", "narrow", "base", "mid")
        gen "I think a \"codename\" would be the appropriate term." ("base", xpos="far_left", ypos="head")
        gen "How about..." ("base", xpos="far_left", ypos="head")

        menu:
            "\"Jason Porn\"":
                gen "Explosive truth seeker." ("grin", xpos="far_left", ypos="head")
            "\"Agent 69\"":
                gen "Licence to frisk." ("grin", xpos="far_left", ypos="head")
            "\"Cody Spanks\"":
                gen "No ass left untouched!" ("grin", xpos="far_left", ypos="head")

        cho "Merlin's beard..." ("angry", "narrow", "raised", "downR") # Facepalm
        gen "Merlin's beard.... That's a pretty good codename, I like it!" ("grin", xpos="far_left", ypos="head")
        cho "But I was..." ("mad", "base", "raised", "mid")
        gen "..." ("grin", xpos="far_left", ypos="head")
        cho "Yes... Merlin's beard." ("soft", "narrow", "base", "downR")
        cho "What is today's assign--{w=0.4} mission then?" ("open", "base", "base", "mid")
        gen "Today's mission, if you choose to accept it..." ("base", xpos="far_left", ypos="head")
        gen "And by choose I mean there's not really much choice in the matter." ("base", xpos="far_left", ypos="head")
        cho "..." ("normal", "narrow", "base", "mid") #rolls eyes, bit pissed off
        gen "I'd like you to spy on the beaters... Those {i}Weasel{/i} twins." ("base", xpos="far_left", ypos="head")
        cho "Weasley..." ("soft", "narrow", "base", "mid")
        gen "Yeah, that!" ("base", xpos="far_left", ypos="head")
        gen "I'd like you to follow them and see what they are doing, find out if there's anything we could use against them during the match." ("base", xpos="far_left", ypos="head")
        cho "You want me to follow them around the entire day?" ("angry", "base", "base", "mid")
        gen "Of course, isn't that what a spy is supposed to do?" ("base", xpos="far_left", ypos="head")
        cho "Yeah, it's not like I have school or anything important to do." ("upset", "base", "angry", "downR")
        gen "Great!" ("grin", xpos="far_left", ypos="head")
        gen "Report back to me this evening as usual B!" ("grin", xpos="far_left", ypos="head")
        cho "Fine..." ("angry", "narrow", "base", "mid")

    elif not states.cho.ev.spy_on_boys.t3_e2_complete: # Completed Ron Weasley?
        # Spy on Ron Weasley

        gen "Ready for some more espionage B?" ("base", xpos="far_left", ypos="head")
        cho "Of course!" ("open", "base", "base", "mid")
        cho "Who are we targeting today?" ("soft", "base", "raised", "mid")
        gen "The keeper... Tom, or whatever his name was." ("base", xpos="far_left", ypos="head")
        cho "Ron..." ("angry", "narrow", "base", "mid")
        gen "Oh, yes. That guy!" ("base", xpos="far_left", ypos="head")
        cho "And what would you have me do?" ("open", "base", "raised", "mid")
        gen "Spy on him, of course!" ("base", xpos="far_left", ypos="head")
        gen "See if there's anything we can use against him during the match." ("base", xpos="far_left", ypos="head")
        cho "Fine... I'll do my best, but don't get your hopes up..." ("soft", "base", "base", "downR")
        gen "You'll do excellent B, now make haste!" ("base", xpos="far_left", ypos="head")
        gen "Quietly, make haste... quietly..." ("base", xpos="far_left", ypos="head")
        cho "As you wish..." ("base", "narrow", "base", "downR")

    elif not states.cho.ev.spy_on_boys.t3_e3_complete: # Completed Harry Potter?
        # Spy on Harry Potter

        gen "Ready for some more espionage B?" ("base", xpos="far_left", ypos="head")
        cho "Of course!" ("open", "base", "base", "mid")
        cho "Who are we targeting today?" ("soft", "base", "raised", "mid")
        gen "The seeker...{w=0.3} that Potter Boy." ("base", xpos="far_left", ypos="head")
        cho "Why do you say his name with such an odd tone?" ("angry", "narrow", "base", "mid")
        gen "Am I? That's how Snape says it..." ("base", xpos="far_left", ypos="head")
        cho "Right... So, what is it that you want me to do with him?" ("open", "base", "raised", "downR")
        gen "I'll tell you what you shouldn't do." ("base", xpos="far_left", ypos="head")
        gen "Don't share your wine with him, or he'll drink it all..." ("base", xpos="far_left", ypos="head")
        cho "Harry drinks your wine?" ("annoyed", "base", "raised", "mid")
        cho "This isn't one of your weird euphemisms again, is it?" ("open", "narrow", "raised", "mid")
        gen "I was talking about Snape." ("base", xpos="far_left", ypos="head")
        cho "I see..." ("soft", "base", "base", "mid")
        gen "Anyhow..." ("base", xpos="far_left", ypos="head")
        gen "The Potter boy!" ("base", xpos="far_left", ypos="head")
        gen "I want you to follow him around, see what he's up to!" ("base", xpos="far_left", ypos="head")
        cho "But what about Hermione?" ("clench", "base", "base", "mid")
        gen "What about her?" ("base", xpos="far_left", ypos="head")
        cho "Harry usually hangs around her at all time, how am I supposed to spy on him if she's around?" ("annoyed", "narrow", "base", "mid")
        gen "I'm sure you'll figure it out..." ("base", xpos="far_left", ypos="head")
        cho "..." ("disgust", "closed", "base", "down")
        cho "Fine, I'll see what I can do..." ("open", "narrow", "base", "downR")
        gen "That's the spirit." ("base", xpos="far_left", ypos="head")

    else:
        gen "Let's spy on those boys some more!" ("base", xpos="far_left", ypos="head")
        cho "Again? I've already spied on them all..." ("angry", "base", "base", "mid")
        gen "You can never have enough intel." ("base", xpos="far_left", ypos="head")
        cho "Right..." ("open", "narrow", "base", "R")
        gen "Make sure to bring me your report as usual B." ("base", xpos="far_left", ypos="head")
        cho "Of course." ("open", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_event

### Tier 3 (pre Gryffindor) ###

label cc_pr_spy_boys_T3_twins:
    ## Weasley Twins - Blueberry candies ##

    $ states.cho.ev.spy_on_boys.t3_e1_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "Mission successful?" ("base", xpos="far_left", ypos="head")
    cho "Well, in terms of not getting caught, I suppose so." ("angry", "closed", "base", "down")
    gen "Then spill those beans B, what did you manage to learn about them?" ("base", xpos="far_left", ypos="head")
    cho "They're pigs. I'll tell you that much." ("annoyed", "base", "angry", "mid")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    cho "Well, I guess calling them pigs is a bit uncalled-for... They're a pair of pranksters, that's for sure." ("open", "closed", "angry", "mid")
    cho "Those two would do anything for a laugh..." ("clench", "narrow", "angry", "mid")
    gen "So, what did they do?" ("base", xpos="far_left", ypos="head")
    cho "They tricked some poor Hufflepuff girls by giving them sweets that they had tampered with..." ("angry", "base", "angry", "downR")
    cho "All with various effects to embarrass whoever ate them..." ("open", "narrow", "angry", "mid")
    cho "As one girl ate one, she turned blue and began swelling until she ended up looking like a giant blueberry." ("clench", "base", "base", "mid")
    gen "That's pretty funny..." ("base", xpos="far_left", ypos="head")
    cho "How is that funny!?" ("angry", "wide", "angry", "mid")
    gen "What if the girl was Hermione?" ("base", xpos="far_left", ypos="head")
    cho "I..." ("angry", "base", "base", "mid")
    cho "I suppose...{w=0.4} No...{w=0.4} No, it's still not--" ("soft", "happyCl", "angry", "mid")
    gen "She'd look like a blueberry with a huge wig draped on top of it." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Giggles*" ("smile", "closed", "base", "mid")
    cho @ cheeks blush "Anyhow...{w=0.4} It completely ruined her clothes, and as she deflated she quickly ran off stark naked and crying to her dormitory." ("annoyed", "closed", "base", "mid")
    gen "Wait, so the clothes didn't expand as well?" ("base", xpos="far_left", ypos="head")
    cho "It's not a spell... she ate it, so why would her clothes be affected?" ("clench", "base", "raised", "mid")
    gen "Sounds like amateurish magic to me... If they just imbued those sweets with some sort of effect which allows the consumer's sweat to permeate their clothes, then..." ("base", xpos="far_left", ypos="head")
    cho "..." ("disgust", "wide", "angry", "mid")
    gen "*Ahem*...{w=0.4} I suppose I better have a word with those two..." ("base", xpos="far_left", ypos="head")
    cho "Please do..." ("annoyed", "narrow", "angry", "mid")

    gen "Anyhow, I'm sure we'll find something we can use against some of the other players." ("base", xpos="far_left", ypos="head")
    cho "I hope so..." ("upset", "base", "angry", "downR")
    gen "Anything else to report?" ("base", xpos="far_left", ypos="head")
    cho "No, that's all." ("angry", "base", "base", "mid")
    gen "Then that will be it for today." ("base", xpos="far_left", ypos="head")
    cho "Okay then." ("open", "base", "base", "R")
    cho "Good night." ("soft", "base", "base", "mid")
    gen "Good night, Miss Chang." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points till 12.
        $ states.cho.public_level += 1

    jump end_cho_event

label cc_pr_spy_boys_T3_ron:
    ## Ron Weasley ##

    $ states.cho.ev.spy_on_boys.t3_e2_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    cho "..." ("annoyed", "base", "angry", "downR") #Annoyed
    gen "Mission successful?" ("base", xpos="far_left", ypos="head")
    cho "No, of course it wasn't..." ("clench", "closed", "angry", "mid")
    cho "It's as if Granger could smell me as soon as I get anywhere near her friend group." ("open", "narrow", "angry", "R")
    gen "So, you didn't manage to glean any sort of information?" ("base", xpos="far_left", ypos="head")
    cho "Well, I'm certain about one thing... That boy is a perv." ("upset", "narrow", "angry", "mid")
    cho "Before Hermione caught me, I could tell he was checking her out any time he could." ("open", "base", "angry", "downR")
    cho "It's quite sad really, you could tell from a mile off that she has no interest in him whatsoever." ("normal", "narrow", "angry", "R")
    gen "Maybe he's not mature enough for his age, but once his character develops, then love and attraction could unexpectedly come into fruition." ("base", xpos="far_left", ypos="head")
    cho "*Pfff*... What kind of soppy romance novels have you been reading?" ("soft", "closed", "angry", "mid")
    cho "In any case... He comes off as the clingy type... If anything ever happened between them, it'd probably be out of pity on Hermione's part..." ("soft", "closed", "angry", "mid")
    gen "And here I thought you'd make the assumption Miss Granger is sleeping with her friends." ("base", xpos="far_left", ypos="head")
    cho "..." ("clench", "base", "base", "down") #Blushing
    cho "Why would you think that?" ("open", "narrow", "angry", "downR")
    gen "No reason..." ("base", xpos="far_left", ypos="head")
    gen "Anyhow... We'll find our way in at some point, I'm sure." ("base", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "base", "base", "downR") #Blushing
    gen "Our mission continues..." ("base", xpos="far_left", ypos="head")
    cho "Right..." ("angry", "narrow", "base", "down")
    cho "I'll be going then... Good night." ("open", "narrow", "base", "down")
    gen "Good night, Miss Chang." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points till 12.
        $ states.cho.public_level += 1

    jump end_cho_event

## Harry Potter ##
label cc_pr_spy_boys_T3_harry:

    $ states.cho.ev.spy_on_boys.t3_e3_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)

    gen "B, you return..." ("base", xpos="far_left", ypos="head")
    gen "Was your mission successful?" ("base", xpos="far_left", ypos="head")
    cho "..." ("disgust", "closed", "angry", "mid")
    cho "This is such a waste of time..." ("open", "base", "angry", "downR")
    gen "I gather you didn't get any useful information?" ("base", xpos="far_left", ypos="head")
    cho "No..." ("annoyed", "base", "angry", "downR")
    cho "I've been hiding in the boys' bathroom, trying to listen in on Harry and Ron." ("open", "closed", "angry", "mid")
    gen "Why in the boys' bathroom?" ("base", xpos="far_left", ypos="head")
    cho "That's the only time Hermione isn't around..." ("soft", "base", "angry", "downR")
    gen "I see, then what were they talking about?" ("base", xpos="far_left", ypos="head")
    cho "Ron was going on about wizard's chess." ("open", "closed", "angry", "mid")
    gen "Wizard's chess?" ("base", xpos="far_left", ypos="head")
    cho "Yes, wizard's--{w=0.4} Surely you know about wizard's chess..." ("angry", "narrow", "raised", "mid")
    cho "It's like regular chess except the pieces move on their own." ("soft", "narrow", "base", "mid")
    gen "Sounds as dull as regular chess." ("base", xpos="far_left", ypos="head")
    gen "Anything else?" ("base", xpos="far_left", ypos="head")
    cho "Harry was talking a bit about quidditch, but it was mostly bragging about some previous win of his." ("annoyed", "narrow", "base", "R")
    cho "Honestly, that boy could learn to be a bit more humble... I have no idea why Hermione hangs around with him." ("soft", "narrow", "angry", "downR")
    cho "Quidditch seems to be the only thing that he has going for him..." ("open", "narrow", "angry", "mid")
    gen "Looks like you two have a lot in--" ("base", xpos="far_left", ypos="head")
    cho "Those three seem to constantly have some sort of dick measuring contest in terms of who is best at something. Harry goes on about Quidditch, Ron about Chess and Hermione..." ("open", "closed", "angry", "mid")
    cho @ cheeks blush "Well, Hermione seems to be the best at pretty much any other subject at this school..." ("annoyed", "base", "angry", "downR")
    gen "I'm sure she'll be very impressed if you manage to win the quidditch cup." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I don't care about her approval... I'm only doing this for me and my house..." ("open", "happyCl", "angry", "mid")
    gen "You tell yourself that..." ("base", xpos="far_left", ypos="head")
    gen "Well, I'm sure we'll find a good tactic to use against them." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I hope so..." ("upset", "closed", "base", "mid")

    cho @ cheeks blush "So, are we done here?" ("angry", "base", "base", "down")
    gen "Yes, that will be all." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Good..." ("upset", "base", "base", "R")
    cho @ cheeks blush "Good night then..." ("open", "base", "base", "mid")
    gen "Good night, Miss Chang." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points till 12.
        $ states.cho.public_level += 1

    jump end_cho_event
