#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/Internal.hpp"
#include "Internal/LoggingManager.hpp"

#include "Types/Color.hpp"

#include "Display.hpp"

inline void ColorConfiguredCheck(bool Configured) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
}

inline void ColorSetCheck(bool IsSet) {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a color - please set a color \
before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }
}

PMMA::Types::Color::Color() {
    RandomColorGenerator = PMMA::Core::RandomGenerator;
}

void PMMA::Types::Color::SetColorName(std::string color_name) {
    std::optional<std::array<uint8_t, 3>> Color = PMMA::Internal::FindColor(color_name);

    if (!Color.has_value()) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            60,
            "The color name '" + color_name + "' is not recognized.");
        throw std::runtime_error("Unrecognized color name!");
    }

    auto &rgb = Color.value();
    uint8_t in_color[4] = {rgb[0], rgb[1], rgb[2], 255};
    Set_RGBA(in_color);
}

void PMMA::Types::Color::SetColorName(std::string_view color_name) {
    PMMA::Types::Color::SetColorName(static_cast<std::string>(color_name));
}

uint32_t PMMA::Types::Color::GetSeed() {
    ColorConfiguredCheck(Configured);
    return seed;
}

uint32_t PMMA::Types::Color::GetOctaves() {
    ColorConfiguredCheck(Configured);
    return octaves;
}

float PMMA::Types::Color::GetFrequency() {
    ColorConfiguredCheck(Configured);
    return frequency;
}

float PMMA::Types::Color::GetAmplitude() {
    ColorConfiguredCheck(Configured);
    return amplitude;
}

void PMMA::Types::Color::GenerateFrom1DPerlinNoise(float value, bool GenerateAlpha) {
    ColorConfiguredCheck(Configured);

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
void PMMA::Types::Color::GenerateFrom2DPerlinNoise(float value_one, float value_two, bool GenerateAlpha) {
    ColorConfiguredCheck(Configured);

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

void PMMA::Types::Color::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three, bool GenerateAlpha) {
    ColorConfiguredCheck(Configured);

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

void PMMA::Types::Color::GenerateFrom1DFractalBrownianMotion(float value, bool GenerateAlpha) {
    ColorConfiguredCheck(Configured);

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

void PMMA::Types::Color::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two, bool GenerateAlpha) {
    ColorConfiguredCheck(Configured);

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

void PMMA::Types::Color::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three, bool GenerateAlpha) {
    ColorConfiguredCheck(Configured);

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

void PMMA::Types::Color::Set_RGBA(uint8_t *in_color) {
    if (std::memcmp(InternalColor, in_color, 4) != 0) {
        Changed = true;
        InternalChanged = true;

        std::memcpy(InternalColor, in_color, 4);
    }

    IsSet = true;

    if (LinkedToDisplayBackground && Changed) {
        if (PMMA::Core::ActiveDisplayInstance != nullptr) {
            PMMA::Core::ActiveDisplayInstance->TriggerEventRefresh();
        }
    }
}

void PMMA::Types::Color::Get_RGBA(uint8_t *out_color) {
    ColorSetCheck(IsSet);

    std::memcpy(out_color, InternalColor, 4);
}

void PMMA::Types::Color::Get_RGB(uint8_t *out_color) {
    ColorSetCheck(IsSet);

    std::memcpy(out_color, InternalColor, 3);
}

std::string PMMA::Types::Color::Get_HEXA() {
    ColorSetCheck(IsSet);

    return std::format(
        "#{0:02X}{1:02X}{2:02X}{3:02X}",
        InternalColor[0], InternalColor[1], InternalColor[2],
        InternalColor[3]);
}

std::string PMMA::Types::Color::Get_HEX() {
    ColorSetCheck(IsSet);

    return std::format(
        "#{0:02X}{1:02X}{2:02X}", InternalColor[0],
        InternalColor[1], InternalColor[2]);
}

uint8_t hexByte(char a, char b) {
    auto hex = [](char c) -> uint8_t {
        if (c >= '0' && c <= '9') {
            return c - '0';
        }
        if (c >= 'a' && c <= 'f') {
            return c - 'a' + 10;
        }
        if (c >= 'A' && c <= 'F') {
            return c - 'A' + 10;
        }

        throw std::runtime_error("Invalid hex digit");
    };

    return (hex(a) << 4) | hex(b);
}

void PMMA::Types::Color::Set_HEXA(std::string input_color) {
    if (!input_color.empty() && input_color[0] == '#') {
        input_color.erase(0, 1);
    }

    if (input_color.size() != 8) {
        throw std::runtime_error("Invalid hex color length");
    }

    uint8_t in_color[4] = {
        hexByte(input_color[0], input_color[1]),
        hexByte(input_color[2], input_color[3]),
        hexByte(input_color[4], input_color[5]),
        hexByte(input_color[6], input_color[7])};

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

    if (LinkedToDisplayBackground && Changed) {
        if (PMMA::Core::ActiveDisplayInstance != nullptr) {
            PMMA::Core::ActiveDisplayInstance->TriggerEventRefresh();
        }
    }
}

void PMMA::Types::Color::Set_RGB(uint8_t *in_color) {
    PMMA::Core::LoggingManagerInstance->InternalLogDebug(
        9,
        "The alpha channel is automatically set to opaque.");

    if (std::memcmp(InternalColor, in_color, 3) != 0 ||
        InternalColor[3] != 255) {
        Changed = true;
        InternalChanged = true;

        std::memcpy(InternalColor, in_color, 3);
        InternalColor[3] = 255;
    }

    IsSet = true;

    if (LinkedToDisplayBackground && Changed) {
        if (PMMA::Core::ActiveDisplayInstance != nullptr) {
            PMMA::Core::ActiveDisplayInstance->TriggerEventRefresh();
        }
    }
}

void PMMA::Types::Color::Set_HEX(std::string input_color) {
    if (!input_color.empty() && input_color[0] == '#') {
        input_color.erase(0, 1);
    }

    if (input_color.size() != 6) {
        throw std::runtime_error("Invalid hex color length");
    }

    uint8_t in_color[3] = {
        hexByte(input_color[0], input_color[1]),
        hexByte(input_color[2], input_color[3]),
        hexByte(input_color[4], input_color[5])};

    PMMA::Core::LoggingManagerInstance->InternalLogDebug(
        9,
        "The alpha channel is automatically set to opaque.");

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

    if (LinkedToDisplayBackground && Changed) {
        if (PMMA::Core::ActiveDisplayInstance != nullptr) {
            PMMA::Core::ActiveDisplayInstance->TriggerEventRefresh();
        }
    }
}

bool PMMA::Types::Color::IsTransparent() {
    ColorSetCheck(IsSet);

    return InternalColor[3] != 255;
}

bool PMMA::Types::Color::IsOpaque() {
    ColorSetCheck(IsSet);

    return InternalColor[3] == 255;
}

bool PMMA::Types::Color::IsClear() {
    ColorSetCheck(IsSet);

    return InternalColor[3] == 0;
}