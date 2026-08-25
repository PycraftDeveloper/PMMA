#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <chrono>
#include <iostream>

#include "Internal/AnimationManager.hpp"

namespace PMMA::Types::TwoD {
class Coordinate;
};

namespace PMMA::Animation {
class EXPORT RadialAnimation : public PMMA::Internal::AnimationCore {
public:
    PMMA::Types::TwoD::Coordinate *TargetCoordinatePtr;
    PMMA::Types::TwoD::Coordinate *StartCoordinatePtr;
    PMMA::Types::TwoD::Coordinate *CenterCoordinatePtr;

    std::chrono::time_point<std::chrono::high_resolution_clock> StartTime;
    std::chrono::duration<float> Duration;
    std::chrono::duration<float> RunTime;

    bool Playing = false;
    bool Paused = false;
    bool Repeat = false;

    RadialAnimation(PMMA::Types::TwoD::Coordinate *NewTargetCoordinatePtr);

    ~RadialAnimation();

    bool Update(std::chrono::duration<float> FrameTime) override;

    void Start();

    void Stop();

    inline void Pause() {
        Paused = true;
    }

    inline void Resume() {
        Paused = false;
    }

    inline void SetDuration(float NewDuration) {
        Duration = std::chrono::duration<float>(NewDuration);
    }

    inline float GetDuration() {
        return Duration.count();
    }

    inline float GetRemainingDuration() {
        return (Duration - RunTime).count();
    }

    inline bool IsPlaying() {
        return Playing;
    }

    inline bool IsPaused() {
        return Paused;
    }

    inline void SetRepeating(bool NewRepeating) {
        Repeat = NewRepeating;
    }

    inline bool IsRepeating() {
        return Repeat;
    }
};
}