import pmma
import random

import pygame

import time

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True)

events = pmma.Events()

rp = pmma.RenderPipeline()
circ = pmma.Circle([46, 255, 231], (0, 0), 1)
rp.add(circ)

color = pmma.Color()
color.input_color((0, 0, 0))

while pmma.Registry.running:
    events.handle()

    display.clear(color)

    #second_rect.draw()

    #draw.rect([255, 0, 0], (100, 100), (500, 500))

    #pygame.draw.circle(display.pygame_surface.pygame_surface, (0, 0, 255), (100, 100), 50)

    start = time.perf_counter()
    rp.render()
    end = time.perf_counter()
    #print(1/(end-start))
    #print(display.get_refresh_rate())

    #print(rect.hardware_accelerated_data)
    #time.sleep(3)

    pmma.compute()
    display.refresh()

pmma.quit()