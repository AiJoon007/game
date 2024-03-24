###############
## Character ##
###############

default astoria = Doll(name="astoria")

default ast_frame_default = DollBodypart("astoria", ("hidden", "frame"), "frame", "default")
default ast_body_default = DollOutfit([ast_frame_default], hidden=True)

##########
## Hair ##
##########

default ast_hair_base = DollCloth("astoria", ("head", "hair"), "hair", "base", ["#e5c681ff", "#a37d50ff"], unlocked=True, zorder=205)
default ast_hair_short = DollCloth("astoria", ("head", "hair"), "hair", "short", ["#e5c681ff", "#a37d50ff"], unlocked=True)

#######################
## Schoolgirl Outfit ##
#######################

default ast_top_school1 = DollCloth("astoria", ("upper body", "shirts"), "top", "top_school_1", ["#b7b7b8ff", "#6d6979ff", "#3a734bff", "#cdcdceff"], unlocked=True)
default ast_top_school2 = DollCloth("astoria", ("upper body", "shirts"), "top", "top_school_2", ["#b7b7b8ff", "#6d6979ff", "#3a734bff", "#cdcdceff"], level=4, unlocked=True)
default ast_top_school3 = DollCloth("astoria", ("upper body", "shirts"), "top", "top_school_3", ["#b7b7b8ff", "#3a734bff", "#cdcdceff"], level=8, unlocked=True)
default ast_top_school4 = DollCloth("astoria", ("upper body", "shirts"), "top", "top_school_4", ["#b7b7b8ff", "#3a734bff", "#cdcdceff"], level=8, unlocked=True)
default ast_top_school5 = DollCloth("astoria", ("upper body", "shirts"), "top", "top_school_5", ["#b7b7b8ff", "#3a734bff", "#cdcdceff"], level=12, unlocked=True)
default ast_top_school6 = DollCloth("astoria", ("upper body", "shirts"), "top", "top_school_6", ["#6d6979ff", "#3a734bff", "#cdcdceff"], level=12, unlocked=True)

default ast_bottom_skirt1 = DollCloth("astoria", ("lower body", "skirts"), "bottom", "school_skirt_1", ["#675a6cff", "#e8b10dff"], unlocked=True)
default ast_bottom_skirt2 = DollCloth("astoria", ("lower body", "skirts"), "bottom", "school_skirt_2", ["#675a6cff", "#e8b10dff"], level=4, unlocked=True)
default ast_bottom_skirt3 = DollCloth("astoria", ("lower body", "skirts"), "bottom", "school_skirt_3", ["#675a6cff", "#e8b10dff"], level=8, unlocked=True)
default ast_bottom_skirt4 = DollCloth("astoria", ("lower body", "skirts"), "bottom", "school_skirt_4", ["#675a6cff", "#e8b10dff"], level=12, unlocked=True)

default ast_bra_basic1 = DollCloth("astoria", ("upper undergarment", "bras"), "bra", "basic_bra_1", ["#d53e41ff", "#eaeceaff"], unlocked=True)
default ast_bra_basic2 = DollCloth("astoria", ("upper undergarment", "bras"), "bra", "basic_bra_2", ["#d53e41ff"], unlocked=True)
default ast_panties_basic1 = DollCloth("astoria", ("lower undergarment", "panties"), "panties", "basic_panties_1", ["#d53e41ff", "#eaeceaff"], unlocked=True)
default ast_panties_basic2 = DollCloth("astoria", ("lower undergarment", "panties"), "panties", "basic_panties_2", ["#d53e41ff"], unlocked=True)

default ast_outfit_default = DollOutfit([ast_hair_base, ast_top_school1, ast_bottom_skirt1, ast_bra_basic1, ast_panties_basic1], unlocked=True)
default ast_outfit_last = DollOutfit([ast_hair_base], hidden=True)

################
## Ann Outfit ##
################

default ast_hair_ann = DollCloth("astoria", ("head", "hair"), "hair", "ann_takamaki", ["#e5c681ff", "#a37d50ff", "#ffd169ff"])
default ast_hat_ann = DollClothDynamic("astoria", ("head", "headgear"), "headgear", "ann_takamaki", ["#ad1212ff", "#eebcbbff"], level=14, tracking="?hair")
default ast_top_ann = DollCloth("astoria", ("upper body", "other"), "top", "ann_takamaki", ["#ad1212ff", "#e8e8e8ff", "#eebcbbff"], level=14, blacklist=("bottom", "bra", "garterbelt"))
default ast_stockings_ann = DollCloth("astoria", ("legwear", "stockings"), "stockings", "ann_takamaki", ["#632a2aff", "#b58787ff"], level=14, blacklist=["bottom"])
default ast_gloves_ann = DollCloth("astoria", ("upper body", "gloves"), "gloves", "ann_takamaki", ["#f98be1ff"])
default ast_buttplug_ann = DollCloth("astoria", ("misc", "accessory"), "accessory", "ann_takamaki", ["#632a2aff", "#b58787ff"], level=14, zorder=-1)

default ast_outfit_ann = DollOutfit([ast_hair_ann, ast_hat_ann, ast_top_ann, ast_stockings_ann, ast_gloves_ann, ast_buttplug_ann, ast_panties_basic1], price=500, name="Ann Costume", desc="Wearing this will make you look like a different persona.")

################
## Pubic Hair ##
################

default ast_pubes_arrow = DollCloth("astoria", ("lower undergarment", "pubes"), "pubes", "arrow", ["#e5c681ff"], unlocked=True)
default ast_pubes_beaver = DollCloth("astoria", ("lower undergarment", "pubes"), "pubes", "beaver", ["#e5c681ff"], unlocked=True)
default ast_pubes_stuble = DollCloth("astoria", ("lower undergarment", "pubes"), "pubes", "stuble", ["#8b6b45ff"], unlocked=True)
default ast_pubes_unshaved = DollCloth("astoria", ("lower undergarment", "pubes"), "pubes", "unshaved", ["#8b6b45ff"], unlocked=True)

# Lipstick
default ast_makeup_lipstick = DollMakeup("astoria", ("head", "makeup"), "makeup", "lipstick", ["#ff4646ff"], unlocked=True, tracking="mouth")

##########
## Misc ##
##########

default ast_cloth_pants1 = DollCloth("astoria", ("lower body", "trousers"), "bottom", "pants_1", ["#b4b4b4ff", "#d5a10dff"], unlocked=True)
default ast_cloth_shorts1 = DollCloth("astoria", ("lower body", "shorts"), "bottom", "pants_1_short", ["#b4b4b4ff", "#d5a10dff"], level=8, unlocked=True)
default ast_cloth_pantyhose1 = DollCloth("astoria", ("legwear", "pantyhose"), "stockings", "pantyhose", ["#be9281ff"], unlocked=True)
