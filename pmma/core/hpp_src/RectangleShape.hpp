#pragma once
#include "PMMA_Exports.hpp"

#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "RenderPipelineManager.hpp"

class EXPORT CPP_RectangleShape {
    private:

    public:
        unsigned int type = CPP_Constants::TYPE_RECTANGLE_SHAPE;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;
        glm::vec4 RenderPipelineColorData;

        void Render();

        void InternalRender();
};