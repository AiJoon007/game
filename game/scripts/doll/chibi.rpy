init 5 python:
    class DollChibi(renpy.Displayable):

        def __init__(self, name, layer="screens", zorder=12, zoom=0.28, **properties):

            super().__init__(**properties)

            self.name = name
            self.tag = name + "_chibi"
            self.pose = None
            self.walk = "walk"
            self.idle = "stand"
            self.layer = layer
            self.zorder = zorder
            self.zoom = zoom
            self.pos = (0,0)
            self.xzoom = 1
            self.char = eval(name)
            self.poses = {}

            # Animation
            self.anim_frames = None
            self.anim_sprite = None
            self.anim_speed = 1.0
            self.anim_fps = 8.0
            self.anim_trans = None
            self.anim_interval = None
            self.anim_interval_total = None

            # ATL
            self.atl_time = 0
            self.atl_time_total = 0
            self.atl_partial = None
            self.atl_looping = False
            self.atl_pause = False
            self.atl_at_list = []

        def register(self, pose, frames, size):
            self.poses[pose] = (frames, size)

            if config.developer:
                print(f"Registered \"{pose}\" pose for {self.name}")

        @functools.cache
        def build_image(self, hash, pose):
            states = self.char.states
            items = [v[0] for v in states.values() if v[0] and v[2]]
            subpath = posixpath.join("chibi", pose)

            sprites = [(ltype, img, z) for i in items for ltype, img, z in i.build_image(i._hash, subpath, maxsize=None)]
            masks = [sprites.pop(sprites.index(i)) for i in sprites if i[0] == "mask"]

            sprites.sort(key=itemgetter(2))
            masks.sort(key=itemgetter(2))

            back_sprites = [x[1] for x in sprites if x[2] < 0]

            #Apply alpha mask
            for m in masks:
                _, mask, mask_zorder = m

                for i, s in enumerate(sprites):
                    _, sprite, sprite_zorder = s

                    if i < 1 or mask_zorder > sprite_zorder:
                        continue

                    masked = AlphaMask(Fixed(*(x[1] for x in sprites[:i]), fit_first=True), mask)
                    sprites = sprites[i:]
                    sprites.insert(0, (None, masked, mask_zorder))
                    break

            sprites = back_sprites + [x[1] for x in sprites]

            return Fixed(*sprites, fit_first=True)

        def build_animation(self):
            pose = self.pose
            frames = self.poses[pose][0]
            sprite = self.build_image(self.char._hash, pose)

            if frames > 1:
                interval = self.anim_speed / self.anim_fps
            else:
                interval = (365.25 * 86400.0) # About one year

            self.anim_frames = frames
            self.anim_interval = interval
            self.anim_interval_total = (frames * interval)
            self.anim_sprite = sprite

        def render(self, width, height, st, at):
            frame_width, frame_height = self.poses[self.pose][1]

            # Calculate the current frame based on the time
            trans = self.anim_trans
            interval = self.anim_interval
            time = (st % self.anim_interval_total)
            frame = int(time / interval)
            sprite = self.anim_sprite

            if trans and st >= interval:
                sprite = trans(old_widget=sprite, new_widget=sprite)

            cr = renpy.render(sprite, width, height, st, at)
            sheet_width, sheet_height = cr.get_size()

            # Calculate the position of the current frame within the sprite sheet
            sheet_cols = sheet_width // frame_width
            sheet_row = int(frame / sheet_cols)
            sheet_col = frame % sheet_cols
            frame_x = sheet_col * frame_width
            frame_y = sheet_row * frame_height

            rv = renpy.Render(frame_width, frame_height)
            rv.blit(cr.subsurface((frame_x, frame_y, frame_width, frame_height)), (0, 0))

            if not self.atl_looping and st > self.atl_time_total:
                renpy.timeout(0)
            elif not renpy.game.less_updates:
                renpy.redraw(self, interval - time)

            return rv

        def event(self, ev, x, y, st):
            # Determine pose change if show time exceeds animation time.
            # Looping animations ignore this check because they are rebuilt every loop.

            if renpy.in_rollback():
                # We don't want to use 'raise renpy.IgnoreEvent' because it blocks events in other displayables, including interfaces
                return

            elif renpy.is_skipping():
                self.stop()
                return

            elif ((not self.atl_looping and st > self.atl_time_total)
                or (ev.type == pygame.MOUSEBUTTONUP and ev.button == 1)
                or (ev.type == pygame.KEYDOWN and ev.key in [pygame.K_RETURN, pygame.K_SPACE, pygame.K_KP_ENTER, pygame.K_SELECT])):
                self.stop()

        # def per_interact(self):
        #     # Handle interrupt events
        #     if (renpy.is_skipping() or self.atl_pause) and not self.pose == self.idle:
        #         self.stop()

        def set_pose(self, pose):
            if self.pose == pose:
                return

            self.pose = pose
            self.update()

        def place(self, pos=None, speed=1.0, pause=False, at_list=[], pose=None, xzoom=None):
            self.set_pose(pose or self.idle)

            self.atl_time = 0
            self.atl_time_total = 0
            self.atl_partial = None
            self.atl_looping = False
            self.atl_pause = False
            self.atl_at_list = []

            frames = self.anim_frames
            if frames > 1:
                interval = (self.anim_speed / self.anim_fps) / speed
                interval_total = (frames * interval)

                self.anim_interval = interval
                self.anim_interval_total = interval_total

            xzoom = xzoom or (-1 if (pos > self.pos) else 1)

            self.pos = pos or self.pos
            self.xzoom = xzoom

            transform = Transform(pos=pos, zoom=self.zoom, xzoom=xzoom, anchor=(0.5, 1.0))

            self.show(transform, at_list, self.layer, self.zorder)

            if pause:
                renpy.pause(None)

            return

        def move(self, path, speed=1.0, pause=True, loop=False, warper="linear", at_list=[], pose=None, repeat=None, wrap=True, reverse=True):
            """Makes chibi move"""

            self.atl_looping = loop
            self.atl_pause = pause
            self.atl_at_list = at_list

            if isinstance(path, tuple):
                path = [path]

            # If 'A' position is not supplied for A -> B movement, use last known position instead.
            if len(path) < 2:
                path = [self.pos] + path
            # If reverse and loop/repeat is True, and pathing has more than two entries,
            # use complex looping by joining the reversed paths
            elif reverse and (loop or repeat):
                # Reverses the list, strips last entry from the reverse list, and finally joins them.
                path += path[1::-1]

            if repeat:
                path *= repeat

                if wrap:
                    # Wrap pathing back to starting position
                    path.append(path[0])

            self.set_pose(pose or self.walk)

            # Note: Warper names and their count can change over time,
            # so it's easier to just evaluate the input.
            # List of available warpers:
            # https://www.renpy.org/doc/html/atl.html?#warpers
            warper = eval(f"_warper.{warper}")

            distances = []
            times = []

            if loop:
                # Append first position as last to create a looped path.
                path.append(path[0])

            # Calculate distances and timings using euclidean distance algorithm.
            for xy1, xy2 in zip(path, path[1:]):
                x1, y1 = xy1
                x2, y2 = xy2

                distance = math.hypot(x2 - x1, y2 - y1)
                time = distance / (100.0 * speed)

                distances.append(distance)
                times.append(time)

            # Calculate total ATL time required to reach the destination
            total_time = sum(times)
            self.atl_time_total = total_time

            # Recalculate animation intervals when necessary, including speed factors.
            frames = self.anim_frames
            if frames > 1:
                interval = (self.anim_speed / self.anim_fps) / speed
                interval_total = (frames * interval)

                self.anim_interval = interval
                self.anim_interval_total = interval_total

            # renpy.partial allows us to pass arguments into a transform function.
            partial = renpy.partial(self.move_atl, path, times, loop, warper)
            self.atl_partial = partial

            transform = Transform(function=partial, anchor=(0.5, 1.0))

            self.show(transform, at_list, self.layer, self.zorder)

            if pause:
                if loop:
                    renpy.pause(None)
                else:
                    renpy.pause(total_time)

            return (distances, times)

        def stop(self):
            if not self.atl_partial:
                return

            # Freezes the animation
            path, _, _, _ = self.atl_partial.args
            pos = path[-1]
            xzoom = -1 if (path[-1] > path[-2]) else 1
            zpos = self.zorder + (1.0 / (pos[1] / config.screen_height))

            self.pos = pos
            self.xzoom = xzoom

            self.atl_time = 0
            self.atl_time_total = 0

            self.set_pose(self.idle)
            transform = Transform(pos=pos, zoom=self.zoom, xzoom=xzoom, anchor=(0.5, 1.0))
            self.show(transform, self.atl_at_list, self.layer, zpos)

        def move_atl(self, path, times, loop, warper, trans, st, at):
            """Animations are time based, so each segment will happen at a specific frame time."""
            if self.atl_time_total == 0:
                # Stops updating the animation
                return None

            if loop:
                timer = st % self.atl_time_total
            else:
                timer = st

                if timer > self.atl_time_total:
                    return None

            internal_time = 0
            current_segment = 0

            # TODO: This loop feels unnecessary, need to find a better way.
            for i, t in enumerate(times):
                if (internal_time + t) > timer:
                    current_segment = i
                    break

                internal_time += t

            segment_time = (timer - internal_time) / times[current_segment]
            next_segment = current_segment + 1

            # Adjust XY position
            trans.pos = renpy.atl.interpolate(warper(segment_time), path[current_segment], path[next_segment], renpy.atl.PROPERTIES["pos"])
            self.pos = trans.pos

            # Adjust X zoom based on target X position
            # 1 = Facing Right, -1 = Facing Left
            trans.xzoom = 1 if (path[current_segment][0] > path[next_segment][0]) else -1
            self.xzoom = trans.xzoom

            # Adjust zoom
            trans.zoom = self.zoom

            # Adjust Z position based on Y axis
            # TODO: Add room support with bottom, middle, and top vanishing points.
            # room_scale = 0.5
            # zpos1 = ((path[current_segment][1] / 600.0) * 1000.0) * room_scale
            # zpos2 = ((path[next_segment][1] / 600.0) * 1000.0) * room_scale
            # trans.zpos = renpy.atl.interpolate(warper(segment_time), zpos1, zpos2, renpy.atl.PROPERTIES["zpos"])
            # self.zpos = trans.zpos

            # TODO: Using zorders is suboptimal and expensive, using 3D staging would be preferable.
            zpos = self.zorder + (1.0 / (self.pos[1] / config.screen_height))
            renpy.change_zorder(self.layer, self.tag, zpos)
            return 0

        def show(self, transform, at_list, layer, zorder):
            # The safest way to restart the transform is to rebuild it.
            # Other methods proved to be too finicky...

            image = At(self, transform) # IMPORTANT: Enable perspective and gl_depth for 3D staging

            if not renpy.is_init_phase():
                renpy.show(name=self.tag, what=image, at_list=at_list, layer=layer, zorder=zorder)

        def hide(self):
            if not renpy.is_init_phase():
                renpy.hide(name=self.tag)

        def update(self):
            self.build_animation()
            renpy.redraw(self, 0)

        @property
        def image(self):
            return self

init offset = 5

default hooch_chibi = DollChibi(name="hooch", doll=hooch)
# default cho_chibi_new = DollChibi(name="cho", doll=cho)
# default tonks_chibi_new = DollChibi(name="tonks", doll=tonks)

# label chibitest:
#     chibi tonks register ("stand", 1, (600, 800))
#     chibi tonks register ("walk", 8, (600, 800))
#     "Rollback block"
#     $ renpy.block_rollback()

#     "repeat 3"
#     chibi tonks move (path=[(500, 421), (650, 521), (800, 421)], repeat=3)
#     "loop"
#     chibi tonks move (path=[(500, 421), (650, 521), (800, 421)], loop=True)
#     "doll synchronisation"
#     chibi tonks move (path=[(500, 421), (650, 521), (800, 421)], loop=True, pause=False)
#     ton @ hair default "Default" ("base", "base", "base", "mid")
#     ton @ hair angry "Angry" ("angry", "narrow", "angry", "mid")
#     ton @ hair scared "Scared" ("scream", "wide", "worried", "mid")
#     "End"
#     hide tonks_chibi
#     hide tonks_main

#     jump main_room_menu

# label chibitest2:
#     chibi tonks register ("stand", 1, (600, 800))
#     chibi tonks register ("walk", 8, (600, 800))
#     "Rollback block"
#     $ renpy.block_rollback()

#     "pos 1"
#     chibi tonks place (pos=(300,300))
#     "pos 2"
#     chibi tonks place (pos=(400,300))
#     "pos 3"
#     chibi tonks place (pos=(400,400))
#     "pos 4"
#     chibi tonks place (pos=(200,400))
#     "pos 5"
#     chibi tonks place (pos=(600,400))
#     "End"
#     hide tonks_chibi
#     hide tonks_main

#     jump main_room_menu
