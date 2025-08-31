# type: ignore

from deps_utils import *

for component in previous_hashes:
    merge_all_subdirs(
        os.path.join(build_cache_dir, 'cmake', 'dependencies', component, 'build'),
        extern_dir)