###############
## Character ##
###############

default luna = Doll(name="luna")

default lun_frame_default = DollBodypart("luna", ("hidden", "frame"), "frame", "default")
default lun_body_default = DollOutfit([lun_frame_default], hidden=True)

##########
## Hair ##
##########

default lun_hair_base = DollCloth("luna", ("head", "hair"), "hair", "base", ["#ede0c3ff", "#bfa46bff", "#309087ff"], unlocked=True)

#######################
## Schoolgirl Outfit ##
#######################

default lun_hair_wand = DollCloth("luna", ("head", "hair"), "hair", "wand", ["#ede0c3ff", "#bfa46bff", "#309087ff"], unlocked=True)
default lun_glasses_hearts = DollCloth("luna", ("head", "glasses"), "glasses", "sunglasses_2", ["#f078ffff", "#009effff"], unlocked=True)
default lun_glasses_spectrespecs = DollCloth("luna", ("head", "glasses"), "glasses", "spectrespecs", ["#e36682ff", "#3d6e8cff"], unlocked=True)
default lun_accessory_pin_radish = DollCloth("luna", ("misc", "accessory"), "accessory", "pin_radish", ["#b61710ff", "#e8bebcff"], zorder=213, unlocked=True)
default lun_accessory_hair_bug = DollCloth("luna", ("misc", "accessory"), "accessory", "hair_bug", ["#ffffffff"], unlocked = True, zorder=252)

default lun_top_school1 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_1", ["#b7b7b8ff", "#6d6979ff", "#5974c2ff", "#d8a30aff"], unlocked=True)
default lun_top_school2 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_2", ["#b7b7b8ff", "#6d6979ff", "#5974c2ff", "#d8a30aff"], unlocked=True)
default lun_top_school3 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_3", ["#b7b7b8ff", "#6d6979ff", "#5974c2ff", "#d8a30aff"], unlocked=True)
default lun_top_school4 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_4", ["#b7b7b8ff", "#5974c2ff", "#d8a30aff"], unlocked=True)
default lun_top_vest = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_vest", ["#6d6979ff", "#5974c2ff", "#d8a30aff"], unlocked=True, level=4)
default lun_top_school5 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_5", ["#b7b7b8ff", "#5974c2ff", "#d8a30aff"], unlocked=True, level=4)
default lun_top_school6 = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_6", ["#b7b7b8ff", "#5974c2ff", "#d8a30aff"], unlocked=True, level=5)
default lun_top_crop = DollCloth("luna", ("upper body", "shirts"), "top", "top_school_crop", ["#b7b7b8ff", "#5974c2ff", "#d8a30aff"], unlocked=True, level=7)

default lun_neckwear_tie = DollCloth("luna", ("head", "neckwear"), "neckwear", "tie", ["#5974c2ff", "#d8a30aff"], unlocked = True, zorder=213) # Tie Only

default lun_bottom_school1 = DollCloth("luna", ("lower body", "skirts"), "bottom", "school_skirt_1", ["#675a6cff", "#e8b10dff"], unlocked=True)
default lun_bottom_school2 = DollCloth("luna", ("lower body", "skirts"), "bottom", "school_skirt_2", ["#675a6cff", "#e8b10dff"], unlocked=True)
default lun_bottom_school3 = DollCloth("luna", ("lower body", "skirts"), "bottom", "school_skirt_3", ["#675a6cff", "#e8b10dff"], unlocked=True, level=4)
default lun_bottom_school4 = DollCloth("luna", ("lower body", "skirts"), "bottom", "school_skirt_4", ["#675a6cff", "#e8b10dff"], unlocked=True, level=6)

default lun_stockings_school = DollCloth("luna", ("legwear", "stockings"), "stockings", "short_school_1", ["#5974c2ff", "#d8a30aff"], unlocked=True)
default lun_stockings_school2 = DollCloth("luna", ("legwear", "stockings"), "stockings", "short_school_2", ["#5974c2ff"], unlocked=True)

default lun_bra_base1 = DollCloth("luna", ("upper undergarment", "bras"), "bra", "basic_bra_1", ["#525c6bff", "#003280ff", "#003280ff"], unlocked=True)
default lun_panties_base1 = DollCloth("luna", ("lower undergarment", "panties"), "panties", "basic_panties_1", ["#525c6bff", "#003280ff", "#003280ff"], unlocked=True)
default lun_panties_lace2 = DollCloth("luna", ("lower undergarment", "panties"), "panties", "lace_panties_2", ["#1f5bb0ff", "#fff1edff", "#fff1edff"], level=7, unlocked=True)

default lun_robe_school_1 = DollCloth("luna", ("upper body", "robes"), "robe", "robe_school_1", ["#606060ff", "#5974c2ff"], unlocked=True, level=0)
default lun_robe_school_2 = DollCloth("luna", ("upper body", "robes"), "robe", "robe_school_2", ["#606060ff", "#5974c2ff"], unlocked=True, level=4)
default lun_robe_school_3 = DollCloth("luna", ("upper body", "robes"), "robe", "robe_school_3", ["#606060ff", "#5974c2ff"], unlocked=True, level=5)
default lun_robe_school_4 = DollCloth("luna", ("upper body", "robes"), "robe", "robe_school_4", ["#606060ff", "#5974c2ff"], unlocked=True, level=7)

default lun_outfit_default = DollOutfit([lun_hair_base, lun_top_school1, lun_bottom_school2, lun_bra_base1, lun_panties_base1, lun_stockings_school], unlocked=True)
default lun_outfit_default_quirky = DollOutfit([lun_hair_wand, lun_accessory_hair_bug, lun_glasses_spectrespecs, lun_accessory_pin_radish, lun_neckwear_tie, lun_top_school3, lun_bottom_school2, lun_bra_base1, lun_panties_base1, lun_stockings_school], unlocked=True)
default lun_outfit_default_no_vest = DollOutfit([lun_hair_base, lun_top_school4, lun_bottom_school2, lun_bra_base1, lun_panties_base1, lun_stockings_school], hidden=True)
default lun_outfit_school_slut = DollOutfit([lun_hair_base, lun_glasses_hearts, lun_top_crop, lun_bottom_school4, lun_panties_lace2, lun_stockings_school])#, hidden=True)
default lun_outfit_last = DollOutfit([lun_hair_base], hidden=True)

###################
## Bikini Outfit ##
###################

default lun_bra_bikini3 = DollCloth("luna", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_3", ["#0052c6ff", "#ad987eff"], level=7)
default lun_panties_bikini3 = DollCloth("luna", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_3", ["#0052c6ff", "#ad987eff"], level=7)

default lun_outfit_bikini3 = DollOutfit([lun_hair_base, lun_bra_bikini3, lun_panties_bikini3], price=350, name="Rave Bikini Set", desc="Skilfully assembled from scrapped materials.")

###########################
## Lace Underwear Outfit ##
###########################

default lun_bra_lace1 = DollCloth("luna", ("upper undergarment", "bras"), "bra", "lace_bra_1", ["#717171ff", "#343434ff"], level=7)
default lun_panties_lace1 = DollCloth("luna", ("lower undergarment", "panties"), "panties", "lace_panties_1", ["#717171ff", "#343434ff"], level=7)

default lun_outfit_lace1 = DollOutfit([lun_hair_base, lun_bra_lace1, lun_panties_lace1], price=250, name="Lace Lingerie", desc="For a girl that's feeling a bit lacy.")

#####################
## Swimsuit Outfit ##
#####################

default lun_top_swimsuit1 = DollCloth("luna", ("upper body", "one-piece suits"), "top", "swimsuit_1", ["#ffacb8d7", "#ee7572ff"], blacklist=["panties", "bra"], zorder=183, level=6)

default lun_outfit_swimsuit = DollOutfit([lun_hair_base, lun_top_swimsuit1], price=350, name="One-piece Swimsuit", desc="Buy this outfit and everything will work out swimmingly.")

###################
## Pajama Outfit ## #Unlocked in Luna Intro
###################

default lun_top_pajama = DollCloth("luna", ("upper body", "shirts"), "top", "pajama_1", ["#f97ec5ff", "#b61710ff"])
default lun_bottom_pajama = DollCloth("luna", ("lower body", "trousers"), "bottom", "pajama_1", ["#ffc5d3ff", "#b61710ff"])

default lun_outfit_pajama = DollOutfit([lun_hair_base, lun_accessory_pin_radish, lun_top_pajama, lun_bottom_pajama, lun_bra_base1, lun_panties_base1], unlocked=True)

######################
## Flight Attendant ##
######################

default lun_top_flight_attendant_1 = DollCloth("luna", ("upper body", "dresses"), "top", "flight_attendant_1", ["#525282ff", "#e14010ff"])
default lun_top_flight_attendant_2 = DollCloth("luna", ("upper body", "dresses"), "top", "flight_attendant_2", ["#525282ff", "#e14010ff"], level=6)
default lun_neckwear_neckerchief = DollCloth("luna", ("head", "neckwear"), "neckwear", "neckerchief", ["#525282ff"])
default lun_headgear_flight_attendant = DollClothDynamic("luna", ("head", "headgear"), "headgear", "flight_attendant", ["#e14010ff"], tracking="?hair")
default lun_panties_flight_attendant_1 = DollCloth("luna", ("lower undergarment", "bikini panties"), "panties", "flight_attendant_thongs_1", ["#e14010ff"], level=7)
default lun_panties_flight_attendant_2 = DollCloth("luna", ("lower undergarment", "bikini panties"), "panties", "flight_attendant_thongs_2", ["#e14010ff", "#e8b77bff"], level=9)

default lun_outfit_flight_attendant = DollOutfit([lun_hair_base, lun_top_flight_attendant_1, lun_neckwear_neckerchief, lun_headgear_flight_attendant, lun_panties_flight_attendant_1], addons=[lun_top_flight_attendant_2, lun_panties_flight_attendant_2], price=350, name="Flight Attendant Costume", desc="An outfit attendants wear in those flying metal things.")

###################
## Muggle Outfit ##
###################

default lun_top_muggle_top = DollCloth("luna", ("upper body", "shirts"), "top", "muggle_top", ["#7f6d8cff", "#e783baff"])
default lun_robe_muggle_jacket = DollCloth("luna", ("upper body", "robes"), "robe", "muggle_jacket", ["#f7bec4ff", "#863c4aff"], level=4)
default lun_bottom_muggle_skirt = DollCloth("luna", ("lower body", "skirts"), "bottom", "muggle_skirt", ["#2b2b2bff", "#3d8ec2ff", "#53a996ff", "#f3f3f3ff", "#e29496ff", "#f5d284ff"])
default lun_stockings_muggle_knee_socks = DollCloth("luna", ("legwear", "stockings"), "stockings", "muggle_knee_socks", ["#025792ff", "#00767fff", "#000f2bff"])

default lun_outfit_muggle = DollOutfit([lun_hair_base, lun_top_muggle_top, lun_robe_muggle_jacket, lun_bottom_muggle_skirt, lun_stockings_muggle_knee_socks, lun_bra_base1, lun_panties_base1], price=300, name="Muggle Outfit", desc="An outfit that probably at least one muggle somewhere would wear.")

###################
## Summer Outfit ##
###################

default lun_top_summer_top1 = DollCloth("luna", ("upper body", "shirts"), "top", "summer_top_1", ["#ff9acdff"])
default lun_top_summer_top2 = DollCloth("luna", ("upper body", "shirts"), "top", "summer_top_2", ["#ff9acdff"], level=7)
default lun_bottom_summer_shorts = DollCloth("luna", ("lower body", "shorts"), "bottom", "summer_shorts", ["#2f9688ff", "#afdcbfff", "#f79826ff"])
default lun_accessory_bracelets = DollCloth("luna", ("misc", "accessory"), "accessory", "bracelets", ["#24b82dff", "#3ab0d4ff", "#c2310fff"], zorder=225)

default lun_outfit_summer = DollOutfit([lun_hair_base, lun_top_summer_top1, lun_bottom_summer_shorts, lun_panties_base1, lun_accessory_bracelets], addons=[lun_top_summer_top2], price=350, name="Summer Set", desc="It's pretty hot.")

######################
## Reindeer Costume ## #unlocked in genies_christmas_wish mirror story
######################

default lun_top_bunny2 = DollCloth("luna", ("upper body", "one-piece suits"), "top", "bunny_top_2", ["#8e4a0aff"], blacklist=["panties", "bra"], zorder=183, level=7)
default lun_neckwear_chocolate_frog = DollCloth("luna", ("head", "neckwear"), "neckwear", "chocolate_frog", ["#ffffffff"])
default lun_earring_bauble = DollCloth("luna", ("head", "earrings"), "earrings", "bauble_earring", ["#a30000ff"], level=4)
default lun_hat_antlers = DollClothDynamic("luna", ("head", "headgear"), "headgear", "antlers", ["#8e4a0aff", "#ffffffff", "#dbc095ff"], tracking="?hair")
default lun_accessory_mistletoe = DollCloth("luna", ("misc", "accessory"), "accessory", "mistletoe", ["#bfbf56ff"], zorder=213, level=7)
default lun_stockings_pantyhose_meshed = DollCloth("luna", ("legwear", "pantyhose"), "stockings", "pantyhose_meshed", ["#000000ff"], unlocked=True)

default lun_outfit_reindeer = DollOutfit([lun_hair_base, lun_top_bunny2, lun_neckwear_chocolate_frog, lun_earring_bauble, lun_hat_antlers, lun_stockings_pantyhose_meshed, lun_accessory_mistletoe])

##################
## Bunny Outfit ##
##################

default lun_hat_bunny1 = DollClothDynamic("luna", ("head", "headgear"), "headgear", "bunny_hat_1", ["#dba18cff", "#fde3abff"], tracking="?hair")
default lun_top_bunny1 = DollCloth("luna", ("upper body", "one-piece suits"), "top", "bunny_top_1", ["#000000ff"], blacklist=["panties", "bra"], zorder=183, level=7)

default lun_outfit_bunny = DollOutfit([lun_hair_base, lun_top_bunny1, lun_stockings_pantyhose_meshed, lun_hat_bunny1], price=250, name="Sexy Bunny Costume", desc="A bunny costume for when you're hopping mad.")

########################
## Party Dress Outfit ##
########################

default lun_top_party_dress = DollCloth("luna", ("upper body", "dresses"), "top", "party_dress", ["#f8a800ff", "#ac5e1bff"])

default lun_outfit_party = DollOutfit([lun_hair_base, lun_top_party_dress, lun_panties_base1], price=350, name="Party Dress", desc="A weird dress for a weird girl.")

####################
## Nightie Outfit ##
####################

default lun_top_nightie1 = DollCloth("luna", ("upper body", "shirts"), "top", "nightie_1", ["#ffffffd7"], level=5)

default lun_outfit_nightie1 = DollOutfit([lun_hair_base, lun_top_nightie1], price=350, name="Loose-fitting Nightie", desc="The prefect nightie for a girl with her screws loose.")

##########################
## Loose Nightie Outfit ##
##########################

default lun_top_nightie2 = DollCloth("luna", ("upper body", "shirts"), "top", "nightie_2", ["#ffacb8d7"], level=6)

default lun_outfit_nightie2 = DollOutfit([lun_hair_base, lun_top_nightie2], price=350, name="Nightie", desc="The perfect garment if you're tired of wearing a pyjamas.")

###########################
## Police Officer Outfit ## #unlocked in not_so_great_escape mirror story
###########################

default lun_stockings_police = DollCloth("luna", ("legwear", "stockings"), "stockings", "police_thigh_highs", ["#2b2b55ff", "#8e8eb3ff"])
default lun_bottom_police_skirt = DollCloth("luna", ("lower body", "skirts"), "bottom", "police_skirt", ["#2e47abff"], level=5)
default lun_top_police_shirt = DollCloth("luna", ("upper body", "shirts"), "top", "police_shirt", ["#2e47abff", "#bbbbd2ff"], level=5)
default lun_accessory_police_belt = DollCloth("luna", ("misc", "accessory"), "accessory", "police_belt", ["#26265bff", "#bbbbd2ff"], zorder=212)
default lun_accessory_police_badge = DollCloth("luna", ("misc", "accessory"), "accessory", "police_badge", ["#192655ff", "#fcf16dff"], zorder=213)
default lun_accessory_police_cuffs = DollCloth("luna", ("misc", "accessory"), "accessory", "police_cuffs", ["#bbbbd2ff"], zorder=225)

default lun_outfit_police = DollOutfit([lun_hair_base, lun_stockings_police, lun_bottom_police_skirt, lun_top_police_shirt, lun_panties_base1, lun_accessory_police_badge, lun_accessory_police_belt], addons=[lun_accessory_police_cuffs])

#########################
## Harley Quinn Outfit ##
#########################

default lun_hair_harley_quinn = DollCloth("luna", ("head", "hair"), "hair", "harley_quinn", ["#ede0c3ff", "#bfa46bff", "#e43713ff", "#1365e4ff", "#ff5bf8ff"])
default lun_pantyhose_harley_quinn = DollCloth("luna", ("legwear", "pantyhose"), "stockings", "harley_quinn", ["#ae3512ff"])
default lun_top_harley_quinn = DollCloth("luna", ("upper body", "one-piece suits"), "top", "harley_quinn", ["#326280ff", "#8c9fb4ff", "#e43612ff", "#1264e4ff"])
default lun_robe_harley_quinn = DollCloth("luna", ("upper body", "robes"), "robe", "harley_quinn", ["#d8fcffff", "#8c9fb4ff", "#58d532ff", "#e44e14ff", "#ea48c0ff"])
default lun_gloves_harley_quinn = DollCloth("luna", ("upper body", "gloves"), "gloves", "harley_quinn", ["#1f3349ff"])
default lun_accessory_harley_quinn_strap = DollCloth("luna", ("misc", "accessory"), "accessory", "harley_quinn_strap", ["#1f3349ff"], zorder=183)

default lun_outfit_harley_quinn = DollOutfit([lun_hair_harley_quinn, lun_pantyhose_harley_quinn, lun_top_harley_quinn, lun_robe_harley_quinn, lun_gloves_harley_quinn, lun_accessory_harley_quinn_strap], price=500, name="Harley Quinn Outfit", desc="Attractively crazy.")

#################
## Lion Outfit ## (Event only)
#################

default lun_bottom_casual_jeans = DollCloth("luna", ("lower body", "trousers"), "bottom", "casual_jeans", ["#8027bfff"])
default lun_top_casual_sweater = DollCloth("luna", ("upper body", "shirts"), "top", "casual_sweater", ["#382088ff", "#382088ff"])
default lun_accessory_lionhead = DollCloth("luna", ("misc", "accessory"), "accessory", "lionhead", None)

default lun_outfit_casual= DollOutfit([lun_hair_base, lun_panties_base1, lun_bra_base1, lun_bottom_casual_jeans, lun_top_casual_sweater], unlocked=True)
default lun_outfit_lion_event = DollOutfit([lun_panties_base1, lun_bra_base1, lun_accessory_lionhead, lun_bottom_casual_jeans, lun_top_casual_sweater], hidden=True)

###############
## Underwear ##
###############

# Plain Underwear
default lun_bra_base2 = DollCloth("luna", ("upper undergarment", "bras"), "bra", "basic_bra_2", ["#d8e1e6ff", "#5974c2ff"], unlocked=True)
default lun_panties_base2 = DollCloth("luna", ("lower undergarment", "panties"), "panties", "basic_panties_2", ["#d8e1e6ff", "#5974c2ff"], unlocked=True)

#################
## Accessories ##
#################

default lun_neckwear_cork = DollCloth("luna", ("head", "neckwear"), "neckwear", "cork", ["#E98E2AFF", "#CECECEFF"], unlocked = True, zorder=213)

default lun_accessory_wand_mouth = DollCloth("luna", ("misc", "accessory"), "accessory", "wand_mouth", ["#ffffffff"], unlocked = True, zorder=213)
default lun_accessory_wand_hand = DollCloth("luna", ("misc", "accessory"), "accessory", "wand_hand", ["#ffffffff"], unlocked = True, zorder=222)
default lun_accessory_wand_breasts = DollCloth("luna", ("misc", "accessory"), "accessory", "wand_breasts", ["#ffffffff"], unlocked = True, zorder=213)
default lun_accessory_wand_pussy = DollCloth("luna", ("misc", "accessory"), "accessory", "wand_pussy", ["#ffffffff"], unlocked = True, zorder=183)

################
## Pubic Hair ##
################

default lun_pubes_arrow = DollCloth("luna", ("lower undergarment", "pubes"), "pubes", "arrow", ["#e4c991ff"], unlocked=True)
default lun_pubes_beaver = DollCloth("luna", ("lower undergarment", "pubes"), "pubes", "beaver", ["#e4c991ff"], unlocked=True)
default lun_pubes_stuble = DollCloth("luna", ("lower undergarment", "pubes"), "pubes", "stuble", ["#9b8558ff"], unlocked=True)
default lin_pubes_unshaved = DollCloth("luna", ("lower undergarment", "pubes"), "pubes", "unshaved", ["#9b8558ff"], unlocked=True)

#############
## Tattoos ##
#############

default lun_tattoo_measure = DollCloth("luna", ("piercings & tattoos", "tattoos"), "tattoo", "measure", ["#000000ff", "#db492cff"], unlocked=True)
default lun_tattoo_spurt_here = DollCloth("luna", ("piercings & tattoos", "tattoos"), "tattoo", "spurt_here", ["#000000ff"], unlocked=True)
default lun_tattoo_loony = DollCloth("luna", ("piercings & tattoos", "tattoos"), "tattoo", "loony", ["#000000ff"], unlocked=True)
default lun_tattoo_baby_oven = DollCloth("luna", ("piercings & tattoos", "tattoos"), "tattoo", "baby_oven", ["#000000ff", "#db492cff"], unlocked=True)

default lun_tattoo_lab_rat = DollCloth("luna", ("piercings & tattoos", "tattoos"), "tattoo", "lab_rat", ["#000000ff"], unlocked=True)

default lun_tattoo_cumdump = DollCloth("luna", ("piercings & tattoos", "tattoos"), "tattoo", "cumdump", ["#000000ff"], unlocked=True)

##########
## Misc ##
##########

default lun_stockings_pantyhose = DollCloth("luna", ("legwear", "pantyhose"), "stockings", "pantyhose_1", ["#b19083ff"], unlocked=True)

