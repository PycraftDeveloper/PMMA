# type: ignore

from build_deps import *

ts_print("Automatically moving on to building PMMA.")

import build_pmma

# Note: Find a way of determining if geometry changing and ONLY call shape Internal Render if needed.