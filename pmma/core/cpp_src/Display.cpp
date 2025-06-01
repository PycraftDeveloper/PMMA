#include <iostream>

#include <GLFW/glfw3.h>

#include "Display.hpp"

#include "Registry.hpp"

using namespace std;

namespace CPP_StaticDisplay {
    unsigned int Size[2] = {0, 0};
    char* Caption;
    bool DisplayCreated = false;
    GLFWwindow* Window = nullptr;
    CPP_Display* Display_Context = nullptr;
}

CPP_Display::CPP_Display() {
    if (CPP_StaticDisplay::Display_Context != nullptr) {
        CPP_StaticDisplay::Display_Context->~CPP_Display();
    }
    CPP_StaticDisplay::Display_Context = this;
}

void CPP_Display::Create(unsigned int* Size, char* Caption) {
    if (!CPP_Registry::Is_GLFW_Initialized) {
        glfwInit();
        CPP_Registry::Is_GLFW_Initialized = true;
    }
    CPP_Registry::GLFW_References++;

    CPP_StaticDisplay::Window = glfwCreateWindow(Size[0], Size[1], Caption, NULL, NULL);

    CPP_StaticDisplay::Size[0] = Size[0];
    CPP_StaticDisplay::Size[1] = Size[1];
    CPP_StaticDisplay::Caption = Caption;
    CPP_StaticDisplay::DisplayCreated = true;

    glfwMakeContextCurrent(CPP_StaticDisplay::Window);
}

unsigned int CPP_Display::GetWidth() {
    if (!CPP_StaticDisplay::DisplayCreated) {
        throw runtime_error("Display not created yet!");
    }
    return CPP_StaticDisplay::Size[0];
}

unsigned int CPP_Display::GetHeight() {
    if (!CPP_StaticDisplay::DisplayCreated) {
        throw runtime_error("Display not created yet!");
    }
    return CPP_StaticDisplay::Size[1];
}

CPP_Display::~CPP_Display() {
    CPP_StaticDisplay::Window = nullptr;
    CPP_StaticDisplay::DisplayCreated = false;
    CPP_StaticDisplay::Size[0] = 0;
    CPP_StaticDisplay::Size[1] = 0;
    CPP_StaticDisplay::Caption = nullptr;

    CPP_Registry::GLFW_References--;
    if (CPP_Registry::GLFW_References <= 0) {
        glfwTerminate();
        CPP_Registry::Is_GLFW_Initialized = false;
    }

    CPP_StaticDisplay::Display_Context = nullptr;
}