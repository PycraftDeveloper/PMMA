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

void CPP_Shader::CompileShaderComponent(
        string RawFilePath,
        string CompiledFilePath,
        string Type) {

    bgfx::ShaderHandle shader_component = BGFX_INVALID_HANDLE;

    string PlatformName = CPP_General::GetOperatingSystem();
    if (PlatformName == CPP_Constants::OperatingSystems::ANDROID) {
        PlatformName = "android";
    } else if (PlatformName == CPP_Constants::OperatingSystems::EMSCRIPTEN) {
        PlatformName = "asm.js";
    } else if (PlatformName == CPP_Constants::OperatingSystems::IOS) {
        PlatformName = "ios";
    } else if (PlatformName == CPP_Constants::OperatingSystems::LINUX) {
        PlatformName = "linux";
    } else if (PlatformName == CPP_Constants::OperatingSystems::PS4) {
        PlatformName = "orbis";
    } else if (PlatformName == CPP_Constants::OperatingSystems::MACOS) {
        PlatformName = "osx";
    } else if (PlatformName == CPP_Constants::OperatingSystems::WINDOWS) {
        PlatformName = "windows";
    } else {
        throw std::runtime_error("Unsupported platform: " + PlatformName);
    }

    PMMA_Core::LoggingManagerInstance->InternalLogInfo(
        34,
        "PMMA is using '" + PlatformName + "' for shaders."
    );

    string Shader_C_Location = PMMA_Registry::PMMA_Location +
        PMMA_Registry::PathSeparator + "extern" +
        PMMA_Registry::PathSeparator + "bin" +
        PMMA_Registry::PathSeparator + "shaderc";

    if (PlatformName == "windows") {
        Shader_C_Location += ".exe";
    }

    string ShaderBuildToolsLocation = PMMA_Registry::PMMA_Location +
        PMMA_Registry::PathSeparator + "extern" +
        PMMA_Registry::PathSeparator + "shader_build_tools";

    string VaryingDefLocation = filesystem::path(RawFilePath).parent_path().string() +
        PMMA_Registry::PathSeparator + "varying.def.sc";

    string GraphicsProfile = CPP_Shader::GetGraphicsProfile();

    string command = Shader_C_Location + " -f " + RawFilePath + " -o " +
        CompiledFilePath + " --type " + Type + " --platform " +
        PlatformName + " -i " + ShaderBuildToolsLocation +
        " --varyingdef " + VaryingDefLocation + " --profile " +
        GraphicsProfile;

    if (!filesystem::exists(CompiledFilePath)) {
        filesystem::create_directories(
            filesystem::path(CompiledFilePath).parent_path());
    }

    bool DontRepeatOutput = false;

    try {
        if (system(command.c_str()) != 0) {
            DontRepeatOutput = true;

            if (IsInternalShader){
                PMMA_Core::LoggingManagerInstance->InternalLogError(
                    49,
                    "PMMA was unable to compile the following shader: '" +
                    RawFilePath + "'. This is a shader that comes included \
with PMMA, so please report this issue to us here: \
'https://github.com/PycraftDeveloper/PMMA/issues' so we can fix the issue. \
We would also greatly appreciate it if you could include all information/debug/warn/error \
logs from your application run to help us diagnose the issue as it could \
be specific to a single platform or graphics backend. Thank you!");
            } else {
                PMMA_Core::LoggingManagerInstance->InternalLogError(
                    49,
                    "Shader compilation failed for '" + RawFilePath +
                    "' with command: '" + command + "'\n\n" +
                    "To diagnose this shader compilation issue, please run the \
command listed above in your system terminal/command prompt directly."
                );
            }
            throw std::runtime_error("Shader compilation failed for '" +
                RawFilePath + "' with command: '" + command + "'.");
        }
    } catch (const std::exception& e) {
        if (!DontRepeatOutput) {
            PMMA_Core::LoggingManagerInstance->InternalLogError(
                49,
                "Shader compilation failed: '" + string(e.what()) + "'."
            );
            throw std::runtime_error("Shader compilation failed for '" +
                RawFilePath + "' with command: '" + command +
                "'\nError: '" + string(e.what()) + "'.");
        }
        exit(49);
    }
}

void CPP_Shader::CompileShader(bool InternalShader) {
    IsInternalShader = InternalShader;

    std::string PlatformName = CPP_General::GetOperatingSystem();

    if (RawVertexShaderPath != "") {
        if (CompiledVertexShaderPath == "") {
            string ShaderName = filesystem::path(RawVertexShaderPath).stem().string();
            if (InternalShader || !PMMA_Core::PassportInstance->IsRegistered) {
                CompiledVertexShaderPath = PMMA_Registry::PMMA_Location
                    + PMMA_Registry::PathSeparator + "temporary"
                    + PMMA_Registry::PathSeparator + "shader_cache"
                    + PMMA_Registry::PathSeparator + PlatformName
                    + PMMA_Registry::PathSeparator + GetGraphicsProfile()
                    + PMMA_Registry::PathSeparator + ShaderName + ".bin";
            } else {
                CompiledVertexShaderPath = PMMA_Core::PassportInstance->GetTemporaryPath()
                    + PMMA_Registry::PathSeparator + "shader_cache"
                    + PMMA_Registry::PathSeparator + PlatformName
                    + PMMA_Registry::PathSeparator + GetGraphicsProfile()
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
                    + PMMA_Registry::PathSeparator + PlatformName
                    + PMMA_Registry::PathSeparator + GetGraphicsProfile()
                    + PMMA_Registry::PathSeparator + ShaderName + ".bin";
            } else {
                CompiledFragmentShaderPath = PMMA_Core::PassportInstance->GetTemporaryPath()
                    + PMMA_Registry::PathSeparator + "shader_cache"
                    + PMMA_Registry::PathSeparator + PlatformName
                    + PMMA_Registry::PathSeparator + GetGraphicsProfile()
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
        bgfx::ShaderHandle vertex_shader = bgfx::createShader(
            InternalLoadShader(CompiledVertexShaderPath));
        bgfx::ShaderHandle fragment_shader = bgfx::createShader(
            InternalLoadShader(CompiledFragmentShaderPath));

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
    if (IsCompiled) {
        return ShaderProgram;
    } else {
        throw std::runtime_error("Shader is not compiled");
    }

    if (RawVertexShaderPath == "" || CompiledVertexShaderPath == "") {
        throw std::runtime_error("Vertex shader path is not set");
    }

    if (RawFragmentShaderPath == "" || CompiledFragmentShaderPath == "") {
        throw std::runtime_error("Fragment shader path is not set");
    }
}