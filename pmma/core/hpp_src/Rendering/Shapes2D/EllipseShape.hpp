#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Logger.hpp"
#include "Types.hpp"

namespace PMMA::Rendering::TwoD {
class EXPORT CPP_Ellipse {
public:
    PMMA::Types::DisplayCoordinate ShapeCenter;
    PMMA::Types::Color Color;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    uintptr_t ID;

    float Rotation = 0;

    uint16_t Width = 0;
    uint16_t PointCount = 0;
    uint16_t ShapeSize[2];

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;
    bool ShapeSizeSet = false;

    inline CPP_Ellipse() {
        ID = reinterpret_cast<uintptr_t>(this);
    }

    void Render();

    inline void SetSize(uint16_t *in_size) {
        if (in_size[0] != ShapeSize[0] || in_size[1] != ShapeSize[1]) {
            ShapePropertyChanged = true;
        }

        ShapeSize[0] = in_size[0];
        ShapeSize[1] = in_size[1];
        ShapeSizeSet = true;
    };

    void GetSize(uint16_t *out_size);

    inline void SetPointCount(uint16_t in_pointCount) {
        if (in_pointCount != PointCount) {
            ShapePropertyChanged = true;
        }

        PointCount = in_pointCount;
    };

    uint16_t GetPointCount() {
        return PointCount;
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
};
} // namespace PMMA::Rendering::TwoD