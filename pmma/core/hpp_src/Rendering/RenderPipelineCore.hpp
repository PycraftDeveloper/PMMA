#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <variant>
#include <iostream>

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/RenderPipelineManager.hpp"

using RenderDataObject = std::variant<CPP_RenderPipelineManager*, CPP_RadialPolygonShape*, CPP_RectangleShape*>;

class EXPORT CPP_RenderPipelineCore {
    public:
        std::vector<RenderDataObject> RenderData;
        unsigned int MaxSize;
        GLuint shader;

        unsigned int AverageRenderPipelineManagerSize = 0;

        CPP_RenderPipelineCore();
        ~CPP_RenderPipelineCore();

        void Render();

        void Reset();

        void AddObject(const RenderPipelineDataObject& RenderObject, bool RenderPipelineCompatable=true);

        inline GLuint GetColorIndex() {
            if (RenderData.empty()) {
                return 0;
            }

            auto& lastVariant = RenderData.back();
            // Try to extract the CPP_RenderPipelineManager*
            if (CPP_RenderPipelineManager** managerPtr = std::get_if<CPP_RenderPipelineManager*>(&lastVariant)) {
                if ((*managerPtr)->shape_colors.size() < MaxSize) {
                    return (*managerPtr)->shape_colors.size();
                } else {
                    return 0;
                }
            } else {
                return 0;
            }
        }
};