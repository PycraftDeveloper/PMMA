#include <glad/gl.h>

#include "PMMA_Core.hpp"

using namespace std;

string CPP_Shader::LoadShaderComponent(const string& path) {
    ifstream file(path);
    stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

GLuint CPP_Shader::CompileShader(GLenum type, const string& source) {
    GLuint shader = glCreateShader(type);
    const char* src = source.c_str();
    glShaderSource(shader, 1, &src, nullptr);
    glCompileShader(shader);

    // Check for compile errors
    GLint success;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
    if (!success) {
        char log[512];
        glGetShaderInfoLog(shader, 512, nullptr, log);
        throw runtime_error("Shader Compilation Failed:\n" + string(log));
    }

    return shader;
}

GLuint CPP_Shader::CreateShaderProgram(const std::string& vertexPath, const std::string& fragmentPath) {
    std::string vertexCode = LoadShaderComponent(vertexPath);
    std::string fragmentCode = LoadShaderComponent(fragmentPath);

    GLuint vertexShader = CompileShader(GL_VERTEX_SHADER, vertexCode);
    GLuint fragmentShader = CompileShader(GL_FRAGMENT_SHADER, fragmentCode);

    GLuint program = glCreateProgram();
    glAttachShader(program, vertexShader);
    glAttachShader(program, fragmentShader);
    glLinkProgram(program);

    // Check linking errors
    GLint success;
    glGetProgramiv(program, GL_LINK_STATUS, &success);
    if (!success) {
        char log[512];
        glGetProgramInfoLog(program, 512, nullptr, log);
        throw runtime_error("Program Linking Failed:\n" + std::string(log));
    }

    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    return program;
}