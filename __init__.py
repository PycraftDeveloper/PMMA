from os import sep

def _up(file_path: str) -> str:
    return file_path[::-1].split(sep, 1)[-1][::-1]

base_path = _up(__file__)

from . import Perlin_utils