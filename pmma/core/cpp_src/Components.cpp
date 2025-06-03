#include "Components.hpp"

#include "Display.hpp"

namespace CPP_Components {
    CPP_Display* display = nullptr;
}

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

extern "C" EXPORT void PMMA_dummy_export() {
    // No-op export
}