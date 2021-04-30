# Get thinkdsp.py

import os

if not os.path.exists('signal test.py'):
    !wget https://freesound.org/people/tim.kahn/sounds/563652/ #https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py

    #if not os.path.exists('170255__dublie__trumpet.wav'):
    #!wget https://github.com/AllenDowney/ThinkDSP/raw/master/code/170255__dublie__trumpet.wav


from signal test import read_wave

wave = read_wave('563561__badoink__scratchy118bpm.wav')
wave.normalize()
wave.make_audio()

segment = wave.segment(start=1.1, duration=0.3)
segment.make_audio()

segment.plot()

segment.segment(start=1.1, duration=0.005).plot()

spectrum = segment.make_spectrum()
spectrum.plot(high=7000)

spectrum = segment.make_spectrum()
spectrum.plot(high=1000)

spectrum.peaks()[:30]

spectrum.low_pass(2000)

spectrum.make_wave().make_audio()

from signal test import decorate
from IPython.display import display

def filter_wave(wave, start, duration, cutoff):
    """Selects a segment from the wave and filters it.
    
    Plots the spectrum and displays an Audio widget.
    
    wave: Wave object
    start: time in s
    duration: time in s
    cutoff: frequency in Hz
    """
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()

    spectrum.plot(high=5000, color='0.7')
    spectrum.low_pass(cutoff)
    spectrum.plot(high=5000, color='#045a8d')
    decorate(xlabel='Frequency (Hz)')
    
    audio = spectrum.make_wave().make_audio()
    display(audio)

################################################


from thinkdsp import SinSignal

signal = (SinSignal(freq=400, amp=1.0) +
          SinSignal(freq=600, amp=0.5) +
          SinSignal(freq=800, amp=0.25))
signal.plot()

wave2 = signal.make_wave(duration=1)
wave2.apodize()

wave2.make_audio()

spectrum = wave2.make_spectrum()
spectrum.plot(high=2000)

signal += SinSignal(freq=450)
signal.make_wave().make_audio()


########################################################


wave3 = read_wave('170255__dublie__trumpet.wav')
wave3.normalize()
wave3.make_audio()

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

    stretch(wave3, 0.5)
wave3.make_audio()

wave3.plot()

