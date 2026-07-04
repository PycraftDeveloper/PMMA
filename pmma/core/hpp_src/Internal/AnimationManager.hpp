#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>
#include <variant>
#include <vector>

namespace PMMA::Internal {
class EXPORT AnimationCore {
public:
    virtual ~AnimationCore() {}

    inline bool virtual Update(std::chrono::duration<float> FrameTime) {
        return false;
    }
};

class AnimationManager {
private:
    std::vector<PMMA::Internal::AnimationCore *> CurrentlyPlayingAnimations;

    std::chrono::time_point<std::chrono::high_resolution_clock> LastFrameTime;

    bool FirstRun = true;

public:
    bool Update();

    void AddAnimation(PMMA::Internal::AnimationCore *animation) {
        CurrentlyPlayingAnimations.push_back(animation);
    }

    void RemoveAnimation(PMMA::Internal::AnimationCore *animation) {
        for (unsigned int i = 0; i < CurrentlyPlayingAnimations.size(); i++) {
            if (CurrentlyPlayingAnimations[i] == animation) {
                CurrentlyPlayingAnimations.erase(CurrentlyPlayingAnimations.begin() + i);
                break;
            }
        }
    }
};
} // namespace PMMA::Internal