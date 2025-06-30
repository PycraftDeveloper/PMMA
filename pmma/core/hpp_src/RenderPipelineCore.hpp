#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <variant>
#include <iostream>

#include "RadialPolygonShape.hpp"
#include "RectangleShape.hpp"
#include "RenderPipelineManager.hpp"

using RenderDataObject = std::variant<CPP_RenderPipelineManager*, CPP_RadialPolygonShape*, CPP_RectangleShape*>;

class EXPORT CPP_RenderPipelineCore {
    public:
        std::vector<RenderDataObject> RenderData;

        CPP_RenderPipelineCore();

        void Render();

        void Clear();

        void AddObject(RenderPipelineDataObject* RenderObject, bool RenderPipelineCompatable=true);
};