#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>

class EXPORT CPP_AnimationCore {
    public:
        virtual ~CPP_AnimationCore() {}

        inline bool virtual Update(std::chrono::duration<float> FrameTime) {
            return false;
        }
};