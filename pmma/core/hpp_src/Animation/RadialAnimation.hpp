#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>
#include <iostream>

#include "Internal/AnimationManager.hpp"
#include "Maths.hpp"
#include "Types.hpp"

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

    inline bool Update(std::chrono::duration<float> FrameTime) override {
        // Return TRUE if animation finished
        if (Paused) {
            return false;
        }

        RunTime += FrameTime;

        uint16_t start_pos[2];
        uint16_t center_pos[2];
        StartCoordinatePtr->GetCoordinate(start_pos);
        CenterCoordinatePtr->GetCoordinate(center_pos); // Now the "center" of orbit

        // radius = start - center
        float dx = static_cast<float>(start_pos[0]) - static_cast<float>(center_pos[0]);
        float dy = static_cast<float>(start_pos[1]) - static_cast<float>(center_pos[1]);
        float radius = std::sqrt(dx * dx + dy * dy);

        // Initial angle (from center to start)
        float initial_angle = std::atan2(dy, dx);

        // Normalized progress [0,1]
        float t = RunTime.count() / Duration.count();
        if (t > 1.0f)
            t = 1.0f;

        float sweep = 2.0f * 3.14159265f * t; // one full orbit
        float angle = initial_angle + sweep;

        // Compute new position
        uint16_t new_location[2];
        new_location[0] = static_cast<uint16_t>(center_pos[0] + std::cos(angle) * radius);
        new_location[1] = static_cast<uint16_t>(center_pos[1] + std::sin(angle) * radius);

        TargetCoordinatePtr->SetCoordinate(new_location);

        if (RunTime >= Duration) {
            RunTime = Duration;

            if (!Repeat) {
                Playing = false;
                return true;
            }

            if (Repeat) {
                RunTime = std::chrono::seconds(0);
            }
        }
        return false;
    }

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