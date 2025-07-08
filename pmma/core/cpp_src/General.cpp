#include "PMMA_Core.hpp"

using namespace std;

void CPP_General::Set_PMMA_Location(string& location) {
    PMMA::PMMA_Location = location;
}

void CPP_General::Set_Path_Separator(string& separator) {
    PMMA::PathSeparator = separator;
}