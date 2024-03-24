
default mr_ev_WPIIA = MirrorEvent(
    id="mr_ev_WPIIA",
    name="Whose points is it anyway?",
    cast =["luna", "astoria", "hermione"],
    desc="Parody of the famous game show, \"Whose points is it anyway?\".",
    label="whose_points",
    authors=["SilverStudioGames"],
    tags=["Humorous","Sexual"],
)

default mr_ev_GHE = MirrorEvent(
    id="mr_ev_GHE",
    name="The Genie, the desk, and the door",
    cast=[],
    desc="You try to figure out how people know when you call for them.",
    label="genie_house_elf",
    authors=["SilverStudioGames"],
    tags=["Humorous"],
    unlocked=True,
)

default mr_ev_AOC = MirrorEvent(
    id="mr_ev_AOC",
    name="An odd circumstance",
    cast=["hermione"],
    desc="You find yourself being confronted by a mysterious girl that seemingly seems to know you.",
    label="an_odd_circumstance",
    authors=["SilverStudioGames"],
    tags=["Humorous","Sexual","Noir"],
    req="states.her.status.blowjob",
)

default mr_ev_ABTTD = MirrorEvent(
    id="mr_ev_ABTTD",
    name="A bad time to disrobe",
    cast=["hermione"],
    desc="You get a hold of a invisibility cloak and put it to good use.",
    label="a_bad_time_to_disrobe",
    authors=["SilverStudioGames"],
    tags=["Sexual","Flashing"],
    req="states.her.status.show_tits",
)

default mr_ev_ASOC = MirrorEvent(
    id="mr_ev_ASOC",
    name="A spaced out conversation",
    cast=[],
    desc="You and Snape get real for a little bit.",
    label="a_spaced_out_conversation",
    authors=["Ignatz"],
    tags=["Noir"],
    req="states.sna.level > 60",
)

default mr_ev_ABAS = MirrorEvent(
    id="mr_ev_ABAS",
    name="Booty at sea",
    cast=["hermione"],
    desc="You imagine yourself a great pirate and replay your most intimate times with Hermione.",
    label="anal_pirate_event",
    label_rewards="anal_pirate_rewards",
    authors=["SilverStudioGames"],
    tags=["Humorous", "Sexual"],
    req="states.her.status.anal",
)

# BROKEN
#
# default mr_ev_ADR = MirrorEvent(
#     id="mr_ev_ADR",
#     name="A Dark Room",
#     cast=[],
#     desc="A minigame inspired by the text-based game \"A Dark Room\".\n>It is currently incomplete but in a playable state.",
#     label="start_dark_room_game",
#     authors=["SilverStudioGames"],
#     tags=["Minigame", "Noir"],
#     unlocked=True,
# )

default mr_ev_AXmasTale = MirrorEvent(
    id="mr_ev_AXmasTale",
    name="A Christmas Tale",
    cast=[],
    desc="A surprise visit in the time of need.",
    label="a_christmas_tale",
    label_rewards="a_christmas_tale_rewards",
    authors=["SilverStudioGames"],
    tags=["Seasonal", "Noir"],
    unlocked=True,
)

default mr_ev_AXmasTale2 = MirrorEvent(
    id="mr_ev_AXmasTale2",
    name="Santa's Little Helper",
    cast=[],
    desc="The tall broody guy is about to get his present.",
    label="a_christmas_tale2",
    label_rewards="a_christmas_tale2_rewards",
    authors=["SilverStudioGames"],
    tags=["Seasonal", "Noir"],
    unlocked=True,
)

default mr_ev_PaH = MirrorEvent(
    id="mr_ev_PaH",
    name="Previously at Hogwarts",
    cast=[],
    desc="Snape tries to find a solution to stifle his anger and finds himself yet again in the headmaster's office.",
    label="prev_at_hogwarts",
    authors=["SilverStudioGames"],
    tags=["Noir"],
    unlocked=True,
)

default mr_ev_PR = MirrorEvent(
    id="mr_ev_PR",
    name="Panty Raid",
    cast=["hermione"],
    desc="You ask Hermione to go out and collect other girls panties.",
    label="panty_raid",
    authors=["WaxerRed"],
    tags=["Sexual", "Fetish"],
    req="states.her.level > 15",
)

default mr_ev_EFP = MirrorEvent(
    id="mr_ev_EFP",
    name="Eating for pleasure",
    cast=["hermione"],
    desc="You get hungry and decide to get something to eat.",
    label="eating_for_pleasure",
    label_rewards="eating_for_pleasure_rewards",
    authors=["SilverStudioGames"],
    tags=["Humorous", "Sexual", "Fetish"],
)

default mr_ev_SNR = MirrorEvent(
    id="mr_ev_SNR",
    name="Suck & Run",
    cast=["tonks"],
    desc="Someone or {i}something{/i} is sucking the life force out of the students.",
    label="suck_and_run",
    label_rewards="suck_and_run_rewards",
    authors=["SilverStudioGames"],
    tags=["Seasonal", "Sexual", "Fetish"],
)

default mr_ev_BD = MirrorEvent(
    id="mr_ev_BD",
    name="Biggus Dickus",
    cast=["hermione"],
    desc="Hermione comes to you with an odd request.",
    label="biggus_dickus",
    authors=["Livvypoo"],
    tags=["Humorous","Sexual"],
)

default mr_ev_NSGE = MirrorEvent(
    id="mr_ev_NSGE",
    name="A not so great escape",
    cast=["tonks", "cho", "luna"],
    desc="You find yourself in a bit of a pickle.",
    label="not_so_great_escape",
    label_rewards="not_so_great_escape_rewards",
    authors=["SilverStudioGames"],
    tags=["Seasonal", "Humorous"],
    unlocked=True,
)

default mr_ev_WC = MirrorEvent(
    id="mr_ev_WC",
    name="A white Christmas",
    cast=["tonks", "hermione"],
    desc="Genie is not so happy with the narration and decides to take it into his own hands.",
    label="a_white_christmas",
    label_rewards="a_white_christmas_rewards",
    authors=["SilverStudioGames"],
    tags=["Seasonal", "Humorous", "Sexual"],
    unlocked=True,
)

default mr_ev_BBB = MirrorEvent(
    id="mr_ev_BBB",
    name="Blueballing bad",
    cast=["tonks", "hermione"],
    desc="In an alternate universe where Genie never followed his urges.",
    label="blueballing_bad",
    label_rewards="blueballing_bad_rewards",
    authors=["NotTera"],
    tags=["Humorous", "Flashing"],
    unlocked=True,
)

default mr_ev_GCW = MirrorEvent(
    id="mr_ev_GCW",
    name="Genie's Christmas Wish",
    cast=["genie"],
    desc="",
    label="genies_christmas_wish",
    label_rewards="genies_christmas_wish_rewards",
    authors=["SilverStudioGames"],
    tags=["Seasonal", "Noir"],
    unlocked=True,
)
