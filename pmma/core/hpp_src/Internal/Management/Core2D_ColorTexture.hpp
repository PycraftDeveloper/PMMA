#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "CoreTypes.hpp"

class CPP_Core2D_ColorTexture {
private:
    std::vector<uint8_t> PreviousColorData;
    std::vector<uint8_t> CurrentColorData;
    std::vector<uintptr_t> PreviousShapeIDs;
    std::vector<uintptr_t> CurrentShapeIDs;
    uint32_t ShapeCount = 0;
    uint32_t PreviousShapeCount = 0;
    uint32_t CurrentDataSize = 0;

    bool ColorChanged = true;

public:
    bool UsingCache = false;

    bgfx::TextureHandle ColorTexture;

    uint32_t m_colorTextureWidth = 0;
    uint32_t m_colorTextureHeight = 0;
    uint32_t MaxTextureDimension;

    CPP_Core2D_ColorTexture() {
        ColorTexture = BGFX_INVALID_HANDLE;
    }

    ~CPP_Core2D_ColorTexture() {
        if (bgfx::isValid(ColorTexture)) {
            bgfx::destroy(ColorTexture);
        }
    }

    inline uint32_t AddColor(CPP_Color *Color, uintptr_t ShapeID, bool ColorDataChanged) {
        ColorChanged |= ColorDataChanged;

        if (UsingCache && ShapeCount < CurrentDataSize && CurrentShapeIDs[ShapeCount] == ShapeID) {
            if (ColorDataChanged) {
                size_t requiredSize = ShapeCount * 4;
                if (CurrentDataSize < requiredSize) {
                    CurrentColorData.resize(requiredSize);
                }
                Color->Get_RGBA(&CurrentColorData[ShapeCount * 4]);
            }

            ShapeCount++;
            return ShapeCount;
        }

        UsingCache = false;

        if (ShapeCount >= CurrentDataSize) {
            size_t requiredSize = ShapeCount * 4;
            if (CurrentDataSize < requiredSize) {
                CurrentColorData.resize(requiredSize);
            }
            Color->Get_RGBA(&CurrentColorData[ShapeCount * 4]);

            CurrentShapeIDs.push_back(ShapeID);
            CurrentDataSize++;
        } else {
            Color->Get_RGBA(&CurrentColorData[ShapeCount * 4]);
            CurrentShapeIDs[ShapeCount] = ShapeID;
        }
        ShapeCount++;

        return ShapeCount;
    }

    inline void Reset() {
        ShapeCount = 0;
        UsingCache = true;
        ColorChanged = false;

        CurrentShapeIDs = PreviousShapeIDs;
        CurrentColorData = PreviousColorData;

        CurrentDataSize = CurrentColorData.size();
    }

    inline void Assemble() {
        if (ColorChanged || ShapeCount != PreviousShapeCount || !bgfx::isValid(ColorTexture)) {
            CurrentColorData.resize(ShapeCount * 4);
            CurrentColorData.shrink_to_fit();

            CurrentShapeIDs.resize(ShapeCount);
            CurrentShapeIDs.shrink_to_fit();

            PreviousShapeIDs = CurrentShapeIDs;
            PreviousColorData = CurrentColorData;

            uint32_t CurrentBufferSize = PreviousColorData.size();

            uint32_t numColors = (uint32_t)ShapeCount;
            uint32_t width = std::min(MaxTextureDimension, numColors);
            uint32_t height = (numColors + width - 1) / width;

            size_t expectedSize = width * height * 4;
            if (CurrentBufferSize < expectedSize) {
                PreviousColorData.resize(expectedSize, 0); // Pad with transparent black
            }

            const bgfx::Memory *texMem = bgfx::copy(
                PreviousColorData.data(),
                static_cast<uint32_t>(CurrentBufferSize * sizeof(uint8_t)));

            // If texture exists but size changed, destroy and recreate it
            if (bgfx::isValid(ColorTexture)) {
                if (m_colorTextureWidth != width || m_colorTextureHeight != height) {
                    bgfx::destroy(ColorTexture);
                    ColorTexture = BGFX_INVALID_HANDLE;
                }
            }

            // create texture if missing
            if (!bgfx::isValid(ColorTexture)) {
                ColorTexture = bgfx::createTexture2D(
                    (uint16_t)width, (uint16_t)height,
                    false, // hasMips
                    1,     // num layers
                    bgfx::TextureFormat::RGBA8,
                    BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
            }

            bgfx::updateTexture2D(ColorTexture, 0, 0, 0, 0, width, height, texMem);

            // store width/height for shader normalization
            m_colorTextureWidth = width;
            m_colorTextureHeight = height;
        }
    }
};