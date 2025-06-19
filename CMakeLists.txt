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

set(EXTERN_INSTALL_DIR ${CMAKE_CURRENT_SOURCE_DIR}/pmma/extern)
file(MAKE_DIRECTORY ${EXTERN_INSTALL_DIR})

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
    "${SRC_DIR}/TextRenderer.cpp")

include(FetchContent)

# Fetch GLFW ###########################################################
FetchContent_Declare(
    glfw
    GIT_REPOSITORY https://github.com/glfw/glfw.git
    GIT_TAG 3.4
)
FetchContent_MakeAvailable(glfw)  # Just downloads, doesn't configure

# Build + install paths
set(GLFW_SOURCE_DIR ${glfw_SOURCE_DIR})
set(GLFW_BUILD_DIR ${CMAKE_BINARY_DIR}/_glfw_build)

file(MAKE_DIRECTORY ${GLFW_BUILD_DIR})

# Custom install target
add_custom_target(glfw_install
    COMMAND ${CMAKE_COMMAND}
        -DGLFW_BUILD_EXAMPLES=OFF
        -DGLFW_BUILD_TESTS=OFF
        -DGLFW_BUILD_DOCS=OFF
        -DCMAKE_INSTALL_PREFIX=${EXTERN_INSTALL_DIR}
        -DCMAKE_BUILD_TYPE=Release
        -S ${GLFW_SOURCE_DIR}
        -B ${GLFW_BUILD_DIR}
    COMMAND ${CMAKE_COMMAND} --build ${GLFW_BUILD_DIR} --config Release --target install
    COMMENT "Installing GLFW to ${EXTERN_INSTALL_DIR}"
)

# ZLib #################################################################
FetchContent_Declare(
    zlib
    GIT_REPOSITORY https://github.com/madler/zlib.git
    GIT_TAG v1.2.11  # adjust tag if needed
)
FetchContent_MakeAvailable(zlib)

file(READ "${zlib_SOURCE_DIR}/CMakeLists.txt" ZLIB_CMAKE_CONTENTS)
string(REPLACE "cmake_minimum_required(VERSION 2.8)" "cmake_minimum_required(VERSION 3.5)" ZLIB_CMAKE_CONTENTS "${ZLIB_CMAKE_CONTENTS}")
file(WRITE "${zlib_SOURCE_DIR}/CMakeLists.txt" "${ZLIB_CMAKE_CONTENTS}")

set(ZLIB_SOURCE_DIR ${zlib_SOURCE_DIR})
set(ZLIB_BUILD_DIR ${CMAKE_BINARY_DIR}/_zlib_build)
file(MAKE_DIRECTORY ${ZLIB_BUILD_DIR})

add_custom_target(zlib_install
    COMMAND ${CMAKE_COMMAND} -DCMAKE_INSTALL_PREFIX=${EXTERN_INSTALL_DIR}
                             -S ${ZLIB_SOURCE_DIR}
                             -B ${ZLIB_BUILD_DIR}
    COMMAND ${CMAKE_COMMAND} --build ${ZLIB_BUILD_DIR} --target install --config Release
    COMMENT "Installing ZLib to ${EXTERN_INSTALL_DIR}"
)

execute_process(
    COMMAND ${CMAKE_COMMAND} -DCMAKE_INSTALL_PREFIX=${EXTERN_INSTALL_DIR}
                              -DCMAKE_BUILD_TYPE=Release
                              -S ${ZLIB_SOURCE_DIR}
                              -B ${ZLIB_BUILD_DIR}
)

execute_process(
    COMMAND ${CMAKE_COMMAND} --build ${ZLIB_BUILD_DIR} --target install --config Release
)

set(ZLIB_ROOT ${EXTERN_INSTALL_DIR})
if (WIN32)
    set(ZLIB_LIBRARY "${EXTERN_INSTALL_DIR}/lib/zlibstatic.lib")

elseif(APPLE)
    set(ZLIB_LIBRARY "${EXTERN_INSTALL_DIR}/lib/libz.a")

elseif(UNIX)
    set(ZLIB_LIBRARY "${EXTERN_INSTALL_DIR}/lib/libz.a")
endif()

set(ZLIB_INCLUDE_DIR "${EXTERN_INSTALL_DIR}/include")

# libpng ###############################################################
FetchContent_Declare(
    libpng
    GIT_REPOSITORY https://github.com/glennrp/libpng.git
    GIT_TAG v1.6.37  # adjust if required
)
FetchContent_MakeAvailable(libpng)

file(READ "${libpng_SOURCE_DIR}/CMakeLists.txt" LIBPNG_CMAKE_CONTENTS)
string(REPLACE "cmake_minimum_required(VERSION 2.8)" "cmake_minimum_required(VERSION 3.5)" LIBPNG_CMAKE_CONTENTS "${LIBPNG_CMAKE_CONTENTS}")
file(WRITE "${libpng_SOURCE_DIR}/CMakeLists.txt" "${LIBPNG_CMAKE_CONTENTS}")

set(LIBPNG_SOURCE_DIR ${libpng_SOURCE_DIR})
set(LIBPNG_BUILD_DIR ${CMAKE_BINARY_DIR}/_libpng_build)
file(MAKE_DIRECTORY ${LIBPNG_BUILD_DIR})

add_custom_target(libpng_install
    COMMAND ${CMAKE_COMMAND} -DCMAKE_INSTALL_PREFIX=${EXTERN_INSTALL_DIR}
                             -S ${LIBPNG_SOURCE_DIR}
                             -B ${LIBPNG_BUILD_DIR}
    COMMAND ${CMAKE_COMMAND} --build ${LIBPNG_BUILD_DIR} --target install --config Release
    COMMENT "Installing libpng to ${EXTERN_INSTALL_DIR}"
)

# BZip2 ################################################################
FetchContent_Declare(
    bzip2
    GIT_REPOSITORY https://github.com/libarchive/bzip2.git
    GIT_TAG master  # You could choose a stable commit or tag here
)
FetchContent_MakeAvailable(bzip2)
set(BZIP2_SOURCE_DIR ${bzip2_SOURCE_DIR})
set(BZIP2_BUILD_DIR ${CMAKE_BINARY_DIR}/_bzip2_build)
file(MAKE_DIRECTORY ${BZIP2_BUILD_DIR})

add_custom_target(bzip2_install
    COMMAND ${CMAKE_COMMAND} -DCMAKE_INSTALL_PREFIX=${EXTERN_INSTALL_DIR}
                             -S ${BZIP2_SOURCE_DIR}
                             -B ${BZIP2_BUILD_DIR}
    COMMAND ${CMAKE_COMMAND} --build ${BZIP2_BUILD_DIR} --target install --config Release
    COMMENT "Installing BZip2 to ${EXTERN_INSTALL_DIR}"
)

# Brotli (Decoder) ##################################################
FetchContent_Declare(
    brotli
    GIT_REPOSITORY https://github.com/google/brotli.git
    GIT_TAG v1.1.0  # adjust tag if needed
)
FetchContent_MakeAvailable(brotli)
set(BROTLIDEC_SOURCE_DIR ${brotli_SOURCE_DIR})
set(BROTLIDEC_BUILD_DIR ${CMAKE_BINARY_DIR}/_brotlidec_build)
file(MAKE_DIRECTORY ${BROTLIDEC_BUILD_DIR})

# Note: Depending on the brotli repo structure, you might only need the decoder part.
# The following assumes a similar CMake-based build is provided.
add_custom_target(brotlidec_install
    COMMAND ${CMAKE_COMMAND} -DCMAKE_INSTALL_PREFIX=${EXTERN_INSTALL_DIR}
                             -S ${BROTLIDEC_SOURCE_DIR}
                             -B ${BROTLIDEC_BUILD_DIR}
    COMMAND ${CMAKE_COMMAND} --build ${BROTLIDEC_BUILD_DIR} --target install --config Release
    COMMENT "Installing Brotli Decoder to ${EXTERN_INSTALL_DIR}"
)

# Fetch FreeType #######################################################
set(FETCHCONTENT_UPDATES_DISCONNECTED ON)

FetchContent_Declare(
    freetype
    GIT_REPOSITORY https://gitlab.freedesktop.org/freetype/freetype.git
    GIT_TAG VER-2-13-3
)
FetchContent_MakeAvailable(freetype)

file(READ "${freetype_SOURCE_DIR}/CMakeLists.txt" FREETYPE_CMAKE_CONTENTS)
string(REPLACE "cmake_minimum_required(VERSION 2.8)" "cmake_minimum_required(VERSION 3.5)" FREETYPE_CMAKE_CONTENTS "${FREETYPE_CMAKE_CONTENTS}")
file(WRITE "${freetype_SOURCE_DIR}/CMakeLists.txt" "${FREETYPE_CMAKE_CONTENTS}")

# Build + install paths
set(FREETYPE_SOURCE_DIR ${freetype_SOURCE_DIR})
set(FREETYPE_BUILD_DIR ${CMAKE_BINARY_DIR}/_freetype_build)

file(MAKE_DIRECTORY ${FREETYPE_BUILD_DIR})

# Custom install target
add_custom_target(freetype_install
    COMMAND ${CMAKE_COMMAND}
        -DFT_DISABLE_HARFBUZZ=ON
        -DBUILD_SHARED_LIBS=OFF
        -DCMAKE_INSTALL_PREFIX=${EXTERN_INSTALL_DIR}
        -DCMAKE_PREFIX_PATH=${EXTERN_INSTALL_DIR}
        -DCMAKE_BUILD_TYPE=Release
        -S ${FREETYPE_SOURCE_DIR}
        -B ${FREETYPE_BUILD_DIR}
    COMMAND ${CMAKE_COMMAND} --build ${FREETYPE_BUILD_DIR} --config Release --target install
    COMMENT "Installing FreeType to ${EXTERN_INSTALL_DIR}"
)

########################################################################

# Add shared library
add_library(${LIB_NAME} SHARED ${SOURCES})

add_dependencies(freetype_install zlib_install libpng_install bzip2_install brotlidec_install)
add_dependencies(${LIB_NAME} glfw_install freetype_install)
add_custom_target(build_all DEPENDS glfw_install freetype_install ${LIB_NAME})

target_compile_definitions(${LIB_NAME} PRIVATE PMMA_CORE_EXPORTS)

target_include_directories(${LIB_NAME} PRIVATE ${INCLUDE_DIR} ${EXTERN_INSTALL_DIR}/include)

find_package(OpenGL REQUIRED)

# GLFW settings (platform-specific)
if (WIN32)
    add_compile_options(/O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251)
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /LTCG")
    target_link_libraries(${LIB_NAME} PRIVATE glfw OpenGL::GL freetype)

elseif(APPLE)
    add_compile_options(-O3 -ffast-math -funroll-loops -fstrict-aliasing -fomit-frame-pointer -std=c++17)
    target_link_libraries(${LIB_NAME} PRIVATE "-framework Cocoa" "-framework OpenGL" "-framework IOKit" "-framework CoreVideo" glfw freetype)

elseif(UNIX)
    add_compile_options(-O3 -ffast-math -funroll-loops -fstrict-aliasing -fomit-frame-pointer -std=c++17)
    target_link_libraries(${LIB_NAME} PRIVATE glfw OpenGL::GL freetype)
endif()

# Set output path
set_target_properties(${LIB_NAME} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    RUNTIME_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
)

message(STATUS "GLFW installed in ${GLFW_INSTALL_DIR}")
