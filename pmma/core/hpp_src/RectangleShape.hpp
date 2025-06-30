#pragma once
#include "PMMA_Exports.hpp"

#include "Constants.hpp"

class EXPORT CPP_RectangleShape {
    private:

    public:
        unsigned int type = CPP_Constants::TYPE_RECTANGLE_SHAPE;

        void Render();

        void InternalRender();
};