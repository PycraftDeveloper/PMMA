# type: ignore

from deps_utils import *
from utils import *

for component in previous_hashes:
    merge_all_subdirs(
        join_path(build_cache_dir, 'cmake', 'dependencies', component, 'build'),
        extern_dir)