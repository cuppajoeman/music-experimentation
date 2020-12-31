import pyaudio
import struct
import math
import wave
import random
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

SHRT_MAX=32767 # short uses 16 bits in complement 2

def my_sin(t,frequency):
    radians = t * frequency * 2.0 * math.pi
    pulse = math.sin(radians)
    return pulse

#pulse_function creates numbers in [-1,1] interval
def generate(duration = 5,pulse_function = (lambda t: my_sin(t,1000))):
    frames = []
    # Configuration
    sample_width=2  
    sample_rate = 44100
    #sample_rate = 16000
    #sample_rate = 48000
    sample_duration = 1.0/sample_rate
    total_samples = int(sample_rate * duration)
    p = pyaudio.PyAudio()
    pformat = p.get_format_from_width(sample_width)
    # Open stream for writing
    stream = p.open(format=pformat,channels=1,rate=sample_rate,output=True)
    for n in range(total_samples):
        t = n*sample_duration
        pulse = int(SHRT_MAX*pulse_function(t))
        data=struct.pack("h",pulse)
        frames.append(data)
        #frames.append(pulse.to_bytes(16, byteorder='little',signed=True))
        #stream.write(data)
    return frames

#example of a function I took from wikipedia.
major_chord = f = lambda t: (my_sin(t,440)+my_sin(t,550)+my_sin(t,660))/3

#choose any frequency you want
#choose amplitude from 0 to 1
def create_pulse_function(frequency=1000,amplitude=1):
    return lambda t: amplitude * my_sin(t,frequency)

def chord_sampler(pitches):
    return lambda t: sum(p(t) for p in pitches)/len(pitches)

if __name__=="__main__":
    frames = []
    b = 440
    c = 2
    m = 12
    b = int(sys.argv[1])
    c = int(sys.argv[2])
    m = int(sys.argv[3])
    # Demonstrate Equivalence
    f = create_pulse_function(b,1)
    frames.extend(generate(1,pulse_function=f))
    f = create_pulse_function(b * c,1)
    frames.extend(generate(1,pulse_function=f))
    # Run through all notes
    for k in range(m+1):
        f = create_pulse_function(b * (c ** (k/m)),1)
        frames.extend(generate(.5,pulse_function=f))

    ### Play chord
    #pitches= [create_pulse_function(b * c,1) ,  create_pulse_function(b * c/2,1) , create_pulse_function(b * c,1)]
    #f = chord_sampler(pitches)
    #frames.extend(generate(3,pulse_function=f))

    ##Jazz
    ## Play jump pattern
    pattern = [0 ,3 ,5 ,6 ,7 ,10 ,12]
    #pattern = [0 ,6, 7,10 ,12 ,14, 18,20 ,24]
    for k in pattern:
        f = create_pulse_function(b * (c ** (k/m)),1)
        frames.extend(generate(.5,pulse_function=f))

    # Produce random song
    for _ in range(random.randint(30, 100)):
        duration = 2 ** random.randint(-2, 2)

        pitches = []
        for _ in range(random.randint(1, 5)):
            k = random.choice(pattern)
            pitches.append(create_pulse_function(b * (c ** (k/m)),1))

        f = chord_sampler(pitches)
        frames.extend(generate(duration,pulse_function=f))

    ## Random number of chords
    for _ in range(random.randint(5,10)):
        # Random number of notes in the chord
        pitches = []
        for _ in range(random.randint(2, 6)):
            k = random.randint(0,m+1)
            pitches.append(create_pulse_function(b * (c ** (k/m)),1))

        f = chord_sampler(pitches)
        frames.extend(generate(3,pulse_function=f))

    ### Produce random song
    #for _ in range(random.randint(500, 1000)):
    #    duration = 2 ** random.randint(-4, 1)
    #    duration = random.random()
    #    k = random.randint(0,m+1)
    #    f = create_pulse_function(b * (c ** (k/m)),1)
    #    frames.extend(generate(duration,pulse_function=f))



    WAVE_OUTPUT_FILENAME = "samples/N({}Hz,{},{}) sample.wav".format(b, c, m)
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

