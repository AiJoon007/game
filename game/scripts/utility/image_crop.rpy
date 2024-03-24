init python:
    whitespace_dict = {}
    with renpy.open_file("images.whitespace") as fp:
        line = fp.readline()
        while line:
            path, area = line.strip("\r\n").split(':')
            whitespace_dict[path] = list(map(int, area.split(',')))
            line = fp.readline()

    def crop_whitespace(path):
        # Return box from whitespace_dict, or calculate and store it

        def _find_file_surface(obj):
            if isinstance(obj, str):
                return obj, Image(obj).load()
            elif isinstance(obj, im.Image):
                return obj.filename, obj.load()
            elif isinstance(obj, Transform):
                return _find_file_surface(obj.child)

        if path in whitespace_dict:
            box = whitespace_dict[path]
        else:
            path, surf = _find_file_surface(path)
            size = surf.get_size()
            box = tuple(surf.get_bounding_rect())

            if "/clothes/" in path and size[0] != 1010:
                ratio = size[0] / 1010
                box = tuple(v/ratio for v in box)
            whitespace_dict[path] = tuple(map(int, box))
        return box

    def crop_image_zoom(path, xsize, ysize, grayscale=False):
        x, y, w, h = crop_whitespace(path)
        matrix = SaturationMatrix(0) if grayscale else None
        sprite = Image(path)

        return Transform(sprite, crop=(x, y, w, h), xsize=xsize, ysize=ysize, fit="contain", matrixcolor=matrix, subpixel=True)

    def get_zoom(image, size):
        if isinstance(image, str):
            image = Image(image)

        r = renpy.render(image, 800, 800, 0, 0)
        x, y = r.get_size()
        xsize, ysize = size

        return min(ysize / y, xsize / x)
