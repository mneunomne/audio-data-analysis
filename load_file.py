import pyaudio
import wave
import sys
import time
import matplotlib as mpl
from matplotlib import pyplot
from matplotlib import colors
import numpy as np
import codecs, json

CHUNK = 1024 * 10 # 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
print(p.get_format_from_width(wf.getsampwidth()),wf.getframerate(), wf.getnchannels())
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)

values = []

# play stream (3)
while len(data) > 0:
    int_list = []
    byte_list = []

    # print(data.decode("utf-16"))
    byte_array = [data[i:i+2] for i in range(0, len(data), 2)]
    # byte = b"".join(byte_array)
    print(len(byte_array))

    # stream.write(data)
    a = 0
    b = 255
    for i in byte_array:
        int_val = int.from_bytes(i, "big")
        # print(int_val)
        int_val = int(int_val)
        val = float(int_val / 2**16 * 255)
        values.append(val)
        # print(val)
        # time.sleep(0.01)
        a = min(a, val)
        b = max(b, val)
        int_list.append(int_val)
        bytes_val = int_val.to_bytes(2, 'big')
        byte_list.append(bytes_val)
    
    # print(a, b)
    byte = b"".join(byte_list)
    stream.write(byte)
        # print(byte)

    data = wf.readframes(CHUNK)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
# p.terminate()


grid_values = np.reshape(values, (-1, 62))

# print(grid_values)

data = grid_values.tolist() # nested lists with same data, indices
print(data)
file_path = "data.json" ## your path variable
json.dump(int_list, codecs.open(file_path, 'w', encoding='utf-8'), indent=2) ### this saves the array in .json format

# tell imshow about color map so that only set colors are used
# img = pyplot.imshow(grid_values, interpolation='nearest', cmap = 'magma')

pyplot.show()