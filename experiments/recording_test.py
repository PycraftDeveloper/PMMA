import pmma
import time

sampler_src = pmma.Sampler()
sampler_src.start_sampling()

volume = sampler_src.get_volume()
frequency = sampler_src.get_frequency()

print(volume, frequency)

while sampler_src.is_sampling() is False:
    time.sleep(1/10)

volume = sampler_src.get_volume()
frequency = sampler_src.get_frequency()

print(volume, frequency)