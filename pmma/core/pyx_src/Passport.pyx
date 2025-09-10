# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string
from libcpp cimport bool

import ctypes, os, pathlib

from pmma.core.py_src.Constants import Constants
from pmma.core.py_src.Utility import Registry

from pmma.build.General import General
from Logger cimport Logger

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_Passport:
        inline void SetProductName(string NewProductName) except + nogil
        inline void SetProductSubName(string NewProductSubName) except + nogil
        inline void SetCompanyName(string NewCompanyName) except + nogil
        inline void SetProductVersion(string NewProductVersion) except + nogil
        inline void SetProductPath(string NewProductPath) except + nogil
        inline void SetProfilingPath(string NewProfilingPath) except + nogil
        void SetLoggingPath(string NewLoggingPath, bool ExplicitlySet) except + nogil

        void Register() except + nogil

        inline bool GetIsRegistered() except + nogil
        inline string GetProductName() except + nogil
        inline string GetProductSubName() except + nogil
        inline string GetCompanyName() except + nogil
        inline string GetProductVersion() except + nogil
        inline string GetProductPath() except + nogil
        inline string GetLoggingPath() except + nogil
        inline string GetProfilingPath() except + nogil

cdef class Passport:
    cdef:
        CPP_Passport* cpp_class_ptr
        Logger logger

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Passport()
        self.logger = Logger()

        Registry.passport_instance = self

    def __dealloc__(self):
        Registry.passport_instance = None

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
        product_path = str(pathlib.Path(product_path))
        cdef string encoded_product_path = product_path.encode("utf-8")
        self.cpp_class_ptr.SetProductPath(encoded_product_path)

    def set_logging_path(self, logging_path):
        logging_path = str(pathlib.Path(logging_path))
        cdef string encoded_logging_path = logging_path.encode("utf-8")
        self.cpp_class_ptr.SetLoggingPath(encoded_logging_path, True)

    def set_profiling_path(self, profiling_path):
        profiling_path = str(pathlib.Path(profiling_path))
        cdef string encoded_profiling_path = profiling_path.encode("utf-8")
        self.cpp_class_ptr.SetProfilingPath(encoded_profiling_path)

    def register(self):
        cdef string raw_product_path = self.cpp_class_ptr.GetProductPath()
        cdef string raw_logging_path = self.cpp_class_ptr.GetLoggingPath()
        cdef string raw_profiling_path = self.cpp_class_ptr.GetProfilingPath()
        cdef string encoded_logging_path
        cdef string encoded_profiling_path

        product_path = raw_product_path.c_str().decode("utf-8")

        if product_path != "" and (not os.path.exists(product_path)):
            self.logger.internal_log_warn(
                25,
                (f"The path '{product_path}'' is not a valid path on this "
                    "system. Please ensure you enter a valid product path "
                    "using `Passport.set_product_path`."),
                False
            )
            raise IsADirectoryError("This is not a valid path!")

        logging_path = raw_logging_path.c_str().decode("utf-8")

        if logging_path != "" and (not os.path.exists(logging_path)):
            self.logger.internal_log_warn(
                25,
                (f"The path '{logging_path}'' is not a valid path on this "
                    "system. Please ensure you enter a valid logging path "
                    "using `Passport.set_logging_path`. Alternatively you "
                    "can let PMMA automatically detect a suitable logging "
                    "location by not specifying a logging path!"),
                False
            )
            raise IsADirectoryError("This is not a valid path!")

        profiling_path = raw_profiling_path.c_str().decode("utf-8")

        logging_path_not_set = logging_path == ""
        profiling_path_not_set = profiling_path == ""

        if logging_path_not_set and product_path != "":
            if os.path.exists(os.path.join(product_path, "logs")):
                logging_path = os.path.join(product_path, "logs")
                encoded_logging_path = logging_path.encode("utf-8")
                self.cpp_class_ptr.SetLoggingPath(encoded_logging_path, True)

                self.logger.internal_log_debug(
                    26,
                    ("Passport.register - You have not specified a logging "
                        "path, which you can do with `Passport.set_logging_path`. "
                        "Until specified PMMA has automatically found a suitable "
                        f"location for your log files has been found at: '{logging_path}'."),
                    False
                )

            elif os.path.exists(os.path.join(product_path, "Logs")):
                logging_path = os.path.join(product_path, "Logs")
                encoded_logging_path = logging_path.encode("utf-8")
                self.cpp_class_ptr.SetLoggingPath(encoded_logging_path, True)

                self.logger.internal_log_debug(
                    26,
                    ("Passport.register - You have not specified a logging "
                        "path, which you can do with `Passport.set_logging_path`. "
                        "Until specified PMMA has automatically found a suitable "
                        f"location for your log files has been found at: '{logging_path}'."),
                    False
                )
            else:
                for dirpath, _, _ in os.walk(product_path):
                    if "logs" in os.path.basename(dirpath):
                        logging_path = dirpath
                        encoded_logging_path = logging_path.encode("utf-8")
                        self.cpp_class_ptr.SetLoggingPath(encoded_logging_path, True)

                        self.logger.internal_log_debug(
                            26,
                            ("Passport.register - You have not specified a logging "
                                "path, which you can do with `Passport.set_logging_path`. "
                                "Until specified PMMA has automatically found a suitable "
                                f"location for your log files at: '{logging_path}' "
                                "after searching inside the specified product path."),
                                False
                        )

                        break
                else:
                    for dirpath, _, _ in os.walk(product_path):
                        if "Logs" in os.path.basename(dirpath):
                            logging_path = dirpath
                            encoded_logging_path = logging_path.encode("utf-8")
                            self.cpp_class_ptr.SetLoggingPath(encoded_logging_path, True)

                            self.logger.internal_log_debug(
                                26,
                                ("Passport.register - You have not specified a logging "
                                    "path, which you can do with `Passport.set_logging_path`. "
                                    "Until specified PMMA has automatically found a suitable "
                                    f"location for your log files at: '{logging_path}' "
                                    "after searching inside the specified product path."),
                                    False
                            )

                            break
                    else:
                        self.logger.internal_log_debug(
                            27,
                            ("Passport.register - No suitable location for log "
                                "files could automatically be detected. If you want to have PMMA "
                                "automatically manage where your log files go when stored to disk "
                                "please create a designated 'logs' folder in the specified product location "
                                "or manually specify a location for your log "
                                "files to go using `Passport.set_logging_path`."),
                        False
                        )

        if profiling_path_not_set and product_path != "":
            if os.path.exists(os.path.join(product_path, "profiles")):
                profiling_path = os.path.join(product_path, "profiles")
                encoded_profiling_path = profiling_path.encode("utf-8")
                self.cpp_class_ptr.SetProfilingPath(encoded_profiling_path)

                self.logger.internal_log_debug(
                    43,
                    ("Passport.register - You have not specified a profiling "
                        "path, which you can do with `Passport.set_profiling_path`. "
                        "Until specified PMMA has automatically found a suitable "
                        f"location for your profiling files has been found at: '{profiling_path}'."),
                    False
                )

            elif os.path.exists(os.path.join(product_path, "Profiles")):
                profiling_path = os.path.join(product_path, "Profiles")
                encoded_profiling_path = profiling_path.encode("utf-8")
                self.cpp_class_ptr.SetProfilingPath(encoded_profiling_path)

                self.logger.internal_log_debug(
                    43,
                    ("Passport.register - You have not specified a profiling "
                        "path, which you can do with `Passport.set_profiling_path`. "
                        "Until specified PMMA has automatically found a suitable "
                        f"location for your profiling files has been found at: '{profiling_path}'."),
                    False
                )
            else:
                for dirpath, _, _ in os.walk(product_path):
                    if "profiles" in os.path.basename(dirpath):
                        profiling_path = dirpath
                        encoded_profiling_path = profiling_path.encode("utf-8")
                        self.cpp_class_ptr.SetProfilingPath(encoded_profiling_path)

                        self.logger.internal_log_debug(
                            43,
                            ("Passport.register - You have not specified a profiling "
                                "path, which you can do with `Passport.set_profiling_path`. "
                                "Until specified PMMA has automatically found a suitable "
                                f"location for your profiling files at: '{profiling_path}' "
                                "after searching inside the specified product path."),
                                False
                        )

                        break

                else:
                    for dirpath, _, _ in os.walk(product_path):
                        if "Profiles" in os.path.basename(dirpath):
                            profiling_path = dirpath
                            encoded_profiling_path = profiling_path.encode("utf-8")
                            self.cpp_class_ptr.SetProfilingPath(encoded_profiling_path)

                            self.logger.internal_log_debug(
                                43,
                                ("Passport.register - You have not specified a profiling "
                                    "path, which you can do with `Passport.set_profiling_path`. "
                                    "Until specified PMMA has automatically found a suitable "
                                    f"location for your profiling files at: '{profiling_path}' "
                                    "after searching inside the specified product path."),
                                    False
                            )

                            break
                    else:
                        self.logger.internal_log_debug(
                            44,
                            ("Passport.register - No suitable location for profiling "
                                "files could automatically be detected. If you want to have PMMA "
                                "automatically manage where your profiling files go when stored to disk "
                                "please create a designated 'profiles' folder in the specified product location "
                                "or manually specify a location for your profiling "
                                "files to go using `Passport.set_profiling_path`."),
                        False
                        )

        self.cpp_class_ptr.Register()

        if General.get_operating_system() == Constants.OS_WINDOWS:
            if General.is_window_created():
                self.logger.internal_log_debug(
                    28,
                    ("Passport.register - You have registered your "
                        "application after the window has been created. "
                        "This matters as Windows will not register the "
                        "change after the window has been created so your "
                        "application may not appear correctly to the system "
                        "(most notably taskbar icons will not correctly "
                        "display). Please make sure to call `Passport.register` "
                        "before `Display.create`."),
                    False
                )

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

    def get_profiling_path(self):
        cdef string cpp_string = self.cpp_class_ptr.GetProfilingPath()
        return cpp_string.c_str().decode("utf-8")