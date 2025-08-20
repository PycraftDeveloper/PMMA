#pragma once

#include <vector>
#include <variant>

#include "Animation/AnimationCore.hpp"

class CPP_AnimationManager {
    private:
        std::vector<CPP_AnimationCore*> CurrentlyPlayingAnimations;

        std::chrono::time_point<std::chrono::high_resolution_clock> LastFrameTime;

        bool FirstRun = true;

    public:
        bool Update();

        void AddAnimation(CPP_AnimationCore* animation) {
            CurrentlyPlayingAnimations.push_back(animation);
        }

        void RemoveAnimation(CPP_AnimationCore* animation) {
            for (unsigned int i = 0; i < CurrentlyPlayingAnimations.size(); i++) {
                if (CurrentlyPlayingAnimations[i] == animation) {
                    CurrentlyPlayingAnimations.erase(CurrentlyPlayingAnimations.begin() + i);
                    break;
                }
            }
        }
};