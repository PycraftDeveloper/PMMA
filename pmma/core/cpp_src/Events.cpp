#include <string>

#include "Events.hpp"

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

void CPP_TextEvent::Update(string NewTextContent) {
    if (!IsEnabled) {
        return;
    }
    Text += NewTextContent;
};

string CPP_TextEvent::GetText() {
    return Text;
};

void CPP_TextEvent::SetEnabled(bool NewIsEnabled) {
    IsEnabled = NewIsEnabled;
};

bool CPP_TextEvent::GetEnabled() {
    return IsEnabled;
};