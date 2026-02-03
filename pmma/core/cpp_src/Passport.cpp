#include <filesystem>

#include "PMMA_Core.hpp"

CPP_Passport::CPP_Passport() {
    if (PMMA_Core::PassportInstance != nullptr) {
        delete PMMA_Core::PassportInstance;
        PMMA_Core::PassportInstance = nullptr;
    }

    PMMA_Core::PassportInstance = this;
}

CPP_Passport::~CPP_Passport() {
    if (PMMA_Core::PassportInstance == this) {
        PMMA_Core::PassportInstance = nullptr;
    }
}

void CPP_Passport::Register() {
    IsRegistered = true;

    PMMA_Core::LoggingManagerInstance->SetLogFileLocation(LoggingPath);

    if (TemporaryPath == "") {
        TemporaryPath = ProductPath + PMMA_Registry::PathSeparator + "temporary";
    }

    std::filesystem::create_directories(TemporaryPath);
}

void CPP_Passport::SetLoggingPath(std::string NewLoggingPath, bool ExplicitlySet) {
    LoggingPath = NewLoggingPath;
    IsRegistered = false;
    if (ExplicitlySet) {
        PMMA_Core::LoggingManagerInstance->LogFilePathExplicitlySet();
    }
}