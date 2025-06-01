#pragma once

#include <string>

#include <GLFW/glfw3.h>

namespace CPP_StaticDisplay {
    extern unsigned int Size[2];
    extern char* Caption;
    extern bool DisplayCreated;
    extern GLFWwindow* Window;
}

class CPP_Display {
    public:
        void Create(unsigned int* Size, char* Caption);

        unsigned int GetWidth();
        unsigned int GetHeight();
};