#pragma once
#include "PMMA_Exports.hpp"

#include <algorithm>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <future>
#include <string>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "General.hpp"
#include "Logger.hpp"

namespace PMMA::Graphics {
class Shader {
private:
    std::future<void> CompileShaderFuture;

    bgfx::ProgramHandle ShaderProgram = BGFX_INVALID_HANDLE;
    PMMA::Logger *Logger;

    std::string RawVertexShaderPath = "";
    std::string RawFragmentShaderPath = "";
    std::string CompiledVertexShaderPath = "";
    std::string CompiledFragmentShaderPath = "";

    bool IsCompiled = false;
    bool IsInternalShader = false;

    void CompileShader(bool InternalShader);

    void CompileShaderComponent(std::string RawFilePath, std::string CompiledFilePath, std::string Type);

    std::string GetGraphicsProfile() {
        std::string GraphicsBackend = PMMA::General::GetGraphicsBackend();
        if (GraphicsBackend == PMMA::Constants::GraphicsBackends::OPENGL_ES) {
            return "100_es";
        } else if (GraphicsBackend == PMMA::Constants::GraphicsBackends::DIRECT3D11 || GraphicsBackend == PMMA::Constants::GraphicsBackends::DIRECT3D12) {
            return "s_4_0";
        } else if (GraphicsBackend == PMMA::Constants::GraphicsBackends::METAL) {
            return "metal";
        } else if (GraphicsBackend == PMMA::Constants::GraphicsBackends::GNM) {
            return "pssl";
        } else if (GraphicsBackend == PMMA::Constants::GraphicsBackends::VULKAN) {
            return "spirv";
        } else if (GraphicsBackend == PMMA::Constants::GraphicsBackends::OPENGL) {
            return "150";
        } else {
            if (Logger == nullptr) {
                Logger = new PMMA::Logger();
            }

            Logger->InternalLogError(
                58,
                "Cannot compile shader as the graphics backend '" +
                    GraphicsBackend + "' is not recognized. Please report \
this as a GitHub issue so we can add support for it.");

            throw std::runtime_error("Cannot compile shader for " + GraphicsBackend + " as its profile is not known.");
        }
    }

public:
    ~Shader() {
        if (CompileShaderFuture.valid()) {
            CompileShaderFuture.wait();
        }

        if (bgfx::isValid(ShaderProgram)) {
            bgfx::destroy(ShaderProgram);
        }

        if (Logger != nullptr) {
            delete Logger;
            Logger = nullptr;
        }
    }

    void CreateShader();

    void LoadShader(std::string VertexShaderPath, std::string FragmentShaderPath, bool InternalShader);

    void LoadVertexShader(std::string VertexShaderPath, bool InternalShader);

    void LoadFragmentShader(std::string FragmentShaderPath, bool InternalShader);

    void LoadShaderFromFolder(std::string FolderPath, bool InternalShader);

    bgfx::ProgramHandle Use();
};
} // namespace PMMA::Graphics