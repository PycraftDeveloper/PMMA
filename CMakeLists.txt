cmake_minimum_required(VERSION 3.16)
project(PMMA_Core LANGUAGES CXX)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(LIB_NAME PMMA_Core)

# Source and header directories
set(SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}/pmma/core/cpp_src")
set(INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/pmma/core/hpp_src")

# Output directory for the library
set(LIB_OUTPUT_DIR "${CMAKE_CURRENT_SOURCE_DIR}/pmma/lib")
file(MAKE_DIRECTORY ${LIB_OUTPUT_DIR})

# Collect source files
set(SOURCES
    "${SRC_DIR}/PMMA_Core.cpp"
    "${SRC_DIR}/AdvancedMathematics.cpp"
    "${SRC_DIR}/Display.cpp"
    "${SRC_DIR}/Events.cpp"
    "${SRC_DIR}/FractalBrownianMotion.cpp"
    "${SRC_DIR}/InternalEventsManager.cpp"
    "${SRC_DIR}/NumberConverter.cpp"
    "${SRC_DIR}/PerlinNoise.cpp"
)

# Add shared library
add_library(${LIB_NAME} SHARED ${SOURCES})
target_compile_definitions(${LIB_NAME} PRIVATE PMMA_CORE_EXPORTS)

# Set include directories
target_include_directories(${LIB_NAME} PRIVATE ${INCLUDE_DIR})

# --- Fetch GLFW from GitHub ---
include(FetchContent)

set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_DOCS OFF CACHE BOOL "" FORCE)
set(GLFW_INSTALL OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_SHARED_LIBS OFF CACHE BOOL "" FORCE)

FetchContent_Declare(
  glfw
  GIT_REPOSITORY https://github.com/glfw/glfw.git
  GIT_TAG latest
)

FetchContent_MakeAvailable(glfw)

# Find OpenGL (still system-provided)
find_package(OpenGL REQUIRED)

# Platform-specific flags and linking
if (WIN32)
    add_compile_options(/O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251)
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /LTCG")

    target_link_libraries(${LIB_NAME}
        PRIVATE
            glfw
            OpenGL::GL
    )

elseif(APPLE)
    add_compile_options(-O3 -ffast-math -funroll-loops -fstrict-aliasing -fomit-frame-pointer -std=c++17)

    target_link_libraries(${LIB_NAME}
        PRIVATE
            glfw
            "-framework Cocoa"
            "-framework OpenGL"
            "-framework IOKit"
            "-framework CoreVideo"
    )

elseif(UNIX)
    add_compile_options(-O3 -ffast-math -funroll-loops -fstrict-aliasing -fomit-frame-pointer -std=c++17)

    target_link_libraries(${LIB_NAME}
        PRIVATE
            glfw
            OpenGL::GL
    )
endif()

# Set output path
set_target_properties(${LIB_NAME} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    RUNTIME_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
)
