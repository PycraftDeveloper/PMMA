#include <glad/gl.h>
#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

#include <vector>
#include <chrono>
#include <iostream>

#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "PMMA_Core.hpp"

using namespace std;

CPP_Shape2D_RenderPipelineManager::CPP_Shape2D_RenderPipelineManager() {
    combined_vertexes.reserve(PMMA::RenderPipelineCore->Shape2D_AverageRenderPipelineManagerSize);
    glGenVertexArrays(1, &vao);
    glGenBuffers(1, &vbo);
}

CPP_Shape2D_RenderPipelineManager::~CPP_Shape2D_RenderPipelineManager() {
    glDeleteBuffers(1, &vbo);
    glDeleteVertexArrays(1, &vao);
}

void CPP_Shape2D_RenderPipelineManager::InternalAddRenderTarget(CPP_RadialPolygonShape* TargetPtr) {
    glm::vec4 Color = TargetPtr->RenderPipelineColorData;
    shape_colors.emplace_back(Color);
    if (Color.w != 1) {
        HasAlpha = true;
    }

    const auto& vertices = TargetPtr->RenderPipelineVertexData;

    // Insert degenerate vertices if this is not the first shape
    if (!combined_vertexes.empty() && vertices.size() >= 2) {
        // Repeat last vertex of previous shape
        combined_vertexes.emplace_back(combined_vertexes.back());

        // Repeat first vertex of new shape
        combined_vertexes.emplace_back(vertices[0]);
    }

    combined_vertexes.insert(combined_vertexes.end(), vertices.begin(), vertices.end());
}

void CPP_Shape2D_RenderPipelineManager::InternalAddRenderTarget(CPP_RectangleShape* TargetPtr) {
    glm::vec4 Color = TargetPtr->RenderPipelineColorData;
    shape_colors.emplace_back(Color);
    if (Color.w != 1) {
        HasAlpha = true;
    }

    const auto& vertices = TargetPtr->RenderPipelineVertexData;

    // Insert degenerate vertices if this is not the first shape
    if (!combined_vertexes.empty() && vertices.size() >= 2) {
        // Repeat last vertex of previous shape
        combined_vertexes.emplace_back(combined_vertexes.back());

        // Repeat first vertex of new shape
        combined_vertexes.emplace_back(vertices[0]);
    }

    combined_vertexes.insert(combined_vertexes.end(), vertices.begin(), vertices.end());
}

void CPP_Shape2D_RenderPipelineManager::AddRenderTarget(const Shape2D_RenderObject& NewObject) {
    if (auto actualPtr = std::get_if<CPP_RadialPolygonShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    } else if (auto actualPtr = std::get_if<CPP_RectangleShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    }
}

void CPP_Shape2D_RenderPipelineManager::InternalRender() {
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

    if (HasAlpha) {
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    }

    glUseProgram(PMMA::RenderPipelineCore->shader);

    glBindVertexArray(vao);

    glDrawArrays(GL_TRIANGLE_STRIP, 0, combined_vertexes.size());
    //glDrawArrays(GL_POINTS, 0, combined_vertexes.size());

    glDeleteBuffers(1, &ubo);

    if (HasAlpha) {
        glDisable(GL_BLEND);
    }
}