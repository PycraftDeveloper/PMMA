#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "NumberFormats.hpp"

class EXPORT CPP_PixelShape {
    public:
        CPP_DisplayCoordinateFormat* ShapeCenterFormat;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec2 ShapeSize;

        uint64_t ID;
        GLuint ColorIndex;

        bool CenterSet = false;
        bool HasAlpha = false;
        bool Changed = true;

        CPP_PixelShape();

        ~CPP_PixelShape() {
            delete ShapeCenterFormat;
            ShapeCenterFormat = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render();

        void InternalRender();
};