from create_song import *
import pprint
from math import ceil
from musical_intelligence import *



chords = []
for i in range(48):
  oct_band, int_not = divmod(2 + 5*i, 12)
  if i == 0:
    intervals = [0,3,7,10]
  else:
    prev_intervals = chords[-1][1]

    # [0, +1, 0, 0]
    # [0, 0, +1, 0]
    # ...
    idx = 1 + 2*((i+1)%2)
    intervals[idx] = (intervals[idx] + 1) % 12

  #chords.append( (  (4+oct_band, int_not), intervals.copy(), 4) )
  chords.append( (  (3, int_not), intervals.copy(), 2 + 2*(i%2) ))

beats_chords_length = sum([x[2] for x in chords])

d = Drummer(8)
d.create_jazz_groove(beats_chords_length)

create_midi_song("251-extension.mid", 120,parse_note_song_into_objects(parse_song_into_notes(chords)),d.beat)
