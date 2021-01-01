from sound import *

BPM = 160.0
BPS = BPM/60
SPB = 1/BPS
SPMEA = 4 * SPB

intro = [
        ('A5', 'min7', 1), ('D5', 'dom7', 1), ('G5', 'maj7', 1), ('C5', 'maj7', 1),
        ('F#5', 'half_dim7', 1), ('B5', 'dom7', 1), ('E5', 'min6', 2)
]

body = [
        ('F#5', 'half_dim7', 1), ('B5', 'dom7', 1), ('E5', 'min6', 2),
        ('A5', 'min7', 1), ('D5', 'dom7', 1), ('G5', 'maj7', 2),
        ('F#5', 'half_dim7', 1), ('B5', 'dom7', 1), 
        ('E6', 'min7', .5), ('Eb6', 'dom7', .5), ('D6', 'min7', .5), ('Db6', 'dom7', .5), 
        ('C5', 'maj7', 1), ('B5', 'dom7', 1), ('E5', 'min6', 2)
]
changes = intro * 2 + body


def play_chords(BPM, chord_changes):
    all_waves = np.array([])

    BPS = BPM/60.0
    SPB = 1/BPS
    SPMEA = 4 * SPB

    for chord_change in chord_changes:
        root_freq = sci_to_freq(chord_change[0])
        chord_type = chord_change[1]
        duration = chord_change[2]
        chord_movement = chord_generator(root_freq, chords[chord_type], duration * SPMEA)
        all_waves = np.append(all_waves, chord_movement)

    return all_waves

s = play_chords(120, changes)
s = np.tile(s, 3)
wavio.write("autumn_leaves.wav", s , RATE, sampwidth=3)
