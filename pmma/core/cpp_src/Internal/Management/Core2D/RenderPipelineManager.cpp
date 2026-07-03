#include "Internal/Management/Core2D/RenderPipelineManager.hpp"
#include "Internal/Management/Core2D/RenderPipelineInstance.hpp"

PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::~CPP_RenderPipelineManager() {
    for (PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *instance : RenderPipelineInstances) {
        delete instance;
    }
    RenderPipelineInstances.clear();

    for (PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *instance : CachedRenderPipelineInstances) {
        delete instance;
    }
    CachedRenderPipelineInstances.clear();
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::Add(PMMA::Rendering::TwoD::CPP_Line *lineShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(lineShape);
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::Add(PMMA::Rendering::TwoD::CPP_Pixel *pixelShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(pixelShape);
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::Add(PMMA::Rendering::TwoD::CPP_RadialPolygon *radialPolygonShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(radialPolygonShape);
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::Add(PMMA::Rendering::TwoD::CPP_Arc *arcShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(arcShape);
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::Add(PMMA::Rendering::TwoD::CPP_Rectangle *rectangleShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(rectangleShape);
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::Add(PMMA::Rendering::TwoD::CPP_Ellipse *ellipseShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(ellipseShape);
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::Reset() {
    for (PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *instance : RenderPipelineInstances) {
        instance->Reset();
    }

    for (PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *instance : CachedRenderPipelineInstances) {
        delete instance;
    }
    CachedRenderPipelineInstances.clear();

    for (PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *instance : RenderPipelineInstances) {
        CachedRenderPipelineInstances.push_back(instance);
    }

    RenderPipelineInstances.clear();
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineManager::Render() {
    for (PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance *instance : RenderPipelineInstances) {
        instance->Render();
    }
}