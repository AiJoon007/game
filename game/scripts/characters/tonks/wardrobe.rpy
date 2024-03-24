###############
## Character ##
###############

default tonks = Doll(name="tonks")

default ton_frame_default = DollBodypart("tonks", ("hidden", "frame"), "frame", "default")
default ton_body_default = DollOutfit([ton_frame_default], hidden=True)

##########
## Hair ##
##########

default ton_hair_short = DollCloth("tonks", ("head", "hair"), "hair", "base", ["#ff92b9ff", "#fedaeeff"], unlocked=True)
default ton_hair_base = DollCloth("tonks", ("head", "hair"), "hair", "new", ["#ff92b9ff", "#fedaeeff"], unlocked=True)

##################
## Auror Outfit ##
##################

default ton_neckwear_beads = DollCloth("tonks", ("head", "neckwear"), "neckwear", "choker_beads",["#2d2d30ff", "#f4e6ecff"], unlocked=True)
default ton_gloves_auror = DollCloth("tonks", ("upper body", "gloves"), "gloves", "auror_gloves",["#2d2d30ff"], unlocked=True)

default ton_top_auror  = DollCloth("tonks", ("upper body", "shirts"), "top", "auror",["#1c1b1fff", "#7c2a32ff"], unlocked=True)
default ton_top_auror2 = DollCloth("tonks", ("upper body", "shirts"), "top", "auror2",["#7c2a32ff"], unlocked=True)

default ton_bottoms_leggings = DollCloth("tonks", ("lower body", "leggings"), "bottom", "leggings",["#2d2d30ff"], unlocked=True)
default ton_bottoms_leggings_hole = DollCloth("tonks", ("lower body", "leggings"), "bottom", "leggings_hole",["#2d2d30ff"], level=60, unlocked=True)

default ton_stockings_auror = DollCloth("tonks", ("legwear", "stockings"), "stockings", "auror",["#2d2d30ff", "#b1a8acff"], unlocked=True)

default ton_robe_auror = DollCloth("tonks", ("upper body", "robes"), "robe", "auror_coat",["#282829ff", "#f4e6ecff"], unlocked=True)

default ton_outfit_default = DollOutfit([ton_hair_base, ton_neckwear_beads, ton_gloves_auror, ton_top_auror, ton_robe_auror, ton_bottoms_leggings, ton_stockings_auror], unlocked=True)
default ton_outfit_last = DollOutfit([ton_hair_base], hidden=True)

#######################
## Schoolgirl Outfit ##
#######################

#default ton_bottom_school1 = DollCloth("tonks", ("lower body", "skirts"), "bottom", "school_skirt_1", ["#675a6cff", "#e8b10dff"], unlocked=True) # Not implemented
default ton_top_tied = DollCloth("tonks", ("upper body", "other"), "top", "tied_top",["#b7b7b8ff"], blacklist=["bra"])
default ton_bottom_school2 = DollCloth("tonks", ("lower body", "skirts"), "bottom", "school_skirt_2", ["#675a6cff", "#e8b10dff"], level=20)
default ton_bottom_school3 = DollCloth("tonks", ("lower body", "skirts"), "bottom", "school_skirt_3", ["#675a6cff", "#e8b10dff"], level=40)
default ton_bottom_school4 = DollCloth("tonks", ("lower body", "skirts"), "bottom", "school_skirt_4", ["#675a6cff", "#e8b10dff"], level=60)

default ton_outfit_school = DollOutfit([ton_hair_base, ton_top_tied, ton_bottom_school2], price=350, name="Oldschool School Uniform", desc="A very tight school outfit back from 1995!")

###################
## Casual Outfit ##
###################

default ton_top_crop_casual = DollCloth("tonks", ("upper body", "shirts"), "top", "crop_top",["#c8082dff"])
default ton_bottoms_leggings_casual = DollCloth("tonks", ("lower body", "leggings"), "bottom", "latex_leggings",["#202020ff", "#191818ff"])

default ton_outfit_casual = DollOutfit([ton_hair_base, ton_top_crop_casual, ton_bottoms_leggings_casual], price=350, name="Sexy Casual Outfit", desc="Leggings make squeaky sounds when rubbed together.")

####################
## Nightie Outfit ##
####################

default ton_top_nightie_1 = DollCloth("tonks", ("upper body", "shirts"), "top", "nightie_1", ["#992660ff"])

default ton_outfit_nightie = DollOutfit([ton_hair_base, ton_top_nightie_1], price=350, name="Nightie", desc="Doesn't leave much for the imagination.")

##################
## Bunny Outfit ##
##################

default ton_top_bunny1 = DollCloth("tonks", ("upper body", "one-piece suits"), "top", "bunnysuit", ["#303030ff"], blacklist=["panties", "bra"], zorder=183, level=40)
default ton_stockings_bunny1 = DollCloth("tonks", ("legwear", "pantyhose"), "stockings", "bunny_stockings_1", ["#515151ff"], level=40)
default ton_hat_bunny1 = DollClothDynamic("tonks", ("head", "headgear"), "headgear", "bunny", ["#303030ff", "#e8e8e8ff"], level=20, tracking="?hair")
default ton_neckwear_bunny1 = DollCloth("tonks", ("head", "neckwear"), "neckwear", "bunny_bowtie_1", ["#e8e8e8ff", "#303030ff"], level=10)

default ton_outfit_bunny = DollOutfit([ton_hair_base, ton_top_bunny1, ton_stockings_bunny1, ton_hat_bunny1, ton_neckwear_bunny1], price=350, name="Sexy Bunny Outfit", desc="Vewy sexy :3")

##########################
## Dressing Gown Outfit ##
##########################

default ton_robe_dressing_gown = DollCloth("tonks", ("upper body", "robes"), "robe", "dressing_gown", ["#0d004cff", "#1f29abff"])

default ton_outfit_dressing_gown = DollOutfit([ton_hair_base, ton_robe_dressing_gown])

########################
## Silky Dress Outfit ##
########################

default ton_top_silk_dress = DollCloth("tonks", ("upper body", "dresses"), "top", "silk_dress", ["#f0edfaBF", "#eaeaeaff"], blacklist=["bra", "bottom"])
default ton_robe_silk = DollCloth("tonks", ("upper body", "robes"), "robe", "silk_robe", ["#f0edfaff"])

default ton_outfit_silky = DollOutfit([ton_hair_base, ton_top_silk_dress, ton_robe_silk], price=350, name="Silky Dress", desc="{size=-4}Disclaimer: Madam Mafkin isn't responsible for damaged nipples.{/size}")

#################################
## Very Revealing Dress Outfit ##
#################################

default ton_top_skimpy_dress = DollCloth("tonks", ("upper body", "dresses"), "top", "skimpy_dress", ["#930101ff"], blacklist=["bottom"], level=40)
default ton_stockings_long2 = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_basic_2",["#000000ff", "#101010ff"])

default ton_outfit_skimpy_dress = DollOutfit([ton_hair_base, ton_top_skimpy_dress, ton_stockings_long2], price=300, name="Very Revealing Dress", desc="This dress shows quite a bit of cleavage... All of it in fact.")

#######################
## Club Dress Outfit ##
#######################

default ton_top_skimpy_dress2 = DollCloth("tonks", ("upper body", "dresses"), "top", "skimpy_dress_2", ["#6c0069ff"], blacklist=["bottom"], level=20)
default ton_stockings_long_meshed = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_meshed",["#000000ff", "#000000ff"]) # Referee Outfit - SOON

default ton_outfit_club_dress = DollOutfit([ton_hair_base, ton_top_skimpy_dress2, ton_stockings_long_meshed], price=300, name="Club Dress", desc="A sultry muggle dress like this will turn heads at any wizard pub.")

#####################
## Succubus Outfit ##
#####################

default ton_hat_succubus = DollClothDynamic("tonks", ("head", "headgear"), "headgear", "horns", ["#3e3339ff", "#6a3f43ff"], tracking="?hair")
default ton_neckwear_succubus = DollCloth("tonks", ("head", "neckwear"), "neckwear", "succubus_colar", ["#3e3339ff"])

default ton_gloves_succubus = DollCloth("tonks", ("upper body", "gloves"), "gloves", "succubus_gloves", ["#3e3339ff"])
default ton_top_succubus = DollCloth("tonks", ("upper body", "other"), "top", "succubus_corset",["#3e3339ff", "#b55654ff", "#888686ff"], blacklist=["bra"])
default ton_top_succubus2 = DollCloth("tonks", ("upper body", "other"), "top", "succubus_corset_2",["#3e3339ff", "#b55654ff", "#888686ff"])
default ton_panties_succubus = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "succubus_panties", ["#3e3339ff", "#888686ff"])

default ton_accessory1_succubus = DollCloth("tonks", ("misc", "accessory"), "accessory", "succubus_wings", ["#3e3339ff", "#b55654ff", "#888686ff"], zorder=-500)
default ton_accessory2_succubus = DollCloth("tonks", ("misc", "accessory"), "accessory", "succubus_tail", ["#3e3339ff", "#b55654ff"], zorder=-11)

default ton_outfit_succubus = DollOutfit([ton_hair_base, ton_hat_succubus, ton_neckwear_succubus, ton_gloves_succubus, ton_top_succubus, ton_panties_succubus, ton_accessory1_succubus, ton_accessory2_succubus], addons=[ton_top_succubus2], name="Succubus Costume", desc="Hot as hell.")

#####################
## Cavegirl Outfit ##
#####################

default ton_earring_pearls = DollCloth("tonks", ("head", "earrings"), "earrings", "pearls", ["#dff0ffff"])
default ton_neckwear_pearls = DollCloth("tonks", ("head", "neckwear"), "neckwear", "pearls_1", ["#dff0ffff"], zorder=213)
default ton_top_cavegirl = DollCloth("tonks", ("upper body", "dresses"), "top", "cavegirl_dress", ["#dff0ffff"])

default ton_outfit_cavegirl = DollOutfit([ton_hair_base, ton_top_cavegirl, ton_earring_pearls, ton_neckwear_pearls], price=200, name="Cavegirl Dress", desc="A stone age inspired dress that brings you back to the age of rocking knockers.")

#####################
## Pullover Outfit ##
#####################

default ton_top_pullover = DollCloth("tonks", ("upper body", "shirts"), "top", "pullover",["#fdf0e6fa"])
default ton_stockings_long_ribbed = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_ribbed",["#fdf0e6ff", "#ff4fbaff"])

default ton_outfit_pullover = DollOutfit([ton_hair_base, ton_top_pullover, ton_stockings_long_ribbed], price=200, name="Pullover Outfit", desc="An outfit so defined it will make anyone pull over when they spot it.")

###################
## Lady D Outfit ##
###################

default ton_hat_classy = DollClothDynamic("tonks", ("head", "headgear"), "headgear", "classy_hat", ["#52525eff"], tracking="?hair")
default ton_neckwear_pearls2 = DollCloth("tonks", ("head", "neckwear"), "neckwear", "pearls_2", ["#dcc88bff"])
default ton_earring_pearls2 = DollCloth("tonks", ("head", "earrings"), "earrings", "pearls_2", ["#dcc88bff"])

default ton_accessory_flower = DollCloth("tonks", ("misc", "accessory"), "accessory", "flower", ["#5c5c5cff"], zorder=213)
default ton_gloves_leather = DollCloth("tonks", ("upper body", "gloves"), "gloves", "leather_gloves", ["#4f4940ff"])
default ton_top_classy_dress = DollCloth("tonks", ("upper body", "dresses"), "top", "classy_dress",["#cbc9b8ff"], blacklist=["bra"])

default ton_outfit_lady_D = DollOutfit([ton_hair_base, ton_hat_classy, ton_neckwear_pearls2, ton_earring_pearls2, ton_accessory_flower, ton_gloves_leather, ton_top_classy_dress], price=400, name="Lady D Costume", desc="This outfit was once worn by a very tall and scary lady.")

##################
## Police Woman ## #Unlocked in not_so_great_escape mirror story
##################

default ton_headgear_police = DollClothDynamic("tonks", ("head", "headgear"), "headgear", "police", ["#7e7ec0ff", "#4865b7ff", "#ebd165ff"], tracking="?hair")
default ton_glasses_police = DollCloth("tonks", ("head", "glasses"), "glasses", "police", ["#b5c7d6ff", "#b14d74ff"])

default ton_top_police1 = DollCloth("tonks", ("upper body", "shirts"), "top", "police1", ["#7e7ec0ff", "#4865b7ff", "#ebd165ff"])
default ton_top_police2 = DollCloth("tonks", ("upper body", "shirts"), "top", "police2", ["#4865b7ff", "#ebd165ff"])
default ton_top_police3 = DollCloth("tonks", ("upper body", "shirts"), "top", "police3", ["#7e7ec0ff"])
default ton_bottom_police = DollCloth("tonks", ("lower body", "shorts"), "bottom", "police",["#4865b7ff", "#7e7ec0ff"])
default ton_accessory_police = DollCloth("tonks", ("misc", "accessory"), "accessory", "police_badge", ["#eed165ff"], zorder=213)

default ton_outfit_police = DollOutfit([ton_hair_base, ton_headgear_police, ton_accessory_police, ton_glasses_police, ton_top_police1, ton_bottom_police], addons=[ton_top_police2, ton_top_police3])

############################
## Wrestling Coach Outfit ## #Unlocked in a_white_christmas mirror story
############################

default ton_neckwear_whistle = DollCloth ("tonks", ("head", "neckwear"), "neckwear", "whistle", ["#6e4025ff", "#86a0a9ff"])
default ton_top_sweatshirt = DollCloth("tonks", ("upper body", "shirts"), "top", "sweatshirt", ["#f3f0d8ff"])
default ton_bottom_sweatpants = DollCloth("tonks", ("lower body", "trousers"), "bottom", "sweatpants", ["#a33530ff", "#f3f0d8ff"])
default ton_accessory_neck_towel = DollCloth("tonks", ("misc", "accessory"), "accessory", "neck_towel", ["#fffcd8ff"], zorder=213)

default ton_outfit_wrestling_coach = DollOutfit([ton_hair_base, ton_neckwear_whistle, ton_top_sweatshirt, ton_bottom_sweatpants, ton_accessory_neck_towel])

#####################
## Mechanic Outfit ##
#####################

default ton_hair_mechanic = DollCloth("tonks", ("head", "hair"), "hair", "mechanic_hair", ["#ff92b9ff", "#fedaeeff"])
default ton_top_vest_mechanic = DollCloth("tonks", ("upper body", "other"), "top", "mechanic_vest", ["#ff840bff", "#fff24aff", "#97a9abff"], blacklist=["bra", "piercing"])
default ton_shorts_mechanic = DollCloth("tonks", ("lower body", "shorts"), "bottom", "mechanic_shorts", ["#6891ceff", "#7a4335ff", "#97a9abff", "#b6cbe9ff"])
default ton_gloves_mechanic = DollCloth("tonks", ("upper body", "gloves"), "gloves", "mechanic_gloves", ["#303030ff"])
default ton_headgear_cap_mechanic = DollClothDynamic("tonks", ("head", "headgear"), "headgear", "mechanic_cap", ["#ff840bff", "#fff24aff"], tracking="?hair")
default ton_panties_mechanic = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "mechanic_bikini", ["#ff840bff"])
default ton_socks_mechanic = DollCloth("tonks", ("legwear", "socks"), "stockings", "mechanic_thigh_socks",["#303030ff"])

default ton_outfit_mechanic = DollOutfit([ton_hair_mechanic, ton_top_vest_mechanic, ton_shorts_mechanic, ton_gloves_mechanic, ton_headgear_cap_mechanic, ton_panties_mechanic, ton_socks_mechanic], price=450, name="Mechanic Outfit", desc="If your exhaust pipe needs cleaning, this is the perfect outfit for the occassion!")

#####################
## Tuxedo (Office) ##
#####################

default ton_robe_office = DollCloth("tonks", ("upper body", "robes"), "robe", "office",["#353843ff", "#fff24aff"])
default ton_top_office = DollCloth("tonks", ("upper body", "shirts"), "top", "office", ["#e7e7e7ff", "#d1cebbff"])
default ton_bottoms_office = DollCloth("tonks", ("lower body", "trousers"), "bottom", "office",["#353843ff"])
default ton_accessory_office = DollCloth("tonks", ("misc", "accessory"), "accessory", "office_pin", ["#e7e7e7ff", "#fff24aff", "#d8422cff"], zorder=225)

default ton_outfit_office = DollOutfit([ton_hair_base, ton_robe_office, ton_top_office, ton_bottoms_office, ton_accessory_office], price=450, name="SECS Outfit", desc="A smart suit for a clever girl.")

#########################
## Flag Bikini Outfits ##
#########################

default ton_bra_bikini_1 = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1", ["#ffffffff", "#ffffffff"])
default ton_bra_bikini_1_striped = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1_striped", ["#ffffffff", "#8b0000ff", "#ffffffff"])
default ton_bra_bikini_1_UK = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1_UK", ["#ffffffff", "#c8102eff", "#012169ff", "#ffffffff"])
default ton_bra_bikini_1_USA = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1_USA", ["#ffffffff", "#8b0000ff", "#0c63d8ff", "#ffffffff"])

default ton_panties_bikini_1 = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1", ["#ffffffff", "#ffffffff"])
default ton_panties_bikini_1_jock = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1_jock", ["#ffffffff"])
default ton_panties_bikini_1_striped = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1_striped", ["#ffffffff", "#8b0000ff"])
default ton_panties_bikini_1_UK = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1_UK", ["#ffffffff", "#c8102eff", "#012169ff"])

default ton_outfit_bikini_1 = DollOutfit([ton_hair_base, ton_bra_bikini_1, ton_panties_bikini_1], price=250, name="Simple Bikini Set", desc="It ain't much, but it at least covers the important bits.")
default ton_outfit_bikini_2 = DollOutfit([ton_hair_base, ton_bra_bikini_1_striped, ton_panties_bikini_1_striped], price=250, name="Striped Bikini Set", desc="It ain't much, but it at least covers the important bits. Did I mention the stripes?")
default ton_outfit_bikini_3 = DollOutfit([ton_hair_base, ton_bra_bikini_1_UK, ton_panties_bikini_1_UK], price=250, name="\"For The Queen!\" Bikini Set", desc="This is the way.")
default ton_outfit_bikini_4 = DollOutfit([ton_hair_base, ton_bra_bikini_1_USA, ton_panties_bikini_1_jock], price=250, name="American Bikini Set", desc="Fuck yeah!")

#############################
## Skimpy Swimsuit Outfits ##
#############################

default ton_swimsuit_1 = DollCloth("tonks", ("upper body", "one-piece suits"), "top", "swimsuit_1", ["#c52a6eff"], zorder=183, level=40)
default ton_swimsuit_1_striped = DollCloth("tonks", ("upper body", "one-piece suits"), "top", "swimsuit_1_striped", ["#fff5e7ff", "#a80000ff"], zorder=183, level=40)
default ton_swimsuit_1_USA = DollCloth("tonks", ("upper body", "one-piece suits"), "top", "swimsuit_1_USA", ["#ffffffff", "#a80000ff", "#0c40d8ff", "#ffffffff"], zorder=183, level=40)

default ton_outfit_swimsuit_1 = DollOutfit([ton_hair_base, ton_swimsuit_1], price=260, name="Skimpy Swimsuit", desc="Disclaimer: Translucent swimsuits should not be worn in merman inhabited waters under any circumstance.")
default ton_outfit_swimsuit_2 = DollOutfit([ton_hair_base, ton_swimsuit_1_striped], price=260, name="Striped Skimpy Swimsuit", desc="A Translucent swimsuit with vertical stripes to make you look even thinner! Or maybe it's the other way around...")
default ton_outfit_swimsuit_3 = DollOutfit([ton_hair_base, ton_swimsuit_1_USA], price=260, name="Freedom Swimsuit", desc="May attract eagles.")

##################
## Santa Outfit ## #unlocked in genies_christmas_wish mirror story
##################

default ton_bra_santa = DollCloth("tonks", ("upper undergarment", "bras"), "bra", "santa_bra", ["#a13730ff"])
default ton_top_santa = DollCloth("tonks", ("upper body", "shirts"), "top", "santa_top", ["#a13730ff", "#ffffffff"])
default ton_panties_santa = DollCloth("tonks", ("lower undergarment", "panties"), "panties", "santa_panties", ["#a13730ff"])

default ton_outfit_santa = DollOutfit([ton_hair_base, ton_panties_santa, ton_top_santa, ton_bra_santa])

################# ~*~Ä~*~*~*~*~ #################
## Xmas Stuff ###   /%\  ___$__ ### Elf Outfit ##
#################  /% \ |=I~I=| #################

# Accessories
default ton_makeup_elf_ears = DollCloth("tonks", ("head", "makeup"), "makeup", "elf_ears", None)
default ton_hat_antlers = DollClothDynamic("tonks", ("head", "headgear"), "headgear", "antlers", ["#eabbaaff"], tracking="?hair")
default ton_hat_elf = DollClothDynamic("tonks", ("head", "headgear"), "headgear", "elf", ["#027447ff", "#ffeff8ff"], tracking="?hair")
default ton_neckwear_choker1 = DollCloth("tonks", ("head", "neckwear"), "neckwear", "choker_1", ["#ff2b95ff"])
default ton_neckwear_bell1 = DollCloth("tonks", ("head", "neckwear"), "neckwear", "bell_1", ["#027447ff", "#f4b552ff"], zorder=213)
default ton_accessory_bells = DollCloth("tonks", ("misc", "accessory"), "accessory", "bells_1", ["#f4b552ff"], zorder=213)
default ton_accessory_belt1 = DollCloth("tonks", ("misc", "accessory"), "accessory", "belt_1", ["#2a2a2aff", "#b98749ff"], zorder=213)
default ton_earring_bells = DollCloth("tonks", ("head", "earrings"), "earrings", "bells", ["#f4b552ff"])
default ton_piercing_nipple_bells = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "nipple_bells", ["#f4b552ff"])
# Main Clothing
default ton_top_elf = DollCloth("tonks", ("upper body", "dresses"), "top", "elf_dress",["#027447ff"])
default ton_bra_ribbon = DollCloth("tonks", ("upper undergarment", "other"), "bra", "ribbon", ["#ff2b95ff"], blacklist=["top", "piercing"])
default ton_panties_ribbon = DollCloth("tonks", ("lower undergarment", "other"), "panties", "ribbon", ["#ff2b95ff"], blacklist=["bottom"])
default ton_bra_pasties = DollCloth("tonks", ("upper undergarment", "other"), "bra", "pasties_1",["#ff2b95ff"], unlocked=True)
default ton_bra_pasties2 = DollCloth("tonks", ("upper undergarment", "other"), "bra", "pasties_2",["#027447ff", "#f4b552ff"])
default ton_bottom_xmas = DollCloth("tonks", ("lower body", "other"), "bottom", "xmas",["#027447ff", "#ffeff8ff"])
default ton_gloves_xmas = DollCloth("tonks", ("upper body", "gloves"), "gloves", "xmas", ["#ffeff8ff"])
default ton_stockings_xmas = DollCloth("tonks", ("legwear", "stockings"), "stockings", "xmas",["#ffffffff", "#ffffff78"])

default ton_stockings_long_striped = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_striped",["#ffe9f6ff", "#b41224ff"])
default ton_garterbelt_long_basic = DollCloth("tonks", ("legwear", "garterbelts"), "garterbelt", "long_basic_1", ["#ffffffff"])

default ton_outfit_elf = DollOutfit([ton_hair_base, ton_makeup_elf_ears, ton_earring_bells, ton_hat_elf, ton_neckwear_bell1, ton_top_elf, ton_accessory_belt1, ton_accessory_bells, ton_garterbelt_long_basic, ton_stockings_long_striped])
default ton_outfit_ribbon = DollOutfit([ton_hair_base, ton_neckwear_choker1, ton_bra_ribbon, ton_panties_ribbon])
default ton_outfit_xmas = DollOutfit([ton_hair_base, ton_hat_antlers, ton_earring_bells, ton_neckwear_bell1, ton_bra_pasties2, ton_bottom_xmas, ton_gloves_xmas, ton_stockings_xmas], addons=[ton_piercing_nipple_bells, ton_bra_pasties2])

#############################
## Stockings & Garterbelts ##
#############################

default ton_stockings_long = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_basic_1",["#ffffffff"], unlocked=True)
default ton_stockings_long_sports = DollCloth("tonks", ("legwear", "stockings"), "stockings", "long_sports",["#ffffffff", "#171717ff"], unlocked=True)

################
## Pubic Hair ##
################

default ton_pubes_arrow = DollCloth("tonks", ("lower undergarment", "pubes"), "pubes", "arrow", ["#ff92b9ff"], unlocked=True)
default ton_pubes_beaver = DollCloth("tonks", ("lower undergarment", "pubes"), "pubes", "beaver", ["#ff92b9ff"], unlocked=True)
default ton_pubes_stuble = DollCloth("tonks", ("lower undergarment", "pubes"), "pubes", "stuble", ["#844059ff"], unlocked=True)
default ton_pubes_unshaved = DollCloth("tonks", ("lower undergarment", "pubes"), "pubes", "unshaved", ["#844059ff"], unlocked=True)

# Lipstick
default ton_makeup_lipstick = DollMakeup("tonks", ("head", "makeup"), "makeup", "lipstick", ["#ff4646ff"], unlocked=True, tracking="mouth")

##########
## Misc ##
##########

default ton_top_corset = DollCloth("tonks", ("upper body", "other"), "top", "corset",["#f7ce92ff"], blacklist=["bra", "piercing"], unlocked=True)
default ton_bottoms_jeans = DollCloth("tonks", ("lower body", "trousers"), "bottom", "jeans",["#336869ff"], unlocked=True)
default ton_panties_base = DollCloth("tonks", ("lower undergarment", "bikini panties"), "panties", "base",["#e4faffff", "#e43714ff"], unlocked=True)
default ton_bra_base = DollCloth("tonks", ("upper undergarment", "bikini bras"), "bra", "bikini",["#e4faffff", "#e43714ff"], unlocked=True)
default ton_ruffled_top = DollCloth("tonks", ("upper body", "shirts"), "top", "ruffled_top",["#d5addbff"], level=25, unlocked=True)

default ton_earring_cartilege = DollCloth("tonks", ("head", "earrings"), "earrings", "cartilege", ["#a19f9fff"], unlocked=True)
default ton_earring_hoops = DollCloth("tonks", ("head", "earrings"), "earrings", "hoops", ["#a19f9fff"], unlocked=True)
default ton_earring_industrial = DollCloth("tonks", ("head", "earrings"), "earrings", "industrial", ["#a19f9fff"], unlocked=True)

default ton_piercing_clit_stud = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "clit_stud", ["#a19f9fff"], unlocked=True)
default ton_piercing_nipple_stud = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "nipple_stud", ["#a19f9fff"], unlocked=True)
default ton_piercing_nipple_rings = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "nipple_rings", ["#a19f9fff"], unlocked=True)
default ton_piercing_nipple_rings2 = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "nipple_rings2", ["#a19f9fff"], unlocked=True)
default ton_piercing_nipple_rings3 = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "nipple_rings3", ["#a19f9fff"], unlocked=True)

default ton_piercing_belly_stud = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "belly_stud", ["#a19f9fff"], unlocked=True)
default ton_piercing_belly_heart = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "belly_heart", ["#a19f9fff"], unlocked=True)
default ton_piercing_belly_dick = DollCloth("tonks", ("piercings & tattoos", "piercings"), "piercing", "belly_dick", ["#a19f9fff"], unlocked=True)
