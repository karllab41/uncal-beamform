import numpy as np
import scipy.io.wavfile as wav

(rate,sig) = wav.read("output.wav")

sig = sig.astype(np.float64) / sig.max()

import numpy as np
import scikits.audiolab

# data = np.random.uniform(-1,1,44100)
# write array to file:
# scikits.audiolab.wavwrite(data, 'test.wav', fs=44100, enc='pcm16')
# play the array:
scikits.audiolab.play(sig[:,1], fs=rate)



# import numpy as np
# from scipy.io.wavfile import write
# 
# data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
# scaled = np.int16(data/np.max(np.abs(data)) * 32767)
# write('test.wav', 44100, scaled)


