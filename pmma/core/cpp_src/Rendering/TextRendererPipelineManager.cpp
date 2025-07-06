#include <iostream>
#include <map>
#include <vector>

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glad/gl.h>
#include <GLFW/glfw3.h>
#include <ft2build.h>
#include FT_FREETYPE_H

#include "Rendering/TextRendererPipelineManager.hpp"

#include "OpenGL.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_TextRendererPipelineManager::CPP_TextRendererPipelineManager() {
    string vertex_shader_path[] = {"shaders", "text_renderer", "vertex_shader.glsl"};
    string fragment_shader_path[] = {"shaders", "text_renderer", "fragment_shader.glsl"};

    string vertex_shader = PMMA::PMMA_Location;
    for (const auto& part : vertex_shader_path) {
        vertex_shader += PMMA::PathSeparator + part;
    }

    string fragment_shader = PMMA::PMMA_Location;
    for (const auto& part : fragment_shader_path) {
        fragment_shader += PMMA::PathSeparator + part;
    }

    CPP_Shader Shader;
    shaderProgram = Shader.CreateShaderProgram(vertex_shader, fragment_shader);

    float quadVertices[] = {
        // positions   // texcoords
        0.0f, 1.0f,    0.0f, 1.0f,
        1.0f, 0.0f,    1.0f, 0.0f,
        0.0f, 0.0f,    0.0f, 0.0f,

        0.0f, 1.0f,    0.0f, 1.0f,
        1.0f, 1.0f,    1.0f, 1.0f,
        1.0f, 0.0f,    1.0f, 0.0f
    };

    glGenVertexArrays(1, &quadVAO);
    glGenBuffers(1, &quadVBO);
    glBindVertexArray(quadVAO);

    glBindBuffer(GL_ARRAY_BUFFER, quadVBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(quadVertices), quadVertices, GL_STATIC_DRAW);

    glEnableVertexAttribArray(0); // pos
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(1); // uv
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)(2 * sizeof(float)));

    glGenBuffers(1, &instanceVBO);
    glBindBuffer(GL_ARRAY_BUFFER, instanceVBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(GlyphInstance) * 1000, nullptr, GL_DYNAMIC_DRAW);

    int attrIndex = 2;

    // glyphPos (vec2)
    glEnableVertexAttribArray(attrIndex);
    glVertexAttribPointer(
        attrIndex,                          // Attribute index
        2,                                  // Number of components (vec2)
        GL_FLOAT,                           // Type
        GL_FALSE,                           // Normalized
        sizeof(GlyphInstance),             // Stride (size of one instance)
        (void*)offsetof(GlyphInstance, pos) // Offset to 'pos' in struct
    );
    glVertexAttribDivisor(attrIndex, 1);
    ++attrIndex;

    // glyphSize (vec2)
    glEnableVertexAttribArray(attrIndex);
    glVertexAttribPointer(
        attrIndex,
        2,
        GL_FLOAT,
        GL_FALSE,
        sizeof(GlyphInstance),
        (void*)offsetof(GlyphInstance, scale)
    );
    glVertexAttribDivisor(attrIndex, 1);
    ++attrIndex;

    // uvOrigin (vec2)
    glEnableVertexAttribArray(attrIndex);
    glVertexAttribPointer(
        attrIndex,
        2,
        GL_FLOAT,
        GL_FALSE,
        sizeof(GlyphInstance),
        (void*)offsetof(GlyphInstance, uvOrigin)
    );
    glVertexAttribDivisor(attrIndex, 1);
    ++attrIndex;

    // uvSize (vec2)
    glEnableVertexAttribArray(attrIndex);
    glVertexAttribPointer(
        attrIndex,
        2,
        GL_FLOAT,
        GL_FALSE,
        sizeof(GlyphInstance),
        (void*)offsetof(GlyphInstance, uvSize)
    );
    glVertexAttribDivisor(attrIndex, 1);
    ++attrIndex;

    // glyphForegroundColor (vec4)
    glEnableVertexAttribArray(attrIndex);
    glVertexAttribPointer(
        attrIndex,
        4, // vec4 has 4 components
        GL_FLOAT,
        GL_FALSE,
        sizeof(GlyphInstance),
        (void*)offsetof(GlyphInstance, foreground_color)
    );
    glVertexAttribDivisor(attrIndex, 1);
    ++attrIndex;

    // glyphBackgroundColor (vec4)
    glEnableVertexAttribArray(attrIndex);
    glVertexAttribPointer(
        attrIndex,
        4, // vec4 has 4 components
        GL_FLOAT,
        GL_FALSE,
        sizeof(GlyphInstance),
        (void*)offsetof(GlyphInstance, background_color)
    );
    glVertexAttribDivisor(attrIndex, 1);
    ++attrIndex;

    glBindVertexArray(0);

    glyphs.clear();
}

CPP_TextRendererPipelineManager::~CPP_TextRendererPipelineManager() {
    glDeleteVertexArrays(1, &quadVAO);
    glDeleteBuffers(1, &quadVBO);
    glDeleteBuffers(1, &instanceVBO);
    glDeleteProgram(shaderProgram);

    delete atlas;
    atlas = nullptr;
}

void CPP_TextRendererPipelineManager::DelayedSetup(string NewFont, unsigned int NewPixelHeight) {
    Font = NewFont;
    PixelHeight = NewPixelHeight;
    Setup = true;

    atlas = new FontAtlas(NewFont, NewPixelHeight);
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

        glyphs.push_back({
            glm::vec2(xpos, ypos),
            glm::vec2(ch.size),
            ch.uvOrigin,
            ch.uvSize,
            foreground_color,
            background_color
        });

        x += ch.advance >> 6;
    }
}

void CPP_TextRendererPipelineManager::InternalRender() {
    glUseProgram(shaderProgram);
    glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "projection"), 1, GL_FALSE, glm::value_ptr(PMMA::DisplayInstance->GetDisplayProjection()));

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    glBindBuffer(GL_ARRAY_BUFFER, instanceVBO);
    glBufferSubData(GL_ARRAY_BUFFER, 0, glyphs.size() * sizeof(GlyphInstance), glyphs.data());

    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, atlas->textureID);

    glBindVertexArray(quadVAO);
    glDrawArraysInstanced(GL_TRIANGLES, 0, 6, glyphs.size());
    glBindVertexArray(0);

    glDisable(GL_BLEND);
}