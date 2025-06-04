#pragma once

#include <stdexcept>

#include "libshared.h"

class CPP_ColorConverter {
    private:
        float InternalColor[4];
        bool ColorIsSet = false;

    public:
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

class CPP_DisplayCoordinatesConverter {
    private:
        float InternalCoordinates[2];
        bool CoordinatesAreSet = false;
        CPP_Display* display = nullptr;

    public:
        CPP_DisplayCoordinatesConverter(CPP_Display* in_display) {
            display = in_display;
        }

        inline void SetCoordinates_Pixel(unsigned int* in_coordinates) {
            if (display == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            unsigned int DisplaySize[2];
            display->GetSize(DisplaySize);

            float HalfDisplaySize[2] = { DisplaySize[0] / 2.f, DisplaySize[1] / 2.f };

            InternalCoordinates[0] = (in_coordinates[0] - HalfDisplaySize[0]) / HalfDisplaySize[0];
            InternalCoordinates[1] = (in_coordinates[1] - HalfDisplaySize[1]) / HalfDisplaySize[1];
            CoordinatesAreSet = true;
        }

        inline void SetCoordinates_Normalized(float* in_coordinates) {
            InternalCoordinates[0] = in_coordinates[0];
            InternalCoordinates[1] = in_coordinates[1];
            CoordinatesAreSet = true;
        }

        inline void GetCoordinates_Pixel(unsigned int* out_coordinates) {
            if (!CoordinatesAreSet) {
                throw std::runtime_error("Coordinates not set!");
            }
            if (display == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            unsigned int DisplaySize[2];
            display->GetSize(DisplaySize);

            float HalfDisplaySize[2] = { DisplaySize[0] / 2.f, DisplaySize[1] / 2.f };

            out_coordinates[0] = (unsigned int)(InternalCoordinates[0] * HalfDisplaySize[0] + HalfDisplaySize[0]);
            out_coordinates[1] = (unsigned int)(InternalCoordinates[1] * HalfDisplaySize[1] + HalfDisplaySize[1]);
        }

        inline void GetCoordinates_Normalized(float* out_coordinates) {
            if (!CoordinatesAreSet) {
                throw std::runtime_error("Coordinates not set!");
            }
            out_coordinates[0] = InternalCoordinates[0];
            out_coordinates[1] = InternalCoordinates[1];
        }
};

class CPP_AngleConverter {
    private:
        float InternalAngle;
        bool AngleIsSet = false;
        const float RADIANS_TO_DEGREES = 180.f / 3.14159265358979323846f;
        const float DEGREES_TO_RADIANS = 3.14159265358979323846f / 180.f;

    public:
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

class CPP_DisplayScalarConverter {
    public:
        float InternalScalar;
        bool ScalarIsSet = false;

    public:
        //inline void SetScalar_Pixel(unsigned int in_scalar) {
            /*InternalScalar = (float)(in_scalar) * (2.f / CPP_Components::display->GetHeight());
            ScalarIsSet = true;*/
        //}

        inline void SetScalar_Normalized(float in_scalar) {
            InternalScalar = in_scalar;
            ScalarIsSet = true;
        }

        //inline unsigned int GetScalar_Pixel() {
            /*if (!ScalarIsSet) {
                throw std::runtime_error("Scalar not set!");
            }
            return (unsigned int)(InternalScalar * CPP_Components::display->GetHeight() / 2.f);*/
        //}

        inline float GetScalar_Normalized() {
            if (!ScalarIsSet) {
                throw std::runtime_error("Scalar not set!");
            }
            return InternalScalar;
        }
};