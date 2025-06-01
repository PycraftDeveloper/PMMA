#include <iostream>

#include <GLFW/glfw3.h>

#include "Display.hpp"

#include "Registry.hpp"

using namespace std;

namespace CPP_StaticDisplay {
    unsigned int Size[2];
    char* Caption;
    bool DisplayCreated = false;
    GLFWwindow* Window = nullptr;
}

void CPP_Display::Create(unsigned int* Size, char* Caption) {
    if (!CPP_Registry::Is_GLFW_Initialized) {
        glfwInit();
        CPP_Registry::Is_GLFW_Initialized = true;
    }

    CPP_StaticDisplay::Window = glfwCreateWindow(Size[0], Size[1], Caption, NULL, NULL);

    CPP_StaticDisplay::Size[0] = Size[0];
    CPP_StaticDisplay::Size[1] = Size[1];
    CPP_StaticDisplay::Caption = Caption;
    CPP_StaticDisplay::DisplayCreated = true;
}

unsigned int CPP_Display::GetWidth() {
    if (!CPP_StaticDisplay::DisplayCreated) {
        cerr << "Display not created yet!" << endl;
        return 0;
    }
    return CPP_StaticDisplay::Size[0];
}

unsigned int CPP_Display::GetHeight() {
    if (!CPP_StaticDisplay::DisplayCreated) {
        cerr << "Display not created yet!" << endl;
        return 0;
    }
    return CPP_StaticDisplay::Size[1];
}