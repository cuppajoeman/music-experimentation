from create_song import *
import pprint
from math import ceil
from musical_intelligence import *


song = [
#3[(3, 9),[0, 3, 7, 10], 4],
#3[(3, 5),[0, 3, 7, 10], 4],
#3[(3, 2),[0, 4, 7, 10], 4],
#3[(3, 3),[0, 3, 6, 10], 2],
#3[(3, 3),[0, 4, 6, 10], 2],
#3
#3[(3, 9),[0, 3, 7, 10], 4],
#3[(3, 5),[0, 3, 7, 10], 4],
#3[(3, 4),[0, 4, 7, 10], 4],
#3[(3, 5),[0, 4, 7, 10], 2],
#3[(3, 7),[0, 3, 6, 10], 2],
[(3, 8),[0,2, 3, 7, 10], 2],
[(3, 6),[0, 4, 7, 10], 2],
[(3, 4),[0, 2, 7, 10], 2],
[(3, 4),[0, 2, 5, 10], 2],
[(3, 1),[0, 3, 7, 10], 4],

[(3, 4),[0, 2, 5, 10], 4],
[(3, 3),[0, 3, 7, 10], 2],

]

beats_chords_length = sum([x[2] for x in song])

d = Drummer(8)
d.create_jazz_groove(beats_chords_length)

create_midi_song("6_to_4512_test.mid", 120,parse_note_song_into_objects(parse_song_into_notes(song)),d.beat)
