
image CG her_intro hermione = Fixed(
    "images/CG/her_intro/bg.webp",
    AlphaMask(Composite((2160, 1200), (880, -180), Transform("CG her_doll", zoom=1.2)), "images/CG/her_intro/mask.webp"),
    )

image CG her_intro hermione bendover = Fixed(
    "images/CG/her_intro/bg.webp",
    "images/CG/her_intro/hermione_bendover.webp",
    )

layeredimage her_vibrators_public:
    fit "cover"
    fit_first True

    attribute background default

    group npc multiple prefix "npc":
        attribute sus_ron:
            "her_vibrators_public_npc_sus_ron"
        attribute shock_ron:
            Fixed("her_vibrators_public_npc_shock_ron", \
            "her_vibrators_public_npc_shock_ron_effect")
        attribute shock_harry:
            Fixed("her_vibrators_public_npc_shock_harry", \
            "her_vibrators_public_npc_shock_harry_effect")

    attribute no_hermione null
    attribute body default if_not "no_hermione"
    group blush auto prefix "blush" if_not "no_hermione":
        attribute neutral default
    group tears auto prefix "tears" if_not "no_hermione"
    group eyes auto prefix "eyes" if_not "no_hermione":
        attribute forward default
    group eyebrows auto prefix "eyebrows" if_not "no_hermione":
        attribute neutral default
    group mouth auto prefix "mouth" if_not "no_hermione":
        attribute neutral default
    attribute hair default if_not "no_hermione"

    group wetness multiple auto prefix "wetness" if_not "no_hermione"

    group vibrator_upper variant "vibrator_upper" multiple if_not "no_hermione":
        attribute base default
        attribute egg default at shake_xlinear
        attribute tape default
        attribute effect default at shake_xlinear

    group vibrator_lower variant "vibrator_lower" multiple if_not "no_hermione":
        attribute base default
        attribute egg default at shake_xlinear
        attribute tape default
        attribute effect default at shake_xlinear

    group underwear multiple if_not "no_hermione":
        attribute bra default if_any ["underwear", "nopanties"]
        attribute panties default if_any ["underwear", "nobra"]

    group outfit if_not "no_hermione":
        attribute uniform default
        attribute underwear null
        attribute nobra null
        attribute nopanties null
        attribute nude null

    group effects auto multiple prefix "effects" if_not "no_hermione"

image her_vibrators_public_proxy = LayeredImageProxy("her_vibrators_public")
image her_vibrators_public_xray = Xray("her_vibrators_public", "her_vibrators_public_proxy", radius=0.18)

layeredimage her_vibrators_personal hermione1:
    fit "cover"
    fit_first True

    always "her_vibrators_personal_background"

    attribute shadow default
    attribute body default
    group blush auto prefix "blush":
        attribute neutral null default
    group eyes auto prefix "eyes":
        attribute open_forward default
    group eyebrows auto prefix "eyebrows":
        attribute neutral default
    group mouth auto prefix "mouth":
        attribute horny default
    attribute fringe default

    group effects auto multiple prefix "effects"

    group vibrator multiple variant "vibrator":
        attribute base default
        attribute eggl default at shake_xlinear if_not "noshake"
        attribute eggr default at shake_xlinear if_not "noshake"
        attribute eggl default if_any "noshake"
        attribute eggr default if_any "noshake"
        attribute tape default

    attribute noshake null

layeredimage her_vibrators_personal hermione2:
    fit "cover"
    fit_first True

    always "her_vibrators_personal_background"

    attribute shadow default
    attribute body default
    group blush auto prefix "blush":
        attribute neutral null default
    group eyes auto prefix "eyes":
        attribute open_forward default
    group eyebrows auto prefix "eyebrows":
        attribute neutral default
    group mouth auto prefix "mouth":
        attribute horny default
    attribute fringe default

    group effects auto multiple prefix "effects"

    group vibrator multiple variant "vibrator":
        attribute base default
        attribute eggl default at shake_xlinear if_not "noshake"
        attribute eggr default at shake_xlinear if_not "noshake"
        attribute eggm default at shake_xlinear if_not "noshake"
        attribute eggl default if_any "noshake"
        attribute eggr default if_any "noshake"
        attribute eggm default if_any "noshake"
        attribute tape default

    attribute noshake null

layeredimage her_vibrators_personal hermione3:
    fit "cover"
    fit_first True

    always "her_vibrators_personal_background"

    attribute shadow default
    attribute body default
    group blush auto prefix "blush":
        attribute neutral null default
    group eyes auto prefix "eyes":
        attribute clenched default
    group eyebrows auto prefix "eyebrows":
        attribute worried default
    group mouth auto prefix "mouth":
        attribute open default

    group effects auto multiple prefix "effects"

    group vibrator multiple variant "vibrator":
        attribute base default
        attribute eggl default at shake_xlinear
        attribute eggr default at shake_xlinear

layeredimage her_flash_public:
    fit "cover"

    always "her_flash_public_background"

    group npc auto prefix "npc":
        attribute pose5:
            at blink_repeat # TODO: Figure out why this does not work.

    group hermione auto prefix "hermione":
        attribute pose1 default

    group blush auto prefix "blush":
        attribute neutral null default
    group eyes auto prefix "eyes":
        attribute open_forward default
    group eyebrows auto prefix "eyebrows":
        attribute worried default
    group mouth auto prefix "mouth":
        attribute soft default
    group effects auto prefix "effects"

transform her_flirt_public_flitwick_feather:
    align (0.5, 0.5)
    rotate 10
    offset (-60, 40)
    ease_quad 3.0 rotate 5 offset (-30, -20)
    ease_quad 3.0 rotate 10 offset (-60, 40)
    repeat

transform her_flirt_public_flitwick_hermione_hand:
    subpixel True

    align (0.5, 0.5)
    rotate 1
    offset (-25, 10)
    pause 0.2
    ease_quad 2.8 rotate -1 offset (25, 15)
    ease_quad 2.8 rotate 1 offset (-25, 10)
    pause 0.2
    repeat

layeredimage her_flirt_public_flitwick:
    fit "cover"
    fit_first True

    #always "her_flirt_public_flitwick_background"
    always "her_flirt_public_flitwick_hermione"

    attribute feather default at her_flirt_public_flitwick_feather
    attribute hermione_hand default at her_flirt_public_flitwick_hermione_hand

    group hermione_eyes auto prefix "eyes":
        attribute forward default
    group hermione_eyebrows auto prefix "eyebrows":
        attribute neutral default
    group hermione_mouth auto prefix "mouth":
        attribute closed default

    ypan 180

layeredimage her_sex_personal bent_over:
    pos (0, 0)
    fit_first True

    always "her_sex_personal_background"

    group genie auto:
        attribute caress default

    attribute shadow default
    attribute body default
    group cheeks auto prefix "cheeks":
        attribute neutral null default
    group eyes auto prefix "eyes":
        attribute base default
    group tears auto prefix "tears":
        attribute none null default
    group eyebrows auto prefix "eyebrows":
        attribute base default

    group cum_pussy auto prefix "cum_pussy":
        attribute none null default

    group outfit multiple variant "outfit":
        attribute stockings default
        attribute skirt
        attribute shirt

    group mouth auto prefix "mouth":
        attribute base default

    group hair auto prefix "hair":
        attribute normal default

    attribute armfix default

    group outfit multiple variant "outfit_fix":
        attribute shirt

    group mouth prefix "mouth" variant "fix":
        attribute open_wide_tongue
        attribute scream

    group cum_ass auto prefix "cum_ass":
        attribute none null default

    group genie auto variant "armfix":
        attribute caress default

    always "her_sex_personal_background_clutter"

    if game.daytime:
        "her_sex_personal_overlay_day"
    else:
        "her_sex_personal_overlay_night"

layeredimage her_sex_personal lean_back:
    pos (0, 0)
    fit_first True

    always "her_sex_personal_background"

    group genie auto:
        attribute caress default

    attribute body default
    group cheeks auto prefix "cheeks":
        attribute neutral null default
    group eyes auto prefix "eyes":
        attribute base default
    group tears auto prefix "tears":
        attribute none null default
    group eyebrows auto prefix "eyebrows":
        attribute base default

    group hair auto prefix "hair":
        attribute normal default

    attribute armfix default

    group outfit multiple variant "outfit":
        attribute skirt
        attribute shirt

    attribute armfix2 default if_any ["skirt"]

    attribute breastfix default if_not "shirt"

    group mouth auto prefix "mouth":
        attribute base default

    group genie auto variant "armfix"

    always "her_sex_personal_background_clutter"

    if game.daytime:
        "her_sex_personal_overlay_day"
    else:
        "her_sex_personal_overlay_night"

layeredimage her_sex_personal lean_forward:
    pos (0, 0)
    fit_first True

    always "her_sex_personal_background"

    group genie auto:
        attribute caress default

    attribute body default
    group cheeks auto prefix "cheeks":
        attribute neutral null default
    group eyes auto prefix "eyes":
        attribute base default
    group tears auto prefix "tears":
        attribute none null default
    group eyebrows auto prefix "eyebrows":
        attribute base default

    group hair auto prefix "hair":
        attribute normal default

    group outfit multiple variant "outfit":
        attribute skirt
        attribute shirt

    attribute armfix default if_any ["shirt", "skirt"]
    attribute breastfix default if_not "shirt"

    group mouth auto prefix "mouth":
        attribute base default

    group genie auto variant "armfix":
        attribute caress default

    always "her_sex_personal_background_clutter"

    if game.daytime:
        "her_sex_personal_overlay_day"
    else:
        "her_sex_personal_overlay_night"

layeredimage her_forest bj:

    always "her_forest_bj_background"

    group myrtle auto:
        attribute none null default

    group hermione auto:
        attribute none null default

    always "her_forest_bj_overlay"

layeredimage her_titjob_personal:

    always "her_titjob_personal_background"

    group hermione auto:
        attribute none null default

layeredimage her_ball outskirts:
    always "her_ball_outskirts_background"

    group genie auto:
        attribute none null default

    group effect auto:
        attribute none null default

layeredimage her_ball entrance:

    group background auto:
        attribute wall default

    group hermione auto:
        attribute none null default

    group foreground auto:
        attribute none null default

    group background:
        attribute hall "her_ball_entrance_overlay_hall"
        attribute wall "her_ball_entrance_overlay_wall"

layeredimage her_ball blowjob:

    group background auto:
        attribute wall default

    group hermione auto:
        attribute none null default

    group mouth auto prefix "mouth":
        attribute none null default

    group blush auto prefix "blush":
        attribute none null default

    group eyes auto prefix "eyes":
        attribute none null default

    group lashes auto prefix "lashes":
        attribute none null default

    group brows auto prefix "brows":
        attribute none null default

    group mascara auto prefix "mascara":
        attribute none null default

    group tears auto prefix "tears":
        attribute none null default

    group sweat auto prefix "sweat":
        attribute none null default

    group sperm auto prefix "sperm":
        attribute none null default

    group spit auto prefix "spit" multiple:
        attribute none null default

    always "her_ball_entrance_overlay_wall"

layeredimage her_ball speech:

    always "her_ball_speech_background_wall"

    group hermione auto:
        attribute none null default

    group mouth auto prefix "mouth":
        attribute none null default

    group blush auto prefix "blush":
        attribute none null default

    group eyes auto prefix "eyes":
        attribute none null default

    group brows auto prefix "brows":
        attribute none null default

    group mascara auto prefix "mascara":
        attribute none null default

    group sweat auto prefix "sweat":
        attribute none null default

    group sperm auto prefix "sperm":
        attribute none null default

    group foreground auto:
        attribute none null default

    always "her_ball_speech_overlay_bloom"
    always "her_ball_speech_overlay_wall"

layeredimage her_ball sex:

    group background auto:
        attribute wall default

    group hermione auto:
        attribute none null default

    group spank auto prefix "spank":
        attribute none null default

    group guy2 auto prefix "guy2":
        attribute none null default

    group guy1 auto prefix "guy1":
        attribute none null default

    group mouth auto prefix "mouth":
        attribute none null default

    group blush auto prefix "blush":
        attribute none null default

    group eyes auto prefix "eyes":
        attribute none null default

    group brows auto prefix "brows":
        attribute none null default

    group mascara auto prefix "mascara":
        attribute none null default

    group lashes auto prefix "lashes":
        attribute none null default

    group tears auto prefix "tears":
        attribute none null default

    group sperm auto prefix "sperm" multiple:
        attribute none null default

    group spit auto prefix "spit" multiple:
        attribute none null default

    always "her_ball_entrance_overlay_wall"
