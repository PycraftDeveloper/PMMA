#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"

class EXPORT CPP_ArcShape {
public:
    CPP_DisplayCoordinate ShapeCenter;
    CPP_Color Color;

    InstanceData ShapeInstanceData;

    float Rotation = 0;
    float StartAngle;
    float EndAngle;

    uint64_t ID;
    uint16_t Width = 0;
    uint16_t PointCount = 0;
    uint16_t Radius;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;
    bool StartAngleSet = false;
    bool EndAngleSet = false;
    bool RadiusSet = false;

    CPP_ArcShape();

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

    inline void SetRadius(unsigned int in_radius) {
        if (in_radius != Radius) {
            ShapePropertyChanged = true;
        }

        RadiusSet = true;
        Radius = in_radius;
    };

    unsigned int GetRadius();

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