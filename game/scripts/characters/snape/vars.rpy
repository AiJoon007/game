
# General states

default states.sna.busy = False
default states.sna.unlocked = False
default states.sna.level = 0
default states.sna.chatted = False
default states.sna.map_location = "room_potions"

# Image states

default states.sna.image.xpos = 525
default states.sna.image.ypos = 0
default states.sna.image.zorder = 15
default states.sna.image.xzoom = 1
default states.sna.image.zoom = 0.5
default states.sna.image.face = "snape_01"
default states.sna.image.animation = []

# Event flags

default states.sna.ev.intro.e1_complete = False # 1st visit
default states.sna.ev.intro.e2_complete = False # 2nd visit
default states.sna.ev.intro.e3_complete = False # 3rd visit, before the duel.
default states.sna.ev.intro.duel_complete = False
default states.sna.ev.intro.e4_complete = False # After the duel.
default states.sna.ev.intro.e5_complete = False # 4th visit, summon unlocked.
default states.sna.ev.hangouts.hermione_strip_invite = False
default states.sna.ev.hangouts.hermione_e1 = False
default states.sna.ev.hangouts.hermione_e2 = False
default states.sna.ev.hangouts.tonks_e1 = False
default states.sna.ev.hangouts.tonks_e2 = False
default states.sna.ev.hangouts.tonks_e3 = False
default states.sna.ev.hangouts.cho_e1 = False
default states.sna.ev.hangouts.cho_e2 = False
default states.sna.ev.cardgame.stage = 0
default states.sna.ev.cardgame.wagers = False
default states.sna.ev.cardgame.known = False
