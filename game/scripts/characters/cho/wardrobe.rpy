###############
## Character ##
###############

default cho = Doll(name="cho")

default cho_frame_default = DollBodypart("cho", ("hidden", "frame"), "frame", "default")
default cho_body_default = DollOutfit([cho_frame_default], hidden=True)

##########
## Hair ##
##########

default cho_hair_base = DollCloth("cho", ("head", "hair"), "hair", "ponytail", ["#343b50ff", "#465a93ff"], unlocked=True)

#######################
## Schoolgirl Outfit ##
#######################

default cho_top_school1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_1", ["#b7b7b8ff", "#6d6979ff", "#d8a30aff", "#5974c2ff"], unlocked=True)
default cho_top_school2 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_2", ["#b7b7b8ff", "#6d6979ff", "#d8a30aff", "#5974c2ff"], unlocked=True)
default cho_top_school3 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_3", ["#b7b7b8ff", "#d8a30aff", "#5974c2ff"], unlocked=True)
default cho_top_school4 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_4", ["#b7b7b8ff", "#d8a30aff", "#5974c2ff"], level=8, unlocked=True)
default cho_top_school5 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_5", ["#b7b7b8ff", "#d8a30aff", "#5974c2ff"], level=12, unlocked=True)
default cho_top_school6 = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_6", ["#6d6979ff", "#d8a30aff", "#5974c2ff"], level=12, unlocked=True)

default cho_bottom_school1 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_1", ["#675a6cff", "#e8b10dff"], unlocked=True)
default cho_bottom_school2 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_2", ["#675a6cff", "#e8b10dff"], level=4, unlocked=True)
default cho_bottom_school3 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_3", ["#675a6cff", "#e8b10dff"], level=8, unlocked=True)
default cho_bottom_school4 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_4", ["#675a6cff", "#e8b10dff"], level=12, unlocked=True)

default cho_bra_basic1 = DollCloth("cho", ("upper undergarment", "bras"), "bra", "basic_bra_1", ["#e6e6e7ff", "#5974c2ff"], unlocked=True)
default cho_panties_basic1 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "basic_panties_1", ["#e6e6e7ff", "#5974c2ff"], unlocked=True)

default cho_stockings_house = DollCloth("cho", ("legwear", "socks"), "stockings", "house", ["#d8a30aff", "#5974c2ff"], unlocked=True)

default cho_robe_school_1 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_school_1", color=["#606060ff", "#ceced1ff", "#5974c2ff"], level=0, unlocked=True)
default cho_robe_school_2 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_school_2", color=["#606060ff", "#ceced1ff", "#5974c2ff"], level=4, unlocked=True)
default cho_robe_school_3 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_school_3", color=["#606060ff", "#ceced1ff", "#5974c2ff"], level=8, unlocked=True)

default cho_outfit_last = DollOutfit([cho_hair_base], hidden=True)
default cho_outfit_default = DollOutfit([cho_hair_base, cho_top_school1, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_house], unlocked=True)

########################
## Cheerleader Outfit ##
########################

default cho_earring_snitch = DollCloth("cho", ("head", "earrings"), "earrings", "snitch", ["#dcdcddff", "#d5a10dff"])
default cho_top_quid1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_quid_1", ["#40548dff", "#d5a10dff"], level=10)
default cho_bottom_quid1 = DollCloth("cho", ("lower body", "skirts"), "bottom", "quid_skirt_1", ["#40548dff", "#d5a10dff"], level=10)
default cho_stockings_quid1 = DollCloth("cho", ("legwear", "socks"), "stockings", "quid1", ["#40548dff", "#d5a10dff"], level=10)
default cho_panties_sport2 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "sport_panties_2", ["#9cccf9ff"], level=4)
default cho_bra_sports1 = DollCloth("cho", ("upper undergarment", "bras"), "bra", "sport_bra_1", ["#9cccf9ff"], unlocked=True)
default cho_makeup_blush = DollCloth("cho", ("makeup", "blush"), "makeup", "blush", ["#ee71c4ff"], level=2)

default cho_outfit_cheerleader = DollOutfit([cho_hair_base, cho_earring_snitch, cho_stockings_quid1, cho_panties_sport2, cho_bra_sports1, cho_bottom_quid1, cho_top_quid1, cho_makeup_blush], price=500, name="Ravenclaw Cheerleader Uniform", desc="Ravenclaw! Ravenclaw!")

##################
## Misty Outfit ##
##################

default cho_top_shirt1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_shirt_1", ["#ffe57eff"], level=14)
default cho_bottom_shorts3 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_3", ["#2f9688ff", "#afdcbfff", "#f79826ff"], level=10)
default cho_accessory_suspenders = DollCloth("cho", ("misc", "accessory"), "accessory", "suspenders", ["#891611ff", "#e58c21ff"], zorder=213)

default cho_outfit_misty = DollOutfit([cho_hair_base, cho_accessory_suspenders, cho_top_shirt1, cho_bottom_shorts3, cho_panties_sport2], price=500, name="Misty Costume", desc="For trainers that want to be the very best! To train them is your cause!")

#####################
## Clubslut Outfit ##
#####################

default cho_bottom_skirt2 = DollCloth("cho", ("lower body", "skirts"), "bottom", "skirt_short_2", ["#5d77adff"], level=16)
default cho_bra_bikini1 = DollCloth("cho", ("upper undergarment", "bikini bras"), "bra", "bikini_top_1", ["#03edeaff"], level=10)

default cho_outfit_party = DollOutfit([cho_hair_base, cho_bottom_skirt2, cho_bra_bikini1], price=500, name="Clubslut Outfit", desc="Release your inner slut with this unique club outfit!")

###################
## Sailor Outfit ##
###################

default cho_bottom_skirt1 = DollCloth("cho", ("lower body", "skirts"), "bottom", "skirt_short_1", ["#5974c2ff"], level=18)
default cho_top_sailor1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_sailor_1", ["#fcfcfdff", "#5974c2ff"], level=14)
default cho_stockings_sailor1 = DollCloth("cho", ("legwear", "stockings"), "stockings", "sailor", ["#e8e8e9ff"])
default cho_panties_bikini2 = DollCloth("cho", ("lower undergarment", "bikini panties"), "panties", "bikini_bottom_2", ["#d5a10dff"], level=18)

default cho_outfit_sailor = DollOutfit([cho_hair_base, cho_top_sailor1, cho_bottom_skirt1, cho_stockings_sailor1, cho_panties_bikini2], price=500, name="Sailor Outfit", desc="A slutty sailor outfit, perfect for the average cannon swabber.")

############################
## Japanese School Outfit ##
############################

default cho_top_j_school1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_j_school_1", ["#fff8dfff", "#5f6e8eff", "#a1a1a4ff", "#fdfefaff"], level=4)
default cho_bottom_j_skirt1 = DollCloth("cho", ("lower body", "skirts"), "bottom", "j_school_skirt_1", ["#a1a1a4ff"], level=4)
default cho_stockings_j_kneehigh1 = DollCloth("cho", ("legwear", "socks"), "stockings", "kneehigh", ["#fdfefaff"], level=0)

default cho_outfit_j_school = DollOutfit([cho_hair_base, cho_top_j_school1, cho_bottom_j_skirt1, cho_stockings_j_kneehigh1, cho_panties_basic1, cho_bra_basic1], price=300, name="Japanese School Uniform", desc="A school girl uniform inspired by the land of culture.")

###################
## Bikini Outfit ##
###################

default cho_bra_bikini2 = DollCloth("cho", ("upper undergarment", "bikini bras"), "bra", "bikini_top_2", ["#5974c2ff"], level=14)
default cho_panties_bikini1 = DollCloth("cho", ("lower undergarment", "bikini panties"), "panties", "bikini_bottom_1", ["#d5a10dff"], level=14)

default cho_outfit_bikini = DollOutfit([cho_hair_base, cho_bra_bikini2, cho_panties_bikini1], price=500, name="Micro Bikini Set", desc="It's like a regular sized bikini that's shrunk in the wash.")

##########################
## Lace Lingerie Outfit ##
##########################

default cho_neckwear_lace1 = DollCloth("cho", ("head", "neckwear"), "neckwear", "choker_lace_1", ["#6464ffff", "#dcdcddff"])
default cho_garterbelt_lace1 = DollCloth("cho", ("legwear", "garterbelts"), "garterbelt", "lace_garter_1", ["#dcdcddff", "#6464ffff", "#dcdcddff", "#5974c2ff"], level=12)
default cho_stockings_lace1 = DollCloth("cho", ("legwear", "stockings"), "stockings", "lace_stockings_1", ["#6464ffff", "#dcdcddff"], level=12)
default cho_bra_lace1 = DollCloth("cho", ("upper undergarment", "bras"), "bra", "lace_bra_1", ["#6464ffff", "#dcdcddff", "#5974c2ff"], level=14)
default cho_panties_lace1 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "lace_panties_1", ["#6464ffff", "#dcdcddff", "#5974c2ff"], level=14)
default cho_earring_feather = DollCloth("cho", ("head", "earrings"), "earrings", "feather", ["#e8e8e8ff", "#465a93ff", "#885b22ff"])

default cho_outfit_lacelingerie = DollOutfit([cho_hair_base, cho_neckwear_lace1, cho_garterbelt_lace1, cho_panties_lace1, cho_bra_lace1, cho_stockings_lace1, cho_earring_feather], price=500, name="Lace Lingerie Set", desc="This lingerie set turns even the toughest tomboy into a cute and sexy princess!")

##################
## Dress Outfit ##
##################

default cho_top_dress1 = DollCloth("cho", ("upper body", "dresses"), "top", "dress_1", ["#e71d29ff", "#f2a249ff"], level=12, blacklist=["bottom"])

default cho_outfit_dress1 = DollOutfit([cho_hair_base, cho_top_dress1, cho_panties_basic1, cho_bra_basic1], price=500, name="Traditional Chinese Dress", desc="A traditional dress inspired by Chinese culture.")

####################
## Trainee Outfit ##
####################

default cho_top_tank2 = DollCloth("cho", ("upper body", "shirts"), "top", "top_tanktop_2", ["#fcc0d5ff", "#fddde8ff"], level=10)
default cho_bottom_shorts1 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_1", ["#e6e6e7ff"], level=8)
default cho_stockings_pantyhose = DollCloth("cho", ("legwear", "pantyhose"), "stockings", "pantyhose", ["#be9281ff"])
default cho_earring_basic = DollCloth("cho", ("head", "earrings"), "earrings", "basic", ["#dcdcddff"])

default cho_outfit_trainee = DollOutfit([cho_hair_base, cho_bra_basic1, cho_panties_basic1, cho_bottom_shorts1, cho_top_tank2, cho_stockings_pantyhose, cho_earring_basic], price=500, name="Sporty Outfit", desc="Great for reducing fat.")

######################
## Toonsquad Outfit ##
######################

default cho_headgear_toon_band = DollClothDynamic("cho", ("head", "headgear"), "headgear", "toon_band", ["#2b5197ff"], level=4, tracking="?hair")
default cho_top_toon_shirt = DollCloth("cho", ("upper body", "shirts"), "top", "toon_shirt", ["#ffffffff"], level=4)
default cho_bottom_toon_shorts = DollCloth("cho", ("lower body", "shorts"), "bottom", "toon_shorts", ["#2b5197ff", "#ffffffff"], level=4)
default cho_stockings_toon_socks = DollCloth("cho", ("legwear", "socks"), "stockings", "toon_socks", ["#2b5197ff", "#ffffffff"], level=4)

default cho_outfit_toon = DollOutfit([cho_hair_base, cho_headgear_toon_band, cho_top_toon_shirt, cho_bottom_toon_shorts, cho_stockings_toon_socks, cho_bra_basic1, cho_panties_basic1], price=500, name="Toonsquad Outfit", desc="\"Don't ever call me a doll!\" - Some Sexy Bunny")

####################
## Chun-Li Outfit ##
####################

default cho_top_chun_li = DollCloth("cho", ("upper body", "shirts"), "top", "top_chun_li", ["#ed224fff", "#ffe279ff"], level=12)
default cho_bottom_chun_li_skirt = DollCloth("cho", ("lower body", "skirts"), "bottom", "skirt_chun_li", ["#ed224fff", "#ffe279ff"], level=12)
default cho_accessory_chun_li_wrap = DollCloth("cho", ("misc", "accessory"), "accessory", "body_wrap", ["#fffbdeff"], level=12, zorder=193)
default cho_accessory_chun_li_shoulders = DollCloth("cho", ("misc", "accessory"), "accessory", "chun_li_shoulders", ["#ed224fff", "#ffe279ff"], level=12, zorder=213)
default cho_headgear_chun_li_puffies = DollClothDynamic("cho", ("head", "headgear"), "headgear", "chun_li_puffies", ["#fffbdeff"], level=10, tracking="?hair")
default cho_tattoo_chun_li_dragon = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "chun_li_dragon", ["#ed224fff", "#ffe279ff"])
default cho_tattoo_chun_li_mule = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "chun_li_mule", ["#000000ff"])

default cho_outfit_chun_li = DollOutfit([cho_hair_base, cho_top_chun_li, cho_bottom_chun_li_skirt, cho_accessory_chun_li_wrap, cho_accessory_chun_li_shoulders, cho_headgear_chun_li_puffies, cho_bra_basic1, cho_panties_basic1, cho_tattoo_chun_li_dragon, cho_tattoo_chun_li_mule], price=500, name="Chun-Li Outfit", desc="For the strongest woman in the world!")

##################
## Police Woman ## #unlocked in not_so_great_escape mirror story
##################

default cho_top_police1 = DollCloth("cho", ("upper body", "shirts"), "top", "police", ["#455495ff", "#ebd165ff"], level=9)
default cho_bottom_police_skirt = DollCloth("cho", ("lower body", "skirts"), "bottom", "police_skirt", ["#455495ff", "#ebd165ff", "#a35f3aff", "#ebd165ff"], level=10)
default cho_glasses_aviators = DollCloth("cho", ("head", "glasses"), "glasses", "aviators", ["#b7c7d8ff", "#f3d954ff"], level=6)
default cho_headgear_police_cap = DollClothDynamic("cho", ("head", "headgear"), "headgear", "police_cap", ["#7e7ec0ff", "#ebd165ff", "#b7c7d8ff", "#ebd165ff"], level=6, tracking="?hair")

default cho_outfit_police = DollOutfit([cho_hair_base, cho_top_police1, cho_bottom_police_skirt, cho_bra_basic1, cho_panties_basic1, cho_glasses_aviators, cho_headgear_police_cap])

######################
## Reindeer Costume ## #unlocked in genies_christmas_wish mirror story
######################

default cho_top_bunny2 = DollCloth("cho", ("upper body", "one-piece suits"), "top", "bunny_top_2", ["#84220bff"], blacklist=["panties", "bra"], zorder=183, level=15)
default cho_hat_antlers = DollClothDynamic("cho", ("head", "headgear"), "headgear", "antlers", ["#984b30ff", "#ffffffff", "#c29d63ff"], level=12, tracking="?hair")
default cho_neckwear_reindeer_collar = DollCloth("cho", ("head", "neckwear"), "neckwear", "reindeer_collar", ["#7e4422ff", "#c4ab5fff"], level=15)
default cho_accessory_mistletoe = DollCloth("cho", ("misc", "accessory"), "accessory", "mistletoe", ["#1b5cc9ff"], zorder=193, level=7)

default cho_outfit_reindeer = DollOutfit([cho_hair_base, cho_top_bunny2, cho_accessory_mistletoe, cho_hat_antlers, cho_neckwear_reindeer_collar])

###################
## Bunny Costume ##
###################

default cho_top_bunny1 = DollCloth("cho", ("upper body", "one-piece suits"), "top", "bunny_top_1", ["#000000ff"], blacklist=["panties", "bra"], zorder=183, level=15)
default cho_stockings_bunny1 = DollCloth("cho", ("legwear", "pantyhose"), "stockings", "bunny_stockings_1", ["#515151ff"], level=5)
default cho_hat_bunny1 = DollClothDynamic("cho", ("head", "headgear"), "headgear", "bunny_hat_1", ["#2b2a32ff", "#575370ff"], level=15, tracking="?hair")

default cho_outfit_bunny = DollOutfit([cho_hair_base, cho_top_bunny1, cho_stockings_bunny1, cho_hat_bunny1], price=250, name="Sexy Bunny Costume", desc="A costume to turn you into the bunny equivalent of a neko.")

##########################
## Virgin Killer Outfit ##
##########################

default cho_top_virgin_killer = DollCloth("cho", ("upper body", "one-piece suits"), "top", "top_virgin_killer", ["#de4047ff", "#de4047ff"], blacklist=["bottom", "panties", "bra"], zorder=183, level=15)

default cho_outfit_virgin_killer = DollOutfit([cho_hair_base, cho_top_virgin_killer], price=200, name="Virgin Killer", desc="Disclaimer: Does not actually kill virgins.")

##########################
## Sheer Nightie Outfit ##
##########################

default cho_nightie_sheer1 = DollCloth("cho", ("upper body", "shirts"), "top", "sheer_nightie_1", ["#CBE5F8BF", "#000000FF"], level=13)
default cho_panties_sheer1 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "sheer_panties_1", ["#CBE5F8BF"], level=16)

default cho_outfit_sheer_nightie = DollOutfit([cho_hair_base, cho_nightie_sheer1, cho_panties_sheer1], price=400, name="Sheer Nightie Set", desc="Like a regular nightie, except you can see through it.")

##########################
## Sporty Bikini Outfit ##
##########################

default cho_bra_bikini_sporty1 = DollCloth("cho", ("upper undergarment", "bikini bras"), "bra", "sporty_bikini_top_1", ["#484A6CFF"], level=8)
default cho_panties_bikini_sporty1 = DollCloth("cho", ("lower undergarment", "bikini panties"), "panties", "sporty_bikini_bottom_1", ["#484A6CFF"], level=12)

default cho_outfit_sporty_bikini = DollOutfit([cho_hair_base, cho_bra_bikini_sporty1, cho_panties_bikini_sporty1], price=400, name="Sporty Bikini Set", desc="A sporty bikini for the more athletic kind of witch.")

#######################
## Club Dress Outfit ##
#######################

default cho_top_dress_club = DollCloth("cho", ("upper body", "dresses"), "top", "dress_club", ["#212638ff"], level=12)
default cho_bra_padding_1 = DollCloth("cho", ("upper undergarment", "bras"), "bra", "padding_bra_1", ["#212638FF"], level=12)
default cho_panties_sheer_2 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "sheer_panties_2", ["#212638FF", "#2D2D4BFF" ], level=16)

default cho_outfit_club_dress = DollOutfit([cho_hair_base, cho_top_dress_club, cho_bra_padding_1, cho_panties_sheer_2], price=450, name="Club Dress Set", desc="The perfect dress set for an outgoing witch.")

################
## Pubic Hair ##
################

default cho_pubes_arrow = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "arrow", ["#465a93ff"], unlocked=True)
default cho_pubes_beaver = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "beaver", ["#465a93ff"], unlocked=True)
default cho_pubes_stuble = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "stuble", ["#343b50ff"], unlocked=True)
default cho_pubes_unshaved = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "unshaved", ["#343b50ff"], unlocked=True)
default cho_pubes_thick = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "thick", ["#343b50ff", "#465a93ff"], unlocked=True)
default cho_pubes_heart = DollCloth("cho", ("lower undergarment", "pubes"), "pubes", "heart", ["#343b50ff", "#465a93ff"], unlocked=True)

############
## Makeup ##
############

default cho_makeup_freckles1 = DollCloth("cho", ("head", "makeup"), "makeup", "freckles1", ["#BB7A49ff"], unlocked=True)
default cho_makeup_freckles2 = DollCloth("cho", ("head", "makeup"), "makeup", "freckles2", ["#BB7A49ff"], unlocked=True)

default cho_makeup_lipstick = DollMakeup("cho", ("head", "makeup"), "makeup", "lipstick", ["#ff4646ff"], unlocked=True, tracking="mouth")


#############
## Tattoos ##
#############

default cho_tattoo_free = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "pelv_free", ["#000001ff"], unlocked=True)
default cho_tattoo_slut = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "breasts_slut", ["#000001ff"], unlocked=True)
default cho_tattoo_arrows = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "arrows_tattoo", ["#C96548ff"], unlocked=True)
default cho_tattoo_barcode = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "barcode_tattoo", ["#000001ff"], unlocked=True)
default cho_tattoo_bitemark = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "bitemark_tattoo", ["#ffffffff"], unlocked=True)
default cho_tattoo_cumhere = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "cumhere_tattoo", ["#000001ff"], unlocked=True)
default cho_tattoo_lickme = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "lickme_tattoo", ["#000001ff"], unlocked=True)
default cho_tattoo_pull = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "pull_tattoo", ["#000001ff"], unlocked=True)
default cho_tattoo_snatch = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "snatch_tattoo", ["#000001ff"], unlocked=True)
default cho_tattoo_trainee = DollCloth("cho", ("piercings & tattoos", "tattoos"), "tattoo", "trainee_tattoo", ["#000001ff"], unlocked=True)

###############
## Piercings ##
###############

default cho_piercing_stud = DollCloth("cho", ("piercings & tattoos", "piercings"), "piercing", "stud", ["#dcdcddff"], unlocked=True)
default cho_piercing_barbell = DollCloth("cho", ("piercings & tattoos", "piercings"), "piercing", "breast_barbell", ["#dcdcddff"], unlocked=True)

# Quidditch separate category
default choq_bra_sports1 = DollCloth("cho", ("upper undergarment", "bras"), "bra", "sport_bra_1", ["#9cccf9ff"])
default choq_panties_sport1 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "sport_panties_1", ["#9cccf9ff"])
default choq_panties_sport2 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "sport_panties_2", ["#9cccf9ff"])
default choq_cloth_robequidditch1 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_quidditch_1", ["#3c4e83ff", "#ba8d0bff"])
default choq_cloth_topsweater1 = DollCloth("cho", ("upper body", "sweaters"), "top", "top_sweater_1", ["#3c4e83ff", "#ba8d0bff"])
default choq_cloth_pantslong2 = DollCloth("cho", ("lower body", "trousers"), "bottom", "pants_long_2", ["#6d6979ff", "#d5a10dff"])
default choq_cloth_pantsshort4 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_4", ["#6d6979ff", "#d5a10dff"])
#default choq_cloth_glovesquidditch1 = DollCloth("cho", ("upper body", "gloves"), "gloves", "quidditch", ["#d5a10dff"]) # Not in use anymore.
default choq_goggles = DollCloth("cho", ("head", "glasses"), "glasses", "goggles", ["#8996c1ff", "#a5a5a6ff"])
#default choq_goggles_face = DollCloth("cho", ("head", "headgear"), "headgear", "goggles_face", ["#8996c1ff", "#a5a5a6ff"], unlocked=False) # Not in use
default choq_cloth_schoolskirt2 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_2", ["#675a6cff", "#e8b10dff"])
default choq_cloth_schoolskirt3 = DollCloth("cho", ("lower body", "skirts"), "bottom", "school_skirt_3", ["#675a6cff", "#e8b10dff"])
default choq_panties_in_hand = DollCloth("cho", ("misc", "accessory"), "accessory", "panties_in_hand", ["#9cccf9ff"])

default choq_accessory_protectors = DollCloth("cho", ("misc", "accessory"), "accessory", "protectors1", None, zorder=300)
default choq_accessory_protectors2 = DollCloth("cho", ("misc", "accessory"), "accessory", "protectors2", None, zorder=300)
default choq_accessory_snitch_in_hand = DollCloth("cho", ("hidden", "accessory"), "accessory", "snitch_in_hand", None, zorder=-1)

# Add choq_accessory_protectors2 once drawn for normal pose
default cho_outfit_quidditch = DollOutfit([cho_hair_base, choq_cloth_topsweater1, choq_cloth_pantslong2, choq_cloth_robequidditch1, choq_bra_sports1, choq_panties_sport2], hidden=True)

default cho_outfit_quidditch_hufflepuff = DollOutfit([cho_hair_base, choq_cloth_topsweater1, choq_cloth_schoolskirt2, choq_cloth_robequidditch1, choq_accessory_protectors, choq_bra_sports1, choq_panties_sport2], hidden=True)
default cho_outfit_quidditch_slytherin = DollOutfit([cho_hair_base, choq_cloth_topsweater1, choq_cloth_pantslong2, choq_accessory_protectors2, choq_bra_sports1, choq_panties_sport2], hidden=True)
default cho_outfit_quidditch_gryffindor = DollOutfit([cho_hair_base, choq_cloth_topsweater1, choq_cloth_schoolskirt2, choq_accessory_protectors, choq_bra_sports1, choq_panties_sport2], hidden=True)

############
## Events ##
############

# cc_pr_manipulate_boys_twins_branch
default cho_top_school1_slyt = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_1", ["#b7b7b8ff", "#6d6979ff", "#3a734bff", "#cdcdceff"])
default cho_top_school1_gryf = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_1", ["#b7b7b8ff", "#6d6979ff", "#a74d2aff", "#edb30eff"])
default cho_top_school1_huff = DollCloth("cho", ("upper body", "shirts"), "top", "top_school_1", ["#b7b7b8ff", "#6d6979ff", "#fbc60aff", "#332b36ff"])
default cho_stockings_slyt = DollCloth("cho", ("legwear", "socks"), "stockings", "house", ["#3a734bff", "#cdcdceff"])
default cho_stockings_gryf = DollCloth("cho", ("legwear", "socks"), "stockings", "house", ["#dba50dff", "#923f1eff"])
default cho_stockings_huff = DollCloth("cho", ("legwear", "socks"), "stockings", "house", ["#fbc60aff", "#332b36ff"])

default smurfette_hair = DollCloth("cho", ("head", "hair"), "hair", "smurfette", ["#ffdd47ff", "#ffed9eff"], level=4)
default smurfette_hat = DollClothDynamic("cho", ("head", "headgear"), "headgear", "smurfette", ["#fbfbfbff"], level=4, tracking="?hair")
default smurfette_top = DollCloth("cho", ("upper body", "dresses"), "top", "smurfette", ["#fbfbfbff", "#fbfbfbff"], level=4, blacklist=["bottom"])

default cho_outfit_slyt = DollOutfit([cho_hair_base, cho_top_school1_slyt, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_slyt], hidden=True)
default cho_outfit_gryf = DollOutfit([cho_hair_base, cho_top_school1_gryf, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_gryf], hidden=True)
default cho_outfit_huff = DollOutfit([cho_hair_base, cho_top_school1_huff, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_huff], hidden=True)
default cho_outfit_smurfette = DollOutfit([smurfette_hair, smurfette_hat, smurfette_top], price=0, name="Smurfette Costume", desc="I'm coming for you, Gargamel.{heart}")

##########
## Misc ##
##########

default cho_panties_sport1 = DollCloth("cho", ("lower undergarment", "panties"), "panties", "sport_panties_1", ["#9cccf9ff"], unlocked=True)
default cho_hat_catears = DollClothDynamic("cho", ("head", "headgear"), "headgear", "catears", ["#465a93ff"], level=10, unlocked=True, tracking="?hair")
default cho_hat_witch = DollClothDynamic("cho", ("head", "headgear"), "headgear", "witch", ["#473366ff", "#d7aa62ff"], unlocked=True, tracking="?hair")
default cho_accessory_glasses1 = DollCloth("cho", ("head", "glasses"), "glasses", "glasses1", ["#f0f0f1ff"], unlocked=True)
default cho_hat_goggles = DollClothDynamic("cho", ("head", "headgear"), "headgear", "goggles", ["#8996c1ff", "#a5a5a6ff"], unlocked=True, tracking="?hair")
default cho_neckwear_medallion = DollCloth("cho", ("head", "neckwear"), "neckwear", "choker_medallion", ["#19191aff"], unlocked=True)
default cho_neckwear_leather1 = DollCloth("cho", ("head", "neckwear"), "neckwear", "collar_leather_1", ["#383839ff"], unlocked=True)
default cho_stockings_fishnet = DollCloth("cho", ("legwear", "stockings"), "stockings", "fishnet", ["#646465ff", "#323233ff"], level=14, unlocked=True)
default cho_top_sweater1 = DollCloth("cho", ("upper body", "sweaters"), "top", "top_sweater_1", ["#5974c2ff", "#d5a10dff"], unlocked=True)
default cho_top_sweater2 = DollCloth("cho", ("upper body", "sweaters"), "top", "top_sweater_2", ["#5974c2ff"], level=6, unlocked=True)
default cho_top_hoodie1 = DollCloth("cho", ("upper body", "sweaters"), "top", "top_hoodie_1", ["#2F5D91ff", "#B8CEE7ff"], unlocked=True)
default cho_top_woolly_sweater1 = DollCloth("cho", ("upper body", "sweaters"), "top", "top_woolly_sweater_1", ["#2F5D91ff"], unlocked=True)
default cho_top_tanktop1 = DollCloth("cho", ("upper body", "shirts"), "top", "top_tanktop_1", ["#e6e6e7ff"], level=14, unlocked=True)
default cho_robe_quidditch1 = DollCloth("cho", ("upper body", "robes"), "robe", "robe_quidditch_1", ["#5974c2ff", "#d5a10dff"], unlocked=True)
default cho_bottom_pants1 = DollCloth("cho", ("lower body", "trousers"), "bottom", "pants_long_1", ["#e6e6e7ff"], unlocked=True)
default cho_bottom_shorts2 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_2", ["#72a8d2ff", "#e8b10dff"], level=10, unlocked=True)
default cho_bottom_pants2 = DollCloth("cho", ("lower body", "trousers"), "bottom", "pants_long_2", ["#6d6979ff", "#d5a10dff"], unlocked=True)
default cho_bottom_shorts4 = DollCloth("cho", ("lower body", "shorts"), "bottom", "pants_short_4", ["#6d6979ff", "#d5a10dff"], level=8, unlocked=True)
default cho_jeans_long1 = DollCloth("cho", ("lower body", "trousers"), "bottom", "jeans_long_1", ["#6D8EAEff", "#3C5064ff"], unlocked=True)

### Default Schedules ###

default cho_outfit_s_clearday = DollOutfit([cho_hair_base, cho_top_school3, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1], True, schedule={"day": True})
default cho_outfit_s_clearnight = DollOutfit([cho_hair_base, cho_top_sweater1, cho_jeans_long1, cho_bra_basic1, cho_panties_basic1], True, schedule={"night": True})
default cho_outfit_s_snow = DollOutfit([cho_hair_base, cho_top_woolly_sweater1, cho_jeans_long1, cho_bra_basic1, cho_panties_basic1], True, schedule={"day": True, "night": True, "snowy": True})
default cho_outfit_s_overcast = DollOutfit([cho_hair_base, cho_top_hoodie1, cho_jeans_long1, cho_bra_basic1, cho_panties_basic1], True, schedule={"day": True, "night": True, "cloudy": True})
default cho_outfit_s_rain = DollOutfit([cho_hair_base, cho_robe_school_1, cho_top_school1, cho_bottom_school1, cho_bra_basic1, cho_panties_basic1, cho_stockings_house], True, schedule={"day": True, "night": True, "rainy": True})

################
## Not In Use ##
################

#default cho_hair_pigtails = DollCloth("cho", ("head", "hair"), "hair", "pigtails", ["#343b50ff", "#465a93ff", "#f2a249ff"], level=8)
#default cho_neckwear_tie1  = DollCloth("cho", ("head", "neckwear"), "neckwear", "tie_1", ["#d8a30aff", "#5974c2ff"]) #Tie Only
