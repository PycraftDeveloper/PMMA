#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "Internal/Rendering/Core2D/ColorTextureManager.hpp"
#include "Internal/Rendering/Core2D/RenderPipelineManager.hpp"
#include "Internal/Rendering/Core2D/TextureManager.hpp"

namespace PMMA::Graphics {
class Shader;
}

namespace PMMA::Internal::Rendering::Core2D {
class EXPORT RenderPipelineInstance {
private:
    PMMA::Graphics::Shader *ShapeDefinitionsShaderProgram = nullptr;

    std::array<std::array<std::vector<uintptr_t>, 2>, 4> PreviousShapeIDs;
    std::array<std::vector<uintptr_t>, 2> CurrentShapeIDs;

    bool UsingCache = false;

    bgfx::VertexLayout m_layout;
    bgfx::VertexBufferHandle vbh;
    bgfx::IndexBufferHandle ibh;
    bgfx::UniformHandle OrthDisplayProj;
    std::array<std::array<std::vector<InstanceData>, 2>, 4> PreviousInstanceData;
    std::array<std::vector<InstanceData>, 2> CurrentInstanceData; // opaque, transparent

    bgfx::DynamicVertexBufferHandle OpaqueInstanceVbh = BGFX_INVALID_HANDLE;
    bgfx::DynamicVertexBufferHandle TransparentInstanceVbh = BGFX_INVALID_HANDLE;
    bgfx::VertexLayout instanceLayout;

    Vertex VertexData[4];
    uint16_t IndexData[6];
    uint32_t numTiles;
    uint32_t OpaquePreviousBufferSize = 0;
    uint32_t TransparentPreviousBufferSize = 0;
    uint32_t CurrentOpaqueDataSize = 0;
    uint32_t CurrentTransparentDataSize = 0;

    bgfx::UniformHandle u_colorInfo;
    bgfx::UniformHandle u_transparency;
    bgfx::UniformHandle s_colorTex;

    PMMA::Internal::Rendering::Core2D::ColorTextureManager ColorTexture;
    PMMA::Internal::Rendering::Core2D::TextureManager TextureManager;

    char BufferID = 0;
    char PreviousBufferID = 0;

    bool ColorChanged = true;
    bool ShapePropertyChanged = true;

public:
    uintptr_t ID;

    uint32_t OpaqueInstanceCount = 0;
    uint32_t TransparentInstanceCount = 0;

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

        if (bgfx::isValid(u_colorInfo)) {
            bgfx::destroy(u_colorInfo);
        }

        if (bgfx::isValid(OrthDisplayProj)) {
            bgfx::destroy(OrthDisplayProj);
        }

        delete ShapeDefinitionsShaderProgram;
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

        instance.color_index = ColorTexture.AddColor(Color, ShapeID, shape->ColorDataChanged);

        // Texture
        // Texture Information
        uint16_t TexturePositionInAtlas[2] = {0, 0};
        uint16_t TextureSizeInAtlas[2] = {0, 0};
        if (shape->Texture.IsEnabled()) {
            TextureManager.RegisterTexture(shape->Texture.TextureProperties);
            shape->Texture.GetPositionInAtlas(ID, TexturePositionInAtlas);
            shape->Texture.GetSize(TextureSizeInAtlas);
        }

        instance.texture_position = PMMA::Internal::PackValues(TexturePositionInAtlas[0], TexturePositionInAtlas[1]);
        instance.texture_size = PMMA::Internal::PackValues(TextureSizeInAtlas[0], TextureSizeInAtlas[1]);

        ColorChanged |= shape->ColorDataChanged;
        ShapePropertyChanged |= shape->ShapePropertyChanged;

        if (Color[3] == 255) { // opaque
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