#include "Internal/AnimationManager.hpp"

#include "PMMA_Core.hpp"

PMMA::Animation::RadialAnimation::RadialAnimation(PMMA::Types::DisplayCoordinate *NewTargetCoordinatePtr) {
    TargetCoordinatePtr = NewTargetCoordinatePtr;

    StartCoordinatePtr = new PMMA::Types::DisplayCoordinate();
    CenterCoordinatePtr = new PMMA::Types::DisplayCoordinate();
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

    uint16_t start_position[2];
    StartCoordinatePtr->Get(start_position);
    TargetCoordinatePtr->Set(start_position);
}

void PMMA::Animation::RadialAnimation::RadialAnimation::Stop() {
    if (!Playing) {
        return;
    }

    PMMA::Core::AnimationManagerInstance->RemoveAnimation(this);
    Playing = false;
}