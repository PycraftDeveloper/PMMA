#define STB_IMAGE_IMPLEMENTATION
#include <STB/stb_image.h>

#include <filesystem>
#include <numeric>

#include "PMMA_Core.hpp"

namespace PMMA::Core {
PMMA::Display *ActiveDisplayInstance = nullptr;
PMMA::Display *MasterDisplayInstance = nullptr;
PMMA::Internal::Rendering::Core2D::RenderPipelineManager *RenderPipelineCore = nullptr;

std::vector<PMMA::Events::Key_Space *> KeyEvent_Space_Instances;
std::vector<PMMA::Events::Key_Apostrophe *> KeyEvent_Apostrophe_Instances;
std::vector<PMMA::Events::Key_Comma *> KeyEvent_Comma_Instances;
std::vector<PMMA::Events::Key_Minus *> KeyEvent_Minus_Instances;
std::vector<PMMA::Events::Key_Period *> KeyEvent_Period_Instances;
std::vector<PMMA::Events::Key_Slash *> KeyEvent_Slash_Instances;
std::vector<PMMA::Events::Key_0 *> KeyEvent_0_Instances;
std::vector<PMMA::Events::Key_1 *> KeyEvent_1_Instances;
std::vector<PMMA::Events::Key_2 *> KeyEvent_2_Instances;
std::vector<PMMA::Events::Key_3 *> KeyEvent_3_Instances;
std::vector<PMMA::Events::Key_4 *> KeyEvent_4_Instances;
std::vector<PMMA::Events::Key_5 *> KeyEvent_5_Instances;
std::vector<PMMA::Events::Key_6 *> KeyEvent_6_Instances;
std::vector<PMMA::Events::Key_7 *> KeyEvent_7_Instances;
std::vector<PMMA::Events::Key_8 *> KeyEvent_8_Instances;
std::vector<PMMA::Events::Key_9 *> KeyEvent_9_Instances;
std::vector<PMMA::Events::Key_Semicolon *> KeyEvent_Semicolon_Instances;
std::vector<PMMA::Events::Key_Equal *> KeyEvent_Equal_Instances;
std::vector<PMMA::Events::Key_A *> KeyEvent_A_Instances;
std::vector<PMMA::Events::Key_B *> KeyEvent_B_Instances;
std::vector<PMMA::Events::Key_C *> KeyEvent_C_Instances;
std::vector<PMMA::Events::Key_D *> KeyEvent_D_Instances;
std::vector<PMMA::Events::Key_E *> KeyEvent_E_Instances;
std::vector<PMMA::Events::Key_F *> KeyEvent_F_Instances;
std::vector<PMMA::Events::Key_G *> KeyEvent_G_Instances;
std::vector<PMMA::Events::Key_H *> KeyEvent_H_Instances;
std::vector<PMMA::Events::Key_I *> KeyEvent_I_Instances;
std::vector<PMMA::Events::Key_J *> KeyEvent_J_Instances;
std::vector<PMMA::Events::Key_K *> KeyEvent_K_Instances;
std::vector<PMMA::Events::Key_L *> KeyEvent_L_Instances;
std::vector<PMMA::Events::Key_M *> KeyEvent_M_Instances;
std::vector<PMMA::Events::Key_N *> KeyEvent_N_Instances;
std::vector<PMMA::Events::Key_O *> KeyEvent_O_Instances;
std::vector<PMMA::Events::Key_P *> KeyEvent_P_Instances;
std::vector<PMMA::Events::Key_Q *> KeyEvent_Q_Instances;
std::vector<PMMA::Events::Key_R *> KeyEvent_R_Instances;
std::vector<PMMA::Events::Key_S *> KeyEvent_S_Instances;
std::vector<PMMA::Events::Key_T *> KeyEvent_T_Instances;
std::vector<PMMA::Events::Key_U *> KeyEvent_U_Instances;
std::vector<PMMA::Events::Key_V *> KeyEvent_V_Instances;
std::vector<PMMA::Events::Key_W *> KeyEvent_W_Instances;
std::vector<PMMA::Events::Key_X *> KeyEvent_X_Instances;
std::vector<PMMA::Events::Key_Y *> KeyEvent_Y_Instances;
std::vector<PMMA::Events::Key_Z *> KeyEvent_Z_Instances;
std::vector<PMMA::Events::Key_Left_Bracket *> KeyEvent_Left_Bracket_Instances;
std::vector<PMMA::Events::Key_Backslash *> KeyEvent_Backslash_Instances;
std::vector<PMMA::Events::Key_Right_Bracket *> KeyEvent_Right_Bracket_Instances;
std::vector<PMMA::Events::Key_Grave_Accent *> KeyEvent_Grave_Accent_Instances;
std::vector<PMMA::Events::Key_World_1 *> KeyEvent_World_1_Instances;
std::vector<PMMA::Events::Key_World_2 *> KeyEvent_World_2_Instances;
std::vector<PMMA::Events::Key_Escape *> KeyEvent_Escape_Instances;
std::vector<PMMA::Events::Key_Enter *> KeyEvent_Enter_Instances;
std::vector<PMMA::Events::Key_Tab *> KeyEvent_Tab_Instances;
std::vector<PMMA::Events::Key_Backspace *> KeyEvent_Backspace_Instances;
std::vector<PMMA::Events::Key_Insert *> KeyEvent_Insert_Instances;
std::vector<PMMA::Events::Key_Delete *> KeyEvent_Delete_Instances;
std::vector<PMMA::Events::Key_Right *> KeyEvent_Right_Instances;
std::vector<PMMA::Events::Key_Left *> KeyEvent_Left_Instances;
std::vector<PMMA::Events::Key_Down *> KeyEvent_Down_Instances;
std::vector<PMMA::Events::Key_Up *> KeyEvent_Up_Instances;
std::vector<PMMA::Events::Key_Page_Up *> KeyEvent_Page_Up_Instances;
std::vector<PMMA::Events::Key_Page_Down *> KeyEvent_Page_Down_Instances;
std::vector<PMMA::Events::Key_Home *> KeyEvent_Home_Instances;
std::vector<PMMA::Events::Key_End *> KeyEvent_End_Instances;
std::vector<PMMA::Events::Key_Caps_Lock *> KeyEvent_Caps_Lock_Instances;
std::vector<PMMA::Events::Key_Scroll_Lock *> KeyEvent_Scroll_Lock_Instances;
std::vector<PMMA::Events::Key_Num_Lock *> KeyEvent_Num_Lock_Instances;
std::vector<PMMA::Events::Key_Print_Screen *> KeyEvent_Print_Screen_Instances;
std::vector<PMMA::Events::Key_Pause *> KeyEvent_Pause_Instances;
std::vector<PMMA::Events::Key_F1 *> KeyEvent_F1_Instances;
std::vector<PMMA::Events::Key_F2 *> KeyEvent_F2_Instances;
std::vector<PMMA::Events::Key_F3 *> KeyEvent_F3_Instances;
std::vector<PMMA::Events::Key_F4 *> KeyEvent_F4_Instances;
std::vector<PMMA::Events::Key_F5 *> KeyEvent_F5_Instances;
std::vector<PMMA::Events::Key_F6 *> KeyEvent_F6_Instances;
std::vector<PMMA::Events::Key_F7 *> KeyEvent_F7_Instances;
std::vector<PMMA::Events::Key_F8 *> KeyEvent_F8_Instances;
std::vector<PMMA::Events::Key_F9 *> KeyEvent_F9_Instances;
std::vector<PMMA::Events::Key_F10 *> KeyEvent_F10_Instances;
std::vector<PMMA::Events::Key_F11 *> KeyEvent_F11_Instances;
std::vector<PMMA::Events::Key_F12 *> KeyEvent_F12_Instances;
std::vector<PMMA::Events::Key_F13 *> KeyEvent_F13_Instances;
std::vector<PMMA::Events::Key_F14 *> KeyEvent_F14_Instances;
std::vector<PMMA::Events::Key_F15 *> KeyEvent_F15_Instances;
std::vector<PMMA::Events::Key_F16 *> KeyEvent_F16_Instances;
std::vector<PMMA::Events::Key_F17 *> KeyEvent_F17_Instances;
std::vector<PMMA::Events::Key_F18 *> KeyEvent_F18_Instances;
std::vector<PMMA::Events::Key_F19 *> KeyEvent_F19_Instances;
std::vector<PMMA::Events::Key_F20 *> KeyEvent_F20_Instances;
std::vector<PMMA::Events::Key_F21 *> KeyEvent_F21_Instances;
std::vector<PMMA::Events::Key_F22 *> KeyEvent_F22_Instances;
std::vector<PMMA::Events::Key_F23 *> KeyEvent_F23_Instances;
std::vector<PMMA::Events::Key_F24 *> KeyEvent_F24_Instances;
std::vector<PMMA::Events::Key_F25 *> KeyEvent_F25_Instances;
std::vector<PMMA::Events::Key_Left_Shift *> KeyEvent_Left_Shift_Instances;
std::vector<PMMA::Events::Key_Left_Control *> KeyEvent_Left_Control_Instances;
std::vector<PMMA::Events::Key_Left_Alt *> KeyEvent_Left_Alt_Instances;
std::vector<PMMA::Events::Key_Left_Super *> KeyEvent_Left_Super_Instances;
std::vector<PMMA::Events::Key_Right_Shift *> KeyEvent_Right_Shift_Instances;
std::vector<PMMA::Events::Key_Right_Control *> KeyEvent_Right_Control_Instances;
std::vector<PMMA::Events::Key_Right_Alt *> KeyEvent_Right_Alt_Instances;
std::vector<PMMA::Events::Key_Right_Super *> KeyEvent_Right_Super_Instances;
std::vector<PMMA::Events::Key_Shift *> KeyEvent_Shift_Instances;
std::vector<PMMA::Events::Key_Control *> KeyEvent_Control_Instances;
std::vector<PMMA::Events::Key_Alt *> KeyEvent_Alt_Instances;
std::vector<PMMA::Events::Key_Super *> KeyEvent_Super_Instances;
std::vector<PMMA::Events::Key_Menu *> KeyEvent_Menu_Instances;
std::vector<PMMA::Events::KeyPad_0 *> KeyPadEvent_0_Instances;
std::vector<PMMA::Events::KeyPad_1 *> KeyPadEvent_1_Instances;
std::vector<PMMA::Events::KeyPad_2 *> KeyPadEvent_2_Instances;
std::vector<PMMA::Events::KeyPad_3 *> KeyPadEvent_3_Instances;
std::vector<PMMA::Events::KeyPad_4 *> KeyPadEvent_4_Instances;
std::vector<PMMA::Events::KeyPad_5 *> KeyPadEvent_5_Instances;
std::vector<PMMA::Events::KeyPad_6 *> KeyPadEvent_6_Instances;
std::vector<PMMA::Events::KeyPad_7 *> KeyPadEvent_7_Instances;
std::vector<PMMA::Events::KeyPad_8 *> KeyPadEvent_8_Instances;
std::vector<PMMA::Events::KeyPad_9 *> KeyPadEvent_9_Instances;
std::vector<PMMA::Events::KeyPad_Decimal *> KeyPadEvent_Decimal_Instances;
std::vector<PMMA::Events::KeyPad_Divide *> KeyPadEvent_Divide_Instances;
std::vector<PMMA::Events::KeyPad_Multiply *> KeyPadEvent_Multiply_Instances;
std::vector<PMMA::Events::KeyPad_Subtract *> KeyPadEvent_Subtract_Instances;
std::vector<PMMA::Events::KeyPad_Add *> KeyPadEvent_Add_Instances;
std::vector<PMMA::Events::KeyPad_Enter *> KeyPadEvent_Enter_Instances;
std::vector<PMMA::Events::KeyPad_Equal *> KeyPadEvent_Equal_Instances;

std::vector<PMMA::Events::Text *> TextEventInstances;

std::vector<PMMA::Events::Mouse_Position *> MousePositionEvent_Instances;
std::vector<PMMA::Events::Mouse_EnterWindow *> MouseEnterWindowEvent_Instances;

std::vector<PMMA::Events::Mouse_Button_Left *> MouseButtonEvent_Left_Instances;
std::vector<PMMA::Events::Mouse_Button_Right *> MouseButtonEvent_Right_Instances;
std::vector<PMMA::Events::Mouse_Button_Middle *> MouseButtonEvent_Middle_Instances;
std::vector<PMMA::Events::Mouse_Button_0 *> MouseButtonEvent_0_Instances;
std::vector<PMMA::Events::Mouse_Button_1 *> MouseButtonEvent_1_Instances;
std::vector<PMMA::Events::Mouse_Button_2 *> MouseButtonEvent_2_Instances;
std::vector<PMMA::Events::Mouse_Button_3 *> MouseButtonEvent_3_Instances;
std::vector<PMMA::Events::Mouse_Button_4 *> MouseButtonEvent_4_Instances;

std::vector<PMMA::Events::Mouse_Scroll *> MouseScrollEventInstances;

std::vector<PMMA::Internal::Events::InternalController *> InternalControllerEventInstances;
std::vector<PMMA::Events::Controller *> ControllerEvent_Instances;

std::vector<PMMA::Events::Drop *> DropEvent_Instances;

PMMA::Internal::Events::InternalKeyManager *KeyManagerInstance = nullptr;
PMMA::Internal::Events::InternalTextManager *TextManagerInstance = nullptr;
PMMA::Internal::Events::InternalMousePositionManager *MousePositionManagerInstance = nullptr;
PMMA::Internal::Events::InternalMouseEnterWindowManager *MouseEnterWindowManagerInstance = nullptr;
PMMA::Internal::Events::InternalMouseButtonManager *MouseButtonManagerInstance = nullptr;
PMMA::Internal::Events::InternalMouseScrollManager *MouseScrollManagerInstance = nullptr;
PMMA::Internal::Events::InternalControllerManager *ControllerManagerInstance = nullptr;
PMMA::Internal::Events::InternalDropManager *DropManagerInstance = nullptr;

PMMA::Passport *PassportInstance = nullptr;
PMMA::Internal::LoggingManager *LoggingManagerInstance = nullptr;

PowerSavingManager PowerSavingManagerInstance;

PMMA::Internal::AnimationManager *AnimationManagerInstance = nullptr;

PMMA::FastRandom *RandomGenerator = new PMMA::FastRandom();
} // namespace PMMA::Core

namespace PMMA::Registry {
std::vector<unsigned char> SecondaryDisplayIDs;

std::string PMMA_Location = "";
std::string PathSeparator = std::string(1, std::filesystem::path::preferred_separator);
std::string Current_PMMA_Version = "5.0.16";
std::string Latest_PMMA_Version = "";
std::string Locale = "en-US";

std::mutex SeedGeneratorLock;
std::mt19937 RandomSeedGenerator;
std::uniform_int_distribution<uint32_t> SeedDistribution;

std::chrono::high_resolution_clock::time_point StartupTime = std::chrono::high_resolution_clock::now();

unsigned int KeyboardEventInstanceCount = 0;
unsigned int TextEventInstanceCount = 0;
unsigned int MousePositionEventInstanceCount = 0;
unsigned int MouseEnterWindowEventInstanceCount = 0;
unsigned int MouseButtonEventInstanceCount = 0;
unsigned int MouseScrollEventInstanceCount = 0;
unsigned int ControllerEventInstanceCount = 0;
unsigned int DropEventInstanceCount = 0;

float CurrentShapeQuality = PMMA::Constants::SHAPE_QUALITY;

int GLFW_References = 0;

bool GLFW_Initialized = false;
bool CPU_Supports_AVX2 = PMMA::Utils::CPU_FeatureSet::SupportsAVX2();
bool CPU_Supports_AVX512 = PMMA::Utils::CPU_FeatureSet::SupportsAVX512();
bool IsPowerSavingModeEnabled = false;
bool IsDebuggingModeEnabled = true;
bool IsApplicationRunning = true;
bool EscapeKeyShouldCloseWindow = false;
bool UserSetEscapeKeyShouldCloseWindow = false;
bool F11KeyShouldToggleFullScreen = true;
bool UserDefinedShapeQuality = false;
} // namespace PMMA::Registry

void PMMA_Initialize(std::string location) {
    if (std::filesystem::exists(location)) {
        if (!std::filesystem::is_directory(location)) {
            throw std::runtime_error("The provided PMMA location is not a directory.");
        }
    } else {
        throw std::runtime_error("The provided PMMA location does not exist.");
    }

    PMMA::Registry::PMMA_Location = location;

    PMMA::Registry::RandomSeedGenerator.seed(std::random_device{}());

    PMMA::Core::LoggingManagerInstance = new PMMA::Internal::LoggingManager();

    PMMA::Core::LoggingManagerInstance->InternalLogInfo(
        0,
        "PMMA logging initialized, log files are named: 'DD-MM-YYYY at HH-MM-SS.txt'.");

    PMMA::Core::LoggingManagerInstance->InternalLogInfo(
        12,
        "Welcome to Python Multi-Media API (PMMA) version: " + PMMA::Registry::Current_PMMA_Version);

    std::string OperatingSystem = PMMA::General::GetOperatingSystem();
    PMMA::Core::LoggingManagerInstance->InternalLogInfo(
        46,
        "You are running on the Operating System: '" + OperatingSystem + "'.");

    PMMA::Core::LoggingManagerInstance->InternalLogInfo(
        14,
        "Please note that PMMA is currently in a developmental state, \
meaning that the API is subject to change - we are hoping to remove this \
warning and improve backwards compatibility in PMMA 6.");

    PMMA::Registry::IsPowerSavingModeEnabled = PMMA::General::Is_Power_Saving_Mode_Enabled(true);

    if (PMMA::Registry::CPU_Supports_AVX512) {
        PMMA::Core::LoggingManagerInstance->InternalLogInfo(
            3,
            "PMMA has detected that your system has AVX-512 support \
and will automatically use it where applicable. AVX-512 allows for up to \
16 operations to be performed simultaneously on the CPU.");
    } else {
        if (PMMA::Registry::CPU_Supports_AVX2) {
            PMMA::Core::LoggingManagerInstance->InternalLogInfo(
                4,
                "PMMA has detected that your system has AVX2 support \
and will automatically use it where applicable. AVX2 allows for up to \
8 operations to be performed simultaneously on the CPU.");
        } else {
            PMMA::Core::LoggingManagerInstance->InternalLogInfo(
                5,
                "PMMA has detected that your system does not have any \
support for AVX-512 or AVX2. This will not affect the usability of PMMA \
but may result in reduced performance.");
        }
    }

#ifdef USE_PYTHON
    PMMA::Core::LoggingManagerInstance->InternalLogInfo(
        6,
        "PMMA has been built with compatibility for the Python programming language!");
#else
    PMMA::Core::LoggingManagerInstance->InternalLogInfo(
        6,
        "PMMA has not been built with additional compatibility \
for Python, this does not effect the operation of PMMA but will change \
how PMMA and Python interact.");
#endif

    PMMA::Core::PowerSavingManagerInstance.PowerSavingModeCheckingThread = std::thread(PowerSavingUpdaterThread);

    PMMA::Registry::SecondaryDisplayIDs.reserve(255);
    PMMA::Registry::SecondaryDisplayIDs.resize(255);
    std::iota(PMMA::Registry::SecondaryDisplayIDs.begin(), PMMA::Registry::SecondaryDisplayIDs.end(), 1);
}

void PMMA_Uninitialize() {
    PMMA::Core::PowerSavingManagerInstance.stop();

    delete PMMA::Core::LoggingManagerInstance;
    PMMA::Core::LoggingManagerInstance = nullptr;
}

uint32_t GetRandomSeed() {
    std::lock_guard<std::mutex> lock(PMMA::Registry::SeedGeneratorLock);
    return PMMA::Registry::SeedDistribution(PMMA::Registry::RandomSeedGenerator);
}