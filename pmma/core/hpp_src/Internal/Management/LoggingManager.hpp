#pragma once

#include <string>
#include <vector>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <iostream>

class CPP_LoggingManager {
    public:
        std::vector<std::string> ContentToLogToFile;
        std::vector<int> PreviouslyLoggedContent;

        std::string LogFileLocation;
        std::string LogFileName;

        unsigned int KeepCount = 5;

        bool LogToFile = false;
        bool LogToConsole = true;
        bool LogToFileSpecifiedByUser = false;

        bool LogDebug = false;
        bool LogInfo = true;
        bool LogWarn = true;
        bool LogError = true;

    private:
        void FileCatchUp();

        inline std::string GetDateTimeCode() {
            auto now = std::chrono::system_clock::now();

            std::time_t new_time = std::chrono::system_clock::to_time_t(now);

            std::tm local_tm;

            #ifdef _WIN32
                localtime_s(&local_tm, &new_time);
            #else
                localtime_r(&new_time, &local_tm);
            #endif

            auto duration = now.time_since_epoch();
            auto milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(duration) % 1000;

            std::ostringstream oss;

            oss << std::setfill('0')
            << std::setw(2) << local_tm.tm_mday << "/"
            << std::setw(2) << local_tm.tm_mon + 1 << "/"
            << std::setw(4) << local_tm.tm_year + 1900 << " at "
            << std::setw(2) << local_tm.tm_hour << ":"
            << std::setw(2) << local_tm.tm_min << ":"
            << std::setw(2) << local_tm.tm_sec << "."
            << std::setw(3) << milliseconds.count();

            return oss.str();
        }

        inline std::string GenerateLogFileName() {
            auto now = std::chrono::system_clock::now();

            std::time_t new_time = std::chrono::system_clock::to_time_t(now);

            std::tm local_tm;

            #ifdef _WIN32
                localtime_s(&local_tm, &new_time);
            #else
                localtime_r(&new_time, &local_tm);
            #endif

            auto duration = now.time_since_epoch();
            auto milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(duration) % 1000;

            std::ostringstream oss;

            oss << std::setfill('0')
            << std::setw(2) << local_tm.tm_mday << "-"
            << std::setw(2) << local_tm.tm_mon + 1 << "-"
            << std::setw(4) << local_tm.tm_year + 1900 << " at "
            << std::setw(2) << local_tm.tm_hour << "-"
            << std::setw(2) << local_tm.tm_min << "-"
            << std::setw(2) << local_tm.tm_sec;

            return oss.str();
        }

        void Log(std::string Content);

    public:
        CPP_LoggingManager();
        ~CPP_LoggingManager();

        void LogFilePathExplicitlySet() {
            if (!LogToFileSpecifiedByUser) {
                LogToFile = true;

                FileCatchUp();
            }
        }

        void SetLogFileLocation(std::string NewLogFileLocation);

        void SetLogToFile(bool NewLogToFile);

        inline void SetLogToConsole(bool NewLogToConsole) {
            LogToConsole = NewLogToConsole;
        }

        inline bool GetLogToFile() {
            return LogToFile;
        }

        inline bool GetLogToConsole() {
            return LogToConsole;
        }

        inline void SetKeepCount(unsigned int NewKeepCount) {
            KeepCount = NewKeepCount;
        }

        inline unsigned int GetKeepCount() {
            return KeepCount;
        }

        inline void SetLogDebug(bool NewLogDebug) {
            LogDebug = NewLogDebug;
        }

        inline void SetLogInfo(bool NewLogInfo) {
            LogInfo = NewLogInfo;
        }

        inline bool GetLogInfo() {
            return LogInfo;
        }

        inline bool GetLogDebug() {
            return LogDebug;
        }

        inline void SetLogWarn(bool NewLogWarn) {
            LogWarn = NewLogWarn;
        }

        inline bool GetLogWarn() {
            return LogWarn;
        }

        inline void SetLogError(bool NewLogError) {
            LogError = NewLogError;
        }

        inline bool GetLogError() {
            return LogError;
        }

        void InternalLogDebug(int ID, std::string Content, bool RepeatForEffect=false);

        inline void InternalLogInfo(int ID, std::string Content, bool RepeatForEffect=false) {
            if (!LogInfo) {
                return;
            }

            if (!RepeatForEffect) {
                auto PreviousIndex = std::find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), ID);
                if (PreviousIndex == PreviouslyLoggedContent.end()) {
                    PreviouslyLoggedContent.push_back(ID);
                    std::string DateTimeCode = GetDateTimeCode();
                    Log("PMMA (Info) - " + DateTimeCode + " - " + Content);
                }
            } else {
                std::string DateTimeCode = GetDateTimeCode();
                Log("PMMA (Info) - " + DateTimeCode + " - " + Content);
            }
        }

        inline void InternalLogWarn(int ID, std::string Content, bool RepeatForEffect=true) {
            if (!LogWarn) {
                return;
            }

            if (!RepeatForEffect) {
                auto PreviousIndex = std::find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), ID);
                if (PreviousIndex == PreviouslyLoggedContent.end()) {
                    PreviouslyLoggedContent.push_back(ID);
                    std::string DateTimeCode = GetDateTimeCode();
                    Log("PMMA (Warn) - " + DateTimeCode + " - " + Content);
                }
            } else {
                std::string DateTimeCode = GetDateTimeCode();
                Log("PMMA (Warn) - " + DateTimeCode + " - " + Content);
            }
        }

        inline void InternalLogError(int ID, std::string Content, bool RepeatForEffect=true) {
            if (!LogError) {
                return;
            }

            if (!RepeatForEffect) {
                auto PreviousIndex = std::find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), ID);
                if (PreviousIndex == PreviouslyLoggedContent.end()) {
                    PreviouslyLoggedContent.push_back(ID);
                    std::string DateTimeCode = GetDateTimeCode();
                    Log("PMMA (Error) - " + DateTimeCode + " - " + Content);
                }
            } else {
                std::string DateTimeCode = GetDateTimeCode();
                Log("PMMA (Error) - " + DateTimeCode + " - " + Content);
            }
        }

        void ExternalLogDebug(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect=false);

        void ExternalLogInfo(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect=false);

        void ExternalLogWarn(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect=true);

        void ExternalLogError(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect=true);
};