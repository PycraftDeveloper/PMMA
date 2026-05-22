$input a_position , a_texcoord0 , i_data0 , i_data1 , i_data2
$output v_uv , v_data0 , v_data1 , v_data2 , v_data3 , v_col0

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
    vec2 ShapeTypeWidth = Unpack2Values(i_data1.y);
    vec2 RotationShapeProperty = Unpack2Values(i_data0.w);
    float ColorIndex = i_data1.x;
    vec2 TextureStart = Unpack2Values(i_data1.z) / vec2(u_colorInfo.xy);
    vec2 TextureEnd = Unpack2Values(i_data1.w) / vec2(u_colorInfo.xy);
    vec2 LineStart = Unpack2Values(i_data2.x);
    vec2 LineEnd = Unpack2Values(i_data2.y);

    v_data0.x = PointCountGradientType.x; // Point Count
    v_data0.y = PointCountGradientType.y; // Gradient Type
    v_data0.z = ColorIndex;
    v_data0.w = ShapeTypeWidth.x; // Shape Type
    v_data1.x = ShapeTypeWidth.y; // Width
    v_data1.y = TextureStart.x;
    v_data1.z = TextureStart.y;
    v_data1.w = TextureEnd.x;
    v_data2.x = TextureEnd.y;
    v_data2.y = RotationShapeProperty.y; // Shape Property (corner radius, end angle exct...)
    v_data2.z = LineStart.x;
    v_data2.w = LineStart.y;
    v_data3.x = LineEnd.x;
    v_data3.y = LineEnd.y;

    // Rotation
    float Rotation = (RotationShapeProperty.x / 182.0) * (3.14159265359 / 180.0);
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
}
