try:
    from traceback import format_exception
    import random
    import time
    import pmma
    import math

    pmma.init(general_profile_application=False)

    pmma.set_allow_anti_aliasing(False)
    pmma.set_anti_aliasing_level(8)

    canvas = pmma.Display()
    canvas.create(1280, 720, full_screen=False, resizable=True)
    events = pmma.Events()

    N = 1000

    s = int((canvas.get_width()**2 + canvas.get_height()**2)**0.5)

    class Particle:
        def __init__(self, n):
            self.n = n
            self.o = random.randint(500, s)
            self.circ = pmma.RadialPolygon()
            #self.pixel = pmma.Pixel()
            self.circ.set_radius(3)
            self.circ.set_point_count()
            self.circ.set_color([255, 255, 255])
            self.color = pmma.ColorConverter()

        def __del__(self):
            self.circ.quit()

        def render(self, now_time):
            x = (canvas.get_width() - (math.sin(now_time+self.n) * self.o))/2
            y = (canvas.get_height() - (math.cos(now_time+self.n) * self.o))/2

            #self.pixel.set_color(self.color.generate_color(now_time/2))
            #self.pixel.set_position([x, y])
            self.circ.set_center([x, y])

            self.circ.render()

    particles = []

    for i in range(N):
        particles.append(Particle(i))

    col = pmma.ColorConverter()

    start = time.perf_counter()
    now_time = 0
    #pmma.targeted_profile_start()
    while pmma.get_application_running():
        canvas.clear()

        events.handle()

        for particle in particles:
            particle.render(now_time)

        pmma.compute()
        canvas.refresh(refresh_rate=2000)

        now_time = (time.perf_counter() - start)/5

    #pmma.targeted_profile_end()
    pmma.quit()
except Exception as error:
    print("".join(
        format_exception(
            None,
            error,
            error.__traceback__)))