import pmma
import time
from PIL import Image
import numpy
import numba

@numba.njit()
def to_tuple(array):
    final_result = numpy.empty((array.shape[0], array.shape[1], 3), dtype=numpy.int64)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            final_result[i, j, :] = array[i, j]
    return final_result

pmma.init()

noise = pmma.Perlin(do_prefill=False, octaves=4, persistence=0.4)

array = noise.generate_2D_perlin_noise_from_range([0, 2, 1000], [0, 2, 1000], new_range=[0, 255])

final_result = to_tuple(array)

###

s = time.perf_counter()
array = noise.generate_2D_perlin_noise_from_range([0, 2, 1000], [0, 2, 1000], new_range=[0, 255])

final_result = to_tuple(array)

e = time.perf_counter()

img = Image.new("RGB", [1000, 1000])
img.putdata([tuple(pixel) for row in final_result for pixel in row])
#e = time.perf_counter()
print(1/(e-s))
img.show()

pmma.quit()
quit()