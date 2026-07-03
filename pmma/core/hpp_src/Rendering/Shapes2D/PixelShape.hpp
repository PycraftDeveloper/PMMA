#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Logger.hpp"
#include "Types.hpp"

namespace PMMA::Rendering::TwoD {
class EXPORT CPP_Pixel {
public:
    PMMA::Types::DisplayCoordinate ShapeCenter;
    PMMA::Types::Color Color;

    PMMA::Internal::Rendering::Core2D::InstanceData ShapeInstanceData;

    uintptr_t ID;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    inline CPP_Pixel() {
        ID = reinterpret_cast<uintptr_t>(this);
    }

    void Render();
};
} // namespace PMMA::Rendering::TwoD