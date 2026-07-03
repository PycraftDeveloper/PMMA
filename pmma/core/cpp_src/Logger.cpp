#include "PMMA_Core.hpp"

void CPP_Logger::SetLogToFile(bool NewLogToFile) {
    PMMA::Core::LoggingManagerInstance->SetLogToFile(NewLogToFile);
}

bool CPP_Logger::GetLogToFile() {
    return PMMA::Core::LoggingManagerInstance->GetLogToFile();
}

void CPP_Logger::SetLogToConsole(bool NewLogToConsole) {
    PMMA::Core::LoggingManagerInstance->SetLogToConsole(NewLogToConsole);
}

bool CPP_Logger::GetLogToConsole() {
    return PMMA::Core::LoggingManagerInstance->GetLogToConsole();
}

void CPP_Logger::SetKeepCount(unsigned int NewKeepCount) {
    PMMA::Core::LoggingManagerInstance->SetKeepCount(NewKeepCount);
}

unsigned int CPP_Logger::GetKeepCount() {
    return PMMA::Core::LoggingManagerInstance->GetKeepCount();
}

void CPP_Logger::SetLogDebug(bool NewLogDebug) {
    PMMA::Core::LoggingManagerInstance->SetLogDebug(NewLogDebug);
}

void CPP_Logger::SetLogInfo(bool NewLogInfo) {
    PMMA::Core::LoggingManagerInstance->SetLogInfo(NewLogInfo);
}

void CPP_Logger::SetLogWarn(bool NewLogWarn) {
    PMMA::Core::LoggingManagerInstance->SetLogWarn(NewLogWarn);
}

void CPP_Logger::SetLogError(bool NewLogError) {
    PMMA::Core::LoggingManagerInstance->SetLogError(NewLogError);
}

bool CPP_Logger::GetLogDebug() {
    return PMMA::Core::LoggingManagerInstance->GetLogDebug();
}

bool CPP_Logger::GetLogInfo() {
    return PMMA::Core::LoggingManagerInstance->GetLogInfo();
}

bool CPP_Logger::GetLogWarn() {
    return PMMA::Core::LoggingManagerInstance->GetLogWarn();
}

bool CPP_Logger::GetLogError() {
    return PMMA::Core::LoggingManagerInstance->GetLogError();
}

void CPP_Logger::LogDebug(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->ExternalLogDebug(ID, Content, ProductName, RepeatForEffect);
}

void CPP_Logger::LogInfo(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->ExternalLogInfo(ID, Content, ProductName, RepeatForEffect);
}

void CPP_Logger::LogWarn(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->ExternalLogWarn(ID, Content, ProductName, RepeatForEffect);
}

void CPP_Logger::LogError(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->ExternalLogError(ID, Content, ProductName, RepeatForEffect);
}

void CPP_Logger::InternalLogDebug(int ID, std::string Content, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->InternalLogDebug(ID, Content, RepeatForEffect);
}

void CPP_Logger::InternalLogInfo(int ID, std::string Content, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->InternalLogInfo(ID, Content, RepeatForEffect);
}

void CPP_Logger::InternalLogWarn(int ID, std::string Content, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->InternalLogWarn(ID, Content, RepeatForEffect);
}

void CPP_Logger::InternalLogError(int ID, std::string Content, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->InternalLogError(ID, Content, RepeatForEffect);
}