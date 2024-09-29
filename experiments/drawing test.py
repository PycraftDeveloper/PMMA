import pmma
import random
import math

import pygame

import time

pmma.init()

pmma.set_allow_anti_aliasing(False)
pmma.set_anti_aliasing_level(8)

#pmma._Registry.do_anti_aliasing = False
#pmma._Registry.anti_aliasing_level = 16

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True, vsync=False)

events = pmma.Events()

line = pmma.Line()
line.set_start((300, 300))
line.set_end((500, 300))
line.set_color([255, 0, 0])
line.set_width(3)

pixel = pmma.Pixel()
pixel.set_position((100, 100))
pixel.set_color([255, 255, 255])

radial_polygon = pmma.RadialPolygon()
radial_polygon.set_center([500, 500])
radial_polygon.set_radius(400)
radial_polygon.set_color([255, 0, 0])
radial_polygon.set_point_count()
radial_polygon.set_width(10)

rectangle = pmma.Rectangle()
rectangle.set_position((100, 100))
rectangle.set_size((100, 300))
rectangle.set_color([0, 255, 0])
rectangle.set_width(10)

arc = pmma.Arc()
arc.set_center([500, 500])
arc.set_color([0, 0, 255])
arc.set_start_angle(0)
arc.set_stop_angle(68, angle_format=pmma.Constants.DEGREES)
arc.set_radius(300)
arc.set_width(10)

ellipse = pmma.Ellipse()
ellipse.set_position([500, 500])
ellipse.set_color([255, 255, 0])
ellipse.set_size([300, 200])
ellipse.set_width(10)

polygon = pmma.Polygon()
polygon.set_color([255, 0, 255])
polygon.set_points([(100, 100), (200, 100), (200, 200), (100, 200)])
polygon.set_closed(False)
polygon.set_width(10)

s = time.perf_counter()
while pmma.Backpack.running:
    events.handle()

    display.clear([0, 0, 0])

    start = time.perf_counter()
    #radial_polygon.render()
    line.render()
    rectangle.render()
    pixel.render()
    #arc.render()
    ellipse.render()
    polygon.render()
    end = time.perf_counter()
    #print(1/(end-start))
    #radial_polygon.set_rotation((time.perf_counter()-s)*60)

    #line.set_rotation((time.perf_counter()-s)*5)
    #line.set_end((500, 60*(time.perf_counter()-start)))
    #rectangle.set_rotation((time.perf_counter()-s)*10)

    #ellipse.set_rotation((time.perf_counter()-s))
    #arc.set_rotation((time.perf_counter()-s)*50)

    pmma.compute()
    display.refresh(refresh_rate=60)
    #print(display.get_refresh_rate())

pmma.quit()