#pragma once
#include <algorithm>
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "Types.hpp"

namespace PMMA::Internal::Rendering::Core2D {
class ColorTextureManager {
private:
    std::array<std::vector<uint8_t>, 4> PreviousColorData;
    std::vector<uint8_t> CurrentColorData;

    std::array<std::vector<uintptr_t>, 4> PreviousShapeIDs;
    std::vector<uintptr_t> CurrentShapeIDs;

    uint32_t ShapeCount = 0;
    uint32_t PreviousShapeCount = 0;
    uint32_t CurrentShapeCount = 0;

    char BufferID = 0;
    char PreviousBufferID = 0;

    bool ColorChanged = true;

public:
    bool UsingCache = false;

    uint32_t m_colorTextureWidth = 0;
    uint32_t m_colorTextureHeight = 0;
    uint32_t MaxTextureDimension = 1024;

    bgfx::TextureHandle ColorTextureHandle = BGFX_INVALID_HANDLE;

    ~ColorTextureManager() {
        if (bgfx::isValid(ColorTextureHandle)) {
            bgfx::destroy(ColorTextureHandle);
        }
    }

    // ------------------------------------------------------------
    // ADD COLOR (hot path)
    // ------------------------------------------------------------
    inline uint32_t AddColor(
        PMMA::Types::Color *Color,
        uintptr_t ShapeID,
        bool ColorDataChanged) {
        uint32_t idx = ShapeCount++;

        if (UsingCache) {
            if (idx < CurrentShapeCount && CurrentShapeIDs[idx] == ShapeID) {
                if (ColorDataChanged) {
                    Color->Get_RGBA(CurrentColorData.data() + (idx << 2));

                    ColorChanged = true;
                }

                return idx;
            }
        }

        UsingCache = false;

        uint32_t byteIndex = idx << 2;

        if (idx >= CurrentShapeCount) {
            CurrentShapeIDs.push_back(ShapeID);
            CurrentColorData.resize(byteIndex + 4);
            CurrentShapeCount++;
        } else {
            CurrentShapeIDs[idx] = ShapeID;
        }

        Color->Get_RGBA(CurrentColorData.data() + (idx << 2));

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

        CurrentShapeCount = PreviousShapeCount;
    }

    // ------------------------------------------------------------
    // ASSEMBLE (upload texture)
    // ------------------------------------------------------------
    inline void Assemble() {
        if (!ColorChanged &&
            ShapeCount == PreviousShapeCount &&
            bgfx::isValid(ColorTextureHandle)) {
            return;
        }

        if (ShapeCount == 0) {
            return;
        }

        uint32_t numColors = ShapeCount;

        uint32_t width = std::min(MaxTextureDimension, numColors);
        width = std::max(width, 1u);

        uint32_t height = (numColors + width - 1) / width;

        size_t expectedSize = static_cast<size_t>(width) * height * 4;

        CurrentColorData.resize(expectedSize, 0);

        PreviousColorData[BufferID] = CurrentColorData;

        PreviousShapeIDs[BufferID].assign(
            CurrentShapeIDs.begin(),
            CurrentShapeIDs.begin() + ShapeCount);

        const std::vector<uint8_t> &gpuData = PreviousColorData[BufferID];

        const bgfx::Memory *texMem = bgfx::makeRef(
            gpuData.data(),
            static_cast<uint32_t>(gpuData.size()));

        if (bgfx::isValid(ColorTextureHandle)) {
            if (m_colorTextureWidth != width ||
                m_colorTextureHeight != height) {
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
                BGFX_SAMPLER_U_CLAMP |
                    BGFX_SAMPLER_V_CLAMP |
                    BGFX_SAMPLER_POINT);
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