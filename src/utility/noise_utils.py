import math
import random

import numpy as np

from pmma.src.registry import Registry
from pmma.src.constants import Constants

import numba
from pmma.src.utility.math_utils import *

GRADIENTS2 = Constants.GRADIENTS2
STRETCH_CONSTANT2 = Constants.STRETCH_CONSTANT2
SQUISH_CONSTANT2 = Constants.SQUISH_CONSTANT2
SQUISH_CONSTANT2 = Constants.SQUISH_CONSTANT2
NORM_CONSTANT2 = Constants.NORM_CONSTANT2
GRADIENTS3 = Constants.GRADIENTS3

class PerlinNoise():
    def __init__(
            self,
            seed,
            amplitude=1,
            frequency=1,
            octaves=1,
            interpolation=Constants.COSINE,
            use_fade=False):

        self.seed = random.Random(seed).random()
        self.amplitude = amplitude
        self.frequency = frequency
        self.octaves = octaves
        self.interp = interpolation
        self.use_fade = use_fade

        self.mem_x = dict()

    def __raw_noise(self, x):
        # made for improve performance
        if x not in self.mem_x:
            self.mem_x[x] = random.Random(self.seed + x).uniform(-1, 1)
        return self.mem_x[x]

    def __raw_interpolated_noise(self, x, linear_interpolation_function, cosine_interpolation_function, cubic_interpolation_function, fade_function):
        prev_x = int(x) # previous integer
        next_x = prev_x + 1 # next integer
        frac_x = x - prev_x # fractional of x

        if self.use_fade:
            frac_x = fade_function(frac_x)

        # intepolate x
        if self.interp is Constants.LINEAR:
            res = linear_interpolation_function(
                self.__raw_noise(prev_x),
                self.__raw_noise(next_x),
                frac_x)
        elif self.interp is Constants.COSINE:
            res = cosine_interpolation_function(
                self.__raw_noise(prev_x),
                self.__raw_noise(next_x),
                frac_x)
        else:
            res = cubic_interpolation_function(
                self.__raw_noise(prev_x - 1),
                self.__raw_noise(prev_x),
                self.__raw_noise(next_x),
                self.__raw_noise(next_x + 1),
                frac_x)

        return res

    def raw_get(self, x, linear_interpolation_function, cosine_interpolation_function, cubic_interpolation_function, fade_function):
        frequency = self.frequency
        amplitude = self.amplitude
        result = 0
        for _ in range(self.octaves):
            result += self.__raw_interpolated_noise(
                x * frequency,
                linear_interpolation_function,
                cosine_interpolation_function,
                cubic_interpolation_function,
                fade_function) * amplitude
            frequency *= 2
            amplitude /= 2

        return result

@numba.njit(fastmath=True, cache=True)
def raw_generate_2D_perlin_noise(extrapolate_function, x, y, perm):
    stretch_offset = (x + y) * STRETCH_CONSTANT2

    xs = x + stretch_offset
    ys = y + stretch_offset

    xsb = math.floor(xs)
    ysb = math.floor(ys)

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
        value += attn1 * attn1 * extrapolate_function(perm, xsb + 1, ysb + 0, dx1, dy1)

    dx2 = dx0 - 0 - SQUISH_CONSTANT2
    dy2 = dy0 - 1 - SQUISH_CONSTANT2
    attn2 = 2 - dx2 * dx2 - dy2 * dy2
    if attn2 > 0:
        attn2 *= attn2
        value += attn2 * attn2 * extrapolate_function(perm, xsb + 0, ysb + 1, dx2, dy2)

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
        value += attn0 * attn0 * extrapolate_function(perm, xsb, ysb, dx0, dy0)

    attn_ext = 2 - dx_ext * dx_ext - dy_ext * dy_ext
    if attn_ext > 0:
        attn_ext *= attn_ext
        value += attn_ext * attn_ext * extrapolate_function(perm, xsv_ext, ysv_ext, dx_ext, dy_ext)

    return value / NORM_CONSTANT2

def raw_get_seed(seed):
    perm = np.zeros(256, dtype=np.int64)
    perm_grad_index3 = np.zeros(256, dtype=np.int64)
    source = np.arange(256)

    seed = raw_overflow(seed * 6364136223846793005 + 1442695040888963407)
    seed = raw_overflow(seed * 6364136223846793005 + 1442695040888963407)
    seed = raw_overflow(seed * 6364136223846793005 + 1442695040888963407)
    for i in range(255, -1, -1):
        seed = raw_overflow(seed * 6364136223846793005 + 1442695040888963407)
        r = int((seed + 31) % (i + 1))
        if r < 0:
            r += i + 1
        perm[i] = source[r]

        perm_grad_index3[i] = int((perm[i] % (len(GRADIENTS3) / 3)) * 3)
        source[r] = source[i]

    return perm