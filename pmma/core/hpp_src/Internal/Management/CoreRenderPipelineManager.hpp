#pragma once

#include <iostream>
#include <variant>
#include <vector>

#include <bgfx/bgfx.h>

#include "Internal/Management/Shape2DRenderPipelineManager.hpp"
#include "Internal/Management/TextRenderPipelineManager.hpp"
#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/TextRenderer.hpp"

using RawRenderObject = std::variant<
    CPP_Shape2D_RenderPipelineManager *,
    CPP_TextRenderPipelineManager *,
    CPP_RadialPolygonShape *,
    CPP_RectangleShape *,
    CPP_PixelShape *,
    CPP_LineShape *,
    CPP_PolygonShape *,
    CPP_EllipseShape *,
    CPP_ArcShape *>;

class CPP_Shader;

class CPP_RenderPipelineCore {
public:
    std::vector<CPP_Shape2D_RenderPipelineManager *> Shape_2D_RenderManagerCache;
    std::vector<CPP_TextRenderPipelineManager *> Text_RenderManagerCache;
    std::vector<RawRenderObject> RenderData;

    bgfx::UniformHandle OrthDisplayProj;

    CPP_Shader *Shape2D_RenderPipelineShader = nullptr;

    uint64_t MaxSize;
    uint32_t MaxWidth;

    CPP_RenderPipelineCore();
    ~CPP_RenderPipelineCore();

    void Render();

    void Reset();

    template <typename T>
    inline void Add_2D_Shape_Object(T *RenderObject, bool RenderPipelineCompatable) {
        if (RenderData.empty()) {
            if (RenderPipelineCompatable) {
                if (!Shape_2D_RenderManagerCache.empty()) {
                    RenderData.emplace_back(Shape_2D_RenderManagerCache.front());
                    Shape_2D_RenderManagerCache.erase(Shape_2D_RenderManagerCache.begin());
                } else {
                    RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                }
            } else {
                RenderData.emplace_back(RenderObject);
                return;
            }
        }

        if (RenderPipelineCompatable) {
            auto &manager = *std::get<CPP_Shape2D_RenderPipelineManager *>(RenderData.back());
            manager.AddRenderTarget(RenderObject);
        } else {
            RenderData.emplace_back(RenderObject);
        }
    }

    void Add_Text_Object(CPP_TextRenderer *RenderObject);
};