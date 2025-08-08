cmake_minimum_required(VERSION 3.16)
project(PMMA_Core LANGUAGES CXX)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Core library name
set(LIB_NAME PMMA_Core)

# Source and header directories
set(SRC_DIR "${CMAKE_INSTALL_PREFIX}/pmma/core/cpp_src")
set(INCLUDE_DIR "${CMAKE_INSTALL_PREFIX}/pmma/core/hpp_src")

set(EXTERN_INSTALL_DIR ${CMAKE_INSTALL_PREFIX}/pmma/extern)

# Output directory for the library
set(LIB_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/pmma/lib")

set(Python3_EXECUTABLE "" CACHE STRING "Path to Python executable")

option(INTERNAL_USE_PYTHON "Enable Python integration" OFF)

# Collect source files
set(SOURCES
    "${SRC_DIR}/PMMA_Core.cpp"
    "${SRC_DIR}/AdvancedMathematics_BASE.cpp"
    "${SRC_DIR}/Display.cpp"
    "${SRC_DIR}/FractalBrownianMotion.cpp"
    "${SRC_DIR}/PerlinNoise_BASE.cpp"
    "${SRC_DIR}/OpenGL.cpp"
    "${SRC_DIR}/General.cpp"
    "${SRC_DIR}/NumberFormats.cpp"
    "${SRC_DIR}/InternalManagement.cpp"
    "${SRC_DIR}/Passport.cpp"
    "${SRC_DIR}/Logger.cpp"
    "${SRC_DIR}/InternalLogger.cpp"

    "${SRC_DIR}/Utility/FontUtils.cpp"
    "${SRC_DIR}/Utility/CPU_FeatureSetUtils.cpp"

    "${SRC_DIR}/Rendering/RenderPipelineCore.cpp"
    "${SRC_DIR}/Rendering/Shape2DRenderPipelineManager.cpp"
    "${SRC_DIR}/Rendering/TextRendererPipelineManager.cpp"
    "${SRC_DIR}/Rendering/TextRenderer.cpp"

    "${SRC_DIR}/Rendering/Shapes2D/RectangleShape.cpp"
    "${SRC_DIR}/Rendering/Shapes2D/RadialPolygonShape.cpp"
    "${SRC_DIR}/Rendering/Shapes2D/PixelShape.cpp"
    "${SRC_DIR}/Rendering/Shapes2D/LineShape.cpp"
    "${SRC_DIR}/Rendering/Shapes2D/ArcShape.cpp"
    "${SRC_DIR}/Rendering/Shapes2D/EllipseShape.cpp"
    "${SRC_DIR}/Rendering/Shapes2D/PolygonShape.cpp"

    "${SRC_DIR}/Events/InternalEventsManager.cpp"
    "${SRC_DIR}/Events/KeyPadEvents.cpp"
    "${SRC_DIR}/Events/KeyEvents.cpp"
    "${SRC_DIR}/Events/WindowEvents.cpp"
    "${SRC_DIR}/Events/ControllerEvents.cpp"
    "${SRC_DIR}/Events/MouseEvents.cpp"
    )

# AVX2 optimized sub-component -----------------------------------------
# Path to the files
set(AVX2_SOURCES
    "${SRC_DIR}/AdvancedMathematics_AVX2.cpp"
    "${SRC_DIR}/PerlinNoise_AVX2.cpp")

# Create an object library for myfile.cpp with AVX2 flags
add_library(AVX2_obj OBJECT ${AVX2_SOURCES})

# Apply AVX2 flags depending on the compiler
if (MSVC)
    target_compile_options(AVX2_obj PRIVATE
        /O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251 /Oi /Ob2
        /arch:AVX2)

elseif(CMAKE_CXX_COMPILER_ID MATCHES "Clang|GNU")
    target_compile_options(AVX2_obj PRIVATE
        -O3 -ffast-math -funroll-loops -fstrict-aliasing
        -fomit-frame-pointer -std=c++17 -mtune=generic
        -finline-functions -flto -ftree-vectorize -mavx2 -mfma)
endif()

# Inherit include directories and definitions
target_include_directories(AVX2_obj PRIVATE
    ${INCLUDE_DIR}
    ${EXTERN_INSTALL_DIR}/include
    ${EXTERN_INSTALL_DIR}/include/freetype2)

target_compile_definitions(AVX2_obj PRIVATE PMMA_CORE_EXPORTS)
# END OF AVX2 optimized sub-component ----------------------------------
# AVX-512 optimized sub-component --------------------------------------
# Path to the files
set(AVX512_SOURCES
    "${SRC_DIR}/AdvancedMathematics_AVX512.cpp"
    "${SRC_DIR}/PerlinNoise_AVX512.cpp")

# Create an object library for myfile.cpp with AVX2 flags
add_library(AVX512_obj OBJECT ${AVX512_SOURCES})

# Apply AVX2 flags depending on the compiler
if (MSVC)
    target_compile_options(AVX512_obj PRIVATE
        /O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251 /Oi /Ob2
        /arch:AVX512)

elseif(CMAKE_CXX_COMPILER_ID MATCHES "Clang|GNU")
    target_compile_options(AVX512_obj PRIVATE
        -O3 -ffast-math -funroll-loops -fstrict-aliasing
        -fomit-frame-pointer -std=c++17 -mtune=generic
        -finline-functions -flto -ftree-vectorize -mavx512f -mavx512dq)
endif()

# Inherit include directories and definitions
target_include_directories(AVX512_obj PRIVATE
    ${INCLUDE_DIR}
    ${EXTERN_INSTALL_DIR}/include
    ${EXTERN_INSTALL_DIR}/include/freetype2)

target_compile_definitions(AVX512_obj PRIVATE PMMA_CORE_EXPORTS)
# END OF AVX-512 optimized sub-component -------------------------------

# Add shared library including the AVX objects
add_library(${LIB_NAME} SHARED ${SOURCES} $<TARGET_OBJECTS:AVX2_obj> $<TARGET_OBJECTS:AVX512_obj>)

include(CheckIPOSupported)
check_ipo_supported(RESULT lto_supported OUTPUT lto_msg)
if(lto_supported)
    set_target_properties(${LIB_NAME} PROPERTIES
        INTERPROCEDURAL_OPTIMIZATION TRUE)
endif()

target_compile_definitions(${LIB_NAME} PRIVATE PMMA_CORE_EXPORTS)

target_include_directories(${LIB_NAME} PRIVATE
    ${INCLUDE_DIR}
    ${EXTERN_INSTALL_DIR}/include
    ${EXTERN_INSTALL_DIR}/include/freetype2)

file(GLOB LIBDIRS "${EXTERN_INSTALL_DIR}/lib*")

foreach(libdir ${LIBDIRS})
    if(IS_DIRECTORY "${libdir}")
        message(STATUS "Using link directory: ${libdir}")
        target_link_directories(${LIB_NAME} PRIVATE ${libdir})
    endif()
endforeach()

if(INTERNAL_USE_PYTHON)
    find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
    target_compile_definitions(${LIB_NAME} PRIVATE INTERNAL_USE_PYTHON)
    target_include_directories(${LIB_NAME} PRIVATE ${Python3_INCLUDE_DIRS})
    target_link_libraries(${LIB_NAME} PRIVATE ${Python3_LIBRARIES})
endif()

find_package(OpenGL REQUIRED)

if (WIN32)
    add_compile_options(
        /O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251 /Oi /Ob2)

    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /LTCG")
    target_link_libraries(${LIB_NAME} PRIVATE
        glfw3 OpenGL::GL freetype libpng16 zlib harfbuzz)

elseif(APPLE)
    add_compile_options(
        -O3 -ffast-math -funroll-loops -fstrict-aliasing
        -fomit-frame-pointer -std=c++17 -mtune=generic
        -finline-functions -flto -ftree-vectorize)

    target_link_libraries(${LIB_NAME} PRIVATE
        "-framework Cocoa" "-framework OpenGL" "-framework IOKit"
        "-framework CoreVideo" "-framework CoreFoundation" glfw3
        freetype png z harfbuzz)

    target_link_options(${LIB_NAME} PUBLIC -flto=auto)
elseif(UNIX)
    add_compile_options(
        -O3 -ffast-math -funroll-loops -fstrict-aliasing
        -fomit-frame-pointer -std=c++17 -mtune=generic
        -finline-functions -flto -ftree-vectorize)

    target_link_libraries(${LIB_NAME} PRIVATE
        glfw3 OpenGL::GL freetype png z harfbuzz)

    target_link_options(${LIB_NAME} PUBLIC -flto=auto)
endif()

# Set output path
set_target_properties(${LIB_NAME} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    RUNTIME_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
)

install(TARGETS ${LIB_NAME}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/pmma/lib
    LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/pmma/lib
    RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/pmma/lib
)

message(STATUS "PMMA_Core & Dependencies code compilation complete!")

# AVX2 MSVC ADD: /arch:AVX2
# AVX2 GCC/CLANG ADD: -mavx2 -mfma
# Note: -mfma is enabled automatically on MSVC with AVX2 flag

# AVX512 MSVC ADD: /arch:AVX512
# AVX512 GCC?CLANG ADD: -mavx512f

# NOTE, PMMA REQUIRES AVX-512 components: "-mavx512f -mavx512dq"
