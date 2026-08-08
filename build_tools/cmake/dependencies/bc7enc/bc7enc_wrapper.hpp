#pragma once

#include <stdint.h>

#ifdef _WIN32
#ifdef BC7ENC_EXPORTS
#define BC7ENC_API __declspec(dllexport)
#else
#define BC7ENC_API __declspec(dllimport)
#endif
#else
#define BC7ENC_API
#endif

#ifdef __cplusplus
extern "C" {
#endif

BC7ENC_API void bc7enc_init();

BC7ENC_API int bc7enc_encode_block(
    uint8_t *dst_bc7,
    const uint8_t *src_rgba,
    uint32_t mode_mask,
    uint32_t max_partitions,
    uint32_t uber_level,
    int perceptual);

#ifdef __cplusplus
}
#endif