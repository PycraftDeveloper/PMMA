#include <algorithm>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <stdexcept>
#include <vector>

#include <bc7dec_wrapper.hpp>
#include <bc7enc_wrapper.hpp>

#include "PMMA_Core.hpp"

static size_t GetBC7MipSize(
    uint32_t width,
    uint32_t height) {
    const uint32_t blocksX =
        (width + 3) / 4;

    const uint32_t blocksY =
        (height + 3) / 4;

    return size_t(blocksX) *
           size_t(blocksY) *
           16;
}

//
// BC7 -> RGBA8
//
// Decodes one BC7 mip into a tightly packed RGBA8 image.
//
static bool DecodeBC7Mip(
    const PMMA::Internal::MipData &source,
    std::vector<uint8_t> &output) {
    const uint32_t width =
        static_cast<uint32_t>(source.Size[0]);

    const uint32_t height =
        static_cast<uint32_t>(source.Size[1]);

    if (width == 0 || height == 0) {
        output.clear();
        return false;
    }

    const uint32_t blocksX =
        (width + 3) / 4;

    const uint32_t blocksY =
        (height + 3) / 4;

    const size_t expectedBC7Size =
        size_t(blocksX) *
        size_t(blocksY) *
        16;

    if (source.PixelData.size() != expectedBC7Size) {
        std::cerr
            << "Invalid BC7 mip size. Expected "
            << expectedBC7Size
            << " bytes but got "
            << source.PixelData.size()
            << " bytes."
            << std::endl;

        output.clear();
        return false;
    }

    const size_t rgbaSize =
        size_t(width) *
        size_t(height) *
        4;

    output.resize(rgbaSize);

    const uint8_t *srcBC7 =
        source.PixelData.data();

    for (uint32_t blockY = 0;
         blockY < blocksY;
         ++blockY) {
        for (uint32_t blockX = 0;
             blockX < blocksX;
             ++blockX) {
            uint8_t blockRGBA[4 * 4 * 4];

            if (!bc7_decode_block(
                    blockRGBA,
                    srcBC7)) {
                output.clear();

                std::cerr
                    << "Failed to decode BC7 block "
                    << blockX
                    << ", "
                    << blockY
                    << " in mip "
                    << width
                    << "x"
                    << height
                    << std::endl;

                return false;
            }

            //
            // Copy the decoded 4x4 block into the image.
            //
            for (uint32_t py = 0;
                 py < 4;
                 ++py) {
                const uint32_t y =
                    blockY * 4 + py;

                //
                // The final block may extend past the image.
                //
                if (y >= height) {
                    continue;
                }

                for (uint32_t px = 0;
                     px < 4;
                     ++px) {
                    const uint32_t x =
                        blockX * 4 + px;

                    if (x >= width) {
                        continue;
                    }

                    const size_t srcOffset =
                        (size_t(py) * 4 + px) * 4;

                    const size_t dstOffset =
                        (size_t(y) * width + x) * 4;

                    output[dstOffset + 0] =
                        blockRGBA[srcOffset + 0];

                    output[dstOffset + 1] =
                        blockRGBA[srcOffset + 1];

                    output[dstOffset + 2] =
                        blockRGBA[srcOffset + 2];

                    output[dstOffset + 3] =
                        blockRGBA[srcOffset + 3];
                }
            }

            srcBC7 += 16;
        }
    }

    return true;
}

//
// RGBA8 -> BC7
//
// Compresses one tightly packed RGBA8 image into BC7.
//
static bool CompressRGBA8ToBC7(
    const uint8_t *rgba,
    uint32_t width,
    uint32_t height,
    std::vector<uint8_t> &output) {
    if (rgba == nullptr ||
        width == 0 ||
        height == 0) {
        output.clear();
        return false;
    }

    const uint32_t blocksX =
        (width + 3) / 4;

    const uint32_t blocksY =
        (height + 3) / 4;

    const size_t compressedSize =
        size_t(blocksX) *
        size_t(blocksY) *
        16;

    output.resize(compressedSize);

    uint8_t *dst =
        output.data();

    //
    // Temporary 4x4 RGBA block.
    //
    uint8_t block[4 * 4 * 4];

    for (uint32_t blockY = 0;
         blockY < blocksY;
         ++blockY) {
        for (uint32_t blockX = 0;
             blockX < blocksX;
             ++blockX) {
            //
            // Construct the 4x4 block.
            //
            // Clamp at the image edge so BC7 always receives
            // a complete 4x4 block.
            //
            for (uint32_t py = 0;
                 py < 4;
                 ++py) {
                const uint32_t y =
                    std::min(
                        blockY * 4 + py,
                        height - 1);

                for (uint32_t px = 0;
                     px < 4;
                     ++px) {
                    const uint32_t x =
                        std::min(
                            blockX * 4 + px,
                            width - 1);

                    const size_t srcOffset =
                        (size_t(y) * width + x) * 4;

                    const size_t dstOffset =
                        (size_t(py) * 4 + px) * 4;

                    block[dstOffset + 0] =
                        rgba[srcOffset + 0];

                    block[dstOffset + 1] =
                        rgba[srcOffset + 1];

                    block[dstOffset + 2] =
                        rgba[srcOffset + 2];

                    block[dstOffset + 3] =
                        rgba[srcOffset + 3];
                }
            }

            //
            // Encode BC7 block.
            //
            bc7enc_encode_block(
                dst,
                block,

                //
                // Mode mask.
                //
                // These are the values that worked with
                // your bc7enc_rdo wrapper.
                //
                0xFF,

                //
                // Maximum number of partitions.
                //
                64,

                //
                // Uber level / quality.
                //
                3,

                //
                // Perceptual encoding.
                //
                1);

            dst += 16;
        }
    }

    return true;
}

void PMMA::Internal::Rendering::Core2D::TextureManager::Assemble() {
    if (!Dirty) {
        return;
    }

    constexpr uint32_t Channels = 4;

    //
    // ---------------------------------------------------------
    // 1. Determine atlas dimensions from mip 0.
    // ---------------------------------------------------------
    //

    m_TextureWidth = 1;
    m_TextureHeight = 1;

    for (auto &[id, allocation] : Allocations) {
        m_TextureWidth =
            std::max(
                m_TextureWidth,
                allocation.X +
                    allocation.Width);

        m_TextureHeight =
            std::max(
                m_TextureHeight,
                allocation.Y +
                    allocation.Height);
    }

    //
    // ---------------------------------------------------------
    // 2. Round atlas dimensions to power-of-two.
    // ---------------------------------------------------------
    //

    auto NextPowerOfTwo =
        [](uint32_t value) {
            uint32_t result = 1;

            while (result < value) {
                result <<= 1;
            }

            return result;
        };

    m_TextureWidth =
        NextPowerOfTwo(m_TextureWidth);

    m_TextureHeight =
        NextPowerOfTwo(m_TextureHeight);

    //
    // ---------------------------------------------------------
    // 3. Determine mip count and RGBA8 atlas size.
    // ---------------------------------------------------------
    //

    uint32_t mipCount = 0;

    size_t AtlasMipChainSize = 0;

    uint32_t mipW =
        m_TextureWidth;

    uint32_t mipH =
        m_TextureHeight;

    while (true) {
        ++mipCount;

        AtlasMipChainSize +=
            size_t(mipW) *
            size_t(mipH) *
            Channels;

        if (mipW == 1 &&
            mipH == 1) {
            break;
        }

        mipW =
            std::max(
                1u,
                mipW >> 1);

        mipH =
            std::max(
                1u,
                mipH >> 1);
    }

    //
    // ---------------------------------------------------------
    // 4. Build an UNCOMPRESSED RGBA8 atlas mip chain.
    //
    // This buffer is temporary. It is NOT uploaded to BGFX.
    // ---------------------------------------------------------
    //

    std::vector<uint8_t> AtlasMipChain(
        AtlasMipChainSize,
        0);

    size_t mipOffset = 0;

    //
    // Reuse this allocation for every source texture.
    //
    std::vector<uint8_t> decodedMip;

    for (uint32_t mipLevel = 0;
         mipLevel < mipCount;
         ++mipLevel) {
        const uint32_t mipWidth =
            std::max(
                1u,
                m_TextureWidth >> mipLevel);

        const uint32_t mipHeight =
            std::max(
                1u,
                m_TextureHeight >> mipLevel);

        uint8_t *mipDestination =
            AtlasMipChain.data() +
            mipOffset;

        //
        // -----------------------------------------------------
        // Place every texture into this atlas mip.
        // -----------------------------------------------------
        //

        for (auto *texture : PendingTextures) {
            if (texture == nullptr) {
                continue;
            }

            auto allocationIt =
                Allocations.find(
                    texture->ID);

            if (allocationIt ==
                Allocations.end()) {
                continue;
            }

            const AtlasAllocation &allocation =
                allocationIt->second;

            //
            // Texture doesn't have this mip.
            //
            if (mipLevel >=
                texture->MipChain.size()) {
                continue;
            }

            const auto &source =
                texture->MipChain[mipLevel];

            const uint32_t sourceWidth =
                static_cast<uint32_t>(
                    source.Size[0]);

            const uint32_t sourceHeight =
                static_cast<uint32_t>(
                    source.Size[1]);

            if (sourceWidth == 0 ||
                sourceHeight == 0) {
                continue;
            }

            //
            // Atlas position at this mip.
            //
            uint32_t x =
                allocation.X >> mipLevel;

            uint32_t y =
                allocation.Y >> mipLevel;

            //
            // Make sure the source fits.
            //
            if (sourceWidth > mipWidth ||
                sourceHeight > mipHeight) {
                std::cout
                    << "Skipping texture "
                    << texture->ID
                    << " at mip "
                    << mipLevel
                    << " source "
                    << sourceWidth
                    << "x"
                    << sourceHeight
                    << " atlas "
                    << mipWidth
                    << "x"
                    << mipHeight
                    << std::endl;

                continue;
            }

            x =
                std::min(
                    x,
                    mipWidth -
                        sourceWidth);

            y =
                std::min(
                    y,
                    mipHeight -
                        sourceHeight);

            //
            // -------------------------------------------------
            // BC7 -> RGBA8
            // -------------------------------------------------
            //

            if (!DecodeBC7Mip(
                    source,
                    decodedMip)) {
                std::cerr
                    << "Failed to decode BC7 mip "
                    << mipLevel
                    << " for texture "
                    << texture->ID
                    << std::endl;

                continue;
            }

            //
            // -------------------------------------------------
            // RGBA8 -> RGBA8 atlas
            // -------------------------------------------------
            //

            CopyMipIntoAtlas(
                decodedMip.data(),
                sourceWidth,
                sourceHeight,
                x,
                y,
                mipWidth,
                mipHeight,
                mipDestination);
        }

        //
        // Move to next RGBA8 mip.
        //
        mipOffset +=
            size_t(mipWidth) *
            size_t(mipHeight) *
            Channels;
    }

    //
    // ---------------------------------------------------------
    // 5. Now compress every atlas mip individually to BC7.
    // ---------------------------------------------------------
    //

    std::vector<uint8_t>
        CompressedAtlasMipChain;

    //
    // Calculate the total BC7 size so we can reserve once.
    //
    size_t TotalBC7Size = 0;

    mipW = m_TextureWidth;
    mipH = m_TextureHeight;

    while (true) {
        TotalBC7Size +=
            GetBC7MipSize(
                mipW,
                mipH);

        if (mipW == 1 &&
            mipH == 1) {
            break;
        }

        mipW =
            std::max(
                1u,
                mipW >> 1);

        mipH =
            std::max(
                1u,
                mipH >> 1);
    }

    CompressedAtlasMipChain.reserve(
        TotalBC7Size);

    //
    // Reset offset into the RGBA8 atlas.
    //
    mipOffset = 0;

    for (uint32_t mipLevel = 0;
         mipLevel < mipCount;
         ++mipLevel) {
        const uint32_t mipWidth =
            std::max(
                1u,
                m_TextureWidth >> mipLevel);

        const uint32_t mipHeight =
            std::max(
                1u,
                m_TextureHeight >> mipLevel);

        const uint8_t *mipSource =
            AtlasMipChain.data() +
            mipOffset;

        //
        // Temporary compressed mip.
        //
        std::vector<uint8_t>
            compressedMip;

        //
        // -----------------------------------------------------
        // RGBA8 -> BC7
        // -----------------------------------------------------
        //

        if (!CompressRGBA8ToBC7(
                mipSource,
                mipWidth,
                mipHeight,
                compressedMip)) {
            std::cerr
                << "Failed to compress atlas mip "
                << mipLevel
                << " to BC7."
                << std::endl;

            PendingTextures.clear();

            Dirty = false;

            return;
        }

        //
        // Append compressed mip.
        //
        CompressedAtlasMipChain.insert(
            CompressedAtlasMipChain.end(),
            compressedMip.begin(),
            compressedMip.end());

        //
        // Advance through the RGBA8 source.
        //
        mipOffset +=
            size_t(mipWidth) *
            size_t(mipHeight) *
            Channels;
    }

    //
    // ---------------------------------------------------------
    // 6. The RGBA8 atlas is no longer needed.
    // ---------------------------------------------------------
    //

    AtlasMipChain.clear();
    AtlasMipChain.shrink_to_fit();

    //
    // ---------------------------------------------------------
    // 7. Destroy previous GPU texture.
    // ---------------------------------------------------------
    //

    if (bgfx::isValid(TextureHandle)) {
        bgfx::destroy(TextureHandle);

        TextureHandle =
            BGFX_INVALID_HANDLE;
    }

    //
    // ---------------------------------------------------------
    // 8. Upload the ACTUAL BC7 data.
    // ---------------------------------------------------------
    //

    if (CompressedAtlasMipChain.empty()) {
        std::cerr
            << "Compressed atlas is empty."
            << std::endl;

        PendingTextures.clear();

        Dirty = false;

        return;
    }

    TextureHandle =
        bgfx::createTexture2D(
            static_cast<uint16_t>(m_TextureWidth),
            static_cast<uint16_t>(m_TextureHeight),

            false, // <-- NO MIPS: mip-0-only test

            1,

            bgfx::TextureFormat::BC7,

            BGFX_TEXTURE_NONE,

            bgfx::copy(
                CompressedAtlasMipChain.data(),
                static_cast<uint32_t>(
                    GetBC7MipSize(
                        m_TextureWidth,
                        m_TextureHeight))));

    //
    // ---------------------------------------------------------
    // 9. Cleanup.
    // ---------------------------------------------------------
    //

    PendingTextures.clear();

    Dirty = false;
}