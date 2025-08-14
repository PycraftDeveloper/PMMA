cmake_minimum_required(VERSION 3.16)
project(Stage1 LANGUAGES C)

include(FetchContent)

set(FETCHCONTENT_UPDATES_DISCONNECTED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# ZLIB configuration ---------------------------------------------------
set(ZLIB_ENABLE_TESTS OFF CACHE BOOL "" FORCE) # Avoid building ZLib tests
# Build static library
set(ZLIB_BUILD_SHARED ON CACHE BOOL "" FORCE)
set(ZLIB_BUILD_STATIC OFF CACHE BOOL "" FORCE)
set(ZLIB_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)

# HARFBUZZ configuration -----------------------------------------------
set(HB_HAVE_GLIB OFF CACHE BOOL "" FORCE)
set(HB_HAVE_FREETYPE OFF CACHE BOOL "" FORCE)   # FreeType will link to HarfBuzz, not the other way around
set(HB_HAVE_ICU OFF CACHE BOOL "" FORCE)
set(HB_HAVE_UNISCRIBE OFF CACHE BOOL "" FORCE)
set(HB_HAVE_DIRECTWRITE OFF CACHE BOOL "" FORCE)
set(HB_HAVE_CORETEXT OFF CACHE BOOL "" FORCE)
set(HB_BUILD_UTILS OFF CACHE BOOL "" FORCE)     # Don’t build hb-view, hb-shape, etc.
set(HB_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(HB_BUILD_DOCS OFF CACHE BOOL "" FORCE)

# Declare and fetch zlib -----------------------------------------------
FetchContent_Declare(
    zlib
    GIT_REPOSITORY https://github.com/madler/zlib.git
    GIT_TAG v1.3.1
)

FetchContent_MakeAvailable(zlib)

# Declare and fetch harfbuzz -------------------------------------------
FetchContent_Declare(
    harfbuzz
    GIT_REPOSITORY https://github.com/harfbuzz/harfbuzz.git
    GIT_TAG 11.2.1
)

FetchContent_MakeAvailable(harfbuzz)