#include <filesystem>

#define PMMA_ALLOW_UMBRELLA_HEADER
#include "PMMA_Core.hpp"

PMMA::Passport::Passport() {
    if (PMMA::Core::PassportInstance != nullptr) {
        delete PMMA::Core::PassportInstance;
        PMMA::Core::PassportInstance = nullptr;
    }

    PMMA::Core::PassportInstance = this;
}

PMMA::Passport::~Passport() {
    if (PMMA::Core::PassportInstance == this) {
        PMMA::Core::PassportInstance = nullptr;
    }
}

void PMMA::Passport::Register() {
    IsRegistered = true;

    PMMA::Core::LoggingManagerInstance->SetLogFileLocation(LoggingPath);

    if (TemporaryPath == "") {
        TemporaryPath = ProductPath + PMMA::Registry::PathSeparator + "temporary";
    }

    std::filesystem::create_directories(TemporaryPath);
}

void PMMA::Passport::SetLoggingPath(std::string NewLoggingPath, bool ExplicitlySet) {
    LoggingPath = NewLoggingPath;
    IsRegistered = false;
    if (ExplicitlySet) {
        PMMA::Core::LoggingManagerInstance->LogFilePathExplicitlySet();
    }
}