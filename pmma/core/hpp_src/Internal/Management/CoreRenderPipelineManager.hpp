#pragma once

#include <iostream>
#include <variant>
#include <vector>

#include <bgfx/bgfx.h>

#include "Internal/Management/Shape2DRenderPipelineManager.hpp"
#include "Internal/Management/TextRenderPipelineManager.hpp"
#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/TextRenderer.hpp"

#include <taskflow/taskflow.hpp>

using RawRenderObject = std::variant<
    CPP_Shape2D_RenderPipelineManager *,
    CPP_TextRenderPipelineManager *>;

class CPP_Shader;

struct Task {
    void *object;
    void (*func)(void *);
};

template <typename T>
static void TaskInvoker(void *obj) {
    T *o = static_cast<T *>(obj);
    o->InternalRender();
}

class CPP_RenderPipelineCore {
public:
    std::vector<CPP_Shape2D_RenderPipelineManager *> Shape_2D_RenderManagerCache;
    std::vector<CPP_TextRenderPipelineManager *> Text_RenderManagerCache;
    std::vector<RawRenderObject> RenderData;

    std::vector<std::vector<Task>> taskChunks;

    tf::Executor ParallelExecutor;
    tf::Taskflow Taskflow;
    int ThreadCount;
    int nextChunk = 0;

    bgfx::UniformHandle OrthDisplayProj;

    CPP_Shader *Shape2D_RenderPipelineShader = nullptr;

    uint64_t MaxSize;
    uint32_t MaxWidth;

    bool ParallelWorkToDo = false;

    CPP_RenderPipelineCore();
    ~CPP_RenderPipelineCore();

    void Render();

    void Reset();

    template <typename T>
    inline void Add_2D_Shape_Object(T *RenderObject) {
        if (RenderData.empty()) {
            if (!Shape_2D_RenderManagerCache.empty()) {
                RenderData.emplace_back(Shape_2D_RenderManagerCache.front());
                Shape_2D_RenderManagerCache.erase(Shape_2D_RenderManagerCache.begin());
            } else {
                RenderData.emplace_back(new CPP_Shape2D_RenderPipelineManager());
            }
        }

        CPP_Shape2D_RenderPipelineManager *manager = std::get<CPP_Shape2D_RenderPipelineManager *>(RenderData.back());

        RenderObject->Shape2D_RenderPipelineManager = manager;
        unsigned int NextReserveSize = manager->NextReserveSize;
        RenderObject->Location = NextReserveSize;
        RenderObject->ShapeIndex = manager->NewRenderContent.size();
        manager->NewRenderContent.emplace_back(RenderObject->ID, NextReserveSize);

        manager->NextReserveSize += RenderObject->GetVertexCount() + 3; // accounting for degens
        RenderObject->UpdateColorIndex();

        if (RenderObject->ColorIndexChanged) {
            ++manager->ColorIndexesChanged;
        }
        ++manager->ColorsInserted;

        manager->ColorDataChanged |= RenderObject->ColorDataChanged;

        if (RenderObject->VertexDataChanged) {
            taskChunks[nextChunk].emplace_back(Task{
                RenderObject,
                &TaskInvoker<T>});

            ParallelWorkToDo = true;

            nextChunk++;
            nextChunk = nextChunk % ThreadCount;
        }
    }

    void Add_Text_Object(CPP_TextRenderer *RenderObject);
};