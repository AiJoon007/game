
# General states

default states.ton.tier = 1
default states.ton.level = 0
default states.ton.public_tier = 0
default states.ton.public_level = 0
default states.ton.mood = 0
default states.ton.unlocked = False
default states.ton.busy = False
default states.ton.gifted = False
default states.ton.favors_unlocked = False
default states.ton.requests_unlocked = False
default states.ton.wardrobe_unlocked = True # Unlocked by default
default states.ton.wardrobe_scheduling = True
default states.ton.chatted = False
default states.ton.map_location = "room_defense"

# Event flags

default states.ton.ev.intro.e1_complete = False # 1st visit
default states.ton.ev.intro.e2_complete = False # 2nd visit
default states.ton.ev.intro.e3_complete = False # 3rd visit, summon unlocked.
default states.ton.ev.hangouts.hermione_e1 = False
default states.ton.ev.hangouts.susan_e1 = False
default states.ton.ev.hangouts.astoria_e1 = False
default states.ton.ev.hangouts.favors_e1 = False
default states.ton.ev.hangouts.favors_e2 = False
default states.ton.ev.random_strip.complete = False
default states.ton.ev.oral_practice.completed_once = False
default states.ton.ev.hands_on_lessons.completed_once = False
default states.ton.ev.hangouts.wine_intro = False

default ton_level_up = None

init offset = 5
default tonks_haircolor = [c for c in ton_hair_base.color]
init offset = 0

# Names
default name_tonks_genie = "Tonks"
default name_genie_tonks = "Professor"
default name_astoria_tonks = "Cutie"
