#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

class EXPORT CPP_ArcShape {
public:
    CPP_ArcShape();

    ~CPP_ArcShape() {
    }

    void Render();

    void InternalRender();

    inline void SetStartAngle(float in_start_angle) {
    };

    inline float GetStartAngle() {
        return 0.0f;
    }

    inline void SetEndAngle(float in_end_angle) {
    };

    inline float GetEndAngle() {
        return 0.0f;
    }

    inline void SetWidth(unsigned int in_width) {
    };

    inline unsigned int GetWidth() const {
        return 0;
    }

    inline void SetRadius(unsigned int in_radius) {
    };

    inline unsigned int GetRadius() {
        return 0;
    }

    inline void SetRotation(float in_rotation) {
    }

    inline float GetRotation() const {
        return 0.0f;
    }

    inline void SetPointCount(unsigned int in_point_count) {
    }

    unsigned int GetPointCount();
};