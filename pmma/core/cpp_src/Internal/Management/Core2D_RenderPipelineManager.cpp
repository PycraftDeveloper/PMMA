#include "Internal/Management/Core2D_RenderPipelineManager.hpp"
#include "Internal/Management/Core2D_RenderPipelineInstance.hpp"

void CPP_Core2D_RenderPipelineManager::Add(CPP_LineShape *lineShape) {
    if (RenderPipelineInstances.empty()) {
        RenderPipelineInstances.push_back(new CPP_Core2D_RenderPipelineInstance());
    }

    CPP_Core2D_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        RenderPipelineInstances.push_back(new CPP_Core2D_RenderPipelineInstance());
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(lineShape);
}

void CPP_Core2D_RenderPipelineManager::Reset() {
    for (CPP_Core2D_RenderPipelineInstance *instance : RenderPipelineInstances) {
        instance->Reset();
    }
}

void CPP_Core2D_RenderPipelineManager::Render() {
    for (CPP_Core2D_RenderPipelineInstance *instance : RenderPipelineInstances) {
        instance->Render();
    }
}