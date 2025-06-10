#pragma once

#include "PMMA_Exports.hpp"

#include "Display.hpp"
#include "NumberConverter.hpp"
#include "EventsManager.hpp"

EXPORT CPP_Display* GetDisplayInstance();
EXPORT void SetDisplayInstance(CPP_Display* new_instance);

EXPORT CPP_ColorConverter* GetWindowFillColor();
EXPORT void SetWindowFillColor(CPP_ColorConverter* new_instance);

EXPORT bool Get_GLFW_Initialized();
EXPORT void Set_GLFW_Initialized(bool new_value);

EXPORT int Get_GLFW_References();
EXPORT void Set_GLFW_References(int new_value);

EXPORT int GetWindowFillColorReferences();
EXPORT void SetWindowFillColorReferences(int value);