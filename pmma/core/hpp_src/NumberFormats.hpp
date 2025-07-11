#pragma once
#include "PMMA_Exports.hpp"

#include <glm/glm.hpp>

#include "FractalBrownianMotion.hpp"
#include "AdvancedMathematics.hpp"

#include "NumberConverter.hpp"

class EXPORT CPP_ColorFormat: public CPP_BasicColorConverter {
    private:
        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float out_range[2] = {0.f, 1.f};
        float r_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float g_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float b_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float a_offset = CPP_AdvancedMathematics::RandomFloat(out_range);

        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

    public:
        CPP_ColorFormat(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            srand((unsigned int)time(0));

            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
        }

        ~CPP_ColorFormat() {
            delete PerlinNoiseGenerator;
            delete FractalBrownianMotionGenerator;

            PerlinNoiseGenerator = nullptr;
            FractalBrownianMotionGenerator = nullptr;
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
            float color_range[2] = {0, 1};
            InternalColor[0] = CPP_AdvancedMathematics::RandomFloat(color_range);
            InternalColor[1] = CPP_AdvancedMathematics::RandomFloat(color_range);
            InternalColor[2] = CPP_AdvancedMathematics::RandomFloat(color_range);
            InternalColor[3] = CPP_AdvancedMathematics::RandomFloat(color_range);
            ColorIsSet = true;
        }

        inline void GeneratePerlinColor(float value) {
            float BatchedColorGeneration[4][2] = {
                {0, value + r_offset},
                {1, value + g_offset},
                {2, value + b_offset},
                {3, value + a_offset}};

            float OutputColor[4];
            PerlinNoiseGenerator->ArrayNoise2D(BatchedColorGeneration, 4, OutputColor);

            float noise_range[2] = {-1, 1};
            float color_range[2] = {0, 1};
            CPP_AdvancedMathematics::ArrayRanger(OutputColor, 4, noise_range, color_range, OutputColor);
            InternalColor[0] = OutputColor[0];
            InternalColor[1] = OutputColor[1];
            InternalColor[2] = OutputColor[2];
            InternalColor[3] = OutputColor[3];
            ColorIsSet = true;
        }

        inline void GenerateFractalBrownianMotionColor(float value) {
            float BatchedColorGeneration[4][2] = {
                {0, value + r_offset},
                {1, value + g_offset},
                {2, value + b_offset},
                {3, value + a_offset}};

            float OutputColor[4];
            FractalBrownianMotionGenerator->ArrayNoise2D(BatchedColorGeneration, 4, OutputColor);
            float noise_range[2] = {-1, 1};
            float color_range[2] = {0, 1};
            CPP_AdvancedMathematics::ArrayRanger(OutputColor, 4, noise_range, color_range, OutputColor);
            InternalColor[0] = OutputColor[0];
            InternalColor[1] = OutputColor[1];
            InternalColor[2] = OutputColor[2];
            InternalColor[3] = OutputColor[3];
            ColorIsSet = true;
        }
};

class EXPORT CPP_DisplayCoordinateFormat {
    private:
        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

        glm::vec2 DisplayCoordinate;

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float offset_range[2] = {0, 1};
        float x_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);
        float y_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);

        bool DisplayCoordinateSet = false;

    public:
        CPP_DisplayCoordinateFormat(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            srand((unsigned int)time(0));

            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
        }

        ~CPP_DisplayCoordinateFormat() {
            delete PerlinNoiseGenerator;
            delete FractalBrownianMotionGenerator;

            PerlinNoiseGenerator = nullptr;
            FractalBrownianMotionGenerator = nullptr;
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

        void GenerateRandomDisplayCoordinate();

        void GeneratePerlinDisplayCoordinate(float value);

        void GenerateFractalBrownianMotionDisplayCoordinate(float value);

        inline void SetDisplayCoordinate(unsigned int* in_coordinate) {
            DisplayCoordinate.x = (float)in_coordinate[0];
            DisplayCoordinate.y = (float)in_coordinate[1];

            DisplayCoordinateSet = true;
        }

        inline void GetDisplayCoordinate(unsigned int * out_coordinate) {
            if (!DisplayCoordinateSet) {
                throw std::runtime_error("Display coordinate not set!");
            }
            out_coordinate[0] = (unsigned int)DisplayCoordinate.x;
            out_coordinate[1] = (unsigned int)DisplayCoordinate.y;
        }
};

class EXPORT CPP_AngleFormat: public CPP_BasicAngleConverter {
    private:
        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

    public:
        CPP_AngleFormat(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            srand((unsigned int)time(0));

            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
        }

        ~CPP_AngleFormat() {
            delete PerlinNoiseGenerator;
            delete FractalBrownianMotionGenerator;

            PerlinNoiseGenerator = nullptr;
            FractalBrownianMotionGenerator = nullptr;
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
            float angle_range[2] = {0, 3.14159265358979323846f * 2};
            InternalAngle = CPP_AdvancedMathematics::RandomFloat(angle_range);
            AngleIsSet = true;
        }

        inline void GeneratePerlinAngle(float value) {
            InternalAngle = PerlinNoiseGenerator->Noise1D(value);
            float noise_range[] = {-1, 1};
            float angle_range[] = {0, 3.14159265358979323846f * 2};
            InternalAngle = CPP_AdvancedMathematics::Ranger(InternalAngle, noise_range, angle_range);
            AngleIsSet = true;
        }

        inline void GenerateFractalBrownianMotionAngle(float value) {
            InternalAngle = FractalBrownianMotionGenerator->Noise1D(value);
            float noise_range[] = {-1, 1};
            float angle_range[] = {0, 3.14159265358979323846f * 2};
            InternalAngle = CPP_AdvancedMathematics::Ranger(InternalAngle, noise_range, angle_range);
            AngleIsSet = true;
        }
};

class EXPORT CPP_ProportionFormat: public CPP_BasicProportionConverter {
    private:
        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

    public:
        CPP_ProportionFormat(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            srand((unsigned int)time(0));

            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
        }

        ~CPP_ProportionFormat() {
            delete PerlinNoiseGenerator;
            delete FractalBrownianMotionGenerator;

            PerlinNoiseGenerator = nullptr;
            FractalBrownianMotionGenerator = nullptr;
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
            float proportion_range[2] = {0, 1};
            InternalProportion = CPP_AdvancedMathematics::RandomFloat(proportion_range);
            ProportionIsSet = true;
        }

        inline void GeneratePerlinProportion(float value) {
            InternalProportion = PerlinNoiseGenerator->Noise1D(value);
            float perlin_range[2] = {-1, 1};
            float proportion_range[2] = {0, 1};
            InternalProportion = CPP_AdvancedMathematics::Ranger(InternalProportion, perlin_range, proportion_range);
            ProportionIsSet = true;
        }

        inline void GenerateFractalBrownianMotionProportion(float value) {
            InternalProportion = FractalBrownianMotionGenerator->Noise1D(value);
            float perlin_range[2] = {-1, 1};
            float proportion_range[2] = {0, 1};
            InternalProportion = CPP_AdvancedMathematics::Ranger(InternalProportion, perlin_range, proportion_range);
            ProportionIsSet = true;
        }
};