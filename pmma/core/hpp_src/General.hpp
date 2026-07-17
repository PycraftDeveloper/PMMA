#pragma once
#include "PMMA_Exports.hpp"

#include <iostream>
#include <string>

namespace PMMA::General {
EXPORT std::string Get_PMMA_Location();

EXPORT bool Is_Power_Saving_Mode_Enabled(bool ForceRefresh);

EXPORT bool Is_DebugModeEnabled();

EXPORT void Set_DebugModeEnabled(bool DebugMode);

EXPORT bool IsWindowCreated();

EXPORT bool IsApplicationRunning();

EXPORT bool IsEscapeKeyToCloseWindow();

EXPORT void SetEscapeKeyToCloseWindow(bool EscapeKeyToCloseWindow);

EXPORT bool IsF11KeyToToggleFullscreen();

EXPORT void SetF11KeyToToggleFullscreen(bool F11KeyToToggleFullscreen);

EXPORT std::string GetCurrent_PMMA_Version();

EXPORT std::string GetLatest_PMMA_Version();

EXPORT void SetLatest_PMMA_Version(std::string latest_version);

EXPORT bool IsUpdateAvailable();

EXPORT double GetApplicationStartTime();

EXPORT double GetApplicationRunTime();

EXPORT void SetLocale(std::string locale);

EXPORT std::string GetLocale();

EXPORT std::string GetOperatingSystem();

EXPORT std::string GetGraphicsBackend();
} // namespace PMMA::General