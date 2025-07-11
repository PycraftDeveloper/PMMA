cmake_minimum_required(VERSION 3.16)
project(PMMA_Core LANGUAGES CXX)

option(BUILD_DEPS "Build PMMA_Core's dependencies" ON)

get_filename_component(DIR_ONE_ABOVE "${CMAKE_CURRENT_SOURCE_DIR}/.." ABSOLUTE)
get_filename_component(ROOT "${DIR_ONE_ABOVE}/.." ABSOLUTE)

set(EXTERN_DIR "${ROOT}/pmma/extern - DEBUG")
file(MAKE_DIRECTORY ${EXTERN_DIR})

set(EXTERN_LIBS "${EXTERN_DIR}/lib")
file(MAKE_DIRECTORY ${EXTERN_LIBS})

set(EXTERN_INCLUDE "${EXTERN_DIR}/include")
file(MAKE_DIRECTORY ${EXTERN_INCLUDE})

set(CORE_LIB "${ROOT}/pmma/lib - DEBUG")
file(MAKE_DIRECTORY ${CORE_LIB})

find_program(CCACHE_PROGRAM ccache)

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
        CMAKE_ARGS
            -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR}
            ${CMAKE_ARGS}
    )

    ExternalProject_Add(stage2
        SOURCE_DIR "${CMAKE_SOURCE_DIR}/2_build_deps_second_pass" # libpng
        CMAKE_ARGS
            -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR}
            ${CMAKE_ARGS}
        DEPENDS stage1
    )

    if (APPLE)
        set(ZLIB_LIBRARY ${EXTERN_DIR}/bin/libz.dylib)
        set(PNG_LIBRARY ${EXTERN_DIR}/bin/libpng.dylib)
    elseif (UNIX)
        set(ZLIB_LIBRARY ${EXTERN_DIR}/lib/libz.so)
        set(PNG_LIBRARY ${EXTERN_DIR}/lib/libpng.so)
    elseif (WIN32)
        set(ZLIB_LIBRARY ${EXTERN_DIR}/bin/zlibd.dll)
        set(PNG_LIBRARY ${EXTERN_DIR}/bin/libpng16d.dll)
    endif()

    ExternalProject_Add(stage3
        SOURCE_DIR "${CMAKE_SOURCE_DIR}/3_build_extern" # GLFW, FreeType, GLM
        CMAKE_ARGS
            -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR}
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
        DEPENDS stage2
    )
endif()

if (BUILD_DEPS)
    set(STAGE4_DEPENDS DEPENDS stage3)
else()
    set(STAGE4_DEPENDS "")
endif()

ExternalProject_Add(stage4
    SOURCE_DIR "${CMAKE_SOURCE_DIR}/4_build_core" # PMMA_Core
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX=${ROOT}
    ${STAGE4_DEPENDS}
    BUILD_ALWAYS 1
)