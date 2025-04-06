import numpy

import pmma

pmma.init(use_c_acceleration=True)

math = pmma.Math()

math.smooth_step(0.1)

math.pythag([1, 2])

math.ranger(10, [0, 10], [0, 1])

math.nparray_ranger(numpy.array([10, 10]), [0, 10], [0, 1])

math.compute_position(numpy.array([0, 0, 0]), numpy.array([0, 0, 1]), numpy.array([0, 1, 0]))

math.perspective_fov(70, 16/9, 0.1, 1000)

math.look_at(numpy.array([0, 0, 0]), numpy.array([0, 0, 1]), numpy.array([0, 1, 0]))

math.multiply(numpy.array([1, 2, 3]), numpy.array([4, 5, 6]))

math.quit()

print("All tests ran successfully!")