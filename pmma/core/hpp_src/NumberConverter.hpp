#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <array>
#include <ctime>

#include "Logger.hpp"

class EXPORT CPP_BasicColorConverter {
    protected:
        CPP_Logger* Logger;

        glm::vec4 InternalColor = glm::vec4(0.f, 0.f, 0.f, 1.f); // Default is black with full opacity

        bool IsSet = false;
        bool Changed = true;

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

        inline void Set_RGBA(unsigned int* in_color) {
            glm::vec4 converted_in_color = glm::vec4(
                in_color[0] / 255.f,
                in_color[1] / 255.f,
                in_color[2] / 255.f,
                in_color[3] / 255.f
            );

            if (converted_in_color != InternalColor) {
                Changed = true;
                InternalColor = converted_in_color;
            }

            IsSet = true;
        }

        inline void Set_rgba(float* in_color) {
            glm::vec4 converted_in_color = glm::vec4(
                in_color[0],
                in_color[1],
                in_color[2],
                in_color[3]
            );

            if (converted_in_color != InternalColor) {
                Changed = true;
                InternalColor = converted_in_color;
            }

            IsSet = true;
        }

        inline void Set_RGB(unsigned int* in_color) {
            Logger->InternalLogDebug(
                9,
                "The alpha channel is automatically set to opaque."
            );

            glm::vec4 converted_in_color = glm::vec4(
                in_color[0] / 255.f,
                in_color[1] / 255.f,
                in_color[2] / 255.f,
                1.f // Default alpha is 1 (fully opaque)
            );

            if (converted_in_color != InternalColor) {
                Changed = true;
                InternalColor = converted_in_color;
            }

            IsSet = true;
        }

        inline void Set_rgb(float* in_color) {
            Logger->InternalLogDebug(
                9,
                "The alpha channel is automatically set to opaque."
            );

            glm::vec4 converted_in_color = glm::vec4(
                in_color[0],
                in_color[1],
                in_color[2],
                1.f // Default alpha is 1 (fully opaque)
            );

            if (converted_in_color != InternalColor) {
                Changed = true;
                InternalColor = converted_in_color;
            }

            IsSet = true;
        }

        inline void Get_RGBA(unsigned int* out_color) {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a color - please set a color \
before attempting to get it.");

                throw std::runtime_error("Color not set!");
            }

            out_color[0] = (unsigned int)(InternalColor.r * 255);
            out_color[1] = (unsigned int)(InternalColor.g * 255);
            out_color[2] = (unsigned int)(InternalColor.b * 255);
            out_color[3] = (unsigned int)(InternalColor.a * 255);
        }

        inline void Get_rgba(float* out_color) {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a color - please set a color \
before attempting to get it.");

                throw std::runtime_error("Color not set!");
            }

            out_color[0] = InternalColor.r;
            out_color[1] = InternalColor.g;
            out_color[2] = InternalColor.b;
            out_color[3] = InternalColor.a;
        }

        inline glm::vec4 Get_rgba() {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a color - please set a color \
before attempting to get it.");

                throw std::runtime_error("Color not set!");
            }
            return InternalColor;
        }

        inline void Get_RGB(unsigned int* out_color) {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a color - please set a color \
before attempting to get it.");

                throw std::runtime_error("Color not set!");
            }

            out_color[0] = (unsigned int)(InternalColor.r * 255);
            out_color[1] = (unsigned int)(InternalColor.g * 255);
            out_color[2] = (unsigned int)(InternalColor.b * 255);
        }

        inline void Get_rgb(float* out_color) {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a color - please set a color \
before attempting to get it.");

                throw std::runtime_error("Color not set!");
            }

            out_color[0] = InternalColor.r;
            out_color[1] = InternalColor.g;
            out_color[2] = InternalColor.b;
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