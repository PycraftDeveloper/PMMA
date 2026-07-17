#include "Internal/Rendering/Core2D/RenderPipelineManager.hpp"
#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"

#include "Constants.hpp"

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

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Line *lineShape) {
    lastInstance->Add(lineShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::RadialPolygon *radialPolygonShape) {
    lastInstance->Add(radialPolygonShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Arc *arcShape) {
    lastInstance->Add(arcShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Ellipse *ellipseShape) {
    lastInstance->Add(ellipseShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Rectangle *rectangleShape) {
    lastInstance->Add(rectangleShape);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineManager::Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Pixel *pixelShape) {
    lastInstance->Add(pixelShape);
}

PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *PMMA::Internal::Rendering::Core2D::RenderPipelineManager::GetInstance() {
    if (RenderPipelineInstances.empty()) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.front());
            CachedRenderPipelineInstances.erase(
                CachedRenderPipelineInstances.begin());
        }
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance = RenderPipelineInstances.back();

    if ((lastInstance->OpaqueInstanceCount + lastInstance->TransparentInstanceCount) >= PMMA::Constants::RENDER_PIPELINE_INSTANCE_MAX_SIZE) {
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.front());
            CachedRenderPipelineInstances.erase(
                CachedRenderPipelineInstances.begin());
        }
        lastInstance = RenderPipelineInstances.back();
    }

    return lastInstance;
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