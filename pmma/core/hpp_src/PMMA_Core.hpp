// libshared.h
#pragma once

#ifdef _WIN32
  #ifdef BUILDING_LIBSHARED
    #define EXPORT __declspec(dllexport)
  #else
    #define EXPORT __declspec(dllimport)
  #endif
#else
  #define EXPORT
#endif

#include "Display.hpp"

extern "C" {
    EXPORT CPP_Display* get_display_instance();
    EXPORT void set_display_instance(CPP_Display* new_instance);
}
