# type: ignore

from build_deps import *

ts_print("Automatically moving on to building PMMA.")

import build_pmma

# Note: Same issue as before, shapes can be added but are never removed. If shape breaks Shape2D cache, it MUST invalidate cache.