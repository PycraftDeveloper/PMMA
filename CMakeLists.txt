cmake_minimum_required(VERSION 3.16)
project(PMMA_Core LANGUAGES CXX)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Core library name
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
    "${SRC_DIR}/PerlinNoise.cpp")

include(FetchContent)

# Fetch GLFW
FetchContent_Declare(
    glfw
    GIT_REPOSITORY https://github.com/glfw/glfw.git
    GIT_TAG latest
)
FetchContent_MakeAvailable(glfw)  # Just downloads, doesn't configure

# Build + install paths
set(GLFW_SOURCE_DIR ${glfw_SOURCE_DIR})
set(GLFW_BUILD_DIR ${CMAKE_BINARY_DIR}/_glfw_build)
set(GLFW_INSTALL_DIR ${CMAKE_CURRENT_SOURCE_DIR}/pmma/extern)

file(MAKE_DIRECTORY ${GLFW_BUILD_DIR})
file(MAKE_DIRECTORY ${GLFW_INSTALL_DIR})

# Custom install target
add_custom_target(glfw_install
    COMMAND ${CMAKE_COMMAND}
        -DGLFW_BUILD_EXAMPLES=OFF
        -DGLFW_BUILD_TESTS=OFF
        -DGLFW_BUILD_DOCS=OFF
        -DCMAKE_INSTALL_PREFIX=${GLFW_INSTALL_DIR}
        -DCMAKE_BUILD_TYPE=Release
        -S ${GLFW_SOURCE_DIR}
        -B ${GLFW_BUILD_DIR}
    COMMAND ${CMAKE_COMMAND} --build ${GLFW_BUILD_DIR} --config Release --target install
    COMMENT "Installing GLFW to ${GLFW_INSTALL_DIR}"
)

# Add shared library
add_library(${LIB_NAME} SHARED ${SOURCES})

add_dependencies(${LIB_NAME} glfw_install)
add_custom_target(build_all DEPENDS glfw_install ${LIB_NAME})

target_compile_definitions(${LIB_NAME} PRIVATE PMMA_CORE_EXPORTS)

target_include_directories(${LIB_NAME} PRIVATE ${INCLUDE_DIR} ${GLFW_INSTALL_DIR}/include)

find_package(OpenGL REQUIRED)

# GLFW settings (platform-specific)
if (WIN32)
    add_compile_options(/O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251)
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /LTCG")
    target_link_libraries(${LIB_NAME} PRIVATE glfw OpenGL::GL)

elseif(APPLE)
    add_compile_options(-O3 -ffast-math -funroll-loops -fstrict-aliasing -fomit-frame-pointer -std=c++17)
    target_link_libraries(${LIB_NAME} PRIVATE "-framework Cocoa" "-framework OpenGL" "-framework IOKit" "-framework CoreVideo" glfw)

elseif(UNIX)
    add_compile_options(-O3 -ffast-math -funroll-loops -fstrict-aliasing -fomit-frame-pointer -std=c++17)
    target_link_libraries(${LIB_NAME} PRIVATE glfw OpenGL::GL)
endif()

# Set output path
set_target_properties(${LIB_NAME} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    RUNTIME_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
)

message(STATUS "GLFW installed in ${GLFW_INSTALL_DIR}")
