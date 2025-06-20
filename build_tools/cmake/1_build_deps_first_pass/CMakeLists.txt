cmake_minimum_required(VERSION 3.16)
project(Stage1 LANGUAGES C)

include(FetchContent)

# Avoid building ZLib tests
set(ZLIB_ENABLE_TESTS OFF CACHE BOOL "" FORCE)
# Build static library
set(ZLIB_BUILD_SHARED OFF CACHE BOOL "" FORCE)

# Declare and fetch zlib
FetchContent_Declare(
    zlib
    GIT_REPOSITORY https://github.com/madler/zlib.git
    GIT_TAG v1.3.1
)

FetchContent_MakeAvailable(zlib)