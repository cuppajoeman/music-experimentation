import os,sys
from fretboard_position_generator import *

def mark_fretboard_no_gui(to_be_marked, fb):
    for info in to_be_marked:
        str_num, fret_pos, symbol = info
        fb[str_num][fret_pos] = symbol

