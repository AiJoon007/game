label a_spaced_out_conversation:

    # Setup
    $ fireplace_OBJ.foreground = "fireplace_fire"
    $ game.daytime = False
    $ game.weather = "clear"
    $ chair_OBJ.hidden = True
    stop weather
    call room("main_room")
    stop music fadeout 1
    call gen_chibi("hide")
    show screen with_snape(ani=False)
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}A spaced out conversation.{/color}{/size}"

    hide screen blkfade
    with d5

    play music "music/Anguish.ogg" fadein 1 if_changed

    nar "The flames flickered higher up the fireplace."
    nar "Licking in greedy hunger, as if wanting to taste the wine, the two men sedately drank just out of the fire's reach."
    nar "The men took no notice of the flames, except to silently acknowledge the warmth it provided."
    nar "They were an odd pair, these two, sitting as they frequently did, beside the old fireplace sipping wine."
    nar "One, dressed all in black, with matching flowing black hair, stared sullenly at his glass."
    nar "Perhaps it was the darkness surrounding him that made his skin look so pale."
    nar "And maybe it was only the voluminous robes wrapped loosely across his body that made him appear gaunt."
    nar "The other was even more mysterious..."
    nar "Draped in a gray-white costume, he had a long, flowing beard and a curious aura of both age and vitality."
    nar "Sometimes, if the flames flickered just so, he almost appeared entirely different, as a burly, cowled man with a short curled beard."
    nar "They sat in front of the fire as they did on many nights and talked of worlds upon worlds. And of magic. The dark man was the first to speak."

    sna "So, let me try to understand this..." ("snape_05", ypos="head", trans=d3)
    nar "Snape said slowly."
    sna "You live in a little bottle?" ("snape_05")
    nar "The gray figure nodded."
    sna "How does that work?" ("snape_05")
    gen "I believe it's based on tessaracted space." ("base", xpos="far_left", ypos="head")
    nar "Said Genie, his tone becoming akin to a professor lecturing a class."
    gen "The whole process is very Loki." ("base", xpos="far_left", ypos="head")
    show screen a_spaced_out_conversation_horns
    with d9
    nar "Snape didn't hear the last words as a flicker and shadow from the flames made Genie appear different."
    nar "Almost as if gleaming golden horns arose from his head."
    sna "Come again?" ("snape_03")
    hide screen a_spaced_out_conversation_horns
    with d9
    nar "Snape asked, gaping at the sight before it was gone so fast that he was left unsure if he had seen anything."
    gen "I said, they keep the whole thing low-key." ("base", xpos="far_left", ypos="head")
    nar "Genie repeated."
    gen "Keeps most people from knowing how they make it bigger on the inside." ("base", xpos="far_left", ypos="head")
    sna "Most people?" ("snape_05")
    nar "Snape asked."
    gen "Well, Who knows..." ("base", xpos="far_left", ypos="head")
    nar "Genie answered."
    sna "Do you know?" ("snape_24")
    nar "Snape asked."
    gen "Who knows." ("base", xpos="far_left", ypos="head")
    nar "Genie repeated."
    sna "So, who knows?" ("snape_08")
    nar "Snape asked again, getting a little irritated."
    nar "Patience was not a trait Snape had ever cared to master."
    gen "Yes, Who knows!" ("base", xpos="far_left", ypos="head")
    nar "Genie said."
    show screen with_snape(ani=True)
    nar "Snape flicked his hands impatiently and just decided to move on."
    show screen with_snape(ani=False)
    nar "Determining when Genie was serious or not was still beyond his ability."
    nar "Plus, there had been another one of those weird flickers, and he could have sworn he had seen a multicoloured scarf around Genie's neck."
    sna "And, you then grant the summoner three wishes?" ("snape_01")
    nar "Snape continued."
    sna "Anything they want? You can make anything come true?" ("snape_05")
    gen "Those are the rules of my existence, yes." ("base", xpos="far_left", ypos="head")
    nar "Genie replied, thinking, not for the first time, how limited his real life was."
    sna "That seems stupid." ("snape_09")
    nar "Snape said bluntly."
    nar "Genie smiled. Snape was never much for niceties."
    nar "Genie found it refreshing to talk with someone whose disdain for others so matched his own."
    nar "Snape frowned at that smile. He got along almost perfectly with Genie."
    nar "Their lusts and passions were quite similar..."
    nar "It's just Genie's sense of humour that made Snape doubt his seriousness sometimes."
    sna "You've got the power of a god." ("snape_06")
    nar "Snape pushed forward."
    sna "Can't you just \"wish\" yourself free?" ("snape_05")
    gen "It doesn't work that way." ("base", xpos="far_left", ypos="head")
    nar "Genie said with sadness."
    gen "I can only grant wishes to others." ("base", xpos="far_left", ypos="head")
    nar "Snape shook his head."
    sna "It still seems stupid..." ("snape_06")
    sna "What if I were to visit you in your world and make one of my wishes that you be free to use your magic however you should please?" ("snape_09")
    nar "Genie stared at Snape with something like wonder."
    nar "It takes quite a bit to make an ageless being like Genie gape in awe."
    gen "That's... {w=1.0}That's brilliant!" ("open", xpos="far_left", ypos="head")
    nar "Genie shouted."
    gen "Great Gods, man, that could actually work!" ("smile", xpos="far_left", ypos="head")
    nar "Snape was taken aback by Genie's enthusiastic shout, but quickly recovered."
    nar "He was happy for his friend's excitement, but puzzled."
    sna "Haven't you ever thought of that before?" ("snape_05")
    nar "Snape asked."
    gen "Well, no..." ("base", xpos="far_left", ypos="head")
    nar "Said Genie, and if ageless beings could blush, one would assume that's what Genie would be doing."
    gen "It's not something that ever came up." ("base", xpos="far_left", ypos="head")
    sna "No one suggested it to you?" ("snape_01")
    nar "Snape asked, hoping to skip past Genie's discomfort."
    gen "Surprisingly, when given three opportunities at your fondest dreams, helping others doesn't seem to come up very often." ("base", xpos="far_left", ypos="head")
    nar "Genie said with a sarcastic edge that relieved Snape."
    sna "Well, then..." ("snape_01")
    nar "Snape said."
    sna "After we find a way to get you back to your home, maybe I could come visit you, and we could work something out." ("snape_28")
    nar "Genie eyed him curiously and then, with a bit of his usual humour, then asked."
    gen "Are you sure you could resist the urge to use all three on yourself?" ("grin", xpos="far_left", ypos="head")
    nar "Snape chuckled. He momentarily considered how rarely he chuckled."
    nar "Not with humour, at least. He hadn't really done that since..."
    sna "Yes." ("snape_28")
    nar "Snape said with sudden certainty."
    sna "There is really only one wish I would really want." ("snape_23")
    nar "Genie raised an eyebrow at that, but let it stand."
    gen "What would be your wish, my friend?" ("base", xpos="far_left", ypos="head")
    nar "He asked Snape kindly."
    sna "I wish I could go back and have wooed Lily for my own..." ("snape_23")
    nar "Snape said dreamily. In his mind's eye, he remembered the flaming red hair that lit a fire in his own heart."
    sna "I sometimes wonder if that would have made all the difference." ("snape_29")
    nar "Snape mused."
    sna "If I had been a better, a kinder man than I am today." ("snape_06")
    gen "But would you have been as popular?" ("grin", xpos="far_left", ypos="head")
    nar "Genie asked."
    gen "you were central in every book and movie. Everyone loves you." ("base", xpos="far_left", ypos="head")
    sna "What?" ("snape_05")
    nar "Snape snapped from his reverie. He looked at Genie in confusion."
    gen "I mean, would you have been as powerful?" ("base", xpos="far_left", ypos="head")
    nar "Genie said hastily."
    gen "Wasn't that rejection what drove you to your studies and your mastery?" ("base", xpos="far_left", ypos="head")
    nar "Snape eyed Genie suspiciously, but let the matter pass."
    sna "Yes, but I would sacrifice all that to be rid of this loneliness." ("snape_06")
    nar "Snape returned to his imaginings."
    gen "Well, even if you didn't stay together..." ("base", xpos="far_left", ypos="head")
    nar "Genie said mischievously."
    gen "you could at least have had a little fun with her. Maybe even take her on her wedding night." ("base", xpos="far_left", ypos="head")
    nar "Snape's head snapped up angrily. How dare Genie sully the memory of Lily."
    nar "But then, a wicked thought entered his head."
    sna "*Hmm*... What if the boy wasn't really James' after all?" ("snape_02")
    nar "Snape said, and the smile that formed on his face could have frozen the dancing fire beside them."
    sna "Then, one day, I could reach out to that insipid boy, with his foolish fantasies about Potter and say, \"Harry, I am your father\"!" ("snape_28")
    nar "Genie nodded."
    gen "It could work. You've got the black robes already. You just need the helmet." ("grin", xpos="far_left", ypos="head")
    nar "Snape cocked an eyebrow in confusion. The flames leapt and danced, and Genie flickered once again."
    gen "No mind pay you." ("grin", xpos="far_left", ypos="head")
    nar "Genie said."
    gen "Darkness that path, take you it will." ("grin", xpos="far_left", ypos="head")
    sna "Um?" ("snape_29")
    nar "Snape stammered."
    gen "What?" ("base", xpos="far_left", ypos="head")
    nar "Genie asked."
    sna "For a moment there, I thought you..." ("snape_01")
    nar "Snape trailed off, reluctant to go on."
    gen "You thought {b}I{/b} what?" ("base", xpos="far_left", ypos="head")
    nar "Genie prodded."
    gen "Out with it man!" ("base", xpos="far_left", ypos="head")
    sna "I thought you looked all shrunken, like a deformed house elf." ("snape_06")
    nar "Snape finally managed to say."
    nar "Genie laughed."
    gen "Muppet?" ("base", xpos="far_left", ypos="head")
    sna "No, thanks... I'll just have the wine." ("snape_05")
    nar "Snape replied."
    gen "I'm afraid that's the last of it." ("base", xpos="far_left", ypos="head")
    nar "Genie said, looking mournfully at the bottle."
    nar "He eyed Snape through the red droppings of wine still remaining in his glass. It looked like Snape was bleeding."
    nar "The image disturbed him, and he put his glass down."
    gen "So..." ("base", xpos="far_left", ypos="head")
    nar "Genie coughed once, cleared his throat and continued."
    gen "Did you mean it?" ("base", xpos="far_left", ypos="head")
    sna "About the wishes?" ("snape_05")
    nar "Snape asked."
    gen "Yes." ("base", xpos="far_left", ypos="head")
    nar "Genie said, unable to keep the excitement from his voice."
    gen "Would you really come to my world and set me free with a wish?" ("base", xpos="far_left", ypos="head")
    sna "Why not?" ("snape_06")
    nar "Snape said."
    sna "Assuming we can find a way to send you back." ("snape_09")
    gen "Right." ("base", xpos="far_left", ypos="head")
    nar "Genie said, sobering up."
    gen "There's that." ("base", xpos="far_left", ypos="head")
    nar "Snape looked at his friend and sensed his growing gloom."
    sna "Cheer up, Genie." ("snape_23")
    nar "He said, clapping the image of his old wizard master on the shoulder."
    sna "We just need to be careful. We don't want to make a mistake and send you somewhere crazy." ("snape_05")
    gen "Like a space station?" ("base", xpos="far_left", ypos="head")
    nar "Genie asked, his humour returning with his hope."
    sna "Exactly." ("snape_28")
    nar "Snape replied."
    nar "Not sure what a ‘space station' was."
    sna "We don't want you to end up far, far away." ("snape_24")
    gen "In the final frontier?" ("base", xpos="far_left", ypos="head")
    nar "Genie asked, with a wink that to Snape always meant some kind of inside joke Snape never understood."
    nar "He decided to ignore it as he had many other times."
    sna "Let me continue to research why your powers of transdimensional travel are muted here, and we'll find a way to fix your problem." ("snape_05")
    gen "Both our problems." ("base", xpos="far_left", ypos="head")
    nar "Genie suggested and this time, both of them laughed together."
    sna "You know, Genie, this could be the start of a beautiful friendship." ("snape_23")
    nar "Snape said, standing to leave."
    hide snape_main
    with d3
    gen "Well, you know what the game devs say." ("base", xpos="far_left", ypos="head")
    nar "Genie replied, causing the dark man to pause and look back quizzically."
    gen "Play it again, Snape." ("base", xpos="far_left", ypos="head")

    show screen blkfade
    with d9

    stop music fadeout 3.0

    centered "{size=+7}{color=#cbcbcb}The end.{/color}{/size}"

    $ renpy.end_replay()

screen a_spaced_out_conversation_horns():
    zorder 4

    add "images/rooms/room_of_requirement/horns.webp" xpos 435 ypos 200 zoom 0.5
