#pragma once
#include "PMMA_Exports.hpp"

#include <string>
#include <filesystem>
#include <fstream>
#include <algorithm>
#include <cstdlib>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "General.hpp"
#include "Logger.hpp"

class CPP_Shader {
    private:
        bgfx::ProgramHandle ShaderProgram = BGFX_INVALID_HANDLE;
        CPP_Logger* Logger;

        std::string RawVertexShaderPath = "";
        std::string RawFragmentShaderPath = "";
        std::string CompiledVertexShaderPath = "";
        std::string CompiledFragmentShaderPath = "";

        bool IsCompiled = false;
        bool IsInternalShader = false;

        void CompileShader(bool InternalShader);

        void CompileShaderComponent(std::string RawFilePath, std::string CompiledFilePath, std::string Type);

        std::string GetGraphicsProfile() {
            std::string GraphicsBackend = CPP_General::GetGraphicsBackend();
            if (GraphicsBackend == CPP_Constants::GraphicsBackends::OPENGL_ES) {
                return "100_es";
            } else if (GraphicsBackend == CPP_Constants::GraphicsBackends::DIRECT3D11 || GraphicsBackend == CPP_Constants::GraphicsBackends::DIRECT3D12) {
                return "s_4_0";
            } else if (GraphicsBackend == CPP_Constants::GraphicsBackends::METAL) {
                return "metal";
            } else if (GraphicsBackend == CPP_Constants::GraphicsBackends::GNM) {
                return "pssl";
            } else if (GraphicsBackend == CPP_Constants::GraphicsBackends::VULKAN) {
                return "spirv";
            } else if (GraphicsBackend == CPP_Constants::GraphicsBackends::OPENGL) {
                return "120";
            } else {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
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
        ~CPP_Shader() {
            if (bgfx::isValid(ShaderProgram)) {
                bgfx::destroy(ShaderProgram);
            }

            if (Logger != nullptr) {
                delete Logger;
                Logger = nullptr;
            }
        }

        void LoadShader(std::string VertexShaderPath, std::string FragmentShaderPath, bool InternalShader) {
            bool IsCompiled;
            if (VertexShaderPath.size() >= 5 && VertexShaderPath.substr(VertexShaderPath.size() - 5) == ".bin") {
                IsCompiled = true;
                CompiledVertexShaderPath = VertexShaderPath;
                RawVertexShaderPath = "";
            } else {
                IsCompiled = false;
                RawVertexShaderPath = VertexShaderPath;
                CompiledVertexShaderPath = "";
            }

            if (FragmentShaderPath.size() >= 5 && FragmentShaderPath.substr(FragmentShaderPath.size() - 5) == ".bin") {
                IsCompiled = true;
                CompiledFragmentShaderPath = FragmentShaderPath;
                RawFragmentShaderPath = "";
            } else {
                IsCompiled = false;
                RawFragmentShaderPath = FragmentShaderPath;
                CompiledFragmentShaderPath = "";
            }

            CompileShader(InternalShader);
        }

        void LoadVertexShader(std::string VertexShaderPath, bool InternalShader) {
            bool IsCompiled;
            if (VertexShaderPath.size() >= 5 && VertexShaderPath.substr(VertexShaderPath.size() - 5) == ".bin") {
                IsCompiled = true;
                CompiledVertexShaderPath = VertexShaderPath;
                RawVertexShaderPath = "";
            } else {
                IsCompiled = false;
                RawVertexShaderPath = VertexShaderPath;
                CompiledVertexShaderPath = "";
            }

            CompileShader(InternalShader);
        }

        void LoadFragmentShader(std::string FragmentShaderPath, bool InternalShader) {
            bool IsCompiled;
            if (FragmentShaderPath.size() >= 5 && FragmentShaderPath.substr(FragmentShaderPath.size() - 5) == ".bin") {
                IsCompiled = true;
                CompiledFragmentShaderPath = FragmentShaderPath;
                RawFragmentShaderPath = "";
            } else {
                IsCompiled = false;
                RawFragmentShaderPath = FragmentShaderPath;
                CompiledFragmentShaderPath = "";
            }

            CompileShader(InternalShader);
        }

        void LoadShaderFromFolder(std::string FolderPath, bool InternalShader) {
            bool IsCompiled = false;
            try {
                for (const auto& entry : std::filesystem::directory_iterator(FolderPath)) {
                    std::string FileName = entry.path().filename().string();
                    std::string FilePath = entry.path().string();

                    if (FileName.size() >= 7 && FileName.substr(FileName.size() - 5) == ".bin") {
                        IsCompiled = true;
                    } else {
                        IsCompiled = false;
                    }

                    std::string LowerFileName = FileName;
                    std::transform(LowerFileName.begin(), LowerFileName.end(), LowerFileName.begin(), ::tolower);
                    if (LowerFileName.find("vertex") != std::string::npos) {
                        if (IsCompiled) {
                            CompiledVertexShaderPath = FilePath;
                            RawVertexShaderPath = "";
                        } else {
                            RawVertexShaderPath = FilePath;
                            CompiledVertexShaderPath = "";
                        }
                    } else if (LowerFileName.find("fragment") != std::string::npos) {
                        if (IsCompiled) {
                            CompiledFragmentShaderPath = FilePath;
                            RawFragmentShaderPath = "";
                        } else {
                            RawFragmentShaderPath = FilePath;
                            CompiledFragmentShaderPath = "";
                        }
                    } else if (LowerFileName.substr(0, 3) == "vs_") {
                        if (IsCompiled) {
                            CompiledVertexShaderPath = FilePath;
                            RawVertexShaderPath = "";
                        } else {
                            RawVertexShaderPath = FilePath;
                            CompiledVertexShaderPath = "";
                        }
                    } else if (LowerFileName.substr(0, 3) == "fs_") {
                        if (IsCompiled) {
                            CompiledFragmentShaderPath = FilePath;
                            RawFragmentShaderPath = "";
                        } else {
                            RawFragmentShaderPath = FilePath;
                            CompiledFragmentShaderPath = "";
                        }
                    }

                    if ((CompiledVertexShaderPath != "" || RawVertexShaderPath != "") &&
                            (CompiledFragmentShaderPath != "" || RawFragmentShaderPath != "")) {
                        break;
                    }
                }
            } catch (const std::filesystem::filesystem_error& error) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }

                Logger->InternalLogWarn(
                    48,
                    "Whilst looking for shader files in the folder: '" +
                    FolderPath + "' the following filesystem error occurred: '" +
                    error.what() + "'");
            }

            CompileShader(InternalShader);
        }

        bgfx::ProgramHandle Use();
};