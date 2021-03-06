from theory import *
from theory_utils import *
import numpy as np
import wavio
import random

# Parameters
RATE = 44100    # samples per second

def single_tone_generator(frequency, duration,scale=1):
    # Compute waveform samples
    t = np.linspace(0, duration, int(duration*RATE), endpoint=False)
    x = np.sin(2*np.pi * frequency* t)  
    x *= scale
    return x

def harmonic_tone_generator(frequency, duration, num_harmonics=3):
    out_wave = np.zeros(int(duration * RATE))
    for i in range(1, num_harmonics + 1):
        single_tone = single_tone_generator(frequency * i, duration, 1/i)
        out_wave= np.add(out_wave, single_tone)
    return out_wave

def generate_chord_with_harmonics(base_frequency, intervals, duration, num_harmonics=3):
    out_wave = np.zeros(int(duration * RATE))
    for i in intervals:
        harmonic_tone = harmonic_tone_generator(base_frequency * (2**(i/12)), duration, num_harmonics)
        out_wave= np.add(out_wave, harmonic_tone)
    return out_wave


def sum_waves(waves):
    # assuming they are all the same duration
    out_wave = np.zeros(int(duration * RATE))
    for w in waves:
        out_wave= np.add(out_wave, w)
    return out_wave

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

def freq_to_sci(frequency):
    # TODO
    pass

def generate_roman_chord_frequencies(scale_freqs, roman_numeral):
    chord = []

    N = len(scale_freqs) - 1
    idx = ROMAN_NUMERALS.index(roman_numeral)

    for j in [0, 2, 4]:
        # We need to go to the next octave if we're out of the current scale
        # If you are or more than 7, we double you up (because we count from 0)
        mult = 2 if idx + j >= N else 1
        # 7 needs to map to 0 (7 unique notes in a scale 0, ... 6)
        freq = scale_freqs[(idx + j) % N] * mult
        chord.append(freq)
    return chord

def construct_romans(scale_freqs):
    duration = 1
    roman_chords = {}
    N = len(scale_freqs) - 1

    for i in range(N+1):
        # third up + 2 scale tones
        # 5 th up + 4 scale tones
        # need room to go up by four
        chord = np.zeros(int(duration * RATE))
        for j in [0, 2, 4]:
            # We need to go to the next octave if we're out of the current scale
            # If you are or more than 7, we double you up (because we count from 0)
            mult = 2 if i + j >= N else 1
            # 7 needs to map to 0 (7 unique notes in a scale 0, ... 6)
            freq = scale_freqs[(i + j) % N] * mult
            single_tone = single_tone_generator(freq, duration)
            chord = np.add(chord, single_tone)

        numeral = ROMAN_NUMERALS[i % len(ROMAN_NUMERALS)]
        roman_chords[numeral] = chord

    return roman_chords

def construct_scale(root_freq, scale_pattern, duration):
    intervals = [0]

    semitones_from_root = 0
    scale = np.array([])

    for f in generate_scale_frequencies(root_freq, scale_pattern):
        scale = np.append(scale, single_tone_generator(f, duration))

    return scale

def generate_scale_frequencies(root_freq, scale_pattern):
    intervals = [0]

    semitones_from_root = 0
    scale = []

    for skip in [0] + scale_pattern:
        semitones_from_root += skip
        interval = semitones_from_root
        scale.append(root_freq * (2 ** (interval/12)))

    return scale

def combine_waves_over_time(chord_waves):
    """chord waves is a list of sums of sin waves"""
    chord_progression = np.array([])
    for chord in chord_waves:
        chord_progression = np.append(chord_progression, chord)
    return chord_progression

def play_scale(scale, duration):
    """
    scale is a sequence of frequencies
    duraiton is the duraiton of each note
    """
    scale_output = np.array([])
    for f in scale:
        scale_output.extend(single_tone_generator(f, duration))
    return scale_output

def augment_chord(frequencies, interval):
    # TOOD MAKE A CHORD CLASS (MAYBE USE ALREADY ONE OR MAKE OWN)
    # That way we can write freqs.rootnote rather than freqs[0]
    root_freq = frequencies[0]
    frequencies.append(root_freq * (EQUIVALENCE_RATIO ** (interval/NUMBER_ATOMIC_UNITS)))

def create_series_of_interval_contexts(base_frequency, interval_contexts, durations = [], num_harmonics=3, BPM=120):
    # an interval context is a voicing
    # len(i_c) == len(durations) or len(durations) == 0
    waves = []
    duration_index = 0
    for interval_context in interval_contexts:
        intervals = get_intervals(interval_context)
        if durations == []:
          waves.append(generate_chord_with_harmonics(base_frequency, intervals, 1.5, num_harmonics))
        else:
          measure_length = bpm_to_measure_length(BPM)
          true_duration = durations[duration_index] * measure_length
          waves.append(generate_chord_with_harmonics(base_frequency, intervals, true_duration, num_harmonics))
        duration_index += 1

    return combine_waves_over_time(waves)

two_five_one = ["2,, 2 5 9 0 4'", "7,, 7 11 2 5 8,", "0,, 0 4 7 11 2'"]
#new_one = ["8,, 8 0' 5' 6'", "7,, 7 11 3' 5", "3 9 2' 0''"]
#new_one = ["0 4 7 11", "0''' 4 7 11"]
new_one = [
   "0, 9, 11, 2 4 7",   # 0 2 4 7 9 11
   "6, 8, 9, 11 4 8",   # 6 8 9 11 4   (6)
   "11,, 7, 9, 1 3 7",  # 11 7 9 1 3 7 (1)
   "4, 5, 8, 9, 2 9",   # 4 5 8 9 2 9  (8)
   "9,, 6, 7, 11, 1 6", # 9 6 7 11 1 6 (1 6)
   "2, 5, 9, 0 7",      # 2 5 9 0 7
   "7,, 5, 9, 11, 4",   # 7 5 9 11 4
   "0, 4, 9, 11, 2"     # 0 4 9 11 2
]


TEMPLATE = [
    "X    X    X    X    ",
    "X    X    X    X    ",
    "X    X    X    X    ",
    "X    X    X    X    ",
    "X    X    X    X    ",
    "X    X    X    X    ",
    ]


not_voiceled = [
    "0,   0    4    7    ",
    "4,   4    8    11    2'   ",
    "5,   5    9    0'   ",
    "7,   7    11   5'   ",
    "0,   0'   4'   7'   ",
    ]

voiceled = [
    "0,   0    4    7    ",
    "4,   4    8    2'   ",
    "5,   5    9    0'   ",
    "7,   7    11   5'   ",
    "0,   0'   4'   7'   ",
    ]


durations = [1, 0.5, 0.5, 0.5, 0.5,0.5, 0.5, 1]
durations = [1/2, 1/2, 1/2, 1/2, 1]
    

def generate_wav_file(filename, samples):
    wavio.write(filename, samples , RATE, sampwidth=3)
    return


generate_wav_file("simple.wav", create_series_of_interval_contexts(440, not_voiceled, durations, num_harmonics = 3, BPM=80))
