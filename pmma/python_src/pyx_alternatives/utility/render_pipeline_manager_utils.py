from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class RenderPipelineManager:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.RENDER_PIPELINE_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self._Render_pipeline_utils__module = _ModuleManager.import_module("pmma.python_src.pyx_alternatives.utility.render_pipeline_utils")

        _Registry.render_pipeline_acceleration_available = True

        self._render_queue = []
        self._groupings = []
        self._raw_data = []
        self._pipeline_cache = {}  # Cache of pipelines keyed by shape IDs

    def __del__(self):
        """
        🟩 **R** -
        """
        if not self._shut_down:
            _Registry.render_pipeline_acceleration_available = False

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def add_to_render_pipeline(self, shape):
        """
        🟩 **R** -
        """
        self._raw_data.append(shape)

    def arrange(self):
        """
        🟩 **R** -
        """
        # Group shapes by compatibility and preserve pipeline cache
        new_groupings = []
        current_group = None

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

        # Update or create render pipelines
        new_render_queue = []
        new_pipeline_cache = {}

        for group in new_groupings:
            if isinstance(group, list):
                shape_ids = tuple(id(shape) for shape in group)
                if shape_ids in self._pipeline_cache:
                    # Use cached pipeline and update if necessary
                    pipeline = self._pipeline_cache[shape_ids]
                    pipeline.update(group)  # Check and update data
                else:
                    # Create a new pipeline for this group
                    pipeline = self._Render_pipeline_utils__module.RenderPipeline()
                    pipeline.update(group)  # Populate with group data
                new_render_queue.append(pipeline)
                new_pipeline_cache[shape_ids] = pipeline
            else:
                # Add non-groupable objects directly
                new_render_queue.append(group)

        # Replace render queue and pipeline cache
        self._render_queue = new_render_queue
        self._pipeline_cache = new_pipeline_cache
        self._raw_data.clear()

    def render(self):
        """
        🟩 **R** -
        """
        self.arrange()
        _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_2D_hardware_accelerated_surface()
        for renderable in self._render_queue:
            if hasattr(renderable, "_properties"):
                renderable._internal_render(*renderable._properties[_InternalConstants.ADDITIONAL_INTERNAL_RENDER_DATA])
            else:
                renderable._internal_render()
