#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

namespace PMMA::Rendering::TwoD {
class EXPORT CPP_Pixel {
public:
    CPP_DisplayCoordinate ShapeCenter;
    CPP_Color Color;

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