#pragma once

#include "PMMA_Exports.hpp"

#include "Display.hpp"
#include "NumberConverter.hpp"

namespace PMMA {
    EXPORT extern CPP_Display* DisplayInstance;
    EXPORT extern bool GLFW_Initialized;
    EXPORT extern int GLFW_References;
}