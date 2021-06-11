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

two_five_one = [generate_chord_with_harmonics(shift_freq_by_n_semitones(440,2), [-24, 0,3,7,10, 2], 1.5, 3), generate_chord_with_harmonics(shift_freq_by_n_semitones(440, 7), [-24, 0,4,7,10, 1], 1.5, 3) , generate_chord_with_harmonics(440, [24,4,7,11, 2], 1.5, 3)]

new_one = [generate_chord_with_harmonics(shift_freq_by_n_semitones(440,8), [-24, 0,4,9,10], 1.5, 3), generate_chord_with_harmonics(shift_freq_by_n_semitones(440, 7), [-24, 0,4,8,10], 1.5, 3) , generate_chord_with_harmonics(440, [-24, 0,3,9,2], 1.5, 3)]

wavio.write("simple.wav", combine_waves_over_time(new_one) , RATE, sampwidth=3)
