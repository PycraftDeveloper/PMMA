
####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was Config.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

macro(check_required_components _NAME)
  foreach(comp ${${_NAME}_FIND_COMPONENTS})
    if(NOT ${_NAME}_${comp}_FOUND)
      if(${_NAME}_FIND_REQUIRED_${comp})
        set(${_NAME}_FOUND FALSE)
      endif()
    endif()
  endforeach()
endmacro()

####################################################################################

if(OFF)
	include("${CMAKE_CURRENT_LIST_DIR}/NOT-USED")
endif()
include("${CMAKE_CURRENT_LIST_DIR}/bgfxTargets.cmake")
get_target_property(BGFX_INCLUDE_PATH bgfx::bgfx INTERFACE_INCLUDE_DIRECTORIES)
list(GET BGFX_INCLUDE_PATH 0 BGFX_INCLUDE_PATH_1) # bgfx::bgfx exports include directory twice?
set(BGFX_SHADER_INCLUDE_PATH ${BGFX_INCLUDE_PATH_1}/bgfx)

# If cross compiling, we need a host-compatible version of shaderc to compile shaders
macro(_bgfx_crosscompile_use_host_tool TOOL_NAME)
	if(NOT TARGET bgfx::${TOOL_NAME})
		find_program(
			${TOOL_NAME}_EXECUTABLE
			NAMES bgfx-${TOOL_NAME} ${TOOL_NAME}
			PATHS  /usr/bin
		)
		add_executable(bgfx::${TOOL_NAME} IMPORTED)
		set_target_properties(bgfx::${TOOL_NAME} PROPERTIES IMPORTED_LOCATION "${${TOOL_NAME}_EXECUTABLE}")
	endif()
endmacro()

_bgfx_crosscompile_use_host_tool(bin2c)
_bgfx_crosscompile_use_host_tool(texturec)
_bgfx_crosscompile_use_host_tool(shaderc)
_bgfx_crosscompile_use_host_tool(texturev)
_bgfx_crosscompile_use_host_tool(geometryv)

include("${CMAKE_CURRENT_LIST_DIR}/bgfxToolUtils.cmake")
check_required_components("bgfx")
