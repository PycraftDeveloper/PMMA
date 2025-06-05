// libshared.cpp
#include "Display.hpp"
#include "PMMA_Core.hpp"

static CPP_Display* display_instance = nullptr;

extern "C" {

EXPORT CPP_Display* get_display_instance() {
    return display_instance;
}

EXPORT void set_display_instance(CPP_Display* new_instance) {
    display_instance = new_instance;
}

}