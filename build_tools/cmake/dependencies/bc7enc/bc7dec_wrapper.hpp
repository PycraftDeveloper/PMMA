#pragma once

#include <cstdint>

#ifdef _WIN32
#ifdef BC7ENC_EXPORTS
#define BC7DEC_API __declspec(dllexport)
#else
#define BC7DEC_API __declspec(dllimport)
#endif
#else
#define BC7DEC_API
#endif

#ifdef __cplusplus
extern "C" {
#endif

BC7DEC_API bool bc7_decode_block(
    std::uint8_t *dst_rgba,
    const std::uint8_t *src_bc7);

#ifdef __cplusplus
}
#endif