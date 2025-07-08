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

void CPP_Shape2D_RenderPipelineManager::InternalAddRenderTarget(CPP_RadialPolygonShape* TargetPtr) {
    const bool shapeChanged = TargetPtr->Changed;
    const size_t currentIndex = InsertionIndex;
    size_t insertPos = combined_vertexes.size();

    // Handle update or insertion
    if (currentIndex < PreviousRenderContent.size()) {
        const auto& [existingID, existingOffset] = PreviousRenderContent[currentIndex];

        if (TargetPtr->ID == existingID) {
            if (!shapeChanged) {
                // Shape hasn't changed, skip
                InsertionIndex++;
                return;
            } else {
                // Changed shape — erase all after current
                PreviousRenderContent.erase(PreviousRenderContent.begin() + currentIndex, PreviousRenderContent.end());
                combined_vertexes.erase(combined_vertexes.begin() + existingOffset, combined_vertexes.end());
                shape_colors.resize(currentIndex);
                insertPos = existingOffset;
            }
        } else {
            // Mismatch — treat as new insertion
            PreviousRenderContent.erase(PreviousRenderContent.begin() + currentIndex, PreviousRenderContent.end());
            combined_vertexes.erase(combined_vertexes.begin() + existingOffset, combined_vertexes.end());
            shape_colors.resize(currentIndex);
            insertPos = existingOffset;
        }
    }

    Changed = true;

    const glm::vec4 color = TargetPtr->RenderPipelineColorData;

    // Add or replace color
    if (currentIndex < shape_colors.size()) {
        shape_colors[currentIndex] = color;
    } else {
        shape_colors.emplace_back(color);
    }

    const auto& vertices = TargetPtr->RenderPipelineVertexData;

    // Ensure vertex buffer is resized properly
    if (insertPos < combined_vertexes.size()) {
        combined_vertexes.resize(insertPos);
    }

    // Insert degenerate bridge if applicable
    if (currentIndex > 0 && vertices.size() >= 2 && !combined_vertexes.empty()) {
        combined_vertexes.emplace_back(combined_vertexes.back()); // Repeat last of previous
        combined_vertexes.emplace_back(vertices[0]);              // Repeat first of current
    }

    // Insert current shape's vertices
    const size_t shapeStartIndex = combined_vertexes.size();
    combined_vertexes.insert(combined_vertexes.end(), vertices.begin(), vertices.end());

    // Update PreviousRenderContent
    if (currentIndex < PreviousRenderContent.size()) {
        PreviousRenderContent[currentIndex] = { TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex) };
    } else {
        PreviousRenderContent.emplace_back(TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex));
    }

    InsertionIndex++;
}

void CPP_Shape2D_RenderPipelineManager::InternalAddRenderTarget(CPP_RectangleShape* TargetPtr) {
    glm::vec4 Color = TargetPtr->RenderPipelineColorData;
    shape_colors.emplace_back(Color);

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

void CPP_Shape2D_RenderPipelineManager::Reset() {

}

void CPP_Shape2D_RenderPipelineManager::AddRenderTarget(const Shape2D_RenderObject& NewObject) {
    if (auto actualPtr = std::get_if<CPP_RadialPolygonShape*>(&NewObject)) {
        InternalAddRenderTarget(*actualPtr);
    } else if (auto actualPtr = std::get_if<CPP_RectangleShape*>(&NewObject)) {
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