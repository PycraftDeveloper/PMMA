// CPP_TextRendererPipelineManager_BGFX.cpp
// BGFX rewrite of your OpenGL text renderer pipeline.
// Requires: bgfx, bimg, glm, FreeType (your FontAtlas BGFX version from earlier)

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>
#include <bx/math.h>

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

#include <ft2build.h>
#include FT_FREETYPE_H

#include "PMMA_Core.hpp"

using namespace std;

// Vertex format for the quad (non-instanced)
struct TextVertex {
    float x, y;   // position (2)
    float u, v;   // texcoord (2)
    static void init(bgfx::VertexLayout& layout) {
        layout.begin()
              .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
              .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
              .end();
    }
};

CPP_TextRendererPipelineManager::CPP_TextRendererPipelineManager() {
    // create static quad vb (two triangles, 6 vertices) in normalized quad space 0..1
    TextVertex::init(m_vlayout);

    TextVertex vertices[6] = {
        {0.0f, 1.0f, 0.0f, 1.0f},
        {1.0f, 0.0f, 1.0f, 0.0f},
        {0.0f, 0.0f, 0.0f, 0.0f},

        {0.0f, 1.0f, 0.0f, 1.0f},
        {1.0f, 1.0f, 1.0f, 1.0f},
        {1.0f, 0.0f, 1.0f, 0.0f}
    };

    const bgfx::Memory* mem = bgfx::copy(vertices, sizeof(vertices));
    m_vbh = bgfx::createVertexBuffer(mem, m_vlayout);

    // instance layout - map to BGFX attribute semantics.
    // We'll place our instance attributes in: a_texcoord1..4, a_color0, a_color1
    m_instanceDecl.begin()
        .add(bgfx::Attrib::TexCoord1, 2, bgfx::AttribType::Float)  // pos
        .add(bgfx::Attrib::TexCoord2, 2, bgfx::AttribType::Float)  // scale (size)
        .add(bgfx::Attrib::TexCoord3, 2, bgfx::AttribType::Float)  // uvOrigin
        .add(bgfx::Attrib::TexCoord4, 2, bgfx::AttribType::Float)  // uvSize
        .add(bgfx::Attrib::Color0,    4, bgfx::AttribType::Float)  // fgColor
        .add(bgfx::Attrib::Color1,    4, bgfx::AttribType::Float)  // bgColor
        .end();

    // Create uniforms
    u_proj = bgfx::createUniform("screen_space_one", bgfx::UniformType::Mat4);
    s_tex  = bgfx::createUniform("s_tex",  bgfx::UniformType::Sampler);

    string TextRendererShaderPath = PMMA_Registry::PMMA_Location
        + PMMA_Registry::PathSeparator + "shaders"
        + PMMA_Registry::PathSeparator + "text_renderer";

    ShaderProgram = new CPP_Shader();
    ShaderProgram->LoadShaderFromFolder(TextRendererShaderPath, true);

    glyphs.clear();
}

CPP_TextRendererPipelineManager::~CPP_TextRendererPipelineManager() {
    if (bgfx::isValid(m_vbh)) {
        bgfx::destroy(m_vbh);
    }
    if (bgfx::isValid(u_proj)) {
        bgfx::destroy(u_proj);
    }
    if (bgfx::isValid(s_tex)) {
        bgfx::destroy(s_tex);
    }

    if (atlas) {
        delete atlas;
        atlas = nullptr;
    }
}

void CPP_TextRendererPipelineManager::DelayedSetup(string NewFont, unsigned int NewPixelHeight) {
    Font = NewFont;
    PixelHeight = NewPixelHeight;
    Setup = true;

    atlas = new FontAtlas(NewFont, NewPixelHeight); // your BGFX FontAtlas from earlier
}

void CPP_TextRendererPipelineManager::AddRenderTarget(CPP_TextRenderer* NewObject) {
    std::string text = NewObject->Text;
    glm::vec2 pos = NewObject->Position;
    glm::vec4 foreground_color = NewObject->ForegroundColor;
    glm::vec4 background_color = NewObject->BackgroundColor;

    float x = pos.x;
    for (char c : text) {
        if (atlas->characters.count(c) == 0) {
            continue;
        }
        const Character& ch = atlas->characters[c];
        float xpos = x + ch.bearing.x;
        float ypos = pos.y + (atlas->BaseLine - ch.bearing.y);

        GlyphInstance gi;
        gi.pos[0] = xpos;  gi.pos[1] = ypos;
        gi.scale[0] = (float)ch.size.x; gi.scale[1] = (float)ch.size.y;
        gi.uvOrigin[0] = ch.uvOrigin.x; gi.uvOrigin[1] = ch.uvOrigin.y;
        gi.uvSize[0] = ch.uvSize.x; gi.uvSize[1] = ch.uvSize.y;
        gi.fgColor[0] = foreground_color.r; gi.fgColor[1] = foreground_color.g; gi.fgColor[2] = foreground_color.b; gi.fgColor[3] = foreground_color.a;
        gi.bgColor[0] = background_color.r; gi.bgColor[1] = background_color.g; gi.bgColor[2] = background_color.b; gi.bgColor[3] = background_color.a;

        glyphs.push_back(gi);

        x += (ch.advance >> 6);
    }
}

void CPP_TextRendererPipelineManager::Reset() {
    glyphs.clear();
}

void CPP_TextRendererPipelineManager::InternalRender() {
    if (glyphs.empty() || !atlas) return;

    // Allocate instance buffer and fill it
    const uint32_t num = (uint32_t)glyphs.size();
    bgfx::InstanceDataBuffer idb;
    bgfx::allocInstanceDataBuffer(&idb, num, (uint16_t)m_instanceDecl.getStride());
    if (idb.data == nullptr) {
        // allocation failed
        return;
    }

    // Copy data into idb.data (it must match the order of m_instanceDecl)
    // Our GlyphInstance binary layout matches the declaration order, so memcpy is OK.
    memcpy(idb.data, glyphs.data(), sizeof(GlyphInstance) * num);

    // Set state: blend (alpha), no culling, write RGB + A
    uint64_t state = BGFX_STATE_WRITE_RGB | BGFX_STATE_WRITE_A | BGFX_STATE_BLEND_ALPHA;

    // Set view (assume view 0; adapt if you use multiple views)
    const uint16_t view = 0;

    // Set vertex buffer (quad)
    bgfx::setVertexBuffer(0, m_vbh);

    // Set instance data
    bgfx::setInstanceDataBuffer(&idb);

    // Set projection uniform: expect projection matrix in pixel-space to put glyphs directly
    // We expect PMMA_Core::DisplayInstance->GetDisplayProjection() returns glm::mat4
    glm::mat4 proj = PMMA_Core::DisplayInstance->GetDisplayProjection();
    bgfx::setUniform(u_proj, glm::value_ptr(proj));

    // Bind texture (atlas texture handle) to slot 0
    bgfx::setTexture(0, s_tex, atlas->texture);

    // Submit
    bgfx::setState(state);
    bgfx::submit(view, ShaderProgram->Use());

    // Clear glyph list - original code kept glyphs until Reset() so keep consistent and don't clear here
}
