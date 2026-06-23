#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "Internal/Management/Core2D_ColorTexture.hpp"
#include "Internal/Management/Core2D_RenderPipelineManager.hpp"

class CPP_Shader;
class CPP_Core2D_ColorTexture;

class EXPORT CPP_Core2D_RenderPipelineInstance {
private:
    CPP_Shader *ShapeDefinitionsShaderProgram = nullptr;

    std::array<std::vector<uintptr_t>, 4> PreviousShapeIDs;
    std::vector<uintptr_t> CurrentShapeIDs;

    bool UsingCache = false;

    bgfx::VertexLayout m_layout;
    bgfx::VertexBufferHandle vbh;
    bgfx::IndexBufferHandle ibh;
    bgfx::UniformHandle OrthDisplayProj;
    std::array<std::vector<InstanceData>, 4> PreviousInstanceData;
    std::vector<InstanceData> CurrentInstanceData;

    bgfx::DynamicVertexBufferHandle instanceVbh = BGFX_INVALID_HANDLE;
    bgfx::VertexLayout instanceLayout;

    Vertex VertexData[4];
    uint16_t IndexData[6];
    uint32_t numTiles;
    uint32_t PreviousBufferSize = 0;
    uint32_t CurrentDataSize = 0;

    bgfx::UniformHandle u_colorInfo;
    bgfx::UniformHandle s_colorTex;

    CPP_Core2D_ColorTexture ColorTexture;

    char BufferID = 0;

    bool ColorChanged = true;
    bool ShapePropertyChanged = true;

public:
    uint32_t instanceCount = 0;

    CPP_Core2D_RenderPipelineInstance();

    ~CPP_Core2D_RenderPipelineInstance() {
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

    inline void Reset() {
        ColorTexture.Reset();
        instanceCount = 0;

        ColorChanged = false;
        ShapePropertyChanged = false;
        UsingCache = true;

        CurrentShapeIDs = PreviousShapeIDs[BufferID];
        CurrentInstanceData = PreviousInstanceData[BufferID];

        CurrentDataSize = CurrentInstanceData.size();
    }

    template <typename T>
    inline void Add(T *lineShape) {
        uintptr_t ShapeID = lineShape->ID;

        auto &instance = lineShape->ShapeInstanceData;

        instance.color_index = ColorTexture.AddColor(&lineShape->Color, ShapeID, lineShape->ColorDataChanged);

        ColorChanged |= lineShape->ColorDataChanged;
        ShapePropertyChanged |= lineShape->ShapePropertyChanged;

        if (UsingCache && instanceCount < CurrentDataSize && CurrentShapeIDs[instanceCount] == ShapeID) {
            if (lineShape->ShapePropertyChanged) {
                CurrentInstanceData[instanceCount] = instance;
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        if (instanceCount >= CurrentDataSize) {
            CurrentInstanceData.push_back(instance);
            CurrentShapeIDs.push_back(ShapeID);
            CurrentDataSize++;
        } else {
            CurrentInstanceData[instanceCount] = instance;
            CurrentShapeIDs[instanceCount] = ShapeID;
        }
        instanceCount++;
    }

    void Render();
};