#include "PMMA_Core.hpp"

void PMMA::Logger::SetLogToFile(bool NewLogToFile) {
    PMMA::Core::LoggingManagerInstance->SetLogToFile(NewLogToFile);
}

bool PMMA::Logger::GetLogToFile() {
    return PMMA::Core::LoggingManagerInstance->GetLogToFile();
}

void PMMA::Logger::SetLogToConsole(bool NewLogToConsole) {
    PMMA::Core::LoggingManagerInstance->SetLogToConsole(NewLogToConsole);
}

bool PMMA::Logger::GetLogToConsole() {
    return PMMA::Core::LoggingManagerInstance->GetLogToConsole();
}

void PMMA::Logger::SetKeepCount(unsigned int NewKeepCount) {
    PMMA::Core::LoggingManagerInstance->SetKeepCount(NewKeepCount);
}

unsigned int PMMA::Logger::GetKeepCount() {
    return PMMA::Core::LoggingManagerInstance->GetKeepCount();
}

void PMMA::Logger::SetLogDebug(bool NewLogDebug) {
    PMMA::Core::LoggingManagerInstance->SetLogDebug(NewLogDebug);
}

void PMMA::Logger::SetLogInfo(bool NewLogInfo) {
    PMMA::Core::LoggingManagerInstance->SetLogInfo(NewLogInfo);
}

void PMMA::Logger::SetLogWarn(bool NewLogWarn) {
    PMMA::Core::LoggingManagerInstance->SetLogWarn(NewLogWarn);
}

void PMMA::Logger::SetLogError(bool NewLogError) {
    PMMA::Core::LoggingManagerInstance->SetLogError(NewLogError);
}

bool PMMA::Logger::GetLogDebug() {
    return PMMA::Core::LoggingManagerInstance->GetLogDebug();
}

bool PMMA::Logger::GetLogInfo() {
    return PMMA::Core::LoggingManagerInstance->GetLogInfo();
}

bool PMMA::Logger::GetLogWarn() {
    return PMMA::Core::LoggingManagerInstance->GetLogWarn();
}

bool PMMA::Logger::GetLogError() {
    return PMMA::Core::LoggingManagerInstance->GetLogError();
}

void PMMA::Logger::LogDebug(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->ExternalLogDebug(ID, Content, ProductName, RepeatForEffect);
}

void PMMA::Logger::LogInfo(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->ExternalLogInfo(ID, Content, ProductName, RepeatForEffect);
}

void PMMA::Logger::LogWarn(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->ExternalLogWarn(ID, Content, ProductName, RepeatForEffect);
}

void PMMA::Logger::LogError(std::string ID, std::string Content, std::string ProductName, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->ExternalLogError(ID, Content, ProductName, RepeatForEffect);
}

void PMMA::Logger::InternalLogDebug(int ID, std::string Content, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->InternalLogDebug(ID, Content, RepeatForEffect);
}

void PMMA::Logger::InternalLogInfo(int ID, std::string Content, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->InternalLogInfo(ID, Content, RepeatForEffect);
}

void PMMA::Logger::InternalLogWarn(int ID, std::string Content, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->InternalLogWarn(ID, Content, RepeatForEffect);
}

void PMMA::Logger::InternalLogError(int ID, std::string Content, bool RepeatForEffect) {
    PMMA::Core::LoggingManagerInstance->InternalLogError(ID, Content, RepeatForEffect);
}