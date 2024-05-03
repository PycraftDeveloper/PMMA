import importlib
import math

from pmma.src.registry import Registry
from pmma.src.constants import Constants

class Draw(Registry, Constants):
    def __init__(self):
        if Registry.display_mode == Constants.PYGAME:
            self.drawing_extension = importlib.import_module("pygame.gfxdraw")

    def line(self, color, start, end, width):
        if Registry.display_mode == Constants.PYGAME:
            if Registry.anti_aliasing:
                Registry.graphics_backend.draw.aaline(self.surface, color, start, end, width)
            else:
                Registry.graphics_backend.draw.line(self.surface, color, start, end, width)
        else:
            raise NotImplementedError

    def lines(self, color, points, width=1, closed=False):
        if Registry.display_mode == Constants.PYGAME:
            if len(points) < 2:
                return
            if Registry.anti_aliasing:
                Registry.graphics_backend.draw.aalines(self.surface, color, closed, points, width)
            else:
                Registry.graphics_backend.draw.lines(self.surface, color, closed, points, width)
        else:
            raise NotImplementedError

    def rotated_rect(self, color, center_of_rect, width, height, rotation_angle=0): # https://stackoverflow.com/a/73855696
        """Draw a rectangle, centered at x, y.
        All credit to Tim Swast for this `function that helped make this possible!

        Arguments:
        x (int/float):
            The x coordinate of the center of the shape.
        y (int/float):
            The y coordinate of the center of the shape.
        width (int/float):
            The width of the rectangle.
        height (int/float):
            The height of the rectangle.
        color (str):
            Name of the fill color, in HTML format.
        """
        x, y = center_of_rect
        points = []

        # The distance from the center of the rectangle to
        # one of the corners is the same for each corner.
        radius = math.sqrt((height / 2)**2 + (width / 2)**2)

        # Get the angle to one of the corners with respect
        # to the x-axis.
        angle = math.atan2(height / 2, width / 2)

        # Transform that angle to reach each corner of the rectangle.
        angles = [angle, -angle + math.pi, angle + math.pi, -angle]

        # Convert rotation from degrees to radians.
        rot_radians = (math.pi / 180) * rotation_angle

        # Calculate the coordinates of each point.
        for angle in angles:
            y_offset = -1 * radius * math.sin(angle + rot_radians)
            x_offset = radius * math.cos(angle + rot_radians)
            points.append((x + x_offset, y + y_offset))

        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.draw.polygon(self.surface, color, points)
        else:
            raise NotImplementedError

    def rect(self, color, rect, width, border_radius=-1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1):
        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.draw.rect(self.surface, color, rect, width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius)
        else:
            raise NotImplementedError

    def circle(self, color, center, radius, width=0):
        if abs(radius) < 1:
            return
        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.draw.circle(self.surface, color, center, abs(radius), width)
        else:
            raise NotImplementedError

    def arc(self, color, rect, start_angle, stop_angle, width=1):
        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.draw.arc(self.surface, color, rect, start_angle, stop_angle, width)
        else:
            raise NotImplementedError

    def polygon(self, color, points, width=0):
        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.draw.polygon(self.surface, color, points, width)
        else:
            raise NotImplementedError

    def ellipse(self, color, rect, width=0):
        if Registry.display_mode == Constants.PYGAME:
            Registry.graphics_backend.draw.ellipse(self.surface, color, rect, width)
        else:
            raise NotImplementedError

    def pixel(self, color, point):
        if Registry.display_mode == Constants.PYGAME:
            try:
                self.drawing_extension.pixel(self.surface, color, point)
            except:
                temp_rect = Registry.graphics_backend.rect.Rect(*point, 1, 1)
                Registry.graphics_backend.draw.rect(self.surface, color, temp_rect, 1)
        else:
            raise NotImplementedError

    def curved_lines(self, color, points, steps=2):
        if Registry.display_mode == Constants.PYGAME:
            if len(points) > 2:
                try:
                    self.drawing_extension.bezier(self.surface, points, steps, color)
                    return True
                except:
                    pass
            self.lines(color, points, width=1, closed=False)
            return False
        else:
            raise NotImplementedError