from pmma.python_src.projection import OrthographicProjection as _OrthographicProjection
from pmma.python_src.projection import PerspectiveProjection as _PerspectiveProjection
from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class ProjectionIntermediary:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_Constants.PROJECTION_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True)

        self.orthographic_projection: "_OrthographicProjection" = None
        self.perspective_projection: "_PerspectiveProjection" = None

    def get_orthographic_projection(self):
        """
        🟩 **R** -
        """
        return self.orthographic_projection

    def get_perspective_projection(self):
        """
        🟩 **R** -
        """
        return self.perspective_projection

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True