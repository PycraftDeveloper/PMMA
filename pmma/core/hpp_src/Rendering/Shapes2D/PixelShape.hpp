#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include "Types/Color.hpp"
#include "Types/CompressedTexture.hpp"
#include "Types/Coordinate.hpp"

namespace PMMA::Internal::Rendering::Core2D {
struct InstanceData;
}

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT Pixel {
public:
    PMMA::Types::TwoD::Coordinate ShapeCenter;
    PMMA::Types::Color Color;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    uintptr_t ID;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    inline Pixel() {
        ID = reinterpret_cast<uintptr_t>(this);
    }

    void Render();
};
} // namespace PMMA::Rendering::TwoD::Shapes