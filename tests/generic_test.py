import random
import sys
from math import floor
from ctypes import c_int64
import time

import numpy as np
import numba
import pygame

import pmma

class Point:
    def __init__(self, n):
        self.x_perlin = pmma.Perlin(random.randint(0, 9999))
        self.y_perlin = pmma.Perlin(random.randint(0, 9999))

        self.x = 1920/2
        self.y = 1080/2

        self.dir_x = (random.random()*2)-1
        self.dir_y = (random.random()*2)-1

        self.n = n

    def render(self):
        v_x = self.x_perlin.generate_2D_perlin_noise(now_time, 0, [0, 10])
        v_y = self.x_perlin.generate_2D_perlin_noise(now_time, 0, [0, 10])

        self.x += v_x*self.dir_x
        self.y += v_y*self.dir_y

        if self.x > 1920 or self.x < 0 or self.y > 1080 or self.y < 0:
            self.x = 1920/2
            self.y = 1080/2

            self.dir_x = (random.random()*2)-1
            self.dir_y = (random.random()*2)-1

        pygame.draw.circle(Surface, [r, g, b], [int(self.x), int(self.y)], 1.5)

pygame.init()

display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

clock = pygame.time.Clock()

start = time.perf_counter()

N = 1000
points = []
for _ in range(N):
    points.append(Point(_))

r_perlin = pmma.Perlin(random.randint(0, 9999))
g_perlin = pmma.Perlin(random.randint(0, 9999))
b_perlin = pmma.Perlin(random.randint(0, 9999))

perlin = pmma.Perlin(random.randint(0, 9999))

k = 255/2

now_time = 0
while True:
    window_size = display.get_width(), display.get_height()

    Surface = pygame.Surface(window_size).convert()
    Surface.fill((0, 0, 0))

    Surface.set_colorkey((0, 0, 0))
    Surface2 = pygame.Surface(window_size)

    Surface2.fill((0, 0, 0))

    r = r_perlin.generate_2D_perlin_noise(now_time/10, 0, [0, 255])
    g = g_perlin.generate_2D_perlin_noise(now_time/10, 0, [0, 255])
    b = b_perlin.generate_2D_perlin_noise(now_time/10, 0, [0, 255])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    for point in points:
        point.render()

    Surface2.set_alpha(perlin.generate_2D_perlin_noise(now_time/10, 0, [0, 100])) # 10

    display.blit(Surface2, (0, 0))

    display.blit(Surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)
    now_time = time.perf_counter()-start
