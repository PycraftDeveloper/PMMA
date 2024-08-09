import pmma
import time
import pygame
import traceback

pmma.init()

noise = pmma.Perlin()
r_noise = pmma.Perlin()
g_noise = pmma.Perlin()
b_noise = pmma.Perlin()

display = pmma.Display()
display.create(fullscreen=False, resizable=True)

events = pmma.Events()

draw = pmma.Draw()

backpack = pmma.Backpack

math = pmma.Math()

render_pipeline = []

start = time.perf_counter()
now_time = 0
while backpack.running:
    events.handle()
    display.clear(0, 0, 0)

    draw.circle([255, 255, 255], (300, 300), 100)

    pmma.compute()
    display.refresh(refresh_rate=75)