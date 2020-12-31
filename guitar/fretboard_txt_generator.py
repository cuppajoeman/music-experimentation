import os,sys
# Hack in parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from chord_generation import *
def mark_fretboard_no_gui(to_be_marked, fb):
    for info in to_be_marked:
        str_num, fret_pos, symbol = info
        fb[str_num][fret_pos] = symbol

