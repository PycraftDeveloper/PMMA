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
private:
    std::map<uintptr_t, PMMA::Internal::TextureProperty *> RegisteredTextures;
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

    inline void RegisterTexture(
        PMMA::Internal::TextureProperty *Texture) {

        if (Texture == nullptr) {
            return;
        }

        if (RegisteredTextures.contains(Texture->ID)) {
            return;
        }

        if (Texture->MipChain.empty()) {
            return;
        }

        //
        // Treat each mip as an independent texture.
        // This TextureManager only wants the mip selected
        // by MipLevel.
        //
        if (MipLevel >= Texture->MipChain.size()) {
            return;
        }

        const auto &Mip =
            Texture->MipChain[MipLevel];

        uint32_t PackedWidth =
            Mip.Size[0] + AtlasPadding * 2;

        uint32_t PackedHeight =
            Mip.Size[1] + AtlasPadding * 2;

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

            return;
        }

        InsertSkylineLevel(
            SkylineIndex,
            X,
            Y,
            PackedWidth,
            PackedHeight);

        MergeSkyline();

        Allocations[Texture->ID] =
            {
                X + AtlasPadding,
                Y + AtlasPadding,
                Mip.Size[0],
                Mip.Size[1]};

        RegisteredTextures.emplace(
            Texture->ID,
            Texture);

        ++Texture->References;

        if (MipLevel == 0) {
            auto &Location =
                Texture->RegisteredRenderPipelineInstances
                    [RenderPipelineInstanceID];

            Location[0] =
                static_cast<uint16_t>(X);

            Location[1] =
                static_cast<uint16_t>(Y);
        }

        PendingTextures.push_back(Texture);

        Dirty = true;
    }

    void Assemble();
};
} // namespace PMMA::Internal::Rendering::Core2D