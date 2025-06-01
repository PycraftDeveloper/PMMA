#pragma once

#include <string>

#include <GLFW/glfw3.h>

class CPP_Display {
    public:
        CPP_Display();

        void Create(unsigned int* Size, char* Caption);

        unsigned int GetWidth();
        unsigned int GetHeight();

        ~CPP_Display();
};

namespace CPP_StaticDisplay {
    extern unsigned int Size[2];
    extern char* Caption;
    extern bool DisplayCreated;
    extern GLFWwindow* Window;
    extern CPP_Display* Display_Context;
}