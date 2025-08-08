#pragma once
#include "PMMA_Exports.hpp"

#include <iostream>
#include <string>

namespace CPP_General {
    EXPORT void Set_PMMA_Location(std::string& out_location);

    EXPORT void Set_Path_Separator(std::string& out_separator);

    EXPORT std::string Get_PMMA_Location();

    EXPORT bool Is_Power_Saving_Mode_Enabled(bool ForceRefresh);

    EXPORT bool Is_DebugModeEnabled();

    EXPORT void Set_DebugModeEnabled(bool DebugMode);
}