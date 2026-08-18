#include <optional>

#include <STB/stb_image.h>
#include <bc7enc_wrapper.hpp>

#include "PMMA_Core.hpp"

static size_t GetBC7MipSize(
    uint32_t width,
    uint32_t height) {
    const uint32_t blocksX = (width + 3) / 4;
    const uint32_t blocksY = (height + 3) / 4;

    return size_t(blocksX) * size_t(blocksY) * 16;
}

inline void GenerateMipChain(
    PMMA::Internal::TextureProperty *TextureProperties,
    const unsigned char *basePixels,
    uint32_t width,
    uint32_t height,
    uint32_t channels) {
    TextureProperties->MipChain.clear();

    std::vector<uint8_t> current(
        basePixels,
        basePixels + (width * height * channels));

    uint32_t currentWidth = width;
    uint32_t currentHeight = height;

    uint32_t mipLevel = 0;

    while (true) {
        //
        // Store the current mip.
        //
        PMMA::Internal::MipData mip;

        mip.Size[0] =
            static_cast<uint16_t>(currentWidth);

        mip.Size[1] =
            static_cast<uint16_t>(currentHeight);

        mip.Padding = 0;

        mip.PixelData = current;

        TextureProperties->MipChain.emplace_back(std::move(mip));

        ++mipLevel;

        //
        // Finished once we've reached 1x1.
        //
        if (mipLevel >= PMMA::Constants::MAX_TEXTURE_MIPS ||
            (currentWidth == 1 && currentHeight == 1)) {
            break;
        }

        const uint32_t nextWidth =
            std::max(1u, currentWidth / 2);

        const uint32_t nextHeight =
            std::max(1u, currentHeight / 2);

        std::vector<uint8_t> next(
            nextWidth *
            nextHeight *
            channels);

        for (uint32_t y = 0; y < nextHeight; ++y) {
            for (uint32_t x = 0; x < nextWidth; ++x) {
                const uint32_t sx = x * 2;
                const uint32_t sy = y * 2;

                if (channels == 4) {
                    //
                    // Premultiplied alpha box filter.
                    //
                    float r = 0.0f;
                    float g = 0.0f;
                    float b = 0.0f;
                    float a = 0.0f;

                    for (uint32_t oy = 0; oy < 2; ++oy) {
                        for (uint32_t ox = 0; ox < 2; ++ox) {
                            const uint32_t px =
                                std::min(sx + ox, currentWidth - 1);

                            const uint32_t py =
                                std::min(sy + oy, currentHeight - 1);

                            const size_t src =
                                (py * currentWidth + px) * channels;

                            const float alpha =
                                current[src + 3] / 255.0f;

                            r += current[src + 0] * alpha;
                            g += current[src + 1] * alpha;
                            b += current[src + 2] * alpha;
                            a += alpha;
                        }
                    }

                    r *= 0.25f;
                    g *= 0.25f;
                    b *= 0.25f;
                    a *= 0.25f;

                    const size_t dst =
                        (y * nextWidth + x) * channels;

                    if (a > 0.00001f) {
                        next[dst + 0] =
                            static_cast<uint8_t>(
                                std::clamp(r / a, 0.0f, 255.0f));

                        next[dst + 1] =
                            static_cast<uint8_t>(
                                std::clamp(g / a, 0.0f, 255.0f));

                        next[dst + 2] =
                            static_cast<uint8_t>(
                                std::clamp(b / a, 0.0f, 255.0f));
                    } else {
                        next[dst + 0] = 0;
                        next[dst + 1] = 0;
                        next[dst + 2] = 0;
                    }

                    next[dst + 3] =
                        static_cast<uint8_t>(
                            std::clamp(a * 255.0f, 0.0f, 255.0f));
                } else {
                    //
                    // Standard RGB box filter.
                    //
                    for (uint32_t c = 0; c < channels; ++c) {
                        uint32_t sum = 0;

                        for (uint32_t oy = 0; oy < 2; ++oy) {
                            for (uint32_t ox = 0; ox < 2; ++ox) {
                                const uint32_t px =
                                    std::min(sx + ox, currentWidth - 1);

                                const uint32_t py =
                                    std::min(sy + oy, currentHeight - 1);

                                sum +=
                                    current[(py * currentWidth + px) *
                                                channels +
                                            c];
                            }
                        }

                        next[(y * nextWidth + x) *
                                 channels +
                             c] =
                            static_cast<uint8_t>(sum / 4);
                    }
                }
            }
        }

        current = std::move(next);
        currentWidth = nextWidth;
        currentHeight = nextHeight;
    }
}

inline void ExtrudeMip(
    PMMA::Internal::MipData &mip,
    uint32_t channels) {
    const uint32_t oldWidth =
        mip.Size[0];

    const uint32_t oldHeight =
        mip.Size[1];

    const uint32_t newWidth =
        oldWidth + (mip.Padding * 2);

    const uint32_t newHeight =
        oldHeight + (mip.Padding * 2);

    std::vector<uint8_t> expanded(
        newWidth *
        newHeight *
        channels);

    auto CopyPixel =
        [&](uint32_t dstX,
            uint32_t dstY,
            uint32_t srcX,
            uint32_t srcY) {
            memcpy(
                &expanded[(dstY * newWidth + dstX) *
                          channels],

                &mip.PixelData[(srcY * oldWidth + srcX) *
                               channels],

                channels);
        };

    //
    // Copy original image into centre.
    //
    for (uint32_t y = 0; y < oldHeight; y++) {
        for (uint32_t x = 0; x < oldWidth; x++) {
            CopyPixel(
                x + mip.Padding,
                y + mip.Padding,
                x,
                y);
        }
    }

    //
    // Left/right extrusion.
    //
    for (uint32_t y = 0; y < oldHeight; y++) {
        for (uint32_t p = 0; p < mip.Padding; p++) {
            //
            // Left
            //
            CopyPixel(
                p,
                y + mip.Padding,
                0,
                y);

            //
            // Right
            //
            CopyPixel(
                newWidth - mip.Padding + p,
                y + mip.Padding,
                oldWidth - 1,
                y);
        }
    }

    //
    // Top/bottom extrusion.
    //
    for (uint32_t x = 0; x < oldWidth; x++) {
        for (uint32_t p = 0; p < mip.Padding; p++) {
            //
            // Top
            //
            CopyPixel(
                x + mip.Padding,
                p,
                x,
                0);

            //
            // Bottom
            //
            CopyPixel(
                x + mip.Padding,
                newHeight - mip.Padding + p,
                x,
                oldHeight - 1);
        }
    }

    //
    // Corners.
    //
    for (uint32_t x = 0; x < mip.Padding; x++) {
        for (uint32_t y = 0; y < mip.Padding; y++) {
            //
            // Top-left
            //
            CopyPixel(
                x,
                y,
                0,
                0);

            //
            // Top-right
            //
            CopyPixel(
                newWidth - mip.Padding + x,
                y,
                oldWidth - 1,
                0);

            //
            // Bottom-left
            //
            CopyPixel(
                x,
                newHeight - mip.Padding + y,
                0,
                oldHeight - 1);

            //
            // Bottom-right
            //
            CopyPixel(
                newWidth - mip.Padding + x,
                newHeight - mip.Padding + y,
                oldWidth - 1,
                oldHeight - 1);
        }
    }

    //
    // Replace mip data.
    //
    mip.PixelData =
        std::move(expanded);

    mip.Size[0] =
        static_cast<uint16_t>(newWidth);

    mip.Size[1] =
        static_cast<uint16_t>(newHeight);
}

inline void CompressMipChainToBC7(
    std::vector<PMMA::Internal::MipData> &mipChain) {
    if (mipChain.empty()) {
        throw std::invalid_argument(
            "CompressMipChainToBC7: mip chain is empty.");
    }

    for (PMMA::Internal::MipData &mip : mipChain) {
        const uint32_t width =
            static_cast<uint32_t>(mip.Size[0]);

        const uint32_t height =
            static_cast<uint32_t>(mip.Size[1]);

        if (width == 0 || height == 0) {
            throw std::runtime_error(
                "CompressMipChainToBC7: mip has invalid dimensions.");
        }

        const size_t expectedRGBA8Size =
            size_t(width) *
            size_t(height) *
            4;

        if (mip.PixelData.size() != expectedRGBA8Size) {
            throw std::runtime_error(
                "CompressMipChainToBC7: mip PixelData is not RGBA8.");
        }

        const uint32_t blocksX =
            (width + 3) >> 2;

        const uint32_t blocksY =
            (height + 3) >> 2;

        const size_t blockCount =
            size_t(blocksX) *
            size_t(blocksY);

        std::vector<uint8_t> compressedData(
            blockCount * 16);

        const uint8_t *src =
            mip.PixelData.data();

        uint8_t *dst =
            compressedData.data();

        //
        // One temporary 4x4 RGBA block.
        //
        alignas(16) uint8_t block[64];

        //
        // Number of bytes in one source RGBA row.
        //
        const size_t srcRowBytes =
            size_t(width) * 4;

        //
        // Number of complete 4-pixel-wide blocks.
        //
        const uint32_t fullBlocksX =
            width >> 2;

        //
        // Encode all completely interior blocks first.
        //
        // This is the overwhelmingly common path and avoids
        // all per-pixel coordinate calculations.
        //
        for (uint32_t blockY = 0;
             blockY < (height >> 2);
             ++blockY) {
            const uint8_t *row0 =
                src +
                size_t(blockY * 4 + 0) * srcRowBytes;

            const uint8_t *row1 =
                src +
                size_t(blockY * 4 + 1) * srcRowBytes;

            const uint8_t *row2 =
                src +
                size_t(blockY * 4 + 2) * srcRowBytes;

            const uint8_t *row3 =
                src +
                size_t(blockY * 4 + 3) * srcRowBytes;

            for (uint32_t blockX = 0;
                 blockX < fullBlocksX;
                 ++blockX) {
                const size_t x =
                    size_t(blockX) * 16;

                //
                // Each 4-pixel RGBA row is exactly 16 bytes.
                //
                std::memcpy(
                    block + 0,
                    row0 + x,
                    16);

                std::memcpy(
                    block + 16,
                    row1 + x,
                    16);

                std::memcpy(
                    block + 32,
                    row2 + x,
                    16);

                std::memcpy(
                    block + 48,
                    row3 + x,
                    16);

                bc7enc_encode_block(
                    dst,
                    block,
                    0xFF, // all modes
                    16,   // max partitions
                    1,    // uber level
                    1);   // perceptual

                dst += 16;
            }

            //
            // Right edge block, if width isn't divisible by 4.
            //
            if (fullBlocksX < blocksX) {
                const uint32_t x =
                    fullBlocksX * 4;

                const uint32_t lastX =
                    width - 1;

                for (uint32_t py = 0;
                     py < 4;
                     ++py) {
                    const uint8_t *row =
                        src +
                        size_t(blockY * 4 + py) *
                            srcRowBytes;

                    uint8_t *blockRow =
                        block +
                        size_t(py) * 16;

                    //
                    // Copy the remaining real pixels.
                    //
                    const uint32_t remaining =
                        width - x;

                    std::memcpy(
                        blockRow,
                        row + size_t(x) * 4,
                        size_t(remaining) * 4);

                    //
                    // Clamp the remaining pixels to the
                    // final pixel in the row.
                    //
                    const uint8_t *edgePixel =
                        row + size_t(lastX) * 4;

                    for (uint32_t px = remaining;
                         px < 4;
                         ++px) {
                        std::memcpy(
                            blockRow + size_t(px) * 4,
                            edgePixel,
                            4);
                    }
                }

                bc7enc_encode_block(
                    dst,
                    block,
                    0xFF,
                    16,
                    1,
                    1);

                dst += 16;
            }
        }

        //
        // Bottom edge.
        //
        // This is only needed when height isn't divisible by 4.
        //
        if ((height & 3) != 0) {
            const uint32_t blockY =
                height >> 2;

            const uint32_t y =
                blockY * 4;

            const uint32_t remainingRows =
                height - y;

            const uint32_t lastY =
                height - 1;

            const uint8_t *lastRow =
                src +
                size_t(lastY) * srcRowBytes;

            //
            // All full-width blocks on the bottom row.
            //
            for (uint32_t blockX = 0;
                 blockX < fullBlocksX;
                 ++blockX) {
                const uint32_t x =
                    blockX * 4;

                const size_t blockOffset =
                    size_t(x) * 4;

                for (uint32_t py = 0;
                     py < remainingRows;
                     ++py) {
                    const uint8_t *row =
                        src +
                        size_t(y + py) * srcRowBytes;

                    std::memcpy(
                        block + size_t(py) * 16,
                        row + blockOffset,
                        16);
                }

                //
                // Clamp remaining rows to the last real row.
                //
                for (uint32_t py = remainingRows;
                     py < 4;
                     ++py) {
                    std::memcpy(
                        block + size_t(py) * 16,
                        lastRow + blockOffset,
                        16);
                }

                bc7enc_encode_block(
                    dst,
                    block,
                    0xFF,
                    16,
                    1,
                    1);

                dst += 16;
            }

            //
            // Bottom-right corner block.
            //
            if (fullBlocksX < blocksX) {
                const uint32_t x =
                    fullBlocksX * 4;

                const uint32_t remainingPixels =
                    width - x;

                const uint8_t *edgePixel =
                    src +
                    size_t(lastY) * srcRowBytes +
                    size_t(width - 1) * 4;

                for (uint32_t py = 0;
                     py < remainingRows;
                     ++py) {
                    const uint8_t *row =
                        src +
                        size_t(y + py) * srcRowBytes;

                    uint8_t *blockRow =
                        block +
                        size_t(py) * 16;

                    std::memcpy(
                        blockRow,
                        row + size_t(x) * 4,
                        size_t(remainingPixels) * 4);

                    const uint8_t *horizontalEdge =
                        row +
                        size_t(width - 1) * 4;

                    for (uint32_t px = remainingPixels;
                         px < 4;
                         ++px) {
                        std::memcpy(
                            blockRow + size_t(px) * 4,
                            horizontalEdge,
                            4);
                    }
                }

                //
                // Fill remaining rows from the final pixel row.
                //
                for (uint32_t py = remainingRows;
                     py < 4;
                     ++py) {
                    uint8_t *blockRow =
                        block +
                        size_t(py) * 16;

                    const uint8_t *edge =
                        edgePixel;

                    for (uint32_t px = 0;
                         px < remainingPixels;
                         ++px) {
                        const uint8_t *pixel =
                            lastRow +
                            size_t(x + px) * 4;

                        std::memcpy(
                            blockRow + size_t(px) * 4,
                            pixel,
                            4);
                    }

                    for (uint32_t px = remainingPixels;
                         px < 4;
                         ++px) {
                        std::memcpy(
                            blockRow + size_t(px) * 4,
                            edge,
                            4);
                    }
                }

                bc7enc_encode_block(
                    dst,
                    block,
                    0xFF,
                    16,
                    1,
                    1);

                dst += 16;
            }
        }

        mip.PixelData =
            std::move(compressedData);
    }
}

void PMMA::Types::Texture::InternalLoad() {
    // Attempt to load from cache first

    std::string CachedTexturePath = "";
    std::string ShaderName = std::filesystem::path(Path).stem().string();
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

    if (!PMMA::Registry::TextureCompilationStartTime.has_value()) {
        PMMA::Registry::TextureCompilationStartTime = std::chrono::steady_clock::now();
    }

    std::filesystem::create_directories(std::filesystem::path(CachedTexturePath).parent_path());

    // Load texture and generate mipmaps/extrusion before building cached data.

    int width, height, original_channels;
    if (!stbi_info(Path.c_str(), &width, &height, &original_channels)) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            67,
            "Failed to query image information. Please ensure the \
image path is valid and is a valid format. The image path is: '" +
                Path + "'. The reason for the fail is: " + stbi_failure_reason());

        throw std::runtime_error("Failed to query image information.");
    }

    // 2. Determine target channels (Force 4 if it has 4, otherwise force 3)
    TextureProperties->Channels = (original_channels == 4) ? 4 : 3;

    unsigned char *data = stbi_load(
        Path.c_str(),
        &width, &height,
        nullptr, 4);

    if (data) {
        PMMA::Internal::MipData base;

        base.Size[0] = width;
        base.Size[1] = height;
        base.PixelData.assign(
            data,
            data + width * height * 4);

        stbi_image_free(data);
        data = nullptr;

        base.Padding = 1;

        ExtrudeMip(
            base,
            4); // channels, force to RGBA

        GenerateMipChain(
            TextureProperties,
            base.PixelData.data(),
            base.Size[0],
            base.Size[1],
            4); // channels, force to RGBA

        CompressMipChainToBC7(
            TextureProperties->MipChain);

        std::chrono::steady_clock::time_point CurrentTime = std::chrono::steady_clock::now();
        std::chrono::duration<float> Duration = CurrentTime - PMMA::Registry::TextureCompilationStartTime.value();

        if (Duration.count() > 60) { // if loading for more than 60 seconds, prioritize caching inline so if the user closes program because they feel it's not responding, some progress is kept!
            SaveTextureCache(
                CachedTexturePath,
                *TextureProperties);
        } else {
            PMMA::Core::ParallelWorkerInstance->Enqueue([this, CachedTexturePath]() {
                SaveTextureCache(
                    CachedTexturePath,
                    *TextureProperties);
            });
        }

    } else {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            68,
            "Failed to read image data. Please ensure the \
image path is valid and is a valid format. The image path is: '" +
                Path + "'. The reason for the fail is: " + stbi_failure_reason());

        throw std::runtime_error("Failed to read image data.");
    }
}

void PMMA::Types::Texture::Load(std::string TexturePath) {
    if (Path == TexturePath) {
        return;
    }

    if (Path != "") {
        Unload();
    }

    Path = TexturePath;

    auto it = PMMA::Core::TextureCatalogue.find(TexturePath);

    // its already loaded, just use the existing one
    if (it != PMMA::Core::TextureCatalogue.end()) {
        std::pair<const std::string, PMMA::Internal::TextureProperty> *pairPtr = &*it;

        TextureProperties = &(pairPtr->second);
    } else {
        PMMA::Internal::TextureProperty &propertyRef = PMMA::Core::TextureCatalogue[TexturePath];

        TextureProperties = &propertyRef;

        TextureProperties->LoadFuture = PMMA::Core::ParallelWorkerInstance->Enqueue([this]() {
            InternalLoad();
        });
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
        if (TextureProperties->LoadFuture.valid()) {
            TextureProperties->LoadFuture.wait();

            TextureProperties->LoadFuture = std::future<void>();
        }

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
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            69,
            "Cannot enable an image that has not been loaded yet. \
Please load an image first.");
    }

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
    }

    IsTextureEnabled = true;
}

void PMMA::Types::Texture::GetSize(uint16_t *size) {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture size. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
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

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
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

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
    }

    return TextureProperties->MipChain[0].Size[1];
}

std::string PMMA::Types::Texture::GetPath() {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture path. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
    }

    return Path;
}

unsigned char PMMA::Types::Texture::GetChannels() {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture size. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
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

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
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

#include <cstring>

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

#include <cstring>

void PMMA::Types::Color::Get_RGBA(uint8_t *out_color) {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            30,
            "You have not set a color - please set a color before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }

    std::memcpy(out_color, InternalColor, 4);
}

void PMMA::Types::Color::Get_RGB(uint8_t *out_color) {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a color - please set a color before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }

    std::memcpy(out_color, InternalColor, 3);
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
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a color - please set a color \
before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }

    return InternalColor[3] != 255;
}

bool PMMA::Types::Color::IsOpaque() {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a color - please set a color \
before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }

    return InternalColor[3] == 255;
}

bool PMMA::Types::Color::IsClear() {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a color - please set a color \
before attempting to get it.");

        throw std::runtime_error("Color not set!");
    }

    return InternalColor[3] == 0;
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

void PMMA::Types::TwoD::Coordinate::GetCoordinate(int16_t *out) {
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

int16_t PMMA::Types::TwoD::Coordinate::GetX() {
    if (!Get_X_Set()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
        throw std::runtime_error("Display coordinate not set!");
    }

    return coordinate[0];
}

int16_t PMMA::Types::TwoD::Coordinate::GetY() {
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

    int16_t coord_float[2];
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

    int16_t center = PMMA::Core::ActiveDisplayInstance->GetHorizontalCenterPosition();

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

    int16_t center = PMMA::Core::ActiveDisplayInstance->GetVerticalCenterPosition();

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

    int16_t new_coord[2];
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

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise1D(value + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise1D(value + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

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

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

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

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

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

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise1D(value + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise1D(value + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

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

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

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

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

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