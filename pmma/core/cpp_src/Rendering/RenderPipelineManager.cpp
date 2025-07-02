#include <glad/gl.h>
#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

#include <vector>
#include <chrono>

#include "Rendering/RenderPipelineManager.hpp"
#include "PMMA_Core.hpp"

using namespace std;

CPP_RenderPipelineManager::CPP_RenderPipelineManager() {
    glGenVertexArrays(1, &vao);
    glGenBuffers(1, &vbo);
}

CPP_RenderPipelineManager::~CPP_RenderPipelineManager() {
    glDeleteBuffers(1, &vbo);
    glDeleteVertexArrays(1, &vao);
}

void CPP_RenderPipelineManager::AddRenderTarget(RenderPipelineDataObject* NewObject) {
    std::visit([&](auto* actualPtr) {
        GLuint color_index = shape_colors.size();
        shape_colors.emplace_back(actualPtr->RenderPipelineColorData);

        const auto& vertices = actualPtr->RenderPipelineVertexData;

        //combined_vertexes.reserve(combined_vertexes.size() + vertices.size() + 2);

        // Insert degenerate vertices if this is not the first shape
        if (!combined_vertexes.empty() && vertices.size() >= 2) {
            // Repeat last vertex of previous shape
            combined_vertexes.emplace_back(combined_vertexes.back());

            // Repeat first vertex of new shape
            combined_vertexes.emplace_back(vertices[0]);
        }

        // Add actual shape vertices
        combined_vertexes.insert(combined_vertexes.end(), vertices.begin(), vertices.end());

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

    glUseProgram(PMMA::RenderPipelineCore->shader);

    glBindVertexArray(vao);
    glDrawArrays(GL_TRIANGLE_STRIP, 0, combined_vertexes.size());

    glDeleteBuffers(1, &ubo);
}