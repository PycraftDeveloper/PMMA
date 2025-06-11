#pragma once

#include "PMMA_Exports.hpp"

#include "Display.hpp"
#include "NumberConverter.hpp"

#include "InternalEvents.hpp"

namespace PMMA {
    EXPORT extern CPP_Display* DisplayInstance;

    EXPORT extern CPP_InternalSpaceKeyEvent* SpaceKeyEventInstance;

    EXPORT extern bool GLFW_Initialized;

    EXPORT extern int GLFW_References;
}

#include "AdvancedMathematics.hpp"
#include "Events.hpp"
#include "InternalEventsManager.hpp"
#include "FractalBrownianMotion.hpp"
#include "PerlinNoise.hpp"