# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string
from libcpp cimport bool

cdef extern from "Logger.hpp" nogil:
    cdef cppclass CPP_Logger:
        void SetLogToFile(bool NewLogToFile) except + nogil
        void SetLogToConsole(bool NewLogToConsole) except + nogil
        void SetKeepCount(unsigned int NewKeepCount) except + nogil
        void SetLogDebug(bool NewLogDebug) except + nogil
        void SetLogInfo(bool NewLogInfo) except + nogil
        void SetLogWarn(bool NewLogWarn) except + nogil
        void SetLogError(bool NewLogError) except + nogil

        bool GetLogToFile() except + nogil
        bool GetLogToConsole() except + nogil
        unsigned int GetKeepCount() except + nogil
        bool GetLogDebug() except + nogil
        bool GetLogInfo() except + nogil
        bool GetLogWarn() except + nogil
        bool GetLogError() except + nogil

        void LogDebug(string ID, string Content, string ProductName, bool RepeatForEffect) except + nogil
        void LogInfo(string ID, string Content, string ProductName, bool RepeatForEffect) except + nogil
        void LogWarn(string ID, string Content, string ProductName, bool RepeatForEffect) except + nogil
        void LogError(string ID, string Content, string ProductName, bool RepeatForEffect) except + nogil

        void InternalLogDebug(int ID, string Content, bool RepeatForEffect) except + nogil
        void InternalLogInfo(int ID, string Content, bool RepeatForEffect) except + nogil
        void InternalLogWarn(int ID, string Content, bool RepeatForEffect) except + nogil
        void InternalLogError(int ID, string Content, bool RepeatForEffect) except + nogil

cdef class Logger:
    cdef:
        CPP_Logger* cpp_class_ptr

    cpdef internal_log_debug(self, int log_id, content, RepeatForEffect)
    cpdef internal_log_info(self, int log_id, content, RepeatForEffect)
    cpdef internal_log_warn(self, int log_id, content, RepeatForEffect)
    cpdef internal_log_error(self, int log_id, content, RepeatForEffect)