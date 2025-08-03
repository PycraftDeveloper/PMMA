#include "PMMA_Exports.hpp"

#include <chrono>
#include <thread>
#include <condition_variable>

struct PowerSavingManager {
    std::thread PowerSavingModeCheckingThread;
    std::condition_variable cv;
    unsigned int updateCounter = 30; // Update every 30 seconds
    bool running = true;
};

void PowerSavingUpdaterThread();