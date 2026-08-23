#include "Internal/AnimationManager.hpp"

#define PMMA_ALLOW_UMBRELLA_HEADER
#include "PMMA_Core.hpp"

PMMA::Animation::RadialAnimation::RadialAnimation(PMMA::Types::TwoD::Coordinate *NewTargetCoordinatePtr) {
    TargetCoordinatePtr = NewTargetCoordinatePtr;

    StartCoordinatePtr = new PMMA::Types::TwoD::Coordinate();
    CenterCoordinatePtr = new PMMA::Types::TwoD::Coordinate();
}

PMMA::Animation::RadialAnimation::~RadialAnimation() {
    if (TargetCoordinatePtr != nullptr) {
        delete TargetCoordinatePtr;
        TargetCoordinatePtr = nullptr;
    }

    if (StartCoordinatePtr != nullptr) {
        delete StartCoordinatePtr;
        StartCoordinatePtr = nullptr;
    }

    if (CenterCoordinatePtr != nullptr) {
        delete CenterCoordinatePtr;
        CenterCoordinatePtr = nullptr;
    }
}

void PMMA::Animation::RadialAnimation::RadialAnimation::Start() {
    if (Playing) {
        return;
    }

    Playing = true;

    if (PMMA::Core::AnimationManagerInstance == nullptr) {
        PMMA::Core::AnimationManagerInstance = new PMMA::Internal::AnimationManager();
    }

    PMMA::Core::AnimationManagerInstance->AddAnimation(this);

    StartTime = std::chrono::high_resolution_clock::now();
    RunTime = std::chrono::seconds(0);

    int16_t start_position[2];
    StartCoordinatePtr->GetCoordinate(start_position);
    TargetCoordinatePtr->SetCoordinate(start_position);
}

bool PMMA::Animation::RadialAnimation::RadialAnimation::Update(std::chrono::duration<float> FrameTime) {
    // Return TRUE if animation finished
    if (Paused) {
        return false;
    }

    RunTime += FrameTime;

    int16_t start_pos[2];
    int16_t center_pos[2];
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
    int16_t new_location[2];
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

void PMMA::Animation::RadialAnimation::RadialAnimation::Stop() {
    if (!Playing) {
        return;
    }

    PMMA::Core::AnimationManagerInstance->RemoveAnimation(this);
    Playing = false;
}