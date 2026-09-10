#include "Internal/Core/PMMA_Registry.hpp"

#include "Internal/TerminalColorChecker.hpp"

PMMA::Internal::TerminalColorChecker::TerminalColorChecker() {
    PMMA::Core::Registry::TerminalSupportsColor = init_and_check_color_support();
}