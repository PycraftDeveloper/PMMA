import pmma

pmma.init()

events = pmma.Events()
controllers = pmma.Controllers()

while True:
    events.handle()

    print(controllers.get_controller(0))

    pmma.compute()

pmma.quit()