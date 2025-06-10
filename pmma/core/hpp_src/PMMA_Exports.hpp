// PMMA_Export.hpp
#pragma once

#ifdef _WIN32
  #ifdef PMMA_CORE_EXPORTS
    #define EXPORT __declspec(dllexport)
  #else
    #define EXPORT __declspec(dllimport)
  #endif
#else
  #define EXPORT
#endif
