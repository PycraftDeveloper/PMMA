#pragma once

#include "PMMA_Exports.hpp"

#include "Display.hpp"
#include "NumberConverter.hpp"
#include "EventsManager.hpp"

namespace PMMA {
    EXPORT extern CPP_Display* DisplayInstance;
    EXPORT extern CPP_ColorConverter* WindowFillColorInstance;
    EXPORT extern bool GLFW_Initialized;
    EXPORT extern int GLFW_References;
    EXPORT extern int WindowFillColorReferences;
}