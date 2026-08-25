#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/PowerSavingManager.hpp"

void PMMA::Internal::PowerSavingManager::PowerSavingUpdaterThread() {
    PMMA::Internal::PowerSavingManager &mgr = *PMMA::Core::PowerSavingManagerInstance;

    std::unique_lock<std::mutex> lock(mgr.m);

    while (mgr.running) {
        // Wait for either: timeout OR stop request
        if (mgr.cv.wait_for(
                lock,
                std::chrono::seconds(mgr.updateCounter),
                [&] {
                    return !mgr.running;
                })) {
            break; // running became false
        }

        // Do the work
        PMMA::General::Is_Power_Saving_Mode_Enabled(true);
    }
}