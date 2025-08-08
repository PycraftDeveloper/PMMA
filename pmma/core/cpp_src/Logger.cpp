#include "PMMA_Core.hpp"

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