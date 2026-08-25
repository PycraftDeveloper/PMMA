#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <string>

namespace PMMA {
class EXPORT Passport {
public:
    std::string ProductName = "";
    std::string ProductSubName = "";
    std::string CompanyName = "";
    std::string ProductVersion = "";
    std::string ProductPath = "";
    std::string LoggingPath = "";
    std::string ProfilingPath = "";
    std::string TemporaryPath = "";
    bool IsRegistered = false;

    Passport();
    ~Passport();

    inline void SetProductName(std::string NewProductName) {
        ProductName = NewProductName;
        IsRegistered = false;
    }

    inline void SetProductSubName(std::string NewProductSubName) {
        ProductSubName = NewProductSubName;
        IsRegistered = false;
    }

    inline void SetCompanyName(std::string NewCompanyName) {
        CompanyName = NewCompanyName;
        IsRegistered = false;
    }

    inline void SetProductVersion(std::string NewProductVersion) {
        ProductVersion = NewProductVersion;
        IsRegistered = false;
    }

    inline void SetProductPath(std::string NewProductPath) {
        ProductPath = NewProductPath;
        IsRegistered = false;
    }

    inline void SetProfilingPath(std::string NewProfilingPath) {
        ProfilingPath = NewProfilingPath;
        IsRegistered = false;
    }

    inline void SetTemporaryPath(std::string NewTemporaryPath) {
        TemporaryPath = NewTemporaryPath;
        IsRegistered = false;
    }

    void SetLoggingPath(std::string NewLoggingPath, bool ExplicitlySet);

    void Register();

    inline bool GetIsRegistered() {
        return IsRegistered;
    }

    inline std::string GetProductName() {
        return ProductName;
    }

    inline bool GetIsProductNameSet() {
        return !ProductName.empty();
    }

    inline std::string GetProductSubName() {
        return ProductSubName;
    }

    inline bool GetIsProductSubNameSet() {
        return !ProductSubName.empty();
    }

    inline std::string GetCompanyName() {
        return CompanyName;
    }

    inline bool GetIsCompanyNameSet() {
        return !CompanyName.empty();
    }

    inline std::string GetProductVersion() {
        return ProductVersion;
    }

    inline bool GetIsProductVersionSet() {
        return !ProductVersion.empty();
    }

    inline std::string GetProductPath() {
        return ProductPath;
    }

    inline bool GetIsProductPathSet() {
        return !ProductPath.empty();
    }

    inline std::string GetLoggingPath() {
        return LoggingPath;
    }

    inline bool GetIsLoggingPathSet() {
        return !LoggingPath.empty();
    }

    inline std::string GetProfilingPath() {
        return ProfilingPath;
    }

    inline bool GetIsProfilingPathSet() {
        return !ProfilingPath.empty();
    }

    inline std::string GetTemporaryPath() {
        return TemporaryPath;
    }

    inline bool GetIsTemporaryPathSet() {
        return !TemporaryPath.empty();
    }
};
} // namespace PMMA