#include <iostream>

#include <GLFW/glfw3.h>

#include "InternalEventsManager.hpp"

#include "InternalEvents.hpp"
#include "PMMA_Core.hpp"

using namespace std;

CPP_EventsManager::CPP_EventsManager(GLFWwindow* Window) {
    PMMA::SpaceKeyEventInstance = new CPP_InternalSpaceKeyEvent();

    glfwSetKeyCallback(Window, CPP_EventsManager::KeyCallback);
    glfwSetCharCallback(Window, CPP_EventsManager::TextCallback);
    glfwSetCursorPosCallback(Window, CPP_EventsManager::CursorPositionCallback);
    glfwSetCursorEnterCallback(Window, CPP_EventsManager::CursorEnterCallback);
    glfwSetMouseButtonCallback(Window, CPP_EventsManager::MouseButtonCallback);
    glfwSetScrollCallback(Window, CPP_EventsManager::ScrollCallback);
    glfwSetJoystickCallback(CPP_EventsManager::JoystickCallback);
    glfwSetDropCallback(Window, CPP_EventsManager::DropCallback);
}

CPP_EventsManager::~CPP_EventsManager() {
    delete PMMA::SpaceKeyEventInstance;
    PMMA::SpaceKeyEventInstance = nullptr;
}

void CPP_EventsManager::KeyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    if (key == GLFW_KEY_SPACE) {
        PMMA::SpaceKeyEventInstance->Update(action == GLFW_PRESS);
    }
}

void CPP_EventsManager::TextCallback(GLFWwindow* window, unsigned int codepoint) {

}

void CPP_EventsManager::CursorPositionCallback(GLFWwindow* window, double xpos, double ypos) {

}

void CPP_EventsManager::CursorEnterCallback(GLFWwindow* window, int entered) {

}

void CPP_EventsManager::MousePositionCallback(GLFWwindow* window, int button, int action, int mods) {

}

void CPP_EventsManager::MouseButtonCallback(GLFWwindow* window, int button, int action, int mods) {

}

void CPP_EventsManager::ScrollCallback(GLFWwindow* window, double xoffset, double yoffset) {

}

void CPP_EventsManager::JoystickCallback(int jid, int event) {

}

void CPP_EventsManager::DropCallback(GLFWwindow* window, int count, const char** paths) {

}