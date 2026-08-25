#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include "Types.hpp"

namespace PMMA::Internal::Rendering::Core2D {
struct InstanceData;
}

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT Line {
public:
    PMMA::Types::TwoD::Coordinate ShapeStart;
    PMMA::Types::TwoD::Coordinate ShapeEnd;
    PMMA::Types::Color Color;
    PMMA::Types::Texture Texture;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    float Rotation = 0;

    uintptr_t ID;
    uint16_t Width = 1;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    inline Line() {
        ID = reinterpret_cast<uintptr_t>(this);
    }

    void Render();

    inline void SetWidth(uint16_t in_width) {
        if (in_width != Width) {
            ShapePropertyChanged = true;
        }
        Width = in_width;
    };

    inline uint16_t GetWidth() const {
        return Width;
    }

    inline void SetRotation(float in_rotation) {
        if (in_rotation != Rotation) {
            ShapePropertyChanged = true;
        }
        Rotation = in_rotation;
    }

    inline float GetRotation() const {
        return Rotation;
    }
};
} // namespace PMMA::Rendering::TwoD::Shapes