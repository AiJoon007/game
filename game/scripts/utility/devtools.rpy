init -999 python early:
    if renpy.version_tuple < (7,5,3,22090809):
        raise RuntimeWarning("Your Ren'Py launcher is outdated, the current minimal requirement is 7.5.3.22090809+\nPlease perform an update and try launching the game again.")

    from renpy.uguu import glGetString, GL_VENDOR, GL_RENDERER, GL_VERSION

    def get_gpu_info():
        try:
            info = "\n".join([glGetString(GL_VENDOR).decode(), glGetString(GL_RENDERER).decode(), glGetString(GL_VERSION).decode()])
        except:
            info = "ERR: Unknown or incompatible driver."
        return info

    def get_renderer():
        return "DirectX" if preferences.renderer == "angle2" else "OpenGL"

    class stdcol:
       PURPLE = '\033[1;35;48m'
       CYAN = '\033[1;36;48m'
       BOLD = '\033[1;37;48m'
       BLUE = '\033[1;34;48m'
       GREEN = '\033[1;32;48m'
       YELLOW = '\033[1;33;48m'
       RED = '\033[1;31;48m'
       BLACK = '\033[1;30;48m'
       UNDERLINE = '\033[4;37;48m'
       END = '\033[1;37;0m'

    if config.developer:
        # Debug

        def detect_orphaned_rpyc_files():
            excluded = ["tl/"]

            files = renpy.list_files(common=True)
            compiled = [x for x in files if x.endswith(".rpyc") if not any(x.startswith(i) for i in excluded)]
            scripts = [x for x in files if x.endswith(".rpy")]
            orphaned = []

            for i in compiled:
                if not i[:-1] in scripts:
                    orphaned.append(i)

            if orphaned:
                raise Exception("Orphaned compiled scripts detected, please delete them before continuing:\n{}".format(orphaned))

        detect_orphaned_rpyc_files()


    # class InstanceDebugger(object):

    #     def __init__(self, obj):
    #         object.__setattr__(self, 'instance', obj)

    #     def __get__(self, obj, type=None):
    #         return functools.partial(self, obj)

    #     def __call__(self, *args, **kwargs):
    #         return self.instance(*args,**kwargs)

    #     def __getattr__(self, attr):
    #         attr = getattr(self.instance, attr)

    #         return self.__class__(attr) if hasattr(attr, '__dict__') else attr

    #     def __setattr__(self, attr, value):
    #         instance = self.instance

    #         if getattr(instance, attr, None) != value:
    #             print(f"'{self.instance.id}' setting attribute '{attr}' to '{value}' ...")

    #         instance.attr = value

init python:
    config.missing_image_callback = missing_image_func

    if config.developer:
        renpy.arguments.register_command("whitespace", save_whitespace)
    else:
        config.missing_label_callback = missing_label_func
        config.return_not_found_label = "missing_return"

init -2 python:

    def missing_image_func(path):
        global systemerror
        systemerror = ["Missing image", path]
        file, ext = os.path.splitext(path)

        if renpy.loadable(file + ".png"):
            return Image(file + ".png")

        if config.developer:
            raise IOError("Missing image: {}".format(path))
        return Image("images/blank.webp")

    def missing_label_func(name):
        global systemerror
        systemerror = ["Missing label", name]
        return "missing_label"

    def TBA_message(msg="Currently unavailable, check in later versions of the game."):
        renpy.say(nar, msg)

    def save_whitespace(refresh=False):
        """
        Generates a whitespace information file.
        """
        global whitespace_dict

        ap = renpy.arguments.ArgumentParser("Generates a whitespace information file.", require_command=False)
        ap.add_argument("--refresh", action="store_true", help="Recalculate for all images.")
        args = ap.parse_args()
        if args.refresh or refresh:
            whitespace_dict = {}

        path = os.path.normpath(config.gamedir)
        images = []
        for root, dirs, files in os.walk(path):
            for file in fnmatch.filter(files, "*.webp"):
                img = os.path.join(root, file).replace("\\", "/").split("/game/")[1]
                images.append(img)

        c = len(images)
        for i, img in enumerate(images):
            # stdout causes issues on Windows

            # sys.stdout.write("\rCalculating whitespace... {:3.0f}%".format(i / float(c - 1) * 100.0))
            # sys.stdout.flush()
            crop_whitespace(img)

        file = os.path.normpath(config.gamedir + "/images.whitespace")
        with open(file, "w") as f:
            for img, box in sorted(whitespace_dict.items()):
                f.write("{}:{},{},{},{}\n".format(img, *box))

        print("\rCalculating whitespace... Done!")
        return False

label missing_label():
    $ renpy.choice_for_skipping()
    $ err_msg1 = systemerror[0]
    $ err_msg2 = systemerror[1]
    "{color=#7a0000}System{/color}" "Uh-oh. Looks like you've encountered a bug. Don't worry, we will try to return you back to the office after displaying the error message, your save file won't be affected."
    "{color=#7a0000}System{/color}" "{color=#7a0000}Error:{/color} [err_msg1] '{color=#7a0000}[err_msg2]{/color}'\n\n\n{size=-4}You can report this bug on our {a=https://discord.gg/7PD57yt}discord{/a}.{/size}"
    $ states.last_girl = None
    $ states.active_girl = None
    $ systemerror = [None, None]
    jump main_room

label missing_return():
    $ renpy.choice_for_skipping()
    "{color=#7a0000}System{/color}" "Uh-oh. Looks like you've encountered a bug. Don't worry, we will try to return you back to the office after displaying the error message, your save file won't be affected."
    "{color=#7a0000}System{/color}" "{color=#7a0000}Error:{/color} Point of no return.\n\n\n{size=-4}You can report this bug on our {a=https://discord.gg/7PD57yt}discord{/a}.{/size}"
    $ states.last_girl = None
    $ states.active_girl = None
    jump main_room

screen placeholder():
    tag cg
    zorder 16 # above dolls

    add Placeholder("bg")
    add Placeholder("girl")


init 999 python hide:
    def set_screen_layer(layer, *screens):
        for scr_name in screens:
            for _, scr in renpy.display.screen.get_all_screen_variants(scr_name):
                scr.layer = layer

    set_screen_layer("interface", "_performance", "_image_load_log")
