# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string
from libcpp cimport bool

import ctypes

from pmma.core.py_src.Constants import Constants

from pmma.build.General import General

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_Passport:
        inline void SetProductName(string NewProductName) except + nogil
        inline void SetProductSubName(string NewProductSubName) except + nogil
        inline void SetCompanyName(string NewCompanyName) except + nogil
        inline void SetProductVersion(string NewProductVersion) except + nogil
        inline void SetProductPath(string NewProductPath) except + nogil
        inline void SetLoggingPath(string NewLoggingPath) except + nogil

        inline void Register() except + nogil

        inline bool GetIsRegistered() except + nogil
        inline string GetProductName() except + nogil
        inline string GetProductSubName() except + nogil
        inline string GetCompanyName() except + nogil
        inline string GetProductVersion() except + nogil
        inline string GetProductPath() except + nogil
        inline string GetLoggingPath() except + nogil

cdef class Passport:
    cdef:
        CPP_Passport* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Passport()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def set_product_name(self, product_name):
        cdef string encoded_product_name = product_name.encode("utf-8")
        self.cpp_class_ptr.SetProductName(encoded_product_name)

    def set_product_sub_name(self, product_sub_name):
        cdef string encoded_product_sub_name = product_sub_name.encode("utf-8")
        self.cpp_class_ptr.SetProductSubName(encoded_product_sub_name)

    def set_company_name(self, company_name):
        cdef string encoded_company_name = company_name.encode("utf-8")
        self.cpp_class_ptr.SetCompanyName(encoded_company_name)

    def set_product_version(self, product_version):
        cdef string encoded_product_version = product_version.encode("utf-8")
        self.cpp_class_ptr.SetProductVersion(encoded_product_version)

    def set_product_path(self, product_path):
        cdef string encoded_product_path = product_path.encode("utf-8")
        self.cpp_class_ptr.SetProductPath(encoded_product_path)

    def set_logging_path(self, logging_path):
        cdef string encoded_logging_path = logging_path.encode("utf-8")
        self.cpp_class_ptr.SetLoggingPath(encoded_logging_path)

    def register(self):
        self.cpp_class_ptr.Register()

        if General.get_operating_system() == Constants.WINDOWS: # Call this BEFORE display.create()
            myappid = f"{self.get_company_name()}.{self.get_product_name()}.{self.get_product_sub_name()}.{self.get_product_version()}"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    def is_registered(self):
        return self.cpp_class_ptr.GetIsRegistered()

    def get_product_name(self):
        cdef string cpp_string = self.cpp_class_ptr.GetProductName()
        return cpp_string.c_str().decode("utf-8")

    def get_product_sub_name(self):
        cdef string cpp_string = self.cpp_class_ptr.GetProductSubName()
        return cpp_string.c_str().decode("utf-8")

    def get_company_name(self):
        cdef string cpp_string = self.cpp_class_ptr.GetCompanyName()
        return cpp_string.c_str().decode("utf-8")

    def get_product_version(self):
        cdef string cpp_string = self.cpp_class_ptr.GetProductVersion()
        return cpp_string.c_str().decode("utf-8")

    def get_product_path(self):
        cdef string cpp_string = self.cpp_class_ptr.GetProductPath()
        return cpp_string.c_str().decode("utf-8")

    def get_logging_path(self):
        cdef string cpp_string = self.cpp_class_ptr.GetLoggingPath()
        return cpp_string.c_str().decode("utf-8")