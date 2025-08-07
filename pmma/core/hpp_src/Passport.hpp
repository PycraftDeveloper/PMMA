#pragma once
#include "PMMA_Exports.hpp"

#include <string>

class EXPORT CPP_Passport {
    public:
        std::string ProductName = "";
        std::string ProductSubName = "";
        std::string CompanyName = "";
        std::string ProductVersion = "";
        std::string ProductPath = "";
        std::string LoggingPath = "";
        bool IsRegistered = false;

        CPP_Passport();
        ~CPP_Passport();

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

        inline void SetLoggingPath(std::string NewLoggingPath) {
            LoggingPath = NewLoggingPath;
            IsRegistered = false;
        }

        inline void Register() {
            IsRegistered = true;
        }

        inline bool GetIsRegistered() {
            return IsRegistered;
        }

        inline std::string GetProductName() {
            return ProductName;
        }

        inline std::string GetProductSubName() {
            return ProductSubName;
        }

        inline std::string GetCompanyName() {
            return CompanyName;
        }

        inline std::string GetProductVersion() {
            return ProductVersion;
        }

        inline std::string GetProductPath() {
            return ProductPath;
        }

        inline std::string GetLoggingPath() {
            return LoggingPath;
        }
};