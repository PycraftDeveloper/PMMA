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

line = pmma.Line()
line.set_start((300, 300))
line.set_end((1000, 700))
line.set_color([255, 0, 0])

while pmma.Backpack.running:
    events.handle()

    display.clear([255, 255, 255])

    line.render()

    line.set_end((500, 0))

    pmma.compute()
    display.refresh(refresh_rate=60)

pmma.quit()