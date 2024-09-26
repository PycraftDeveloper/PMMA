Audio (``pmma.Audio``)
======================

Not Yet Written

Create
------

.. py:method:: pmma.Audio() -> pmma.Audio

   Not Yet Written

Methods
-------

.. py:method:: Audio.quit() -> None

   Not Yet Written

.. py:method:: Audio.load_from_file() -> None

   Not Yet Written

.. py:method:: Audio.add_effect() -> None

   Not Yet Written

.. py:method:: Audio.set_volume() -> None

 t the volume (0.0 to 1.0)
    self._volume.set_value(volume, format=format)
    
    def set_pan(self, pan, format=_Constants.PERCENTAGE):
    Set the panning (-1.0 to 1.0, where 0 is center)

.. py:method:: Audio.set_pan() -> None

 t the panning (-1.0 to 1.0, where 0 is center)
    self._pan.set_value(pan, format=format)
    
    def play(self, blocking=True):
    if self._audio_loaded:
    self._effects = _Pedalboard(self._effects_list)
    self._paused = False
    self._stop_signal = False
    
    if blocking:
    # Start playback in the current thread (blocking)
    self._start_playback()
    else:
    # Start playback in a separate thread (non-blocking)
    self._playback_thread = _threading.Thread(target=self._start_playback)
    self._playback_thread.daemon = True
    self._playback_thread.start()
    
    def _wait_for_chunk_to_play(self):
    return not (self._start_frame < len(self._file) and not self._stop_signal)
    
    def _start_playback(self):
    # Start the audio stream
    with _sound_device.OutputStream(callback=self._audio_callback, samplerate=self._sample_rate, channels=self._file.channels):
    # Loop while playback is ongoing and not stopped
    _waiting.wait(self._wait_for_chunk_to_play)
    
    def _audio_callback(self, outdata, frames, time, status):
    if status:
    print(status)
    
    if self._paused or self._stop_signal:
    outdata[:] = _numpy.zeros(outdata.shape)
    return
    
    # Read frames from the file
    chunk = self._file.read(frames, dtype='float32')
    if len(chunk) < frames:
    chunk = _numpy.pad(chunk, ((0, frames - len(chunk)), (0, 0)), mode='constant')
    
    # Apply volume and panning
    chunk = self._apply_volume_and_pan(chunk)
    
    # Apply effects
    processed_audio = self._effects(chunk, self._sample_rate)
    
    # Output the processed audio
    outdata[:len(processed_audio)] = processed_audio
    
    self._start_frame += frames
    
    def _apply_volume_and_pan(self, chunk):
    Apply volume and panning to the chunk of audio

.. py:method:: Audio.play() -> None

   Not Yet Written

.. py:method:: Audio.pause() -> None

   Not Yet Written

.. py:method:: Audio.resume() -> None

   Not Yet Written

.. py:method:: Audio.stop() -> None

   Not Yet Written

.. py:method:: Audio.is_playing() -> None

   Not Yet Written

Bit Crush (``pmma.BitCrush``)
=============================

Not Yet Written

Create
------

.. py:method:: pmma.BitCrush() -> pmma.BitCrush

   Not Yet Written

Methods
-------

.. py:method:: BitCrush.set_bit_depth() -> None

   Not Yet Written

.. py:method:: BitCrush.get_bit_depth() -> None

   Not Yet Written

.. py:method:: BitCrush.quit() -> None

   Not Yet Written

Chorus (``pmma.Chorus``)
========================

Not Yet Written

Create
------

.. py:method:: pmma.Chorus() -> pmma.Chorus

   Not Yet Written

Methods
-------

.. py:method:: Chorus.set_rate() -> None

   Not Yet Written

.. py:method:: Chorus.get_rate() -> None

   Not Yet Written

.. py:method:: Chorus.set_depth() -> None

   Not Yet Written

.. py:method:: Chorus.get_depth() -> None

   Not Yet Written

.. py:method:: Chorus.set_center_delay() -> None

   Not Yet Written

.. py:method:: Chorus.get_center_delay() -> None

   Not Yet Written

.. py:method:: Chorus.set_feedback() -> None

   Not Yet Written

.. py:method:: Chorus.get_feedback() -> None

   Not Yet Written

.. py:method:: Chorus.set_mix() -> None

   Not Yet Written

.. py:method:: Chorus.get_mix() -> None

   Not Yet Written

.. py:method:: Chorus.quit() -> None

   Not Yet Written

Clipping (``pmma.Clipping``)
============================

Not Yet Written

Create
------

.. py:method:: pmma.Clipping() -> pmma.Clipping

   Not Yet Written

Methods
-------

.. py:method:: Clipping.set_threshold() -> None

   Not Yet Written

.. py:method:: Clipping.get_threshold() -> None

   Not Yet Written

.. py:method:: Clipping.quit() -> None

   Not Yet Written

Compressor (``pmma.Compressor``)
================================

Not Yet Written

Create
------

.. py:method:: pmma.Compressor() -> pmma.Compressor

   Not Yet Written

Methods
-------

.. py:method:: Compressor.set_threshold() -> None

   Not Yet Written

.. py:method:: Compressor.get_threshold() -> None

   Not Yet Written

.. py:method:: Compressor.set_ratio() -> None

   Not Yet Written

.. py:method:: Compressor.get_ratio() -> None

   Not Yet Written

.. py:method:: Compressor.set_attack() -> None

   Not Yet Written

.. py:method:: Compressor.get_attack() -> None

   Not Yet Written

.. py:method:: Compressor.set_release() -> None

   Not Yet Written

.. py:method:: Compressor.get_release() -> None

   Not Yet Written

.. py:method:: Compressor.quit() -> None

   Not Yet Written

Convolution (``pmma.Convolution``)
==================================

Not Yet Written

Create
------

.. py:method:: pmma.Convolution() -> pmma.Convolution

   Not Yet Written

Methods
-------

.. py:method:: Convolution.set_impulse_response_filename() -> None

   Not Yet Written

.. py:method:: Convolution.get_impulse_response_filename() -> None

   Not Yet Written

.. py:method:: Convolution.set_mix() -> None

   Not Yet Written

.. py:method:: Convolution.get_mix() -> None

   Not Yet Written

.. py:method:: Convolution.set_sample_rate() -> None

   Not Yet Written

.. py:method:: Convolution.get_sample_rate() -> None

   Not Yet Written

.. py:method:: Convolution.quit() -> None

   Not Yet Written

Delay (``pmma.Delay``)
======================

Not Yet Written

Create
------

.. py:method:: pmma.Delay() -> pmma.Delay

   Not Yet Written

Methods
-------

.. py:method:: Delay.set_delay() -> None

   Not Yet Written

.. py:method:: Delay.get_delay() -> None

   Not Yet Written

.. py:method:: Delay.set_feedback() -> None

   Not Yet Written

.. py:method:: Delay.get_feedback() -> None

   Not Yet Written

.. py:method:: Delay.set_mix() -> None

   Not Yet Written

.. py:method:: Delay.get_mix() -> None

   Not Yet Written

.. py:method:: Delay.quit() -> None

   Not Yet Written

Distortion (``pmma.Distortion``)
================================

Not Yet Written

Create
------

.. py:method:: pmma.Distortion() -> pmma.Distortion

   Not Yet Written

Methods
-------

.. py:method:: Distortion.set_drive() -> None

   Not Yet Written

.. py:method:: Distortion.get_drive() -> None

   Not Yet Written

.. py:method:: Distortion.quit() -> None

   Not Yet Written

G S M Full Rate Compressor (``pmma.GSMFullRateCompressor``)
===========================================================

Not Yet Written

Create
------

.. py:method:: pmma.GSMFullRateCompressor() -> pmma.GSMFullRateCompressor

   Not Yet Written

Methods
-------

.. py:method:: GSMFullRateCompressor.quit() -> None

   Not Yet Written

Gain (``pmma.Gain``)
====================

Not Yet Written

Create
------

.. py:method:: pmma.Gain() -> pmma.Gain

   Not Yet Written

Methods
-------

.. py:method:: Gain.set_gain() -> None

   Not Yet Written

.. py:method:: Gain.get_gain() -> None

   Not Yet Written

.. py:method:: Gain.quit() -> None

   Not Yet Written

High Shelf Filter (``pmma.HighShelfFilter``)
============================================

Not Yet Written

Create
------

.. py:method:: pmma.HighShelfFilter() -> pmma.HighShelfFilter

   Not Yet Written

Methods
-------

.. py:method:: HighShelfFilter.set_cutoff() -> None

   Not Yet Written

.. py:method:: HighShelfFilter.get_cutoff() -> None

   Not Yet Written

.. py:method:: HighShelfFilter.set_gain() -> None

   Not Yet Written

.. py:method:: HighShelfFilter.get_gain() -> None

   Not Yet Written

.. py:method:: HighShelfFilter.set_q() -> None

   Not Yet Written

.. py:method:: HighShelfFilter.get_q() -> None

   Not Yet Written

.. py:method:: HighShelfFilter.quit() -> None

   Not Yet Written

High Pass Filter (``pmma.HighPassFilter``)
==========================================

Not Yet Written

Create
------

.. py:method:: pmma.HighPassFilter() -> pmma.HighPassFilter

   Not Yet Written

Methods
-------

.. py:method:: HighPassFilter.set_cutoff() -> None

   Not Yet Written

.. py:method:: HighPassFilter.get_cutoff() -> None

   Not Yet Written

.. py:method:: HighPassFilter.quit() -> None

   Not Yet Written

Ladder Filter (``pmma.LadderFilter``)
=====================================

Not Yet Written

Create
------

.. py:method:: pmma.LadderFilter() -> pmma.LadderFilter

   Not Yet Written

Methods
-------

.. py:method:: LadderFilter.set_cutoff() -> None

   Not Yet Written

.. py:method:: LadderFilter.get_cutoff() -> None

   Not Yet Written

.. py:method:: LadderFilter.set_resonance() -> None

   Not Yet Written

.. py:method:: LadderFilter.get_resonance() -> None

   Not Yet Written

.. py:method:: LadderFilter.set_drive() -> None

   Not Yet Written

.. py:method:: LadderFilter.get_drive() -> None

   Not Yet Written

.. py:method:: LadderFilter.quit() -> None

   Not Yet Written

Limiter (``pmma.Limiter``)
==========================

Not Yet Written

Create
------

.. py:method:: pmma.Limiter() -> pmma.Limiter

   Not Yet Written

Methods
-------

.. py:method:: Limiter.set_threshold() -> None

   Not Yet Written

.. py:method:: Limiter.get_threshold() -> None

   Not Yet Written

.. py:method:: Limiter.set_release() -> None

   Not Yet Written

.. py:method:: Limiter.get_release() -> None

   Not Yet Written

.. py:method:: Limiter.quit() -> None

   Not Yet Written

Low Shelf Filter (``pmma.LowShelfFilter``)
==========================================

Not Yet Written

Create
------

.. py:method:: pmma.LowShelfFilter() -> pmma.LowShelfFilter

   Not Yet Written

Methods
-------

.. py:method:: LowShelfFilter.set_cutoff() -> None

   Not Yet Written

.. py:method:: LowShelfFilter.get_cutoff() -> None

   Not Yet Written

.. py:method:: LowShelfFilter.set_gain() -> None

   Not Yet Written

.. py:method:: LowShelfFilter.get_gain() -> None

   Not Yet Written

.. py:method:: LowShelfFilter.set_q() -> None

   Not Yet Written

.. py:method:: LowShelfFilter.get_q() -> None

   Not Yet Written

.. py:method:: LowShelfFilter.quit() -> None

   Not Yet Written

Low Pass Filter (``pmma.LowPassFilter``)
========================================

Not Yet Written

Create
------

.. py:method:: pmma.LowPassFilter() -> pmma.LowPassFilter

   Not Yet Written

Methods
-------

.. py:method:: LowPassFilter.set_cutoff() -> None

   Not Yet Written

.. py:method:: LowPassFilter.get_cutoff() -> None

   Not Yet Written

.. py:method:: LowPassFilter.quit() -> None

   Not Yet Written

M P 3 Compressor (``pmma.MP3Compressor``)
=========================================

Not Yet Written

Create
------

.. py:method:: pmma.MP3Compressor() -> pmma.MP3Compressor

   Not Yet Written

Methods
-------

.. py:method:: MP3Compressor.set_vbr_quality() -> None

   Not Yet Written

.. py:method:: MP3Compressor.get_vbr_quality() -> None

   Not Yet Written

.. py:method:: MP3Compressor.quit() -> None

   Not Yet Written

Noise Gate (``pmma.NoiseGate``)
===============================

Not Yet Written

Create
------

.. py:method:: pmma.NoiseGate() -> pmma.NoiseGate

   Not Yet Written

Methods
-------

.. py:method:: NoiseGate.set_threshold() -> None

   Not Yet Written

.. py:method:: NoiseGate.get_threshold() -> None

   Not Yet Written

.. py:method:: NoiseGate.set_ratio() -> None

   Not Yet Written

.. py:method:: NoiseGate.get_ratio() -> None

   Not Yet Written

.. py:method:: NoiseGate.set_attack() -> None

   Not Yet Written

.. py:method:: NoiseGate.get_attack() -> None

   Not Yet Written

.. py:method:: NoiseGate.set_release() -> None

   Not Yet Written

.. py:method:: NoiseGate.get_release() -> None

   Not Yet Written

.. py:method:: NoiseGate.quit() -> None

   Not Yet Written

Peak Filter (``pmma.PeakFilter``)
=================================

Not Yet Written

Create
------

.. py:method:: pmma.PeakFilter() -> pmma.PeakFilter

   Not Yet Written

Methods
-------

.. py:method:: PeakFilter.set_frequency() -> None

   Not Yet Written

.. py:method:: PeakFilter.get_frequency() -> None

   Not Yet Written

.. py:method:: PeakFilter.set_gain() -> None

   Not Yet Written

.. py:method:: PeakFilter.get_gain() -> None

   Not Yet Written

.. py:method:: PeakFilter.set_q() -> None

   Not Yet Written

.. py:method:: PeakFilter.get_q() -> None

   Not Yet Written

.. py:method:: PeakFilter.quit() -> None

   Not Yet Written

Phaser (``pmma.Phaser``)
========================

Not Yet Written

Create
------

.. py:method:: pmma.Phaser() -> pmma.Phaser

   Not Yet Written

Methods
-------

.. py:method:: Phaser.set_rate() -> None

   Not Yet Written

.. py:method:: Phaser.get_rate() -> None

   Not Yet Written

.. py:method:: Phaser.set_depth() -> None

   Not Yet Written

.. py:method:: Phaser.get_depth() -> None

   Not Yet Written

.. py:method:: Phaser.set_center_frequency() -> None

   Not Yet Written

.. py:method:: Phaser.get_center_frequency() -> None

   Not Yet Written

.. py:method:: Phaser.set_feedback() -> None

   Not Yet Written

.. py:method:: Phaser.get_feedback() -> None

   Not Yet Written

.. py:method:: Phaser.set_mix() -> None

   Not Yet Written

.. py:method:: Phaser.get_mix() -> None

   Not Yet Written

.. py:method:: Phaser.quit() -> None

   Not Yet Written

Pitch Shift (``pmma.PitchShift``)
=================================

Not Yet Written

Create
------

.. py:method:: pmma.PitchShift() -> pmma.PitchShift

   Not Yet Written

Methods
-------

.. py:method:: PitchShift.set_semitones() -> None

   Not Yet Written

.. py:method:: PitchShift.get_semitones() -> None

   Not Yet Written

.. py:method:: PitchShift.quit() -> None

   Not Yet Written

Re Sample (``pmma.ReSample``)
=============================

Not Yet Written

Create
------

.. py:method:: pmma.ReSample() -> pmma.ReSample

   Not Yet Written

Methods
-------

.. py:method:: ReSample.set_sample_rate() -> None

   Not Yet Written

.. py:method:: ReSample.get_sample_rate() -> None

   Not Yet Written

.. py:method:: ReSample.quit() -> None

   Not Yet Written

Reverb (``pmma.Reverb``)
========================

Not Yet Written

Create
------

.. py:method:: pmma.Reverb() -> pmma.Reverb

   Not Yet Written

Methods
-------

.. py:method:: Reverb.set_room_size() -> None

   Not Yet Written

.. py:method:: Reverb.get_room_size() -> None

   Not Yet Written

.. py:method:: Reverb.set_damping() -> None

   Not Yet Written

.. py:method:: Reverb.get_damping() -> None

   Not Yet Written

.. py:method:: Reverb.set_wet_level() -> None

   Not Yet Written

.. py:method:: Reverb.get_wet_level() -> None

   Not Yet Written

.. py:method:: Reverb.set_dry_level() -> None

   Not Yet Written

.. py:method:: Reverb.get_dry_level() -> None

   Not Yet Written

.. py:method:: Reverb.set_width() -> None

   Not Yet Written

.. py:method:: Reverb.get_width() -> None

   Not Yet Written

.. py:method:: Reverb.set_freeze_mode() -> None

   Not Yet Written

.. py:method:: Reverb.get_freeze_mode() -> None

   Not Yet Written

.. py:method:: Reverb.quit() -> None

   Not Yet Written

