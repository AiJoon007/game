
# Preferences
# https://www.renpy.org/doc/html/preferences.html

# Note: Only use default keyword for renpy preferences. Use settings.default for custom ones.
default preferences.text_cps = 40
default preferences.afm_time = 15
default preferences.pad_enabled = False
default preferences.renderer = "auto"
default preferences.gl_powersave = False
default preferences.audio_when_minimized = False

init python:
    settings.default("theme", "auto")
    settings.default("text_color_day", "#402313ff")
    settings.default("text_color_night", "#341c0fff")
    settings.default("text_outline", "#00000000")
    settings.default("tooltip", True)
    settings.default("tutorials", True)
    settings.default("preserve_aspect_ratio", True)
    settings.default("animations", True)
    settings.default("updates", True)
    settings.default("image_cache_size", 512)
    settings.default("multithreading", True)

    renpy.music.register_channel("background", "sfx", True)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("weather", "weather", True)

# Configuration
# https://www.renpy.org/doc/html/config.html

# Pre-Release related flags and variables
define prerelease = False
define config.autoreload = False
define config.developer = "auto"
define config.debug = config.developer or prerelease
define config.console = True

# Game version and naming
define config.version = "1.45.3"
define compatible_version = 1.451
define config.name = "Witch Trainer Silver"


# Application window settings
define config.window_title = f"{config.name} (v{config.version}{' PRE-RELEASE' if prerelease else ''}) ({get_renderer()}) ({renpy.bits}-bit)"
define config.window_icon = "gui/icon.webp"
define config.screen_width = 1080
define config.screen_height = 600
define config.physical_width = 1280
define config.physical_height = 720
define config.save_physical_size = True

# User interface settings
define config.layers = ["master", "transient", "screens", "overlay"]
define config.default_tag_layer = "screens"
define config.top_layers = ["interface"]
define config.transparent_tile = False
define config.narrator_menu = True
define config.hard_rollback_limit = 100
define config.history_length = 250
define config.mouse = {"default": [("interface/cursor.webp", 0, 0)]}
define config.help = None
define config.side_image_only_not_showing = True
define config.allow_underfull_grids = True
define config.crop_relative_default = False

# Graphics and cache settings
define config.gl2 = True
define config.gl_enable = True
define config.gl_resize = True
define config.gl_clear_color = "#000"
define config.hw_video = True
define config.nearest_neighbor = False
define config.atl_start_on_show = False # Enables compatibility for ATL behaviour after Ren'py 7.4.7
# define config.use_drawable_resolution = (not renpy.android)
# define config.drawable_resolution_text = True
define config.cache_surfaces = False
define config.image_cache_size = None
define config.image_cache_size_mb = settings.get("image_cache_size")
define config.load_before_transition = True
define config.imagemap_cache = True
define config.optimize_texture_bounds = True
define config.debug_image_cache = False
# define config.atl_one_frame = False
define config.tag_zorder = {
    "xray_child": -1,
    "xray_overlay": -1,
    "xray_mask": -1,
    "cg": 17,
}

# Saving and loading
define config.save_directory = "Witch Trainer Silver"
define config.has_autosave = True
define config.autosave_on_quit = True
define config.autosave_on_choice = True
define config.autosave_frequency = 200
define config.autosave_slots = 12

# Sound and music
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.sound_sample_rate = 48000
define config.main_menu_music = "music/aquarium-by-kevin-macleod.ogg"
define config.fadeout_audio = 1.0
define config.default_music_volume = 0.8
define config.default_sfx_volume = 1.0

# Transitions
define config.enter_transition = f3
define config.exit_transition = f3
define config.intra_transition = d1
define config.main_game_transition = f3
define config.game_main_transition = f3
define config.end_splash_transition = d3
define config.end_game_transition = fade
define config.after_load_transition = fade
define config.window_show_transition = d3
define config.window_hide_transition = d3
define config.adv_nvl_transition = d3
define config.nvl_adv_transition = d3
define config.enter_yesno_transition = None
define config.exit_yesno_transition = None
define config.enter_replay_transition = None
define config.exit_replay_transition = None
define config.say_attribute_transition = d3

# Python
define config.open_file_encoding = "utf-8"

# Debug
define config.profile = False

# Garbage Collector
# define config.manage_gc = True
# define config.gc_thresholds = (25000, 10, 10)
# define config.idle_gc_count = 10000
# define config.gc_print_unreachable = False

################################################
##           Build configuration              ##
##      For information please refer to:      ##
## https://www.renpy.org/doc/html/build.html  ##
################################################

init python:
    build.name = "WTS"
    build.directory_name = f"WTS-{config.version}"
    build.include_update = True
    build.include_old_themes = False
    build.exclude_empty_directories = True

    build.classify("**.rpy", "renpy")
    build.classify("**.rpyc", "all")
    build.classify("game/images.whitespace", "all")
    build.classify("**.webp", "all")
    build.classify("**.webm", "all")
    build.classify("**.ogg", "all")

    build.classify("game/gui/**", "all")
    build.classify("android-icon_*.png", "android")
    build.classify("android-presplash.jpg", "android")
    build.classify("icon.icns", "mac")
    build.classify("icon.ico", "windows")
    build.classify("game/presplash_*.png", "renpy")
    build.classify("game/outfits/**", "all")
    build.classify("game/mods/ExampleMod/**", "all")
    build.classify("update/generic.webp", "pc mac")

    build.classify("**.py", None)
    build.classify("**.txt", None)
    build.classify("**.md", None)
    build.classify("**.png", None)
    build.classify("**.jpg", None)
    build.classify("**.jpeg", None)
    build.classify("**.json", None)
    build.classify("LICENSE", None)
    build.classify("**.bak", None)
    build.classify("**.old", None)
    build.classify("**~", None)
    build.classify("**.db", None)
    build.classify("**.zip", None)

    build.classify("cache/**", "android")
    build.classify("game/saves/**", None)
    build.classify("game/mods/**", None)

    # build.android_permissions = ["android.permission.WRITE_EXTERNAL_STORAGE"] # Not functional since API level 30+
