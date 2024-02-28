import pmma

pmma.Registry.compile_math_functions = True

print("Go")
perlin = pmma.Perlin(100)

pmma.extrapolate2(perlin.seed, 0, 0, 0, 0)

print(perlin.generate_2D_perlin_noise(0, 0))