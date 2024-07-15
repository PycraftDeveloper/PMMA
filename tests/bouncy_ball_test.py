import random

import pmma

import time

import pygame

pmma.init()

display = pmma.Display()
display.create(1280, 720)

events = pmma.Events()

compute_pipeline = pmma.ComputePipeline(num_threads=1)

registry = pmma.Registry()

math = pmma.Math()

### temp ###

from math import floor
from ctypes import c_int64

import numpy as np
import numba

GRADIENTS2 = np.array([
    5, 2, 2, 5,
    -5, 2, -2, 5,
    5, -2, 2, -5,
    -5, -2, -2, -5,
], dtype=np.int64)

GRADIENTS3 = np.array([
    -11, 4, 4, -4, 11, 4, -4, 4, 11,
    11, 4, 4, 4, 11, 4, 4, 4, 11,
    -11, -4, 4, -4, -11, 4, -4, -4, 11,
    11, -4, 4, 4, -11, 4, 4, -4, 11,
    -11, 4, -4, -4, 11, -4, -4, 4, -11,
    11, 4, -4, 4, 11, -4, 4, 4, -11,
    -11, -4, -4, -4, -11, -4, -4, -4, -11,
    11, -4, -4, 4, -11, -4, 4, -4, -11,
], dtype=np.int64)

GRADIENTS4 = np.array([
    3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3,
    -3, 1, 1, 1, -1, 3, 1, 1, -1, 1, 3, 1, -1, 1, 1, 3,
    3, -1, 1, 1, 1, -3, 1, 1, 1, -1, 3, 1, 1, -1, 1, 3,
    -3, -1, 1, 1, -1, -3, 1, 1, -1, -1, 3, 1, -1, -1, 1, 3,
    3, 1, -1, 1, 1, 3, -1, 1, 1, 1, -3, 1, 1, 1, -1, 3,
    -3, 1, -1, 1, -1, 3, -1, 1, -1, 1, -3, 1, -1, 1, -1, 3,
    3, -1, -1, 1, 1, -3, -1, 1, 1, -1, -3, 1, 1, -1, -1, 3,
    -3, -1, -1, 1, -1, -3, -1, 1, -1, -1, -3, 1, -1, -1, -1, 3,
    3, 1, 1, -1, 1, 3, 1, -1, 1, 1, 3, -1, 1, 1, 1, -3,
    -3, 1, 1, -1, -1, 3, 1, -1, -1, 1, 3, -1, -1, 1, 1, -3,
    3, -1, 1, -1, 1, -3, 1, -1, 1, -1, 3, -1, 1, -1, 1, -3,
    -3, -1, 1, -1, -1, -3, 1, -1, -1, -1, 3, -1, -1, -1, 1, -3,
    3, 1, -1, -1, 1, 3, -1, -1, 1, 1, -3, -1, 1, 1, -1, -3,
    -3, 1, -1, -1, -1, 3, -1, -1, -1, 1, -3, -1, -1, 1, -1, -3,
    3, -1, -1, -1, 1, -3, -1, -1, 1, -1, -3, -1, 1, -1, -1, -3,
    -3, -1, -1, -1, -1, -3, -1, -1, -1, -1, -3, -1, -1, -1, -1, -3,
], dtype=np.int64)

STRETCH_CONSTANT2 = -0.211324865405187
SQUISH_CONSTANT2 = 0.366025403784439
STRETCH_CONSTANT3 = -1.0 / 6
SQUISH_CONSTANT3 = 1.0 / 3
STRETCH_CONSTANT4 = -0.138196601125011
SQUISH_CONSTANT4 = 0.309016994374947

NORM_CONSTANT2 = 47
NORM_CONSTANT3 = 103
NORM_CONSTANT4 = 30

@numba.njit()
def extrapolate2(perm, xsb, ysb, dx, dy):
    index = perm[(perm[xsb & 0xFF] + ysb) & 0xFF] & 0x0E
    g1, g2 = GRADIENTS2[index : index + 2]
    return g1 * dx + g2 * dy

@numba.njit()
def generatekey(x, y, perm):
    stretch_offset = (x + y) * STRETCH_CONSTANT2

    xs = x + stretch_offset
    ys = y + stretch_offset

    xsb = floor(xs)
    ysb = floor(ys)

    squish_offset = (xsb + ysb) * SQUISH_CONSTANT2
    xb = xsb + squish_offset
    yb = ysb + squish_offset

    xins = xs - xsb
    yins = ys - ysb

    in_sum = xins + yins

    dx0 = x - xb
    dy0 = y - yb

    value = 0

    dx1 = dx0 - 1 - SQUISH_CONSTANT2
    dy1 = dy0 - 0 - SQUISH_CONSTANT2
    attn1 = 2 - dx1 * dx1 - dy1 * dy1
    if attn1 > 0:
        attn1 *= attn1
        value += attn1 * attn1 * extrapolate2(perm, xsb + 1, ysb + 0, dx1, dy1)

    dx2 = dx0 - 0 - SQUISH_CONSTANT2
    dy2 = dy0 - 1 - SQUISH_CONSTANT2
    attn2 = 2 - dx2 * dx2 - dy2 * dy2
    if attn2 > 0:
        attn2 *= attn2
        value += attn2 * attn2 * extrapolate2(perm, xsb + 0, ysb + 1, dx2, dy2)

    if in_sum <= 1:
        zins = 1 - in_sum
        if zins > xins or zins > yins:
            if xins > yins:
                xsv_ext = xsb + 1
                ysv_ext = ysb - 1
                dx_ext = dx0 - 1
                dy_ext = dy0 + 1
            else:
                xsv_ext = xsb - 1
                ysv_ext = ysb + 1
                dx_ext = dx0 + 1
                dy_ext = dy0 - 1
        else:
            xsv_ext = xsb + 1
            ysv_ext = ysb + 1
            dx_ext = dx0 - 1 - 2 * SQUISH_CONSTANT2
            dy_ext = dy0 - 1 - 2 * SQUISH_CONSTANT2
    else:
        zins = 2 - in_sum
        if zins < xins or zins < yins:
            if xins > yins:
                xsv_ext = xsb + 2
                ysv_ext = ysb + 0
                dx_ext = dx0 - 2 - 2 * SQUISH_CONSTANT2
                dy_ext = dy0 + 0 - 2 * SQUISH_CONSTANT2
            else:
                xsv_ext = xsb + 0
                ysv_ext = ysb + 2
                dx_ext = dx0 + 0 - 2 * SQUISH_CONSTANT2
                dy_ext = dy0 - 2 - 2 * SQUISH_CONSTANT2
        else:
            dx_ext = dx0
            dy_ext = dy0
            xsv_ext = xsb
            ysv_ext = ysb
        xsb += 1
        ysb += 1
        dx0 = dx0 - 1 - 2 * SQUISH_CONSTANT2
        dy0 = dy0 - 1 - 2 * SQUISH_CONSTANT2

    attn0 = 2 - dx0 * dx0 - dy0 * dy0
    if attn0 > 0:
        attn0 *= attn0
        value += attn0 * attn0 * extrapolate2(perm, xsb, ysb, dx0, dy0)

    attn_ext = 2 - dx_ext * dx_ext - dy_ext * dy_ext
    if attn_ext > 0:
        attn_ext *= attn_ext
        value += attn_ext * attn_ext * extrapolate2(perm, xsv_ext, ysv_ext, dx_ext, dy_ext)

    return value / NORM_CONSTANT2

def overflow(x):
    return c_int64(x).value

def getseed(seed):
    perm = np.zeros(256, dtype=np.int64)
    perm_grad_index3 = np.zeros(256, dtype=np.int64)
    source = np.arange(256)

    seed = overflow(seed * 6364136223846793005 + 1442695040888963407)
    seed = overflow(seed * 6364136223846793005 + 1442695040888963407)
    seed = overflow(seed * 6364136223846793005 + 1442695040888963407)
    for i in range(255, -1, -1):
        seed = overflow(seed * 6364136223846793005 + 1442695040888963407)
        r = int((seed + 31) % (i + 1))
        if r < 0:
            r += i + 1
        perm[i] = source[r]

        perm_grad_index3[i] = int((perm[i] % (len(GRADIENTS3) / 3)) * 3)
        source[r] = source[i]

    return perm

### temp ###

class Ball:
    def __init__(self):
        self.x = random.randint(0, display.get_width())
        self.y = random.randint(0, display.get_height())
        self.dir_x = (random.random()*2)-1
        self.dir_y = (random.random()*2)-1
        self.seed = getseed(random.randint(0, 1000000))
        self.mass = (1+generatekey(0, 0, self.seed))*10
        self.mag_x = random.random()*5
        self.mag_y = random.random()*5
        self.last_collision_time = time.perf_counter()
        self.color = [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)]
        self.ball_arr = None
        self.now_time = None

    def compute(self):
        self.mass = (1+generatekey(self.now_time/100, 0, self.seed))*10
        self.x += self.dir_x * self.mag_x
        self.y += self.dir_y * self.mag_y

        if self.x > display.get_width()-self.mass:
            self.x = display.get_width()-self.mass
            self.dir_x *= -1
            pygame.draw.circle(Surface, [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)], (self.x, self.y), self.mass*2, width=1)
        elif self.x < self.mass:
            self.x = self.mass
            self.dir_x *= -1
            pygame.draw.circle(Surface, [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)], (self.x, self.y), self.mass*2, width=1)

        if self.y > display.get_height()-self.mass:
            self.y = display.get_height()-self.mass
            self.dir_y *= -1
            pygame.draw.circle(Surface, [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)], (self.x, self.y), self.mass*2, width=1)
        elif self.y < self.mass:
            self.y = self.mass
            self.dir_y *= -1
            pygame.draw.circle(Surface, [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)], (self.x, self.y), self.mass*2, width=1)

        if time.perf_counter()-self.last_collision_time > 1/15:
            for ball in self.ball_arr:
                if ball is self:
                    continue
                if abs(self.x-ball.x) < self.mass+ball.mass and abs(self.y-ball.y) < self.mass+ball.mass:
                    #self.x += (self.x-ball.x)/2
                    #self.y += (self.y-ball.y)/2
                    self.dir_x *= -1
                    self.dir_y *= -1
                    ball.dir_x *= -1
                    ball.dir_y *= -1
                    self.last_collision_time = time.perf_counter()
                    ball.last_collision_time = time.perf_counter()
                    self.color = [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)]
                    ball.color = [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)]
                    pygame.draw.circle(Surface, [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)], (self.x, self.y), self.mass*2, width=1)
                    pygame.draw.circle(Surface, [random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)], (ball.x, ball.y), ball.mass*2, width=1)


    def render(self):
        pygame.draw.circle(Surface, self.color, (self.x, self.y), self.mass)

balls = []
n_balls = 5000
for i in range(n_balls):
    ba = Ball()
    compute_pipeline.add_compute_function(ba.compute, parallel=True)
    balls.append(ba)

for ball in balls:
    ball.ball_arr = balls

start = time.perf_counter()
now_time = 0
a = []
while registry.running:
    display.set_caption(str(display.get_fps()))
    window_x, window_y = display.get_size()
    window_size = (window_x, window_y)

    Surface = pygame.Surface(window_size).convert()
    Surface.fill((0, 0, 0))

    Surface.set_colorkey((0, 0, 0))
    Surface2 = pygame.Surface(window_size)

    Surface2.fill((0, 0, 0))

    events.handle()

    for ball in balls:
        ball.now_time = now_time

    dx = time.perf_counter()
    compute_pipeline.execute()
    dy = time.perf_counter()

    a.append(1/(dy-dx))

    print(sum(a)/len(a))
    print(1/(sum(a)/len(a)))

    for ball in balls:
        ball.render()

    Surface2.set_alpha(5) # 10

    display.blit(Surface2, (0, 0))

    display.blit(Surface, (0, 0))

    display.refresh()

    now_time = time.perf_counter() - start