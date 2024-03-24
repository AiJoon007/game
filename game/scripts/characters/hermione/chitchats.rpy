
label hermione_chitchat:

    if states.her.chatted:
        return

    $ states.her.chatted = True

    ### Tier 1 ###
    if states.her.level >= 0 and states.her.level <= 3:
        random:
            block:
                her "Maybe, if I work harder, I could squeeze a few more classes into my schedule..." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "Actually, I don't mind being called a \"know-it-all\"." ("open", "closed", "angry", "mid")
                her "I think it's rather flattering..." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "The basilisk, also known as the king of serpents." ("open", "closed", "angry", "mid")
                her "{i}Herpo the Foul{/i} was the first to breed a Basilisk." ("open", "closed", "angry", "mid")
                her "He accomplished that by--" ("open", "closed", "angry", "mid")
                her "Oh, I'm sorry, [name_genie_hermione]... We have another test tomorrow." ("open", "base", "worried", "R")
                her "I just want to make sure that I'm ready..." ("open", "base", "worried", "R")
                her "" ("base", "base", "base", "mid")

            block:
                her "If my body wouldn't require sleep..." ("open", "base", "worried", "R")
                her "I would be able to spend twice as much time with studying!" ("angry", "wide", "base", "stare")
                her "I wonder if there's a spell for that..." ("open", "base", "base", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "So far, Professor Trelawney did not teach me a single piece of any actual knowledge, [name_genie_hermione]." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "If only more students were honest, responsible, and diligent like me." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "How can some people be so ignorant about the problems in the world?" ("open", "closed", "angry", "mid")
                her "I believe that we all need to work harder to make the world a better place." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "It's been raining quite a lot lately..." ("open", "base", "worried", "R")
                her "" ("base", "base", "base", "mid")

            block:
                her "Very few people know this..." ("open", "base", "worried", "R")
                her "... But I really like chocolate." ("base", "base", "base", "mid")
                her "" ("base", "base", "base", "mid")

            block:
                her "I am sorry [name_genie_hermione], but I don't really have time for idle chit-chats..." ("base", "base", "base", "mid")
                her "" ("normal", "base", "base", "mid")

    ### Tier 2 Low ###
    if states.her.level >= 4 and states.her.level <= 6:
        random:
            block:
                her "I read somewhere that a full moon often makes it easier to concentrate at a task at hand..." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "I love nothing more than to curl up by a fireplace during a rainstorm with a good book..." ("base", "base", "base", "mid")
                her "" ("base", "base", "base", "mid")

            block:
                her "A peculiar rumour concerning professor Snape has been circulating in the school lately..." ("open", "base", "worried", "R")
                her "No, I probably shouldn't..." ("soft", "base", "base", "mid")
                her "" ("normal", "base", "base", "mid")

            block if states.her.status.show_bra or states.her.status.show_panties:
                her "Despite the questionable nature of the favours you have been buying from me lately, [name_genie_hermione]..." ("open", "closed", "angry", "mid")
                her "I am grateful to you for your help..." ("open", "closed", "angry", "mid")
                her "Gryffindor needs those points now more than ever..." ("annoyed", "squint", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "Quidditch being so popular is simply beyond me..." ("open", "closed", "angry", "mid")
                her "I mean, the game doesn't make any sense..." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "The \"Men's Rights Movement\" is steadily gaining popularity." ("open", "closed", "angry", "mid")
                her "It's very fulfilling to know that I am helping to improve our society." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "The Hogwarts school library is considered to be quite extensive..." ("open", "closed", "angry", "mid")
                her "Still... I'd like it to be bigger." ("open", "squint", "base", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "As one of the top students in this school, I have a reputation to keep..." ("open", "base", "worried", "R")
                her "People look up to me..." ("open", "base", "worried", "R")
                her "... So, your discretion is very appreciated, [name_genie_hermione]." ("open", "base", "base", "mid")
                her "" ("annoyed", "base", "worried", "R")

            block if states.her.status.show_bra or states.her.status.show_panties:
                her "That favour I sold you the other day, [name_genie_hermione]..." ("open", "base", "worried", "mid")
                her "......." ("normal", "happyCl", "worried", "mid")
                her "I only agreed to it because the needs of my house always come first." ("open", "narrow", "worried", "down")
                her "I just wanted you to know that, [name_genie_hermione]..." ("upset", "closed", "base", "mid")

            block:
                her "My favourite subject?" ("open", "base", "base", "mid")
                her "*Hmm*..." ("soft", "base", "base", "R")
                her "I suppose that would be \"charms\"..." ("open", "base", "base", "mid")
                her "Or \"transfiguration\" perhaps..." ("open", "base", "base", "mid")
                her "Although I do enjoy \"arithmancy\"..." ("open", "base", "base", "mid")
                her "" ("soft", "base", "base", "mid")

            block if not hermione.is_worn("top", "bottom"):
                her "Yes, standing in-front of your headmaster without a top or bottoms is completely normal..." ("open", "closed", "base", "mid")
                her "I suppose you are helping me..." ("open", "base", "base", "mid")

    ### Tier 2 High ###
    if states.her.level >= 7 and states.her.level <= 9:
        random:
            her "I dislike the entire house of Slytherin with all my heart, [name_genie_hermione]." ("angry", "base", "angry", "mid")

            block if states.her.status.show_panties:
                her "Do you remember when you asked me to show you my panties for the first time, [name_genie_hermione]?" ("open", "closed", "angry", "mid")
                her "I was so furious with you then..." ("open", "closed", "angry", "mid")
                her "Now I see that I was just being selfish..." ("annoyed", "squint", "angry", "mid")
                her "After all, the honour of my house is at stake here..." ("annoyed", "squint", "angry", "mid")
                her "And that shall be my one and only concern!" ("normal", "squint", "angry", "mid")

            block:
                her "The rate at which the Slytherin house has been gaining points lately is simply ridiculous." ("open", "closed", "angry", "mid")
                her "I think professor Snape might be behind it." ("angry", "base", "angry", "mid")
                her "You should look into this, [name_genie_hermione]." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "Ashwinder eggs, rose thorns, moonstone..." ("open", "base", "worried", "R")
                her "*Huh*? Am I thinking out loud again?" ("open", "base", "worried", "mid")
                her "I apologise..." ("grin", "happyCl", "worried", "mid",emote="sweat")
                her "It's just that we have another test soon..." ("soft", "base", "base", "R")

            block:
                her "Hogwarts has really become a second home to me lately..." ("open", "closed", "base", "mid")
                her "I don't even miss my parents nearly as much anymore..." ("annoyed", "narrow", "worried", "down")
                her "Come to think of it, I don't miss them at all..." ("angry", "wide", "base", "stare")
                her "I'm an awful daughter..." ("angry", "narrow", "base", "down")

            block:
                her "*Yawn*! I read about this technique that supposedly allows you to cut your sleep time in half..." ("annoyed", "narrow", "annoyed", "up")
                her "I don't think it's working though... *Yawn*!" ("annoyed", "narrow", "worried", "down")

            block:
                her "Even after I graduate from Hogwarts, I plan to keep on working hard." ("open", "closed", "angry", "mid")
                her "If I give it my all, I can make this world a better place, I know it!" ("open", "base", "base", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "Somehow I have the feeling that this year will become a pivotal turning point in my life..." ("open", "base", "worried", "mid")
                her "" ("soft", "base", "base", "R")

            block:
                her "Some of the less travelled school corridors are not very well lit, and rather dusty..." ("open", "closed", "angry", "mid")
                her "Please take care of this, [name_genie_hermione]..." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "I've read about this thing called a \"Time-Turner\"." ("open", "base", "base", "mid")
                her "It allows the user to control the flow of time..." ("open", "base", "base", "mid")
                her "Having a device like that would do wonders for my schedule..." ("open", "closed", "base", "mid")
                her "" ("annoyed", "squint", "base", "mid")

            block if not hermione.is_worn("top", "bottom"):
                her "Is it just me, or is it a bit chilly in here?" ("open", "closed", "base", "mid")
                her "It must be due to my current state of undress..." ("open", "base", "base", "mid")

    ### Tier 3 ###
    if states.her.level >= 10 and states.her.level <= 12:
        random:
            block:
                her "My \"men's rights movement\" has been losing its popularity lately..." ("open", "base", "worried", "mid")
                her "It's as if people don't even care!" ("annoyed", "narrow", "angry", "R")

            block:
                her "Thank you for buying all those favours from me, [name_genie_hermione]." ("open", "closed", "angry", "mid")
                her "Some of them were borderline inappropriate, sure..." ("normal", "squint", "angry", "mid")
                her "But I don't mind sacrificing my dignity, if it will allow Gryffindor to compete with Slytherin." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "If you can find someone who knows all the rules of Quidditch, let me know." ("angry", "base", "angry", "mid")
                her "Although, I highly doubt that person exists..." ("annoyed", "squint", "base", "mid")

            block:
                her "[name_genie_hermione], there is something about professor Snape that I think you should know..." ("open", "base", "base", "mid")
                her "................." ("open", "base", "worried", "R")
                her "........................." ("annoyed", "squint", "angry", "mid")
                her "*Ehm*... Never mind..." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "Some of the Slytherin girls sell sexual favours almost openly these days..." ("open", "closed", "angry", "mid")
                her "You need to put an end to such practices, [name_genie_hermione]." ("open", "base", "base", "mid")
                her "(I can barely keep up...)" ("annoyed", "narrow", "angry", "R")

            block:
                her "Life works in mysterious ways..." ("open", "base", "worried", "R")
                her "Wouldn't you agree, [name_genie_hermione]?" ("open", "squint", "base", "mid")
                her "" ("soft", "base", "base", "R")

            block:
                her "Slytherins..." ("angry", "base", "angry", "mid",emote="angry")
                her "" ("angry", "base", "angry", "mid")

            block:
                her "I've been spending so much time in your office lately, [name_genie_hermione]..." ("open", "base", "worried", "R")
                her "If I'm not careful, some people may think that I have become your pet..." ("open", "base", "worried", "mid")
                her "I mean--{w=0.2} The teacher's pet!" ("angry", "happyCl", "worried", "mid",emote="sweat")
                her "" ("normal", "happyCl", "worried", "mid")

            block:
                her "My favourite colours?" ("open", "base", "base", "mid")
                her "Scarlet and gold of course!" ("open", "base", "base", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "Is it weird that my best friends are boys?" ("open", "base", "worried", "R")
                her "" ("base", "base", "base", "mid")

            block if not hermione.is_worn("top", "bottom"):
                her "This is as much as I'm willing to take off... Unless you pay me, of course..." ("open", "closed", "base", "mid")
                her "Thirty-five points, please..." ("open", "base", "base", "mid")

            block if states.her.status.stripping:
                her "Just because I've taken my clothes off, that doesn't mean I'll agree to standing around naked all willy-nilly." ("open", "closed", "base", "mid")
                her "No, you'll still have to pay me for that." ("open", "base", "base", "mid")

    ### Tier 4 Low ###
    if states.her.level >= 13 and states.her.level <= 15:
        random:
            her "What will it be today, [name_genie_hermione]?" ("annoyed", "narrow", "annoyed", "mid")

            block:
                her "[name_genie_hermione], with all due respect..." ("normal", "squint", "angry", "mid")
                her "Professor Snape's debauchery is getting out of hand!" ("normal", "squint", "angry", "mid")
                her "You must do something, [name_genie_hermione]." ("open", "base", "worried", "mid")
                her "" ("normal", "base", "base", "mid")

            #block:
                #her "I am willing to go to great lengths to insure the superiority of my house..." ("open", "closed", "angry", "mid")
                #her "But that does not mean that I take pleasure in selling myself out to you in exchange for house points, [name_genie_hermione]." ("open", "closed", "angry", "mid")
                #her "{size=-4}(Like some sort of prostitute-witch...){/size}" ("angry", "narrow", "base", "down")

            block:
                her "Lately I have not been studying nearly as much as I used to..." ("open", "base", "worried", "mid")
                her "Am I losing my motivation?" ("open", "base", "worried", "R")
                her "" ("soft", "base", "base", "R")

            block:
                her "My least favourite subject?" ("open", "squint", "base", "mid")
                her "Divination." ("annoyed", "squint", "angry", "mid")

            block:
                her "My father used to say that \"magic is just science we don't understand yet\"." ("open", "base", "base", "mid")
                her "He couldn't be more wrong, of course..." ("open", "base", "worried", "R")
                her "" ("soft", "base", "base", "R")

            block:
                her "Despite everything..." ("open", "closed", "angry", "mid")
                her "I am thankful that you keep on buying favours from me, [name_genie_hermione]..." ("open", "base", "worried", "R")
                her "" ("soft", "base", "base", "R")

            block if game.weather in {"snow", "blizzard"}:
                her "It's quite cold outside today, isn't it?" ("open", "base", "base", "mid")
                her "" ("soft", "base", "base", "mid")

            #block:
                #her "The \"Autumn Ball\" will be soon..." ("open", "base", "base", "mid")
                #her "" ("soft", "base", "base", "mid")

            block:
                her "People hardly show up for my \"men's rights movement\" meetings anymore..." ("open", "base", "worried", "R")
                her "" ("soft", "base", "base", "R")

            block if states.her.ev.dance_for_me.snape_invited:
                her "Do you believe we have learned enough, or will you be inviting Professor Snape again in the future?" ("annoyed", "base", "base", "R")


    ### Tier 4 High ###
    if states.her.level >= 16 and states.her.level <= 18:
        random:
            block if hermione.is_any_worn("top", "bra"):
                her "Would you like me to show you my breasts today, [name_genie_hermione]?" ("open", "narrow", "worried", "down")
                her "Yes... I would willingly expose myself to you, professor..." ("base", "narrow", "base", "up")
                her "That's how selfless I am!" ("annoyed", "narrow", "annoyed", "mid")

            block if states.her.status.cumshot:
                her "I can't help but feel bad for the house elves who do my laundry..." ("open", "base", "base", "mid")
                her "I mean, all those dreadful semen stains..." ("open", "narrow", "worried", "down")
                her "" ("angry", "narrow", "base", "down")

            block:
                her "It doesn't matter how many times you ask me this, [name_genie_hermione]..." ("open", "base", "base", "mid")
                her "The answer shall remain the same..." ("open", "base", "base", "mid")
                her "I have nothing but resentment for the Slytherins!" ("angry", "base", "angry", "mid")
                her "" ("annoyed", "narrow", "angry", "R")

            block:
                her "I've been thinking about all the favours I've sold you over these last months, [name_genie_hermione]..." ("open", "base", "base", "mid")
                her "Even though I do feel a little bit embarrassed..." ("open", "narrow", "worried", "down")
                her "I also feel very proud of myself." ("upset", "closed", "base", "mid")

            block:
                her "I still dedicate a lot of my time to studying..." ("open", "base", "base", "mid")
                her "But not nearly as much of it as I used to..." ("open", "base", "base", "mid")
                her "" ("soft", "base", "base", "R")

            block:
                her "Gryffindor shall get the house cup this year!" ("open", "closed", "angry", "mid")
                her "{size=-4}(Even if it should cost me my dignity...){/size}" ("angry", "narrow", "base", "down")
                her "" ("upset", "closed", "base", "mid")

            block:
                her "I don't mind autumn, spring, or summer..." ("open", "base", "base", "mid")
                her "But my favourite season is winter." ("open", "closed", "base", "mid")
                her "" ("soft", "base", "base", "mid")

            block:
                her "I used to look down on girls who spend too much of their time, worrying about the way they look..." ("open", "base", "base", "mid")
                her "But I was wrong to do so..." ("open", "base", "base", "mid")
                her "I am starting to understand how important it really is for a girl to look pretty." ("open", "base", "base", "mid")
                her "..............." ("annoyed", "base", "worried", "R")
                her "I've been on a diet lately..." ("angry", "wink", "base", "mid")
                her "" ("angry", "happyCl", "worried", "mid",emote="sweat")
                her "" ("normal", "happyCl", "worried", "mid")

            block:
                her "I've been feeling rather confident around the boys lately..." ("open", "base", "base", "mid")
                her "I believe I have you to thank for that, [name_genie_hermione]." ("base", "base", "base", "mid")

            block if not hermione.is_any_worn("clothes"):
                her "Will I get any extra points for being naked inside your office, [name_genie_hermione]?" ("open", "base", "base", "mid")
                her "An additional ten points added to my next favour is enough." ("open", "closed", "base", "mid")
                her "" ("base", "narrow", "base", "mid_soft")

            block if states.her.ev.dance_for_me.snape_invited:
                her "Do you believe we have learned enough, or will you be inviting Professor Snape again in the future?" ("annoyed", "base", "base", "R")

    ### Tier 5 ###
    if states.her.level >= 19 and states.her.level <= 21:
        random:
            her "I am doing well... Thank you for asking." ("base", "base", "base", "mid")

            block:
                her "Just let me know what will be required of me today, [name_genie_hermione]." ("open", "closed", "angry", "mid")
                her "" ("normal", "base", "base", "mid")

            block:
                her "I don't study nearly as much as I used to..." ("open", "base", "worried", "mid")
                her "Despite that, my popularity among the other students seems to be growing..." ("open", "base", "worried", "mid")
                her "*Hmm*..." ("soft", "base", "base", "R")

            block:
                her "I wouldn't say \"no\" to a bottle of butterbeer right about now..." ("smile", "narrow", "base", "mid_soft")
                her "" ("grin", "base", "base", "R")

            block:
                her "What is it, [name_genie_hermione]? Do you have a present for me?" ("base", "base", "base", "mid")
                her "Oh... I see..." ("annoyed", "narrow", "angry", "R")

            block:
                her "Do I look fat to you, [name_genie_hermione]?" ("open", "base", "worried", "mid")
                her "(I hope the diet is working...)" ("annoyed", "base", "worried", "R")

            block:
                her "I remember that I used to say that books were my friends..." ("open", "closed", "base", "mid")
                her "When I think back on that now, it sounds so lame." ("grin", "happyCl", "worried", "mid",emote="sweat")
                her "" ("soft", "base", "base", "mid")

            block:
                her "Add Ashwinder's egg to the cauldron..." ("open", "closed", "angry", "mid")
                her "Then add horseshoe reddish and heat it up..." ("open", "closed", "angry", "mid")
                her "Then juice a squill bulb..." ("open", "closed", "angry", "mid")
                her "Or was it a dash of thyme first?" ("open", "base", "worried", "R")
                her ".............." ("soft", "base", "base", "R")
                her "Oh, who cares?" ("grin", "happyCl", "worried", "mid",emote="sweat")
                her "" ("base", "base", "base", "mid")

            block:
                her "Do you think I am wearing enough make-up, [name_genie_hermione]?" ("open", "base", "base", "mid")
                her "Wearing too much would look vulgar..." ("open", "base", "base", "mid")
                her "But wearing too little would make me look plain..." ("soft", "base", "base", "R")
                her "I don't want to look plain!" ("annoyed", "narrow", "angry", "R")

            block if hermione.is_any_worn("top", "bra"):
                her "Would you like to see my tits today, [name_genie_hermione]?" ("open", "closed", "base", "mid")
                her "Or would you rather I do something else?" ("open", "base", "angry", "mid")
                her "" ("soft", "base", "base", "mid")

            block if not hermione.is_any_worn("clothes"):
                her "You know, I don't really mind being naked in your office anymore..." ("open", "closed", "base", "mid")
                her "I would almost say I'm used to it." ("open", "closed", "base", "mid")
                her "" ("base", "narrow", "base", "mid_soft")

    ### Tier 6 Low ###
    if states.her.level == 22:
        random:
            block if not states.her.ev.yule_ball.complete:
                her "I wonder what everyone are going to wear for the ball..." ("base", "base", "base", "mid")

            block:
                her @ cheeks blush "Do you have any adult magazines you don't need, [name_genie_hermione]?" ("open", "base", "base", "R")
                her @ cheeks blush "" ("base", "base", "base", "R")

            block:
                her "If you need anything, [name_genie_hermione... Just ask, okay?" ("open", "base", "base", "mid")
                her "" ("base", "base", "base", "mid")

            #block:
                #her "It's been getting so cold lately..." ("open", "base", "base", "mid")
                #her "I hope it's going to start snowing soon..." ("base", "base", "base", "mid")

            block if not states.cho.tier >= 4:
                her "Jump and scream for the Gryffindor team!" ("open", "closed", "base", "mid")
                her "So daring and bold, sporting red and gold!" ("smile", "happyCl", "base", "mid",emote="happy")
                her "" ("base", "base", "base", "mid")

            block if not states.her.ev.yule_ball.complete:
                her "I hope the ball goes smoothly..." ("open", "base", "worried", "R")
                her "" ("soft", "base", "base", "R")

            block:
                her "Considering the nature of the favours you keep buying from me, [name_genie_hermione].." ("open", "closed", "base", "mid")
                her "I've had to shower a lot more frequently than I used to..." ("open", "base", "worried", "mid")

            block:
                her "[name_genie_hermione], could you put your penis in my mouth?" ("angry", "base", "base", "mid")
                her "[name_genie_hermione], I am begging you..." ("open_wide_tongue", "narrow", "annoyed", "up")
                her "Fifty-five points, please!" ("smile", "base", "angry", "mid")
                her "" ("angry", "wink", "base", "mid")

            block:
                her "I have read this one article about the positive effects of semen on a woman's skin..." ("open", "closed", "base", "mid")
                her "I wonder where their information is coming from..." ("base", "narrow", "base", "mid_soft")
                her "Did the magazine conduct research of some sort?" ("angry", "wink", "base", "mid")
                her "" ("base", "narrow", "base", "mid_soft")

            block:
                her "It goes like this..." ("open", "closed", "base", "mid")
                her "First Gryffindor, then Ravenclaw, then Hufflepuff..." ("open", "closed", "base", "mid")
                her @ cheeks blush "Slytherin is not even on the list!" ("open", "narrow", "annoyed", "mid")
                her "" ("upset", "closed", "base", "mid")

    ### Tier 6 High ###
    if states.her.level >= 23:
        random:
            block:
                her @ cheeks blush "If you ever need some \"assistance\", [name_genie_hermione]... Please let me know." ("open_wide_tongue", "base", "base", "R")
                her @ cheeks blush "" ("base", "base", "base", "R")

            block if states.her.status.public_sex:
                her "I am sorry to bother you with this, [name_genie_hermione]..." ("open", "base", "base", "mid")
                her "But do you have any condoms?" ("open", "base", "base", "mid")
                her "Sadly, the ones I've bought are already gone..." ("annoyed", "happyCl", "worried", "mid",emote="sweat")
                her "" ("base", "base", "base", "R")

            block if game.weather in {"rain", "storm", "overcast"}:
                her "It certainly is chilly outside..." ("open", "base", "base", "mid")
                her "I hope it's going to start snowing soon..." ("base", "base", "base", "mid")
                her "You will let me wear a coat at least, right?" ("angry", "happyCl", "worried", "mid",emote="sweat")
                her "" ("base", "narrow", "base", "mid_soft")

            block if not states.cho.tier >= 4:
                her "Jump and scream for the Gryffindor team!" ("open", "closed", "base", "mid")
                her "So daring and bold, sporting red and gold!" ("smile", "happyCl", "base", "mid",emote="happy")
                her "" ("base", "base", "base", "mid")

            block:
                her "[name_genie_hermione], I have a favour to ask..." ("base", "base", "worried", "mid")
                her "Could you help me with one of my dresses later, [name_genie_hermione]?" ("base", "base", "base", "R")
                her @ cheeks blush "I could use some of your... insight." ("soft", "narrow", "base", "mid_soft")
                her "" ("base", "narrow", "base", "mid_soft")

            block:
                her "I can't believe I was such a prude before." ("angry", "base", "worried", "mid")
                her "Meeting you was the best thing that ever happened to me, [name_genie_hermione]." ("smile", "narrow", "base", "mid_soft")
                her "" ("base", "narrow", "base", "mid_soft")

            block:
                her "Considering the nature of the favours you keep buying from me, [name_genie_hermione]..." ("open", "closed", "base", "mid")
                her "I've had to shower way more than I used to..." ("open", "base", "worried", "mid")
                her "(Although, I kind of enjoy the smell...)" ("soft", "narrow", "annoyed", "up")

            block:
                her "[name_genie_hermione], could you put your penis in my mouth?" ("angry", "base", "base", "mid")
                her "[name_genie_hermione], I am begging you..." ("open_wide_tongue", "narrow", "annoyed", "up")
                her "Fifty-five points, please!" ("smile", "base", "angry", "mid")
                her "(Although I wouldn't mind doing it for free...)" ("smile", "narrow", "annoyed", "up")

            block:
                her "There was this one article... I'm not sure if I told you." ("open", "closed", "base", "mid")
                her "It was about the positive effects of semen on a woman's skin." ("open", "closed", "base", "mid")
                her "And it actually works!" ("smile", "narrow", "base", "mid_soft")
                her "My skin definitely is getting softer." ("smile", "closed", "base", "mid")
                her "" ("base", "narrow", "base", "mid_soft")

            block:
                her "It goes like this..." ("open", "closed", "base", "mid")
                her "First Gryffindor, then Ravenclaw, then Hufflepuff..." ("open", "closed", "base", "mid")
                her @ cheeks blush "And Slytherin is not even on the list!" ("open", "narrow", "annoyed", "mid")
                her "" ("upset", "closed", "base", "mid")

            block if not hermione.is_any_worn("clothes"):
                her "You know, being naked isn't that bad..." ("open", "closed", "base", "mid")
                her "Putting on clothes is just a waste of time, anyway..." ("open", "closed", "base", "mid")
                her "" ("base", "narrow", "base", "mid_soft")

            block if states.her.status.creampie:
                her @ cheeks blush "I know what you said before, [name_genie_hermione]... But, are you certain that there is no way for you to get me pregnant?" ("open", "base", "base", "mid")
                her @ cheeks blush "Or is there still a chance it may happen?" ("soft", "base", "base", "R")

            block if states.her.status.anal:
                her "[name_genie_hermione]... If you're planning on doing \"that\" again... Please use plenty of lube..." ("open", "base", "base", "mid")

            block if states.her.ev.yule_ball.complete:
                her "Thank you again for providing me with a dress for the ball." ("open", "base", "base", "mid")
                her "I had a wonderful time..." ("base", "base", "base", "mid")

            block if states.her.ev.potions.breast_expand_drank:
                her "You don't happen to have any more of that breast expansion potion, [name_genie_hermione]?" ("open", "base", "base", "mid")
                her "I've noticed some correlations between your grades and your chest size, so I thought I'd give it a shot during our next exam..." ("open", "base", "base", "mid")

    return
