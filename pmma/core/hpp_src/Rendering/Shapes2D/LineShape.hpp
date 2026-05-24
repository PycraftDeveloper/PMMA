#pragma once
#include "PMMA_Exports.hpp"

#include <cstdint>
#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

class EXPORT CPP_LineShape {
public:
    CPP_Logger *Logger;
    CPP_DisplayCoordinate *ShapeStart;
    CPP_DisplayCoordinate *ShapeEnd;
    CPP_Color *Color;

    InstanceData ShapeInstanceData;

    float Rotation = 0;

    uintptr_t ID;
    unsigned int Width = 1;

    bool ColorDataChanged = true;
    bool ShapePropertyChanged = true;

    CPP_LineShape();

    ~CPP_LineShape() {
        if (Logger != nullptr) {
            delete Logger;
            Logger = nullptr;
        }

        delete ShapeStart;
        ShapeStart = nullptr;

        delete ShapeEnd;
        ShapeEnd = nullptr;

        delete Color;
        Color = nullptr;
    }

    void Render();

    inline void SetWidth(unsigned int in_width) {
        if (in_width != Width) {
            ShapePropertyChanged = true;
        }
        Width = in_width;
    };

    inline unsigned int GetWidth() const {
        return Width;
    }

    inline void SetRotation(float in_rotation) {
        if (in_rotation != Rotation) {
            ShapePropertyChanged = true;
        }
        Rotation = in_rotation;
    }

    inline float GetRotation() const {
        return Rotation;
    }
};