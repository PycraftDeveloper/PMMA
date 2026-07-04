#pragma once
#include <algorithm>
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "Types.hpp"

namespace PMMA::Internal::Rendering::Core2D {
class ColorTexture {
private:
    std::array<std::vector<uint8_t>, 4> PreviousColorData;
    std::vector<uint8_t> CurrentColorData;

    std::array<std::vector<uintptr_t>, 4> PreviousShapeIDs;
    std::vector<uintptr_t> CurrentShapeIDs;

    uint32_t ShapeCount = 0;
    uint32_t PreviousShapeCount = 0;

    char BufferID = 0;
    char PreviousBufferID = 0;

    bool ColorChanged = true;

public:
    bool UsingCache = false;

    bgfx::TextureHandle ColorTextureHandle = BGFX_INVALID_HANDLE;

    uint32_t m_colorTextureWidth = 0;
    uint32_t m_colorTextureHeight = 0;
    uint32_t MaxTextureDimension = 1024;

    ~ColorTexture() {
        if (bgfx::isValid(ColorTextureHandle)) {
            bgfx::destroy(ColorTextureHandle);
        }
    }

    // ------------------------------------------------------------
    // ADD COLOR (hot path)
    // ------------------------------------------------------------
    inline uint32_t AddColor(PMMA::Types::Color *Color, uintptr_t ShapeID, bool ColorDataChanged) {
        ColorChanged |= ColorDataChanged;

        uint32_t idx = ShapeCount++;
        uint32_t byteIndex = idx * 4;

        // Ensure buffer size (safe + single responsibility)
        if (byteIndex + 4 > CurrentColorData.size()) {
            CurrentColorData.resize(byteIndex + 4);
        }

        // Ensure ID buffer size
        if (idx >= CurrentShapeIDs.size()) {
            CurrentShapeIDs.resize(idx + 1);
        }

        bool cacheHit =
            UsingCache &&
            idx < PreviousShapeIDs[BufferID].size() &&
            PreviousShapeIDs[BufferID][idx] == ShapeID;

        if (!cacheHit || ColorDataChanged) {
            Color->Get_RGBA(&CurrentColorData[byteIndex]);
        } else if (cacheHit) {
            // reuse previous color data
            const uint8_t *prev =
                PreviousColorData[BufferID].data() + byteIndex;

            CurrentColorData[byteIndex + 0] = prev[0];
            CurrentColorData[byteIndex + 1] = prev[1];
            CurrentColorData[byteIndex + 2] = prev[2];
            CurrentColorData[byteIndex + 3] = prev[3];
        }

        CurrentShapeIDs[idx] = ShapeID;

        return idx;
    }

    // ------------------------------------------------------------
    // RESET (start new frame)
    // ------------------------------------------------------------
    inline void Reset() {
        ShapeCount = 0;
        UsingCache = true;
        ColorChanged = false;

        CurrentShapeIDs = PreviousShapeIDs[PreviousBufferID];
        CurrentColorData = PreviousColorData[PreviousBufferID];
    }

    // ------------------------------------------------------------
    // ASSEMBLE (upload texture)
    // ------------------------------------------------------------
    inline void Assemble() {
        if (!ColorChanged && ShapeCount == PreviousShapeCount && bgfx::isValid(ColorTextureHandle))
            return;

        uint32_t numColors = ShapeCount;

        uint32_t width = std::min(MaxTextureDimension, numColors);
        width = std::max(width, 1u);

        uint32_t height = (numColors + width - 1) / width;

        size_t expectedSize = static_cast<size_t>(width) * height * 4;

        // Ensure buffer is FULL texture size (not logical size)
        CurrentColorData.resize(expectedSize, 0); // <-- PAD WITH TRANSPARENT BLACK

        // Copy into persistent buffer for BGFX
        PreviousColorData[BufferID] = CurrentColorData;
        PreviousShapeIDs[BufferID] = CurrentShapeIDs;

        const std::vector<uint8_t> &gpuData = PreviousColorData[BufferID];

        const bgfx::Memory *texMem = bgfx::makeRef(
            gpuData.data(),
            static_cast<uint32_t>(gpuData.size()));

        if (bgfx::isValid(ColorTextureHandle)) {
            if (m_colorTextureWidth != width || m_colorTextureHeight != height) {
                bgfx::destroy(ColorTextureHandle);
                ColorTextureHandle = BGFX_INVALID_HANDLE;
            }
        }

        if (!bgfx::isValid(ColorTextureHandle)) {
            ColorTextureHandle = bgfx::createTexture2D(
                (uint16_t)width,
                (uint16_t)height,
                false,
                1,
                bgfx::TextureFormat::RGBA8,
                BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
        }

        bgfx::updateTexture2D(
            ColorTextureHandle,
            0, 0, 0, 0,
            width,
            height,
            texMem);

        m_colorTextureWidth = width;
        m_colorTextureHeight = height;

        PreviousShapeCount = ShapeCount;

        PreviousBufferID = BufferID;
        BufferID = (BufferID + 1) % 4;
    }
};
} // namespace PMMA::Internal::Rendering::Core2D