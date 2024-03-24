
label cho_chitchat:

    if states.cho.chatted:
        return

    $ states.cho.chatted = True

    if states.cho.tier == 1: #Pre Hufflepuff

        random:
            block:
                cho "Of course I nailed my first flying lesson, I was practically born with a broom between my legs." ("smile", "closed", "base", "mid")
                cho "" ("smile", "base", "base", "mid")

            block:
                cho "I've been an avid fan of Quidditch ever since the age of six." ("smile", "base", "base", "mid")
                cho "The Tutshill Tornadoes is my favourite team, and I hope I'll get to where they are one day..." ("base", "base", "base", "mid")

            block:
                cho "I couldn't believe it when they appointed me as a seeker for the Ravenclaw try-outs." ("smile", "narrow", "base", "down")
                cho "It's the most important role in Quidditch! Without a good seeker, the game literally won't end." ("grin", "narrow", "base", "mid")
                cho "" ("base", "base", "base", "mid")

            block:
                cho "I hope I'll be as good a seeker as Roderick Plumpton one day..." ("open", "narrow", "base", "down")
                cho "Managing to catch the snitch in only three and a half seconds is a legendary feat." ("smile", "base", "base", "mid")
                cho "Although I doubt the audience was too happy about paying the full ticket price for that game." ("smile", "narrow", "base", "R")

            block:
                cho "Most students complain about all the walking they have to do to get to their classes." ("open", "base", "base", "mid")
                cho "Lazy is what they are... I've already been up for hours before they even manage to roll out of bed." ("open", "closed", "base", "mid")
                cho "" ("base", "base", "base", "mid")

            block:
                cho "I wish I would've been born when the Tutshill Tornadoes won the British and Irish league five times in a row." ("soft", "narrow", "base", "down")
                cho "Hold on, you were alive when--" ("angry", "base", "base", "down")
                cho "[name_genie_cho], please tell me all you know about it!" ("smile", "wide", "base", "mid")
                cho "" ("base", "base", "base", "mid")

            block:
                cho "[name_genie_cho], could you please have a talk with Professor McGonagall." ("annoyed", "base", "base", "mid")
                cho "She took ten points off Ravenclaw when I arrived late to her class after practice the other day." ("disgust", "base", "base", "R")
                cho "But she's never taken any points off Gryffindor even though some of their team members have arrived late multiple times." ("annoyed", "narrow", "base", "mid")

            block:
                cho "Why don't we learn much about the history of Quidditch in this school?" ("angry", "closed", "base", "mid")
                cho "Although I suppose it wouldn't be history of magic if we focused on something that students actually care about." ("soft", "narrow", "base", "R")

            block:
                cho "I don't want to ask for too much, but..." ("soft", "base", "base", "downR")
                cho "Would you consider installing a landing pad on the Ravenclaw Tower?" ("soft", "wink", "base", "mid")
                cho "And how about making owning a broom mandatory to attend Hogwarts?" ("smile", "base", "base", "mid")

            block:
                cho "As a seeker, it is very important that I keep in shape." ("open", "closed", "base", "mid")
                cho "Even though I spend most of the game searching for the snitch, the required effort to catch that thing is way higher than anything the other players have to endure." ("open", "closed", "base", "mid")
                cho "" ("base", "base", "base", "mid")

            block:
                cho "It's a shame Brooms are so easy to spot... Even flying close to smaller muggle villages is a risk." ("open", "base", "base", "R")

    elif states.cho.tier == 2: #Pre Slytherin

        random:
            block:
                cho "I've got a bunch of admirers now since my win against Hufflepuff." ("smile", "base", "base", "mid")
                cho "But I can't let that distract me from my training." ("base", "base", "base", "mid")

            block:
                cho "I've had a pair of panties go missing after a recent practice game..." ("open", "narrow", "base", "R")
                cho "Not my lucky pair though, fortunately... I only wear those during the official matches." ("soft", "base", "base", "R")

            block:
                cho "I sent an owl telling my parents about our win against Hufflepuff, they couldn't believe it!" ("smile", "happyCl", "base", "mid")
                cho "Although perhaps they would if they knew what I did to beat Cedric..." ("smile", "narrow", "base", "R")
                cho "From what I've heard from my mother, his obsession with panties runs in the family." ("base", "narrow", "base", "R")

            block:
                cho "There's nothing quite like the feeling of the rush of air running through your hair when up on that broom." ("smile", "closed", "base", "mid")
                cho "It's very freeing." ("base", "narrow", "base", "mid")

            block:
                cho "I thought wearing a skirt on a broom would've been terrible, but it wasn't as bad as I had imagined..." ("soft", "narrow", "base", "R")

            block:
                cho "I was quite surprised when you showed so much interest in getting involved with quidditch..." ("soft", "base", "base", "mid")
                cho "I don't think even our team captain shows as much enthusiasm." ("smile", "narrow", "base", "mid")

            block:
                cho "I can't believe your tactical methods were enough to have such an effect on Cedric." ("open", "narrow", "base", "down")
                cho "Boys will be boys I suppose..." ("base", "narrow", "base", "down")

            block:
                cho "I can't believe I thought the Quidditch robes would be enough for the crowd not to notice me wearing a skirt during the last game." ("angry", "narrow", "base", "down")
                cho @ cheeks blush "I wonder how many people saw it before Granger pointed it out..." ("soft", "narrow", "base", "down")

            block:
                cho "People skirting the rules in Quidditch is more common than most people think." ("open", "closed", "base", "mid")
                cho "Illegal broom tampering... Jinxing off the other team's robes..." ("open", "narrow", "base", "downR")
                cho "I'm surprised that you found there's nothing rule breaking about adjustments to your own clothing." ("smile", "narrow", "base", "mid")

            block:
                cho "I can't help but think about what would've happened if it had rained during the game against Hufflepuff." ("angry", "narrow", "base", "R")
                cho "It would probably have weighted down my robes too much to be able to distract Cedric." ("mad", "narrow", "base", "downR")

    elif states.cho.tier == 3: #Pre Gryffindor
        random:
            block:
                cho "I've been getting some odd looks from other students lately." ("soft", "narrow", "base", "R")
                cho @ cheeks blush "*Hmph*... Jealousy, no doubt." ("open", "closed", "base", "mid")

            block:
                cho "[name_genie_cho], can you do anything about those Slytherins?" ("angry", "closed", "base", "mid")
                cho "Ever since my match against them, they don't seem to be able to take their eyes off my ass!" ("disgust", "narrow", "base", "mid")

            block:
                cho "I've been asked a lot about my exercise routines lately." ("soft", "narrow", "base", "R")
                cho "Stretching in particular..." ("open", "narrow", "base", "R")
                cho "No doubt trying to fish for a demonstration." ("base", "narrow", "base", "downR")

            block:
                cho "I've heard a lot more Ravenclaw quidditch chants in school lately. I'm so happy people are getting behind the team!" ("smile", "narrow", "base", "mid")
                cho "Though, a lot of the chants do seem to involve my ass..." ("soft", "narrow", "base", "R")

            block:
                cho @ cheeks blush "If it helps the team win, I don't mind debasing myself." ("open", "closed", "base", "mid")
                cho @ cheeks blush "All the greatest sportspeople in history made sacrifices!" ("open", "closed", "base", "mid")
                cho @ cheeks blush "Y-- yeah, that's what I'll tell them..." ("soft", "narrow", "base", "downR")

            block:
                cho "You know, I have this weird feeling that this Quidditch season is revolving all around me. Like I'm some sort of protagonist in a book." ("disgust", "narrow", "base", "L")

            block:
                cho "Quite a few teachers started giving me weird looks." ("soft", "base", "base", "R")
                cho "Although professor Snape still gives me the same look of contempt as usual..." ("soft", "narrow", "base", "R")

            block:
                cho "I'm glad our dormitory isn't in the basement like Hufflepuff and Slytherin." ("base", "closed", "base", "mid")
                cho "Means I can take my broom for a midnight flight whenever I like." ("smile", "wink", "base", "mid")
                cho "*Err*... I mean... I could do that if it's okay with you..." ("disgust", "narrow", "base", "mid")

            block:
                cho "You know, I think I look quite good wearing tight trousers." ("smile", "base", "base", "mid")
                cho "No wonder those muscle obsessed Slytherins like it so much." ("smile", "narrow", "base", "R")

            block:
                cho "I always appreciate when you call me up to your office..." ("base", "narrow", "base", "mid")
                cho "Although could you do it when we've got potions class next time?" ("smile", "wink", "base", "mid")
                cho "" ("base", "base", "base", "mid")

    elif states.cho.tier == 4: #After Quidditch Finals
        random:
            block:
                cho "I wake up earlier than my fellow teammates so that I can be naked when I do my stretching at the pitch." ("smile", "narrow", "base", "R")
                cho "Of course Madam Hooch is there, setting things up for the day, but she doesn't mind." ("base", "narrow", "base", "R")

            block:
                cho @ cheeks blush "I wonder how many others have adopted Hooch's flying techniques after that last match." ("soft", "narrow", "base", "R")
                cho @ cheeks blush "Hopefully they won't ban it... It is quite literally a game changer..." ("grin", "narrow", "base", "mid")

            block:
                cho "Madam Hooch let me keep her broom, which I'm very thankful for." ("smile", "base", "base", "mid")
                cho @ cheeks blush "Although perhaps it's time I do some personal adjustments..." ("base", "narrow", "base", "R")

            block:
                cho "People are still talking about the Ravenclaw versus Gryffindor game." ("smile", "wink", "base", "mid")
                cho "Not so much the game itself, though..." ("smile", "narrow", "base", "mid")

            block:
                cho "Don't tell anyone... But I've always thought that one of the best parts of flying is the vibrations that come from the broom." ("smile", "narrow", "base", "R")

            block:
                cho "Does your bird always have such a blank look on its face?" ("soft", "narrow", "base", "L")
                cho "I suppose when you're constantly reborn, you must've seen anything and everything there ever is to see." ("soft", "narrow", "base", "L")

            block:
                cho "Robes sure are useful, don't you think?" ("smile", "narrow", "base", "mid")
                cho @ cheeks blush "As long as I keep them closed I could be wearing nothing underneath and nobody would ever know..." ("smile", "narrow", "base", "R")

            block:
                cho "The Slytherin students have been a lot nicer to me lately." ("soft", "base", "base", "mid")
                cho "I suppose since they didn't make the finals, they were at least happy seeing Gryffindor lose." ("smile", "narrow", "base", "mid")

            block:
                cho "The one who was the maddest about Gryffindor losing the Quidditch cup was probably Hermione." ("smile", "narrow", "base", "R")
                cho "The girls on the Gryffindor Quidditch team were more interested in borrowing my broom than holding any sort of grudge." ("base", "narrow", "base", "mid")

            block:
                cho "So... How about we make this office a clothes free zone?" ("base", "narrow", "base", "mid")
                cho "Like enchant the door, so you can't enter if you got clothes on, or something." ("smile", "base", "base", "R")
                cho "I'm sure some bitter old witch or wizard must've invented a spell like that, so people wouldn't wander into their house with their shoes on..." ("base", "narrow", "base", "R")

            block:
                cho "I read somewhere that ejaculate is a good source of protein." ("open", "narrow", "base", "R")
                cho "There's even a cookbook!" ("smile", "wide", "base", "mid")
                cho "The things you find hidden in the library..." ("grin", "narrow", "base", "R")

    return
