import pmma
import pygame

display = pmma.Display()
display.create(1280, 720)

registry = pmma.Registry

events = pmma.Events()

color = [0, 0, 0]
switch = False

draw = pmma.Draw(display)

while registry.running:
    display.clear(*color)

    event_list = events.handle(display)
    for event in event_list:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                switch = not switch

    if switch:
        color = [255, 255, 255]
    else:
        color = [0, 0, 0]

    draw.curved_lines((255, 0, 0), [(0, 0), (1000, 1000), (500, 100)], steps=100)

    display.refresh()