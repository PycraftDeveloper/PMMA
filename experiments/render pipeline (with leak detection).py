import pmma
import random

import pygame

import time

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False, resizable=True, vsync=False)

events = pmma.Events()

rp = pmma.RenderPipeline()
circ = pmma.Circle([46, 255, 231], (0, 0), 1)
rp.add(circ)

color = pmma.Color()
color.input_color((0, 0, 0))

import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

while pmma.Registry.running:
    events.handle()

    color.generate_random_color(format=pmma.Constants.RGB)

    #display.clear(color.generate_random_color(format=pmma.Constants.RGB))

    #print(color.output_color(pmma.Constants.RGB))

    display.clear([0, 123, 0])

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
    display.refresh(refresh_rate=2000)

# Take a snapshot of memory allocations
snapshot = tracemalloc.take_snapshot()

# Filter and sort statistics by memory usage
top_stats = snapshot.statistics('lineno')

print("[ Top 10 memory consuming lines ]")
for stat in top_stats[:10]:
    print(stat)

print("\n[ Memory consumption by object type ]")
for stat in snapshot.statistics('traceback')[:10]:
    print(f"{stat.count} objects of {stat.size / 1024:.1f} KiB each allocated at:\n")
    for line in stat.traceback.format():
        print(line)

#pmma.quit()