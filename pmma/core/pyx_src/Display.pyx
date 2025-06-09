# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

import random

import numpy as np
cimport numpy as np

# Declare the external C++ function
cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_Display:
        CPP_Display(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude);

        inline void Create(unsigned int* NewSize, string NewCaption, string NewIcon, bool NewFullScreen, bool NewResizable, bool NewNoFrame, bool NewVsync, bool NewCentered, bool NewMaximized, bool Transparent) except + nogil

        inline unsigned int GetWidth() except + nogil
        inline unsigned int GetHeight() except + nogil

        inline void GetSize(unsigned int* out) except + nogil

        void SetRelativeWindowPosition(unsigned int* Position) except + nogil
        void SetAbsoluteWindowPosition(unsigned int* Position) except + nogil

        void CenterWindow() except + nogil

        void Clear() except + nogil
        void Clear(float* in_color) except + nogil

        void SetWindowInFocus() except + nogil

        void SetWindowMinimized(bool IsMinimized) except + nogil
        void SetWindowMaximized(bool IsMaximized) except + nogil

        void SetCaption(string& new_caption) except + nogil
        string GetCaption() except + nogil

        void GetCenter_Pixels(unsigned int* out) except + nogil
        void GetCenter_Pixels(unsigned int* ObjectSize, unsigned int* out) except + nogil

        float GetAspectRatio() except + nogil

        void Refresh(unsigned int RefreshRate, bool Minimized,
            bool FocusLoss, bool LowBattery,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery) except + nogil

        void Refresh() except + nogil

        inline unsigned int GetFrameRate() except + nogil

        inline float GetFrameTime() except + nogil

cdef class Display:
    cdef:
        CPP_Display* cpp_class_ptr
        bool using_numpy_arrays

    def __cinit__(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_Display(seed, octaves, lacunarity, gain)

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    def create(self, size=np.array([0, 0], dtype=np.uint32, order='C'), caption="PMMA Display", fullscreen=True, resizable=False, no_frame=False, vsync=True, icon="", centered=True, maximized=False, transparent=False):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            string encoded_caption = caption.encode('utf-8')
            string encoded_icon = icon.encode('utf-8')
            unsigned int* size_ptr


        if not isinstance(size, np.ndarray) or size.dtype != np.uint32 or not size.flags['C_CONTIGUOUS']:
            size_np = np.array(size, dtype=np.uint32, order='C')
            self.using_numpy_arrays = True
        else:
            size_np = size
            self.using_numpy_arrays = False

        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.Create(size_ptr, encoded_caption, encoded_icon, fullscreen, resizable, no_frame, vsync, centered, maximized, transparent)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def get_height(self):
        return self.cpp_class_ptr.GetHeight()

    def get_size(self):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            unsigned int* size_ptr

        size_np = np.empty(2, dtype=np.uint32, order='C')

        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.GetSize(size_ptr)

        if self.using_numpy_arrays:
            return size_np
        else:
            return size_np.tolist()

    def set_relative_window_position(self, position):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] position_np
            unsigned int* position_ptr

        if not isinstance(position, np.ndarray) or position.dtype != np.uint32 or not position.flags['C_CONTIGUOUS']:
            position_np = np.array(position, dtype=np.uint32, order='C')
        else:
            position_np = position

        position_ptr = <unsigned int*>&position_np[0]

        self.cpp_class_ptr.SetRelativeWindowPosition(position_ptr)

    def set_absolute_window_position(self, position):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] position_np
            unsigned int* position_ptr

        if not isinstance(position, np.ndarray) or position.dtype != np.uint32 or not position.flags['C_CONTIGUOUS']:
            position_np = np.array(position, dtype=np.uint32, order='C')
        else:
            position_np = position

        position_ptr = <unsigned int*>&position_np[0]

        self.cpp_class_ptr.SetAbsoluteWindowPosition(position_ptr)

    def center_window(self):
        self.cpp_class_ptr.CenterWindow()

    def clear(self, new_color=None):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] color_np
            float* color_ptr

        if new_color == None or new_color.get_color_set() is False:
            self.cpp_class_ptr.Clear()
        else:
            color_np = new_color.get_color_small_rgba(detect_format=False)
            color_ptr = <float*>&color_np[0]
            self.cpp_class_ptr.Clear(color_ptr)

    def set_window_in_focus(self):
        self.cpp_class_ptr.SetWindowInFocus()

    def set_window_minimized(self, value):
        self.cpp_class_ptr.SetWindowMinimized(value)

    def set_window_maximized(self, value):
        self.cpp_class_ptr.SetWindowMaximized(value)

    def set_caption(self, caption):
        cdef:
            string encoded_caption = caption.encode('utf-8')

        self.cpp_class_ptr.SetCaption(caption)

    def get_caption(self):
        cdef string cpp_str = self.cpp_class_ptr.GetCaption()
        return cpp_str.c_str().decode('utf-8')

    def get_center(self, object_size=None):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] object_size_np
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_np
            unsigned int* object_size_ptr
            unsigned int* out_ptr;

        out_np = np.empty(2, dtype=np.uint32, order='C')
        out_ptr = <unsigned int*>&out_np[0]

        if object_size != None:
            if not isinstance(object_size, np.ndarray) or object_size.dtype != np.uint32 or not object_size.flags['C_CONTIGUOUS']:
                object_size_np = np.array(object_size, dtype=np.uint32, order='C')
            else:
                object_size_np = object_size

            object_size_ptr = <unsigned int*>&object_size_np[0]

            self.cpp_class_ptr.GetCenter_Pixels(object_size_ptr, out_ptr)

            if isinstance(object_size, np.ndarray):
                return out_np
            else:
                if self.using_numpy_arrays:
                    return out_np
                else:
                    return out_np.tolist()

        self.cpp_class_ptr.GetCenter_Pixels(out_ptr)

        if self.using_numpy_arrays:
            return out_np
        else:
            return out_np.tolist()

    def get_aspect_ratio(self):
        return self.cpp_class_ptr.GetAspectRatio()

    def refresh(self,
        refresh_rate=60,
        lower_refresh_rate_on_minimize=True,
        lower_refresh_rate_on_focus_loss=True,
        lower_refresh_rate_on_low_battery=True):

        if refresh_rate <= 0:
            self.cpp_class_ptr.Refresh()
        else:
            self.cpp_class_ptr.Refresh(refresh_rate, False, False, False,
        lower_refresh_rate_on_minimize, lower_refresh_rate_on_focus_loss,
        lower_refresh_rate_on_low_battery)

    def get_frame_rate(self):
        return self.cpp_class_ptr.GetFrameRate()

    def get_frame_time(self):
        return self.cpp_class_ptr.GetFrameTime()