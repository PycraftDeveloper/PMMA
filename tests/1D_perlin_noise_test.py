import pmma
import time

perlin = pmma.Perlin(seed=0)

perlin.generate_1D_perlin_noise(0)
perlin.generate_2D_perlin_noise(0, 0)

start = time.perf_counter()
for i in range(1000):
    perlin.generate_1D_perlin_noise(i)
end = time.perf_counter()
num_range = (end-start)/i
print(f"1D took {num_range} seconds or {1/num_range}")

start = time.perf_counter()
for i in range(1000):
    perlin.generate_2D_perlin_noise(i, -i)
end = time.perf_counter()
num_range = (end-start)/i
print(f"2D took {num_range} seconds or {1/num_range}")