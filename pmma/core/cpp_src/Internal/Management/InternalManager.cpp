#include "PMMA_Core.hpp"

void PowerSavingUpdaterThread() {
    auto& mgr = PMMA_Core::PowerSavingManagerInstance;

    std::unique_lock<std::mutex> lock(mgr.m);

    while (mgr.running) {
        // Wait for either: timeout OR stop request
        if (mgr.cv.wait_for(
                lock,
                std::chrono::seconds(mgr.updateCounter),
                [&]{
                    return !mgr.running;
                })) {
            break; // running became false
        }

        // Do the work
        CPP_General::Is_Power_Saving_Mode_Enabled(true);
    }
}