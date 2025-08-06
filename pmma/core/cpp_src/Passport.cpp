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