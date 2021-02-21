from create_song import *

# Measured in beats

song = [
        ((4,0),{0},1),
        ((4,1),{0},1),
        ((4,2),{0},1),
        ((4,3),{0},1),
        ((4,4),{0},1),
        ((4,5),{0},1),
        ((4,6),{0},1),
        ((4,7),{0},1),
        ((4,8),{0},1),
        ((4,9),{0},1),
        ((4,10),{0},1),
        ((4,11),{0},1),
        ((5,0),{0},1),
]

print(parse_song_into_notes(song))

create_midi_song("scale.mid", 120,parse_note_song_into_objects(parse_song_into_notes(song)))
