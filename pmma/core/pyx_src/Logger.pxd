# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string
from libcpp cimport bool

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_Logger:
        void SetLogToFile(bool NewLogToFile) except + nogil
        void SetLogToConsole(bool NewLogToConsole) except + nogil
        void SetKeepCount(unsigned int NewKeepCount) except + nogil
        void SetLogDebug(bool NewLogDebug) except + nogil
        void SetLogWarn(bool NewLogWarn) except + nogil
        void SetLogError(bool NewLogError) except + nogil

        bool GetLogToFile() except + nogil
        bool GetLogToConsole() except + nogil
        unsigned int GetKeepCount() except + nogil
        bool GetLogDebug() except + nogil
        bool GetLogWarn() except + nogil
        bool GetLogError() except + nogil

        void LogDebug(string ID, string Content, string ProductName) except + nogil
        void LogWarn(string ID, string Content, string ProductName) except + nogil
        void LogError(string ID, string Content, string ProductName) except + nogil

        void InternalLogDebug(string ID, string Content) except + nogil
        void InternalLogWarn(string ID, string Content) except + nogil
        void InternalLogError(string ID, string Content) except + nogil

cdef class Logger:
    cdef:
        CPP_Logger* cpp_class_ptr

    cpdef internal_log_debug(self, string log_id, content)
    cpdef internal_log_warn(self, string log_id, content)
    cpdef internal_log_error(self, string log_id, content)