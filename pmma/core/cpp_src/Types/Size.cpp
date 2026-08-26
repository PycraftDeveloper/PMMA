#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/Internal.hpp"
#include "Internal/LoggingManager.hpp"

#include "Types/Size.hpp"

#include "Display.hpp"

inline void SizeConfiguredCheck(bool Configured) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
}

PMMA::Types::TwoD::Size::Size() {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);

    RandomSizeGenerator = PMMA::Core::RandomGenerator;

    PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);

    HorizontalScale.SetDecimal(1.0f);
    VerticalScale.SetDecimal(1.0f);
}

void PMMA::Types::TwoD::Size::GetSize(uint16_t *out) {
    bool SizeSet = GetSizeSet();
    bool TextureLoaded = Texture->IsLoaded();
    if (!(SizeSet || TextureLoaded)) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a size - please set a \
size before attempting to get it.");
        throw std::runtime_error("Size not set!");
    }

    if (!SizeSet) {
        SetSizeToTextureSize();
    }

    float scale_x = HorizontalScale.GetDecimal();
    float scale_y = VerticalScale.GetDecimal();

    out[0] = size[0] * scale_x;
    out[1] = size[1] * scale_y;
}

void PMMA::Types::TwoD::Size::GetScaledSize(uint16_t *out) {
    if (ScaledSizeSet && !HorizontalScale.GetChangedToggle() && !VerticalScale.GetChangedToggle()) {
        out[0] = scaled_size[0];
        out[1] = scaled_size[1];
        return;
    }

    bool SizeSet = GetSizeSet();
    bool TextureLoaded = Texture->IsLoaded();
    if (!(SizeSet || TextureLoaded)) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a size - please set a \
size before attempting to get it.");
        throw std::runtime_error("Size not set!");
    }

    if (!SizeSet) {
        SetSizeToTextureSize();
    }

    float scale_x = HorizontalScale.GetDecimal();
    float scale_y = VerticalScale.GetDecimal();

    scaled_size[0] = size[0] * scale_x;
    scaled_size[1] = size[1] * scale_y;

    out[0] = scaled_size[0];
    out[1] = scaled_size[1];

    ScaledSizeSet = true;
}

uint16_t PMMA::Types::TwoD::Size::GetWidth() {
    if (!GetWidthSet()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a size - please set a \
size before attempting to get it.");
        throw std::runtime_error("Size not set!");
    }

    return size[0];
}

uint16_t PMMA::Types::TwoD::Size::GetHeight() {
    if (!GetHeightSet()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a size - please set a \
size before attempting to get it.");
        throw std::runtime_error("Size not set!");
    }

    return size[1];
}

uint32_t PMMA::Types::TwoD::Size::GetSeed() {
    SizeConfiguredCheck(Configured);
    return seed;
}

uint32_t PMMA::Types::TwoD::Size::GetOctaves() {
    SizeConfiguredCheck(Configured);
    return octaves;
}

float PMMA::Types::TwoD::Size::GetFrequency() {
    SizeConfiguredCheck(Configured);
    return frequency;
}

float PMMA::Types::TwoD::Size::GetAmplitude() {
    SizeConfiguredCheck(Configured);
    return amplitude;
}

void PMMA::Types::TwoD::Size::Configure(PMMA::Types::Configure_Kwargs kwargs) {
    uint32_t new_seed;

    if (!kwargs.seed.has_value()) {
        PMMA::FastRandom TempRandomGenerator;
        new_seed = TempRandomGenerator.Next();
    } else {
        new_seed = kwargs.seed.value();
    }

    X_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed);
    Y_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed + 1);

    X_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
    Y_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed + 1, kwargs.octaves, kwargs.frequency, kwargs.amplitude);

    RandomSizeGenerator = new PMMA::FastRandom();
    RandomSizeGenerator->SetSeed(new_seed);

    seed = new_seed;
    octaves = kwargs.octaves;
    frequency = kwargs.frequency;
    amplitude = kwargs.amplitude;
    Configured = true;
}

void PMMA::Types::TwoD::Size::GenerateFromRandom() {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);

    if (PMMA::Core::ActiveDisplayInstance->DisplaySizeChanged) {
        PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
    }

    uint16_t new_size[2];
    new_size[0] = RandomSizeGenerator->Next(DisplaySize[0]);
    new_size[1] = RandomSizeGenerator->Next(DisplaySize[1]);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::GenerateFrom1DPerlinNoise(float value) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    SizeConfiguredCheck(Configured);

    uint16_t new_size[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise1D(value + x_offset);
    new_size[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise1D(value + y_offset);
    new_size[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    SizeConfiguredCheck(Configured);

    uint16_t new_size[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_size[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_size[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    SizeConfiguredCheck(Configured);

    uint16_t new_size[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_size[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_size[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::GenerateFrom1DFractalBrownianMotion(float value) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    SizeConfiguredCheck(Configured);

    uint16_t new_size[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise1D(value + x_offset);
    new_size[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise1D(value + y_offset);
    new_size[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    SizeConfiguredCheck(Configured);

    uint16_t new_size[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_size[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_size[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    SizeConfiguredCheck(Configured);

    uint16_t new_size[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_size[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_size[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::SetSizeToTextureSize() {
    uint16_t new_size[2];
    Texture->GetSize(new_size);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::SetWidthToTextureWidth() {
    SetWidth(Texture->GetWidth());
}

void PMMA::Types::TwoD::Size::SetWidthToTextureHeight() {
    SetHeight(Texture->GetHeight());
}