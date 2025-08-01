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

void CPP_Shape2D_RenderPipelineManager::Reset() {
    for (auto it = ColorSlotID.begin(); it != ColorSlotID.end(); ) {
        if (SeenThisFrame.count(it->first) == 0) {
            FreeSlots.push_back(it->second);
            it = ColorSlotID.erase(it);
        } else {
            ++it;
        }
    }

    SeenThisFrame.clear();
}

GLuint CPP_Shape2D_RenderPipelineManager::GetColorIndex(glm::vec4 Color, unsigned int ShapeID) {
    SeenThisFrame.insert(ShapeID);

    auto found = ColorSlotID.find(ShapeID);
    if (found != ColorSlotID.end()) {
        GLuint slot = found->second;
        shape_colors[slot] = Color;        // update if the color changed
        return slot;
    }

    GLuint newSlot;
    if (!FreeSlots.empty()) {
        newSlot = FreeSlots.back();
        FreeSlots.pop_back();
        shape_colors[newSlot] = Color;
    } else {
        newSlot = static_cast<GLuint>(shape_colors.size());
        shape_colors.push_back(Color);
    }

    ColorSlotID[ShapeID] = newSlot;
    return newSlot;
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