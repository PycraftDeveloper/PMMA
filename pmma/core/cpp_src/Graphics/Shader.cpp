#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "PMMA_Core.hpp"

const bgfx::Memory* InternalLoadShader(const std::string& filePath) {
    std::ifstream file(filePath, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    const bgfx::Memory* mem = bgfx::alloc(uint32_t(size));
    file.read((char*)mem->data, size);
    return mem;
}

void CompileShaderComponent(string RawFilePath, string CompiledFilePath, string Type) {
    bgfx::ShaderHandle shader_component = BGFX_INVALID_HANDLE;

    string PlatformName;
    #if defined(_WIN32)
        PlatformName = "windows";
    #elif defined(__linux__)
        PlatformName = "linux";
    #else
        PlatformName = "unknown";
    #endif

    string Shader_C_Location = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "extern" + PMMA_Registry::PathSeparator + "bin" + PMMA_Registry::PathSeparator + "shaderc";
    if (PlatformName == "windows") {
        Shader_C_Location += ".exe";
    }

    string command = Shader_C_Location + " -f " + RawFilePath + " -o " + CompiledFilePath + " --type " + Type + " --platform " + PlatformName;
    system(command.c_str());
}

void CPP_Shader::CompileShader(bool InternalShader) {
    std::string PlatformName;
    #if defined(_WIN32)
        PlatformName = "windows";
    #elif defined(__linux__)
        PlatformName = "linux";
    #else
        PlatformName = "unknown";
    #endif

    if (RawVertexShaderPath != "") {
        if (CompiledVertexShaderPath == "") {
            string ShaderName = filesystem::path(RawVertexShaderPath).stem().string();
            if (InternalShader || !PMMA_Core::PassportInstance->IsRegistered) {
                CompiledVertexShaderPath = PMMA_Registry::PMMA_Location
                    + PMMA_Registry::PathSeparator + "temporary"
                    + PMMA_Registry::PathSeparator + "shader_cache"
                    + PMMA_Registry::PathSeparator + ShaderName + ".bin";
            } else {
                CompiledVertexShaderPath = PMMA_Core::PassportInstance->GetTemporaryPath()
                    + PMMA_Registry::PathSeparator + "shader_cache"
                    + PMMA_Registry::PathSeparator + PlatformName
                    + PMMA_Registry::PathSeparator + ShaderName + ".bin";
            }
        }
    }

    if (RawFragmentShaderPath != "") {
        if (CompiledFragmentShaderPath == "") {
            string ShaderName = filesystem::path(RawFragmentShaderPath).stem().string();
            if (InternalShader || !PMMA_Core::PassportInstance->IsRegistered) {
                CompiledFragmentShaderPath = PMMA_Registry::PMMA_Location
                    + PMMA_Registry::PathSeparator + "temporary"
                    + PMMA_Registry::PathSeparator + "shader_cache"
                    + PMMA_Registry::PathSeparator + ShaderName + ".bin";
            } else {
                CompiledFragmentShaderPath = PMMA_Core::PassportInstance->GetTemporaryPath()
                    + PMMA_Registry::PathSeparator + "shader_cache"
                    + PMMA_Registry::PathSeparator + PlatformName
                    + PMMA_Registry::PathSeparator + ShaderName + ".bin";
            }
        }
    }

    if (!filesystem::exists(CompiledVertexShaderPath)) {
        if (RawVertexShaderPath != "") {
            CompileShaderComponent(RawVertexShaderPath, CompiledVertexShaderPath, "vertex");
        }
    }
    if (!filesystem::exists(CompiledFragmentShaderPath)) {
        if (RawFragmentShaderPath != "") {
            CompileShaderComponent(RawFragmentShaderPath, CompiledFragmentShaderPath, "fragment");
        }
    }

    if (CompiledVertexShaderPath != "" && CompiledFragmentShaderPath != "") {
        bgfx::ShaderHandle vertex_shader = bgfx::createShader(InternalLoadShader(CompiledVertexShaderPath));
        bgfx::ShaderHandle fragment_shader = bgfx::createShader(InternalLoadShader(CompiledFragmentShaderPath));
        ShaderProgram = bgfx::createProgram(
            vertex_shader,
            fragment_shader,
            true
        );
        IsCompiled = true;
    } else {
        IsCompiled = false;
    }
}

bgfx::ProgramHandle CPP_Shader::Use() {
    if (!IsCompiled) {
        return ShaderProgram;
    }

    if (RawVertexShaderPath == "" || CompiledVertexShaderPath == "") {
        throw std::runtime_error("Vertex shader path is not set");
    }

    if (RawFragmentShaderPath == "" || CompiledFragmentShaderPath == "") {
        throw std::runtime_error("Fragment shader path is not set");
    }
}