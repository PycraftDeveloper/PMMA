#pragma once

#include <cstdio>
#include <cstdlib>
#include <cstring>

#if defined(_WIN32) || defined(_WIN64)

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <io.h>
#include <windows.h>

#else

#include <unistd.h>

#endif

namespace PMMA::Internal {

class TerminalColorChecker {
private:
    /**
     * Checks if the terminal supports ANSI colors.
     *
     * On Windows, this also attempts to enable
     * Virtual Terminal Processing.
     */
    bool init_and_check_color_support() {
        // If stdout is redirected to a file or pipe,
        // don't use terminal colors.
#if defined(_WIN32) || defined(_WIN64)

        if (!_isatty(_fileno(stdout))) {
            return false;
        }

        HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);

        if (hOut == INVALID_HANDLE_VALUE || hOut == nullptr) {
            return false;
        }

        DWORD dwMode = 0;

        if (!GetConsoleMode(hOut, &dwMode)) {
            return false;
        }

        // Enable ANSI / Virtual Terminal Processing.
        dwMode |= ENABLE_VIRTUAL_TERMINAL_PROCESSING;

        if (!SetConsoleMode(hOut, dwMode)) {
            return false;
        }

        return true;

#else

        if (!isatty(fileno(stdout))) {
            return false;
        }

        const char *term = std::getenv("TERM");

        if (!term) {
            return false;
        }

        // Common terminals that support ANSI escape sequences.
        return std::strstr(term, "color") != nullptr ||
               std::strstr(term, "xterm") != nullptr ||
               std::strstr(term, "screen") != nullptr ||
               std::strstr(term, "tmux") != nullptr ||
               std::strcmp(term, "linux") == 0;

#endif
    }

public:
    TerminalColorChecker();
};

} // namespace PMMA::Internal