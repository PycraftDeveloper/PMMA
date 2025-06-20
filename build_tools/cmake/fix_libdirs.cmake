file(GLOB LIBDIRS "${EXTERN_DIR}/lib*")

foreach(libdir ${LIBDIRS})
    if(IS_DIRECTORY "${libdir}" AND NOT "${libdir}" STREQUAL "${EXTERN_DIR}/lib")
        message(STATUS "Merging ${libdir} into ${EXTERN_DIR}/lib")
        file(COPY "${libdir}/" DESTINATION "${EXTERN_DIR}/lib")
        file(REMOVE_RECURSE "${libdir}")
    endif()
endforeach()
