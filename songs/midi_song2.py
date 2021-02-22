from create_song import *
import pprint
from math import ceil
from musical_intelligence import *

# How insensitive

chords = [
((4,2), {0,3,7,10}, 8), ((4,1), {0,3,6,9}, 8), ((4,0),{0,3,7,9},8),((3,7),{0,4,7,10},8), ((3,10),{0,4,7,9},8), ((4,3),{0,4,7,11},8)
((4,4), {0,3,7,10}, 8)




((4,3), {0,4,7,10}, 8), ((4, 10), {0,4,7,10}, 8),
((4,0), {0,3,7,10}, 4), ((4,5), {0,4,7,10}, 4), ((4,10), {0,4,7,10}, 2),
((4,0), {0,3,7,10}, 2), ((4,5), {0,4,7,10}, 2), ((4,0), {0,3,7,10}, 2) 
]

beats_chords_length = sum([x[2] for x in chords])

d = Drummer(8)
d.create_jazz_groove(beats_chords_length)

create_midi_song("sonny_midi.mid", 110,parse_note_song_into_objects(parse_song_into_notes(chords)),d.beat)
