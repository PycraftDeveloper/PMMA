#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/AnimationManager.hpp"

PMMA::Animation::LinearAnimation::LinearAnimation(PMMA::Types::TwoD::Coordinate *NewTargetCoordinatePtr) {
    TargetCoordinatePtr = NewTargetCoordinatePtr;

    StartCoordinatePtr = new PMMA::Types::TwoD::Coordinate();
    EndCoordinatePtr = new PMMA::Types::TwoD::Coordinate();
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

    int16_t start_position[2];
    StartCoordinatePtr->GetCoordinate(start_position);
    TargetCoordinatePtr->SetCoordinate(start_position);
}

bool PMMA::Animation::LinearAnimation::LinearAnimation::Update(std::chrono::duration<float> FrameTime) { // Return TRUE if animation finished
    if (Paused) {
        return false;
    }

    RunTime += FrameTime;

    int16_t new_location[2];
    int16_t start_pos[2];
    int16_t end_pos[2];

    StartCoordinatePtr->GetCoordinate(start_pos);
    EndCoordinatePtr->GetCoordinate(end_pos);

    new_location[0] = (uint16_t)PMMA::Maths::Lerp(
        (float)start_pos[0], (float)end_pos[0],
        Duration.count(), RunTime.count());

    new_location[1] = (uint16_t)PMMA::Maths::Lerp(
        (float)start_pos[1], (float)end_pos[1],
        Duration.count(), RunTime.count());

    TargetCoordinatePtr->SetCoordinate(new_location);

    if (RunTime >= Duration) {
        RunTime = Duration;

        if (!(Repeat || Loop)) {
            Playing = false;
            return true;
        }

        if (Repeat) {
            RunTime = std::chrono::seconds(0);
        }

        if (Loop) { // Switch start and end
            PMMA::Types::TwoD::Coordinate *TempPtr = StartCoordinatePtr;
            StartCoordinatePtr = EndCoordinatePtr;
            EndCoordinatePtr = TempPtr;

            RunTime = std::chrono::seconds(0);
        }
    }
    return false;
}

void PMMA::Animation::LinearAnimation::LinearAnimation::Stop() {
    if (!Playing) {
        return;
    }

    PMMA::Core::AnimationManagerInstance->RemoveAnimation(this);
    Playing = false;
}

void PMMA::Animation::LinearAnimation::LinearAnimation::SetLooping(bool NewLooping) {
    if (Repeat && NewLooping) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            40,
            "This animation has already been set to repeat. The \
looping and repeating modes are mutually exclusive - meaning they cannot be \
both set - as they customize the same behaviour. We have turned off Repeat \
as that was what was previous set.");
        Repeat = false;
    }
    Loop = NewLooping;
}

void PMMA::Animation::LinearAnimation::LinearAnimation::SetRepeating(bool NewRepeating) {
    if (Loop && NewRepeating) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            40,
            "This animation has already been set to loop. The \
looping and repeating modes are mutually exclusive - meaning they cannot be \
both set - as they customize the same behaviour. We have turned off Looping \
as that was what was previous set.");
        Loop = false;
    }
    Repeat = NewRepeating;
}