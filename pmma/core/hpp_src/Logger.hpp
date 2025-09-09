#pragma once
#include "PMMA_Exports.hpp"

#include <string>

class EXPORT CPP_Logger {
    public:
        void SetLogToFile(bool NewLogToFile);
        void SetLogToConsole(bool NewLogToConsole);
        void SetKeepCount(unsigned int NewKeepCount);
        void SetLogDebug(bool NewLogDebug);
        void SetLogInfo(bool NewLogInfo);
        void SetLogWarn(bool NewLogWarn);
        void SetLogError(bool NewLogError);

        bool GetLogToFile();
        bool GetLogToConsole();
        unsigned int GetKeepCount();
        bool GetLogDebug();
        bool GetLogInfo();
        bool GetLogWarn();
        bool GetLogError();

        // For public use
        void LogDebug(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect);
        void LogInfo(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect);
        void LogWarn(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect);
        void LogError(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect);

        // For PMMA's Cython and Python API
        void InternalLogDebug(int ID, std::string Content, bool RepeatForEffect=false);
        void InternalLogInfo(int ID, std::string Content, bool RepeatForEffect=false);
        void InternalLogWarn(int ID, std::string Content, bool RepeatForEffect=true);
        void InternalLogError(int ID, std::string Content, bool RepeatForEffect=true);
};