#include <glm/gtc/type_ptr.hpp>
#include <bx/math.h>

#include "PMMA_Core.hpp"

using namespace std;

CPP_RenderPipelineCore::CPP_RenderPipelineCore() {
    string Shape2D_RenderPipelineShaderPath = PMMA_Registry::PMMA_Location
        + PMMA_Registry::PathSeparator + "shaders"
        + PMMA_Registry::PathSeparator + "shape_2D_render_pipeline";

    Shape2D_RenderPipelineShader = new CPP_Shader();
    Shape2D_RenderPipelineShader->LoadShaderFromFolder(Shape2D_RenderPipelineShaderPath, true);

    OrthDisplayProj = bgfx::createUniform("OrthDisplayProj", bgfx::UniformType::Mat4);

    const bgfx::Caps* caps = bgfx::getCaps();
    // unsigned int MaxSize;
    MaxWidth = caps->limits.maxTextureSize;
    MaxSize = static_cast<uint64_t>(caps->limits.maxTextureSize) * caps->limits.maxTextureSize;
}

CPP_RenderPipelineCore::~CPP_RenderPipelineCore() {
    for (unsigned int i = 0; i < RenderData.size(); ++i) {
        if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&RenderData[i])) {
            delete (*newManagerPtr);
        } else if (CPP_TextRenderPipelineManager** newManagerPtr = std::get_if<CPP_TextRenderPipelineManager*>(&RenderData[i])) {
            delete (*newManagerPtr);
        }
    }
    RenderData.clear();

    if (Shape2D_RenderPipelineShader) {
        delete Shape2D_RenderPipelineShader;
        Shape2D_RenderPipelineShader = nullptr;
    }

    if (bgfx::isValid(OrthDisplayProj)) {
        bgfx::destroy(OrthDisplayProj);
    }
}

void CPP_RenderPipelineCore::Render() {
    float proj[16];
    PMMA_Core::DisplayInstance->GetDisplayProjection(proj);
    bgfx::setUniform(OrthDisplayProj, proj);

    for (auto& item : RenderData) {
        std::visit([](auto* ptr) {
            ptr->InternalRender();
        }, item);
    }
}

void CPP_RenderPipelineCore::Reset() {
    for (unsigned int i = 0; i < Shape_2D_RenderManagerCache.size(); ++i) {
        delete Shape_2D_RenderManagerCache[i];
    }
    Shape_2D_RenderManagerCache.clear();

    for (unsigned int i = 0; i < Text_RenderManagerCache.size(); ++i) {
        delete Text_RenderManagerCache[i];
    }
    Text_RenderManagerCache.clear();

    for (unsigned int i = 0; i < RenderData.size(); ++i) {
        if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&RenderData[i])) {
            (*newManagerPtr)->Reset();
            Shape_2D_RenderManagerCache.emplace_back(*newManagerPtr);
        } else if (CPP_TextRenderPipelineManager** newManagerPtr = std::get_if<CPP_TextRenderPipelineManager*>(&RenderData[i])) {
            (*newManagerPtr)->Reset();
            Text_RenderManagerCache.emplace_back(*newManagerPtr);
        }
    }
    RenderData.clear();
}

void CPP_RenderPipelineCore::Add_Text_Object(CPP_TextRenderer* RenderObject) {
    if (RenderData.empty()) {
        if (Text_RenderManagerCache.empty()) {
            RenderData.emplace_back(new CPP_TextRenderPipelineManager());

            auto& manager = *std::get<CPP_TextRenderPipelineManager*>(RenderData.back());
            manager.DelayedSetup(RenderObject->Font, RenderObject->Size);
            manager.AddRenderTarget(RenderObject);
            return;
        } else {
            for (unsigned int i = 0; i < Text_RenderManagerCache.size(); i++) {
                if (Text_RenderManagerCache[i]->FontPath == RenderObject->Font && Text_RenderManagerCache[i]->PixelHeight == RenderObject->Size) {
                    RenderData.emplace_back(Text_RenderManagerCache[i]);
                    Text_RenderManagerCache.erase(Text_RenderManagerCache.begin() + i);

                    auto& manager = *std::get<CPP_TextRenderPipelineManager*>(RenderData.back());
                    manager.AddRenderTarget(RenderObject);

                    return;
                }
            }

            RenderData.emplace_back(new CPP_TextRenderPipelineManager());

            auto& manager = *std::get<CPP_TextRenderPipelineManager*>(RenderData.back());
            manager.DelayedSetup(RenderObject->Font, RenderObject->Size);
            manager.AddRenderTarget(RenderObject);
            return;
        }
    }
}