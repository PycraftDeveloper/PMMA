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
class EXPORT Line {
public:
    PMMA::Types::TwoD::Coordinate *ShapeStart = nullptr;
    PMMA::Types::TwoD::Coordinate *ShapeEnd = nullptr;
    PMMA::Types::Color *Color = nullptr;
    PMMA::Types::Texture *Texture = nullptr;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    float Rotation = 0;

    uintptr_t ID;
    uint16_t Width = 1;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    Line();

    ~Line() {
        delete ShapeStart;
        delete ShapeEnd;
        delete Color;
        delete Texture;

        ShapeStart = nullptr;
        ShapeEnd = nullptr;
        Color = nullptr;
        Texture = nullptr;
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