cmake_minimum_required(VERSION 3.10...3.27)
project(Stage2 LANGUAGES C)
cmake_policy(VERSION 3.22)

include(FetchContent)

set(FETCHCONTENT_UPDATES_DISCONNECTED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

set(PNG_TESTS OFF CACHE BOOL "" FORCE)
set(PNG_SHARED ON CACHE BOOL "" FORCE)
set(PNG_STATIC OFF CACHE BOOL "" FORCE)

FetchContent_Declare(
    libpng
    GIT_REPOSITORY https://github.com/glennrp/libpng.git
    GIT_TAG v1.6.49
)
FetchContent_MakeAvailable(libpng)