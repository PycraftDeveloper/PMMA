#include <algorithm>
#include <array>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <stdexcept>
#include <vector>

#include <bc7enc_wrapper.hpp>

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
    const PMMA::Internal::Rendering::Core2D::MipData &source,
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

void PMMA::Internal::Rendering::Core2D::CompressedTextureInstance::Assemble() {

    if (!Dirty) {
        return;
    }

    // ========================================================================
    // 1. Determine atlas dimensions.
    //
    // Every texture is treated as an independent texture.
    // This atlas contains ONLY the mip selected by MipLevel.
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
    // 3. Allocate one BC7 atlas.
    //
    // There are NO atlas mip levels.
    // MipLevel was already selected when the textures were registered.
    // ========================================================================

    const size_t atlasSize =
        GetBC7MipSize(
            m_TextureWidth,
            m_TextureHeight);

    std::vector<uint8_t> compressedAtlas(
        atlasSize);

    // ========================================================================
    // 4. Initialize the atlas to transparent black.
    // ========================================================================

    ClearBC7Mip(
        compressedAtlas.data(),
        m_TextureWidth,
        m_TextureHeight);

    // ========================================================================
    // 5. Copy the selected mip of every texture into the atlas.
    //
    // Each mip is treated as an independent texture.
    // ========================================================================

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

        // --------------------------------------------------------------------
        // The requested mip does not exist.
        // --------------------------------------------------------------------

        if (MipLevel >=
            texture->MipChain.size()) {

            std::cerr
                << "Texture "
                << texture->ID
                << " does not contain mip "
                << MipLevel
                << "."
                << std::endl;

            continue;
        }

        // --------------------------------------------------------------------
        // Get ONLY the requested mip.
        // --------------------------------------------------------------------

        const auto &source =
            texture->MipChain[MipLevel];

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

        // --------------------------------------------------------------------
        // The allocation was made for this exact mip, so use its position
        // directly.
        //
        // DO NOT divide the coordinates by MipLevel.
        // --------------------------------------------------------------------

        uint32_t x =
            allocation.X;

        uint32_t y =
            allocation.Y;

        // --------------------------------------------------------------------
        // BC7 requires block-aligned destinations.
        // --------------------------------------------------------------------

        if ((x & 3u) != 0 ||
            (y & 3u) != 0) {

            std::cerr
                << "Cannot atlas texture "
                << texture->ID
                << " at mip "
                << MipLevel
                << ". Atlas position "
                << x
                << ", "
                << y
                << " is not BC7 4x4 aligned."
                << std::endl;

            continue;
        }

        // --------------------------------------------------------------------
        // Make sure the selected mip fits.
        // --------------------------------------------------------------------

        if (sourceWidth > m_TextureWidth ||
            sourceHeight > m_TextureHeight) {

            std::cerr
                << "Skipping texture "
                << texture->ID
                << " at mip "
                << MipLevel
                << ". Source is "
                << sourceWidth
                << "x"
                << sourceHeight
                << ", atlas is "
                << m_TextureWidth
                << "x"
                << m_TextureHeight
                << "."
                << std::endl;

            continue;
        }

        // --------------------------------------------------------------------
        // Destination must contain the entire texture.
        // --------------------------------------------------------------------

        if (x + sourceWidth > m_TextureWidth ||
            y + sourceHeight > m_TextureHeight) {

            std::cerr
                << "Texture "
                << texture->ID
                << " does not fit in atlas at "
                << x
                << ", "
                << y
                << "."
                << std::endl;

            continue;
        }

        // --------------------------------------------------------------------
        // Direct BC7 -> BC7 block copy.
        // --------------------------------------------------------------------

        if (!CopyBC7MipIntoAtlas(
                source,
                sourceWidth,
                sourceHeight,
                x,
                y,
                m_TextureWidth,
                m_TextureHeight,
                compressedAtlas.data())) {

            std::cerr
                << "Failed to copy mip "
                << MipLevel
                << " for texture "
                << texture->ID
                << "."
                << std::endl;

            continue;
        }
    }

    // ========================================================================
    // 6. Destroy previous GPU texture.
    // ========================================================================

    if (bgfx::isValid(TextureHandle)) {

        bgfx::destroy(
            TextureHandle);

        TextureHandle =
            BGFX_INVALID_HANDLE;
    }

    // ========================================================================
    // 7. Upload ONE BC7 texture.
    //
    // This texture has no mip chain.
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

            false, // no mipmaps

            1, // layers

            bgfx::TextureFormat::BC7,

            BGFX_TEXTURE_NONE,

            bgfx::copy(
                compressedAtlas.data(),

                static_cast<uint32_t>(
                    compressedAtlas.size())));

    // ========================================================================
    // 8. Cleanup.
    // ========================================================================

    PendingTextures.clear();

    Dirty = false;
}