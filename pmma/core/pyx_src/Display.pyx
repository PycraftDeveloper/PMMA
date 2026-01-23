# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string
from libcpp.optional cimport optional

import random, threading

import numpy as np
cimport numpy as np

import pmma.core.py_src.Utility as Utility

from CoreTypes cimport Color, CPP_Color

np.import_array()

# Declare the external C++ function
cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_Display:
        CPP_Color* WindowFillColor

        void Create(
            unsigned int* NewSize,
            string NewCaption,
            string NewIcon,
            bool NewFullScreen,
            bool NewResizable,
            bool NewNoFrame,
            bool NewVsync,
            bool NewCentered,
            bool NewMaximized) except + nogil

        inline void CenterWindow() except + nogil

        void Clear() except + nogil

        inline void SetWindowInFocus() except + nogil
        inline void SetWindowMinimized(bool IsMinimized) except + nogil
        inline void SetWindowMaximized(bool IsMaximized) except + nogil
        inline void SetCaption(string& new_caption) except + nogil
        inline void SetRelativeWindowPosition(unsigned int* Position) except + nogil
        inline void SetAbsoluteWindowPosition(unsigned int* Position) except + nogil
        void SetIcon(string IconPath) except + nogil

        inline string GetCaption() except + nogil
        inline void GetCenterPosition(unsigned int* out) except + nogil
        inline void GetCenterPosition(unsigned int* ObjectSize, unsigned int* out) except + nogil
        inline unsigned int GetWidth() except + nogil
        inline unsigned int GetHeight() except + nogil
        inline void GetSize(int* out) except + nogil
        inline float GetAspectRatio() except + nogil
        inline unsigned int GetFrameRate() except + nogil
        inline float GetFrameTime() except + nogil
        inline bool GetIsWindowInFocus() except + nogil
        inline bool GetIsWindowMinimized() except + nogil
        inline bool GetIsWindowResizable() except + nogil
        inline bool GetIsWindowVisible() except + nogil
        inline bool GetIsWindowAlwaysOnTop() except + nogil
        inline bool GetIsWindowAutoMinimize() except + nogil
        inline bool GetIsWindowMaximized() except + nogil
        inline unsigned int GetWindow_MSAA_Samples() except + nogil
        inline bool GetIsWindowUsingVsync() except + nogil
        inline unsigned int GetCurrentMonitorRefreshRate() except + nogil

        void Refresh(
            unsigned int MinRefreshRate,
            optional[unsigned int] MaxRefreshRate,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery) except + nogil

        inline void TriggerEventRefresh() except + nogil

        void ToggleFullScreen() except + nogil

cdef class Display:
    cdef:
        CPP_Display* cpp_class_ptr
        Color cpp_window_fill_color_format
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Display()

        self.cpp_window_fill_color_format = Color()
        self.cpp_window_fill_color_format.set_pointer(self.cpp_class_ptr.WindowFillColor)

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    property window_fill_color:
        def __get__(self):
            return self.cpp_window_fill_color_format

    def create(
            self,
            size=np.array([0, 0], dtype=np.uint32, order='C'),
            caption="PMMA Display",
            fullscreen=None,
            resizable=False,
            no_frame=False,
            vsync=True,
            icon="",
            centered=True,
            maximized=False):
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

        zero_array = np.array([0, 0], dtype=np.uint32, order='C')

        if fullscreen == None:
            if np.array_equal(size_np, zero_array):
                fullscreen = True
            else:
                fullscreen = False

        self.cpp_class_ptr.Create(
            size_ptr,
            encoded_caption,
            encoded_icon,
            fullscreen,
            resizable,
            no_frame,
            vsync,
            centered,
            maximized)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def get_height(self):
        return self.cpp_class_ptr.GetHeight()

    def get_size(self):
        cdef:
            np.ndarray[np.int32_t, ndim=1, mode='c'] size_np
            int* size_ptr

        size_np = np.empty(2, dtype=np.int32, order='C')
        size_ptr = <int*>&size_np[0]

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

        self.cpp_class_ptr.SetCaption(encoded_caption)

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

            self.cpp_class_ptr.GetCenterPosition(object_size_ptr, out_ptr)

            if isinstance(object_size, np.ndarray):
                return out_np
            else:
                if self.using_numpy_arrays:
                    return out_np
                else:
                    return out_np.tolist()

        self.cpp_class_ptr.GetCenterPosition(out_ptr)

        if self.using_numpy_arrays:
            return out_np
        else:
            return out_np.tolist()

    def get_aspect_ratio(self):
        return self.cpp_class_ptr.GetAspectRatio()

    @Utility.require_render_thread
    def refresh(
            self, min_refresh_rate=5, max_refresh_rate=None,
            lower_refresh_rate_on_minimize=True,
            lower_refresh_rate_on_focus_loss=True,
            lower_refresh_rate_on_low_battery=True):

        cdef optional[unsigned int] opt_max

        if max_refresh_rate is None:
            opt_max.reset()
        else:
            opt_max = <unsigned int>max_refresh_rate

        self.cpp_class_ptr.Refresh(
            min_refresh_rate, opt_max,
            lower_refresh_rate_on_minimize,
            lower_refresh_rate_on_focus_loss,
            lower_refresh_rate_on_low_battery)

    def trigger_event_refresh(self):
        self.cpp_class_ptr.TriggerEventRefresh()

    def get_frame_rate(self):
        return self.cpp_class_ptr.GetFrameRate()

    def get_frame_time(self):
        return self.cpp_class_ptr.GetFrameTime()

    def set_icon(self, icon_path):
        cdef encoded_icon_path = icon_path.encode('utf-8')

        self.cpp_class_ptr.SetIcon(icon_path)

    def toggle_full_screen(self):
        self.cpp_class_ptr.ToggleFullScreen()

    def is_window_in_focus(self):
        return self.cpp_class_ptr.GetIsWindowInFocus()

    def is_window_minimized(self):
        return self.cpp_class_ptr.GetIsWindowMinimized()

    def is_window_resizable(self):
        return self.cpp_class_ptr.GetIsWindowResizable()

    def is_window_visible(self):
        return self.cpp_class_ptr.GetIsWindowVisible()

    def is_window_always_on_top(self):
        return self.cpp_class_ptr.GetIsWindowAlwaysOnTop()

    def is_window_auto_minimize(self):
        return self.cpp_class_ptr.GetIsWindowAutoMinimize()

    def is_window_maximized(self):
        return self.cpp_class_ptr.GetIsWindowMaximized()

    def get_msaa_samples(self):
        return self.cpp_class_ptr.GetWindow_MSAA_Samples()

    def is_window_using_vsync(self):
        return self.cpp_class_ptr.GetIsWindowUsingVsync()

    def get_current_monitor_refresh_rate(self):
        return self.cpp_class_ptr.GetCurrentMonitorRefreshRate()