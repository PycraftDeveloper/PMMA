import pmma

pmma.init(log_information=True, log_development=True)

display = pmma.Display()
display.create(resizable=True, full_screen=False, caption="RED", transparent_display=True)

events = pmma.Events()

while True:
    events.handle()

    display.clear(255, 0, 0)

    pmma.compute()
    display.refresh()

pmma.quit()