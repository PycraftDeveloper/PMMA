#pragma once

#include <vector>
#include <variant>
#include <iostream>

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "Rendering/TextRendererPipelineManager.hpp"
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

        template<typename T>
        inline void AddObject(T* RenderObject, bool RenderPipelineCompatable) {
            if (RenderData.empty()) {
                if (RenderPipelineCompatable) {
                    if (Shape_2D_RenderManagerCache.empty()) {
                        RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                    } else {
                        RenderData.emplace_back(Shape_2D_RenderManagerCache.front());
                        Shape_2D_RenderManagerCache.erase(Shape_2D_RenderManagerCache.begin());
                    }
                } else {
                    RenderData.emplace_back(RenderObject);
                    return;
                }
            }

            auto& lastVariant = RenderData.back();

            if (RenderPipelineCompatable) {
                // Try to extract the CPP_Shape2D_RenderPipelineManager*
                if (CPP_Shape2D_RenderPipelineManager** managerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&lastVariant)) {
                    if ((*managerPtr)->shape_colors.size() < MaxSize) {
                        (*managerPtr)->AddRenderTarget(RenderObject);
                    } else {
                        // Manager full — add new one and push to it
                        if (Shape_2D_RenderManagerCache.empty()) {
                            RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                        } else {
                            RenderData.emplace_back(Shape_2D_RenderManagerCache.front());
                            Shape_2D_RenderManagerCache.erase(Shape_2D_RenderManagerCache.begin());
                        }
                        auto& newVariant = RenderData.back();
                        if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&newVariant)) {
                            (*newManagerPtr)->AddRenderTarget(RenderObject);
                        }
                    }
                } else {
                    // Last item is NOT a CPP_Shape2D_RenderPipelineManager — add a new one
                    if (Shape_2D_RenderManagerCache.empty()) {
                        RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                    } else {
                        RenderData.emplace_back(Shape_2D_RenderManagerCache.front());
                        Shape_2D_RenderManagerCache.erase(Shape_2D_RenderManagerCache.begin());
                    }
                    auto& newVariant = RenderData.back();
                    if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&newVariant)) {
                        (*newManagerPtr)->AddRenderTarget(RenderObject);
                    }
                }
            } else {
                RenderData.emplace_back(RenderObject);
            }
        }

        void AddObject(CPP_TextRenderer* RenderObject);

        inline GLuint Get_Shape2D_ColorIndex(glm::vec4 Color) { // Issue here with colors - trace and diagnose
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
                    return (*managerPtr)->GetColorIndex(Color);
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
                        return (*newManagerPtr)->GetColorIndex(Color);
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
                    return (*newManagerPtr)->GetColorIndex(Color);
                }
            }

            return 0; // fallback
        }
};