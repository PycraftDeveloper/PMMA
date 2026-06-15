#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"

class EXPORT CPP_RadialPolygonShape {
public:
    CPP_DisplayCoordinate ShapeCenter;
    CPP_Color Color;

    InstanceData ShapeInstanceData;

    uintptr_t ID;

    float Rotation = 0;
    float ColorIndex = 0;

    uint16_t Radius;
    uint16_t Width = 0;
    uint16_t PointCount = 0;

    bool RadiusSet = false;
    bool HasAlpha = false;
    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    CPP_RadialPolygonShape();

    void Render();

    inline void SetRadius(uint16_t in_radius) {
        if (in_radius != Radius) {
            ShapePropertyChanged = true;
        }
        Radius = in_radius;
        RadiusSet = true;
    };

    inline uint16_t GetRadius() {
        return Radius;
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