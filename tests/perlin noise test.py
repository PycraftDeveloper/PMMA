from perlin_noise import PerlinNoise
import time

# Parameters for fBM
octaves = 1 # 6
persistence = 0.5
x, y, z = 0.1, 0.1, 0.1

# Generate noise with different seeds
seed1 = int(time.time())
seed2 = seed1 + 1

noise_1 = PerlinNoise(seed1)
noise_2 = PerlinNoise(seed2)

tt = 0
for i in range(100_000):
    start = time.perf_counter()
    noise1 = noise_1.fBM1D(i/100, octaves, persistence)
    end = time.perf_counter()
    tt += end - start
    noise2 = noise_2.fBM1D(i/100, octaves, persistence)
    value = 1+(noise1 - noise2)
    print("#"*int(value*50))

print(1/(tt/i))