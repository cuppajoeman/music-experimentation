import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from theory_utils import *
from sound_utils import *

def create_song(title, BPM, chord_changes, times=1):
    all_waves = np.array([])
    final = np.array([])

    BPS = BPM/60.0
    SPB = 1/BPS
    SPMEA = 4 * SPB

    for chord_change in chord_changes:
        root_freq = sci_to_freq(chord_change[0])
        chord_type = chord_change[1]
        duration = chord_change[2]
        chord_movement = chord_generator(root_freq, chord_to_interval[chord_type], duration * SPMEA)
        all_waves = np.append(all_waves, chord_movement)

    for _ in range(times):
        final = np.append(final, all_waves)

    # Write the samples to a file
    wavio.write('generated_songs/' + title + ".wav", final, RATE, sampwidth=3)
