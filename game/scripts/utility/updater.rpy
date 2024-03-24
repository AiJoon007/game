init python:
    import requests

    UPDATE_URL = bytes.fromhex("687474703a2f2f757064617465732e73696c76657273747564696f67616d65732e6f7267").decode()
    UPDATE_VER = None
    UPDATE_HINT = ""

    if config.developer:
        persistent._update_version = {}
        persistent._update_last_checked = {}

    @renpy.pure
    class CheckUpdates(Action):
        def __init__(self, interval=3600*6, simulate=None, onetime=False, autostart=True, **kwargs):
            self.url = UPDATE_URL
            self.interval = interval
            self.simulate = simulate
            self.onetime = onetime
            self.autostart = autostart
            self.kwargs = kwargs

        def __call__(self):
            # Since source files are publicly available,
            # we need to forbid updater from affecting
            # GIT-supplied versions of the game to avoid bugs.

            global UPDATE_VER, UPDATE_HINT

            if (config.developer or not updater.can_update()) and not self.simulate:

                if config.developer:
                    UPDATE_HINT = "Updater is disabled."
                else:
                    UPDATE_HINT = "Cannot fetch updates."

                renpy.restart_interaction()
                return

            check = True
            url = self.url

            if not self.onetime:
                UPDATE_HINT = "Checking for updates..."
                renpy.restart_interaction()

            if self.onetime and url in updater.checked:
                check = False

            if time.time() < persistent._update_last_checked.get(url, 0) + self.interval:
                check = False

            if check:
                updater.checked.add(url)
                persistent._update_last_checked[url] = time.time()
                updater.Updater(url, check_only=True, simulate=self.simulate, **self.kwargs)

            UPDATE_VER = persistent._update_version.get(url, None)

            if version_float(UPDATE_VER) > version_float():
                if not self.onetime:
                    UPDATE_HINT = "New game version available!"
                    renpy.restart_interaction()

                if self.autostart:
                    renpy.invoke_in_new_context(updater.update, self.url, simulate=self.simulate, **self.kwargs)
            # elif not UPDATE_VER:
            #     ui.timer(2.0, SetVariable("UPDATE_HINT", "Server is not responding."))
            elif not self.onetime:
                ui.timer(2.0, SetVariable("UPDATE_HINT", "You are already up-to-date."))

    @renpy.pure
    class InstallUpdates(Action):
        def __init__(self, simulate=None, **kwargs):
            self.url = UPDATE_URL
            self.simulate = simulate
            self.kwargs = kwargs

        def __call__(self):
            renpy.invoke_in_new_context(updater.update, self.url, simulate=self.simulate, **self.kwargs)

    def fix_return_stack():
        for layer in config.layers:
            renpy.scene(layer)

        for channel in renpy.audio.audio.channels.keys():
            if isinstance(channel, str) and not channel.startswith("_"):
                renpy.music.stop(channel)

        renpy.set_return_stack(("main_room",))

    def version_float(version=None):
        version = version or config.version

        control, major, *minor = version.split(" ")[0].split(".")
        return float("{}.{}{}".format(control, major, "".join(minor)))

    def version_patch():
        if renpy.is_init_phase():
            # Don't update save files from when game recovers from a crash.
            return

        latest = version_float()
        # For unknown reasons, sometimes version is missing from the save, so we need a fallback
        current = getattr(renpy.store, "version", latest)

        if current < 1.452:
            
            for i in states.dolls:
                doll = getattr(store, i)
                doll._sprite = DefaultQueue()

                for j in doll.wardrobe_list:
                    # Add new button handler for clothes
                    j._button = DefaultQueue()

                for j in doll.outfits:
                    # Add new button handler for outfits
                    j._button = DefaultQueue()

                    # Fix makeup object types inside saved outfits
                    if j.has_type("makeup"):
                        
                        objects = [x.parent.clone() for x in j.group]

                        j.group = objects
                        j.is_stale()

            # Patch removed events
            events = ["her_ev_handjob_t1_to_t3_e1", "her_ev_titjob_t1_to_t4_e1", "her_ev_sex_t1_to_t5_e1", "her_ev_panty_thief_t1_to_t3"]

            for i in events:
                ev = getattr(store, i, None)

                if ev:
                    ev.dequeue()
                    delattr(store, i)

            # Fix cardgame events
            delattr(states.twi.ev.cardgame, "delay")

            if states.twi.ev.cardgame.stage == 1 and not states.twi.ev.cardgame.stock_talk and not letter_cards_store in mailbox.letters:
                # In case the player already started the event chain, send the letter early.
                letter_cards_store.send()

            getattr(store, "letter_cards_store").wait = 7

            # Fix revertable types for modding
            mods_enabled = getattr(persistent, "mods_enabled", _set()) or _set()
            setattr(persistent, "mods_enabled", _set(mods_enabled))

            mods_list = getattr(persistent, "mods_list", _dict()) or _dict()
            setattr(persistent, "mods_list", _dict(mods_list))

            # Fix event issue with Cho
            ev = getattr(store, "cho_ev_inspect_her_body_t2_e3")
            if ev.completed and not states.cho.ev.inspect_her_body.T2_E3_complete:
                states.cho.ev.inspect_her_body.T2_E3_complete = True

        if current < 1.453:
            for i in states.dolls:
                doll = getattr(store, i)

                for j in doll.outfits:

                    for k in j.group:
                        if k.modpath:
                            k.modpath = "mods/" + k.modpath.split("/")[-1]

        if current > latest:
            raise Exception("Loaded save file is incompatible. (Save Version: {}, Game Version: {})".format(current, latest))

        if current < latest:
            setattr(renpy.store, "version", latest)
            message = "Have fun!"

            achievements.attempt_repair()

            renpy.call_in_new_context("modal_popup", "Update Successful", "\nYour save file has been successfully updated to version {{b}}{}{{/b}}.\n\n{}".format(config.version, message), None, "Hurray!")

            renpy.block_rollback()
        return

    def version_logo():
        url = UPDATE_URL
        filename = "logo_{}.webp".format(UPDATE_VER)
        path = os.path.join(config.basedir, "update", filename)

        # Read file if exists
        if os.path.isfile(path):
            with open(path, "rb") as f:
                data = f.read()
                return im.Data(data, path)

        # Fetch file if doesn't exist
        url = os.path.join(url.split("updates.json")[0], "logo.webp")

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.content

            with open(path, "wb") as f:
                f.write(data)

            return im.Data(data, path)
        except:
            path = os.path.join(config.basedir, "update", "generic.webp")

            if os.path.isfile(path):
                with open(path, "rb") as f:
                    data = f.read()
            else:
                return Null()

            return Fixed(im.Data(data, path), Text(UPDATE_VER, size=96, align=(0.5, 0.8), color="#000000", outlines=[( 1, "#ffffff", 0, 0 )]), fit_first=True)

    config.after_load_callbacks.append(version_patch)

define update_message_list = [
        "Spinning up disks",
        "Lubricating Hermione",
        "Filling up Tonks' glass",
        "Rendering Cho's marvellous abs",
        "Teaching Astoria some manners",
        "Gazing into the crystal ball",
        "Waxing Cho's broom",
        "Sanitizing Dumbledore's desk",
        "Confiscating Hermione's panties",
        "Adjusting the dress code",
        "Deleting Hermiobrine",
        "Initializing Snape walk physics",
        "Loading Genie's name mispronunciation engine",
        "Generating {s}dad{/s} bad jokes",
        "Perverting common nouns",
        "Inserting obscure pop culture references",
        "Loading wardrobe feature fondling",
        "Corrupting Teachers",
        "Ignoring plot holes",
        "Inflating Susan's tits",
        "Hiding Room of Requirement",
        "Predicting images",
        "Initializing sex-drive",
        "Loading loading screen",
        "Bribing ministry of magic employees",
        "Maximizing student gullibility levels",
        "Tuning out Luna's rambles",
        "Filling cupboard with trash",
        "Shredding rule violation reports",
        "Adding tissue box of holding to desk",
        "Ignoring established lore",
        "Neglecting minor characters",
        "Hiding the marauders map",
        "Injecting British slang",
        "Stiffening nipples",
        "Nickering at knickers",
        "Greasing Snape's hair",
        "Increasing Genie's imagination levels",
        "Adding illusion of choice dialogue options",
        "Redirecting blood flow",
        "Slutifying Slytherins",
        "Dampening Genie's powers",
        "Sleeving wizard cards",
        "Breaking old save files",
        "Loading pointless bird petting mechanics",
        "Applying desk chair cushioning charm",
        "Calculating semen trajectory",
        "Opening spank-bank account at Gringotts",
        "Scratching Genie's leg",
        "Polishing Genie's wand",
        "Defiling Cho's panties",
        "Eliminating common sense",
        "Applying lube",
        "Restocking chocolate frog supply",
        "Charming students",
        "Breaking the fourth wall",
        "Shortening skirts",
        "Undressing house-elves",
        "Lewdifying spells",
        "Inserting sexual innuendoes",
        "Searching for the g-spot",
        "Adjusting refractory period levels",
        "Indexing breast sizes",
        "Prolonging the inevitable heat death of the universe",
        "Redefining the big bang",
        "Insert disc 2",
        ]

# Do not add parenthesis to the updater screen, otherwise it will break screen parameter interpolation.
screen updater:

    tag menu

    default msg = renpy.random.choice(update_message_list)
    default logo = version_logo()

    use game_menu(_("Updater"), scroll="viewport"):

        style_prefix "updater"

        vbox:
            spacing gui.pref_spacing
            xfill True

            button:
                xalign 0.5
                action OpenURL("https://www.silverstudiogames.org/")
                add logo xysize(570, 324)

            if u.state == u.ERROR:
                text _("An error has occured:")
            elif u.state == u.CHECKING:
                text _("Fetching for updates.")
            elif u.state == u.UPDATE_NOT_AVAILABLE:
                text _("This program is up to date.")
            elif u.state == u.UPDATE_AVAILABLE:
                text _("[u.version] is available. Do you want to install it?")
                hbox:
                    xalign 0.5

                    textbutton "Changelog" action OpenURL("https://www.silverstudiogames.org/p/changelog.html")
                    textbutton "Patreon" action OpenURL("https://patreon.com/silverstudiogames")
                    textbutton "Discord" action OpenURL("https://discord.gg/UbQeTCJ5RW")
            elif u.state == u.PREPARING:
                text _("Preparing to download the updates.")
            elif u.state == u.DOWNLOADING:
                text _("Downloading the updates.")
            elif u.state == u.UNPACKING:
                text _("Unpacking the updates.")
            elif u.state == u.FINISHING:
                text _("Finishing up.")
            elif u.state == u.DONE:
                text _("The updates have been installed. The program will restart.")
            elif u.state == u.DONE_NO_RESTART:
                text _("The updates have been installed.")
            elif u.state == u.CANCELLED:
                text _("The updates were cancelled.")

            if u.message is not None:
                text "[u.message!q]"

            if u.progress is not None:
                fixed:
                    bar value (u.progress or 0.0) range 1.0 style "updater_bar"
                    text "[msg]" color "#fff" size 10 yoffset 5

            hbox:
                xalign 0.5

                if u.can_proceed:
                    textbutton _("Proceed") action u.proceed keysym "K_RETURN"

                if u.can_cancel:
                    textbutton _("Cancel") action u.cancel keysym "K_ESCAPE"

    timer 2.0 action SetScreenVariable("msg", renpy.random.choice(update_message_list)) repeat True

style updater_text:
    xalign 0.5

style updater_button_text is gui_button_text
style updater_label is gui_label:
    xsize 209
    right_padding 17

style updater_label_text is gui_label_text:
    xalign 1.0
    text_align 1.0
    outlines [(2, "#000", 0, 0)]

style updater_bar is empty:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", Borders(8, 8, 8, 8), tile=False)
    right_bar Frame("gui/bar/right.png", Borders(8, 8, 8, 8), tile=False)

style update_available_button:
    xalign 0.5

style update_available_button_text:
    color "#F9A001"
    hover_color "#fff"
    xalign 0.5

label before_main_menu():
    python:
        if settings.get("updates") and not prerelease:
            CheckUpdates(onetime=True, autostart=False)()

    if mods_incompatible:
        $ mods = "\n".join(mods_incompatible)

        call modal_popup("Attention!", "The listed mods are incompatible and have been deactivated:\n" + mods, "interface/warning.webp")

    return
