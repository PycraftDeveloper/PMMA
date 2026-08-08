#include "bc7dec_wrapper.hpp"

#include "bc7decomp.h"

bool bc7_decode_block(
    std::uint8_t *dst_rgba,
    const std::uint8_t *src_bc7) {
    if (dst_rgba == nullptr || src_bc7 == nullptr)
        return false;

    // BC7 block: 16 bytes
    // RGBA 4x4 block: 16 pixels * 4 bytes = 64 bytes
    //
    // bc7decomp::color_rgba is exactly 4 bytes, so the output
    // buffer can be used directly as a color_rgba[16] array.

    auto *pixels =
        reinterpret_cast<bc7decomp::color_rgba *>(dst_rgba);

    return bc7decomp::unpack_bc7(
        src_bc7,
        pixels);
}