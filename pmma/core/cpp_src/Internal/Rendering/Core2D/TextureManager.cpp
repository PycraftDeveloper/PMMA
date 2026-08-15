#include <algorithm>
#include <array>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <stdexcept>
#include <vector>

#include <bc7enc_wrapper.hpp>

#include "PMMA_Core.hpp"

// ============================================================================
// BC7 helpers
// ============================================================================

static constexpr uint32_t BC7_BLOCK_WIDTH = 4;
static constexpr uint32_t BC7_BLOCK_HEIGHT = 4;
static constexpr size_t BC7_BLOCK_SIZE = 16;

// ============================================================================
// Get compressed BC7 mip size
// ============================================================================

static size_t GetBC7MipSize(
    uint32_t width,
    uint32_t height) {

    const uint32_t blocksX =
        (width + BC7_BLOCK_WIDTH - 1) /
        BC7_BLOCK_WIDTH;

    const uint32_t blocksY =
        (height + BC7_BLOCK_HEIGHT - 1) /
        BC7_BLOCK_HEIGHT;

    return size_t(blocksX) *
           size_t(blocksY) *
           BC7_BLOCK_SIZE;
}

// ============================================================================
// Generate one valid BC7 block representing transparent black.
//
// This is used to initialize unused portions of the atlas.
//
// It is generated only once.
// ============================================================================

static const std::array<uint8_t, BC7_BLOCK_SIZE> &
GetZeroBC7Block() {

    static const std::array<uint8_t, BC7_BLOCK_SIZE> zeroBC7 =
        []() {
            std::array<uint8_t, 64> zeroRGBA{};
            std::array<uint8_t, BC7_BLOCK_SIZE> encoded{};

            bc7enc_encode_block(
                encoded.data(),
                zeroRGBA.data(),
                0xFF, // all modes
                16,   // max partitions
                1,    // uber level
                1);   // perceptual

            return encoded;
        }();

    return zeroBC7;
}

// ============================================================================
// Fill an entire BC7 mip with one BC7 block.
//
// This avoids having to memset compressed data, since a BC7 block is not
// necessarily represented by all-zero bytes.
//
// The atlas therefore starts as completely transparent black.
// ============================================================================

static inline void ClearBC7Mip(
    uint8_t *atlas,
    uint32_t width,
    uint32_t height) {
    if (!atlas || width == 0 || height == 0)
        return;

    const size_t blocksX =
        (size_t(width) + BC7_BLOCK_WIDTH - 1) /
        BC7_BLOCK_WIDTH;

    const size_t blocksY =
        (size_t(height) + BC7_BLOCK_HEIGHT - 1) /
        BC7_BLOCK_HEIGHT;

    const size_t totalBytes =
        blocksX * blocksY * BC7_BLOCK_SIZE;

    const auto &zeroBC7 = GetZeroBC7Block();

    // First 16 bytes.
    std::memcpy(atlas, zeroBC7.data(), BC7_BLOCK_SIZE);

    size_t filled = BC7_BLOCK_SIZE;

    while (filled < totalBytes) {
        const size_t copySize =
            std::min(filled, totalBytes - filled);

        std::memcpy(
            atlas + filled,
            atlas,
            copySize);

        filled += copySize;
    }
}

// ============================================================================
// Copy a BC7 mip directly into a BC7 atlas.
//
// IMPORTANT:
//
// BC7 operates on 4x4 pixel blocks. Therefore dstX and dstY must be aligned
// to 4 pixels.
//
// No decoding or encoding happens here.
//
// The source PixelData is copied block-for-block.
//
// ============================================================================

static inline bool CopyBC7MipIntoAtlas(
    const PMMA::Internal::MipData &source,
    uint32_t sourceWidth,
    uint32_t sourceHeight,
    uint32_t dstX,
    uint32_t dstY,
    uint32_t atlasWidth,
    uint32_t atlasHeight,
    uint8_t *atlas) {

    if (!atlas ||
        sourceWidth == 0 ||
        sourceHeight == 0 ||
        atlasWidth == 0 ||
        atlasHeight == 0) {

        return false;
    }

    // ------------------------------------------------------------------------
    // BC7 requires the destination to start on a block boundary.
    // ------------------------------------------------------------------------

    if ((dstX & 3u) != 0 ||
        (dstY & 3u) != 0) {

        std::cerr
            << "Cannot copy BC7 mip at unaligned atlas position "
            << dstX
            << ", "
            << dstY
            << ". BC7 positions must be 4-pixel aligned."
            << std::endl;

        return false;
    }

    // ------------------------------------------------------------------------
    // Calculate source and destination block dimensions.
    // ------------------------------------------------------------------------

    const uint32_t sourceBlocksX =
        (sourceWidth + BC7_BLOCK_WIDTH - 1) /
        BC7_BLOCK_WIDTH;

    const uint32_t sourceBlocksY =
        (sourceHeight + BC7_BLOCK_HEIGHT - 1) /
        BC7_BLOCK_HEIGHT;

    const uint32_t atlasBlocksX =
        (atlasWidth + BC7_BLOCK_WIDTH - 1) /
        BC7_BLOCK_WIDTH;

    const uint32_t atlasBlocksY =
        (atlasHeight + BC7_BLOCK_HEIGHT - 1) /
        BC7_BLOCK_HEIGHT;

    // ------------------------------------------------------------------------
    // Validate the cached BC7 data.
    // ------------------------------------------------------------------------

    const size_t expectedSize =
        size_t(sourceBlocksX) *
        size_t(sourceBlocksY) *
        BC7_BLOCK_SIZE;

    if (source.PixelData.size() != expectedSize) {

        std::cerr
            << "Invalid BC7 mip size. Expected "
            << expectedSize
            << " bytes but got "
            << source.PixelData.size()
            << " bytes."
            << std::endl;

        return false;
    }

    // ------------------------------------------------------------------------
    // Destination block position.
    // ------------------------------------------------------------------------

    const uint32_t dstBlockX =
        dstX / BC7_BLOCK_WIDTH;

    const uint32_t dstBlockY =
        dstY / BC7_BLOCK_HEIGHT;

    if (dstBlockX >= atlasBlocksX ||
        dstBlockY >= atlasBlocksY) {

        return false;
    }

    // ------------------------------------------------------------------------
    // Number of complete BC7 blocks that fit.
    //
    // We copy complete compressed blocks only.
    // ------------------------------------------------------------------------

    const uint32_t copyBlocksX =
        std::min(
            sourceBlocksX,
            atlasBlocksX - dstBlockX);

    const uint32_t copyBlocksY =
        std::min(
            sourceBlocksY,
            atlasBlocksY - dstBlockY);

    if (copyBlocksX == 0 ||
        copyBlocksY == 0) {

        return false;
    }

    // ------------------------------------------------------------------------
    // Copy complete BC7 rows.
    //
    // One BC7 block = 16 bytes.
    //
    // This means a whole row of blocks can be copied with ONE memcpy.
    // ------------------------------------------------------------------------

    const uint8_t *sourceData =
        source.PixelData.data();

    for (uint32_t blockY = 0;
         blockY < copyBlocksY;
         ++blockY) {

        const uint8_t *sourceRow =
            sourceData +
            size_t(blockY) *
                size_t(sourceBlocksX) *
                BC7_BLOCK_SIZE;

        uint8_t *destinationRow =
            atlas +
            (size_t(dstBlockY + blockY) *
                 size_t(atlasBlocksX) +
             size_t(dstBlockX)) *
                BC7_BLOCK_SIZE;

        std::memcpy(
            destinationRow,
            sourceRow,
            size_t(copyBlocksX) *
                BC7_BLOCK_SIZE);
    }

    return true;
}

// ============================================================================
// Assemble
//
// Builds the atlas directly in BC7 format.
//
// Pipeline:
//
//     cached BC7 texture
//             |
//             | memcpy 16-byte blocks
//             v
//         BC7 atlas
//             |
//             v
//         bgfx texture
//
// There is NO:
//
//     BC7 -> RGBA8
//
// and NO:
//
//     RGBA8 -> BC7
//
// ============================================================================

void PMMA::Internal::Rendering::Core2D::TextureManager::Assemble() {

    if (!Dirty) {
        return;
    }

    // ========================================================================
    // 1. Determine atlas dimensions from mip 0.
    // ========================================================================

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

    // ========================================================================
    // 2. BC7 operates on 4x4 blocks.
    //
    // Round the atlas dimensions up to the next BC7 block boundary.
    // ========================================================================

    auto RoundUp4 =
        [](uint32_t value) {
            return (value + 3u) & ~3u;
        };

    m_TextureWidth =
        RoundUp4(m_TextureWidth);

    m_TextureHeight =
        RoundUp4(m_TextureHeight);

    // ========================================================================
    // 3. Determine mip count and total BC7 atlas size.
    // ========================================================================

    uint32_t mipCount = 0;

    size_t totalBC7Size = 0;

    uint32_t mipW =
        m_TextureWidth;

    uint32_t mipH =
        m_TextureHeight;

    while (true) {

        ++mipCount;

        totalBC7Size +=
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

    // ========================================================================
    // 4. Allocate the final BC7 atlas.
    //
    // There is no temporary RGBA8 atlas anymore.
    // ========================================================================

    std::vector<uint8_t> compressedAtlas(
        totalBC7Size);

    // ========================================================================
    // 5. Initialize every atlas block to transparent black.
    //
    // This means areas not occupied by textures are valid BC7 blocks.
    // ========================================================================

    size_t mipOffset = 0;

    mipW =
        m_TextureWidth;

    mipH =
        m_TextureHeight;

    for (uint32_t mipLevel = 0;
         mipLevel < mipCount;
         ++mipLevel) {

        uint8_t *mipDestination =
            compressedAtlas.data() +
            mipOffset;

        ClearBC7Mip(
            mipDestination,
            mipW,
            mipH);

        mipOffset +=
            GetBC7MipSize(
                mipW,
                mipH);

        mipW =
            std::max(
                1u,
                mipW >> 1);

        mipH =
            std::max(
                1u,
                mipH >> 1);
    }

    // ========================================================================
    // 6. Copy cached BC7 textures directly into the atlas.
    // ========================================================================

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

        uint8_t *mipDestination =
            compressedAtlas.data() +
            mipOffset;

        // --------------------------------------------------------------------
        // Process every pending texture.
        // --------------------------------------------------------------------

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

            // ----------------------------------------------------------------
            // Texture does not contain this mip.
            // ----------------------------------------------------------------

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

            // ----------------------------------------------------------------
            // Calculate the texture's position at this mip.
            // ----------------------------------------------------------------

            uint32_t x =
                allocation.X >>
                mipLevel;

            uint32_t y =
                allocation.Y >>
                mipLevel;

            // ----------------------------------------------------------------
            // BC7 alignment check.
            //
            // The source cannot be shifted by a non-block-aligned amount.
            // ----------------------------------------------------------------

            if ((x & 3u) != 0 ||
                (y & 3u) != 0) {

                /*std::cerr
                    << "Cannot atlas texture "
                    << texture->ID
                    << " at mip "
                    << mipLevel
                    << ". "
                    << "Atlas position "
                    << x
                    << ", "
                    << y
                    << " is not BC7 4x4 aligned."
                    << std::endl;*/

                continue;
            }

            // ----------------------------------------------------------------
            // Check that the source fits into the atlas mip.
            // ----------------------------------------------------------------

            if (sourceWidth > mipWidth ||
                sourceHeight > mipHeight) {

                std::cerr
                    << "Skipping texture "
                    << texture->ID
                    << " at mip "
                    << mipLevel
                    << ". Source is "
                    << sourceWidth
                    << "x"
                    << sourceHeight
                    << ", atlas mip is "
                    << mipWidth
                    << "x"
                    << mipHeight
                    << "."
                    << std::endl;

                continue;
            }

            // ----------------------------------------------------------------
            // Clamp destination position so the nominal source rectangle fits.
            // ----------------------------------------------------------------

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

            // ----------------------------------------------------------------
            // IMPORTANT:
            //
            // The clamp above can theoretically produce a non-aligned
            // coordinate.
            //
            // Do NOT round it here, because that would change the placement.
            // Just reject the placement.
            // ----------------------------------------------------------------

            if ((x & 3u) != 0 ||
                (y & 3u) != 0) {

                std::cerr
                    << "Texture "
                    << texture->ID
                    << " became unaligned after atlas clamping at mip "
                    << mipLevel
                    << "."
                    << std::endl;

                continue;
            }

            // ----------------------------------------------------------------
            // Direct BC7 -> BC7 block copy.
            // ----------------------------------------------------------------

            if (!CopyBC7MipIntoAtlas(
                    source,
                    sourceWidth,
                    sourceHeight,
                    x,
                    y,
                    mipWidth,
                    mipHeight,
                    mipDestination)) {

                std::cerr
                    << "Failed to copy BC7 mip "
                    << mipLevel
                    << " for texture "
                    << texture->ID
                    << "."
                    << std::endl;

                continue;
            }
        }

        // --------------------------------------------------------------------
        // Advance to the next compressed mip.
        // --------------------------------------------------------------------

        mipOffset +=
            GetBC7MipSize(
                mipWidth,
                mipHeight);
    }

    // ========================================================================
    // 7. Destroy previous GPU texture.
    // ========================================================================

    if (bgfx::isValid(TextureHandle)) {

        bgfx::destroy(
            TextureHandle);

        TextureHandle =
            BGFX_INVALID_HANDLE;
    }

    // ========================================================================
    // 8. Upload the BC7 atlas directly.
    // ========================================================================

    if (compressedAtlas.empty()) {

        std::cerr
            << "Compressed atlas is empty."
            << std::endl;

        PendingTextures.clear();

        Dirty = false;

        return;
    }

    TextureHandle =
        bgfx::createTexture2D(
            static_cast<uint16_t>(
                m_TextureWidth),

            static_cast<uint16_t>(
                m_TextureHeight),

            true, // has mipmaps

            1, // layers

            bgfx::TextureFormat::BC7,

            BGFX_TEXTURE_NONE,

            bgfx::copy(
                compressedAtlas.data(),

                static_cast<uint32_t>(
                    compressedAtlas.size())));

    // ========================================================================
    // 9. Cleanup.
    // ========================================================================

    PendingTextures.clear();

    Dirty = false;
}