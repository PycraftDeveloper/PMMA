# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string

cdef class Logger:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Logger()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def set_log_to_file(self, log_to_file):
        self.cpp_class_ptr.SetLogToFile(log_to_file)

    def is_log_to_file(self):
        return self.cpp_class_ptr.GetLogToFile()

    def set_log_to_console(self, log_to_console):
        self.cpp_class_ptr.SetLogToConsole(log_to_console)

    def is_log_to_console(self):
        return self.cpp_class_ptr.GetLogToConsole()

    def set_max_log_files_to_keep(self, value):
        self.cpp_class_ptr.SetKeepCount(value)

    def get_max_log_files_to_keep(self):
        return self.cpp_class_ptr.GetKeepCount()

    def set_log_debug(self, log_debug):
        self.cpp_class_ptr.SetLogDebug(log_debug)

    def set_log_warn(self, log_warn):
        self.cpp_class_ptr.SetLogWarn(log_warn)

    def set_log_error(self, log_error):
        self.cpp_class_ptr.SetLogError(log_error)

    def get_log_debug(self):
        return self.cpp_class_ptr.GetLogDebug()

    def get_log_warn(self):
        return self.cpp_class_ptr.GetLogWarn()

    def get_log_error(self):
        return self.cpp_class_ptr.GetLogError()

    def log_debug_with_id(self, log_id, content, product_name="", repeat_for_effect=False):
        cdef string encoded_id = log_id.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")
        cdef string encoded_product_name = product_name.encode("utf-8")

        self.cpp_class_ptr.LogDebug(encoded_id, encoded_content, encoded_product_name, repeat_for_effect)

    def log_debug(self, content, values=[], product_name="", repeat_for_effect=False):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content
        cdef string encoded_product_name = product_name.encode("utf-8")

        content = content.format(*values)
        encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.LogDebug(encoded_id, encoded_content, encoded_product_name, repeat_for_effect)

    def log_warn_with_id(self, log_id, content, product_name="", repeat_for_effect=False):
        cdef string encoded_id = log_id.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")
        cdef string encoded_product_name = product_name.encode("utf-8")

        self.cpp_class_ptr.LogWarn(encoded_id, encoded_content, encoded_product_name, repeat_for_effect)

    def log_warn(self, content, values=[], product_name="", repeat_for_effect=False):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content
        cdef string encoded_product_name = product_name.encode("utf-8")

        content = content.format(*values)
        encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.LogWarn(encoded_id, encoded_content, encoded_product_name, repeat_for_effect)

    def log_error_with_id(self, log_id, content, product_name="", repeat_for_effect=False):
        cdef string encoded_id = log_id.encode("utf-8")
        cdef string encoded_content = content.encode("utf-8")
        cdef string encoded_product_name = product_name.encode("utf-8")

        self.cpp_class_ptr.LogError(encoded_id, encoded_content, encoded_product_name, repeat_for_effect)

    def log_error(self, content, values=[], product_name="", repeat_for_effect=False):
        cdef string encoded_id = content.encode("utf-8")
        cdef string encoded_content
        cdef string encoded_product_name = product_name.encode("utf-8")

        content = content.format(*values)
        encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.LogError(encoded_id, encoded_content, encoded_product_name, repeat_for_effect)

    cpdef internal_log_debug(self, string log_id, content, repeat_for_effect):
        cdef string encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.InternalLogDebug(log_id, encoded_content, repeat_for_effect)

    cpdef internal_log_warn(self, string log_id, content, repeat_for_effect):
        cdef string encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.InternalLogWarn(log_id, encoded_content, repeat_for_effect)

    cpdef internal_log_error(self, string log_id, content, repeat_for_effect):
        cdef string encoded_content = content.encode("utf-8")

        self.cpp_class_ptr.InternalLogError(log_id, encoded_content, repeat_for_effect)
