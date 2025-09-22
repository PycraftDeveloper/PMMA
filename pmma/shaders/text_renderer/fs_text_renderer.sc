$input v_uv, v_color0
SAMPLER2D(u_fontAtlas, 0);

void main() {
    float alpha = texture2D(u_fontAtlas, v_uv).r;
    gl_FragColor = v_color0 * alpha;
}