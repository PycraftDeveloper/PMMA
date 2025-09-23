#pragma once

struct GlyphInfo {
    uint16_t atlasX, atlasY;
    uint16_t width, height;
    int16_t  bearingX, bearingY;
    uint16_t advance;
};

struct CharacterData {
    float x, y; // 8 bytes
    float col_index, padding0; // 8 bytes (with padding)
    float u_tex_coord, v_tex_coord; //  8 bytes
};