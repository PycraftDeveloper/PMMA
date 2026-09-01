#pragma once

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <string>
#include <vector>

#include <bgfx/bgfx.h>

#include "Constants.hpp"
#include "Internal/Internal.hpp"

namespace PMMA::Internal::Rendering::Core2D {

class CompressedTextureInstance {
private:
    std::vector<PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *> PendingTextures;

    std::vector<PMMA::Internal::Rendering::Core2D::SkylineNode> Skyline;

    // ------------------------------------------------------------------------
    // Calculate the exact rectangle that will be reserved in the skyline.
    //
    // This is deliberately shared by CanFitTexture() and RegisterTexture()
    // so that the two operations can never disagree about BC7 alignment or
    // padding.
    // ------------------------------------------------------------------------
    inline bool GetPackedDimensions(
        const PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *Texture,
        uint32_t &OutMipWidth,
        uint32_t &OutMipHeight,
        uint32_t &OutAlignedWidth,
        uint32_t &OutAlignedHeight,
        uint32_t &OutPackedWidth,
        uint32_t &OutPackedHeight,
        uint32_t &OutAlignedPadding) const {

        if (Texture == nullptr ||
            MipLevel >= Texture->MipChain.size()) {
            return false;
        }

        const auto &Mip =
            Texture->MipChain[MipLevel];

        const uint32_t MipWidth =
            static_cast<uint32_t>(Mip.Size[0]);

        const uint32_t MipHeight =
            static_cast<uint32_t>(Mip.Size[1]);

        if (MipWidth == 0 ||
            MipHeight == 0) {
            return false;
        }

        const uint32_t AlignedWidth =
            AlignUp4(MipWidth);

        const uint32_t AlignedHeight =
            AlignUp4(MipHeight);

        const uint32_t AlignedPadding =
            AlignUp4(AtlasPadding);

        const uint32_t PackedWidth =
            AlignedWidth + AlignedPadding * 2;

        const uint32_t PackedHeight =
            AlignedHeight + AlignedPadding * 2;

        OutMipWidth = MipWidth;
        OutMipHeight = MipHeight;

        OutAlignedWidth = AlignedWidth;
        OutAlignedHeight = AlignedHeight;

        OutPackedWidth = PackedWidth;
        OutPackedHeight = PackedHeight;

        OutAlignedPadding = AlignedPadding;

        return true;
    }

public:
    std::unordered_map<uintptr_t, AtlasAllocation> PreviousAllocations;
    std::unordered_map<uintptr_t, AtlasAllocation> CurrentAllocations;

    std::array<std::vector<unsigned char>, 4> AtlasPixels;

    uint32_t AtlasPadding = 0;
    uint32_t MipLevel = 0;

public:
    bool Dirty = false;

    char BufferID = 0;
    char PreviousBufferID = 0;

    bgfx::TextureHandle TextureHandle = BGFX_INVALID_HANDLE;

    uint32_t m_TextureWidth = 0;
    uint32_t m_TextureHeight = 0;
    uint32_t MaxTextureDimension = 1024;
    uintptr_t RenderPipelineInstanceID;

    static constexpr uint32_t BC7_ALIGNMENT = 4;

    static constexpr uint32_t AlignUp4(
        uint32_t value) noexcept {

        return (value + (BC7_ALIGNMENT - 1)) &
               ~(BC7_ALIGNMENT - 1);
    }

    static constexpr uint32_t AlignDown4(
        uint32_t value) noexcept {

        return value &
               ~(BC7_ALIGNMENT - 1);
    }

    CompressedTextureInstance(
        uintptr_t NewRenderPipelineInstanceID,
        uint32_t NewMaxTextureDimension,
        uint32_t NewMipLevel)
        : MipLevel(NewMipLevel),
          MaxTextureDimension(NewMaxTextureDimension),
          RenderPipelineInstanceID(NewRenderPipelineInstanceID) {

        Skyline.reserve(64);

        Skyline.push_back(
            {0,
             0,
             MaxTextureDimension});
    }

    ~CompressedTextureInstance() {
        if (bgfx::isValid(TextureHandle)) {
            bgfx::destroy(TextureHandle);
        }
    }

    inline void Reset() {
        PreviousAllocations = std::move(CurrentAllocations);
        CurrentAllocations.clear();

        // Reuse the existing allocation rather than forcing a new allocation.
        Skyline.clear();
        Skyline.push_back(
            {0,
             0,
             MaxTextureDimension});

        Dirty = false;
    }

    // ------------------------------------------------------------------------
    // Query whether this exact texture can be inserted.
    //
    // This is a pure query. The caller guarantees that RegisterTexture()
    // for this same texture follows before another texture is added.
    // ------------------------------------------------------------------------
    inline bool CanFitTexture(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *Texture) {

        uint32_t MipWidth;
        uint32_t MipHeight;
        uint32_t AlignedWidth;
        uint32_t AlignedHeight;
        uint32_t PackedWidth;
        uint32_t PackedHeight;
        uint32_t AlignedPadding;

        if (!GetPackedDimensions(
                Texture,
                MipWidth,
                MipHeight,
                AlignedWidth,
                AlignedHeight,
                PackedWidth,
                PackedHeight,
                AlignedPadding)) {

            return false;
        }

        if (PackedWidth > MaxTextureDimension ||
            PackedHeight > MaxTextureDimension) {

            return false;
        }

        uint32_t X;
        uint32_t Y;
        size_t SkylineIndex;

        return FindPosition(
            PackedWidth,
            PackedHeight,
            X,
            Y,
            SkylineIndex);
    }

    // ------------------------------------------------------------------------
    // Find the best position for a rectangle using the bottom-left heuristic.
    //
    // The skyline is kept ordered by X.
    // ------------------------------------------------------------------------
    inline bool FindPosition(
        uint32_t Width,
        uint32_t Height,
        uint32_t &OutX,
        uint32_t &OutY,
        size_t &OutSkylineIndex) const {

        uint32_t BestY = std::numeric_limits<uint32_t>::max();
        uint32_t BestX = std::numeric_limits<uint32_t>::max();
        size_t BestIndex = std::numeric_limits<size_t>::max();

        const size_t NodeCount = Skyline.size();

        for (size_t i = 0; i < NodeCount; ++i) {
            const auto &StartNode = Skyline[i];

            const uint32_t X = StartNode.x;

            // Fast horizontal rejection.
            if (Width > MaxTextureDimension - X) {
                continue;
            }

            uint32_t Y = StartNode.y;
            uint32_t WidthRemaining = Width;

            size_t NodeIndex = i;

            while (WidthRemaining > 0) {
                const auto &Node = Skyline[NodeIndex];

                Y = std::max(Y, Node.y);

                // Fast vertical rejection.
                if (Height > MaxTextureDimension - Y) {
                    break;
                }

                if (Node.width >= WidthRemaining) {
                    WidthRemaining = 0;
                    break;
                }

                WidthRemaining -= Node.width;

                ++NodeIndex;

                if (NodeIndex >= NodeCount) {
                    break;
                }
            }

            if (WidthRemaining != 0) {
                continue;
            }

            // Bottom-left heuristic:
            // lowest Y first, then lowest X.
            if (Y < BestY ||
                (Y == BestY && X < BestX)) {

                BestY = Y;
                BestX = X;
                BestIndex = i;
            }
        }

        if (BestIndex == std::numeric_limits<size_t>::max()) {
            return false;
        }

        OutX = BestX;
        OutY = BestY;
        OutSkylineIndex = BestIndex;

        return true;
    }

    inline void InsertSkylineLevel(
        size_t Index,
        uint32_t X,
        uint32_t Y,
        uint32_t Width,
        uint32_t Height) {

        SkylineNode NewNode{
            X,
            Y + Height,
            Width};

        Skyline.insert(
            Skyline.begin() + Index,
            NewNode);

        // --------------------------------------------------------------------
        // Remove/shrink nodes covered by the new rectangle.
        // --------------------------------------------------------------------
        for (size_t i = Index + 1;
             i < Skyline.size();) {

            SkylineNode &Current =
                Skyline[i];

            SkylineNode &Previous =
                Skyline[i - 1];

            const uint32_t PreviousEnd =
                Previous.x + Previous.width;

            // The remaining nodes are completely to the right.
            if (Current.x >= PreviousEnd) {
                break;
            }

            const uint32_t Shrink =
                PreviousEnd - Current.x;

            // Completely covered.
            if (Shrink >= Current.width) {
                Skyline.erase(
                    Skyline.begin() + i);

                continue;
            }

            // Partially covered.
            Current.x += Shrink;
            Current.width -= Shrink;

            break;
        }
    }

    inline void MergeSkyline() {
        for (size_t i = 0;
             i + 1 < Skyline.size();) {

            SkylineNode &Current =
                Skyline[i];

            const SkylineNode &Next =
                Skyline[i + 1];

            if (Current.y == Next.y) {
                Current.width += Next.width;

                Skyline.erase(
                    Skyline.begin() + i + 1);

                continue;
            }

            ++i;
        }
    }

    inline bool RegisterTexture(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *Texture,
        std::vector<float> &LookUpTextureData,
        uint32_t TextureID) {

        if (Texture == nullptr) {
            std::cout
                << "Texture is nullptr"
                << std::endl;

            return false;
        }

        // --------------------------------------------------------------------
        // Do not allocate the same texture twice in the same atlas build.
        //
        // This protects the skyline from duplicate registration if the
        // rendering/buffer logic ever submits the same texture more than once.
        // --------------------------------------------------------------------
        const auto ExistingAllocation =
            CurrentAllocations.find(Texture->ID);

        if (ExistingAllocation != CurrentAllocations.end()) {

            const AtlasAllocation &Allocation =
                ExistingAllocation->second;

            const size_t Offset =
                (static_cast<size_t>(TextureID) *
                     PMMA::Constants::MAX_TEXTURE_MIPS +
                 static_cast<size_t>(MipLevel)) *
                4;

            if (LookUpTextureData.size() < Offset + 4) {
                LookUpTextureData.resize(
                    Offset + 4,
                    0.0f);
            }

            const auto &Mip =
                Texture->MipChain[MipLevel];

            LookUpTextureData[Offset + 0] =
                static_cast<float>(Allocation.X);

            LookUpTextureData[Offset + 1] =
                static_cast<float>(Allocation.Y);

            LookUpTextureData[Offset + 2] =
                static_cast<float>(Mip.Size[0]);

            LookUpTextureData[Offset + 3] =
                static_cast<float>(Mip.Size[1]);

            PendingTextures.push_back(Texture);

            ++Texture->References;

            return true;
        }

        // --------------------------------------------------------------------
        // Calculate the exact dimensions used by the skyline.
        // --------------------------------------------------------------------
        uint32_t MipWidth;
        uint32_t MipHeight;
        uint32_t AlignedWidth;
        uint32_t AlignedHeight;
        uint32_t PackedWidth;
        uint32_t PackedHeight;
        uint32_t AlignedPadding;

        if (!GetPackedDimensions(
                Texture,
                MipWidth,
                MipHeight,
                AlignedWidth,
                AlignedHeight,
                PackedWidth,
                PackedHeight,
                AlignedPadding)) {

            if (Texture->MipChain.empty()) {
                std::cout
                    << "Texture has no mip data"
                    << std::endl;
            } else if (MipLevel >= Texture->MipChain.size()) {
                std::cout
                    << "Texture has not got this mip lvl"
                    << std::endl;
            }

            return false;
        }

        // --------------------------------------------------------------------
        // The rectangle itself cannot fit.
        // --------------------------------------------------------------------
        if (PackedWidth > MaxTextureDimension ||
            PackedHeight > MaxTextureDimension) {

            std::cerr
                << "Texture "
                << Texture->ID
                << " is too large for the atlas. Required "
                << PackedWidth
                << "x"
                << PackedHeight
                << ", atlas is "
                << MaxTextureDimension
                << "x"
                << MaxTextureDimension
                << "."
                << std::endl;

            return false;
        }

        // --------------------------------------------------------------------
        // Find the exact position.
        // --------------------------------------------------------------------
        uint32_t X;
        uint32_t Y;
        size_t SkylineIndex;

        if (!FindPosition(
                PackedWidth,
                PackedHeight,
                X,
                Y,
                SkylineIndex)) {

            std::cout
                << "Atlas full"
                << std::endl;

            return false;
        }

        // --------------------------------------------------------------------
        // All skyline coordinates should remain BC7 aligned.
        // --------------------------------------------------------------------
        if ((X & (BC7_ALIGNMENT - 1)) != 0 ||
            (Y & (BC7_ALIGNMENT - 1)) != 0) {

            std::cerr
                << "Internal error: skyline returned "
                << "unaligned BC7 position "
                << X
                << ", "
                << Y
                << std::endl;

            return false;
        }

        // --------------------------------------------------------------------
        // Reserve the complete padded rectangle.
        // --------------------------------------------------------------------
        InsertSkylineLevel(
            SkylineIndex,
            X,
            Y,
            PackedWidth,
            PackedHeight);

        MergeSkyline();

        // --------------------------------------------------------------------
        // Actual texture coordinates exclude padding.
        // --------------------------------------------------------------------
        const uint32_t TextureX =
            X + AlignedPadding;

        const uint32_t TextureY =
            Y + AlignedPadding;

        // --------------------------------------------------------------------
        // The texture was not present in the previous atlas.
        // --------------------------------------------------------------------
        if (!PreviousAllocations.contains(Texture->ID)) {
            Dirty = true;
        }

        CurrentAllocations.emplace(
            Texture->ID,
            AtlasAllocation{
                TextureX,
                TextureY,
                AlignedWidth,
                AlignedHeight});

        ++Texture->References;

        // --------------------------------------------------------------------
        // Update lookup texture.
        // --------------------------------------------------------------------
        const size_t Offset =
            (static_cast<size_t>(TextureID) *
                 PMMA::Constants::MAX_TEXTURE_MIPS +
             static_cast<size_t>(MipLevel)) *
            4;

        if (LookUpTextureData.size() < Offset + 4) {
            LookUpTextureData.resize(
                Offset + 4,
                0.0f);
        }

        LookUpTextureData[Offset + 0] =
            static_cast<float>(TextureX);

        LookUpTextureData[Offset + 1] =
            static_cast<float>(TextureY);

        LookUpTextureData[Offset + 2] =
            static_cast<float>(MipWidth);

        LookUpTextureData[Offset + 3] =
            static_cast<float>(MipHeight);

        PendingTextures.push_back(Texture);

        return true;
    }

    void Assemble();
};

} // namespace PMMA::Internal::Rendering::Core2D