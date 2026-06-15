#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "Internal/Management/Core2D_ColorTexture.hpp"
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

    std::array<std::vector<uintptr_t>, 4> PreviousShapeIDs;
    std::array<std::vector<uintptr_t>, 4> CurrentShapeIDs;

    bool UsingCache = false;

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
        PreviousInstanceCount = instanceCount;
        instanceCount = 0;
        ColorChanged = false;
        ShapePropertyChanged = false;
        PreviousShapeIDs[BufferID] = CurrentShapeIDs[BufferID];
        CurrentShapeIDs[BufferID].clear();
        UsingCache = true;
    }

    inline void Add(CPP_LineShape *lineShape) {
        uintptr_t ShapeID = lineShape->ID;

        lineShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&lineShape->Color, ShapeID, lineShape->ColorDataChanged);

        ColorChanged |= lineShape->ColorDataChanged;
        ShapePropertyChanged |= lineShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < PreviousShapeIDs[BufferID].size() && PreviousShapeIDs[BufferID][instanceCount] == ShapeID) {
            if (ShapePropertyChanged) {
                if (instanceCount < instanceDataArray[BufferID].size()) {
                    instanceDataArray[BufferID][instanceCount] = lineShape->ShapeInstanceData;
                } else {
                    instanceDataArray[BufferID].push_back(lineShape->ShapeInstanceData);
                }
            }

            if (CurrentShapeIDs[BufferID].empty() || CurrentShapeIDs[BufferID].back() != ShapeID) {
                CurrentShapeIDs[BufferID].push_back(ShapeID);
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        if (CurrentShapeIDs[BufferID].empty() || CurrentShapeIDs[BufferID].back() != ShapeID) {
            if (instanceCount < CurrentShapeIDs[BufferID].size()) {
                CurrentShapeIDs[BufferID].resize(instanceCount);
            }
            CurrentShapeIDs[BufferID].push_back(ShapeID);
        }

        instanceDataArray[BufferID].push_back(lineShape->ShapeInstanceData);
        instanceCount++;
    }

    inline void Add(CPP_EllipseShape *ellipseShape) {
        uintptr_t ShapeID = ellipseShape->ID;

        ellipseShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&ellipseShape->Color, ShapeID, ellipseShape->ColorDataChanged);

        ColorChanged |= ellipseShape->ColorDataChanged;
        ShapePropertyChanged |= ellipseShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < PreviousShapeIDs[BufferID].size() && PreviousShapeIDs[BufferID][instanceCount] == ShapeID) {
            if (ShapePropertyChanged) {
                if (instanceCount < instanceDataArray[BufferID].size()) {
                    instanceDataArray[BufferID][instanceCount] = ellipseShape->ShapeInstanceData;
                } else {
                    instanceDataArray[BufferID].push_back(ellipseShape->ShapeInstanceData);
                }
            }

            if (CurrentShapeIDs[BufferID].empty() || CurrentShapeIDs[BufferID].back() != ShapeID) {
                CurrentShapeIDs[BufferID].push_back(ShapeID);
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        if (CurrentShapeIDs[BufferID].empty() || CurrentShapeIDs[BufferID].back() != ShapeID) {
            if (instanceCount < CurrentShapeIDs[BufferID].size()) {
                CurrentShapeIDs[BufferID].resize(instanceCount);
            }
            CurrentShapeIDs[BufferID].push_back(ShapeID);
        }

        instanceDataArray[BufferID].push_back(ellipseShape->ShapeInstanceData);
        instanceCount++;
    }

    inline void Add(CPP_RadialPolygonShape *radialPolygonShape) {
        uintptr_t ShapeID = radialPolygonShape->ID;

        radialPolygonShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&radialPolygonShape->Color, ShapeID, radialPolygonShape->ColorDataChanged);

        ColorChanged |= radialPolygonShape->ColorDataChanged;
        ShapePropertyChanged |= radialPolygonShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < PreviousShapeIDs[BufferID].size() && PreviousShapeIDs[BufferID][instanceCount] == ShapeID) {
            if (ShapePropertyChanged) {
                if (instanceCount < instanceDataArray[BufferID].size()) {
                    instanceDataArray[BufferID][instanceCount] = radialPolygonShape->ShapeInstanceData;
                } else {
                    instanceDataArray[BufferID].push_back(radialPolygonShape->ShapeInstanceData);
                }
            }

            if (CurrentShapeIDs[BufferID].empty() || CurrentShapeIDs[BufferID].back() != ShapeID) {
                if (instanceCount < CurrentShapeIDs[BufferID].size()) {
                    CurrentShapeIDs[BufferID].resize(instanceCount);
                }
                CurrentShapeIDs[BufferID].push_back(ShapeID);
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        if (CurrentShapeIDs[BufferID].empty() || CurrentShapeIDs[BufferID].back() != ShapeID) {
            CurrentShapeIDs[BufferID].push_back(ShapeID);
        }

        instanceDataArray[BufferID].push_back(radialPolygonShape->ShapeInstanceData);
        instanceCount++;
    }

    inline void Add(CPP_ArcShape *arcShape) {
        uintptr_t ShapeID = arcShape->ID;

        arcShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&arcShape->Color, ShapeID, arcShape->ColorDataChanged);

        ColorChanged |= arcShape->ColorDataChanged;
        ShapePropertyChanged |= arcShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < PreviousShapeIDs[BufferID].size() && PreviousShapeIDs[BufferID][instanceCount] == ShapeID) {
            if (ShapePropertyChanged) {
                if (instanceCount < instanceDataArray[BufferID].size()) {
                    instanceDataArray[BufferID][instanceCount] = arcShape->ShapeInstanceData;
                } else {
                    instanceDataArray[BufferID].push_back(arcShape->ShapeInstanceData);
                }
            }

            if (CurrentShapeIDs[BufferID].empty() || CurrentShapeIDs[BufferID].back() != ShapeID) {
                if (instanceCount < CurrentShapeIDs[BufferID].size()) {
                    CurrentShapeIDs[BufferID].resize(instanceCount);
                }
                CurrentShapeIDs[BufferID].push_back(ShapeID);
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        if (CurrentShapeIDs[BufferID].empty() || CurrentShapeIDs[BufferID].back() != ShapeID) {
            CurrentShapeIDs[BufferID].push_back(ShapeID);
        }

        instanceDataArray[BufferID].push_back(arcShape->ShapeInstanceData);
        instanceCount++;
    }

    void Render();
};