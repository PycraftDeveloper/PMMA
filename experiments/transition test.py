import time
import pmma

pmma.init()

transition = pmma.Transition()
transition.create(None, pmma.Constants.COORDINATE_TRANSITION, [0, 0], [10, 10], 10)
transition.start()
while True:
    time.sleep(1)
    print(transition.get_animated_value())