#include "Internal/Management/Core2D_RenderPipelineManager.hpp"
#include "Internal/Management/Core2D_RenderPipelineInstance.hpp"

CPP_Core2D_RenderPipelineManager::~CPP_Core2D_RenderPipelineManager() {
    for (CPP_Core2D_RenderPipelineInstance *instance : RenderPipelineInstances) {
        delete instance;
    }
    RenderPipelineInstances.clear();

    for (CPP_Core2D_RenderPipelineInstance *instance : CachedRenderPipelineInstances) {
        delete instance;
    }
    CachedRenderPipelineInstances.clear();
}

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

void CPP_Core2D_RenderPipelineManager::Add(CPP_RadialPolygonShape *radialPolygonShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new CPP_Core2D_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    CPP_Core2D_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new CPP_Core2D_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(radialPolygonShape);
}

void CPP_Core2D_RenderPipelineManager::Add(CPP_ArcShape *arcShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new CPP_Core2D_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    CPP_Core2D_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new CPP_Core2D_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(arcShape);
}

void CPP_Core2D_RenderPipelineManager::Add(CPP_EllipseShape *ellipseShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new CPP_Core2D_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    CPP_Core2D_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new CPP_Core2D_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(ellipseShape);
}

void CPP_Core2D_RenderPipelineManager::Reset() {
    for (CPP_Core2D_RenderPipelineInstance *instance : RenderPipelineInstances) {
        instance->Reset();
    }

    for (CPP_Core2D_RenderPipelineInstance *instance : CachedRenderPipelineInstances) {
        delete instance;
    }
    CachedRenderPipelineInstances.clear();

    for (CPP_Core2D_RenderPipelineInstance *instance : RenderPipelineInstances) {
        CachedRenderPipelineInstances.push_back(instance);
    }

    RenderPipelineInstances.clear();
}

void CPP_Core2D_RenderPipelineManager::Render() {
    for (CPP_Core2D_RenderPipelineInstance *instance : RenderPipelineInstances) {
        instance->Render();
    }
}