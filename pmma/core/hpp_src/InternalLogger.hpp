#pragma once

#include <string>
#include <vector>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>
#include <fstream>

class CPP_InternalLogger {
    std::vector<std::string> ContentToLogToFile;
    std::vector<std::string> PreviouslyLoggedContent;

    std::string LogFileLocation;
    std::string LogFileName;

    bool LogToFile = false;
    bool LogToConsole = true;

    inline void SetLogFileLocation(std::string NewLogFileLocation) {
        LogFileLocation = NewLogFileLocation;
        LogToFile = true;

        if (ContentToLogToFile.size() > 0) {
            std::ofstream LogFile(LogFileLocation + LogFileName, std::ios::app);
            for (unsigned int i = 0; i < ContentToLogToFile.size(); i++) {
                LogFile << ContentToLogToFile[i] << std::endl;
            }
            LogFile.close();

            ContentToLogToFile.clear();
        }
    }

    inline void SetLogToFile(bool NewLogToFile) {
        LogToFile = NewLogToFile;
    }

    inline void SetLogToConsole(bool NewLogToConsole) {
        LogToConsole = NewLogToConsole;
    }

    inline bool GetLogToFile() {
        return LogToFile;
    }

    inline bool GetLogToConsole() {
        return LogToConsole;
    }

    inline std::string GetDateCode() {
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
        << std::setw(2) << local_tm.tm_sec << ":"
        << std::setw(3) << milliseconds.count();

        return oss.str();
    }

    void InternalLog(std::string Content);
};