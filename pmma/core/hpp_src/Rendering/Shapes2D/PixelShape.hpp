#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Internal/Management/Shape2DRenderPipelineManager.hpp"
#include "Constants.hpp"
#include "NumberFormats.hpp"
#include "Logger.hpp"

class EXPORT CPP_PixelShape {
    public:
        CPP_Logger* Logger;
        CPP_DisplayCoordinateFormat* ShapeCenterFormat;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;

        std::vector<Vertex> Shape2D_RenderPipelineData;

        glm::vec2 ShapeSize;

        uint64_t ID;
        float ColorIndex;

        bool CenterSet = false;
        bool HasAlpha = false;
        bool VertexDataChanged = true;
        bool ColorDataChanged = true;

        CPP_PixelShape();

        ~CPP_PixelShape() {
            delete Logger;
            Logger = nullptr;

            delete ShapeCenterFormat;
            ShapeCenterFormat = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render();

        void InternalRender();
};