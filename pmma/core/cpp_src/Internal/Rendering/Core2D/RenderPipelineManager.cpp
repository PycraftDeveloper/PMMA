#include "Internal/Rendering/Core2D/RenderPipelineManager.hpp"
#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"

#include "Internal/Rendering/Core2D/Base.hpp"

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

PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *PMMA::Internal::Rendering::Core2D::RenderPipelineManager::GetInstance(PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *Texture, uint16_t *TextureSize, unsigned char Channels) {
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

    bool TextureCanFit = true;
    if (Texture != nullptr && TextureSize[0] > 0 && TextureSize[1] > 0 && Channels >= 3) {
        if (Channels == 3) {
            TextureCanFit = lastInstance->CompressedTextureManager.CanFitTextureOpaque(Texture, TextureSize[0], TextureSize[1]);
        } else {
            TextureCanFit = lastInstance->CompressedTextureManager.CanFitTextureTransparent(Texture, TextureSize[0], TextureSize[1]);
        }
    }

    if ((lastInstance->OpaqueInstanceCount + lastInstance->TransparentInstanceCount) >= PMMA::Constants::RENDER_PIPELINE_INSTANCE_MAX_SIZE || !TextureCanFit) {
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