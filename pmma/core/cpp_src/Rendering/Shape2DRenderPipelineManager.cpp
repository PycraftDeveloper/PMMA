#include <glad/gl.h>
#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

#include "PMMA_Core.hpp"

using namespace std;

CPP_Shape2D_RenderPipelineManager::CPP_Shape2D_RenderPipelineManager() {
    combined_vertexes.reserve(PMMA::RenderPipelineCore->Shape2D_AverageRenderPipelineManagerSize);
    glGenVertexArrays(1, &vao);
    glGenBuffers(1, &vbo);
    glGenBuffers(1, &ubo);
}

CPP_Shape2D_RenderPipelineManager::~CPP_Shape2D_RenderPipelineManager() {
    glDeleteBuffers(1, &vbo);
    glDeleteVertexArrays(1, &vao);
    glDeleteBuffers(1, &ubo);
}

void CPP_Shape2D_RenderPipelineManager::Reset() {
    OldProbabilityOfDuplicateColor = NewProbabilityOfDuplicateColor / (float)(SamplesOfColor);
    NewProbabilityOfDuplicateColor = 1.0f;
}

GLuint CPP_Shape2D_RenderPipelineManager::GetColorIndex(glm::vec4 Color) {
    SamplesOfColor++;
    if (shape_colors.empty()) {
        shape_colors.emplace_back(Color);
        return 0;
    }

    if (OldProbabilityOfDuplicateColor >= 0.05f) {
        auto it = std::find(shape_colors.begin(), shape_colors.end(), Color);
        if (it != shape_colors.end()) {
            NewProbabilityOfDuplicateColor++;
            return static_cast<GLuint>(std::distance(shape_colors.begin(), it));
        }
    }

    return static_cast<GLuint>(shape_colors.size());
}

void CPP_Shape2D_RenderPipelineManager::AddRenderTarget(const Shape2D_RenderObject& NewObject) {
    if (auto actualPtr = std::get_if<CPP_RadialPolygonShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    } else if (auto actualPtr = std::get_if<CPP_RectangleShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    } else if (auto actualPtr = std::get_if<CPP_PixelShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    } else if (auto actualPtr = std::get_if<CPP_LineShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    } else if (auto actualPtr = std::get_if<CPP_PolygonShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    } else if (auto actualPtr = std::get_if<CPP_ArcShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    } else if (auto actualPtr = std::get_if<CPP_EllipseShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    }
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