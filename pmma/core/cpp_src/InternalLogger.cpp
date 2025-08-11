#ifdef INTERNAL_USE_PYTHON
    #include <Python.h>
#endif

#include <filesystem>
#include <regex>

#include "PMMA_Core.hpp"

struct LogFileEntry {
    filesystem::path path;
    time_t timestamp;
};

tm parseTimestamp(const std::string& name) {
    tm tm = {};
    sscanf(name.c_str(), "%2d-%2d-%4d at %2d-%2d-%2d",
                &tm.tm_mday, &tm.tm_mon, &tm.tm_year,
                &tm.tm_hour, &tm.tm_min, &tm.tm_sec);
    tm.tm_mon -= 1;       // tm_mon is 0-based
    tm.tm_year -= 1900;   // tm_year is years since 1900
    return tm;
}

void ClearOldLogs(string LogDirectory, unsigned int KeepCount) {
    std::regex pattern(R"((\d{2}-\d{2}-\d{4} at \d{2}-\d{2}-\d{2})\.txt)");
    std::vector<LogFileEntry> files;

    for (const auto& entry : filesystem::directory_iterator(LogDirectory)) {
        if (!entry.is_regular_file()) continue;

        smatch match;
        string filename = entry.path().filename().string();

        if (regex_match(filename, match, pattern)) {
            tm tm = parseTimestamp(match[1]);
            time_t ts = mktime(&tm);
            files.push_back({entry.path(), ts});
        }
    }

    // Sort by timestamp descending
    std::sort(files.begin(), files.end(), [](const LogFileEntry& a, const LogFileEntry& b) {
        return a.timestamp > b.timestamp;
    });

    // Delete files beyond the most recent `keep_count`
    for (size_t i = KeepCount; i < files.size(); ++i) {
        cout << "Deleting: " << files[i].path << "\n";
        try {
            filesystem::remove(files[i].path);
        } catch (const filesystem::filesystem_error& e) {
            cout << "Error deleting file: " << e.what() << "\n";
        }
    }
}

CPP_InternalLogger::CPP_InternalLogger() {
    LogDebug = PMMA_Registry::IsDebuggingModeEnabled;
}

CPP_InternalLogger::~CPP_InternalLogger() {
    if (LogToFile && std::filesystem::exists(LogFileLocation)) {
        ClearOldLogs(LogFileLocation, KeepCount);
    }
}

void CPP_InternalLogger::Log(std::string Content) {
    if (LogToConsole) {
        #ifdef INTERNAL_USE_PYTHON
            PyGILState_STATE gstate = PyGILState_Ensure();
            PySys_WriteStdout((Content + "\n").c_str());
            PyGILState_Release(gstate);
        #else
            cout << Content;
        #endif
    }

    if (LogToFile) {
        std::ofstream LogFile(LogFileLocation + PMMA_Registry::PathSeparator + LogFileName, std::ios::app);
        LogFile << Content << endl;
        LogFile.close();
    } else {
        ContentToLogToFile.push_back(Content);
    }
}

void CPP_InternalLogger::FileCatchUp() {
    if (LogToFile && ContentToLogToFile.size() > 0) {
        std::string fullPath = LogFileLocation + PMMA_Registry::PathSeparator + LogFileName;

        std::ifstream inputFile(fullPath);
        std::string originalContents;
        if (inputFile.is_open()) {
            std::ostringstream buffer;
            buffer << inputFile.rdbuf();
            originalContents = buffer.str();
            inputFile.close();
        }

        std::ofstream outputFile(fullPath, std::ios::trunc);
        if (outputFile.is_open()) {
            for (const auto& line : ContentToLogToFile) {
                outputFile << line << std::endl;
            }

            outputFile << originalContents;
            outputFile.close();
        }

        ContentToLogToFile.clear();
    }
}

void CPP_InternalLogger::SetLogFileLocation(std::string NewLogFileLocation) {
    LogFileLocation = NewLogFileLocation;
    LogFileName = GenerateLogFileName() + ".txt";

    FileCatchUp();
}

void CPP_InternalLogger::InternalLogDebug(std::string ID, std::string Content) {
    if (!LogDebug) {
        return;
    }

    if (PMMA_Registry::IsDebuggingModeEnabled) {
        auto PreviousIndex = std::find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), ID);
        if (PreviousIndex == PreviouslyLoggedContent.end()) {
            PreviouslyLoggedContent.push_back(ID);
            std::string DateTimeCode = GetDateTimeCode();
            Log("PMMA (Debug) - " + DateTimeCode + " - " + Content);
        }
    }
}

void CPP_InternalLogger::ExternalLogDebug(std::string ID, std::string Content, std::string ProductName) {
    if (!LogDebug) {
        return;
    }

    if (PMMA_Registry::IsDebuggingModeEnabled) {
        std::transform(ProductName.begin(), ProductName.end(), ProductName.begin(), ::tolower);
        if (ProductName == "pmma") {
            throw runtime_error("The name PMMA or pmma is reserved!");
        }
        auto PreviousIndex = std::find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), ID);
        if (PreviousIndex == PreviouslyLoggedContent.end()) {
            PreviouslyLoggedContent.push_back(ID);
            std::string DateTimeCode = GetDateTimeCode();
            if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
                ProductName = PMMA_Core::PassportInstance->ProductName + " ";
            }
            Log(ProductName + "(Debug) - " + DateTimeCode + " - " + Content);
        }
    }
}

void CPP_InternalLogger::ExternalLogWarn(std::string ID, std::string Content, std::string ProductName) {
    if (!LogWarn) {
        return;
    }

    std::transform(ProductName.begin(), ProductName.end(), ProductName.begin(), ::tolower);
    if (ProductName == "pmma") {
        throw runtime_error("The name PMMA or pmma is reserved!");
    }
    auto PreviousIndex = std::find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), ID);
    if (PreviousIndex == PreviouslyLoggedContent.end()) {
        PreviouslyLoggedContent.push_back(ID);
        std::string DateTimeCode = GetDateTimeCode();
        if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
            ProductName = PMMA_Core::PassportInstance->ProductName + " ";
        }
        Log(ProductName + "(Warn) - " + DateTimeCode + " - " + Content);
    }
}

void CPP_InternalLogger::ExternalLogError(std::string ID, std::string Content, std::string ProductName) {
    if (!LogError) {
        return;
    }

    std::transform(ProductName.begin(), ProductName.end(), ProductName.begin(), ::tolower);
    if (ProductName == "pmma") {
        throw runtime_error("The name PMMA or pmma is reserved!");
    }
    auto PreviousIndex = std::find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), ID);
    if (PreviousIndex == PreviouslyLoggedContent.end()) {
        PreviouslyLoggedContent.push_back(ID);
        std::string DateTimeCode = GetDateTimeCode();
        if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
            ProductName = PMMA_Core::PassportInstance->ProductName + " ";
        }
        Log(ProductName + "(Error) - " + DateTimeCode + " - " + Content);
    }
}