#include <glad/gl.h>
#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

#include <vector>

#include "RenderPipelineManager.hpp"
#include "PMMA_Core.hpp"

using namespace std;

CPP_RenderPipelineManager::CPP_RenderPipelineManager() {
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

    glGenVertexArrays(1, &vao);
    glGenBuffers(1, &vbo);
}

CPP_RenderPipelineManager::~CPP_RenderPipelineManager() {
}

void CPP_RenderPipelineManager::AddRenderTarget(RenderPipelineDataObject* NewObject) {
    std::visit([&](auto* actualPtr) {
        GLuint color_index = shape_colors.size();
        shape_colors.emplace_back(actualPtr->ColorData[0]);

        const auto& vertices = actualPtr->VertexData;

        // Insert degenerate vertices if this is not the first shape
        if (!combined_vertexes.empty() && vertices.size() >= 2) {
            // Repeat last vertex of previous shape
            combined_vertexes.push_back(combined_vertexes.back());

            // Repeat first vertex of new shape
            combined_vertexes.push_back({vertices[0], color_index});
        }

        // Add actual shape vertices
        for (const auto& vertex : vertices) {
            combined_vertexes.push_back({vertex, color_index});
        }

    }, *NewObject);
}

void CPP_RenderPipelineManager::InternalRender() {
    glBindVertexArray(vao);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, combined_vertexes.size() * sizeof(Vertex), combined_vertexes.data(), GL_STATIC_DRAW);

    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(Vertex), (void*)0);

    glEnableVertexAttribArray(1);
    glVertexAttribIPointer(1, 1, GL_UNSIGNED_INT, sizeof(Vertex), (void*)offsetof(Vertex, shape_id));

    GLuint ubo;
    glGenBuffers(1, &ubo);
    glBindBuffer(GL_UNIFORM_BUFFER, ubo);
    glBufferData(GL_UNIFORM_BUFFER, shape_colors.size() * sizeof(glm::vec4), nullptr, GL_STATIC_DRAW);
    glBufferSubData(GL_UNIFORM_BUFFER, 0, shape_colors.size() * sizeof(glm::vec4), shape_colors.data());

    glBindBufferBase(GL_UNIFORM_BUFFER, 0, ubo);

    glUseProgram(shader);
    glUniformMatrix4fv(glGetUniformLocation(shader, "projection"), 1, GL_FALSE, glm::value_ptr(PMMA::DisplayInstance->GetDisplayProjection()));

    GLuint block_index = glGetUniformBlockIndex(shader, "ShapeColors");
    glUniformBlockBinding(shader, block_index, 0);

    glBindVertexArray(vao);
    glDrawArrays(GL_TRIANGLE_STRIP, 0, combined_vertexes.size());
}