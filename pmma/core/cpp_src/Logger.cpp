#include "PMMA_Core.hpp"

void CPP_Logger::SetLogToFile(bool NewLogToFile) {
    PMMA_Core::InternalLoggerInstance->SetLogToFile(NewLogToFile);
}

bool CPP_Logger::GetLogToFile() {
    return PMMA_Core::InternalLoggerInstance->GetLogToFile();
}

void CPP_Logger::SetLogToConsole(bool NewLogToConsole) {
    PMMA_Core::InternalLoggerInstance->SetLogToConsole(NewLogToConsole);
}

bool CPP_Logger::GetLogToConsole() {
    return PMMA_Core::InternalLoggerInstance->GetLogToConsole();
}

void CPP_Logger::LogDebug(string ID, string Content, string ProductName) {
    PMMA_Core::InternalLoggerInstance->ExternalLogDebug(ID, Content, ProductName);
}

void CPP_Logger::LogWarn(string ID, string Content, string ProductName) {
    PMMA_Core::InternalLoggerInstance->ExternalLogWarn(ID, Content, ProductName);
}

void CPP_Logger::LogError(string ID, string Content, string ProductName) {
    PMMA_Core::InternalLoggerInstance->ExternalLogError(ID, Content, ProductName);
}

void CPP_Logger::InternalLogDebug(string ID, string Content) {
    PMMA_Core::InternalLoggerInstance->InternalLogDebug(ID, Content);
}

void CPP_Logger::InternalLogWarn(string ID, string Content) {
    PMMA_Core::InternalLoggerInstance->InternalLogWarn(ID, Content);
}

void CPP_Logger::InternalLogError(string ID, string Content) {
    PMMA_Core::InternalLoggerInstance->InternalLogError(ID, Content);
}