from create_song import *
import pprint
from math import ceil
from musical_intelligence import *

import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '../visualizations'))
from chord_drawer import *

def pos_mod(x,m):
    return (x%m + m)%m;

def elementwise_sum(l1, l2):
    """
    Precondition: len(l1) == len(l2)
    """
    return [pos_mod((a + b), 12) for a, b in zip(l1, l2)]



key = 5
intro = [
    [[3, 5], [0, 4, 7, 11], 4],
    [[3, 7], [0, 4, 7, 10], 4],
    [[3, 5], [0, 5, 7, 10], 8],
    [[3, 2], [0, 4, 7, 10], 4],
    [[3, 4], [0, 3, 7, 10], 4],
    [[3, 2], [0, 2, 4, 7, 10], 8],
    [[3, 2], [0, 3, 7, 9], 4],
    [[3, 6], [0, 5, 8], 2],
    [[3, 7], [0, 4, 7, 9], 2],
    [[3, 2], [0,2,4, 7, 11], 4],
    [[2, 11], [0, 3, 7, 10], 4],
    [[3, 4], [0, 2, 6, 10], 4],
    [[3, 4], [0, 3,5, 7, 10], 4],
]

main = [
    [[3, 0], [0, 3, 7, 10], 4],
    [[3, 4], [0, 4, 7, 9], 2],
    [[3, 6], [0, 2, 4, 7], 2],
    [[3, 7], [0, 3, 9], 4],
    [[3, 5], [0, 3, 7, 10], 2],

    [[3, 2], [0, 3, 7, 10], 2],
    [[3, 3], [0,2, 4, 7, 11], 4],
    [[3, 0], [0, 3, 7, 10], 4],
]

ending = [
    [[3, 0], [0, 3, 7, 10], 4],
    [[3, 10], [0, 2, 4, 7, 10], 8],
    [[3, 10], [0, 3, 7, 9], 4],
    [[3, 8], [0, 5, 8], 2],
    [[3, 3], [0, 4, 7, 9], 2],
    [[3, 1], [0, 4, 7, 9], 8],
    [[3, 0], [0, 5, 7, 9], 16],
]



song = []

song.extend(intro*2 + main + ending)



beats_chords_length = sum([x[2] for x in song])

d = Drummer(8)
d.create_jazz_groove(beats_chords_length)

create_midi_song("new.mid", 100,parse_note_song_into_objects(parse_song_into_notes(song,key)),d.beat)
visualize_chords(song,key,"new")
#create_midi_song("new.mid", 120,parse_note_song_into_objects(parse_song_into_notes(ending,key)), d.beat)
