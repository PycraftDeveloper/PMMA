import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720, fullscreen=False)

events = pmma.Events()

rp = pmma.RenderPipeline()
rect = pmma.Rect(color=[1, 1, 1], position=[-0.5, -0.5], size=[1, 1])

rp.add(rect)

while pmma.Registry.running:
    events.handle()

    display.clear()

    rp.render()

    print(rect.hardware_accelerated_data)

    pmma.compute()
    display.refresh()

pmma.quit()