#include <filesystem>

#include "PMMA_Core.hpp"

CPP_Passport::CPP_Passport() {
    if (PMMA::Core::PassportInstance != nullptr) {
        delete PMMA::Core::PassportInstance;
        PMMA::Core::PassportInstance = nullptr;
    }

    PMMA::Core::PassportInstance = this;
}

CPP_Passport::~CPP_Passport() {
    if (PMMA::Core::PassportInstance == this) {
        PMMA::Core::PassportInstance = nullptr;
    }
}

void CPP_Passport::Register() {
    IsRegistered = true;

    PMMA::Core::LoggingManagerInstance->SetLogFileLocation(LoggingPath);

    if (TemporaryPath == "") {
        TemporaryPath = ProductPath + PMMA::Registry::PathSeparator + "temporary";
    }

    std::filesystem::create_directories(TemporaryPath);
}

void CPP_Passport::SetLoggingPath(std::string NewLoggingPath, bool ExplicitlySet) {
    LoggingPath = NewLoggingPath;
    IsRegistered = false;
    if (ExplicitlySet) {
        PMMA::Core::LoggingManagerInstance->LogFilePathExplicitlySet();
    }
}