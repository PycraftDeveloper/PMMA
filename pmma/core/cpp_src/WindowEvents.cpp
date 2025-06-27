#include <stdexcept>

#include "WindowEvents.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_DropEvent::CPP_DropEvent() {
    PMMA::DropEvent_Instances.push_back(this);

    PMMA::DropEventInstanceCount++;
};

CPP_DropEvent::~CPP_DropEvent() {
    auto it = find(PMMA::DropEvent_Instances.begin(), PMMA::DropEvent_Instances.end(), this);
    if (it != PMMA::DropEvent_Instances.end()) {
        PMMA::DropEvent_Instances.erase(it);
    }

    PMMA::DropEventInstanceCount--;
};