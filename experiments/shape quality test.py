import pmma

display = pmma.Display()
display.create()

pmma.set_allow_anti_aliasing(False)

events = pmma.Events()

background = pmma.RadialPolygon()
background.set_radius(display.get_height()//2 - 100)
background.set_color((255, 0, 0))
background.set_center((0, 0), pmma.Constants.OPENGL_COORDINATES)

foreground = pmma.RadialPolygon()
foreground.set_radius(display.get_height()//2 - 100)
foreground.set_color((0, 255, 0))
foreground.set_center((0, 0), pmma.Constants.OPENGL_COORDINATES)

while pmma.get_application_running():
    events.handle()

    display.clear([0, 0, 0])

    background.render()
    foreground.render()

    pmma.compute()
    display.refresh(refresh_rate=60)

    print(background.get_point_count(), foreground.get_point_count())