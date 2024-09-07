import pmma
import random
import math

import pygame

import time

pmma.init()

pmma.set_allow_anti_aliasing(True)
pmma.set_anti_aliasing_level(8)

#pmma._Registry.do_anti_aliasing = False
#pmma._Registry.anti_aliasing_level = 16

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True, vsync=False)

events = pmma.Events()

rp = pmma.RenderPipeline()
circ = pmma.Circle([46, 255, 231], (0, 0), 360)
rp.add(circ)
circ2 = pmma.Circle([46, 120, 231], (0, 0), 500, canvas=display)

color = pmma.Color()
color.input_color((255, 255, 255))

while pmma.Backpack.running:
    events.handle()

    #display.clear(color.generate_random_color(format=pmma.Constants.RGB))

    #print(color.output_color(pmma.Constants.RGB))

    display.clear(color)

    #circ.set_radius((1+math.cos(nt))/2)

    #second_rect.draw()

    #draw.rect([255, 0, 0], (100, 100), (500, 500))

    #pygame.draw.circle(display.pygame_surface.pygame_surface, (0, 0, 255), (100, 100), 50)

    start = time.perf_counter()
    rp.render()
    end = time.perf_counter()
    fr = 1/(end-start)
    #print(display.get_refresh_rate())
    #print(fr)
    #coord = (random.randint(0, 1280), random.randint(0, 720))

    #coordinate.input_coordinates(coord)
    #print(coord, coordinate.output_coordinates(format=pmma.Constants.OPENGL_COORDINATES))

    #circ.set_radius(1+(math.sin(time.time())))

    #print(rect.hardware_accelerated_data)
    #time.sleep(3)

    pmma.compute()
    display.refresh(refresh_rate=60)

pmma.quit()