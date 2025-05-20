from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

PERMUTATION_SIZE = 512

def fade(t):
    """
    🟩 **R** -
    """
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(t, a, b):
    """
    🟩 **R** -
    """
    return a + t * (b - a)

def grad1(hash, x):
    """
    🟩 **R** -
    """
    h = hash & 15
    grad = 1.0 + (h & 7)  # Gradient value is one of 1.0, 2.0, ..., 8.0
    if h & 8:
        grad = -grad  # and a random sign for the gradient
    return grad * x  # Multiply the gradient with the distance

def grad2(hash, x, y):
    """
    🟩 **R** -
    """
    h = hash & 7  # Convert low 3 bits of hash code
    u = x if h < 4 else y  # into 8 simple gradient directions,
    v = y if h < 4 else x  # and compute the dot product with (x,y).
    return ((-u if h & 1 else u) + (-2.0 * v if h & 2 else 2.0 * v))

def grad3(hash, x, y, z):
    """
    🟩 **R** -
    """
    h = hash & 15
    u = x if h < 8 else y
    v = y if h < 4 else (x if h == 12 or h == 14 else z)
    return ((u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v))

class PerlinNoise:
    """
    🟩 **R** -
    """
    def __init__(self, seed, octaves, persistence):
        """
        🟩 **R** -
        """
        self._random__module = _ModuleManager.import_module("random")
        self._math__module = _ModuleManager.import_module("math")

        self.p = [0]*512
        self.init_permutation(seed)
        self.octaves = octaves
        self.persistence = persistence

    def init_permutation(self, seed):
        """
        🟩 **R** -
        """
        perm = [0]*256

        for i in range(256):
            perm[i] = i

        self._random__module.seed(seed)
        for i in range(255, 0, -1):
            j = self._random__module.randint(0, i)
            temp = perm[i]
            perm[i] = perm[j]
            perm[j] = temp

        for i in range(256):
            self.p[256 + i] = self.p[i] = perm[i]

    def perlin1D(self, x):
        """
        🟩 **R** -
        """
        X = int(self._math__module.floor(x)) & 255
        x -= self._math__module.floor(x)

        u = fade(x)

        A = self.p[X]
        B = self.p[X + 1]

        return lerp(u, grad1(self.p[A], x), grad1(self.p[B], x - 1))

    def perlin2D(self, x, y):
        """
        🟩 **R** -
        """
        X = int(self._math__module.floor(x)) & 255
        Y = int(self._math__module.floor(y)) & 255
        x -= self._math__module.floor(x)
        y -= self._math__module.floor(y)

        u = fade(x)
        v = fade(y)

        A = self.p[X] + Y
        B = self.p[X + 1] + Y

        return lerp(v, lerp(u, grad2(self.p[A], x, y), grad2(self.p[B], x - 1, y)),
                            lerp(u, grad2(self.p[A + 1], x, y - 1), grad2(self.p[B + 1], x - 1, y - 1)))

    def perlin3D(self, x, y, z):
        """
        🟩 **R** -
        """
        X = int(self._math__module.floor(x)) & 255
        Y = int(self._math__module.floor(y)) & 255
        Z = int(self._math__module.floor(z)) & 255
        x -= self._math__module.floor(x)
        y -= self._math__module.floor(y)
        z -= self._math__module.floor(z)

        u = fade(x)
        v = fade(y)
        w = fade(z)

        A = self.p[X] + Y
        AA = self.p[A] + Z
        AB = self.p[A + 1] + Z
        B = self.p[X + 1] + Y
        BA = self.p[B] + Z
        BB = self.p[B + 1] + Z

        return lerp(w, lerp(v, lerp(u, grad3(self.p[AA], x, y, z), grad3(self.p[BA], x - 1, y, z)),
                                lerp(u, grad3(self.p[AB], x, y - 1, z), grad3(self.p[BB], x - 1, y - 1, z))),
                            lerp(v, lerp(u, grad3(self.p[AA + 1], x, y, z - 1), grad3(self.p[BA + 1], x - 1, y, z - 1)),
                                lerp(u, grad3(self.p[AB + 1], x, y - 1, z - 1), grad3(self.p[BB + 1], x - 1, y - 1, z - 1))))

    def fBM1D(self, x):
        """
        🟩 **R** -
        """
        total = 0.0
        frequency = 1.0
        amplitude = 1.0
        maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin1D(x * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue

    def fBM2D(self, x, y):
        """
        🟩 **R** -
        """
        total = 0.0
        frequency = 1.0
        amplitude = 1.0
        maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin2D(x * frequency, y * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue

    def fBM3D(self, x, y, z):
        """
        🟩 **R** -
        """
        total = 0.0
        frequency = 1.0
        amplitude = 1.0
        maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin3D(x * frequency, y * frequency, z * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue