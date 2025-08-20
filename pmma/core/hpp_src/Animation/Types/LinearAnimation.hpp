#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>
#include <iostream>

#include "Animation/AnimationCore.hpp"
#include "NumberFormats.hpp"
#include "AdvancedMathematics.hpp"
#include "Logger.hpp"

class EXPORT CPP_LinearAnimation: public CPP_AnimationCore {
    public:
        CPP_DisplayCoordinateFormat* TargetCoordinatePtr;
        CPP_DisplayCoordinateFormat* StartCoordinatePtr;
        CPP_DisplayCoordinateFormat* EndCoordinatePtr;
        CPP_Logger* Logger;

        std::chrono::time_point<std::chrono::high_resolution_clock> StartTime;
        std::chrono::duration<float> Duration;
        std::chrono::duration<float> RunTime;

        bool Playing = false;
        bool Paused = false;
        bool Loop = false;
        bool Repeat = false;

        CPP_LinearAnimation(CPP_DisplayCoordinateFormat* NewTargetCoordinatePtr);

        ~CPP_LinearAnimation();

        inline bool Update(std::chrono::duration<float> FrameTime) override { // Return TRUE if animation finished
            if (Paused) {
                return false;
            }

            RunTime += FrameTime;

            unsigned int new_location[2];
            unsigned int start_pos[2];
            unsigned int end_pos[2];

            StartCoordinatePtr->Get(start_pos);
            EndCoordinatePtr->Get(end_pos);

            new_location[0] = (unsigned int)CPP_AdvancedMathematics::Lerp(
                (float)start_pos[0], (float)end_pos[0],
                Duration.count(), RunTime.count());

            new_location[1] = (unsigned int)CPP_AdvancedMathematics::Lerp(
                (float)start_pos[1], (float)end_pos[1],
                Duration.count(), RunTime.count());

            TargetCoordinatePtr->Set(new_location);

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
                    CPP_DisplayCoordinateFormat* TempPtr = StartCoordinatePtr;
                    StartCoordinatePtr = EndCoordinatePtr;
                    EndCoordinatePtr = TempPtr;

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

        inline void SetLooping(bool NewLooping) {
            if (Repeat && NewLooping) {
                Logger->InternalLogWarn(
                    40,
                    "This animation has already been set to repeat. The \
looping and repeating modes are mutually exclusive - meaning they cannot be \
both set - as they customize the same behaviour. We have turned off Repeat \
as that was what was previous set."
                );
                Repeat = false;
            }
            Loop = NewLooping;
        }

        inline bool IsLooping() {
            return Loop;
        }

        inline void SetRepeating(bool NewRepeating) {
            if (Loop && NewRepeating) {
                Logger->InternalLogWarn(
                    40,
                    "This animation has already been set to loop. The \
looping and repeating modes are mutually exclusive - meaning they cannot be \
both set - as they customize the same behaviour. We have turned off Looping \
as that was what was previous set."
                );
                Loop = false;
            }
            Repeat = NewRepeating;
        }

        inline bool IsRepeating() {
            return Repeat;
        }
};