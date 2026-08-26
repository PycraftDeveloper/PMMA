#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include "Types/Color.hpp"
#include "Types/Coordinate.hpp"
#include "Types/Size.hpp"
#include "Types/Texture.hpp"

namespace PMMA::Internal::Rendering::Core2D {
struct InstanceData;
}

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT Arc {
public:
    PMMA::Types::TwoD::Coordinate ShapeCenter;
    PMMA::Types::TwoD::Size ShapeSize;
    PMMA::Types::Color Color;
    PMMA::Types::Texture Texture;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    uintptr_t ID;

    float Rotation = 0;
    float StartAngle;
    float EndAngle;

    uint16_t Width = 0;
    uint16_t PointCount = 0;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    bool StartAngleSet = false;
    bool EndAngleSet = false;
    bool UseTextureSize = false;

    inline Arc() {
        ID = reinterpret_cast<uintptr_t>(this);

        ShapeSize.Texture = &Texture;
    }

    void Render();

    inline void SetStartAngle(float in_start_angle) {
        if (StartAngleSet && (in_start_angle != StartAngle)) {
            ShapePropertyChanged = true;
        }

        StartAngle = in_start_angle;
        StartAngleSet = true;
    };

    float GetStartAngle();

    inline void SetEndAngle(float in_end_angle) {
        if (EndAngleSet && (in_end_angle != EndAngle)) {
            ShapePropertyChanged = true;
        }

        EndAngle = in_end_angle;
        EndAngleSet = true;
    };

    float GetEndAngle();

    inline void SetWidth(uint16_t in_width) {
        if (in_width != Width) {
            ShapePropertyChanged = true;
        }

        Width = in_width;
    };

    inline uint16_t GetWidth() const {
        return Width;
    }

    inline void SetSizeToTexture() {
        UseTextureSize = true;
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

    inline void SetPointCount(uint16_t in_point_count) {
        if (in_point_count != PointCount) {
            ShapePropertyChanged = true;
        }

        PointCount = in_point_count;
    }

    uint16_t GetPointCount() {
        return PointCount;
    }
};
} // namespace PMMA::Rendering::TwoD::Shapes