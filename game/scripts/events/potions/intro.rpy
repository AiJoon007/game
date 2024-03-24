
label potions_intro_E0:
    # (Optional) Genie gets caught by Snape, happens only during night time
    $ states.map.snape_office.visited = True

    if not states.map.snape_office.intro_e1:
        # First time
        $ states.map.snape_office.intro_e1 = True

        pause .5
        $ snape_office_desk_OBJ.set_image("snape_desk_work_idle")
        with d3

        sna "... Genie?" ("snape_01", ypos="head", xpos="base", trans=d3)

        gen "(Oh shit...)" ("angry", xpos="far_left", ypos="head")

        pause .5
        $ snape_office_desk_OBJ.set_image("snape_desk_idle")
        with d3

        if states.map.room_of_requirement.intro_e1:
            sna "Didn't I tell you not to leave your office?" ("snape_04")
        else:
            sna "A bit far from your office, don't you think?" ("snape_03")
            sna "Are you sure it's wise for you to wander the dungeons?" ("snape_04")

        gen "*Err*...{w=0.4} So this isn't my office?" ("base", xpos="far_left", ypos="head")
        sna "No... This is my office... As I'm sure you're aware." ("snape_01")
        gen "Oh... I must've been sleepwalking!" ("base", xpos="far_left", ypos="head")
        sna "Sleepwalking?" ("snape_05")
        sna "I didn't think genies needed sleep." ("snape_03")
        gen "Of course we do!" ("base", xpos="far_left", ypos="head")
        gen "(Wait...{w=0.4} Do we?{w} Why do I sleep so much?)" ("base", xpos="far_left", ypos="head")
        sna "*Sigh*..." ("snape_06")
        sna "Did anyone see you?" ("snape_01")
        gen "Oh yeah, lots of people." ("base", xpos="far_left", ypos="head")
        gen "A bunch of weirdos were staring at me on the way here." ("base", xpos="far_left", ypos="head")
        sna "Bloody hell..." ("snape_08")
        sna "This is why I told you not to leave your office..." ("snape_07")
        sna "Any students?" ("snape_10")
        gen "Well, there was this weird knight." ("base", xpos="far_left", ypos="head")
        sna "A knight?" ("snape_36")
        gen "Yeah! He was getting a blowjob from some lady!" ("base", xpos="far_left", ypos="head")
        sna "What are you--{w=0.2}{nw}" ("snape_25")
        sna "What are you--{fast} Oh I see..." ("snape_01")
        sna "You're talking about the paintings..." ("snape_03")
        sna "That would be Sir Cadogan and the fat lady." ("snape_24")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "That's a bit rude, don't you think?" ("base", xpos="far_left", ypos="head")
        sna "That's her name." ("snape_03")
        gen "Oh..." ("base", xpos="far_left", ypos="head")
        sna "Did you need something?" ("snape_04")
        sna "You could just call for me, you know." ("snape_05")
        gen "Oh... Yes, Well I thought that it was a bit unfair to have you walk all the way to my office every time." ("base", xpos="far_left", ypos="head")
        sna "Is that so?" ("snape_44")
        gen "Yes..." ("base", xpos="far_left", ypos="head")
        sna "And my other question..." ("snape_03")
        gen "Which was?" ("base", xpos="far_left", ypos="head")
        sna "..." ("snape_04")
        gen "Oh! *Err*..." ("base", xpos="far_left", ypos="head")

        menu:
            "\"I was just looking around.\"":
                sna "Are you done sightseeing then?" ("snape_03")
                menu:
                    "\"Not yet.\"":
                        sna "..." ("snape_01")
                        call gen_walk(xpos="mid", ypos="base")
                        call ctc
                        call gen_chibi(flip=False)
                        call ctc
                        call gen_chibi("stand_alt", flip=False)
                        call ctc
                        call gen_chibi(flip=True)
                        call gen_chibi("stand_alt")
                        pause .5
                        sna "... {w=0.4} Well?" ("snape_04")
                        call gen_chibi("stand")
                        gen "Okay, now I'm done." ("base", xpos="far_left", ypos="head")
                        sna "Good..." ("snape_04")
                    "\"Yes.\"":
                        gen "I'll just go then shall I?" ("base", xpos="far_left", ypos="head")
                        sna "That would be for the best..." ("snape_04")
            "\"I just came to visit a friend.\"":
                if states.sna.level <= 25:
                    sna "A friend? In here? Who are you--" ("snape_03")
                    sna "*Oh*...{w=0.4} I see..." ("snape_04")
                    gen "(That was cold...)" ("base", xpos="far_left", ypos="head")
                else:
                    gen "I wanted to see how he's doing." ("base", xpos="far_left", ypos="head")
                    sna "*Hmm*...{w=0.4} Well, I appreciate it, but I'm quite busy right now." ("snape_09")
                    sna "Being a teacher is not an easy job." ("snape_06")
                    gen "I know something about it." ("base", xpos="far_left", ypos="head")
                    sna "You do?" ("snape_05")
                    gen "Yeah. I might tell you about it someday, but for now, I'll leave you to it." ("base", xpos="far_left", ypos="head")
                    sna "Right... In that case..." ("snape_04")
            "\"I like your office!\"":
                gen "Way nicer than the one I have." ("base", xpos="far_left", ypos="head")
                sna "Thanks. I always had a thing for interior design--" ("snape_23")
                sna "Hold up. You're doing it again!" ("snape_17")
                gen "Doing what?" ("base", xpos="far_left", ypos="head")
                sna "Trying to talk your way out of things and changing subjects!" ("snape_32")

                if states.sna.level <= 25:
                    sna "If you don't have anything important to report I think you should leave." ("snape_31")
                    gen "... Alright. I see how it is." ("base", xpos="far_left", ypos="head")
                else:
                    sna "*Sigh*..." ("snape_06")
            "\"Can I borrow your brewing station?\"" if states.map.snape_office.intro_e2:
                gen "I thought I could use it to make some potions." ("base", xpos="far_left", ypos="head")
                sna "Hell no!" ("snape_03")
                gen "Why not?" ("base", xpos="far_left", ypos="head")
                sna "Well, I don't know, maybe so you don't explode the castle?" ("snape_01")
                gen "So... That's a maybe..." ("base", xpos="far_left", ypos="head")
                sna "It's a hard {b}NO{/b}." ("snape_31")
                gen "(... I guess I will need more convincing arguments.)" ("base", xpos="far_left", ypos="head")
                gen "(Better not mention snooping in his office though, he would definitely kill me...)" ("base", xpos="far_left", ypos="head")
            "\"What's the Wi-Fi password?\"":
                sna "Sorry?" ("snape_05")
                #check day counter
                if game.day > 35:
                    gen "I've been here for ages and I still don't know the password..." ("base", xpos="far_left", ypos="head")
                else:
                    gen "I know I've only been here for a little bit. But it's boring up there." ("base", xpos="far_left", ypos="head")

                random:
                    gen "Where am I supposed to watch \"Great British bake off\"?" ("base", xpos="far_left", ypos="head")
                    gen "I sleep so much better with \"Friends\" on in the background." ("base", xpos="far_left", ypos="head")
                    gen "I need to know what the Kardashians are up to." ("base", xpos="far_left", ypos="head")
                    gen "I was just about to start season six of \"Lost\", I need to know how it ends!" ("base", xpos="far_left", ypos="head")

                sna "I don't know what a \"Wife-I\" is, so I assume it's some muggle thing... Muggle electronics do not work at Hogwarts..." ("snape_03")
                gen "Oh shit, so you've bricked my phone?" ("base", xpos="far_left", ypos="head")
                sna "..." ("snape_04")
                gen "I don't have a phone..." ("base", xpos="far_left", ypos="head")

        sna "I need to get back to grading these papers..." ("snape_01")
        sna "Just call for me if you need me next time." ("snape_39")
        gen "Noted..." ("base", xpos="far_left", ypos="head")

    else:
        # Repeat

        sna "Genie... Didn't I tell you to call for me if you needed anything?" ("snape_03")
        gen "Ah, yes... My bad." ("base", xpos="far_left", ypos="head")

        if not states.map.snape_office.intro_e2:
            gen "(Why is he always in his office?)" ("base", xpos="far_left", ypos="head")
            gen "(Maybe I should try snooping around when he's busy teaching...)" ("base", xpos="far_left", ypos="head")
        else:
            gen "I'll be going then." ("base", xpos="far_left", ypos="head")
            sna "Don't let the door hit you on your way out." ("snape_04")
            gen "(If I want to brew potions, I need to get here during the day when Snape's busy teaching.)" ("base", xpos="far_left", ypos="head")

    jump return_office

label potions_intro_E1:
    # Plays when you first enter the office and Snape is not there
    $ states.map.snape_office.visited = True

    if states.map.snape_office.intro_e2_stage == 0:
        # Before examination
        $ states.map.snape_office.intro_e2_stage = 1

        if states.map.snape_office.intro_e1:
            gen "(Great... No Snape in sight this time.)" ("base", xpos="far_left", ypos="head")
        else:
            pause .5
            gen "...Hello?" ("base", xpos="far_left", ypos="head")
            gen "(Snape must be busy teaching...)" ("base", xpos="far_left", ypos="head")

        gen "(Let's have a look around...)" ("base", xpos="far_left", ypos="head")

        $ snape_office_brewing_station_OBJ.idle = At("snape_office_brewing_station_off", pulse_hover)
        $ snape_office_shelves_OBJ.idle = At("snape_office_shelves", pulse_hover)
        $ snape_office_picture_OBJ.idle = At("snape_office_picture", pulse_hover)
        $ snape_office_statue_OBJ.idle = At("snape_office_statue", pulse_hover)
        $ snape_office_desk_OBJ.idle = At("snape_office_desk", pulse_hover)
        $ snape_office_candelabra_OBJ.idle = At("snape_office_candelabra_on", pulse_hover)

        jump snape_office_menu

    elif (states.map.snape_office.intro_e2_stage == 1 and
        states.map.snape_office.station_examined and
        states.map.snape_office.shelves_examined and
        states.map.snape_office.picture_examined and
        states.map.snape_office.statue_examined and
        states.map.snape_office.desk_examined and
        states.map.snape_office.candelabra_examined):

        # After examination

        with fade

        gen "(Well, I've found some recipes... I doubt there's many more useful things in here...)" ("base", xpos="far_left", ypos="head")
        gen "(*Hmm*... I might be pushing my luck if I stay too long...)" ("base", xpos="far_left", ypos="head")
        gen "(Better head back to my office for now.)" ("base", xpos="far_left", ypos="head")

        call popup("You can now brew potions when Snape's not around!", "Congratulations!", "interface/icons/head/snape.webp")

        $ game.daytime = False
        $ states.map.snape_office.intro_e2 = True
        $ states.map.snape_office.intro_e2_stage = 2

        jump return_office

    jump snape_office_menu

label potions_intro_E2:
    # Genie gets caught by the painting
    $ states.map.snape_office.intro_e3 = True

    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "Looks like the coast is clear..." ("base", xpos="far_left", ypos="head")

    #Genie walks into the room
    call gen_walk(xpos="mid", ypos="base")

    "The Painting" "{i}Alarm!{/i} Alarm! {b}ALARM!{/b}"

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")

        "\"Shut it Van Gogh...\"":
            # Fun fact: This is a rare insult as Van Gogh has sold only but a single painting in his lifetime, he got famous only after his passing.
            pass
        "\"These bloody paintings...\"":
            gen "Whoever thought it was a good idea to make paintings talk should be drowned in paint..." ("angry", xpos="far_left", ypos="head")
        "\"...\"":
            pass

    "The Painting" "Alarm! Major asshole detected!"
    gen "How do I shut this thing off..." ("base", xpos="far_left", ypos="head")

    #Snape walks in
    call sna_walk(action="enter", xpos="door", ypos="base", flip=True)

    sna "Genie!"
    if states.map.snape_office.intro_e1:
        gen "Quiet you, Only my friends get to call me that!" ("base", xpos="far_left", ypos="head")
    else:
        gen "Wait, how do you know my name?" ("base", xpos="far_left", ypos="head")
        # gen "The simulation must be failing..." ("base", xpos="far_left", ypos="head")
    gen "Darn painting... If only there was some paint thinner around here..." ("base", xpos="far_left", ypos="head")
    gen "Water will have to do I suppose..." ("base", xpos="far_left", ypos="head")

    #Genie turns around towards door
    call gen_chibi(flip=False)
    pause .5
    call gen_chibi("stand_shocked", flip=False)
    play sound "sounds/malegasp.ogg" volume 0.40
    gen "..." ("angry", xpos="far_left", ypos="head")

    if states.map.snape_office.intro_e1:
        sna "I thought I told you to call for me if you needed anything." ("snape_04", ypos="head", trans=d3)
        call gen_chibi("stand", flip=False)
        gen "That's weird..." ("base", xpos="far_left", ypos="head")
        sna "..." ("snape_04")
        gen "This isn't my office!" ("angry", xpos="far_left", ypos="head")
        sna "Your office couldn't be further away from here Genie, you're not fooling me with that one again..." ("snape_03")
        gen "*Err*..." ("base", xpos="far_left", ypos="head")
    else:
        sna "What the hell are you doing in my office at this time of day?" ("snape_03")
        call gen_chibi("stand", flip=False)
        gen "*Err*..." ("base", xpos="far_left", ypos="head")
        gen "Sightseeing?" ("base", xpos="far_left", ypos="head")
        sna "In the dungeon?" ("snape_03")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        sna "I somehow find that hard to believe..." ("snape_01")

    #Snape walks past genie and sits down at his desk
    call sna_walk(xpos="mid", ypos="base")
    call sna_chibi("hide")
    $ snape_office_desk_OBJ.set_image("snape_desk_idle")
    with d3

    call gen_chibi(flip=True)
    with d3

    pause 0.5

    gen "Well I can assure you--" ("base", xpos="far_left", ypos="head")

    sna "If this is going to work then I expect you to be more careful." ("snape_01", trans=d3)
    sna "It appears you're not the only one who's been snooping around..." ("snape_35")
    gen "Spies?" ("base", xpos="far_left", ypos="head")
    sna "No... Not spies..." ("snape_43")

    random:
        block:
            sna "Someone's been rummaging around in my office." ("snape_39")
            gen "Really? Now that's--" ("base", xpos="far_left", ypos="head")
            "The Painting" "That's him!"
            sna "Be quiet you--" ("snape_43")
            "The Painting" "But, that's the asshole that snooped around here!"
            sna "..." ("snape_25")
            gen "Bugger..." ("base", xpos="far_left", ypos="head")
        block:
            sna "Someone's gone through my desk drawers." ("snape_01")
            gen "Gross!" ("base", xpos="far_left", ypos="head")
            sna "Excuse me?" ("snape_05")
            gen "I mean--{w=0.2} That's not good!" ("base", xpos="far_left", ypos="head")
            sna "Quite..." ("snape_03")
            sna "That's where I keep my list of the more...{w=0.4} Slutty Slytherins." ("snape_01")
            gen "Wait, there was a list under those panties?--" ("base", xpos="far_left", ypos="head")
            sna "" ("snape_04")
            gen "..." ("angry", xpos="far_left", ypos="head")
        block:
            sna "Someone's gone through my desk." ("snape_03")
            gen "And? Did they take anything?" ("base", xpos="far_left", ypos="head")
            sna "It's not really about what they took but what I have in there..." ("snape_31")
            gen "..." ("base", xpos="far_left", ypos="head")
            sna "It'd be a bit embarrassing if my purchase history got spread around..." ("snape_35")
            sna "Knockturn alley provides some fairly..." ("snape_41")
            sna "Unorthodox pleasure devices." ("snape_40")
            gen "Stop!" ("angry", xpos="far_left", ypos="head")
            sna "What?" ("snape_25")
            gen "I don't want to hear about your basi-lick or whatever you call it!" ("angry", xpos="far_left", ypos="head")

    sna "So it was you!" ("snape_10")
    sna "Why have you been snooping around my office?" ("snape_01")
    gen "I wasn't snooping. I just wanted to brew some potions!" ("base", xpos="far_left", ypos="head")
    sna "You wanted to brew potions?" ("snape_05")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    sna "Are you insane?" ("snape_10")
    gen "I'm quite adept at potion making, I'll have you know!" ("base", xpos="far_left", ypos="head")
    gen "It's what got me here in the first place!" ("base", xpos="far_left", ypos="head")
    sna "Right... And that effect was deliberate, was it?" ("snape_03")
    gen "..." ("base", xpos="far_left", ypos="head")
    sna "You're lucky I caught you before you did anything stupid!" ("snape_01")
    gen "Like what? It's just potions..." ("base", xpos="far_left", ypos="head")
    sna "Like caving this whole room in!" ("snape_10")
    gen "I'm immortal, why would I care..." ("base", xpos="far_left", ypos="head")
    sna "Do you phase through debris as well?" ("snape_03")
    gen "Good point..." ("base", xpos="far_left", ypos="head")

    gen "So... Will you teach me how to brew your potions, then?" ("base", xpos="far_left", ypos="head")
    sna "..." ("snape_03")
    sna "*Hah-Hah-Hah!*" ("snape_28")
    gen "*Heh-Heh*..." ("grin", xpos="far_left", ypos="head")
    sna "Hell no!" ("snape_03")
    gen "{size=+3}WHY NOT?{/size}" ("angry", xpos="far_left", ypos="head")

    if states.sna.level > 50:
        sna "Because...{w=0.4} I...{w=0.2} know...{w=0.2} You..." ("snape_10")
        gen "You do?" ("base", xpos="far_left", ypos="head")
        sna "I {i}know{/i} that you would mess it up, I should say..." ("snape_03")
    else:
        sna "Because...{w=0.4} I...{w=0.2} Don't...{w=0.2} Trust...{w=0.2} You..." ("snape_10")
        gen "You don't?" ("base", xpos="far_left", ypos="head")
        sna "I don't trust that you wont mess it up I should say..." ("snape_03")

    gen "Come on! Those recipes I found inside your desk look simple enough..." ("base", xpos="far_left", ypos="head")
    sna "You read that?" ("snape_14")
    gen "Of course I did!" ("grin", xpos="far_left", ypos="head")
    gen "They're quite genius actually..." ("base", xpos="far_left", ypos="head")
    sna "Oh... Why I wouldn't say--" ("snape_23")
    gen "A lot of them appeared to be derivatives from other potions, is that correct?" ("base", xpos="far_left", ypos="head")
    sna "*Ahem*...{w=0.4} Yes." ("snape_25")
    sna "They weren't really useful for what I wanted, so I changed them a bit..." ("snape_37")

    if states.map.room_of_requirement.intro_e1:
        gen "Much like that mirror..." ("base", xpos="far_left", ypos="head")
        sna "Actually, about that...{w=0.4} I can't seem to be able to get into that room again..." ("snape_38")

    gen "I noticed you've got some of the base liquids already." ("base", xpos="far_left", ypos="head")
    gen "I must say I am very much a fan of using breast milk in my own concoctions." ("base", xpos="far_left", ypos="head")
    sna "Hold on... You're saying you've used it in potion brewing already?" ("snape_25")
    gen "All the time!" ("base", xpos="far_left", ypos="head")
    sna "*Hmm*... Maybe you have more potential than I first thought..." ("snape_04")
    sna "These recipes are still in an experimental stage..." ("snape_03")
    sna "{size=-3}And it does mean I wouldn't have to put myself in any danger...{/size}" ("snape_09")
    sna "...{w} Fine." ("snape_01")
    sna "You can use my brewing station..." ("snape_01")
    sna "I have a spare one if you somehow manage to burn a hole through it..." ("snape_37")
    gen "Great!" ("base", xpos="far_left", ypos="head")
    sna "But only during the day... I'd rather not be bothered in the evenings as I need to--" ("snape_01")
    sna "*Ahem*...{w=0.4} Grade tests..." ("snape_35")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    menu:
        "-Ask about ingredients-":
            gen "So...{w} *Err*..." ("base", xpos="far_left", ypos="head")
            gen "The recipe's mentioned some additional ingredients..." ("base", xpos="far_left", ypos="head")
            sna "Yes?" ("snape_05")
            gen "Well, I didn't really see a cupboard with ingredients or anything in here..." ("base", xpos="far_left", ypos="head")
            sna "Right?" ("snape_03")
            gen "So, where do you keep your... *Err*..." ("base", xpos="far_left", ypos="head")
            sna "Keep {size=+5}my{/size} what?" ("snape_04")
            gen "You know what, I think I'll probably manage to find some on my own..." ("base", xpos="far_left", ypos="head")
            sna "*Hmm*..." ("snape_04")
            gen "Drinks later?" ("angry", xpos="far_left", ypos="head")
            gen "On me, obviously." ("base", xpos="far_left", ypos="head")
            sna "..." ("snape_04")
            gen "*Hah-hah*... See you later then, buddy!" ("grin", xpos="far_left", ypos="head")
            gen "*Ahem*..." ("base", xpos="far_left", ypos="head")
            call gen_chibi("stand", flip=False)
        "-Indirectly ask about ingredients-":
            gen "I'll just go now then shall I?" ("base", xpos="far_left", ypos="head")
            sna "You do that..." ("snape_01")
            call gen_walk(xpos="station", ypos="station", flip=False)
            pause .5
            call gen_chibi("stand_alt", flip=True)
            gen "Unless there's anything else that I'll need to brew these potions?" ("base", xpos="far_left", ypos="head")
            sna "Well, obviously you wouldn't be able to brew them with just the base liquids..." ("snape_05")
            gen "*Hah-Hah*... Yeah..." ("base", xpos="far_left", ypos="head")
            sna "..." ("snape_04")
            gen "See you later then!" ("base", xpos="far_left", ypos="head")
            call gen_chibi("stand", flip=False)

    gen "(I guess I'll just have to find any additional ingredients that I'll need on my own...)" ("base", xpos="far_left", ypos="head")
    call gen_walk(action="leave")

    sna "..."

    $ snape_office_desk_OBJ.set_image("snape_office_desk")

    call sna_chibi("stand", xpos="beside_chair", ypos="beside_chair", flip=True)

    call sna_walk(path=[(745, 438), (730, 405)])

    call sna_chibi("stand", xpos="shelves", ypos="shelves", flip=False)
    with d3

    pause 0.5

    sna "As If I'd let anyone have my ingredients..." ("snape_03", trans=d3)
    sna "Revelio!" ("snape_10", wand=True)

    hide snape_main
    hide screen bld1
    with d3

    pause 0.5
    play sound "sounds/magic1.ogg"
    $ snape_office_shelves_OBJ.set_image("snape_office_shelves_alt")
    $ snape_office_shelves_OBJ.foreground = None
    with d9
    pause 2.0

    sna "*Heh-Heh*..." ("snape_37", wand=True, trans=d1)
    sna "... W-- Where's my fluxweed?!" ("snape_25", wand=True, trans=d1)

    #Back to office screen

    $ snape_office_shelves_OBJ.set_image("snape_office_shelves")
    $ snape_office_shelves_OBJ.foreground = "snape_office_shelves_anim"
    jump return_office
