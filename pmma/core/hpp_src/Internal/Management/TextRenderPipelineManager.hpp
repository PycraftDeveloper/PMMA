#pragma once

#include <vector>

#include <glm/glm.hpp>

#include "Internal/Utility/FontUtils.hpp"

typedef struct FT_LibraryRec_ *FT_Library;
typedef struct FT_FaceRec_ *FT_Face;
typedef unsigned int GLuint;

class CPP_TextRenderer;

class CPP_TextRendererPipelineManager {
    private:
        GLuint quadVAO, quadVBO, instanceVBO;
        GLuint shaderProgram;
        std::vector<GlyphInstance> glyphs;
        FontAtlas* atlas = nullptr;

    public:
        std::string Font;
        unsigned int PixelHeight;
        bool Setup = false;

        CPP_TextRendererPipelineManager();
        ~CPP_TextRendererPipelineManager();

        void DelayedSetup(std::string path, unsigned int pixelHeight);

        void InternalRender();

        void AddRenderTarget(CPP_TextRenderer* NewObject);

        void Reset();
};