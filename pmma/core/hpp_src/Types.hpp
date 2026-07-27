#pragma once
#include "PMMA_Exports.hpp"

#include <glm/glm.hpp>
#include <optional>
#include <random>
#include <thread>

#include "Internal/Internal.hpp"
#include "Logger.hpp"
#include "Maths.hpp"
#include "Noise/FractalBrownianMotion.hpp"
#include "PMMA_Core.hpp"
#include "Random.hpp"

namespace PMMA::Types {
struct Configure_Kwargs {
    std::optional<uint32_t> seed = std::nullopt;
    uint32_t octaves = 2;
    float frequency = 0.75f;
    float amplitude = 1.0f;
};

class EXPORT Texture {
private:
    std::string Path = "";

public:
    PMMA::Internal::TextureProperty *TextureProperties;
    bool IsTextureEnabled = false;

    ~Texture();

    void Load(std::string TexturePath);
    void Load();

    void Unload();

    void Enable();

    inline void Disable() {
        IsTextureEnabled = false;
    }

    inline bool IsEnabled() {
        return IsTextureEnabled;
    }

    void GetSize(uint16_t *size);

    void GetPositionInAtlas(uintptr_t RenderPipelineInstance_ID, uint16_t *position);

    unsigned char GetChannels();

    uint32_t GetReferences();

    bool IsLoaded() {
        return TextureProperties != nullptr;
    }
};

class EXPORT Color {
private:
    PMMA::Noise::PerlinNoise *R_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *G_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *B_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *A_PerlinNoiseGenerator = nullptr;

    PMMA::Noise::FractalBrownianMotion *R_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *G_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *B_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *A_FractalBrownianMotionGenerator = nullptr;

    PMMA::FastRandom *RandomColorGenerator = nullptr;

    uint8_t InternalColor[4] = {0, 0, 0, 255}; // Default is black with full opacity

    uint32_t seed;
    uint32_t octaves;

    float frequency;
    float amplitude;
    float half_color_max = 255.f / 2.f;

    float offset_range[2] = {0.f, 1.f};
    float r_offset = PMMA::Maths::RandomFloat(offset_range);
    float g_offset = PMMA::Maths::RandomFloat(offset_range);
    float b_offset = PMMA::Maths::RandomFloat(offset_range);
    float a_offset = PMMA::Maths::RandomFloat(offset_range);

    const float noise_range[2] = {-1.f, 1.f};
    const float color_range[2] = {0, 255};

    bool Configured = false;
    bool IsSet = false;
    bool Changed = true;
    bool InternalChanged = true;

public:
    bool LinkedToDisplayBackground = false;

    Color();

    ~Color() {
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

            delete RandomColorGenerator;
            RandomColorGenerator = nullptr;
        }
    }

    inline void Configure(Configure_Kwargs kwargs = {}) {
        uint32_t new_seed;

        if (!kwargs.seed.has_value()) {
            PMMA::FastRandom TempRandomGenerator;
            new_seed = TempRandomGenerator.Next();
        } else {
            new_seed = kwargs.seed.value();
        }

        R_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed);
        G_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed + 1);
        B_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed + 2);
        A_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed + 3);

        R_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
        G_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed + 1, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
        B_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed + 2, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
        A_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed + 3, kwargs.octaves, kwargs.frequency, kwargs.amplitude);

        RandomColorGenerator = new PMMA::FastRandom();
        RandomColorGenerator->SetSeed(new_seed);

        seed = new_seed;
        octaves = kwargs.octaves;
        frequency = kwargs.frequency;
        amplitude = kwargs.amplitude;
        Configured = true;
    }

    uint32_t GetSeed();

    uint32_t GetOctaves();

    float GetFrequency();

    float GetAmplitude();

    inline void GenerateFromRandom(bool GenerateAlpha = true) {
        uint8_t in_color[4];
        uint32_t packedColor = RandomColorGenerator->Next();

        in_color[0] = static_cast<uint8_t>((packedColor >> 24) & 0xFF); // R
        in_color[1] = static_cast<uint8_t>((packedColor >> 16) & 0xFF); // G
        in_color[2] = static_cast<uint8_t>((packedColor >> 8) & 0xFF);  // B

        if (GenerateAlpha) {
            in_color[3] = static_cast<uint8_t>(packedColor & 0xFF);
        } else {
            in_color[3] = 255;
        }

        Set_RGBA(in_color);
    }

    void GenerateFrom1DPerlinNoise(float value, bool GenerateAlpha = true);

    void GenerateFrom2DPerlinNoise(float value_one, float value_two, bool GenerateAlpha = true);

    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three, bool GenerateAlpha = true);

    void GenerateFrom1DFractalBrownianMotion(float value, bool GenerateAlpha = true);

    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two, bool GenerateAlpha = true);

    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three, bool GenerateAlpha = true);

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

    void Set_ColorName(std::string color_name);
    void Set_ColorName(std::string_view color_name);

    void Set_RGBA(uint8_t *in_color);
    void Set_RGB(uint8_t *in_color);

    void Set_HEX(std::string input_color);
    void Set_HEXA(std::string input_color);

    void Get_RGBA(uint8_t *out_color);
    void Get_RGB(uint8_t *out_color);

    std::string Get_HEXA();
    std::string Get_HEX();
};

class EXPORT Angle {
private:
    PMMA::Logger *Logger;
    PMMA::Noise::PerlinNoise *PerlinNoiseGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *FractalBrownianMotionGenerator = nullptr;

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
    ~Angle() {
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

    inline void Configure(Configure_Kwargs kwargs = {}) {
        uint32_t new_seed;

        if (!kwargs.seed.has_value()) {
            PMMA::FastRandom TempRandomGenerator;
            new_seed = TempRandomGenerator.Next();
        } else {
            new_seed = kwargs.seed.value();
        }

        PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed);
        FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed, kwargs.octaves, kwargs.frequency, kwargs.amplitude);

        srand(new_seed);

        seed = new_seed;
        octaves = kwargs.octaves;
        frequency = kwargs.frequency;
        amplitude = kwargs.amplitude;
        Configured = true;
    }

    inline uint32_t GetSeed() {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }
        return seed;
    }

    inline uint32_t GetOctaves() {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }
        return octaves;
    }

    inline float GetFrequency() {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }
        return frequency;
    }

    inline float GetAmplitude() {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }
        return amplitude;
    }

    inline void GenerateFromRandom() {
        float converted_in_angle = PMMA::Maths::RandomFloat(angle_range);

        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    inline void GenerateFrom1DPerlinNoise(float value) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalAngle = PerlinNoiseGenerator->Noise1D(value);
        float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    inline void GenerateFrom2DPerlinNoise(float value_one, float value_two) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalAngle = PerlinNoiseGenerator->Noise2D(value_one, value_two);
        float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    inline void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalAngle = PerlinNoiseGenerator->Noise3D(value_one, value_two, value_three);
        float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    inline void GenerateFrom1DFractalBrownianMotion(float value) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalAngle = FractalBrownianMotionGenerator->Noise1D(value);
        float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    inline void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalAngle = FractalBrownianMotionGenerator->Noise2D(value_one, value_two);
        float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    inline void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalAngle = FractalBrownianMotionGenerator->Noise3D(value_one, value_two, value_three);
        float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

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
                Logger = new PMMA::Logger();
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
                Logger = new PMMA::Logger();
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

class EXPORT Proportion {
private:
    PMMA::Logger *Logger;

    PMMA::Noise::PerlinNoise *PerlinNoiseGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *FractalBrownianMotionGenerator = nullptr;

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
    ~Proportion() {
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

    inline void Configure(Configure_Kwargs kwargs = {}) {
        uint32_t new_seed;

        if (!kwargs.seed.has_value()) {
            PMMA::FastRandom TempRandomGenerator;
            new_seed = TempRandomGenerator.Next();
        } else {
            new_seed = kwargs.seed.value();
        }

        PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed);
        FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed, kwargs.octaves, kwargs.frequency, kwargs.amplitude);

        srand(new_seed);

        seed = new_seed;
        octaves = kwargs.octaves;
        frequency = kwargs.frequency;
        amplitude = kwargs.amplitude;
        Configured = true;
    }

    inline uint32_t GetSeed() {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }
        return seed;
    }

    inline uint32_t GetOctaves() {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }
        return octaves;
    }

    inline float GetFrequency() {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }
        return frequency;
    }

    inline float GetAmplitude() {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }
        return amplitude;
    }

    inline void GenerateFromRandom() {
        float converted_in_proportion = PMMA::Maths::RandomFloat(proportion_range);

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    inline void GenerateFrom1DPerlinNoise(float value) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalProportion = PerlinNoiseGenerator->Noise1D(value);
        float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    inline void GenerateFrom2DPerlinNoise(float value_one, float value_two) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalProportion = PerlinNoiseGenerator->Noise2D(value_one, value_two);
        float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    inline void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalProportion = PerlinNoiseGenerator->Noise3D(value_one, value_two, value_three);
        float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    inline void GenerateFrom1DFractalBrownianMotion(float value) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalProportion = FractalBrownianMotionGenerator->Noise1D(value);
        float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    inline void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalProportion = FractalBrownianMotionGenerator->Noise2D(value_one, value_two);
        float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    inline void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
        if (!Configured) {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }
            Logger->InternalLogError(
                13,
                "You need to configure this component before calling this.");
            throw std::runtime_error("You need to configure this component first!");
        }

        InternalProportion = FractalBrownianMotionGenerator->Noise3D(value_one, value_two, value_three);
        float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

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
                Logger = new PMMA::Logger();
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
                Logger = new PMMA::Logger();
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
} // namespace PMMA::Types

namespace PMMA::Types::TwoD {
struct Coordinate_Configure_Kwargs {
    std::optional<uint32_t> seed = std::nullopt;
    uint32_t octaves = 2;
    float frequency = 0.75f;
    float amplitude = 1.0f;
};

class EXPORT Coordinate {
private:
    PMMA::Noise::PerlinNoise *X_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *Y_PerlinNoiseGenerator = nullptr;

    PMMA::Noise::FractalBrownianMotion *X_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *Y_FractalBrownianMotionGenerator = nullptr;

    uint16_t coordinate[2] = {0, 0}; // Default display coordinate is (0, 0)

    PMMA::FastRandom *RandomCoordGenerator = nullptr;
    uint16_t DisplaySize[2];

    uint32_t seed;
    uint32_t octaves;
    float frequency;
    float amplitude;

    float offset_range[2] = {0.f, 1.f};
    float x_offset = PMMA::Maths::RandomFloat(offset_range);
    float y_offset = PMMA::Maths::RandomFloat(offset_range);

    const float noise_range[2] = {-1.f, 1.f};

    bool X_IsSet = false;
    bool Y_IsSet = false;
    bool Changed = true;
    bool Configured = false;

public:
    Coordinate();

    ~Coordinate() {
        if (Configured) {
            delete X_PerlinNoiseGenerator;
            delete Y_PerlinNoiseGenerator;

            delete X_FractalBrownianMotionGenerator;
            delete Y_FractalBrownianMotionGenerator;

            X_PerlinNoiseGenerator = nullptr;
            Y_PerlinNoiseGenerator = nullptr;

            X_FractalBrownianMotionGenerator = nullptr;
            Y_FractalBrownianMotionGenerator = nullptr;

            delete RandomCoordGenerator;
            RandomCoordGenerator = nullptr;
        }
    }

    void Configure(PMMA::Types::Configure_Kwargs kwargs = {});

    inline bool GetChangedToggle() {
        bool OldChanged = Changed;
        Changed = false;
        return OldChanged;
    }

    inline bool GetSet() {
        return X_IsSet && Y_IsSet;
    }

    inline bool Get_X_Set() {
        return X_IsSet;
    }

    inline bool Get_Y_Set() {
        return Y_IsSet;
    }

    uint32_t GetSeed();
    uint32_t GetOctaves();
    float GetFrequency();
    float GetAmplitude();

    void Center();
    void CenterHorizontal();
    void CenterVertical();

    void GenerateFromRandom();

    void GenerateFrom1DPerlinNoise(float value);
    void GenerateFrom2DPerlinNoise(float value_one, float value_two);
    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

    void GenerateFrom1DFractalBrownianMotion(float value);
    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

    inline void Set(uint16_t *in_coordinate) {
        if (in_coordinate[0] != coordinate[0] || in_coordinate[1] != coordinate[1]) {
            Changed = true;
            coordinate[0] = in_coordinate[0];
            coordinate[1] = in_coordinate[1];
        }

        X_IsSet = true;
        Y_IsSet = true;
    }

    inline void Set_X(uint16_t in_coordinate) {
        if (in_coordinate != coordinate[0]) {
            Changed = true;
            coordinate[0] = in_coordinate;
        }

        X_IsSet = true;
    }

    inline void Set_Y(uint16_t in_coordinate) {
        if (in_coordinate != coordinate[1]) {
            Changed = true;
            coordinate[1] = in_coordinate;
        }

        Y_IsSet = true;
    }

    void Get(uint16_t *out);
    uint16_t GetX();
    uint16_t GetY();
};

class EXPORT Size {
private:
    PMMA::Noise::PerlinNoise *X_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *Y_PerlinNoiseGenerator = nullptr;

    PMMA::Noise::FractalBrownianMotion *X_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *Y_FractalBrownianMotionGenerator = nullptr;

    uint16_t size[2] = {0, 0}; // Default display coordinate is (0, 0)

    PMMA::FastRandom *RandomSizeGenerator = nullptr;
    uint16_t DisplaySize[2];

    uint32_t seed;
    uint32_t octaves;
    float frequency;
    float amplitude;

    float offset_range[2] = {0.f, 1.f};
    float x_offset = PMMA::Maths::RandomFloat(offset_range);
    float y_offset = PMMA::Maths::RandomFloat(offset_range);

    const float noise_range[2] = {-1.f, 1.f};

    bool X_IsSet = false;
    bool Y_IsSet = false;
    bool Changed = true;
    bool Configured = false;

public:
    Size();

    ~Size() {
        if (Configured) {
            delete X_PerlinNoiseGenerator;
            delete Y_PerlinNoiseGenerator;

            delete X_FractalBrownianMotionGenerator;
            delete Y_FractalBrownianMotionGenerator;

            X_PerlinNoiseGenerator = nullptr;
            Y_PerlinNoiseGenerator = nullptr;

            X_FractalBrownianMotionGenerator = nullptr;
            Y_FractalBrownianMotionGenerator = nullptr;

            delete RandomSizeGenerator;
            RandomSizeGenerator = nullptr;
        }
    }

    void Configure(PMMA::Types::Configure_Kwargs kwargs = {});

    inline bool GetChangedToggle() {
        bool OldChanged = Changed;
        Changed = false;
        return OldChanged;
    }

    inline bool GetSet() {
        return X_IsSet && Y_IsSet;
    }

    inline bool Get_X_Set() {
        return X_IsSet;
    }

    inline bool Get_Y_Set() {
        return Y_IsSet;
    }

    uint32_t GetSeed();
    uint32_t GetOctaves();
    float GetFrequency();
    float GetAmplitude();

    void GenerateFromRandom();

    void GenerateFrom1DPerlinNoise(float value);
    void GenerateFrom2DPerlinNoise(float value_one, float value_two);
    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

    void GenerateFrom1DFractalBrownianMotion(float value);
    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

    inline void Set(uint16_t *in_size) {
        if (in_size[0] != size[0] || in_size[1] != size[1]) {
            Changed = true;
            size[0] = in_size[0];
            size[1] = in_size[1];
        }

        X_IsSet = true;
        Y_IsSet = true;
    }

    inline void Set_X(uint16_t in_size) {
        if (in_size != size[0]) {
            Changed = true;
            size[0] = in_size;
        }

        X_IsSet = true;
    }

    inline void Set_Y(uint16_t in_size) {
        if (in_size != size[1]) {
            Changed = true;
            size[1] = in_size;
        }

        Y_IsSet = true;
    }

    void Get(uint16_t *out);
    uint16_t GetX();
    uint16_t GetY();
};
}; // namespace PMMA::Types::TwoD