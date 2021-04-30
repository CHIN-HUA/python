#!/usr/bin/env python
# coding: utf-8

# ## ThinkDSP
# 
# This notebook contains code examples from Chapter 1: Sounds and Signals
# 
# Copyright 2015 Allen Downey
# 
# License: [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)
# 

# ## Think DSP module
# 
# `thinkdsp` is a module that accompanies _Think DSP_ and provides classes and functions for working with signals.
# 
# [Documentation of the thinkdsp module is here](http://greenteapress.com/thinkdsp.html). 

# In[32]:


# Get thinkdsp.py

import os

if not os.path.exists('thinkdsp.py'):
    get_ipython().system('wget https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py')


# ## Signals
# 
# Instantiate cosine and sine signals.

# In[33]:


from thinkdsp import CosSignal, SinSignal

cos_sig = CosSignal(freq=450, amp=1.0, offset=0)
sin_sig = SinSignal(freq=900, amp=0.5, offset=0)


# Plot the sine and cosine signals.  By default, `plot` plots three periods.  

# In[34]:


from thinkdsp import decorate

cos_sig.plot()
decorate(xlabel='Time (s)')


# Here's the sine signal.

# In[35]:


sin_sig.plot()
decorate(xlabel='Time (s)')


# Notice that the frequency of the sine signal is doubled, so the period is halved.
# 
# The sum of two signals is a SumSignal.

# In[36]:


mix = sin_sig + cos_sig
mix


# Here's what it looks like.

# In[37]:


mix.plot()
decorate(xlabel='Time (s)')


# ## Waves
# 
# A Signal represents a mathematical function defined for all values of time.  If you evaluate a signal at a sequence of equally-spaced times, the result is a Wave.  `framerate` is the number of samples per second.

# In[38]:


wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave


# IPython provides an Audio widget that can play a wave.

# In[39]:


from IPython.display import Audio
audio = Audio(data=wave.ys, rate=wave.framerate)
audio


# Wave also provides `make_audio()`, which does the same thing:

# In[40]:


wave.make_audio()


# The `ys` attribute is a NumPy array that contains the values from the signal.  The interval between samples is the inverse of the framerate.

# In[41]:


print('Number of samples', len(wave.ys))
print('Timestep in ms', 1 / wave.framerate * 1000)


# Signal objects that represent periodic signals have a `period` attribute.
# 
# Wave provides `segment`, which creates a new wave.  So we can pull out a 3 period segment of this wave.

# In[42]:


period = mix.period
segment = wave.segment(start=0, duration=period*3)
period


# Wave provides `plot`

# In[43]:


segment.plot()
decorate(xlabel='Time (s)')


# `normalize` scales a wave so the range doesn't exceed -1 to 1.
# 
# `apodize` tapers the beginning and end of the wave so it doesn't click when you play it.

# In[44]:


wave.normalize()
wave.apodize()
wave.plot()
decorate(xlabel='Time (s)')


# You can write a wave to a WAV file.

# In[45]:


wave.write('temp.wav')


# `wave.write` writes the wave to a file so it can be used by an exernal player.

# In[46]:


from thinkdsp import play_wave

play_wave(filename='temp.wav', player='aplay')


# `read_wave` reads WAV files.  The WAV examples in the book are from freesound.org.  In the contributors section of the book, I list and thank the people who uploaded the sounds I use.

# In[49]:


from thinkdsp import read_wave

wave = read_wave('328878__tzurkan__guitar-phrase-tzu.wav')

##試試其他音效


# In[50]:


wave.make_audio()


# I pulled out a segment of this recording where the pitch is constant.  When we plot the segment, we can't see the waveform clearly, but we can see the "envelope", which tracks the change in amplitude during the segment.

# In[51]:


start = 1.0
duration = 0.9
segment = wave.segment(start, duration)
segment.plot()
decorate(xlabel='Time (s)')


# ## Spectrums
# 
# Wave provides `make_spectrum`, which computes the spectrum of the wave.

# In[52]:


spectrum = segment.make_spectrum()


# Spectrum provides `plot`

# In[53]:


spectrum.plot()
decorate(xlabel='Frequency (Hz)')


# The frequency components above 10 kHz are small.  We can see the lower frequencies more clearly by providing an upper bound:

# In[54]:


spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')


# Spectrum provides `low_pass`, which applies a low pass filter; that is, it attenuates all frequency components above a cutoff frequency.

# In[55]:


spectrum.low_pass(3000)


# The result is a spectrum with fewer components.

# In[56]:


spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')


# We can convert the filtered spectrum back to a wave:

# In[57]:


filtered = spectrum.make_wave()


# And then normalize it to the range -1 to 1.

# In[58]:


filtered.normalize()


# Before playing it back, I'll apodize it (to avoid clicks).

# In[59]:


filtered.apodize()
filtered.plot()
decorate(xlabel='Time (s)')


# And I'll do the same with the original segment.

# In[60]:


segment.normalize()
segment.apodize()
segment.plot()
decorate(xlabel='Time (s)')


# Finally, we can listen to the original segment and the filtered version.

# In[61]:


segment.make_audio()


# In[62]:


filtered.make_audio()


# The original sounds more complex, with some high-frequency components that sound buzzy.
# The filtered version sounds more like a pure tone, with a more muffled quality.  The cutoff frequency I chose, 3000 Hz, is similar to the quality of a telephone line, so this example simulates the sound of a violin recording played over a telephone.

# ## Interaction
# 
# The following example shows how to use interactive IPython widgets.

# In[63]:


import matplotlib.pyplot as plt
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

    spectrum.plot(color='0.7')
    spectrum.low_pass(cutoff)
    spectrum.plot(color='#045a8d')
    decorate(xlabel='Frequency (Hz)')
    plt.show()
    
    audio = spectrum.make_wave().make_audio()
    display(audio)


# Adjust the sliders to control the start and duration of the segment and the cutoff frequency applied to the spectrum.

# In[64]:


from ipywidgets import interact, fixed

wave = read_wave('92002__jcveliz__violin-origional.wav')
interact(filter_wave, wave=fixed(wave), 
         start=(0, 5, 0.1), duration=(0, 5, 0.1), cutoff=(0, 10000, 100));


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




