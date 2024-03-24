
init 5 python:
    def her_cg_doll(st, at):
        return hermione.image, None

    def lun_cg_doll(st, at):
        return luna.image, None

    def ton_cg_doll(st, at):
        return tonks.image, None

    def cho_cg_doll(st, at):
        return cho.image, None

    def ast_cg_doll(st, at):
        return astoria.image, None

    def sus_cg_doll(st, at):
        return susan.image, None

image CG her_doll = DynamicDisplayable(her_cg_doll)
image CG lun_doll = DynamicDisplayable(lun_cg_doll)
image CG ton_doll = DynamicDisplayable(ton_cg_doll)
image CG cho_doll = DynamicDisplayable(cho_cg_doll)
image CG ast_doll = DynamicDisplayable(ast_cg_doll)
image CG sus_doll = DynamicDisplayable(sus_cg_doll)

image CG luna = Fixed(
    "images/CG/common/bg.webp",
    AlphaMask(Composite((2160, 1200), (880, -180), Transform("CG lun_doll", zoom=1.2)), "images/CG/common/mask.webp"),
    )

image CG hermione = Fixed(
    "images/CG/common/bg.webp",
    AlphaMask(Composite((2160, 1200), (880, -180), Transform("CG her_doll", zoom=1.2)), "images/CG/common/mask.webp"),
    )

image CG tonks = Fixed(
    "images/CG/common/bg.webp",
    AlphaMask(Composite((2160, 1200), (880, -180), Transform("CG ton_doll", zoom=1.2)), "images/CG/common/mask.webp"),
    )

image CG cho = Fixed(
    "images/CG/common/bg.webp",
    AlphaMask(Composite((2160, 1200), (880, -180), Transform("CG cho_doll", zoom=1.2)), "images/CG/common/mask.webp"),
    )

image CG astoria = Fixed(
    "images/CG/common/bg.webp",
    AlphaMask(Composite((2160, 1200), (880, -180), Transform("CG ast_doll", zoom=1.2)), "images/CG/common/mask.webp"),
    )

image CG susan = Fixed(
    "images/CG/common/bg.webp",
    AlphaMask(Composite((2160, 1200), (880, -180), Transform("CG sus_doll", zoom=1.2)), "images/CG/common/mask.webp"),
    )

# Snape CG
screen snape_groping():
    add "images/CG/scene_01.webp" zoom 0.5
    zorder 14

screen snape_facial():
    add "images/CG/scene_03.webp" zoom 0.5
    zorder 14

screen snape_sex():
    add "images/CG/scene_04.webp" zoom 0.5
    zorder 14

screen dual_hand_job():
    add "images/CG/scene_02.webp" zoom 0.5
    zorder 14
