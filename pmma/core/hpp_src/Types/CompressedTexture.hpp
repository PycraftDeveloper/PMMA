#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <fstream>
#include <iostream>
#include <string>

#include <zstd.h>

#include "Internal/Rendering/Core2D/Base.hpp"

namespace PMMA::Types {
class EXPORT CompressedTexture {
private:
    std::string Path = "";

public:
    PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *TextureProperties = nullptr;
    bool IsTextureEnabled = false;

    ~CompressedTexture();

    void Load(std::string TexturePath);
    void Load();

    void InternalLoad();

    inline bool LoadCached(
        const std::string &CachedTexturePath) {
        std::ifstream file(
            CachedTexturePath,
            std::ios::binary);

        if (!file.is_open()) {
            return false;
        }

        char Magic[4];

        file.read(
            Magic,
            sizeof(Magic));

        if (memcmp(Magic, "PMTX", 4) != 0) {
            return false;
        }

        uint32_t Version = 0;

        file.read(
            reinterpret_cast<char *>(&Version),
            sizeof(Version));

        constexpr uint32_t CurrentVersion = 1;

        if (Version != CurrentVersion) {
            return false;
        }

        uint8_t Transparent = 0;

        file.read(
            reinterpret_cast<char *>(&Transparent),
            sizeof(Transparent));

        if (Transparent > 1) {
            return false;
        }

        TextureProperties->Transparent =
            Transparent != 0;

        uint8_t MipCount = 0;

        file.read(
            reinterpret_cast<char *>(&MipCount),
            sizeof(MipCount));

        if (MipCount == 0 ||
            MipCount > 32) {

            return false;
        }

        std::vector<PMMA::Internal::Rendering::Core2D::MipData>
            LoadedMipChain;

        LoadedMipChain.reserve(
            MipCount);

        for (uint32_t i = 0;
             i < MipCount;
             i++) {

            PMMA::Internal::Rendering::Core2D::MipData mip;

            //
            // Logical mip size.
            //
            file.read(
                reinterpret_cast<char *>(&mip.Size[0]),
                sizeof(uint16_t));

            file.read(
                reinterpret_cast<char *>(&mip.Size[1]),
                sizeof(uint16_t));

            //
            // Padding amount.
            //
            file.read(
                reinterpret_cast<char *>(&mip.Padding),
                sizeof(uint8_t));

            uint32_t CompressedSize = 0;
            uint32_t RawSize = 0;

            file.read(
                reinterpret_cast<char *>(&CompressedSize),
                sizeof(uint32_t));

            file.read(
                reinterpret_cast<char *>(&RawSize),
                sizeof(uint32_t));

            if (mip.Size[0] == 0 ||
                mip.Size[1] == 0) {

                return false;
            }

            uint64_t BlocksX =
                (static_cast<uint64_t>(mip.Size[0]) + 3) / 4;

            uint64_t BlocksY =
                (static_cast<uint64_t>(mip.Size[1]) + 3) / 4;

            uint64_t ExpectedSize =
                BlocksX * BlocksY * 16;

            if (RawSize != ExpectedSize) {
                return false;
            }

            //
            // Safety check before allocation.
            //
            if (CompressedSize == 0 ||
                RawSize == 0) {

                return false;
            }

            std::vector<uint8_t>
                CompressedData(
                    CompressedSize);

            file.read(
                reinterpret_cast<char *>(
                    CompressedData.data()),
                CompressedSize);

            if (file.fail()) {
                return false;
            }

            mip.PixelData.resize(
                RawSize);

            size_t DecompressedSize =
                ZSTD_decompress(
                    mip.PixelData.data(),
                    RawSize,
                    CompressedData.data(),
                    CompressedSize);

            if (ZSTD_isError(DecompressedSize)) {
                std::cout
                    << "Failed to open cache: zstd decompression failed: "
                    << ZSTD_getErrorName(DecompressedSize)
                    << std::endl;

                return false;
            }

            if (DecompressedSize != RawSize) {

                return false;
            }

            LoadedMipChain.push_back(
                std::move(mip));
        }

        if (file.fail()) {
            return false;
        }

        TextureProperties->MipChain =
            std::move(
                LoadedMipChain);

        TextureProperties->MipLevels =
            MipCount;

        return true;
    }

    inline void SaveTextureCache(
        const std::string &path,
        const PMMA::Internal::Rendering::Core2D::CompressedTextureProperty &texture) {

        std::ofstream file(
            path,
            std::ios::binary);

        if (!file) {
            throw std::runtime_error(
                "Failed to create texture cache.");
        }

        file.write("PMTX", 4);

        uint32_t Version = 1;

        file.write(
            reinterpret_cast<char *>(&Version),
            sizeof(Version));

        const uint8_t Transparent =
            texture.Transparent ? 1 : 0;

        file.write(
            reinterpret_cast<const char *>(&Transparent),
            sizeof(Transparent));

        uint8_t MipCount =
            static_cast<uint8_t>(
                texture.MipChain.size());

        file.write(
            reinterpret_cast<char *>(&MipCount),
            sizeof(MipCount));

        for (const auto &mip : texture.MipChain) {
            file.write(
                reinterpret_cast<const char *>(&mip.Size[0]),
                sizeof(uint16_t));

            file.write(
                reinterpret_cast<const char *>(&mip.Size[1]),
                sizeof(uint16_t));

            file.write(
                reinterpret_cast<const char *>(&mip.Padding),
                sizeof(uint8_t));

            uint32_t rawSize =
                static_cast<uint32_t>(
                    mip.PixelData.size());

            size_t maxCompressedSize =
                ZSTD_compressBound(
                    rawSize);

            std::vector<uint8_t> compressedData(
                maxCompressedSize);

            size_t compressedSize =
                ZSTD_compress(
                    compressedData.data(),
                    compressedData.size(),
                    mip.PixelData.data(),
                    rawSize,
                    3); // zstd level

            if (ZSTD_isError(compressedSize)) {
                throw std::runtime_error(
                    ZSTD_getErrorName(compressedSize));
            }

            uint32_t compressedSize32 =
                static_cast<uint32_t>(
                    compressedSize);

            file.write(
                reinterpret_cast<char *>(&compressedSize32),
                sizeof(uint32_t));

            file.write(
                reinterpret_cast<char *>(&rawSize),
                sizeof(uint32_t));

            file.write(
                reinterpret_cast<const char *>(
                    compressedData.data()),
                compressedSize32);
        }
    }

    void Unload();

    void Enable();

    inline void Disable() {
        IsTextureEnabled = false;
    }

    inline bool IsEnabled() {
        return IsTextureEnabled;
    }

    void GetSize(uint16_t *size);

    unsigned char GetChannels();

    uint32_t GetReferences();

    inline bool IsLoaded() {
        return TextureProperties != nullptr;
    }

    uint16_t GetWidth();
    uint16_t GetHeight();

    std::string GetPath();
};
} // namespace PMMA::Types