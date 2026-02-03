#include "PMMA_Core.hpp"

void CPP_Logger::SetLogToFile(bool NewLogToFile) {
    PMMA_Core::LoggingManagerInstance->SetLogToFile(NewLogToFile);
}

bool CPP_Logger::GetLogToFile() {
    return PMMA_Core::LoggingManagerInstance->GetLogToFile();
}

void CPP_Logger::SetLogToConsole(bool NewLogToConsole) {
    PMMA_Core::LoggingManagerInstance->SetLogToConsole(NewLogToConsole);
}

bool CPP_Logger::GetLogToConsole() {
    return PMMA_Core::LoggingManagerInstance->GetLogToConsole();
}

void CPP_Logger::SetKeepCount(unsigned int NewKeepCount) {
    PMMA_Core::LoggingManagerInstance->SetKeepCount(NewKeepCount);
}

unsigned int CPP_Logger::GetKeepCount() {
    return PMMA_Core::LoggingManagerInstance->GetKeepCount();
}

void CPP_Logger::SetLogDebug(bool NewLogDebug) {
    PMMA_Core::LoggingManagerInstance->SetLogDebug(NewLogDebug);
}

void CPP_Logger::SetLogInfo(bool NewLogInfo) {
    PMMA_Core::LoggingManagerInstance->SetLogInfo(NewLogInfo);
}

void CPP_Logger::SetLogWarn(bool NewLogWarn) {
    PMMA_Core::LoggingManagerInstance->SetLogWarn(NewLogWarn);
}

void CPP_Logger::SetLogError(bool NewLogError) {
    PMMA_Core::LoggingManagerInstance->SetLogError(NewLogError);
}

bool CPP_Logger::GetLogDebug() {
    return PMMA_Core::LoggingManagerInstance->GetLogDebug();
}

bool CPP_Logger::GetLogInfo() {
    return PMMA_Core::LoggingManagerInstance->GetLogInfo();
}

bool CPP_Logger::GetLogWarn() {
    return PMMA_Core::LoggingManagerInstance->GetLogWarn();
}

bool CPP_Logger::GetLogError() {
    return PMMA_Core::LoggingManagerInstance->GetLogError();
}

void CPP_Logger::LogDebug(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA_Core::LoggingManagerInstance->ExternalLogDebug(ID, Content, ProductName, RepeatForEffect);
}

void CPP_Logger::LogInfo(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA_Core::LoggingManagerInstance->ExternalLogInfo(ID, Content, ProductName, RepeatForEffect);
}

void CPP_Logger::LogWarn(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA_Core::LoggingManagerInstance->ExternalLogWarn(ID, Content, ProductName, RepeatForEffect);
}

void CPP_Logger::LogError(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA_Core::LoggingManagerInstance->ExternalLogError(ID, Content, ProductName, RepeatForEffect);
}

void CPP_Logger::InternalLogDebug(int ID, std::string Content, bool RepeatForEffect) {
    PMMA_Core::LoggingManagerInstance->InternalLogDebug(ID, Content, RepeatForEffect);
}

void CPP_Logger::InternalLogInfo(int ID, std::string Content, bool RepeatForEffect) {
    PMMA_Core::LoggingManagerInstance->InternalLogInfo(ID, Content, RepeatForEffect);
}

void CPP_Logger::InternalLogWarn(int ID, std::string Content, bool RepeatForEffect) {
    PMMA_Core::LoggingManagerInstance->InternalLogWarn(ID, Content, RepeatForEffect);
}

void CPP_Logger::InternalLogError(int ID, std::string Content, bool RepeatForEffect) {
    PMMA_Core::LoggingManagerInstance->InternalLogError(ID, Content, RepeatForEffect);
}