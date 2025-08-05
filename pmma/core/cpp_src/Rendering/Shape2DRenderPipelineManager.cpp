#include <glad/gl.h>
#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

#include "PMMA_Core.hpp"

using namespace std;

CPP_Shape2D_RenderPipelineManager::CPP_Shape2D_RenderPipelineManager() {
    glGenVertexArrays(1, &vao);
    glGenBuffers(1, &vbo);
    glGenBuffers(1, &ubo);
}

CPP_Shape2D_RenderPipelineManager::~CPP_Shape2D_RenderPipelineManager() {
    glDeleteBuffers(1, &vbo);
    glDeleteVertexArrays(1, &vao);
    glDeleteBuffers(1, &ubo);
}

void CPP_Shape2D_RenderPipelineManager::InternalRender() {
    if (Changed) {
        HasAlpha = false;
        for (const auto& c : shape_colors) {
            if (c.w < 1.0f) {
                HasAlpha = true;
                break;
            }
        }

        glBindVertexArray(vao);
        glBindBuffer(GL_ARRAY_BUFFER, vbo);
        glBufferData(GL_ARRAY_BUFFER, combined_vertexes.size() * sizeof(Vertex), combined_vertexes.data(), GL_STATIC_DRAW);

        glEnableVertexAttribArray(0);
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(Vertex), (void*)0);

        glEnableVertexAttribArray(1);
        glVertexAttribIPointer(1, 1, GL_UNSIGNED_INT, sizeof(Vertex), (void*)offsetof(Vertex, shape_id));

        glBindBuffer(GL_UNIFORM_BUFFER, ubo);
        glBufferData(GL_UNIFORM_BUFFER, shape_colors.size() * sizeof(glm::vec4), nullptr, GL_STATIC_DRAW);
        glBufferSubData(GL_UNIFORM_BUFFER, 0, shape_colors.size() * sizeof(glm::vec4), shape_colors.data());

        glBindBufferBase(GL_UNIFORM_BUFFER, 0, ubo);
    }

    if (HasAlpha) {
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    }

    glUseProgram(PMMA::RenderPipelineCore->shader);

    glBindVertexArray(vao);

    glDrawArrays(GL_TRIANGLE_STRIP, 0, combined_vertexes.size());

    if (HasAlpha) {
        glDisable(GL_BLEND);
    }

    InsertionIndex = 0;
}