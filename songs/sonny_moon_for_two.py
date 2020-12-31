from sound import *


song = [
        ('Bb6', 'dom7', 1), ('Eb5', 'dom7', 1), ('Bb5', 'dom7', 2), 
        ('Eb5', 'dom7', 2), ('Bb5', 'dom7', 2),
        ('C5', 'min7', 1), ('F5', 'dom7', 1), ('Bb5', 'dom7', .5), ('G5', 'dom7', .5), ('C5', 'min7', .5), ('F5', 'dom7', .5)
]

def create_song(BPM, chord_changes):
    all_waves = np.array([])

    BPS = BPM/60.0
    print(BPS)
    SPB = 1/BPS
    SPMEA = 4 * SPB

    for chord_change in chord_changes:
        print(chord_change)
        root_freq = sci_to_freq(chord_change[0])
        print(root_freq)
        chord_type = chord_change[1]
        duration = chord_change[2]
        print(duration, SPMEA)
        chord_movement = chord_generator(root_freq, chords[chord_type], duration * SPMEA)
        all_waves = np.append(all_waves, chord_movement)
    return all_waves

# Write the samples to a file
wavio.write("sonny_moon_for_two.wav", create_song(160, song), RATE, sampwidth=3)
