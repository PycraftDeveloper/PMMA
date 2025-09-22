struct GlyphInfo {
    uint16_t atlasX, atlasY;
    uint16_t width, height;
    int16_t  bearingX, bearingY;
    uint16_t advance;
};

struct TextInstance {
    std::string text;
    float x, y;
    uint32_t color;
    // Internal: filled by renderer
    struct DrawGlyph { float x, y, w, h; float u0, v0, u1, v1; uint32_t color; } *glyphs = nullptr; size_t glyphCount = 0;
    TextInstance(const std::string& t, float xx, float yy, uint32_t c) : text(t), x(xx), y(yy), color(c) {}
};