#include <cmath>

#include "RadialPolygonShape.hpp"
#include "RenderPipelineManager.hpp"

#include "Constants.hpp"

#include "PMMA_Core.hpp"

CPP_RadialPolygonShape::CPP_RadialPolygonShape() {
    RenderPipelineData = new RenderPipelineDataObject(this);
}

void CPP_RadialPolygonShape::Render(float ShapeQuality) {
    bool RenderPipelineCompatable = (HasAlpha == false && UsingGradients == false);

    // Calculate shape geometry here!
    VertexData.clear();

    unsigned int InternalPointCount = PointCount;
    if (PointCount == 0) {
        InternalPointCount = max(3, (int)(1 + (CPP_Constants::TAU / asin(1.0f / Radius)) * ShapeQuality));
    }

    float AngleStep = CPP_Constants::TAU / InternalPointCount;
    vector<float> Angles;
    Angles.reserve(InternalPointCount);

    for (int i = 0; i < InternalPointCount; i++) {
        Angles.push_back(Rotation + (i * AngleStep));
    }

    unsigned int outer_radius = Radius;

    unsigned int inner_radius = max(0, (int)Radius - (int)Width * 2);

    std::vector<float> combined_vertices;
    VertexData.reserve((InternalPointCount * 2 + 2));

    for (unsigned int i = 0; i < InternalPointCount; ++i) {
        float angle = Angles[i];
        glm::vec2 outer_vertex = glm::vec2(
            outer_radius * std::cos(angle),
            outer_radius * std::sin(angle)
        );
        glm::vec2 inner_vertex = glm::vec2(
            inner_radius * std::cos(angle),
            inner_radius * std::sin(angle)
        );

        VertexData.push_back(ShapeCentre + outer_vertex);
        VertexData.push_back(ShapeCentre + inner_vertex);
    }

    // Close the shape by repeating the first pair
    float first_angle = Angles[0];
    glm::vec2 outer_first = glm::vec2(
        outer_radius * std::cos(first_angle),
        outer_radius * std::sin(first_angle)
    );
    glm::vec2 inner_first = glm::vec2(
        inner_radius * std::cos(first_angle),
        inner_radius * std::sin(first_angle)
    );
    VertexData.push_back(ShapeCentre + outer_first);
    VertexData.push_back(ShapeCentre + inner_first);

    PMMA::RenderPipelineCore->AddObject(RenderPipelineData, RenderPipelineCompatable);
}

void CPP_RadialPolygonShape::InternalRender() {

}