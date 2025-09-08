$input v_texcoord, v_fg, v_bg
SAMPLER2D(s_tex, 0);

void main()
{
    float a = texture2D(s_tex, v_texcoord).r;

    vec4 col = mix(v_bg, v_fg, a);

    gl_FragColor = col;
}
