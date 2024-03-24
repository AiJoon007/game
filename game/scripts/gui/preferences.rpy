#
# Preferences screen
#
# The preferences screen allows the player to configure the game to better suit
# themselves.
#
# https://www.renpy.org/doc/html/screen_special.html#preferences

init offset = -1

screen preferences(page="general"):
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):
        style_prefix gui.theme("pref")

        vbox:
            spacing gui.pref_spacing
            null # Tab margin

            if page == "general":
                use preferences_general
            elif page == "visuals":
                use preferences_visuals
            elif page == "sound":
                use preferences_sound
            elif page == "accessibility":
                use preferences_accessibility

    hbox:
        style_prefix gui.theme("tab")
        pos (25 + 15, 100)
        yanchor 0.5

        textbutton "General":
            selected (page == "general")
            action Show("preferences", config.intra_transition, "general")

        textbutton "Visuals":
            selected (page == "visuals")
            action Show("preferences", config.intra_transition, "visuals")

        textbutton "Sound":
            selected (page == "sound")
            action Show("preferences", config.intra_transition, "sound")

        textbutton "Accessibility":
            selected (page == "accessibility")
            action Show("preferences", config.intra_transition, "accessibility")

screen preferences_general():
    hbox:
        box_wrap True

        vbox:
            style_prefix gui.theme("check")

            label _("Interface")
            textbutton _("Animations") action settings.Toggle("animations")
            textbutton _("Tutorials") action settings.Toggle("tutorials")

            if not renpy.mobile:
                textbutton _("Tooltips") action settings.Toggle("tooltip")
                textbutton _("System Cursor") action Preference("system cursor", "toggle")
                textbutton _("Automatic Updates") action settings.Toggle("updates")
                textbutton _("Autosave") action ToggleField(store, "_autosave")

        default trans = config.intra_transition

        vbox:
            style_prefix gui.theme("radio")

            label "Theme"
            textbutton "Auto" action [
                settings.Set("theme", "auto"),
                Function(renpy.transition, trans),
                Function(renpy.restart_interaction)
            ]
            textbutton "Day" action [
                settings.Set("theme", "light"),
                Function(renpy.transition, trans),
                Function(renpy.restart_interaction)
            ]
            textbutton "Night" action [
                settings.Set("theme", "dark"),
                Function(renpy.transition, trans),
                Function(renpy.restart_interaction)
            ]
        vbox:
            style_prefix gui.theme("check")
            label _("Skipping")
            textbutton _("Skip Unseen Text") action Preference("skip", "toggle")
            textbutton _("Until dialog menu") action InvertSelected(Preference("after choices", "toggle"))

    hbox:
        box_wrap True

        vbox:
            style_prefix gui.theme("slider")
            spacing gui.pref_spacing / 2

            label _("Text Speed")
            bar value Preference("text speed")

            label _("Auto-Forward Time")
            bar value Preference("auto-forward time")

    hbox:
        box_wrap True

        vbox:
            style_prefix gui.theme("check")

screen preferences_visuals():
    vbox:
        hbox:
            box_wrap True

            if renpy.variant("pc") or renpy.variant("web"):
                vbox:
                    style_prefix gui.theme("radio")
                    label _("Display")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    textbutton _("Windowed") action Preference("display", "any window")
                    textbutton _("V-Sync") action [ InvertSelected(ToggleField(_preferences, "gl_tearing")), _DisplayReset() ] style gui.theme("check_button")

                    # Probably redundant now that we have aspect ratio preservation.
                    # if not preferences.fullscreen:
                    #     textbutton _("Reset window"):
                    #         action Preference("display", "window")
                    #         sensitive (renpy.get_physical_size() != (config.screen_width, config.screen_height))


            vbox:
                style_prefix gui.theme("radio")

                default fps_msg = "Framerate preference may take effect after restarting the game"

                label "Framerate"

                textbutton ("{} fps".format(int(renpy.get_refresh_rate()))) action [Preference("gl framerate", None), Notify(fps_msg)]
                if renpy.get_refresh_rate() > 60:
                    textbutton "60 fps" action [Preference("gl framerate", 60), Notify(fps_msg)]
                textbutton "30 fps" action [Preference("gl framerate", 30), Notify(fps_msg)]

            if not renpy.mobile:
                vbox:
                    style_prefix gui.theme("radio")

                    label _("Renderer")

                    default renderer_used = renpy.get_renderer_info()["renderer"]

                    textbutton _("OpenGL"):
                        selected renderer_used == "gl2"
                        action Confirm("Changing renderer requires a full restart, do it now?\nUnsaved progress will be lost.", Function(set_renderer, "gl2"))
                    textbutton _("DirectX"):
                        sensitive renpy.windows
                        selected renderer_used == "angle2"
                        action Confirm("Changing renderer requires a full restart, do it now?\nUnsaved progress will be lost.", Function(set_renderer, "angle2"))

            vbox:
                style_prefix gui.theme("check")

                label "Advanced"

                textbutton _("Transitions") action Preference("transitions", "toggle")
                textbutton _("Videos") action InvertSelected(Preference("video sprites", "toggle"))
                textbutton _("Power-saving") action Preference("gl powersave", "toggle")
                textbutton _("multithreading") action settings.Toggle("multithreading") tooltip "Improves performance by executing tasks asynchronously. (Requires restart)"
                #if not renpy.mobile:
                    #textbutton _("Preserve Aspect Ratio") action [settings.Toggle("preserve_aspect_ratio"), _DisplayReset()]

        vbox:
            style_prefix gui.theme("slider")

            label _("Image cache ([persistent.custom_settings[image_cache_size]]MB)")

            hbox:
                bar value DictValue(persistent.custom_settings, "image_cache_size", range=1792, max_is_zero=False, style="slider", offset=256, step=128, force_step=True, action=Notify("Restart the game to apply image cache size changes.")) tooltip "Improves performance at a cost of higher memory usage."
        
        text get_gpu_info() yalign 1.0 size 10

screen preferences_sound():
    hbox:
        box_wrap True

        vbox:
            style_prefix gui.theme("slider")
            spacing gui.pref_spacing / 2

            if config.has_music:
                label _("Music Volume")
                hbox:
                    bar value Preference("music volume")

            if config.has_sound:
                label _("Sound Volume")
                hbox:
                    bar value Preference("sound volume")
                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)

                label _("Weather Volume")
                hbox:
                    bar value Preference("weather volume")
                    if config.sample_sound:
                        textbutton _("Test") action Play("weather", config.sample_sound)

            if config.has_voice:
                label _("Voice Volume")
                hbox:
                    bar value Preference("voice volume")
                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style gui.theme("check_button")

                textbutton _("Mute when minimized"):
                    action Preference("audio when minimized", "toggle")
                    selected (not _preferences.audio_when_minimized)
                    style gui.theme("check_button")

screen preferences_accessibility():

    vbox:
        text "Disclaimer" size 18 xalign 0.5
        hbox:
            xmaximum 731
            text "These menu options are intended to improve accessibility and may not work well in all cases where text might overflow. When changing font, text size or spacing try to keep it close to the default size." size 14

    hbox:
        box_wrap True

        vbox:
            style_prefix gui.theme("radio")

            label _("Text Font")

            textbutton _("Default"):
                action Preference("font transform", None)

            textbutton _("DejaVu Sans"):
                action Preference("font transform", "dejavusans")

            textbutton _("Opendyslexic"):
                action Preference("font transform", "opendyslexic")

        vbox:

            label _("Text Scaling")

            hbox:
                style_prefix gui.theme("radio")

                textbutton "V. small" action Preference("font size", 0.7)
                textbutton "Small" action Preference("font size", 0.9)
                textbutton "Normal" action Preference("font size", 1.0)
                textbutton "Large" action Preference("font size", 1.2)
                textbutton "V. Large" action Preference("font size", 1.4)

            label _("Vertical Text Spacing")

            hbox:
                style_prefix gui.theme("radio")

                textbutton "V. small" action Preference("font line spacing", 0.7)
                textbutton "Small" action Preference("font line spacing", 0.9)
                textbutton "Normal" action Preference("font line spacing", 1.0)
                textbutton "Large" action Preference("font line spacing", 1.2)
                textbutton "V. Large" action Preference("font line spacing", 1.4)

    if not renpy.mobile:
        hbox:
            vbox:
                style_prefix gui.theme("check")

                label _("Text-to-speech")

                textbutton _("Text-to-speech"):
                    action Preference("self voicing", "toggle")

            vbox:
                style_prefix gui.theme("slider")

                label _("Text-to-speech Accentuation")

                bar value Preference("self voicing volume drop")

    vbox:
        label _("Advanced")

        textbutton "Delete persistent data ({color=#f00}!{/color})":
            style gui.theme("pref_button")
            action Confirm(gui.CONFIRM_DELETE_PERSISTENT, Function(delete_persistent))

        textbutton "Delete save files ({color=#f00}!{/color})":
            style gui.theme("pref_button")
            action Confirm(gui.CONFIRM_DELETE_SAVES, Function(delete_saves))

        if renpy.android:
            label _("Android Crash Defender")

            hbox:
                style_prefix gui.theme("radio")

                textbutton "Aggressive" action [settings.Set("crashdefendersetting", 3), Function(crashdefender.set_mode, 3)]
                textbutton "Balanced" action [settings.Set("crashdefendersetting", 2), Function(crashdefender.set_mode, 2)]
                textbutton "Relaxed" action [settings.Set("crashdefendersetting", 1), Function(crashdefender.set_mode, 1)]
                textbutton "Off" action [settings.Set("crashdefendersetting", 0), Function(crashdefender.set_mode, 0)]

define gui.CONFIRM_DELETE_PERSISTENT = """{color=#7a0000}Warning!{/color}
{size=-4}You are about to reset all persistent data, including
achievements, seen text, and preferences.{/size}\n
Are you sure?"""

define gui.CONFIRM_DELETE_SAVES = """{color=#7a0000}Warning!{/color}
{size=-4}You are about to delete all save files, including
auto saves, quick saves, and manual saves.{/size}\n
Are you sure?"""

define gui.SAVE_INCOMPATIBLE_WARNING = """{color=#7a0000}Warning!{/color}
{size=-4}The save file you are attempting to load is not compatible 
with the current game version. While you can try loading it, 
doing so may result in unexpected crashes and bugs. 

Proceed anyway?"""

init python:
    def delete_persistent():
        renpy.loadsave.location.unlink_persistent()
        renpy.persistent.should_save_persistent = False
        renpy.quit(relaunch=True)

    def delete_saves():
        for fn in renpy.list_saved_games(fast=True):
            renpy.unlink_save(fn)

    def set_renderer(s):
        preferences.renderer = s if s in ("gl2", "angle2") else "auto"
        renpy.quit(relaunch=True)

style mute_all_button is check_button
style mute_all_button_text is check_button_text

# Preference

style pref_label is gui_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text is gui_label_text:
    yalign 1.0

style dark_pref_label_text is dark_label_text
style light_pref_label_text is light_label_text

style pref_button is gui_button:
    padding (18, 4, 4, 4)

style pref_button_text is gui_button_text

style pref_vbox is vbox:
    xminimum (245 - 30 - 60) / 2

style pref_hbox:
    spacing 30
    box_wrap_spacing 2 * gui.pref_spacing

# Radio button

style radio_label is pref_label
style radio_label_text is pref_label_text
style dark_radio_label_text is dark_pref_label_text
style light_radio_label_text is light_pref_label_text

style radio_vbox is pref_vbox:
    spacing gui.pref_button_spacing

style radio_button is gui_button:
    background None
    padding (18, 4, 4, 4)

style dark_radio_button is dark_gui_button:
    take radio_button
    foreground "dark_radio_false"
    selected_foreground "dark_radio_true"
    insensitive_foreground "dark_radio_none"

style light_radio_button is light_gui_button:
    take radio_button
    foreground "light_radio_false"
    selected_foreground "light_radio_true"
    insensitive_foreground "light_radio_none"

style radio_button_text is gui_button_text:
    first_indent 6

# Check button

style check_label is pref_label
style check_label_text is pref_label_text
style dark_check_label_text is dark_pref_label_text
style light_check_label_text is light_pref_label_text

style check_vbox is pref_vbox:
    spacing gui.pref_button_spacing

style check_button is gui_button:
    background None
    padding (18, 4, 4, 4)

style dark_check_button is dark_gui_button:
    take check_button
    foreground "dark_check_false"
    selected_foreground "dark_check_true"
    insensitive_foreground "dark_check_none"

style light_check_button is light_gui_button:
    take check_button
    foreground "light_check_false"
    selected_foreground "light_check_true"
    insensitive_foreground "light_check_none"

style check_button_text is gui_button_text:
    first_indent 6

# Slider

style slider_label is pref_label
style slider_label_text is pref_label_text
style dark_slider_label_text is dark_pref_label_text
style light_slider_label_text is light_pref_label_text

style slider_slider is gui_slider:
    xsize 320

style dark_slider_slider is dark_slider
style light_slider_slider is light_slider

style slider_button is gui_button:
    background None
    yalign 0.5
    left_margin 9

style slider_button_text is gui_button_text

style slider_vbox is pref_vbox:
    xsize 320

screen _self_voicing():
    zorder 1500

    if _preferences.self_voicing == "clipboard":
        $ message = _("Clipboard voicing enabled. Press 'shift+C' to disable.")
    elif _preferences.self_voicing == "debug":
        $ message = _("Text-to-speech would say \"[renpy.display.tts.last]\". Press 'alt+shift+V' to disable.")
    else:
        $ message = _("Text-to-speech enabled. Press 'shift+v' to disable.")

    text message:
        alt ""

        xpos 10
        ypos 35
        color "#fff"
        outlines [ (1, "#0008", 0, 0)]
