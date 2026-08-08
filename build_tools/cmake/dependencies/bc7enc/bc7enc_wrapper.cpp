#include "bc7enc_wrapper.hpp"
#include "bc7enc.h"

void bc7enc_init() {
    bc7enc_compress_block_init();
}

int bc7enc_encode_block(
    uint8_t *dst_bc7,
    const uint8_t *src_rgba,
    uint32_t mode_mask,
    uint32_t max_partitions,
    uint32_t uber_level,
    int perceptual) {
    bc7enc_compress_block_params params;

    bc7enc_compress_block_params_init(&params);

    params.m_mode_mask = mode_mask;
    params.m_max_partitions = max_partitions;
    params.m_uber_level = uber_level;
    params.m_perceptual = perceptual != 0;

    return bc7enc_compress_block(
               dst_bc7,
               src_rgba,
               &params)
               ? 1
               : 0;
}