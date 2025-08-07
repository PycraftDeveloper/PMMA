# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string
from libcpp cimport bool

import ctypes, os

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

    def register(self, auto_prepare_logging_dir=True):
        cdef string raw_product_path = self.cpp_class_ptr.GetProductPath()
        cdef string raw_logging_path = self.cpp_class_ptr.GetLoggingPath()
        cdef string encoded_logging_path

        product_path = raw_product_path.c_str().decode("utf-8")

        if product_path != "" and (not os.path.exists(product_path)):
            raise IsADirectoryError("This is not a valid path!")

        logging_path = raw_logging_path.c_str().decode("utf-8")

        if logging_path != "" and (not os.path.exists(logging_path)):
            raise IsADirectoryError("This is not a valid path!")

        logging_path_not_set = logging_path == ""

        if logging_path_not_set and product_path != "":
            print("No logging path set - attempting to find a valid location!")

            if os.path.exists(os.path.join(product_path, "logs")):
                logging_path = os.path.join(product_path, "logs")
                encoded_logging_path = logging_path.encode("utf-8")
                self.cpp_class_ptr.SetLoggingPath(encoded_logging_path)
                print(f"Found location: {logging_path}")
            elif os.path.exists(os.path.join(product_path, "Logs")):
                logging_path = os.path.join(product_path, "Logs")
                encoded_logging_path = logging_path.encode("utf-8")
                self.cpp_class_ptr.SetLoggingPath(encoded_logging_path)
                print(f"Found location: {logging_path}")
            else:
                for dirpath, _, _ in os.walk(product_path):
                    if "logs" in os.path.basename(dirpath).lower():
                        logging_path = dirpath
                        encoded_logging_path = logging_path.encode("utf-8")
                        self.cpp_class_ptr.SetLoggingPath(encoded_logging_path)
                        print(f"Found location: {logging_path}")
                        break
                else:
                    print("No valid logging location found.")

                    if auto_prepare_logging_dir:
                        logging_path = os.path.join(product_path, "logs")
                        encoded_logging_path = logging_path.encode("utf-8")
                        self.cpp_class_ptr.SetLoggingPath(encoded_logging_path)
                        os.mkdir(logging_path)


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