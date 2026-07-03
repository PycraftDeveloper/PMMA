#include <optional>

#include "PMMA_Core.hpp"

PMMA::Types::Color::Color() {
    RandomColorGenerator = PMMA::Core::RandomGenerator;
}

void PMMA::Types::Color::Set_ColorName(std::string color_name) {
    std::optional<std::array<uint8_t, 3>> Color = CPP_Constants::Colors::FindColor(color_name);

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

uint32_t PMMA::Types::Color::GetSeed() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return seed;
}

uint32_t PMMA::Types::Color::GetOctaves() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return octaves;
}

float PMMA::Types::Color::GetFrequency() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return frequency;
}

float PMMA::Types::Color::GetAmplitude() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return amplitude;
}

void PMMA::Types::Color::GenerateFrom1DPerlinNoise(float value, bool GenerateAlpha) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
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
void PMMA::Types::Color::GenerateFrom2DPerlinNoise(float value_one, float value_two, bool GenerateAlpha) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
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

void PMMA::Types::Color::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three, bool GenerateAlpha) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
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

void PMMA::Types::Color::GenerateFrom1DFractalBrownianMotion(float value, bool GenerateAlpha) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
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

void PMMA::Types::Color::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two, bool GenerateAlpha) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
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

void PMMA::Types::Color::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three, bool GenerateAlpha) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
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

void PMMA::Types::Color::Set_RGBA(uint8_t *in_color) {
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

void PMMA::Types::Color::Get_RGBA(uint8_t *out_color) {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Color::Get_RGB(uint8_t *out_color) {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a color - please set a color \
before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }

    out_color[0] = InternalColor[0];
    out_color[1] = InternalColor[1];
    out_color[2] = InternalColor[2];
}

std::string PMMA::Types::Color::Get_HEXA() {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            30,
            "You have not set a color - please set a color \
before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }

    return std::format(
        "#{0:02X}{1:02X}{2:02X}{3:02X}",
        InternalColor[0], InternalColor[1], InternalColor[2],
        InternalColor[3]);
}

std::string PMMA::Types::Color::Get_HEX() {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a color - please set a color \
before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }

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

PMMA::Types::DisplayCoordinate::DisplayCoordinate() {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }

    RandomCoordGenerator = PMMA::Core::RandomGenerator;

    PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
}

void PMMA::Types::DisplayCoordinate::Get(uint16_t *out) {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
        throw std::runtime_error("Display coordinate not set!");
    }

    out[0] = Coordinate[0];
    out[1] = Coordinate[1];
}

uint32_t PMMA::Types::DisplayCoordinate::GetSeed() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return seed;
}

uint32_t PMMA::Types::DisplayCoordinate::GetOctaves() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return octaves;
}

float PMMA::Types::DisplayCoordinate::GetFrequency() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return frequency;
}

float PMMA::Types::DisplayCoordinate::GetAmplitude() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return amplitude;
}

void PMMA::Types::DisplayCoordinate::Configure(DisplayCoordinate_Configure_Kwargs kwargs) {
    uint32_t new_seed;

    if (!kwargs.seed.has_value()) {
        CPP_FastRandom TempRandomGenerator;
        new_seed = TempRandomGenerator.Next();
    } else {
        new_seed = kwargs.seed.value();
    }

    X_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
    Y_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed + 1);

    X_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
    Y_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed + 1, kwargs.octaves, kwargs.frequency, kwargs.amplitude);

    RandomCoordGenerator = new CPP_FastRandom();
    RandomCoordGenerator->SetSeed(new_seed);

    seed = new_seed;
    octaves = kwargs.octaves;
    frequency = kwargs.frequency;
    amplitude = kwargs.amplitude;
    Configured = true;
}

void PMMA::Types::DisplayCoordinate::SetCentered() {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }

    if (PMMA::Core::ActiveDisplayInstance->DisplaySizeChanged) {
        PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
    }

    unsigned int new_coord[2];
    PMMA::Core::ActiveDisplayInstance->GetCenterPosition(new_coord);

    uint16_t coord_float[2];
    coord_float[0] = static_cast<uint16_t>(new_coord[0]);
    coord_float[1] = static_cast<uint16_t>(new_coord[1]);

    Set(coord_float);
}

void PMMA::Types::DisplayCoordinate::GenerateFromRandom() {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }

    if (PMMA::Core::ActiveDisplayInstance->DisplaySizeChanged) {
        PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
    }

    uint16_t new_coord[2];
    new_coord[0] = RandomCoordGenerator->Next(DisplaySize[0]);
    new_coord[1] = RandomCoordGenerator->Next(DisplaySize[1]);

    Set(new_coord);
}

void PMMA::Types::DisplayCoordinate::GenerateFrom1DPerlinNoise(float value) {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }

    uint16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise1D(value + x_offset);
    new_coord[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise1D(value + y_offset);
    new_coord[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
}

void PMMA::Types::DisplayCoordinate::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }

    uint16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coord[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coord[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
}

void PMMA::Types::DisplayCoordinate::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }

    uint16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coord[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coord[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
}

void PMMA::Types::DisplayCoordinate::GenerateFrom1DFractalBrownianMotion(float value) {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }

    uint16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise1D(value + x_offset);
    new_coord[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise1D(value + y_offset);
    new_coord[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
}

void PMMA::Types::DisplayCoordinate::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }

    uint16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coord[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coord[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
}

void PMMA::Types::DisplayCoordinate::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }

    uint16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coord[0] = PMMA::Maths::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coord[1] = PMMA::Maths::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
}