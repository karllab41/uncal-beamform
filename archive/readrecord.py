import sounddevice as sd

fs = 44100
duration = 10  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=2)

