from gc import collect as _gc__collect
import time as _time
import threading as _threading

import moderngl as _moderngl
import numpy as _numpy
import av as _av
import moviepy.editor as _editor
import pygame as _pygame

from pmma.python_src.opengl import Texture as _Texture
from pmma.python_src.opengl import VertexBufferObject as _VertexBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.gpu import GPU as _GPU
from pmma.python_src.gpu_distribution import GPUDistribution as _GPUDistribution
from pmma.python_src.number_converter import DisplayCoordinatesConverter as _DisplayCoordinatesConverter
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.audio import Audio as _Audio

from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Video:
    """
    🟩 **R** -
    """
    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._play_video = False
            if self._video_player_thread is not None:
                self._video_player_thread.join()

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._video_loaded = False
        self._position = _DisplayCoordinatesConverter()
        self._position.set_coordinates([0, 0], _Constants.CONVENTIONAL_COORDINATES)
        self._size = _DisplayCoordinatesConverter()
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

        if not _Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DISPLAY_OBJECT)
            from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
            _DisplayIntermediary()

        self._surface = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._time_since_last_frame = 0.0
        self._video_size = None
        self._is_playing = True
        self._audio_sync = False

        self._video_clock = _pygame.time.Clock()

        self._video_frame = None
        self._video_player_thread = None
        self._play_video = False

        self._looping = True

        self._frame_locker = _threading.Lock()
        self._frame_content_changed = True

        self._video_has_audio = False

    def play(self):
        """
        🟩 **R** -
        """
        self._play_video = True
        self._video_player_thread = _threading.Thread(target=self._video_frame_extractor)
        self._video_player_thread.daemon = True
        self._video_player_thread.name = "Video:Playing_Video_Thread"
        self._video_player_thread.start()

    def set_looping(self, looping):
        """
        🟩 **R** -
        """
        self._audio_player.set_looping(looping)
        self._looping = looping

    def get_looping(self):
        """
        🟩 **R** -
        """
        return self._looping

    def stop(self):
        """
        🟩 **R** -
        """
        self._play_video = False
        if self._video_player_thread is not None:
            self._video_player_thread.join()

    def resume(self):
        """
        🟩 **R** -
        """
        self._is_playing = True

    def pause(self):
        """
        🟩 **R** -
        """
        self._is_playing = False

    def set_surface(self, surface=None):
        """
        🟩 **R** -
        """
        if surface is None:
            surface = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        """
        🟩 **R** -
        """
        return self._surface

    def autodetect_and_set_decoder(self, gpu: _GPU=None):
        """
        🟩 **R** -
        """
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
        """
        🟩 **R** -
        """
        self._video_decoder_manually_set = True
        self._input_stream.codec_context.options = {'hwaccel': decoder}

    def load_from_file(self, file_path, automatically_optimize_silent_videos=True):
        """
        🟩 **R** -
        """
        self._file = file_path
        self._input_container = _av.open(file_path)

        if automatically_optimize_silent_videos:
            self._video_has_audio = self.has_audio_and_non_zero_data()
        else:
            self._video_has_audio = True

        self._input_container.seek(0)

        if self._video_has_audio:
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

        self._shader.set_shader_variable("Texture", 0)
        self._texture.use(location=0)

        self._video_loaded = True

    def has_audio_and_non_zero_data(self):
        """
        🟩 **R** -
        """
        try:
            # Check for audio stream
            audio_stream = next((stream for stream in self._input_container.streams if stream.type == 'audio'), None)
            if not audio_stream:
                return False

            # Total duration of the video in seconds
            duration = self._input_container.duration / _av.time_base

            # Check audio data at each specified percentage
            for percent in _Constants.SINGLE_PERCENTAGES:
                # Calculate the target timestamp
                timestamp = int(duration * percent * _av.time_base)
                self._input_container.seek(timestamp, any_frame=False, backward=True, stream=audio_stream)

                # Check if audio frames at this point have non-zero data
                for packet in self._input_container.demux(audio_stream):
                    for frame in packet.decode():
                        audio_data = frame.to_ndarray()
                        if audio_data.any():  # Non-zero audio data found
                            return True
                    # Only check the first frame after seeking to avoid excessive processing
                    break

            return False

        except Exception as e:
            print(f"Error processing video file: {e}")
            return False

    def set_position(self, position, position_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if type(position) != _DisplayCoordinatesConverter:
            self._position.set_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._position.get_coordinates(format=format)

    def set_target_size(self, size, size_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if type(size) != _DisplayCoordinatesConverter:
            self._size.set_coordinates(size, format=size_format)
        else:
            self._size = size

    def get_target_size(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._size.get_coordinates(format=format)

    def get_video_size(self):
        """
        🟩 **R** -
        """
        return self._video_size

    def get_audio_channel(self):
        """
        🟩 **R** -
        """
        return self._audio_player

    def _loop_video(self):
        """
        🟩 **R** -
        """
        # Loop the video for demonstration purposes

        if self._looping:
            if self._audio_player.get_playing():
                self._audio_player.stop()
                self._audio_player.play(blocking=False, delay=0.58) # close / dont really know what this magic number represents yet

            self._input_container.seek(0)
            frame = next(self._input_container.decode(video=0))

            return frame
        else:
            self._play_video = False
            return

    def _video_frame_extractor(self):
        """
        🟩 **R** -
        """
        while self._play_video:
            if self._video_loaded:
                if self._audio_player.get_playing() is False and self._video_has_audio:
                    self._audio_player.play(blocking=False)
                    _time.sleep(0.48) # 0.5 close / dont really know what this magic number represents yet

                if self._is_playing is False and self._audio_player.get_paused() is False and self._video_has_audio:
                    self._audio_player.pause()

                if self._is_playing and self._audio_player.get_paused() and self._video_has_audio:
                    self._audio_player.resume()

                if self._is_playing:
                    try:
                        next_frame = next(self._input_container.decode(video=0))
                    except StopIteration:
                        next_frame = self._loop_video()
                    except _av.error.EOFError:
                        next_frame = self._loop_video()

                    if next_frame is not None:
                        frame = next_frame

                    # Convert frame to RGB for OpenGL
                    self._video_frame = frame.to_ndarray(format='rgb24')

                    with self._frame_locker:
                        self._frame_content_changed = True

            self._video_clock.tick(1/(self._video_frame_time))

    def render(self):
        """
        🟩 **R** -
        """
        if self._video_loaded and self._video_frame is not None:
            self._surface.update_attempted_render_calls(1)

            if self._surface.get_clear_called_but_skipped():
                return None

            self._surface.set_refresh_optimization_override(True)

            with self._frame_locker:
                if self._frame_content_changed:
                    self._surface.get_2D_hardware_accelerated_surface()

                    self._texture.write(self._video_frame)

                    user_desired_size = self._size.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                    scale = [user_desired_size[0] / self._video_size[0], user_desired_size[1] / self._video_size[1]]

                    offset = self._position.get_coordinates(format=_Constants.OPENGL_COORDINATES)
                    adjusted_offset = [offset[0] + 1, offset[1] - 1]

                    self._shader.set_shader_variable("scale", scale)
                    self._shader.set_shader_variable("offset", adjusted_offset)

                    self._frame_content_changed = False

            # Render the frame
            self._vao.render(_moderngl.TRIANGLE_STRIP)