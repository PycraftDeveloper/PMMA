#pragma once

#include <vector>

#include <glm/glm.hpp>

#include "Internal/Utility/FontUtils.hpp"

typedef struct FT_LibraryRec_ *FT_Library;
typedef struct FT_FaceRec_ *FT_Face;

class CPP_TextRenderer;
class CPP_Shader;

class CPP_TextRendererPipelineManager {
    private:
        std::vector<GlyphInstance> glyphs;
        FontAtlas* atlas = nullptr;
        bgfx::VertexBufferHandle m_vbh = BGFX_INVALID_HANDLE;
        bgfx::VertexLayout m_vlayout;
        bgfx::VertexLayout m_instanceDecl;

        bgfx::UniformHandle u_proj = BGFX_INVALID_HANDLE;
        bgfx::UniformHandle s_tex  = BGFX_INVALID_HANDLE;

        CPP_Shader* ShaderProgram = nullptr;

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