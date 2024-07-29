import pmma
import random

pmma.init()

perlin = pmma.Perlin()

class one_D:
    def __init__(self):
        self.min = float("inf")
        self.max = -float("inf")

    def test(self):
        self.c = False
        option = random.randint(0, 1)
        if option == 0:
            value = perlin.generate_1D_perlin_noise(random.random())
        else:
            value = perlin.generate_1D_perlin_noise(random.randint(0, 999999999))

        if value > self.max:
            self.max = value
            self.c = True
        if value < self.min:
            self.min = value
            self.c = True

class two_D:
    def __init__(self):
        self.min = float("inf")
        self.max = -float("inf")

    def test(self):
        self.c = False
        option = random.randint(0, 1)
        if option == 0:
            value = perlin.generate_2D_perlin_noise(random.random(), random.random())
        else:
            value = perlin.generate_2D_perlin_noise(random.randint(0, 999999999), random.randint(0, 999999999))

        if value > self.max:
            self.max = value
            self.c = True
        if value < self.min:
            self.min = value
            self.c = True

class three_D:
    def __init__(self):
        self.min = float("inf")
        self.max = -float("inf")

    def test(self):
        self.c = False
        option = random.randint(0, 1)
        if option == 0:
            value = perlin.generate_3D_perlin_noise(random.random(), random.random(), random.random())
        else:
            value = perlin.generate_3D_perlin_noise(random.randint(0, 999999999),random.randint(0, 999999999), random.randint(0, 999999999))

        if value > self.max:
            self.max = value
            self.c = True
        if value < self.min:
            self.min = value
            self.c = True

one = one_D()
two = two_D()
three = three_D()

while True:
    one.test()
    two.test()
    three.test()

    if three.c or two.c or one.c:
        print(f"  one: min: {one.min}, max: {one.max}")
        print(f"  two: min: {two.min}, max: {two.max}")
        print(f"three: min: {three.min}, max: {three.max}")