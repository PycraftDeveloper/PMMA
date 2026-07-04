#include "Internal/Rendering/Core2D/RenderPipelineManager.hpp"
#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"

PMMA::Internal::Rendering::Core2D::RenderPipelineManager::~RenderPipelineManager() {
    for (PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *instance : RenderPipelineInstances) {
        delete instance;
    }
    RenderPipelineInstances.clear();

    for (PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *instance : CachedRenderPipelineInstances) {
        delete instance;
    }
    CachedRenderPipelineInstances.clear();
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Rendering::TwoD::Shapes::Line *lineShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(lineShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Rendering::TwoD::Shapes::Pixel *pixelShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(pixelShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Rendering::TwoD::Shapes::RadialPolygon *radialPolygonShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(radialPolygonShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Rendering::TwoD::Shapes::Arc *arcShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(arcShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Rendering::TwoD::Shapes::Rectangle *rectangleShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(rectangleShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Rendering::TwoD::Shapes::Ellipse *ellipseShape) {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if (lastInstance->instanceCount >= 16777216) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.back());
            CachedRenderPipelineInstances.pop_back();
        }
        lastInstance = RenderPipelineInstances.back();
    }

    lastInstance->Add(ellipseShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Reset() {
    for (PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *instance : RenderPipelineInstances) {
        instance->Reset();
    }

    for (PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *instance : CachedRenderPipelineInstances) {
        delete instance;
    }
    CachedRenderPipelineInstances.clear();

    for (PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *instance : RenderPipelineInstances) {
        CachedRenderPipelineInstances.push_back(instance);
    }

    RenderPipelineInstances.clear();
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Render() {
    for (PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *instance : RenderPipelineInstances) {
        instance->Render();
    }
}