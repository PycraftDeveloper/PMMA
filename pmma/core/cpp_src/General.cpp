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

bool CPP_General::Is_Power_Saving_Mode_Enabled() {
    #if defined(_WIN32)
        SYSTEM_POWER_STATUS power_status = {};
        if (GetSystemPowerStatus(&power_status)) {
            if (power_status.SystemStatusFlag == 1) {
                return true;
            }
            if (power_status.ACLineStatus == 0 && power_status.BatteryLifePercent <= 20) {
                return true; // Low battery test
            }
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
                        return true;
                    }
                }
            }
        } catch (const std::filesystem::filesystem_error& error) {
            std::cerr << "Filesystem error: " << error.what() << "\n";
        }
        return false;

    #elif defined(__APPLE__)
        IOPMFeatureFlags flags = 0;
        kern_return_t kr = IOPMCopyFeatureFlags(kIOMasterPortDefault, &flags);
        if (kr != kIOReturnSuccess) {
            std::cerr << "Failed to get power feature flags: " << kr << "\n";
            return false;
        }
        return (flags & kIOPMFeatureLowPowerMode) != 0;

    #else
        std::cout << "Unknown platform for power saving mode check." << std::endl;
        return false;
    #endif
}
