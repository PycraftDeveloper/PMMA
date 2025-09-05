#include "PMMA_Core.hpp"

const bgfx::Memory* InternalLoadShader(const std::string& filePath) {
    std::ifstream file(filePath, std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    const bgfx::Memory* mem = bgfx::alloc(uint32_t(size));
    file.read((char*)mem->data, size);
    return mem;
}

bgfx::ProgramHandle CPP_Shader::Use() {
    if (!IsLoaded) {
        bgfx::ShaderHandle vsh = BGFX_INVALID_HANDLE;
        bgfx::ShaderHandle fsh = BGFX_INVALID_HANDLE;

        std::string PlatformName;
        #if defined(_WIN32)
            PlatformName = "windows";
        #elif defined(__linux__)
            PlatformName = "linux";
        #else
            PlatformName = "unknown";
        #endif

        if (RawVertexShaderPath != "") {
            std::string ShaderName = std::filesystem::path(RawVertexShaderPath).stem().string();
            std::string CompiledShaderLocation;
            if (PMMA_Core::PassportInstance->IsRegistered) {
                CompiledShaderLocation = PMMA_Core::PassportInstance->GetTemporaryPath();
                CompiledShaderLocation += PMMA_Registry::PathSeparator + "shader_cache";
                CompiledShaderLocation += PMMA_Registry::PathSeparator + PlatformName;
                CompiledShaderLocation += PMMA_Registry::PathSeparator + ShaderName + ".bin";
            }

            std::string Shader_C_Location = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "extern" + PMMA_Registry::PathSeparator + "bin" + PMMA_Registry::PathSeparator + "shaderc";
            if (PlatformName == "windows") {
                Shader_C_Location += ".exe";
            }

            std::string command = Shader_C_Location + " -f " + RawVertexShaderPath + " -o " + CompiledShaderLocation + " --type vertex --platform " + PlatformName;
            system(command.c_str());

            CompiledVertexShaderPath = CompiledShaderLocation;
            RawVertexShaderPath = "";

            bgfx::ShaderHandle vsh = bgfx::createShader(InternalLoadShader(CompiledVertexShaderPath));
        } else if (CompiledVertexShaderPath != "") {
            // Load compiled shader
            bgfx::ShaderHandle vsh = bgfx::createShader(InternalLoadShader(CompiledVertexShaderPath));
        } else {
            throw std::runtime_error("No vertex shader loaded.");
        }

        if (RawFragmentShaderPath != "") {
            std::string ShaderName = std::filesystem::path(RawFragmentShaderPath).stem().string();
            std::string CompiledShaderLocation;
            if (PMMA_Core::PassportInstance->IsRegistered) {
                CompiledShaderLocation = PMMA_Core::PassportInstance->GetTemporaryPath();
                CompiledShaderLocation += PMMA_Registry::PathSeparator + "shader_cache";
                CompiledShaderLocation += PMMA_Registry::PathSeparator + PlatformName;
                CompiledShaderLocation += PMMA_Registry::PathSeparator + ShaderName + ".bin";
            }

            std::string Shader_C_Location = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "extern" + PMMA_Registry::PathSeparator + "bin" + PMMA_Registry::PathSeparator + "shaderc";
            if (PlatformName == "windows") {
                Shader_C_Location += ".exe";
            }

            std::string command = Shader_C_Location + " -f " + RawFragmentShaderPath + " -o " + CompiledShaderLocation + " --type vertex --platform " + PlatformName;
            system(command.c_str());

            CompiledFragmentShaderPath = CompiledShaderLocation;
            RawFragmentShaderPath = "";

            bgfx::ShaderHandle fsh = bgfx::createShader(InternalLoadShader(CompiledFragmentShaderPath));
        } else if (CompiledFragmentShaderPath != "") {
            // Load compiled shader
            bgfx::ShaderHandle fsh = bgfx::createShader(InternalLoadShader(CompiledFragmentShaderPath));
        } else {
            throw std::runtime_error("No fragment shader loaded.");
        }

        ShaderProgram = bgfx::createProgram(vsh, fsh, true);
    }

    return ShaderProgram;
}