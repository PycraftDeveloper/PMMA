#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <variant>
#include <chrono>

class EXPORT CPP_AnimationCore {
    public:
        virtual ~CPP_AnimationCore() {}

        inline bool virtual Update(std::chrono::duration<float> FrameTime) {
            return false;
        }
};

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