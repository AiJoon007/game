###############
## Character ##
###############

default hermione = Doll(name="hermione")

default her_frame_default = DollBodypart("hermione", ("hidden", "frame"), "frame", "default")
default her_body_default = DollOutfit([her_frame_default], hidden=True)

##########
## Hair ##
##########

default her_hair_base = DollCloth("hermione", ("head", "hair"), "hair", "base", ["#985930ff", "#c38959ff", "#e68d20ff"], unlocked=True)

#######################
## Schoolgirl Outfit ##
#######################

default her_top_school1 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_1", ["#b7b7b8ff", "#6d6979ff", "#a74d2aff", "#edb30eff"], unlocked=True)
default her_top_school2 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_2", ["#b7b7b8ff", "#6d6979ff", "#a74d2aff", "#edb30eff"], unlocked=True)
default her_top_school3 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_3", ["#b7b7b8ff", "#a74d2aff", "#edb30eff"], unlocked=True)
default her_top_school4 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_4", ["#b7b7b8ff", "#a74d2aff", "#edb30eff"], unlocked=True, level=4)
default her_top_school5 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_5", ["#b7b7b8ff", "#a74d2aff", "#edb30eff"], unlocked=True, level=10)
default her_top_school6 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_6", ["#6d6979ff", "#a74d2aff", "#edb30eff"], unlocked=True, level=10)
default her_top_school7 = DollCloth("hermione", ("upper body", "shirts"), "top", "top_school_7", ["#b7b7b8ff", "#a74d2aff", "#edb30eff"], unlocked=True, level=13)

default her_bottom_school1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "school_skirt_1", ["#675a6cff", "#e8b10dff"], unlocked=True)
default her_bottom_school2 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "school_skirt_2", ["#675a6cff", "#e8b10dff"], unlocked=True, level=4)
default her_bottom_school3 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "school_skirt_3", ["#675a6cff", "#e8b10dff"], unlocked=True, level=10)
default her_bottom_school4 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "school_skirt_4", ["#675a6cff", "#e8b10dff"], unlocked=True, level=19)

default her_stockings_base1 = DollCloth("hermione", ("legwear", "socks"), "stockings", "stockings_1", ["#dba50dff", "#923f1eff"], unlocked=True)

default her_panties_base1 = DollCloth("hermione", ("lower undergarment", "panties"), "panties", "basic_panties_1", ["#e8e8e8ff", "#ca3c01ff"], unlocked=True)
default her_bra_base1 = DollCloth("hermione", ("upper undergarment", "bras"), "bra", "basic_bra_1", ["#e8e8e8ff", "#ca3c01ff"], unlocked=True)

default her_robe_school_1 = DollCloth("hermione", ("upper body", "robes"), "robe", "robe_school_1", ["#606060ff", "#ceced1ff", "#a74d2aff"], unlocked=True, level=0)
default her_robe_school_2 = DollCloth("hermione", ("upper body", "robes"), "robe", "robe_school_2", ["#606060ff", "#ceced1ff", "#a74d2aff"], unlocked=True, level=4)
default her_robe_school_3 = DollCloth("hermione", ("upper body", "robes"), "robe", "robe_school_3", ["#606060ff", "#ceced1ff", "#a74d2aff"], unlocked=True, level=10)
default her_robe_school_4 = DollCloth("hermione", ("upper body", "robes"), "robe", "robe_school_4", ["#606060ff", "#ceced1ff", "#a74d2aff"], unlocked=True, level=13)

default her_outfit_default = DollOutfit([her_hair_base, her_top_school1, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], unlocked=True)
default her_outfit_default_no_vest = DollOutfit([her_hair_base, her_top_school3, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], hidden=True)
default her_outfit_default_no_tie_open_shirt = DollOutfit([her_hair_base, her_top_school5, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], hidden=True)
default her_outfit_last = DollOutfit([her_hair_base], hidden=True)

#######################
## Slutty Schoolgirl ##
#######################

default her_top_slutty1 = DollCloth("hermione", ("upper body", "sweaters"), "top", "open_top_1", ["#b7b7b8ff", "#6d6979ff", "#a74d2aff", "#edb30eff"], level=19)
default her_bottom_slutty1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "open_skirt_1", ["#675a6cff"], level=19)
default her_stockings_slutty = DollCloth("hermione", ("legwear", "stockings"), "stockings", "stockings_2", ["#aaaaaaff"], level=4)

default her_outfit_slutty_schoolgirl = DollOutfit([her_hair_base, her_top_slutty1, her_bottom_slutty1, her_stockings_slutty], price=500, name="Slutty Schoolgirl Outfit", desc="An arguably better version of the regular school outfit.")

########################
## Rave Bikini Outfit ##
########################

default her_panties_bikini1 = DollCloth("hermione", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_1", ["#8a0000ff", "#fc8700ff"], level=18)
default her_bra_bikini1 = DollCloth("hermione", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_1", ["#8a0000ff", "#fc8700ff"], level=18)

default her_outfit_bikini1 = DollOutfit([her_hair_base, her_panties_bikini1, her_bra_bikini1], price=350, name="Rave Bikini Set", desc="A Bunch of straps for a bunch of gold!")

###########################
## Leather Bikini Outfit ##
###########################

default her_panties_bikini2 = DollCloth("hermione", ("lower undergarment", "bikini panties"), "panties", "bikini_panties_2", ["#373737ff", "#c58e23ff"], level=16)
default her_bra_bikini2 = DollCloth("hermione", ("upper undergarment", "bikini bras"), "bra", "bikini_bra_2", ["#373737ff", "#c58e23ff"], level=16)

default her_outfit_bikini2 = DollOutfit([her_hair_base, her_panties_bikini2, her_bra_bikini2], price=350, name="Leathered Bikini Set", desc="Emits a slight squeaking sound when rubbed.")

#########################
## Sling Bikini Outfit ##
#########################
default her_panties_bikini3 = DollCloth("hermione", ("lower undergarment", "bikini panties"), "panties", "sling_panties", ["#3045a4ff", "#d4a420ff"], level=17)
default her_bra_bikini3 = DollCloth("hermione", ("upper undergarment", "bikini bras"), "bra", "sling_bra", ["#3045a4ff", "#d4a420ff"], level=17)

default her_outfit_bikini3 = DollOutfit([her_hair_base, her_panties_bikini3, her_bra_bikini3], price=350, name="Sling Bikini Set", desc="Slingshot your dignity with one simple trick.")

#################
## Maid Outfit ##
#################

default her_top_maid1 = DollCloth("hermione", ("upper body", "dresses"), "top", "maid_dress_1", ["#28333dff", "#ecf3f4ff", "#353f54ff"], level=4)
default her_stockings_maid1 = DollCloth("hermione", ("legwear", "socks"), "stockings", "maid_stockings_1", ["#35211eff"], level=4)
default her_hat_maid1 = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "maid_hat_1", ["#ecf3f4ff"], level=4, tracking="?hair")
default her_neckwear_maid1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "maid_choker_1", ["#28333dff", "#ecf3f4ff"], level=4)
default her_neckwear_maid2 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "maid_choker_2", ["#ecf3f4ff"], level=4)
default her_gloves_maid1 = DollCloth("hermione", ("upper body", "gloves"), "gloves", "maid_gloves_1", ["#28333dff", "#ecf3f4ff", "#353f54ff"], level=4)

default her_outfit_maid = DollOutfit([her_hair_base, her_top_maid1, her_stockings_maid1, her_hat_maid1, her_neckwear_maid1, her_gloves_maid1, her_panties_base1, her_bra_base1], addons=[her_neckwear_maid2], price=450, name="French Maid Costume", desc="A classic Maid Outfit for a classy Witch.")

##################
## Poker Outfit ## # Unlockable with Tokens only
##################

default her_hat_poker1 = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "poker_hat_1", ["#1a1a23ff", "#e8e8e8ff", "#99160aff"], level=4, tracking="?hair")
default her_hat_poker2 = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "poker_hat_2", ["#1a1a23ff", "#e8e8e8ff", "#99160aff"], level=4, tracking="?hair")
default her_neckwear_poker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "poker_bowtie_1", ["#e8e8e8ff", "#99160aff", "#ffb303ff"], level=4)
default her_stockings_poker1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "poker_stockings_1", ["#1a1a23ff", "#99160aff"], level=13)
default her_stockings_poker2 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "poker_stockings_2", ["#1a1a23ff", "#99160aff"], level=13)
default her_panties_poker1 = DollCloth("hermione", ("lower undergarment", "panties"), "panties", "poker_panties_1", ["#1a1a23ff", "#99160aff", "#ffb303ff"], level=19)
default her_bra_poker1 = DollCloth("hermione", ("upper undergarment", "other"), "bra", "poker_bra_1", ["#1a1a23ff", "#e8e8e8ff", "#99160aff", "#ffb303ff"], blacklist=["panties", "top", "bottom"], level=19)
default her_gloves_poker1 = DollCloth("hermione", ("upper body", "gloves"), "gloves", "poker_gloves_1", ["#e8e8e8ff", "#ffb303ff"], level=4)
default her_earring_poker1 = DollCloth("hermione", ("head", "earrings"), "earrings", "poker_earring_1", ["#ffb303ff"], level=4)
default her_piercing_poker1 = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "poker_belly_1", ["#1a1a23ff", "#e8e8e8ff", "#99160aff", "#ffb303ff"])

default her_outfit_poker = DollOutfit([her_hair_base, her_hat_poker1, her_hat_poker2, her_neckwear_poker1, her_stockings_poker1, her_stockings_poker2, her_panties_poker1, her_bra_poker1, her_gloves_poker1, her_earring_poker1, her_piercing_poker1], name="Poke-her-nips Costume", desc="An outfit that doesn't leave much for the mind's desire, perfect for a lewd card loving girl.")

##################
## Bunny Outfit ##
##################

default her_top_bunny1 = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "bunny_top_1", ["#303030ff"], blacklist=["panties", "bra"], zorder=183, level=19)
default her_top_bunny2 = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "bunny_top_2", ["#000000ff"], blacklist=["panties", "bra"], zorder=183, level=19)
default her_stockings_bunny1 = DollCloth("hermione", ("legwear", "pantyhose"), "stockings", "bunny_stockings_1", ["#515151ff"], level=19)
default her_tattoo_bunny1 = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "bunny_tattoo", ["#000001ff"])
default her_hat_bunny1 = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "bunny_hat_1", ["#303030ff", "#e8e8e8ff"], level=13, tracking="?hair")
default her_hat_bunny2 = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "bunny_hat_2", ["#b7a873ff", "#dba18cff", "#fdfdfdff"], level=13, tracking="?hair")
default her_gloves_bunny1 = DollCloth("hermione", ("upper body", "gloves"), "gloves", "bunny_gloves_1", ["#e8e8e8ff"], level=4)
default her_neckwear_bunny1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "bunny_bowtie_1", ["#e8e8e8ff", "#303030ff"], level=4)

default her_outfit_bunny = DollOutfit([her_hair_base, her_top_bunny2, her_stockings_bunny1, her_tattoo_bunny1, her_hat_bunny2, her_gloves_bunny1, her_neckwear_bunny1], addons=[her_top_bunny1, her_hat_bunny1], price=350, name="Sexy Bunny Costume", desc="What's up doc?")

######################
## Reindeer Costume ## #unlocked in genies_christmas_wish mirror story
######################

default her_hat_antlers2 = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "antlers_2", ["#994c30ff", "#ffffffff", "#c69f65ff"], level=12, tracking="?hair")
default her_neckwear_studded_choker = DollCloth("hermione", ("head", "neckwear"), "neckwear", "studded_choker", ["#2b2a32ff", "#d2cfe7ff"], level=16)
default her_top_bunny3 = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "bunny_top_3", ["#8a4b04ff"], blacklist=["panties", "bra"], zorder=183, level=19)
default her_accessory_mistletoe = DollCloth("hermione", ("misc", "accessory"), "accessory", "mistletoe", ["#c82000ff"], zorder=213, level=7)

default her_outfit_reindeer = DollOutfit([her_hair_base, her_top_bunny3, her_accessory_mistletoe, her_stockings_bunny1, her_neckwear_studded_choker, her_hat_antlers2])

################
## Ball Dress ##
################

default her_hair_updo = DollCloth("hermione", ("head", "hair"), "hair", "updo", ["#985930ff", "#c38959ff"])
default her_top_ball1 = DollCloth("hermione", ("upper body", "dresses"), "top", "ball_dress_1", ["#ff8caeff", "#f2daffff"], blacklist=["bottom"])
default her_earring_pearls1 = DollCloth("hermione", ("head", "earrings"), "earrings", "pearl_1", ["#e9a6fdff"], level=4)
default her_neckwear_pearls1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "ball_pearls_1", ["#e9a6fdff"], level=4)
default her_accessory_ball_sash1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "ball_sash", ["#f7dee7ff", "#a1529fff"], zorder=213, level=4)

default her_outfit_ball = DollOutfit([her_hair_updo, her_neckwear_pearls1, her_top_ball1, her_earring_pearls1, her_accessory_ball_sash1, her_panties_base1], price=0, name="Classy Ball Dress", desc="A fancy dress for a fancy witch.")

#####################
## Yennefer Outfit ##
#####################

default her_top_yen1 = DollCloth("hermione", ("upper body", "sweaters"), "top", "yen_top", ["#09202fff"], level=10)
default her_bottom_yen_skirt1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "yen_skirt", ["#1a1a1aff"], level=4)
default her_stockings_yen1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "yen_stockings", ["#4c4c4cff"], level=10)
default her_accessory_yen_sash1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "yen_sash", ["#191919ff", "#333333ff"], zorder=213, level=10)
default her_accessory_yen_belt1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "yen_belt", ["#34251fff", "#928e89ff"], zorder=214, level=4)
default her_accessory_yen_feathers1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "yen_feathers", ["#2abec7ff"], zorder=215, level=4)
default her_accessory_yen_scarf1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "yen_scarf", ["#09202fff"], zorder=216, level=4)
default her_accessory_yen_corset1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "yen_corset", ["#251b1bff", "#130e0bff"], zorder=212, level=10)
default her_neckwear_yen_choker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "yen_choker", ["#1e1d1cff"], level=4)
default her_gloves_yen1 = DollCloth("hermione", ("upper body", "gloves"), "gloves", "yen_gloves", ["#34251fff"], level=4)

default her_outfit_yennefer = DollOutfit([her_hair_base, her_top_yen1, her_bottom_yen_skirt1, her_accessory_yen_sash1, her_stockings_yen1, her_accessory_yen_feathers1, her_accessory_yen_scarf1, her_neckwear_yen_choker1, her_gloves_yen1, her_accessory_yen_corset1, her_accessory_yen_belt1], price=400, name="Yennefer Costume", desc="An outfit that smells of lilac and gooseberries.")

#######################
## Pizza Slut Outfit ## #Unlocked in eating_for_pleasure mirror story
#######################

default her_top_pizza = DollCloth("hermione", ("upper body", "other"), "top", "pizza_top", ["#b4320aff"], level=19)
default her_bottom_pizza = DollCloth("hermione", ("lower body", "skirts"), "bottom", "pizza_skirt", ["#b4320aff", "#ebc72cff"], level=4)
default her_panties_pizza = DollCloth("hermione", ("lower undergarment", "other"), "panties", "pizza_panties", ["#b4320aff"], level=19)

default her_outfit_pizza = DollOutfit([her_hair_base, her_bottom_pizza, her_top_pizza, her_panties_pizza], price=0)

#####################
## Bioshock Outfit ##
#####################

default her_hair_bioshock = DollCloth("hermione", ("head", "hair"), "hair", "bio_hair", ["#1f1d1bff", "#363230ff"], level=4)
default her_neckwear_bioshock = DollCloth("hermione", ("head", "neckwear"), "neckwear", "bioshock_choker", ["#0c0148ff"], level=4)
default her_top_bioshock = DollCloth("hermione", ("upper body", "other"), "top", "bioshock_corset", ["#e1e0e8ff", "#2e2e30ff", "#e8e8e8ff"], level=4)
default her_bottom_bioshock = DollCloth("hermione", ("lower body", "skirts"), "bottom", "bioshock_skirt", ["#0c0148ff"], level=4)
default her_robe_bioshock = DollCloth("hermione", ("upper body", "robes"), "robe", "bioshock_robe", ["#0c0148ff", "#e8e8e8ff"], level=4)

default her_outfit_bioshock = DollOutfit([her_hair_bioshock, her_robe_bioshock, her_bottom_bioshock, her_top_bioshock, her_neckwear_bioshock, her_panties_base1], price=400, name="Elizabeth Costume", desc="Flick some coins for this shockingly inspirational outfit.")

##############
## Swimsuit ##
##############

default her_top_swimsuit_1 = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "swimsuit_top_1", ["#161b30ff", "#e0c610ff"], blacklist=["panties", "bra"], zorder=183, level=13)

default her_outfit_swimsuit = DollOutfit([her_hair_base, her_top_swimsuit_1], price=350, name="One-piece Swimsuit", desc="A swimsuit for witches whom love getting wet.")

#####################
## Egyptian Outfit ##
#####################

default her_top_egypt = DollCloth("hermione", ("upper body", "other"), "top", "egypt_top", ["#f0edfaff"], blacklist=["bra"], level=19)
default her_bottom_egypt = DollCloth("hermione", ("lower body", "other"), "bottom", "egypt_loincloth", ["#f0edfaff", "#e3b665ff", "#2f97ffff"], blacklist=["panties"], level=13)
default her_gloves_egypt = DollCloth("hermione", ("upper body", "gloves"), "gloves", "egypt_armband", ["#e3b665ff"], level=4)
default her_neckwear_egypt = DollCloth("hermione", ("head", "neckwear"), "neckwear", "egypt_neck", ["#e3b665ff", "#5ed1ecff", "#2f97ffff"], level=4)

default her_outfit_egypt = DollOutfit([her_hair_base, her_neckwear_egypt, her_top_egypt, her_bottom_egypt, her_gloves_egypt], price=400, name="Cleopatra Costume", desc="Become the Cleopatra of your times!")

########################
## Latex dress Outfit ##
########################

default her_top_latex_dress_1 = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "latex_dress_1", ["#fa8bf1ff", "#ffad16ff"], blacklist=["bra"], level=19)

default her_outfit_latex_dress = DollOutfit([her_hair_base, her_top_latex_dress_1], price=350, name="Latex Dress", desc="Something you wouldn't normally find in a regular clothing store.")

###################
## Pajama Outfit ## #Unlocked in Luna Intro
###################

default her_top_pajama = DollCloth("hermione", ("upper body", "shirts"), "top", "pajama_1", ["#e4d8c1ff"])
default her_bottom_pajama = DollCloth("hermione", ("lower body", "trousers"), "bottom", "pajama_1", ["#9c8a74ff", "#e4cb99ff", "#e4d8c1ff"])
default her_bottom_pajama2 = DollCloth("hermione", ("lower body", "trousers"), "bottom", "pajama_2", ["#9c8a74ff", "#e4cb99ff"])

default her_outfit_pajama = DollOutfit([her_hair_base, her_top_pajama, her_bottom_pajama], addons=[her_bottom_pajama2])

####################
## Nightie Outfit ##
####################

default her_top_nightie = DollCloth("hermione", ("upper body", "shirts"), "top", "nightie", ["#ffacb8d7"], level=13)

default her_outfit_nightie = DollOutfit([her_hair_base, her_top_nightie], price=350, name="Nightie", desc="Comfortable alternative for a pyjamas.")

##################
## Teddy Outfit ##
##################

default her_top_teddy = DollCloth("hermione", ("upper body", "shirts"), "top", "teddy_top", ["#141414d7", "#9490a3d7", "#9490a3d7"], level=16)

default her_outfit_teddy = DollOutfit([her_hair_base, her_top_teddy], price=350, name="Teddy Nightie", desc="A more airy nightdress leaving not much fabric between you and your bed.")

#################
## Tifa Outfit ##
#################

default her_top_tifa = DollCloth("hermione", ("upper body", "shirts"), "top", "tifa_top", ["#e8e8e8ff"], level=10)
default her_accessory_tifa_belt = DollCloth("hermione", ("misc", "accessory"), "accessory", "tifa_belt", ["#323232ff", "#9a9a9aff"], zorder=192, level=4)
default her_accessory_tifa_suspenders = DollCloth("hermione", ("misc", "accessory"), "accessory", "tifa_suspenders", ["#563d43ff", "#9a9a9aff"], zorder=213, level=4)
default her_gloves_tifa = DollCloth("hermione", ("upper body", "gloves"), "gloves", "tifa_gloves", ["#483f46ff", "#e46b62ff", "#7d787fff", "#bda79eff"], level=4)
default her_bottom_tifa = DollCloth("hermione", ("lower body", "skirts"), "bottom", "tifa_skirt", ["#483f46ff"], level=10)

default her_outfit_tifa = DollOutfit([her_hair_base, her_top_tifa, her_accessory_tifa_belt, her_accessory_tifa_suspenders, her_gloves_tifa, her_bottom_tifa, her_panties_base1], price=400, name="Tifa Costume", desc="An outfit for when your sexual fantasies are just getting started.")

#######################
## Ms. Marvel Outfit ##
#######################

default her_top_msmarv = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "msmarv_suit", ["#404663ff", "#7b88b5ff", "#ffec86ff"], zorder=183, blacklist=["panties", "bra"], level=10)
default her_accessory_msmarv_ribbon = DollCloth("hermione", ("misc", "accessory"), "accessory", "msmarv_ribbon", ["#ce2916ff"], zorder=212, level=4)
default her_gloves_msmarv = DollCloth("hermione", ("upper body", "gloves"), "gloves", "msmarv_gloves", ["#404663ff", "#7b88b5ff"], level=4)
default her_stockings_msmarv = DollCloth("hermione", ("legwear", "stockings"), "stockings", "msmarv_stockings", ["#404663ff", "#7b88b5ff"], level=10)

default her_outfit_msmarv = DollOutfit([her_hair_base, her_top_msmarv, her_accessory_msmarv_ribbon, her_gloves_msmarv, her_stockings_msmarv], price=400, name="Miss Marvel Costume", desc="For the girl that likes the lightning bolt better on her chest than her forehead.")

#######################
## Heart Slut Outfit ##
#######################

default her_earring_hslut = DollCloth("hermione", ("head", "earrings"), "earrings", "hslut_earring", ["#e25f5fff"], level=4)
default her_neckwear_hslut = DollCloth("hermione", ("head", "neckwear"), "neckwear", "hslut_choker", ["#f2f2f2ff", "#e25f5fff"], level=10)
default her_top_hslut = DollCloth("hermione", ("upper body", "other"), "top", "hslut_top", ["#e25f5fff", "#f2f2f2ff"], level=19)
default her_gloves_hslut = DollCloth("hermione", ("upper body", "gloves"), "gloves", "hslut_gloves", ["#f2f2f2ff"], level=10)
default her_stockings_hslut = DollCloth("hermione", ("legwear", "stockings"), "stockings", "hslut_socks", ["#f2f2f2ff"], level=10)
default her_bra_hslut = DollCloth("hermione", ("upper undergarment", "other"), "bra", "hslut_pasties", ["#e25f5fff", "#e25f5fff"], level=19)
default her_panties_hslut = DollCloth("hermione", ("lower undergarment", "other"), "panties", "hslut_panties", ["#e25f5fff"], level=19)
default her_garterbelt_hslut = DollCloth("hermione", ("legwear", "garterbelts"), "garterbelt", "hslut_garter", ["#e25f5fff", "#f99494ff"], level=10)

default her_outfit_hslut = DollOutfit([her_hair_base, her_top_hslut, her_gloves_hslut, her_stockings_hslut, her_panties_hslut, her_bra_hslut, her_earring_hslut, her_neckwear_hslut, her_garterbelt_hslut], price=450, name="Hearty Harlot", desc="A sexy dancers outfit with heart-shaped nipple tassels.")

#######################
## Lora Craft Outfit ##
#######################

default her_accessory_croft_belt = DollCloth("hermione", ("misc", "accessory"), "accessory", "croft_belt", ["#6f5642ff", "#747b72ff", "#fcc004ff"], zorder=212, level=4)
default her_accessory_croft_suspenders = DollCloth("hermione", ("misc", "accessory"), "accessory", "croft_suspenders", ["#6f5642ff", "#747b72ff"], zorder=213, level=4)

default her_top_croft = DollCloth("hermione", ("upper body", "shirts"), "top", "croft_top", ["#a3c998ff"], level=10)
default her_bottom_croft = DollCloth("hermione", ("lower body", "shorts"), "bottom", "croft_shorts", ["#93723dff", "#898878ff", "#fcc004ff"],level=10)

default her_outfit_croft = DollOutfit([her_hair_base, her_top_croft, her_bottom_croft, her_accessory_croft_belt, her_accessory_croft_suspenders, her_panties_base1], price=400, name="Lora Craft Costume", desc="An outfit perfectly suited for exploring deep, dark and moist caverns.\n{size=-4}Disclaimer: This outfit has no association with a character known as Lara Croft. Totally.{/size}")

##################
## Witch Outfit ##
##################

default her_top_witch = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "witch_top", ["#473366ff", "#fcb470ff"], blacklist=["panties"], level=10)
default her_stockings_witch = DollCloth("hermione", ("legwear", "stockings"), "stockings", "witch_stockings", ["#473366ff", "#fcb470ff"], level=4)
default her_robe_witch = DollCloth("hermione", ("upper body", "robes"), "robe", "witch_cape", ["#473366ff", "#fcb470ff", "#24703aff"], level=4)

default her_outfit_witch = DollOutfit([her_hair_base, her_top_witch, her_stockings_witch, her_robe_witch], price=400, name="16th Century Witch Costume", desc="An ancient witch costume coming straight from 16th century. Stay away from the burning stakes!")

##################
## Latex Outfit ##
##################

default her_top_latex = DollCloth("hermione", ("upper body", "shirts"), "top", "latex_top", ["#373737ff"], level=19)
default her_neckwear_latex = DollCloth("hermione", ("head", "neckwear"), "neckwear", "latex_choker", ["#373737ff"], level=13)
default her_gloves_latex = DollCloth("hermione", ("upper body", "gloves"), "gloves", "latex_gloves", ["#373737ff"], level=13)
default her_stockings_latex = DollCloth("hermione", ("legwear", "stockings"), "stockings", "latex_stockings", ["#373737ff"], level=13)
default her_panties_latex = DollCloth("hermione", ("lower undergarment", "bikini panties"), "panties", "latex_panties", ["#373737ff"], level=19)

default her_outfit_latex = DollOutfit([her_hair_base, her_top_latex, her_gloves_latex, her_stockings_latex, her_panties_latex, her_neckwear_latex], price=350, name="Latex Set", desc="A tight fitting outfit that takes approximately twenty minutes to put on properly.")

####################
## Fishnet Outfit ##
####################

default her_top_fishnet = DollCloth("hermione", ("upper body", "other"), "top", "fishnet_top", ["#181818ff"], blacklist=["bra"], level=19)
default her_panties_fishnet = DollCloth("hermione", ("lower undergarment", "other"), "panties", "fishnet_panties", ["#181818ff"], level=19)

default her_outfit_fishnet = DollOutfit([her_hair_base, her_top_fishnet, her_panties_fishnet], price=350, name="Fishnet Set", desc="Disclaimer: Not suitable for actual fish catching.")

##############################
## Fishnet One-piece Outfit ##
##############################

default her_top_fishnet_onepiece = DollCloth("hermione", ("upper body", "one-piece suits"), "top", "fishnet_onepiece", ["#000000ff", "#000000ff"], blacklist=["panties", "bra"], zorder=183, level=19)
default her_stockings_short_meshed = DollCloth("hermione", ("legwear", "socks"), "stockings", "short_meshed", ["#000000ff", "#000000ff"], level=13)

default her_outfit_fishnet_onepiece = DollOutfit([her_hair_base, her_top_fishnet_onepiece, her_stockings_short_meshed], price=350, name="Fishnet One-piece", desc="Perfect for containing your daily catch.")

###################
## Winter Outfit ##
###################

default her_top_pullover_1 = DollCloth("hermione", ("upper body", "sweaters"), "top", "pullover_1", ["#ff7bcfff"], unlocked=True)
default her_top_pullover_2 = DollCloth("hermione", ("upper body", "sweaters"), "top", "pullover_2", ["#ff7bcfff"], unlocked=True, level=8)
default her_top_pullover_3 = DollCloth("hermione", ("upper body", "sweaters"), "top", "pullover_3", ["#ff7bcfff"], unlocked=True, level=16)
default her_stockings_pantyhose_1= DollCloth("hermione", ("legwear", "pantyhose"), "stockings", "pantyhose_1", ["#b19083ff"], unlocked=True, level=4)
default her_stockings_pantyhose_2= DollCloth("hermione", ("legwear", "pantyhose"), "stockings", "pantyhose_2", ["#b19083ff"], unlocked=True, level=10)
default her_stockings_pantyhose_3= DollCloth("hermione", ("legwear", "pantyhose"), "stockings", "pantyhose_3", ["#b19083ff"], unlocked=True, level=19)

###################
## Spring Outfit ##
###################

default her_top_ruffled = DollCloth("hermione", ("upper body", "shirts"), "top", "ruffled_top", ["#ebdfa3ff"], unlocked=True, level=4)
default her_bottom_jeans = DollCloth("hermione", ("lower body", "trousers"), "bottom", "jeans_1", ["#405758ff", "#ae5d0bff", "#9b8e82ff"], unlocked=True)

###################
## Casual Outfit ##
###################

default her_top_casual1 = DollCloth("hermione", ("upper body", "sweaters"), "top", "casual_top_1", ["#741230ff", "#3c6f42ff"], unlocked=True)
default her_top_casual2 = DollCloth("hermione", ("upper body", "sweaters"), "top", "casual_top_2", ["#741230ff"], unlocked=True, level=6)

#########################
## Cheerleader Outfits ##
#########################

default her_top_cheerleader1 = DollCloth("hermione", ("upper body", "shirts"), "top", "cheerleader_top_1", ["#fbfbfbff", "#a74d2aff", "#edb30eff"], level=10)
default her_top_cheerleader2 = DollCloth("hermione", ("upper body", "other"), "top", "cheerleader_top_2", ["#a74d2aff", "#edb30eff"], level=16)

default her_bottom_cheerleader1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "cheerleader_skirt_1", ["#fbfbfbff", "#a74d2aff", "#edb30eff"], level=10)
default her_bottom_cheerleader2 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "cheerleader_skirt_2", ["#e8e8e8ff", "#a74d2aff", "#edb30eff"], level=14)

default her_gloves_cheerleader = DollCloth("hermione", ("upper body", "gloves"), "gloves", "cheerleader_armband", ["#a74d2aff", "#edb30eff"])

default her_outfit_cheerleader_1 = DollOutfit([her_hair_base, her_top_cheerleader1, her_bottom_cheerleader1, her_gloves_cheerleader, her_panties_base1, her_bra_base1], price=450, name="Gryffindor Cheerleader Uniform", desc="So daring and bold, sporting red and gold!")
default her_outfit_cheerleader_2 = DollOutfit([her_hair_base, her_top_cheerleader2, her_bottom_cheerleader2, her_panties_base1, her_bra_base1], price=650, name="Gryffindor Cheerleader Plus Uniform", desc="For when your teammates need an extra push.")

################# ~*~Ä~*~*~*~*~ #################
## Xmas Stuff ###   /%\  ___&__ ###  Ho Ho Ho  ##
#################  /% \ |=I~I=| #################

default her_hat_antlers = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "antlers", ["#eabbaaff"], level=8, tracking="?hair")
default her_hat_elf = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "elf", ["#e5000aff", "#ffeff8ff"], level=8, tracking="?hair")
default her_neckwear_choker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "choker_1", ["#e5000aff"], level=4)
default her_neckwear_bell1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "bell_1", ["#e5000aff", "#f4b552ff"], zorder=213, level=10)

default her_bra_ribbon = DollCloth("hermione", ("upper undergarment", "other"), "bra", "ribbon", ["#e5000aff"], blacklist=["top"], level=18)
default her_panties_ribbon = DollCloth("hermione", ("lower undergarment", "other"), "panties", "ribbon", ["#e5000aff"], blacklist=["bottom"], level=18)

default her_top_xmas = DollCloth("hermione", ("upper body", "other"), "top", "xmas",["#e5000aff", "#ffeff8ff", "#6dc265ff"], level=13)
default her_bottom_xmas = DollCloth("hermione", ("lower body", "other"), "bottom", "xmas",["#e5000aff", "#ffeff8ff"], level=13)
default her_gloves_xmas = DollCloth("hermione", ("upper body", "gloves"), "gloves", "xmas", ["#ffeff8ff"])
default her_stockings_xmas = DollCloth("hermione", ("legwear", "stockings"), "stockings", "xmas",["#ffffffff", "#ffffffff"], level=10)

default her_outfit_ribbon = DollOutfit([her_hair_base, her_neckwear_choker1, her_bra_ribbon, her_panties_ribbon])
default her_outfit_xmas   = DollOutfit([her_hair_base, her_hat_antlers, her_neckwear_bell1, her_top_xmas, her_bottom_xmas, her_gloves_xmas, her_stockings_xmas, her_panties_base1], addons=[her_hat_elf])

############################
## Wrestling Robes Outfit ## #Unlocked in a_white_christmas mirror story
############################

default her_robe_wrestling = DollCloth("hermione", ("upper body", "robes"), "robe", "wrestling_robe", ["#a63f1dff", "#fffdedff"], level=3)
default her_bra_sports = DollCloth("hermione", ("upper undergarment", "bras"), "bra", "sports_bra", ["#424764ff", "#f2f4ffff"], level=3)
default her_panties_sports = DollCloth("hermione", ("lower undergarment", "panties"), "panties", "sports_panties", ["#424764ff", "#f2f4ffff"], level=3)
default her_accessory_belt_wrestling = DollCloth("hermione", ("misc", "accessory"), "accessory", "wrestling_belt", ["#3c475bff", "#f0fb75ff"], zorder=192, level=3)

default her_outfit_wrestling = DollOutfit([her_hair_base, her_robe_wrestling, her_bra_sports, her_panties_sports, her_accessory_belt_wrestling])

############################
## Blueballing Bad Outfit ## #Unlocked in blueballing_bad mirror story
############################

default her_accessory_bb_tie = DollCloth("hermione", ("misc", "accessory"), "accessory", "bb_tie", ["#b1339fff", "#f62800ff", "#fff700ff"], zorder=152)
default her_tattoo_bb_tattoo = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "bb_tattoo", ["#000000ff", "#fff700ff", "#f62800ff"])

default her_outfit_bb = DollOutfit([her_hair_base, her_accessory_bb_tie, her_tattoo_bb_tattoo])

#################
## Accessories ##
#################

default her_accessory_house_emblem = DollCloth("hermione", ("misc", "accessory"), "accessory", "house_emblem", ["#a74d2aff", "#edb30eff"], zorder=212, unlocked=True)

default her_accessory_reading_glasses = DollCloth("hermione", ("head", "glasses"), "glasses", "reading_glasses", ["#f0f0f1ff"], unlocked=True)
default her_accessory_vintage_glasses = DollCloth("hermione", ("head", "glasses"), "glasses", "vintage_glasses", ["#ffffff32", "#242424ff", "#747474ff"], unlocked=True)

#############
## Tattoos ##
#############

# Pelvis/crotch (Slot 0)
default her_tattoo_10g = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "10g_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_cockhole = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "cockhole_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_cumhere = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "cumhere_tattoo1", ["#000000ff"], unlocked=True)
default her_tattoo_cumslut = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "cumslut_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_cunt = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "cunt_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_deatheater = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "deatheater_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_deposit = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "deposit_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_fuckme = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "fuckme_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_mudblood = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "mudblood_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_nocondom = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "nocondom_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_punkblood = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "punkblood_tattoo", ["#c0543aff", "#44bc40ff"], unlocked=True)
default her_tattoo_whore = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "whore_tattoo", ["#000000ff"], unlocked=True)
default her_tattoo_womb = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "womb_tattoo", ["#000000ff"], unlocked=True)

# Breasts/Nipples (Slot 1)
default her_tattoo_twist = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "twist_tattoo", ["#000000ff"], unlocked=True)

# Torso/chest (Slot 2)
default her_tattoo_cumhere2 = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "cumhere_tattoo2", ["#000000ff"], unlocked=True)

# Legs/Thighs (Slot 3)
default her_tattoo_lockhart = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "lockhart_tattoo", ["#464646ff"])
default her_tattoo_free = DollCloth("hermione", ("piercings & tattoos", "tattoos"), "tattoo", "free_tattoo", ["#000000ff"], unlocked=True)

############
## Makeup ##
############

# Face
default her_makeup_freckles1 = DollCloth("hermione", ("head", "makeup"), "makeup", "freckles1", ["#fd9d60ff"], unlocked=True)
default her_makeup_freckles2 = DollCloth("hermione", ("head", "makeup"), "makeup", "freckles2", ["#fd9d60ff"], unlocked=True)

# Breasts
default her_makeup_freckles3 = DollCloth("hermione", ("head", "makeup"), "makeup", "freckles3", ["#b97c51ff"], unlocked=True)

# Torso
default her_makeup_freckles4 = DollCloth("hermione", ("head", "makeup"), "makeup", "freckles4", ["#b97c51ff"], unlocked=True)

# Lipstick
default her_makeup_lipstick = DollMakeup("hermione", ("head", "makeup"), "makeup", "lipstick", ["#ff4646ff"], unlocked=True, tracking="mouth")

################
## Pubic Hair ##
################

default her_pubes_arrow = DollCloth("hermione", ("lower undergarment", "pubes"), "pubes", "arrow", ["#985930ff"], unlocked=True)
default her_pubes_beaver = DollCloth("hermione", ("lower undergarment", "pubes"), "pubes", "beaver", ["#985930ff"], unlocked=True)
default her_pubes_stuble = DollCloth("hermione", ("lower undergarment", "pubes"), "pubes", "stuble", ["#5c361dff"], unlocked=True)
default her_pubes_unshaved = DollCloth("hermione", ("lower undergarment", "pubes"), "pubes", "unshaved", ["#5c361dff"], unlocked=True)

###############
## Piercings ##
###############

default her_piercing_clit_stud = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "clit_stud", ["#a19f9fff"], unlocked=True)
default her_piercing_nipple_stud = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "nipple_stud", ["#a19f9fff"], unlocked=True)
default her_piercing_nipple_rings = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "nipple_rings", ["#a19f9fff"], unlocked=True)
default her_piercing_nipple_rings2 = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "nipple_rings2", ["#a19f9fff"], unlocked=True)
default her_piercing_nipple_rings3 = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "nipple_rings3", ["#a19f9fff"], unlocked=True)
default her_piercing_nipple_bells = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "nipple_bells", ["#f4b552ff"])

default her_piercing_belly_stud = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "belly_stud", ["#a19f9fff"], unlocked=True)
default her_piercing_belly_heart = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "belly_heart", ["#a19f9fff"], unlocked=True)
default her_piercing_belly_dick = DollCloth("hermione", ("piercings & tattoos", "piercings"), "piercing", "belly_dick", ["#a19f9fff"], unlocked=True)

##########
## MISC ##
##########

default her_accessory_gift_wrap = DollCloth("hermione", ("misc", "accessory"), "accessory", "leg_wrap", ["#a74d2aff", "#edb30eff"], zorder=183, unlocked=True, level=5)
default her_bra_bandaids = DollCloth("hermione", ("upper undergarment", "other"), "bra", "bandaids", ["#e9bb95ff"], unlocked=True, level=19)

### Default Schedules ###

default her_outfit_s_clearday = DollOutfit([her_hair_base, her_top_school3, her_bottom_school1, her_panties_base1, her_bra_base1], True, schedule={"day": True})
default her_outfit_s_clearnight = DollOutfit([her_hair_base, her_top_casual1, her_bottom_jeans, her_panties_base1, her_bra_base1], True, schedule={"night": True})
default her_outfit_s_snow = DollOutfit([her_hair_base, her_top_pullover_1, her_bottom_jeans, her_panties_base1, her_bra_base1], True, schedule={"day": True, "night": True, "snowy": True})
default her_outfit_s_overcast = DollOutfit([her_hair_base, her_top_pullover_1, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], True, schedule={"day": True, "night": True, "cloudy": True})
default her_outfit_s_rain = DollOutfit([her_hair_base, her_robe_school_1, her_top_school1, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], True, schedule={"day": True, "night": True, "rainy": True})

############
## Events ##
############

# Gryffindor Quidditch Match
default herq_panties_on_head = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "panties_on_head", ["#9cccf9ff"], tracking="?hair")

# Vibrator
default her_panties_base_vibrators = DollCloth("hermione", ("lower undergarment", "panties"), "panties", "basic_panties_vibrators", ["#e8e8e8ff", "#ca3c01ff"])
default her_bra_base_vibrators = DollCloth("hermione", ("upper undergarment", "bras"), "bra", "basic_bra_vibrators", ["#e8e8e8ff", "#ca3c01ff"])
default her_nipple_vibrators = DollCloth("hermione", ("misc", "accessory"), "accessory", "nipple_vibrators", ["#ea8e61ff", "#fcd987ff", "#ff7660ff"], zorder=152)
default her_clit_vibrators = DollCloth("hermione", ("misc", "accessory"), "accessory", "clit_vibrators", ["#ea8e61ff", "#fcd987ff", "#ff7660ff"], zorder=152)

default her_outfit_vibrators = DollOutfit([her_hair_base, her_panties_base_vibrators, her_bra_base_vibrators, her_nipple_vibrators, her_clit_vibrators], hidden=True)
default her_outfit_vibrators_nude = DollOutfit([her_hair_base, her_nipple_vibrators, her_clit_vibrators], hidden=True)

# Magic Collars
default her_neckwear_basic_collar = DollCloth("hermione", ("head", "neckwear"), "neckwear", "basic_collar", ["#b6725bff", "#ff0000ff"])
default her_neckwear_good_girl_collar = DollCloth("hermione", ("head", "neckwear"), "neckwear", "good_girl_collar", ["#ffb8c0ff", "#ffe0e6ff", "#ff66ccff"])
default her_neckwear_whore_collar = DollCloth("hermione", ("head", "neckwear"), "neckwear", "whore_collar", ["#3b3b3bff"])
default her_neckwear_flasher_collar = DollCloth("hermione", ("head", "neckwear"), "neckwear", "flasher_collar", ["#e940f0ff", "#f5db68ff"], blacklist=["top", "bra"])
default her_neckwear_slut_collar = DollCloth("hermione", ("head", "neckwear"), "neckwear", "slut_collar", ["#fb4252ff", "#282828ff"])
default her_neckwear_slave_collar = DollCloth("hermione", ("head", "neckwear"), "neckwear", "slave_collar", ["#aaa9adff"])

# Butt Plugs
default her_buttplug_small1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "buttplug_small_1", ["#fcc3dbff", "#544cd6ff"], zorder=-1, level=15)
default her_buttplug_medium1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "buttplug_medium_1", ["#ffff77ff", "#f38c09ff", "#ff4c2eff", "#544cd6ff"], zorder=-1, level=19)
default her_buttplug_large1 = DollCloth("hermione", ("misc", "accessory"), "accessory", "buttplug_large_1", ["#63d00eff", "#fe6cb5ff", "#544cd6ff"], zorder=-1, level=23)

# Potions #

default her_chest_breasts1 = DollBodypart("hermione", ("hidden", "chest"), "chest", "big1")
default her_chest_breasts2 = DollBodypart("hermione", ("hidden", "chest"), "chest", "big2")
default her_chest_breasts3 = DollBodypart("hermione", ("hidden", "chest"), "chest", "big3")

default her_hips_ass1 = DollBodypart("hermione", ("hidden", "hips"), "hips", "big1")
default her_hips_ass2 = DollBodypart("hermione", ("hidden", "hips"), "hips", "big2")
default her_hips_ass3 = DollBodypart("hermione", ("hidden", "hips"), "hips", "big3")

# Catgirl
default her_cat_ears = DollClothDynamic("hermione", ("head", "headgear"), "headgear", "cat_ears", ["#d17b43ff", "#e8e8e8ff"], tracking="?hair")
default her_cat_legs = DollCloth("hermione", ("legwear", "stockings"), "stockings", "cat_legs",["#d17b43ff"])
default her_cat_arms = DollCloth("hermione", ("upper body", "gloves"), "gloves", "cat_arms", ["#d17b43ff", "#d67a7aff", "#252525ff"])
default her_cat_tail = DollCloth("hermione", ("misc", "accessory"), "accessory", "cat_tail", ["#d17b43ff"], zorder=-1)
default her_cat_muzzle = DollCloth("hermione", ("head", "makeup"), "makeup", "cat_muzzle", ["#d67a7aff"])

default her_outfit_cat1 = DollOutfit([her_hair_base, her_cat_ears, her_cat_tail], hidden=True)
default her_outfit_cat2 = DollOutfit([her_hair_base, her_cat_ears, her_cat_tail, her_cat_legs, her_cat_arms, her_pubes_beaver], hidden=True)
default her_outfit_cat3 = DollOutfit([her_hair_base, her_cat_ears, her_cat_tail, her_cat_legs, her_cat_arms, her_pubes_beaver, her_cat_muzzle], hidden=True)

################
## Not In Use ##
################

#default her_bottom_winter_1 = DollCloth("hermione", ("lower body", "skirts"), "bottom", "winter_skirt_1", ["#c01f1eff"])
