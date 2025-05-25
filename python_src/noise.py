from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.registry_utils import Registry as _Registry

class Perlin:
    """
    🟩 **R** -
    """
    def __init__(
            self,
            seed: float=None,
            octaves: int=1,
            persistence: float=0.5,
            do_prefill: bool=None):
        """
        🟩 **R** -
        """

        _initialize(self)

        self._importlib__module = _ModuleManager.import_module("importlib")
        self._threading__module = _ModuleManager.import_module("threading")
        self._time__module = _ModuleManager.import_module("time")
        self._traceback__module = _ModuleManager.import_module("traceback")
        self._random__module = _ModuleManager.import_module("random")

        self._numpy__module = _ModuleManager.import_module("numpy")

        self._noise_utils__module = _ModuleManager.import_module("pmma.python_src.utility.noise_utils")
        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")
        self._advmath__module = _ModuleManager.import_module("pmma.python_src.advmath")

        self._internal_prefill_optimizer = self._noise_utils__module.NoiseIntermediary()
        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

        if _Registry.cython_acceleration_available:
            if self._noise_utils__module.NoiseIntermediary.noise_module is None:
                self._noise_utils__module.NoiseIntermediary.noise_module = self._importlib__module.import_module(
                    "pmma.bin.perlin_noise")

            if self._noise_utils__module.NoiseIntermediary.extended_noise_module is None:
                self._noise_utils__module.NoiseIntermediary.extended_noise_module = self._importlib__module.import_module(
                    "pmma.bin.extended_perlin_noise")

        else:
            if self._noise_utils__module.NoiseIntermediary.noise_module is None:
                self._noise_utils__module.NoiseIntermediary.noise_module = self._importlib__module.import_module(
                    "pmma.python_src.pyx_alternatives.utility.perlin_noise")

            if self._noise_utils__module.NoiseIntermediary.extended_noise_module is None:
                self._noise_utils__module.NoiseIntermediary.extended_noise_module = self._importlib__module.import_module(
                    "pmma.python_src.pyx_alternatives.utility.extended_perlin_noise")

        if seed is None:
            seed = self._random__module.randint(0, 1000000)
        self._seed = seed

        self._noise = self._noise_utils__module.NoiseIntermediary.noise_module.PerlinNoise(
            self._seed,
            octaves,
            persistence)

        self._extended_noise = self._noise_utils__module.NoiseIntermediary.extended_noise_module.ExtendedPerlinNoise(
            self._seed,
            octaves,
            persistence)

        if do_prefill is None:
            self._do_prefill = not self._noise_utils__module.NoiseIntermediary.prefill
        else:
            self._do_prefill = do_prefill

        self._math = self._advmath__module.Math()

        if self._do_prefill:
            self._prefill_thread = self._threading__module.Thread(
                target=self.prefill)
            self._prefill_thread.name = "PerlinNoise:Prefill_Thread"

            self._prefill_thread.daemon = True
            self._noise_utils__module.NoiseIntermediary.prefill = True
            self._prefill_thread.start()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def prefill(self):
        """
        🟩 **R** -
        """
        try:
            _Registry.perlin_noise_prefill_single_samples = 0
            x_samples = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            for _ in range(0, 10):
                for _ in range(100):
                    _Registry.perlin_noise_prefill_single_samples += 1
                    x = self._internal_general_utils.random_real_number()
                    self.generate_1D_perlin_noise(x/100)
                    self.generate_2D_perlin_noise(x/100, -x/100)
                    self.generate_3D_perlin_noise(x/100, -x/100, x/100)
                self._time__module.sleep(1/45)

            x = x_samples[0]
            del x_samples[0]
            _Registry.perlin_noise_prefill_array_samples += 1
            x_array, y_array, z_array = self._internal_prefill_optimizer.prefill_optimizer(x)

            self.generate_1D_perlin_noise_from_array(x_array)

            self.generate_2D_perlin_noise_from_array(y_array)

            self.generate_3D_perlin_noise_from_array(z_array)

            self.generate_1D_perlin_noise_from_range([x])
            self.generate_2D_perlin_noise_from_range([x], [x])
            self.generate_3D_perlin_noise_from_range([x], [x], [x])

            while _Registry.in_game_loop is False or _Registry.power_saving_mode:
                for _ in range(100):
                    _Registry.perlin_noise_prefill_single_samples += 1
                    x = self._internal_general_utils.random_real_number()
                    self.generate_1D_perlin_noise(x/100)
                    self.generate_2D_perlin_noise(x/100, -x/100)
                    self.generate_3D_perlin_noise(x/100, -x/100, x/100)

                if x_samples != []:
                    x = x_samples[0]
                    del x_samples[0]
                    _Registry.perlin_noise_prefill_array_samples += 1
                    x_array, y_array, z_array = self._internal_prefill_optimizer.prefill_optimizer(x)

                    self.generate_1D_perlin_noise_from_array(x_array)

                    self.generate_2D_perlin_noise_from_array(y_array)

                    self.generate_3D_perlin_noise_from_array(z_array)

                    self.generate_1D_perlin_noise_from_range([x])
                    self.generate_2D_perlin_noise_from_range([x], [x])
                    self.generate_3D_perlin_noise_from_range([x], [x], [x])
                self._time__module.sleep(1/30)
        except Exception as error:
            print(error)
            print(self._traceback__module.format_exc())

    def generate_1D_perlin_noise(
            self,
            x: float=None,
            new_range=[-1, 1]) -> float:
        """
        🟩 **R** -
        """
        if x is None:
            x = self._internal_general_utils.get_application_run_time()

        noise = self._noise.fBM1D(x)

        if noise > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"] = noise
        if noise < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"] = noise

        return self._math.ranger(
            noise,
            [
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"],
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"]],
            new_range)

    def generate_2D_perlin_noise(
            self,
            x: float=None,
            y: float=None,
            new_range=[-1, 1]) -> float:
        """
        🟩 **R** -
        """
        if x is None:
            x = self._internal_general_utils.get_application_run_time()
        if y is None:
            y = self._internal_general_utils.get_application_run_time()

        noise = self._noise.fBM2D(x, y)

        if noise > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"] = noise
        if noise < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"] = noise

        return self._math.ranger(
            noise,
            [
                    self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"],
                    self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"]],
            new_range)

    def generate_3D_perlin_noise(
            self,
            x: float=None,
            y: float=None,
            z: float=None,
            new_range=[-1, 1]) -> float:
        """
        🟩 **R** -
        """
        if x is None:
            x = self._internal_general_utils.get_application_run_time()
        if y is None:
            y = self._internal_general_utils.get_application_run_time()
        if z is None:
            z = self._internal_general_utils.get_application_run_time()

        noise = self._noise.fBM3D(x, y, z)

        if noise > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"] = noise
        if noise < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"] = noise

        return self._math.ranger(
            noise,
            [
                    self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"],
                    self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"]],
            new_range)


    def generate_1D_perlin_noise_from_array(
            self,
            array,
            new_range=[-1, 1]):
        """
        🟩 **R** -
        """
        noise = self._extended_noise.generate_fbm_1d(array)

        if noise.max() > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"] = noise.min()

        function_range_as_numpy_array = self._numpy__module.array([
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"],
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["max"]],
            dtype=self._numpy__module.float64)
        desired_range_as_numpy_array = self._numpy__module.array(new_range, dtype=self._numpy__module.float64)

        return self._math.nparray_ranger(
            noise,
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

    def generate_2D_perlin_noise_from_array(
            self,
            array,
            new_range=[-1, 1]):
        """
        🟩 **R** -
        """
        noise = self._extended_noise.generate_fbm_2d(array)

        if noise.max() > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"] = noise.min()

        function_range_as_numpy_array = self._numpy__module.array([
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"],
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"]],
            dtype=self._numpy__module.float64)
        desired_range_as_numpy_array = self._numpy__module.array(new_range, dtype=self._numpy__module.float64)

        flattened_array = noise.flatten()

        range_adjusted_array = self._math.nparray_ranger(
            flattened_array, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

        return range_adjusted_array.reshape(noise.shape)

    def generate_3D_perlin_noise_from_array(
            self,
            array,
            new_range=[-1, 1]):
        """
        🟩 **R** -
        """
        noise = self._extended_noise.generate_fbm_3d(array)

        if noise.max() > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"] = noise.min()

        function_range_as_numpy_array = self._numpy__module.array([
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"],
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"]],
            dtype=self._numpy__module.float64)
        desired_range_as_numpy_array = self._numpy__module.array(new_range, dtype=self._numpy__module.float64)

        flattened_array = noise.flatten()

        range_adjusted_array = self._math.nparray_ranger(
            flattened_array, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

        return range_adjusted_array.reshape(noise.shape)

    def generate_1D_perlin_noise_from_range(
            self,
            one_range,
            new_range=[-1, 1]):
        """
        🟩 **R** -
        """
        if len(one_range) == 1:
            array = self._numpy__module.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            array = self._numpy__module.linspace(one_range[0], one_range[1], one_range[1])
        else:
            array = self._numpy__module.linspace(one_range[0], one_range[1], one_range[2])

        noise = self._extended_noise.generate_fbm_1d(array)

        if noise.max() > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"] = noise.min()

        function_range_as_numpy_array = self._numpy__module.array([
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"],
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"]],
            dtype=self._numpy__module.float64)
        desired_range_as_numpy_array = self._numpy__module.array(new_range, dtype=self._numpy__module.float64)

        return self._math.nparray_ranger(
            noise, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

    def generate_2D_perlin_noise_from_range(
            self,
            one_range,
            two_range,
            new_range=[-1, 1]):
        """
        🟩 **R** -
        """
        if len(one_range) == 1:
            x_array = self._numpy__module.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            x_array = self._numpy__module.linspace(one_range[0], one_range[1], one_range[1])
        else:
            x_array = self._numpy__module.linspace(one_range[0], one_range[1], one_range[2])

        if len(two_range) == 1:
            y_array = self._numpy__module.linspace(0, two_range[0], two_range[0])
        elif len(two_range) == 2:
            y_array = self._numpy__module.linspace(two_range[0], two_range[1], two_range[1])
        else:
            y_array = self._numpy__module.linspace(two_range[0], two_range[1], two_range[2])

        x, y = self._numpy__module.meshgrid(x_array, y_array)
        array = self._numpy__module.stack((x, y), axis=-1)

        noise = self._extended_noise.generate_fbm_2d(array)

        if noise.max() > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"] = noise.min()

        function_range_as_numpy_array = self._numpy__module.array([
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"],
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"]],
            dtype=self._numpy__module.float64)
        desired_range_as_numpy_array = self._numpy__module.array(new_range, dtype=self._numpy__module.float64)

        flattened_array = noise.flatten()

        range_adjusted_array = self._math.nparray_ranger(
            flattened_array, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

        return range_adjusted_array.reshape(noise.shape)

    def generate_3D_perlin_noise_from_range(
            self,
            one_range,
            two_range,
            three_range,
            new_range=[-1, 1]):
        """
        🟩 **R** -
        """

        if len(one_range) == 1:
            x_array = self._numpy__module.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            x_array = self._numpy__module.linspace(one_range[0], one_range[1], one_range[1])
        else:
            x_array = self._numpy__module.linspace(one_range[0], one_range[1], one_range[2])

        if len(two_range) == 1:
            y_array = self._numpy__module.linspace(0, two_range[0], two_range[0])
        elif len(two_range) == 2:
            y_array = self._numpy__module.linspace(two_range[0], two_range[1], two_range[1])
        else:
            y_array = self._numpy__module.linspace(two_range[0], two_range[1], two_range[2])

        if len(three_range) == 1:
            z_array = self._numpy__module.linspace(0, three_range[0], three_range[0])
        elif len(three_range) == 2:
            z_array = self._numpy__module.linspace(three_range[0], three_range[1], three_range[1])
        else:
            z_array = self._numpy__module.linspace(three_range[0], three_range[1], three_range[2])

        x, y, z = self._numpy__module.meshgrid(x_array, y_array, z_array)
        array = self._numpy__module.stack((x, y, z), axis=-1)

        noise = self._extended_noise.generate_fbm_3d(array)

        if noise.max() > self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"]:
            self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"] = noise.min()

        function_range_as_numpy_array = self._numpy__module.array([
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"],
                self._noise_utils__module.NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"]],
            dtype=self._numpy__module.float64)
        desired_range_as_numpy_array = self._numpy__module.array(new_range, dtype=self._numpy__module.float64)

        flattened_array = noise.flatten()

        range_adjusted_array = self._math.nparray_ranger(
            flattened_array, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

        return range_adjusted_array.reshape(noise.shape)

    def set_seed(self, seed: float):
        """
        🟩 **R** -
        """
        self.__init__(seed)

    def get_seed(self) -> float:
        """
        🟩 **R** -
        """
        return self._seed