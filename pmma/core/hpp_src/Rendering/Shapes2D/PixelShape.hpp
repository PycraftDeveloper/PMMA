#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

class EXPORT CPP_PixelShape {
public:
    CPP_PixelShape();

    ~CPP_PixelShape() {
    }

    void Render();

    void InternalRender();
};