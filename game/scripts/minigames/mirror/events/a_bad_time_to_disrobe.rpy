
# Mirror story: A bad time to disrobe
label a_bad_time_to_disrobe:

    with d5
    centered "{size=+7}{color=#cbcbcb}A bad time to disrobe{/color}{/size}"

    nar "In this story the genie has found an invisibility cloak."
    nar "And with the cloak come great opportunities."

    label .choices:

    # Setup
    $ hermione.equip(her_outfit_default)
    $ game.daytime = True
    $ game.weather = "clear"
    stop weather
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    menu:
        "-Part 1-":
            jump a_bad_time_to_disrobe_part_1
        "-Part 2-":
            jump a_bad_time_to_disrobe_part_2
        "-Return-":
            $ renpy.end_replay()

label a_bad_time_to_disrobe_part_1:

    call her_chibi("stand","desk","base")

    hide screen blkfade
    with d5

    call music_block
    call bld
    gen "Miss Granger. Have you ever been excited about the thought of being caught?" ("base", xpos="far_left", ypos="head")

    her "Caught?" ("soft", "base", "base", "mid", xpos="right",ypos="base", trans=d3)
    her "In what way, Professor?" ("base", "base", "base", "mid")

    gen "Well, for today's favour I have a prop for you to use." ("base", xpos="far_left", ypos="head")

    her "A prop, sir?" ("base", "base", "base", "mid")

    gen "Yes, I'd like you to put this invisibility cloak on and sneak into one of the boy only areas of the school." ("base", xpos="far_left", ypos="head")

    her "Well, I guess that would be fine..." ("base", "base", "base", "mid")
    her @ cheeks blush "Although it's a bit different from your usual requests." ("soft", "base", "base", "R")

    gen "You'd be naked, of course." ("base", xpos="far_left", ypos="head")

    her "Naked!?! But what if someone sees me?" ("open", "wide", "base", "stare")

    gen "You'd be wearing the cloak..." ("base", xpos="far_left", ypos="head")
    gen "No one would even know you were there." ("base", xpos="far_left", ypos="head")

    her "{size=-7}Thirty-five points...{/size}" ("annoyed", "closed", "angry", "mid")

    gen "Twenty-five points, you said? sounds good to me." ("base", xpos="far_left", ypos="head")

    call her_chibi("stand","desk","base",flip=True)
    her "{size=-7}You heard what I said...{/size}" ("disgust", "closed", "base", "mid", flip=True, trans=dissolve)

    call her_walk("door", "base")
    call her_chibi("leave")

    gen "(Some of that bartering skill put to good use...)" ("grin", xpos="far_left", ypos="head")

    show screen blkfade
    with d5

    $ game.daytime = False
    call music_block

    call her_chibi("stand","desk","base")

    nar "Later that evening, Hermione returns."
    with d3

    hide screen blkfade
    with d5

    call bld
    gen "I'll take that cloak back if you don't mind." ("grin", xpos="far_left", ypos="head")
    her "Certainly." ("base", "base", "base", "mid", xpos="right", ypos="base", flip=False)

    play sound "sounds/cloth_sound3.ogg"
    pause .8

    gen "Now, spill the beans." ("base", xpos="far_left", ypos="head")
    her "I--{w=0.2} I don't have any beans on me, sir." ("soft", "slit", "low", "stare")
    gen "(Is this girl for real?)" ("base", xpos="far_left", ypos="head")
    gen "It's just an expression..." ("base", xpos="far_left", ypos="head")
    gen "Now tell me...{w=0.4} Did you complete your assignment?" ("base", xpos="far_left", ypos="head")
    her "I did, sir...{w=0.4} I sneaked into the boys' dormitory using the cloak, as you suggested." ("soft", "happyCl", "base", "mid")
    gen "Naked?" ("base", xpos="far_left", ypos="head")
    her "Naked...{w=0.2} --ish." ("disgust", "base", "base", "R")
    gen "How can you be naked...{w=0.2} --ish?" ("base", xpos="far_left", ypos="head")
    her "Well, I had to keep my underwear on...{w=0.2} I'd get cold otherwise." ("soft", "narrow", "base", "R")
    gen "Cold? How would you be cold with the cloak on?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*..." ("disgust", "base", "base", "mid")
    gen "*Sigh*... Just tell me what happened next." ("base", xpos="far_left", ypos="head")
    her "Well, a few of the boys were in there." ("base", "base", "base", "mid")
    her "They were playing wizards chess..." ("base", "base", "base", "mid")
    her "Pretty poorly in fact." ("disgust", "wink", "base", "mid")

    gen "..." ("base", xpos="far_left", ypos="head")
    gen "I'm sorry, Miss Granger... But you're going to have to do better than this." ("base", xpos="far_left", ypos="head")
    gen "I expect more from you by now." ("base", xpos="far_left", ypos="head")
    her "So, no points then?" ("angry", "narrow", "annoyed", "mid")
    gen "No, I know you can do better." ("base", xpos="far_left", ypos="head")
    her "Fine! I'll do better next time. Double points! I'll show you!" ("angry", "narrow", "angry", "R")
    gen "That's the spirit. Your house will thank you when you beat the Slytherins by the end of the year." ("base", xpos="far_left", ypos="head")
    her "Thank you professor... I'll remember that for next time." ("grin", "happy", "base", "mid_soft")

    show screen blkfade
    with d3

    show image Text("{image=images/rooms/room_of_requirement/qmark.webp}{size=+4}{color=#cbcbcb}Hermione will remember that{/color}{/size}") as qmark zorder 100:
        pos (10, 10)

    nar "Hermione returns the next morning, looking nervous but more determined than yesterday."

    $ game.daytime = True
    call music_block

    hide qmark
    call her_chibi("stand","desk","base")

    hide screen blkfade
    with d3

    her "I see that you have the cloak ready for me, sir." ("base", "base", "base", "R",xpos="right",ypos="base")
    gen "Indeed... And I'm expecting better from you today, girl." ("base", xpos="far_left", ypos="head")
    her "I won't disappoint you, sir!" ("grin", "base", "base", "mid")
    gen "I'll be the judge of that..." ("base", xpos="far_left", ypos="head")

    hide hermione_main
    show screen blkfade
    with d5

    $ game.daytime = False
    call music_block

    nar "Later that evening, a distraught-looking Hermione enters the office."

    call her_chibi("top_naked","desk","base")
    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")

    hide screen blkfade
    with d5

    her @ tears mascara_soft "..." ("upset", "base", "base", "mid",xpos="right",ypos="base")
    gen "What the-- What, happened? Where's your shirt?" ("base", xpos="far_left", ypos="head")
    her @ tears mascara_soft "What do you think has happened?!" ("upset", "base", "base", "mid")
    gen "Well, I know what I think... But I'd like to hear it from you." ("base", xpos="far_left", ypos="head")
    her @ tears mascara_soft "I didn't want to disappoint, sir, so I did what you asked..." ("soft", "base", "base", "mid")
    her @ tears mascara_soft "I went into the girls' changing room at the Quidditch pitch, undressing and leaving my clothes in one of the lockers." ("base", "base", "base", "mid")
    gen "Well done. And then?" ("base", xpos="far_left", ypos="head")
    her @ tears mascara "I took the cloak and sneaked into the boys' changing room--" ("soft", "squint", "base", "R")
    her @ tears mascara "I didn't want any of them to bump into me, so I decided to stand just around the corner of the doorway." ("open", "base", "base", "mid")
    gen "Judging by your current state, I assume it didn't play out as you thought." ("base", xpos="far_left", ypos="head")
    her @ tears mascara "Well, it did at first... But I had made a miscalculation." ("angry", "base", "base", "mid")
    her @ tears mascara "By thinking I was short enough to fit under the cloak..." ("disgust", "base", "base", "down")
    gen "Right, so your--" ("base", xpos="far_left", ypos="head")
    her @ tears mascara "My feet were completely visible the whole time!" ("upset", "base", "angry", "mid")
    gen "..." ("angry", xpos="far_left", ypos="head")
    her @ tears mascara "And before I knew it, one of the boys was moving closer to inspect them, so I tried to get away, but I slipped...{w=0.4} and...{w=0.4} and." ("upset", "wide", "base", "shocked")
    gen "And what?" ("angry", xpos="far_left", ypos="head")
    her @ tears mascara "My butt fell out!" ("scream", "wide", "worried", "stare")

    gen "{size=18}Thirty points to--{/size}" ("grin", xpos="far_left", ypos="head")

    her @ tears mascara "I'm not finished!" ("open", "narrow", "worried", "down")
    gen "Sorry, you carry on my dear!" ("base", xpos="far_left", ypos="head")
    her @ tears mascara "I sprinted out of there, grabbing as many of my clothes that I could... But even then, I think the boy may have seen me!" ("soft", "narrow", "worried", "mid_soft")
    her @ tears mascara "Professor... I'm beginning to have second thoughts about this whole cloak idea." ("soft", "narrow", "worried", "mid_soft")
    gen "Don't be silly... The boy didn't even see your face, that's what matters." ("base", xpos="far_left", ypos="head")
    her @ tears mascara "But--" ("clench", "narrow", "worried", "mid_soft")
    gen "Even if the cloak was only big enough to cover that bushy head of yours, it would be enough to keep anyone from knowing--" ("base", xpos="far_left", ypos="head")
    her @ tears mascara "Professor!" ("shock", "wide", "base", "mid")
    gen "Just trying to lighten the mood." ("base", xpos="far_left", ypos="head")
    gen "Although I'm sure an extra five points for a job well done should suffice..." ("base", xpos="far_left", ypos="head")
    gen "Thirty-five points to Gryffindor!" ("grin", xpos="far_left", ypos="head")
    her @ tears mascara "Thank you professor..." ("grin", "base", "base", "mid")

    call her_walk ("door", "base")

    her @ cheeks blush tears mascara "(I suppose he's right... Surely nobody would recognize me based on the lower half of my body...)" ("soft", "base", "base", "R", flip=True)
    her @ cheeks blush tears mascara "(Would they?)" ("annoyed", "narrow", "base", "mid")

    call her_chibi("leave")

    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}End of part one.{/color}{/size}"

    jump a_bad_time_to_disrobe.choices

label a_bad_time_to_disrobe_part_2:

    call her_chibi("stand","desk","base")

    hide screen blkfade
    with d5

    call music_block
    call bld
    gen "Good afternoon, Miss Granger." ("base", xpos="far_left", ypos="head")
    her "Good afternoon, Professor... What can I do for you today?" ("base", "base", "base", "mid",xpos="right",ypos="base")
    gen "Glad you asked, I've got another task for you." ("base", xpos="far_left", ypos="head")
    her "Another task? And what task may that be, Professor?" ("soft", "base", "base", "R")
    gen "Well, miss Granger... I think somebody owes me an invisibility cloak." ("base", xpos="far_left", ypos="head")
    her "Oh, do you want me to collect it from somebody?" ("open", "base", "base", "mid")
    gen "That somebody is you, Miss Granger..." ("base", xpos="far_left", ypos="head")
    gen "You left my cloak at the scene of the crime." ("base", xpos="far_left", ypos="head")
    her "Crime? Professor, what have you gotten me into?" ("upset", "narrow", "annoyed", "mid")
    gen "I'm talking about when you went for a visit to the boys' changing room." ("base", xpos="far_left", ypos="head")
    gen "Or have you forgotten already?" ("base", xpos="far_left", ypos="head")
    her "{size=-7}I've tried to.{/size}" ("upset", "base", "worried", "R")
    gen "Sorry?" ("base", xpos="far_left", ypos="head")
    her "I said, I do remember." ("normal", "base", "base", "R")
    gen "Right... Well, good invisibility cloaks are pretty hard to come by..." ("base", xpos="far_left", ypos="head")
    gen "(I think.)" ("base", xpos="far_left", ypos="head")
    her "Really? I thought they were mass-produced?" ("annoyed", "base", "base", "mid")
    her "By house elves I bet..." ("disgust", "closed", "angry", "mid")
    gen "Hey now... I know they might be small, but I wouldn't call them elves." ("base", xpos="far_left", ypos="head")
    gen "In any case, the cloak has more of a sentimental value to me... lots of memories." ("base", xpos="far_left", ypos="head")
    gen "(Like the time when your butt fell out of it.)" ("grin", xpos="far_left", ypos="head")
    gen "Oh, the memories... You must retrieve it for me." ("grin", xpos="far_left", ypos="head")
    her "Fine, I'll do it... Even though I hold you partly responsible for the situation that lead to me dropping it." ("annoyed", "closed", "angry", "mid")
    gen "Great! Let's not dwell on the past, then." ("base", xpos="far_left", ypos="head")
    her "..." ("normal", "narrow", "annoyed", "mid")
    her "Do you happen to have any idea of where it is?" ("open", "base", "base", "mid")
    gen "Well, it hasn't been reported as found, so unless it's been stolen, there's only one place it could be." ("base", xpos="far_left", ypos="head")
    her "The boys' changing room?" ("base", "narrow", "worried", "down")
    gen "The boys 'changing room." ("grin", xpos="far_left", ypos="head")
    her "And how many house points?" ("base", "base", "base", "mid")
    gen "For what exactly?" ("base", xpos="far_left", ypos="head")
    her "Retrieving the cloak, of course." ("annoyed", "base", "base", "mid")
    gen "You're demanding house points, for your own mistakes, Miss Granger?" ("base", xpos="far_left", ypos="head")
    her "But I thought..." ("upset", "base", "worried", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    her "..." ("upset", "narrow", "worried", "down")
    gen "Fine, but only if we continue where we left of." ("base", xpos="far_left", ypos="head")
    her "With my butt out?!?" ("disgust", "wide", "worried", "stare")
    gen "With your butt--" ("base", xpos="far_left", ypos="head")
    gen "No, well... Yes, but this time you'll be prepared." ("base", xpos="far_left", ypos="head")
    her "But... What if they recognise me, sir?" ("open", "base", "worried", "mid")
    gen "If they had recognized you, then I'm sure you'd already know..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "(That's true...)" ("soft", "base", "base", "mid_soft")
    her @ cheeks blush "And then what? You want me to be able to just walk out of there?" ("base", "base", "base", "mid")
    gen "That's for you to figure out, miss Granger. Either way, once you have the cloak, it shouldn't be an issue getting away." ("base", xpos="far_left", ypos="head")
    her "And I want--" ("open", "base", "base", "mid")
    gen "I'll give you forty house points for it." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "(I was going to ask for thirty.)" ("soft", "happy", "base", "R")
    her "I'll do it..." ("base", "base", "base", "mid")
    gen "Great! You're doing an excellent service to your house, and you're making this old man very happy." ("grin", xpos="far_left", ypos="head")
    her "By getting your cloak back, right?" ("base", "base", "worried", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    show screen blkfade
    with d3

    $ game.daytime = False
    call music_block

    nar "Later that evening."

    call her_chibi("stand","door","base")

    hide screen blkfade
    with d3

    call her_walk("desk", "base")
    pause.5

    her @ cheeks blush "..." ("normal", "narrow", "base", "dead",xpos="right",ypos="base")
    gen "Mission success?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("normal", "narrow", "base", "dead")
    gen "Miss Granger?" ("base", xpos="far_left", ypos="head")
    her "Oh, hello professor... Here's your cloak back." ("base", "narrow", "worried", "down")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "So?" ("base", xpos="far_left", ypos="head")
    her "So, what?" ("normal", "happyCl", "worried", "mid")
    gen "So, what about your assignment? How did it go?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh, the assignment... It went very well, thank you... no hurdles in any way." ("soft", "base", "worried", "R")
    gen "Your face is glowing, miss Granger... It's not hard to tell when you're being untruthful." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "It is? I didn't even notice..." ("normal", "narrow", "base", "down")
    gen "You're going to have to elaborate if you'd like those house points." ("base", xpos="far_left", ypos="head")
    her "Oh... okay... I'll just go ahead then." ("mad", "base", "base", "mid")
    gen "Let me get the popcorn." ("base", xpos="far_left", ypos="head")
    her "popcorn? Where would you get popcorn from in this office?" ("annoyed", "base", "base", "mid")
    gen "Magic cupboard." ("grin", xpos="far_left", ypos="head")
    her "Right... I'll just start from the beginning, shall I?" ("base", "narrow", "base", "R_soft")
    her @ cheeks blush "..." ("base", "base", "base", "mid")
    her "So... I went to the boys' changing room when they were busy with their Quidditch practice." ("open", "narrow", "worried", "down")
    gen "{size=+2}*CRUNCH*{/size}" ("base", xpos="far_left", ypos="head")
    her "It's very messy in there... And here I thought that the girls changing room was bad..." ("base", "narrow", "base", "down")
    gen "{size=+3}*CRUNCH* *Chew* *Chew*{/size}" ("base", xpos="far_left", ypos="head")
    gen "{size=+4}*CRUNCH*{/size}" ("base", xpos="far_left", ypos="head")
    her "Anyway... so I rummaged around in that mess..." ("annoyed", "base", "worried", "mid")
    her "I knew it had to be somewhere between the showers and the doorway..." ("base", "base", "base", "mid")
    her "And after looking around for a while, I noticed that the cloak had been pushed underneath one of the benches lining the wall." ("open", "narrow", "worried", "down")
    her "So as I was grabbing for it, I thought to myself... Well, I've already managed to sneak in there, so perhaps I could earn myself some points as well..." ("open", "narrow", "worried", "down")
    her "So I took my clothes off again, and while draping the cloak over me, I began walking to the showers." ("base", "narrow", "base", "down")
    her "But, just as I was about to enter, one of the Slytherin boys emerged in front of me!" ("clench", "base", "worried", "mid")
    gen "{size=+6}*CRUNCH*{/size}" ("base", xpos="far_left", ypos="head")
    her "Professor!" ("scream", "base", "angry", "mid")
    gen "*Cough* *Cough*...{w=0.4} Sorry." ("angry", xpos="far_left", ypos="head")
    her "It is hard enough to talk about this as it is, without your chewing distracting me." ("annoyed", "base", "angry", "mid")

    play sound "sounds/gulp.ogg"
    gen "*Gulp*" ("base", xpos="far_left", ypos="head")

    her "Anyhow..." ("base", "narrow", "angry", "R")
    her "I was expecting that the team would be practising for at least another thirty minutes." ("open", "base", "base", "mid")
    her "But that's when the boy walked in..." ("normal", "closed", "base", "mid")
    her "And I panicked and rushed to hide in one of the toilets." ("open", "base", "worried", "R")
    gen "Smart." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("base", "base", "base", "mid")
    her "If I had been smart, I would've taken into consideration why someone might go to the changing room before practice is finished..." ("base", "narrow", "base", "down")
    gen "To drain the snake, no doubt." ("grin", xpos="far_left", ypos="head")
    her "Do you want me to continue or not?" ("annoyed", "narrow", "annoyed", "mid")
    gen "You're the one receiving the points here, I'm just providing the means of earning them." ("base", xpos="far_left", ypos="head")
    her "*Hmph*..." ("normal", "narrow", "worried", "down")
    her "As I was saying..." ("base", "narrow", "base", "down")
    her "At this point it was already too late... Just as I realised my mistake, he had already opened the door." ("base", "closed", "base", "mid")
    her @ cheeks blush "Since the room was so small, I tried to back into a corner... But to no avail..." ("base", "narrow", "base", "down")
    her "The only thing I could do was pray that he wasn't about to sit down, and to position myself right up against the back of the toilet... With my legs around the base." ("clench", "happyCl", "worried", "mid")
    her "..." ("disgust", "narrow", "base", "down")
    gen "And did he?" ("base", xpos="far_left", ypos="head")
    her "No... But he was close enough for me to feel his..." ("mad", "squint", "worried", "up")
    her "His..." ("base", "slit", "worried", "ahegao")
    gen "His what, Miss Granger?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "His penis... It brushed up against the robes." ("annoyed", "closed", "base", "mid")
    gen "How did he manage that?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well... The boy wasn't there for the purpose of relieving himself... Well, at least not how one would expect it..." ("open", "closed", "angry", "mid")
    gen "He was jacking it!?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Ehm*... Yes... And I suppose he was too busy to notice that his tip was brushing up against--" ("normal", "base", "worried", "mid")
    her @ cheeks blush "*Ahem*..." ("open", "base", "worried", "R")
    gen "..." ("base", xpos="far_left", ypos="head")
    her "I'd like my points now." ("base", "narrow", "worried", "down")
    gen "Certainly, miss Granger..." ("base", xpos="far_left", ypos="head")
    gen "Forty points to Gryffindor!" ("base", xpos="far_left", ypos="head")
    her "Thank you professor..." ("soft", "base", "base", "mid_soft")

    call her_walk("door", "base")

    her @ cheeks blush "(I probably shouldn't tell him about having to clean the cloak before bringing it back to him...)" ("base", "narrow", "base", "dead", flip=True)
    her @ cheeks blush "(*Mmm*... I can still remember the smell of it...)" ("normal", "narrow", "worried", "down")
    her @ cheeks blush "(Wait, what am I thinking? Snap out of it, Hermione...)" ("base", "happyCl", "worried", "mid")

    call her_chibi("leave")

    call blkfade
    centered "{size=+10}{color=#cbcbcb}The end{/color}{/size}"

    jump a_bad_time_to_disrobe.choices
