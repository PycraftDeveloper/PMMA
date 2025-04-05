from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

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

def grad(hash, x, y=0, z=0):
    """
    🟩 **R** -
    """
    h = hash & 15
    u = x if h < 8 else y
    v = y if h < 4 else (x if h == 12 or h == 14 else z)
    return ((u if h & 1 == 0 else -u) + (v if h & 2 == 0 else -v))

class ExtendedPerlinNoise:
    """
    🟩 **R** -
    """
    def __init__(self, seed, octaves, persistence):
        """
        🟩 **R** -
        """
        self._math__module = _ModuleManager.import_module("math")

        self._numpy__module = _ModuleManager.import_module("numpy")

        self.permutation = [0]*512
        self.init_permutation(seed)
        self.octaves = octaves
        self.persistence = persistence

    def init_permutation(self, seed):
        """
        🟩 **R** -
        """
        rng = self._numpy__module.random.RandomState(seed)
        perm = rng.permutation(256)
        for i in range(256):
            self.permutation[i] = self.permutation[i + 256] = perm[i]

    def perlin(self, x, y=0, z=0):
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

        A = self.permutation[X  ]+Y
        AA = self.permutation[A]+Z
        AB = self.permutation[A+1]+Z
        B = self.permutation[X+1]+Y
        BA = self.permutation[B]+Z
        BB = self.permutation[B+1]+Z

        return lerp(w, lerp(v, lerp(u, grad(self.permutation[AA  ], x  , y  , z  ),
                                       grad(self.permutation[BA  ], x-1, y  , z  )),
                               lerp(u, grad(self.permutation[AB  ], x  , y-1, z  ),
                                       grad(self.permutation[BB  ], x-1, y-1, z  ))),
                       lerp(v, lerp(u, grad(self.permutation[AA+1], x  , y  , z-1),
                                       grad(self.permutation[BA+1], x-1, y  , z-1)),
                               lerp(u, grad(self.permutation[AB+1], x  , y-1, z-1),
                                       grad(self.permutation[BB+1], x-1, y-1, z-1))))

    def generate_fbm_1d(self, input_array):
        """
        🟩 **R** -
        """
        length = input_array.shape[0]
        output_array = self._numpy__module.empty(length, dtype=self._numpy__module.float64)
        for i in range(length):
            amplitude = 1.0
            frequency = 1.0
            total = 0.0
            max_amplitude = 0.0
            for j in range(self.octaves):
                total += self.perlin(input_array[i] * frequency) * amplitude
                max_amplitude += amplitude
                amplitude *= self.persistence
                frequency *= 2
            output_array[i] = total / max_amplitude
        return self._numpy__module.asarray(output_array)

    def generate_fbm_2d(self, input_array):
        """
        🟩 **R** -
        """
        height = input_array.shape[0]
        width = input_array.shape[1]
        output_array = self._numpy__module.empty((height, width), dtype=self._numpy__module.float64)
        for i in range(height):
            for j in range(width):
                x = input_array[i, j, 0]
                y = input_array[i, j, 1]
                amplitude = 1.0
                frequency = 1.0
                total = 0.0
                max_amplitude = 0.0
                for k in range(self.octaves):
                    total += self.perlin(x * frequency, y * frequency) * amplitude
                    max_amplitude += amplitude
                    amplitude *= self.persistence
                    frequency *= 2
                output_array[i, j] = total / max_amplitude
        return self._numpy__module.asarray(output_array)

    def generate_fbm_3d(self, input_array):
        """
        🟩 **R** -
        """
        depth = input_array.shape[0]
        height = input_array.shape[1]
        width = input_array.shape[2]
        output_array = self._numpy__module.empty((depth, height, width), dtype=self._numpy__module.float64)

        for i in range(depth):
            for j in range(height):
                for k in range(width):
                    x = input_array[i, j, k, 0]
                    y = input_array[i, j, k, 1]
                    z = input_array[i, j, k, 2]
                    amplitude = 1.0
                    frequency = 1.0
                    total = 0.0
                    max_amplitude = 0.0
                    for l in range(self.octaves):
                        total += self.perlin(x * frequency, y * frequency, z * frequency) * amplitude
                        max_amplitude += amplitude
                        amplitude *= self.persistence
                        frequency *= 2
                    output_array[i, j, k] = total / max_amplitude
        return self._numpy__module.asarray(output_array)