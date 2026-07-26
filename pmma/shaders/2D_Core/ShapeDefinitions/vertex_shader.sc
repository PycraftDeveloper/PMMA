$input a_position , a_texcoord0 , i_data0 , i_data1 , i_data2
$output v_uv , v_data0 , v_data1 , v_data2 , v_data3 , v_col0

#include "common.sh"

uniform mat4 OrthDisplayProj;
uniform vec4 u_textureInfo;
uniform vec4 HasTransparency;

SAMPLER2D(s_colorTex, 0);

vec2 Unpack2Values(float data) {
    uint PackedData = floatBitsToUint(data);

    return vec2(float(PackedData & 0xFFFFu), float(PackedData >> 16u));
}

vec4 ExtractColor(float ColorIndex) {
    float idxF = floor(ColorIndex + 0.5);

    float w = u_textureInfo.x;
    float h = u_textureInfo.y;

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
    vec2 RotationShapePropertyOne = Unpack2Values(i_data0.w);
    float ColorIndex = i_data1.x;
    vec2 TextureStart = Unpack2Values(i_data1.z) / vec2(u_textureInfo.zw);
    vec2 TextureSize = Unpack2Values(i_data1.w) / vec2(u_textureInfo.zw);
    vec2 ShapePropertyTwo = Unpack2Values(i_data2.x);
    vec2 ShapePropertyThree = Unpack2Values(i_data2.y);
    float Rotation = RotationShapePropertyOne.x * 0.0000960012; // equ to '/ 182' in RADIANS
    float depth = i_data2.z;

    v_data0.x = PointCountGradientType.x; // Point Count
    v_data0.y = PointCountGradientType.y; // Gradient Type
    v_data0.z = ColorIndex;
    v_data0.w = ShapeTypeWidth.x; // Shape Type
    v_data1.x = ShapeTypeWidth.y; // Width
    v_data1.y = TextureStart.x;
    v_data1.z = TextureStart.y;
    v_data1.w = TextureSize.x;
    v_data2.x = TextureSize.y;
    v_data2.y = RotationShapePropertyOne.y; // Shape Property (corner radius, end angle exct...)
    v_data2.z = ShapePropertyTwo.x;
    v_data2.w = ShapePropertyTwo.y;
    v_data3.x = ShapePropertyThree.x;
    v_data3.y = ShapePropertyThree.y;
    v_data3.z = HasTransparency.x;

    // 1. Scale the local vertex positions first
    vec2 scaled_pos = a_position * Size;

    // 2. Rotate the already-scaled positions
    float cos_a = cos(Rotation);
    float sin_a = sin(Rotation);
    float rotated_x = scaled_pos.x * cos_a - scaled_pos.y * sin_a;
    float rotated_y = scaled_pos.x * sin_a + scaled_pos.y * cos_a;

    // 3. Apply the translation offset
    vec2 world = Offset + vec2(rotated_x, rotated_y);

    gl_Position = mul(OrthDisplayProj, vec4(world, depth, 1.0));

    v_uv = a_texcoord0;

    v_col0 = ExtractColor(ColorIndex);
}
