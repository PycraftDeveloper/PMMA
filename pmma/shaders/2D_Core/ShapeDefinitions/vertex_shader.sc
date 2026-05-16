$input a_position, a_texcoord0, i_data0, i_data1
$output v_uv, v_col0, v_col1, v_col2, v_col3, v_data2, v_data3

#include "common.sh"

uniform mat4 OrthDisplayProj;
uniform vec4 u_colorInfo;

SAMPLER2D(s_colorTex, 0);

vec2 Unpack2Values(float data) {
    uint PackedData = floatBitsToUint(data);

    return vec2(float(PackedData & 0xFFFFu), float(PackedData >> 16u));
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
    // Instance Data Extraction
    vec2 Offset = Unpack2Values(i_data0.x);
    vec2 Size = Unpack2Values(i_data0.y);
    vec2 PointCountGradientType = Unpack2Values(i_data0.z);
    float Rotation = i_data0.w;
    float ColorIndex = i_data1.x;

    v_data2.x = i_data0.z;
    v_data2.y = i_data1.y;
    v_data2.z = i_data1.z;
    v_data2.w = i_data1.w;

    v_data3.x = u_colorInfo.x;
    v_data3.y = u_colorInfo.y;

    // Rotation
    float cos_a = cos(Rotation);
    float sin_a = sin(Rotation);
    float rotated_x = a_position.x * cos_a - a_position.y * sin_a;
    float rotated_y = a_position.x * sin_a + a_position.y * cos_a;

    // Positioning
    vec2 world = Offset + vec2(rotated_x, rotated_y) * Size;

    gl_Position = mul(OrthDisplayProj, vec4(world, 0.0, 1.0));

    // UV Passthrough
    v_uv = a_texcoord0;

    // Color Extraction
    v_col0 = ExtractColor(ColorIndex);
    v_col1 = vec4(0.0, 0.0, 0.0, 0.0);
    v_col2 = vec4(0.0, 0.0, 0.0, 0.0);
    v_col3 = vec4(0.0, 0.0, 0.0, 0.0);

    if (PointCountGradientType.y > 0.0) {
        v_col1 = ExtractColor(ColorIndex + 1);
    }

    if (PointCountGradientType.y > 13.0 && PointCountGradientType.y <= 26.0) {
        v_col2 = ExtractColor(ColorIndex + 2);
    }

    if (PointCountGradientType.y > 26.0) {
        v_col3 = ExtractColor(ColorIndex + 3);
    }
}