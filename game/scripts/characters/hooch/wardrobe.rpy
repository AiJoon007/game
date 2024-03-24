###############
## Character ##
###############

default hooch = Doll(name="hooch")

default hoo_frame_default = DollBodypart("hooch", ("hidden", "frame"), "frame", "default")
default hoo_body_default = DollOutfit([hoo_frame_default], hidden=True)

###############
##   Hair    ##
###############

default hoo_hair_base = DollCloth("hooch", ("head", "hair"), "hair", "base", ["#7d482aff"], unlocked=True)
default hoo_panties_sport = DollCloth("hooch", ("lower undergarment", "panties"), "panties", "sport", ["#c04136ff", "#ede1ffff"], unlocked=True)
default hoo_bra_sport = DollCloth("hooch", ("upper undergarment", "bras"), "bra", "sport", ["#c04136ff", "#ede1ffff"], unlocked=True)
default hoo_top_sport = DollCloth("hooch", ("upper body", "shirts"), "top", "sport_shirt", ["#ede1ffff", "#8b68c0ff"], unlocked=True)
default hoo_bottom_sport = DollCloth("hooch", ("lower body", "skirts"), "bottom", "sport_trousers", ["#8b68c0ff", "#ede1ffff"], unlocked=True)
default hoo_gloves_sport = DollCloth("hooch", ("upper body", "gloves"), "gloves", "sport_gloves", ["#4e4873ff"], unlocked=True)
default hoo_robe_sport = DollCloth("hooch", ("upper body", "robes"), "robe", "sport_robe", ["#3b3f58ff", "#70226fff", "#c676c6ff"], unlocked=True)
default hoo_headgear_sport = DollCloth("hooch", ("head", "headgear"), "headgear", "sport_goggles", ["#608691ff", "#9a6232ff", "#313c5bff"], unlocked=True)
default hoo_accessory_broom = DollCloth("hooch", ("misc", "accessory"), "accessory", "broom", ["#905340ff", "#795747ff", "#a39f70ff"], unlocked=True, zorder=300)
default hoo_accessory_broom_dildo = DollCloth("hooch", ("misc", "accessory"), "accessory", "broom_dildo", ["#905340ff", "#795747ff", "#a39f70ff"], unlocked=True, zorder=300)

default hoo_outfit_default = DollOutfit([hoo_hair_base, hoo_panties_sport, hoo_bra_sport, hoo_top_sport, hoo_bottom_sport, hoo_gloves_sport, hoo_robe_sport, hoo_headgear_sport, hoo_accessory_broom], unlocked=True)
default hoo_outfit_last = DollOutfit([hoo_hair_base, hoo_panties_sport, hoo_bra_sport, hoo_top_sport, hoo_bottom_sport, hoo_gloves_sport, hoo_robe_sport, hoo_headgear_sport, hoo_accessory_broom], hidden=True)
