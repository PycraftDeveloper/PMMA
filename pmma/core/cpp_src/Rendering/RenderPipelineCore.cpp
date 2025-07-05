#include <iostream>
#include <chrono>

#include <glad/gl.h>
#include <glm/gtc/type_ptr.hpp>

#include "Rendering/RenderPipelineCore.hpp"
#include "Rendering/RenderPipelineManager.hpp"

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
        if (CPP_RenderPipelineManager** newManagerPtr = std::get_if<CPP_RenderPipelineManager*>(&RenderData[i])) {
            delete (*newManagerPtr);
        }
    }
    RenderData.clear();

    glDeleteProgram(shader);
}

void CPP_RenderPipelineCore::Render() {
    glUniformMatrix4fv(glGetUniformLocation(PMMA::RenderPipelineCore->shader, "projection"), 1, GL_FALSE, glm::value_ptr(PMMA::DisplayInstance->GetDisplayProjection()));

    for (auto& item : RenderData) {
        std::visit([](auto* ptr) {
            ptr->InternalRender();
        }, item);
    }
}

void CPP_RenderPipelineCore::Reset() {
}

void CPP_RenderPipelineCore::AddObject(const RenderPipelineDataObject& RenderObject, bool RenderPipelineCompatable) {
    if (RenderData.empty()) {
        if (RenderPipelineCompatable) {
            RenderData.emplace_back(new CPP_RenderPipelineManager());
        } else {
            visit([&](auto* actualPtr) {
                RenderData.emplace_back(actualPtr);
            }, RenderObject);
            return;
        }
    }

    auto& lastVariant = RenderData.back();

    if (RenderPipelineCompatable) {
        // Try to extract the CPP_RenderPipelineManager*
        if (CPP_RenderPipelineManager** managerPtr = std::get_if<CPP_RenderPipelineManager*>(&lastVariant)) {
            if ((*managerPtr)->shape_colors.size() < MaxSize) {
                (*managerPtr)->AddRenderTarget(RenderObject);
            } else {
                // Manager full — add new one and push to it
                RenderData.emplace_back(new CPP_RenderPipelineManager());
                auto& newVariant = RenderData.back();
                if (CPP_RenderPipelineManager** newManagerPtr = std::get_if<CPP_RenderPipelineManager*>(&newVariant)) {
                    (*newManagerPtr)->AddRenderTarget(RenderObject);
                }
            }
        } else {
            // Last item is NOT a CPP_RenderPipelineManager — add a new one
            RenderData.emplace_back(new CPP_RenderPipelineManager());
            auto& newVariant = RenderData.back();
            if (CPP_RenderPipelineManager** newManagerPtr = std::get_if<CPP_RenderPipelineManager*>(&newVariant)) {
                (*newManagerPtr)->AddRenderTarget(RenderObject);
            }
        }
    } else {
        // If not compatible, just add it
        visit([&](auto* actualPtr) {
            RenderData.emplace_back(actualPtr);
        }, RenderObject);
    }
}