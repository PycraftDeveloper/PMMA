#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <variant>
#include <iostream>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "OpenGL.hpp"

class CPP_RadialPolygonShape;
class CPP_RectangleShape;

using RenderPipelineDataObject = std::variant<CPP_RadialPolygonShape*, CPP_RectangleShape*>;

struct Vertex {
    glm::vec2 position;
    GLuint shape_id;
};

class EXPORT CPP_RenderPipelineManager {
    public:
        std::vector<RenderPipelineDataObject> RenderPipelineComponents;
        std::vector<Vertex> combined_vertexes;
        std::vector<glm::vec4> shape_colors;

        unsigned int type = CPP_Constants::TYPE_RENDER_PIPELINE_MANAGER;

        GLuint vao, vbo;

        CPP_RenderPipelineManager();
        ~CPP_RenderPipelineManager();

        void AddRenderTarget(RenderPipelineDataObject* NewObject);

        void InternalRender();

        void InternalAddRenderTarget(CPP_RadialPolygonShape* TargetPtr);
};