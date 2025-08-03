#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "NumberFormats.hpp"

class EXPORT CPP_LineShape {
    public:
        CPP_DisplayCoordinateFormat* ShapeStart;
        CPP_DisplayCoordinateFormat* ShapeEnd;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;

        float Rotation = 0;

        uint64_t ID;
        GLuint ColorIndex;
        unsigned int Width = 1;

        bool HasAlpha = false;
        bool Changed = true;

        CPP_LineShape();

        ~CPP_LineShape() {
            delete ShapeStart;
            delete ShapeEnd;
            delete ColorFormat;

            ShapeStart = nullptr;
            ShapeEnd = nullptr;
            ColorFormat = nullptr;
        }

        void Render(float ShapeQuality);

        void InternalRender();

        inline void SetWidth(unsigned int in_width) {
            if (in_width != Width) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Width = in_width;
        };

        inline unsigned int GetWidth() const {
            return Width;
        }

        inline void SetRotation(float in_rotation) {
            if (in_rotation != Rotation) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline float GetRotation() const {
            return Rotation;
        }
};