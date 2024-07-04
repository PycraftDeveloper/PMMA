import pmma

pmma.init()

display = pmma.Display()
display.create(1280, 720)

text = pmma.Text()

events = pmma.Events()

registry = pmma.Registry()

while registry.running:
    display.clear()

    text.render("Hello my name is PycraftDev", size=30)

    events.handle()

    display.refresh(refresh_rate=1000)