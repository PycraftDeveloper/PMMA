#include <glad/gl.h>
#include <glm/glm.hpp>

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
        // Get Color
        // Get Vertex Data

    }, *NewObject);
}

// Notes: Start shape generation into color and vertex arrays, determine if rp compatable (and add with RP_Vertex and RP_Color). RP_Vertex points to vertex array.
// Then here see if color already exists. If it does then merge existing color pointer - otherwise generate a new one and merge that. THEN MAKE SURE TO ADJUST RENDERING
// MODE BUT SHOULD BE MOSTLY DONE. CONSIDER PROJECTIONS.

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
    glBufferData(GL_UNIFORM_BUFFER, 16 * sizeof(glm::vec4), nullptr, GL_STATIC_DRAW);
    glBufferSubData(GL_UNIFORM_BUFFER, 0, shape_colors.size() * sizeof(glm::vec4), shape_colors.data());

    glBindBufferBase(GL_UNIFORM_BUFFER, 0, ubo);

    glUseProgram(shader);

    GLuint block_index = glGetUniformBlockIndex(shader, "ShapeColors");
    glUniformBlockBinding(shader, block_index, 0);

    glBindVertexArray(vao);
    glDrawArrays(GL_TRIANGLES, 0, combined_vertexes.size());
}