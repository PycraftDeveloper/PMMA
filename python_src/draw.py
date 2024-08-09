import importlib
import math
import time

import pygame
import pygame.gfxdraw as gfxdraw
import pyglet

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class DrawIntermediary:
    number_of_draw_calls = 0
    total_time_spent_drawing = 0

class Line:
    def __init__(
            self,
            color=None,
            start=None,
            end=None,
            width=1,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.start = start
        self.end = end
        self.width = width
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if Registry.display_mode == Constants.PYGAME:
            if Registry.anti_aliasing:
                returnable = pygame.draw.aaline(
                    self.canvas.pygame_surface.pygame_surface,
                    self.color,
                    self.start,
                    self.end,
                    self.width)

            else:
                returnable = pygame.draw.line(
                    self.canvas.pygame_surface.pygame_surface,
                    self.color,
                    self.start,
                    self.end,
                    self.width)
        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class Lines:
    def __init__(
            self,
            color=None,
            points=None,
            width=1,
            closed=False,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.points = points
        self.width = width
        self.closed = closed
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            if len(self.points) < 2:
                end_time = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end_time - start_time
                return
            if Registry.anti_aliasing:
                returnable = pygame.draw.aalines(
                    self.canvas.pygame_surface.pygame_surface,
                    self.color,
                    self.closed,
                    self.points,
                    self.width)

            else:
                returnable = pygame.draw.lines(
                    self.canvas.pygame_surface.pygame_surface,
                    self.color,
                    self.closed,
                    self.points,
                    self.width)
        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class AdvancedPolygon:
    def __init__(
            self,
            color=None,
            centre=None,
            radius=None,
            number_of_sides=None,
            rotation_angle=0,
            width=0,
            cache=None,
            wire_frame=False,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.centre = centre
        self.radius = radius
        self.number_of_sides = number_of_sides
        self.rotation_angle = rotation_angle
        self.width = width
        self.cache = cache
        self.wire_frame = wire_frame
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.wire_frame:
            for i in range(0, self.number_of_sides):
                if Registry.display_mode == Constants.PYGAME:
                    pygame.draw.line(
                        self.canvas.pygame_surface.pygame_surface,
                        self.color,
                        self.centre, (
                            math.cos(i / self.number_of_sides * Constants.TAU) * self.radius + self.centre[0],
                            math.sin(i / self.number_of_sides * Constants.TAU) * self.radius + self.centre[1]))

        points = [
            (math.cos(i / self.number_of_sides * Constants.TAU + self.rotation_angle) * self.radius + self.centre[0],
                math.sin(i / self.number_of_sides * Constants.TAU + self.rotation_angle) * self.radius + self.centre[1]) for i in range(0, self.number_of_sides)]

        if self.wire_frame:
            width = 1

        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.polygon(
                self.canvas.pygame_surface.pygame_surface,
                self.color,
                points,
                width=width), points
        else:
            return None, self.cache
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
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
    def __init__(
            self,
            color=None,
            center_of_rect=None,
            radius=None,
            height=None,
            rotation_angle=0,
            cache=None,
            width=0,
            canvas=None):

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
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.center_of_rect = center_of_rect
        self.radius = radius
        self.height = height
        self.rotation_angle = rotation_angle
        self.cache = cache
        self.width = width
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
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
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        x, y = self.center_of_rect
        points = []

        # The distance from the center of the rectangle to
        # one of the corners is the same for each corner.
        radius = math.sqrt((self.height / 2)**2 + (radius / 2)**2)

        # Get the angle to one of the corners with respect
        # to the x-axis.
        angle = math.atan2(self.height / 2, radius / 2)

        # Transform that angle to reach each corner of the rectangle.
        angles = [angle, -angle + math.pi, angle + math.pi, -angle]

        # Convert rotation from degrees to radians.
        rot_radians = (math.pi / 180) * self.rotation_angle

        # Calculate the coordinates of each point.
        for angle in angles:
            y_offset = -1 * radius * math.sin(angle + rot_radians)
            x_offset = radius * math.cos(angle + rot_radians)
            points.append((x + x_offset, y + y_offset))

        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.polygon(
                self.canvas.pygame_surface.pygame_surface,
                self.color,
                points,
                width=self.width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class Rect:
    def __init__(
            self,
            color=None,
            rect=None,
            width=-1,
            border_radius=-1,
            border_top_left_radius=-1,
            border_top_right_radius=-1,
            border_bottom_left_radius=-1,
            border_bottom_right_radius=-1,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.rect = rect
        self.width = width
        self.border_radius = border_radius
        self.border_top_left_radius = border_top_left_radius
        self.border_top_right_radius = border_top_right_radius
        self.border_bottom_left_radius = border_bottom_left_radius
        self.border_bottom_right_radius = border_bottom_right_radius
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.rect(
                self.canvas.pygame_surface.pygame_surface,
                self.color,
                self.rect,
                self.width,
                self.border_radius,
                self.border_top_left_radius,
                self.border_top_right_radius,
                self.border_bottom_left_radius,
                self.border_bottom_right_radius)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class Circle:
    def __init__(
            self,
            color=None,
            center=None,
            radius=None,
            width=0,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.center = center
        self.radius = radius
        self.width = width
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1

        if abs(self.radius) < 1:
            end_time = time.perf_counter()
            DrawIntermediary.total_time_spent_drawing += end_time - start_time
            return

        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.circle(
                self.canvas.pygame_surface.pygame_surface,
                self.color,
                self.center,
                abs(self.radius),
                self.width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class Arc:
    def __init__(
            self,
            color=None,
            rect=None,
            start_angle=None,
            stop_angle=None,
            width=1,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.rect = rect
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.width = width
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.arc(
                self.canvas.pygame_surface.pygame_surface,
                self.color,
                self.rect,
                self.start_angle,
                self.stop_angle,
                self.width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class Polygon:
    def __init__(
            self,
            color=None,
            points=None,
            width=0,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.points = points
        self.width = width
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.polygon(
                self.canvas.pygame_surface.pygame_surface,
                self.color,
                self.points,
                self.width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class Ellipse:
    def __init__(
            self,
            color=None,
            rect=None,
            width=0,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.rect = rect
        self.width = width
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.ellipse(
                self.canvas.pygame_surface.pygame_surface,
                self.color,
                self.rect,
                self.width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class Pixel:
    def __init__(
            self,
            color=None,
            point=None,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.point = point
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            try:
                returnable = gfxdraw.pixel(
                    self.canvas.pygame_surface.pygame_surface,
                    self.color,
                    self.point), True

            except:
                temp_rect = pygame.rect.Rect(
                    *self.point,
                    1,
                    1)

                returnable = pygame.draw.rect(
                    self.canvas.pygame_surface.pygame_surface,
                    self.color,
                    temp_rect,
                    1), False

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class CurvedLines:
    def __init__(
            self,
            color=None,
            points=None,
            steps=2,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.color = color
        self.points = points
        self.steps = steps
        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def draw(self):
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            if len(self.points) > 2:
                try:
                    returnable = gfxdraw.bezier(
                        self.canvas.pygame_surface.pygame_surface,
                        self.points,
                        self.steps,
                        self.color), True

                    end_time = time.perf_counter()
                    DrawIntermediary.total_time_spent_drawing += end_time - start_time
                    return returnable
                except:
                    pass

            returnable = self.lines(
                self.canvas,
                self.color,
                self.points,
                width=1,
                closed=False), False

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

class Draw:
    def __init__(
            self,
            canvas=None):

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self.canvas = canvas

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def line(
            self,
            color,
            start,
            end,
            width,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if Registry.anti_aliasing:
                returnable = pygame.draw.aaline(
                    canvas.pygame_surface.pygame_surface,
                    color,
                    start,
                    end,
                    width)

            else:
                returnable = pygame.draw.line(
                    canvas.pygame_surface.pygame_surface,
                    color,
                    start,
                    end,
                    width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def lines(
            self,
            color,
            points,
            width=1,
            closed=False,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if len(points) < 2:
                end_time = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end_time - start_time
                return
            if Registry.anti_aliasing:
                returnable = pygame.draw.aalines(
                    canvas.pygame_surface.pygame_surface,
                    color,
                    closed,
                    points,
                    width)

            else:
                returnable = pygame.draw.lines(
                    canvas.pygame_surface.pygame_surface,
                    color,
                    closed,
                    points,
                    width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def advanced_polygon(
            self,
            color,
            centre,
            radius,
            number_of_sides,
            rotation_angle=0,
            width=0,
            cache=None,
            wire_frame=False,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                returnable = pygame.draw.polygon(
                    canvas.pygame_surface.pygame_surface,
                    color,
                    points,
                    width=width), cache

                end_time = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end_time - start_time
                return returnable
            else:
                end_time = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end_time - start_time
                return None, cache

        if wire_frame:
            for i in range(0, number_of_sides):
                DrawIntermediary.number_of_draw_calls += 1
                if Registry.display_mode == Constants.PYGAME:
                    pygame.draw.line(
                        canvas.pygame_surface.pygame_surface,
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
            returnable = pygame.draw.polygon(
                canvas.pygame_surface.pygame_surface,
                color,
                points,
                width=width), points
        else:
            end_time = time.perf_counter()
            DrawIntermediary.total_time_spent_drawing += end_time - start_time
            return None, cache
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def rotated_rect(
            self,
            color,
            center_of_rect,
            radius,
            height,
            rotation_angle=0,
            cache=None,
            width=0,
            canvas=None): # https://stackoverflow.com/a/73855696

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
        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                returnable = pygame.draw.polygon(
                    canvas.pygame_surface.pygame_surface,
                    color,
                    points,
                    width=width), cache

                end_time = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end_time - start_time
                return returnable
            else:
                end_time = time.perf_counter()
                DrawIntermediary.total_time_spent_drawing += end_time - start_time
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
            returnable = pygame.draw.polygon(
                canvas.pygame_surface.pygame_surface,
                color,
                points,
                width=width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def rect(
            self,
            color,
            rect,
            width,
            border_radius=-1,
            border_top_left_radius=-1,
            border_top_right_radius=-1,
            border_bottom_left_radius=-1,
            border_bottom_right_radius=-1,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.rect(
                canvas.pygame_surface.pygame_surface,
                color,
                rect,
                width,
                border_radius,
                border_top_left_radius,
                border_top_right_radius,
                border_bottom_left_radius,
                border_bottom_right_radius)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def circle(
            self,
            color,
            center,
            radius,
            width=0,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if abs(radius) < 1:
            end_time = time.perf_counter()
            DrawIntermediary.total_time_spent_drawing += end_time - start_time
            return
        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.circle(
                canvas.pygame_surface.pygame_surface,
                color,
                center,
                abs(radius),
                width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def arc(
            self,
            color,
            rect,
            start_angle,
            stop_angle,
            width=1,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.arc(
                canvas.pygame_surface.pygame_surface,
                color,
                rect,
                start_angle,
                stop_angle,
                width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def polygon(
            self,
            color,
            points,
            width=0,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.polygon(
            canvas.pygame_surface.pygame_surface,
            color,
            points,
            width)

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def ellipse(
            self,
            color,
            rect,
            width=0,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            returnable = pygame.draw.ellipse(
                canvas.pygame_surface.pygame_surface,
                color,
                rect,
                width)
        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def pixel(
            self,
            color,
            point,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            try:
                returnable = gfxdraw.pixel(
                    canvas.pygame_surface.pygame_surface,
                    color,
                    point), True

            except:
                temp_rect = pygame.rect.Rect(
                    *point,
                    1,
                    1)

                returnable = pygame.draw.rect(
                    canvas.pygame_surface.pygame_surface,
                    color,
                    temp_rect,
                    1), False

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable

    def curved_lines(
            self,
            color,
            points,
            steps=2,
            canvas=None):

        start_time = time.perf_counter()
        DrawIntermediary.number_of_draw_calls += 1
        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas
        if Registry.display_mode == Constants.PYGAME:
            if len(points) > 2:
                try:
                    returnable = gfxdraw.bezier(
                        canvas.pygame_surface.pygame_surface,
                        points,
                        steps,
                        color), True

                    end_time = time.perf_counter()
                    DrawIntermediary.total_time_spent_drawing += end_time - start_time
                    return returnable
                except:
                    pass
            returnable = self.lines(
                canvas,
                color,
                points,
                width=1,
                closed=False), False

        else:
            raise NotImplementedError
        end_time = time.perf_counter()
        DrawIntermediary.total_time_spent_drawing += end_time - start_time
        return returnable