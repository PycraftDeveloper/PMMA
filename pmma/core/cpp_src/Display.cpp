#include <iostream>

#include <GLFW/glfw3.h>

#include "Display.hpp"

using namespace std;

namespace CPP_StaticDisplay {
    unsigned int Width = 0; // Default width
    unsigned int Height = 0; // Default height
    bool DisplayCreated = false;
}

void CPP_Display::Create(unsigned int New_Width, unsigned int New_Height) {
    glfwInit();

    GLFWwindow* window = glfwCreateWindow(New_Width, New_Height, "My Title", NULL, NULL);

    CPP_StaticDisplay::Width = New_Width;
    CPP_StaticDisplay::Height = New_Height;
    CPP_StaticDisplay::DisplayCreated = true;
}

unsigned int CPP_Display::GetWidth() {
    if (!CPP_StaticDisplay::DisplayCreated) {
        cerr << "Display not created yet!" << endl;
        return 0;
    }
    return CPP_StaticDisplay::Width;
}

unsigned int CPP_Display::GetHeight() {
    if (!CPP_StaticDisplay::DisplayCreated) {
        cerr << "Display not created yet!" << endl;
        return 0;
    }
    return CPP_StaticDisplay::Height;
}