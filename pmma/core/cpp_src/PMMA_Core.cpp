#include <filesystem>
#include <numeric>

#define STB_IMAGE_IMPLEMENTATION
#include <STB/stb_image.h>
#include <bgfx/bgfx.h>

#include "Internal/PowerSavingManager.hpp"
#include "PMMA_Core.hpp"

namespace PMMA::Core {
PMMA::Display *ActiveDisplayInstance = nullptr;
PMMA::Display *MasterDisplayInstance = nullptr;

PMMA::Passport *PassportInstance = nullptr;
PMMA::Internal::LoggingManager *LoggingManagerInstance = nullptr;

PMMA::Internal::PowerSavingManager PowerSavingManagerInstance;

PMMA::Internal::AnimationManager *AnimationManagerInstance = nullptr;

PMMA::FastRandom *RandomGenerator = new PMMA::FastRandom();

std::vector<PMMA::Internal::Events::InternalController *> InternalControllerEventInstances;
std::vector<PMMA::Events::Controller *> ControllerEvent_Instances;

PMMA::Internal::Events::InternalControllerManager *ControllerManagerInstance = nullptr;
std::map<std::string, PMMA::Internal::TextureProperty> TextureCatalogue;
} // namespace PMMA::Core

namespace PMMA::Registry {
std::vector<unsigned char> SecondaryDisplayIDs;

std::string PMMA_Location = "";
std::string PathSeparator = std::string(1, std::filesystem::path::preferred_separator);
std::string Current_PMMA_Version = "5.1.0";
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

unsigned int RollingViewID;
unsigned int MaxViewID = 0;

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
} // namespace PMMA::Registry

namespace PMMA {
void Initialize(std::string location) {
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

    PMMA::Core::PowerSavingManagerInstance.PowerSavingModeCheckingThread = std::thread(
        &PMMA::Internal::PowerSavingManager::PowerSavingUpdaterThread,
        &PMMA::Core::PowerSavingManagerInstance);

    PMMA::Registry::SecondaryDisplayIDs.reserve(255);
    PMMA::Registry::SecondaryDisplayIDs.resize(255);
    std::iota(PMMA::Registry::SecondaryDisplayIDs.begin(), PMMA::Registry::SecondaryDisplayIDs.end(), 1);
}

void Uninitialize() {
    PMMA::Core::PowerSavingManagerInstance.stop();

    delete PMMA::Core::LoggingManagerInstance;
    PMMA::Core::LoggingManagerInstance = nullptr;
}
} // namespace PMMA