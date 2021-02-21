from create_song import *

# Measured in beats

song = [
((6,10), {0,4,7,10}, 4), ((5,3), {0,4,7,10}, 4), ((5,10),{0,4,7,10},8),
((5,3), {0,4,7,10}, 8), ((5, 10), {0,4,7,10}, 8),
((5,0), {0,3,7,10}, 4), ((5,5), {0,4,7,10}, 4), ((5,10), {0,4,7,10}, 2),
((5,0), {0,3,7,10}, 2), ((5,5), {0,4,7,10}, 2)
]

print(parse_song_into_notes(song))

create_midi_song("sonny_midi.mid", 120,parse_note_song_into_objects(parse_song_into_notes(song)))
