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

set(EXTERN_INSTALL_DIR "${CMAKE_INSTALL_PREFIX}/pmma/extern - DEBUG")

# Output directory for the library
set(LIB_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/pmma/lib - DEBUG")

# Collect source files
set(SOURCES
    "${SRC_DIR}/PMMA_Core.cpp"
    "${SRC_DIR}/AdvancedMathematics.cpp"
    "${SRC_DIR}/Display.cpp"
    "${SRC_DIR}/FractalBrownianMotion.cpp"
    "${SRC_DIR}/NumberConverter.cpp"
    "${SRC_DIR}/PerlinNoise.cpp"
    "${SRC_DIR}/OpenGL.cpp"
    "${SRC_DIR}/General.cpp"

    "${SRC_DIR}/Rendering/RenderPipelineCore.cpp"
    "${SRC_DIR}/Rendering/RenderPipelineManager.cpp"
    "${SRC_DIR}/Rendering/TextRenderer.cpp"

    "${SRC_DIR}/Rendering/Shapes2D/RectangleShape.cpp"
    "${SRC_DIR}/Rendering/Shapes2D/RadialPolygonShape.cpp"

    "${SRC_DIR}/Events/InternalEventsManager.cpp"
    "${SRC_DIR}/Events/KeyPadEvents.cpp"
    "${SRC_DIR}/Events/KeyEvents.cpp"
    "${SRC_DIR}/Events/WindowEvents.cpp"
    "${SRC_DIR}/Events/ControllerEvents.cpp"
    "${SRC_DIR}/Events/MouseEvents.cpp"
    )

# Add shared library
add_library(${LIB_NAME} SHARED ${SOURCES})

include(CheckIPOSupported)
check_ipo_supported(RESULT lto_supported OUTPUT lto_msg)
if(lto_supported)
    set_target_properties(${LIB_NAME} PROPERTIES INTERPROCEDURAL_OPTIMIZATION TRUE)
endif()

target_compile_definitions(${LIB_NAME} PRIVATE PMMA_CORE_EXPORTS)

target_include_directories(${LIB_NAME} PRIVATE ${INCLUDE_DIR} ${EXTERN_INSTALL_DIR}/include ${EXTERN_INSTALL_DIR}/include/freetype2)

file(GLOB LIBDIRS "${EXTERN_INSTALL_DIR}/lib*")

foreach(libdir ${LIBDIRS})
    if(IS_DIRECTORY "${libdir}")
        message(STATUS "Using link directory: ${libdir}")
        target_link_directories(${LIB_NAME} PRIVATE ${libdir})
    endif()
endforeach()

find_package(OpenGL REQUIRED)

if (WIN32)
    add_compile_options(/O2 /fp:fast /GL /GF /GS- /std:c++17 /wd4551 /wd4251 /Oi /0b2)
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /LTCG")
    target_link_libraries(${LIB_NAME} PRIVATE glfw3 OpenGL::GL freetyped libpng16d zlibd harfbuzz)

elseif(APPLE)
    add_compile_options(-O3 -ffast-math -funroll-loops -fstrict-aliasing -fomit-frame-pointer -std=c++17 -mtune=generic -finline-functions -flto -ftree-vectorize)
    target_link_libraries(${LIB_NAME} PRIVATE "-framework Cocoa" "-framework OpenGL" "-framework IOKit" "-framework CoreVideo" glfw3 freetype png z harfbuzz)

elseif(UNIX)
    add_compile_options(-O3 -ffast-math -funroll-loops -fstrict-aliasing -fomit-frame-pointer -std=c++17 -mtune=generic -finline-functions -flto -ftree-vectorize)
    target_link_libraries(${LIB_NAME} PRIVATE glfw3 OpenGL::GL freetype png z harfbuzz)
endif()

# Set output path
set_target_properties(${LIB_NAME} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    RUNTIME_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
)

install(TARGETS ${LIB_NAME}
    ARCHIVE DESTINATION "${CMAKE_INSTALL_PREFIX}/pmma/lib - DEBUG"
    LIBRARY DESTINATION "${CMAKE_INSTALL_PREFIX}/pmma/lib - DEBUG"
    RUNTIME DESTINATION "${CMAKE_INSTALL_PREFIX}/pmma/lib - DEBUG"
)

message(STATUS "PMMA_Core & Dependencies code compilation complete!")

# AVX2 MSVC ADD: /arch:AVX2
# AVX2 GCC/CLANG ADD: -mavx2 -mfma
# Note: -mfma is enabled automatically on MSVC with AVX2 flag

# AVX512 MSVC ADD: /arch:AVX512
# AVX512 GCC?CLANG ADD: -mavx512f