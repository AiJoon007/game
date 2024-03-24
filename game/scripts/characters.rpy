
init -999 python:
    # Remove style overrides
    adv.who_args.pop("style", None)
    adv.what_args.pop("style", None)
    adv.window_args.pop("style", None)

    # Default icon
    adv.show_args["icon"] = "narrator"

    def narrator_fade(ev, interact=True, **kwargs):
        if ev == "begin":
            behind = [f"{i}_main" for i in states.dolls] + ["snape_main", "genie_main", "cg"]
            renpy.show("fade", zorder=15, behind=behind)
        elif ev == "end":
            renpy.hide("fade")

# Characters
define m = Character(None, show_side_image=Image("characters/genie/mage.webp", xpos=20), show_icon="genie")
define g2 = Character(None, show_side_image=Image("characters/genie/mage2.webp", xpos=20), show_icon="genie")
define g3 = Character(None, show_side_image=Image("characters/genie/mage3.webp", xpos=20), show_icon="genie")
define g4 = Character(None, show_side_image=Image("characters/genie/mage4.webp", xpos=20), show_icon="genie")
define g5 = Character(None, show_side_image=Image("characters/genie/mage5.webp", xpos=20), show_icon="genie")
define g6 = Character(None, show_side_image=Image("characters/genie/mage6.webp", xpos=20), show_icon="genie")
define g7 = Character(None, show_side_image=Image("characters/genie/mage7.webp", xpos=20), show_icon="genie")
define g8 = Character(None, show_side_image=Image("characters/genie/mage8.webp", xpos=20), show_icon="genie")
define g9 = Character(None, show_side_image=Image("characters/genie/mage9.webp", xpos=20), show_icon="genie")
define g10 = Character(None, show_side_image=Image("characters/genie/mage10.webp", xpos=20), show_icon="genie")
define g11 = Character(None, show_side_image=Image("characters/genie/mage11.webp", xpos=20), show_icon="genie")
define g12 = Character(None, show_side_image=Image("characters/genie/mage12.webp", xpos=20), show_icon="genie")
define g13 = Character(None, show_side_image=Image("characters/genie/mage13.webp", xpos=20), show_icon="genie")
define g14 = Character(None, show_side_image=Image("characters/genie/mage14.webp", xpos=20), show_icon="genie")
define g15 = Character(None, show_side_image=Image("characters/genie/mage15.webp", xpos=20), show_icon="genie")
define g16 = Character(None, show_side_image=Image("characters/genie/mage16.webp", xpos=20), show_icon="genie")

# Students
define twi = Character("Fred and George", show_side_image=Image("characters/misc/weasley_twins/base_01.webp", xalign=1.0), show_icon="fred")
define fre = Character("Fred", show_side_image=Image("characters/misc/weasley_twins/fred_01.webp", xalign=1.0), show_icon="fred")
define ger = Character("George", show_side_image=Image("characters/misc/weasley_twins/george_01.webp", xalign=1.0), show_icon="george")

# Teachers
define spo = Character("Professor Sprout")

# Side characters
define hat = Character("Sorting Hat", show_side_image=Image("characters/misc/hat.webp", xalign=1.0), show_icon="hat")
define helf = Character("House-Elf", show_side_image=Image("characters/misc/elf.webp", xalign=0.95))
define malf = Character("Malfoy")
define cra = Character("Crabbe")
define goy = Character("Goyle")
define maf = Character("Madam Mafkin", show_side_image=Image("characters/misc/mafkin.webp", xalign=1.0))
define myr = Character("Moaning Myrtle")
define faw = Character("Fawkes", show_icon="fawkes")
define abe = Character("Aberforth")

# Non-important characters
define fem = Character("Female Student")
define femv = Character("Female Voice")
define mal = Character("Male Student")
define mal2 = Character("Another Male Student")
define sly1 = Character("Slytherin student")
define sly2 = Character("Another Slytherin student")
define qcr = Character("Quidditch Crowd")

# Special
define nar = Character("", what_prefix=">", show_icon="narrator", callback=narrator_fade)
define narrator = nar # Note: Without this definition, anonymous narrator style will be overridden by Renpy.
define anon = Character("???")

# Dumbledore
define dum1 = Character("name_dumbledore_genie", show_side_image=Image("characters/misc/dumbledore/dum_1.webp"), show_icon="dumbledore", dynamic=True)
define dum2 = Character("name_dumbledore_genie", show_side_image=Image("characters/misc/dumbledore/dum_2.webp"), show_icon="dumbledore", dynamic=True)
define dum3 = Character("name_dumbledore_genie", show_side_image=Image("characters/misc/dumbledore/dum_3.webp"), show_icon="dumbledore", dynamic=True)
define dum4 = Character("name_dumbledore_genie", show_side_image=Image("characters/misc/dumbledore/dum_4.webp"), show_icon="dumbledore", dynamic=True)
define dum5 = Character("name_dumbledore_genie", show_side_image=Image("characters/misc/dumbledore/dum_5.webp"), show_icon="dumbledore", dynamic=True)
