#pragma once

#include <map>
#include <string>

#include "Internal/Internal.hpp"

namespace PMMA::Internal::Rendering::Core2D {
struct SkylineNode {
    uint32_t x;
    uint32_t y;
    uint32_t width;
};

struct AtlasAllocation {
    uint32_t X;
    uint32_t Y;

    uint32_t Width;
    uint32_t Height;
};

class CompressedTextureInstance { // makes texture atlas for a RenderPipelineInstance
public:
    std::map<uintptr_t, PMMA::Internal::TextureProperty *> RegisteredTextures;

private:
    std::vector<PMMA::Internal::TextureProperty *> PendingTextures;

    std::vector<SkylineNode> Skyline;

public:
    std::map<uintptr_t, AtlasAllocation> Allocations;

    std::vector<unsigned char> AtlasPixels;

    uint32_t AtlasPadding = 0;
    uint32_t MipLevel = 0;

public:
    bool Dirty = false;

    bgfx::TextureHandle TextureHandle = BGFX_INVALID_HANDLE;

    uint32_t m_TextureWidth = 0;
    uint32_t m_TextureHeight = 0;
    uint32_t MaxTextureDimension = 1024;
    uintptr_t RenderPipelineInstanceID;

    static constexpr uint32_t BC7_ALIGNMENT = 4;

    static constexpr uint32_t AlignUp4(uint32_t value) {
        return (value + (BC7_ALIGNMENT - 1)) &
               ~(BC7_ALIGNMENT - 1);
    }

    static constexpr uint32_t AlignDown4(uint32_t value) {
        return value & ~(BC7_ALIGNMENT - 1);
    }

    CompressedTextureInstance(uintptr_t NewRenderPipelineInstanceID, uint32_t NewMaxTextureDimension, uint32_t NewMipLevel) {
        RenderPipelineInstanceID = NewRenderPipelineInstanceID;
        MaxTextureDimension = NewMaxTextureDimension;
        MipLevel = NewMipLevel;

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
        RegisteredTextures.clear();
        PendingTextures.clear();
        Allocations.clear();

        Skyline.clear();
        Skyline.push_back({0,
                           0,
                           MaxTextureDimension});

        AtlasPixels.clear();

        Dirty = false;

        m_TextureWidth = 0;
        m_TextureHeight = 0;

        if (bgfx::isValid(TextureHandle)) {
            bgfx::destroy(TextureHandle);
            TextureHandle = BGFX_INVALID_HANDLE;
        }
    }

    inline bool CanFitTexture(
        PMMA::Internal::TextureProperty *Texture,
        uint32_t Width,
        uint32_t Height) {

        if (RegisteredTextures.contains(Texture->ID)) {
            return true;
        }
        uint32_t X;
        uint32_t Y;
        size_t Index;

        return FindPosition(
            Width + AtlasPadding * 2,
            Height + AtlasPadding * 2,
            X,
            Y,
            Index);
    }

    inline bool FindPosition(
        uint32_t Width,
        uint32_t Height,
        uint32_t &OutX,
        uint32_t &OutY,
        size_t &OutSkylineIndex) {
        uint32_t BestY = UINT32_MAX;
        uint32_t BestX = UINT32_MAX;
        size_t BestIndex = SIZE_MAX;

        for (size_t i = 0; i < Skyline.size(); ++i) {
            uint32_t CandidateY;

            //
            // Check if the rectangle fits starting
            // at this skyline node.
            //
            uint32_t x = Skyline[i].x;

            if (x + Width > MaxTextureDimension)
                continue;

            uint32_t WidthRemaining = Width;
            uint32_t y = Skyline[i].y;

            size_t NodeIndex = i;

            while (WidthRemaining > 0) {
                //
                // The rectangle must sit above the
                // tallest skyline section it overlaps.
                //
                y = std::max(
                    y,
                    Skyline[NodeIndex].y);

                //
                // Would this exceed atlas height?
                //
                if (y + Height > MaxTextureDimension) {
                    break;
                }

                if (Skyline[NodeIndex].width >= WidthRemaining) {
                    WidthRemaining = 0;
                } else {
                    WidthRemaining -= Skyline[NodeIndex].width;
                }

                ++NodeIndex;

                //
                // Ran out of skyline before fitting.
                //
                if (NodeIndex >= Skyline.size() && WidthRemaining > 0) {
                    break;
                }
            }

            //
            // Failed to fit.
            //
            if (WidthRemaining > 0)
                continue;

            CandidateY = y;

            //
            // Bottom-left heuristic:
            // lower Y wins, then lower X.
            //
            if (CandidateY < BestY ||
                (CandidateY == BestY &&
                 x < BestX)) {
                BestY = CandidateY;
                BestX = x;
                BestIndex = i;
            }
        }

        if (BestIndex == SIZE_MAX) {
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

        //
        // Insert the new skyline segment.
        //
        Skyline.insert(
            Skyline.begin() + Index,
            NewNode);

        //
        // Remove or shrink skyline nodes that
        // are now covered by this rectangle.
        //
        for (size_t i = Index + 1;
             i < Skyline.size();) {
            SkylineNode &Current = Skyline[i];
            SkylineNode &Previous = Skyline[i - 1];

            uint32_t PreviousEnd =
                Previous.x + Previous.width;

            //
            // This node is completely outside the
            // inserted rectangle.
            //
            if (Current.x >= PreviousEnd) {
                break;
            }

            uint32_t Shrink =
                PreviousEnd - Current.x;

            //
            // The new rectangle completely covers
            // this skyline node.
            //
            if (Shrink >= Current.width) {
                Skyline.erase(
                    Skyline.begin() + i);

                continue;
            }

            //
            // The new rectangle partially overlaps
            // this node.
            //
            Current.x += Shrink;
            Current.width -= Shrink;

            break;
        }
    }

    inline void MergeSkyline() {
        if (Skyline.size() < 2)
            return;

        for (size_t i = 0; i < Skyline.size() - 1;) {
            SkylineNode &Current = Skyline[i];
            SkylineNode &Next = Skyline[i + 1];

            //
            // Adjacent nodes at the same height
            // can be represented as one node.
            //
            if (Current.y == Next.y) {
                Current.width += Next.width;

                Skyline.erase(
                    Skyline.begin() + i + 1);

                //
                // Do not increment i here.
                // The newly expanded node may also
                // merge with the following node.
                //
                continue;
            }

            ++i;
        }
    }

    inline bool RegisterTexture(
        PMMA::Internal::TextureProperty *Texture,
        std::vector<float> &LookUpTextureData,
        uint32_t TextureID) {
        if (Texture == nullptr) {
            std::cout << "Texture is nullptr" << std::endl;
            return false;
        }

        if (RegisteredTextures.contains(Texture->ID)) {
            std::cout << "Texture already registered" << std::endl;
            return false;
        }

        if (Texture->MipChain.empty()) {
            std::cout << "Texture has no mip data" << std::endl;
            return false;
        }

        if (MipLevel >= Texture->MipChain.size()) {
            std::cout << "Texture has not got this mip lvl" << std::endl;
            return false;
        }

        const auto &Mip =
            Texture->MipChain[MipLevel];

        // ========================================================================
        // BC7 operates on 4x4 blocks.
        //
        // Round the actual mip dimensions UP to complete BC7 blocks.
        // ========================================================================

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

        // ========================================================================
        // Padding must also be BC7 aligned.
        //
        // Otherwise:
        //
        //     X + AtlasPadding
        //
        // could become something like:
        //
        //     128 + 2 = 130
        //
        // which is invalid for BC7.
        // ========================================================================

        const uint32_t AlignedPadding =
            AlignUp4(AtlasPadding);

        // ========================================================================
        // Reserve the entire BC7-aligned rectangle.
        //
        // Everything entering the skyline is now a multiple of 4.
        // Since the skyline starts at X=0/Y=0, every resulting skyline
        // coordinate will remain a multiple of 4.
        // ========================================================================

        const uint32_t PackedWidth =
            AlignedWidth +
            AlignedPadding * 2;

        const uint32_t PackedHeight =
            AlignedHeight +
            AlignedPadding * 2;

        // ========================================================================
        // Make sure the texture can theoretically fit in the atlas.
        // ========================================================================

        if (PackedWidth > MaxTextureDimension ||
            PackedHeight > MaxTextureDimension) {

            std::cerr
                << "Texture "
                << Texture->ID
                << " is too large for the atlas. "
                << "Required "
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

        // ========================================================================
        // Find a BC7-aligned position.
        // ========================================================================

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

        // ========================================================================
        // Sanity check.
        //
        // This should ALWAYS succeed now because every skyline dimension and
        // position is a multiple of 4.
        // ========================================================================

        if ((X & 3u) != 0 ||
            (Y & 3u) != 0) {

            std::cerr
                << "Internal error: skyline returned "
                << "unaligned BC7 position "
                << X
                << ", "
                << Y
                << std::endl;

            return false;
        }

        // ========================================================================
        // Insert the complete aligned rectangle into the skyline.
        // ========================================================================

        InsertSkylineLevel(
            SkylineIndex,
            X,
            Y,
            PackedWidth,
            PackedHeight);

        MergeSkyline();

        // ========================================================================
        // The actual texture starts after the aligned padding.
        //
        // IMPORTANT:
        //
        // X + AlignedPadding is still guaranteed to be divisible by 4.
        // ========================================================================

        const uint32_t TextureX =
            X + AlignedPadding;

        const uint32_t TextureY =
            Y + AlignedPadding;

        Allocations[Texture->ID] =
            {
                TextureX,
                TextureY,
                AlignedWidth,
                AlignedHeight};

        RegisteredTextures.emplace(
            Texture->ID,
            Texture);

        ++Texture->References;

        const size_t Offset =
            (static_cast<size_t>(TextureID) *
                 PMMA::Constants::MAX_TEXTURE_MIPS +
             static_cast<size_t>(MipLevel)) *
            4;

        if (LookUpTextureData.size() < Offset + 4) {
            LookUpTextureData.resize(Offset + 4, 0.0f);
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

        Dirty = true;

        return true;
    }

    void Assemble();
};
} // namespace PMMA::Internal::Rendering::Core2D