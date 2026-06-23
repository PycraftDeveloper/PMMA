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
#include "Rendering/Shapes2D/PixelShape.hpp"
#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"

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
    }

    inline void Add(PMMA::Rendering::TwoD::CPP_Line *lineShape) {
        uintptr_t ShapeID = lineShape->ID;

        lineShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&lineShape->Color, ShapeID, lineShape->ColorDataChanged);

        ColorChanged |= lineShape->ColorDataChanged;
        ShapePropertyChanged |= lineShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < CurrentInstanceData.size() && CurrentShapeIDs[instanceCount] == ShapeID) {
            if (lineShape->ShapePropertyChanged) {
                CurrentInstanceData[instanceCount] = lineShape->ShapeInstanceData;
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        CurrentInstanceData.resize(instanceCount);
        CurrentShapeIDs.resize(instanceCount);
        CurrentInstanceData.push_back(lineShape->ShapeInstanceData);
        CurrentShapeIDs.push_back(ShapeID);
        instanceCount++;
    }

    inline void Add(PMMA::Rendering::TwoD::CPP_Pixel *pixelShape) {
        uintptr_t ShapeID = pixelShape->ID;

        pixelShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&pixelShape->Color, ShapeID, pixelShape->ColorDataChanged);

        ColorChanged |= pixelShape->ColorDataChanged;
        ShapePropertyChanged |= pixelShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < CurrentInstanceData.size() && CurrentShapeIDs[instanceCount] == ShapeID) {
            if (pixelShape->ShapePropertyChanged) {
                CurrentInstanceData[instanceCount] = pixelShape->ShapeInstanceData;
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        CurrentInstanceData.resize(instanceCount);
        CurrentShapeIDs.resize(instanceCount);
        CurrentInstanceData.push_back(pixelShape->ShapeInstanceData);
        CurrentShapeIDs.push_back(ShapeID);
        instanceCount++;
    }

    inline void Add(PMMA::Rendering::TwoD::CPP_Rectangle *rectangleShape) {
        uintptr_t ShapeID = rectangleShape->ID;

        rectangleShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&rectangleShape->Color, ShapeID, rectangleShape->ColorDataChanged);

        ColorChanged |= rectangleShape->ColorDataChanged;
        ShapePropertyChanged |= rectangleShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < CurrentInstanceData.size() && CurrentShapeIDs[instanceCount] == ShapeID) {
            if (rectangleShape->ShapePropertyChanged) {
                CurrentInstanceData[instanceCount] = rectangleShape->ShapeInstanceData;
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        CurrentInstanceData.resize(instanceCount);
        CurrentShapeIDs.resize(instanceCount);
        CurrentInstanceData.push_back(rectangleShape->ShapeInstanceData);
        CurrentShapeIDs.push_back(ShapeID);
        instanceCount++;
    }

    inline void Add(PMMA::Rendering::TwoD::CPP_Ellipse *ellipseShape) {
        uintptr_t ShapeID = ellipseShape->ID;

        ellipseShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&ellipseShape->Color, ShapeID, ellipseShape->ColorDataChanged);

        ColorChanged |= ellipseShape->ColorDataChanged;
        ShapePropertyChanged |= ellipseShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < CurrentInstanceData.size() && CurrentShapeIDs[instanceCount] == ShapeID) {
            if (ellipseShape->ShapePropertyChanged) {
                CurrentInstanceData[instanceCount] = ellipseShape->ShapeInstanceData;
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        CurrentInstanceData.resize(instanceCount);
        CurrentShapeIDs.resize(instanceCount);
        CurrentInstanceData.push_back(ellipseShape->ShapeInstanceData);
        CurrentShapeIDs.push_back(ShapeID);
        instanceCount++;
    }

    inline void Add(PMMA::Rendering::TwoD::CPP_RadialPolygon *radialPolygonShape) {
        uintptr_t ShapeID = radialPolygonShape->ID;

        radialPolygonShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&radialPolygonShape->Color, ShapeID, radialPolygonShape->ColorDataChanged);

        ColorChanged |= radialPolygonShape->ColorDataChanged;
        ShapePropertyChanged |= radialPolygonShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < CurrentInstanceData.size() && CurrentShapeIDs[instanceCount] == ShapeID) {
            if (radialPolygonShape->ShapePropertyChanged) {
                CurrentInstanceData[instanceCount] = radialPolygonShape->ShapeInstanceData;
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        CurrentInstanceData.resize(instanceCount);
        CurrentShapeIDs.resize(instanceCount);
        CurrentInstanceData.push_back(radialPolygonShape->ShapeInstanceData);
        CurrentShapeIDs.push_back(ShapeID);
        instanceCount++;
    }

    inline void Add(PMMA::Rendering::TwoD::CPP_Arc *arcShape) {
        uintptr_t ShapeID = arcShape->ID;

        arcShape->ShapeInstanceData.color_index = ColorTexture.AddColor(&arcShape->Color, ShapeID, arcShape->ColorDataChanged);

        ColorChanged |= arcShape->ColorDataChanged;
        ShapePropertyChanged |= arcShape->ShapePropertyChanged;

        if (instanceCount >= PreviousShapeIDs[BufferID].size()) {
            UsingCache = false;
        }

        if (UsingCache && instanceCount < CurrentInstanceData.size() && CurrentShapeIDs[instanceCount] == ShapeID) {
            if (arcShape->ShapePropertyChanged) {
                CurrentInstanceData[instanceCount] = arcShape->ShapeInstanceData;
            }

            instanceCount++;
            return;
        }

        UsingCache = false;

        CurrentInstanceData.resize(instanceCount);
        CurrentShapeIDs.resize(instanceCount);
        CurrentInstanceData.push_back(arcShape->ShapeInstanceData);
        CurrentShapeIDs.push_back(ShapeID);
        instanceCount++;
    }

    void Render();
};