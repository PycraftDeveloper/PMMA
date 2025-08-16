#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "NumberFormats.hpp"
#include "Logger.hpp"

class EXPORT CPP_LineShape {
    public:
        CPP_Logger* Logger;
        CPP_DisplayCoordinateFormat* ShapeStart;
        CPP_DisplayCoordinateFormat* ShapeEnd;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> Shape2D_RenderPipelineData;

        float Rotation = 0;

        uint64_t ID;
        GLuint ColorIndex;
        unsigned int Width = 1;

        bool HasAlpha = false;
        bool Changed = true;

        CPP_LineShape();

        ~CPP_LineShape() {
            delete Logger;
            Logger = nullptr;

            delete ShapeStart;
            ShapeStart = nullptr;

            delete ShapeEnd;
            ShapeEnd = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render();

        void InternalRender();

        inline void SetWidth(unsigned int in_width) {
            if (in_width != Width) {
                Changed = true;
                Shape2D_RenderPipelineData.clear();
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
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline float GetRotation() const {
            return Rotation;
        }
};