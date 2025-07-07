#pragma once

#include <vector>
#include <variant>
#include <iostream>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "OpenGL.hpp"

class CPP_RadialPolygonShape;
class CPP_RectangleShape;

using Shape2D_RenderObject = std::variant<CPP_RadialPolygonShape*, CPP_RectangleShape*>;

struct Vertex {
    glm::vec2 position;
    GLuint shape_id;
};

class CPP_Shape2D_RenderPipelineManager {
    public:
        std::vector<Shape2D_RenderObject> RenderPipelineComponents;
        std::vector<Vertex> combined_vertexes;
        std::vector<glm::vec4> shape_colors;

        GLuint vao, vbo;
        bool HasAlpha = false;

        CPP_Shape2D_RenderPipelineManager();
        ~CPP_Shape2D_RenderPipelineManager();

        void AddRenderTarget(const Shape2D_RenderObject& NewObject);

        void InternalRender();

        void InternalAddRenderTarget(CPP_RadialPolygonShape* TargetPtr);
        void InternalAddRenderTarget(CPP_RectangleShape* TargetPtr);
};