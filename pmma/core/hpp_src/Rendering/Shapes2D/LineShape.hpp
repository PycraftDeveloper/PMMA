#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"

class EXPORT CPP_LineShape {
    public:
        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec4 RenderPipelineColorData;
        glm::vec2 StartPosition;
        glm::vec2 EndPosition;

        float Rotation = 0;

        uint64_t ID;
        GLuint ColorIndex;
        unsigned int Width = 1;

        bool ColorSet = false;
        bool StartPositionSet = false;
        bool EndPositionSet = false;
        bool UsingGradients = false;
        bool HasAlpha = false;
        bool Changed = true;

        CPP_LineShape();

        void Render(float ShapeQuality);

        void InternalRender();

        inline void SetColor(float* in_color, unsigned int size) {
            UsingGradients = size > 4; // (determine if multiple colors inputted)

            std::vector<glm::vec4> NewColorData;

            HasAlpha = false;
            for (unsigned int i = 0; i < size; i += 4) { // Color will be in form rgba
                NewColorData.push_back(glm::vec4(in_color[i], in_color[i + 1], in_color[i + 2], in_color[i + 3]));
                if (in_color[i + 3] != 1.0f) {
                    HasAlpha = true;
                }
            }

            if (ColorSet && (size != NewColorData.size() * 4 || ColorData.size() != NewColorData.size() || !std::equal(ColorData.begin(), ColorData.end(), NewColorData.begin()))) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ColorSet = true;
            ColorData = NewColorData;
        };

        inline void SetStartPosition(unsigned int* in_start_position) {
            if (StartPositionSet && (in_start_position[0] != StartPosition.x || in_start_position[1] != StartPosition.y)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            StartPosition = glm::vec2(in_start_position[0], in_start_position[1]);
            StartPositionSet = true;
        };

        inline void SetEndPosition(unsigned int* in_end_position) {
            if (EndPositionSet && (in_end_position[0] != EndPosition.x || in_end_position[1] != EndPosition.y)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            EndPosition = glm::vec2(in_end_position[0], in_end_position[1]);
            EndPositionSet = true;
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
};