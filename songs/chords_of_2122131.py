from create_song import *
import pprint
from math import ceil

chords = [
((4, 0), {0, 3, 7, 11},4),
((4, 2), {0, 3, 6, 10},4),
((4, 3), {0, 4, 8, 11},4),
((4, 5), {0, 3, 7, 10},4),
((4, 7), {0, 4, 7, 10},4),
((4, 8), {0, 4, 7, 11},4),
((4, 11), {0, 3, 6, 9},4),
((5, 0), {0, 3, 7, 11},4),
]



create_midi_song("chords_of_2122131.mid", 110,parse_note_song_into_objects(parse_song_into_notes(chords)))
