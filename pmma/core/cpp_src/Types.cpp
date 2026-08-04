#include <optional>

#include <STB/stb_image.h>

#include "PMMA_Core.hpp"

void PMMA::Types::Texture::Load(std::string TexturePath) {
    if (Path == TexturePath) {
        return;
    }

    if (Path != "") {
        Unload();
    }

    auto it = PMMA::Core::TextureCatalogue.find(TexturePath);

    if (it != PMMA::Core::TextureCatalogue.end()) {
        std::pair<const std::string, PMMA::Internal::TextureProperty> *pairPtr = &*it;

        TextureProperties = &(pairPtr->second);
    } else {
        PMMA::Internal::TextureProperty &propertyRef = PMMA::Core::TextureCatalogue[TexturePath];

        TextureProperties = &propertyRef;

        // Attempt to load from cache first

        std::string CachedTexturePath = "";
        std::string ShaderName = std::filesystem::path(TexturePath).stem().string();
        if (!PMMA::Core::PassportInstance->GetIsRegistered()) {
            CachedTexturePath = PMMA::Registry::PMMA_Location + PMMA::Registry::PathSeparator + "temporary" + PMMA::Registry::PathSeparator + "texture_cache" + PMMA::Registry::PathSeparator + ShaderName + ".dds.cache";
        } else {
            CachedTexturePath = PMMA::Core::PassportInstance->GetTemporaryPath() + PMMA::Registry::PathSeparator + "texture_cache" + PMMA::Registry::PathSeparator + ShaderName + ".dds.cache";
        }

        if (std::filesystem::exists(CachedTexturePath)) {
            if (LoadCached(CachedTexturePath)) {
                TextureProperties->References++;
                IsTextureEnabled = true;
                return;
            }
        }

        std::filesystem::create_directories(std::filesystem::path(CachedTexturePath).parent_path());

        // Load texture and generate mipmaps/extrusion before building cached data.

        int width, height, original_channels;
        if (!stbi_info(TexturePath.c_str(), &width, &height, &original_channels)) {
            PMMA::Core::LoggingManagerInstance->InternalLogError(
                67,
                "Failed to query image information. Please ensure the \
image path is valid and is a valid format. The image path is: '" +
                    TexturePath + "'. The reason for the fail is: " + stbi_failure_reason());

            throw std::runtime_error("Failed to query image information.");
        }

        // 2. Determine target channels (Force 4 if it has 4, otherwise force 3)
        TextureProperties->Channels = (original_channels == 4) ? 4 : 3;

        unsigned char *data = stbi_load(
            TexturePath.c_str(),
            &width, &height,
            nullptr, TextureProperties->Channels);

        if (data) {
            PMMA::Internal::MipData base;

            base.Size[0] = width;
            base.Size[1] = height;
            base.PixelData.assign(
                data,
                data + width * height * TextureProperties->Channels);

            base.Padding = 1;

            ExtrudeMip(
                base,
                TextureProperties->Channels);

            GenerateMipChain(
                base.PixelData.data(),
                base.Size[0],
                base.Size[1],
                TextureProperties->Channels);

            SaveTextureCache(
                CachedTexturePath,
                *TextureProperties);

            stbi_image_free(data);
            data = nullptr;
        } else {
            PMMA::Core::LoggingManagerInstance->InternalLogError(
                68,
                "Failed to read image data. Please ensure the \
image path is valid and is a valid format. The image path is: '" +
                    TexturePath + "'. The reason for the fail is: " + stbi_failure_reason());

            throw std::runtime_error("Failed to read image data.");
        }
    }

    TextureProperties->References++;
    IsTextureEnabled = true;
}

void PMMA::Types::Texture::Load() {
    if (Path != "") {
        PMMA::Types::Texture::Load(Path);
    } else {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            71,
            "Unable to re-load the previously loaded texture as the \
path has not been set. Please specify a valid file path to a texture.");

        throw std::runtime_error("Failed to re-load texture - path was cleared.");
    }
}

void PMMA::Types::Texture::Unload() {
    IsTextureEnabled = false;

    if (TextureProperties != nullptr) {
        TextureProperties->References -= 1;

        if (TextureProperties->References <= 0) {
            PMMA::Core::TextureCatalogue.erase(Path);
        }
    }
}

PMMA::Types::Texture::~Texture() {
    PMMA::Types::Texture::Unload();
}

void PMMA::Types::Texture::Enable() {
    if (TextureProperties != nullptr) {
        IsTextureEnabled = true;
    } else {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            69,
            "Cannot enable an image that has not been loaded yet. \
Please load an image first.");
    }
}

void PMMA::Types::Texture::GetSize(uint16_t *size) {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture size. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    size[0] = TextureProperties->MipChain[0].Size[0];
    size[1] = TextureProperties->MipChain[0].Size[1];
}

uint16_t PMMA::Types::Texture::GetWidth() {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture width. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    return TextureProperties->MipChain[0].Size[0];
}

uint16_t PMMA::Types::Texture::GetHeight() {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture height. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    return TextureProperties->MipChain[0].Size[1];
}

void PMMA::Types::Texture::GetPositionInAtlas(uintptr_t RenderPipelineInstance_ID, uint16_t *position) {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture size. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    auto &storedPosition =
        TextureProperties->RegisteredRenderPipelineInstances[RenderPipelineInstance_ID];

    position[0] = storedPosition[0];
    position[1] = storedPosition[1];
}

unsigned char PMMA::Types::Texture::GetChannels() {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture size. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    return TextureProperties->Channels;
}

uint32_t PMMA::Types::Texture::GetReferences() {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture size. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    return TextureProperties->References;
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

uint32_t PMMA::Types::Angle::GetSeed() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return seed;
}

uint32_t PMMA::Types::Angle::GetOctaves() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return octaves;
}

float PMMA::Types::Angle::GetFrequency() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return frequency;
}

float PMMA::Types::Angle::GetAmplitude() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return amplitude;
}

void PMMA::Types::Angle::GenerateFrom1DPerlinNoise(float value) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Angle::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Angle::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Angle::GenerateFrom1DFractalBrownianMotion(float value) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Angle::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Angle::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

float PMMA::Types::Angle::GetRadians() {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set an angle - please set an angle \
before attempting to get it.");

        throw std::runtime_error("Angle not set!");
    }
    return InternalAngle;
}

float PMMA::Types::Angle::GetDegrees() {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set an angle - please set an angle \
before attempting to get it.");

        throw std::runtime_error("Angle not set!");
    }
    return InternalAngle * RADIANS_TO_DEGREES;
}

uint32_t PMMA::Types::Proportion::GetSeed() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return seed;
}

uint32_t PMMA::Types::Proportion::GetOctaves() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return octaves;
}

float PMMA::Types::Proportion::GetFrequency() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return frequency;
}

float PMMA::Types::Proportion::GetAmplitude() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return amplitude;
}

void PMMA::Types::Proportion::GenerateFrom1DPerlinNoise(float value) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Proportion::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Proportion::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Proportion::GenerateFrom1DFractalBrownianMotion(float value) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Proportion::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

void PMMA::Types::Proportion::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
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

float PMMA::Types::Proportion::GetPercentage() {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a proportion - please set a proportion \
before attempting to get it.");

        throw std::runtime_error("Proportion not set!");
    }
    return InternalProportion * 100;
}

float PMMA::Types::Proportion::GetDecimal() {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a proportion - please set a proportion \
before attempting to get it.");

        throw std::runtime_error("Proportion not set!");
    }
    return InternalProportion;
}

PMMA::Types::TwoD::Coordinate::Coordinate() {
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

void PMMA::Types::TwoD::Coordinate::GetCoordinate(uint16_t *out) {
    if (!GetCoordinateSet()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
        throw std::runtime_error("Display coordinate not set!");
    }

    out[0] = coordinate[0];
    out[1] = coordinate[1];
}

uint16_t PMMA::Types::TwoD::Coordinate::GetX() {
    if (!Get_X_Set()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
        throw std::runtime_error("Display coordinate not set!");
    }

    return coordinate[0];
}

uint16_t PMMA::Types::TwoD::Coordinate::GetY() {
    if (!Get_Y_Set()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
        throw std::runtime_error("Display coordinate not set!");
    }

    return coordinate[1];
}

uint32_t PMMA::Types::TwoD::Coordinate::GetSeed() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return seed;
}

uint32_t PMMA::Types::TwoD::Coordinate::GetOctaves() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return octaves;
}

float PMMA::Types::TwoD::Coordinate::GetFrequency() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return frequency;
}

float PMMA::Types::TwoD::Coordinate::GetAmplitude() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return amplitude;
}

void PMMA::Types::TwoD::Coordinate::Configure(PMMA::Types::Configure_Kwargs kwargs) {
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

    RandomCoordGenerator = new PMMA::FastRandom();
    RandomCoordGenerator->SetSeed(new_seed);

    seed = new_seed;
    octaves = kwargs.octaves;
    frequency = kwargs.frequency;
    amplitude = kwargs.amplitude;
    Configured = true;
}

void PMMA::Types::TwoD::Coordinate::Center() {
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
    PMMA::Core::ActiveDisplayInstance->GetCenterPosition(new_coord);

    uint16_t coord_float[2];
    coord_float[0] = new_coord[0];
    coord_float[1] = new_coord[1];

    SetCoordinate(coord_float);
}

void PMMA::Types::TwoD::Coordinate::CenterHorizontal() {
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

    uint16_t center = PMMA::Core::ActiveDisplayInstance->GetHorizontalCenterPosition();

    SetX(center);
}

void PMMA::Types::TwoD::Coordinate::CenterVertical() {
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

    uint16_t center = PMMA::Core::ActiveDisplayInstance->GetVerticalCenterPosition();

    SetY(center);
}

void PMMA::Types::TwoD::Coordinate::GenerateFromRandom() {
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

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom1DPerlinNoise(float value) {
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

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
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

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
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

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom1DFractalBrownianMotion(float value) {
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

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
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

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
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

    SetCoordinate(new_coord);
}

PMMA::Types::TwoD::Size::Size() {
    if (PMMA::Core::ActiveDisplayInstance == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`.");
        throw std::runtime_error("Display not created yet!");
    }

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
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return seed;
}

uint32_t PMMA::Types::TwoD::Size::GetOctaves() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return octaves;
}

float PMMA::Types::TwoD::Size::GetFrequency() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
    return frequency;
}

float PMMA::Types::TwoD::Size::GetAmplitude() {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
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

    uint16_t new_size[2];
    new_size[0] = RandomSizeGenerator->Next(DisplaySize[0]);
    new_size[1] = RandomSizeGenerator->Next(DisplaySize[1]);

    SetSize(new_size);
}

void PMMA::Types::TwoD::Size::GenerateFrom1DPerlinNoise(float value) {
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