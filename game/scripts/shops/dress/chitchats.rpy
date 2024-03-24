label purchase_outfit(item):
    #
    # Hermione Granger
    #

    if item == her_outfit_maid:
        $ maid_outfit_ITEM.owned = 1

        gen "I'd like to order a maid outfit." ("base", xpos="far_left", ypos="head")
        maf "A maid outfit, what on earth for? Surely the house elves are keeping your office tidy."
        gen "The what?" ("base", xpos="far_left", ypos="head")
        gen "No, you got this all wrong... It's going to be a present." ("base", xpos="far_left", ypos="head")
        maf "For whom?"
        gen "I'm afraid I can't say." ("base", xpos="far_left", ypos="head")
        maf "Well as long as it's not for a student..."
        maf "Did you have any style in mind?"
        gen "Preferably a French maid." ("base", xpos="far_left", ypos="head")
        maf "..."
        maf "Well I should have it available for pick-up in a few days after I get the materials in."
        gen "Thank you." ("base", xpos="far_left", ypos="head")
    elif item == her_outfit_nightie:
        gen "I'd like to order a custom outfit today." ("base", xpos="far_left", ypos="head")
        maf "Certainly honey... Repairing these conservative school clothes all day has been quite dull, to say the least."
        gen "Well, I can assure you that this outfit is not conservative." ("base", xpos="far_left", ypos="head")
        maf "*Hmm*?"
        gen "I'd like to order a girl's Nightgown." ("base", xpos="far_left", ypos="head")
        maf "Well, that doesn't seem overly--"
        gen "And make it out of silk!" ("base", xpos="far_left", ypos="head")
        maf "*Ahh*... So, I assume that you also want it transparent?"
        gen "If that is possible." ("base", xpos="far_left", ypos="head")
        maf "Of course it is possible, who do you take me for?"
        maf "I just have to order in the materials, although silk is not cheap."
        gen "Don't worry about the cost." ("base", xpos="far_left", ypos="head")
        maf "As you wish sweetie... It should be ready shortly."
        gen "Thank you." ("base", xpos="far_left", ypos="head")
    elif item == her_outfit_ball:
        $ parcel_callbacks.append(renpy.curry(setattr)(ball_outfit_ITEM, "owned", 1))

        if not states.her.ev.yule_ball.e4_complete:
            gen "Could you make a dress for me?" ("base", xpos="far_left", ypos="head")
            maf "A dress? Do you mean something like a ball dress, or more burlesque?"
            gen "*Hmm*... A ball dress does sound good, actually." ("base", xpos="far_left", ypos="head")
            maf "How surprising..."
            gen "I was thinking that I could have a custom one made. For a very good girl of mine." ("base", xpos="far_left", ypos="head")
        else:
            gen "Do you sell Ball dresses?" ("base", xpos="far_left", ypos="head")
            maf "*Hmm*... I suppose I do, although they're nothing special... Why do you ask?"
            gen "A 'girl' approached me with a problem. Apparently, she's unable to acquire a dress for this year's autumn ball." ("base", xpos="far_left", ypos="head")
            maf "How tragic.... Well, I'm sure that one of these cheap ones will suffice."
            gen "I was thinking I could have a custom one made... She is a very good girl." ("base", xpos="far_left", ypos="head")
        maf "Very well! I'll make her the best dress this school's ever seen. If you say she's been such a good girl..."
        maf "It should be ready in about a week."
        gen "A week? Why so long?" ("base", xpos="far_left", ypos="head")
        maf "I'm ordering my next batch of material in a couple of days to keep the cost down..."
        maf "Or I could order it now if you pay a bit extra..."
    elif item == her_outfit_msmarv:
        gen "Tell me, Madam Mafkin... Have you ever heard of superheroes?" ("base", xpos="far_left", ypos="head")
        maf "Yes, yes... Those people in the comic books. My grandson is quite fond of them."
        gen "Fantastic, I was wondering if it would be possible for you to make me a costume." ("base", xpos="far_left", ypos="head")
        maf "Certainly, who did you have in mind?"
        gen "Do you know Ms Marvel?" ("base", xpos="far_left", ypos="head")
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this tonight, so I can take a look."
        gen "Thank you very much." ("base", xpos="far_left", ypos="head")
        maf "No need to thank me honey. Payment will suffice."
    elif item == her_outfit_hslut:
        gen "Have you ever seen a burlesque show, Madam?" ("base", xpos="far_left", ypos="head")
        maf "I've done more than that, I've designed a few of the outfits for them!"
        gen "Splendid, in that case I'd love to commission one." ("base", xpos="far_left", ypos="head")
        maf "Most Certainly, any particular colour in mind?"
        gen "Red!" ("base", xpos="far_left", ypos="head")
        maf "As you wish."
        gen "Thank you very much." ("base", xpos="far_left", ypos="head")
        maf "You're quite welcome, sir."
    # elif item == hg_costume_power_girl_ITEM:
        # gen "I was wondering if it would be possible for you to make me a superhero costume." ("base", xpos="far_left", ypos="head")
        # maf "Certainly, who did you have in mind?"
        # gen "Do you know Power Girl?" ("base", xpos="far_left", ypos="head")
        # maf "I'm afraid not..."
        # maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend, so I can take a look."
        # gen "Thank you very much." ("base", xpos="far_left", ypos="head")
        # maf "No need to thank me sir. Payment will suffice."
    elif item == her_outfit_croft:
        gen "Would you be able to make me a cosplay costume?" ("base", xpos="far_left", ypos="head")
        maf "Certainly, what are you after?"
        gen "Do you happen to know Lara Croft?" ("base", xpos="far_left", ypos="head")
        maf "I'm afraid not..."
        gen "She's a video game character..." ("base", xpos="far_left", ypos="head")
        maf "Well, my little squib grandson loves video games. I'm sure he can show me what she looks like."
        gen "Thank you very much." ("base", xpos="far_left", ypos="head")
        maf "You're welcome."
        maf "I'll be seeing him tonight, so I should be able to complete this one slightly faster than usual."
        gen "Fantastic." ("base", xpos="far_left", ypos="head")
    # elif item == hg_outfit_christmas_ITEM:
        # gen "I was wondering if it would be possible for you to make me a festive costume." ("base", xpos="far_left", ypos="head")
        # maf "Certainly, what holiday are you looking to \"celebrate\"?"
        # gen "Christmas." ("base", xpos="far_left", ypos="head")
        # maf "At this time of year?"
        # gen "It's never too early to start the festivities..." ("base", xpos="far_left", ypos="head")
        # maf "Evidently not. I'll have it done as soon as I can. "
        # gen "Thank you very much." ("base", xpos="far_left", ypos="head")
        # maf "You're welcome. I'll even give you a special price. Consider it my Christmas gift to you..."
        # gen "Thank you." ("base", xpos="far_left", ypos="head")
    # elif item == hg_outfit_pirate_ITEM:
        # gen "I want a pirate outfit" ("base", xpos="far_left", ypos="head")
        # maf "ok"
    elif item == her_outfit_bioshock:
        gen "Have you ever heard of Bioshock infinite?" ("base", xpos="far_left", ypos="head")
        maf "Biology what now?"
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "It's a video game..." ("base", xpos="far_left", ypos="head")
        maf "I assume you want the costume from it?"
        gen "If it's not too much..." ("base", xpos="far_left", ypos="head")
        maf "Consider it done!"
        gen "Thank you very much." ("base", xpos="far_left", ypos="head")
        maf "You're welcome."
    elif item == her_outfit_yennefer:
        gen "Have you ever heard of the sorceress Yennefer?" ("base", xpos="far_left", ypos="head")
        maf "Of course! The mother of a universe hopper isn't quickly forgotten..."
        gen "Think you could make me a version of her outfit?" ("base", xpos="far_left", ypos="head")
        maf "Certainly."
        gen "Thank you very much." ("base", xpos="far_left", ypos="head")
        maf "Toss a coin to your tailor."
    elif item == her_outfit_bikini1:
        gen "I'd like to order a bikini." ("base", xpos="far_left", ypos="head")
        maf "A bikini sir? Isn't that a bit cold in this climate?"
        gen "A leather bikini!" ("base", xpos="far_left", ypos="head")
        maf "Are you even--"
        gen "You think you could make something like that for me?" ("base", xpos="far_left", ypos="head")
        maf "Of course sir, as you wish..."
    elif item == her_outfit_bikini2:
        gen "I'd like to order a bikini." ("base", xpos="far_left", ypos="head")
        maf "Of course, what kind of bikini would you like?"
        gen "One that covers the important bits!" ("base", xpos="far_left", ypos="head")
        maf "And who is this bikini for if you don't mind me asking?"
        gen "I do mind..." ("base", xpos="far_left", ypos="head")
        maf "Alright then..."
        maf "Your bikini shall be ready shortly."
        gen "Excellent..." ("base", xpos="far_left", ypos="head")
    elif item == her_outfit_bunny:
        gen "Could you make me a bunny costume?" ("base", xpos="far_left", ypos="head")
        maf "A bunny costume? Do you mean something like the Easter bunny?"
        gen "No, like the ones you might see in Vegas!" ("base", xpos="far_left", ypos="head")
        maf "I'll see what I can--"
        gen "With big bunny ears!" ("base", xpos="far_left", ypos="head")
        maf "Okay then..."
    elif item == her_outfit_swimsuit:
        gen "I need a swimsuit." ("base", xpos="far_left", ypos="head")
        maf "Swimming at your age?"
        gen "Hey, you're only as old as you feel..." ("base", xpos="far_left", ypos="head")
        gen "And no, it's not for me... I need a woman's swimsuit." ("base", xpos="far_left", ypos="head")
        maf "I see... Well, it's about time you set up some swimming lessons..."
        maf "Are you looking for a design to fit the school colours?"
        gen "No, thank you... Something sporty shall suffice." ("base", xpos="far_left", ypos="head")
        maf "..."
        maf "I'll have to look through some of those muggle magazines then..."
        maf "It will be ready shortly."
    elif item == her_outfit_egypt:
        gen "I'd like something that one of my old flames used to wear..." ("base", xpos="far_left", ypos="head")
        maf "An old what, sir?"
        gen "Cleopatra..." ("base", xpos="far_left", ypos="head")
        gen "Ah... What a looker she was..." ("base", xpos="far_left", ypos="head")
        maf "Sweetie, are you okay? Do you want me to fetch the nurse?"
        gen "Would you be able to make me something Egyptian themed?" ("base", xpos="far_left", ypos="head")
        gen "Like the outfits Cleopatra used to wear..." ("base", xpos="far_left", ypos="head")
        maf "..."
        gen "I'll trade you two camels for it." ("base", xpos="far_left", ypos="head")
        maf "Cleopatra you said?"
        gen "Yes..." ("base", xpos="far_left", ypos="head")
        maf "That would require some metal work... Perhaps one of my contacts in Diagon alley..."
        gen "So... up for the challenge?" ("base", xpos="far_left", ypos="head")
        maf "*Hmm*..."
        gen "Or is this too much for {b}the{/b} Mafkin?" ("base", xpos="far_left", ypos="head")
        maf "It most certain isn't!"
        maf "I'll have it ready for you in no time!"
        maf "Although I'd prefer to be paid in gold rather than in camels."
        gen "Ask and you shall receive!" ("base", xpos="far_left", ypos="head")
    elif item == her_outfit_latex_dress:
        gen "Ready to work with some latex?" ("base", xpos="far_left", ypos="head")
        maf "Latex... now that's something I don't get to work with often..."
        maf "Anything particular in mind?"
        if pink_condoms_ITEM.owned > 0:
            gen "Yes... something like this." ("base", xpos="far_left", ypos="head")
            maf "Is that a condo--"
            gen "But you'd cut a heart shape here..." ("base", xpos="far_left", ypos="head")
            maf "..."
            gen "And a hole for the head, obviously." ("base", xpos="far_left", ypos="head")
        else:
            gen "It needs to be tight, that's for sure." ("base", xpos="far_left", ypos="head")
            maf "Naturally..."
            gen "Pink would look good I think!" ("base", xpos="far_left", ypos="head")
            maf "Noted..."
            gen "An make a heart shaped--" ("base", xpos="far_left", ypos="head")
            maf "I'll get it done shortly."
            gen "But I wasn't finished!" ("base", xpos="far_left", ypos="head")
        maf "I think I got the gist of it."
        maf "One latex outfit--"
        maf "With a heart shaped cut-out..."
        maf "I'll have to sharpen my scissors for this one..."
        gen "So you'll make it?" ("base", xpos="far_left", ypos="head")
        maf "Certainly."
        gen "Fantastic!" ("base", xpos="far_left", ypos="head")
    elif item == her_outfit_tifa:
        gen "I'd like a cosplay costume." ("base", xpos="far_left", ypos="head")
        maf "Good idea! Who are we thinking, Gandalf the grey or--"
        gen "Not for me!" ("angry", xpos="far_left", ypos="head")
        maf "Oh... I should've realised..."
        gen "No, I'd like a Tifa cosplay!" ("base", xpos="far_left", ypos="head")
        maf "Ti-fa? Sir?"
        gen "Yes, she's from a video game." ("base", xpos="far_left", ypos="head")
        maf "I'll have to ask my squib grandson about that one... Hopefully he knows who she is."
        gen "Oh, he'll know her, even if he's never played it... could even be his final fantasy." ("base", xpos="far_left", ypos="head")
        maf "Okay then, I shall floo him, and then I'll get that outfit ready for you."
        gen "(She'll do what to him?)" ("base", xpos="far_left", ypos="head")
        maf "Anything else?"
    elif item == her_outfit_witch:
        gen "Do you have time to make a cosplay costume?" ("base", xpos="far_left", ypos="head")
        maf "A cosplay costume?"
        gen "Well, it's more of a Halloween costume." ("base", xpos="far_left", ypos="head")
        gen "One of those witch outfits muggle girls would wear during Halloween." ("base", xpos="far_left", ypos="head")
        maf "Oh... those..."
        gen "Any problem?" ("base", xpos="far_left", ypos="head")
        maf "Those costumes look nothing like a real witch's costume..."
        maf "Oh Well... If I'm to make one, it's going to be the best of the best..."
        gen "Great!" ("base", xpos="far_left", ypos="head")
    elif item == her_outfit_latex:
        gen "I'd like an outfit... a latex one!" ("base", xpos="far_left", ypos="head")
        maf "Latex?"
        maf "Now you do know what kind of outfits are known to be made by latex, don't you, honey?"
        gen "Of course... And I'd like one of those very much." ("base", xpos="far_left", ypos="head")
        maf "Okay then... just making sure."
    elif item == her_outfit_teddy:
        gen "I need a teddy nightgown." ("base", xpos="far_left", ypos="head")
        maf "A teddy--"
        gen "It's a gift..." ("base", xpos="far_left", ypos="head")
        maf "Is this \"gift\" for one of the teachers?"
        gen "I--" ("base", xpos="far_left", ypos="head")
        maf "Oh... don't tell me... Is it for miss Tonks?"
        gen "It's--" ("base", xpos="far_left", ypos="head")
        maf "No... that'd be silly... McGonagall perhaps?"
        maf "No... I shouldn't pry..."
        maf "So, you want it in green then? It's her favourite colour."
        gen "Black shall do fine..." ("base", xpos="far_left", ypos="head")
        maf "Black?! Is it for Professor Sn--"
        gen "Madam..." ("base", xpos="far_left", ypos="head")
        maf "My apologies... I'll get going on this as soon as possible! Can't let a lady wait, can we?"
    elif item == her_outfit_fishnet:
        gen "Could you make me a fishnet outfit?" ("base", xpos="far_left", ypos="head")
        maf "A fishnet... outfit, sir?"
        gen "Yes, like the stockings but a whole outfit..." ("base", xpos="far_left", ypos="head")
        gen "Actually, just a top and underwear shall do." ("base", xpos="far_left", ypos="head")
        maf "Underwear--? surely something like that wouldn't be very effective as underwear, sir?"
        gen "Effective enough to catch a fish..." ("base", xpos="far_left", ypos="head")
        maf "What?"
        gen "So, could you be so kind and make this for me?" ("base", xpos="far_left", ypos="head")
        maf "..."
        maf "Of course, sir."
        gen "Excellent..." ("base", xpos="far_left", ypos="head")
    elif item == her_outfit_fishnet_onepiece:
        gen "I'm looking to require a one-piece fishnet outfit." ("base", xpos="far_left", ypos="head")
        maf "A fishnet outfit?"
        gen "Yes, one-piece please Madam." ("base", xpos="far_left", ypos="head")
        maf "I see."
        gen "Not the sea... For the bedroom." ("base", xpos="far_left", ypos="head")
        maf "Right... Well, you're the boss..."
    elif item == her_outfit_bikini3:
        gen "Madam, I require your finest bikini!" ("base", xpos="far_left", ypos="head")
        maf "Oh my, aren't you a quick one, at least buy me a dinner first."
        gen "...!" ("angry", xpos="far_left", ypos="head")
        gen "You got it wrong... I want to buy a custom-made bikini." ("base", xpos="far_left", ypos="head")
        maf "Oh..."
        maf "Are you looking for anything specific?"
        gen "How about a sling bikini?" ("base", xpos="far_left", ypos="head")
        maf "Are you asking me? You're the one making the order."
        gen "Sling bikini it is! Great idea Madam!" ("base", xpos="far_left", ypos="head")
        maf "Of course, sir..."
        maf "I'll get to it then..."
    elif item == her_outfit_cheerleader_1:
        gen "Could you make me a Gryffindor cheerleader outfit?" ("base", xpos="far_left", ypos="head")
        maf "You're not showing favouritism towards Gryffindor's Quidditch team again, are you, sir?"
        gen "Of course not..." ("angry", xpos="far_left", ypos="head")
        maf "*Hmm*..."
        gen "You have my word that there's no favouritism towards Gryffindor's team going on here." ("base", xpos="far_left", ypos="head")
        maf "Alright then..."
    elif item == her_outfit_cheerleader_2:
        gen "Could you make me a Gryffindor cheerleader outfit?" ("base", xpos="far_left", ypos="head")
        maf "You're not showing favouritism towards--"
        gen "Although could you make it more like this? *scribbles*..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        maf "Oh...{w=0.6} Oh I see..."
        maf "So, you're not planning for this to be used during an actual Quidditch match, I assume?"
        gen "I have no idea what you're talking about..." ("base", xpos="far_left", ypos="head")
        maf "Well, we all do have our fantasies..."
        gen "I thought this was a respectable establishment." ("base", xpos="far_left", ypos="head")
        gen "I didn't come here to be accused of such foul--" ("base", xpos="far_left", ypos="head")
        maf "Very well, sir."
        maf "I shall get to work on it shortly."
        gen "..." ("base", xpos="far_left", ypos="head")

    #
    # Cho Chang
    #

    elif item == cho_outfit_sailor:
        gen "I'd like a sailor's outfit today." ("base", xpos="far_left", ypos="head")
        maf "A sailor's outfit? We're a bit far from the sea, are we not?"
        gen "True, I was just thinking about something in that style." ("base", xpos="far_left", ypos="head")
        maf "The style of a sailor's outfit and what else?"
        gen "Something that doesn't cover all of the hull!" ("base", xpos="far_left", ypos="head")
        maf "Doesn't cover the hull? What do you--"
        maf "Oh, I see what you mean..."
        maf "Yes... that could be done."
        gen "Perfect." ("base", xpos="far_left", ypos="head")
    elif item == cho_outfit_misty:
        gen "I'd like a cosplay outfit please." ("base", xpos="far_left", ypos="head")
        maf "Yes?"
        gen "Do you know Pokémon?" ("base", xpos="far_left", ypos="head")
        maf "Of course!"
        gen "I... Wait, you do?" ("base", xpos="far_left", ypos="head")
        maf "No, I have no clue what you just said..."
        gen "...{w} I'd like a Misty outfit..." ("base", xpos="far_left", ypos="head")
        maf "A misty outfit? I'm good, but I don't think even I could make an outfit out of mist!"
        gen "She's a character from Pokémon..." ("base", xpos="far_left", ypos="head")
        maf "Oh... I see, maybe my grandson will know."
        gen "I'm sure he will..." ("base", xpos="far_left", ypos="head")
    elif item == cho_outfit_j_school:
        gen "Can you make me a school girl uniform?" ("base", xpos="far_left", ypos="head")
        maf "Make you one? Don't you mean repair a uniform?"
        gen "No, I'd like a Japanese school girl uniform." ("base", xpos="far_left", ypos="head")
        maf "I see..."
        gen "One of the Japanese wizarding schools require a new design." ("base", xpos="far_left", ypos="head")
        maf "Is that so?"
        maf "So why did they contact you about it?"
        gen "*Err*... Their headmaster liked your work!" ("base", xpos="far_left", ypos="head")
        maf "Really? What did he say?"
        gen "*Eh*... {i}Sugoi!{/i}" ("base", xpos="far_left", ypos="head")
        maf "..."
        maf "I didn't know you spoke Japanese..."
        gen "*Ha-Hah*, Yeah... {i}Subarashii pantsu!{/i}" ("base", xpos="far_left", ypos="head")
        maf "What does that mean?"
        gen "Nice pants!" ("base", xpos="far_left", ypos="head")
        maf "Pants?!"
        gen "*Ehm*... American English..." ("base", xpos="far_left", ypos="head")
        maf "Oh, I see..."
        gen "So... Can you make the outfit?" ("base", xpos="far_left", ypos="head")
        maf "Certainly... I'll get started right away."
        gen "{i}Domo Arigato Mr Roboto.{/i}" ("base", xpos="far_left", ypos="head")
    elif item == cho_outfit_dress1:
        gen "Could you make me a traditional Chinese dress?" ("base", xpos="far_left", ypos="head")
        maf "Now, who on earth could this dress be for?"
        gen "It's a gift I'll be sending to one of the Chinese wizarding schools." ("base", xpos="far_left", ypos="head")
        maf "Really? Any particular reason to be sending them a dress?"
        gen "Yes... *Ehm*... It's important to be on good terms with the other wizarding schools, is it not?" ("base", xpos="far_left", ypos="head")
        gen "So what better gift than a traditional Chinese dress?" ("base", xpos="far_left", ypos="head")
        maf "Something that they don't have already, perhaps..."
        gen "Sorry?" ("base", xpos="far_left", ypos="head")
        maf "Nothing... Of course I'll make it for something this important!"
        gen "Great!" ("base", xpos="far_left", ypos="head")
    elif item == cho_outfit_lacelingerie:
        gen "I'd like to order some lace lingerie please." ("base", xpos="far_left", ypos="head")
        maf "lingerie..."
        maf "Well I sure don't keep any of that in stock... I'll have to order some."
        maf "*Hmm*... There's this shop in Knockturn alley."
        maf "Not that I've ever been..."
        gen "Of course..." ("base", xpos="far_left", ypos="head")
        maf "Yes, I should be able to procure some for you."
        gen "Excellent." ("base", xpos="far_left", ypos="head")
    elif item == cho_outfit_bikini:
        gen "Bikini please!" ("base", xpos="far_left", ypos="head")
        maf "Straight to the point..."
        gen "Just straps and some fabric to cover up the goods should do..." ("base", xpos="far_left", ypos="head")
        maf "I see..."
        maf "And should I even ask who this is for?"
        gen "If you'd like my continued patronage, I'd prefer if you didn't." ("base", xpos="far_left", ypos="head")
        maf "I suppose the extra income does help with my retirement fund..."
        maf "Okay then... micro bikini coming right up..."
    elif item == cho_outfit_toon:
        gen "Ever heard of Space Jam?" ("base", xpos="far_left", ypos="head")
        maf "Space... Jam, sir?"
        gen "Yes." ("base", xpos="far_left", ypos="head")
        maf "Is that what the youths are eating these days?"
        gen "No, it's not an actual--" ("base", xpos="far_left", ypos="head")
        gen "Nevermind..." ("base", xpos="far_left", ypos="head")
        gen "I need an outfit made." ("base", xpos="far_left", ypos="head")
        maf "Right..."
        gen "This is what I'm talking about..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        maf "Oh... Oh, I see..."
        maf "This is one of those muggle sports uniforms."
        maf "Why didn't you just say so?"
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Could you make one like this?" ("base", xpos="far_left", ypos="head")
        maf "Certainly, sir."
    elif item == cho_outfit_chun_li:
        gen "Miss Mafkin, ever heard of street fighter?" ("base", xpos="far_left", ypos="head")
        maf "I'd rather not talk about it if you don't mind, sir."
        maf "I left those days behind me a long time ago..."
        gen "What are you-- I meant the video game." ("base", xpos="far_left", ypos="head")
        maf "Oh..."
        gen "What were you talking about?" ("base", xpos="far_left", ypos="head")
        maf "Nothing... So, you want an outfit made from this game?"
        gen "I... Yes, something Chun-Li inspired if you please..." ("base", xpos="far_left", ypos="head")
        maf "Alright then, I'll ask my grandson to give me some reference material."
    elif item == cho_outfit_bunny:
        gen "I need a bunny costume." ("base", xpos="far_left", ypos="head")
        maf "Don't tell me you're trying to prove the existence of the were-rabbit again."
        gen "The what?" ("base", xpos="far_left", ypos="head")
        maf "May I remind you about the time you almost got shot by one of the centaurs, when they mistook you for a giant rabbit?"
        gen "(Did this really happen?)" ("base", xpos="far_left", ypos="head")
        gen "I don't want an actual bunny costume..." ("base", xpos="far_left", ypos="head")
        gen "I want one of those sexy bunny outfits, the one you might see in a magazine." ("base", xpos="far_left", ypos="head")
        maf "I see."
        maf "Alright then, I'll see what I can do."

    elif item == cho_outfit_virgin_killer:
        gen "Virgin killer?" ("base", xpos="far_left", ypos="head")
        maf "Not so much these days, but you should've seen me in my--"
        maf "Oh, you're referring to the jumper."
        gen "Of course, although now I'm more intrigued about--" ("base", xpos="far_left", ypos="head")
        maf "I doubt that would be a good idea... You pay me by the hour, after all."
        gen "... Alright then." ("base", xpos="far_left", ypos="head")
        maf "I shall have your jumper ready as soon as possible."
    elif item == cho_outfit_sheer_nightie:
        gen "I'm looking to procure a nightie." ("base", xpos="far_left", ypos="head")
        maf "A nightie, sir? Don't you mean a nightgown?"
        gen "A nightie." ("base", xpos="far_left", ypos="head")
        maf "..."
        gen "It's not for me." ("base", xpos="far_left", ypos="head")
        maf "Oh, I see..."
        maf "So, it's for a lady friend?"
        gen "That's right." ("base", xpos="far_left", ypos="head")
        maf "A nightie for a lady friend... Alright then, I'll see what I can do."

    elif item == cho_outfit_sporty_bikini:
        gen "Would you be able to make me a sporty bikini set, madam?" ("base", xpos="far_left", ypos="head")
        maf "Most certainly."
        gen "I'll need it to withstand copious amounts of stretching." ("base", xpos="far_left", ypos="head")
        maf "Naturally..."
        gen "And they need to be tight-fitting..." ("base", xpos="far_left", ypos="head")
        maf "Yes, that's a given..."
        gen "And could you make them in dark blue?" ("base", xpos="far_left", ypos="head")
        maf "Yes, of course sir..."
        gen "And have a--" ("base", xpos="far_left", ypos="head")
        maf "Yes, yes, anything you like, sir."
        gen "I was going to say, have a lovely day." ("base", xpos="far_left", ypos="head")
        maf "Oh, of course sir, you as well."
    elif item == cho_outfit_club_dress:
        gen "I'm looking to procure a dress, if it's not too much trouble." ("base", xpos="far_left", ypos="head")
        maf "A dress you say... Now that is one of my specialities!"
        gen "It is?" ("base", xpos="far_left", ypos="head")
        maf "Well, technically everything is my speciality."
        maf "So, are you looking for something formal?"
        maf "For dancing?"
        maf "A summer dress perhaps?"
        gen "I was thinking more similar to something you'd wear at a nightclub." ("base", xpos="far_left", ypos="head")
        maf "Oh, I see..."
        gen "Is that a problem?" ("base", xpos="far_left", ypos="head")
        maf "Of course not... I am just contemplating what type of design I should go with..."
        maf "Alright... I believe I got it."
        gen "Already?" ("base", xpos="far_left", ypos="head")
        maf "Of course!"
        maf "I shall have the dress done shortly."
        gen "Excellent." ("base", xpos="far_left", ypos="head")
    #
    # Astoria Greengrass
    #

    elif item == ast_outfit_ann:
        gen "I'd love if you could make me a cosplay outfit." ("base", xpos="far_left", ypos="head")
        maf "Certainly, sir... as long as you could point me to some reference material."
        gen "Of course, it's Ann Takamaki from Persona 5." ("base", xpos="far_left", ypos="head")
        maf "What is a Ann Takamaki?"
        maf "Is it one of them {i}vidya{/i} games?"
        gen "Yes, she's from one of them... {i}vidya{/i} games." ("base", xpos="far_left", ypos="head")
        maf "I'll ask my grandson about it, he's constantly in front of those flat muggle crystal balls."
        gen "You mean a monitor?" ("base", xpos="far_left", ypos="head")
        maf "Sorry?"
        gen "Never mind..." ("base", xpos="far_left", ypos="head")
        maf "Once I've asked him, I'll get that {i}souvlaki{/i} costume ready for you as soon as possible!"
        gen "Takama--{w=0.4} I'm sure he'll know what you mean..." ("base", xpos="far_left", ypos="head")

    #
    # Luna Lovegood
    #

    elif item == lun_outfit_nightie1:
        gen "I need a nightie." ("base", xpos="far_left", ypos="head")
        maf "A nightie, sir?"
        gen "Yes...{w=0.4} One of the girls had theirs stolen." ("base", xpos="far_left", ypos="head")
        maf "Right... So, what type of nightie was stolen from her?"
        gen "I believe it was loose fitting... And translucent!" ("base", xpos="far_left", ypos="head")
        maf "Don't you mean Opaque, sir?"
        gen "No... Pretty sure I'm correct on this one." ("base", xpos="far_left", ypos="head")
        maf "...{w=0.4} Alright then... I'll get started on it now then, shall I?"
        gen "That'd be great, I mean we can't let her sleep naked, can we?" ("base", xpos="far_left", ypos="head")
        maf "..."
    elif item == lun_outfit_nightie2:
        gen "Could you make me a nightie?" ("base", xpos="far_left", ypos="head")
        maf "Certainly... Any specifications?"
        gen "Translucent please." ("base", xpos="far_left", ypos="head")
        maf "Right... I meant more about the shape."
        gen "Oh..." ("base", xpos="far_left", ypos="head")
        maf "Although from that comment I think I see what you're going for..."
        maf "I'll get started on it as soon as possible."
        gen "Excellent." ("base", xpos="far_left", ypos="head")
    elif item == lun_outfit_lace1:
        gen "I need some lace underwear." ("base", xpos="far_left", ypos="head")
        maf "Right... Is this a gift for someone?"
        gen "Nah, just thought I'd experiment a bit... You're never too old to pick up a new hobby." ("base", xpos="far_left", ypos="head")
        maf "Really?"
        gen "No, of course it's a gift." ("base", xpos="far_left", ypos="head")
        maf "Of course, sir."
        maf "A set of lace underwear as a gift it is."
    elif item == lun_outfit_bikini3:
        gen "Could you make me a bikini, Madam?" ("base", xpos="far_left", ypos="head")
        maf "I can make anything, I'm an expert tailor."
        gen "Great, then I'd like one that only covers what it needs to." ("base", xpos="far_left", ypos="head")
        maf "Oh, I'm not sure I have enough material sir..."
        gen "What, you don't have--" ("base", xpos="far_left", ypos="head")
        gen "Oh I see what you're doing..." ("base", xpos="far_left", ypos="head")
        maf "I think I have some old scraps lying around which would be perfect for this..."
        gen "Great!" ("base", xpos="far_left", ypos="head")
    elif item == lun_outfit_swimsuit:
        gen "I need a swimsuit." ("base", xpos="far_left", ypos="head")
        maf "Going to the lake for a swim are we?"
        gen "It's for one of the students." ("base", xpos="far_left", ypos="head")
        maf "I see..."
        gen "Gotta stay in shape and all that, you know how it is..." ("base", xpos="far_left", ypos="head")
        maf "Alright, so something sporty then?"
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Yeah, I suppose that will have to do." ("base", xpos="far_left", ypos="head")
    elif item == lun_outfit_flight_attendant:
        gen "I need a flight attendant outfit." ("base", xpos="far_left", ypos="head")
        maf "A flight attendant outfit? Is that a muggle thing?"
        gen "Yes, it's what the staff wears inside of a plane." ("base", xpos="far_left", ypos="head")
        maf "A plain what, sir?"
        gen "Yes a... Surely, you must've seen a plane before?" ("base", xpos="far_left", ypos="head")
        maf "..."
        gen "Big metal thing in the sky..." ("base", xpos="far_left", ypos="head")
        maf "Oh! The giant metal birds!"
        gen "I suppose you could call them that..." ("base", xpos="far_left", ypos="head")
        gen "Some people use them to travel." ("base", xpos="far_left", ypos="head")
        maf "How silly..."
        gen "I know right..." ("base", xpos="far_left", ypos="head")
        gen "...{w} Anyway, you think you could make an outfit like that?" ("base", xpos="far_left", ypos="head")
        maf "I suppose... I'll have to ask my grandson what it looks like, but it shouldn't be a problem."
        gen "Excellent." ("base", xpos="far_left", ypos="head")
    elif item == lun_outfit_party:
        if not states.her.ev.yule_ball.e4_complete: #If the ball hasn't been brought up yet
            gen "Could you make a dress for me?" ("base", xpos="far_left", ypos="head")
            maf "Certainly, what type of dress would you like?"
            gen "Something weird would do well I think..." ("base", xpos="far_left", ypos="head")
            gen "Something completely out there and non-modern..." ("base", xpos="far_left", ypos="head")
            gen "Something--" ("base", xpos="far_left", ypos="head")
            maf "Are you trying to wind me up, sir?"
            gen "I'm deadly serious..." ("base", xpos="far_left", ypos="head")
            maf "Okay then, well... in that case I'll have to throw fashion out the window..."
        elif not states.her.ev.yule_ball.started: #If the ball has been brought up but not happened
            gen "One of the students needs a dress for the upcoming ball." ("base", xpos="far_left", ypos="head")
            maf "Weren't they required to bring an outfit at the start of the school year?"
            gen "Yes, although you know how scatterbrained students can be." ("base", xpos="far_left", ypos="head")
            maf "And what kind of style of dress would she like?"
            gen "Something eccentric and weird is what she'd normally go for, I believe..." ("base", xpos="far_left", ypos="head")
            maf "So this student is the kind of person that just likes to be different then?"
            gen "Yes... she's quite the odd ball..." ("base", xpos="far_left", ypos="head")
            maf "Okay then, well... in that case I'll have to throw fashion out the window..."
        else: #After the ball
            gen "I need a ball dress..." ("base", xpos="far_left", ypos="head")
            maf "A ball dress?"
            maf "Didn't the ball already take place?"
            gen "Oh yeah..." ("base", xpos="far_left", ypos="head")
            maf "So..."
            gen "So I need something odd, like this..." ("base", xpos="far_left", ypos="head")
            play sound "sounds/scribble.ogg"
            maf "That..."
            maf "Well I guess we're lucky the ball already happened."
            gen "Why is that?" ("base", xpos="far_left", ypos="head")
            maf "Well... Nevermind... I'll make this for you then, shall I?"
        gen "As soon as possible, please." ("base", xpos="far_left", ypos="head")
        maf "I'll see what I can do..."
        gen "Good luck!" ("base", xpos="far_left", ypos="head")
    elif item == lun_outfit_muggle:
        gen "I need some custom clothing done, something like this..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        gen "You think you could make that?" ("base", xpos="far_left", ypos="head")
        maf "Shouldn't be a problem..."
        maf "Isn't that skirt is a bit odd though?"
        gen "I'm sure she'll love it." ("base", xpos="far_left", ypos="head")
        maf "If you say so..."
    elif item == lun_outfit_summer:
        gen "Could you make me something good for the summer?" ("base", xpos="far_left", ypos="head")
        maf "You're going to need to be more specific, I'm afraid."
        gen "Oh... Some shorts and a crop top!" ("base", xpos="far_left", ypos="head")
        maf "Alright then. That shouldn't be that--"
        gen "And make the crop top very tight, please!" ("base", xpos="far_left", ypos="head")
        maf "Tight, sir?"
        maf "But if I do that, it won't stay down very easy."
        gen "Gives the puppies an easier time to breathe." ("base", xpos="far_left", ypos="head")
        maf "Puppies, sir? I'm not sure I follow."
        gen "Trust me, it's for their own good." ("base", xpos="far_left", ypos="head")
        maf "... Alright then, sir... A tight crop top it is."
    elif item == lun_outfit_harley_quinn:
        gen "I need a super villain costume." ("base", xpos="far_left", ypos="head")
        maf "Headmaster by day, villain by night is it?"
        gen "..." ("base", xpos="far_left", ypos="head")
        maf "Or is it for somebody else?"
        gen "You got it." ("base", xpos="far_left", ypos="head")
        maf "Alright then, so who is this villain then?"
        gen "Do you know Harley Quinn?" ("base", xpos="far_left", ypos="head")
        maf "I'm afraid not..."
        gen "She's that crazy chick who's in love with the joker." ("base", xpos="far_left", ypos="head")
        maf "I see... so a villainess then?"
        gen "Sorry?" ("base", xpos="far_left", ypos="head")
        maf "Like a female villain."
        gen "I don't think anyone ever calls it that." ("base", xpos="far_left", ypos="head")
        maf "In any case, I'm sure that my grandson has a comic with her. I'll just have to wrestle it out of his grubby little hands."
        gen "Thank you very much." ("base", xpos="far_left", ypos="head")
        maf "You're quite welcome."
    elif item == lun_outfit_bunny:
        gen "I'm looking to acquire a bunny costume." ("base", xpos="far_left", ypos="head")
        maf "Certainly sir, how big is the bunny?"
        gen "How big is the-- I'm talking about--" ("base", xpos="far_left", ypos="head")
        maf "Just a little joke professor, I'm aware of what you meant."
        gen "Oh... I see... Good one!" ("base", xpos="far_left", ypos="head")
        maf "I'll get working on it as soon as possible."
    #     gen "Could you make me a Ravenclaw Cheerleader outfit?" ("base", xpos="far_left", ypos="head")
    #     maf "You're not showing favouritism towards Ravenclaw's Quidditch team, are you?"
    #     gen "I'm merely looking to see if it'd be worth to bring cheerleading to this country." ("base", xpos="far_left", ypos="head")
    #     maf "If that's the case, then I want some royalties in case these designs are supposed to be widespread."
    #     gen "Oh they'll be widespread alright..." ("base", xpos="far_left", ypos="head")
    #     maf "Great, then that's settled."
    #     gen "(Wait, what did she say?)" ("base", xpos="far_left", ypos="head")
    #     maf "I'll get it done as soon as possible."
    # elif item == ll_lingerie_silk_ITEM:
    #     gen "I need some silk underwear... Do you happen to have any on hand?" ("base", xpos="far_left", ypos="head")
    #     maf "Male or female?"
    #     gen "*Err*..." ("base", xpos="far_left", ypos="head")
    #     maf "Female it is..."
    #     maf "Well, it shouldn't take that much material, so I'll have them done for you rather quickly."
    #     gen "Great." ("base", xpos="far_left", ypos="head")
    #     maf "And I'll be sure to keep this transaction our little secret..."
    #     gen "Right..." ("base", xpos="far_left", ypos="head")
    #     maf "As long as you're wearing the robes it shouldn't be an issue."
    #     gen "That's good to know..." ("base", xpos="far_left", ypos="head")
    #     gen "Wait, what?" ("angry", xpos="far_left", ypos="head")

    #
    # Nymphadora Tonks
    #

    elif item == ton_outfit_school:
        gen "Do you have any spare school uniforms?" ("base", xpos="far_left", ypos="head")
        maf "There should be a couple lying around..."
        maf "Did one of the students spill a potion on theirs again?"
        gen "Not exactly... it's for a friend." ("base", xpos="far_left", ypos="head")
        gen "And they'd probably go for something closer to this sketch..." ("base", xpos="far_left", ypos="head")
        maf "Let me see..."
        maf "Right...{w=0.4} So what kind of friend is this again?"
        gen "A very good one." ("base", xpos="far_left", ypos="head")
        maf "Alright then, I'll see what I can do."
        gen "Excellent." ("base", xpos="far_left", ypos="head")
    elif item  == ton_outfit_casual:
        gen "I'm looking for something casual and tight-fitting." ("base", xpos="far_left", ypos="head")
        maf "That's pretty vague... could you be more specific about what you had in mind?"
        gen "Well... it should be modern..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        maf "Right... *scribbles*."
        maf "What else?"
        gen "How about... One of those tied tops." ("base", xpos="far_left", ypos="head")
        maf "Tied top... got it."
        gen "And latex leggings!" ("grin", xpos="far_left", ypos="head")
        maf "Latex--"
        maf "Now how is this supposed to be modern?"
        gen "*Err*..." ("base", xpos="far_left", ypos="head")
        maf "No matter... I'll get to work on it as soon as possible."
    elif item  == ton_outfit_nightie:
        gen "I'm looking to acquire a nightgown." ("base", xpos="far_left", ypos="head")
        maf "Right, any specifications?"
        gen "It should be the type you'd wear on hot summer nights." ("base", xpos="far_left", ypos="head")
        maf "So, something see-through... got it."
        gen "..." ("base", xpos="far_left", ypos="head")
        maf "Is that all?"
        gen "Yes, that should be all." ("base", xpos="far_left", ypos="head")
        maf "One see-through... nightgown coming right up."
    elif item == ton_outfit_bunny:
        gen "I need a bunny suit, something similar to what they'd wear at a casino." ("base", xpos="far_left", ypos="head")
        maf "*Hmm*...{w=0.3} Not sure what casino's you've been to, but I think I know what you mean..."
        gen "With big bunny ears!" ("grin", xpos="far_left", ypos="head")
        maf "Alright..."
        maf "If that's all, I need to go source the materials for these...{w=0.3} ears."
        gen "Yes, that will be all." ("base", xpos="far_left", ypos="head")
    elif item == ton_outfit_silky:
        gen "I'm looking for something Greek... like a toga." ("base", xpos="far_left", ypos="head")
        maf "A toga, sir?"
        gen "Yes, although maybe more of a modern take on it." ("base", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        maf "Right... *scribbles*..."
        maf "so, something like this then?"
        gen "*Hmm*... close, but maybe you should remove some of this material and replace it with something like this... *scribbles*." ("base", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        maf "Oh...{w=0.8}Oh my..."
        gen "Is that doable?" ("base", xpos="far_left", ypos="head")
        maf "Doable certainly... although it's a bit..."
        gen "A bit, what?" ("base", xpos="far_left", ypos="head")
        maf "Never mind... I'll do it."
        gen "Excellent..." ("base", xpos="far_left", ypos="head")
    elif item == ton_outfit_bikini_1:
        gen "Could you make be a simple bikini-bra?" ("base", xpos="far_left", ypos="head")
        maf "Certainly, looking for any particular pattern?"
        gen "A Plain one should be fine." ("base", xpos="far_left", ypos="head")
        maf "Alright then, I'll get to work on it shortly."
        gen "Thank you very much!" ("base", xpos="far_left", ypos="head")
    elif item == ton_outfit_bikini_2:
        gen "Could you make be a simple bikini-bra?" ("base", xpos="far_left", ypos="head")
        maf "Certainly, looking for any particular pattern?"
        gen "A Striped one would be great." ("base", xpos="far_left", ypos="head")
        maf "Alright then, I'll get to work on it shortly."
        gen "Thank you very much!" ("base", xpos="far_left", ypos="head")
    elif item == ton_outfit_bikini_3:
        gen "Could you make be a bikini-bra?" ("base", xpos="far_left", ypos="head")
        maf "Certainly, looking for any particular pattern?"
        gen "Something to show off our national heritage." ("base", xpos="far_left", ypos="head")
        maf "So a Scottish flag?"
        gen "What, no... I meant the Union Jack." ("base", xpos="far_left", ypos="head")
        maf "Oh... {i}Righto{/i}..."
        maf "One Union Jack bikini-bra it is..."
        gen "(Scottish... As if I wouldn't know straight away that we were in Scotland...)" ("base", xpos="far_left", ypos="head")
    elif item == ton_outfit_bikini_4:
        gen "Could you make be a bikini-bra?" ("base", xpos="far_left", ypos="head")
        maf "Certainly, looking for any particular pattern?"
        gen "How about the American flag?" ("base", xpos="far_left", ypos="head")
        maf "Are you sure? I thought you weren't meant to put it on clothing."
        gen "You're not?" ("base", xpos="far_left", ypos="head")
        maf "I'm fairly sure I read that somewhere..."
        gen "Well, I think if it's being made into something meant to contain immense greatness, then we could make an exception." ("base", xpos="far_left", ypos="head")
        maf "I'm not sure what you mean, sir..."
        gen "Don't worry about it..." ("base", xpos="far_left", ypos="head")
        maf "Okay then..."
        maf "One United States of America patterned bikini-bra coming up."
    elif item == ton_outfit_swimsuit_1:
        gen "Got any swimsuits?" ("base", xpos="far_left", ypos="head")
        maf "Not in stock but I could make you one."
        gen "Fair enough, I doubt you would've carried what I need anyway." ("base", xpos="far_left", ypos="head")
        maf "Is that so?"
        gen "Yes, I'd like something a bit more skimpy than what you'd normally make." ("base", xpos="far_left", ypos="head")
        maf "Skimpier than normal... I see..."
        gen "Oh! Could you also make it a bit translucent?" ("base", xpos="far_left", ypos="head")
        maf "Certainly..."
        maf "Anything else?"
        gen "*Err*... Did I mention that I wanted it to be skimpy?" ("base", xpos="far_left", ypos="head")
        maf "I was more wondering if you wanted a certain pattern or similar."
        gen "A plain one should be fine." ("base", xpos="far_left", ypos="head")
        maf "Okay then, one transparent swimsuit coming--"
        gen "Transparent and skimpy!" ("base", xpos="far_left", ypos="head")
        maf "One transparent and skimpy swimsuit coming up."
    elif item == ton_outfit_swimsuit_2:
        gen "I need a swimsuit." ("base", xpos="far_left", ypos="head")
        maf "Don't you mean swim trunks, sir?"
        gen "Not for me, obviously." ("base", xpos="far_left", ypos="head")
        maf "Right."
        gen "I need a striped, translucent swimsuit." ("base", xpos="far_left", ypos="head")
        maf "Translucent? Doesn't that defeat the purpose a bit?"
        gen "That would depend on what the purpose is..." ("base", xpos="far_left", ypos="head")
        maf "Well, you'd think that you could just go to a nudist beach."
        gen "Have you seen any around here?" ("base", xpos="far_left", ypos="head")
        maf "Can't you just Apparate to one, sir?"
        gen "Do what?" ("base", xpos="far_left", ypos="head")
        maf "Apparate."
        gen "..." ("base", xpos="far_left", ypos="head")
        maf "Teleport..."
        gen "Oh... Why didn't you just say that?" ("base", xpos="far_left", ypos="head")
        gen "Why do wizards keep making up these silly words when teleportation is already a well established term." ("base", xpos="far_left", ypos="head")
        maf "..."
        maf "So?"
        gen "So, what?" ("base", xpos="far_left", ypos="head")
        maf "Why couldn't you just--"
        gen "..." ("base", xpos="far_left", ypos="head")
        maf "Never mind... Who am I to question the headmaster..."
    elif item == ton_outfit_swimsuit_3:
        gen "I need a swimsuit." ("base", xpos="far_left", ypos="head")
        maf "Right, any specifications?"
        gen "Put the American flag on it!" ("base", xpos="far_left", ypos="head")
        maf "The American flag, sir?"
        gen "Yeah!" ("base", xpos="far_left", ypos="head")
        maf "Any particular reason?"
        gen "Would I need a reason to want to put the American flag on things?" ("base", xpos="far_left", ypos="head")
        maf "... I suppose not."
        gen "And make it translucent!" ("base", xpos="far_left", ypos="head")
        maf "Any particular--"
        maf "..."
        maf "Of course headmaster, I'll get started on it then."
    elif item == ton_outfit_cavegirl:
        gen "I'm looking for something primal." ("base", xpos="far_left", ypos="head")
        maf "Primal, sir?"
        gen "Yes... Ever watched the Flintstones?" ("base", xpos="far_left", ypos="head")
        maf "The what, sorry?"
        gen "*Sigh*..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        gen "Could you make me something like this? *Scribbles*" ("base", xpos="far_left", ypos="head")
        maf "I see..."
        maf "Are you sure you've drawn it correctly?"
        maf "There seems to be some fabric missing."
        gen "Positive." ("base", xpos="far_left", ypos="head")
        maf "Okay then."
        maf "One... Flintstone outfit, it is."
        gen "Yabadababoob!" ("grin", xpos="far_left", ypos="head")

    elif item == ton_outfit_club_dress:
        gen "Have you ever been out clubbing, Miss Mafkin?" ("base", xpos="far_left", ypos="head")
        maf "By merlin no... I wouldn't dare hurt an animal."
        gen "Not that... Clubbing Is when you go to a club, listen to music whilst moving your arms around awkwardly." ("base", xpos="far_left", ypos="head")
        maf "Oh... In that case, yes, although it's been a while."
        maf "They used to call me the dancing queen--"
        gen "Yes, yes, very interesting... Loud music with no way of chatting anyone up... Love it." ("base", xpos="far_left", ypos="head")
        gen "Anyway..." ("base", xpos="far_left", ypos="head")
        maf "..."
        gen "You think you could provide me with something a woman might wear when going clubbing?" ("base", xpos="far_left", ypos="head")
        maf "Something tight-fitting I assume."
        gen "Wow, you really do know your craft!" ("base", xpos="far_left", ypos="head")
        maf "Certainly sir, I'll start working on it as soon as I can."

    elif item == ton_outfit_skimpy_dress:
        gen "Could you make me something skimpy?" ("base", xpos="far_left", ypos="head")
        maf "Skimpy, sir?"
        gen "Yes, something with loose hanging fabric." ("base", xpos="far_left", ypos="head")
        gen "Something that makes the nipples part of the integral structure of the piece." ("base", xpos="far_left", ypos="head")
        maf "..."
        maf "This is for a lady I assume?"
        gen "I mean my nipples could probably cut glass when hard... But yes, it's for a lady." ("base", xpos="far_left", ypos="head")
        maf "Was that extra information necessary, sir?"
        gen "Is it normal or do I need to get them checked?" ("base", xpos="far_left", ypos="head")
        maf "I'm not a medical expert, sir... I'm a tailor."
        gen "Ever had to repair a piece of clothing due to nipple damage?" ("base", xpos="far_left", ypos="head")
        maf "Can't say that I have..."
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Then forget what I just said." ("base", xpos="far_left", ypos="head")
        maf "I'll just get to it then, shall I?"
        gen "Yes please..." ("base", xpos="far_left", ypos="head")

    elif item == ton_outfit_lady_D:
        gen "Could you make me a cosplay outfit?" ("base", xpos="far_left", ypos="head")
        maf "Of course, as long as I know it."
        gen "Well, you should know this one." ("base", xpos="far_left", ypos="head")
        gen "It's none other than lady Dimitrescu." ("base", xpos="far_left", ypos="head")
        maf "*Hmm*... Well, I can't say that I've heard of her."
        gen "She's a video game character." ("base", xpos="far_left", ypos="head")
        maf "I see... In that case, I'll have to ask my grandson..."
        gen "I'm sure if your grandson has spent any time online, he'll know who she is." ("base", xpos="far_left", ypos="head")
        maf "On line, sir?"
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Just ask him, and I'm sure he'll know." ("base", xpos="far_left", ypos="head")

    elif item == ton_outfit_mechanic:
        gen "Could you make me a mechanic attire?" ("base", xpos="far_left", ypos="head")
        maf "A mechanic attire?"
        gen "You know, a mechanic, a person whose sole job is repairing things like cars, machinery, you name it." ("base", xpos="far_left", ypos="head")
        maf "I see, one of those muggle jobs."
        maf "Speaking of repairs--"
        gen "Nope, sorry, I don't know how to fix your computer." ("base", xpos="far_left", ypos="head")
        maf "My what?"
        gen "Nevermind." ("base", xpos="far_left", ypos="head")
        maf "I only wanted to say that maybe it's time to quit loafing around, our roof is leaking again."
        gen "Oh. Sure, I'll get Snape to fix that as soon as possible." ("base", xpos="far_left", ypos="head")
        maf "Do you mean Mr Filch?"
        gen "(I didn't know his reputation was so low, people call him filth so openly...)" ("base", xpos="far_left", ypos="head")
        gen "Sure, whatever." ("base", xpos="far_left", ypos="head")
        maf "Thank you, sir."
        maf "As for your outfit, it should be done in a timely fashion."
        gen "Sweet." ("base", xpos="far_left", ypos="head")

    elif item == ton_outfit_office:
        gen "I need a Office worker's outfit, is that something you can do?" ("base", xpos="far_left", ypos="head")
        maf "Certainly, sir. What kind of cut are you looking for?"
        gen "Cut? Am I finally getting paid for letting you set up shop here?" ("base", xpos="far_left", ypos="head")
        maf "I'm referring to how you'd like the suit to be cut."
        gen "Right..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/scribble.ogg"
        gen "Well, if you could, I'd like something like this... *Scribbles*." ("base", xpos="far_left", ypos="head")

        #TODO uncomment once conversion for python 3 allows it
        #show image Transform(Fixed("paper", "geniedrawing", fit_first=True), align=(0.5, 0.5), zoom=0.5) as drawing
        #with d5
        #call ctc
        #hide drawing
        #with d5

        maf "I see..."
        maf "Well, I suppose, with a couple of adjustments... Something like that should be doable."
        gen "Great!" ("base", xpos="far_left", ypos="head")
        maf "I'll have it ready for you as soon as possible."
    elif item  == ton_outfit_pullover:
        gen "I'm looking to get something warm and snug for a lady friend to wear during cold weather." ("base", xpos="far_left", ypos="head")
        gen "Could you make me a pullover?" ("base", xpos="far_left", ypos="head")
        maf "Of course, I can make anything you'd like."
        gen "In that case, how about condoms that doesn't diminish sexual stimuli?" ("base", xpos="far_left", ypos="head")
        maf "I'm sorry, but I believe dark arts are forbidden within these halls, so you'd have to go to Knockturn Alley for that."
        gen "Then a pullover outfit it is." ("base", xpos="far_left", ypos="head")

    #
    # Susan Bones
    #

    elif item == sus_outfit_lace1:
        gen "I'm looking to acquire some lingerie, do you have something like that in stock?" ("base", xpos="far_left", ypos="head")
        maf "Not currently... Although I have some business coming up in Knockturn alley, so I could procure some materials for it."
        gen "I see..." ("base", xpos="far_left", ypos="head")
        maf "Oh, it's nothing sinister I assure you sir, no need to worry."
        gen "So is it going to take long?" ("base", xpos="far_left", ypos="head")
        maf "Sorry?"
        gen "Will it take long to acquire these materials?" ("base", xpos="far_left", ypos="head")
        maf "Oh... No, I should have it done before you can say floo powder."
        gen "Great!" ("base", xpos="far_left", ypos="head")

    elif item == sus_outfit_latex1:
        gen "I'm in the need of some latex underwear... Female, of course." ("base", xpos="far_left", ypos="head")
        maf "Latex you say?"
        maf "Hmm... That's not something I'd normally use to make underwear out of."
        gen "Really? Why's that?" ("base", xpos="far_left", ypos="head")
        maf "It's a terribly tight and constricting material."
        gen "Just the thing I'm looking for!" ("base", xpos="far_left", ypos="head")
        maf "I see."
        maf "Very well then, I'll have your latex underwear ready for you shortly."
        gen "Tight." ("base", xpos="far_left", ypos="head")

    elif item == sus_outfit_priestess:
        gen "Would you be able to provide me with a priestess outfit?" ("base", xpos="far_left", ypos="head")
        maf "A priestess outfit, sir?"
        gen "That's right! And make it sexy!" ("base", xpos="far_left", ypos="head")
        maf "Sexy, sir?"
        maf "Surely that would hardly be appropriate for a priestess."
        gen "Why wouldn't it?" ("base", xpos="far_left", ypos="head")
        maf "As far as I'm aware, priestesses are known for practising celibacy."
        gen "Truly?" ("base", xpos="far_left", ypos="head")
        maf "I believe so, sir."
        gen "*Hmm*... That doesn't sound like any priestess I've ever met." ("base", xpos="far_left", ypos="head")
        gen "..." ("base", xpos="far_left", ypos="head")
        maf "..."
        maf "I can still make it though, if you'd like."
        gen "Great!" ("base", xpos="far_left", ypos="head")


    #
    # Universal
    #

    else:
        gen "Could you make an outfit for me?" ("base", xpos="far_left", ypos="head")
        maf "Certainly... got something specific in mind?"
        gen "Yes... I sketched something out for you..." ("base", xpos="far_left", ypos="head")
        maf "Let's have a look..."
        maf "..."
        gen "Thoughts?" ("base", xpos="far_left", ypos="head")
        maf "That should be quite doable..."
        gen "Excellent." ("base", xpos="far_left", ypos="head")
        maf "I'll get it done as soon as I can."
    return
