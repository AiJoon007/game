
label tonks_chitchat:

    if states.ton.chatted:
        return

    $ states.ton.chatted = True

    # Note: Tonks doesn't use tiers yet.

    # if states.ton.tier == 1:
    #     # $ random_number = renpy.random.randint(MIN, MAX)

    #     pass
    # elif states.ton.tier == 2:
    #     # $ random_number = renpy.random.randint(MIN, MAX)

    #     pass
    # elif states.ton.tier == 3:
    #     # $ random_number = renpy.random.randint(MIN, MAX)

    #     pass
    # elif states.ton.tier == 4:
    #     $ random_number = renpy.random.randint(1, 11)

    # Chitchats #TODO 3, 10 should check if you've done some amount of public favours

    random:
        block:
            ton "Teaching has been so much fun!" ("grin", "base", "raised", "mid")
            ton "It's so much better than working at the Ministry." ("open", "closed", "annoyed", "mid")
            ton "I can't believe how much time I spent in that shit-hole..." ("base", "base", "angry", "R")

        block:
            ton "I spotted another cute girl in my class today..." ("soft", "base", "base", "R")
            ton "I hope she's into points as much as the rest." ("horny", "narrow", "raised", "mid")

        block:
            ton "Don't tell professor McGonagall, but I once used her appearance to search one of the student's underwear drawer..." ("grin", "closed", "worried", "mid")
            ton "They didn't suspect a thing." ("soft", "wink", "base", "mid")

        block:
            ton "Being a teacher certainly has its perks... If I had been caught with firewhisky as a student, I would've been expelled." ("soft", "closed", "annoyed", "mid")
            ton "Now I can have as much as I like, even share some every once in a while." ("grin", "wink", "base", "mid")

        block:
            ton "I sometimes wonder if I should have gone into the medicine field..." ("open", "narrow", "base", "R")
            ton "I could've had Madam Pomfrey's job by now..." ("normal", "base", "base", "mid")
            ton "Maybe I could ask her if she needs any assistance on my off hours." ("soft", "base", "base", "R")

        block:
            ton "I feel like I have a lot more in common with the students than the other teachers..." ("open", "base", "base", "R")
            ton "They're all so old..." ("normal", "base", "base", "up")
            ton "Madam Hooch is cool though, she, and I roll the same way... in more ways than one." ("soft", "base", "base", "mid")

        block:
            ton "I had to keep one of the students after class for special tutoring." ("open", "base", "base", "R")
            ton "As a defence against the dark arts teacher, it is my job to protect them against both outside threats and inner demons..." ("open", "base", "base", "L")
            ton "She has a lot to learn, but it's getting there." ("horny", "base", "raised", "L")

        block:
            ton "Snape doesn't seem to like me much..." ("base", "base", "base", "R")
            ton "First I thought it was because I stole a girding potion in my youth..." ("open", "base", "base", "L")
            ton "But it seems to be more because he wants my job..." ("open", "base", "raised", "mid")
            ton "The sunlight could probably do him some good." ("base", "base", "angry", "mid")

        block:
            ton "When I first saw Snape I thought he must be a vampire..." ("open", "base", "base", "mid")
            ton "Turns out he's just a normal dude with pale skin..." ("open", "base", "base", "R")
            ton "If he were a vampire I would have been all over him..." ("horny", "base", "raised", "R")

        block:
            ton "Good students get a little star from me in the corner on each test." ("open", "base", "base", "mid")
            ton "That doesn't necessarily mean good grades though..." ("base", "base", "base", "mid")

        block:
            ton "We had an accident involving pixies in class today. I can't believe they haven't been taken out of the curriculum." ("open", "base", "base", "R")
            ton "One of the students had her clothes completely destroyed..." ("open", "base", "base", "mid")
            ton "Actually, maybe the pixies aren't that bad..." ("base", "base", "base", "down")

        block:
            ton "I'm not going to throw any of the other teachers under the broom about their teaching methods, but..." ("open", "base", "base", "down")
            ton "I try to not take away points for simple mistakes, I was pretty clumsy myself..." ("soft", "base", "shocked", "downR")
            ton "I like to reward my students rather than punishing them..." ("base", "narrow", "shocked", "mid")

        block:
            ton "There's a secret passage to Honeydukes right outside my classroom..." ("soft", "base", "base", "mid")
            ton "Having free access to the sweetshop has been a real benefit to reward my students." ("base", "base", "base", "R")

        block:
            ton "I hope I'll have enough time to have a positive influence on this school and the students..." ("open", "base", "base", "L")
            ton "If I can't make a mark in the school, I should at least be able to make one on the students." ("horny", "narrow", "base", "mid")

        block:
            ton "Becoming an auror is extremely difficult, and the job is almost entirely dominated by men..." ("upset", "narrow", "worried", "R")
            ton "I think I made the right choice of becoming a teacher." ("open", "closed", "shocked", "mid")

        block:
            ton "My mother was a pure-blood but she was burned off the Black family tree after marrying a muggle-born..." ("open", "base", "base", "down")
            ton "Some people won't understand, but I think you should be allowed to love whoever you want..." ("open", "base", "base", "mid")

        block:
            ton "Don't tell anyone, but I must have spent a fortune on Tolipan Blemish Blitzer in my time studying at Hogwarts..." ("open", "narrow", "base", "downR")
            ton "My parents thought I was just being clumsy and needed replacement materials, but most of the money they sent me was spent on beauty and hair products..." ("annoyed", "base", "base", "R")

        block:
            ton "I only really chased after boys during school because all the other girls did..." ("open", "base", "raised", "down")
            ton "Secretly I just wanted them to chase after me instead..." ("normal", "base", "base", "L")

        block:
            ton "I learned a lot from having Alastor Moody tutor me..." ("soft", "base", "base", "mid")
            ton "Never thought I'd end up being a teacher myself..." ("open", "base", "raised", "down")
            ton "Though my methods are slightly different to his..." ("soft", "base", "base", "downR")

        block:
            ton "I don't like when people call me Nymphadora... It's Tonks!" ("annoyed", "base", "annoyed", "mid")
            ton "Last time someone called me that, I used an engorgement charm on them." ("open", "base", "angry", "R")
            ton "Don't ask me what I aimed at..." ("crooked_smile", "base", "base", "up")

        block:
            ton "My favourite creature has to be the were-wolf..." ("open", "closed", "base", "mid")
            ton "their beast-like nature excites me..." ("soft", "narrow", "base", "mid")
            ton "In another lifetime maybe..." ("base", "base", "raised", "down")

        block:
            ton "The students laughed when I accidentally tripped during my last lesson..." ("open", "base", "base", "R")
            ton "Little did they know I got a good view whilst on the ground..." ("horny", "narrow", "raised", "stare")

        block:
            ton "One of the girls had their boggart turn into a student, and it was pointing and laughing at her..." ("open", "base", "base", "R")
            ton "I'm going to teach her to not be ashamed of her body." ("soft", "narrow", "base", "mid")

        block:
            ton "Today I taught the students about the {i}Tanglepest{/i}..." ("open", "base", "base", "mid")
            ton "A foul creature that is drawn to footwear..." ("open", "base", "base", "R")
            ton "It doesn't actually exist... I just wanted an excuse to have the students show me their feet." ("horny", "base", "base", "mid")

        block if states.gen.ev.tonks.metamorphmagi_aware:
            ton "Since Metamorphmagi can change their skin, I sometimes just don't bother wearing any clothes." ("soft", "base", "shocked", "mid")
            ton "I once changed the colour of my skin and made it look like a tight shirt..." ("grin", "narrow", "base", "R")
            ton "I might have worked topless once or twice..." ("horny", "base", "raised", "mid")

        block if states.gen.ev.tonks.metamorphmagi_aware:
            ton "I often got detentions by morphing into prefects..." ("normal", "base", "base", "R")
            ton "But It was worth it, as I was able to utilize the prefects' bathroom..." ("base", "wide", "base", "mid")

        block if states.gen.ev.tonks.metamorphmagi_aware:
            ton "Most of my abilities are based around emotions..." ("open", "base", "base", "mid")
            ton "My hair can go red when I'm upset or angry..." ("upset", "base", "base", "mid")
            ton "Don't tell anyone, but my natural hair colour is actually more brown..." ("open", "base", "base", "R")
            ton "People think it's pink, but that's because I'm horny all the time." ("base", "base", "base", "down")

        block if states.gen.ev.tonks.metamorphmagi_aware:
            ton "There are rumours that Snape has set up an Age Line to keep students away from his private stash..." ("normal", "narrow", "base", "R")
            ton "Won't stop me borrowing some polyjuice potions though... Not that I need them..." ("open", "base", "base", "R")
            ton "But maybe I can find a girl who doesn't mind drinking it and have some fun." ("horny", "base", "raised", "R")

        block if states.gen.ev.tonks.metamorphmagi_aware:
            ton "I'm a metamorphmagus. I can change my appearance at will..." ("open", "base", "base", "mid")
            ton "Makes spying on the other teachers and students a lot easier..." ("grin", "base", "raised", "mid")

        block if states.gen.ev.tonks.metamorphmagi_aware:
            ton "I can change the shape and length of my tongue any way I want." ("open", "base", "base", "mid")
            ton "Imagine the possibilities..." ("open_wide_tongue2", "narrow", "base", "mid")

        block if states.sus.unlocked:
            ton "Susan is such a lovely girl..." ("open", "base", "base", "mid")
            ton "But she really isn't very confident in her body..." ("open", "base", "raised", "R")
            ton "I do hope your little games can help her open up a bit..." ("base", "base", "base", "mid")

    return
