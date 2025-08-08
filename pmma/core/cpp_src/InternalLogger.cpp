#ifdef INTERNAL_USE_PYTHON
    #include <Python.h>
#endif

#include "PMMA_Core.hpp"

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