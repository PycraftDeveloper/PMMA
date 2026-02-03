#include "PMMA_Core.hpp"

bool CPP_AnimationManager::Update() {
    std::chrono::time_point<std::chrono::high_resolution_clock> CurrentTime = std::chrono::high_resolution_clock::now();

    std::chrono::duration<float> FrameTime;

    if (FirstRun) {
        FirstRun = false;
        FrameTime = std::chrono::seconds(0);
    } else {
        FrameTime = std::chrono::duration_cast<std::chrono::duration<float>>(CurrentTime - LastFrameTime);
    }

    LastFrameTime = CurrentTime;

    std::vector<CPP_AnimationCore*> FinishedAnimations;

    for (unsigned int i = 0; i < CurrentlyPlayingAnimations.size(); i++) {
        if (CurrentlyPlayingAnimations[i]->Update(FrameTime)) {
            FinishedAnimations.push_back(CurrentlyPlayingAnimations[i]);
        }
    }

    for (unsigned int i = 0; i < FinishedAnimations.size(); i++) {
        CurrentlyPlayingAnimations.erase(remove(CurrentlyPlayingAnimations.begin(), CurrentlyPlayingAnimations.end(), FinishedAnimations[i]), CurrentlyPlayingAnimations.end());
    }

    return CurrentlyPlayingAnimations.empty();
}