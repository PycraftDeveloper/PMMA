#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

namespace PMMA::Internal::Rendering::Core2D {
struct InstanceData;
}

namespace PMMA::Types::TwoD {
class Coordinate;
class Size;
} // namespace PMMA::Types::TwoD

namespace PMMA::Types {
class Color;
class Texture;
} // namespace PMMA::Types

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT RadialPolygonBase {
public:
    PMMA::Types::TwoD::Coordinate *ShapeCenter = nullptr;
    PMMA::Types::TwoD::Size *ShapeSize = nullptr;
    PMMA::Types::Color *Color = nullptr;
    PMMA::Types::Texture *Texture = nullptr;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    uintptr_t ID;

    float Rotation = 0;

    uint16_t Width = 0;
    uint16_t PointCount = 0;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;
    bool UseTextureSize = false;

    RadialPolygonBase();

    ~RadialPolygonBase() {
        delete ShapeCenter;
        delete ShapeSize;
        delete Color;
        delete Texture;

        ShapeCenter = nullptr;
        ShapeSize = nullptr;
        Color = nullptr;
        Texture = nullptr;
    }

    void Render();

    inline void SetSizeToTexture() {
        UseTextureSize = true;
    }

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

protected:
    inline void SetPointCount(uint16_t in_pointCount) {
        if (in_pointCount != PointCount) {
            ShapePropertyChanged = true;
        }

        PointCount = in_pointCount;
    };

    uint16_t GetPointCount() {
        return PointCount;
    }
};
} // namespace PMMA::Rendering::TwoD::Shapes