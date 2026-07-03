#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Logger.hpp"
#include "Types.hpp"

namespace PMMA::Rendering::TwoD {
class EXPORT CPP_Line {
public:
    PMMA::Types::DisplayCoordinate ShapeStart;
    PMMA::Types::DisplayCoordinate ShapeEnd;
    PMMA::Types::Color Color;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    float Rotation = 0;
    uint16_t PointCount = 0;

    uintptr_t ID;
    uint16_t Width = 1;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    inline CPP_Line() {
        ID = reinterpret_cast<uintptr_t>(this);
    }

    void Render();

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