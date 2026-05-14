$input a_position, a_texcoord0, i_data0, i_data1
$output v_uv, v_col

#include "common.sh"

uniform mat4 OrthDisplayProj;
uniform vec4 u_colorInfo;

SAMPLER2D(s_colorTex, 0);

vec2 Unpack2Values(float data) {
    uint PackedData = floatBitsToUint(data);

    return vec2(float(PackedData & 0xFFFFu), float(PackedData >> 16u));
}

vec3 Unpack3Values(float data) {
    uint PackedData = floatBitsToUint(data);

    uint val_three = (PackedData >> 24u) & 0xFFu;
    uint val_two   = (PackedData >> 16u) & 0xFFu;
    uint val_one   = (PackedData >> 8u)  & 0xFFu;
    return vec3(float(val_one), float(val_two), float(val_three));
}

vec4 ExtractColor(float ColorIndex) {
    float idxF = floor(ColorIndex + 0.5);

    float w = u_colorInfo.x;
    float h = u_colorInfo.y;

    float x = mod(idxF, w);
    float y = floor(idxF / w);

    vec2 color_uv = vec2((x + 0.5) / w,
                (y + 0.5) / h);

    return texture2DLod(s_colorTex, color_uv, 0.0);
}

void main()
{
    vec2 Offset = Unpack2Values(i_data0.x);
    vec2 Size = Unpack2Values(i_data0.y);
    vec3 PointCountWidthGradientType = Unpack3Values(i_data0.z);
    float Rotation = i_data0.w;
    float ColorIndex = i_data1.x;
    float ShapeType = i_data1.y;
    vec2 TexturePosition = Unpack2Values(i_data1.z) / vec2(u_colorInfo.xy);
    vec2 TextureSize = Unpack2Values(i_data1.w) / vec2(u_colorInfo.xy);

    vec2 world = Offset + a_position.xy * Size;

    gl_Position = mul(OrthDisplayProj, vec4(world, 0.0, 1.0));

    v_uv = a_texcoord0;
    v_col = ExtractColor(ColorIndex); // no color (or black/transparent) here
}