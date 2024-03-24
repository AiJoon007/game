init python:
    def genie_transform(trans, st, at):
        trans.xpos = states.gen.image.xpos
        trans.ypos = states.gen.image.ypos
        trans.zoom = states.gen.image.zoom
        trans.xzoom = states.gen.image.xzoom
        trans.offset = states.gen.image.offset
        return 0

layeredimage genie_stats:
    anchor (0.0, 1.0)

    always "characters/genie/base.webp"
    always "characters/genie/outfits/robes.webp"
    always "characters/genie/outfits/robes_beard.webp"

    # TODO: Add outfit support; Low priority

layeredimage genie:
    anchor (0.0, 1.0)

    group outfit:
        attribute robes default null
        attribute nude "characters/genie/hair.webp"

    always "characters/genie/base.webp"

    group face:
        attribute base default null
        attribute grin "characters/genie/grin.webp"
        attribute angry "characters/genie/angry.webp"
        attribute smile "characters/genie/smile.webp"
        attribute open "characters/genie/open.webp"

    group outfit:
        attribute robes default "characters/genie/outfits/robes.webp"
        attribute nude null
        attribute santa "characters/genie/outfits/santa.webp"

    group face multiple:
        attribute robes default "characters/genie/outfits/robes_beard.webp" if_all ["robes"]
        attribute nude "characters/genie/beard.webp" if_all ["nude"]
        attribute base "characters/genie/outfits/santa_beard_base.webp" if_all ["santa", "base"]
        attribute grin "characters/genie/outfits/santa_beard_grin.webp" if_all ["santa", "grin"]
        attribute angry "characters/genie/outfits/santa_beard_angry.webp" if_all ["santa", "angry"]
        attribute smile "characters/genie/outfits/santa_beard_smile.webp" if_all ["santa", "smile"]
        attribute open "characters/genie/outfits/santa_beard_open.webp" if_all ["santa", "open"]

    at Transform(function=genie_transform)

image side genie = LayeredImageProxy("genie")
