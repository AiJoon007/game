rpy python 3

init python in cli:
    import os
    import collections
    import itertools
    from renpy.translation import quote_unicode
    from renpy.parser import elide_filename

    tl_file_cache = {}

    def open_tl_file(fn, mode):

        if fn in tl_file_cache:
            f = tl_file_cache[fn]

            if f.mode == mode:
                return f

            # elif not f.closed:
            #     # PY 2 only
            #     f.close()

        if not os.path.exists(fn):
            dn = os.path.dirname(fn)

            try:
                os.makedirs(dn)
            except Exception:
                pass

            f = open(fn, mode, encoding="utf-8")
            f.write(u"\ufeff")

        else:
            f = open(fn, mode, encoding="utf-8")

        tl_file_cache[fn] = f

        return f

    def scan_strings(strings, min_priority=0, max_priority=299, common_only=False):

        strings.sort(key=lambda s : s.sort_key)

        rv = [  ]
        seen = set()

        for s in strings:

            if s.priority < min_priority:
                continue

            if s.priority > max_priority:
                continue

            if common_only and not s.common:
                continue

            if s.text in seen:
                continue

            seen.add(s.text)
            rv.append(s)

        return rv

    def write_strings(language, strings):

        stl = renpy.game.script.translator.strings[language]
        stringfiles = collections.defaultdict(list)
        seen = set()

        nstrings = len(strings)-1

        for i, s in enumerate(strings):
            n = round(float(i)/(nstrings)*100)
            print("\rGenerating strings for {} ... Total progress:{} % ... Stage 2/2".format(language, n), end="")

            tlfn = renpy.translation.generation.translation_filename(s)

            if tlfn is None:
                continue

            if s.text in seen:
                continue

            seen.add(s.text)

            if language == "None" and tlfn == "common.rpy":
                tlfn = "common.rpym"

            stringfiles[tlfn].append(s)

        for tlfn, sl in list(stringfiles.items()):
            tlfn = os.path.join(renpy.config.gamedir, renpy.config.tl_directory, language, tlfn)

            f = open_tl_file(tlfn, mode="w")
            f.write(u"translate {} strings:\n".format(language))
            f.write(u"\n")

            for s in sl:
                original = s.text
                translation = stl.translate(s.text) # Keeps translated strings

                f.write(u"    # {}:{}\n".format(elide_filename(s.filename), s.line))
                f.write(u"    old \"{}\"\n".format(quote_unicode(original)))
                f.write(u"    new \"{}\"\n".format(quote_unicode(translation)))
                f.write(u"\n")

    def retranslate():
        translator = renpy.game.script.translator
        generation = renpy.translation.generation
        scanstrings = renpy.translation.scanstrings

        parser = renpy.arguments.ArgumentParser()
        parser.add_argument("--rebuild", action="store_true", help="Rebuilds the translation pointers and adds missing entries.")
        parser.add_argument("--empty", action="store_true", help="When combined with rebuild parameter, it will insert an empty string into added entires. Does nothing on its own.")
        parser.add_argument("--clean", action="store_true", help="Removes translation files that are no longer present within the game files.")
        parser.add_argument("--dry", action="store_true", help="Simulates the removal of translation files that are no longer present within the game files.")
        parser.add_argument("--include-mods", action="store_true", help="Include mod files when generating translations.")
        args = parser.parse_args()

        scripts = generation.translate_list_files()

        if not args.include_mods:
            mods_dir = os.path.join(renpy.config.gamedir, "mods")
            scripts = [f for f in scripts if not f.startswith(mods_dir)]

        strings = []
        nscripts = len(scripts)-1

        for i, filepath in enumerate(scripts):
            n = round(float(i)/(nscripts)*100)

            for language in translator.languages:

                print("\rGenerating dialogues for {} ... Total progress:{} % ... Stage 1/2".format(language, n), end="")

                for _, trans in translator.file_translates[filepath]:

                    trans_new = translator.language_translates.get((trans.identifier, language))
                    filter = generation.null_filter

                    if trans_new is None:
                        if not args.rebuild:
                            continue

                        trans_new = trans

                        if args.empty:
                            filter = generation.empty_filter

                    if hasattr(trans, "alternate") and (trans.alternate, language) in translator.language_translates:
                        continue

                    fp = os.path.relpath(filepath, renpy.config.gamedir)
                    fp = os.path.join(renpy.config.gamedir, renpy.config.tl_directory, language, fp)

                    f = open_tl_file(fp, mode="w")

                    f.write(u"# {}:{}\n".format(trans.filename, trans.linenumber))
                    f.write(u"translate {} {}:\n".format(language, trans.identifier.replace(".", "_")))
                    f.write(u"\n")

                    for n in trans.block:
                        f.write(u"    # " + n.get_code() + "\n")

                    for n in trans_new.block:
                        f.write(u"    " + n.get_code(filter) + "\n")

                    f.write(u"\n")

            strings.extend(scanstrings.scan_strings(filepath))

        strings = scan_strings(strings)

        for language in translator.languages:

            write_strings(language, strings)

            if args.clean:
                translations = [f for f in renpy.list_files() if f.startswith(renpy.config.tl_directory) and f.endswith((".rpy", ".rpym"))]

                for filepath in translations:
                    fn = os.path.basename(filepath)
                    fp = os.path.relpath(filepath, os.path.join(renpy.config.tl_directory, language))
                    fp = os.path.join(renpy.config.gamedir, fp)

                    if fp not in scripts:
                        if fn == "common.rpy":
                            continue

                        if fp in tl_file_cache:
                            f = tl_file_cache.pop(tl_file_cache)
                            f.close()

                        if args.dry:
                            print("Removal required: {}".format(filepath))
                        else:
                            os.unlink(filepath)
                            os.unlink(filepath + "c")

        for f in list(tl_file_cache.values()):
            f.close()

        tl_file_cache.clear()

        return False

    renpy.arguments.register_command("retranslate", retranslate)
