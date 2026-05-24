#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "Internal/Management/Core2D_RenderPipelineManager.hpp"
#include "Rendering/Shapes2D/ArcShape.hpp"
#include "Rendering/Shapes2D/EllipseShape.hpp"
#include "Rendering/Shapes2D/LineShape.hpp"
#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"

class CPP_Shader;
class CPP_Core2D_ColorTexture;

class EXPORT CPP_Core2D_RenderPipelineInstance {
private:
    CPP_Shader *ShapeDefinitionsShaderProgram = nullptr;

    bgfx::VertexLayout m_layout;
    bgfx::VertexBufferHandle vbh;
    bgfx::IndexBufferHandle ibh;
    bgfx::UniformHandle OrthDisplayProj;
    std::array<std::vector<InstanceData>, 4> instanceDataArray;

    bgfx::DynamicVertexBufferHandle instanceVbh = BGFX_INVALID_HANDLE;
    bgfx::VertexLayout instanceLayout;

    Vertex VertexData[4];
    uint16_t IndexData[6];
    uint32_t numTiles;

    bgfx::UniformHandle u_colorInfo;
    bgfx::UniformHandle s_colorTex;

    CPP_Core2D_ColorTexture ColorTexture;
    uint32_t PreviousInstanceCount = 0;

    char BufferID = 0;

    bool ColorChanged = true;
    bool ShapePropertyChanged = true;

public:
    uint32_t instanceCount = 0; // max: 16'777'216

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
        instanceDataArray[BufferID].clear();
        PreviousInstanceCount = instanceCount;
        instanceCount = 0;
        ColorChanged = false;
        ShapePropertyChanged = false;
    }

    void Add(CPP_LineShape *lineShape) {
        instanceCount++;

        lineShape->ShapeInstanceData.color_index = ColorTexture.AddColor(lineShape->Color, lineShape->ID, lineShape->ColorDataChanged);

        ColorChanged |= lineShape->ColorDataChanged;
        ShapePropertyChanged |= lineShape->ShapePropertyChanged;

        instanceDataArray[BufferID].push_back(lineShape->ShapeInstanceData);
    }

    void Add(CPP_RadialPolygonShape *radialPolygonShape) {
        instanceCount++;

        radialPolygonShape->ShapeInstanceData.color_index = ColorTexture.AddColor(radialPolygonShape->Color, radialPolygonShape->ID, radialPolygonShape->ColorDataChanged);

        ColorChanged |= radialPolygonShape->ColorDataChanged;
        ShapePropertyChanged |= radialPolygonShape->ShapePropertyChanged;

        instanceDataArray[BufferID].push_back(radialPolygonShape->ShapeInstanceData);
    }

    void Render();
};