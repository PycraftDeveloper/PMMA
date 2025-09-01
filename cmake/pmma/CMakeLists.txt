cmake_minimum_required(VERSION 3.10...3.27)
project(PMMA_Core LANGUAGES CXX)
cmake_policy(VERSION 3.22)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Core library name
set(LIB_NAME PMMA_Core)

if (NOT DEFINED WORKING_DIR)
    message(FATAL_ERROR "WORKING_DIR is not defined. Please define WORKING_DIR to specify where PMMA is located.")
endif()

# Source and header directories
set(SRC_DIR "${WORKING_DIR}/pmma/core/cpp_src")
set(INCLUDE_DIR "${WORKING_DIR}/pmma/core/hpp_src")

set(EXTERN_INSTALL_DIR ${WORKING_DIR}/pmma/extern)

# Output directory for the library
set(LIB_OUTPUT_DIR "${WORKING_DIR}/pmma/lib")

option(USE_PYTHON "Enable Python integration" OFF)

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

    "${SRC_DIR}/Animation/AnimationManager.cpp"
    "${SRC_DIR}/Animation/Types/LinearAnimation.cpp"
    "${SRC_DIR}/Animation/Types/RadialAnimation.cpp"
    )

if(NOT APPLE)
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
else()
    message(STATUS "Skipping AVX PMMA extensions for Apple build platform")
    set(AVX_FILLER_SOURCES
        "${SRC_DIR}/AVX_Filler.cpp")

    # Create an object library for myfile.cpp with AVX2 flags
    add_library(AVX_Filler_obj OBJECT ${AVX_FILLER_SOURCES})

    # Apply AVX2 flags depending on the compiler
    if (MSVC)
        target_compile_options(AVX_Filler_obj PRIVATE
            /O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251 /Oi /Ob2)

    elseif(CMAKE_CXX_COMPILER_ID MATCHES "Clang|GNU")
        target_compile_options(AVX_Filler_obj PRIVATE
            -O3 -ffast-math -funroll-loops -fstrict-aliasing
            -fomit-frame-pointer -std=c++17 -mtune=generic
            -finline-functions -flto -ftree-vectorize)
    endif()

    # Inherit include directories and definitions
    target_include_directories(AVX_Filler_obj PRIVATE
        ${INCLUDE_DIR}
        ${EXTERN_INSTALL_DIR}/include
        ${EXTERN_INSTALL_DIR}/include/freetype2)

    target_compile_definitions(AVX_Filler_obj PRIVATE PMMA_CORE_EXPORTS)

    add_library(${LIB_NAME} SHARED ${SOURCES} $<TARGET_OBJECTS:AVX_Filler_obj>)
endif()

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

if(USE_PYTHON)
    find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
    target_compile_definitions(${LIB_NAME} PRIVATE USE_PYTHON)
    target_include_directories(${LIB_NAME} PRIVATE ${Python3_INCLUDE_DIRS})
    target_link_libraries(${LIB_NAME} PRIVATE ${Python3_LIBRARIES})
endif()

find_package(OpenGL REQUIRED)

if (WIN32)
    add_compile_options(
        /O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251 /Oi /Ob2)

    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /LTCG")
    target_link_libraries(${LIB_NAME} PRIVATE
        glfw3dll OpenGL::GL freetype libpng16 zlib harfbuzz)

elseif(UNIX)
    add_compile_options(
        -O3 -ffast-math -funroll-loops -fstrict-aliasing
        -fomit-frame-pointer -std=c++17 -mtune=generic
        -finline-functions -flto -ftree-vectorize)

    target_link_libraries(${LIB_NAME} PRIVATE
        glfw OpenGL::GL freetype png z harfbuzz)

    target_link_options(${LIB_NAME} PUBLIC -flto=auto)
endif()

if(CMAKE_CONFIGURATION_TYPES) # Multi-config (MSVC, Xcode)
    foreach(OUTPUTCONFIG ${CMAKE_CONFIGURATION_TYPES})
        string(TOUPPER ${OUTPUTCONFIG} OUTPUTCONFIG_UPPER)
        set_target_properties(${LIB_NAME} PROPERTIES
            RUNTIME_OUTPUT_DIRECTORY_${OUTPUTCONFIG_UPPER} ${LIB_OUTPUT_DIR}
            LIBRARY_OUTPUT_DIRECTORY_${OUTPUTCONFIG_UPPER} ${LIB_OUTPUT_DIR}
            ARCHIVE_OUTPUT_DIRECTORY_${OUTPUTCONFIG_UPPER} ${LIB_OUTPUT_DIR}
        )
    endforeach()
else() # Single-config (Makefiles, Ninja)
    set_target_properties(${LIB_NAME} PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
        LIBRARY_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
        ARCHIVE_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    )
endif()

# AVX2 MSVC ADD: /arch:AVX2
# AVX2 GCC/CLANG ADD: -mavx2 -mfma
# Note: -mfma is enabled automatically on MSVC with AVX2 flag

# AVX512 MSVC ADD: /arch:AVX512
# AVX512 GCC?CLANG ADD: -mavx512f

# NOTE, PMMA REQUIRES AVX-512 components: "-mavx512f -mavx512dq"
