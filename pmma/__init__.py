import os
import platform
import ctypes

system = platform.system()

pmma_lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")

if system == "Windows":
    ctypes.CDLL(os.path.join(pmma_lib_dir, "PMMA_Core.dll"))
elif system == "Linux":
    ctypes.CDLL(os.path.join(pmma_lib_dir, "libPMMA_Core.so"))

from pmma.build.AdvancedMathematics import AdvancedMathematics
from pmma.build.PerlinNoise import PerlinNoise
from pmma.build.FractalBrownianMotion import FractalBrownianMotion
from pmma.build.Display import Display
from pmma.build.NumberConverter import (
    ColorConverter, DisplayCoordinatesConverter, AngleConverter,
    DisplayScalarConverter, ProportionConverter)
from pmma.build.Events import *
from pmma.build.KeyEvents import (
    KeyEvent_Space, KeyEvent_Apostrophe, KeyEvent_Comma,
    KeyEvent_Minus, KeyEvent_Period, KeyEvent_Slash, KeyEvent_0,
    KeyEvent_1, KeyEvent_2, KeyEvent_3, KeyEvent_4, KeyEvent_5,
    KeyEvent_6, KeyEvent_7, KeyEvent_8, KeyEvent_9, KeyEvent_Semicolon,
    KeyEvent_Equal, KeyEvent_A, KeyEvent_B, KeyEvent_C, KeyEvent_D,
    KeyEvent_E, KeyEvent_F, KeyEvent_G, KeyEvent_H, KeyEvent_I,
    KeyEvent_J, KeyEvent_K, KeyEvent_L, KeyEvent_M, KeyEvent_N,
    KeyEvent_O, KeyEvent_P, KeyEvent_Q, KeyEvent_R, KeyEvent_S,
    KeyEvent_T, KeyEvent_U, KeyEvent_V, KeyEvent_W, KeyEvent_X,
    KeyEvent_Y, KeyEvent_Z, KeyEvent_Left_Bracket, KeyEvent_Backslash,
    KeyEvent_Right_Bracket, KeyEvent_Grave_Accent, KeyEvent_World_1,
    KeyEvent_World_2, KeyEvent_Escape, KeyEvent_Enter, KeyEvent_Tab,
    KeyEvent_Backspace, KeyEvent_Insert, KeyEvent_Delete, KeyEvent_Right,
    KeyEvent_Left, KeyEvent_Down, KeyEvent_Up, KeyEvent_Page_Up,
    KeyEvent_Page_Down, KeyEvent_Home, KeyEvent_End, KeyEvent_Caps_Lock,
    KeyEvent_Scroll_Lock, KeyEvent_Num_Lock, KeyEvent_Print_Screen,
    KeyEvent_Pause, KeyEvent_F1, KeyEvent_F2, KeyEvent_F3, KeyEvent_F4,
    KeyEvent_F5, KeyEvent_F6, KeyEvent_F7, KeyEvent_F8, KeyEvent_F9,
    KeyEvent_F10, KeyEvent_F11, KeyEvent_F12, KeyEvent_F13, KeyEvent_F14,
    KeyEvent_F15, KeyEvent_F16, KeyEvent_F17, KeyEvent_F18, KeyEvent_F19,
    KeyEvent_F20, KeyEvent_F21, KeyEvent_F22, KeyEvent_F23, KeyEvent_F24,
    KeyEvent_F25, KeyPadEvent_0, KeyPadEvent_1, KeyPadEvent_2,
    KeyPadEvent_3, KeyPadEvent_4, KeyPadEvent_5, KeyPadEvent_6,
    KeyPadEvent_7, KeyPadEvent_8, KeyPadEvent_9, KeyPadEvent_Decimal,
    KeyPadEvent_Divide, KeyPadEvent_Multiply, KeyPadEvent_Subtract,
    KeyPadEvent_Add, KeyPadEvent_Enter, KeyPadEvent_Equal,
    KeyEvent_Left_Shift, KeyEvent_Left_Control, KeyEvent_Left_Alt,
    KeyEvent_Left_Super, KeyEvent_Right_Shift, KeyEvent_Right_Control,
    KeyEvent_Right_Alt, KeyEvent_Right_Super, KeyEvent_Menu)

from pmma.core.py_src.Backpack import Backpack
from pmma.core.py_src.Audio import *
from pmma.core.py_src.Executor import Executor, AdvancedExecutor
from pmma.core.py_src.General import General
from pmma.core.py_src.GPU import GPUs