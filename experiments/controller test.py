import pmma

pmma.init()

display = pmma.Display()
display.create(600, 600, fullscreen=False)

events = pmma.Events()
controllers = pmma.Controllers()
w_key = pmma.PrimaryW_KEY()
d_key = pmma.PrimaryD_KEY()

while True:
    events.handle()

    print(w_key.get_double_tapped(), d_key.get_double_tapped())

    pmma.compute()

pmma.quit()