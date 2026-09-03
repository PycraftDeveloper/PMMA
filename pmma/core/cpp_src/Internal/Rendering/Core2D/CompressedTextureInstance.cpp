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

static constexpr uint32_t BC7_BLOCK_WIDTH = 4;
static constexpr uint32_t BC7_BLOCK_HEIGHT = 4;
static constexpr size_t BC7_BLOCK_SIZE = 16;

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

static const std::array<uint8_t, BC7_BLOCK_SIZE> &
GetZeroBC7Block() {

    static const std::array<uint8_t, BC7_BLOCK_SIZE> zeroBC7 =
        []() {
            std::array<uint8_t, 64> zeroRGBA{};
            std::array<uint8_t, BC7_BLOCK_SIZE> encoded{};

            bc7enc_encode_block(
                encoded.data(),
                zeroRGBA.data(),
                0xFF,
                16,
                1,
                1);

            return encoded;
        }();

    return zeroBC7;
}

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

    const uint32_t dstBlockX =
        dstX / BC7_BLOCK_WIDTH;

    const uint32_t dstBlockY =
        dstY / BC7_BLOCK_HEIGHT;

    if (dstBlockX >= atlasBlocksX ||
        dstBlockY >= atlasBlocksY) {

        return false;
    }

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

void PMMA::Internal::Rendering::Core2D::CompressedTextureInstance::Assemble() {

    if (!Dirty) {
        return;
    }

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

    const auto RoundUp4 =
        [](uint32_t Value) -> uint32_t {
        return (Value + 3u) & ~3u;
    };

    NewTextureWidth =
        RoundUp4(NewTextureWidth);

    NewTextureHeight =
        RoundUp4(NewTextureHeight);

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

    const size_t AtlasSize =
        GetBC7MipSize(
            NewTextureWidth,
            NewTextureHeight);

    AtlasPixels[BufferID].Data.resize(
        AtlasSize);

    const bool CanPreservePreviousAtlas =
        HasPreviousAtlas &&
        !HasRemovedTextures &&
        !AtlasShrank;

    bool PreservedPreviousAtlas = false;

    if (CanPreservePreviousAtlas) {

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

    if (!PreservedPreviousAtlas) {

        ClearBC7Mip(
            AtlasPixels[BufferID].Data.data(),
            NewTextureWidth,
            NewTextureHeight);
    }

    for (auto *Texture : PendingTextures) {

        if (Texture == nullptr) {
            continue;
        }

        const auto AllocationIt =
            CurrentAllocations.find(
                Texture->ID);

        if (AllocationIt ==
            CurrentAllocations.end()) {

            continue;
        }

        const AtlasAllocation &Allocation =
            AllocationIt->second;

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

        const uint32_t X =
            Allocation.X;

        const uint32_t Y =
            Allocation.Y;

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

    m_TextureWidth =
        NewTextureWidth;

    m_TextureHeight =
        NewTextureHeight;

    if (bgfx::isValid(TextureHandle)) {

        bgfx::destroy(
            TextureHandle);

        TextureHandle =
            BGFX_INVALID_HANDLE;
    }

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

    AtlasPixels[PreviousBufferID].Active = false;
    AtlasPixels[BufferID].Active = true;
    AtlasPixels[BufferID].Clear = false;

    TextureHandle =
        bgfx::createTexture2D(
            static_cast<uint16_t>(
                m_TextureWidth),

            static_cast<uint16_t>(
                m_TextureHeight),

            false,

            1,

            bgfx::TextureFormat::BC7,

            BGFX_TEXTURE_NONE,

            bgfx::makeRef(
                AtlasPixels[BufferID].Data.data(),
                static_cast<uint32_t>(
                    AtlasPixels[BufferID].Data.size())));

    Dirty = false;

    PreviousBufferID =
        BufferID;

    BufferID =
        (BufferID + 1) % 4;

    FramesSinceLastChange = 0;
}
