#pragma once

#include <map>
#include <string>
#include <vector>

#include <bgfx/bgfx.h>

#include "Internal/Internal.hpp"

#include "Internal/Rendering/Core2D/GeneratedTextureInstance.hpp"

namespace PMMA::Internal::Rendering::Core2D {
class GeneratedTextureManager {
private:
    PMMA::Internal::Rendering::Core2D::GeneratedTextureInstance OpaqueGeneratedTextureInstance;

    PMMA::Internal::Rendering::Core2D::GeneratedTextureInstance TransparentGeneratedTextureInstance;

public:
    void OpaquePass();

    void TransparentPass();

    void Assemble();
};
} // namespace PMMA::Internal::Rendering::Core2D