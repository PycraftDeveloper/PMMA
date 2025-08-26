# type: ignore

import time

from utils import *

if __name__ == "__main__":
    program_start = time.perf_counter()

    bm = DependencyBuildManager()

    bm.add_component("zlib") # why is this python file not building zlib (it should be built first)
    bm.add_component("harfbuzz")
    bm.add_component("libpng", dependencies=["zlib"])
    bm.add_component("glfw")
    bm.add_component("freetype", dependencies=["zlib", "libpng"])
    bm.add_component("bgfx")

    bm.build()

    end = time.perf_counter()
    print(f"🕒 Dependency Build took {end - program_start:.2f} seconds")

    start = time.perf_counter()

    build_pmma()

    program_end = time.perf_counter()
    print(f"🕒 PMMA Build took {program_end - start:.2f} seconds")
    print(f"🕒 Total Build took {program_end - program_start:.2f} seconds")