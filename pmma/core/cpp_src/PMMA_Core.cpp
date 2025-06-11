#include "Display.hpp"
#include "PMMA_Core.hpp"

namespace PMMA {
    EXPORT CPP_Display* DisplayInstance = nullptr;
    EXPORT bool GLFW_Initialized = false;
    EXPORT int GLFW_References = 0;
}