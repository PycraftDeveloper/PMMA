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
line.set_start((10, 10))
line.set_end((200, 200))
line.set_color([255, 0, 255])

pixel = pmma.Pixel()
pixel.set_position((400, 350))
pixel.set_color([255, 255, 255])

radial_polygon = pmma.RadialPolygon()
radial_polygon.set_center([400, 350])
radial_polygon.set_radius(300)
radial_polygon.generate_random_color()
radial_polygon.set_point_count(3)

rectangle = pmma.Rectangle()
rectangle.set_center((900, 200))
rectangle.set_size((100, 300))
rectangle.set_color([0, 255, 0])
rectangle.set_width(9000)
#rectangle.set_corner_radius(100)
rectangle.set_rotation(90, format=pmma.Constants.DEGREES)

arc = pmma.Arc()
arc.set_center([500, 500])
arc.set_color([0, 0, 255])
arc.set_start_angle(0)
arc.set_stop_angle(68, angle_format=pmma.Constants.DEGREES)
arc.set_radius(300)

ellipse = pmma.Ellipse()
ellipse.set_center([500, 500])
ellipse.set_color([255, 255, 0])
ellipse.set_size([300, 200])

polygon = pmma.Lines()
polygon.set_color([255, 0, 255])
polygon.set_points([(100, 100), (200, 100), (200, 200), (100, 200), (900, 100)])

general = pmma.General()

s = time.perf_counter()
while pmma.Backpack.running:
    a = time.perf_counter()
    radial_polygon.generate_random_color()
    b = time.perf_counter()
    #print(1/(b-a))
    start = time.perf_counter()
    events.handle()

    display.clear([0, 0, 0])

    line.render()
    radial_polygon.render()
    radial_polygon.render()
    rectangle.render()
    pixel.render()
    #if random.choice([True, False]):
    arc.render()
    ellipse.render()
    polygon.render()

    #radial_polygon.set_point_count(4)

    rectangle.set_corner_radius(int((1+math.sin(general.get_application_run_time()))*50))
    #print(int((1+math.sin(general.get_application_run_time()))*10))
    radial_polygon.set_point_count(int((1+math.sin(general.get_application_run_time()))*10))

    #line.set_end((500, 60*(time.perf_counter()-start)))

    #radial_polygon.set_rotation((time.perf_counter()-s)*60)
    #line.set_rotation((time.perf_counter()-s)*5)
    #rectangle.set_rotation((time.perf_counter()-s)*10)
    ellipse.set_rotation((time.perf_counter()-s))
    arc.set_rotation((time.perf_counter()-s)*50)
    #polygon.set_rotation((time.perf_counter()-s)*10)

    general.compute()
    end = time.perf_counter()

    display.refresh(refresh_rate=75)
    #print(1/(end-start))
    #quit()

pmma.quit()