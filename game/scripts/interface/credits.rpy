init python:
    def credits_title(title):
        return "{k=5.0}{size=+15}{outlinecolor=#842500}{color=#f9a001}{{" + title + "}{/color}{/outlinecolor}{/size}{/k}\n"

    def credits_group(*lines):
        return "".join(map(lambda x: "{k=1.5}"+x+"{/k}\n", lines))

define credits_text = "\n".join([
    "{image=credits_title}\n{vspace=200}",
    credits_title("Artwork"),
    credits_group("Soggy", "DostojevskijSTG", "LoafyLemon", "Noodle", "perniciousducks", "KitsuneArts", "BopJp"),
    credits_title("Writing"),
    credits_group("Johnny", "MadMerlin", "Livvypoo", "Mo"),
    credits_title("Programming"),
    credits_group("Asease1", "LoafyLemon", "TropeCode"),
    credits_title("Music"),
    credits_group(
        "Kevin MacLeod\n{size=-5}{color=#808080}{k=0.7}\"Anguish\"\n\"Awkward Meeting\"\n\"Deadly Roulette\"\n\"Brittle Rille\"\n\"Firebrand\"\n\"Chipper Doodle v2\"\n\"Dark Fog\"\n\"Despair\"\n\"Game Over Theme\"\n\"Boss Theme\"\n\"Hitman\"\n\"Music for Manatees\"\n\"Plaint\"\n\"Fuzzball Parade\"\n\"Teddy Bear Waltz\"\n\"Scheming Weasel (Slower version)\"\n\"Open Those Bright Eyes\"\n\"Wallpaper\"\n\"Hidden Agenda\"\n\"Aquarium\"\n\"Court of the Queen\"\n\"Machinations\"\n\"Brandenburg Concerto No. 4 in G, Movement I (Allegro), BWV 1049\"\n\"March of the spoons\"\n\"The other side of the door\"{/k}{/color}{/size}\n",
        "PhobyAk\n{size=-5}{color=#808080}{k=0.7}\"Under-the-radar\"{/k}{/color}{/size}\n",
        "Shadow16nh\n{size=-5}{color=#808080}{k=0.7}\"Playful Tension (Orchestral)\"{/k}{/color}{/size}\n",
        "controllerhead\n{size=-5}{color=#808080}{k=0.7}\"Item Shop\"{/k}{/color}{/size}\n",
        "jrayteam6\n{size=-5}{color=#808080}{k=0.7}\"Grape Soda is Fucking Raw\"{/k}{/color}{/size}\n",
        "Juhani Junkala\n{size=-5}{color=#808080}{k=0.7}Retro Game Music Pack:\n\"Title Screen\"\n\"Level 1\"\n\"Level 3\"{/k}{/color}{/size}\n",
        "Snabisch\n{size=-5}{color=#808080}{k=0.7}\"Only 115 (Dance Loop)\"{/k}{/color}{/size}\n",
        "Nene\n{size=-5}{color=#808080}{k=0.7}\"Boss Battle #2\"{/k}{/color}{/size}\n",
        "Tim Kulig\n{size=-5}{color=#808080}{k=0.7}\"Anticipations\"{/k}{/color}{/size}\n",
        "BoxCat Games\n{size=-5}{color=#808080}{k=0.7}\"Battle (Boss)\"{/k}{/color}{/size}\n"
    ),
    credits_title("Special Thanks"),
    credits_group(
        "{size=+4}Akabur{/size}",
        "{color=#808080}{size=-5}{k=0.7}Creator of the original Witch Trainer and other awesome games! {a=https://www.patreon.com/akabur}PATREON{/a}{/size}{/color}{/k}\n",
        "Dr. Lupin", "Lineup", "MaiL", "MedicBear", "STG Anon", "Booom313", "Sandmaster", "Pinguino", "UE Crew", "Catbug", "CaptainNemo", "Artguy", "Linear", "Amadan", "Anons", "Heretic", "Maverick", "Cleanzo", "Techy", "Zuel32", "Darwin7", "Ven", "NotTera", "Armise", "Cosmic"
    ),
"""{vspace=100}
\n\n
Special thanks\n
to the fans, discord moderators\n
and {a=https://www.patreon.com/SilverStudioGames/}patreon supporters{/a} {image=images/misc/heart.webp}
\n\n
{image=credits_logo}\n
{vspace=100}
\n\n
Thank you for playing!
\n\n
{image=credits_genie}"""
])

define credits_width = 700

define credits_duration = 45

define credits_chibis = (
    (Transform("ch_sna wand_defend", xzoom=-1), 1, 12, True),
    ("ch_sna jerk_off", 15, 8, False),
    ("ch_hem run", 17, 6, True),
    (Transform("hj", zoom=2, crop=(225,200,200,235)), 25, 8, True),
)

label credits:
    if not _menu:
        play music "music/Only 115 (Electro Loop)_125 BPM.ogg" fadein 1 fadeout 1 if_changed

    $ renpy.scene("screens")

    show screen credits(credits_text)
    with dissolve
    $ achievements.unlock("Credits")
    pause credits_duration
    if not _menu:
        stop music fadeout 3
    call ctc
    hide screen credits
    with dissolve

    if _menu:
        # play music config.main_menu_music fadein 1 fadeout 3 if_changed
        jump main_menu_screen
    else:
        return

# Workaround for centered images, because text_align doesn't work

image credits_title:
    size (credits_width, 200)
    contains:
        "images/logo/title.webp"
        fit "contain"
        xalign 0.5

image credits_logo:
    size (credits_width, 50)
    contains:
        "images/logo/silverstudiogames.webp"
        fit "contain"
        xalign 0.5

image credits_genie:
    size (credits_width, 300)
    contains:
        "characters/genie/mage9.webp"
        fit "contain"
        xalign 0.5

transform credits_chibi_fade(start, duration):
    alpha 0
    pause start
    linear 0.5 alpha 1.0
    pause duration
    linear 0.5 alpha 0.0

transform credits_scroll(duration):
    subpixel True

    xalign 0.5
    yanchor 0.0
    ypos (config.screen_height / 2 - 125)
    pause 1
    parallel:
        linear (duration - 1) yanchor 1.0
    parallel:
        linear (duration - 1) ypos (config.screen_height + 50)

screen credits(credits=credits_text, duration=credits_duration, chibis=credits_chibis):
    tag credits
    zorder 20

    add Solid("#000")

    for img, t, d, left in chibis:
        add img:
            at credits_chibi_fade(t, d)
            zoom 0.5
            if left:
                pos (20, config.screen_height - 20)
                align (0.0, 1.0)
            else:
                pos (config.screen_width - 20, config.screen_height - 20)
                align (1.0, 1.0)

    text credits:
        at credits_scroll(duration)
        xsize credits_width
        text_align 0.5
        color "#fff"
        outlines [(2, "#000", 0, 0)]
