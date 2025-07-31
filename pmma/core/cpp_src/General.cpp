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
    PMMA::PMMA_Location = location;
}

void CPP_General::Set_Path_Separator(std::string& separator) {
    PMMA::PathSeparator = separator;
}

string CPP_General::Get_PMMA_Location() {
    return PMMA::PMMA_Location;
}

bool CPP_General::Is_Power_Saving_Mode_Enabled(bool ForceRefresh) {
    if (!ForceRefresh) {
        return PMMA::IsPowerSavingModeEnabled; // Return cached value if not forcing a refresh
    }

    #if defined(_WIN32)
        SYSTEM_POWER_STATUS power_status = {};
        if (GetSystemPowerStatus(&power_status)) {
            if (power_status.SystemStatusFlag == 1) {
                PMMA::IsPowerSavingModeEnabled = true;
                PMMA::PowerSavingManagerInstance.updateCounter = 30;
                return true;
            }
            if (power_status.ACLineStatus == 0 && power_status.BatteryLifePercent <= 20) {
                PMMA::IsPowerSavingModeEnabled = true;
                PMMA::PowerSavingManagerInstance.updateCounter = 30;
                return true; // Low battery test
            }
        }

        PMMA::IsPowerSavingModeEnabled = false;
        PMMA::PowerSavingManagerInstance.updateCounter = 15;
        return false;

    #elif defined(__linux__)
        const std::string powerPath = "/sys/class/power_supply/";

        try {
            for (const auto& entry : std::filesystem::directory_iterator(powerPath)) {
                if (entry.is_directory() && entry.path().filename().string().find("BAT") == 0) {
                    std::ifstream statusFile(entry.path() / "status");
                    std::string status;
                    if (statusFile >> status && status == "Discharging") {
                        PMMA::IsPowerSavingModeEnabled = true;
                        PMMA::PowerSavingManagerInstance.updateCounter = 30;
                        return true;
                    }
                }
            }
        } catch (const std::filesystem::filesystem_error& error) {
            std::cerr << "Filesystem error: " << error.what() << "\n";
        }
        PMMA::IsPowerSavingModeEnabled = false;
        PMMA::PowerSavingManagerInstance.updateCounter = 15;
        return false;

    #elif defined(__APPLE__)
        IOPMFeatureFlags flags = 0;
        kern_return_t kr = IOPMCopyFeatureFlags(kIOMasterPortDefault, &flags);
        if (kr != kIOReturnSuccess) {
            std::cerr << "Failed to get power feature flags: " << kr << "\n";
            PMMA::IsPowerSavingModeEnabled = false;
            PMMA::PowerSavingManagerInstance.updateCounter = 15;
            return false;
        }

        if (flags & kIOPMFeatureLowPowerMode) {
            PMMA::IsPowerSavingModeEnabled = true;
            PMMA::PowerSavingManagerInstance.updateCounter = 30;
            return true; // Low power mode is enabled
        }
        PMMA::IsPowerSavingModeEnabled = false;
        PMMA::PowerSavingManagerInstance.updateCounter = 15;
        return false;

    #else
        std::cout << "Unknown platform for power saving mode check." << std::endl;
        PMMA::IsPowerSavingModeEnabled = false;
        PMMA::PowerSavingManagerInstance.running = false;
        PMMA::PowerSavingManagerInstance.updateCounter = 5;
        return false;
    #endif
}
