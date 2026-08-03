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
    uint32_t Padding;

    uint32_t X;
    uint32_t Y;

    uint32_t Width;
    uint32_t Height;

    uint32_t ContentX;
    uint32_t ContentY;

    uint32_t ContentWidth;
    uint32_t ContentHeight;
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

    uint32_t CalculatePadding(
        uint32_t Width,
        uint32_t Height) {
        uint32_t Size =
            std::max(
                Width,
                Height);

        uint32_t Levels = 0;

        while (Size > 1 && Levels < MaxMipLevels) {
            Size >>= 1;
            Levels++;
        }

        return 1u << Levels;
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

    // This function takes a TextureProperty struct instance by ref and adds it as a registered texture to this atlas.
    // This function should identify where in the texture atlas the texture shall be placed using properties from TextureProperty.
    // This data must be written to RegisteredTextures[Texture->ID]->RegisteredRenderPipelineInstances[RenderPipelineInstanceID] as (x, y).
    // Textures must be padded with consideration for the following MipMap generation:
    /*
    Mip LevelScaleRequired Padding Left to Avoid BleedingMip 0 (Base)100%1 pixel (Minimum required for bilinear filtering)Mip 150%2 pixelsMip 225%4 pixelsMip 312.5%8 pixelsMip 46.25%16 pixels
    */
    // Note, if an item is untextured, it's texture position and size is (1, 1) by default, so that position in the texture must be solid white.
    void RegisterTexture(PMMA::Internal::TextureProperty *Texture) {
        if (Skyline.empty()) {
            Skyline.push_back({0,
                               0,
                               MaxTextureDimension});
        }

        if (Texture == nullptr) {
            return;
        }

        if (RegisteredTextures.find(Texture->ID) != RegisteredTextures.end()) {
            return;
        }

        uint32_t Padding =
            CalculatePadding(
                Texture->TextureSize[0],
                Texture->TextureSize[1]);

        uint32_t PackedWidth =
            Texture->TextureSize[0] + Padding * 2;

        uint32_t PackedHeight =
            Texture->TextureSize[1] + Padding * 2;

        uint32_t X;
        uint32_t Y;
        size_t SkylineIndex;

        //
        // Attempt to allocate space.
        //
        if (!FindPosition(
                PackedWidth,
                PackedHeight,
                X,
                Y,
                SkylineIndex)) {
            // Atlas full.
            // Later this can trigger atlas growth.
            std::cout << "Atlas full" << std::endl;
            return;
        }

        //
        // Reserve space immediately.
        //
        InsertSkylineLevel(
            SkylineIndex,
            X,
            Y,
            PackedWidth,
            PackedHeight);

        MergeSkyline();

        Allocations[Texture->ID] =
            {
                Padding,

                X,
                Y,

                PackedWidth,
                PackedHeight,

                X + Padding,
                Y + Padding,

                Texture->TextureSize[0],
                Texture->TextureSize[1]};

        //
        // Register texture.
        //
        RegisteredTextures.emplace(
            Texture->ID,
            Texture);

        ++Texture->References;

        //
        // Store actual usable texture location.
        //
        auto &Location =
            Texture->RegisteredRenderPipelineInstances
                [RenderPipelineInstanceID];

        Location[0] =
            static_cast<uint16_t>(X + Padding);

        Location[1] =
            static_cast<uint16_t>(Y + Padding);

        PendingTextures.push_back(Texture);
        Dirty = true;
    }

    std::vector<uint8_t> GenerateMipChain(
        const std::vector<uint8_t> &basePixels,
        uint32_t width,
        uint32_t height,
        uint32_t channels) {
        std::vector<uint8_t> result;

        // Reserve approximately enough space for the full mip chain.
        result.reserve(basePixels.size() * 4 / 3);

        std::vector<uint8_t> current = basePixels;

        uint32_t currentWidth = width;
        uint32_t currentHeight = height;

        //
        // Mip 0
        //
        result.insert(
            result.end(),
            current.begin(),
            current.end());

        //
        // Generate remaining mip levels.
        //
        while (currentWidth > 1 || currentHeight > 1) {
            uint32_t nextWidth =
                std::max(1u, currentWidth / 2);

            uint32_t nextHeight =
                std::max(1u, currentHeight / 2);

            std::vector<uint8_t> next(
                nextWidth *
                nextHeight *
                channels);

            for (uint32_t y = 0; y < nextHeight; ++y) {
                for (uint32_t x = 0; x < nextWidth; ++x) {
                    uint32_t sx = x * 2;
                    uint32_t sy = y * 2;

                    if (channels == 4) {
                        //
                        // Premultiplied alpha filtering.
                        //
                        float r = 0.0f;
                        float g = 0.0f;
                        float b = 0.0f;
                        float a = 0.0f;

                        for (uint32_t oy = 0; oy < 2; ++oy) {
                            for (uint32_t ox = 0; ox < 2; ++ox) {
                                uint32_t px =
                                    std::min(
                                        sx + ox,
                                        currentWidth - 1);

                                uint32_t py =
                                    std::min(
                                        sy + oy,
                                        currentHeight - 1);

                                size_t index =
                                    (py * currentWidth + px) *
                                    channels;

                                float alpha =
                                    current[index + 3] /
                                    255.0f;

                                r += current[index + 0] * alpha;
                                g += current[index + 1] * alpha;
                                b += current[index + 2] * alpha;
                                a += alpha;
                            }
                        }

                        r *= 0.25f;
                        g *= 0.25f;
                        b *= 0.25f;
                        a *= 0.25f;

                        size_t dst =
                            (y * nextWidth + x) *
                            channels;

                        if (a > 0.00001f) {
                            next[dst + 0] =
                                static_cast<uint8_t>(
                                    std::clamp(
                                        r / a,
                                        0.0f,
                                        255.0f));

                            next[dst + 1] =
                                static_cast<uint8_t>(
                                    std::clamp(
                                        g / a,
                                        0.0f,
                                        255.0f));

                            next[dst + 2] =
                                static_cast<uint8_t>(
                                    std::clamp(
                                        b / a,
                                        0.0f,
                                        255.0f));
                        } else {
                            next[dst + 0] = 0;
                            next[dst + 1] = 0;
                            next[dst + 2] = 0;
                        }

                        next[dst + 3] =
                            static_cast<uint8_t>(
                                std::clamp(
                                    a * 255.0f,
                                    0.0f,
                                    255.0f));
                    } else {
                        //
                        // RGB filtering.
                        //
                        for (uint32_t c = 0; c < channels; ++c) {
                            uint32_t sum = 0;

                            for (uint32_t oy = 0; oy < 2; ++oy) {
                                for (uint32_t ox = 0; ox < 2; ++ox) {
                                    uint32_t px =
                                        std::min(
                                            sx + ox,
                                            currentWidth - 1);

                                    uint32_t py =
                                        std::min(
                                            sy + oy,
                                            currentHeight - 1);

                                    sum +=
                                        current[(py * currentWidth + px) *
                                                    channels +
                                                c];
                                }
                            }

                            next[(y * nextWidth + x) *
                                     channels +
                                 c] =
                                static_cast<uint8_t>(
                                    sum / 4);
                        }
                    }
                }
            }

            //
            // Append this mip directly to BGFX data.
            //
            result.insert(
                result.end(),
                next.begin(),
                next.end());

            current =
                std::move(next);

            currentWidth =
                nextWidth;

            currentHeight =
                nextHeight;
        }

        return result;
    }

    void ExtrudeTextureEdges(
        int32_t X,
        int32_t Y,
        int32_t Width,
        int32_t Height,
        int32_t Padding,
        int32_t Channels) {
        int32_t AtlasWidth = m_TextureWidth;

        auto CopyPixel =
            [&](int32_t dstX,
                int32_t dstY,
                int32_t srcX,
                int32_t srcY) {
                if (dstX < 0 ||
                    dstY < 0 ||
                    srcX < 0 ||
                    srcY < 0)
                    return;

                if (dstX >= (int32_t)m_TextureWidth ||
                    dstY >= (int32_t)m_TextureHeight)
                    return;

                if (srcX >= (int32_t)m_TextureWidth ||
                    srcY >= (int32_t)m_TextureHeight)
                    return;

                memcpy(
                    &AtlasPixels[((uint32_t)dstY * AtlasWidth +
                                  (uint32_t)dstX) *
                                 Channels],

                    &AtlasPixels[((uint32_t)srcY * AtlasWidth +
                                  (uint32_t)srcX) *
                                 Channels],

                    Channels);
            };

        //
        // Left/right borders
        //
        for (uint32_t y = 0; y < Height; y++) {
            for (uint32_t p = 1; p <= Padding; p++) {
                CopyPixel(
                    X - p,
                    Y + y,
                    X,
                    Y + y);

                CopyPixel(
                    X + Width - 1 + p,
                    Y + y,
                    X + Width - 1,
                    Y + y);
            }
        }

        //
        // Top/bottom borders
        //
        for (uint32_t x = 0; x < Width; x++) {
            for (uint32_t p = 1; p <= Padding; p++) {
                CopyPixel(
                    X + x,
                    Y - p,
                    X + x,
                    Y);

                CopyPixel(
                    X + x,
                    Y + Height - 1 + p,
                    X + x,
                    Y + Height - 1);
            }
        }

        //
        // Corners
        //
        for (uint32_t x = 1; x <= Padding; x++) {
            for (uint32_t y = 1; y <= Padding; y++) {
                CopyPixel(
                    X - x,
                    Y - y,
                    X,
                    Y);

                CopyPixel(
                    X + Width - 1 + x,
                    Y - y,
                    X + Width - 1,
                    Y);

                CopyPixel(
                    X - x,
                    Y + Height - 1 + y,
                    X,
                    Y + Height - 1);

                CopyPixel(
                    X + Width - 1 + x,
                    Y + Height - 1 + y,
                    X + Width - 1,
                    Y + Height - 1);
            }
        }
    }

    // Here, if the texture atlas is dirty, the texture atlas should be generated using the properties from 'RegisteredTextures' and written to a BGFX texture.
    void Assemble() {
        char Channels = 3;
        if (Transparent) {
            Channels++;
        }

        //
        // Find required atlas dimensions.
        //
        m_TextureWidth = 1;
        m_TextureHeight = 1;

        for (auto &[ID, Allocation] : Allocations) {
            m_TextureWidth =
                std::max(
                    m_TextureWidth,
                    Allocation.X + Allocation.Width);

            m_TextureHeight =
                std::max(
                    m_TextureHeight,
                    Allocation.Y + Allocation.Height);
        }

        //
        // Round atlas dimensions up to power-of-two.
        //
        auto NextPowerOfTwo =
            [](uint32_t Value) {
                uint32_t Result = 1;

                while (Result < Value)
                    Result <<= 1;

                return Result;
            };

        m_TextureWidth =
            NextPowerOfTwo(m_TextureWidth);

        m_TextureHeight =
            NextPowerOfTwo(m_TextureHeight);

        size_t RequiredSize =
            m_TextureWidth *
            m_TextureHeight *
            Channels;

        AtlasPixels.assign(
            RequiredSize,
            0);

        //
        // Copy textures into their assigned regions.
        //
        for (auto *Texture : PendingTextures) {
            auto Allocation =
                Allocations[Texture->ID];

            uint32_t DestX =
                Allocation.ContentX;

            uint32_t DestY =
                Allocation.ContentY;

            uint32_t SrcChannels =
                Texture->Channels;

            for (uint32_t Y = 0;
                 Y < Texture->TextureSize[1];
                 ++Y) {
                for (uint32_t X = 0;
                     X < Texture->TextureSize[0];
                     ++X) {
                    size_t SourceIndex =
                        (Y * Texture->TextureSize[0] + X) *
                        SrcChannels;

                    size_t DestinationIndex =
                        ((DestY + Y) * m_TextureWidth +
                         (DestX + X)) *
                        Channels;

                    AtlasPixels[DestinationIndex + 0] =
                        Texture->PixelData[SourceIndex + 0];

                    AtlasPixels[DestinationIndex + 1] =
                        SrcChannels > 1
                            ? Texture->PixelData[SourceIndex + 1]
                            : 255;

                    AtlasPixels[DestinationIndex + 2] =
                        SrcChannels > 2
                            ? Texture->PixelData[SourceIndex + 2]
                            : 255;

                    if (Channels == 4) {
                        AtlasPixels[DestinationIndex + 3] =
                            SrcChannels > 3
                                ? Texture->PixelData[SourceIndex + 3]
                                : 255;
                    }
                }
            }

            ExtrudeTextureEdges(
                Allocation.ContentX,
                Allocation.ContentY,
                Allocation.ContentWidth,
                Allocation.ContentHeight,
                Allocation.Padding,
                Channels);
        }

        //
        // Replace BGFX texture.
        //
        if (bgfx::isValid(TextureHandle)) {
            bgfx::destroy(TextureHandle);
        }

        std::vector<uint8_t> MipPixels =
            GenerateMipChain(
                AtlasPixels,
                m_TextureWidth,
                m_TextureHeight,
                Channels);

        TextureHandle =
            bgfx::createTexture2D(
                (uint16_t)m_TextureWidth,
                (uint16_t)m_TextureHeight,
                true, // Has mip chain
                1,
                Transparent
                    ? bgfx::TextureFormat::RGBA8
                    : bgfx::TextureFormat::RGB8,
                BGFX_TEXTURE_NONE,
                bgfx::copy(
                    MipPixels.data(),
                    (uint32_t)MipPixels.size()));

        PendingTextures.clear();
        Dirty = false;
    }
};
} // namespace PMMA::Internal::Rendering::Core2D