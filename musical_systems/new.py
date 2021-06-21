import numpy as np
import wavio

RATE = 22050  # samples per second

BASE_FREQUENCY = 195.99771799087466;

EQUIVALENCE_RATIO = 3

PARTITIONS = 5

MULTIPLIER = EQUIVALENCE_RATIO ** (1/PARTITIONS)

# 440 = A4

def SIN_to_freq(octave, semitones):
    return BASE_FREQUENCY * (EQUIVALENCE_RATIO ** (octave)) * (EQUIVALENCE_RATIO ** ((semitones)/PARTITIONS));

def create_sound_file(file_name, sound_array):
    wavio.write(file_name, sound_array, RATE, sampwidth=3)

def single_tone_generator(frequency, duration):
    # duration is in seconds because of hertz
    # Compute waveform samples
    t = np.linspace(0, duration, int(duration*RATE), endpoint=False)
    x = np.sin(2*np.pi * frequency* t)  
    return x

def sum_frequencies(frequencies, duration):
    out_wave = np.zeros(int(duration * RATE))
    for f in frequencies:
        single_tone = single_tone_generator(f, duration)
        out_wave= np.add(out_wave, single_tone)
    return out_wave

def chord_generator(root_freq, intervals, duration):
    out_wave = np.zeros(int(duration * RATE))
    # TODO: use sum_frequencies in here
    for i in intervals:
        freq = root_freq * (EQUIVALENCE_RATIO ** (i/PARTITIONS))
        single_tone = single_tone_generator(freq, duration)
        out_wave= np.add(out_wave, single_tone)
    return out_wave

def gen_chord_progression(chord_waves):
    """chord waves is a list of sums of sin waves"""
    chord_progression = np.array([])
    for chord in chord_waves:
        chord_progression = np.append(chord_progression, chord)
    return chord_progression

def demonstrate_system(duration):
    # returns a a sound array
    notes = []
    for octave in range(2):
        for i in range(PARTITIONS + 1):
            notes.append(single_tone_generator(SIN_to_freq(octave, i), duration))

    return gen_chord_progression(notes);

chord = sum_frequencies([SIN_to_freq(0,0), SIN_to_freq(0, 2), SIN_to_freq(0, 3), SIN_to_freq(0, 5)], 3)

system_demo = demonstrate_system(3);

sound_array = gen_chord_progression([system_demo, chord]);

create_sound_file("demo.wav", sound_array);



