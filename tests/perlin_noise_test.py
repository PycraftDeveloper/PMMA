import pmma
import random

pmma.Registry.compile_math_functions = True

perlin_src = pmma.Perlin(random.randint(0, 999))
result = perlin_src.generate_2D_perlin_noise(0, 0, [-10, 10])
print(result)

pmma.Registry.compile_math_functions = False

perlin_src = pmma.Perlin(random.randint(0, 999))
result = perlin_src.generate_2D_perlin_noise(0, 0, [-10, 10])
print(result)