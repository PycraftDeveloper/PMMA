import time
import pmma

pmma.init()

transition = pmma.Transition()
transition.create(None, pmma.Constants.COORDINATE_TRANSITION, [0, 0], [10, 10], 3)
transition.start()
while transition._animation_running:
    time.sleep(1)
    print(transition.get_animated_value())