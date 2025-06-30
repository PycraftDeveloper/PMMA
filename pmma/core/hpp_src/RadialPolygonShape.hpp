#pragma once
#include "PMMA_Exports.hpp"

#include "Constants.hpp"

class EXPORT CPP_RadialPolygonShape {
    private:

    public:
        unsigned int type = CPP_Constants::TYPE_RADIAL_POLYGON_SHAPE;

        void Render();

        void InternalRender();
};