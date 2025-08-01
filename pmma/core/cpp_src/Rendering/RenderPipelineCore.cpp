#include <glad/gl.h>
#include <glm/gtc/type_ptr.hpp>

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
        } else if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&RenderData[i])) {
            (*newManagerPtr)->Reset();
            Text_RenderManagerCache.emplace_back(*newManagerPtr);
        }
    }
    RenderData.clear();
}

void CPP_RenderPipelineCore::AddObject(CPP_TextRenderer* RenderObject) {
    if (RenderData.empty()) {
        if (Text_RenderManagerCache.empty()) {
            RenderData.emplace_back(new CPP_TextRendererPipelineManager());

            auto& newVariant = RenderData.back();
            if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&newVariant)) {
                (*newManagerPtr)->DelayedSetup(RenderObject->Font, RenderObject->Size);
                (*newManagerPtr)->AddRenderTarget(RenderObject);
                return;
            }
        } else {
            for (unsigned int i = 0; i < Text_RenderManagerCache.size(); i++) {
                if (Text_RenderManagerCache[i]->Font == RenderObject->Font && Text_RenderManagerCache[i]->PixelHeight == RenderObject->Size) {
                    RenderData.emplace_back(Text_RenderManagerCache[i]);
                    Text_RenderManagerCache.erase(Text_RenderManagerCache.begin() + i);
                    auto& newVariant = RenderData.back();
                    if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&newVariant)) {
                        (*newManagerPtr)->AddRenderTarget(RenderObject);
                    }
                    return;
                }
            }

            RenderData.emplace_back(new CPP_TextRendererPipelineManager());

            auto& newVariant = RenderData.back();
            if (CPP_TextRendererPipelineManager** newManagerPtr = std::get_if<CPP_TextRendererPipelineManager*>(&newVariant)) {
                (*newManagerPtr)->DelayedSetup(RenderObject->Font, RenderObject->Size);
                (*newManagerPtr)->AddRenderTarget(RenderObject);
                return;
            }
        }
    }
}