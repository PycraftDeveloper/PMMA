#pragma once

#include <vector>
#include <variant>
#include <iostream>

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "Rendering/TextRendererPipelineManager.hpp"
#include "Rendering/TextRenderer.hpp"

using RawRenderObject = std::variant<CPP_Shape2D_RenderPipelineManager*, CPP_TextRendererPipelineManager*, CPP_RadialPolygonShape*, CPP_RectangleShape*, CPP_PixelShape*>;

class CPP_RenderPipelineCore {
    public:
        std::vector<CPP_Shape2D_RenderPipelineManager*> Shape_2D_RenderManagerCache;
        std::vector<CPP_TextRendererPipelineManager*> Text_RenderManagerCache;
        std::vector<RawRenderObject> RenderData;
        unsigned int MaxSize;
        GLuint shader;

        unsigned int Shape2D_AverageRenderPipelineManagerSize = 0;

        CPP_RenderPipelineCore();
        ~CPP_RenderPipelineCore();

        void Render();

        void Reset();

        void AddObject(CPP_RadialPolygonShape* RenderObject, bool RenderPipelineCompatable);
        void AddObject(CPP_RectangleShape* RenderObject, bool RenderPipelineCompatable);
        void AddObject(CPP_PixelShape* RenderObject, bool RenderPipelineCompatable);
        void AddObject(CPP_TextRenderer* RenderObject);

        inline GLuint Get_Shape2D_ColorIndex() {
            if (RenderData.empty()) {
                return 0;
            }

            auto& lastVariant = RenderData.back();
            // Try to extract the CPP_Shape2D_RenderPipelineManager*
            if (CPP_Shape2D_RenderPipelineManager** managerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&lastVariant)) {
                if ((*managerPtr)->shape_colors.size() < MaxSize) {
                    return (GLuint)(*managerPtr)->InsertionIndex;
                } else {
                    return 0;
                }
            } else {
                return 0;
            }
        }
};