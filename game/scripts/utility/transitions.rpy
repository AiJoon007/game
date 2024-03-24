
image fade = "#00000080"
image fade_gradient = "interface/bld.webp"

# Transitions
init offset = -1
define d1 = Dissolve(0.1)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d4 = Dissolve(0.4)
define d5 = Dissolve(0.5)
define d6 = Dissolve(0.6)
define d7 = Dissolve(0.7)
define d8 = Dissolve(0.8)
define d9 = Dissolve(0.9)

define f1 = Fade(0.1, 0.0, 0.1)
define f2 = Fade(0.2, 0.0, 0.2)
define f3 = Fade(0.3, 0.0, 0.3)

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define flashbb = Fade(0.2, 0.0, 0.8, color='#000')
define flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
define kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')
define black_magic = Fade(0.2, 0.0, 0.5, color='#7f3590')
define blackfade = Fade(0.9, 0.5, 1, color='#000000')

define morph = ComposeTransition(Dissolve(0.9), before=Fade(0.1, 0.5, 0.5, color="#fff"), after=Dissolve(0.5))
define teleport = ImageDissolve("id_teleport.webp", 1.0, 0)

define faderight = ImageDissolve("interface/transitions/faderight.webp", 1.0)
define fadeleft = ImageDissolve("interface/transitions/faderight.webp", 1.0, reverse=True)
