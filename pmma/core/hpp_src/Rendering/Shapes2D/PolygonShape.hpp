#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT Polygon {
public:
    Polygon();

    ~Polygon() {
    }

    void Render();

    void InternalRender();

    inline void SetPoints(unsigned int (*in_points)[2], unsigned int count) {
    }

    inline void GetPoints(unsigned int (*out_points)[2]) {
    }

    inline unsigned int GetPointCount() {
        return 0;
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

    inline void SetClosed(bool in_closed) {
    }

    inline bool GetClosed() const {
        return false;
    }
};
}