#pragma once

float CPP_PythagoreanDifference(const float x1, const float y1, const float x2, const float y2);

float CPP_PythagoreanDistance(const float x, const float y);

float CPP_SmoothStep(const float value);

float CPP_Ranger(const float value, const float* old_range, const float* new_range);

float CPP_ArrayRanger(float* values, const int length, const float* old_range, const float* new_range);

void CPP_ArrayNormalize(float* value);

void CPP_Cross(const float* a, const float* b, float* out);

void CPP_Subtract(const float* a, const float* b, float* out);

float CPP_Dot(const float* a, const float* b);

void CPP_LookAt(const float* eye, const float* target, const float* up, float* out);

void CPP_ComputePosition(const float* position, const float* target, const float* up, float* out_x, float* out_y, float* out_z);

void CPP_PerspectiveFOV(const float fov, const float aspect_ratio, const float near, const float far, float (*out)[4]);