#include <filesystem>

#include <STB/stb_image.h>
#include <bc7enc_wrapper.hpp>

#include "Internal/Core/PMMA_Core.hpp"
#include "Internal/Core/PMMA_Registry.hpp"

#include "Internal/ParallelWorker.hpp"

#include "Types/Texture.hpp"

#include "Constants.hpp"
#include "Passport.hpp"

inline void TextureSetCheck(PMMA::Internal::Rendering::Core2D::TextureProperty *TextureProperties) {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture size. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }
}

static size_t GetBC7MipSize(
    uint32_t width,
    uint32_t height) {
    const uint32_t blocksX = (width + 3) / 4;
    const uint32_t blocksY = (height + 3) / 4;

    return size_t(blocksX) * size_t(blocksY) * 16;
}

inline void GenerateMipChain(
    PMMA::Internal::Rendering::Core2D::TextureProperty *TextureProperties,
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
        PMMA::Internal::Rendering::Core2D::MipData mip;

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
    PMMA::Internal::Rendering::Core2D::MipData &mip,
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
    std::vector<PMMA::Internal::Rendering::Core2D::MipData> &mipChain) {
    if (mipChain.empty()) {
        throw std::invalid_argument(
            "CompressMipChainToBC7: mip chain is empty.");
    }

    for (PMMA::Internal::Rendering::Core2D::MipData &mip : mipChain) {
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
        CachedTexturePath = PMMA::Core::Registry::PMMA_Location + PMMA::Core::Registry::PathSeparator + "temporary" + PMMA::Core::Registry::PathSeparator + "texture_cache" + PMMA::Core::Registry::PathSeparator + ShaderName + ".dds.cache";
    } else {
        CachedTexturePath = PMMA::Core::PassportInstance->GetTemporaryPath() + PMMA::Core::Registry::PathSeparator + "texture_cache" + PMMA::Core::Registry::PathSeparator + ShaderName + ".dds.cache";
    }

    if (std::filesystem::exists(CachedTexturePath)) {
        if (LoadCached(CachedTexturePath)) {
            TextureProperties->References++;
            IsTextureEnabled = true;
            return;
        }
    }

    if (PMMA::Core::Registry::InitialSetup && !PMMA::Core::Registry::TextureCompilationStartTime.has_value()) {
        PMMA::Core::Registry::TextureCompilationStartTime = std::chrono::steady_clock::now();
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

    unsigned char *data = stbi_load(
        Path.c_str(),
        &width, &height,
        nullptr, 4);

    if (data) {
        const uint8_t *alpha = data + 3;
        const uint8_t *end =
            data + size_t(width) * size_t(height) * 4;

        for (; alpha < end; alpha += 4) {
            if (*alpha != 255) {
                TextureProperties->Transparent = true;
                break;
            }
        }

        PMMA::Internal::Rendering::Core2D::MipData base;

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

        if (!PMMA::Core::Registry::InitialSetup) {
            PMMA::Core::ParallelWorkerInstance->Enqueue([this, CachedTexturePath]() {
                SaveTextureCache(
                    CachedTexturePath,
                    *TextureProperties);
            });
        } else {
            std::chrono::steady_clock::time_point CurrentTime = std::chrono::steady_clock::now();
            std::chrono::duration<float> Duration = CurrentTime - PMMA::Core::Registry::TextureCompilationStartTime.value();

            if (Duration.count() < 6) { // if loading for more than 60 seconds, prioritize caching inline so if the user closes program because they feel it's not responding, some progress is kept!
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
        std::pair<const std::string, PMMA::Internal::Rendering::Core2D::TextureProperty> *pairPtr = &*it;

        TextureProperties = &(pairPtr->second);
    } else {
        PMMA::Internal::Rendering::Core2D::TextureProperty &propertyRef = PMMA::Core::TextureCatalogue[TexturePath];

        TextureProperties = &propertyRef;

        PMMA::Core::ParallelWorkerInstance->TexturesToLoad++;
        TextureProperties->LoadFuture = PMMA::Core::ParallelWorkerInstance->Enqueue([this]() {
            InternalLoad();
            PMMA::Core::ParallelWorkerInstance->TexturesLoaded++;
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
    TextureSetCheck(TextureProperties);

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
    TextureSetCheck(TextureProperties);

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
    }

    if (TextureProperties->Transparent) {
        return 4;
    }

    return 3;
}

uint32_t PMMA::Types::Texture::GetReferences() {
    TextureSetCheck(TextureProperties);

    if (TextureProperties->LoadFuture.valid()) {
        TextureProperties->LoadFuture.wait();

        TextureProperties->LoadFuture = std::future<void>();
    }

    return TextureProperties->References;
}