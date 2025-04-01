from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

class NoiseIntermediary:
    """
    🟩 **R** -
    """
    prefill = False
    noise_ranges = {
        "generate_1D_perlin_noise": {"min": 2, "max": -2},
        "generate_2D_perlin_noise": {"min": 2, "max": -2},
        "generate_3D_perlin_noise": {"min": 2, "max": -2},
        "generate_1D_perlin_noise_from_array": {"min": 2, "max": -2},
        "generate_2D_perlin_noise_from_array": {"min": 2, "max": -2},
        "generate_3D_perlin_noise_from_array": {"min": 2, "max": -2},
        "generate_1D_perlin_noise_from_range": {"min": 2, "max": -2},
        "generate_2D_perlin_noise_from_range": {"min": 2, "max": -2},
        "generate_3D_perlin_noise_from_range": {"min": 2, "max": -2},
    }

    noise_module = None
    extended_noise_module = None

    def __init__(self):
        self._numpy__module = _ModuleManager.import_module("numpy")

    def prefill_optimizer(self, x):
        """
        🟩 **R** -
        """
        x_array = self._numpy__module.linspace(0, x, x)
        x_out_array = x_array
        y_array = self._numpy__module.linspace(0, x, x)
        z_array = self._numpy__module.linspace(0, x, x)

        _x, _y = self._numpy__module.meshgrid(x_array, y_array)
        y_out_array = self._numpy__module.stack((_x, _y), axis=-1)

        _x, _y, _z = self._numpy__module.meshgrid(x_array, y_array, z_array)
        z_out_array = self._numpy__module.stack((_x, _y, _z), axis=-1)

        return x_out_array, y_out_array, z_out_array