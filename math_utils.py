from ctypes import c_int64

import numba

from pmma.constants import Constants

GRADIENTS2 = Constants.GRADIENTS2

@numba.njit()
def extrapolate2(perm, xsb, ysb, dx, dy):
    index = perm[(perm[xsb & 0xFF] + ysb) & 0xFF] & 0x0E
    g1, g2 = GRADIENTS2[index : index + 2]
    return g1 * dx + g2 * dy

def overflow(x):
    return c_int64(x).value