import pmma
import time
import random

pmma.init()

display = pmma.Display()
display.create(1280, 720)

text = pmma.Text()

image = pmma.Image(r"H:\Pictures\Screenshot 2023-09-30 115219.png")

events = pmma.Events()

registry = pmma.Registry()

while registry.running:
    #print(display.get_fps())
    display.clear(255, 0, 0)

    image.blit([0, 0])

    text.render(
        "Pycraft",
size=30, foreground_color=(0, 0, 0), background_color=(0, 0, 255), position=[0, 0])

    events.handle()

    display.refresh(refresh_rate=2000)

time.sleep(30)