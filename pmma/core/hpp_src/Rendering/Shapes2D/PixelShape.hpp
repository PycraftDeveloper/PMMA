#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"

class EXPORT CPP_PixelShape {
    public:
        std::vector<glm::vec2> VertexData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec4 RenderPipelineColorData;
        glm::vec2 ShapeCentre;
        glm::vec2 ShapeSize;

        uint64_t ID;
        GLuint ColorIndex;

        bool ColorSet = false;
        bool CentreSet = false;
        bool HasAlpha = false;
        bool Changed = true;

        CPP_PixelShape();

        void Render();

        void InternalRender();

        inline void SetColor(float* in_color) {
            glm::vec4 NewColorData = glm::vec4(in_color[0], in_color[1], in_color[2], in_color[3]);
            HasAlpha = (NewColorData.w != 1);

            if (ColorSet && (
                    RenderPipelineColorData.x == in_color[0] ||
                    RenderPipelineColorData.y == in_color[1] ||
                    RenderPipelineColorData.z == in_color[2] ||
                    RenderPipelineColorData.z == in_color[3])) {

                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ColorSet = true;
            RenderPipelineColorData = NewColorData;
        };

        inline void SetCentre(unsigned int* in_position) {
            if (CentreSet && (in_position[0] != ShapeCentre.x || in_position[1] != ShapeCentre.y)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ShapeCentre = glm::vec2(in_position[0], in_position[1]);
            CentreSet = true;
        };
};