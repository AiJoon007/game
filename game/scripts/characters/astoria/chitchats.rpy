
label astoria_chitchat:

    if states.ast.chatted:
        return

    $ states.ast.chatted = True

    # Story related chitchats (marked out as they are meant to be added into randomized set of chats when counter is met)

    # if ag_st_imperio.counter == 1:
    #     ast "Professor Tonks keeps telling me these stupid things about temper and focus." ("clench", "base", "base", "down")
    #     ast "Why can't this stupid curse just work like it should!?" ("open", "base", "angry", "mid")
    #     ast "Stupid...{w=0.5} Cursed...{w=0.5} {size=+5}CURSE!{/size}" ("angry", "narrow", "angry", "down")
    #
    # elif ag_st_imperio.counter == 2:
    #     ast "I've heard about some students taking private tutoring from other teachers..." ("open", "base", "base", "mid")
    #     ast "When Professor Tonks asked me to let her tutor me, I didn't think it was going to be so...{w=0.5} hands on..." ("annoyed", "narrow", "angry", "R")
    #
    # elif ag_st_imperio.counter == 3:
    #     ast "This spell training thing is so easy, Tonks doesn't seem to be able to resist me at all." ("smile", "narrow", "base", "R")
    #     ast "I can't wait for another go at it!" ("open", "narrow", "base", "down")
    #
    # elif ag_st_imperio.counter == 4:
    #     ast "How come you constantly have me use Imperio to make Tonks take her clothes off?" ("annoyed", "narrow", "worried", "mid")
    #     ast "Let's have her do something more fun like...{w=0.4} *uhm*...{w=0.4} bark like a dog or...{w=0.4} step on a lego brick." ("horny", "base", "base", "down")
    #
    # elif ag_se_imperio_sb.counter >= 1:
    #     ast "Susan is such a dumb cow." ("clench", "base", "base", "mid")
    #     ast "I can't believe that she's as gullible as she is." ("angry", "closed", "base", "mid")
    #     ast "Well, I guess that's what you'd expect from a Hufflepuff." ("base", "base", "base", "down")

    # Note: Astoria does not have Tiers yet.

    random:
        block:
            ast "Why do we have to do potions with the Gryffindors?" ("base", "narrow", "worried", "R")
            ast "They have no talent whatsoever, they might as well be Hufflepuffs." ("annoyed", "narrow", "base", "mid")
            ast "You can clearly tell none of them has brewed a Draught of Living Death before." ("annoyed", "base", "base", "mid")

        block:
            ast "Why do we even have muggle studies at Hogwarts?" ("open", "narrow", "angry", "L")
            ast "One of my classmates was forced to take it by her parents, and she's one of the few Slytherins in our year taking it." ("annoyed", "base", "base", "L")
            ast "It's one of the few classes my parents aren't making me take." ("open", "closed", "base", "mid")

        block:
            ast "Divination is one of the worst subjects at this school." ("open", "narrow", "base", "mid")
            ast "We literally sat the entire lesson yesterday staring a tea leaves." ("base", "base", "angry", "R")
            ast "Although that wasn't the worst bit. It was that I had to drink the tea without any sugar whatsoever." ("clench", "base", "base", "mid")

        block:
            ast "Why can't we learn something more useful, like how to make stink pellets or Dung bombs?" ("upset", "narrow", "base", "R")
            ast "When am I ever going to use something as stupid as a Hiccoughing Potion!?" ("annoyed", "base", "base", "mid")
            ast "*Hick*...{w=0.8}...{w=0.8} *Hick!*{w=0.6} Damnit..." ("open", "narrow", "worried", "down")

        block:
            ast "I found the perfect use for the Wingardium leviosa charm today..." ("smile", "base", "base", "mid")
            ast "Granger was being especially annoying, prancing around one of the corridors, so I used it to lift her skirt up!" ("open", "base", "angry", "down")
            ast @ cheeks blush "But she didn't even see that I did it! She just punched that Weasley boy on the arm." ("angry", "narrow", "base", "down")
            ast "Snap-- {i}Professor{/i} Snape saw it, though. I thought I was in trouble for a moment, but he just corrected me on my pronunciation." ("grin", "narrow", "base", "mid")

        block:
            ast "I've still not been able to cast spells properly without saying the words." ("open", "base", "base", "mid")
            ast "Some bullshit about focus..." ("base", "base", "angry", "mid")

        block:
            ast "When are we going to learn the Serpensortia spell?" ("open", "base", "worried", "mid")
            ast "I already asked Professor McGonagall, but she didn't want to teach it to us for some reason..." ("annoyed", "base", "angry", "mid")

        block:
            ast "I used a switching spell to swap one of the clothes of a female Hufflepuff student with one of the Gryffindor boy's." ("smile", "base", "angry", "mid")
            ast "You should've seen the confusion and horror on their faces..." ("grin", "narrow", "base", "L")

        block:
            ast "I just came back with a great haul from the last Hogsmeade trip." ("smile", "narrow", "base", "mid")
            ast "My best purchase was probably the nose biting tea-cup I bought at Zonko's." ("smile", "base", "base", "mid")

        block:
            ast "Could you give me access to the restricted section of the library?" ("open", "base", "base", "mid")
            ast "Miss Pince says I need a note from a teacher to have her fetch a book and that I'm not allowed to actually go in there..." ("annoyed", "base", "base", "mid")

        block:
            ast "Rules are meant to be broken. We break the laws of physics all the time so how come most teachers are so strict?" ("annoyed", "base", "angry", "mid")

        block:
            ast "I was bored during class and doodled a bit on one of the books I brought from the library, and it started smacking me on the head." ("upset", "narrow", "angry", "mid")
            ast "Why is Miss Pince allowed to jinx books when I get in trouble for making somebody's quill turn into a worm when touched?" ("base", "base", "base", "mid")

        block:
            ast "Flying is probably one of my favourite subjects..." ("open", "base", "base", "mid")
            ast "But some of the fun was taken out of it once the other students stopped smashing into things." ("annoyed", "base", "base", "R")

        block:
            ast "History of magic is so dull. Who wants to sit in front of a literal ghost and listen to boring facts for hours on end?" ("clench", "closed", "base", "mid")
            ast "I can't wait to drop the subject once I finish my {i}O.W.L.{/i}s." ("base", "narrow", "base", "down")

        block:
            ast "Professor Snape always seems to look at me whenever something goes wrong during his class... As if it's always going to be me who did it." ("annoyed", "narrow", "angry", "R")
            ast "I mean, I might have, but you can't prove anything..." ("upset", "narrow", "base", "down")

    return
