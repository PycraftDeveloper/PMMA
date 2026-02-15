#define STB_IMAGE_IMPLEMENTATION
#include <STB/stb_image.h>

#include <filesystem>

#include "PMMA_Core.hpp"

namespace PMMA_Core {
    CPP_Display* DisplayInstance = nullptr;
    CPP_RenderPipelineCore* RenderPipelineCore = nullptr;

    std::vector<CPP_KeyEvent_Space*> KeyEvent_Space_Instances;
    std::vector<CPP_KeyEvent_Apostrophe*> KeyEvent_Apostrophe_Instances;
    std::vector<CPP_KeyEvent_Comma*> KeyEvent_Comma_Instances;
    std::vector<CPP_KeyEvent_Minus*> KeyEvent_Minus_Instances;
    std::vector<CPP_KeyEvent_Period*> KeyEvent_Period_Instances;
    std::vector<CPP_KeyEvent_Slash*> KeyEvent_Slash_Instances;
    std::vector<CPP_KeyEvent_0*> KeyEvent_0_Instances;
    std::vector<CPP_KeyEvent_1*> KeyEvent_1_Instances;
    std::vector<CPP_KeyEvent_2*> KeyEvent_2_Instances;
    std::vector<CPP_KeyEvent_3*> KeyEvent_3_Instances;
    std::vector<CPP_KeyEvent_4*> KeyEvent_4_Instances;
    std::vector<CPP_KeyEvent_5*> KeyEvent_5_Instances;
    std::vector<CPP_KeyEvent_6*> KeyEvent_6_Instances;
    std::vector<CPP_KeyEvent_7*> KeyEvent_7_Instances;
    std::vector<CPP_KeyEvent_8*> KeyEvent_8_Instances;
    std::vector<CPP_KeyEvent_9*> KeyEvent_9_Instances;
    std::vector<CPP_KeyEvent_Semicolon*> KeyEvent_Semicolon_Instances;
    std::vector<CPP_KeyEvent_Equal*> KeyEvent_Equal_Instances;
    std::vector<CPP_KeyEvent_A*> KeyEvent_A_Instances;
    std::vector<CPP_KeyEvent_B*> KeyEvent_B_Instances;
    std::vector<CPP_KeyEvent_C*> KeyEvent_C_Instances;
    std::vector<CPP_KeyEvent_D*> KeyEvent_D_Instances;
    std::vector<CPP_KeyEvent_E*> KeyEvent_E_Instances;
    std::vector<CPP_KeyEvent_F*> KeyEvent_F_Instances;
    std::vector<CPP_KeyEvent_G*> KeyEvent_G_Instances;
    std::vector<CPP_KeyEvent_H*> KeyEvent_H_Instances;
    std::vector<CPP_KeyEvent_I*> KeyEvent_I_Instances;
    std::vector<CPP_KeyEvent_J*> KeyEvent_J_Instances;
    std::vector<CPP_KeyEvent_K*> KeyEvent_K_Instances;
    std::vector<CPP_KeyEvent_L*> KeyEvent_L_Instances;
    std::vector<CPP_KeyEvent_M*> KeyEvent_M_Instances;
    std::vector<CPP_KeyEvent_N*> KeyEvent_N_Instances;
    std::vector<CPP_KeyEvent_O*> KeyEvent_O_Instances;
    std::vector<CPP_KeyEvent_P*> KeyEvent_P_Instances;
    std::vector<CPP_KeyEvent_Q*> KeyEvent_Q_Instances;
    std::vector<CPP_KeyEvent_R*> KeyEvent_R_Instances;
    std::vector<CPP_KeyEvent_S*> KeyEvent_S_Instances;
    std::vector<CPP_KeyEvent_T*> KeyEvent_T_Instances;
    std::vector<CPP_KeyEvent_U*> KeyEvent_U_Instances;
    std::vector<CPP_KeyEvent_V*> KeyEvent_V_Instances;
    std::vector<CPP_KeyEvent_W*> KeyEvent_W_Instances;
    std::vector<CPP_KeyEvent_X*> KeyEvent_X_Instances;
    std::vector<CPP_KeyEvent_Y*> KeyEvent_Y_Instances;
    std::vector<CPP_KeyEvent_Z*> KeyEvent_Z_Instances;
    std::vector<CPP_KeyEvent_Left_Bracket*> KeyEvent_Left_Bracket_Instances;
    std::vector<CPP_KeyEvent_Backslash*> KeyEvent_Backslash_Instances;
    std::vector<CPP_KeyEvent_Right_Bracket*> KeyEvent_Right_Bracket_Instances;
    std::vector<CPP_KeyEvent_Grave_Accent*> KeyEvent_Grave_Accent_Instances;
    std::vector<CPP_KeyEvent_World_1*> KeyEvent_World_1_Instances;
    std::vector<CPP_KeyEvent_World_2*> KeyEvent_World_2_Instances;
    std::vector<CPP_KeyEvent_Escape*> KeyEvent_Escape_Instances;
    std::vector<CPP_KeyEvent_Enter*> KeyEvent_Enter_Instances;
    std::vector<CPP_KeyEvent_Tab*> KeyEvent_Tab_Instances;
    std::vector<CPP_KeyEvent_Backspace*> KeyEvent_Backspace_Instances;
    std::vector<CPP_KeyEvent_Insert*> KeyEvent_Insert_Instances;
    std::vector<CPP_KeyEvent_Delete*> KeyEvent_Delete_Instances;
    std::vector<CPP_KeyEvent_Right*> KeyEvent_Right_Instances;
    std::vector<CPP_KeyEvent_Left*> KeyEvent_Left_Instances;
    std::vector<CPP_KeyEvent_Down*> KeyEvent_Down_Instances;
    std::vector<CPP_KeyEvent_Up*> KeyEvent_Up_Instances;
    std::vector<CPP_KeyEvent_Page_Up*> KeyEvent_Page_Up_Instances;
    std::vector<CPP_KeyEvent_Page_Down*> KeyEvent_Page_Down_Instances;
    std::vector<CPP_KeyEvent_Home*> KeyEvent_Home_Instances;
    std::vector<CPP_KeyEvent_End*> KeyEvent_End_Instances;
    std::vector<CPP_KeyEvent_Caps_Lock*> KeyEvent_Caps_Lock_Instances;
    std::vector<CPP_KeyEvent_Scroll_Lock*> KeyEvent_Scroll_Lock_Instances;
    std::vector<CPP_KeyEvent_Num_Lock*> KeyEvent_Num_Lock_Instances;
    std::vector<CPP_KeyEvent_Print_Screen*> KeyEvent_Print_Screen_Instances;
    std::vector<CPP_KeyEvent_Pause*> KeyEvent_Pause_Instances;
    std::vector<CPP_KeyEvent_F1*> KeyEvent_F1_Instances;
    std::vector<CPP_KeyEvent_F2*> KeyEvent_F2_Instances;
    std::vector<CPP_KeyEvent_F3*> KeyEvent_F3_Instances;
    std::vector<CPP_KeyEvent_F4*> KeyEvent_F4_Instances;
    std::vector<CPP_KeyEvent_F5*> KeyEvent_F5_Instances;
    std::vector<CPP_KeyEvent_F6*> KeyEvent_F6_Instances;
    std::vector<CPP_KeyEvent_F7*> KeyEvent_F7_Instances;
    std::vector<CPP_KeyEvent_F8*> KeyEvent_F8_Instances;
    std::vector<CPP_KeyEvent_F9*> KeyEvent_F9_Instances;
    std::vector<CPP_KeyEvent_F10*> KeyEvent_F10_Instances;
    std::vector<CPP_KeyEvent_F11*> KeyEvent_F11_Instances;
    std::vector<CPP_KeyEvent_F12*> KeyEvent_F12_Instances;
    std::vector<CPP_KeyEvent_F13*> KeyEvent_F13_Instances;
    std::vector<CPP_KeyEvent_F14*> KeyEvent_F14_Instances;
    std::vector<CPP_KeyEvent_F15*> KeyEvent_F15_Instances;
    std::vector<CPP_KeyEvent_F16*> KeyEvent_F16_Instances;
    std::vector<CPP_KeyEvent_F17*> KeyEvent_F17_Instances;
    std::vector<CPP_KeyEvent_F18*> KeyEvent_F18_Instances;
    std::vector<CPP_KeyEvent_F19*> KeyEvent_F19_Instances;
    std::vector<CPP_KeyEvent_F20*> KeyEvent_F20_Instances;
    std::vector<CPP_KeyEvent_F21*> KeyEvent_F21_Instances;
    std::vector<CPP_KeyEvent_F22*> KeyEvent_F22_Instances;
    std::vector<CPP_KeyEvent_F23*> KeyEvent_F23_Instances;
    std::vector<CPP_KeyEvent_F24*> KeyEvent_F24_Instances;
    std::vector<CPP_KeyEvent_F25*> KeyEvent_F25_Instances;
    std::vector<CPP_KeyEvent_Left_Shift*> KeyEvent_Left_Shift_Instances;
    std::vector<CPP_KeyEvent_Left_Control*> KeyEvent_Left_Control_Instances;
    std::vector<CPP_KeyEvent_Left_Alt*> KeyEvent_Left_Alt_Instances;
    std::vector<CPP_KeyEvent_Left_Super*> KeyEvent_Left_Super_Instances;
    std::vector<CPP_KeyEvent_Right_Shift*> KeyEvent_Right_Shift_Instances;
    std::vector<CPP_KeyEvent_Right_Control*> KeyEvent_Right_Control_Instances;
    std::vector<CPP_KeyEvent_Right_Alt*> KeyEvent_Right_Alt_Instances;
    std::vector<CPP_KeyEvent_Right_Super*> KeyEvent_Right_Super_Instances;
    std::vector<CPP_KeyEvent_Shift*> KeyEvent_Shift_Instances;
    std::vector<CPP_KeyEvent_Control*> KeyEvent_Control_Instances;
    std::vector<CPP_KeyEvent_Alt*> KeyEvent_Alt_Instances;
    std::vector<CPP_KeyEvent_Super*> KeyEvent_Super_Instances;
    std::vector<CPP_KeyEvent_Menu*> KeyEvent_Menu_Instances;
    std::vector<CPP_KeyPadEvent_0*> KeyPadEvent_0_Instances;
    std::vector<CPP_KeyPadEvent_1*> KeyPadEvent_1_Instances;
    std::vector<CPP_KeyPadEvent_2*> KeyPadEvent_2_Instances;
    std::vector<CPP_KeyPadEvent_3*> KeyPadEvent_3_Instances;
    std::vector<CPP_KeyPadEvent_4*> KeyPadEvent_4_Instances;
    std::vector<CPP_KeyPadEvent_5*> KeyPadEvent_5_Instances;
    std::vector<CPP_KeyPadEvent_6*> KeyPadEvent_6_Instances;
    std::vector<CPP_KeyPadEvent_7*> KeyPadEvent_7_Instances;
    std::vector<CPP_KeyPadEvent_8*> KeyPadEvent_8_Instances;
    std::vector<CPP_KeyPadEvent_9*> KeyPadEvent_9_Instances;
    std::vector<CPP_KeyPadEvent_Decimal*> KeyPadEvent_Decimal_Instances;
    std::vector<CPP_KeyPadEvent_Divide*> KeyPadEvent_Divide_Instances;
    std::vector<CPP_KeyPadEvent_Multiply*> KeyPadEvent_Multiply_Instances;
    std::vector<CPP_KeyPadEvent_Subtract*> KeyPadEvent_Subtract_Instances;
    std::vector<CPP_KeyPadEvent_Add*> KeyPadEvent_Add_Instances;
    std::vector<CPP_KeyPadEvent_Enter*> KeyPadEvent_Enter_Instances;
    std::vector<CPP_KeyPadEvent_Equal*> KeyPadEvent_Equal_Instances;

    std::vector<CPP_TextEvent*> TextEventInstances;

    std::vector<CPP_MousePositionEvent*> MousePositionEvent_Instances;
    std::vector<CPP_MouseEnterWindowEvent*> MouseEnterWindowEvent_Instances;

    std::vector<CPP_MouseButtonEvent_Left*> MouseButtonEvent_Left_Instances;
    std::vector<CPP_MouseButtonEvent_Right*> MouseButtonEvent_Right_Instances;
    std::vector<CPP_MouseButtonEvent_Middle*> MouseButtonEvent_Middle_Instances;
    std::vector<CPP_MouseButtonEvent_0*> MouseButtonEvent_0_Instances;
    std::vector<CPP_MouseButtonEvent_1*> MouseButtonEvent_1_Instances;
    std::vector<CPP_MouseButtonEvent_2*> MouseButtonEvent_2_Instances;
    std::vector<CPP_MouseButtonEvent_3*> MouseButtonEvent_3_Instances;
    std::vector<CPP_MouseButtonEvent_4*> MouseButtonEvent_4_Instances;

    std::vector<CPP_MouseScrollEvent*> MouseScrollEventInstances;

    std::vector<CPP_InternalControllerEvent*> InternalControllerEventInstances;
    std::vector<CPP_ControllerEvent*> ControllerEvent_Instances;

    std::vector<CPP_DropEvent*> DropEvent_Instances;

    CPP_InternalKeyEventManager* KeyManagerInstance = nullptr;
    CPP_InternalTextEventManager* TextManagerInstance = nullptr;
    CPP_InternalMousePositionEventManager* MousePositionManagerInstance = nullptr;
    CPP_InternalMouseEnterWindowEventManager* MouseEnterWindowManagerInstance = nullptr;
    CPP_InternalMouseButtonEventManager* MouseButtonManagerInstance = nullptr;
    CPP_InternalMouseScrollEventManager* MouseScrollManagerInstance = nullptr;
    CPP_InternalControllerEventManager* ControllerManagerInstance = nullptr;
    CPP_InternalDropEventManager* DropManagerInstance = nullptr;

    CPP_Passport* PassportInstance = nullptr;
    CPP_LoggingManager* LoggingManagerInstance = nullptr;

    PowerSavingManager PowerSavingManagerInstance;

    CPP_AnimationManager* AnimationManagerInstance = nullptr;
}

namespace PMMA_Registry {
    std::string PMMA_Location = "";
    std::string PathSeparator = std::string(1, std::filesystem::path::preferred_separator);
    std::string Current_PMMA_Version = "5.0.16";
    std::string Latest_PMMA_Version = "";
    std::string Locale = "en-US";

    std::mutex SeedGeneratorLock;
    std::mt19937 RandomSeedGenerator;
    std::uniform_int_distribution<uint32_t> SeedDistribution;

    std::chrono::high_resolution_clock::time_point StartupTime = std::chrono::high_resolution_clock::now();

    uint64_t ClassObject_ID_System = 0;

    unsigned int KeyboardEventInstanceCount = 0;
    unsigned int TextEventInstanceCount = 0;
    unsigned int MousePositionEventInstanceCount = 0;
    unsigned int MouseEnterWindowEventInstanceCount = 0;
    unsigned int MouseButtonEventInstanceCount = 0;
    unsigned int MouseScrollEventInstanceCount = 0;
    unsigned int ControllerEventInstanceCount = 0;
    unsigned int DropEventInstanceCount = 0;

    float CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY;

    int GLFW_References = 0;

    bool GLFW_Initialized = false;
    bool CPU_Supports_AVX2 = CPP_CPU_FeatureSetUtils::SupportsAVX2();
    bool CPU_Supports_AVX512 = CPP_CPU_FeatureSetUtils::SupportsAVX512();
    bool IsPowerSavingModeEnabled = CPP_General::Is_Power_Saving_Mode_Enabled(true);
    bool IsDebuggingModeEnabled = true;
    bool IsApplicationRunning = true;
    bool EscapeKeyShouldCloseWindow = false;
    bool UserSetEscapeKeyShouldCloseWindow = false;
    bool F11KeyShouldToggleFullScreen = true;
    bool UserDefinedShapeQuality = false;
}

void PMMA_Initialize(std::string location) {
    if (std::filesystem::exists(location)) {
        if (!std::filesystem::is_directory(location)) {
            throw std::runtime_error("The provided PMMA location is not a directory.");
        }
    } else {
        throw std::runtime_error("The provided PMMA location does not exist.");
    }

    PMMA_Registry::PMMA_Location = location;

    PMMA_Registry::RandomSeedGenerator.seed(std::random_device{}());

    PMMA_Core::LoggingManagerInstance = new CPP_LoggingManager();

    PMMA_Core::LoggingManagerInstance->InternalLogInfo(
        0,
        "PMMA logging initialized, log files are named: 'DD-MM-YYYY at HH-MM-SS.txt'.");

    PMMA_Core::LoggingManagerInstance->InternalLogInfo(
        12,
        "Welcome to Python Multi-Media API (PMMA) version: " + PMMA_Registry::Current_PMMA_Version);

    PMMA_Core::LoggingManagerInstance->InternalLogInfo(
        14,
        "Please note that PMMA is currently in a developmental state, \
meaning that the API is subject to change - we are hoping to remove this \
warning and improve backwards compatibility in PMMA 6.");

    if (PMMA_Registry::IsPowerSavingModeEnabled) {
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 30; // Reset the counter to a lower value if power saving mode is enabled
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY * 0.5f;
        PMMA_Core::LoggingManagerInstance->InternalLogInfo(
            1,
            "Your device is running in power saving mode.", true);
    } else {
        PMMA_Core::LoggingManagerInstance->InternalLogInfo(
            2,
            "Your device is not running in power saving mode.", true);
    }

    if (PMMA_Registry::CPU_Supports_AVX512) {
        PMMA_Core::LoggingManagerInstance->InternalLogInfo(
            3,
            "PMMA has detected that your system has AVX-512 support \
and will automatically use it where applicable. AVX-512 allows for up to \
16 operations to be performed simultaneously on the CPU.");
    } else {
        if (PMMA_Registry::CPU_Supports_AVX2) {
            PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                4,
                "PMMA has detected that your system has AVX2 support \
and will automatically use it where applicable. AVX2 allows for up to \
8 operations to be performed simultaneously on the CPU.");
        } else {
            PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                5,
                "PMMA has detected that your system does not have any \
support for AVX-512 or AVX2. This will not affect the usability of PMMA \
but may result in reduced performance.");
        }
    }

    #ifdef USE_PYTHON
        PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                6,
                "PMMA has been built with compatibility for the Python programming language!");
    #else
        PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                6,
                "PMMA has not been built with additional compatibility \
for Python, this does not effect the operation of PMMA but will change \
how PMMA and Python interact.");
    #endif

    PMMA_Core::PowerSavingManagerInstance.PowerSavingModeCheckingThread = std::thread(PowerSavingUpdaterThread);
}

void PMMA_Uninitialize() {
    PMMA_Core::PowerSavingManagerInstance.stop();

    delete PMMA_Core::LoggingManagerInstance;
    PMMA_Core::LoggingManagerInstance = nullptr;
}

uint32_t GetRandomSeed() {
    std::lock_guard<std::mutex> lock(PMMA_Registry::SeedGeneratorLock);
    return PMMA_Registry::SeedDistribution(PMMA_Registry::RandomSeedGenerator);
}