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
    CPP_EllipseShape();

    ~CPP_EllipseShape() {
    }

    void Render();

    void InternalRender();

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

    inline void SetPointCount(unsigned int in_point_count) {
    }

    unsigned int GetPointCount();
};