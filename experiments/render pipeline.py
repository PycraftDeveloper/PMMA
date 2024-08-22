import pmma

import pygame

import time

pmma.init()

display = pmma.Display()
display.create(1280, 720, fullscreen=False)

events = pmma.Events()

rp = pmma.RenderPipeline()
rect = pmma.Rect(color=[1, 0, 1], position=[0, 0], size=[1, 1])

second_rect = pmma.Rect(color=[0, 0, 255], position=[-0.5, -0.5], size=[1, 1])

draw = pmma.Draw()
for i in range(1000):
    rp.add(rect)

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