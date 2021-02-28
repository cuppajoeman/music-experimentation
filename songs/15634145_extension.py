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

changes = [
   [0, 0, 0, -1],
   [0, -1, 0, 0],
   [0, 0, 0, 0 ],
   [0, -1, 0, 1],
   [0, 0, 0, 0 ],
   [0, 0, 0, 0 ],
   [0, 0, 0, -1]
]

root_changes = [7, 2, -5, 1, -5, 5, 2]

chords = []
for i in range(64):
  if i == 0:
    intervals = [0,4,7,11]
    int_not = 0
  else:
    # Uses -1, because this block only get's run after first iteration
    prev_intervals = chords[-1][1]
    intervals = elementwise_sum(changes[(i-1)%len(changes)], prev_intervals)
    int_not = (int_not + root_changes[(i-1)%len(root_changes)]) % 12


  chords.append(((3, int_not), intervals.copy(), 2 + 2* (i % 2)))
  # chords.append( (  (3, int_not), intervals.copy(), 2 + 2*(i%2) ))

beats_chords_length = sum([x[2] for x in chords])

d = Drummer(8)
d.create_jazz_groove(beats_chords_length)

create_midi_song("15634145_extension.mid", 120,parse_note_song_into_objects(parse_song_into_notes(chords)),d.beat)
