#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "NumberFormats.hpp"

class EXPORT CPP_EllipseShape {
    public:
        CPP_DisplayCoordinateFormat* ShapeCentreFormat;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec2 ShapeSize;

        float Rotation = 0;

        uint64_t ID;
        GLuint ColorIndex;
        unsigned int Width = 0;
        unsigned int PointCount = 0;

        bool SizeSet = false;
        bool HasAlpha = false;
        bool Changed = true;

        CPP_EllipseShape();

        ~CPP_EllipseShape() {
            delete ShapeCentreFormat;
            ShapeCentreFormat = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render(float ShapeQuality);

        void InternalRender();

        inline void SetSize(unsigned int* in_size) {
            if (SizeSet && (in_size[0] != ShapeSize.x || in_size[1] != ShapeSize.y)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ShapeSize = glm::vec2(in_size[0], in_size[1]);
            SizeSet = true;
        };

        inline void SetWidth(unsigned int in_width) {
            if (in_width != Width) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Width = in_width;
        };

        inline void SetRotation(float in_rotation) {
            if (in_rotation != Rotation) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline void SetPointCount(unsigned int in_point_count) {
            if (in_point_count != PointCount) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            PointCount = in_point_count;
        }
};