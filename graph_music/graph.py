

import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print(user_paths)



import numpy as np
import re
import matplotlib.pyplot as plt
from numuse.converters import *
from fractions import Fraction


b = 1
# half
h = 1 / 2
# thirds
t = Fraction(b, 3)
# two thirds
tt = 2 * t

jens_solo_arps = [
    [("0' 4' 7' 11' R", [tt, t, tt, t + b, b])],
    [("R 7' 4' 7' 7'", [tt, t, tt, t + b, b])],
    [("9' 6' R", [b + tt, t + b, b])],
    [("6' 2' 9' 6' 0'' 9' R", [tt, t, tt, t, tt, t, b])],
    [("5' 2' 9' 0'' 5'", [tt, t, tt, t + b, b])],
    [("2' 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
    [("4' 4' 4' 0'", [b, tt, t + b, b])],
    [("11 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
    [("4' 0' R 4' R 4' R 4'", [tt, t, tt, t, tt, t, tt, t])],
    [("7' 4' 7' 7' R 11'", [tt, t, tt, t, 1 + tt, t])],
    [("0'' 0'' 9' R 9' 6'", [b, tt, t, tt, t, b])],
    [("R 2' 2' 2' R", [b, b, tt, t, b])],
    [("0'' 0'' 9' R 9' 5'", [b, tt, t, tt, t, b])],
    [("R 2' 11 5' 2' 11 7", [b, tt, t, tt, t, tt, t])],
    [("4' 0' R 4' 0' R", [tt, t, tt, t, b, b])],
    [("7' 4' 7' 10' R", [tt, t, tt, t + b, b])],
    [("R 9 0' 9 0' 9", [b, b, tt, t, tt, t])],
    [("5 9 0' 4' R", [tt, t, tt, t + b, b])],
    [("R 0' 4' 0' R", [b, b, tt, t, b])],
    [("9 0' 5 R", [b, tt, t + b, b])],
    [("2' R 0'' 6' 9' 6'", [b, b, tt, t, tt, t])],
    [("0'' 0'' 9' R", [b, tt, t + b, b])],
    [("9' R 9' 2' 5' 2'", [b, b, tt, t, tt, t])],
    [("11 11 2' R", [b, tt, t + b, b])],
    [("4' 0' 7' 0' R 4' 7' 11'", [tt, t, tt, t, tt, t, tt, t + b])],
    [("7' 11' R", [tt, t + b, b])],
    [("6' 2' 9' 2' R 9'", [tt, t, tt, t, b, b])],
    [("0'' 6' R 9' R", [tt, t, tt, t + b, b])],
    [("9' 2' R 5' 2'", [tt, t, tt, t + b, b])],
    [("5' 11 R 2' 5'", [tt, t, tt, t + b, b])],
    [("4' 0' 7' 4' 7' 11'", [tt, t, tt, t, tt, t + b])],
    [("R", [4 * b])],
]

m = parse_music(jens_solo_arps)

plt.rcParams["figure.figsize"] = (20,5)



def get_intervals(x):
  intervals = []
  for notation in x.split():
    result = parse_notation(notation)
    intervals.append(result)
  return intervals


def parse_notation(notation):
  # It will always have a digit
  d = re.search(r"[0-9R]+", notation)
  found = notation[d.start():d.end()]
  if found == "R":
      digit = None
  else:
      digit = int(found)

  m = re.search(r"[,'ud]", notation)

  if m:
     direction = notation[m.start()]
     count = len(notation[m.start():])
     multiplier = -1 if direction in ['d',','] else 1

     return digit + multiplier * count * 12
  else:
    return digit

def pos_mod(x,m):
  while x < 0:
    x += m
  return x % m

#duration = 0
#song_points = []
#rhythm_lines = []
#for measure in song:
#    notes, rhythms = measure
#    notes = get_intervals(notes)
#    note_to_rhythm = zip(notes, rhythms)
#    for n, r in note_to_rhythm:
#        if n is not None:
#            song_points.append((duration, n))
#            rhythm_lines.append(r)
#        duration += r

song_points = []
rhythm_lines = []
for measure in m.measures:
    for line in measure.m_lines:
        for moment in line.m_moments:
            # for this specific case
            if list(moment.notes.notes) != []:
                song_points.append((moment.time, list(moment.notes.notes)[0]))
                rhythm_lines.append(moment.duration)

x,y = zip(*song_points)


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

plt.plot(x, y, 'xb-')
#plt.title("Musical Analysis")
plt.xlabel("time")
plt.ylabel("notes")

plt.grid(True)
plt.xticks(np.arange(float(min(x)), float(max(x)+1), 1.0))
plt.yticks(np.arange(float(min(y)-1), float(max(y)+1), 1.0))


# Add rhythm markers

k = 0 
for i in range(len(x)):
    x_pos = x[i]
    y_pos = y[i]
    rhythm_line = rhythm_lines[i]
    plt.plot([x_pos, x_pos+rhythm_line],[y_pos, y_pos], 'r-|')

    # assuming plot of more than 2 notes
    if i == 0:
        #about to figure out the direction of it 
        y_next = y[i+1]
        if y_next > y_pos:
            # put text 
            annotate_pos = (x_pos, y_pos - .5)
        else:
            annotate_pos = (x_pos, y_pos + .5)
    elif i == len(x)-1:
        y_prev = y[i-1]
        if y_prev > y_pos:
            # put text 
            annotate_pos = (x_pos, y_pos - .5)
        else:
            annotate_pos = (x_pos, y_pos + .5)
    else:
        y_prev = y[i-1]
        y_next = y[i+1]
        between = y_prev <= y_pos <= y_next or y_prev >= y_pos >= y_next
        if between:
            # downhill
            if y_prev >= y_pos:
                annotate_pos = (x_pos, y_pos + .5)
            else:
                annotate_pos = (x_pos, y_pos + .5)
        elif y_pos <= y_prev:
            # v formation put text under
            annotate_pos = (x_pos, y_pos - 1.5)
        elif y_pos >= y_prev:
            # mountain top
            annotate_pos = (x_pos, y_pos + .5)

    txt = pos_mod(y_pos - k, 12)

    plt.annotate(txt, (x_pos, y_pos), annotate_pos)


plt.savefig("lets_go_numuse.png")


# give it a key shift 

#add slider 
#axcolor = 'lightgoldenrodyellow'
#axpos = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
#spos = Slider(axpos, 'Pos', float(min(x)-5), float(max(x)+5))


#def update(val):
#    pos = spos.val
#    ax.axis([pos,pos+10,min(y)-1, max(y)+1])
#    fig.canvas.draw_idle()
#
#
#spos.on_changed(update)

#for i in range(8):
#    start = i * 16
#    end = start + 16
#    ax.axis([start, end, min(y)-1, max(y)+1])
#    fig.canvas.draw_idle()
#    plt.savefig(str(i) + 'analysis.png',pad_inches=0)

#pos = 0
#i=0
#for example in all_examples:
#   start = pos
#   end = start + 4 * len(example)
#   all_notes = ' '.join([tup[0] for tup in example if tup])
#   intervals = [x for x in get_intervals(all_notes) if x is not None]
#   print(all_notes, intervals, sep="|")
#   ax.axis([start, end, min(intervals)-1, max(intervals)+1])
#   fig.canvas.draw_idle()
#   plt.savefig(str(i) + 'example.png',pad_inches=0)
#   pos = end
#   i+=1


#plt.show()
