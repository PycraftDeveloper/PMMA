#pragma once
#include "PMMA_Exports.hpp"

#include <string>

class EXPORT CPP_Logger {
    public:
        // For public use
        void LogDebug(std::string ID, std::string Content, std::string ProductName);
        void LogWarn(std::string ID, std::string Content, std::string ProductName);
        void LogError(std::string ID, std::string Content, std::string ProductName);

        // For PMMA's Cython and Python API
        void InternalLogDebug(std::string ID, std::string Content);
        void InternalLogWarn(std::string ID, std::string Content);
        void InternalLogError(std::string ID, std::string Content);
};