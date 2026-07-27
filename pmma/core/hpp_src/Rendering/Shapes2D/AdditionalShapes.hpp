#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Logger.hpp"
#include "Types.hpp"

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"

namespace PMMA::Rendering::TwoD::Shapes {
class EXPORT RadialPolygon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    using PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::ShapeSize;

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }

    inline void SetPointCount(uint16_t in_pointCount) {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(in_pointCount);
    };

    uint16_t GetPointCount() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetPointCount();
    }
};

class EXPORT Ellipse : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetPointCount(uint16_t in_pointCount) {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(in_pointCount);
    };

    uint16_t GetPointCount() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetPointCount();
    }
};

class EXPORT Circle : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};

class EXPORT Triangle : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Triangle() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(3);
    }

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};

class EXPORT Pentagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Pentagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(5);
    }

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};

class EXPORT Hexagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Hexagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(6);
    }

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};

class EXPORT Septagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Septagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(7);
    }

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};

class EXPORT Heptagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Heptagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(7);
    }

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};

class EXPORT Octagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Octagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(8);
    }

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};

class EXPORT Nonagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Nonagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(9);
    }

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};

class EXPORT Decagon : public PMMA::Rendering::TwoD::Shapes::RadialPolygonBase {
public:
    Decagon() {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetPointCount(10);
    }

    void GetSize(uint16_t *out_size) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetSize(out_size);
    }

    inline void SetRadius(uint16_t in_radius) {
        PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::SetRadius(in_radius);
    };

    inline uint16_t GetRadius() {
        return PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::GetRadius();
    }
};
} // namespace PMMA::Rendering::TwoD::Shapes