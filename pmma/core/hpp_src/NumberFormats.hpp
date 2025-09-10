#pragma once
#include "PMMA_Exports.hpp"

#include <glm/glm.hpp>

#include "FractalBrownianMotion.hpp"
#include "AdvancedMathematics.hpp"
#include "NumberConverter.hpp"
#include "Logger.hpp"

class EXPORT CPP_ColorFormat: public CPP_BasicColorConverter {
    private:
        CPP_Logger* Logger;

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
        float half_color_max = 255.f / 2.f;

        float offset_range[2] = {0.f, 1.f};
        float r_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);
        float g_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);
        float b_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);
        float a_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);

        const float noise_range[2] = {-1.f, 1.f};
        const float color_range[2] = {0, 255};

        bool Configured = false;

    public:
        CPP_ColorFormat() {
            Logger = new CPP_Logger();
        }

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

            delete Logger;
            Logger = nullptr;
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
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return amplitude;
        }

        inline void GenerateFromRandom(bool GenerateAlpha=true) {
            uint8_t in_color[4];
            if (GenerateAlpha) {
                in_color[0] = (uint8_t)rand() % 255;
                in_color[1] = (uint8_t)rand() % 255;
                in_color[2] = (uint8_t)rand() % 255;
                in_color[3] = (uint8_t)rand() % 255;
            } else {
                in_color[0] = (uint8_t)rand() % 255;
                in_color[1] = (uint8_t)rand() % 255;
                in_color[2] = (uint8_t)rand() % 255;
                in_color[3] = 255;
            }

            Set_RGBA(in_color);
        }

        inline void GenerateFrom1DPerlinNoise(float value, bool GenerateAlpha=true) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            float OutputColor[4];
            OutputColor[0] = R_PerlinNoiseGenerator->Noise1D(value + r_offset);
            OutputColor[1] = G_PerlinNoiseGenerator->Noise1D(value + g_offset);
            OutputColor[2] = B_PerlinNoiseGenerator->Noise1D(value + b_offset);
            if (GenerateAlpha) {
                OutputColor[3] = A_PerlinNoiseGenerator->Noise1D(value + a_offset);
            } else {
                OutputColor[3] = 1.0f;
            }

            uint8_t in_color[4];
            in_color[0] = (uint8_t)((1 + OutputColor[0]) * half_color_max);
            in_color[1] = (uint8_t)((1 + OutputColor[1]) * half_color_max);
            in_color[2] = (uint8_t)((1 + OutputColor[2]) * half_color_max);
            in_color[3] = (uint8_t)((1 + OutputColor[3]) * half_color_max);

            Set_RGBA(in_color);
        }

        inline void GenerateFrom2DPerlinNoise(float value_one, float value_two, bool GenerateAlpha=true) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            float OutputColor[4];
            OutputColor[0] = R_PerlinNoiseGenerator->Noise2D(value_one + r_offset, value_two + r_offset);
            OutputColor[1] = G_PerlinNoiseGenerator->Noise2D(value_one + g_offset, value_two + g_offset);
            OutputColor[2] = B_PerlinNoiseGenerator->Noise2D(value_one + b_offset, value_two + b_offset);
            if (GenerateAlpha) {
                OutputColor[3] = A_PerlinNoiseGenerator->Noise2D(value_one + a_offset, value_two + a_offset);
            } else {
                OutputColor[3] = 1.0f;
            }

            uint8_t in_color[4];
            in_color[0] = (uint8_t)((1 + OutputColor[0]) * half_color_max);
            in_color[1] = (uint8_t)((1 + OutputColor[1]) * half_color_max);
            in_color[2] = (uint8_t)((1 + OutputColor[2]) * half_color_max);
            in_color[3] = (uint8_t)((1 + OutputColor[3]) * half_color_max);

            Set_RGBA(in_color);
        }

        inline void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three, bool GenerateAlpha=true) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            float OutputColor[4];
            OutputColor[0] = R_PerlinNoiseGenerator->Noise3D(value_one + r_offset, value_two + r_offset, value_three + r_offset);
            OutputColor[1] = G_PerlinNoiseGenerator->Noise3D(value_one + g_offset, value_two + g_offset, value_three + g_offset);
            OutputColor[2] = B_PerlinNoiseGenerator->Noise3D(value_one + b_offset, value_two + b_offset, value_three + b_offset);
            if (GenerateAlpha) {
                OutputColor[3] = A_PerlinNoiseGenerator->Noise3D(value_one + a_offset, value_two + a_offset, value_three + a_offset);
            } else {
                OutputColor[3] = 1.0f;
            }

            uint8_t in_color[4];
            in_color[0] = (uint8_t)((1 + OutputColor[0]) * half_color_max);
            in_color[1] = (uint8_t)((1 + OutputColor[1]) * half_color_max);
            in_color[2] = (uint8_t)((1 + OutputColor[2]) * half_color_max);
            in_color[3] = (uint8_t)((1 + OutputColor[3]) * half_color_max);

            Set_RGBA(in_color);
        }

        inline void GenerateFrom1DFractalBrownianMotion(float value, bool GenerateAlpha=true) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            float OutputColor[4];
            OutputColor[0] = R_FractalBrownianMotionGenerator->Noise1D(value + r_offset);
            OutputColor[1] = G_FractalBrownianMotionGenerator->Noise1D(value + g_offset);
            OutputColor[2] = B_FractalBrownianMotionGenerator->Noise1D(value + b_offset);
            if (GenerateAlpha) {
                OutputColor[3] = A_FractalBrownianMotionGenerator->Noise1D(value + a_offset);
            } else {
                OutputColor[3] = 1.0f;
            }

            uint8_t in_color[4];
            in_color[0] = (uint8_t)((1 + OutputColor[0]) * half_color_max);
            in_color[1] = (uint8_t)((1 + OutputColor[1]) * half_color_max);
            in_color[2] = (uint8_t)((1 + OutputColor[2]) * half_color_max);
            in_color[3] = (uint8_t)((1 + OutputColor[3]) * half_color_max);

            Set_RGBA(in_color);
        }

        inline void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two, bool GenerateAlpha=true) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            float OutputColor[4];
            OutputColor[0] = R_FractalBrownianMotionGenerator->Noise2D(value_one + r_offset, value_two + r_offset);
            OutputColor[1] = G_FractalBrownianMotionGenerator->Noise2D(value_one + g_offset, value_two + g_offset);
            OutputColor[2] = B_FractalBrownianMotionGenerator->Noise2D(value_one + b_offset, value_two + b_offset);
            if (GenerateAlpha) {
                OutputColor[3] = A_FractalBrownianMotionGenerator->Noise2D(value_one + a_offset, value_two + a_offset);
            } else {
                OutputColor[3] = 1.0f;
            }

            uint8_t in_color[4];
            in_color[0] = (uint8_t)((1 + OutputColor[0]) * half_color_max);
            in_color[1] = (uint8_t)((1 + OutputColor[1]) * half_color_max);
            in_color[2] = (uint8_t)((1 + OutputColor[2]) * half_color_max);
            in_color[3] = (uint8_t)((1 + OutputColor[3]) * half_color_max);

            Set_RGBA(in_color);
        }

        inline void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three, bool GenerateAlpha=true) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            float OutputColor[4];
            OutputColor[0] = R_FractalBrownianMotionGenerator->Noise3D(value_one + r_offset, value_two + r_offset, value_three + r_offset);
            OutputColor[1] = G_FractalBrownianMotionGenerator->Noise3D(value_one + g_offset, value_two + g_offset, value_three + g_offset);
            OutputColor[2] = B_FractalBrownianMotionGenerator->Noise3D(value_one + b_offset, value_two + b_offset, value_three + b_offset);
            if (GenerateAlpha) {
                OutputColor[3] = A_FractalBrownianMotionGenerator->Noise3D(value_one + a_offset, value_two + a_offset, value_three + a_offset);
            } else {
                OutputColor[3] = 1.0f;
            }

            uint8_t in_color[4];
            in_color[0] = (uint8_t)((1 + OutputColor[0]) * half_color_max);
            in_color[1] = (uint8_t)((1 + OutputColor[1]) * half_color_max);
            in_color[2] = (uint8_t)((1 + OutputColor[2]) * half_color_max);
            in_color[3] = (uint8_t)((1 + OutputColor[3]) * half_color_max);

            Set_RGBA(in_color);
        }
};

class EXPORT CPP_DisplayCoordinateFormat {
    private:
        CPP_Logger* Logger;

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
        CPP_DisplayCoordinateFormat() {
            Logger = new CPP_Logger();
        }

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

            delete Logger;
            Logger = nullptr;
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
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return amplitude;
        }

        void GenerateFromRandom();

        void GenerateFrom1DPerlinNoise(float value);
        void GenerateFrom2DPerlinNoise(float value_one, float value_two);
        void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

        void GenerateFrom1DFractalBrownianMotion(float value);
        void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
        void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

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
                Logger->InternalLogWarn(
                    30,
                    "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
                throw std::runtime_error("Display coordinate not set!");
            }
            out_coordinate[0] = (unsigned int)DisplayCoordinate.x;
            out_coordinate[1] = (unsigned int)DisplayCoordinate.y;
        }

        inline glm::vec2 Get() {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
                throw std::runtime_error("Display coordinate not set!");
            }
            return DisplayCoordinate;
        }

        inline void Get(float* out) {
            if (!IsSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
                throw std::runtime_error("Display coordinate not set!");
            }
            out[0] = DisplayCoordinate.x;
            out[1] = DisplayCoordinate.y;
        }
};

class EXPORT CPP_AngleFormat: public CPP_BasicAngleConverter {
    private:
        CPP_Logger* Logger;

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
        CPP_AngleFormat() {
            Logger = new CPP_Logger();
        }

        ~CPP_AngleFormat() {
            if (Configured) {
                delete PerlinNoiseGenerator;
                delete FractalBrownianMotionGenerator;

                PerlinNoiseGenerator = nullptr;
                FractalBrownianMotionGenerator = nullptr;
            }

            delete Logger;
            Logger = nullptr;
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
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
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

        inline void GenerateFrom1DPerlinNoise(float value) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
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

        inline void GenerateFrom2DPerlinNoise(float value_one, float value_two) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            InternalAngle = PerlinNoiseGenerator->Noise2D(value_one, value_two);
            float converted_in_angle = CPP_AdvancedMathematics::Ranger(InternalAngle, noise_range, angle_range);

            if (converted_in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = converted_in_angle;
            }

            IsSet = true;
        }

        inline void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            InternalAngle = PerlinNoiseGenerator->Noise3D(value_one, value_two, value_three);
            float converted_in_angle = CPP_AdvancedMathematics::Ranger(InternalAngle, noise_range, angle_range);

            if (converted_in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = converted_in_angle;
            }

            IsSet = true;
        }

        inline void GenerateFrom1DFractalBrownianMotion(float value) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
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

        inline void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            InternalAngle = FractalBrownianMotionGenerator->Noise2D(value_one, value_two);
            float converted_in_angle = CPP_AdvancedMathematics::Ranger(InternalAngle, noise_range, angle_range);

            if (converted_in_angle != InternalAngle) {
                Changed = true;
                InternalAngle = converted_in_angle;
            }

            IsSet = true;
        }

        inline void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            InternalAngle = FractalBrownianMotionGenerator->Noise3D(value_one, value_two, value_three);
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
        CPP_Logger* Logger;

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
        CPP_ProportionFormat() {
            Logger = new CPP_Logger();
        }

        ~CPP_ProportionFormat() {
            if (Configured) {
                delete PerlinNoiseGenerator;
                delete FractalBrownianMotionGenerator;

                PerlinNoiseGenerator = nullptr;
                FractalBrownianMotionGenerator = nullptr;
            }

            delete Logger;
            Logger = nullptr;
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
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
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

        inline void GenerateFrom1DPerlinNoise(float value) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
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

        inline void GenerateFrom2DPerlinNoise(float value_one, float value_two) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            InternalProportion = PerlinNoiseGenerator->Noise2D(value_one, value_two);
            float converted_in_proportion = CPP_AdvancedMathematics::Ranger(InternalProportion, noise_range, proportion_range);

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }

        inline void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            InternalProportion = PerlinNoiseGenerator->Noise3D(value_one, value_two, value_three);
            float converted_in_proportion = CPP_AdvancedMathematics::Ranger(InternalProportion, noise_range, proportion_range);

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }

        inline void GenerateFrom1DFractalBrownianMotion(float value) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
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

        inline void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            InternalProportion = FractalBrownianMotionGenerator->Noise2D(value_one, value_two);
            float converted_in_proportion = CPP_AdvancedMathematics::Ranger(InternalProportion, noise_range, proportion_range);

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }

        inline void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
            if (!Configured) {
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }

            InternalProportion = FractalBrownianMotionGenerator->Noise3D(value_one, value_two, value_three);
            float converted_in_proportion = CPP_AdvancedMathematics::Ranger(InternalProportion, noise_range, proportion_range);

            if (converted_in_proportion != InternalProportion) {
                Changed = true;
                InternalProportion = converted_in_proportion;
            }

            IsSet = true;
        }
};