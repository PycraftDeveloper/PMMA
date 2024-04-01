import importlib

from pmma.src.registry import Registry
from pmma.src.constants import Constants

class Draw(Registry, Constants):
    def __init__(self, canvas):
        self.canvas = canvas
        if Registry.display_mode == Constants.PYGAME:
            self.drawing_extension = importlib.import_module("pygame.gfxdraw")

    def line(self, color, start, end, width):
        if Registry.anti_aliasing:
            Registry.graphics_backend.draw.aaline(self.canvas.surface, color, start, end, width)
        else:
            Registry.graphics_backend.draw.line(self.canvas.surface, color, start, end, width)

    def lines(self, color, points, width=1, closed=False):
        if len(points) < 2:
            return
        if Registry.anti_aliasing:
            Registry.graphics_backend.draw.aalines(self.canvas.surface, color, closed, points, width)
        else:
            Registry.graphics_backend.draw.lines(self.canvas.surface, color, closed, points, width)

    def rect(self, color, rect, width, border_radius=-1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1):
        Registry.graphics_backend.draw.rect(self.canvas.surface, color, rect, width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius)

    def circle(self, color, center, radius, width=0):
        if radius < 1:
            return
        Registry.graphics_backend.draw.circle(self.canvas.surface, color, center, radius, width)

    def arc(self, color, rect, start_angle, stop_angle, width=1):
        Registry.graphics_backend.draw.arc(self.canvas.surface, color, rect, start_angle, stop_angle, width)

    def polygon(self, color, points, width=0):
        Registry.graphics_backend.draw.polygon(self.canvas.surface, color, points, width)

    def ellipse(self, color, rect, width=0):
        Registry.graphics_backend.draw.ellipse(self.canvas.surface, color, rect, width)

    def pixel(self, color, point):
        try:
            self.drawing_extension.pixel(self.canvas.surface, color, point)
        except:
            temp_rect = Registry.graphics_backend.rect.Rect(*point, 1, 1)
            Registry.graphics_backend.draw.rect(self.canvas.surface, color, temp_rect, 1)

    def curved_lines(self, color, points, steps=2):
        if len(points) > 2:
            try:
                self.drawing_extension.bezier(self.canvas.surface, points, steps, color)
                return
            except:
                pass
        self.lines(color, points, width=1, closed=False)