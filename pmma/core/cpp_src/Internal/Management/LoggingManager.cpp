#ifdef USE_PYTHON
    #include <Python.h>
#endif

#include <filesystem>
#include <regex>
#include <functional>

#include "PMMA_Core.hpp"

struct LogFileEntry {
    std::filesystem::path path;
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

void ClearOldLogs(std::string LogDirectory, unsigned int KeepCount) {
    std::regex pattern(R"((\d{2}-\d{2}-\d{4} at \d{2}-\d{2}-\d{2})\.txt)");
    std::vector<LogFileEntry> files;

    for (const auto& entry : std::filesystem::directory_iterator(LogDirectory)) {
        if (!entry.is_regular_file()) continue;

        std::smatch match;
        std::string filename = entry.path().filename().string();

        if (regex_match(filename, match, pattern)) {
            tm tm = parseTimestamp(match[1]);
            time_t ts = mktime(&tm);
            files.push_back({entry.path(), ts});
        }
    }

    // Sort by timestamp descending
    sort(files.begin(), files.end(), [](const LogFileEntry& a, const LogFileEntry& b) {
        return a.timestamp > b.timestamp;
    });

    // Delete files beyond the most recent `keep_count`
    for (size_t i = KeepCount; i < files.size(); ++i) {
        std::cout << "Deleting: " << files[i].path << "\n";
        try {
            std::filesystem::remove(files[i].path);
        } catch (const std::filesystem::filesystem_error& e) {
            std::cout << "Error deleting file: " << e.what() << "\n";
        }
    }
}

CPP_LoggingManager::CPP_LoggingManager() {
    LogDebug = PMMA_Registry::IsDebuggingModeEnabled;
}

CPP_LoggingManager::~CPP_LoggingManager() {
    if (LogToFile && std::filesystem::exists(LogFileLocation)) {
        ClearOldLogs(LogFileLocation, KeepCount);
    }
}

void CPP_LoggingManager::SetLogToFile(bool NewLogToFile) {
    LogToFile = NewLogToFile;
    LogToFileSpecifiedByUser = true;

    if (std::filesystem::exists(LogFileLocation)) {
        return;
    }

    if (PMMA_Core::PassportInstance != nullptr) {
        std::string ProductPath = PMMA_Core::PassportInstance->GetProductPath();

        if (LogToFile && std::filesystem::exists(ProductPath)) {
            try {
                std::filesystem::create_directory(ProductPath + PMMA_Registry::PathSeparator + "logs");
                LogFileLocation = ProductPath + PMMA_Registry::PathSeparator + "logs";
                FileCatchUp();
            } catch (const std::filesystem::filesystem_error& e) {
                PMMA_Core::LoggingManagerInstance->InternalLogError(
                    11,
                    "An error occurred whilst trying to create the \
directory: '" + ProductPath + PMMA_Registry::PathSeparator + "logs" + "'. \
The error details are: " + e.what()
                );
            }

            return;
        }
    }
    PMMA_Core::LoggingManagerInstance->InternalLogWarn(
        10,
        "No logging location has been set. Please use: \
`Passport.set_logging_location` to directly set a directory for the logs \
to be stored, or use `Passport.set_product_path` to allow PMMA to automatically \
manage a log file directory in your application. Until such a time, logs \
cannot be stored and only displayed at runtime."
    );
    LogToFile = false;
    LogToFileSpecifiedByUser = false;
}

void CPP_LoggingManager::Log(std::string Content) {
    if (LogToConsole) {
        #ifdef USE_PYTHON
            PyGILState_STATE gstate = PyGILState_Ensure();
            PySys_WriteStdout("%s\n", Content.c_str());
            PyGILState_Release(gstate);
        #else
            std::cout << Content << std::endl;
        #endif
    }

    if (LogToFile) {
        std::ofstream LogFile(LogFileLocation + PMMA_Registry::PathSeparator + LogFileName, std::ios::app);
        LogFile << Content << std::endl;
        LogFile.close();
    } else {
        ContentToLogToFile.push_back(Content);
    }
}

void CPP_LoggingManager::FileCatchUp() {
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

void CPP_LoggingManager::SetLogFileLocation(std::string NewLogFileLocation) {
    LogFileLocation = NewLogFileLocation;
    LogFileName = GenerateLogFileName() + ".txt";

    FileCatchUp();
}

void CPP_LoggingManager::InternalLogDebug(int ID, std::string Content, bool RepeatForEffect) {
    if (!LogDebug) {
        return;
    }

    if (PMMA_Registry::IsDebuggingModeEnabled) {
        if (!RepeatForEffect) {
            auto PreviousIndex = find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), ID);
            if (PreviousIndex == PreviouslyLoggedContent.end()) {
                PreviouslyLoggedContent.push_back(ID);
                std::string DateTimeCode = GetDateTimeCode();
                Log("PMMA (Debug) - " + DateTimeCode + " - " + Content);
            }
        } else {
            std::string DateTimeCode = GetDateTimeCode();
            Log("PMMA (Debug) - " + DateTimeCode + " - " + Content);
        }
    }
}

void CPP_LoggingManager::ExternalLogDebug(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    if (!LogDebug) {
        return;
    }

    if (PMMA_Registry::IsDebuggingModeEnabled) {
        transform(ProductName.begin(), ProductName.end(), ProductName.begin(), ::tolower);
        if (ProductName == "pmma") {
            PMMA_Core::LoggingManagerInstance->InternalLogError(
                57,
                "Failed to log debug message: The name PMMA or pmma is reserved!"
            );

            throw std::runtime_error("The name PMMA or pmma is reserved!");
        }

        if (!RepeatForEffect) {
            int InternalID;
            transform(ID.begin(), ID.end(), ID.begin(), ::tolower);
            std::hash<std::string> hasher;
            InternalID = -(int)(hasher(ID));

            auto PreviousIndex = find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), InternalID);
            if (PreviousIndex == PreviouslyLoggedContent.end()) {
                PreviouslyLoggedContent.push_back(InternalID);
                std::string DateTimeCode = GetDateTimeCode();
                if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
                    ProductName = PMMA_Core::PassportInstance->ProductName + " ";
                }
                Log(ProductName + "(Debug) - " + DateTimeCode + " - " + Content);
            }
        } else {
            std::string DateTimeCode = GetDateTimeCode();
            if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
                ProductName = PMMA_Core::PassportInstance->ProductName + " ";
            }
            Log(ProductName + "(Debug) - " + DateTimeCode + " - " + Content);
        }
    }
}

void CPP_LoggingManager::ExternalLogInfo(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    if (!LogInfo) {
        return;
    }

    transform(ProductName.begin(), ProductName.end(), ProductName.begin(), ::tolower);
    if (ProductName == "pmma") {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            57,
            "Failed to log debug message: The name PMMA or pmma is reserved!"
        );

        throw std::runtime_error("The name PMMA or pmma is reserved!");
    }

    if (!RepeatForEffect) {
        int InternalID;
        transform(ID.begin(), ID.end(), ID.begin(), ::tolower);
        std::hash<std::string> hasher;
        InternalID = -(int)(hasher(ID));

        auto PreviousIndex = find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), InternalID);
        if (PreviousIndex == PreviouslyLoggedContent.end()) {
            PreviouslyLoggedContent.push_back(InternalID);
            std::string DateTimeCode = GetDateTimeCode();
            if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
                ProductName = PMMA_Core::PassportInstance->ProductName + " ";
            }
            Log(ProductName + "(Info) - " + DateTimeCode + " - " + Content);
        }
    } else {
        std::string DateTimeCode = GetDateTimeCode();
        if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
            ProductName = PMMA_Core::PassportInstance->ProductName + " ";
        }
        Log(ProductName + "(Info) - " + DateTimeCode + " - " + Content);
    }
}

void CPP_LoggingManager::ExternalLogWarn(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    if (!LogWarn) {
        return;
    }

    transform(ProductName.begin(), ProductName.end(), ProductName.begin(), ::tolower);
    if (ProductName == "pmma") {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            57,
            "Failed to log debug message: The name PMMA or pmma is reserved!"
        );

        throw std::runtime_error("The name PMMA or pmma is reserved!");
    }

    if (!RepeatForEffect) {
        int InternalID;
        transform(ID.begin(), ID.end(), ID.begin(), ::tolower);
        std::hash<std::string> hasher;
        InternalID = -(int)(hasher(ID));

        auto PreviousIndex = find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), InternalID);
        if (PreviousIndex == PreviouslyLoggedContent.end()) {
            PreviouslyLoggedContent.push_back(InternalID);
            std::string DateTimeCode = GetDateTimeCode();
            if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
                ProductName = PMMA_Core::PassportInstance->ProductName + " ";
            }
            Log(ProductName + "(Warn) - " + DateTimeCode + " - " + Content);
        }
    } else {
        std::string DateTimeCode = GetDateTimeCode();
        if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
            ProductName = PMMA_Core::PassportInstance->ProductName + " ";
        }
        Log(ProductName + "(Warn) - " + DateTimeCode + " - " + Content);
    }
}

void CPP_LoggingManager::ExternalLogError(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    if (!LogError) {
        return;
    }

    transform(ProductName.begin(), ProductName.end(), ProductName.begin(), ::tolower);
    if (ProductName == "pmma") {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            57,
            "Failed to log debug message: The name PMMA or pmma is reserved!"
        );

        throw std::runtime_error("The name PMMA or pmma is reserved!");
    }

    if (!RepeatForEffect) {
        int InternalID;
        transform(ID.begin(), ID.end(), ID.begin(), ::tolower);
        std::hash<std::string> hasher;
        InternalID = -(int)(hasher(ID));

        auto PreviousIndex = find(PreviouslyLoggedContent.begin(), PreviouslyLoggedContent.end(), InternalID);
        if (PreviousIndex == PreviouslyLoggedContent.end()) {
            PreviouslyLoggedContent.push_back(InternalID);
            std::string DateTimeCode = GetDateTimeCode();
            if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
                ProductName = PMMA_Core::PassportInstance->ProductName + " ";
            }
            Log(ProductName + "(Error) - " + DateTimeCode + " - " + Content);
        }
    } else {
        std::string DateTimeCode = GetDateTimeCode();
        if (ProductName == "" && PMMA_Core::PassportInstance->IsRegistered) {
            ProductName = PMMA_Core::PassportInstance->ProductName + " ";
        }
        Log(ProductName + "(Error) - " + DateTimeCode + " - " + Content);
    }
}