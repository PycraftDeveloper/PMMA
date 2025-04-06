import time
import tkinter

import numpy

import pmma

pmma.init(use_c_acceleration=True)

########################################################################

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

########################################################################

def simple_procedure():
    for i in range(10):
        print(i)
        time.sleep(1)

_thread = pmma.Thread(target=simple_procedure)
_thread.start()
time.sleep(3)
_thread.kill()
time.sleep(10)

########################################################################

root = tkinter.Tk()

_tkinter = pmma.Tkinter()
_tkinter.style('label')
_tkinter.get_display_size()
_tkinter.set_window_size(root, 64, 64, x_position=pmma.Constants.CENTER, y_position=0)

root.update_idletasks()

_tkinter.quit()
root.quit()

########################################################################

print("All tests ran successfully!")