cmake_minimum_required(VERSION 3.10...3.27)
project(PMMA_Core LANGUAGES CXX)
cmake_policy(VERSION 3.27)

option(BUILD_DEPS "Build PMMA_Core's dependencies" ON)
option(USE_PYTHON "Enable Python integration" OFF)
option(USE_NINJA "Enable Ninja for faster code compilation" ON)

set(PYTHON_PATH "" CACHE STRING "Path to Python executable")

# If PYTHON_PATH is not set or doesn't exist, try to find Python automatically
if(PYTHON_PATH STREQUAL "" OR NOT EXISTS ${PYTHON_PATH})
    message(STATUS "PYTHON_PATH not provided or invalid. Attempting to find Python automatically...")

    # Try to find Python using modern CMake (>= 3.12)
    find_package(Python3 COMPONENTS Interpreter REQUIRED)
    set(PYTHON_PATH ${Python3_EXECUTABLE})
else()
    message(STATUS "Using provided Python path: ${PYTHON_PATH}")
endif()

# Final confirmation
message(STATUS "Final Python path: ${PYTHON_PATH}")

get_filename_component(DIR_ONE_ABOVE "${CMAKE_CURRENT_SOURCE_DIR}/.." ABSOLUTE)
get_filename_component(ROOT "${DIR_ONE_ABOVE}/.." ABSOLUTE)

set(EXTERN_DIR "${ROOT}/pmma/extern")
file(MAKE_DIRECTORY ${EXTERN_DIR})

set(EXTERN_LIBS "${EXTERN_DIR}/lib")
file(MAKE_DIRECTORY ${EXTERN_LIBS})

set(EXTERN_INCLUDE "${EXTERN_DIR}/include")
file(MAKE_DIRECTORY ${EXTERN_INCLUDE})

set(CORE_LIB "${ROOT}/pmma/lib")
file(MAKE_DIRECTORY ${CORE_LIB})

find_program(CCACHE_PROGRAM ccache)

include(ProcessorCount)
ProcessorCount(NPROC)
if(NOT DEFINED PARALLEL_CORES)
    set(PARALLEL_CORES ${NPROC})
endif()

if(CCACHE_PROGRAM)
    message(STATUS "Using ccache for compilation")
    list(APPEND CMAKE_ARGS
        -DCMAKE_C_COMPILER=${CCACHE_PROGRAM}
        -DCMAKE_C_COMPILER_ARG1=gcc
        -DCMAKE_CXX_COMPILER=${CCACHE_PROGRAM}
        -DCMAKE_CXX_COMPILER_ARG1=g++
    )
endif()

include(ExternalProject)

if (BUILD_DEPS)
    ExternalProject_Add(stage1
        SOURCE_DIR "${CMAKE_SOURCE_DIR}/1_build_deps_first_pass" # LibZ
        CMAKE_GENERATOR Ninja
        CMAKE_ARGS
            -DCMAKE_BUILD_TYPE=Release
            -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR}
            -DCMAKE_BUILD_PARALLEL_LEVEL=${PARALLEL_CORES}
            ${CMAKE_ARGS}
        BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR> --config Release --parallel ${PARALLEL_CORES}
        INSTALL_COMMAND ${CMAKE_COMMAND} --install <BINARY_DIR> --config Release
    )

    ExternalProject_Add(stage2
        SOURCE_DIR "${CMAKE_SOURCE_DIR}/2_build_deps_second_pass" # libpng
        CMAKE_GENERATOR Ninja
        CMAKE_ARGS
            -DCMAKE_BUILD_TYPE=Release
            -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR}
            -DCMAKE_BUILD_PARALLEL_LEVEL=${PARALLEL_CORES}
            ${CMAKE_ARGS}
        BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR> --config Release --parallel ${PARALLEL_CORES}
        INSTALL_COMMAND ${CMAKE_COMMAND} --install <BINARY_DIR> --config Release
        DEPENDS stage1
    )

    if (APPLE)
        set(ZLIB_LIBRARY ${EXTERN_DIR}/bin/libz.dylib)
        set(PNG_LIBRARY ${EXTERN_DIR}/bin/libpng.dylib)
    elseif (UNIX)
        set(ZLIB_LIBRARY ${EXTERN_DIR}/lib/libz.so)
        set(PNG_LIBRARY ${EXTERN_DIR}/lib/libpng.so)
    elseif (WIN32)
        set(ZLIB_LIBRARY ${EXTERN_DIR}/bin/zlib.dll)
        set(PNG_LIBRARY ${EXTERN_DIR}/bin/libpng16.dll)
    endif()

    ExternalProject_Add(stage3
        SOURCE_DIR "${CMAKE_SOURCE_DIR}/3_build_extern" # GLFW, FreeType, GLM
        CMAKE_GENERATOR Ninja
        CMAKE_ARGS
            -DCMAKE_BUILD_TYPE=Release
            -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR}
            -DCMAKE_BUILD_PARALLEL_LEVEL=${PARALLEL_CORES}
            -DFT_DISABLE_BZIP2=ON
            -DFT_DISABLE_BROTLI=ON
            -DGLFW_BUILD_EXAMPLES=OFF
            -DGLFW_BUILD_TESTS=OFF
            -DGLFW_BUILD_DOCS=OFF
            -DZLIB_LIBRARY=${ZLIB_LIBRARY}
            -DZLIB_INCLUDE_DIR=${EXTERN_DIR}/include
            -DPNG_LIBRARY=${PNG_LIBRARY}
            -DPNG_INCLUDE_DIR=${EXTERN_DIR}/include
            ${CMAKE_ARGS}
        BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR> --config Release --parallel ${PARALLEL_CORES}
        INSTALL_COMMAND ${CMAKE_COMMAND} --install <BINARY_DIR> --config Release
        DEPENDS stage2
    )
endif()

if (BUILD_DEPS)
    set(STAGE4_DEPENDS DEPENDS stage3)
else()
    set(STAGE4_DEPENDS "")
endif()

if (USE_NINJA)
    ExternalProject_Add(stage4
        SOURCE_DIR "${CMAKE_SOURCE_DIR}/4_build_core" # PMMA_Core
        CMAKE_GENERATOR Ninja
        CMAKE_ARGS
            -DINTERNAL_USE_PYTHON=${USE_PYTHON}
            -DPython3_EXECUTABLE=${PYTHON_PATH}
            -DCMAKE_BUILD_TYPE=Release
            -DCMAKE_INSTALL_PREFIX=${ROOT}
            -DCMAKE_BUILD_PARALLEL_LEVEL=${PARALLEL_CORES}
        BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR> --config Release --parallel ${PARALLEL_CORES}
        INSTALL_COMMAND ${CMAKE_COMMAND} --install <BINARY_DIR> --config Release
        ${STAGE4_DEPENDS}
        BUILD_ALWAYS 1
    )
else()
    ExternalProject_Add(stage4
        SOURCE_DIR "${CMAKE_SOURCE_DIR}/4_build_core" # PMMA_Core
        CMAKE_ARGS
            -DINTERNAL_USE_PYTHON=${USE_PYTHON}
            -DPython3_EXECUTABLE=${PYTHON_PATH}
            -DCMAKE_BUILD_TYPE=Release
            -DCMAKE_INSTALL_PREFIX=${ROOT}
            -DCMAKE_BUILD_PARALLEL_LEVEL=${PARALLEL_CORES}
        BUILD_COMMAND ${CMAKE_COMMAND} --build <BINARY_DIR> --config Release --parallel ${PARALLEL_CORES}
        INSTALL_COMMAND ${CMAKE_COMMAND} --install <BINARY_DIR> --config Release
        ${STAGE4_DEPENDS}
        BUILD_ALWAYS 1
    )
endif()