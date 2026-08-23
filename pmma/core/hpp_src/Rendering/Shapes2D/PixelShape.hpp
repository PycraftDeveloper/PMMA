#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

namespace PMMA::Internal::Rendering::Core2D {
struct InstanceData;
}

namespace PMMA::Types::TwoD {
class Coordinate;
} // namespace PMMA::Types::TwoD

namespace PMMA::Types {
class Color;
class Texture;
} // namespace PMMA::Types

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT Pixel {
public:
    PMMA::Types::TwoD::Coordinate *ShapeCenter = nullptr;
    PMMA::Types::Color *Color = nullptr;
    PMMA::Types::Texture *Texture = nullptr;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    uintptr_t ID;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    Pixel();

    ~Pixel() {
        delete ShapeCenter;
        delete Color;
        delete Texture;

        ShapeCenter = nullptr;
        Color = nullptr;
        Texture = nullptr;
    }

    void Render();
};
} // namespace PMMA::Rendering::TwoD::Shapes