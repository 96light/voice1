
import sounddevice as sd
import soundfile as sf
import time
import queue
import numpy

q = queue.Queue()



def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


def recording_file( sentence, name):
    try:
        # Make sure the file is opened before recording anything:
        with sf.SoundFile(name, mode='x', samplerate=22000,
                        channels=1) as file:
            with sd.InputStream(samplerate=22000, device=sd.default.device,
                                channels=1, callback=callback):
                print('#' * 80)
                print(sentence)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(name))

name='cau_18.wav'
sentence='ấ'

recording_file(sentence, name)
