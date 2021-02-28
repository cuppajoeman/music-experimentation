from create_song import *
import pprint
from math import ceil
from musical_intelligence import *

def pos_mod(x,m):
    return (x%m + m)%m;

def elementwise_sum(l1, l2):
    """
    Precondition: len(l1) == len(l2)
    """
    return [pos_mod((a + b), 12) for a, b in zip(l1, l2)]



# Observation, the intervals only change by a small amount each time
changes = [
[-1, [0, 0, -1, -1]],
[-1, [0, 0, 1, 0]],
[7, [0, 1, 0, 1]],
[3, [0, 0, 0, -1]],
[-7, [0, 0, 0, 2]],
[0, [0, -1, -1, -1]],
[6, [0, 1, 1, 0]],
[-7, [0, -1, 0, 0]],
[-2, [0, 0, 0, -1]],
[4, [0, -1, 0, +1]],
[0, [0, -1, -1, 0]],
[5, [0, 1, 1, 0]],
[-7, [0, -1, 0, 0]]
]

rhythm = [ 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 2, 4 ]


chords = []
for i in range(len(rhythm)):
  if i == 0:
    intervals = [0, 3, 7, 10]
    int_not = 2
    duration = rhythm[0]
  else:
    # Uses -1, because this block only get's run after first iteration
    prev_intervals = chords[-1][1]

    current_change = changes[(i-1)%len(changes)]
    chord_change = current_change[1]
    root_change = current_change[0]

    duration = rhythm[i]

    intervals = elementwise_sum(chord_change, prev_intervals)
    int_not = pos_mod((int_not + root_change), 12)


  chords.append(((3, int_not), intervals.copy(), duration))
  # chords.append( (  (3, int_not), intervals.copy(), 2 + 2*(i%2) ))


beats_chords_length = sum([x[2] for x in chords])

d = Drummer(8)
d.create_jazz_groove(beats_chords_length)

#create_midi_song("how_insensitive.mid", 110,parse_note_song_into_objects(parse_song_into_notes(chords)),d.beat)
create_midi_song("how_insensitive.mid", 110,parse_note_song_into_objects(parse_song_into_notes(chords)))
