#include "Display.hpp"
#include "NumberConverter.hpp"
#include "EventsManager.hpp"
#include "PMMA_Core.hpp"

static CPP_Display* DisplayInstance = nullptr;
static bool GLFW_Initialized = false;
static int GLFW_References = 0;
static CPP_ColorConverter* WindowFillColor = nullptr;
static int WindowFillColorReferences = 0;

namespace PMMA {
    EXPORT CPP_Display* DisplayInstance = nullptr;
    EXPORT CPP_ColorConverter* WindowFillColorInstance = nullptr;
    EXPORT bool GLFW_Initialized = false;
    EXPORT int GLFW_References = 0;
    EXPORT int WindowFillColorReferences = 0;
}