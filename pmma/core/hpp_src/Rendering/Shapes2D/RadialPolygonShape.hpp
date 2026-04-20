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
    CPP_RadialPolygonShape();

    ~CPP_RadialPolygonShape() {
    }

    void Render();

    void InternalRender();

    inline void SetRadius(unsigned int in_radius) {
    };

    inline unsigned int GetRadius() {
        return 0;
    };

    inline void SetPointCount(unsigned int in_pointCount) {
    };

    unsigned int GetPointCount();

    inline void SetWidth(unsigned int in_width) {
    };

    inline unsigned int GetWidth() const {
        return 0;
    }

    inline void SetRotation(float in_rotation) {
    }

    inline float GetRotation() const {
        return 0.0f;
    }
};