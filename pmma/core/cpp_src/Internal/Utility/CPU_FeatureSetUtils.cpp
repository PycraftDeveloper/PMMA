#if defined(_MSC_VER)
  #include <intrin.h>
#elif defined(__GNUC__) || defined(__clang__)
  #include <cpuid.h>
#endif

#include <cstdint>

#include "Internal/Utility/CPU_FeatureSetUtils.hpp"

// Wrapper to invoke CPUID with eax and ecx arguments
static void cpuid(int32_t out[4], int32_t eax, int32_t ecx) {
#if defined(_MSC_VER)
    __cpuidex(out, eax, ecx);
#else
    __cpuid_count(eax, ecx, out[0], out[1], out[2], out[3]);
#endif
}

// Wrapper to invoke XGETBV (reads extended control register XCR0)
static uint64_t xgetbv(uint32_t index) {
#if defined(_MSC_VER)
    return _xgetbv(index);
#elif defined(__GNUC__) || defined(__clang__)
    uint32_t eax, edx;
    __asm__ volatile (
        "xgetbv"
        : "=a"(eax), "=d"(edx)
        : "c"(index)
    );
    return (uint64_t(edx) << 32) | eax;
#else
    return 0;
#endif
}

// Check if OS has enabled AVX state via XCR0[2:1] == 11b
static bool os_supports_avx() {
    // Bit 1 = XMM state, Bit 2 = YMM state
    const uint64_t mask = (1ULL << 1) | (1ULL << 2);
    return (xgetbv(0) & mask) == mask;
}

bool CPP_CPU_FeatureSetUtils::SupportsAVX2() {
    int32_t info[4];
    // Leaf 1: check OSXSAVE and AVX bit
    cpuid(info, 1, 0);
    bool has_osxsave = (info[2] & (1 << 27)) != 0;
    bool has_avx     = (info[2] & (1 << 28)) != 0;
    if (!has_osxsave || !has_avx || !os_supports_avx()) {
        return false;
    }

    // Leaf 7 subleaf 0: check AVX2 bit (EBX[5])
    cpuid(info, 7, 0);

    return (info[1] & (1 << 5)) != 0;
}

bool CPP_CPU_FeatureSetUtils::SupportsAVX512() { // AVX512f ONLY for now
    int32_t info[4];

    // Leaf 1: check OSXSAVE and AVX bit
    cpuid(info, 1, 0);
    bool has_osxsave = (info[2] & (1 << 27)) != 0;
    bool has_avx     = (info[2] & (1 << 28)) != 0;
    if (!has_osxsave || !has_avx) {
        return false;
    }

    // For AVX-512, OS must enable opmask, ZMM_Hi256, and Hi16_ZMM states: XCR0[7:5] == 111b
    const uint64_t mask512 = (1ULL << 5) | (1ULL << 6) | (1ULL << 7);
    if ((xgetbv(0) & mask512) != mask512) {
        return false;
    }

    // Leaf 7 subleaf 0: check AVX-512F (EBX[16]) and AVX-512DQ (EBX[17])
    cpuid(info, 7, 0);
    bool has_avx512f  = (info[1] & (1 << 16)) != 0;
    bool has_avx512dq = (info[1] & (1 << 17)) != 0;

    return has_avx512f && has_avx512dq;
}