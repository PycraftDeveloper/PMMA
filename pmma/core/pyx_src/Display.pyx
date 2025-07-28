# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

import random, threading

import numpy as np
cimport numpy as np

import pmma.core.py_src.Utility as Utility
from NumberFormats cimport Color, CPP_ColorFormat

# Declare the external C++ function
cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_ColorFormat:
        inline void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except + nogil

        inline void GenerateRandomColor() except + nogil
        inline void GeneratePerlinColor(float value) except + nogil
        inline void GenerateFractalBrownianMotionColor(float value) except + nogil

        inline void SetColor_RGBA(unsigned int* in_color) except + nogil
        inline void SetColor_rgba(float* in_color) except + nogil
        inline void SetColor_RGB(unsigned int* in_color) except + nogil
        inline void SetColor_rgb(float* in_color) except + nogil

        inline void GetColor_RGBA(unsigned int* out_color) except + nogil
        inline void GetColor_rgba(float* out_color) except + nogil
        inline void GetColor_RGB(unsigned int* out_color) except + nogil
        inline void GetColor_rgb(float* out_color) except + nogil

        inline unsigned int GetSeed() except + nogil
        inline unsigned int GetOctaves() except + nogil
        inline float GetFrequency() except + nogil
        inline float GetAmplitude() except + nogil

    cdef cppclass CPP_Display:
        CPP_ColorFormat* WindowFillColor

        void Create(unsigned int* NewSize, string NewCaption, string NewIcon, bool NewFullScreen, bool NewResizable, bool NewNoFrame, bool NewVsync, bool NewCentered, bool NewMaximized, bool Transparent) except + nogil

        inline unsigned int GetWidth() except + nogil
        inline unsigned int GetHeight() except + nogil

        inline void GetSize(unsigned int* out) except + nogil

        inline void SetRelativeWindowPosition(unsigned int* Position) except + nogil
        inline void SetAbsoluteWindowPosition(unsigned int* Position) except + nogil

        inline void CenterWindow() except + nogil

        void Clear() except + nogil

        inline void SetWindowInFocus() except + nogil

        inline void SetWindowMinimized(bool IsMinimized) except + nogil
        inline void SetWindowMaximized(bool IsMaximized) except + nogil

        inline void SetCaption(string& new_caption) except + nogil
        inline string GetCaption() except + nogil

        inline void GetCenter_Pixels(unsigned int* out) except + nogil
        inline void GetCenter_Pixels(unsigned int* ObjectSize, unsigned int* out) except + nogil

        inline float GetAspectRatio() except + nogil

        void ContinuousRefresh(unsigned int RefreshRate, bool Minimized,
            bool FocusLoss, bool LowBattery,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery) except + nogil

        void EventRefresh(unsigned int RefreshRate,
            unsigned int MaxRefreshRate, bool Minimized,
            bool FocusLoss, bool LowBattery,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery) except + nogil

        inline void TriggerEventRefresh() except + nogil

        inline unsigned int GetFrameRate() except + nogil

        inline float GetFrameTime() except + nogil

cdef class Color:
    cdef:
        CPP_ColorFormat* cpp_base_class_ptr
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_base_class_ptr = new CPP_ColorFormat()

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_base_class_ptr

    def configure(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_base_class_ptr.Configure(seed, octaves, lacunarity, gain)

    def get_seed(self):
        return self.cpp_base_class_ptr.GetSeed()

    def get_octaves(self):
        return self.cpp_base_class_ptr.GetOctaves()

    def get_lacunarity(self):
        return self.cpp_base_class_ptr.GetFrequency()

    def get_gain(self):
        return self.cpp_base_class_ptr.GetAmplitude()

    def get_color_set(self):
        return self.self.cpp_base_class_ptr.GetSet()

    def generate_random_color(self):
        self.cpp_base_class_ptr.GenerateRandomColor()

    def generate_color_from_perlin_noise(self, value):
        self.cpp_base_class_ptr.GeneratePerlinColor(value)

    def generate_color_from_fractal_brownian_motion(self, value):
        self.cpp_base_class_ptr.GenerateFractalBrownianMotionColor(value)

    def set_color_RGBA(self, in_color):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] in_color_np
            unsigned int* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.uint32 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.uint32, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <unsigned int*>&in_color_np[0]

        self.cpp_base_class_ptr.SetColor_RGBA(in_color_ptr)

    def set_color_small_rgba(self, in_color):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] in_color_np
            float* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.float32 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.float32, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <float*>&in_color_np[0]

        self.cpp_base_class_ptr.SetColor_rgba(in_color_ptr)

    def set_color_RGB(self, in_color):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] in_color_np
            unsigned int* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.uint32 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.uint32, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <unsigned int*>&in_color_np[0]

        self.cpp_base_class_ptr.SetColor_RGB(in_color_ptr)

    def set_color_small_rgb(self, in_color):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] in_color_np
            float* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.float32 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.float32, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <float*>&in_color_np[0]

        self.cpp_base_class_ptr.SetColor_rgb(in_color_ptr)

    def get_color_RGBA(self, detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_color_np
            unsigned int* out_color_ptr

        out_color_np = np.empty(4, dtype=np.uint32, order='C')
        out_color_ptr = <unsigned int*>&out_color_np[0]

        self.cpp_base_class_ptr.GetColor_RGBA(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    def get_color_small_rgba(self, detect_format=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_color_np
            float* out_color_ptr

        out_color_np = np.empty(4, dtype=np.float32, order='C')
        out_color_ptr = <float*>&out_color_np[0]

        self.cpp_base_class_ptr.GetColor_rgba(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    def get_color_RGB(self, detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_color_np
            unsigned int* out_color_ptr

        out_color_np = np.empty(3, dtype=np.uint32, order='C')
        out_color_ptr = <unsigned int*>&out_color_np[0]

        self.cpp_base_class_ptr.GetColor_RGB(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    def get_color_small_rgb(self, detect_format=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_color_np
            float* out_color_ptr

        out_color_np = np.empty(3, dtype=np.float32, order='C')
        out_color_ptr = <float*>&out_color_np[0]

        self.cpp_base_class_ptr.GetColor_rgb(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

cdef class Display:
    cdef:
        CPP_Display* cpp_class_ptr
        Color cpp_window_fill_color_format
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Display()

        self.cpp_window_fill_color_format = Color()
        self.cpp_window_fill_color_format.cpp_base_class_ptr = self.cpp_class_ptr.WindowFillColor

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    property window_fill_color:
        def __get__(self):
            self.cpp_window_fill_color_format.cpp_base_class_ptr = self.cpp_class_ptr.WindowFillColor
            return self.cpp_window_fill_color_format

    def create(self, size=np.array([0, 0], dtype=np.uint32, order='C'), caption="PMMA Display", fullscreen=True, resizable=False, no_frame=False, vsync=True, icon="", centered=True, maximized=False, transparent=False):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            string encoded_caption = caption.encode('utf-8')
            string encoded_icon = icon.encode('utf-8')
            unsigned int* size_ptr

        Utility.Registry.render_thread = threading.current_thread()

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

    @Utility.require_render_thread
    def clear(self):
        self.cpp_class_ptr.Clear()

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

    @Utility.require_render_thread
    def continuous_refresh(self,
        refresh_rate=60,
        lower_refresh_rate_on_minimize=True,
        lower_refresh_rate_on_focus_loss=True,
        lower_refresh_rate_on_low_battery=True):

        if refresh_rate <= 0:
            refresh_rate = 0

        self.cpp_class_ptr.ContinuousRefresh(refresh_rate, False, False,
            False, lower_refresh_rate_on_minimize,
            lower_refresh_rate_on_focus_loss,
            lower_refresh_rate_on_low_battery)

    @Utility.require_render_thread
    def event_refresh(self, refresh_rate=0, max_refresh_rate=60,
        lower_refresh_rate_on_minimize=True,
        lower_refresh_rate_on_focus_loss=True,
        lower_refresh_rate_on_low_battery=True):

        self.cpp_class_ptr.EventRefresh(refresh_rate, max_refresh_rate,
            False, False, False, lower_refresh_rate_on_minimize,
            lower_refresh_rate_on_focus_loss,
            lower_refresh_rate_on_low_battery)

    def trigger_event_refresh(self):
        self.cpp_class_ptr.TriggerEventRefresh()

    def get_frame_rate(self):
        return self.cpp_class_ptr.GetFrameRate()

    def get_frame_time(self):
        return self.cpp_class_ptr.GetFrameTime()