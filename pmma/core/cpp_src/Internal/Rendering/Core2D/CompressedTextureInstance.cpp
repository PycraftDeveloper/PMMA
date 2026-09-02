#include <algorithm>
#include <array>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <stdexcept>
#include <vector>

#include <bc7enc_wrapper.hpp>

#include "Internal/Rendering/Core2D/Base.hpp"
#include "Internal/Rendering/Core2D/CompressedTextureInstance.hpp"

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

    // ========================================================================
    // 0. Nothing changed.
    //
    // RegisterTexture() and FinalizeAllocationCache() have already determined
    // that the current frame has exactly the same atlas layout as the
    // previous frame.
    //
    // The existing CPU/GPU atlas is therefore still authoritative.
    //
    // Do absolutely nothing here.
    // ========================================================================

    if (!Dirty) {
        return;
    }

    // ========================================================================
    // 1. Determine the required dimensions of the new atlas.
    //
    // CurrentAllocations contains the FINAL allocation for every texture
    // which exists in the current frame.
    //
    // Importantly, this is independent of PendingTextures.
    //
    // PendingTextures is not authoritative because a texture can already
    // have a cached allocation and still be required in the newly assembled
    // atlas.
    // ========================================================================

    uint32_t NewTextureWidth = 1;
    uint32_t NewTextureHeight = 1;

    for (const auto &[TextureID, Allocation] :
         CurrentAllocations) {

        (void)TextureID;

        NewTextureWidth =
            std::max(
                NewTextureWidth,
                Allocation.X +
                    Allocation.Width);

        NewTextureHeight =
            std::max(
                NewTextureHeight,
                Allocation.Y +
                    Allocation.Height);
    }

    // ========================================================================
    // 2. BC7 operates on 4x4 blocks.
    // ========================================================================

    const auto RoundUp4 =
        [](uint32_t Value) -> uint32_t {
        return (Value + 3u) & ~3u;
    };

    NewTextureWidth =
        RoundUp4(NewTextureWidth);

    NewTextureHeight =
        RoundUp4(NewTextureHeight);

    // ========================================================================
    // 3. Determine whether the previous CPU atlas is usable as a starting
    //    point.
    //
    // There are two separate concepts here:
    //
    //   - PreviousAllocations tells us where each texture used to live.
    //   - CurrentAllocations tells us where each texture lives now.
    //
    // If a texture still exists and its allocation is unchanged, its pixels
    // can be retained directly from the previous atlas.
    //
    // If the atlas grew, the old atlas can still be copied into the new one.
    //
    // If the atlas shrank, the old BC7 rows cannot simply be retained because
    // the destination row stride has changed. In that case we reconstruct
    // the atlas from CurrentTextures.
    //
    // A removal also forces a reconstruction. Otherwise stale pixels belonging
    // to removed textures could remain in the atlas.
    // ========================================================================

    const uint32_t PreviousTextureWidth =
        m_TextureWidth;

    const uint32_t PreviousTextureHeight =
        m_TextureHeight;

    const bool HasPreviousAtlas =
        PreviousTextureWidth != 0 &&
        PreviousTextureHeight != 0 &&
        !AtlasPixels[PreviousBufferID].Data.empty();

    const bool AtlasGrew =
        HasPreviousAtlas &&
        (NewTextureWidth > PreviousTextureWidth ||
         NewTextureHeight > PreviousTextureHeight);

    const bool AtlasShrank =
        HasPreviousAtlas &&
        (NewTextureWidth < PreviousTextureWidth ||
         NewTextureHeight < PreviousTextureHeight);

    // ========================================================================
    // 4. Allocate the destination CPU atlas.
    //
    // BufferID is the CPU buffer which will become the new atlas.
    // ========================================================================

    const size_t AtlasSize =
        GetBC7MipSize(
            NewTextureWidth,
            NewTextureHeight);

    AtlasPixels[BufferID].Data.resize(
        AtlasSize);

    // ========================================================================
    // 5. Decide whether we can preserve the previous atlas.
    //
    // We can preserve it when:
    //
    //   - a previous atlas exists
    //   - no textures were removed
    //
    // Atlas growth is explicitly supported.
    //
    // Atlas shrink is not preserved because the BC7 row stride changes.
    //
    // NOTE:
    //
    // Even when the old atlas is preserved, individual textures whose
    // allocations changed will be overwritten later from CurrentTextures.
    // ========================================================================

    const bool CanPreservePreviousAtlas =
        HasPreviousAtlas &&
        !HasRemovedTextures &&
        !AtlasShrank;

    bool PreservedPreviousAtlas = false;

    if (CanPreservePreviousAtlas) {

        // --------------------------------------------------------------------
        // Copy the old BC7 atlas into the new buffer.
        //
        // We cannot memcpy the whole atlas when it grew because the number
        // of BC7 blocks per row may have changed.
        // --------------------------------------------------------------------

        constexpr size_t BC7BlockSize = 16;

        const uint32_t SourceBlocksX =
            PreviousTextureWidth / 4;

        const uint32_t SourceBlocksY =
            PreviousTextureHeight / 4;

        const uint32_t DestinationBlocksX =
            NewTextureWidth / 4;

        const uint32_t DestinationBlocksY =
            NewTextureHeight / 4;

        const uint32_t BlocksToCopyX =
            std::min(
                SourceBlocksX,
                DestinationBlocksX);

        const uint32_t BlocksToCopyY =
            std::min(
                SourceBlocksY,
                DestinationBlocksY);

        const size_t SourceRowSize =
            static_cast<size_t>(
                SourceBlocksX) *
            BC7BlockSize;

        const size_t DestinationRowSize =
            static_cast<size_t>(
                DestinationBlocksX) *
            BC7BlockSize;

        const size_t BytesToCopyPerRow =
            static_cast<size_t>(
                BlocksToCopyX) *
            BC7BlockSize;

        const auto &Source =
            AtlasPixels[PreviousBufferID];

        auto &Destination =
            AtlasPixels[BufferID];

        for (uint32_t BlockY = 0;
             BlockY < BlocksToCopyY;
             ++BlockY) {

            const size_t SourceOffset =
                static_cast<size_t>(BlockY) *
                SourceRowSize;

            const size_t DestinationOffset =
                static_cast<size_t>(BlockY) *
                DestinationRowSize;

            std::copy_n(
                Source.Data.data() +
                    SourceOffset,
                BytesToCopyPerRow,
                Destination.Data.data() +
                    DestinationOffset);
        }

        PreservedPreviousAtlas = true;
    }

    // ========================================================================
    // 6. If the previous atlas could not be preserved, start from a completely
    //    clean atlas.
    //
    // This handles:
    //
    //   - first assembly
    //   - texture removal
    //   - atlas shrink
    //   - replacement/re-layout where the previous atlas is no longer
    //     authoritative
    // ========================================================================

    if (!PreservedPreviousAtlas) {

        ClearBC7Mip(
            AtlasPixels[BufferID].Data.data(),
            NewTextureWidth,
            NewTextureHeight);
    }

    // ========================================================================
    // 7. Copy the current textures into the atlas.
    //
    // CurrentTextures is the authoritative source of textures for this
    // frame.
    //
    // We deliberately do NOT iterate PendingTextures here.
    //
    // ------------------------------------------------------------------------
    //
    // If the previous atlas was preserved:
    //
    //   Existing texture + same allocation
    //       -> already present, skip
    //
    //   Existing texture + changed allocation
    //       -> copy again
    //
    //   New texture
    //       -> copy
    //
    // If the previous atlas was not preserved:
    //
    //   Every current texture is copied.
    //
    // This correctly handles both growth and shrinkage.
    // ========================================================================

    // ========================================================================
    // 7. Copy textures into the atlas.
    //
    // PendingTextures contains the texture objects registered during the
    // current frame.
    //
    // If the previous atlas was preserved, textures which still have exactly
    // the same allocation are already present in the copied atlas and do not
    // need to be copied again.
    //
    // If the previous atlas was NOT preserved, every current texture must be
    // copied into the newly cleared atlas.
    // ========================================================================

    for (auto *Texture : PendingTextures) {

        if (Texture == nullptr) {
            continue;
        }

        // --------------------------------------------------------------------
        // Find the final allocation for this texture.
        // --------------------------------------------------------------------

        const auto AllocationIt =
            CurrentAllocations.find(
                Texture->ID);

        if (AllocationIt ==
            CurrentAllocations.end()) {

            continue;
        }

        const AtlasAllocation &Allocation =
            AllocationIt->second;

        // --------------------------------------------------------------------
        // If the old atlas was preserved and this texture existed previously
        // at exactly the same location and size, its pixels are already in
        // the destination atlas.
        //
        // There is no need to copy it again.
        // --------------------------------------------------------------------

        if (PreservedPreviousAtlas) {

            const auto PreviousIt =
                PreviousAllocations.find(
                    Texture->ID);

            if (PreviousIt !=
                PreviousAllocations.end()) {

                const AtlasAllocation
                    &PreviousAllocation =
                        PreviousIt->second;

                const bool SameAllocation =
                    PreviousAllocation.X ==
                        Allocation.X &&
                    PreviousAllocation.Y ==
                        Allocation.Y &&
                    PreviousAllocation.Width ==
                        Allocation.Width &&
                    PreviousAllocation.Height ==
                        Allocation.Height;

                if (SameAllocation) {
                    continue;
                }
            }
        }

        // --------------------------------------------------------------------
        // The requested mip must exist.
        // --------------------------------------------------------------------

        if (MipLevel >=
            Texture->MipChain.size()) {

            std::cerr
                << "Texture "
                << Texture->ID
                << " does not contain mip "
                << MipLevel
                << "."
                << std::endl;

            continue;
        }

        // --------------------------------------------------------------------
        // Get ONLY the selected mip.
        // --------------------------------------------------------------------

        const auto &Source =
            Texture->MipChain[MipLevel];

        const uint32_t SourceWidth =
            static_cast<uint32_t>(
                Source.Size[0]);

        const uint32_t SourceHeight =
            static_cast<uint32_t>(
                Source.Size[1]);

        if (SourceWidth == 0 ||
            SourceHeight == 0) {

            continue;
        }

        // --------------------------------------------------------------------
        // Allocation coordinates are already in atlas coordinates.
        //
        // DO NOT divide by MipLevel.
        // --------------------------------------------------------------------

        const uint32_t X =
            Allocation.X;

        const uint32_t Y =
            Allocation.Y;

        // --------------------------------------------------------------------
        // BC7 requires block-aligned destinations.
        // --------------------------------------------------------------------

        if ((X & 3u) != 0 ||
            (Y & 3u) != 0) {

            std::cerr
                << "Cannot atlas texture "
                << Texture->ID
                << " at mip "
                << MipLevel
                << ". Atlas position "
                << X
                << ", "
                << Y
                << " is not BC7 4x4 aligned."
                << std::endl;

            continue;
        }

        // --------------------------------------------------------------------
        // Verify that the cached allocation is large enough for the source.
        // --------------------------------------------------------------------

        if (Allocation.Width <
                SourceWidth ||
            Allocation.Height <
                SourceHeight) {

            std::cerr
                << "Texture "
                << Texture->ID
                << " allocation is too small for mip "
                << MipLevel
                << ". Allocation is "
                << Allocation.Width
                << "x"
                << Allocation.Height
                << ", source is "
                << SourceWidth
                << "x"
                << SourceHeight
                << "."
                << std::endl;

            continue;
        }

        // --------------------------------------------------------------------
        // Verify that the source fits inside the new atlas.
        // --------------------------------------------------------------------

        if (X + SourceWidth >
                NewTextureWidth ||
            Y + SourceHeight >
                NewTextureHeight) {

            std::cerr
                << "Texture "
                << Texture->ID
                << " does not fit in atlas at "
                << X
                << ", "
                << Y
                << "."
                << std::endl;

            continue;
        }

        // --------------------------------------------------------------------
        // Copy BC7 blocks directly into the atlas.
        // --------------------------------------------------------------------

        if (!CopyBC7MipIntoAtlas(
                Source,
                SourceWidth,
                SourceHeight,
                X,
                Y,
                NewTextureWidth,
                NewTextureHeight,
                AtlasPixels[BufferID].Data.data())) {

            std::cerr
                << "Failed to copy mip "
                << MipLevel
                << " for texture "
                << Texture->ID
                << "."
                << std::endl;

            continue;
        }
    }

    // ========================================================================
    // 8. The CPU atlas is now complete.
    // ========================================================================

    m_TextureWidth =
        NewTextureWidth;

    m_TextureHeight =
        NewTextureHeight;

    // ========================================================================
    // 9. Replace the GPU atlas.
    //
    // We only reach this point when Dirty was true.
    // ========================================================================

    if (bgfx::isValid(TextureHandle)) {

        bgfx::destroy(
            TextureHandle);

        TextureHandle =
            BGFX_INVALID_HANDLE;
    }

    // ========================================================================
    // 10. Empty atlas handling.
    // ========================================================================

    if (AtlasPixels[BufferID].Data.empty()) {

        std::cerr
            << "Compressed atlas is empty."
            << std::endl;

        Dirty = false;

        PreviousBufferID =
            BufferID;

        BufferID =
            (BufferID + 1) % 4;

        return;
    }

    // ========================================================================
    // 11. Upload ONE BC7 texture.
    //
    // This atlas contains no mip chain.
    // ========================================================================

    AtlasPixels[PreviousBufferID].Active = false;
    AtlasPixels[BufferID].Active = true;
    AtlasPixels[BufferID].Clear = false;

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

            bgfx::makeRef(
                AtlasPixels[BufferID].Data.data(),
                static_cast<uint32_t>(
                    AtlasPixels[BufferID].Data.size())));

    // ========================================================================
    // 12. Finalise the CPU buffer rotation.
    //
    // The buffer we just uploaded becomes the authoritative previous atlas
    // for the next frame.
    // ========================================================================

    Dirty = false;

    PreviousBufferID =
        BufferID;

    BufferID =
        (BufferID + 1) % 4;

    FramesSinceLastChange = 0;
}