#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Logger.hpp"
#include "Types.hpp"

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT Pixel {
public:
    PMMA::Types::DisplayCoordinate ShapeCenter;
    PMMA::Types::Color Color;
    PMMA::Types::Texture Texture;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    uintptr_t ID;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    inline Pixel() {
        ID = reinterpret_cast<uintptr_t>(this);
    }

    void Render();
};
} // namespace PMMA::Rendering::TwoD