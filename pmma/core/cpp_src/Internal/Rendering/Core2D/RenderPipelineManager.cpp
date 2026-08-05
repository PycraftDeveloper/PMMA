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

PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *PMMA::Internal::Rendering::Core2D::RenderPipelineManager::GetInstance(uint16_t *TextureSize, unsigned char Channels) {
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

    // THIS NEEDS TO CHECK IF THE EXISTING TEXTURE IS NOT ALREADY IN THE ATLAS AS OTHERWISE MEMORY LEAKS
    bool TextureCanFit = true;
    if (TextureSize[0] > 0 && TextureSize[1] > 0) {
        if (Channels == 3) {
            TextureCanFit = lastInstance->OpaqueTextureManager.CanFitTexture(TextureSize[0], TextureSize[1]);
        } else {
            TextureCanFit = lastInstance->TransparentTextureManager.CanFitTexture(TextureSize[0], TextureSize[1]);
        }
    }

    if ((lastInstance->OpaqueInstanceCount + lastInstance->TransparentInstanceCount) >= PMMA::Constants::RENDER_PIPELINE_INSTANCE_MAX_SIZE || !TextureCanFit) {
        std::cout << "New RPI" << std::endl;
        if (CachedRenderPipelineInstances.empty()) {
            RenderPipelineInstances.push_back(new PMMA::Internal::Rendering::Core2D::RenderPipelineInstance());
        } else {
            RenderPipelineInstances.push_back(CachedRenderPipelineInstances.front());
            CachedRenderPipelineInstances.erase(
                CachedRenderPipelineInstances.begin());
        }
        lastInstance = RenderPipelineInstances.back();
    }

    // adds textures and uses lastInstance batch

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