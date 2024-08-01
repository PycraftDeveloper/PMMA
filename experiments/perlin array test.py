import pmma
import numpy as np

pmma.init()

perlin = pmma.Perlin(seed=0)
perlin.prefill()
print(perlin.generate_3D_perlin_noise_from_range([10], [10], [10]))