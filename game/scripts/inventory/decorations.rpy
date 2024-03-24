
init offset = 2

default agrabah_poster_ITEM = Decoration("agrabah_poster", "decoration", "Agrabah Poster", poster_OBJ, 2, "A remnant of a distant land and memories about different times. A reminder for when you just want to ponder about what could've been.")
default gryffindor_poster_ITEM = Decoration("gryffindor_poster", "decoration", "Gryffindor Poster", poster_OBJ, 2, "Make your stance that you support the house of Gryffindor with this themed poster.")
default ravenclaw_poster_ITEM = Decoration("ravenclaw_poster", "decoration", "Ravenclaw Poster", poster_OBJ, 2, "Make your stance that you support the house of Ravenclaw with this themed poster.")
default hufflepuff_poster_ITEM = Decoration("hufflepuff_poster", "decoration", "Hufflepuff Poster", poster_OBJ, 2, "Make your stance that you support the house of Hufflepuff with this themed poster.")
default slytherin_poster_ITEM = Decoration("slytherin_poster", "decoration", "Slytherin Poster", poster_OBJ, 2, "Make your stance that you support the house of Slytherin with this themed poster.")
default hermione_poster_ITEM = Decoration("hermione_poster", "decoration", "Hermione Poster", poster_OBJ, 2, "A little lewdness for the office. Don't worry, with a special illusion charm no one but you will notice a thing...")
default harlot_poster_ITEM = Decoration("harlot_poster", "decoration", "Hogwarts' Harlot Poster", poster_OBJ, 2, "Hogwarts' Harlot showing off her true colours at last with this special poster... illusion charm included...")
default stripper_poster_ITEM = Decoration("stripper_poster", "decoration", "Stripper Poster", poster_OBJ, 2, "Hermione showing off how to work the pole... illusion charm included...")
default wanted_poster_ITEM = Decoration("wanted_poster", "decoration", "Wanted Poster", poster_OBJ, 2, "A Wild West styled Wanted poster depicting our dear headmaster...")
default tonks_poster_ITEM = Decoration("tonks_poster", "decoration", "Tonks Poster", poster_OBJ, 2, "Professor Tonks in her early twenties.")
default naughty_list_ITEM = Decoration("santas_naughty_list", "decoration", "Santa's Naughty List", poster_OBJ, 2, "See who was a bad boy, or a bad girl this year!", replace_action=Jump("naughty_list"))

default stag_trophy_ITEM = Decoration("stag_trophy", "decoration", "Stag Trophy", trophy_OBJ, 3, "A perfect decoration over your mantelpiece to add a sense of masculinity to the office.")
default crest_trophy_ITEM = Decoration("crest_trophy", "decoration", "Hogwarts Crest", trophy_OBJ, 3, "A perfect decoration for the headmaster.")

default hat_phoenix_ITEM = Decoration("hat_phoenix", "decoration", "Phoenix Hat", phoenix_OBJ, 3, "A little something to make your pet look less depressing.")
default xmas_phoenix_ITEM = Decoration("xmas_phoenix", "decoration", "Phoenix Christmas Set", phoenix_OBJ, 3, "Spreads the Christmas spirit around.")
default halloween_phoenix_ITEM = Decoration("halloween_phoenix", "decoration", "Phoenix Halloween Set", phoenix_OBJ, 3, "A Halloween themed set for your favourite bird!")

default hat_owl_ITEM = Decoration("hat_owl", "decoration", "Owl Hat", owl_OBJ, 3, "A hat for an owl. Don't ask, just accept it...")
default xmas_owl_ITEM = Decoration("xmas_owl", "decoration", "Owl Christmas Set", owl_OBJ, 3, "Spreads the christmas spirit around.")

default hat_fireplace_ITEM = Decoration("hat_fireplace", "decoration", "Fireplace Hat", fireplace_OBJ, 3, "Don't let Johnny get a cold!")
default xmas_fireplace_ITEM = Decoration("xmas_fireplace", "decoration", "Fireplace Christmas Set", fireplace_OBJ, 3, "Spreads the Christmas spirit around.")
default halloween_fireplace_ITEM = Decoration("halloween_fireplace", "decoration", "Fireplace Halloween set #1", fireplace_OBJ, 3, "Adds a spooky pumpkin near your fireplace!")

default halloween_cupboard = Decoration("halloween_cupboard", "decoration", "Cupboard Pumpkin", cupboard_OBJ, 3, "Get in the Halloween spirit with this pumpkin, nobody's eating them so might as well decorate with them!")

default halloween_rug_ITEM = Decoration("halloween_rug", "decoration", "Witch's Rug", rug_OBJ, 5, "Not to be used for unregulated summoning rituals!")
default halloween_chandelier_ITEM = Decoration("halloween_chandelier", "decoration", "Haunted mansion chandelier", chandelier_OBJ, 5, "Adds that haunted mansion vibe...", room_image="halloween_chandelier")
default halloween_fireplace2_ITEM = Decoration("halloween_fireplace2", "decoration", "Jack-Off-Lanterns", fireplace_OBJ, 3, "Spooky scary pumpkins!", room_image="halloween_fireplace_jackolanterns")
default halloween_window_monster = Decoration("halloween_monster", "decoration", "Halloween Peeper", window_OBJ, 5, "Adds a friendly little visitor outside your window, I assure you they don't bite... much.", room_image="halloween_window_monster")
default halloween_cupboard_caskets = Decoration("halloween_cupboard2", "decoration", "Cupboard Halloween Casket", cupboard_OBJ, 3, "A casket decoration, not even big enough to fit your ego.", room_image="halloween_cupboard_caskets")
default halloween_chair_caskets = Decoration("halloween_chair", "decoration", "Chair Halloween Casket", chair_OBJ, 3, "A casket decoration, not even big enough to fit your ego.", room_image="halloween_chair_caskets")
default halloween_bat_trophy_ITEM = Decoration("bats_trophy", "decoration", "Wall Bats Decorations", trophy_OBJ, 3, "Decorate your walls with these envirnomental-friendly paper bat stickers!", room_image="halloween_bats_trophy")
default halloween_lampL_ITEM = Decoration("halloween_lampL", "decoration", "Stolen Graveyard Lamp (Left)", candleL_OBJ, 4, "Replace those candles with a spooky looking lamp.", room_image="halloween_lamp_left", replaces=True, use_action=SetVariable("candleL_OBJ.foreground", None), replace_action=ToggleVariable("candleL_OBJ.foreground", "halloween_lamp_left_glow", None))
default halloween_lampR_ITEM = Decoration("halloween_lampR", "decoration", "Stolen Graveyard Lamp (Right)", candleR_OBJ, 4, "Replace those candles with a spooky looking lamp.", room_image="halloween_lamp_right", replaces=True, use_action=SetVariable("candleR_OBJ.foreground", None), replace_action=ToggleVariable("candleR_OBJ.foreground", "halloween_lamp_right_glow", None))

default snow_owl_ITEM = Decoration("snow_owl", "decoration", "Snow Owl", owl_OBJ, 3, "A trusty snow owl that can travel through the worst of storms.", replaces=True, room_image="snow_owl_letter", room_image_hover="snow_owl_letter_hover")
default small_owl_ITEM = Decoration("small_owl", "decoration", "Small Owl", owl_OBJ, 3, "A cute little owl to deliver cute little parcels.", replaces=True, room_image="small_owl_letter", room_image_hover="small_owl_letter_hover")

default xmas_lights_ITEM = Decoration("xmas_lights", "decoration", "Christmas Lights", chandelier_OBJ, 5, "A programmable set of LED lights. Remote control batteries not included.", replaces=True, room_image="xmas_lights_alternate", replace_action=Jump("xmas_lights_settings"), replace_anchor=(0.0, 0.0), replace_pos=(0, 0))
default xmas_wreaths_ITEM = Decoration("xmas_wreaths", "decoration", "Christmas Wreaths", door_OBJ, 5, "Chrismtas Wreaths to spread the christmas cheer.", room_image="xmas_wreaths")
default xmas_giftchair_ITEM = Decoration("xmas_giftchair", "decoration", "Christmas Wreaths", chair_OBJ, 5, "A baby-sized gift-wrapped box. I wonder what's inside?", room_image="xmas_giftchair")
default xmas_garland_ITEM = Decoration("xmas_garland", "decoration", "Christmas Garland", chandelier_OBJ, 5, "A ever-so-green enchanted garland to get you into christmas spirit!", replace_anchor=(0.0, 0.0), replace_pos=(0, 0))
default xmas_window_santa_ITEM = Decoration("xmas_window_santa", "decoration", "Christmas Window Enchantement", window_OBJ, 5, "A window enchantment that will make you think twice before saying \"I don't believe in Santa\" ever again.", room_image="xmas_window_santa", replace_anchor=(0.0, 0.0), replace_pos=(0,0))
