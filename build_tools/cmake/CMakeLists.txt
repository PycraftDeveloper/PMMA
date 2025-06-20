cmake_minimum_required(VERSION 3.16)
project(PMMA_Core LANGUAGES CXX)

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

include(ExternalProject)

ExternalProject_Add(stage1
  SOURCE_DIR "${CMAKE_SOURCE_DIR}/1_build_deps_first_pass" # LibZ
  CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR}
  BUILD_ALWAYS 1
)

ExternalProject_Add(stage2
  SOURCE_DIR "${CMAKE_SOURCE_DIR}/2_build_deps_second_pass" # libpng
  CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR}
  DEPENDS stage1
)

ExternalProject_Add(stage3
  SOURCE_DIR "${CMAKE_SOURCE_DIR}/3_build_extern" # GLFW, FreeType, GLM
  CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${EXTERN_DIR} -DFT_DISABLE_BZIP2=ON -DFT_DISABLE_BROTLI=ON -DGLFW_BUILD_EXAMPLES=OFF -DGLFW_BUILD_TESTS=OFF -DGLFW_BUILD_DOCS=OFF
  DEPENDS stage2
)

ExternalProject_Add(stage4
  SOURCE_DIR "${CMAKE_SOURCE_DIR}/4_build_core" # PMMA_Core
  CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${ROOT}
  DEPENDS stage3
)