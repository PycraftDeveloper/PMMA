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

    inline float PackValues(uint16_t value_one, uint16_t value_two) {
        uint32_t bits = (uint32_t(value_two) << 16) | uint32_t(value_one);
        float packed;
        std::memcpy(&packed, &bits, sizeof(float));
        return packed;
    }

    inline float PackValues(uint8_t value_one, uint8_t value_two, uint8_t value_three) {
        uint32_t bits = (static_cast<uint32_t>(value_three) << 24) |
                        (static_cast<uint32_t>(value_two) << 16) |
                        (static_cast<uint32_t>(value_one) << 8); // Leaving lowest 8 bits empty/0

        float packed;
        std::memcpy(&packed, &bits, sizeof(float));
        return packed;
    }

    void Add(CPP_LineShape *lineShape) {
        instanceCount++;

        InstanceData instance;
        uint16_t start_position[2], end_position[2];
        lineShape->ShapeStart->Get(start_position);
        lineShape->ShapeEnd->Get(end_position);

        float width = abs((float)end_position[0] - start_position[0]);
        float height = abs((float)end_position[1] - start_position[1]);

        if (width == 0.0f)
            width = 1.0f;
        if (height == 0.0f)
            height = 1.0f;

        float rel_start_x = (start_position[0] <= end_position[0]) ? 0.0f : 1.0f;
        float rel_end_x = (start_position[0] <= end_position[0]) ? 1.0f : 0.0f;

        float rel_start_y = (start_position[1] <= end_position[1]) ? 0.0f : 1.0f;
        float rel_end_y = (start_position[1] <= end_position[1]) ? 1.0f : 0.0f;

        instance.position = PackValues((start_position[0] + end_position[0]) / 2, (start_position[1] + end_position[1]) / 2);
        instance.size = PackValues((uint16_t)width, (uint16_t)height);
        instance.point_count_gradient_type = PackValues(0, 0);
        instance.rotation_shape_property = PackValues(lineShape->GetRotation() * 182, 0);

        uint8_t Color[4];
        lineShape->Color->Get_RGBA(Color);
        instance.color_index = ColorTexture.AddColor(Color);
        instance.shape_type_width = PackValues(3, lineShape->GetWidth());
        instance.texture_position = PackValues(0, 0);
        instance.texture_size = PackValues(0, 0);

        instance.line_start = PackValues(rel_start_x, rel_start_y);
        instance.line_end = PackValues(rel_end_x, rel_end_y);

        ColorChanged |= lineShape->ColorDataChanged;
        ShapePropertyChanged |= lineShape->ShapePropertyChanged;

        instanceDataArray[BufferID].push_back(instance);
    }

    void Add(CPP_RadialPolygonShape *radialPolygonShape) {
        instanceCount++;

        InstanceData instance;
        uint16_t start_position[2];
        radialPolygonShape->ShapeCenter->Get(start_position);
        unsigned int radius = radialPolygonShape->GetRadius() * 2;

        // Existing packing logic
        instance.position = PackValues(start_position[0], start_position[1]);
        instance.size = PackValues((uint16_t)radius, (uint16_t)radius);
        instance.point_count_gradient_type = PackValues(0, 0);
        instance.rotation_shape_property = PackValues(radialPolygonShape->GetRotation() * 182, 0);

        uint8_t Color[4];
        radialPolygonShape->Color->Get_RGBA(Color);
        instance.color_index = ColorTexture.AddColor(Color);
        instance.shape_type_width = PackValues(0, radialPolygonShape->GetWidth());
        instance.texture_position = PackValues(0, 0);
        instance.texture_size = PackValues(0, 0);

        ColorChanged |= radialPolygonShape->ColorDataChanged;
        ShapePropertyChanged |= radialPolygonShape->ShapePropertyChanged;

        instanceDataArray[BufferID].push_back(instance);
    }

    void Render();
};