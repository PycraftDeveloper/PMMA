#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <array>
#include <ctime>

class EXPORT CPP_BasicColorConverter {
    protected:
        float InternalColor[4];

        bool ColorIsSet = false;

    public:
        inline bool GetColorIsSet() {
            return ColorIsSet;
        }

        inline void SetColor_RGBA(unsigned int* in_color) {
            InternalColor[0] = in_color[0] / 255.f;
            InternalColor[1] = in_color[1] / 255.f;
            InternalColor[2] = in_color[2] / 255.f;
            InternalColor[3] = in_color[3] / 255.f;
            ColorIsSet = true;
        }

        inline void SetColor_rgba(float* in_color) {
            InternalColor[0] = in_color[0];
            InternalColor[1] = in_color[1];
            InternalColor[2] = in_color[2];
            InternalColor[3] = in_color[3];
            ColorIsSet = true;
        }

        inline void SetColor_RGB(unsigned int* in_color) {
            InternalColor[0] = in_color[0] / 255.f;
            InternalColor[1] = in_color[1] / 255.f;
            InternalColor[2] = in_color[2] / 255.f;
            InternalColor[3] = 1.f;
            ColorIsSet = true;
        }

        inline void SetColor_rgb(float* in_color) {
            InternalColor[0] = in_color[0];
            InternalColor[1] = in_color[1];
            InternalColor[2] = in_color[2];
            InternalColor[3] = 1.f;
            ColorIsSet = true;
        }

        inline void GetColor_RGBA(unsigned int* out_color) {
            if (!ColorIsSet) {
                throw std::runtime_error("Color not set!");
            }
            out_color[0] = (unsigned int)(InternalColor[0] * 255);
            out_color[1] = (unsigned int)(InternalColor[1] * 255);
            out_color[2] = (unsigned int)(InternalColor[2] * 255);
            out_color[3] = (unsigned int)(InternalColor[3] * 255);
        }

        inline void GetColor_rgba(float* out_color) {
            if (!ColorIsSet) {
                throw std::runtime_error("Color not set!");
            }
            out_color[0] = InternalColor[0];
            out_color[1] = InternalColor[1];
            out_color[2] = InternalColor[2];
            out_color[3] = InternalColor[3];
        }

        inline void GetColor_RGB(unsigned int* out_color) {
            if (!ColorIsSet) {
                throw std::runtime_error("Color not set!");
            }
            out_color[0] = (unsigned int)(InternalColor[0] * 255);
            out_color[1] = (unsigned int)(InternalColor[1] * 255);
            out_color[2] = (unsigned int)(InternalColor[2] * 255);
        }

        inline void GetColor_rgb(float* out_color) {
            if (!ColorIsSet) {
                throw std::runtime_error("Color not set!");
            }
            out_color[0] = InternalColor[0];
            out_color[1] = InternalColor[1];
            out_color[2] = InternalColor[2];
        }
};

class EXPORT CPP_BasicAngleConverter {
    protected:
        float InternalAngle;
        bool AngleIsSet = false;
        const float RADIANS_TO_DEGREES = 180.f / 3.14159265358979323846f;
        const float DEGREES_TO_RADIANS = 3.14159265358979323846f / 180.f;

    public:
        inline bool GetAngleIsSet() {
            return AngleIsSet;
        }

        inline void SetAngle_Radians(float in_angle) {
            InternalAngle = in_angle;
            AngleIsSet = true;
        }

        inline void SetAngle_Degrees(float in_angle) {
            InternalAngle = in_angle * DEGREES_TO_RADIANS;
            AngleIsSet = true;
        }

        inline float GetAngle_Radians() {
            if (!AngleIsSet) {
                throw std::runtime_error("Angle not set!");
            }
            return InternalAngle;
        }

        inline float GetAngle_Degrees() {
            if (!AngleIsSet) {
                throw std::runtime_error("Angle not set!");
            }
            return InternalAngle * RADIANS_TO_DEGREES;
        }
};

class EXPORT CPP_BasicProportionConverter {
    protected:
        float InternalProportion;
        bool ProportionIsSet = false;

    public:
        inline bool GetProportionIsSet() {
            return ProportionIsSet;
        }

        inline void SetProportion_Percentage(float in_proportion) {
            InternalProportion = in_proportion / 100;
            ProportionIsSet = true;
        }

        inline void SetProportion_Decimal(float in_proportion) {
            InternalProportion = in_proportion;
            ProportionIsSet = true;
        }

        inline float GetProportion_Percentage() {
            if (!ProportionIsSet) {
                throw std::runtime_error("Proportion not set!");
            }
            return InternalProportion * 100;
        }

        inline float GetProportion_Decimal() {
            if (!ProportionIsSet) {
                throw std::runtime_error("Proportion not set!");
            }
            return InternalProportion;
        }
};