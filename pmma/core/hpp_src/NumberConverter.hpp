#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <array>
#include <ctime>

#include "FractalBrownianMotion.hpp"
#include "AdvancedMathematics.hpp"

class CPP_Display;

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

class EXPORT CPP_ColorConverter: public CPP_BasicColorConverter {
    private:
        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

    public:
        CPP_ColorConverter(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            srand((unsigned int)time(0));

            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
        }

        inline uint32_t GetSeed() {
            return seed;
        }

        inline uint32_t GetOctaves() {
            return octaves;
        }

        inline float GetFrequency() {
            return frequency;
        }

        inline float GetAmplitude() {
            return amplitude;
        }

        inline void GenerateRandomColor() {
            InternalColor[0] = CPP_AdvancedMathematics::RandomFloat(new float[2]{0, 1});
            InternalColor[1] = CPP_AdvancedMathematics::RandomFloat(new float[2]{0, 1});
            InternalColor[2] = CPP_AdvancedMathematics::RandomFloat(new float[2]{0, 1});
            InternalColor[3] = CPP_AdvancedMathematics::RandomFloat(new float[2]{0, 1});
            ColorIsSet = true;
        }

        inline void GeneratePerlinColor(float value) {
            float BatchedColorGeneration[4][2] = {{0, value}, {1, value}, {2, value}, {3, value}};
            float OutputColor[4];
            PerlinNoiseGenerator->ArrayNoise2D(BatchedColorGeneration, 4, OutputColor);
            CPP_AdvancedMathematics::ArrayRanger(OutputColor, 4, new float[2]{-1, 1}, new float[2]{0, 1}, OutputColor);
            InternalColor[0] = OutputColor[0];
            InternalColor[1] = OutputColor[1];
            InternalColor[2] = OutputColor[2];
            InternalColor[3] = OutputColor[3];
            ColorIsSet = true;
        }

        inline void GenerateFractalBrownianMotionColor(float value) {
            float BatchedColorGeneration[4][2] = {{0, value}, {1, value}, {2, value}, {3, value}};
            float OutputColor[4];
            FractalBrownianMotionGenerator->ArrayNoise2D(BatchedColorGeneration, 4, OutputColor);
            CPP_AdvancedMathematics::ArrayRanger(OutputColor, 4, new float[2]{-1, 1}, new float[2]{0, 1}, OutputColor);
            InternalColor[0] = OutputColor[0];
            InternalColor[1] = OutputColor[1];
            InternalColor[2] = OutputColor[2];
            InternalColor[3] = OutputColor[3];
            ColorIsSet = true;
        }
};

class EXPORT CPP_BasicDisplayCoordinatesConverter {
    protected:
        float InternalCoordinates[2];
        bool CoordinatesAreSet = false;
        CPP_Display* display = nullptr;

    public:
        CPP_BasicDisplayCoordinatesConverter();

        inline bool GetCoordinatesAreSet() {
            return CoordinatesAreSet;
        }

        void SetCoordinates_Pixel(unsigned int* in_coordinates);

        inline void SetCoordinates_Normalized(float* in_coordinates) {
            InternalCoordinates[0] = in_coordinates[0];
            InternalCoordinates[1] = in_coordinates[1];
            CoordinatesAreSet = true;
        }

        void GetCoordinates_Pixel(unsigned int* out_coordinates);

        inline void GetCoordinates_Normalized(float* out_coordinates) {
            if (!CoordinatesAreSet) {
                throw std::runtime_error("Coordinates not set!");
            }
            out_coordinates[0] = InternalCoordinates[0];
            out_coordinates[1] = InternalCoordinates[1];
        }
};

class EXPORT CPP_DisplayCoordinatesConverter: public CPP_BasicDisplayCoordinatesConverter {
    private:
        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

    public:
        CPP_DisplayCoordinatesConverter(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude);

        inline uint32_t GetSeed() {
            return seed;
        }

        inline uint32_t GetOctaves() {
            return octaves;
        }

        inline float GetFrequency() {
            return frequency;
        }

        inline float GetAmplitude() {
            return amplitude;
        }

        inline void GenerateRandomCoordinates() {
            InternalCoordinates[0] = CPP_AdvancedMathematics::RandomFloat(new float[2]{-1, 1});
            InternalCoordinates[1] = CPP_AdvancedMathematics::RandomFloat(new float[2]{-1, 1});
            CoordinatesAreSet = true;
        }

        inline void GeneratePerlinCoordinates(float value) {
            float BatchedCoordinatesGeneration[2][2] = {{0, value}, {1, value}};
            float OutputCoordinates[2];
            PerlinNoiseGenerator->ArrayNoise2D(BatchedCoordinatesGeneration, 3, OutputCoordinates);
            InternalCoordinates[0] = OutputCoordinates[0];
            InternalCoordinates[1] = OutputCoordinates[1];
            CoordinatesAreSet = true;
        }

        inline void GenerateFractalBrownianMotionCoordinates(float value) {
            float BatchedCoordinatesGeneration[2][2] = {{0, value}, {1, value}};
            float OutputCoordinates[2];
            FractalBrownianMotionGenerator->ArrayNoise2D(BatchedCoordinatesGeneration, 3, OutputCoordinates);
            InternalCoordinates[0] = OutputCoordinates[0];
            InternalCoordinates[1] = OutputCoordinates[1];
            CoordinatesAreSet = true;
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

class EXPORT CPP_AngleConverter: public CPP_BasicAngleConverter {
    private:
        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

    public:
        CPP_AngleConverter(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            srand((unsigned int)time(0));

            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
        }

        inline uint32_t GetSeed() {
            return seed;
        }

        inline uint32_t GetOctaves() {
            return octaves;
        }

        inline float GetFrequency() {
            return frequency;
        }

        inline float GetAmplitude() {
            return amplitude;
        }

        inline void GenerateRandomAngle() {
            InternalAngle = CPP_AdvancedMathematics::RandomFloat(new float[2]{0, 3.14159265358979323846f * 2});
            AngleIsSet = true;
        }

        inline void GeneratePerlinAngle(float value) {
            InternalAngle = PerlinNoiseGenerator->Noise1D(value);
            InternalAngle = CPP_AdvancedMathematics::Ranger(InternalAngle, new float[2]{-1, 1}, new float[2]{0, 3.14159265358979323846f * 2});
            AngleIsSet = true;
        }

        inline void GenerateFractalBrownianMotionAngle(float value) {
            InternalAngle = FractalBrownianMotionGenerator->Noise1D(value);
            InternalAngle = CPP_AdvancedMathematics::Ranger(InternalAngle, new float[2]{-1, 1}, new float[2]{0, 3.14159265358979323846f * 2});
            AngleIsSet = true;
        }
};

class EXPORT CPP_BasicDisplayScalarConverter {
    protected:
        float InternalScalar;
        bool ScalarIsSet = false;
        CPP_Display* display = nullptr;

    public:
        CPP_BasicDisplayScalarConverter();

        inline bool GetScalarIsSet() {
            return ScalarIsSet;
        }

        void SetScalar_Pixel(unsigned int in_scalar);

        inline void SetScalar_Normalized(float in_scalar) {
            InternalScalar = in_scalar;
            ScalarIsSet = true;
        }

        unsigned int GetScalar_Pixel();

        inline float GetScalar_Normalized() {
            if (!ScalarIsSet) {
                throw std::runtime_error("Scalar not set!");
            }
            return InternalScalar;
        }
};

class EXPORT CPP_DisplayScalarConverter: public CPP_BasicDisplayScalarConverter{
    private:
        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

    public:
        CPP_DisplayScalarConverter(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude);

        inline uint32_t GetSeed() {
            return seed;
        }

        inline uint32_t GetOctaves() {
            return octaves;
        }

        inline float GetFrequency() {
            return frequency;
        }

        inline float GetAmplitude() {
            return amplitude;
        }

        inline void GenerateRandomScalar() {
            InternalScalar = CPP_AdvancedMathematics::RandomFloat(new float[2]{-1, 1});
            ScalarIsSet = true;
        }

        inline void GeneratePerlinScalar(float value) {
            InternalScalar = PerlinNoiseGenerator->Noise1D(value);
            ScalarIsSet = true;
        }

        inline void GenerateFractalBrownianMotionScalar(float value) {
            InternalScalar = FractalBrownianMotionGenerator->Noise1D(value);
            ScalarIsSet = true;
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

class EXPORT CPP_ProportionConverter: public CPP_BasicProportionConverter {
    private:
        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

    public:
        CPP_ProportionConverter(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            srand((unsigned int)time(0));

            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
        }

        inline uint32_t GetSeed() {
            return seed;
        }

        inline uint32_t GetOctaves() {
            return octaves;
        }

        inline float GetFrequency() {
            return frequency;
        }

        inline float GetAmplitude() {
            return amplitude;
        }

        inline void GenerateRandomProportion() {
            InternalProportion = CPP_AdvancedMathematics::RandomFloat(new float[2]{0, 1});
            ProportionIsSet = true;
        }

        inline void GeneratePerlinProportion(float value) {
            InternalProportion = PerlinNoiseGenerator->Noise1D(value);
            InternalProportion = CPP_AdvancedMathematics::Ranger(InternalProportion, new float[2]{-1, 1}, new float[2]{0, 1});
            ProportionIsSet = true;
        }

        inline void GenerateFractalBrownianMotionProportion(float value) {
            InternalProportion = FractalBrownianMotionGenerator->Noise1D(value);
            InternalProportion = CPP_AdvancedMathematics::Ranger(InternalProportion, new float[2]{-1, 1}, new float[2]{0, 1});
            ProportionIsSet = true;
        }
};