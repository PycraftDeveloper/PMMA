#pragma once

#include <map>
#include <string>

#include "Internal/Internal.hpp"

/*
struct TextureProperty {
    uintptr_t ID;
    uint16_t TextureSize[2];
    unsigned char Channels;
    uint32_t References = 0;
    std::vector<unsigned char> PixelData;
    std::map<uintptr_t, uint16_t[2]> RegisteredRenderPipelineInstances;

    TextureProperty() {
        ID = reinterpret_cast<uintptr_t>(this);
    }
};
*/

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

class TextureManager { // makes texture atlas for a RenderPipelineInstance
private:
    std::map<uintptr_t, PMMA::Internal::TextureProperty *> RegisteredTextures;
    std::vector<PMMA::Internal::TextureProperty *> PendingTextures;

    std::vector<SkylineNode> Skyline;
    std::map<uintptr_t, AtlasAllocation> Allocations;

    std::vector<unsigned char> AtlasPixels;

    uint32_t MaxMipLevels = 5;

public:
    bool Dirty = false;

    bgfx::TextureHandle TextureHandle = BGFX_INVALID_HANDLE;

    uint32_t m_TextureWidth = 0;
    uint32_t m_TextureHeight = 0;
    uint32_t MaxTextureDimension = 1024;
    uintptr_t RenderPipelineInstanceID;
    bool Transparent = false;

    ~TextureManager() {
        if (bgfx::isValid(TextureHandle)) {
            bgfx::destroy(TextureHandle);
        }
    }

    bool FindPosition(
        uint32_t Width,
        uint32_t Height,
        uint32_t &OutX,
        uint32_t &OutY,
        size_t &OutSkylineIndex) {

        std::cout
            << "FindPosition "
            << Width << "x" << Height
            << " skyline nodes: "
            << Skyline.size()
            << std::endl;

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

    void InsertSkylineLevel(
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

    void MergeSkyline() {
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

    void RegisterTexture(
        PMMA::Internal::TextureProperty *Texture) {
        if (Skyline.empty()) {
            Skyline.push_back(
                {0,
                 0,
                 MaxTextureDimension});
        }

        if (Texture == nullptr)
            return;

        if (RegisteredTextures.contains(Texture->ID))
            return;

        if (Texture->MipChain.empty())
            return;

        //
        // Mip 0 is the atlas packing size.
        //
        const auto &Mip0 =
            Texture->MipChain[0];

        uint32_t PackedWidth =
            Mip0.Size[0];

        uint32_t PackedHeight =
            Mip0.Size[1];

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
                X,
                Y,
                PackedWidth,
                PackedHeight};

        RegisteredTextures.emplace(
            Texture->ID,
            Texture);

        ++Texture->References;

        auto &Location =
            Texture->RegisteredRenderPipelineInstances
                [RenderPipelineInstanceID];

        Location[0] =
            static_cast<uint16_t>(X);

        Location[1] =
            static_cast<uint16_t>(Y);

        PendingTextures.push_back(Texture);

        Dirty = true;
    }

    void CopyMipIntoAtlas(
        const PMMA::Internal::MipData &mip,
        uint32_t dstX,
        uint32_t dstY,
        uint32_t atlasWidth,
        uint32_t atlasHeight,
        uint32_t srcChannels,
        uint32_t dstChannels,
        std::vector<uint8_t> &atlas) {
        for (uint32_t y = 0;
             y < mip.Size[1];
             y++) {
            for (uint32_t x = 0;
                 x < mip.Size[0];
                 x++) {
                uint32_t sourceIndex =
                    (y * mip.Size[0] + x) *
                    srcChannels;

                uint32_t destX =
                    dstX + x;

                uint32_t destY =
                    dstY + y;

                //
                // Outside atlas.
                //
                if (destX >= atlasWidth ||
                    destY >= atlasHeight) {
                    continue;
                }

                uint32_t destinationIndex =
                    (destY * atlasWidth + destX) *
                    dstChannels;

                //
                // RGB/RGBA conversion.
                //
                atlas[destinationIndex + 0] =
                    mip.PixelData[sourceIndex + 0];

                if (dstChannels > 1) {
                    atlas[destinationIndex + 1] =
                        srcChannels > 1
                            ? mip.PixelData[sourceIndex + 1]
                            : 255;
                }

                if (dstChannels > 2) {
                    atlas[destinationIndex + 2] =
                        srcChannels > 2
                            ? mip.PixelData[sourceIndex + 2]
                            : 255;
                }

                if (dstChannels > 3) {
                    atlas[destinationIndex + 3] =
                        srcChannels > 3
                            ? mip.PixelData[sourceIndex + 3]
                            : 255;
                }
            }
        }
    }

    void Assemble() {
        if (!Dirty)
            return;

        uint32_t channels =
            Transparent ? 4 : 3;

        //
        // Find atlas size from mip 0.
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

        auto NextPowerOfTwo =
            [](uint32_t value) {
                uint32_t result = 1;

                while (result < value)
                    result <<= 1;

                return result;
            };

        m_TextureWidth =
            NextPowerOfTwo(m_TextureWidth);

        m_TextureHeight =
            NextPowerOfTwo(m_TextureHeight);

        //
        // Determine number of mip levels.
        //
        uint32_t mipCount = 1;

        for (auto *texture : PendingTextures) {
            mipCount =
                std::max(
                    mipCount,
                    static_cast<uint32_t>(
                        texture->MipChain.size()));
        }

        std::vector<uint8_t> AtlasMipChain;

        for (uint32_t mipLevel = 0;
             mipLevel < mipCount;
             mipLevel++) {
            uint32_t mipWidth =
                std::max(
                    1u,
                    m_TextureWidth >> mipLevel);

            uint32_t mipHeight =
                std::max(
                    1u,
                    m_TextureHeight >> mipLevel);

            std::vector<uint8_t> mipPixels(
                mipWidth *
                    mipHeight *
                    channels,
                0);

            for (auto *texture : PendingTextures) {
                auto allocation =
                    Allocations[texture->ID];

                if (mipLevel >= texture->MipChain.size())
                    continue;

                const auto &source =
                    texture->MipChain[mipLevel];

                uint32_t x =
                    allocation.X >> mipLevel;

                uint32_t y =
                    allocation.Y >> mipLevel;

                x = std::min(
                    x,
                    mipWidth - source.Size[0]);

                y = std::min(
                    y,
                    mipHeight - source.Size[1]);

                CopyMipIntoAtlas(
                    source,
                    x,
                    y,
                    mipWidth,
                    mipHeight,
                    texture->Channels,
                    channels,
                    mipPixels);
            }

            //
            // Append this mip to BGFX stream
            //
            AtlasMipChain.insert(
                AtlasMipChain.end(),
                mipPixels.begin(),
                mipPixels.end());
        }

        TextureHandle =
            bgfx::createTexture2D(
                (uint16_t)m_TextureWidth,
                (uint16_t)m_TextureHeight,
                true, // has mips
                1,
                Transparent
                    ? bgfx::TextureFormat::RGBA8
                    : bgfx::TextureFormat::RGB8,
                BGFX_TEXTURE_NONE,
                bgfx::copy(
                    AtlasMipChain.data(),
                    (uint32_t)AtlasMipChain.size()));

        PendingTextures.clear();
        Dirty = false;
    }
};
} // namespace PMMA::Internal::Rendering::Core2D