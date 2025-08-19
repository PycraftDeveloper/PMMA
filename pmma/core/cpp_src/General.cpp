#if defined(_WIN32)
    #include <Windows.h>

#elif defined(__linux__)
    #include <fstream>
    #include <filesystem>

#elif defined(__APPLE__)
    #include <IOKit/IOKitLib.h>
    #include <IOKit/pwr_mgt/IOPMLib.h>
#endif

#include "PMMA_Core.hpp"

void CPP_General::Set_PMMA_Location(std::string location) {
    PMMA_Registry::PMMA_Location = location;
}

void CPP_General::Set_Path_Separator(std::string separator) {
    PMMA_Registry::PathSeparator = separator;
}

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
                    PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                        1,
                        "Your device is running in power saving mode.", true);
                }
                PMMA_Registry::IsPowerSavingModeEnabled = true;
                PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
                PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality * 0.5f;
                return true;
            }
            if (power_status.ACLineStatus == 0 && power_status.BatteryLifePercent <= 20) {
                if (!PMMA_Registry::IsPowerSavingModeEnabled) {
                    PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                        1,
                        "Your device is running in power saving mode.", true);
                }
                PMMA_Registry::IsPowerSavingModeEnabled = true;
                PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
                PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality * 0.5f;
                return true; // Low battery test
            }
        }

        if (PMMA_Registry::IsPowerSavingModeEnabled) {
            PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                2,
                "Your device is not running in power saving mode.", true);
        }
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality;
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
                            PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                                1,
                                "Your device is running in power saving mode.", true);
                        }
                        PMMA_Registry::IsPowerSavingModeEnabled = true;
                        PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
                        PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality * 0.5f;
                        return true;
                    }
                }
            }
        } catch (const std::filesystem::filesystem_error& error) {
            std::cerr << "Filesystem error: " << error.what() << "\n";
        }
        if (PMMA_Registry::IsPowerSavingModeEnabled) {
            PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                2,
                "Your device is not running in power saving mode.", true);
        }
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality;
        return false;

    #elif defined(__APPLE__)
        IOPMFeatureFlags flags = 0;
        kern_return_t kr = IOPMCopyFeatureFlags(kIOMasterPortDefault, &flags);
        if (kr != kIOReturnSuccess) {
            std::cerr << "Failed to get power feature flags: " << kr << "\n";
            if (PMMA_Registry::IsPowerSavingModeEnabled) {
                PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                    2,
                    "Your device is not running in power saving mode.", true);
            }
            PMMA_Registry::IsPowerSavingModeEnabled = false;
            PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
            PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality;
            return false;
        }

        if (flags & kIOPMFeatureLowPowerMode) {
            if (!PMMA_Registry::IsPowerSavingModeEnabled) {
                PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                    1,
                    "Your device is running in power saving mode.", true);
            }
            PMMA_Registry::IsPowerSavingModeEnabled = true;
            PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
            PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality * 0.5f;
            return true; // Low power mode is enabled
        }
        if (PMMA_Registry::IsPowerSavingModeEnabled) {
            PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                2,
                "Your device is not running in power saving mode.", true);
        }
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality;
        return false;

    #else
        PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                7,
                "Your platform is not supported for power saving mode \
checking using PMMA.");

        if (PMMA_Registry::IsPowerSavingModeEnabled) {
            PMMA_Core::InternalLoggerInstance->InternalLogDebug(
                2,
                "Your device is not running in power saving mode.", true);
        }
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.running = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 5;
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality;
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
        PMMA_Core::InternalLoggerInstance->InternalLogDebug(
            22,
            "Thank you for using a pre-released version of PMMA! Please \
note that there will likely be issues or missing/broken features as we work \
towards creating the next version of the API. If you find any bugs or think \
something could be improved it would be invaluable for you to let us know \
by creating a new issue here: 'https://github.com/PycraftDeveloper/PMMA/issues'.");
    }

    return numerical_current_version < numerical_latest_version;
}