#pragma once
#include "PMMA_Exports.hpp"

#include <glm/glm.hpp>
#include <random>
#include <thread>

#include "FractalBrownianMotion.hpp"
#include "AdvancedMathematics.hpp"
#include "Logger.hpp"
#include "Random.hpp"

class EXPORT CPP_Color {
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

        CPP_FastRandom* RandomColorGenerator = nullptr;

        uint8_t InternalColor[4] = {0, 0, 0, 0}; // Default is black with full opacity

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
        bool IsSet = false;
        bool Changed = true;
        bool InternalChanged = true;

    public:
        CPP_Color();

        ~CPP_Color() {
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

            delete RandomColorGenerator;
            RandomColorGenerator = nullptr;

            if (Logger != nullptr) {
                delete Logger;
                Logger = nullptr;
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

            RandomColorGenerator->SetSeed(new_seed);

            seed = new_seed;
            octaves = new_octaves;
            frequency = new_frequency;
            amplitude = new_amplitude;
            Configured = true;
        }

        inline uint32_t GetSeed() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return amplitude;
        }

        inline void GenerateFromRandom(bool GenerateAlpha=true) {
            uint8_t in_color[4];
            uint32_t packedColor = RandomColorGenerator->Next();

            in_color[0] = static_cast<uint8_t>((packedColor >> 24) & 0xFF); // R
            in_color[1] = static_cast<uint8_t>((packedColor >> 16) & 0xFF); // G
            in_color[2] = static_cast<uint8_t>((packedColor >> 8)  & 0xFF); // B

            if (GenerateAlpha) {
                in_color[3] = static_cast<uint8_t>(packedColor & 0xFF);
            } else {
                in_color[3] = 255;
            }

            Set_RGBA(in_color);
        }

        inline void GenerateFrom1DPerlinNoise(float value, bool GenerateAlpha=true) {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
            if (Logger == nullptr) {
                Logger = new CPP_Logger();
            }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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

class EXPORT CPP_DisplayCoordinate {
    private:
        CPP_Logger* Logger = nullptr;

        CPP_PerlinNoise* X_PerlinNoiseGenerator = nullptr;
        CPP_PerlinNoise* Y_PerlinNoiseGenerator = nullptr;

        CPP_FractalBrownianMotion* X_FractalBrownianMotionGenerator = nullptr;
        CPP_FractalBrownianMotion* Y_FractalBrownianMotionGenerator = nullptr;

        float DisplayCoordinate[2] = {0.f, 0.f}; // Default display coordinate is (0, 0)

        CPP_FastRandom* RandomCoordGenerator = nullptr;
        int DisplaySize[2];

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float offset_range[2] = {0.f, 1.f};
        float x_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);
        float y_offset = CPP_AdvancedMathematics::RandomFloat(offset_range);

        const float noise_range[2] = {-1.f, 1.f};

        bool IsSet = false;
        bool Changed = true;
        bool Configured = false;

    public:
        CPP_DisplayCoordinate();

        ~CPP_DisplayCoordinate() {
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

            delete RandomCoordGenerator;
            RandomCoordGenerator = nullptr;

            if (Logger != nullptr) {
                delete Logger;
                Logger = nullptr;
            }
        }

        void Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude);

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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return amplitude;
        }

        void SetCentered();

        void GenerateFromRandom();

        void GenerateFrom1DPerlinNoise(float value);
        void GenerateFrom2DPerlinNoise(float value_one, float value_two);
        void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

        void GenerateFrom1DFractalBrownianMotion(float value);
        void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
        void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

        inline void Set(float* in_coordinate) {
            if (in_coordinate[0] != DisplayCoordinate[0] || in_coordinate[1] != DisplayCoordinate[1]) {
                Changed = true;
                DisplayCoordinate[0] = in_coordinate[0];
                DisplayCoordinate[1] = in_coordinate[1];
            }

            IsSet = true;
        }

        inline void Get(float* out) {
            if (!IsSet) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogWarn(
                    30,
                    "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
                throw std::runtime_error("Display coordinate not set!");
            }

            out[0] = DisplayCoordinate[0];
            out[1] = DisplayCoordinate[1];
        }
};

class EXPORT CPP_Angle {
    private:
        CPP_Logger* Logger;
        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float InternalAngle = 0.f; // Default angle is 0 radians
        const float RADIANS_TO_DEGREES = 180.f / 3.14159265358979323846f;
        const float DEGREES_TO_RADIANS = 3.14159265358979323846f / 180.f;

        const float noise_range[2] = {-1.f, 1.f};
        const float angle_range[2] = {0.f, 3.14159265358979323846f * 2};

        bool Configured = false;
        bool Changed = true;
        bool IsSet = false;

    public:
        ~CPP_Angle() {
            if (Configured) {
                delete PerlinNoiseGenerator;
                delete FractalBrownianMotionGenerator;

                PerlinNoiseGenerator = nullptr;
                FractalBrownianMotionGenerator = nullptr;
            }

            if (Logger != nullptr) {
                delete Logger;
                Logger = nullptr;
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
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogWarn(
                    30,
                    "You have not set an angle - please set an angle \
before attempting to get it.");

                throw std::runtime_error("Angle not set!");
            }
            return InternalAngle * RADIANS_TO_DEGREES;
        }
};

class EXPORT CPP_Proportion {
    private:
        CPP_Logger* Logger;

        CPP_PerlinNoise* PerlinNoiseGenerator = nullptr;
        CPP_FractalBrownianMotion* FractalBrownianMotionGenerator = nullptr;

        uint32_t seed;
        uint32_t octaves;
        float frequency;
        float amplitude;

        float InternalProportion = 0.f; // Default proportion is 0 (0%)

        const float noise_range[2] = {-1.f, 1.f};
        const float proportion_range[2] = {0.f, 1.f};

        bool Configured = false;
        bool IsSet = false;
        bool Changed = true;

    public:
        ~CPP_Proportion() {
            if (Configured) {
                delete PerlinNoiseGenerator;
                delete FractalBrownianMotionGenerator;

                PerlinNoiseGenerator = nullptr;
                FractalBrownianMotionGenerator = nullptr;
            }

            if (Logger != nullptr) {
                delete Logger;
                Logger = nullptr;
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
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return seed;
        }

        inline uint32_t GetOctaves() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return octaves;
        }

        inline float GetFrequency() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    13,
                    "You need to configure this component before calling this.");
                throw runtime_error("You need to configure this component first!");
            }
            return frequency;
        }

        inline float GetAmplitude() {
            if (!Configured) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
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
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogWarn(
                    30,
                    "You have not set a proportion - please set a proportion \
before attempting to get it.");

                throw std::runtime_error("Proportion not set!");
            }
            return InternalProportion;
        }
};