#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

class EXPORT CPP_RadialPolygonShape {
public:
    CPP_Logger *Logger;
    CPP_DisplayCoordinate *ShapeCenter;
    CPP_Color *Color;

    InstanceData ShapeInstanceData;

    uintptr_t ID;

    float Rotation = 0;
    float ColorIndex = 0;

    unsigned int Radius;
    unsigned int Width = 0;
    unsigned int PointCount = 0;

    bool RadiusSet = false;
    bool WidthSet = true;
    bool HasAlpha = false;
    bool PointCountSet = true;
    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    CPP_RadialPolygonShape();

    ~CPP_RadialPolygonShape() {
        if (Logger != nullptr) {
            delete Logger;
            Logger = nullptr;
        }

        delete ShapeCenter;
        ShapeCenter = nullptr;

        delete Color;
        Color = nullptr;
    }

    void Render();

    inline void SetRadius(unsigned int in_radius) {
        if (in_radius != Radius) {
            ShapePropertyChanged = true;
        }
        Radius = in_radius;
        RadiusSet = true;
    };

    inline unsigned int GetRadius() {
        if (!RadiusSet) {
            if (Logger == nullptr) {
                Logger = new CPP_Logger();
            }
            Logger->InternalLogWarn(
                30,
                "You have not specified a radius for the arc \
please use `RadialPolygon.set_radius` to set it before attempting to get it.");
            throw std::runtime_error("Radius not set");
        }
        return Radius;
    };

    inline void SetPointCount(unsigned int in_pointCount) {
        if (in_pointCount != PointCount) {
            ShapePropertyChanged = true;
        }

        PointCount = in_pointCount;
        PointCountSet = true;
    };

    inline void SetWidth(unsigned int in_width) {
        if (in_width != Width) {
            ShapePropertyChanged = true;
        }

        Width = in_width;
        WidthSet = true;
    };

    inline unsigned int GetWidth() const {
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