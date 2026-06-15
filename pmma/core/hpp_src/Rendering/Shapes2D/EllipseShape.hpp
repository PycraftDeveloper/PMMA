#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

class EXPORT CPP_EllipseShape {
public:
    CPP_DisplayCoordinate ShapeCenter;
    CPP_Color Color;

    InstanceData ShapeInstanceData;

    uintptr_t ID;

    float Rotation = 0;
    float ColorIndex = 0;

    uint16_t Width = 0;
    uint16_t PointCount = 0;
    uint16_t ShapeSize[2] = {10, 10};

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    CPP_EllipseShape();

    void Render();

    inline void SetSize(uint16_t *in_size) {
        if (in_size[0] != ShapeSize[0] || in_size[1] != ShapeSize[1]) {
            ShapePropertyChanged = true;
        }

        ShapeSize[0] = in_size[0];
        ShapeSize[1] = in_size[1];
    };

    inline void GetSize(uint16_t *out_size) {
        out_size[0] = ShapeSize[0];
        out_size[1] = ShapeSize[1];
    }

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