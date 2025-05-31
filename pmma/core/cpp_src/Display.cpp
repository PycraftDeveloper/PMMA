#include <iostream>

#include <GLFW/glfw3.h>

#include "Display.hpp"

using namespace std;

void CW() {
    glfwInit();

    GLFWwindow* window = glfwCreateWindow(640, 480, "My Title", NULL, NULL);
}