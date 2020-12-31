import numpy as np
import wavio
import random
import sys


# Parameters
RATE = 44100    # samples per second
# Musical System
BASE_FREQUENCY = 440.0
EQUIVALENCE_RATIO = 2
NUMBER_ATOMIC_UNITS = 12
NUM_OCTS = random.randint(-3,3)
# diff = BASE_FREQUENCY * (EQUIVALENCE_RATIO-1)

seq = set()
# part = random.randint(1,69)
part = int(sys.argv[1])
print(sys.argv[2])
print(part)
for rip in range(part):
    # missing 1 1 thing
    seq.add(random.uniform(1/EQUIVALENCE_RATIO,EQUIVALENCE_RATIO))


# CHORDS
chords = {
        'dom7': [0, 4, 7, 10],
        'maj7': [0, 4, 7, 11],
        'min7': [0, 3, 7, 10], 
        'dim7': [0, 3, 6, 9],
        'half_dim7': [0, 3, 6, 10],
        'dom7flat9':[0, 3, 7, 11],
        'aug_maj7': [0, 4, 8, 10],
        'min7flat5':[0, 3, 6, 10],
        # Because 9 = 14 semitones, flat 9, 13 and 13 % 12 = 1
        'dom7flat9':[0, 4, 7, 10, 1], 
        'dom7sharp9': [0, 4, 7, 10, 3]
        }

letter_to_semitone = {
        'C':0 ,
        'C#':1,
        'Db':2,
        'D':2,
        'D#':3,
        'Eb':3,
        'E':4,
        'F':5,
        'F#':6,
        'Gb':6,
        'G':7,
        'G#':8,
        'Ab':8,
        'A':9,
        'A#':10,
        'Bb':10,
        'B':11
        }

def single_tone_generator(frequency, duration):
    # Compute waveform samples
    t = np.linspace(0, duration, duration*RATE, endpoint=False)
    x = np.sin(2*np.pi * frequency* t)
    return x

def chord_generator(root_freq, intervals, duration):
    out_wave = np.zeros(int(duration * RATE))
    for i in intervals:
        freq = root_freq * (2 ** (i/12.0))
        single_tone = single_tone_generator(freq, duration)
        out_wave= np.add(out_wave, single_tone)
    return out_wave

def sci_to_freq(sci_not):
    if len(sci_not) == 3:
        note = sci_not[0:2]
        octave = int(sci_not[2])
    else:
        note = sci_not[0]
        octave = int(sci_not[1])

    return 440 * (2 ** (octave -5 )) * (2 ** ((letter_to_semitone[note] - 9)/12.0))

print(sci_to_freq("Bb4"))


sort_seq = sorted(list(seq))
oof = np.array([])
for s in sort_seq:
    # print(len(oof))
    octopus = BASE_FREQUENCY*EQUIVALENCE_RATIO**2
    oof=np.append(oof,single_tone_generator(octopus*s, 1))
# print(oof)
# print(len(oof))

# Write the samples to a file
wavio.write("random_fuck.wav", oof, RATE, sampwidth=3)
