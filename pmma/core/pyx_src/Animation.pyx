# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

from NumberFormats cimport DisplayCoordinate, CPP_DisplayCoordinateFormat

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_LinearAnimation:
        CPP_DisplayCoordinateFormat* StartCoordinatePtr
        CPP_DisplayCoordinateFormat* EndCoordinatePtr;

        CPP_LinearAnimation(CPP_DisplayCoordinateFormat* NewTargetCoordinatePtr) except + nogil

        void Start() except + nogil
        void Stop() except + nogil

        void Pause() except + nogil
        void Resume() except + nogil

        void SetDuration(float NewDuration) except + nogil
        float GetDuration() except + nogil

        float GetRemainingDuration() except + nogil

        bool IsPlaying() except + nogil
        bool IsPaused() except + nogil

        void SetLooping(bool NewLooping) except + nogil
        bool IsLooping() except + nogil

        void SetRepeating(bool NewRepeating) except + nogil
        bool IsRepeating() except + nogil

    cdef cppclass CPP_RadialAnimation:
        CPP_DisplayCoordinateFormat* StartCoordinatePtr
        CPP_DisplayCoordinateFormat* CenterCoordinatePtr;

        CPP_RadialAnimation(CPP_DisplayCoordinateFormat* NewTargetCoordinatePtr) except + nogil

        void Start() except + nogil
        void Stop() except + nogil

        void Pause() except + nogil
        void Resume() except + nogil

        void SetDuration(float NewDuration) except + nogil
        float GetDuration() except + nogil

        float GetRemainingDuration() except + nogil

        bool IsPlaying() except + nogil
        bool IsPaused() except + nogil

        void SetRepeating(bool NewRepeating) except + nogil
        bool IsRepeating() except + nogil

cdef class Linear:
    cdef:
        CPP_LinearAnimation* cpp_class_ptr
        DisplayCoordinate animation_start_pos
        DisplayCoordinate animation_end_pos

    def __cinit__(self, DisplayCoordinate DisplayCoordinateInstance):
        cdef CPP_DisplayCoordinateFormat* input_class_ptr;
        input_class_ptr = DisplayCoordinateInstance.cpp_class_ptr

        self.cpp_class_ptr = new CPP_LinearAnimation(input_class_ptr)

        self.animation_start_pos = DisplayCoordinate()
        self.animation_start_pos.set_pointer(self.cpp_class_ptr.StartCoordinatePtr)

        self.animation_end_pos = DisplayCoordinate()
        self.animation_end_pos.set_pointer(self.cpp_class_ptr.EndCoordinatePtr)

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    property start_position:
        def __get__(self):
            return self.animation_start_pos

    property end_position:
        def __get__(self):
            return self.animation_end_pos

    def start(self):
        self.cpp_class_ptr.Start()

    def stop(self):
        self.cpp_class_ptr.Stop()

    def pause(self):
        self.cpp_class_ptr.Pause()

    def resume(self):
        self.cpp_class_ptr.Resume()

    def set_duration(self, duration):
        self.cpp_class_ptr.SetDuration(duration)

    def get_duration(self):
        return self.cpp_class_ptr.GetDuration()

    def get_remaining_duration(self):
        return self.cpp_class_ptr.GetRemainingDuration()

    def is_paused(self):
        return self.cpp_class_ptr.IsPaused()

    def is_playing(self):
        return self.cpp_class_ptr.IsPlaying()

    def set_repeating(self, repeating):
        self.cpp_class_ptr.SetRepeating(repeating)

    def is_repeating(self):
        return self.cpp_class_ptr.IsRepeating()

    def set_looping(self, looping):
        self.cpp_class_ptr.SetLooping(looping)

    def is_looping(self):
        return self.cpp_class_ptr.IsLooping()

cdef class Radial:
    cdef:
        CPP_RadialAnimation* cpp_class_ptr
        DisplayCoordinate animation_start_pos
        DisplayCoordinate animation_center_pos

    def __cinit__(self, DisplayCoordinate DisplayCoordinateInstance):
        cdef CPP_DisplayCoordinateFormat* input_class_ptr;
        input_class_ptr = DisplayCoordinateInstance.cpp_class_ptr

        self.cpp_class_ptr = new CPP_RadialAnimation(input_class_ptr)

        self.animation_start_pos = DisplayCoordinate()
        self.animation_start_pos.set_pointer(self.cpp_class_ptr.StartCoordinatePtr)

        self.animation_center_pos = DisplayCoordinate()
        self.animation_center_pos.set_pointer(self.cpp_class_ptr.CenterCoordinatePtr)

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    property start_position:
        def __get__(self):
            return self.animation_start_pos

    property orbit_position:
        def __get__(self):
            return self.animation_center_pos

    def start(self):
        self.cpp_class_ptr.Start()

    def stop(self):
        self.cpp_class_ptr.Stop()

    def pause(self):
        self.cpp_class_ptr.Pause()

    def resume(self):
        self.cpp_class_ptr.Resume()

    def set_duration(self, duration):
        self.cpp_class_ptr.SetDuration(duration)

    def get_duration(self):
        return self.cpp_class_ptr.GetDuration()

    def get_remaining_duration(self):
        return self.cpp_class_ptr.GetRemainingDuration()

    def is_paused(self):
        return self.cpp_class_ptr.IsPaused()

    def is_playing(self):
        return self.cpp_class_ptr.IsPlaying()

    def set_repeating(self, repeating):
        self.cpp_class_ptr.SetRepeating(repeating)

    def is_repeating(self):
        return self.cpp_class_ptr.IsRepeating()