# pmma/core/pyx_src/display_registry.pxd

cdef extern from "display_registry.hpp":
    cdef cppclass CPP_Display  # forward declaration

    void set_display_instance(CPP_Display* display)
    CPP_Display* get_display_instance()

cdef void register_display(CPP_Display* display)

cdef CPP_Display* fetch_display()