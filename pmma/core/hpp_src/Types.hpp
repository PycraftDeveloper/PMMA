#pragma once
#include "PMMA_Exports.hpp"

#include <fstream>
#include <future>
#include <optional>
#include <random>
#include <thread>

#include <zstd.h>

#include "Internal/Internal.hpp"
#include "Logger.hpp"
#include "Maths.hpp"
#include "Noise/FractalBrownianMotion.hpp"
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

    void InternalLoad();

    inline bool LoadCached(
        const std::string &CachedTexturePath) {
        std::ifstream file(
            CachedTexturePath,
            std::ios::binary);

        if (!file.is_open()) {
            return false;
        }

        char Magic[4];

        file.read(
            Magic,
            sizeof(Magic));

        if (memcmp(Magic, "PMTX", 4) != 0) {
            return false;
        }

        uint32_t Version = 0;

        file.read(
            reinterpret_cast<char *>(&Version),
            sizeof(Version));

        constexpr uint32_t CurrentVersion = 1;

        if (Version != CurrentVersion) {
            return false;
        }

        uint8_t Transparent = 0;

        file.read(
            reinterpret_cast<char *>(&Transparent),
            sizeof(Transparent));

        if (Transparent > 1) {
            return false;
        }

        TextureProperties->Transparent =
            Transparent != 0;

        uint8_t MipCount = 0;

        file.read(
            reinterpret_cast<char *>(&MipCount),
            sizeof(MipCount));

        if (MipCount == 0 ||
            MipCount > 32) {

            return false;
        }

        std::vector<PMMA::Internal::MipData>
            LoadedMipChain;

        LoadedMipChain.reserve(
            MipCount);

        for (uint32_t i = 0;
             i < MipCount;
             i++) {

            PMMA::Internal::MipData mip;

            //
            // Logical mip size.
            //
            file.read(
                reinterpret_cast<char *>(&mip.Size[0]),
                sizeof(uint16_t));

            file.read(
                reinterpret_cast<char *>(&mip.Size[1]),
                sizeof(uint16_t));

            //
            // Padding amount.
            //
            file.read(
                reinterpret_cast<char *>(&mip.Padding),
                sizeof(uint8_t));

            uint32_t CompressedSize = 0;
            uint32_t RawSize = 0;

            file.read(
                reinterpret_cast<char *>(&CompressedSize),
                sizeof(uint32_t));

            file.read(
                reinterpret_cast<char *>(&RawSize),
                sizeof(uint32_t));

            if (mip.Size[0] == 0 ||
                mip.Size[1] == 0) {

                return false;
            }

            uint64_t BlocksX =
                (static_cast<uint64_t>(mip.Size[0]) + 3) / 4;

            uint64_t BlocksY =
                (static_cast<uint64_t>(mip.Size[1]) + 3) / 4;

            uint64_t ExpectedSize =
                BlocksX * BlocksY * 16;

            if (RawSize != ExpectedSize) {
                return false;
            }

            //
            // Safety check before allocation.
            //
            if (CompressedSize == 0 ||
                RawSize == 0) {

                return false;
            }

            std::vector<uint8_t>
                CompressedData(
                    CompressedSize);

            file.read(
                reinterpret_cast<char *>(
                    CompressedData.data()),
                CompressedSize);

            if (file.fail()) {
                return false;
            }

            mip.PixelData.resize(
                RawSize);

            size_t DecompressedSize =
                ZSTD_decompress(
                    mip.PixelData.data(),
                    RawSize,
                    CompressedData.data(),
                    CompressedSize);

            if (ZSTD_isError(DecompressedSize)) {
                std::cout
                    << "Failed to open cache: zstd decompression failed: "
                    << ZSTD_getErrorName(DecompressedSize)
                    << std::endl;

                return false;
            }

            if (DecompressedSize != RawSize) {

                return false;
            }

            LoadedMipChain.push_back(
                std::move(mip));
        }

        if (file.fail()) {
            return false;
        }

        TextureProperties->MipChain =
            std::move(
                LoadedMipChain);

        TextureProperties->MipLevels =
            MipCount;

        return true;
    }

    inline void SaveTextureCache(
        const std::string &path,
        const PMMA::Internal::TextureProperty &texture) {

        std::ofstream file(
            path,
            std::ios::binary);

        if (!file) {
            throw std::runtime_error(
                "Failed to create texture cache.");
        }

        file.write("PMTX", 4);

        uint32_t Version = 1;

        file.write(
            reinterpret_cast<char *>(&Version),
            sizeof(Version));

        const uint8_t Transparent =
            texture.Transparent ? 1 : 0;

        file.write(
            reinterpret_cast<const char *>(&Transparent),
            sizeof(Transparent));

        uint8_t MipCount =
            static_cast<uint8_t>(
                texture.MipChain.size());

        file.write(
            reinterpret_cast<char *>(&MipCount),
            sizeof(MipCount));

        for (const auto &mip : texture.MipChain) {
            file.write(
                reinterpret_cast<const char *>(&mip.Size[0]),
                sizeof(uint16_t));

            file.write(
                reinterpret_cast<const char *>(&mip.Size[1]),
                sizeof(uint16_t));

            file.write(
                reinterpret_cast<const char *>(&mip.Padding),
                sizeof(uint8_t));

            uint32_t rawSize =
                static_cast<uint32_t>(
                    mip.PixelData.size());

            size_t maxCompressedSize =
                ZSTD_compressBound(
                    rawSize);

            std::vector<uint8_t> compressedData(
                maxCompressedSize);

            size_t compressedSize =
                ZSTD_compress(
                    compressedData.data(),
                    compressedData.size(),
                    mip.PixelData.data(),
                    rawSize,
                    3); // zstd level

            if (ZSTD_isError(compressedSize)) {
                throw std::runtime_error(
                    ZSTD_getErrorName(compressedSize));
            }

            uint32_t compressedSize32 =
                static_cast<uint32_t>(
                    compressedSize);

            file.write(
                reinterpret_cast<char *>(&compressedSize32),
                sizeof(uint32_t));

            file.write(
                reinterpret_cast<char *>(&rawSize),
                sizeof(uint32_t));

            file.write(
                reinterpret_cast<const char *>(
                    compressedData.data()),
                compressedSize32);
        }
    }

    void Unload();

    void Enable();

    inline void Disable() {
        IsTextureEnabled = false;
    }

    inline bool IsEnabled() {
        return IsTextureEnabled;
    }

    void GetSize(uint16_t *size);

    unsigned char GetChannels();

    uint32_t GetReferences();

    bool IsLoaded() {
        return TextureProperties != nullptr;
    }

    uint16_t GetWidth();
    uint16_t GetHeight();

    std::string GetPath();
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

    void SetColorName(std::string color_name);
    void SetColorName(std::string_view color_name);

    void Set_RGBA(uint8_t *in_color);
    void Set_RGB(uint8_t *in_color);

    void Set_HEX(std::string input_color);
    void Set_HEXA(std::string input_color);

    void Get_RGBA(uint8_t *out_color);
    void Get_RGB(uint8_t *out_color);

    std::string Get_HEXA();
    std::string Get_HEX();

    bool IsTransparent();
    bool IsOpaque();
    bool IsClear();
};

class EXPORT Angle {
private:
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

    uint32_t GetSeed();

    uint32_t GetOctaves();

    float GetFrequency();

    float GetAmplitude();

    inline void GenerateFromRandom() {
        float converted_in_angle = PMMA::Maths::RandomFloat(angle_range);

        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    void GenerateFrom1DPerlinNoise(float value);
    void GenerateFrom2DPerlinNoise(float value_one, float value_two);
    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

    void GenerateFrom1DFractalBrownianMotion(float value);
    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

    inline bool GetSet() {
        return IsSet;
    }

    inline bool GetChangedToggle() {
        bool OldChanged = Changed;
        Changed = false;
        return OldChanged;
    }

    inline void SetRadians(float in_angle) {
        if (in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = in_angle;
        }

        IsSet = true;
    }

    inline void SetDegrees(float in_angle) {
        float converted_in_angle = in_angle * DEGREES_TO_RADIANS;
        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    float GetRadians();
    float GetDegrees();
};

class EXPORT Proportion {
private:
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

    uint32_t GetSeed();
    uint32_t GetOctaves();
    float GetFrequency();
    float GetAmplitude();

    inline void GenerateFromRandom() {
        float converted_in_proportion = PMMA::Maths::RandomFloat(proportion_range);

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    void GenerateFrom1DPerlinNoise(float value);
    void GenerateFrom2DPerlinNoise(float value_one, float value_two);
    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

    void GenerateFrom1DFractalBrownianMotion(float value);
    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

    inline bool GetSet() {
        return IsSet;
    }

    inline bool GetChangedToggle() {
        bool OldChanged = Changed;
        Changed = false;
        return OldChanged;
    }

    inline void SetPercentage(float in_proportion) {
        float converted_in_proportion = in_proportion / 100;

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    inline void SetDecimal(float in_proportion) {
        if (in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = in_proportion;
        }

        IsSet = true;
    }

    inline float GetPercentage();
    inline float GetDecimal();
};
} // namespace PMMA::Types

namespace PMMA::Types::TwoD {
class EXPORT Coordinate {
private:
    PMMA::Noise::PerlinNoise *X_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *Y_PerlinNoiseGenerator = nullptr;

    PMMA::Noise::FractalBrownianMotion *X_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *Y_FractalBrownianMotionGenerator = nullptr;

    PMMA::FastRandom *RandomCoordGenerator = nullptr;

    int16_t coordinate[2] = {0, 0}; // Default display coordinate is (0, 0)
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

    inline bool GetCoordinateSet() {
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

    inline void SetCoordinate(int16_t *in_coordinate) {
        if (in_coordinate[0] != coordinate[0] || in_coordinate[1] != coordinate[1]) {
            Changed = true;
            coordinate[0] = in_coordinate[0];
            coordinate[1] = in_coordinate[1];
        }

        X_IsSet = true;
        Y_IsSet = true;
    }

    inline void SetX(int16_t in_coordinate) {
        if (in_coordinate != coordinate[0]) {
            Changed = true;
            coordinate[0] = in_coordinate;
        }

        X_IsSet = true;
    }

    inline void SetY(int16_t in_coordinate) {
        if (in_coordinate != coordinate[1]) {
            Changed = true;
            coordinate[1] = in_coordinate;
        }

        Y_IsSet = true;
    }

    void GetCoordinate(int16_t *out);
    int16_t GetX();
    int16_t GetY();
};

class EXPORT Size {
public:
    PMMA::Types::Texture *Texture;
    Proportion HorizontalScale;
    Proportion VerticalScale;

private:
    PMMA::Noise::PerlinNoise *X_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *Y_PerlinNoiseGenerator = nullptr;

    PMMA::Noise::FractalBrownianMotion *X_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *Y_FractalBrownianMotionGenerator = nullptr;

    PMMA::FastRandom *RandomSizeGenerator = nullptr;

    uint16_t size[2] = {0, 0}; // Default display coordinate is (0, 0)
    uint16_t scaled_size[2] = {0, 0};
    uint16_t DisplaySize[2];

    uint32_t seed;
    uint32_t octaves;
    float frequency;
    float amplitude;

    float offset_range[2] = {0.f, 1.f};
    float x_offset = PMMA::Maths::RandomFloat(offset_range);
    float y_offset = PMMA::Maths::RandomFloat(offset_range);

    const float noise_range[2] = {-1.f, 1.f};

    uint16_t Radius = 0;

    bool X_IsSet = false;
    bool Y_IsSet = false;
    bool Changed = true;
    bool ScaledSizeSet = false;
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

    inline bool GetScaledChangedToggle() {
        bool ScaleChanged = HorizontalScale.GetChangedToggle() || VerticalScale.GetChangedToggle();
        if (ScaleChanged) {
            ScaledSizeSet = false;
        }
        bool OldChanged = Changed || ScaleChanged;
        Changed = false;
        return OldChanged;
    }

    inline bool GetSizeSet() {
        return X_IsSet && Y_IsSet;
    }

    inline bool GetWidthSet() {
        return X_IsSet;
    }

    inline bool GetHeightSet() {
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

    inline void SetSize(uint16_t *in_size) {
        if (in_size[0] != size[0] || in_size[1] != size[1]) {
            Changed = true;
            ScaledSizeSet = false;
            size[0] = in_size[0];
            size[1] = in_size[1];

            Radius = static_cast<uint16_t>(PMMA::Maths::PythagoreanDistance(size[0], size[1]));
        }

        X_IsSet = true;
        Y_IsSet = true;
    }

    inline void SetWidth(uint16_t in_size) {
        if (in_size != size[0]) {
            Changed = true;
            ScaledSizeSet = false;
            size[0] = in_size;

            Radius = static_cast<uint16_t>(PMMA::Maths::PythagoreanDistance(size[0], size[1]));
        }

        X_IsSet = true;
    }

    inline void SetHeight(uint16_t in_size) {
        if (in_size != size[1]) {
            Changed = true;
            ScaledSizeSet = false;
            size[1] = in_size;

            Radius = static_cast<uint16_t>(PMMA::Maths::PythagoreanDistance(size[0], size[1]));
        }

        Y_IsSet = true;
    }

    void SetSizeToTextureSize();
    void SetWidthToTextureWidth();
    void SetWidthToTextureHeight();

    void GetSize(uint16_t *out);
    uint16_t GetWidth();
    uint16_t GetHeight();

    void GetScaledSize(uint16_t *out);
    uint16_t GetScaledWidth();
    uint16_t GetScaledHeight();

    inline uint16_t GetRadius() {
        return Radius;
    }

    inline void SetRadius(uint16_t in_radius) {
        in_radius *= 2;
        uint16_t new_size[2] = {in_radius, in_radius};
        SetSize(new_size);
    }
};
}; // namespace PMMA::Types::TwoD