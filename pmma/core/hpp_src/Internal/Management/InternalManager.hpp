#include "PMMA_Exports.hpp"

#include <chrono>
#include <thread>
#include <condition_variable>

struct PowerSavingManager {
    std::thread PowerSavingModeCheckingThread;
    std::condition_variable cv;
    std::mutex m;
    unsigned int updateCounter = 30;
    bool running = true;

    PowerSavingManager() = default;
    ~PowerSavingManager() {
        stop();
    }

    PowerSavingManager(const PowerSavingManager&) = delete;
    PowerSavingManager& operator=(const PowerSavingManager&) = delete;

    void stop() {
        {
            std::lock_guard<std::mutex> lock(m);
            running = false;
        }
        cv.notify_all();

        if (PowerSavingModeCheckingThread.joinable())
            PowerSavingModeCheckingThread.join();
    }
};

void PowerSavingUpdaterThread();