#include <iostream>
#include <chrono>

#include <glad/gl.h>
#include <glm/gtc/type_ptr.hpp>

#include "Rendering/RenderPipelineCore.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "Rendering/TextRendererPipelineManager.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_RenderPipelineCore::CPP_RenderPipelineCore() {
    GLint max_block_size;
    glGetIntegerv(GL_MAX_UNIFORM_BLOCK_SIZE, &max_block_size);
    MaxSize = (unsigned int)max_block_size / sizeof(glm::vec4);

    string vertex_shader_path[] = {"shaders", "render_pipeline", "vertex_shader.glsl"};
    string fragment_shader_path[] = {"shaders", "render_pipeline", "fragment_shader.glsl"};

    string vertex_shader = PMMA::PMMA_Location;
    for (const auto& part : vertex_shader_path) {
        vertex_shader += PMMA::PathSeparator + part;
    }

    string fragment_shader = PMMA::PMMA_Location;
    for (const auto& part : fragment_shader_path) {
        fragment_shader += PMMA::PathSeparator + part;
    }

    CPP_Shader ShaderObject;
    shader = ShaderObject.CreateShaderProgram(vertex_shader, fragment_shader);

    GLuint block_index = glGetUniformBlockIndex(shader, "ShapeColors");
    glUniformBlockBinding(shader, block_index, 0);
}

CPP_RenderPipelineCore::~CPP_RenderPipelineCore() {
    for (unsigned int i = 0; i < RenderData.size(); ++i) {
        if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&RenderData[i])) {
            delete (*newManagerPtr);
        } else if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&RenderData[i])) {
            delete (*newManagerPtr);
        }
    }
    RenderData.clear();

    glDeleteProgram(shader);
}

void CPP_RenderPipelineCore::Render() {
    glUniformMatrix4fv(glGetUniformLocation(PMMA::RenderPipelineCore->shader, "projection"), 1, GL_FALSE, glm::value_ptr(PMMA::DisplayInstance->GetDisplayProjection()));

    unsigned int Shape2D_RenderPipelineTotalSize = 0;
    unsigned int Shape2D_Samples = 0;

    for (auto& item : RenderData) {
        if (CPP_Shape2D_RenderPipelineManager** managerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&item)) {
            Shape2D_RenderPipelineTotalSize += (*managerPtr)->combined_vertexes.size();
            Shape2D_Samples++;
        }
        std::visit([](auto* ptr) {
            ptr->InternalRender();
        }, item);
    }

    if (Shape2D_Samples > 0) {
        unsigned int Average = Shape2D_RenderPipelineTotalSize / Shape2D_Samples;

        if (Average > Shape2D_AverageRenderPipelineManagerSize * 1.1f) {
            Shape2D_AverageRenderPipelineManagerSize = Average;
        } else if (Average < Shape2D_AverageRenderPipelineManagerSize * 0.9f) {
            Shape2D_AverageRenderPipelineManagerSize = Average;
        }
    }
}

void CPP_RenderPipelineCore::Reset() {
    for (unsigned int i = 0; i < RenderData.size(); ++i) {
        if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&RenderData[i])) {
            delete (*newManagerPtr);
        } else if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&RenderData[i])) {
            delete (*newManagerPtr);
        }
    }
    RenderData.clear();
}

void CPP_RenderPipelineCore::AddObject(CPP_RadialPolygonShape* RenderObject, bool RenderPipelineCompatable) {
    if (RenderData.empty()) {
        if (RenderPipelineCompatable) {
            RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
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
                RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                auto& newVariant = RenderData.back();
                if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&newVariant)) {
                    (*newManagerPtr)->AddRenderTarget(RenderObject);
                }
            }
        } else {
            // Last item is NOT a CPP_Shape2D_RenderPipelineManager — add a new one
            RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
            auto& newVariant = RenderData.back();
            if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&newVariant)) {
                (*newManagerPtr)->AddRenderTarget(RenderObject);
            }
        }
    } else {
        RenderData.emplace_back(RenderObject);
    }
}

void CPP_RenderPipelineCore::AddObject(CPP_RectangleShape* RenderObject, bool RenderPipelineCompatable) {
    if (RenderData.empty()) {
        if (RenderPipelineCompatable) {
            RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
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
                RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
                auto& newVariant = RenderData.back();
                if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&newVariant)) {
                    (*newManagerPtr)->AddRenderTarget(RenderObject);
                }
            }
        } else {
            // Last item is NOT a CPP_Shape2D_RenderPipelineManager — add a new one
            RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
            auto& newVariant = RenderData.back();
            if (CPP_Shape2D_RenderPipelineManager** newManagerPtr = std::get_if<CPP_Shape2D_RenderPipelineManager*>(&newVariant)) {
                (*newManagerPtr)->AddRenderTarget(RenderObject);
            }
        }
    } else {
        RenderData.emplace_back(RenderObject);
    }
}

void CPP_RenderPipelineCore::AddObject(CPP_TextRenderer* RenderObject) {
    if (RenderData.empty()) {
        RenderData.emplace_back(new CPP_TextRendererPipelineManager());
        auto& newVariant = RenderData.back();
        if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&newVariant)) {
            (*newManagerPtr)->DelayedSetup(RenderObject->Font, RenderObject->Size);
            (*newManagerPtr)->AddRenderTarget(RenderObject);
            return;
        }
    }

    auto& lastVariant = RenderData.back();

    // Try to extract the CPP_TextRendererPipelineManager*
    if (CPP_TextRendererPipelineManager** managerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&lastVariant)) {
        if ((*managerPtr)->Font == RenderObject->Font && (*managerPtr)->PixelHeight == RenderObject->Size) {
            (*managerPtr)->AddRenderTarget(RenderObject);
        } else {
            // Manager full — add new one and push to it
            RenderData.emplace_back(new CPP_TextRendererPipelineManager());
            auto& newVariant = RenderData.back();
            if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&newVariant)) {
                (*newManagerPtr)->DelayedSetup(RenderObject->Font, RenderObject->Size);
                (*newManagerPtr)->AddRenderTarget(RenderObject);
            }
        }
    } else {
        // Last item is NOT a CPP_Shape2D_RenderPipelineManager — add a new one
        RenderData.emplace_back(new CPP_TextRendererPipelineManager());
        auto& newVariant = RenderData.back();
        if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&newVariant)) {
            (*newManagerPtr)->DelayedSetup(RenderObject->Font, RenderObject->Size);
            (*newManagerPtr)->AddRenderTarget(RenderObject);
        }
    }
}