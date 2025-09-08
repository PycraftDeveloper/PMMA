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

class CPP_Shader {
    private:
        bgfx::ProgramHandle ShaderProgram = BGFX_INVALID_HANDLE;

        std::string RawVertexShaderPath = "";
        std::string RawFragmentShaderPath = "";
        std::string CompiledVertexShaderPath = "";
        std::string CompiledFragmentShaderPath = "";

        bool IsCompiled = false;

        void CompileShader(bool InternalShader);

        void CompileShaderComponent(string RawFilePath, string CompiledFilePath, string Type);

        std::string GetGraphicsProfile() {
            string GraphicsBackend = CPP_General::GetGraphicsBackend();
            if (GraphicsBackend == CPP_Constants::GRAPHICS_BACKEND_OPENGL_ES) {
                return "100_es";
            } else if (GraphicsBackend == CPP_Constants::GRAPHICS_BACKEND_DIRECT3D11 || GraphicsBackend == CPP_Constants::GRAPHICS_BACKEND_DIRECT3D12) {
                return "s_4_0";
            } else if (GraphicsBackend == CPP_Constants::GRAPHICS_BACKEND_METAL) {
                return "metal";
            } else if (GraphicsBackend == CPP_Constants::GRAPHICS_BACKEND_GNM) {
                return "pssl";
            } else if (GraphicsBackend == CPP_Constants::GRAPHICS_BACKEND_VULKAN) {
                return "spirv";
            } else if (GraphicsBackend == CPP_Constants::GRAPHICS_BACKEND_OPENGL) {
                return "120";
            } else {
                throw runtime_error("Cannot compile shader for " + GraphicsBackend + " as its profile is not known.");
            }
        }

    public:
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
            } catch (const std::filesystem::filesystem_error& e) {
                // Handle error (e.g., log it)
            }

            CompileShader(InternalShader);
        }

        bgfx::ProgramHandle Use();
};