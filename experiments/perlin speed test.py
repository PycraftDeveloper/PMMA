import pmma

pmma.init(use_c_acceleration=False)

import time

noise = pmma.Perlin()

while True:
    total_time = 0
    for i in range(1_000_000):
        s = time.perf_counter()
        noise.generate_1D_perlin_noise(i)
        e = time.perf_counter()
        total_time += e - s
    print(1/(total_time/i))