#pragma once
#include "PMMA_Exports.hpp"

#include <string>
#include <filesystem>
#include <fstream>
#include <algorithm>
#include <cstdlib>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

class CPP_Shader {
    private:
        bgfx::ProgramHandle ShaderProgram = BGFX_INVALID_HANDLE;

        std::string RawVertexShaderPath = "";
        std::string RawFragmentShaderPath = "";
        std::string CompiledVertexShaderPath = "";
        std::string CompiledFragmentShaderPath = "";

        bool IsLoaded = false;

    public:
        void LoadShader(std::string VertexShaderPath, std::string FragmentShaderPath) {
            IsLoaded = false;

            bool IsCompiled;
            if (VertexShaderPath.size() >= 5 && VertexShaderPath.substr(VertexShaderPath.size() - 5) == ".bin") {
                IsCompiled = true;
                CompiledVertexShaderPath = VertexShaderPath;
            } else {
                IsCompiled = false;
                RawVertexShaderPath = VertexShaderPath;
            }

            if (FragmentShaderPath.size() >= 5 && FragmentShaderPath.substr(FragmentShaderPath.size() - 5) == ".bin") {
                IsCompiled = true;
                CompiledFragmentShaderPath = FragmentShaderPath;
            } else {
                IsCompiled = false;
                RawFragmentShaderPath = FragmentShaderPath;
            }
        }

        void LoadVertexShader(std::string VertexShaderPath) {
            IsLoaded = false;

            bool IsCompiled;
            if (VertexShaderPath.size() >= 5 && VertexShaderPath.substr(VertexShaderPath.size() - 5) == ".bin") {
                IsCompiled = true;
                CompiledVertexShaderPath = VertexShaderPath;
            } else {
                IsCompiled = false;
                RawVertexShaderPath = VertexShaderPath;
            }
        }

        void LoadFragmentShader(std::string FragmentShaderPath) {
            IsLoaded = false;

            bool IsCompiled;
            if (FragmentShaderPath.size() >= 5 && FragmentShaderPath.substr(FragmentShaderPath.size() - 5) == ".bin") {
                IsCompiled = true;
                CompiledFragmentShaderPath = FragmentShaderPath;
            } else {
                IsCompiled = false;
                RawFragmentShaderPath = FragmentShaderPath;
            }
        }

        void LoadShaderFromFolder(std::string FolderPath) {
            IsLoaded = false;

            bool IsCompiled = false;
            try {
                for (const auto& entry : std::filesystem::directory_iterator(FolderPath)) {
                    std::string FileName = entry.path().filename().string();

                    if (FileName.size() >= 7 && FileName.substr(FileName.size() - 5) == ".bin") {
                        IsCompiled = true;
                    } else {
                        IsCompiled = false;
                    }

                    std::string LowerFileName = FileName;
                    std::transform(LowerFileName.begin(), LowerFileName.end(), LowerFileName.begin(), ::tolower);
                    if (LowerFileName.find("vertex") != std::string::npos) {
                        if (IsCompiled) {
                            CompiledVertexShaderPath = FileName;
                        } else {
                            RawVertexShaderPath = FileName;
                        }
                    } else if (LowerFileName.find("fragment") != std::string::npos) {
                        if (IsCompiled) {
                            CompiledFragmentShaderPath = FileName;
                        } else {
                            RawFragmentShaderPath = FileName;
                        }
                    } else if (LowerFileName.substr(0, 3) == "vs_") {
                        if (IsCompiled) {
                            CompiledVertexShaderPath = FileName;
                        } else {
                            RawVertexShaderPath = FileName;
                        }
                    } else if (LowerFileName.substr(0, 3) == "fs_") {
                        if (IsCompiled) {
                            CompiledFragmentShaderPath = FileName;
                        } else {
                            RawFragmentShaderPath = FileName;
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
        }

        bgfx::ProgramHandle Use();
};