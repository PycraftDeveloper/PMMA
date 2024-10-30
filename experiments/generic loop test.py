import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720, full_screen=False)

events = pmma.Events()

while True:
    events.handle()

    pmma.compute()

    display.refresh(refresh_rate=60)