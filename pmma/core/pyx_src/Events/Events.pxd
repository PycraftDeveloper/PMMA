from libcpp cimport bool

cdef extern from "Internal/Events/InternalEvents.hpp" nogil:
    cdef cppclass CPP_ButtonPressed "PMMA::Internal::Events::ButtonPressed":
        inline bool GetPressed() except + nogil

        inline bool GetPressedToggle() except + nogil
        inline bool GetDoublePressed() except + nogil

        inline void SetLongPressDuration(float Duration) except + nogil
        inline void SetRepeatPressDuration(float Duration) except + nogil
        inline void SetDoublePressDuration(float Duration) except + nogil

        inline bool GetLongPressed() except + nogil
        inline bool PollLongPressed() except + nogil

        inline float GetRepeatPressDuration() except + nogil
        inline float GetLongPressDuration() except + nogil
        inline float GetDoublePressDuration() except + nogil

cdef class ButtonPressed:
    cdef:
        CPP_ButtonPressed* cpp_base_class_ptr

    cpdef bool get_pressed(self)
    cpdef bool get_pressed_toggle(self)
    cpdef bool get_double_pressed(self)
    cpdef bool get_long_pressed(self)
    cpdef bool poll_long_pressed(self)
    cpdef float get_repeat_press_duration(self)
    cpdef float get_long_press_duration(self)
    cpdef float get_double_press_duration(self)
    cpdef void set_repeat_press_duration(self, float duration)
    cpdef void set_double_press_duration(self, float duration)
    cpdef void set_long_press_duration(self, float duration)
