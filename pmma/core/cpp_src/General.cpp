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

void CPP_General::Set_PMMA_Location(std::string& location) {
    PMMA_Registry::PMMA_Location = location;
}

void CPP_General::Set_Path_Separator(std::string& separator) {
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
                PMMA_Registry::IsPowerSavingModeEnabled = true;
                PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
                PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality * 0.5f;
                return true;
            }
            if (power_status.ACLineStatus == 0 && power_status.BatteryLifePercent <= 20) {
                PMMA_Registry::IsPowerSavingModeEnabled = true;
                PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
                PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality * 0.5f;
                return true; // Low battery test
            }
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
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality;
        return false;

    #elif defined(__APPLE__)
        IOPMFeatureFlags flags = 0;
        kern_return_t kr = IOPMCopyFeatureFlags(kIOMasterPortDefault, &flags);
        if (kr != kIOReturnSuccess) {
            std::cerr << "Failed to get power feature flags: " << kr << "\n";
            PMMA_Registry::IsPowerSavingModeEnabled = false;
            PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
            PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality;
            return false;
        }

        if (flags & kIOPMFeatureLowPowerMode) {
            PMMA_Registry::IsPowerSavingModeEnabled = true;
            PMMA_Core::PowerSavingManagerInstance.updateCounter = 30;
            PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality * 0.5f;
            return true; // Low power mode is enabled
        }
        PMMA_Registry::IsPowerSavingModeEnabled = false;
        PMMA_Core::PowerSavingManagerInstance.updateCounter = 15;
        PMMA_Registry::CurrentShapeQuality = CPP_Constants::ShapeQuality;
        return false;

    #else
        std::cout << "Unknown platform for power saving mode check." << std::endl;
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