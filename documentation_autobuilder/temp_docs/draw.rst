
Methods
++++++
.. py:method:: generate_rect_from_points(x, y, width, height) -> NYD:

Line (``pmma.Line``)
=======

Object
++++++
.. py:class:: Line

Methods
++++++
.. py:method:: Line.set_color(color) -> NYD:

.. py:method:: Line.set_start(start) -> NYD:

.. py:method:: Line.set_end(end) -> NYD:

.. py:method:: Line.set_width(width) -> NYD:

.. py:method:: Line.set_canvas(canvas) -> NYD:

.. py:method:: Line.quit() -> NYD:

.. py:method:: Line.draw() -> NYD:

Lines (``pmma.Lines``)
=======

Object
++++++
.. py:class:: Lines

Methods
++++++
.. py:method:: Lines.set_color(color) -> NYD:

.. py:method:: Lines.set_points(points) -> NYD:

.. py:method:: Lines.set_width(width) -> NYD:

.. py:method:: Lines.set_closed(closed) -> NYD:

.. py:method:: Lines.set_canvas(canvas) -> NYD:

.. py:method:: Lines.quit() -> NYD:

.. py:method:: Lines.draw() -> NYD:

Advanced Polygon (``pmma.AdvancedPolygon``)
=======

Object
++++++
.. py:class:: AdvancedPolygon

Methods
++++++
.. py:method:: AdvancedPolygon.set_color(color) -> NYD:

.. py:method:: AdvancedPolygon.set_centre(centre) -> NYD:

.. py:method:: AdvancedPolygon.set_radius(radius) -> NYD:

.. py:method:: AdvancedPolygon.set_number_of_sides(number_of_sides) -> NYD:

.. py:method:: AdvancedPolygon.set_rotation_angle(rotation_angle) -> NYD:

.. py:method:: AdvancedPolygon.set_width(width) -> NYD:

.. py:method:: AdvancedPolygon.set_wire_frame(wire_frame) -> NYD:

.. py:method:: AdvancedPolygon.set_canvas(canvas) -> NYD:

.. py:method:: AdvancedPolygon.quit() -> NYD:

.. py:method:: AdvancedPolygon.draw() -> NYD:

Rotated Rect (``pmma.RotatedRect``)
=======

Object
++++++
.. py:class:: RotatedRect

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
  
Methods
++++++
.. py:method:: RotatedRect.set_color(color) -> NYD:

.. py:method:: RotatedRect.set_center_of_rect(center_of_rect) -> NYD:

.. py:method:: RotatedRect.set_radius(radius) -> NYD:

.. py:method:: RotatedRect.set_height(height) -> NYD:

.. py:method:: RotatedRect.set_rotation_angle(rotation_angle) -> NYD:

.. py:method:: RotatedRect.set_width(width) -> NYD:

.. py:method:: RotatedRect.set_canvas(canvas) -> NYD:

.. py:method:: RotatedRect.quit() -> NYD:

.. py:method:: RotatedRect.draw() -> NYD:

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
  
Rect (``pmma.Rect``)
=======

Object
++++++
.. py:class:: Rect

Methods
++++++
.. py:method:: Rect.set_color(color) -> NYD:

.. py:method:: Rect.set_rect(rect) -> NYD:

.. py:method:: Rect.set_width(width) -> NYD:

.. py:method:: Rect.set_border_radius(border_radius) -> NYD:

.. py:method:: Rect.set_border_top_left_radius(border_top_left_radius) -> NYD:

.. py:method:: Rect.set_border_top_right_radius(border_top_right_radius) -> NYD:

.. py:method:: Rect.set_border_bottom_left_radius(border_bottom_left_radius) -> NYD:

.. py:method:: Rect.set_border_bottom_right_radius(border_bottom_right_radius) -> NYD:

.. py:method:: Rect.set_canvas(canvas) -> NYD:

.. py:method:: Rect.quit() -> NYD:

.. py:method:: Rect.draw() -> NYD:

Circle (``pmma.Circle``)
=======

Object
++++++
.. py:class:: Circle

Methods
++++++
.. py:method:: Circle.set_color(color) -> NYD:

.. py:method:: Circle.set_center(center) -> NYD:

.. py:method:: Circle.set_radius(radius) -> NYD:

.. py:method:: Circle.set_width(width) -> NYD:

.. py:method:: Circle.set_canvas(canvas) -> NYD:

.. py:method:: Circle.quit() -> NYD:

.. py:method:: Circle.draw() -> NYD:

Arc (``pmma.Arc``)
=======

Object
++++++
.. py:class:: Arc

Methods
++++++
.. py:method:: Arc.set_color(color) -> NYD:

.. py:method:: Arc.set_rect(rect) -> NYD:

.. py:method:: Arc.set_start_angle(start_angle) -> NYD:

.. py:method:: Arc.set_stop_angle(stop_angle) -> NYD:

.. py:method:: Arc.set_width(width) -> NYD:

.. py:method:: Arc.set_canvas(canvas) -> NYD:

.. py:method:: Arc.quit() -> NYD:

.. py:method:: Arc.draw() -> NYD:

Polygon (``pmma.Polygon``)
=======

Object
++++++
.. py:class:: Polygon

Methods
++++++
.. py:method:: Polygon.set_color(color) -> NYD:

.. py:method:: Polygon.set_points(points) -> NYD:

.. py:method:: Polygon.set_width(width) -> NYD:

.. py:method:: Polygon.set_canvas(canvas) -> NYD:

.. py:method:: Polygon.quit() -> NYD:

.. py:method:: Polygon.draw() -> NYD:

Ellipse (``pmma.Ellipse``)
=======

Object
++++++
.. py:class:: Ellipse

Methods
++++++
.. py:method:: Ellipse.set_color(color) -> NYD:

.. py:method:: Ellipse.set_rect(rect) -> NYD:

.. py:method:: Ellipse.set_width(width) -> NYD:

.. py:method:: Ellipse.set_canvas(canvas) -> NYD:

.. py:method:: Ellipse.quit() -> NYD:

.. py:method:: Ellipse.draw() -> NYD:

Pixel (``pmma.Pixel``)
=======

Object
++++++
.. py:class:: Pixel

Methods
++++++
.. py:method:: Pixel.set_color(color) -> NYD:

.. py:method:: Pixel.set_point(point) -> NYD:

.. py:method:: Pixel.set_canvas(canvas) -> NYD:

.. py:method:: Pixel.quit() -> NYD:

.. py:method:: Pixel.draw() -> NYD:

Curved Lines (``pmma.CurvedLines``)
=======

Object
++++++
.. py:class:: CurvedLines

Methods
++++++
.. py:method:: CurvedLines.set_color(color) -> NYD:

.. py:method:: CurvedLines.set_points(points) -> NYD:

.. py:method:: CurvedLines.set_steps(steps) -> NYD:

.. py:method:: CurvedLines.set_canvas(canvas) -> NYD:

.. py:method:: CurvedLines.quit() -> NYD:

.. py:method:: CurvedLines.draw() -> NYD:

Draw (``pmma.Draw``)
=======

Object
++++++
.. py:class:: Draw

Methods
++++++
.. py:method:: Draw.quit() -> NYD:

.. py:method:: Draw.line(color, start, end, width, canvas=None) -> NYD:

.. py:method:: Draw.lines(color, points, width=1, closed=False, canvas=None) -> NYD:

.. py:method:: Draw.advanced_polygon(color, centre, radius, number_of_sides, rotation_angle=0, width=0, cache=None, wire_frame=False, canvas=None) -> NYD:

.. py:method:: Draw.rotated_rect(color, center_of_rect, radius, height, rotation_angle=0, cache=None, width=0, canvas=None) -> NYD:

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
  
.. py:method:: Draw.rect(color, rect, width, border_radius=-1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1, canvas=None) -> NYD:

.. py:method:: Draw.circle(color, center, radius, width=0, canvas=None) -> NYD:

.. py:method:: Draw.arc(color, rect, start_angle, stop_angle, width=1, canvas=None) -> NYD:

.. py:method:: Draw.polygon(color, points, width=0, canvas=None) -> NYD:

.. py:method:: Draw.ellipse(color, rect, width=0, canvas=None) -> NYD:

.. py:method:: Draw.pixel(color, point, canvas=None) -> NYD:

.. py:method:: Draw.curved_lines(color, points, steps=2, canvas=None) -> NYD:
