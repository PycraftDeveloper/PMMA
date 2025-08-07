#ifdef INTERNAL_USE_PYTHON
#include <Python.h>
#endif

#include "PMMA_Core.hpp"

void CPP_InternalLogger::InternalLog(std::string Content) {
    if (LogToConsole) {
        #ifdef INTERNAL_USE_PYTHON
            PySys_WriteStdout(Content.c_str());
        #else
            cout << Content;
        #endif
    }

    if (LogToFile) {
        std::ofstream LogFile(LogFileLocation + PMMA_Registry::PathSeparator + LogFileName, std::ios::app);
    } else {
        ContentToLogToFile.push_back(Content);
    }
}