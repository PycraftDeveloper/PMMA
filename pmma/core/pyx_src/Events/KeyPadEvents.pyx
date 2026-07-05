# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

from Events cimport CPP_ButtonPressed, ButtonPressed

cdef extern from "Events/KeyPadEvents.hpp" nogil:
    cdef cppclass _CPP_KeyPadEvent_0(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_0 CPP_KeyPadEvent_0 "PMMA::Events::KeyPad_0"

    cdef cppclass _CPP_KeyPadEvent_1(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_1 CPP_KeyPadEvent_1 "PMMA::Events::KeyPad_1"

    cdef cppclass _CPP_KeyPadEvent_2(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_2 CPP_KeyPadEvent_2 "PMMA::Events::KeyPad_2"

    cdef cppclass _CPP_KeyPadEvent_3(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_3 CPP_KeyPadEvent_3 "PMMA::Events::KeyPad_3"

    cdef cppclass _CPP_KeyPadEvent_4(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_4 CPP_KeyPadEvent_4 "PMMA::Events::KeyPad_4"

    cdef cppclass _CPP_KeyPadEvent_5(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_5 CPP_KeyPadEvent_5 "PMMA::Events::KeyPad_5"

    cdef cppclass _CPP_KeyPadEvent_6(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_6 CPP_KeyPadEvent_6 "PMMA::Events::KeyPad_6"

    cdef cppclass _CPP_KeyPadEvent_7(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_7 CPP_KeyPadEvent_7 "PMMA::Events::KeyPad_7"

    cdef cppclass _CPP_KeyPadEvent_8(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_8 CPP_KeyPadEvent_8 "PMMA::Events::KeyPad_8"

    cdef cppclass _CPP_KeyPadEvent_9(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_9 CPP_KeyPadEvent_9 "PMMA::Events::KeyPad_9"

    cdef cppclass _CPP_KeyPadEvent_Decimal(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_Decimal CPP_KeyPadEvent_Decimal "PMMA::Events::KeyPad_Decimal"

    cdef cppclass _CPP_KeyPadEvent_Divide(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_Divide CPP_KeyPadEvent_Divide "PMMA::Events::KeyPad_Divide"

    cdef cppclass _CPP_KeyPadEvent_Multiply(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_Multiply CPP_KeyPadEvent_Multiply "PMMA::Events::KeyPad_Multiply"

    cdef cppclass _CPP_KeyPadEvent_Subtract(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_Subtract CPP_KeyPadEvent_Subtract "PMMA::Events::KeyPad_Subtract"

    cdef cppclass _CPP_KeyPadEvent_Add(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_Add CPP_KeyPadEvent_Add "PMMA::Events::KeyPad_Add"

    cdef cppclass _CPP_KeyPadEvent_Enter(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_Enter CPP_KeyPadEvent_Enter "PMMA::Events::KeyPad_Enter"

    cdef cppclass _CPP_KeyPadEvent_Equal(CPP_ButtonPressed):
        pass

    ctypedef _CPP_KeyPadEvent_Equal CPP_KeyPadEvent_Equal "PMMA::Events::KeyPad_Equal"

cdef class Zero(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_0()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class One(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Two(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Three(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_3()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Four(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_4()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Five(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_5()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Six(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_6()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Seven(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_7()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Eight(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_8()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Nine(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_9()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Decimal(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_Decimal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Decimal()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Divide(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_Divide* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Divide()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Multiply(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_Multiply* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Multiply()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Subtract(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_Subtract* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Subtract()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Add(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_Add* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Add()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Enter(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_Enter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Enter()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Equal(ButtonPressed):
    cdef:
        CPP_KeyPadEvent_Equal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Equal()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL