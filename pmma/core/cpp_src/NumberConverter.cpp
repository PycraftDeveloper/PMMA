#include "PMMA_Core.hpp"

#include "NumberConverter.hpp"

CPP_BasicDisplayCoordinatesConverter::CPP_BasicDisplayCoordinatesConverter() {
    display = PMMA::DisplayInstance;
}

void CPP_BasicDisplayCoordinatesConverter::GetCoordinates_Pixel(unsigned int* out_coordinates) {
    if (!CoordinatesAreSet) {
        throw std::runtime_error("Coordinates not set!");
    }
    if (display == nullptr) {
        throw std::runtime_error("Display not created yet!");
    }
    unsigned int DisplaySize[2];
    display->GetSize(DisplaySize);

    float HalfDisplaySize[2] = { DisplaySize[0] / 2.f, DisplaySize[1] / 2.f };

    out_coordinates[0] = (unsigned int)(InternalCoordinates[0] * HalfDisplaySize[0] + HalfDisplaySize[0]);
    out_coordinates[1] = (unsigned int)(InternalCoordinates[1] * HalfDisplaySize[1] + HalfDisplaySize[1]);
}

void CPP_BasicDisplayCoordinatesConverter::SetCoordinates_Pixel(unsigned int* in_coordinates) {
    if (display == nullptr) {
        throw std::runtime_error("Display not created yet!");
    }
    unsigned int DisplaySize[2];
    display->GetSize(DisplaySize);

    float HalfDisplaySize[2] = { DisplaySize[0] / 2.f, DisplaySize[1] / 2.f };

    InternalCoordinates[0] = (in_coordinates[0] - HalfDisplaySize[0]) / HalfDisplaySize[0];
    InternalCoordinates[1] = (in_coordinates[1] - HalfDisplaySize[1]) / HalfDisplaySize[1];
    CoordinatesAreSet = true;
}

CPP_DisplayCoordinatesConverter::CPP_DisplayCoordinatesConverter(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
    srand((unsigned int)time(0));

    PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
    FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

    seed = new_seed;
    octaves = new_octaves;
    frequency = new_frequency;
    amplitude = new_amplitude;
}

CPP_BasicDisplayScalarConverter::CPP_BasicDisplayScalarConverter() {
    display = PMMA::DisplayInstance;
}

void CPP_BasicDisplayScalarConverter::SetScalar_Pixel(unsigned int in_scalar) {
    if (display == nullptr) {
        throw std::runtime_error("Display not created yet!");
    }
    InternalScalar = (float)(in_scalar) * (2.f / display->GetHeight());
    ScalarIsSet = true;
}

unsigned int CPP_BasicDisplayScalarConverter::GetScalar_Pixel() {
    if (!ScalarIsSet) {
        throw std::runtime_error("Scalar not set!");
    }
    if (display == nullptr) {
        throw std::runtime_error("Display not created yet!");
    }
    return (unsigned int)(InternalScalar * display->GetHeight() / 2.f);
}

CPP_DisplayScalarConverter::CPP_DisplayScalarConverter(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
    srand((unsigned int)time(0));

    PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
    FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);

    seed = new_seed;
    octaves = new_octaves;
    frequency = new_frequency;
    amplitude = new_amplitude;
}