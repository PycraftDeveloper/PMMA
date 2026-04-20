#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

class EXPORT CPP_RectangleShape {
public:
    CPP_RectangleShape();

    ~CPP_RectangleShape() {
    }

    void Render();

    void InternalRender();

    inline void SimpleApplyRotation(float *position, float *shape_center, float RotationSin, float RotationCos, unsigned int HalfWidth, unsigned int HalfHeight, float *out) {
    }

    inline void ComplexApplyRotation(float *point, float *shape_center, float RotationSin, float RotationCos, float *out) {
    }

    inline void SetSize(unsigned int *in_size) {
    };

    inline void GetSize(unsigned int *out_size) {
    }

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

    inline void SetCornerRadius(unsigned int in_corner_radius) {
    }

    inline unsigned int GetCornerRadius() const {
        return 0;
    }
};