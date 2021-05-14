import pyaudio
import numpy as np
from gpio_translator import gpio_leds

def responsiveAudio (full_color):

    CHUNK = 2**11
    RATE = 44100
    PAINT16_MAXVAL = 32,767

    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                frames_per_buffer=CHUNK)

    while True:
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)

        peak=np.average(np.abs(data))*2
        bars="#"*int(50*peak/2**16)
        print("%05d %s"%(peak,bars))

        gpio_leds(full_color*peak/PAINT16_MAXVAL)


    #TODO LOOPBACK DEL OUTPUT AL INPUT VIRTUAL