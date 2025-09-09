#pragma once

#include <vector>
#include <variant>
#include <iostream>

#include <bgfx/bgfx.h>

#include "Internal/Management/Shape2DRenderPipelineManager.hpp"
#include "Internal/Management/TextRenderPipelineManager.hpp"
#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/TextRenderer.hpp"

using RawRenderObject = std::variant<
    CPP_Shape2D_RenderPipelineManager*,
    CPP_TextRendererPipelineManager*,
    CPP_RadialPolygonShape*,
    CPP_RectangleShape*,
    CPP_PixelShape*,
    CPP_LineShape*,
    CPP_PolygonShape*,
    CPP_EllipseShape*,
    CPP_ArcShape*>;

class CPP_Shader;

class CPP_RenderPipelineCore {
    public:
        std::vector<CPP_Shape2D_RenderPipelineManager*> Shape_2D_RenderManagerCache;
        std::vector<CPP_TextRendererPipelineManager*> Text_RenderManagerCache;
        std::vector<RawRenderObject> RenderData;

        bgfx::UniformHandle u_proj;

        CPP_Shader* Shape2D_RenderPipelineShader = nullptr;

        uint64_t MaxSize;
        uint32_t MaxWidth;

        CPP_RenderPipelineCore();
        ~CPP_RenderPipelineCore();

        void Render();

        void Reset();

        template<typename T>
        inline void AddObject(T* RenderObject, bool RenderPipelineCompatable, bool ColorIndexChanged) {
            if (RenderData.empty()) {
                if (!RenderPipelineCompatable) {
                    RenderData.emplace_back(RenderObject);
                    return;
                }
            }

            auto& lastVariant = RenderData.back();

            if (RenderPipelineCompatable) {
                // Try to extract the CPP_Shape2D_RenderPipelineManager*
                if (CPP_Shape2D_RenderPipelineManager** managerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&lastVariant)) {
                    (*managerPtr)->AddRenderTarget(RenderObject, ColorIndexChanged);
                }
            } else {
                RenderData.emplace_back(RenderObject);
            }
        }

        void AddObject(CPP_TextRenderer* RenderObject);

        inline GLuint Shape2D_GetColorIndex(glm::vec4 Color, unsigned int ShapeID) {
            if (RenderData.empty()) {
                if (!Shape_2D_RenderManagerCache.empty()) {
                    RenderData.emplace_back(Shape_2D_RenderManagerCache.front());
                    Shape_2D_RenderManagerCache.erase(Shape_2D_RenderManagerCache.begin());
                } else {
                    RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                }
            }

            auto& lastVariant = RenderData.back();
            if (CPP_Shape2D_RenderPipelineManager** managerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&lastVariant)) {
                if ((*managerPtr)->shape_colors.size() < MaxSize) {
                    return (*managerPtr)->GetColorIndex(Color, ShapeID);
                } else {
                    // Too many vertexes — need a new manager
                    if (!Shape_2D_RenderManagerCache.empty()) {
                        RenderData.emplace_back(Shape_2D_RenderManagerCache.front());
                        Shape_2D_RenderManagerCache.erase(Shape_2D_RenderManagerCache.begin());
                    } else {
                        RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                    }

                    auto& newVariant = RenderData.back();
                    if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&newVariant)) {
                        return (*newManagerPtr)->GetColorIndex(Color, ShapeID);
                    }
                }
            } else {
                // Last RenderData item is not a manager — insert new manager
                if (!Shape_2D_RenderManagerCache.empty()) {
                    RenderData.emplace_back(Shape_2D_RenderManagerCache.front());
                    Shape_2D_RenderManagerCache.erase(Shape_2D_RenderManagerCache.begin());
                } else {
                    RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                }

                auto& newVariant = RenderData.back();
                if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&newVariant)) {
                    return (*newManagerPtr)->GetColorIndex(Color, ShapeID);
                }
            }

            return 0; // fallback
        }
};