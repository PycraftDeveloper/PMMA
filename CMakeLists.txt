cmake_minimum_required(VERSION 3.16)
project(PMMA_Core LANGUAGES CXX)

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

# Add shared library
add_library(
    ${LIB_NAME} SHARED ${SOURCES})
target_compile_definitions(${LIB_NAME} PRIVATE PMMA_CORE_EXPORTS)

# GLFW settings (platform-specific)
if (WIN32)
    set(GLFW_INCLUDE_DIR "D:/Visual Studio C++ Extensions/glfw-3.4.bin.WIN64/include")
    set(GLFW_LIB_DIR "D:/Visual Studio C++ Extensions/glfw-3.4.bin.WIN64/lib-vc2022")

    target_include_directories(${LIB_NAME}
        PRIVATE
            ${INCLUDE_DIR}
            ${GLFW_INCLUDE_DIR}
    )

    target_link_directories(${LIB_NAME} PRIVATE ${GLFW_LIB_DIR})
    target_link_libraries(${LIB_NAME} PRIVATE glfw3)
    target_link_libraries(${LIB_NAME} PRIVATE opengl32)
elseif(APPLE)
    target_include_directories(${LIB_NAME}
        PRIVATE ${INCLUDE_DIR}
    )

    find_package(glfw3 REQUIRED)
    target_link_libraries(${LIB_NAME} PRIVATE glfw)

    find_library(OpenGL_LIBRARY OpenGL)
    target_link_libraries(${LIB_NAME} PRIVATE glfw ${OpenGL_LIBRARY})

elseif(UNIX)
    target_include_directories(${LIB_NAME}
        PRIVATE ${INCLUDE_DIR}
    )

    find_package(glfw3 REQUIRED)
    find_package(OpenGL REQUIRED)
    target_link_libraries(${LIB_NAME} PRIVATE glfw)
    target_link_libraries(${LIB_NAME} PRIVATE glfw OpenGL::GL)
endif()

# Set output path
set_target_properties(${LIB_NAME} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    RUNTIME_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
    ARCHIVE_OUTPUT_DIRECTORY ${LIB_OUTPUT_DIR}
)
