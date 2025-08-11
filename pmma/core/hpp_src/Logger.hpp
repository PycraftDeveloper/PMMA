#pragma once
#include "PMMA_Exports.hpp"

#include <string>

class EXPORT CPP_Logger {
    public:
        void SetLogToFile(bool NewLogToFile);
        void SetLogToConsole(bool NewLogToConsole);
        void SetKeepCount(unsigned int NewKeepCount);
        void SetLogDebug(bool NewLogDebug);
        void SetLogWarn(bool NewLogWarn);
        void SetLogError(bool NewLogError);

        bool GetLogToFile();
        bool GetLogToConsole();
        unsigned int GetKeepCount();
        bool GetLogDebug();
        bool GetLogWarn();
        bool GetLogError();

        // For public use
        void LogDebug(std::string ID, std::string Content, std::string ProductName);
        void LogWarn(std::string ID, std::string Content, std::string ProductName);
        void LogError(std::string ID, std::string Content, std::string ProductName);

        // For PMMA's Cython and Python API
        void InternalLogDebug(std::string ID, std::string Content);
        void InternalLogWarn(std::string ID, std::string Content);
        void InternalLogError(std::string ID, std::string Content);
};