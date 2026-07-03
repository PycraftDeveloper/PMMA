#include "Internal/AnimationManager.hpp"

#include "PMMA_Core.hpp"

CPP_RadialAnimation::CPP_RadialAnimation(PMMA::Types::DisplayCoordinate *NewTargetCoordinatePtr) {
    TargetCoordinatePtr = NewTargetCoordinatePtr;

    StartCoordinatePtr = new PMMA::Types::DisplayCoordinate();
    CenterCoordinatePtr = new PMMA::Types::DisplayCoordinate();
}

CPP_RadialAnimation::~CPP_RadialAnimation() {
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

void CPP_RadialAnimation::Start() {
    if (Playing) {
        return;
    }

    Playing = true;

    if (PMMA::Core::AnimationManagerInstance == nullptr) {
        PMMA::Core::AnimationManagerInstance = new CPP_AnimationManager();
    }

    PMMA::Core::AnimationManagerInstance->AddAnimation(this);

    StartTime = std::chrono::high_resolution_clock::now();
    RunTime = std::chrono::seconds(0);

    uint16_t start_position[2];
    StartCoordinatePtr->Get(start_position);
    TargetCoordinatePtr->Set(start_position);
}

void CPP_RadialAnimation::Stop() {
    if (!Playing) {
        return;
    }

    PMMA::Core::AnimationManagerInstance->RemoveAnimation(this);
    Playing = false;
}