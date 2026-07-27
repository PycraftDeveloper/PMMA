#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Logger.hpp"
#include "Types.hpp"

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT Rectangle {
public:
    PMMA::Types::TwoD::Coordinate ShapeCenter;
    PMMA::Types::TwoD::Size ShapeSize;
    PMMA::Types::Color Color;
    PMMA::Types::Texture Texture;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    float Rotation = 0;

    uintptr_t ID;
    uint16_t Width = 0;
    uint16_t CornerRadius = 0;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;
    bool UseTextureSize = false;

    inline Rectangle() {
        ID = reinterpret_cast<uintptr_t>(this);

        ShapeSize.Texture = &Texture;
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

    inline void SetCornerRadius(uint16_t in_corner_radius) {
        if (in_corner_radius != CornerRadius) {
            ShapePropertyChanged = true;
        }

        CornerRadius = in_corner_radius;
    }

    inline uint16_t GetCornerRadius() const {
        return CornerRadius;
    }

    inline void SetSizeToTexture() {
        UseTextureSize = true;
    }
};
} // namespace PMMA::Rendering::TwoD