#pragma once
#include "PMMA_Exports.hpp"

#include <glm/glm.hpp>

#include "FractalBrownianMotion.hpp"
#include "AdvancedMathematics.hpp"

#include "NumberConverter.hpp"

class EXPORT CPP_ColorFormat: public CPP_BasicColorConverter {
    private:
        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float out_range[2] = {0.f, 1.f};
        float r_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float g_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float b_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float a_offset = CPP_AdvancedMathematics::RandomFloat(out_range);

        bool Configured = false;

    public:
        ~CPP_ColorFormat() {
            if (Configured) {
                delete PerlinNoiseGenerator;
                delete FractalBrownianMotionGenerator;

                PerlinNoiseGenerator = nullptr;
                FractalBrownianMotionGenerator = nullptr;
            }
        }

        inline void Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            srand(new_seed);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
            Configured = true;
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

        inline void GenerateFromRandom() {
            float color_range[2] = {0, 1};
            glm::vec4 converted_in_color = glm::vec4(
                CPP_AdvancedMathematics::RandomFloat(color_range),
                CPP_AdvancedMathematics::RandomFloat(color_range),
                CPP_AdvancedMathematics::RandomFloat(color_range),
                CPP_AdvancedMathematics::RandomFloat(color_range)
            );

            if (converted_in_color != InternalColor) {
                Changed = true;
                InternalColor = converted_in_color;
            }

            IsSet = true;
        }

        inline void GenerateFromPerlinNoise(float value) {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }

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

            glm::vec4 converted_in_color = glm::vec4(
                OutputColor[0],
                OutputColor[1],
                OutputColor[2],
                OutputColor[3]
            );

            if (converted_in_color != InternalColor) {
                Changed = true;
                InternalColor = converted_in_color;
            }

            IsSet = true;
        }

        inline void GenerateFromFractalBrownianMotion(float value) {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }

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

            glm::vec4 converted_in_color = glm::vec4(
                OutputColor[0],
                OutputColor[1],
                OutputColor[2],
                OutputColor[3]
            );

            if (converted_in_color != InternalColor) {
                Changed = true;
                InternalColor = converted_in_color;
            }

            IsSet = true;
        }
};

class EXPORT CPP_DisplayCoordinateFormat {
    private:
        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

        glm::vec2 DisplayCoordinate = {0.f, 0.f}; // Default display coordinate is (0, 0)

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float offset_range[2] = {0, 1};
        float x_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);
        float y_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);

        bool IsSet = false;
        bool Changed = true;
        bool Configured = false;

    public:
        ~CPP_DisplayCoordinateFormat() {
            if (Configured) {
                delete PerlinNoiseGenerator;
                delete FractalBrownianMotionGenerator;

                PerlinNoiseGenerator = nullptr;
                FractalBrownianMotionGenerator = nullptr;
            }
        }

        inline void Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            srand(new_seed);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
            Configured = true;
        }

        inline bool GetChangedToggle() {
            bool OldChanged = Changed;
            Changed = false;
            return OldChanged;
        }

        inline bool GetSet() {
            return IsSet;
        }

        inline uint32_t GetSeed() {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }
            return amplitude;
        }

        void GenerateFromRandom();

        void GenerateFromPerlinNoise(float value);

        void GenerateFromFractalBrownianMotion(float value);

        inline void Set(unsigned int* in_coordinate) {
            glm::vec2 converted_in_coordinate = {
                (float)in_coordinate[0],
                (float)in_coordinate[1]
            };

            if (converted_in_coordinate != DisplayCoordinate) {
                Changed = true;
                DisplayCoordinate = converted_in_coordinate;
            }

            IsSet = true;
        }

        inline void Get(unsigned int * out_coordinate) {
            if (!IsSet) {
                throw std::runtime_error("Display coordinate not set!");
            }
            out_coordinate[0] = (unsigned int)DisplayCoordinate.x;
            out_coordinate[1] = (unsigned int)DisplayCoordinate.y;
        }

        inline glm::vec2 Get() {
            if (!IsSet) {
                throw std::runtime_error("Display coordinate not set!");
            }
            return DisplayCoordinate;
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

        bool Configured = false;

    public:
        ~CPP_AngleFormat() {
            delete PerlinNoiseGenerator;
            delete FractalBrownianMotionGenerator;

            PerlinNoiseGenerator = nullptr;
            FractalBrownianMotionGenerator = nullptr;
        }

        inline void Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            srand(new_seed);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
            Configured = true;
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

        inline void GenerateFromRandom() {
            float angle_range[2] = {0, 3.14159265358979323846f * 2};
            float converted_in_angle = CPP_AdvancedMathematics::RandomFloat(angle_range);

            if (converted_in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = converted_in_angle;
            }

            IsSet = true;
        }

        inline void GenerateFromPerlinNoise(float value) {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }

            InternalAngle = PerlinNoiseGenerator->Noise1D(value);
            float noise_range[] = {-1, 1};
            float angle_range[] = {0, 3.14159265358979323846f * 2};
            float converted_in_angle = CPP_AdvancedMathematics::Ranger(InternalAngle, noise_range, angle_range);

            if (converted_in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = converted_in_angle;
            }

            IsSet = true;
        }

        inline void GenerateFromFractalBrownianMotion(float value) {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }

            InternalAngle = FractalBrownianMotionGenerator->Noise1D(value);
            float noise_range[] = {-1, 1};
            float angle_range[] = {0, 3.14159265358979323846f * 2};
            float converted_in_angle = CPP_AdvancedMathematics::Ranger(InternalAngle, noise_range, angle_range);

            if (converted_in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = converted_in_angle;
            }

            IsSet = true;
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

        bool Configured = false;

    public:
        ~CPP_ProportionFormat() {
            delete PerlinNoiseGenerator;
            delete FractalBrownianMotionGenerator;

            PerlinNoiseGenerator = nullptr;
            FractalBrownianMotionGenerator = nullptr;
        }

        inline void Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

            srand(new_seed);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
            Configured = true;
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

        inline void GenerateFromRandom() {
            float proportion_range[2] = {0, 1};
            float converted_in_proportion = CPP_AdvancedMathematics::RandomFloat(proportion_range);

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }

        inline void GenerateFromPerlinNoise(float value) {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }

            InternalProportion = PerlinNoiseGenerator->Noise1D(value);
            float perlin_range[2] = {-1, 1};
            float proportion_range[2] = {0, 1};
            float converted_in_proportion = CPP_AdvancedMathematics::Ranger(InternalProportion, perlin_range, proportion_range);

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }

        inline void GenerateFromFractalBrownianMotion(float value) {
            if (!Configured) {
                throw runtime_error("You need to configure this component first!");
            }

            InternalProportion = FractalBrownianMotionGenerator->Noise1D(value);
            float perlin_range[2] = {-1, 1};
            float proportion_range[2] = {0, 1};
            float converted_in_proportion = CPP_AdvancedMathematics::Ranger(InternalProportion, perlin_range, proportion_range);

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }
};