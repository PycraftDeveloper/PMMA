#include "Internal/AnimationManager.hpp"

#include "PMMA_Core.hpp"

PMMA::Animation::LinearAnimation::LinearAnimation(PMMA::Types::TwoD::Coordinate *NewTargetCoordinatePtr) {
    TargetCoordinatePtr = NewTargetCoordinatePtr;

    StartCoordinatePtr = new PMMA::Types::TwoD::Coordinate();
    EndCoordinatePtr = new PMMA::Types::TwoD::Coordinate();
    Logger = new PMMA::Logger();
}

PMMA::Animation::LinearAnimation::LinearAnimation::~LinearAnimation() {
    if (TargetCoordinatePtr != nullptr) {
        delete TargetCoordinatePtr;
        TargetCoordinatePtr = nullptr;
    }

    if (StartCoordinatePtr != nullptr) {
        delete StartCoordinatePtr;
        StartCoordinatePtr = nullptr;
    }

    if (EndCoordinatePtr != nullptr) {
        delete EndCoordinatePtr;
        EndCoordinatePtr = nullptr;
    }

    delete Logger;
    Logger = nullptr;
}

void PMMA::Animation::LinearAnimation::LinearAnimation::Start() {
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
    StartCoordinatePtr->GetCoordinate(start_position);
    TargetCoordinatePtr->SetCoordinate(start_position);
}

void PMMA::Animation::LinearAnimation::LinearAnimation::Stop() {
    if (!Playing) {
        return;
    }

    PMMA::Core::AnimationManagerInstance->RemoveAnimation(this);
    Playing = false;
}