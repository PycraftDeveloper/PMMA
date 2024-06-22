import pmma
import numpy

pmma.init()

perlin = pmma.ExtendedPerlin()

values = numpy.linspace(0, 1, 10_000)
data = perlin.generate_1D_perlin_noise(values)
data = [*data]
print(max(data), min(data))