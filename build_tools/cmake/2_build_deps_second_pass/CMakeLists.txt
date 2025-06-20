cmake_minimum_required(VERSION 3.16)
project(Stage2 LANGUAGES C)

include(FetchContent)

set(FETCHCONTENT_UPDATES_DISCONNECTED ON)

set(PNG_TESTS OFF CACHE BOOL "" FORCE)
set(PNG_SHARED OFF CACHE BOOL "" FORCE)
set(PNG_STATIC ON CACHE BOOL "" FORCE)

FetchContent_Declare(
    libpng
    GIT_REPOSITORY https://github.com/glennrp/libpng.git
    GIT_TAG v1.6.49
)
FetchContent_MakeAvailable(libpng)