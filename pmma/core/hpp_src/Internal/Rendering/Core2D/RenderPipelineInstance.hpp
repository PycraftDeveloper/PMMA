#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "Internal/Rendering/Core2D/ColorTextureManager.hpp"
#include "Internal/Rendering/Core2D/RenderPipelineManager.hpp"
#include "Internal/Rendering/Core2D/TextureManager.hpp"

namespace PMMA::Internal::Rendering::Core2D {
class EXPORT RenderPipelineInstance {
private:
    std::array<std::array<std::vector<uintptr_t>, 2>, 4> PreviousShapeIDs;
    std::array<std::vector<uintptr_t>, 2> CurrentShapeIDs;

    std::array<std::array<std::vector<InstanceData>, 2>, 4> PreviousInstanceData;
    std::array<std::vector<InstanceData>, 2> CurrentInstanceData; // opaque, transparent

    PMMA::Internal::Rendering::Core2D::ColorTextureManager ColorTexture;
    PMMA::Internal::Rendering::Core2D::TextureManager TransparentTextureManager;
    PMMA::Internal::Rendering::Core2D::TextureManager OpaqueTextureManager;

    Vertex VertexData[4];
    uint16_t IndexData[6];

    bgfx::VertexLayout m_layout;
    bgfx::VertexLayout instanceLayout;

    uint32_t numTiles;

public:
    uintptr_t ID;

    uint32_t OpaqueInstanceCount = 0;
    uint32_t TransparentInstanceCount = 0;

private:
    uint32_t OpaquePreviousBufferSize = 0;
    uint32_t TransparentPreviousBufferSize = 0;
    uint32_t CurrentOpaqueDataSize = 0;
    uint32_t CurrentTransparentDataSize = 0;

    bgfx::VertexBufferHandle vbh;
    bgfx::IndexBufferHandle ibh;
    bgfx::UniformHandle OrthDisplayProj;

    bgfx::DynamicVertexBufferHandle OpaqueInstanceVbh = BGFX_INVALID_HANDLE;
    bgfx::DynamicVertexBufferHandle TransparentInstanceVbh = BGFX_INVALID_HANDLE;

    bgfx::UniformHandle u_textureInfo;
    bgfx::UniformHandle u_transparency;
    bgfx::UniformHandle s_colorTex;
    bgfx::UniformHandle s_Tex;

    char BufferID = 0;
    char PreviousBufferID = 0;

    bool ColorChanged = true;
    bool ShapePropertyChanged = true;
    bool UsingCache = false;

public:
    RenderPipelineInstance();

    ~RenderPipelineInstance() {
        if (bgfx::isValid(vbh)) {
            bgfx::destroy(vbh);
        }

        if (bgfx::isValid(ibh)) {
            bgfx::destroy(ibh);
        }

        if (bgfx::isValid(s_colorTex)) {
            bgfx::destroy(s_colorTex);
        }

        if (bgfx::isValid(u_textureInfo)) {
            bgfx::destroy(u_textureInfo);
        }

        if (bgfx::isValid(OrthDisplayProj)) {
            bgfx::destroy(OrthDisplayProj);
        }
    };

    void AdvanceView();

    inline void Reset() {
        ColorTexture.Reset();
        OpaqueInstanceCount = 0;
        TransparentInstanceCount = 0;

        ColorChanged = false;
        ShapePropertyChanged = false;
        UsingCache = true;

        CurrentShapeIDs = PreviousShapeIDs[PreviousBufferID];
        CurrentInstanceData = PreviousInstanceData[PreviousBufferID];

        CurrentOpaqueDataSize = CurrentInstanceData[0].size();
        CurrentTransparentDataSize = CurrentInstanceData[1].size();
    }

    template <typename T>
    inline void Add(T *shape) {
        uintptr_t ShapeID = shape->ID;

        auto &instance = shape->ShapeInstanceData;

        uint8_t Color[4];
        shape->Color.Get_RGBA(Color);
        bool IsOpaque = Color[3] == 255;

        instance.color_index = ColorTexture.AddColor(Color, ShapeID, shape->ColorDataChanged);

        // Texture
        // Texture Information
        uint16_t TexturePositionInAtlas[2] = {0, 0};
        uint16_t TextureSizeInAtlas[2] = {0, 0};
        if (shape->Texture.IsEnabled()) {
            if (shape->Texture.GetChannels() == 3) {
                OpaqueTextureManager.RegisterTexture(shape->Texture.TextureProperties);
            } else {
                TransparentTextureManager.RegisterTexture(shape->Texture.TextureProperties);
                IsOpaque = false;
            }
            shape->Texture.GetPositionInAtlas(ID, TexturePositionInAtlas);
            shape->Texture.GetSize(TextureSizeInAtlas);
        }

        instance.texture_position = PMMA::Internal::PackValues(TexturePositionInAtlas[0], TexturePositionInAtlas[1]);
        instance.texture_size = PMMA::Internal::PackValues(TextureSizeInAtlas[0], TextureSizeInAtlas[1]);

        ColorChanged |= shape->ColorDataChanged;
        ShapePropertyChanged |= shape->ShapePropertyChanged;

        if (IsOpaque) { // opaque
            if (UsingCache && OpaqueInstanceCount < CurrentOpaqueDataSize && CurrentShapeIDs[0][OpaqueInstanceCount] == ShapeID) {
                if (shape->ShapePropertyChanged) {
                    CurrentInstanceData[0][OpaqueInstanceCount] = instance;
                }

                OpaqueInstanceCount++;
                return;
            }

            UsingCache = false;

            if (OpaqueInstanceCount >= CurrentOpaqueDataSize) {
                CurrentInstanceData[0].push_back(instance);
                CurrentShapeIDs[0].push_back(ShapeID);
                CurrentOpaqueDataSize++;
            } else {
                CurrentInstanceData[0][OpaqueInstanceCount] = instance;
                CurrentShapeIDs[0][OpaqueInstanceCount] = ShapeID;
            }

            OpaqueInstanceCount++;
        } else { // transparent
            if (UsingCache && TransparentInstanceCount < CurrentTransparentDataSize && CurrentShapeIDs[1][TransparentInstanceCount] == ShapeID) {
                if (shape->ShapePropertyChanged) {
                    CurrentInstanceData[1][TransparentInstanceCount] = instance;
                }

                TransparentInstanceCount++;
                return;
            }

            UsingCache = false;

            if (TransparentInstanceCount >= CurrentTransparentDataSize) {
                CurrentInstanceData[1].push_back(instance);
                CurrentShapeIDs[1].push_back(ShapeID);
                CurrentTransparentDataSize++;
            } else {
                CurrentInstanceData[1][TransparentInstanceCount] = instance;
                CurrentShapeIDs[1][TransparentInstanceCount] = ShapeID;
            }

            TransparentInstanceCount++;
        }
    }

    void Render();
};
} // namespace PMMA::Internal::Rendering::Core2D