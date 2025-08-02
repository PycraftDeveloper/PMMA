#pragma once
#include "PMMA_Exports.hpp"

#include <glm/glm.hpp>

#include "FractalBrownianMotion.hpp"
#include "AdvancedMathematics.hpp"

#include "NumberConverter.hpp"

class EXPORT CPP_ColorFormat: public CPP_BasicColorConverter {
    private:
        CPP_PerlinNoise* R_PerlinNoiseGenerator = nullptr;
        CPP_PerlinNoise* G_PerlinNoiseGenerator = nullptr;
        CPP_PerlinNoise* B_PerlinNoiseGenerator = nullptr;
        CPP_PerlinNoise* A_PerlinNoiseGenerator = nullptr;

        CPP_FractalBrownianMotion* R_FractalBrownianMotionGenerator = nullptr;
        CPP_FractalBrownianMotion* G_FractalBrownianMotionGenerator = nullptr;
        CPP_FractalBrownianMotion* B_FractalBrownianMotionGenerator = nullptr;
        CPP_FractalBrownianMotion* A_FractalBrownianMotionGenerator = nullptr;

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float out_range[2] = {0.f, 1.f};
        float r_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float g_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float b_offset = CPP_AdvancedMathematics::RandomFloat(out_range);
        float a_offset = CPP_AdvancedMathematics::RandomFloat(out_range);

        const float noise_range[2] = {-1.f, 1.f};
        const float color_range[2] = {0.f, 1.f};

        bool Configured = false;

    public:
        ~CPP_ColorFormat() {
            if (Configured) {
                delete R_PerlinNoiseGenerator;
                delete G_PerlinNoiseGenerator;
                delete B_PerlinNoiseGenerator;
                delete A_PerlinNoiseGenerator;

                delete R_FractalBrownianMotionGenerator;
                delete G_FractalBrownianMotionGenerator;
                delete B_FractalBrownianMotionGenerator;
                delete A_FractalBrownianMotionGenerator;

                R_PerlinNoiseGenerator = nullptr;
                G_PerlinNoiseGenerator = nullptr;
                B_PerlinNoiseGenerator = nullptr;
                A_PerlinNoiseGenerator = nullptr;

                R_FractalBrownianMotionGenerator = nullptr;
                G_FractalBrownianMotionGenerator = nullptr;
                B_FractalBrownianMotionGenerator = nullptr;
                A_FractalBrownianMotionGenerator = nullptr;
            }
        }

        inline void Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            R_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            G_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed + 1);
            B_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed + 2);
            A_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed + 3);

            R_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);
            G_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed + 1, new_octaves, new_frequency, new_amplitude);
            B_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed + 2, new_octaves, new_frequency, new_amplitude);
            A_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed + 3, new_octaves, new_frequency, new_amplitude);

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

            float OutputColor[4];
            OutputColor[0] = R_PerlinNoiseGenerator->Noise1D(value + r_offset);
            OutputColor[1] = G_PerlinNoiseGenerator->Noise1D(value + g_offset);
            OutputColor[2] = B_PerlinNoiseGenerator->Noise1D(value + b_offset);
            OutputColor[3] = A_PerlinNoiseGenerator->Noise1D(value + a_offset);

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

            float OutputColor[4];
            OutputColor[0] = R_FractalBrownianMotionGenerator->Noise1D(value + r_offset);
            OutputColor[1] = G_FractalBrownianMotionGenerator->Noise1D(value + g_offset);
            OutputColor[2] = B_FractalBrownianMotionGenerator->Noise1D(value + b_offset);
            OutputColor[3] = A_FractalBrownianMotionGenerator->Noise1D(value + a_offset);

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
        CPP_PerlinNoise* X_PerlinNoiseGenerator = nullptr;
        CPP_PerlinNoise* Y_PerlinNoiseGenerator = nullptr;

        CPP_FractalBrownianMotion* X_FractalBrownianMotionGenerator = nullptr;
        CPP_FractalBrownianMotion* Y_FractalBrownianMotionGenerator = nullptr;

        glm::vec2 DisplayCoordinate = {0.f, 0.f}; // Default display coordinate is (0, 0)

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float offset_range[2] = {0, 1};
        float x_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);
        float y_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);

        const float noise_range[2] = {-1.f, 1.f};

        bool IsSet = false;
        bool Changed = true;
        bool Configured = false;

    public:
        ~CPP_DisplayCoordinateFormat() {
            if (Configured) {
                delete X_PerlinNoiseGenerator;
                delete Y_PerlinNoiseGenerator;

                delete X_FractalBrownianMotionGenerator;
                delete Y_FractalBrownianMotionGenerator;

                X_PerlinNoiseGenerator = nullptr;
                Y_PerlinNoiseGenerator = nullptr;

                X_FractalBrownianMotionGenerator = nullptr;
                Y_FractalBrownianMotionGenerator = nullptr;
            }
        }

        inline void Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
            X_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
            Y_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed + 1);

            X_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);
            Y_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed + 1, new_octaves, new_frequency, new_amplitude);

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

        const float noise_range[2] = {-1.f, 1.f};
        const float angle_range[2] = {0.f, 3.14159265358979323846f * 2};

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

        const float noise_range[2] = {-1.f, 1.f};
        const float proportion_range[2] = {0.f, 1.f};

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
            float converted_in_proportion = CPP_AdvancedMathematics::Ranger(InternalProportion, noise_range, proportion_range);

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
            float converted_in_proportion = CPP_AdvancedMathematics::Ranger(InternalProportion, noise_range, proportion_range);

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }
};