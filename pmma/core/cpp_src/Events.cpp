#include <string>

#include "Events.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_TextEvent::CPP_TextEvent() {
    PMMA::InternalTextEventInstances.push_back(this);
};

CPP_TextEvent::~CPP_TextEvent() {
    auto it = std::find(PMMA::InternalTextEventInstances.begin(), PMMA::InternalTextEventInstances.end(), this);
    if (it != PMMA::InternalTextEventInstances.end()) {
        PMMA::InternalTextEventInstances.erase(it);
    }
};