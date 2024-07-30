import importlib
import math
import time

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class DrawIntermediary:
    number_of_draw_calls = 0
    total_time_spent_drawing = 0

class Line:
    def __init__(self, color=None, start=None, end=None, width=1, canvas=None):
        self.color = color
        self.start = start
        self.end = end
        self.width = width
        self.canvas = canvas

    def draw(self, color=None, start=None, end=None, width=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if start is None:
            start = self.start
        if end is None:
            end = self.end
        if width is None:
            width = self.width
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        if Registry.display_mode == Constants.PYGAME:
            if Registry.anti_aliasing:
                returnable = Registry.graphics_backend.draw.aaline(canvas.pygame_surface, color, start, end, width)
            else:
                returnable = Registry.graphics_backend.draw.line(canvas.pygame_surface, color, start, end, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Lines:
    def __init__(self, color=None, points=None, width=1, closed=False, canvas=None):
        self.color = color
        self.points = points
        self.width = width
        self.closed = closed
        self.canvas = canvas

    def draw(self, color=None, points=None, width=None, closed=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if points is None:
            points = self.points
        if width is None:
            width = self.width
        if closed is None:
            closed = self.closed
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        if Registry.display_mode == Constants.PYGAME:
            if len(points) < 2:
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
                return
            if Registry.anti_aliasing:
                returnable = Registry.graphics_backend.draw.aalines(canvas.pygame_surface, color, closed, points, width)
            else:
                returnable = Registry.graphics_backend.draw.lines(canvas.pygame_surface, color, closed, points, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class AdvancedPolygon:
    def __init__(self, color=None, centre=None, radius=None, number_of_sides=None, rotation_angle=0, width=0, cache=None, wire_frame=False, canvas=None):
        self.color = color
        self.centre = centre
        self.radius = radius
        self.number_of_sides = number_of_sides
        self.rotation_angle = rotation_angle
        self.width = width
        self.cache = cache
        self.wire_frame = wire_frame
        self.canvas = canvas

    def draw(self, color=None, centre=None, radius=None, number_of_sides=None, rotation_angle=None, width=None, cache=None, wire_frame=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if centre is None:
            centre = self.centre
        if radius is None:
            radius = self.radius
        if number_of_sides is None:
            number_of_sides = self.number_of_sides
        if rotation_angle is None:
            rotation_angle = self.rotation_angle
        if width is None:
            width = self.width
        if cache is None:
            cache = self.cache
        if wire_frame is None:
            wire_frame = self.wire_frame
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width=width), cache
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
                return returnable
            else:
                return None, cache
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start

        if wire_frame:
            for i in range(0, number_of_sides):
                if Registry.display_mode == Constants.PYGAME:
                    Registry.graphics_backend.draw.line(
                        canvas.pygame_surface,
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
            returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width=width), points
        else:
            return None, cache
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class RotatedRect: # https://stackoverflow.com/a/73855696
    """
    Draw a rectangle, centered at x, y.
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
    def __init__(self, color=None, center_of_rect=None, radius=None, height=None, rotation_angle=0, cache=None, width=0, canvas=None):
        """
        Draw a rectangle, centered at x, y.
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
        self.color = color
        self.center_of_rect = center_of_rect
        self.radius = radius
        self.height = height
        self.rotation_angle = rotation_angle
        self.cache = cache
        self.width = width
        self.canvas = canvas

    def draw(self, color=None, center_of_rect=None, radius=None, height=None, rotation_angle=None, cache=None, width=None, canvas=None):
        """
        Draw a rectangle, centered at x, y.
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
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if center_of_rect is None:
            center_of_rect = self.center_of_rect
        if radius is None:
            radius = self.radius
        if height is None:
            height = self.height
        if rotation_angle is None:
            rotation_angle = self.rotation_angle
        if cache is None:
            cache = self.cache
        if width is None:
            width = self.width
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width=width), cache
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
                return returnable
            else:
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
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
            returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width=width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Rect:
    def __init__(self, color=None, rect=None, width=-1, border_radius=-1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1, canvas=None):
        self.color = color
        self.rect = rect
        self.width = width
        self.border_radius = border_radius
        self.border_top_left_radius = border_top_left_radius
        self.border_top_right_radius = border_top_right_radius
        self.border_bottom_left_radius = border_bottom_left_radius
        self.border_bottom_right_radius = border_bottom_right_radius
        self.canvas = canvas

    def draw(self, color=None, rect=None, width=None, border_radius=None, border_top_left_radius=None, border_top_right_radius=None, border_bottom_left_radius=None, border_bottom_right_radius=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if rect is None:
            rect = self.rect
        if width is None:
            width = self.width
        if border_radius is None:
            border_radius = self.border_radius
        if border_top_left_radius is None:
            border_top_left_radius = self.border_top_left_radius
        if border_top_right_radius is None:
            border_top_right_radius = self.border_top_right_radius
        if border_bottom_left_radius is None:
            border_bottom_left_radius = self.border_bottom_left_radius
        if border_bottom_right_radius is None:
            border_bottom_right_radius = self.border_bottom_right_radius
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.rect(canvas.pygame_surface, color, rect, width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Circle:
    def __init__(self, color=None, center=None, radius=None, width=0, canvas=None):
        self.color = color
        self.center = center
        self.radius = radius
        self.width = width
        self.canvas = canvas

    def draw(self, color=None, center=None, radius=None, width=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if center is None:
            center = self.center
        if radius is None:
            radius = self.radius
        if width is None:
            width = self.width
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.circle(canvas.pygame_surface, color, center, abs(radius), width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Arc:
    def __init__(self, color=None, rect=None, start_angle=None, stop_angle=None, width=1, canvas=None):
        self.color = color
        self.rect = rect
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.width = width
        self.canvas = canvas

    def draw(self, color=None, rect=None, start_angle=None, stop_angle=None, width=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if rect is None:
            rect = self.rect
        if start_angle is None:
            start_angle = self.start_angle
        if stop_angle is None:
            stop_angle = self.stop_angle
        if width is None:
            width = self.width
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.arc(canvas.pygame_surface, color, rect, start_angle, stop_angle, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Polygon:
    def __init__(self, color=None, points=None, width=0, canvas=None):
        self.color = color
        self.points = points
        self.width = width
        self.canvas = canvas

    def draw(self, color=None, points=None, width=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if points is None:
            points = self.points
        if width is None:
            width = self.width
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Ellipse:
    def __init__(self, color=None, rect=None, width=0, canvas=None):
        self.color = color
        self.rect = rect
        self.width = width
        self.canvas = canvas

    def draw(self, color=None, rect=None, width=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if rect is None:
            rect = self.rect
        if width is None:
            width = self.width
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.ellipse(canvas.pygame_surface, color, rect, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Pixel:
    def __init__(self, color=None, point=None, canvas=None):
        if Registry.display_mode == Constants.PYGAME:
            self.drawing_extension = importlib.import_module("pygame.gfxdraw")

        self.color = color
        self.point = point
        self.canvas = canvas

    def draw(self, color=None, point=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if point is None:
            point = self.point
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            try:
                returnable = self.drawing_extension.pixel(canvas.pygame_surface, color, point), True
            except:
                temp_rect = Registry.graphics_backend.rect.Rect(*point, 1, 1)
                returnable = Registry.graphics_backend.draw.rect(canvas.pygame_surface, color, temp_rect, 1), False
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Curved_Lines:
    def __init__(self, color=None, points=None, steps=2, canvas=None):
        if Registry.display_mode == Constants.PYGAME:
            self.drawing_extension = importlib.import_module("pygame.gfxdraw")

        self.color = color
        self.points = points
        self.steps = steps
        self.canvas = canvas

    def draw(self, color=None, points=None, steps=None, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if color is None:
            color = self.color
        if points is None:
            points = self.points
        if steps is None:
            steps = self.steps
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if len(points) > 2:
                try:
                    returnable = self.drawing_extension.bezier(canvas.pygame_surface, points, steps, color), True
                    end = time.perf_counter()
                    DrawIntermediary.total_time_spent_drawing += end-start
                    return returnable
                except:
                    pass
            returnable = self.lines(canvas, color, points, width=1, closed=False), False
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

class Draw:
    def __init__(self, canvas=None):
        if Registry.display_mode == Constants.PYGAME:
            self.drawing_extension = importlib.import_module("pygame.gfxdraw")

        self.canvas = canvas

    def line(self, color, start, end, width, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if Registry.anti_aliasing:
                returnable = Registry.graphics_backend.draw.aaline(canvas.pygame_surface, color, start, end, width)
            else:
                returnable = Registry.graphics_backend.draw.line(canvas.pygame_surface, color, start, end, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def lines(self, color, points, width=1, closed=False, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if len(points) < 2:
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
                return
            if Registry.anti_aliasing:
                returnable = Registry.graphics_backend.draw.aalines(canvas.pygame_surface, color, closed, points, width)
            else:
                returnable = Registry.graphics_backend.draw.lines(canvas.pygame_surface, color, closed, points, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def advanced_polygon(self, color, centre, radius, number_of_sides, rotation_angle=0, width=0, cache=None, wire_frame=False, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width=width), cache
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
                return returnable
            else:
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
                return None, cache

        if wire_frame:
            for i in range(0, number_of_sides):
                DrawIntermediary.number_of_draw_calls += 1
                if Registry.display_mode == Constants.PYGAME:
                    Registry.graphics_backend.draw.line(
                        canvas.pygame_surface,
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
            returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width=width), points
        else:
            end = time.perf_counter()
            DrawIntermediary.total_time_spent_drawing += end-start
            return None, cache
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

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
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width=width), cache
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
                return returnable
            else:
                end = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end-start
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
            returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width=width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def rect(self, color, rect, width, border_radius=-1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.rect(canvas.pygame_surface, color, rect, width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def circle(self, color, center, radius, width=0, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if abs(radius) < 1:
            end = time.perf_counter()
            DrawIntermediary.total_time_spent_drawing += end-start
            return
        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.circle(canvas.pygame_surface, color, center, abs(radius), width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def arc(self, color, rect, start_angle, stop_angle, width=1, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.arc(canvas.pygame_surface, color, rect, start_angle, stop_angle, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def polygon(self, color, points, width=0, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.polygon(canvas.pygame_surface, color, points, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def ellipse(self, color, rect, width=0, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = Registry.graphics_backend.draw.ellipse(canvas.pygame_surface, color, rect, width)
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def pixel(self, color, point, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            try:
                returnable = self.drawing_extension.pixel(canvas.pygame_surface, color, point), True
            except:
                temp_rect = Registry.graphics_backend.rect.Rect(*point, 1, 1)
                returnable = Registry.graphics_backend.draw.rect(canvas.pygame_surface, color, temp_rect, 1), False
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable

    def curved_lines(self, color, points, steps=2, canvas=None):
        start = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if len(points) > 2:
                try:
                    returnable = self.drawing_extension.bezier(canvas.pygame_surface, points, steps, color), True
                    end = time.perf_counter()
                    DrawIntermediary.total_time_spent_drawing += end-start
                    return returnable
                except:
                    pass
            returnable = self.lines(canvas, color, points, width=1, closed=False), False
        else:
            raise NotImplementedError
        end = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end-start
        return returnable