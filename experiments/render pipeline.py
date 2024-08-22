import pmma
import random

import pygame

import time

pmma.init()

display = pmma.Display()
display.create(1280, 720, fullscreen=False)

events = pmma.Events()

rp = pmma.RenderPipeline()
rp.add(pmma.AdvancedPolygon([1, 1, 0], (0, 0), 1, 8))
rp.add(pmma.Ellipse([0, 1, 0], (0, 0), (0.2, 0.8)))
rp.add(pmma.CurvedLines([1, 1, 1], ((0, 0), (1, 1), (0.5, -0.5))))

while pmma.Registry.running:
    events.handle()

    display.clear(0, 0, 0)

    #second_rect.draw()

    #draw.rect([255, 0, 0], (100, 100), (500, 500))

    #pygame.draw.circle(display.pygame_surface.pygame_surface, (0, 0, 255), (100, 100), 50)
    start = time.perf_counter()
    rp.render()
    end = time.perf_counter()
    print(1/(end-start))

    #print(rect.hardware_accelerated_data)

    pmma.compute()
    display.refresh()

pmma.quit()