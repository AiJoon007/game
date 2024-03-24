default tutorial_dict = {
    "hearts": ["Favours", "Hearts indicate your current status towards a personal favour.\n\n{color=#FFFFFF80}{b}Empty Heart{/b}{/color}{size=-2} indicates the event hasn't been seen yet.{/size}\n{color=#bf5649}{b}Red Heart{/b}{/color}{size=-2} indicates completion of the event.{/size}\n{color=#333333}{b}Black Heart{/b}{/color}{size=-2} indicates failure of the event and you should try it again at a higher character level.{/size}\n{b}{color=#FFFFFF80}Half{/color} {color=#bf5649}Heart{/color}{/b}{size=-2} indicates there's a hidden path inside the event you should follow, in order to progress further.{/size}", False],
    "moodngifts": ["Mood & Gifts", "Sometimes your choices may upset some characters, just like in life. You can try and avoid picking options that you think would upset them, but if you mess up, buy them some nice {color=#204997}{b}gift{/b}{/color} and they might forgive you. Keep in mind that every character has their own gift preferences.\n\nAlternatively, you can wait until they calm down but who knows how long that would take.", False],
    "hangouts": ["Hangouts", "Getting to know your accomplices is an important aspect of progressing through the game. Hanging out with Snape for example improves your friendship and support which has various benefits such as story and character related unlockables.\n\nYou can check your current relationship status in the {color=#204997}{b}characters menu{/b}{/color}.", False],
    "workngold": ["Working & Gold", "Gold is a universal currency in the magical world. To earn gold you must complete at least one full report for the ministry. You can start working by clicking on the {color=#204997}{b}work button{/b}{/color} or clicking on the desk and papers.\n\nYou might find other work opportunities as you progress through the game. Please note that characters may not be available at all times.", False],
    "inventory": ["Inventory & Items", "The inventory screen allows you to examine items you possess. You can access it by clicking on the {color=#204997}{b}inventory button{/b}{/color} located on the top right part of the screen. The inventory is split into two main categories:\n{color=#204997}{b}Gifts{/b}{/color} - Items that can be given to other characters.\n{color=#204997}{b}Quest Items{/b}{/color} - Important items related to game progression. Some of them can be used by clicking on the {b}USE{/b} button next to the item name when it's selected.", False],
    "schedule": ["Outfits Schedule", "Outfits can be assigned into a set schedule, which will allow the girls to pick what they are going to wear next time you summon them, based on time of day and weather conditions.\n\nYou can assign schedules inside the Wardrobe's Outfits Manager section, by clicking on the icon represented above. \n\nThis feature can be disabled at any time in the wardrobe options menu.", False],
    "points": ["House Points", "House points are awarded to students for excelling in their assignments. You can manipulate the points system directly by awarding points to students for completing their tasks, or by befriending the teachers.\n\nSome characters may care about house points more than others so keep that in mind.", False],
    "map": ["Navigation", "The map allows you to traverse the castle by clicking on one of the icons. Highlighted areas indicate a new event on that location. You can access the map from within the desk menu.", False],
    "time": ["Passing Time", "There are many activities you may do at Hogwarts, but occasionally there might not be much to do.\nIf this is the case then you can pass time by clicking on the {color=#204997}{b}pass time button{/b}{/color} located in the top-right corner.\n\n{size=-2}Or you could always rub one out for old time's sake. The choice is yours.{/size}", False],
    "mail": ["Mail", "Owls will occasionally bring you letters or parcels. Click on the owl or parcel to interact with it.\n\nUnlike mail pidgeons, owls are tidy creatures and won't shit all over your floors. Theoretically...", False],
    "brewing": ["Potions Brewing", "Brewing potions wasn't always an easy task, but thanks to Magic Cauldron incorporated (TM), the entire process became automated. Once you have the required ingredients in your inventory, simply click on the {color=#204997}{b}cauldron{/b}{/color} to make the desired potion.", False],
    "milestones": ["Relationship milestones", "Every milestone is a chance to level up your bond with your virtual companion, leaving your real love life in the dust. Instead of boring old XP, you'll earn a boatload of (s)ass. Now that's what I call an upgrade! No need to go through any awkward first date chat, just advance to the next level.\n\nChoosing this option will progress their story and unlock more favours and events.\n\nBut beware, once you commit, old favours become inaccessible and are replaced with new ones. You may wish to postpone it until you exhaust all content you wish to see on the current level. So choose wisely, my friend.", False],
}

init python:
    def tutorial_is_done(entry):
        if not settings.get('tutorials'):
            return True
        return tutorial_dict[entry][2]

label tutorial(entry):
    if not tutorial_dict[entry][2] and settings.get('tutorials'):
        $ tutorial_dict[entry][2] = True
        play sound "sounds/pop01.ogg"
        $ renpy.music.set_volume(0.5, 3.0)
        $ gui.in_context("tutorial.display", entry)
        $ renpy.music.set_volume(1.0, 3.0)
        $ enable_game_menu()
    return

    label .display(entry):
        show screen tutorial(entry)
        $ _choice = ui.interact()
        return

screen tutorial(entry):
    modal True

    add "gui_fade"

    frame:
        style_prefix gui.theme()
        xsize 518
        align (0.5, 0.5)
        padding (12 + 6, 6, 12 + 6, 12 + 6)

        vbox:
            spacing 12
            first_spacing 0

            fixed:
                ysize 24
                add gui.format("interface/achievements/{}/highlight.webp") xalign 0.5
                add gui.format("interface/achievements/{}/spacer.webp") align (0.5, 1.0)
                text "Tutorial" size 10 yalign 0.5
                text tutorial_dict[entry][0] size 16 xalign 0.5 yalign 0.5

            if renpy.loadable("interface/tutorials/{}.webp".format(entry)):
                add "interface/tutorials/{}.webp".format(entry) xalign 0.5

            text tutorial_dict[entry][1] size 12

            textbutton "Ok" align (1.0, 1.0) action Return(True)
