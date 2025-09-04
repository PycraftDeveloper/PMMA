#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "bgfx::bx" for configuration "Release"
set_property(TARGET bgfx::bx APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::bx PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libbx.a"
  )

list(APPEND _cmake_import_check_targets bgfx::bx )
list(APPEND _cmake_import_check_files_for_bgfx::bx "${_IMPORT_PREFIX}/lib64/libbx.a" )

# Import target "bgfx::bin2c" for configuration "Release"
set_property(TARGET bgfx::bin2c APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::bin2c PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/bin2c"
  )

list(APPEND _cmake_import_check_targets bgfx::bin2c )
list(APPEND _cmake_import_check_files_for_bgfx::bin2c "${_IMPORT_PREFIX}/bin/bin2c" )

# Import target "bgfx::bimg" for configuration "Release"
set_property(TARGET bgfx::bimg APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::bimg PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C;CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libbimg.a"
  )

list(APPEND _cmake_import_check_targets bgfx::bimg )
list(APPEND _cmake_import_check_files_for_bgfx::bimg "${_IMPORT_PREFIX}/lib64/libbimg.a" )

# Import target "bgfx::bimg_decode" for configuration "Release"
set_property(TARGET bgfx::bimg_decode APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::bimg_decode PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C;CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libbimg_decode.a"
  )

list(APPEND _cmake_import_check_targets bgfx::bimg_decode )
list(APPEND _cmake_import_check_files_for_bgfx::bimg_decode "${_IMPORT_PREFIX}/lib64/libbimg_decode.a" )

# Import target "bgfx::bimg_encode" for configuration "Release"
set_property(TARGET bgfx::bimg_encode APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::bimg_encode PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C;CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libbimg_encode.a"
  )

list(APPEND _cmake_import_check_targets bgfx::bimg_encode )
list(APPEND _cmake_import_check_files_for_bgfx::bimg_encode "${_IMPORT_PREFIX}/lib64/libbimg_encode.a" )

# Import target "bgfx::texturec" for configuration "Release"
set_property(TARGET bgfx::texturec APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::texturec PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/texturec"
  )

list(APPEND _cmake_import_check_targets bgfx::texturec )
list(APPEND _cmake_import_check_files_for_bgfx::texturec "${_IMPORT_PREFIX}/bin/texturec" )

# Import target "bgfx::bgfx" for configuration "Release"
set_property(TARGET bgfx::bgfx APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::bgfx PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libbgfx.a"
  )

list(APPEND _cmake_import_check_targets bgfx::bgfx )
list(APPEND _cmake_import_check_files_for_bgfx::bgfx "${_IMPORT_PREFIX}/lib64/libbgfx.a" )

# Import target "bgfx::texturev" for configuration "Release"
set_property(TARGET bgfx::texturev APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::texturev PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/texturev"
  )

list(APPEND _cmake_import_check_targets bgfx::texturev )
list(APPEND _cmake_import_check_files_for_bgfx::texturev "${_IMPORT_PREFIX}/bin/texturev" )

# Import target "bgfx::geometryc" for configuration "Release"
set_property(TARGET bgfx::geometryc APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::geometryc PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/geometryc"
  )

list(APPEND _cmake_import_check_targets bgfx::geometryc )
list(APPEND _cmake_import_check_files_for_bgfx::geometryc "${_IMPORT_PREFIX}/bin/geometryc" )

# Import target "bgfx::geometryv" for configuration "Release"
set_property(TARGET bgfx::geometryv APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::geometryv PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/geometryv"
  )

list(APPEND _cmake_import_check_targets bgfx::geometryv )
list(APPEND _cmake_import_check_files_for_bgfx::geometryv "${_IMPORT_PREFIX}/bin/geometryv" )

# Import target "bgfx::shaderc" for configuration "Release"
set_property(TARGET bgfx::shaderc APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(bgfx::shaderc PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/shaderc"
  )

list(APPEND _cmake_import_check_targets bgfx::shaderc )
list(APPEND _cmake_import_check_files_for_bgfx::shaderc "${_IMPORT_PREFIX}/bin/shaderc" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
