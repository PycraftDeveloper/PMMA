#pragma once

namespace CPP_StaticDisplay {
    extern unsigned int Width;
    extern unsigned int Height;
    extern bool DisplayCreated;
}

class CPP_Display {
    public:
        void Create(unsigned int New_Width, unsigned int New_Height);

        unsigned int GetWidth();
        unsigned int GetHeight();
};