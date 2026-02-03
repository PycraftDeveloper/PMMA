#include <GLFW/glfw3.h>

#include "PMMA_Core.hpp"

inline std::string encode_utf8(unsigned int codepoint) {
    std::string out;
    if (codepoint <= 0x7F) {
        out += static_cast<char>(codepoint);
    } else if (codepoint <= 0x7FF) {
        out += static_cast<char>(0xC0 | ((codepoint >> 6) & 0x1F));
        out += static_cast<char>(0x80 | (codepoint & 0x3F));
    } else if (codepoint <= 0xFFFF) {
        out += static_cast<char>(0xE0 | ((codepoint >> 12) & 0x0F));
        out += static_cast<char>(0x80 | ((codepoint >> 6) & 0x3F));
        out += static_cast<char>(0x80 | (codepoint & 0x3F));
    } else if (codepoint <= 0x10FFFF) {
        out += static_cast<char>(0xF0 | ((codepoint >> 18) & 0x07));
        out += static_cast<char>(0x80 | ((codepoint >> 12) & 0x3F));
        out += static_cast<char>(0x80 | ((codepoint >> 6) & 0x3F));
        out += static_cast<char>(0x80 | (codepoint & 0x3F));
    }
    return out;
}

CPP_InternalTextEventManager::CPP_InternalTextEventManager() {
    Active = false;
}

CPP_InternalTextEventManager::~CPP_InternalTextEventManager() {
    Active = false;
}

void CPP_InternalTextEventManager::Update(GLFWwindow* Window) {
    for (int i = 0; i < PMMA_Core::TextEventInstances.size(); i++) {
        PMMA_Core::TextEventInstances[i]->GenericUpdate(Window);
    }
    Active = true;
}

void CPP_InternalTextEventManager::TextCallback(GLFWwindow* window, unsigned int codepoint) {
    std::string NewTextContent = encode_utf8(codepoint);
    for (int i = 0; i < PMMA_Core::TextEventInstances.size(); i++) {
        PMMA_Core::TextEventInstances[i]->Update(NewTextContent);
    }
}

CPP_InternalMousePositionEventManager::CPP_InternalMousePositionEventManager() {
    Active = false;
}

CPP_InternalMousePositionEventManager::~CPP_InternalMousePositionEventManager() {
    Active = false;
}

void CPP_InternalMousePositionEventManager::Update(GLFWwindow* Window) {
    Active = true;
}

void CPP_InternalMousePositionEventManager::CursorPositionCallback(GLFWwindow* window, double xpos, double ypos) {
    for (unsigned int i = 0; i < PMMA_Core::MousePositionEvent_Instances.size(); i++) {
        PMMA_Core::MousePositionEvent_Instances[i]->Update(static_cast<float>(xpos), static_cast<float>(ypos));
    }
}

CPP_InternalMouseEnterWindowEventManager::CPP_InternalMouseEnterWindowEventManager() {
    Active = false;
}

CPP_InternalMouseEnterWindowEventManager::~CPP_InternalMouseEnterWindowEventManager() {
    Active = false;
}

void CPP_InternalMouseEnterWindowEventManager::Update(GLFWwindow* Window) {
    Active = true;
}

void CPP_InternalMouseEnterWindowEventManager::CursorEnterCallback(GLFWwindow* window, int entered) {
    for (unsigned int i = 0; i < PMMA_Core::MouseEnterWindowEvent_Instances.size(); i++) {
        PMMA_Core::MouseEnterWindowEvent_Instances[i]->Update(entered);
    }
}

CPP_InternalMouseButtonEventManager::CPP_InternalMouseButtonEventManager() {
    Active = false;
}

CPP_InternalMouseButtonEventManager::~CPP_InternalMouseButtonEventManager() {
    Active = false;
}

void CPP_InternalMouseButtonEventManager::Update(GLFWwindow* Window) {
    Active = true;
}

void CPP_InternalMouseButtonEventManager::MouseButtonCallback(GLFWwindow* window, int button, int action, int mods) {
    if (button == GLFW_MOUSE_BUTTON_LEFT) {
        for (unsigned int i = 0; i < PMMA_Core::MouseButtonEvent_Left_Instances.size(); i++) {
            PMMA_Core::MouseButtonEvent_Left_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (button == GLFW_MOUSE_BUTTON_RIGHT) {
        for (unsigned int i = 0; i < PMMA_Core::MouseButtonEvent_Right_Instances.size(); i++) {
            PMMA_Core::MouseButtonEvent_Right_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (button == GLFW_MOUSE_BUTTON_MIDDLE) {
        for (unsigned int i = 0; i < PMMA_Core::MouseButtonEvent_Middle_Instances.size(); i++) {
            PMMA_Core::MouseButtonEvent_Middle_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (button == GLFW_MOUSE_BUTTON_4) {
        for (unsigned int i = 0; i < PMMA_Core::MouseButtonEvent_0_Instances.size(); i++) {
            PMMA_Core::MouseButtonEvent_0_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (button == GLFW_MOUSE_BUTTON_5) {
        for (unsigned int i = 0; i < PMMA_Core::MouseButtonEvent_1_Instances.size(); i++) {
            PMMA_Core::MouseButtonEvent_1_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (button == GLFW_MOUSE_BUTTON_6) {
        for (unsigned int i = 0; i < PMMA_Core::MouseButtonEvent_2_Instances.size(); i++) {
            PMMA_Core::MouseButtonEvent_2_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (button == GLFW_MOUSE_BUTTON_7) {
        for (unsigned int i = 0; i < PMMA_Core::MouseButtonEvent_3_Instances.size(); i++) {
            PMMA_Core::MouseButtonEvent_3_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (button == GLFW_MOUSE_BUTTON_8) {
        for (unsigned int i = 0; i < PMMA_Core::MouseButtonEvent_4_Instances.size(); i++) {
            PMMA_Core::MouseButtonEvent_4_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else {
        std::cout << "Unknown mouse button: " << button << std::endl;
    }
}

CPP_InternalMouseScrollEventManager::CPP_InternalMouseScrollEventManager() {
    Active = false;
}

CPP_InternalMouseScrollEventManager::~CPP_InternalMouseScrollEventManager() {
    Active = false;
}

void CPP_InternalMouseScrollEventManager::Update(GLFWwindow* Window) {
    Active = true;
}

void CPP_InternalMouseScrollEventManager::ScrollCallback(GLFWwindow* window, double xoffset, double yoffset) {
    for (int i = 0; i < PMMA_Core::MouseScrollEventInstances.size(); i++) {
        PMMA_Core::MouseScrollEventInstances[i]->Update(xoffset, yoffset);
    }
}

CPP_InternalControllerEventManager::CPP_InternalControllerEventManager() {
    Active = false;

    for (unsigned int i = 0; i < 16; i++) {
        PMMA_Core::InternalControllerEventInstances.emplace_back(new CPP_InternalControllerEvent(i));
        PMMA_Core::InternalControllerEventInstances[i]->UpdateConnection(glfwJoystickPresent(i) == GLFW_TRUE);
    }
}

CPP_InternalControllerEventManager::~CPP_InternalControllerEventManager() {
    Active = false;

    for (unsigned int i = 0; i < 16; i++) {
        delete PMMA_Core::InternalControllerEventInstances[i];
    }
    PMMA_Core::InternalControllerEventInstances.clear();
}

void CPP_InternalControllerEventManager::Update(GLFWwindow* Window) {
    std::vector<CPP_InternalControllerEvent*> ConnectedControllers;
    for (int i = 0; i < PMMA_Core::InternalControllerEventInstances.size(); i++) {
        if (PMMA_Core::InternalControllerEventInstances[i]->GetConnected()) {
            ConnectedControllers.push_back(PMMA_Core::InternalControllerEventInstances[i]);
        }
    }

    if (ConnectedControllers.size() > 0) {
        for (int i = 0; i < ConnectedControllers.size(); i++) {
            ConnectedControllers[i]->Update();
        }
    }
    Active = true;

    for (unsigned int i = 0; i < PMMA_Core::ControllerEvent_Instances.size(); i++) {
        PMMA_Core::ControllerEvent_Instances[i]->Update();
    }
}

void CPP_InternalControllerEventManager::JoystickCallback(int jid, int event) {
    PMMA_Core::InternalControllerEventInstances[jid]->UpdateConnection(event==GLFW_CONNECTED);
}

CPP_InternalDropEventManager::CPP_InternalDropEventManager() {
    Active = false;
}

CPP_InternalDropEventManager::~CPP_InternalDropEventManager() {
    Active = false;
}

void CPP_InternalDropEventManager::Update(GLFWwindow* Window) {
    Active = true;
}

void CPP_InternalDropEventManager::DropCallback(GLFWwindow* window, int count, const char** paths) {
    std::vector<std::string> PathList;
    for (int i = 0; i < count; i++) {
        PathList.push_back(paths[i]);
    }

    for (int i = 0; i < PMMA_Core::DropEvent_Instances.size(); i++) {
        PMMA_Core::DropEvent_Instances[i]->Update(PathList, count);
    }
}

CPP_InternalKeyEventManager::CPP_InternalKeyEventManager() {
    Active = false;

    Left_Shift_Instance = new CPP_KeyEvent_Left_Shift();
    Right_Shift_Instance = new CPP_KeyEvent_Right_Shift();
    Left_Control_Instance = new CPP_KeyEvent_Left_Control();
    Right_Control_Instance = new CPP_KeyEvent_Right_Control();
    Left_Alt_Instance = new CPP_KeyEvent_Left_Alt();
    Right_Alt_Instance = new CPP_KeyEvent_Right_Alt();
    Left_Super_Instance = new CPP_KeyEvent_Left_Super();
    Right_Super_Instance = new CPP_KeyEvent_Right_Super();
}

CPP_InternalKeyEventManager::~CPP_InternalKeyEventManager() {
    Active = false;

    delete Left_Shift_Instance;
    delete Right_Shift_Instance;
    delete Left_Control_Instance;
    delete Right_Control_Instance;
    delete Left_Alt_Instance;
    delete Right_Alt_Instance;
    delete Left_Super_Instance;
    delete Right_Super_Instance;

    Left_Shift_Instance = nullptr;
    Right_Shift_Instance = nullptr;
    Left_Control_Instance = nullptr;
    Right_Control_Instance = nullptr;
    Left_Alt_Instance = nullptr;
    Right_Alt_Instance = nullptr;
    Left_Super_Instance = nullptr;
    Right_Super_Instance = nullptr;
}

void CPP_InternalKeyEventManager::Update(GLFWwindow* Window) {
    for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Shift_Instances.size(); i++) {
        PMMA_Core::KeyEvent_Shift_Instances[i]->Update((Left_Shift_Instance->GetPressed() || Right_Shift_Instance->GetPressed()));
    }

    for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Control_Instances.size(); i++) {
        PMMA_Core::KeyEvent_Control_Instances[i]->Update((Left_Control_Instance->GetPressed() || Right_Control_Instance->GetPressed()));
    }

    for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Alt_Instances.size(); i++) {
        PMMA_Core::KeyEvent_Alt_Instances[i]->Update((Left_Alt_Instance->GetPressed() || Right_Alt_Instance->GetPressed()));
    }

    for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Super_Instances.size(); i++) {
        PMMA_Core::KeyEvent_Super_Instances[i]->Update((Left_Super_Instance->GetPressed() || Right_Super_Instance->GetPressed()));
    }

    Active = true;
}

void CPP_InternalKeyEventManager::KeyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    if (key == GLFW_KEY_SPACE) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Space_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Space_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_APOSTROPHE) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Apostrophe_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Apostrophe_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_COMMA) {
    for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Comma_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Comma_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_MINUS) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Minus_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Minus_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_PERIOD) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Period_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Period_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_SLASH) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Slash_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Slash_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_0) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_0_Instances.size(); i++) {
            PMMA_Core::KeyEvent_0_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_1) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_1_Instances.size(); i++) {
            PMMA_Core::KeyEvent_1_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_2) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_2_Instances.size(); i++) {
            PMMA_Core::KeyEvent_2_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_3) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_3_Instances.size(); i++) {
            PMMA_Core::KeyEvent_3_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_4) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_4_Instances.size(); i++) {
            PMMA_Core::KeyEvent_4_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_5) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_5_Instances.size(); i++) {
            PMMA_Core::KeyEvent_5_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_6) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_6_Instances.size(); i++) {
            PMMA_Core::KeyEvent_6_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_7) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_7_Instances.size(); i++) {
            PMMA_Core::KeyEvent_7_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_8) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_8_Instances.size(); i++) {
            PMMA_Core::KeyEvent_8_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_9) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_9_Instances.size(); i++) {
            PMMA_Core::KeyEvent_9_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_SEMICOLON) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Semicolon_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Semicolon_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_EQUAL) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Equal_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Equal_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_A) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_A_Instances.size(); i++) {
            PMMA_Core::KeyEvent_A_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_B) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_B_Instances.size(); i++) {
            PMMA_Core::KeyEvent_B_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_C) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_C_Instances.size(); i++) {
            PMMA_Core::KeyEvent_C_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_D) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_D_Instances.size(); i++) {
            PMMA_Core::KeyEvent_D_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_E) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_E_Instances.size(); i++) {
            PMMA_Core::KeyEvent_E_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_G) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_G_Instances.size(); i++) {
            PMMA_Core::KeyEvent_G_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_H) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_H_Instances.size(); i++) {
            PMMA_Core::KeyEvent_H_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_I) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_I_Instances.size(); i++) {
            PMMA_Core::KeyEvent_I_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_J) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_J_Instances.size(); i++) {
            PMMA_Core::KeyEvent_J_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_K) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_K_Instances.size(); i++) {
            PMMA_Core::KeyEvent_K_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_L) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_L_Instances.size(); i++) {
            PMMA_Core::KeyEvent_L_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_M) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_M_Instances.size(); i++) {
            PMMA_Core::KeyEvent_M_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_N) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_N_Instances.size(); i++) {
            PMMA_Core::KeyEvent_N_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_O) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_O_Instances.size(); i++) {
            PMMA_Core::KeyEvent_O_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_P) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_P_Instances.size(); i++) {
            PMMA_Core::KeyEvent_P_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_Q) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Q_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Q_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_R) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_R_Instances.size(); i++) {
            PMMA_Core::KeyEvent_R_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_S) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_S_Instances.size(); i++) {
            PMMA_Core::KeyEvent_S_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_T) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_T_Instances.size(); i++) {
            PMMA_Core::KeyEvent_T_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_U) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_U_Instances.size(); i++) {
            PMMA_Core::KeyEvent_U_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_V) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_V_Instances.size(); i++) {
            PMMA_Core::KeyEvent_V_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_W) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_W_Instances.size(); i++) {
            PMMA_Core::KeyEvent_W_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_X) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_X_Instances.size(); i++) {
            PMMA_Core::KeyEvent_X_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_Y) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Y_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Y_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_Z) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Z_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Z_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_LEFT_BRACKET) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Left_Bracket_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Left_Bracket_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_BACKSLASH) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Backslash_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Backslash_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_RIGHT_BRACKET) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Right_Bracket_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Right_Bracket_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_GRAVE_ACCENT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Grave_Accent_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Grave_Accent_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_WORLD_1) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_World_1_Instances.size(); i++) {
            PMMA_Core::KeyEvent_World_1_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_WORLD_2) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_World_2_Instances.size(); i++) {
            PMMA_Core::KeyEvent_World_2_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_ESCAPE) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Escape_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Escape_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_ENTER) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Enter_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Enter_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_TAB) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Tab_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Tab_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_BACKSPACE) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Backspace_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Backspace_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_INSERT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Insert_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Insert_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_DELETE) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Delete_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Delete_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_RIGHT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Right_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Right_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_LEFT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Left_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Left_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_DOWN) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Down_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Down_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_UP) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Up_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Up_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_PAGE_UP) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Page_Up_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Page_Up_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_PAGE_DOWN) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Page_Down_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Page_Down_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_HOME) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Home_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Home_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_END) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_End_Instances.size(); i++) {
            PMMA_Core::KeyEvent_End_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_CAPS_LOCK) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Caps_Lock_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Caps_Lock_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_SCROLL_LOCK) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Scroll_Lock_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Scroll_Lock_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_NUM_LOCK) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Num_Lock_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Num_Lock_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_PRINT_SCREEN) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Print_Screen_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Print_Screen_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_PAUSE) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Pause_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Pause_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F1) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F1_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F1_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F2) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F2_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F2_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F3) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F3_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F3_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F4) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F4_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F4_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F5) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F5_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F5_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F6) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F6_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F6_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F7) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F7_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F7_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F8) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F8_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F8_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F9) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F9_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F9_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F10) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F10_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F10_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F11) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F11_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F11_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F12) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F12_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F12_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F13) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F13_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F13_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F14) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F14_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F14_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F15) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F15_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F15_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F16) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F16_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F16_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F17) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F17_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F17_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F18) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F18_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F18_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F19) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F19_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F19_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F20) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F20_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F20_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F21) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F21_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F21_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F22) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F22_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F22_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F23) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F23_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F23_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F24) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F24_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F24_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_F25) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_F25_Instances.size(); i++) {
            PMMA_Core::KeyEvent_F25_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_0) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_0_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_0_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_1) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_1_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_1_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_2) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_2_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_2_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_3) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_3_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_3_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_4) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_4_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_4_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_5) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_5_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_5_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_6) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_6_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_6_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_7) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_7_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_7_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_8) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_8_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_8_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_9) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_9_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_9_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_DECIMAL) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_Decimal_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_Decimal_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_DIVIDE) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_Divide_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_Divide_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_MULTIPLY) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_Multiply_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_Multiply_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_SUBTRACT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_Subtract_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_Subtract_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_ADD) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_Add_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_Add_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_ENTER) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_Enter_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_Enter_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_KP_EQUAL) {
        for (unsigned int i = 0; i < PMMA_Core::KeyPadEvent_Equal_Instances.size(); i++) {
            PMMA_Core::KeyPadEvent_Equal_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_LEFT_SHIFT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Left_Shift_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Left_Shift_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_LEFT_CONTROL) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Left_Control_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Left_Control_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_LEFT_ALT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Left_Alt_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Left_Alt_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_LEFT_SUPER) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Left_Super_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Left_Super_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_RIGHT_SHIFT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Right_Shift_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Right_Shift_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_RIGHT_CONTROL) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Right_Control_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Right_Control_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_RIGHT_ALT) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Right_Alt_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Right_Alt_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_RIGHT_SUPER) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Right_Super_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Right_Super_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else if (key == GLFW_KEY_MENU) {
        for (unsigned int i = 0; i < PMMA_Core::KeyEvent_Menu_Instances.size(); i++) {
            PMMA_Core::KeyEvent_Menu_Instances[i]->Update(action!=GLFW_RELEASE);
        }
    } else {
        std::cout << "Unknown key: " << key << std::endl;
    }
}