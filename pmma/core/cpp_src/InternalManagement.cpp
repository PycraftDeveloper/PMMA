#include "PMMA_Core.hpp"

void PowerSavingUpdaterThread() {
    while (PMMA::PowerSavingManagerInstance.running) {
        for (int i = 0; i < PMMA::PowerSavingManagerInstance.updateCounter; i += 5) {
            std::this_thread::sleep_for(std::chrono::seconds(5));
            if (!PMMA::PowerSavingManagerInstance.running) {
                break;
            }
        }

        if (!PMMA::PowerSavingManagerInstance.running) {
            break;
        }

        CPP_General::Is_Power_Saving_Mode_Enabled(true);
    }
}