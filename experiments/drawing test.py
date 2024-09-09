import pmma
import random
import math

import pygame

import time

pmma.init()

pmma.set_allow_anti_aliasing(True)
pmma.set_anti_aliasing_level(128)

#pmma._Registry.do_anti_aliasing = False
#pmma._Registry.anti_aliasing_level = 16

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True, vsync=False)

events = pmma.Events()

line = pmma.Line()
line.set_start((300, 300))
line.set_end((500, 500))
line.set_color([255, 0, 0])

pixel = pmma.Pixel()
pixel.set_position((100, 100))
pixel.set_color([255, 255, 255])

radial_polygon = pmma.RadialPolygon()
radial_polygon.set_center([500, 500])
radial_polygon.set_radius(100)
radial_polygon.set_color([255, 0, 0])
radial_polygon.set_point_count(point_count=30)

s = time.perf_counter()
while pmma.Backpack.running:
    events.handle()

    display.clear([0, 0, 0])

    start = time.perf_counter()
    radial_polygon.render()
    line.render()
    end = time.perf_counter()
    #print(1/(end-start))
    #radial_polygon.set_rotation((time.perf_counter()-s)*60)

    line.set_rotation((time.perf_counter()-s)*5)
    #line.set_end((500, 60*(time.perf_counter()-start)))

    pmma.compute()
    display.refresh(refresh_rate=60)
    #print(display.get_refresh_rate())

pmma.quit()