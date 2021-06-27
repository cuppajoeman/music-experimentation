from theory import *
import math

# === CONVERT TO AND FROM SCIENTIFIC NOTATION & FREQUENCY ===


def sci_to_freq(sci_not):
    if len(sci_not) == 3:
        note = sci_not[0:2]
        octave = int(sci_not[2])
    else:
        note = sci_not[0]
        octave = int(sci_not[1])

    return 440 * (2 ** (octave - 4)) * (2 ** ((letter_to_semitone[note] - 9) / 12.0))


# === CONVERT TO AND FROM INTEGER NOTATION & FREQUENCY ===


def int_to_freq(oct_band, note_num):
    return 440 * (2 ** (oct_band - 4)) * (2 ** ((note_num) / 12.0))


def int_to_midi(oct_band, note_num):
    # We use 60 because that is c4
    return 60 + (oct_band - 4) * 12 + note_num


def root_and_intervals_to_int(root_octave_band, root_number, intervals):
    """Given a root note and a set of intervals (all in integer notation),
    we will generate the notes in integer notation and return them"""
    notes = []
    for interval in intervals:
        additional_bands, new_note_num = divmod(root_number + interval, 12)
        notes.append(
            SemitoneIntegerNotation(root_octave_band + additional_bands, new_note_num)
        )
    return notes


def root_and_intervals_to_int_no_obj(root_octave_band, root_number, intervals):
    """Given a root note and a set of intervals (all in integer notation),
    we will generate the notes in integer notation and return them"""
    notes = []
    for interval in intervals:
        additional_bands, new_note_num = divmod(root_number + interval, 12)
        notes.append((root_octave_band + additional_bands, new_note_num))
    return notes


def root_and_intervals_to_int_basic(root_number, intervals, octs=1):
    """
    This one actually returns integers, and doesn't use octave band

    octs represents the number of ocatave bands the notes can be within

    Given a root note and a set of intervals (all in integer notation),
    we will generate the notes in integer notation and return them"""
    notes = []
    for interval in intervals:
        notes.append((root_number + interval) % (12 * octs))
    return notes


def freq_to_sci(freq):
    # The fundemental observation is that any frequency is of the following form
    #           440 * 2 ** (x + y/12)  x in Z, and 0 <= y < 12
    # Think quotient remainder where the integers are the start points of each octave
    # x is the oct_range and y is the semi_count

    exp = math.log(freq / 440.0, 2)
    oct_range = math.floor(exp)
    # modulo one gives the decimal part of the number
    semi_count = round((exp % 1) * 12)
    # Since it's relative to A4, which is in the 5th octave range
    shifted_oct_range = oct_range + 4
    letter = semitone_to_letter[semi_count]
    return letter + str(shifted_oct_range)


def generate_scale_frequencies(root_freq, scale_pattern):
    intervals = [0]

    semitones_from_root = 0
    scale = []

    # Add zero for the first note
    for skip in [0] + scale_pattern:
        semitones_from_root += skip
        interval = semitones_from_root
        next_freq = shift_freq_by_n_semitones(root_freq, interval)
        scale.append(next_freq)

    return scale


def shift_freq_by_n_semitones(freq, n):
    return freq * (2 ** (n / 12.0))


def num_semi_above(f1, f2):
    # Return how many semitones higher f2 is than f1
    # Precond f1 < f2
    exp1 = math.log(f1 / 440.0, 2)
    exp2 = math.log(f2 / 440.0, 2)
    return round((exp2 - exp1) * 12)


def construct_roman_frequencies(scale_freqs):
    roman_chords = {}
    N = len(scale_freqs) - 1

    for i in range(N + 1):
        # third up + 2 scale tones
        # 5 th up + 4 scale tones
        # need room to go up by four
        chord = []
        for j in [0, 2, 4, 6]:
            # We need to go to the next octave if we're out of the current scale
            # If you are or more than 7, we double you up (because we count from 0)
            mult = 2 if i + j >= N else 1
            # 7 needs to map to 0 (7 unique notes in a scale 0, ... 6)
            freq = scale_freqs[(i + j) % N] * mult
            chord.append(freq)

        numeral = ROMAN_NUMERALS[i % len(ROMAN_NUMERALS)]
        roman_chords[numeral] = tuple(chord)

    return roman_chords


def analyze_roman_chords(rf):
    # rf is roman frequencies
    for k in rf:
        intervals = []
        for f in rf[k]:
            intervals.append(num_semi_above(rf[k][0], f))
        rf[k] = interval_to_chord[tuple(intervals)]
    return rf


def bpm_to_measure_length(BPM, beats_in_a_measure=4):
    # returns in seconds
    beats_per_second = BPM * 1 / 60
    seconds_per_beat = 1 / beats_per_second
    measure_length = seconds_per_beat * beats_in_a_measure

    return measure_length


import re

# Voicing Notation


def get_intervals(x):
    intervals = []
    for notation in x.split():
        intervals.append(parse_notation(notation))
    return intervals


def parse_notation(notation):
    # It will always have a digit
    d = re.search(r"[0-9]+", notation)
    digit = int(notation[d.start() : d.end()])

    m = re.search(r"[,']", notation)

    if m:
        direction = notation[m.start()]
        count = len(notation[m.start() :])
        multiplier = -1 if direction == "," else 1

        return digit + multiplier * count * 12
    else:
        return digit


# sf = generate_scale_frequencies(110, scales['mel_min'])
# sn = [freq_to_sci(y) for y in sf ]
#
# rf = construct_roman_frequencies(sf)
#
# print(analyze_roman_chords(rf))

# for k in rf:
#    rf[k] = [freq_to_sci(y) for y in rf[k] ]
#
# print(rf)
