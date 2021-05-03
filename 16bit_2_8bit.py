import numpy as np
from scipy.io import wavfile

sampling_rate = 44100
freq = 440
samples = 44100

x = np.arange(samples)
y = 100*np.sin(2 * np.pi * freq * x / sampling_rate)

wavfile.write("362.wav", sampling_rate, y)