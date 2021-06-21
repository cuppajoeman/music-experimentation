import numpy as np
import re
from fractions import Fraction
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

plt.rcParams["figure.figsize"] = (20,5)

# single beat (4 beats in a measure
b = 1
# half
h = 1/2
# thirds
t = Fraction(b, 3)
# two thirds
tt = 2 * t

song = [
    ("0' 4' 7' 11' R", [tt, t, tt, t+b, b]), ("R 7' 4' 7' 7'", [tt, t, tt, t + b, b]),
    ("9' 6' R", [b + tt, t + b, b]), ("6' 2' 9' 6' 0'' 9' R",[tt, t, tt, t, tt, t, b]),

    ("5' 2' 9' 0'' 5'", [tt, t, tt, t + b, b]),
    ("2' 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b]),
    ("4' 4' 4' 0'",  [b, tt, t + b, b]),
    ("11 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b]),

    ("4' 0' R 4' R 4' R 4'",[tt, t, tt, t, tt, t, tt, t]), ("7' 4' 7' 7' R 11'", [tt, t, tt, t, 1 + tt, t]),
    ("0'' 0'' 9' R 9' 6'", [b, tt, t, tt, t, b]), ( "R 2' 2' 2' R",[ b, b, tt, t, b]),

    ("0'' 0'' 9' R 9' 5'", [b, tt, t, tt, t, b]),
    ("R 2' 11 5' 2' 11 7", [b, tt, t, tt, t, tt, t]),
    ("4' 0' R 4' 0' R", [tt, t, tt, t, b, b]),
    ("7' 4' 7' 10' R", [tt, t, tt, t + b, b]),
    
    ("R 9 0' 9 0' 9",[b, b, tt, t, tt, t]), ("5 9 0' 4' R",[tt, t, tt, t + b, b]), ( "R 0' 4' 0' R",[b, b, tt, t, b]), ("9 0' 5 R", [b, tt, t + b, b]),

    ("2' R 0'' 6' 9' 6'",[b, b, tt, t, tt, t]), ( "0'' 0'' 9' R",[b, tt, t + b, b]),
    ("9' R 9' 2' 5' 2'", [b, b, tt, t, tt, t]),
    ("11 11 2' R", [b, tt, t + b, b]),
    
    ("4' 0' 7' 0' R 4' 7' 11'", [tt, t, tt, t, tt, t, tt, t+b]),("7' 11' R", [tt, t + b, b]),
    ("6' 2' 9' 2' R 9'", [tt, t, tt, t, b, b]),("0'' 6' R 9' R",[tt, t, tt, t + b, b]),

    ("9' 2' R 5' 2'", [tt, t, tt, t + b, b]),
    ("5' 11 R 2' 5'", [tt, t, tt, t + b, b]),
    ("4' 0' 7' 4' 7' 11'", [tt, t, tt, t, tt, t + b]),
    ("R", [4 * b]),
]

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

  m = re.search(r"[,']", notation)

  if m:
     direction = notation[m.start()]
     count = len(notation[m.start():])
     multiplier = -1 if direction == ',' else 1

     return digit + multiplier * count * 12
  else:
    return digit

def pos_mod(x,m):
  while x < 0:
    x += m
  return x % m

duration = 0
song_points = []
rhythm_lines = []
for measure in song:
    notes, rhythms = measure
    notes = get_intervals(notes)
    note_to_rhythm = zip(notes, rhythms)
    for n, r in note_to_rhythm:
        if n is not None:
            song_points.append((duration, n))
            rhythm_lines.append(r)
        duration += r

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
for i in range(len(x)):
    x_pos = x[i]
    y_pos = y[i]
    rhythm_line = rhythm_lines[i]
    plt.plot([x_pos, x_pos+rhythm_line],[y_pos, y_pos], 'r-|')

k = 0 


# give it a key shift 
k_y = []
for p in y:
    k_y.append(pos_mod(p, 12))

for i, txt in enumerate(k_y):
    x_pos = x[i]
    y_pos = y[i]
    if y != None:
        plt.annotate(txt, (x_pos, y_pos))

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

for i in range(8):
    start = i * 16
    end = start + 16
    ax.axis([start, end, min(y)-1, max(y)+1])
    fig.canvas.draw_idle()
    plt.savefig(str(i) + 'analysis.png',pad_inches=0)

#plt.show()
