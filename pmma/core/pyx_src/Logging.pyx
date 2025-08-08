# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_Logger:
        void LogDebug(string ID, string Content, string ProductName) except + nogil
        void LogWarn(string ID, string Content, string ProductName) except + nogil
        void LogError(string ID, string Content, string ProductName) except + nogil

        void InternalLogDebug(string ID, string Content) except + nogil
        void InternalLogWarn(string ID, string Content) except + nogil
        void InternalLogError(string ID, string Content) except + nogil

cdef class TextRenderer:
    cdef:
        CPP_Logger* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Logger()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def log_debug_with_id(self, log_id, content, product_name=""):
        cdef string encoded_id = log_id.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")
        cdef string encoded_product_name = product_name.encode("utf-8")

        self.cpp_class_ptr.LogDebug(encoded_id, encoded_content, encoded_product_name)

    def log_debug(self, content, values, product_name=""):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content
        cdef string encoded_product_name = product_name.encode("utf-8")

        content.format(values)
        encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.LogDebug(encoded_id, encoded_content, encoded_product_name)

    def log_warn_with_id(self, log_id, content, product_name=""):
        cdef string encoded_id = log_id.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")
        cdef string encoded_product_name = product_name.encode("utf-8")

        self.cpp_class_ptr.LogWarn(encoded_id, encoded_content, encoded_product_name)

    def log_warn(self, content, values, product_name=""):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content
        cdef string encoded_product_name = product_name.encode("utf-8")

        content.format(values)
        encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.LogWarn(encoded_id, encoded_content, encoded_product_name)

    def log_error_with_id(self, log_id, content, product_name=""):
        cdef string encoded_id = log_id.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")
        cdef string encoded_product_name = product_name.encode("utf-8")

        self.cpp_class_ptr.LogError(encoded_id, encoded_content, encoded_product_name)

    def log_error(self, content, values, product_name=""):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content
        cdef string encoded_product_name = product_name.encode("utf-8")

        content.format(values)
        encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.LogError(encoded_id, encoded_content, encoded_product_name)

    def internal_log_debug(self, log_id, content):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.InternalLogDebug(encoded_id, encoded_content)

    def internal_log_warn(self, log_id, content):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.InternalLogWarn(encoded_id, encoded_content)

    def internal_log_error(self, log_id, content):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.InternalLogError(encoded_id, encoded_content)
