import gc as _gc

import moderngl as _moderngl
import numpy as _numpy
import av as _av
import moviepy.editor as _editor

from pmma.python_src.opengl import Texture as _Texture
from pmma.python_src.opengl import VertexBufferObject as _VertexBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.gpu import GPU as _GPU
from pmma.python_src.gpu_distribution import GPUDistribution as _GPUDistribution
from pmma.python_src.number_converter import CoordinateConverter as _CoordinateConverter
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.audio import Audio as _Audio

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Video:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)

        self._video_loaded = False
        self._position = _CoordinateConverter()
        self._position.set_coordinates([0, 0], _Constants.CONVENTIONAL_COORDINATES)
        self._size = _CoordinateConverter()
        self._input_container = None
        self._gpu_distribution = _GPUDistribution()
        self._video_stream = None
        self._video_decoder_manually_set = False
        self._video_frame_time = None
        self._texture = None
        self._surface_vertices = _numpy.array(
            [
                -1.0,  1.0, 0.0, 1.0,
                -1.0, -1.0, 0.0, 0.0,
                1.0,  1.0, 1.0, 1.0,
                1.0, -1.0, 1.0, 0.0,
            ], dtype='f4')

        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._shader = _Shader()
        self._shader.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "video_playback"))
        self._shader.create()

        self._audio_player = _Audio()

        if _Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._surface = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        else:
            self._surface = None

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._time_since_last_frame = 0.0
        self._video_size = None
        self._is_playing = True
        self._audio_sync = False

    def resume(self):
        self._is_playing = True

    def pause(self):
        self._is_playing = False

    def set_surface(self, surface=None):
        if surface is None and _Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def autodetect_and_set_decoder(self, gpu: _GPU=None):
        if self._video_loaded:
            if gpu is None:
                gpu = self._gpu_distribution.get_video_gpu()[0]

            codec = None
            for stream in self._input_container.streams:
                if stream.type == 'video':
                    codec = stream.codec.name
                    break

            decoder = None
            if codec == "h264":
                if "nvidia" in gpu.get_name().lower():
                    decoder = "h264_nvenc"
                elif "intel" in gpu.get_name().lower():
                    decoder = "h264_qsv"
                elif "amd" in gpu.get_name().lower():
                    decoder = "h264_vaapi"
            elif codec == "h265":
                if "nvidia" in gpu.get_name().lower():
                    decoder = "hevc_nvenc"
                elif "intel" in gpu.get_name().lower():
                    decoder = "hevc_qsv"
                elif "amd" in gpu.get_name().lower():
                    decoder = "hevc_vaapi"

            self._input_stream.codec_context.options = {'hwaccel': decoder}

    def manually_set_decoder(self, decoder):
        self._video_decoder_manually_set = True
        self._input_stream.codec_context.options = {'hwaccel': decoder}

    def load_from_file(self, file_path):
        self._file = file_path
        self._input_container = _av.open(file_path)

        video_file = _editor.VideoFileClip(file_path)
        raw_audio_data = video_file.audio
        self._audio_player.load_from_moviepy(raw_audio_data)

        self._input_stream = next(s for s in self._input_container.streams if s.type == 'video')

        frame = next(self._input_container.decode(video=0))

        self._video_size = frame.width, frame.height

        if self._size.get_coordinate_set() is False:
            self._size.set_coordinates(self._video_size, _Constants.CONVENTIONAL_COORDINATES)

        if self._video_decoder_manually_set is False:
            self.autodetect_and_set_decoder()

        frame_rate = self._input_stream.average_rate
        self._video_frame_time = 1.0 / float(frame_rate)  # Duration for each frame in seconds

        if self._texture is not None:
            self._texture.quit()

        self._texture = _Texture()
        self._texture.create(self._video_size, components=_Constants.RGB)

        if self._vbo.get_created() is False:
            self._vbo.create(self._surface_vertices)

        if self._vao.get_created() is False:
            self._vao.create(self._shader, self._vbo, ["2f", "in_vert", "2f", "in_text"])

        self._time_since_last_frame = 0.0

        self._video_loaded = True

    def set_position(self, position, position_format=_Constants.CONVENTIONAL_COORDINATES):
        if type(position) != _CoordinateConverter:
            self._position.set_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=_Constants.CONVENTIONAL_COORDINATES):
        return self._position.get_coordinates(format=format)

    def set_target_size(self, size, size_format=_Constants.CONVENTIONAL_COORDINATES):
        if type(size) != _CoordinateConverter:
            self._size.set_coordinates(size, format=size_format)
        else:
            self._size = size

    def get_target_size(self, format=_Constants.CONVENTIONAL_COORDINATES):
        return self._size.get_coordinates(format=format)

    def get_video_size(self):
        return self._video_size

    def render(self):
        if self._video_loaded:
            if self._audio_player.get_playing() is False:
                self._audio_player.play(blocking=False)

            if self._is_playing is False and self._audio_player.get_playing():
                self._audio_player.pause()

            if self._is_playing and self._audio_player.get_playing() is False:
                self._audio_player.resume()

            elapsed_time = _Registry.ms_since_previous_tick / 1000
            self._time_since_last_frame += elapsed_time

            # Update video frame if enough time has passed
            if self._is_playing and self._time_since_last_frame >= self._video_frame_time:
                self._surface.update_attempted_render_calls(1)

                self._surface.set_refresh_optimization_override(True)

                if self._surface.get_clear_called_but_skipped():
                    return None

                self._surface.get_2D_hardware_accelerated_surface()

                try:
                    frame = next(self._input_container.decode(video=0))
                except StopIteration:
                    # Loop the video for demonstration purposes
                    self._input_container.seek(0)
                    frame = next(self._input_container.decode(video=0))
                except _av.error.EOFError:
                    # Loop the video for demonstration purposes
                    self._input_container.seek(0)
                    frame = next(self._input_container.decode(video=0))

                # Convert frame to RGB for OpenGL
                img = frame.to_ndarray(format='rgb24')
                self._texture.write(img)

                self._time_since_last_frame -= self._video_frame_time  # Reset the time counter

            user_desired_size = self._size.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
            scale = [user_desired_size[0] / self._video_size[0], user_desired_size[1] / self._video_size[1]]

            offset = self._position.get_coordinates(format=_Constants.OPENGL_COORDINATES)
            adjusted_offset = [offset[0] + 1, offset[1] - 1]

            self._shader.set_shader_variable("scale", scale)
            self._shader.set_shader_variable("offset", adjusted_offset)

            # Render the frame
            self._shader.set_shader_variable("Texture", 0)
            self._texture.use(location=0)
            self._vao.render(_moderngl.TRIANGLE_STRIP)