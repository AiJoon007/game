# init python:
#     # TODO: Optimize the render functions, they seem to be too resource heavy.

#     class class_draw_sign(renpy.Displayable):
#         def __init__(self, width, height, shape):
#             super(class_draw_sign, self).__init__(self)
            
#             self.width = width
#             self.height = height

#             self.shape = shape

#         def render(self, width, height, st, at):
#             render = renpy.Render(self.width, self.height)
            
#             for i in self.shape:
#                 render.canvas().circle((0, 0, 0), i, 10, 0)
#             return render

#     class class_draw_shape(renpy.Displayable):
#         def __init__(self, color, width, height, mode):
#             super(class_draw_shape, self).__init__(self)

#             self.color = color
#             self.mode = mode
            
#             self.width = width
#             self.height = height

#             self.shape = []

#             self.drawing = False
#             self.active = True
#             self.cached = False

#         def render(self, width, height, st, at):
#             render = renpy.Render(self.width, self.height)

#             if self.mode == 0:
#                 for i in self.shape:
#                     render.canvas().circle(self.color, i, 5, 0)
#             elif self.mode == 1:
#                 if self.shape:
#                     render.canvas().lines(self.color, False, self.shape, 10)
#             return render
                    
#         def event(self, ev, x, y, st):
#             if self.active:
#                 if renpy.map_event(ev, 'mousedown_1'):
#                     self.drawing = True
#                 elif renpy.map_event(ev, 'mouseup_1'):
#                     self.drawing = False
#                     self.cached = False

#                 if self.drawing:
#                     if ev.type == pygame.MOUSEMOTION:
#                         self.shape.append((x, y))
#                         if self.mode == 1:
#                             renpy.redraw(self, 0)
                                
#             else:
#                 if not self.cached:
#                     self.cached = True
#                     renpy.redraw(self, 0)
            

#     class class_draw_canvas(renpy.Displayable):
#         _precision = 10
#         interactive = True
#         mode = 1 # 0 Precise, 1 fast
        
#         color = (211, 211, 211) # Green
        
#         def __init__(self, width, height, sign):
#             super(class_draw_canvas, self).__init__(self)

#             self.width = width
#             self.height = height
#             self.sign = class_draw_sign(self.width, self.height, sign)
            
#             self.children = []
#             self.current_child = None
            
#             self.score = 0
            
#             self.set_boundries()

#         def render(self, width, height, st, at):
#             render = renpy.Render(self.width, self.height)
#             render.place(self.sign, 0, 0)
#             for child in self.children:
#                 render.place(child, 0, 0)
#             return render

#         def event(self, ev, x, y, st):
#             if self.width > x > 0 and self.height > y > 0:
#                 if self.interactive:
#                     if renpy.map_event(ev, 'mousedown_1'):
#                         #self.clear()
#                         new_child = class_draw_shape(self.color, self.width, self.height, self.mode)
#                         self.children.append(new_child)
#                         self.current_child = new_child
#                         renpy.redraw(self, 0)

#                     if renpy.map_event(ev, 'mouseup_1'):
#                         self.current_child.cached = False
#                         self.current_child.active = False
#                         self.check_shape()

#                     for child in self.children:
#                         child.event(ev, x, y, st)

#         def clear(self):
#             for i in self.children:
#                 del i
#             self.children = []
#             self.score = 0
#             renpy.redraw(self, 0)

#         def visit(self):
#             return self.children
            
#         def check_shape(self):
#             global _sign_value, _sign_max
#             max_score = len(self.sign.shape)
#             score = 0
#             temp = []

#             if self.current_child.shape != []:
#                 for t in self.sign.shape:
#                     if t in temp:
#                         continue
#                     for i in self.current_child.shape:
#                         if t[0]-self.precision <= i[0] <= t[0]+self.precision and t[1]-self.precision <= i[1] <= t[1]+self.precision:
#                             temp.append(t)
#                             score += 1
#                             break
                            
#             for i in self.current_child.shape:
#                 if not self.boundries[0] <= i[0] <= self.boundries[2] or not self.boundries[1] <= i[1] <= self.boundries[3]:
#                     score -= 1
                            
#             if len(temp) < max_score:
#                 score -= max_score-len(temp)
                
#             print "scored %s out of %s" % (score, max_score)
#             print "boundries = %s" % self.boundries
#             if score > 0:
#                 self.score = round(100 * float(score)/float(max_score), 2)
#             else:
#                 self.score = 0.0
#             _sign_value = 0.0
#             _sign_max = self.score

#             renpy.end_interaction(("result", self.score))
#             return
            
#         def set_boundries(self):
#             self.boundries = [1000, 1000, -1000, -1000]
            
#             for i in self.sign.shape:
#                 self.boundries[0] = min(self.boundries[0], i[0])
#                 self.boundries[1] = min(self.boundries[1], i[1])
#                 self.boundries[2] = max(self.boundries[2], i[0])
#                 self.boundries[3] = max(self.boundries[3], i[1])
#             self.boundries[0], self.boundries[1], self.boundries[2], self.boundries[3] = self.boundries[0]-self.precision, self.boundries[1]-self.precision, self.boundries[2]+self.precision, self.boundries[3]+self.precision
#             return
            
#         @property
#         def precision(self):
#             return self._precision
            
#         @precision.setter
#         def precision(self, value):
#             self._precision = value
#             self.set_boundries()
            
#         def force_redraw(self):
#             renpy.redraw(self, 0)
#             return
#
