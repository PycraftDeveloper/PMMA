import pmma
import random

import pygame

import time

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False)

events = pmma.Events()

rp = pmma.RenderPipeline()
#rp.add(pmma.Rect([1, 0, 0], (0, 0), (0.8, 0.1)))
line = pmma.Line([255, 0, 0], (0, 0), (0.8, 0))
rp.add(line)
rp.add(pmma.Circle([0, 1, 0], (0, 0), 0.5))
rotrect = pmma.RotatedRect([0, 0, 1], (0, 0), 0.5, 0.5, rotation_angle=45)
rp.add(rotrect)

line.set_width(50)
n = 0
while pmma.Registry.running:
    events.handle()

    display.clear(0, 0, 0)
    rotrect.set_rotation_angle(n)

    #second_rect.draw()

    #draw.rect([255, 0, 0], (100, 100), (500, 500))

    #pygame.draw.circle(display.pygame_surface.pygame_surface, (0, 0, 255), (100, 100), 50)

    start = time.perf_counter()
    rp.render()
    end = time.perf_counter()
    print(1/(end-start))

    line.draw()

    #print(rect.hardware_accelerated_data)

    pmma.compute()
    display.refresh()
    n += 10

pmma.quit()