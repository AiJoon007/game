###############
## Character ##
###############

default susan = Doll(name="susan")

default sus_frame_default = DollBodypart("susan", ("hidden", "frame"), "frame", "default")
default sus_body_default = DollOutfit([sus_frame_default], hidden=True)

##########
## Hair ##
##########

default sus_hair_base = DollCloth("susan", ("head", "hair"), "hair", "base", ["#d55523ff", "#e76d3dff"], unlocked=True, zorder=205)

#######################
## Schoolgirl Outfit ##
#######################

default sus_top_school1 = DollCloth("susan", ("upper body", "shirts"), "top", "top_school_1", ["#b9b8b8ff", "#726d7eff", "#332b36ff", "#d4a10eff"], unlocked=True)
default sus_top_school2 = DollCloth("susan", ("upper body", "shirts"), "top", "top_school_2", ["#b9b8b8ff", "#726d7eff", "#332b36ff", "#d4a10eff"], unlocked=True)
default sus_top_school3 = DollCloth("susan", ("upper body", "shirts"), "top", "top_school_3", ["#b9b8b8ff", "#e7dbdbff", "#726d7eff", "#332b36ff", "#d4a10eff"], unlocked=True)
default sus_top_school4 = DollCloth("susan", ("upper body", "shirts"), "top", "top_school_4", ["#b9b8b8ff", "#e7dbdbff", "#332b36ff", "#d4a10eff"], unlocked=True)
default sus_top_school5 = DollCloth("susan", ("upper body", "shirts"), "top", "top_school_5", ["#b9b8b8ff", "#332b36ff", "#d4a10eff", "#e7dbdbff"], unlocked=True)
#TODO open collar variant default sus_top_school6 = DollCloth("susan", ("upper body", "shirts"), "top", "top_school_6", ["#b9b8b8ff", "#726d7eff", "#332b36ff", "#d4a10eff"], unlocked=True)
default sus_top_school7 = DollCloth("susan", ("upper body", "shirts"), "top", "top_school_7", ["#726d7eff", "#332b36ff", "#d4a10eff"], unlocked=True)

default sus_bottom_school1 = DollCloth("susan", ("lower body", "skirts"), "bottom", "school_skirt_1", ["#675a6cff", "#e8b10dff"], unlocked=True)
default sus_bottom_school2 = DollCloth("susan", ("lower body", "skirts"), "bottom", "school_skirt_2", ["#675a6cff", "#e8b10dff"], unlocked=True)
default sus_bottom_school3 = DollCloth("susan", ("lower body", "skirts"), "bottom", "school_skirt_3", ["#675a6cff", "#e8b10dff"], unlocked=True)
default sus_bottom_school4 = DollCloth("susan", ("lower body", "skirts"), "bottom", "school_skirt_4", ["#675a6cff", "#e8b10dff"], unlocked=True)

default sus_bra_base1 = DollCloth("susan", ("upper undergarment", "bras"), "bra", "basic_bra_1", ["#ffeeedff", "#ecbfbfff", "#f98787ff"], unlocked=True)
default sus_panties_base1 = DollCloth("susan", ("lower undergarment", "panties"), "panties", "basic_panties_1", ["#ffeeedff", "#ecbfbfff", "#f98787ff"], unlocked=True)

default sus_stockings_school1 = DollCloth("susan", ("legwear", "stockings"), "stockings", "short_school_1", ["#d4a10eff", "#332b36ff"], unlocked=True)
default sus_stockings_school2 = DollCloth("susan", ("legwear", "stockings"), "stockings", "short_school_2", ["#332b36ff"], unlocked=True)

default sus_robe_school_1 = DollCloth("susan", ("upper body", "robes"), "robe", "robe_school_1", ["#606060ff", "#d4a10eff"], unlocked=True, level=0)
default sus_robe_school_2 = DollCloth("susan", ("upper body", "robes"), "robe", "robe_school_2", ["#606060ff", "#d4a10eff"], unlocked=True, level=4)
default sus_robe_school_3 = DollCloth("susan", ("upper body", "robes"), "robe", "robe_school_3", ["#606060ff", "#d4a10eff"], unlocked=True, level=10)
default sus_robe_school_4 = DollCloth("susan", ("upper body", "robes"), "robe", "robe_school_4", ["#606060ff", "#d4a10eff"], unlocked=True, level=13)

default sus_outfit_default = DollOutfit([sus_hair_base, sus_top_school1, sus_bottom_school1, sus_bra_base1, sus_panties_base1, sus_stockings_school1], unlocked=True)
default sus_outfit_last = DollOutfit([sus_hair_base], hidden=True)

##########################
## Muggle Casual Outfit ##
##########################

default sus_top_muggle_casual1 = DollCloth("susan", ("upper body", "sweaters"), "top", "muggle_casual_top_1", ["#9d6944ff"])
default sus_bottom_jeans1 = DollCloth("susan", ("lower body", "trousers"), "bottom", "jeans_1", ["#4e417fff", "#f27223ff"])
default sus_bra_muggle1 = DollCloth("susan", ("upper undergarment", "bras"), "bra", "muggle_bra_1", ["#e1c9a1ff", "#fffbdbff"])
default sus_panties_muggle1 = DollCloth("susan", ("lower undergarment", "panties"), "panties", "muggle_panties_1", ["#e1c9a1ff", "#fffbdbff"])

default sus_outfit_muggle_casual1 = DollOutfit([sus_hair_base, sus_top_muggle_casual1, sus_bottom_jeans1, sus_bra_muggle1, sus_panties_muggle1], unlocked=True)

######################
## Priestess Outfit ##
######################

default sus_headgear_priestess = DollClothDynamic("susan", ("head", "headgear"), "headgear", "priestess_headdress", ["#273843ff", "#e4ebf0ff"], tracking="?hair")
default sus_top_priestess = DollCloth("susan", ("upper body", "dresses"), "top", "priestess_dress", ["#273843ff", "#e4ebf0ff"])
default sus_lace_stockings1 = DollCloth("susan", ("legwear", "stockings"), "stockings", "lace_stockings_1", ["#000000ff"])
default sus_hat_necklace =DollCloth("susan", ("head", "neckwear"), "neckwear", "hat_necklace", ["#f0be78ff"], zorder=213)

default sus_outfit_priestess = DollOutfit([sus_hair_base, sus_headgear_priestess, sus_top_priestess, sus_lace_stockings1, sus_hat_necklace, sus_bra_base1, sus_panties_base1,], price=400, name="Priestess Outfit", desc="This outfit radiates innocence.")

##################
## Latex Outfit ##
##################

default sus_bra_latex1 = DollCloth("susan", ("upper undergarment", "bras"), "bra", "latex_bra_1", ["#fa8bf1ff"])
default sus_panties_latex1 = DollCloth("susan", ("lower undergarment", "panties"), "panties", "latex_panties_1", ["#fa8bf1ff"])

default sus_outfit_latex1 = DollOutfit([sus_hair_base, sus_bra_latex1, sus_panties_latex1], price=200, name="Latex Underwear", desc="Enchanted to prevent chafing.")

###########################
## Lace Lingerie Outfit ##
###########################

default sus_panties_lace1 = DollCloth("susan", ("lower undergarment", "panties"), "panties", "lace_panties_1", ["#f6f3d8ff", "#ce7be764", "#a3b4d8ff"])
default sus_stockings_striped_1 = DollCloth("susan", ("legwear", "stockings"), "stockings", "striped_stockings_1", ["#f6f3d8ff", "#ce7be7aa"])
default sus_garterbelt_1 = DollCloth("susan", ("legwear", "garterbelts"), "garterbelt", "garter_belt_1", ["#ce83e7ff"])
default sus_bra_lace1 = DollCloth("susan", ("upper undergarment", "bras"), "bra", "lace_bra_1", ["#f6f3d8ff", "#ce7be764"])

default sus_outfit_lace1 = DollOutfit([sus_hair_base, sus_bra_lace1, sus_panties_lace1, sus_stockings_striped_1, sus_garterbelt_1], price=250, name="Lace Lingerie", desc="Perfect for making a girl look even more presentable.")

###############
## Underwear ##
###############

# Sport
default sus_bra_sport1 = DollCloth("susan", ("upper undergarment", "bras"), "bra", "sport_bra_1", ["#6b6b8bff", "#dbcd4fff"], unlocked=True)
default sus_panties_sport1 = DollCloth("susan", ("lower undergarment", "panties"), "panties", "sport_panties_1", ["#6b6b8bff", "#dbcd4fff"], unlocked=True)
