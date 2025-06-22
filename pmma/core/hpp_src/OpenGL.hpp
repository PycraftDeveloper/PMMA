#pragma once
#include "PMMA_Exports.hpp"

#include <string>

typedef unsigned int GLuint;
typedef unsigned int GLenum;

class EXPORT CPP_Shader {
    private:
        std::string LoadShaderComponent(const std::string& path);

        GLuint CompileShader(GLenum type, const std::string& source);

    public:
        GLuint CreateShaderProgram(const std::string& vertexShaderSource, const std::string& fragmentShaderSource);
};