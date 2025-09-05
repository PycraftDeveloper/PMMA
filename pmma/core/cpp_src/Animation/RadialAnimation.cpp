#include "Internal/Management/AnimationManager.hpp"

#include "PMMA_Core.hpp"

CPP_RadialAnimation::CPP_RadialAnimation(CPP_DisplayCoordinateFormat* NewTargetCoordinatePtr) {
    TargetCoordinatePtr = NewTargetCoordinatePtr;

    StartCoordinatePtr = new CPP_DisplayCoordinateFormat();
    CenterCoordinatePtr = new CPP_DisplayCoordinateFormat();
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

    if (PMMA_Core::AnimationManagerInstance == nullptr) {
        PMMA_Core::AnimationManagerInstance = new CPP_AnimationManager();
    }

    PMMA_Core::AnimationManagerInstance->AddAnimation(this);

    StartTime = chrono::high_resolution_clock::now();
    RunTime = chrono::seconds(0);

    unsigned int start_position[2];
    StartCoordinatePtr->Get(start_position);
    TargetCoordinatePtr->Set(start_position);
}

void CPP_RadialAnimation::Stop() {
    if (!Playing) {
        return;
    }

    PMMA_Core::AnimationManagerInstance->RemoveAnimation(this);
    Playing = false;
}