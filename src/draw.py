import importlib
import math

from pmma.src.registry import Registry
from pmma.src.constants import Constants

Constants.TAU = math.pi * 2

class Draw:
    def __init__(self, canvas=None):
        if Registry.display_mode == Constants.PYGAME:
            self.drawing_extension = importlib.import_module("pygame.gfxdraw")

        self.canvas = canvas

    def line(self, color, start, end, width, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if Registry.anti_aliasing:
                return Registry.graphics_backend.draw.aaline(canvas.surface, color, start, end, width)
            else:
                return Registry.graphics_backend.draw.line(canvas.surface, color, start, end, width)
        else:
            raise NotImplementedError

    def lines(self, color, points, width=1, closed=False, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if len(points) < 2:
                return
            if Registry.anti_aliasing:
                return Registry.graphics_backend.draw.aalines(canvas.surface, color, closed, points, width)
            else:
                return Registry.graphics_backend.draw.lines(canvas.surface, color, closed, points, width)
        else:
            raise NotImplementedError

    def advanced_polygon(self, color, centre, radius, number_of_sides, rotation_angle=0, width=0, cache=None, wire_frame=False, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                return Registry.graphics_backend.draw.polygon(canvas.surface, color, points, width=width), cache
            else:
                return None, cache

        if wire_frame:
            for i in range(0, number_of_sides):
                if Registry.display_mode == Constants.PYGAME:
                    Registry.graphics_backend.draw.line(
                        canvas.surface,
                        color,
                        centre, (
                            math.cos(i / number_of_sides * Constants.TAU) * radius + centre[0],
                            math.sin(i / number_of_sides * Constants.TAU) * radius + centre[1]))

        points = [
            (math.cos(i / number_of_sides * Constants.TAU + rotation_angle) * radius + centre[0],
                math.sin(i / number_of_sides * Constants.TAU + rotation_angle) * radius + centre[1]) for i in range(0, number_of_sides)]

        if wire_frame:
            width = 1

        if Registry.display_mode == Constants.PYGAME:
            return Registry.graphics_backend.draw.polygon(canvas.surface, color, points, width=width), points
        else:
            return None, cache

    def rotated_rect(self, color, center_of_rect, radius, height, rotation_angle=0, cache=None, width=0, canvas=None): # https://stackoverflow.com/a/73855696
        """Draw a rectangle, centered at x, y.
        All credit to Tim Swast for this function!

        Arguments:
        x (int/float):
            The x coordinate of the center of the shape.
        y (int/float):
            The y coordinate of the center of the shape.
        radius (int/float):
            The radius of the rectangle.
        height (int/float):
            The height of the rectangle.
        color (str):
            Name of the fill color, in HTML format.
        """
        if canvas is None:
            canvas = self.canvas
        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                return Registry.graphics_backend.draw.polygon(canvas.surface, color, points, width=width), cache
            else:
                return None, cache

        x, y = center_of_rect
        points = []

        # The distance from the center of the rectangle to
        # one of the corners is the same for each corner.
        radius = math.sqrt((height / 2)**2 + (radius / 2)**2)

        # Get the angle to one of the corners with respect
        # to the x-axis.
        angle = math.atan2(height / 2, radius / 2)

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
            return Registry.graphics_backend.draw.polygon(canvas.surface, color, points, width=width)
        else:
            raise NotImplementedError

    def rect(self, color, rect, width, border_radius=-1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            return Registry.graphics_backend.draw.rect(canvas.surface, color, rect, width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius)
        else:
            raise NotImplementedError

    def circle(self, color, center, radius, width=0, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if abs(radius) < 1:
            return
        if Registry.display_mode == Constants.PYGAME:
            return Registry.graphics_backend.draw.circle(canvas.surface, color, center, abs(radius), width)
        else:
            raise NotImplementedError

    def arc(self, color, rect, start_angle, stop_angle, width=1, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            return Registry.graphics_backend.draw.arc(canvas.surface, color, rect, start_angle, stop_angle, width)
        else:
            raise NotImplementedError

    def polygon(self, color, points, width=0, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            return Registry.graphics_backend.draw.polygon(canvas.surface, color, points, width)
        else:
            raise NotImplementedError

    def ellipse(self, color, rect, width=0, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            return Registry.graphics_backend.draw.ellipse(canvas.surface, color, rect, width)
        else:
            raise NotImplementedError

    def pixel(self, color, point, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            try:
                return self.drawing_extension.pixel(canvas.surface, color, point), True
            except:
                temp_rect = Registry.graphics_backend.rect.Rect(*point, 1, 1)
                return Registry.graphics_backend.draw.rect(canvas.surface, color, temp_rect, 1), False
        else:
            raise NotImplementedError

    def curved_lines(self, color, points, steps=2, canvas=None):
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if len(points) > 2:
                try:
                    return self.drawing_extension.bezier(canvas.surface, points, steps, color), True
                except:
                    pass
            return self.lines(canvas, color, points, width=1, closed=False), False
        else:
            raise NotImplementedError