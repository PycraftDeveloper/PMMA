#pragma once

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <vector>

#include <bgfx/bgfx.h>

#include "Constants.hpp"
#include "Internal/Internal.hpp"

namespace PMMA::Internal::Rendering::Core2D {

struct CompressedTexture_BufferData {
    std::vector<uint8_t> Data;
    bool Active = false;
    bool Clear = true;
    int FramesSinceLastActive = 0;
};

class CompressedTextureInstance {
private:
    std::vector<
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *>
        PendingTextures;

    std::vector<
        PMMA::Internal::Rendering::Core2D::SkylineNode>
        Skyline;

    std::vector<
        PMMA::Internal::Rendering::Core2D::SkylineNode>
        PreviousSkyline;

    bool HasAddedTextures = false;
    bool HasRemovedTextures = false;

    inline bool GetPackedDimensions(
        const PMMA::Internal::Rendering::Core2D::CompressedTextureProperty
            *Texture,
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
            static_cast<uint32_t>(
                Mip.Size[0]);

        const uint32_t MipHeight =
            static_cast<uint32_t>(
                Mip.Size[1]);

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
            AlignedWidth +
            AlignedPadding * 2;

        const uint32_t PackedHeight =
            AlignedHeight +
            AlignedPadding * 2;

        OutMipWidth =
            MipWidth;

        OutMipHeight =
            MipHeight;

        OutAlignedWidth =
            AlignedWidth;

        OutAlignedHeight =
            AlignedHeight;

        OutPackedWidth =
            PackedWidth;

        OutPackedHeight =
            PackedHeight;

        OutAlignedPadding =
            AlignedPadding;

        return true;
    }

    inline void RebuildSkylineFromCurrentAllocations() {

        Skyline.clear();

        Skyline.push_back({0,
                           0,
                           MaxTextureDimension});

        if (CurrentAllocations.empty()) {
            return;
        }

        const uint32_t AlignedPadding =
            AlignUp4(AtlasPadding);

        std::vector<uint32_t> XCoordinates;

        XCoordinates.reserve(
            CurrentAllocations.size() * 2 + 2);

        XCoordinates.push_back(0);

        XCoordinates.push_back(
            MaxTextureDimension);

        for (const auto &[TextureID, Allocation] :
             CurrentAllocations) {

            (void)TextureID;

            const uint32_t PackedX =
                Allocation.X -
                AlignedPadding;

            const uint32_t PackedWidth =
                Allocation.Width +
                AlignedPadding * 2;

            const uint32_t PackedEndX =
                PackedX +
                PackedWidth;

            XCoordinates.push_back(
                PackedX);

            XCoordinates.push_back(
                PackedEndX);
        }

        std::sort(
            XCoordinates.begin(),
            XCoordinates.end());

        XCoordinates.erase(
            std::unique(
                XCoordinates.begin(),
                XCoordinates.end()),
            XCoordinates.end());

        std::vector<SkylineNode> RebuiltSkyline;

        RebuiltSkyline.reserve(
            XCoordinates.size());

        for (size_t i = 0;
             i + 1 < XCoordinates.size();
             ++i) {

            const uint32_t X =
                XCoordinates[i];

            const uint32_t NextX =
                XCoordinates[i + 1];

            if (NextX <= X) {
                continue;
            }

            uint32_t Height = 0;

            for (const auto &[TextureID, Allocation] :
                 CurrentAllocations) {

                (void)TextureID;

                const uint32_t PackedX =
                    Allocation.X -
                    AlignedPadding;

                const uint32_t PackedWidth =
                    Allocation.Width +
                    AlignedPadding * 2;

                const uint32_t PackedEndX =
                    PackedX +
                    PackedWidth;

                if (PackedEndX <= X ||
                    PackedX >= NextX) {

                    continue;
                }

                const uint32_t PackedY =
                    Allocation.Y -
                    AlignedPadding;

                const uint32_t PackedHeight =
                    Allocation.Height +
                    AlignedPadding * 2;

                const uint32_t PackedEndY =
                    PackedY +
                    PackedHeight;

                Height =
                    std::max(
                        Height,
                        PackedEndY);
            }

            Height =
                std::min(
                    Height,
                    MaxTextureDimension);

            RebuiltSkyline.push_back({X,
                                      Height,
                                      NextX - X});
        }

        for (size_t i = 0;
             i + 1 < RebuiltSkyline.size();) {

            SkylineNode &Current =
                RebuiltSkyline[i];

            const SkylineNode &Next =
                RebuiltSkyline[i + 1];

            if (Current.y ==
                    Next.y &&
                Current.x +
                        Current.width ==
                    Next.x) {

                Current.width +=
                    Next.width;

                RebuiltSkyline.erase(
                    RebuiltSkyline.begin() +
                    i + 1);

                continue;
            }

            ++i;
        }

        if (RebuiltSkyline.empty()) {

            RebuiltSkyline.push_back({0,
                                      0,
                                      MaxTextureDimension});

        } else {

            const SkylineNode &Last =
                RebuiltSkyline.back();

            const uint32_t End =
                Last.x +
                Last.width;

            if (End < MaxTextureDimension) {

                RebuiltSkyline.push_back({End,
                                          0,
                                          MaxTextureDimension - End});

            } else if (End > MaxTextureDimension) {

                std::cerr
                    << "Internal error: rebuilt skyline "
                    << "extends beyond atlas width."
                    << std::endl;
            }
        }

        Skyline =
            std::move(
                RebuiltSkyline);
    }

    inline void UpdateLookupTexture(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty
            *Texture,
        std::vector<float> &LookUpTextureData,
        uint32_t TextureID,
        const AtlasAllocation &Allocation) {

        if (Texture == nullptr ||
            MipLevel >= Texture->MipChain.size()) {

            return;
        }

        const size_t Offset =
            (static_cast<size_t>(TextureID) *
                 PMMA::Constants::MAX_TEXTURE_MIPS +
             static_cast<size_t>(MipLevel)) *
            4;

        if (LookUpTextureData.size() <
            Offset + 4) {

            LookUpTextureData.resize(
                Offset + 4,
                0.0f);
        }

        const auto &Mip =
            Texture->MipChain[MipLevel];

        LookUpTextureData[Offset + 0] =
            static_cast<float>(
                Allocation.X);

        LookUpTextureData[Offset + 1] =
            static_cast<float>(
                Allocation.Y);

        LookUpTextureData[Offset + 2] =
            static_cast<float>(
                Mip.Size[0]);

        LookUpTextureData[Offset + 3] =
            static_cast<float>(
                Mip.Size[1]);
    }

public:
    std::unordered_map<
        uintptr_t,
        AtlasAllocation>
        PreviousAllocations;

    std::unordered_map<
        uintptr_t,
        AtlasAllocation>
        CurrentAllocations;

    std::array<
        CompressedTexture_BufferData,
        4>
        AtlasPixels;

    uint32_t AtlasPadding = 0;

    uint32_t MipLevel = 0;

    uint32_t FramesSinceLastChange = 0;

public:
    bool Dirty = false;

    char BufferID = 0;

    char PreviousBufferID = 0;

    bgfx::TextureHandle TextureHandle =
        BGFX_INVALID_HANDLE;

    uint32_t m_TextureWidth = 0;

    uint32_t m_TextureHeight = 0;

    uint32_t MaxTextureDimension = 1024;

    uintptr_t RenderPipelineInstanceID = 0;

    static constexpr uint32_t BC7_ALIGNMENT = 4;

    static constexpr uint32_t AlignUp4(
        uint32_t value) noexcept {

        return (
                   value +
                   (BC7_ALIGNMENT - 1)) &
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
          MaxTextureDimension(
              NewMaxTextureDimension),
          RenderPipelineInstanceID(
              NewRenderPipelineInstanceID) {

        Skyline.reserve(64);

        PreviousSkyline.reserve(64);

        Skyline.push_back({0,
                           0,
                           MaxTextureDimension});
    }

    ~CompressedTextureInstance() {

        if (bgfx::isValid(TextureHandle)) {

            bgfx::destroy(
                TextureHandle);

            TextureHandle =
                BGFX_INVALID_HANDLE;
        }
    }

    inline void Reset() {

        PreviousAllocations =
            std::move(
                CurrentAllocations);

        CurrentAllocations.clear();

        PreviousSkyline =
            std::move(
                Skyline);

        Skyline =
            PreviousSkyline;

        if (Skyline.empty()) {

            Skyline.push_back({0,
                               0,
                               MaxTextureDimension});
        }

        HasAddedTextures =
            false;

        HasRemovedTextures =
            false;

        Dirty =
            false;

        PendingTextures.clear();

        if (FramesSinceLastChange >=
            PMMA::Constants::MAX_FRAMES_BETWEEN_STALE_BUFFER_CLEANUP) {

            for (auto &Buffer :
                 AtlasPixels) {

                if (!Buffer.Active &&
                    !Buffer.Clear) {

                    Buffer.Data.clear();
                    Buffer.Data.shrink_to_fit();
                    Buffer.Clear = true;
                    Buffer.FramesSinceLastActive = 0;
                }
            }
        } else {
            FramesSinceLastChange++;
        }
    }

    inline bool CanFitTexture(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty
            *Texture) {

        if (Texture == nullptr) {
            return false;
        }

        if (CurrentAllocations.contains(
                Texture->ID)) {

            return true;
        }

        const auto PreviousAllocation =
            PreviousAllocations.find(
                Texture->ID);

        if (PreviousAllocation !=
            PreviousAllocations.end()) {

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

            (void)MipWidth;
            (void)MipHeight;
            (void)PackedWidth;
            (void)PackedHeight;
            (void)AlignedPadding;

            const AtlasAllocation
                &Allocation =
                    PreviousAllocation->second;

            return Allocation.Width ==
                       AlignedWidth &&
                   Allocation.Height ==
                       AlignedHeight;
        }

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

        (void)MipWidth;
        (void)MipHeight;
        (void)AlignedWidth;
        (void)AlignedHeight;
        (void)AlignedPadding;

        if (PackedWidth >
                MaxTextureDimension ||
            PackedHeight >
                MaxTextureDimension) {

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

    inline bool FindPosition(
        uint32_t Width,
        uint32_t Height,
        uint32_t &OutX,
        uint32_t &OutY,
        size_t &OutSkylineIndex) const {

        uint32_t BestY =
            std::numeric_limits<uint32_t>::max();

        uint32_t BestX =
            std::numeric_limits<uint32_t>::max();

        size_t BestIndex =
            std::numeric_limits<size_t>::max();

        const size_t NodeCount =
            Skyline.size();

        for (size_t i = 0;
             i < NodeCount;
             ++i) {

            const auto &StartNode =
                Skyline[i];

            const uint32_t X =
                StartNode.x;

            if (X > MaxTextureDimension ||
                Width >
                    MaxTextureDimension - X) {

                continue;
            }

            uint32_t Y =
                StartNode.y;

            uint32_t WidthRemaining =
                Width;

            size_t NodeIndex =
                i;

            while (WidthRemaining > 0) {

                if (NodeIndex >= NodeCount) {
                    break;
                }

                const auto &Node =
                    Skyline[NodeIndex];

                Y =
                    std::max(
                        Y,
                        Node.y);

                if (Y > MaxTextureDimension ||
                    Height >
                        MaxTextureDimension - Y) {

                    break;
                }

                if (Node.width >=
                    WidthRemaining) {

                    WidthRemaining = 0;
                    break;
                }

                WidthRemaining -=
                    Node.width;

                ++NodeIndex;
            }

            if (WidthRemaining != 0) {
                continue;
            }

            if (Y < BestY ||
                (Y == BestY &&
                 X < BestX)) {

                BestY =
                    Y;

                BestX =
                    X;

                BestIndex =
                    i;
            }
        }

        if (BestIndex ==
            std::numeric_limits<size_t>::max()) {

            return false;
        }

        OutX =
            BestX;

        OutY =
            BestY;

        OutSkylineIndex =
            BestIndex;

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

        for (size_t i = Index + 1;
             i < Skyline.size();) {

            SkylineNode &Current =
                Skyline[i];

            SkylineNode &Previous =
                Skyline[i - 1];

            const uint32_t PreviousEnd =
                Previous.x +
                Previous.width;

            if (Current.x >=
                PreviousEnd) {

                break;
            }

            const uint32_t Shrink =
                PreviousEnd -
                Current.x;

            if (Shrink >=
                Current.width) {

                Skyline.erase(
                    Skyline.begin() + i);

                continue;
            }

            Current.x +=
                Shrink;

            Current.width -=
                Shrink;

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

            if (Current.y ==
                    Next.y &&
                Current.x +
                        Current.width ==
                    Next.x) {

                Current.width +=
                    Next.width;

                Skyline.erase(
                    Skyline.begin() +
                    i + 1);

                continue;
            }

            ++i;
        }
    }

    inline bool RegisterTexture(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty
            *Texture,
        std::vector<float> &LookUpTextureData,
        uint32_t TextureID) {

        if (Texture == nullptr) {

            std::cout
                << "Texture is nullptr"
                << std::endl;

            return false;
        }

        if (MipLevel >=
            Texture->MipChain.size()) {

            if (Texture->MipChain.empty()) {

                std::cout
                    << "Texture has no mip data"
                    << std::endl;

            } else {

                std::cout
                    << "Texture has not got this mip lvl"
                    << std::endl;
            }

            return false;
        }

        const auto ExistingAllocation =
            CurrentAllocations.find(
                Texture->ID);

        if (ExistingAllocation !=
            CurrentAllocations.end()) {

            const AtlasAllocation
                &Allocation =
                    ExistingAllocation->second;

            UpdateLookupTexture(
                Texture,
                LookUpTextureData,
                TextureID,
                Allocation);

            ++Texture->References;

            return true;
        }

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

            } else {

                std::cout
                    << "Texture has not got this mip lvl"
                    << std::endl;
            }

            return false;
        }

        if (PackedWidth >
                MaxTextureDimension ||
            PackedHeight >
                MaxTextureDimension) {

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

        const auto PreviousAllocation =
            PreviousAllocations.find(
                Texture->ID);

        if (PreviousAllocation !=
            PreviousAllocations.end()) {

            const AtlasAllocation
                &Allocation =
                    PreviousAllocation->second;

            if (Allocation.Width ==
                    AlignedWidth &&
                Allocation.Height ==
                    AlignedHeight) {

                CurrentAllocations.emplace(
                    Texture->ID,
                    Allocation);

                UpdateLookupTexture(
                    Texture,
                    LookUpTextureData,
                    TextureID,
                    Allocation);

                PendingTextures.push_back(
                    Texture);

                ++Texture->References;

                return true;
            }

            HasRemovedTextures =
                true;

            HasAddedTextures =
                true;

            Dirty =
                true;
        }

        if (PreviousAllocation ==
            PreviousAllocations.end()) {

            HasAddedTextures =
                true;

            Dirty =
                true;
        }

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

        if ((X &
             (BC7_ALIGNMENT - 1)) != 0 ||
            (Y &
             (BC7_ALIGNMENT - 1)) != 0) {

            std::cerr
                << "Internal error: skyline returned "
                << "unaligned BC7 position "
                << X
                << ", "
                << Y
                << std::endl;

            return false;
        }

        InsertSkylineLevel(
            SkylineIndex,
            X,
            Y,
            PackedWidth,
            PackedHeight);

        MergeSkyline();

        const uint32_t TextureX =
            X +
            AlignedPadding;

        const uint32_t TextureY =
            Y +
            AlignedPadding;

        const AtlasAllocation Allocation{
            TextureX,
            TextureY,
            AlignedWidth,
            AlignedHeight};

        CurrentAllocations.emplace(
            Texture->ID,
            Allocation);

        ++Texture->References;

        UpdateLookupTexture(
            Texture,
            LookUpTextureData,
            TextureID,
            Allocation);

        PendingTextures.push_back(
            Texture);

        return true;
    }

    inline void FinalizeAllocationCache() {

        bool FoundAddedTexture =
            false;

        bool FoundRemovedTexture =
            false;

        for (const auto &[TextureID, Allocation] :
             PreviousAllocations) {

            (void)Allocation;

            if (!CurrentAllocations.contains(
                    TextureID)) {

                FoundRemovedTexture =
                    true;

                break;
            }
        }

        for (const auto &[TextureID, Allocation] :
             CurrentAllocations) {

            (void)Allocation;

            if (!PreviousAllocations.contains(
                    TextureID)) {

                FoundAddedTexture =
                    true;

                break;
            }
        }

        HasAddedTextures =
            HasAddedTextures ||
            FoundAddedTexture;

        HasRemovedTextures =
            HasRemovedTextures ||
            FoundRemovedTexture;

        if (HasRemovedTextures) {

            RebuildSkylineFromCurrentAllocations();

            Dirty =
                true;

            return;
        }

        if (HasAddedTextures) {

            Dirty =
                true;

            return;
        }

        Dirty =
            false;
    }

    void Assemble();
};

} // namespace PMMA::Internal::Rendering::Core2D
