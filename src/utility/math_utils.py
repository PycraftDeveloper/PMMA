from ctypes import c_int64

from pmma.src.registry import Registry

import numba

from pmma.src.constants import Constants

GRADIENTS2 = Constants.GRADIENTS2

@numba.njit(cache=True)
def extrapolate2(perm, xsb, ysb, dx, dy):
    index = perm[(perm[xsb & 0xFF] + ysb) & 0xFF] & 0x0E
    g1, g2 = GRADIENTS2[index : index + 2]
    return g1 * dx + g2 * dy

def overflow(x):
    return c_int64(x).value

def ranger(value, old, new):
    if old == new:
        return value
    else:
        old_range = (old[1] - old[0])
        new_range = (new[1] - new[0])
        new_value = (((value - old[0]) * new_range) / old_range) + new[0]
        return new_value