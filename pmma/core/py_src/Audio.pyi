from typing import Literal, Union, Callable, Any

import pedalboard
from moviepy.audio.io.AudioFileClip import AudioFileClip

from pmma.build.NumberConverter import ProportionConverter, LinkedProportionConverter

Numerical = Union[float, int]

class Audio:
    volume: ProportionConverter  # Default volume is 100%
    pan: ProportionConverter  # Pan: -1 (left) to 1 (right), 0 is center

    def __init__(self) -> None: ...

    def __del__(self) -> None: ...

    def set_custom_audio_callback_function_pre_effects(self, function: Union[Callable[..., Any], None]=None) -> None: ...

    def set_custom_audio_callback_function_post_effects(self, function: Union[Callable[..., Any], None]=None) -> None: ...

    def get_custom_audio_callback_function_pre_effects_results(self) -> Any: ...

    def get_custom_audio_callback_function_post_effects_results(self) -> Any: ...

    def load_from_file(self, file_path: str) -> None: ...

    def get_sample_rate(self) -> int: ...

    def get_number_of_channels(self) -> int: ...

    def set_looping(self, loop: bool) -> None: ...

    def get_looping(self) -> bool: ...

    def set_duration(self, duration: Numerical) -> None: ...

    def set_silence_at_end_of_track(self, duration: Numerical) -> None: ...

    def load_from_moviepy(self, audio: AudioFileClip) -> None: ...

    def add_effect(
            self,
            effect: Union[Chorus, Compressor,
                            Convolution, Delay, Phaser,
                            Reverb, pedalboard.Bitcrush,
                            pedalboard.Chorus, pedalboard.Clipping,
                            pedalboard.Compressor,
                            pedalboard.Convolution, pedalboard.Delay,
                            pedalboard.Distortion,
                            pedalboard.GSMFullRateCompressor,
                            pedalboard.Gain, pedalboard.HighShelfFilter,
                            pedalboard.HighpassFilter,
                            pedalboard.LadderFilter, pedalboard.Limiter,
                            pedalboard.LowShelfFilter,
                            pedalboard.LowpassFilter,
                            pedalboard.MP3Compressor,
                            pedalboard.NoiseGate, pedalboard.PeakFilter,
                            pedalboard.Phaser, pedalboard.PitchShift,
                            pedalboard.Resample,
                            pedalboard.Reverb]) -> None: ...

    def remove_effect(
            self,
            effect: Union[Chorus, Compressor,
                            Convolution, Delay, Phaser,
                            Reverb, pedalboard.Bitcrush,
                            pedalboard.Chorus, pedalboard.Clipping,
                            pedalboard.Compressor,
                            pedalboard.Convolution, pedalboard.Delay,
                            pedalboard.Distortion,
                            pedalboard.GSMFullRateCompressor,
                            pedalboard.Gain, pedalboard.HighShelfFilter,
                            pedalboard.HighpassFilter,
                            pedalboard.LadderFilter, pedalboard.Limiter,
                            pedalboard.LowShelfFilter,
                            pedalboard.LowpassFilter,
                            pedalboard.MP3Compressor,
                            pedalboard.NoiseGate, pedalboard.PeakFilter,
                            pedalboard.Phaser, pedalboard.PitchShift,
                            pedalboard.Resample,
                            pedalboard.Reverb]) -> None: ...

    def play(self, blocking: bool=True, delay: Numerical=0) -> bool: ...

    def pause(self) -> None: ...

    def resume(self) -> None: ...

    def stop(self) -> None: ...

    def get_paused(self) -> bool: ...

    def get_playing(self) -> bool: ...

class Chorus(pedalboard.Chorus):
    proportion_adjusted_depth: LinkedProportionConverter
    proportion_adjusted_feedback: LinkedProportionConverter
    proportion_adjusted_mix: LinkedProportionConverter

    def __init__(
            self,
            rate: int=1,
            depth: Numerical=25,
            center_delay: Numerical=0.007,
            feedback: Numerical=0,
            mix: Numerical=50,
            format: Literal["percentage", "decimal"]="percentage",
            depth_format: Literal["percentage", "decimal", None]=None,
            feedback_format: Literal["percentage", "decimal", None]=None,
            mix_format: Literal["percentage", "decimal", None]=None) -> None: ...

    def set_rate(self, rate: int) -> None: ...

    def get_rate(self) -> int: ...

    def set_center_delay(self, center_delay: Numerical) -> None: ...

    def get_center_delay(self) -> Numerical: ...

class Compressor(pedalboard.Compressor):
    def __init__(
            self,
            threshold: Numerical=0,
            ratio: Numerical=4,
            attack: Numerical=0.001,
            release: Numerical=0.1) -> None: ...

    def set_threshold(self, threshold: Numerical) -> None: ...

    def get_threshold(self) -> Numerical: ...

    def set_ratio(self, ratio: Numerical) -> None: ...

    def get_ratio(self) -> Numerical: ...

    def set_attack(self, attack: Numerical) -> None: ...

    def get_attack(self) -> Numerical: ...

    def set_release(self, release: Numerical) -> None: ...

    def get_release(self) -> Numerical: ...

class Convolution(pedalboard.Convolution):
    proportion_adjusted_mix: LinkedProportionConverter

    def __init__(
            self,
            impulse_response_filename: str,
            mix: Numerical=100,
            sample_rate: Union[int, None]=None,
            format: Literal["percentage", "decimal"]="percentage",
            mix_format: Literal["percentage", "decimal", None]=None) -> None: ...

    def set_impulse_response_filename(self, impulse_response: str) -> None: ...

    def get_impulse_response_filename(self) -> str: ...

    def set_sample_rate(self, sample_rate: Union[int, None]) -> None: ...

    def get_sample_rate(self) -> Union[int, None]: ...

class Delay(pedalboard.Delay):
    proportion_adjusted_feedback: LinkedProportionConverter
    proportion_adjusted_mix: LinkedProportionConverter

    def __init__(
            self,
            delay: Numerical=0.5,
            feedback: Numerical=0,
            mix: Numerical=50,
            format: Literal["percentage", "decimal"]="percentage",
            feedback_format: Literal["percentage", "decimal", None]=None,
            mix_format: Literal["percentage", "decimal", None]=None) -> None: ...

    def set_delay(self, delay: Numerical) -> None: ...

    def get_delay(self) -> Numerical: ...

class Phaser(pedalboard.Phaser):
    proportion_adjusted_depth = LinkedProportionConverter
    proportion_adjusted_feedback = LinkedProportionConverter
    proportion_adjusted_mix = LinkedProportionConverter

    def __init__(
            self,
            rate: int=1,
            depth: Numerical=50,
            center_frequency: int=1300,
            feedback: Numerical=0,
            mix: Numerical=50,
            format: Literal["percentage", "decimal"]="percentage",
            depth_format: Literal["percentage", "decimal", None]=None,
            feedback_format: Literal["percentage", "decimal", None]=None,
            mix_format: Literal["percentage", "decimal", None]=None) -> None: ...

    def set_rate(self, rate: int) -> None: ...

    def get_rate(self) -> int: ...

    def set_center_frequency(self, center_frequency: int) -> None: ...

    def get_center_frequency(self) -> int: ...

class Reverb(pedalboard.Reverb):
    proportion_adjusted_room_size = LinkedProportionConverter
    proportion_adjusted_damping = LinkedProportionConverter
    proportion_adjusted_wet_level = LinkedProportionConverter
    proportion_adjusted_dry_level = LinkedProportionConverter
    proportion_adjusted_width = LinkedProportionConverter

    def __init__(
            self,
            room_size: Numerical=100,
            damping: Numerical=50,
            wet_level: Numerical=33,
            dry_level: Numerical=40,
            width: Numerical=100,
            freeze_mode: bool=False,
            format: Literal["percentage", "decimal"]="percentage",
            room_size_format: Literal["percentage", "decimal", None]=None,
            damping_format: Literal["percentage", "decimal", None]=None,
            wet_level_format: Literal["percentage", "decimal", None]=None,
            dry_level_format: Literal["percentage", "decimal", None]=None,
            width_format: Literal["percentage", "decimal", None]=None) -> None: ...

    def set_freeze_mode(self, freeze_mode: bool) -> None: ...

    def get_freeze_mode(self) -> bool: ...