from create_song import *
from math import ceil

# Measured in beats

chords = [
((6,10), {0,4,7,10}, 4), ((5,3), {0,4,7,10}, 4), ((5,10),{0,4,7,10},8),
((5,3), {0,4,7,10}, 8), ((5, 10), {0,4,7,10}, 8),
((5,0), {0,3,7,10}, 4), ((5,5), {0,4,7,10}, 4), ((5,10), {0,4,7,10}, 2),
((5,0), {0,3,7,10}, 2), ((5,5), {0,4,7,10}, 2), ((5,0), {0,3,7,10}, 2) 
]

beats_chords_length = sum([x[2] for x in chords])
print(beats_chords_length)



beat = [
    [["Ride Cymbal 1", "Acoustic Bass Drum"], 1],
    [["Ride Cymbal 1"], 2/3],
    [["Ride Cymbal 1", "Acoustic Snare"], 1/3],
    [["Ride Cymbal 1"], 1],
    [["Ride Cymbal 1", "Acoustic Snare"], 2/3],
    [["Ride Cymbal 1"], 1/3],
]


drum_beat_len = sum([x[1] for x in beat])

beat_repeats = ceil(beats_chords_length/drum_beat_len)
print(beat_repeats)

beat = beat * beat_repeats





create_midi_song("sonny_midi.mid", 120,parse_note_song_into_objects(parse_song_into_notes(chords)),parse_drum_beat_into_objects(beat))
