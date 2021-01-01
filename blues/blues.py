import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from sound import *

KEY = sys.argv[1]


# TODO: After roman analysis, we won't need to pass in the chord type.
changes = [
        ("I", "maj_tri", 1), ("IV", "maj_tri", 1), ("I", "maj_tri", 1),("I", "dom7", 1),
        ("IV", "maj_tri", 1), ("IV", "dom7", 1), ("I", "maj_tri", 1),("I", "dom7", 1),
        ("V", "maj_tri", 1), ("IV", "maj_tri", 1), ("I", "maj_tri", 1),("V", "dom7", 1)
]

def create_blues_roman(BPM, changes):
    all_waves = np.array([])

    BPS = BPM/60.0
    SPB = 1/BPS
    SPMEA = 4 * SPB

    scale_freqs = generate_scale_frequencies(sci_to_freq(KEY), scales['maj'])

    all_waves = np.array([])
    for change in changes:
        roman_numeral = change[0]
        chord_type = change[1]
        duration = change[2]

        chord = generate_roman_chord_frequencies(scale_freqs, roman_numeral)
        
        print(chord)

        if '7' in chord_type:
            augment_chord(chord, 10)


        chord_waves = sum_frequencies(chord, duration * SPMEA)
        all_waves = np.append(all_waves, chord_waves)

    return all_waves


wavio.write("blues.wav", create_blues_roman(160, changes), RATE, sampwidth=3)

