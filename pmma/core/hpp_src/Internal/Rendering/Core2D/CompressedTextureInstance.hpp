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
    // ========================================================================
    // Textures registered during the current frame.
    //
    // Assemble() uses this list to determine which texture mip data may need
    // to be copied into the CPU atlas.
    //
    // A texture may appear more than once if it is registered multiple times
    // during the same frame. That is intentional; CurrentAllocations is the
    // authoritative source for the allocation itself.
    // ========================================================================

    std::vector<
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *>
        PendingTextures;

    // ========================================================================
    // Current working skyline.
    //
    // This describes the rectangles currently present in
    // CurrentAllocations.
    //
    // During normal operation this starts from PreviousSkyline and receives
    // new allocations as textures are registered.
    //
    // If a removal is detected, FinalizeAllocationCache() reconstructs this
    // skyline from CurrentAllocations.
    // ========================================================================

    std::vector<
        PMMA::Internal::Rendering::Core2D::SkylineNode>
        Skyline;

    // ========================================================================
    // Skyline belonging to the previous completed frame.
    //
    // This corresponds to PreviousAllocations.
    //
    // It can be reused when the current frame contains the same set of
    // allocations, and it remains a valid conservative starting point when
    // textures are only added.
    //
    // If a texture is removed, this skyline contains a ghost rectangle and
    // therefore must not remain the authoritative skyline.
    // ========================================================================

    std::vector<
        PMMA::Internal::Rendering::Core2D::SkylineNode>
        PreviousSkyline;

    // ========================================================================
    // Frame-level change state.
    //
    // HasAddedTextures:
    //     At least one current allocation did not exist in the previous
    //     frame, or an existing texture changed dimensions and therefore
    //     required a new allocation.
    //
    // HasRemovedTextures:
    //     At least one allocation from the previous frame is no longer
    //     present in the current frame, or an existing texture changed
    //     dimensions.
    //
    // Assemble() uses these indirectly through Dirty and the allocation
    // caches to determine whether the previous CPU atlas can be preserved.
    // ========================================================================

    bool HasAddedTextures = false;
    bool HasRemovedTextures = false;

    // ========================================================================
    // Calculate the exact rectangle reserved by a mip in the atlas.
    //
    // The returned values are:
    //
    //     OutMipWidth / OutMipHeight
    //         Actual source texture dimensions.
    //
    //     OutAlignedWidth / OutAlignedHeight
    //         Dimensions rounded up to BC7's 4x4 block size.
    //
    //     OutPackedWidth / OutPackedHeight
    //         Full skyline reservation including padding.
    //
    //     OutAlignedPadding
    //         Padding rounded to a BC7 block boundary.
    //
    // CanFitTexture() and RegisterTexture() both use this function so they
    // cannot disagree about the dimensions of a texture.
    // ========================================================================

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

    // ========================================================================
    // Rebuild the skyline directly from CurrentAllocations.
    //
    // This is used after a removal or replacement.
    //
    // We deliberately do NOT replay InsertSkylineLevel() because doing so
    // would make the reconstructed skyline dependent on unordered_map
    // iteration order.
    //
    // Instead, all rectangle boundaries are converted into X intervals and
    // the maximum occupied Y for each interval is calculated.
    // ========================================================================

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

        // --------------------------------------------------------------------
        // Collect every X boundary.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // Generate a skyline node for each horizontal interval.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // Merge adjacent nodes with the same height.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // Ensure the complete atlas width is represented.
        // --------------------------------------------------------------------

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

    // ========================================================================
    // Write one allocation into the frame lookup-data array.
    //
    // IMPORTANT:
    //
    // The lookup texture contains the ACTUAL texture rectangle:
    //
    //     X
    //     Y
    //     actual width
    //     actual height
    //
    // It does NOT contain the padded skyline rectangle.
    //
    // AssembleLookupTexture() in CompressedTextureManager later converts
    // these values into normalized atlas coordinates.
    // ========================================================================

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
    // ========================================================================
    // Allocation cache.
    //
    // PreviousAllocations:
    //     The exact allocation layout belonging to the previous frame.
    //
    // CurrentAllocations:
    //     The exact allocation layout belonging to the current frame.
    //
    // An AtlasAllocation stores the unpadded texture position and the
    // BC7-aligned texture dimensions.
    // ========================================================================

    std::unordered_map<
        uintptr_t,
        AtlasAllocation>
        PreviousAllocations;

    std::unordered_map<
        uintptr_t,
        AtlasAllocation>
        CurrentAllocations;

    // ========================================================================
    // CPU atlas buffers.
    //
    // Four buffers are used so that the buffer uploaded to bgfx can remain
    // untouched while another CPU buffer is assembled.
    // ========================================================================

    std::array<
        CompressedTexture_BufferData,
        4>
        AtlasPixels;

    // ========================================================================
    // Atlas configuration.
    // ========================================================================

    uint32_t AtlasPadding = 0;

    uint32_t MipLevel = 0;

    uint32_t FramesSinceLastChange = 0;

public:
    // ========================================================================
    // Indicates that the current CPU/GPU atlas must be rebuilt.
    //
    // This is true when:
    //
    //     - a texture was added;
    //     - a texture was removed;
    //     - an existing texture changed dimensions;
    //     - the atlas was otherwise invalidated.
    //
    // If false, Assemble() does nothing and the existing GPU texture remains
    // valid.
    // ========================================================================

    bool Dirty = false;

    // ========================================================================
    // CPU atlas buffer currently being constructed.
    //
    // PreviousBufferID identifies the CPU atlas containing the previous
    // completed layout and is therefore the source buffer for incremental
    // atlas reconstruction.
    // ========================================================================

    char BufferID = 0;

    char PreviousBufferID = 0;

    // ========================================================================
    // GPU atlas texture.
    //
    // This contains exactly ONE BC7 texture for this mip level.
    // It has no mip chain of its own.
    // ========================================================================

    bgfx::TextureHandle TextureHandle =
        BGFX_INVALID_HANDLE;

    uint32_t m_TextureWidth = 0;

    uint32_t m_TextureHeight = 0;

    // ========================================================================
    // Maximum atlas dimension.
    // ========================================================================

    uint32_t MaxTextureDimension = 1024;

    // ========================================================================
    // Render pipeline instance owning this atlas.
    // ========================================================================

    uintptr_t RenderPipelineInstanceID = 0;

    // ========================================================================
    // BC7 alignment.
    // ========================================================================

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

    // ========================================================================
    // Constructor.
    // ========================================================================

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

    // ========================================================================
    // Destructor.
    // ========================================================================

    ~CompressedTextureInstance() {

        if (bgfx::isValid(TextureHandle)) {

            bgfx::destroy(
                TextureHandle);

            TextureHandle =
                BGFX_INVALID_HANDLE;
        }
    }

    // ========================================================================
    // Begin a new frame.
    //
    // The current frame becomes the previous frame's cached layout.
    //
    // The important invariant after Reset() is:
    //
    //     PreviousAllocations == layout used by previous frame
    //     CurrentAllocations  == empty
    //
    // and:
    //
    //     PreviousSkyline == skyline for PreviousAllocations
    //     Skyline         == working copy of PreviousSkyline
    //
    // This lets normal frames reuse allocations without repacking.
    // ========================================================================

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

    // ========================================================================
    // Query whether a texture can be registered.
    //
    // Existing textures reuse their cached allocation.
    //
    // New textures are tested against the current skyline.
    //
    // If a later registration causes a removal to be discovered, the final
    // authoritative skyline is reconstructed by FinalizeAllocationCache().
    // ========================================================================

    inline bool CanFitTexture(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty
            *Texture) {

        if (Texture == nullptr) {
            return false;
        }

        // --------------------------------------------------------------------
        // Already registered this frame.
        // --------------------------------------------------------------------

        if (CurrentAllocations.contains(
                Texture->ID)) {

            return true;
        }

        // --------------------------------------------------------------------
        // Existing previous allocation.
        //
        // Validate that its dimensions still match this mip.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // New texture.
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

    // ========================================================================
    // Find the best skyline position using the bottom-left heuristic.
    //
    // The returned X/Y describe the complete padded rectangle.
    // ========================================================================

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

    // ========================================================================
    // Insert a padded rectangle into the skyline.
    // ========================================================================

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

    // ========================================================================
    // Merge adjacent skyline nodes with identical heights.
    // ========================================================================

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

    // ========================================================================
    // Register a texture in this mip-level atlas.
    //
    // There are three important paths:
    //
    // 1. Already registered this frame:
    //      Reuse CurrentAllocations.
    //
    // 2. Existing allocation with identical dimensions:
    //      Reuse PreviousAllocations.
    //
    // 3. New or dimension-changed texture:
    //      Allocate a new skyline position.
    //
    // The final texture set is not known until all registrations have
    // completed, so removals are reconciled by FinalizeAllocationCache().
    // ========================================================================

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

        // --------------------------------------------------------------------
        // Validate mip data.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // Already registered during this frame.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // Calculate dimensions.
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

            } else {

                std::cout
                    << "Texture has not got this mip lvl"
                    << std::endl;
            }

            return false;
        }

        // --------------------------------------------------------------------
        // The padded rectangle cannot fit in the atlas.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // Look for an allocation from the previous frame.
        // --------------------------------------------------------------------

        const auto PreviousAllocation =
            PreviousAllocations.find(
                Texture->ID);

        if (PreviousAllocation !=
            PreviousAllocations.end()) {

            const AtlasAllocation
                &Allocation =
                    PreviousAllocation->second;

            // ----------------------------------------------------------------
            // Existing allocation still matches.
            //
            // Reuse the exact position.
            // ----------------------------------------------------------------

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

            // ----------------------------------------------------------------
            // Same texture ID, but dimensions changed.
            //
            // The old allocation can no longer be trusted.
            //
            // Treat this as both a removal and an addition so that
            // FinalizeAllocationCache() rebuilds the skyline and Assemble()
            // reconstructs the atlas rather than trying to preserve stale
            // pixels.
            // ----------------------------------------------------------------

            HasRemovedTextures =
                true;

            HasAddedTextures =
                true;

            Dirty =
                true;
        }

        // --------------------------------------------------------------------
        // Genuinely new texture.
        // --------------------------------------------------------------------

        if (PreviousAllocation ==
            PreviousAllocations.end()) {

            HasAddedTextures =
                true;

            Dirty =
                true;
        }

        // --------------------------------------------------------------------
        // Find a position against the current skyline.
        //
        // If a removal is eventually detected, FinalizeAllocationCache()
        // will rebuild the skyline from CurrentAllocations.
        //
        // Until then, retaining the old skyline is conservative because old
        // rectangles can only make placement less efficient; they cannot
        // cause a new texture to overlap a still-existing texture.
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
        // Every skyline coordinate must be BC7 aligned.
        // --------------------------------------------------------------------

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
        // Remove the padding from the actual texture coordinates.
        // --------------------------------------------------------------------

        const uint32_t TextureX =
            X +
            AlignedPadding;

        const uint32_t TextureY =
            Y +
            AlignedPadding;

        // --------------------------------------------------------------------
        // Store the actual BC7-aligned texture allocation.
        // --------------------------------------------------------------------

        const AtlasAllocation Allocation{
            TextureX,
            TextureY,
            AlignedWidth,
            AlignedHeight};

        CurrentAllocations.emplace(
            Texture->ID,
            Allocation);

        ++Texture->References;

        // --------------------------------------------------------------------
        // Update lookup information.
        //
        // The lookup stores the actual mip dimensions rather than the
        // padded allocation dimensions.
        // --------------------------------------------------------------------

        UpdateLookupTexture(
            Texture,
            LookUpTextureData,
            TextureID,
            Allocation);

        PendingTextures.push_back(
            Texture);

        return true;
    }

    // ========================================================================
    // Reconcile the complete current texture set against the previous frame.
    //
    // THIS MUST BE CALLED AFTER ALL RegisterTexture() CALLS FOR THE FRAME.
    //
    // This is the authoritative point at which we know whether textures have
    // disappeared.
    //
    // Cases:
    //
    //     A B C -> A B C
    //         No change.
    //
    //     A B C -> A B C D
    //         Addition only.
    //
    //     A B C D -> A B C
    //         Removal.
    //
    //     A B C -> A B D
    //         Removal + addition.
    //
    //     A -> A (different dimensions)
    //         Replacement.
    //
    // Removal/replacement requires the skyline to be reconstructed from the
    // current allocation set.
    // ========================================================================

    inline void FinalizeAllocationCache() {

        bool FoundAddedTexture =
            false;

        bool FoundRemovedTexture =
            false;

        // --------------------------------------------------------------------
        // Detect removals.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // Detect additions.
        // --------------------------------------------------------------------

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

        // --------------------------------------------------------------------
        // Preserve information discovered during RegisterTexture().
        // --------------------------------------------------------------------

        HasAddedTextures =
            HasAddedTextures ||
            FoundAddedTexture;

        HasRemovedTextures =
            HasRemovedTextures ||
            FoundRemovedTexture;

        // --------------------------------------------------------------------
        // Removal/replacement.
        //
        // The old skyline contains rectangles that no longer belong to the
        // current atlas, so it must be reconstructed.
        // --------------------------------------------------------------------

        if (HasRemovedTextures) {

            RebuildSkylineFromCurrentAllocations();

            Dirty =
                true;

            return;
        }

        // --------------------------------------------------------------------
        // Addition only.
        //
        // RegisterTexture() already inserted the new allocations into the
        // working skyline.
        // --------------------------------------------------------------------

        if (HasAddedTextures) {

            Dirty =
                true;

            return;
        }

        // --------------------------------------------------------------------
        // No additions and no removals.
        //
        // The allocation set is unchanged, so the existing GPU atlas remains
        // authoritative.
        // --------------------------------------------------------------------

        Dirty =
            false;
    }

    // ========================================================================
    // Assemble the CPU/GPU atlas.
    //
    // The implementation is in the .cpp.
    //
    // IMPORTANT:
    //
    // The caller must invoke:
    //
    //     RegisterTexture(...)
    //     ...
    //     FinalizeAllocationCache()
    //     Assemble()
    //
    // in that order for every frame.
    // ========================================================================

    void Assemble();
};

} // namespace PMMA::Internal::Rendering::Core2D