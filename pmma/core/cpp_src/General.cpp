#if defined(_WIN32)
    #include <Windows.h>
#elif defined(__linux__)
    #include <fstream>
    #include <filesystem>
#endif

#include <string>

#include <bx/platform.h>
#include <bgfx/bgfx.h>

#include "PMMA_Core.hpp"
#include "General.hpp"
#include "Display.hpp"
#include "Internal/Management/LoggingManager.hpp"
#include "Internal/Management/InternalManager.hpp"

#include "Constants.hpp"

using namespace std;

string CPP_General::Get_PMMA_Location() {
    return PMMA_Registry::PMMA_Location;
}

bool CPP_General::Is_Power_Saving_Mode_Enabled(bool ForceRefresh) {
    if (!ForceRefresh) {
        return PMMA_Registry::IsPowerSavingModeEnabled; // Return cached value if not forcing a refresh
    }

    #if defined(_WIN32)
        SYSTEM_POWER_STATUS power_status = {};
        if (GetSystemPowerStatus(&power_status)) {
            if (power_status.SystemStatusFlag == 1) {
                if (!PMMA_Registry::IsPowerSavingModeEnabled) {
                    PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                        1,
                        "Your device is running in power saving mode.", true);
                }
                PMMA_Registry::IsPowerSavingModeEnabled = true;
                PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
                if (!PMMA_Registry::UserDefinedShapeQuality) {
                    PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY * 0.5f;
                }
                return true;
            }
            if (power_status.ACLineStatus == 0 && power_status.BatteryLifePercent <= 20) {
                if (!PMMA_Registry::IsPowerSavingModeEnabled) {
                    PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                        1,
                        "Your device is running in power saving mode.", true);
                }
                PMMA_Registry::IsPowerSavingModeEnabled = true;
                PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
                if (!PMMA_Registry::UserDefinedShapeQuality) {
                    PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY * 0.5f;
                }
                return true; // Low battery test
            }
        }

        if (PMMA_Registry::IsPowerSavingModeEnabled) {
            PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                2,
                "Your device is not running in power saving mode.", true);
        }
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
        if (!PMMA_Registry::UserDefinedShapeQuality) {
            PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY;
        }
        return false;

    #elif defined(__linux__)
        const std::string powerPath = "/sys/class/power_supply/";

        try {
            for (const auto& entry : std::filesystem::directory_iterator(powerPath)) {
                if (entry.is_directory() && entry.path().filename().string().find("BAT") == 0) {
                    std::ifstream statusFile(entry.path() / "status");
                    std::string status;
                    if (statusFile >> status && status == "Discharging") {
                        if (!PMMA_Registry::IsPowerSavingModeEnabled) {
                            PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                                1,
                                "Your device is running in power saving mode.", true);
                        }
                        PMMA_Registry::IsPowerSavingModeEnabled = true;
                        PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
                        if (!PMMA_Registry::UserDefinedShapeQuality) {
                            PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY * 0.5f;
                        }
                        return true;
                    }
                }
            }
        } catch (const std::filesystem::filesystem_error& error) {
            std::cerr << "Filesystem error: " << error.what() << "\n";
        }
        if (PMMA_Registry::IsPowerSavingModeEnabled) {
            PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                2,
                "Your device is not running in power saving mode.", true);
        }
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
        if (!PMMA_Registry::UserDefinedShapeQuality) {
            PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY;
        }
        return false;

    #else
        PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                7,
                "Your platform is not supported for power saving mode \
checking using PMMA.");

        if (PMMA_Registry::IsPowerSavingModeEnabled) {
            PMMA_Core::LoggingManagerInstance->InternalLogInfo(
                2,
                "Your device is not running in power saving mode.", true);
        }
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.running = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 5;
        if (!PMMA_Registry::UserDefinedShapeQuality) {
            PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY;
        }
        return false;
    #endif
}

bool CPP_General::Is_DebugModeEnabled() {
    return PMMA_Registry::IsDebuggingModeEnabled;
}

void CPP_General::Set_DebugModeEnabled(bool DebugMode) {
    PMMA_Registry::IsDebuggingModeEnabled = DebugMode;
}

bool CPP_General::IsWindowCreated() {
    return (PMMA_Core::DisplayInstance != nullptr && PMMA_Core::DisplayInstance->IsWindowCreated());
}

bool CPP_General::IsApplicationRunning() {
    return PMMA_Registry::IsApplicationRunning;
}

bool CPP_General::IsEscapeKeyToCloseWindow() {
    return PMMA_Registry::EscapeKeyShouldCloseWindow;
}

void CPP_General::SetEscapeKeyToCloseWindow(bool EscapeKeyShouldCloseWindow) {
    PMMA_Registry::EscapeKeyShouldCloseWindow = EscapeKeyShouldCloseWindow;
    PMMA_Registry::UserSetEscapeKeyShouldCloseWindow = true;
}

bool CPP_General::IsF11KeyToToggleFullscreen() {
    return PMMA_Registry::F11KeyShouldToggleFullScreen;
}

void CPP_General::SetF11KeyToToggleFullscreen(bool F11KeyShouldToggleFullScreen) {
    PMMA_Registry::F11KeyShouldToggleFullScreen = F11KeyShouldToggleFullScreen;
}

string CPP_General::GetCurrent_PMMA_Version() {
    return PMMA_Registry::Current_PMMA_Version;
}

string CPP_General::GetLatest_PMMA_Version() {
    return PMMA_Registry::Latest_PMMA_Version;
}

void CPP_General::SetLatest_PMMA_Version(string latest_version) {
    PMMA_Registry::Latest_PMMA_Version = latest_version;
}

string PadVersionString(string item) {
    unsigned int string_size = item.length();
    string padded_string = "";
    for (unsigned int i = 0; i < 4 - string_size; i++) {
        padded_string += "0";
    }
    padded_string += item;
    return padded_string;
}

bool CPP_General::IsUpdateAvailable() {
    string padded_current_version;
    string split_current_version[3];
    unsigned int split_count = 0;
    for (unsigned int i = 0; i < PMMA_Registry::Current_PMMA_Version.length(); i++) {
        if (PMMA_Registry::Current_PMMA_Version[i] == '.') {
            split_count++;
            continue;
        }
        split_current_version[split_count] += PMMA_Registry::Current_PMMA_Version[i];
    }

    for (unsigned int i = 0; i < 3; i++) {
        padded_current_version += PadVersionString(split_current_version[i]);
    }

    string padded_latest_version;
    string split_latest_version[3];
    split_count = 0;
    for (unsigned int i = 0; i < PMMA_Registry::Latest_PMMA_Version.length(); i++) {
        if (PMMA_Registry::Latest_PMMA_Version[i] == '.') {
            split_count++;
            continue;
        }
        split_latest_version[split_count] += PMMA_Registry::Latest_PMMA_Version[i];
    }

    for (unsigned int i = 0; i < 3; i++) {
        padded_latest_version += PadVersionString(split_latest_version[i]);
    }

    uint64_t numerical_current_version = std::stoull(padded_current_version);
    uint64_t numerical_latest_version = std::stoull(padded_latest_version);

    if (numerical_current_version > numerical_latest_version) {
        PMMA_Core::LoggingManagerInstance->InternalLogDebug(
            22,
            "Thank you for using a pre-released version of PMMA! Please \
note that there will likely be issues or missing/broken features as we work \
towards creating the next version of the API. If you find any bugs or think \
something could be improved it would be invaluable for you to let us know \
by creating a new issue here: 'https://github.com/PycraftDeveloper/PMMA/issues'.");
    }

    return numerical_current_version < numerical_latest_version;
}

double CPP_General::GetApplicationStartTime() {
    return PMMA_Registry::StartupTime.time_since_epoch().count() / 1000000000.0;
}

double CPP_General::GetApplicationRunTime() {
    chrono::high_resolution_clock::time_point current_time = chrono::high_resolution_clock::now();
    return (current_time - PMMA_Registry::StartupTime).count() / 1000000000.0;
}

float CPP_General::GetShapeQuality() {
    return PMMA_Registry::CurrentShapeQuality;
}

void CPP_General::SetShapeQuality(float ShapeQuality) {
    if (ShapeQuality > CPP_Constants::SHAPE_QUALITY) {
        PMMA_Core::LoggingManagerInstance->InternalLogWarn(
            41,
            "You have set the shape quality to a very high value of: " +
            to_string(ShapeQuality) +
            ". This is typically not necessary and may cause performance \
issues. Please consider setting the shape quality to a lower value."
        );
    }
    PMMA_Registry::CurrentShapeQuality = ShapeQuality;
    PMMA_Registry::UserDefinedShapeQuality = true;
}

void CPP_General::Let_PMMA_ControlShapeQuality() {
    if (PMMA_Registry::IsPowerSavingModeEnabled) {
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY * 0.5f;
    } else {
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::SHAPE_QUALITY;
    }
    PMMA_Registry::UserDefinedShapeQuality = false;
}

void CPP_General::SetLocale(string locale) {
    PMMA_Registry::Locale = locale;
}

string CPP_General::GetLocale() {
    return PMMA_Registry::Locale;
}

string CPP_General::GetOperatingSystem() {
    #if BX_PLATFORM_ANDROID
        return CPP_Constants::OperatingSystems::ANDROID;
    #elif BX_PLATFORM_BSD
        return CPP_Constants::OperatingSystems::BSD;
    #elif BX_PLATFORM_EMSCRIPTEN
        return CPP_Constants::OperatingSystems::EMSCRIPTEN;
    #elif BX_PLATFORM_HAIKU
        return CPP_Constants::OperatingSystems::HAIKU;
    #elif BX_PLATFORM_HURD
        return CPP_Constants::OperatingSystems::HURD;
    #elif BX_PLATFORM_IOS
        return CPP_Constants::OperatingSystems::IOS;
    #elif BX_PLATFORM_LINUX
        return CPP_Constants::OperatingSystems::LINUX;
    #elif BX_PLATFORM_NX
        return CPP_Constants::OperatingSystems::NX;
    #elif BX_PLATFORM_OSX
        return CPP_Constants::OperatingSystems::OSX;
    #elif BX_PLATFORM_PS4
        return CPP_Constants::OperatingSystems::PS4;
    #elif BX_PLATFORM_PS5
        return CPP_Constants::OperatingSystems::PS5;
    #elif BX_PLATFORM_VISIONOS
        return CPP_Constants::OperatingSystems::VISIONOS;
    #elif BX_PLATFORM_WINDOWS
        return CPP_Constants::OperatingSystems::WINDOWS;
    #elif BX_PLATFORM_WINRT
        return CPP_Constants::OperatingSystems::WINRT;
    #elif BX_PLATFORM_XBOXONE
        return CPP_Constants::OperatingSystems::XBOXONE;
    #else
        return CPP_Constants::OperatingSystems::UNKNOWN;
    #endif
}

string CPP_General::GetGraphicsBackend() {
    bgfx::RendererType::Enum backend = bgfx::getRendererType();

    switch (backend) {
        case bgfx::RendererType::Noop:
            return CPP_Constants::GraphicsBackends::NO_RENDERER;
        case bgfx::RendererType::Direct3D11:
            return CPP_Constants::GraphicsBackends::DIRECT3D11;
        case bgfx::RendererType::Direct3D12:
            return CPP_Constants::GraphicsBackends::DIRECT3D12;
        case bgfx::RendererType::Gnm:
            return CPP_Constants::GraphicsBackends::GNM;
        case bgfx::RendererType::Metal:
            return CPP_Constants::GraphicsBackends::METAL;
        case bgfx::RendererType::Nvn:
            return CPP_Constants::GraphicsBackends::NVN;
        case bgfx::RendererType::OpenGLES:
            return CPP_Constants::GraphicsBackends::OPENGL_ES;
        case bgfx::RendererType::OpenGL:
            return CPP_Constants::GraphicsBackends::OPENGL;
        case bgfx::RendererType::Vulkan:
            return CPP_Constants::GraphicsBackends::VULKAN;
        default:
            return CPP_Constants::GraphicsBackends::UNKNOWN;
    }
}