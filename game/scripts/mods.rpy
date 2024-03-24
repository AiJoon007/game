init -999:
    python:
        import json
        import os

        if not getattr(persistent, "mods_enabled"):
            persistent.mods_enabled = _set()

        mods_list = _dict()
        mods_incompatible = _set()
        mods_compatible = 1.45 # Hardcoded due to initalization offset

        def mods_import():
            global mods_list

            all_files = renpy.list_files()
            mods = [x for x in all_files if x.endswith(".json")]

            for i, manifest in enumerate(mods):
                path = os.path.split(manifest)[0]
                files = [x for x in all_files if path in x]
                scripts = [x for x in files if x.endswith(".rpym")]
                logo = "{}/logo.webp".format(path)

                if not renpy.loadable(logo):
                    logo = "#000"

                # Read manifest
                with renpy.open_file(manifest) as f:
                    data = json.load(f)

                modname = data.get("Name", None)

                if not modname:
                    continue

                mods_list[modname] = data
                mods_list[modname]["Files"] = files
                mods_list[modname]["Scripts"] = scripts
                mods_list[modname]["Path"] = path
                mods_list[modname]["LoadOrder"] = i # TODO: Make load order customisable
                mods_list[modname]["Logo"] = logo

            for mod in list(persistent.mods_enabled):
                if not mods_list.get(mod, None):
                    persistent.mods_enabled.remove(mod)
            return

        def mods_init():
            global mods_incompatible
            for i in persistent.mods_enabled.copy():
                control, major, *minor = mods_list[i]["GameVer"].split(" ")[0].split(".")
                ver = float("{}.{}{}".format(control, major, "".join(minor)))

                if ver < mods_compatible:
                    persistent.mods_enabled.remove(i)
                    mods_incompatible.add(i)
                    continue

                for j in mods_list[i]["Scripts"]:
                    name = os.path.splitext(j)[0]

                    try:
                        renpy.include_module(name)
                    except Exception as e:
                        if config.developer:
                            renpy.error(e)
                        persistent.mods_enabled.remove(i)
                        mods_incompatible.add(i)


        mods_import()
        mods_init()

init python:
    @renpy.pure
    class ToggleMod(Action, NoRollback):
        def __init__(self, name):
            self.name = name

        def __call__(self):
            if not main_menu:
                renpy.notify("Mods can be enabled or disabled from within the main menu only.")
                return

            mods = persistent.mods_enabled
            name = self.name

            if name in mods:
                renpy.notify("Mod disabled. Remember to restart the game for the changes to take effect.")
                mods.remove(name)
            else:
                renpy.notify("Mod Enabled. Remember to restart the game for the changes to take effect.")
                mods.add(name)

            renpy.restart_interaction()

    class AskPermission(Action, NoRollback):
        def __init__(self, name):
            self.name = name

        def __call__(self):
            if not renpy.android:
                return True

            return (renpy.check_permission(self.name) or renpy.request_permission(self.name))
