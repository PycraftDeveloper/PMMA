# cython: language_level=3

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.bin.render_pipeline_utils import RenderPipeline as _RenderPipeline
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

cdef class RenderPipelineManager:
    """
    🟩 **R** -
    """
    cdef:
        list _render_queue
        list _groupings
        list _raw_data
        dict _pipeline_cache

    def __cinit__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RENDER_PIPELINE_MANAGER_OBJECT, add_to_pmma_module_spine=True, cython_class=True)
        _Registry.render_pipeline_acceleration_available = True

        self._render_queue = []
        self._groupings = []
        self._raw_data = []
        self._pipeline_cache = {}  # Cache of pipelines keyed by shape IDs

    def __del__(self):
        """
        🟩 **R** -
        """
        _Registry.render_pipeline_acceleration_available = False

    cpdef void quit(self):
        """
        🟩 **R** -
        """
        self.__del__()

    cpdef void add_to_render_pipeline(self, object shape):
        """
        🟩 **R** -
        """
        self._raw_data.append(shape)

    cdef void arrange(self):
        """
        🟩 **R** -
        """
        cdef list new_groupings = []
        cdef list current_group = None
        cdef object content

        for content in self._raw_data:
            is_compatible = content._properties[_InternalConstants.RENDER_PIPELINE_COMPATIBLE]
            if is_compatible:
                if current_group is None:
                    current_group = []
                    new_groupings.append(current_group)
                current_group.append(content)
            else:
                if current_group is not None:
                    current_group = None
                new_groupings.append(content)

        cdef list new_render_queue = []
        cdef dict new_pipeline_cache = {}
        cdef tuple shape_ids
        cdef object pipeline
        cdef list shape_id_list = []

        for group in new_groupings:
            if isinstance(group, list):
                shape_id_list = []
                for shape in group:
                    shape_id_list.append(id(shape))
                shape_ids = tuple(shape_id_list)

                if shape_ids in self._pipeline_cache:
                    pipeline = self._pipeline_cache[shape_ids]
                    pipeline.update(group)
                else:
                    pipeline = _RenderPipeline()
                    pipeline.update(group)

                new_render_queue.append(pipeline)
                new_pipeline_cache[shape_ids] = pipeline
            else:
                new_render_queue.append(group)

        self._render_queue = new_render_queue
        self._pipeline_cache = new_pipeline_cache
        self._raw_data.clear()

    cpdef void render(self):
        """
        🟩 **R** -
        """
        self.arrange()
        _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_2D_hardware_accelerated_surface()
        cdef object renderable
        for renderable in self._render_queue:
            if hasattr(renderable, "_properties"):
                renderable._internal_render(*renderable._properties[_InternalConstants.ADDITIONAL_INTERNAL_RENDER_DATA])
            else:
                renderable._internal_render()