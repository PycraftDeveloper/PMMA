#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <array>
#include <ctime>

class EXPORT CPP_BasicColorConverter {
    protected:
        glm::vec4 InternalColor = glm::vec4(0.f, 0.f, 0.f, 1.f); // Default is black with full opacity

        bool Set = false;
        bool Changed = true;

    public:
        inline bool GetSet() {
            return Set;
        }

        inline bool GetChangedToggle() {
            bool OldChanged = Changed;
            Changed = false;
            return OldChanged;
        }

        inline void SetColor_RGBA(unsigned int* in_color) {
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

            Set = true;
        }

        inline void SetColor_rgba(float* in_color) {
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

            Set = true;
        }

        inline void SetColor_RGB(unsigned int* in_color) {
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

            Set = true;
        }

        inline void SetColor_rgb(float* in_color) {
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

            Set = true;
        }

        inline void GetColor_RGBA(unsigned int* out_color) {
            if (!Set) {
                throw std::runtime_error("Color not set!");
            }

            out_color[0] = (unsigned int)(InternalColor.r * 255);
            out_color[1] = (unsigned int)(InternalColor.g * 255);
            out_color[2] = (unsigned int)(InternalColor.b * 255);
            out_color[3] = (unsigned int)(InternalColor.a * 255);
        }

        inline void GetColor_rgba(float* out_color) {
            if (!Set) {
                throw std::runtime_error("Color not set!");
            }

            out_color[0] = InternalColor.r;
            out_color[1] = InternalColor.g;
            out_color[2] = InternalColor.b;
            out_color[3] = InternalColor.a;
        }

        inline glm::vec4 GetColor_rgba() {
            if (!Set) {
                throw std::runtime_error("Color not set!");
            }
            return InternalColor;
        }

        inline void GetColor_RGB(unsigned int* out_color) {
            if (!Set) {
                throw std::runtime_error("Color not set!");
            }

            out_color[0] = (unsigned int)(InternalColor.r * 255);
            out_color[1] = (unsigned int)(InternalColor.g * 255);
            out_color[2] = (unsigned int)(InternalColor.b * 255);
        }

        inline void GetColor_rgb(float* out_color) {
            if (!Set) {
                throw std::runtime_error("Color not set!");
            }

            out_color[0] = InternalColor.r;
            out_color[1] = InternalColor.g;
            out_color[2] = InternalColor.b;
        }
};

class EXPORT CPP_BasicAngleConverter {
    protected:
        float InternalAngle = 0.f; // Default angle is 0 radians
        const float RADIANS_TO_DEGREES = 180.f / 3.14159265358979323846f;
        const float DEGREES_TO_RADIANS = 3.14159265358979323846f / 180.f;

        bool Changed = true;
        bool Set = false;

    public:
        inline bool GetSet() {
            return Set;
        }

        inline bool GetChangedToggle() {
            bool OldChanged = Changed;
            Changed = false;
            return OldChanged;
        }

        inline void SetAngle_Radians(float in_angle) {
            if (in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = in_angle;
            }

            Set = true;
        }

        inline void SetAngle_Degrees(float in_angle) {
            float converted_in_angle = in_angle * DEGREES_TO_RADIANS;
            if (converted_in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = converted_in_angle;
            }

            Set = true;
        }

        inline float GetAngle_Radians() {
            if (!Set) {
                throw std::runtime_error("Angle not set!");
            }
            return InternalAngle;
        }

        inline float GetAngle_Degrees() {
            if (!Set) {
                throw std::runtime_error("Angle not set!");
            }
            return InternalAngle * RADIANS_TO_DEGREES;
        }
};

class EXPORT CPP_BasicProportionConverter {
    protected:
        float InternalProportion = 0.f; // Default proportion is 0 (0%)

        bool Set = false;
        bool Changed = true;

    public:
        inline bool GetSet() {
            return Set;
        }

        inline bool GetChangedToggle() {
            bool OldChanged = Changed;
            Changed = false;
            return OldChanged;
        }

        inline void SetProportion_Percentage(float in_proportion) {
            float converted_in_proportion = in_proportion / 100;

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            Set = true;
        }

        inline void SetProportion_Decimal(float in_proportion) {
            if (in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = in_proportion;
            }

            Set = true;
        }

        inline float GetProportion_Percentage() {
            if (!Set) {
                throw std::runtime_error("Proportion not set!");
            }
            return InternalProportion * 100;
        }

        inline float GetProportion_Decimal() {
            if (!Set) {
                throw std::runtime_error("Proportion not set!");
            }
            return InternalProportion;
        }
};