# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

cdef class ButtonPressed:
    cpdef bool get_pressed(self):
        return self.cpp_base_class_ptr.GetPressed()

    cpdef bool get_pressed_toggle(self):
        return self.cpp_base_class_ptr.GetPressedToggle()

    cpdef bool get_double_pressed(self):
        return self.cpp_base_class_ptr.GetDoublePressed()

    cpdef bool get_long_pressed(self):
        return self.cpp_base_class_ptr.GetLongPressed()

    cpdef bool poll_long_pressed(self):
        return self.cpp_base_class_ptr.PollLongPressed()

    cpdef float get_repeat_press_duration(self):
        return self.cpp_base_class_ptr.GetRepeatPressDuration()

    cpdef float get_long_press_duration(self):
        return self.cpp_base_class_ptr.GetLongPressDuration()

    cpdef float get_double_press_duration(self):
        return self.cpp_base_class_ptr.GetDoublePressDuration()

    cpdef void set_repeat_press_duration(self, float duration):
        self.cpp_base_class_ptr.SetRepeatPressDuration(duration)

    cpdef void set_double_press_duration(self, float duration):
        self.cpp_base_class_ptr.SetDoublePressDuration(duration)

    cpdef void set_long_press_duration(self, float duration):
        self.cpp_base_class_ptr.SetLongPressDuration(duration)