#include "Internal/Management/AnimationManager.hpp"

#include "PMMA_Core.hpp"

CPP_LinearAnimation::CPP_LinearAnimation(CPP_DisplayCoordinateFormat* NewTargetCoordinatePtr) {
    TargetCoordinatePtr = NewTargetCoordinatePtr;

    StartCoordinatePtr = new CPP_DisplayCoordinateFormat();
    EndCoordinatePtr = new CPP_DisplayCoordinateFormat();
    Logger = new CPP_Logger();
}

CPP_LinearAnimation::~CPP_LinearAnimation() {
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

void CPP_LinearAnimation::Start() {
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

void CPP_LinearAnimation::Stop() {
    if (!Playing) {
        return;
    }

    PMMA_Core::AnimationManagerInstance->RemoveAnimation(this);
    Playing = false;
}