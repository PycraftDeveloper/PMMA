#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __attribute__((visibility("default")))
#endif

namespace CPP_Components {
    // Export the variable (C++ linkage, mangled symbol)
    EXPORT int value = 10;
}

extern "C" EXPORT void PMMA_dummy_export() {
    // No-op export
}