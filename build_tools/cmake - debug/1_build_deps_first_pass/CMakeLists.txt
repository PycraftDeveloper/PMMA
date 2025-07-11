cmake_minimum_required(VERSION 3.16)
project(Stage1 LANGUAGES C)

include(FetchContent)

# Avoid building ZLib tests
set(ZLIB_ENABLE_TESTS OFF CACHE BOOL "" FORCE)
# Build static library
set(ZLIB_BUILD_SHARED ON CACHE BOOL "" FORCE)
set(ZLIB_BUILD_STATIC OFF CACHE BOOL "" FORCE)

set(FETCHCONTENT_UPDATES_DISCONNECTED ON)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Declare and fetch zlib
FetchContent_Declare(
    zlib
    GIT_REPOSITORY https://github.com/madler/zlib.git
    GIT_TAG v1.3.1
)

FetchContent_MakeAvailable(zlib)

FetchContent_Declare(
    harfbuzz
    GIT_REPOSITORY https://github.com/harfbuzz/harfbuzz.git
    GIT_TAG 11.2.1
)

FetchContent_MakeAvailable(harfbuzz)