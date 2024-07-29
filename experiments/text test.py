import pmma
import random
import time

pmma.init()

display = pmma.Display()
display.create(1280, 720)

text = pmma.Text()

events = pmma.Events()

registry = pmma.Registry()

while registry.running:
    #print(display.get_fps())
    display.clear(255, 0, 0)

    text.render(
str(random.random()),
size=30, foreground_color=(0, 0, 0), background_color=(0, 0, 255), position=[0, 0])

    events.handle()

    display.refresh(refresh_rate=1000)

time.sleep(30)