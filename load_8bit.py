import wave
import librosa
import soundfile as sf
import numpy as np
x,_ = librosa.load('./8bit_8000hz.WAV', sr=8000)
print(len(x))

sf.write('tmp.wav', x, 8000, 'PCM_U8')
# wave.open('tmp.wav','r')

# sf.write('stereo_file.flac', np.random.randn(10), 8000, 'PCM_S8')

print("fac types", sf.available_subtypes('FLAC'))
print("wav types", sf.available_subtypes('WAV'))
