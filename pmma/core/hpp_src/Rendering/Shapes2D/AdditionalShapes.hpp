#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT RadialPolygon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    inline void SetPointCount(uint16_t in_pointCount) {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(in_pointCount);
    };

    uint16_t GetPointCount() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetPointCount();
    }
};

class EXPORT Ellipse : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    inline void SetPointCount(uint16_t in_pointCount) {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(in_pointCount);
    };

    uint16_t GetPointCount() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetPointCount();
    }
};

class EXPORT Circle : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
};

class EXPORT Triangle : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Triangle() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(3);
    }
};

class EXPORT Pentagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Pentagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(5);
    }
};

class EXPORT Hexagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Hexagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(6);
    }
};

class EXPORT Septagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Septagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(7);
    }
};

class EXPORT Heptagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Heptagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(7);
    }
};

class EXPORT Octagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Octagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(8);
    }
};

class EXPORT Nonagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Nonagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(9);
    }
};

class EXPORT Decagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Decagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(10);
    }
};
} // namespace PMMA::Rendering::TwoD::Shapes