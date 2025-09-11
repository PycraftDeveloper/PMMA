#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <array>
#include <ctime>

#include "Logger.hpp"

class EXPORT CPP_BasicColorConverter {
    protected:
        CPP_Logger* Logger;

        uint8_t InternalColor[4] = {0, 0, 0, 0}; // Default is black with full opacity

        bool IsSet = false;
        bool Changed = true;
        bool InternalChanged = true;

    public:
        CPP_BasicColorConverter() {
            Logger = new CPP_Logger();
        }

        ~CPP_BasicColorConverter() {
            delete Logger;
            Logger = nullptr;
        }

        inline bool GetSet() {
            return IsSet;
        }

        inline bool GetChangedToggle() {
            bool OldChanged = Changed;
            Changed = false;
            return OldChanged;
        }

        inline bool GetInternalChangedToggle() {
            bool OldChanged = InternalChanged;
            InternalChanged = false;
            return OldChanged;
        }

        inline void Set_RGBA(uint8_t* in_color) {
            bool Different = false;
            for (int i = 0; i < 4; i++) {
                if (in_color[i] != InternalColor[i]) {
                    Different = true;
                    break;
                }
            }
            if (Different) {
                Changed = true;
                InternalChanged = true;
                InternalColor[0] = in_color[0];
                InternalColor[1] = in_color[1];
                InternalColor[2] = in_color[2];
                InternalColor[3] = in_color[3];
            }

            IsSet = true;
        }

        inline void Set_RGB(uint8_t* in_color) {
            Logger->InternalLogDebug(
                9,
                "The alpha channel is automatically set to opaque."
            );

            bool Different = false;
            for (int i = 0; i < 3; i++) {
                if (in_color[i] != InternalColor[i]) {
                    Different = true;
                    break;
                }
            }
            if (Different) {
                Changed = true;
                InternalChanged = true;
                InternalColor[0] = in_color[0];
                InternalColor[1] = in_color[1];
                InternalColor[2] = in_color[2];
                InternalColor[3] = 255;
            }

            IsSet = true;
        }

        inline void Get_RGBA(uint8_t* out_color) {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a color - please set a color \
before attempting to get it.");

                throw std::runtime_error("Color not set!");
            }

            out_color[0] = InternalColor[0];
            out_color[1] = InternalColor[1];
            out_color[2] = InternalColor[2];
            out_color[3] = InternalColor[3];
        }

        inline void Get_RGB(uint8_t* out_color) {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a color - please set a color \
before attempting to get it.");

                throw std::runtime_error("Color not set!");
            }

            out_color[0] = InternalColor[0];
            out_color[1] = InternalColor[1];
            out_color[2] = InternalColor[2];
        }
};

class EXPORT CPP_BasicAngleConverter {
    protected:
        CPP_Logger* Logger;

        float InternalAngle = 0.f; // Default angle is 0 radians
        const float RADIANS_TO_DEGREES = 180.f / 3.14159265358979323846f;
        const float DEGREES_TO_RADIANS = 3.14159265358979323846f / 180.f;

        bool Changed = true;
        bool IsSet = false;

    public:
        CPP_BasicAngleConverter() {
            Logger = new CPP_Logger();
        }

        ~CPP_BasicAngleConverter() {
            delete Logger;
            Logger = nullptr;
        }

        inline bool GetSet() {
            return IsSet;
        }

        inline bool GetChangedToggle() {
            bool OldChanged = Changed;
            Changed = false;
            return OldChanged;
        }

        inline void Set_Radians(float in_angle) {
            if (in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = in_angle;
            }

            IsSet = true;
        }

        inline void Set_Degrees(float in_angle) {
            float converted_in_angle = in_angle * DEGREES_TO_RADIANS;
            if (converted_in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = converted_in_angle;
            }

            IsSet = true;
        }

        inline float Get_Radians() {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set an angle - please set an angle \
before attempting to get it.");

                throw std::runtime_error("Angle not set!");
            }
            return InternalAngle;
        }

        inline float Get_Degrees() {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set an angle - please set an angle \
before attempting to get it.");

                throw std::runtime_error("Angle not set!");
            }
            return InternalAngle * RADIANS_TO_DEGREES;
        }
};

class EXPORT CPP_BasicProportionConverter {
    protected:
        CPP_Logger* Logger;

        float InternalProportion = 0.f; // Default proportion is 0 (0%)

        bool IsSet = false;
        bool Changed = true;

    public:
        CPP_BasicProportionConverter() {
            Logger = new CPP_Logger();
        }

        ~CPP_BasicProportionConverter() {
            delete Logger;
            Logger = nullptr;
        }

        inline bool GetSet() {
            return IsSet;
        }

        inline bool GetChangedToggle() {
            bool OldChanged = Changed;
            Changed = false;
            return OldChanged;
        }

        inline void Set_Percentage(float in_proportion) {
            float converted_in_proportion = in_proportion / 100;

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }

        inline void Set_Decimal(float in_proportion) {
            if (in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = in_proportion;
            }

            IsSet = true;
        }

        inline float Get_Percentage() {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a proportion - please set a proportion \
before attempting to get it.");

                throw std::runtime_error("Proportion not set!");
            }
            return InternalProportion * 100;
        }

        inline float Get_Decimal() {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a proportion - please set a proportion \
before attempting to get it.");

                throw std::runtime_error("Proportion not set!");
            }
            return InternalProportion;
        }
};