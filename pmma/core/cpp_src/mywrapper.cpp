#include <iostream>

#include <GLFW/glfw3.h>

#include "mywrapper.hpp"

using namespace std;

int multiply(int a, int b) {
    return a * b;
}

void CW() {
    glfwInit();

    GLFWwindow* window = glfwCreateWindow(640, 480, "My Title", NULL, NULL);
}